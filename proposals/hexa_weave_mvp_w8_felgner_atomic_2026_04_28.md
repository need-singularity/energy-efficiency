# HEXA-WEAVE MVP W8 — Felgner step1/2/3 atomic step-down (cycle 10 fan-out 3/5)

**Date:** 2026-04-28
**Cycle:** 10 / fan-out 3/5
**Owner:** Foundation/Axioms.lean
**Parent missions:**
- proposals/hexa_weave_mvp_2026_04_28.md
- proposals/hexa_weave_mvp_w7_axiom_step_down_2026_04_28.md (cycle 9 fan-out 2/5)

## 1. Mission

Cycle 9 W7 deliberately did not touch the three Felgner step axioms
(`axiom_felgner_step1/2/3`) to keep distance from the rejected
"full Felgner proof" track from cycle 8 fan-out 2/5. Cycle 10 W8 picks
that strand back up at one specific level: structural step-down of
those three monolithic step axioms into atomic sub-axioms. No full
proof is attempted. The decomposition is structural only.

Targets (W7 state):

- `axiom_felgner_step1_class_quantifier_to_Vkappa_bounded : True`
- `axiom_felgner_step2_proper_class_in_Vkappa : True`
- `axiom_felgner_step3_LZFC_relativization : True`

## 2. Decomposition performed

### step 1 → 1.a / 1.b / 1.c (3 atomic sub-axioms)

| Sub-axiom | Sub-property | Source |
|---|---|---|
| `axiom_felgner_step1a_class_LZFC_definable_in_Vkappa` | every MK class C is L_ZFC-definable in V_κ (predicate definability) | Felgner 1971 §3 step 1 (p. 30–31); Drake 1974 §3.4; Jech 2003 §10 (Reflection) |
| `axiom_felgner_step1b_Vkappa_definable_to_set` | V_κ-definable predicate → set in V_(κ+1) by extensionality (separation) | Felgner 1971 §3 step 1 (p. 31); Drake 1974 §3.4 |
| `axiom_felgner_step1c_Pi1_preservation` | translation preserves Π₁ formulas (relativization soundness) | Felgner 1971 §3 step 1 (p. 31); Jech 2003 §12.1 absoluteness |

### step 2 → 2.a / 2.b / 2.c / 2.d (4 atomic sub-axioms)

| Sub-axiom | Sub-property | Source |
|---|---|---|
| `axiom_felgner_step2a_Vkappa_Replacement` | V_κ ⊨ Replacement (κ inaccessible ⇒ cofinality preservation) | Felgner 1971 §3 step 2 (p. 31–32); Drake 1974 §3.4; Jech 2003 §12.1 Thm 12.13 |
| `axiom_felgner_step2b_Vkappa_PowerSet` | V_κ ⊨ Power Set (κ regular + strong-limit ⇒ cardinal preservation) | Felgner 1971 §3 step 2 (p. 32); Drake 1974 §3.4 |
| `axiom_felgner_step2c_Vkappa_Choice` | V_κ ⊨ Choice (AC inherited from V via well-ordering of V_α, α<κ) | Felgner 1971 §3 step 2 (p. 32–33); Drake 1974 §3.4 |
| `axiom_felgner_step2d_Vkappa_Foundation` | V_κ ⊨ Foundation (V_κ rank-bounded, hence well-founded under ∈) | Felgner 1971 §3 step 2 (p. 33); Jech 2003 §12.1 |

Note: 2.a–2.d are particularly attackable because mathlib4
`Mathlib.SetTheory.Cardinal.Regular` already defines
`Cardinal.IsInaccessible` and the related cofinality / regularity API.
Surfacing the four properties as separate sub-axioms makes that future
attack incremental rather than monolithic.

### step 3 → 3.a / 3.b / 3.c / 3.d (4 atomic sub-axioms)

| Sub-axiom | Sub-property | Source |
|---|---|---|
| `axiom_felgner_step3a_Delta0_preservation` | bounded-quantifier (Δ₀) formula preservation under V_κ-relativization | Felgner 1971 §3 step 3 (p. 33); Williams 1976; Jech 2003 §12.1 |
| `axiom_felgner_step3b_Sigma1_upward_absoluteness` | Σ₁ formula upward absoluteness V_κ → V | Felgner 1971 §3 step 3 (p. 33–34); Jech 2003 §12.1 Lemma 12.10 |
| `axiom_felgner_step3c_Pi1_downward_absoluteness` | Π₁ formula downward absoluteness V → V_κ | Felgner 1971 §3 step 3 (p. 34); Williams 1976; Jech 2003 §12.1 |
| `axiom_felgner_step3d_LZFC_full_induction` | full L_ZFC reduction by induction on formula complexity (3.a base + 3.b/3.c quantifier-step rungs) | Felgner 1971 §3 step 3 (p. 34); Williams 1976 |

### Composition layer (3 derived theorems + 1 wrapper preserved)

The W7 monolithic step1/step2/step3 symbols are CONVERTED to derived
`theorem`s, each composing its respective atomic sub-axioms via
`have _h : True := ...; trivial`:

- `theorem axiom_felgner_step1_class_quantifier_to_Vkappa_bounded : True` — combines 1.a + 1.b + 1.c
- `theorem axiom_felgner_step2_proper_class_in_Vkappa : True` — combines 2.a + 2.b + 2.c + 2.d
- `theorem axiom_felgner_step3_LZFC_relativization : True` — combines 3.a + 3.b + 3.c + 3.d

The pre-existing wrapper `axiom_felgner_1971_conservativity_meta` is
re-derived from the three step theorems above (rather than from
`trivial` alone) so that `#print axioms axiom_felgner_1971_conservativity_meta`
transitively lists all 11 atomic sub-axioms.

## 3. Option (a) vs option (b) decision

The mission spec offered two options:

- **(a) replace** — remove monolithic step1/2/3 axioms, replace with
  derived theorems composed from 11 atomic sub-axioms; net 15 → 23 axioms
- **(b) add only** — keep monolithic step1/2/3 axioms AND add 11
  atomic sub-axioms; net 15 → 26 axioms

**Decision: option (a).** Rationale:

1. Mission preference recommended (a) — "smaller atomic axioms have
   lower mechanical-proof attack surface."
2. Keeping monolithic step1/2/3 alongside atomics would create
   logical redundancy (step1 = step1.a ∧ step1.b ∧ step1.c on
   the True-content level) without any audit benefit.
3. Conversion to derived theorems preserves downstream callers (none
   exist outside this file at the moment, but the wrapper
   `axiom_felgner_1971_conservativity_meta` now transitively
   depends on the 11 atomics, which is exactly the intended
   #print axioms surface).

## 4. Net axiom-keyword change

```
pre-cycle-10 (W7) Foundation/Axioms.lean: 15 axiom keywords
  1. axiom_felgner_step1_class_quantifier_to_Vkappa_bounded
  2. axiom_felgner_step2_proper_class_in_Vkappa
  3. axiom_felgner_step3_LZFC_relativization
  4. axiom_strand_zfc_witness_amino
  5. axiom_strand_zfc_witness_rna
  6. axiom_strand_zfc_witness_dna
  7. axiom_strand_zfc_witness_small_ligand
  8. axiom_strand_zfc_witness_antibody
  9. axiom_felgner_bridge_to_MK
  10. axiom_hexa_comp_strand_op_well_defined
  11. axiom_hexa_comp_associativity
  12. axiom_hexa_comp_identity
  13. axiom_hexa_comp_zfc_class_closure
  14. axiom_hexa_comp_closure_atom
  15. axiom_robin_hardy_wright_ax1_tail

post-cycle-10 (W8) Foundation/Axioms.lean: 23 axiom keywords
  Removed (W7 step1/2/3 monolithic, now derived theorems): −3
  Added (atomic step1/2/3 sub-axioms): +11
  Net: 15 − 3 + 11 = 23 axiom keywords (consistent with option a)
```

Verified: `grep -c '^axiom ' N6/MechVerif/Foundation/Axioms.lean` → 23.

## 5. lake build verification

```
$ cd lean4-n6 && lake build N6.MechVerif.Foundation.Axioms
✔ [1336/1336] Built N6.MechVerif.Foundation.Axioms (11s)
Build completed successfully (1336 jobs).

$ cd lean4-n6 && lake build
Build completed successfully (8 jobs).
```

`sorry` count in N6/ Lean sources: 0 (verified — string matches in
Main.lean and AX2.lean comments are documentation, not active `sorry`).

AX1.lean, AX2.lean, MKBridge.lean importers: rebuild clean. No symbol
churn — the converted `step1/step2/step3` theorems retain their
W7 names so any (currently empty) external caller list stays valid.

## 6. F-D-3 re-evaluation

**F-D-3 (decomposition disposition track):** the cycle-10 W8 atomic
step-down extends the structural-decomposition pattern established in
cycle 9 W7 (strand 5-way + hexa_comp 4+1) to the previously
"protected" Felgner step axioms. F-D-3 accordingly downgrades from
"deferred — keep distance from rejected full-proof track" to "active —
atomic step-down landed for steps 1/2/3."

The remaining F-D-3 surface:
- **`axiom_felgner_bridge_to_MK`** is the load-bearing application
  axiom (∃z. StrandClass_ZFC z → IsMKProperClass Strand). Its type
  is non-trivial (not `: True`) so a structural step-down would
  require either (i) further factoring the implication's hypothesis
  along the 5-way Strand split, or (ii) actual MK formalisation.
  Both options are outside W8 scope; F-D-3 leaves this axiom as the
  remaining monolithic Felgner-application surface for W9+ work.
- **`axiom_robin_hardy_wright_ax1_tail`** sits outside the Felgner
  cluster and remains untouched.

## 7. raw 91 C3 honesty

The 11 atomic sub-axioms are `: True`-valued placeholders. Their
semantic content is identical to the W7 monolithic step1/step2/step3
axioms they replace — no new semantic claim is made, no claim is
silently dropped. The decomposition is **structural only**:

- It surfaces 11 attack points instead of 3, each with a precise
  literature citation pointing at the smallest possible classical
  result that would discharge it.
- It does NOT discharge any of the 11. Every sub-axiom is still a
  named `axiom`, auditable via `#print axioms`.
- The composite `axiom_felgner_1971_conservativity_meta` now lists
  all 11 atomic sub-axioms in its `#print axioms` transitive closure
  (via the derived step1/step2/step3 theorems).
- No `sorry` introduced. No silent `True`-witness via `Iff.refl`
  shortcuts. No mirror axioms. No name shadowing.

## 8. Falsifiers (raw 71)

1. **F-W8-FELGNER-1**: an atomic sub-axiom (e.g. `axiom_felgner_step2a_Vkappa_Replacement`) is later proved spurious or non-derivable from the cited source — would require reverting that single sub-axiom and re-investigating the source.
2. **F-W8-FELGNER-2**: `axiom_felgner_1971_conservativity_meta` `#print axioms` output unexpectedly omits one of the 11 atomic sub-axioms (composition gap) — would indicate the derived-theorem chain failed to wire dependency through `have _h : True := ...`.
3. **F-W8-FELGNER-3**: a future cycle discharges one of step1.{a,b,c}, step2.{a,b,c,d}, step3.{a,b,c,d} via mathlib4 facilities (e.g. `Cardinal.IsInaccessible` for step2.a), at which point W8's `: True` placeholder must be replaced by the actual proof — minor migration, but a forced rewrite.
4. **F-W8-FELGNER-4**: option (a) replacement is reverted to option (b) by user/system policy (e.g. need to retain monolithic symbols for some external audit) — would force adding back 3 monolithic axiom keywords (15 → 26 instead of 23).
5. **F-W8-FELGNER-5**: 11-element decomposition is judged too fine-grained and merged back to e.g. step2 = 2.a + 2.b only (Replacement + Power), dropping 2.c + 2.d as "AC and Foundation are downstream" — would re-monolithise step2 to a 2-element split; nominal regression of 2 atomics, audit cost moderate.

## 9. Files touched

- `lean4-n6/N6/MechVerif/Foundation/Axioms.lean`
  - decomposition section under `### Felgner 1971 conservativity ...`
  - 11 new atomic `axiom`s
  - 3 W7 monolithic axioms converted to `theorem`s
  - `axiom_felgner_1971_conservativity_meta` re-derived from the 3 step theorems
  - documentation note added above (cycle 10 W8 disposition paragraph)

No other source files modified. No imports added.
