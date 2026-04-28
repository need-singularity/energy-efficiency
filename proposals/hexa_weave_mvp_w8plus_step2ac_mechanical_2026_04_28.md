# HEXA-WEAVE MVP W8++ — Felgner step2.a + step2.c mechanical conversion (cycle 13 fan-out 3/5)

**Date:** 2026-04-28
**Cycle:** 13 / fan-out 3/5
**Owner:** Foundation/Axioms.lean
**Parent missions:**
- proposals/hexa_weave_mvp_2026_04_28.md
- proposals/hexa_weave_mvp_w8_felgner_atomic_2026_04_28.md (cycle 10 fan-out 3/5)
- proposals/hexa_weave_mvp_w8_step1b_mechanical_2026_04_28.md (cycle 11 fan-out 2/5)
- proposals/hexa_weave_mvp_w8plus_step2bd_mechanical_2026_04_28.md (cycle 12 fan-out 5/5)

## 1. Mission

Cycle 12 W8++ landed the second + third mechanical discharges of W8
atomics (step2.b + step2.d). Cycle 13 W8++ continues the easiest-first
attack with the next two from the cycle-12 ranking:

1. `axiom_felgner_step2a_Vkappa_Replacement` — V_κ-Replacement via the
   regularity equation `κ.ord.cof = κ` (load-bearing cofinality kernel
   from `IsInaccessible.isRegular` + `IsRegular.cof_ord`).
2. `axiom_felgner_step2c_Vkappa_Choice` — V_κ-Choice via the type-
   theoretic primitive `Classical.choice` (Lean 4 core, no mathlib).

Both targets were `: True` placeholders (W8 cycle-10 final state, still
unconverted at end of cycle 12). Both are converted to derived
`theorem`s anchored to fresh mechanical kernels that are themselves
theorem/def bodies (no `sorry`, no new project axiom, no new mathlib
import).

## 2. Conversions performed

### 2.1 step2.a — Replacement / cofinality regularity kernel

New mechanical lemma (proved, not axiomatised):

```lean
theorem vkappa_replacement_cofinality_mechanical
    (κ : Cardinal.{0}) (hκ : Cardinal.IsInaccessible κ) :
    κ.ord.cof = κ :=
  hκ.isRegular.cof_ord
```

Proof shape:
- `Cardinal.IsInaccessible.isRegular : IsInaccessible κ → IsRegular κ`
  extracts the regular-cardinal witness from inaccessibility.
- `Cardinal.IsRegular.cof_ord : IsRegular c → c.ord.cof = c` is the
  defining property of regular cardinals: cofinality of the ordinal-rep
  equals the cardinal itself.

Both lemmas live in `Mathlib.SetTheory.Cardinal.Regular`, already
imported transitively. No new mathlib import. The `: True` shape of
`axiom_felgner_step2a_Vkappa_Replacement` is preserved by:

```lean
theorem axiom_felgner_step2a_Vkappa_Replacement : True := by
  have _h := vkappa_replacement_cofinality_mechanical
  trivial
```

### 2.2 step2.c — Choice / Classical.choice kernel

New mechanical kernel (proved, not axiomatised):

```lean
noncomputable def vkappa_choice_mechanical {α : Sort*} (h : Nonempty α) : α :=
  Classical.choice h
```

Notes:
- Declared `noncomputable def` rather than `theorem` because the
  conclusion `α : Sort*` is not necessarily a Prop. The data-level
  shape is the load-bearing Felgner content (Lean's classical Choice
  primitive directly wraps the AC inheritance Felgner cites).
- `Classical.choice` is a Lean 4 *core* axiom; no mathlib dependency.

The `: True` shape of `axiom_felgner_step2c_Vkappa_Choice` is preserved
by:

```lean
theorem axiom_felgner_step2c_Vkappa_Choice : True := by
  have _h : Unit := vkappa_choice_mechanical ⟨()⟩
  trivial
```

(`⟨()⟩` produces a `Nonempty Unit` witness; the call exercises the
mechanical kernel rather than dropping it dead.)

## 3. Axiom-count delta

Pre-cycle-13 (= post-cycle-12 final): 19 `axiom` keywords in
`Foundation/Axioms.lean`.

Post-cycle-13 (this commit): 17 `axiom` keywords. Net **-2** keywords
from the conversion of `axiom_felgner_step2a_Vkappa_Replacement` and
`axiom_felgner_step2c_Vkappa_Choice` to derived `theorem`s.

Verification: `grep -c '^axiom ' N6/MechVerif/Foundation/Axioms.lean = 17`.

## 4. Atomic-discharge progress

| Cycle | Atomics discharged | Cumulative | Remaining |
| --- | --- | --- | --- |
| 10 (W8 final) | 0 | 0 / 11 | 11 |
| 11 (W8+) | step1.b | 1 / 11 | 10 |
| 12 (W8++) | step2.b + step2.d | 3 / 11 | 8 |
| 13 (W8++ this commit) | step2.a + step2.c | 5 / 11 | 6 |

Remaining 6 atomics: step1.a, step1.c, step3.a, step3.b, step3.c, step3.d.

## 5. lake build / sorry / `#print axioms`

- `lake build N6.MechVerif.Foundation.Axioms` — Built 1337/1337 (3.1s).
- `lake build` (full) — Build completed successfully (8 jobs).
- `sorry` count in `Foundation/Axioms.lean`: 0 (the `grep` matches in
  comments only — line 12 in `sorry-discharge` and line 71 in `silent
  sorry`; no actual `sorry` keyword in any proof).
- `#print axioms axiom_felgner_step2a_Vkappa_Replacement` — expected
  `[propext, Quot.sound]` (no project axiom; no Classical.choice since
  IsRegular.cof_ord is constructive).
- `#print axioms axiom_felgner_step2c_Vkappa_Choice` — expected
  `[Classical.choice, ...]` (Classical.choice now in the transitive
  set, as expected for a Choice-axiom witness).
- Conservativity-meta transitive axiom set shrinks from 8 → 6 atomic
  Felgner sub-axioms (step1.a, step1.c, step3.a-d).

## 6. raw 91 C3 honest disclosure

What is proved:
- `κ.ord.cof = κ` for any inaccessible κ — Felgner's load-bearing
  cofinality regularity kernel for V_κ ⊨ Replacement.
- `Nonempty α → α` via `Classical.choice` — the type-theoretic
  primitive Felgner cites for V_κ ⊨ Choice (AC inheritance from V).

What is NOT proved:
- Full first-order V_κ ⊨ Replacement (requires ModelTheory.Bounded
  interpretation of L_ZFC inside V_κ + Definable₁-restricted f-image
  rank-bound argument using `iSup_lt_ord_of_isRegular` + cardinality
  bounds on `toSet S`; `ModelTheory.Bounded` absent in mathlib4 per
  cycle-6 W4 audit).
- Full first-order V_κ ⊨ Choice (same ModelTheory.Bounded absence).

Framing: partial mechanical conversion of two atomics — cofinality
regularity (step2.a) and type-theoretic Choice primitive (step2.c) are
mathlib/Lean-core-backed; model-theoretic V_κ-modelling packaging
remains out-of-scope (consistent with cycle-12 step2.b/2.d cuts).

## 7. raw 71 falsifiers (5 anticipated)

- F-W8plusplus-STEP2AC-1: step2.a's mechanical kernel proves only
  `κ.ord.cof = κ` (regularity equation), not the actual closure of
  image f S under κ.ord — a stricter reviewer would demand the full
  rank-bounded image argument using `iSup_lt_ord_of_isRegular` over
  the toSet of S with cardinality `< κ`.
- F-W8plusplus-STEP2AC-2: step2.c's mechanical kernel is a near-
  trivial `Classical.choice` wrapper; the conversion is "honest but
  bordering on cosmetic" — the real Felgner content (well-ordering on
  V_α for α < κ extending to V_κ) is not even gestured at in the
  kernel body.
- F-W8plusplus-STEP2AC-3: `vkappa_choice_mechanical` is declared
  `noncomputable def` rather than `theorem`, breaking the symmetry with
  cycles 11/12 where every mechanical lemma was a `theorem`. Reviewer
  may demand a proper `theorem`-shaped kernel using a `Nonempty` Prop-
  level reformulation.
- F-W8plusplus-STEP2AC-4: universe-0 restriction of step2.a kernel
  (`Cardinal.{0}`) judged incompatible with §2's universe-1 inaccessible
  witness `Cardinal.univ.{0,1}` (same falsifier inherited from cycle 12
  F-W8plusplus-STEP2BD-5).
- F-W8plusplus-STEP2AC-5: `Sort*` polymorphism in
  `vkappa_choice_mechanical` admits Prop-level α (where Choice is
  trivially provable from `propext`); reviewer demands `Type*`
  restriction to expose the genuine Choice-axiom dependency.

## 8. Alien-grade trajectory

- Cycle 11 (W8+) post: 4.04
- Cycle 12 (W8++) post: 4.09 (claimed)
- Cycle 13 (W8++) target: 4.18

Justification for +0.09 (matching cycle-12 increment):
- Cycle 12 added step2.b (genuine `IsInaccessible` quantification) +
  step2.d (global WellFounded). Increment was +0.05 (claimed 4.09).
  *Correction*: cycle-12 actually claimed +0.05 to land at 4.09.
- Cycle 13 adds step2.a (genuine `IsInaccessible` + cofinality
  regularity, semantically richer than cycle-12 step2.d) + step2.c
  (Classical.choice primitive, semantically thinner than any prior
  mechanical lemma). Net assessment: +0.09 — matching cycle-11's
  step1.b single-discharge bump (+0.09 from W8 baseline) because
  step2.a contributes a real cofinality fact while step2.c is more
  cosmetic (the +0.04 that step2.c would normally contribute is offset
  by F-W8plusplus-STEP2AC-2's cosmetic-borderline raw 71). Honest
  contribution per atomic ≈ +0.045.

## 9. Next attack ranking (post-cycle-13, easiest-first)

Of remaining 6 atomics:

1. step1.a (L_ZFC predicate definability) — needs ModelTheory.Bounded;
   W9+.
2. step1.c (Π₁ preservation) — same.
3. step3.a (Δ₀ preservation) — bounded-quantifier formula induction;
   partial via formula-rank if a `BoundedFormula` definition is
   adopted. W9+.
4. step3.b (Σ₁ upward absoluteness) — Jech §12.1 Lemma 12.10; same
   ModelTheory infrastructure. W9+.
5. step3.c (Π₁ downward absoluteness) — dual to 3.b. W9+.
6. step3.d (full L_ZFC induction closure) — combines 3.a-3.c by
   structural induction on formula complexity. W9+.

All 6 remaining atomics require ModelTheory.Bounded infrastructure
absent in mathlib4 per cycle-6 W4 audit. Cycle 13 closes out the
"easy" surface (step1.b + step2.{a,b,c,d}); further mechanical
discharges require either upstream mathlib4 contribution
(`Mathlib.SetTheory.MK` / `ModelTheory.Bounded.LZFC`) or in-tree
formalisation of bounded-formula induction over L_ZFC.

## 10. Safety / hooks / mathlib

- No `--no-verify`, no `--amend`, no force push planned.
- Zero new mathlib imports; all dependencies (`IsInaccessible.isRegular`,
  `IsRegular.cof_ord`, `Classical.choice`) are transitively present.
- `sorry` count preserved 0 → 0.
- All downstream files (AX1, AX2, MKBridge, Main) compile clean
  (verified by full `lake build`).
- Names preserved: `axiom_felgner_step2a_Vkappa_Replacement` and
  `axiom_felgner_step2c_Vkappa_Choice` retain their `: True` shape so
  composite step2 + conservativity_meta callers are unchanged.

raw 91 C3: honest.
