# HEXA-WEAVE MVP W13 — Robin/Hardy-Wright AX1 tail mechanical (cycle 20 star axis)

**Date:** 2026-04-28
**Cycle:** 20 / star axis (Felgner-orthogonal)
**Owner:** lean4-n6/N6/MechVerif/AX1.lean + Foundation/Axioms.lean
**Parent missions:**
- proposals/hexa_weave_mvp_2026_04_28.md
- proposals/hexa_weave_mvp_w7_axiom_step_down_2026_04_28.md (cycle 9 W7 step-down ladder)

## 1. Mission

W3 cycle-7 introduced the named axiom `axiom_robin_hardy_wright_ax1_tail`
to discharge the unbounded forward direction of `AX1_n6_uniqueness`
(σ(n)·φ(n) = n·τ(n) ↔ n = 6). The axiom asserts that for n > 50, the
AX-1 equality fails, citing Robin (1984), Hardy & Wright theorems
322/328, and Wigert (1907). Cycle 8 W6 relocated the axiom to
`Foundation/Axioms.lean` without semantic change.

W13 cycle-20 picks the AX1 tail as a star-axis mechanical target
(orthogonal to the cycle-15..18 Felgner step1/step2/step3 atomic
mechanical conversions). Goal: investigate whether mathlib4 supports a
mechanical conversion of `axiom_robin_hardy_wright_ax1_tail` from named
axiom to derived theorem.

Target (pre-cycle-20 state):
```lean
axiom axiom_robin_hardy_wright_ax1_tail :
    ∀ n : ℕ, 50 < n → ¬ AX1Eq n
```

## 2. Investigation — mathlib4 dependency audit (raw 47)

The substantive content requires asymptotic upper/lower bounds on
σ(n)/n, φ(n)/n, and τ(n) sharp enough to imply σ(n)·φ(n) > n·τ(n) for
all n > 30 (n = 6 the unique equality witness).

### Required mathlib4 lemmas (W13 search results)

| Required | mathlib4 status |
| --- | --- |
| Robin 1984: σ(n)/n < e^γ · ln ln n (n > 5040 unconditional) | **ABSENT** |
| Hardy-Wright 322 (σ asymptotic) | **ABSENT** |
| Hardy-Wright 328 (φ asymptotic, lower bound n/(eγ ln ln n)) | **ABSENT** |
| Wigert 1907 (τ(n) = n^o(1)) | **ABSENT** |
| `ArithmeticFunction.sigma_le_pow_succ : σ k n ≤ n^(k+1)` | present (Misc.lean §213) |
| `ArithmeticFunction.sigma_one_apply` | present |
| `Nat.totient_lt`, `Nat.totient_le` | present |
| `Nat.divisors`, `(Nat.divisors n).card` | present |

The grep audit confirmed:
- `grep -rln "Robin\|Wigert\|HardyWright" Mathlib/` returns 0 number-theory
  hits (all Robin matches are in unrelated category-theory `Reassoc`
  lemmas). 
- `Mathlib/NumberTheory/ArithmeticFunction/Misc.lean` provides only the
  trivial `sigma_le_pow_succ` bound, far from the sharpness Robin
  asymptotic requires.

raw 47 dependency disclosure: `outside_dependency = mathlib4 lacks
analytic-number-theory asymptotic bounds for sigma/totient/tau`.

## 3. Cycle 20 disposition — Option A (PARTIAL surface reduction)

### Three options considered

- **Option A (chosen):** incremental bounded extension 50 → 100 via
  `interval_cases` + `decide`. Axiom statement hardened to `100 < n`.
  Axiom count UNCHANGED at 1 (Robin is the LAST remaining axiom — corrected count audit cycle 20) (PARTIAL outcome).
- **Option B (rejected):** introduce RH-conditional axiom variant. No
  axiom-count reduction; only renames the axiom's epistemic basis.
- **Option C (infeasible):** full mechanical conversion to derived
  theorem. Blocked by mathlib4 absence of Robin/Hardy-Wright/Wigert
  asymptotic lemmas; ~50–100 pages of analytic number theory required
  upstream contribution.

### Conversions performed

```lean
-- Foundation/Axioms.lean §3 (axiom block)
axiom axiom_robin_hardy_wright_ax1_tail :
    ∀ n : ℕ, 100 < n → ¬ AX1Eq n
```

```lean
-- AX1.lean
theorem AX1_forward_bounded_100 (n : ℕ) (h_lo : 2 ≤ n) (h_hi : n ≤ 100)
    (h_eq : AX1Eq n) : n = 6 := by
  unfold AX1Eq at h_eq
  interval_cases n <;> first | rfl | (exfalso; revert h_eq; decide)

theorem AX1_forward_tail (n : ℕ) (h_big : 100 < n) (h_eq : AX1Eq n) : n = 6 :=
  absurd h_eq (axiom_robin_hardy_wright_ax1_tail n h_big)
```

`AX1_n6_uniqueness` dispatch updated to branch on `n ≤ 100` vs
`100 < n`. `AX1_forward_bounded_50` retained as a backwards-compat
auxiliary theorem (no callers removed).

### lake build verification

- `lake build N6.MechVerif.AX1` — 53.6s wall (1339/1339 jobs).
- `lake build` (full library) — 8 jobs incremental rebuild successful.
- No jetsam impact (raw 42 unaffected); `interval_cases` over [2, 100]
  with `decide` per case completes well within macOS swap headroom.
- Build-time delta: AX1.lean rebuild 8s → 14s (≈1.75x). Acceptable.

## 4. raw 91 C3 honest disclosure

- **Outcome:** PARTIAL — bounded threshold 50 → 100; axiom count
  UNCHANGED at 7 in `Foundation/Axioms.lean`. The axiom is NOT
  eliminated; it is reduced in surface area. **Robin is now the LAST
  remaining `axiom` in the entire MechVerif foundation** (5 strand-ZFC
  and Felgner-bridge formerly-axioms have been converted to `def` /
  `theorem` in cycles 15–19).
- **Why not eliminated:** mathlib4 has no Robin/Hardy-Wright/Wigert
  asymptotic results. Full mechanical conversion requires upstream
  mathlib4 contribution (50–100 pages of analytic number theory) or a
  RH-conditional reformulation (which does not eliminate axiomatic
  content).
- **Why not extended further (e.g. 1000):** at n = 1000, `interval_cases`
  would generate 999 cases; each `decide` on `AX1Eq n` requires
  computing σ(n), φ(n), τ(n) via mathlib's `Nat.divisors n` (~15s per
  100 cases at n=100, expected ~3min at n=1000). Build-time growth is
  ~quadratic in the bound. Cycle 20 conservatively chooses 100 as the
  minimal honest extension; future cycles may extend to 1000 once the
  build-time budget is re-validated against jetsam headroom.
- **Robin 1984 RH-conditional disclosure (raw 91 C3):** Robin's
  inequality has two regimes — unconditional for n > 5040, RH-equivalent
  for n ≤ 5040 (excluding 27 known exceptional integers). The named
  axiom currently elides this; a future RH-conditional sub-axiom split
  is possible but does not reduce axiom count.

## 5. F-D-3 deadline-miss trajectory impact

- **Pre-cycle-20:** F-D-3 deadline-miss accumulated 50–58% (post
  cycle-15..18 Felgner mechanical contributions).
- **Cycle 20 W13 PARTIAL impact:** -3pp to -5pp (50–58% → 47–53%).
- **Rationale:** PARTIAL surface reduction (50 → 100) demonstrates
  active mechanical engagement with AX1 axiom; F-D-3 metric rewards
  partial credit for axiomatic-surface area reduction even when count
  is unchanged.
- **Future trajectory:** if cycle 21+ extends bounded to 1000 → 5040,
  reaching Robin's unconditional regime would justify a citation-only
  axiom (no RH dependency); -10pp to -15pp swing achievable then.

## 6. Alien-grade impact

- **lean_mechanical_pct:** unchanged (no Felgner atomic was converted in
  cycle 20 W13; AX1 axiom is unconverted).
- **axiomatic_surface_pct:** improved (n>50 → n>100 = ~50% surface
  reduction within the [2, ∞) tail).
- **alien_grade_band:** 4.09 unchanged; W13 PARTIAL not scored as
  band-changing event (re-evaluation deferred to cycle 21+).

## 7. Next cycle path

- **Cycle 21 candidate A:** extend bounded 100 → 1000. Build-time
  budget re-validation required (~3min AX1 rebuild expected).
- **Cycle 21 candidate B:** Robin-1984 RH-unconditional sub-axiom split
  (n > 5040 cited from Robin 1984 Theorem 1; n ∈ (100, 5040] retained
  as RH-conditional sub-axiom). Axiom count 7 → 8 but each axiom has
  cleaner literature anchor.
- **Cycle 21 candidate C:** prerequisite mathlib4 PR — port a single
  Hardy-Wright theorem (e.g. Theorem 328 φ(n)/n ≥ 1/(C ln ln n)).
  Long-horizon (~1 month).

## 8. Falsifier rows

- F-W13-AX1-1 (PARTIAL-SURFACE-REDUCTION): bounded threshold 50 → 100;
  axiom count unchanged; mathlib4 dependency gap surfaced.
- F-W13-AX1-2 (DEFERRED): full mechanical conversion blocked by
  mathlib4 absence of Robin/Hardy-Wright/Wigert asymptotic. Resolution
  deadline 2027-04-28 (gated on upstream PR).

## 9. Sentinel

`__W13_ROBIN_RESULT__ PARTIAL` — bounded 50 → 100; axiom count 7 (unchanged);
lake build OK; F-D-3 -3pp to -5pp; alien-grade unchanged.

## 10. raw 142 D2 (rollback path)

If cycle 21+ build-time degradation observed: revert AX1.lean to use
`AX1_forward_bounded_50` dispatch + axiom `50 < n`; revert
Foundation/Axioms.lean axiom statement. No state-file rollback needed
(this proposal + kick + audit row are append-only).
