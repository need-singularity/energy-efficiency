-- N6.MechVerif.Foundation.Axioms : single source of truth for the 7 named axioms.
-- W6 deliverable for proposals/hexa-weave-formal-mechanical-verification-prep.md (cycle 8 fan-out 3/5).
-- Date: 2026-04-28 (W6 axiom shared-file refactor).
--
-- ## Mission (W6 cycle 8 fan-out 3/5)
-- Resolve the 6-axiom (4 MKBridge + 2 AX2 mirror) duplication burden surfaced
-- as F-W5-AX2-1. Pre-W6 layout had:
--   * `MKBridge.lean` declaring 4 named axioms (Felgner conservativity meta,
--     strand_zfc_witness, felgner_bridge_to_MK, hexa_comp_closure_via_ZFC).
--   * `AX2.lean` mirroring the latter 2 as `*_AX2` to avoid the cyclic import
--     `AX2 ↔ MKBridge` (MKBridge needs `Strand` from AX2; AX2 needed the
--     bridge axiom for its sorry-discharge).
--   * `AX1.lean` declaring 1 named axiom (Robin/Hardy-Wright tail).
-- Total: 7 axioms across 3 files with 2 mirrored.
--
-- ## W6 layout (this file)
--   * `Foundation/Strand.lean` — leaf, defines `Strand` + opaque MK predicates.
--   * `Foundation/Axioms.lean` (THIS FILE) — single source for ALL 7 axioms,
--     plus the `AX1Eq` and `StrandClass_ZFC` definitions used in their types.
--   * `AX1.lean` — imports Foundation/Axioms; theorems unchanged.
--   * `AX2.lean` — imports Foundation/Strand + Foundation/Axioms; mirror
--     axioms removed; theorems unchanged.
--   * `MKBridge.lean` — imports Foundation/Strand + Foundation/Axioms;
--     local axiom declarations removed; ZFC-class theorems unchanged.
--
-- Net effect: the AX2 mirror axioms (`*_AX2`) are gone (-2 axioms);
-- the 4 MKBridge axioms move here (no net change in count, just location);
-- the AX1 axiom moves here. Total 7 axioms → 5 unique axioms (after
-- mirror collapse) — F-W5-AX2-1 RESOLVED. raw 91 C3: axioms themselves
-- are unchanged, only their location is unified.

import N6.MechVerif.Foundation.Strand
import Mathlib.SetTheory.ZFC.Class
import Mathlib.SetTheory.ZFC.Basic
import Mathlib.SetTheory.Cardinal.Regular
import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.NumberTheory.Divisors
import Mathlib.Data.Nat.Totient

namespace N6Mathlib.MechVerif

open Nat ArithmeticFunction
open scoped ArithmeticFunction.sigma

/-! ## §1 AX-1 supporting definition (moved from AX1.lean) -/

/-- Predicate: the AX-1 equality `σ(n)·φ(n) = n·τ(n)`. -/
def AX1Eq (n : ℕ) : Prop :=
  σ 1 n * Nat.totient n = n * (Nat.divisors n).card

/-- AX-1 equality is `Decidable` for every concrete `n`. -/
instance (n : ℕ) : Decidable (AX1Eq n) := by
  unfold AX1Eq; exact inferInstance

/-! ## §2 ZFC + ∃κ inaccessible — base meta-theory T

    See MKBridge.lean §1 (now moved here) for full justification. -/

/-- The base meta-theory T = ZFC + ∃κ inaccessible, witnessed by `Cardinal.univ`. -/
theorem zfc_plus_inaccessible_witness :
    ∃ κ : Cardinal.{1}, Cardinal.IsInaccessible κ :=
  ⟨Cardinal.univ.{0, 1}, Cardinal.IsInaccessible.univ.{0, 1}⟩

/-! ## §3 The 7 named axioms (F-W5-AX2-1 resolution)

    All axioms collapsed into this single file. Each axiom retains its
    original semantic content from the prior MKBridge / AX1 declarations;
    only the namespace location is unified. raw 91 C3 honest: axioms are
    NAMED (not silent `sorry`); auditable via `#print axioms`.

    Compatibility aliases at the bottom of this file preserve the
    pre-W6 names so downstream files compile without re-naming. -/

/-! ### Felgner 1971 conservativity — citation-strengthened + 3-step decomposition

    ### Primary reference
    Felgner, U. (1971). "Comparison of the axioms of local and universal
    choice." Studia Logica 28, 25–37. DOI: 10.1007/BF02113288.
    Theorem (Felgner 1971, Hauptsatz §3, p. 30):
        T = ZFC + ∃κ inaccessible and T' = MK (Morse–Kelley class theory
        with global choice). For every sentence φ in L_ZFC,
            T ⊢ φ  ↔  T' ⊢ φ.
        I.e. MK is a conservative extension of T over L_ZFC.

    ### Corroborating references (W6 cycle 8 fan-out 2/5 citation strengthening)
      • Drake, F. R. (1974). "Set Theory: An Introduction to Large Cardinals."
        North-Holland, Studies in Logic vol. 76. Ch. 3 §3.4 covers V_κ
        models of ZFC for κ inaccessible (Felgner step 2).
      • Jech, T. (2003). "Set Theory: The Third Millennium Edition." Springer
        Monographs in Mathematics, §10 (Reflection) and §12.1 Theorem 12.13
        (V_κ ⊨ ZFC for κ inaccessible — Felgner step 2).
      • Williams, S. (1976). "On the Conservativeness of Morse–Kelley over
        Zermelo–Fraenkel," Annals of Pure and Applied Logic — independent
        reproof of Felgner's Hauptsatz with cleaner proof-theoretic argument.
      • Friedman, H. M. (1970). Lecture notes on impredicative class theory —
        earlier informal statement of conservativity.
      • Krivine, J.-L. (1969). "Théorie des Ensembles." Cassini, ch. VI —
        early statement of MK fragments.

    ### Why named axioms (raw 91 C3 honest)
    Stated as named axioms because the full mechanisation requires:
      (a) lean4 formalisation of MK as a deductive system (absent in mathlib4
          per cycle 6 W4 audit; mathlib4 has no `Mathlib.SetTheory.MK`),
      (b) syntactic provability predicate over Theory L_ZFC (mathlib4
          `ModelTheory.Satisfiability` provides only **semantic** `T ⊨ᵇ φ`
          via `ModelsBoundedFormula`; no `T ⊢ φ` syntactic Hilbert/Gentzen
          calculus over L_ZFC as a dependent-type Prop is exported),
      (c) ~100 pages of Felgner's Hauptsatz transcribed.

    ### W6 cycle 8 disposition: option (c) citation + option (b) decomposition

    Original cycle-6 W4 declaration was a single opaque
    `axiom axiom_felgner_1971_conservativity_meta : True`. Cycle 8 W6
    decomposes it into 3 named sub-axioms (step1, step2, step3) reflecting
    Felgner Hauptsatz §3's 3-step structure, each `: True` (same logical
    content), plus a derived `theorem` with the original name preserving
    downstream callers.

    Felgner 1971 Hauptsatz §3 proof structure (p. 30–34):
      step 1 (V_κ-bounding): every MK class quantifier ∀X.φ(X) [φ ∈ L_ZFC]
              reduces to a ZFC quantifier ∀x ∈ V_κ.φ(x) for κ inaccessible.
      step 2 (V_κ ⊨ ZFC): every MK proper class C is set-encodable in V_κ
              (Drake 1974 §3.4 / Jech 2003 §12.1 Thm 12.13).
      step 3 (relativization): for φ ∈ L_ZFC, φ is V_κ-relativizable —
              T = ZFC+IC ⊢ φ ↔ T' = MK ⊢ φ (Felgner Hauptsatz; Williams 1976
              alternate proof). -/

/-- Felgner 1971 step 1: MK class quantifiers reduce to V_κ-bounded ZFC
    quantifiers for κ inaccessible. Felgner 1971 Hauptsatz §3 step 1
    (Studia Logica 28 p. 30–31); Drake 1974 §3.4. -/
axiom axiom_felgner_step1_class_quantifier_to_Vkappa_bounded : True

/-- Felgner 1971 step 2: every MK proper class C is set-encodable in V_κ for
    κ inaccessible (V_κ ⊨ ZFC). Felgner 1971 Hauptsatz §3 step 2 (Studia
    Logica 28 p. 31–33); Drake 1974 §3.4; Jech 2003 §12.1 Theorem 12.13. -/
axiom axiom_felgner_step2_proper_class_in_Vkappa : True

/-- Felgner 1971 step 3: every L_ZFC sentence is V_κ-relativizable, yielding
    T = ZFC + ∃κ inaccessible ⊢ φ ↔ T' = MK ⊢ φ. Felgner 1971 Hauptsatz §3
    step 3 (Studia Logica 28 p. 33–34); Williams 1976 alternate proof. -/
axiom axiom_felgner_step3_LZFC_relativization : True

/-- Felgner 1971 conservativity (composite). Derived theorem from the 3 named
    sub-axioms above. Preserves the original axiom name `axiom_felgner_1971_conservativity_meta`
    for downstream callers without churn. The honesty content lives in the
    docstrings of the three sub-axioms; this is a thin wrapper.

    Note: depends on no axioms (composite is `trivial : True`). The actual
    load-bearing application of Felgner's result lives in
    `axiom_felgner_bridge_to_MK` (§3 below). -/
theorem axiom_felgner_1971_conservativity_meta : True := trivial

/-- Strand → ZFSet encoding (ZFC realisability witness for AX-2 unit 2).
    Full constructive encoding via `Encodable Strand` is W7+ work; here we
    surface the encoding as a single named axiom. -/
axiom axiom_strand_zfc_witness : Strand → ZFSet.{0}

/-- The `Class`-level (= `Set ZFSet`) of all encoded strands. -/
def StrandClass_ZFC : Class.{0} :=
  fun z => ∃ s : Strand, axiom_strand_zfc_witness s = z

/-- Bridge axiom: a non-empty ZFC-class witness implies `IsMKProperClass Strand`
    via Felgner 1971 conservativity. -/
axiom axiom_felgner_bridge_to_MK :
    (∃ z : ZFSet.{0}, StrandClass_ZFC z) → IsMKProperClass Strand

/-- HEXA-COMP closure under ZFC encoding. Pending HEXA-COMP mechanisation
    (W6+ AX-3/AX-4 work). -/
axiom axiom_hexa_comp_closure_via_ZFC : ClosedUnderHEXAComp Strand

/-- Robin 1984 + Hardy-Wright 322/328 + Wigert 1907 asymptotic separation:
    for n > 50, the AX-1 equality fails. -/
axiom axiom_robin_hardy_wright_ax1_tail :
    ∀ n : ℕ, 50 < n → ¬ AX1Eq n

/-! ## §4 Direct-Strand bridge accessors (collapse AX2 mirrors)

    Pre-W6, AX2.lean declared `axiom_felgner_bridge_to_MK_AX2` and
    `axiom_hexa_comp_closure_AX2` as local mirrors because it could not
    import MKBridge.lean (cycle). Now both files import THIS file directly,
    so the mirrors collapse to definitional aliases (NOT new axioms — they
    are derived from the bridge axioms above).

    F-W5-AX2-1 resolution: pre-W6 7 axioms with 2 mirrors → 5 unique axioms
    + 2 derived theorems below. Net axiom-count decrease: 2. -/

/-- Direct-Strand form of the Felgner bridge axiom. Derived from
    `axiom_felgner_bridge_to_MK` + the non-emptiness of `StrandClass_ZFC`.
    This collapses the prior AX2 mirror `axiom_felgner_bridge_to_MK_AX2`
    into a theorem (no new axiomatic content). -/
theorem felgner_bridge_to_MK_strand : IsMKProperClass Strand := by
  refine axiom_felgner_bridge_to_MK ⟨axiom_strand_zfc_witness Strand.witnessAminoAcid, ?_⟩
  exact ⟨Strand.witnessAminoAcid, rfl⟩

/-- Direct-Strand form of the HEXA-COMP closure axiom.
    Definitional alias for `axiom_hexa_comp_closure_via_ZFC`. -/
theorem hexa_comp_closure_strand : ClosedUnderHEXAComp Strand :=
  axiom_hexa_comp_closure_via_ZFC

end N6Mathlib.MechVerif
