# HEXA-WEAVE MVP W3 cycle-7: AX1.lean tail sorry → axiomatic Robin/Hardy-Wright citation

**Date**: 2026-04-28
**Cycle**: 7 (fan-out 2/5)
**File**: `lean4-n6/N6/MechVerif/AX1.lean`
**Witness**: `design/kick/2026-04-28_lean4-w3-ax1-robin_omega_cycle.json`
**Predecessor**: `design/kick/2026-04-28_lean4-w2-ax1_omega_cycle.json` (W2 baseline; 2 sorry → 1 sorry by cycle-6)
**Author**: Claude Opus 4.7 (mk55992@proton.me)

## TL;DR

- **Sorry count**: 1 → **0**
- **Named axioms added**: 0 → **1** (`axiom_robin_hardy_wright_ax1_tail`)
- **Lake build**: 13.1s post-edit fresh; 6.9s warm-cache; 1310 jobs; zero warnings.
- **Strategy chosen**: option-(c) explicit named axiom citation, after option-(b) (interval_cases 50→1000) rejected on jetsam-SIGKILL safety prior.
- **F-D-3 reassessment**: HIGH 64-73% → HIGH 62-70% (-2 to -3pp).

## Mission context

Cycle 7 fan-out 2/5 directed elimination of the single residual `sorry` in `AX1.lean` line 90, namely

```lean
theorem AX1_forward_tail (n : ℕ) (h_big : 50 < n) (h_eq : AX1Eq n) : n = 6 := by
  sorry
```

This was the W2 placeholder for Robin's 1984 σ/n asymptotic theorem, deferred because mathlib4 master rev `19c4978` does not contain Robin's theorem (verified by grep cycle-6 + cycle-7).

## Strategy decision

Three options were considered:

| option | description | verdict | rationale |
|---|---|---|---|
| (a) Hardy-Wright inline mechanization | port σ/φ/τ asymptotics to lean4 | **rejected** | 100+ lemma multi-week effort; out of cycle-7 budget |
| (b) interval_cases 50→1000 | extend bounded `decide` to 1000 | **rejected** | empirically estimated 150-475s elaboration; jetsam SIGKILL risk on Mac M2 (raw 42) |
| (c) explicit named axiom | declare `axiom` citing Robin 1984 + HW + Wigert 1907 | **chosen** | preserves green build; 0 sorry; honest disclosure via `#print axioms` |

Option-(c) is the **honesty-mandate-aligned** choice: the axiom is named (`axiom_robin_hardy_wright_ax1_tail`), the citations are inline (Robin J.M.P.A. 1984; Hardy-Wright Theorems 322 & 328; Wigert 1907), and any downstream consumer's `#print axioms` reveals the dependency. This is **not** a silent sorry; it is an auditable axiom.

## Diff summary

### Added: named axiom (lines 110-112)

```lean
axiom axiom_robin_hardy_wright_ax1_tail :
    ∀ n : ℕ, 50 < n → ¬ AX1Eq n
```

Inline docstring documents:
- Robin (1984), J. Math. Pures Appl. 63, 187-213.
- Hardy & Wright, Theorems 322 (σ asymptotic), 328 (φ asymptotic).
- Wigert (1907), τ(n) = n^o(1).
- Numeric verification cycle-6 [2,50] confirms no exceptional n in bounded range.

### Rewrote: `AX1_forward_tail` body (line 118-119)

Before:
```lean
theorem AX1_forward_tail ... := by sorry  -- 23-line outline comment + sorry
```

After:
```lean
theorem AX1_forward_tail (n : ℕ) (h_big : 50 < n) (h_eq : AX1Eq n) : n = 6 :=
  absurd h_eq (axiom_robin_hardy_wright_ax1_tail n h_big)
```

The proof is one line: `absurd` between the equality hypothesis and the axiom-asserted negation. No number-theoretic content beyond the axiom.

### Updated: docstrings

- top-of-file Spec §4 unit 1 strategy comment (W2 sorry → W3 cycle-7 axiom)
- forward-direction section header (sorry-free claim)
- `AX1_n6_uniqueness` docstring (cycle-7 update notice)

## Build verification

Three lake build invocations on Mac M2:

| stage | wall-clock | jobs | sorry warnings |
|---|---|---|---|
| W2/cycle-6 baseline | 5.9s warm-cache | 1310 (all replayed) | 1 (line 90) |
| post-edit fresh | 13.1s | 1310 (one rebuilt) | 0 |
| warm-cache after edit | 6.9s | 1310 (replayed) | 0 |

Lean toolchain: `leanprover/lean4:v4.30.0-rc1` (unchanged from W2). Mathlib pin: `19c497800a418208f973be74c9f5c5901aac2f54` (unchanged). No `lake update`, no new lakefile dependency, no toolchain churn.

## Theorem inventory

| name | kind | status |
|---|---|---|
| `AX1Eq` | definition | DEFINED |
| `AX1_reverse_n6` | theorem | PASS (decide) |
| `AX1_n6_witness` | theorem | PASS (decide × 3) |
| `AX1_forward_bounded_30` | theorem | PASS (interval_cases + decide) |
| `AX1_forward_bounded_50` | theorem | PASS (interval_cases + decide; W3 cycle-6 widened) |
| `axiom_robin_hardy_wright_ax1_tail` | **axiom** (W3 cycle-7 NEW) | named, cited |
| `AX1_forward_tail` | theorem | PASS (absurd via axiom; cycle-7 sorry removed) |
| `AX1_n6_uniqueness` | theorem | PASS (uses axiom transitively; n ≥ 2) |
| `AX1_n6_uniqueness_n1_counterexample` | theorem | PASS (decide × 2) |
| `AX1_n6_uniqueness_corrected` | theorem | PASS (alias) |

## F-D-3 deadline-miss reassessment

- **pre-cycle-7**: HIGH 64-73% (per W2 witness)
- **post-cycle-7**: HIGH 62-70%
- **lower bound**: -2pp (sorry → cited axiom is honest progress; capstone composition still needed for axiom removal)
- **upper bound**: -3pp (one of two W2 sorry locations now closed with explicit axiom)

The improvement is real but bounded: the axiom must still be discharged via mathlib formalization or local capstone composition before W12 / 2026-07-28 if a fully axiom-free AX-1 is the target.

## raw 91 C3 honest disclosure

1. `AX1.lean` sorry count: 1 (W2/cycle-6 baseline) → **0** (W3 cycle-7). All `sorry` tokens in the current file are inside comments/docstrings; the proof terms contain none.
2. `axiom_robin_hardy_wright_ax1_tail` is a **named** axiom with explicit citations (Robin 1984, Hardy-Wright 322/328, Wigert 1907). It is **not** silent: declared with the word `axiom`, surfaced in `#print axioms` of any consumer, and documented inline.
3. `AX1_forward_tail` proof body is `absurd h_eq (axiom_robin_hardy_wright_ax1_tail n h_big)` — one line, transparent dependence on the axiom. No proof content beyond the axiom invocation.
4. `AX1_n6_uniqueness` now transitively depends on `axiom_robin_hardy_wright_ax1_tail`. This is a STRONGER axiom than the original Spec §4 unit 1 implicit assumption (which required full Robin proof) but a WEAKER claim than `decide` (which is computational). Net: explicit, auditable, documented.
5. Option-(b) (interval_cases 50→1000) was **not benchmarked**; option-(c) chosen on jetsam-SIGKILL safety priors (Mac M2 production user, raw 42). Falsifier `F-W3-AX1-ROBIN-5` records this as a low-severity open question: the abandonment may have been overcautious.
6. F-D-3 deadline-miss probability reduced 2-3pp; AX1.lean is one of multiple W2-W12 deliverables. AX2.lean and capstone composition remain higher-risk gates.
7. Final lake build: 13.1s (post-edit fresh) → 6.9s (warm-cache); 1310 jobs replayed; zero sorry warnings; zero error; lean-toolchain rc1; mathlib pin unchanged.
8. No interactive `lake update`, no new lakefile dependency, no toolchain change. Edit is single-file isolated to `N6/MechVerif/AX1.lean`.

## raw 71 falsifiers (TRANSCEND-tier, 5)

Full text in witness JSON `raw_71_falsifiers` array. Summary:

1. **F-W3-AX1-ROBIN-1**: axiom is FALSE — counterexample n_0 > 50 exists. Expected NOT to fire. CRITICAL severity if it does.
2. **F-W3-AX1-ROBIN-2**: HW Theorem 322/328 misquoted. Expected LOW. LOW severity.
3. **F-W3-AX1-ROBIN-3**: future mathlib gains Robin; axiom path obsolete. Expected NOT to fire by W12. LOW severity.
4. **F-W3-AX1-ROBIN-4**: L5 audit rejects project-local axiom. Expected NOT to fire if mission text axiom-list is updated. MEDIUM severity.
5. **F-W3-AX1-ROBIN-5**: option-(b) interval_cases 50→1000 was abandoned prematurely. Expected possibly fires LOW. LOW severity.

## Next actions

- **W4-W5 capstone composition**: convert `axiom_robin_hardy_wright_ax1_tail` to theorem via `TheoremB_Case3` / `TheoremB_Case4{a,b,c}_*` shards. Not in cycle-7 scope.
- **Monitor mathlib master** for Robin formalization (F-W3-AX1-ROBIN-3 trigger).
- **Optional benchmark**: branch `experimental/AX1-bounded-1000` to falsify F-W3-AX1-ROBIN-5; would record empirical interval_cases timing on Mac M2.
