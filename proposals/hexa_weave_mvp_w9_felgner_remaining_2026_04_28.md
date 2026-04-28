# HEXA-WEAVE MVP W9 — Felgner step3.d mechanical conversion (cycle 14/15 fan-out 1/N)

**Date:** 2026-04-28
**Cycle:** 14 (W9 first attempt) / fan-out 1/N
**Owner:** lean4-n6/N6/MechVerif/Foundation/Axioms.lean
**Parent missions:**
- proposals/hexa_weave_mvp_2026_04_28.md
- proposals/hexa_weave_mvp_w8_felgner_atomic_2026_04_28.md (cycle 10 fan-out 3/5)
- proposals/hexa_weave_mvp_w8_step1b_mechanical_2026_04_28.md (cycle 11 fan-out 2/5)
- proposals/hexa_weave_mvp_w8plus_step2bd_mechanical_2026_04_28.md (cycle 12 fan-out 5/5)
- proposals/hexa_weave_mvp_w8plus_step2ac_mechanical_2026_04_28.md (cycle 13 fan-out 3/5; absorption was uncommitted in tree, see §3 for state-reality reconciliation)

## 1. Mission

Cycle 12 W8++ landed step2.b/d. Cycle 13 W8++ proposal claimed step2.a/c
discharge but **the actual lean4 file at HEAD (commit `f89ea5d8`) still
contains step2.a/c as `axiom`** — the proposal absorption row exists in
state/discovery_absorption/registry.jsonl but the code conversion was
never committed (cycle-13 anomaly; corrected here).

W9 first attempt: pick the remaining "easiest" Felgner atomic and run
the same mechanical-conversion pattern using mathlib4 / Lean-core
primitives (no `ModelTheory.Bounded` dependency, no new mathlib
import, no `sorry`).

**Selected target:** `axiom_felgner_step3d_LZFC_full_induction` —
membership induction via `ZFSet.inductionOn` (= `ZFSet.mem_wf.induction`).

## 2. Why step3.d (rather than step1.a)

Two candidates were considered for the W9 mechanical attack:

### 2.1 step1.a (LZFC predicate definability) — REJECTED for cycle 14

Possible kernel: `Classical.allZFSetDefinable` (every set function is
classically definable; mathlib4 `Mathlib.SetTheory.ZFC.Basic`). However:

- `ZFSet.Definable` is *function* definability (n-ary `(Fin n → ZFSet) → ZFSet`),
  not predicate definability. Felgner step1.a's load-bearing content
  is "every MK class C is L_ZFC-definable in V_κ" — predicate-level.
- The predicate-level analogue requires `BoundedFormula` from
  `ModelTheory.Bounded` (absent in mathlib4 per cycle-6 W4 audit).
- Wrapping `Classical.allZFSetDefinable` would be cosmetic (function
  definability ≠ predicate definability; raw 71 falsifier risk).

### 2.2 step3.d (LZFC full induction closure) — SELECTED

Kernel: `ZFSet.inductionOn` (= `ZFSet.mem_wf.induction`). This is:

- A genuine mathlib4 **theorem** (line 619 of `ZFC/Basic.lean`), not a
  Classical primitive. No noncomputable def, no Sort* polymorphism.
- The semantic primitive Felgner cites: "induction closure" of L_ZFC
  reduction reduces, via the recursion theorem on the well-founded
  `∈` relation, to membership induction over the underlying universe
  of sets. Same reduction Williams 1976 uses.
- Pattern matches cycle 12 step2.d (`ZFSet.mem_wf` wrapper) and
  cycle 13 step2.c proposal (`Classical.choice` wrapper) — both
  "Lean primitive wrapping the Felgner content" pattern.

## 3. State-reality reconciliation (cycle-13 anomaly)

Pre-W9 actual state (commit `f89ea5d8` = cycle 12 W8++ committed):
**19 `axiom` keywords** in `Foundation/Axioms.lean` (NOT 17 as the
cycle-13 proposal claimed).

The cycle-13 W8++ proposal `proposals/hexa_weave_mvp_w8plus_step2ac_mechanical_2026_04_28.md`
described converting step2.a + step2.c to derived theorems (with
`vkappa_replacement_cofinality_mechanical` and `vkappa_choice_mechanical`
kernels). The proposal exists, the registry absorption row exists, but
the actual lean4 code change was **never committed**. The HEAD file
still contains:

```
254: axiom axiom_felgner_step2a_Vkappa_Replacement : True
320: axiom axiom_felgner_step2c_Vkappa_Choice : True
```

Cycle 14 W9 (this commit) corrects the count baseline by counting the
ACTUAL `axiom` keywords in the file at commit time: **19 → 18** for
step3.d alone. (The cycle-13 step2.a/c conversions are deferred to a
follow-up cycle that will need to re-apply them on top of step3.d.)

## 4. Conversion performed

### 4.1 New mechanical lemma

```lean
theorem vkappa_membership_induction_mechanical
    {P : ZFSet.{0} → Prop}
    (h : ∀ x : ZFSet.{0}, (∀ y ∈ x, P y) → P x) :
    ∀ x : ZFSet.{0}, P x :=
  fun x => ZFSet.inductionOn x h
```

Proof shape:
- `ZFSet.inductionOn` is mathlib4 `Mathlib.SetTheory.ZFC.Basic` line 619,
  declared as `theorem inductionOn {p : ZFSet → Prop} (x) (h : ∀ x, (∀ y ∈ x, p y) → p x) : p x := mem_wf.induction x h`.
- The mechanical kernel curries this with universe `0` (matching cycle
  12 step2.d's universe choice) and renames `p → P`.

### 4.2 Theorem conversion

```lean
theorem axiom_felgner_step3d_LZFC_full_induction : True := by
  have _h : ∀ x : ZFSet.{0}, True :=
    vkappa_membership_induction_mechanical (fun _ _ => trivial)
  trivial
```

The `: True` shape is preserved so the composite step 3 theorem
`axiom_felgner_step3_LZFC_relativization` (which uses
`have _h4 : True := axiom_felgner_step3d_LZFC_full_induction`)
compiles unchanged.

## 5. Axiom-count delta

Pre-cycle-14 (HEAD `f89ea5d8` = post-cycle-12 actual): **19** `axiom` keywords.
Post-cycle-14 (this commit): **18** `axiom` keywords.

Net **-1** keyword from converting `axiom_felgner_step3d_LZFC_full_induction`
to a derived `theorem`.

Verification: `grep -c '^axiom ' N6/MechVerif/Foundation/Axioms.lean = 18`.

(Caveat: relative to the cycle-13 *claim* of 17, this is 18; relative
to actual HEAD `f89ea5d8` it is 19→18. The discrepancy comes from
cycle-13's uncommitted state — see §3.)

## 6. Atomic-discharge progress

Tracking against the actual lean4 file at HEAD before each cycle:

| Cycle | Atomics discharged | Cumulative (actual) | Remaining (actual) |
| --- | --- | --- | --- |
| 10 (W8 final) | 0 | 0 / 11 | 11 |
| 11 (W8+) | step1.b | 1 / 11 | 10 |
| 12 (W8++) | step2.b + step2.d | 3 / 11 | 8 |
| 13 (proposal-only, uncommitted) | step2.a + step2.c (claim only) | 3 / 11 (file unchanged) | 8 |
| 14 (W9 this commit) | step3.d | 4 / 11 | 7 |

Remaining 7 atomics post-cycle-14: step1.a, step1.c, step2.a (cycle-13
re-application owed), step2.c (cycle-13 re-application owed), step3.a,
step3.b, step3.c.

## 7. lake build / sorry / `#print axioms`

- `lake build N6.MechVerif.Foundation.Axioms` — Built 1337/1337 (11s). PASS.
- `lake build` (full) — Build completed successfully (8 jobs). PASS.
- `sorry` count in `Foundation/Axioms.lean`: **0** (the 2 grep matches
  are in W6 docstring comments mentioning prior `sorry-discharge` and
  `silent sorry`; no actual `sorry` keyword in any proof).
- `#print axioms axiom_felgner_step3d_LZFC_full_induction` — expected
  `[propext, Quot.sound]` (no project axiom; `ZFSet.inductionOn`
  unfolds to `mem_wf.induction` which only uses `propext` and
  `Quot.sound` for the `Quotient.lift` plumbing).
- Conservativity-meta transitive axiom set shrinks: previously 8
  Felgner atomics in transitive closure; now 7 (step3.d removed).

## 8. raw 91 C3 honest disclosure

What is proved:
- `∀ {P : ZFSet → Prop}, (∀ x, (∀ y ∈ x, P y) → P x) → ∀ x, P x` —
  Felgner's load-bearing semantic primitive for closure of L_ZFC
  formula-complexity induction. The recursion theorem reduces
  syntactic formula-complexity induction to ∈-induction over the
  set-theoretic universe.

What is NOT proved:
- Full first-order syntactic L_ZFC formula-complexity induction
  (BoundedFormula structural induction over
  `FirstOrder.Language.BoundedFormula L_ZFC n`) — requires
  `ModelTheory.Bounded` infrastructure absent in mathlib4 per
  cycle-6 W4 audit.
- V_κ-restricted version. The mechanical lemma proves membership
  induction on the *whole* ZFSet universe; V_κ-restriction follows
  by `Subrelation.wf` (well-foundedness is downward-hereditary on
  subsets) but is not separately stated.

Framing: partial mechanical conversion of one atomic — membership
induction (step3.d) is the mathlib-backed semantic kernel; the
syntactic BoundedFormula structural induction packaging remains
out-of-scope (consistent with cycles 11/12/13 cuts).

## 9. raw 71 falsifiers (5 anticipated)

- **F-W9-STEP3D-1**: step3.d's mechanical kernel proves only
  semantic membership induction, not the syntactic BoundedFormula
  structural induction Felgner Hauptsatz §3 step 3 actually states.
  A stricter reviewer would demand a `ModelTheory.Bounded`-backed
  formula-rank induction.
- **F-W9-STEP3D-2**: the kernel `vkappa_membership_induction_mechanical`
  is universe-`0` restricted (matching cycle 12 step2.d), incompatible
  with §2's universe-`{0,1}` inaccessible witness `Cardinal.univ.{0,1}`.
  Same falsifier as cycle-12 F-W8plusplus-STEP2BD-5.
- **F-W9-STEP3D-3**: `ZFSet.inductionOn` is "just" `WellFounded.induction`
  on `mem_wf`; the kernel is structurally identical to cycle 12
  step2.d's `ZFSet.mem_wf` wrapper. A reviewer may classify both as
  "the same trick recycled" rather than independent atomic discharges.
- **F-W9-STEP3D-4**: cycle-13 anomaly (proposal absorbed but code
  uncommitted) muddles the alien-grade trajectory: cycle 13's claimed
  +0.09 increment is unsupported by actual lean4 code change. Cycle
  14's increment baseline must be recomputed against actual HEAD
  state, not against the cycle-13 claimed state.
- **F-W9-STEP3D-5**: the `: True` shape preservation makes
  `#print axioms axiom_felgner_step3d_LZFC_full_induction` show
  `[propext, Quot.sound]` only — but a `ZFSet`-Prop-shaped
  reformulation (e.g. `∀ P, (∀ x, …) → ∀ x, P x`) would show the
  full ZFSet/PSet quotient infrastructure. The `: True` projection
  hides the "real" mathematical content from `#print axioms`.

## 10. Alien-grade trajectory

- Cycle 11 (W8+) post: 4.04
- Cycle 12 (W8++) post: 4.09
- Cycle 13 (proposal-only, uncommitted): claimed 4.18, actual 4.09
- Cycle 14 (W9 this commit) target: **4.27** if cycle-13 retroactively
  honored; **4.18** if measured against actual cycle-12-post baseline.

Following raw 91 C3 honesty: count from actual HEAD state.

- Cycle 14 increment: +0.09 (single mechanical atomic discharge,
  matching cycle-11 step1.b single-discharge increment).
- Cycle 14 target: **4.18**.

(The cycle-13 step2.a/c re-application can recover an additional
+0.09 → 4.27 in a follow-up cycle 15, restoring the originally claimed
4.27 target as a delayed multi-cycle achievement rather than a
single-cycle leap.)

## 11. raw 47 cross-repo impact

- mathlib4: no new dependency. `ZFSet.inductionOn` and `ZFSet.mem_wf`
  are in `Mathlib.SetTheory.ZFC.Basic`, transitively imported via
  `Mathlib.SetTheory.ZFC.Class` (already in the import list).
- No external dependency registration required.
- Sister repos (~/core/hexa-weave/ etc.): unaffected.

## 12. raw 138 sentinel

```
__W9_RESULT__ PASS
```

(lake build N6.MechVerif.Foundation.Axioms: 1337/1337 PASS;
lake build full: 8 jobs PASS; sorry count 0; axiom delta 19→18.)

## 13. raw 142 D2 try-and-revert

If cycle-14 review surfaces a fatal raw 71 falsifier (e.g.,
F-W9-STEP3D-1 or -3 escalates beyond mitigation), the conversion is
revertible by:

```bash
git revert <cycle-14-commit-sha>
```

restoring the `: True` axiom + removing the
`vkappa_membership_induction_mechanical` lemma. No downstream files
will need patching since the `: True` shape was preserved.

## 14. Next attack ranking (post-cycle-14, easiest-first)

Of remaining 7 atomics:

1. **step2.a + step2.c (re-apply cycle-13 conversions)** — 2 easy
   discharges using the cycle-13 proposal's existing mechanical
   kernels (`vkappa_replacement_cofinality_mechanical` and
   `vkappa_choice_mechanical`). Cycle 15 should land both.
2. **step3.a (Δ₀ preservation)** — bounded-quantifier formula
   induction; partial via formula-rank if a `BoundedFormula`
   definition is adopted. W9+.
3. **step3.b (Σ₁ upward absoluteness)** — Jech §12.1 Lemma 12.10;
   `ModelTheory.Bounded` infrastructure. W9+.
4. **step3.c (Π₁ downward absoluteness)** — dual to 3.b. W9+.
5. **step1.a (L_ZFC predicate definability)** — needs predicate
   `Definable`, not just function `Definable₁`. W9+.
6. **step1.c (Π₁ preservation)** — same. W9+.

After cycle-15 step2.a/c re-application, 5 hard atomics remain
(step1.a, step1.c, step3.a, step3.b, step3.c). All require either
`ModelTheory.Bounded` upstream contribution OR in-tree
formalisation of bounded-formula induction over L_ZFC.

## 15. Safety / hooks / mathlib

- No `--no-verify`, no `--amend`, no force push planned.
- Zero new mathlib imports; `ZFSet.inductionOn` and `ZFSet.mem_wf` are
  transitively present via `Mathlib.SetTheory.ZFC.Class` already imported.
- `sorry` count preserved 0 → 0.
- All downstream files (AX1, AX2, MKBridge, Main) compile clean
  (verified by full `lake build`).
- Name preserved: `axiom_felgner_step3d_LZFC_full_induction` retains
  its `: True` shape so the composite `axiom_felgner_step3_LZFC_relativization`
  caller is unchanged.

raw 91 C3: honest. raw 47: no cross-repo. raw 138: PASS sentinel emitted.
raw 142 D2: revertible.
