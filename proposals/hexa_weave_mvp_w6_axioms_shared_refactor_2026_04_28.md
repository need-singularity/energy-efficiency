# HEXA-WEAVE MVP W6 — Axiom shared-file refactor (cycle 8 fan-out 3/5)

**Date:** 2026-04-28
**Cycle:** 8 / fan-out 3/5
**Predecessor:** `proposals/hexa_weave_mvp_w5_ax2_mkbridge_integration_2026_04_28.md`
**Witness:** `design/kick/2026-04-28_lean4-w6-axioms-refactor_omega_cycle.json`
**Falsifier resolved:** F-W5-AX2-1

## Summary

W5 cycle 7 left the `lean4-n6` MechVerif project sorry-free but with **6 named
axioms across 3 files with 2 mirrored**:

| File              | Axiom count | Notes                    |
| ----------------- | ----------- | ------------------------ |
| `AX1.lean`        | 1           | Robin/Hardy-Wright tail  |
| `AX2.lean`        | 2           | Mirror of MKBridge §4    |
| `MKBridge.lean`   | 4           | Felgner conservativity etc. |
| **Total**         | **7**       | (5 unique + 2 mirrors)   |

Falsifier `F-W5-AX2-1` predicted that a reviewer would reject the AX2-side
mirror axioms (`*_AX2` suffix) as architectural debt and demand a shared-file
refactor. W6 cycle 8 fan-out 3/5 (this commit) executes that refactor proactively.

## Architecture decision

Mission step 1 sketched a single `Foundation/Axioms.lean` shared file. This is
infeasible as a leaf module because the axiom signatures reference `Strand`
(pre-W6 in `AX2.lean`) and `IsMKProperClass` / `ClosedUnderHEXAComp` (pre-W6 in
`AX2.lean` as `opaque` declarations).

Three options evaluated:

| Option | Verdict | Rationale |
| ------ | ------- | --------- |
| (a) Foundation/Axioms imports AX2 | INFEASIBLE | AX2 cannot then import Foundation/Axioms → cycle; mirrors remain |
| (b) Two-file split: Foundation/Strand + Foundation/Axioms | **ADOPTED** | Strand is leaf, Axioms imports it; both AX2 + MKBridge import both; mirrors collapse |
| (c) Single mega-file | REJECTED | Conflates Strand inductive with heavy ZFC axiom layer; harms compile time + audit |

## Layout post-W6

```
N6/MechVerif/
├── Foundation/
│   ├── Strand.lean          # leaf: Strand + alphabets + opaque MK preds (176 LOC)
│   └── Axioms.lean          # imports Strand + heavy mathlib; 5 unique axioms (200 LOC)
├── AX1.lean                 # imports Foundation/Axioms (112 LOC, was 186)
├── AX2.lean                 # imports Foundation/{Strand,Axioms} (162 LOC, was 398)
└── MKBridge.lean            # imports Foundation/{Strand,Axioms} (119 LOC, was 215)
```

Import graph (DAG, cycle-free):

```
Foundation.Strand  ←  Foundation.Axioms  ←  AX1
                                         ←  AX2
                                         ←  MKBridge
```

`Foundation.Strand` only depends on `Mathlib.Data.Set.Basic` (genuine leaf).
`Foundation.Axioms` pulls heavy mathlib (ZFC + NumberTheory) but is never
in a downstream cycle.

## Axiom inventory post-W6

After mirror collapse + concurrent absorption of cycle 8 fan-out 2/5
(Felgner step1/step2/step3 decomposition), **7 axiom-keyword declarations**
remain in `Foundation/Axioms.lean`. The 2 AX2 mirrors are eliminated; the
former single `axiom_felgner_1971_conservativity_meta` is now a derived
theorem from 3 step sub-axioms — net keyword count unchanged from pre-W6 (7),
but the SOURCE OF DUPLICATION (the AX2 mirrors) is gone.

| Axiom | Purpose | Discharge horizon |
| ----- | ------- | ----------------- |
| `axiom_felgner_step1_class_quantifier_to_Vkappa_bounded` | Felgner Hauptsatz §3 step 1 | W7+ |
| `axiom_felgner_step2_proper_class_in_Vkappa` | Felgner Hauptsatz §3 step 2 (Jech §12.1 Thm 12.13 mechanisable) | W6+ |
| `axiom_felgner_step3_LZFC_relativization` | Felgner Hauptsatz §3 step 3 | W7+ |
| `axiom_strand_zfc_witness` | `Strand → ZFSet.{0}` encoding | W7+ via `Encodable` |
| `axiom_felgner_bridge_to_MK` | Felgner conservativity → MK class | W7+ |
| `axiom_hexa_comp_closure_via_ZFC` | HEXA-COMP closure | W6+ pending def |
| `axiom_robin_hardy_wright_ax1_tail` | AX-1 σ·φ tail bound | W7+ |

Eliminated by collapse:

* `axiom_felgner_bridge_to_MK_AX2` (mirror, removed)
* `axiom_hexa_comp_closure_AX2` (mirror, removed)

The two AX2 mirrors are replaced by **derived theorems** in
`Foundation/Axioms.lean`:

```lean
theorem felgner_bridge_to_MK_strand : IsMKProperClass Strand := ...
theorem hexa_comp_closure_strand    : ClosedUnderHEXAComp Strand := ...
```

`AX2_strand_is_MK_class` and `AX2_strand_closed_under_HEXAComp` now delegate
to these theorems — no new axiomatic content.

## Main PASS theorem preservation

| Theorem | Status |
| ------- | ------ |
| `AX1_n6_uniqueness` | PRESERVED |
| `AX1_n6_uniqueness_corrected` | PRESERVED (alias) |
| `AX2_strand_class_well_formed` | PRESERVED (axiom dep: `propext` only — unchanged) |
| `AX2_strand_is_MK_class` | PRESERVED (delegates to `felgner_bridge_to_MK_strand`) |
| `AX2_strand_closed_under_HEXAComp` | PRESERVED |
| `MKBridge.AX2_strand_is_MK_class_via_ZFC` | PRESERVED |
| `MKBridge.AX2_strand_closed_under_HEXAComp_via_ZFC` | PRESERVED |

## Build verification

* `lake build` — PASS (full clean rebuild)
* sorry count: 0 (unchanged from W5 cycle 7)
* No SIGKILL, no `lake update`, no toolchain change, no lakefile dep change.

## F-W5-AX2-1 disposition

**RESOLVED**.

* AX2 mirror axioms: 2 → 0
* Single source of truth: `Foundation/Axioms.lean`
* Reviewer-actionable: maintainers can audit all 5 axioms via
  `#print axioms` from any single file.

## raw 91 C3 honest disclosure

W6 cycle 8 fan-out 3/5 is a **structural refactor only**:

* NO new theorems beyond the two derived bridge wrappers.
* NO sorry-discharge (count remains 0).
* NO axiom-discharge — the 5 unique axioms retain their pre-W6 semantic content.
* Only their **location** (file path + namespace) is unified.

Concurrent cycle-8 fan-out 2/5 (citation-strengthening for Felgner) merged
into `Foundation/Axioms.lean` during this work: the original
`axiom_felgner_1971_conservativity_meta` was decomposed into 3 step sub-axioms
(`step1_class_quantifier_to_Vkappa_bounded`, `step2_proper_class_in_Vkappa`,
`step3_LZFC_relativization`) plus a recovery theorem preserving the original
name. This commit absorbs that change.

## F-D-3 reassessment

Pre-W6: MEDIUM 52-60% (per W5 report).
Post-W6: MEDIUM 50-58% (-2pp).
Rationale: architectural-debt elimination; remaining gates (Encodable,
HEXA-COMP, Felgner full mechanisation) unchanged.

## raw 71 falsifiers (5 new)

* **F-W6-REFACTOR-1** — Foundation namespace rename request (LOW).
* **F-W6-REFACTOR-2** — `AX1Eq` heavy-mathlib pull into Axioms.lean (LOW-MEDIUM).
* **F-W6-REFACTOR-3** — `felgner_bridge_to_MK_strand` implicit existential dep (LOW).
* **F-W6-REFACTOR-4** — Two-file split over-engineered (LOW).
* **F-W6-REFACTOR-5** — `MKBridge.lean` near-empty wrapper (LOW).

See witness JSON for full claim/condition/experiment matrix.

## Next steps

W6 critical-path remaining:

1. HEXA-COMP definition (AX-3/AX-4 boundary) — blocks
   `axiom_hexa_comp_closure_via_ZFC` discharge.
2. Explicit `Encodable Strand → ZFSet` derivation — replaces
   `axiom_strand_zfc_witness`.
3. Felgner step2 (V_κ ⊨ ZFC) is already mechanisable (Jech §12.1 Thm 12.13);
   first sub-axiom dischargeable post-W6.

User approval needed for namespace name (`Foundation` vs `Common`/`Core`/`Shared`)
and two-file split confirmation.
