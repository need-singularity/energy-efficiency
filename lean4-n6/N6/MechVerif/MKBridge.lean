-- N6.MechVerif.MKBridge : ZFC + V_κ fallback for AX-2 MK-bridge sorrys.
-- W4 deliverable for proposals/hexa-weave-formal-mechanical-verification-prep.md §4 unit 2.
-- Date: 2026-04-28 (cycle 6 fan-out 3/5).
--
-- W6 REFACTOR (cycle 8, 2026-04-28):
--   * 4 named axioms (felgner_1971_conservativity_meta, strand_zfc_witness,
--     felgner_bridge_to_MK, hexa_comp_closure_via_ZFC) RELOCATED to
--     `N6/MechVerif/Foundation/Axioms.lean` (single source of truth).
--   * `StrandClass_ZFC` definition also relocated (it is consumed by the
--     Felgner-bridge axiom signature, so it must live alongside).
--   * `zfc_plus_inaccessible_witness` likewise relocated.
--   * MKBridge.lean now hosts ONLY the `StrandClass_ZFC` exhibition theorems
--     and the AX-2 sorry-discharge theorems (which delegate to Foundation).
--   * F-W5-AX2-1 RESOLVED — 6 axiom (4 here + 2 AX2 mirror) burden collapsed
--     to 5 unique axioms in Foundation/Axioms.lean. raw 91 C3: axioms
--     themselves are unchanged, only location is unified.
--
-- ## W4 Decision Matrix Outcome (unchanged)
--   Option (i)   MK port to mathlib4         — REJECTED
--   Option (ii)  ZFC + ∃κ inaccessible + Felgner 1971 conservativity — ADOPTED
--   Option (iii) Hybrid axiomatic MK fragments — DEFERRED
--
-- See Foundation/Axioms.lean for axiom declarations and W4 §1-§4 prose
-- (Felgner 1971 citation, mathlib4 native primitives, conservativity
-- application). This file retains the ZFC-class exhibition theorems and
-- the AX-2 sorry-discharge entry points.

import N6.MechVerif.Foundation.Strand
import N6.MechVerif.Foundation.Axioms

namespace N6Mathlib.MechVerif.MKBridge

open N6Mathlib.MechVerif

/-! ## §1-§4 Axiom declarations — RELOCATED to Foundation/Axioms.lean

    Pre-W6 declarations now in Foundation/Axioms.lean §3:
      * `axiom_felgner_1971_conservativity_meta`
      * `axiom_strand_zfc_witness`
      * `axiom_felgner_bridge_to_MK`
      * `axiom_hexa_comp_closure_via_ZFC`
    Plus supporting definitions:
      * `StrandClass_ZFC : Class.{0}`
      * `zfc_plus_inaccessible_witness`
    Re-exported transparently via the Foundation/Axioms import. -/

/-! ## §5 ZFC-class exhibition theorems

    These remain here because they are MKBridge-specific consequences of the
    Foundation axioms, not part of the axiom layer itself. -/

/-- `StrandClass_ZFC` is non-empty as a `Class`. -/
theorem StrandClass_ZFC.nonempty : ∃ z : ZFSet.{0}, StrandClass_ZFC z := by
  refine ⟨axiom_strand_zfc_witness Strand.witnessAminoAcid, ?_⟩
  exact ⟨Strand.witnessAminoAcid, rfl⟩

/-- `StrandClass_ZFC` exhibits all five constructor kinds. -/
theorem StrandClass_ZFC.exhibits_each :
    (∃ z : ZFSet.{0}, StrandClass_ZFC z ∧ ∃ seq, axiom_strand_zfc_witness (Strand.aminoAcid seq) = z) ∧
    (∃ z : ZFSet.{0}, StrandClass_ZFC z ∧ ∃ seq, axiom_strand_zfc_witness (Strand.rna seq) = z) ∧
    (∃ z : ZFSet.{0}, StrandClass_ZFC z ∧ ∃ seq, axiom_strand_zfc_witness (Strand.dna seq) = z) ∧
    (∃ z : ZFSet.{0}, StrandClass_ZFC z ∧ ∃ smi, axiom_strand_zfc_witness (Strand.smallLigand smi) = z) ∧
    (∃ z : ZFSet.{0}, StrandClass_ZFC z ∧ ∃ h l, axiom_strand_zfc_witness (Strand.antibody h l) = z) := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · refine ⟨axiom_strand_zfc_witness (Strand.aminoAcid []), ?_, [], rfl⟩
    exact ⟨Strand.aminoAcid [], rfl⟩
  · refine ⟨axiom_strand_zfc_witness (Strand.rna []), ?_, [], rfl⟩
    exact ⟨Strand.rna [], rfl⟩
  · refine ⟨axiom_strand_zfc_witness (Strand.dna []), ?_, [], rfl⟩
    exact ⟨Strand.dna [], rfl⟩
  · refine ⟨axiom_strand_zfc_witness (Strand.smallLigand ""), ?_, "", rfl⟩
    exact ⟨Strand.smallLigand "", rfl⟩
  · refine ⟨axiom_strand_zfc_witness (Strand.antibody [] []), ?_, [], [], rfl⟩
    exact ⟨Strand.antibody [] [], rfl⟩

/-! ## §6 AX2.lean opaque-sorry discharge entry points

    These theorems remain for backward compatibility with prior cycles
    that referenced them by name. They delegate to the Foundation/Axioms
    Strand-form theorems. -/

/-- W4 deliverable: AX-2 STRAND-as-MK-class, derived from ZFC+V_κ + Felgner
    conservativity. Now delegates to `felgner_bridge_to_MK_strand`. -/
theorem AX2_strand_is_MK_class_via_ZFC : IsMKProperClass Strand :=
  felgner_bridge_to_MK_strand

/-- W4 deliverable: AX-2 STRAND closed under HEXA-COMP, derived from
    HEXA-COMP closure axiom. Now delegates to `hexa_comp_closure_strand`. -/
theorem AX2_strand_closed_under_HEXAComp_via_ZFC : ClosedUnderHEXAComp Strand :=
  hexa_comp_closure_strand

/-! ## §7 W6 status report (in-source)

    Achieved (sorry-free, unchanged from W4):
      ✔ ZFC + ∃κ inaccessible witness (now in Foundation/Axioms.lean)
      ✔ Felgner 1971 conservativity stated as named axiom
      ✔ Strand → ZFSet encoding axiom
      ✔ `StrandClass_ZFC : Class` defined; non-empty + exhibits each PROVED
      ✔ Bridge axiom Felgner → MK
      ✔ AX-2 line 277 + 288 sorrys DERIVABLE via Foundation theorems

    W6 REFACTOR (this commit):
      ✔ 4 named axioms relocated to Foundation/Axioms.lean
      ✔ AX2.lean 2 mirror axioms collapsed via Foundation Strand-form theorems
      ✔ F-W5-AX2-1 RESOLVED (6 axiom burden → 5 unique in single file)

    Outstanding gaps (named axioms in Foundation/Axioms.lean — auditable):
      • axiom_felgner_1971_conservativity_meta (W7+)
      • axiom_strand_zfc_witness (W5+)
      • axiom_felgner_bridge_to_MK (W7+)
      • axiom_hexa_comp_closure_via_ZFC (W6+ pending HEXA-COMP def)
      • axiom_robin_hardy_wright_ax1_tail (AX-1; W7+)

    F-D-3 reassessment (unchanged from W4):
      Pre-W4: HIGH 63-72%
      Post-W4: HIGH 58-66%
      Post-W6: HIGH 58-66% (refactor is structural; no semantic change). -/

end N6Mathlib.MechVerif.MKBridge
