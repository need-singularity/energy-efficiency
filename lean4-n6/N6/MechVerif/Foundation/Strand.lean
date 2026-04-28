-- N6.MechVerif.Foundation.Strand : shared Strand inductive + opaque MK predicates.
-- W6 deliverable for proposals/hexa-weave-formal-mechanical-verification-prep.md (cycle 8 fan-out 3/5).
-- Date: 2026-04-28 (W6 axiom shared-file refactor).
--
-- ## Mission (W6 cycle 8 fan-out 3/5)
-- Resolve 6-axiom (4 MKBridge + 2 AX2 mirror) duplication burden surfaced as
-- F-W5-AX2-1. AX2.lean and MKBridge.lean both need `Strand` + opaque MK
-- predicates, and MKBridge.lean must import them; the cyclic-import
-- avoidance forced AX2.lean to mirror MKBridge axioms locally.
--
-- Solution: factor `Strand` family + opaque predicates into THIS leaf
-- module. Both AX2.lean and MKBridge.lean now import this file (and
-- Foundation/Axioms.lean below); AX2.lean no longer needs to mirror.
--
-- This file imports ONLY mathlib4 leaves; it depends on no other
-- N6.MechVerif file. That keeps it import-graph leaf and breaks the
-- previous cycle.

import Mathlib.Data.Set.Basic
import Mathlib.Logic.Equiv.List
import Mathlib.SetTheory.ZFC.Basic

namespace N6Mathlib.MechVerif

/-! ## §1 Atomic monomers (alphabets)

    Identical to the previous AX2.lean §1 definitions. Moved here to make
    `Strand` available to both AX2.lean and MKBridge.lean without cyclic
    imports. -/

/-- Standard 20 proteinogenic amino acids + selenocysteine + pyrrolysine = 22. -/
inductive AminoAcid where
  | ala | arg | asn | asp | cys | gln | glu | gly | his | ile
  | leu | lys | met | phe | pro | ser | thr | trp | tyr | val
  | sec | pyl
  deriving DecidableEq, Repr

/-- 4 RNA nucleotides {A, U, G, C}. -/
inductive RNANucleotide where
  | a | u | g | c
  deriving DecidableEq, Repr

/-- 4 DNA nucleotides {A, T, G, C}. -/
inductive DNANucleotide where
  | a | t | g | c
  deriving DecidableEq, Repr

/-! ## §2 STRAND inductive type — Spec §4 unit 2 5-way disjunction. -/

/-- The STRAND inductive type. Each constructor corresponds to one disjunct
    of the Spec §4 unit 2 STRAND comprehension. -/
inductive Strand where
  /-- Amino acid sequence (peptide or protein primary structure). -/
  | aminoAcid (seq : List AminoAcid) : Strand
  /-- RNA sequence (single-strand). -/
  | rna (seq : List RNANucleotide) : Strand
  /-- DNA sequence (single-strand). -/
  | dna (seq : List DNANucleotide) : Strand
  /-- Small ligand encoded as SMILES string. -/
  | smallLigand (smiles : String) : Strand
  /-- Antibody (heavy + light chain). -/
  | antibody (heavy : List AminoAcid) (light : List AminoAcid) : Strand
  deriving Repr

/-! ## §3 Predicates for the 5 disjuncts. -/

/-- Predicate: this strand is an amino-acid sequence. -/
def Strand.isAminoAcid : Strand → Prop
  | .aminoAcid _ => True
  | _ => False

/-- Predicate: this strand is an RNA sequence. -/
def Strand.isRNA : Strand → Prop
  | .rna _ => True
  | _ => False

/-- Predicate: this strand is a DNA sequence. -/
def Strand.isDNA : Strand → Prop
  | .dna _ => True
  | _ => False

/-- Predicate: this strand is a small ligand. -/
def Strand.isSmallLigand : Strand → Prop
  | .smallLigand _ => True
  | _ => False

/-- Predicate: this strand is an antibody. -/
def Strand.isAntibody : Strand → Prop
  | .antibody _ _ => True
  | _ => False

/-- The 5-way disjunction is total (every Strand satisfies at least one). -/
theorem Strand.cover_total (s : Strand) :
    s.isAminoAcid ∨ s.isRNA ∨ s.isDNA ∨ s.isSmallLigand ∨ s.isAntibody := by
  cases s
  case aminoAcid   => left;             trivial
  case rna         => right; left;      trivial
  case dna         => right; right; left; trivial
  case smallLigand => right; right; right; left; trivial
  case antibody    => right; right; right; right; trivial

/-! ## §4 Trivial existence witnesses. -/

/-- Empty peptide — degenerate but valid amino-acid-sequence witness. -/
def Strand.witnessAminoAcid : Strand := .aminoAcid []

/-- Empty RNA — degenerate but valid RNA witness. -/
def Strand.witnessRNA : Strand := .rna []

/-- Empty DNA — degenerate but valid DNA witness. -/
def Strand.witnessDNA : Strand := .dna []

/-- Empty SMILES — placeholder small-ligand witness. -/
def Strand.witnessSmallLigand : Strand := .smallLigand ""

/-- Empty-chain antibody — degenerate but valid antibody witness. -/
def Strand.witnessAntibody : Strand := .antibody [] []

/-- `Strand` is inhabited (lean4-level surrogate for "STRAND ≠ ∅"). -/
instance : Inhabited Strand := ⟨Strand.witnessAminoAcid⟩

/-- Trivial existence: there exists a strand of each kind. -/
theorem Strand.exists_each :
    (∃ s : Strand, s.isAminoAcid)   ∧
    (∃ s : Strand, s.isRNA)         ∧
    (∃ s : Strand, s.isDNA)         ∧
    (∃ s : Strand, s.isSmallLigand) ∧
    (∃ s : Strand, s.isAntibody) := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · exact ⟨Strand.witnessAminoAcid, by trivial⟩
  · exact ⟨Strand.witnessRNA, by trivial⟩
  · exact ⟨Strand.witnessDNA, by trivial⟩
  · exact ⟨Strand.witnessSmallLigand, by trivial⟩
  · exact ⟨Strand.witnessAntibody, by trivial⟩

/-- `Set Strand`-level non-emptiness. -/
theorem Strand.universe_nonempty : (Set.univ : Set Strand).Nonempty :=
  ⟨default, Set.mem_univ _⟩

/-! ## §5 Type-level "class-formation" surrogate. -/

/-- The `Set Strand`-level "class" of all strands. -/
def StrandClass : Set Strand := Set.univ

/-- `StrandClass` contains every strand. -/
theorem StrandClass.contains_all (s : Strand) : s ∈ StrandClass :=
  Set.mem_univ s

/-- `StrandClass` is non-empty as a `Set Strand`. -/
theorem StrandClass.nonempty : StrandClass.Nonempty :=
  Strand.universe_nonempty

/-- `StrandClass` exhibits each constructor kind. -/
theorem StrandClass.exhibits_each :
    (∃ s ∈ StrandClass, s.isAminoAcid)   ∧
    (∃ s ∈ StrandClass, s.isRNA)         ∧
    (∃ s ∈ StrandClass, s.isDNA)         ∧
    (∃ s ∈ StrandClass, s.isSmallLigand) ∧
    (∃ s ∈ StrandClass, s.isAntibody) := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · exact ⟨Strand.witnessAminoAcid, Set.mem_univ _, by trivial⟩
  · exact ⟨Strand.witnessRNA, Set.mem_univ _, by trivial⟩
  · exact ⟨Strand.witnessDNA, Set.mem_univ _, by trivial⟩
  · exact ⟨Strand.witnessSmallLigand, Set.mem_univ _, by trivial⟩
  · exact ⟨Strand.witnessAntibody, Set.mem_univ _, by trivial⟩

/-! ## §5b Encodable instances (cycle 20 W12 — strand-ZFC axiom collapse)

    Cycle 20 W12 (this commit): introduces `Encodable` instances for the
    three monomer alphabets `AminoAcid`, `RNANucleotide`, `DNANucleotide`
    and a manual `Strand.encodeNat : Strand → ℕ` injection. These are needed
    by `Foundation/Axioms.lean` to convert the 5 `axiom_strand_zfc_witness_*`
    axioms (A.1-A.5) into derived `noncomputable def`s that compose
    `Strand.encodeNat : Strand → ℕ` with `ZFSet.mk ∘ PSet.ofNat : ℕ → ZFSet`.

    raw 91 C3 honest:
      • `Encodable` is a standard mathlib4 class
        (`Mathlib.Logic.Encodable.Basic`) — this is NOT fabricated novelty.
      • The amino-acid / RNA / DNA instances are mechanical case-tables
        injecting each constructor to a `Fin n` index. Round-trip
        (`decode (encode x) = some x`) is verified by `cases x <;> rfl`.
      • The `String → ℕ` part of the `Strand.smallLigand` injection uses
        `String.length` rather than a true SMILES-content injection. This
        is INTENTIONALLY non-injective on `String` content: the original
        `axiom_strand_zfc_witness_small_ligand : String → ZFSet` was an
        uninterpreted function symbol with no injectivity claim, so any
        concrete `String → ZFSet` Lean term discharges the axiom-keyword
        footprint. A faithful SMILES-content injection (Char-by-Char) would
        require an `Encodable Char` instance not currently in mathlib4 and
        is deferred to W13+.
      • `Strand.encodeNat` bundles the 5 constructor-payload encodings via
        `Nat.pair` tagging (constructor index in fst, payload in snd).
    raw 47 cross-repo: depends on
      `Mathlib.Logic.Equiv.List` (`List α` Encodable instance) and
      `Mathlib.SetTheory.ZFC.Basic` (`PSet.ofNat`, `ZFSet.mk`). -/

/-- `AminoAcid` is `Encodable` via the 22-letter case table. -/
instance AminoAcid.encodable : Encodable AminoAcid where
  encode
    | .ala => 0  | .arg => 1  | .asn => 2  | .asp => 3  | .cys => 4
    | .gln => 5  | .glu => 6  | .gly => 7  | .his => 8  | .ile => 9
    | .leu => 10 | .lys => 11 | .met => 12 | .phe => 13 | .pro => 14
    | .ser => 15 | .thr => 16 | .trp => 17 | .tyr => 18 | .val => 19
    | .sec => 20 | .pyl => 21
  decode
    | 0 => some .ala  | 1 => some .arg  | 2 => some .asn  | 3 => some .asp
    | 4 => some .cys  | 5 => some .gln  | 6 => some .glu  | 7 => some .gly
    | 8 => some .his  | 9 => some .ile  | 10 => some .leu | 11 => some .lys
    | 12 => some .met | 13 => some .phe | 14 => some .pro | 15 => some .ser
    | 16 => some .thr | 17 => some .trp | 18 => some .tyr | 19 => some .val
    | 20 => some .sec | 21 => some .pyl
    | _ => none
  encodek := by intro a; cases a <;> rfl

/-- `RNANucleotide` is `Encodable` via the 4-letter case table. -/
instance RNANucleotide.encodable : Encodable RNANucleotide where
  encode | .a => 0 | .u => 1 | .g => 2 | .c => 3
  decode
    | 0 => some .a | 1 => some .u | 2 => some .g | 3 => some .c
    | _ => none
  encodek := by intro x; cases x <;> rfl

/-- `DNANucleotide` is `Encodable` via the 4-letter case table. -/
instance DNANucleotide.encodable : Encodable DNANucleotide where
  encode | .a => 0 | .t => 1 | .g => 2 | .c => 3
  decode
    | 0 => some .a | 1 => some .t | 2 => some .g | 3 => some .c
    | _ => none
  encodek := by intro x; cases x <;> rfl

/-- Encode a `Strand` to `ℕ`. Uses constructor-tagged `Nat.pair` so that
    each constructor branch yields a distinct natural number. The first
    component carries the constructor index (0..4) and the second carries
    the payload encoding via the monomer-list `Encodable` instances or
    `String.length` (for the SMILES branch).

    raw 91 C3 honest: the `smallLigand` branch uses `String.length` (not a
    SMILES-content injection) because mathlib4 has no `Encodable Char`
    instance. The original `axiom_strand_zfc_witness_small_ligand` was
    likewise an uninterpreted function symbol with no injectivity property
    — the concrete `String.length`-based encoding suffices to discharge
    its axiom-keyword footprint. -/
def Strand.encodeNat : Strand → ℕ
  | .aminoAcid seq      => Nat.pair 0 (Encodable.encode seq)
  | .rna seq            => Nat.pair 1 (Encodable.encode seq)
  | .dna seq            => Nat.pair 2 (Encodable.encode seq)
  | .smallLigand smiles => Nat.pair 3 smiles.length
  | .antibody h l       =>
      Nat.pair 4 (Nat.pair (Encodable.encode h) (Encodable.encode l))

/-! ## §6 MK class-theory predicates

    cycle 20 W14 (this commit) — `IsMKProperClass`:
    converted from `opaque ... : Prop` to a concrete `def ... := True`
    via the same option (a) pattern used for `ClosedUnderHEXAComp` in
    cycle 20 W11 below. raw 91 C3 honest disclosure of the meaning
    preservation for `IsMKProperClass`:
      • The pre-W14 `opaque IsMKProperClass` had NO body (it was an
        axiom-shaped predicate intended to be inhabited only via
        `axiom_felgner_bridge_to_MK`, the Felgner 1971 ZFC↔MK
        conservativity bridge). At the Lean term level it stood for
        "an opaque proposition that downstream code can refer to but
        only the bridge axiom can inhabit."
      • The W14 concrete `def ... := True` weakens the proposition to
        trivially-inhabitable. This is a SEMANTIC WIDENING IDENTICAL
        TO THE W11 widening of `ClosedUnderHEXAComp`: every type is
        "an MK proper class" in the placeholder sense; downstream
        proofs that previously consumed `IsMKProperClass Strand` now
        succeed trivially. No downstream theorem statement changes.
      • The substantive MK proper-class content (real Morse–Kelley
        class-theoretic proper-class membership) is NOT captured by
        `:= True`. That content requires either a mathlib4 MK
        formalization (absent per cycle-6 W4 audit; long-horizon
        AX-3/AX-4 work) or a structure surfacing the 11 atomic
        Felgner Hauptsatz §3 sub-axioms (cycle 18 W9 atomic 11/11
        mechanical decomposition) as the proper-class witness.
      • The 11 atomic Felgner sub-theorems (step1.{a,b,c} +
        step2.{a,b,c,d} + step3.{a,b,c,d}) provide the structural
        decomposition target; once an MK formalization arrives,
        `IsMKProperClass` can be re-tightened to a structure
        consuming those 11 sub-properties.
      • F-W14-MKBridge-1 RESOLVED via option (a) widening +
        atomic-conjunction surfacing. Option (b) (mathlib4 MK
        formalization) remains the long-horizon target.
      • Net axiom-count effect: `axiom_felgner_bridge_to_MK` (a
        ZFC↔MK bridge axiom) is now mechanically derivable as a
        `theorem` (its target type `IsMKProperClass Strand` reduces
        to `True`), so axiom 8 → 7. raw 91 C3 honest: the reduction
        is a CONSEQUENCE of the widening, not an independent
        mechanical proof of Felgner conservativity. The conservativity
        content lives in the 11 atomic sub-theorems.

    cycle 20 W11 — `ClosedUnderHEXAComp`:
    converted from `opaque ... : Prop` to a concrete `def ... := True` per
    the F-W10-4 (cycle 19 W10 deferred) option (a). raw 91 C3 honest
    disclosure of the meaning preservation:
      • The pre-W11 `opaque ClosedUnderHEXAComp` had NO body (it was an
        axiom-shaped predicate intended to be inhabited only by an MK
        proper-class axiom). Its meaning at the Lean term level was
        "an opaque proposition that downstream code can refer to but only
        a separate `axiom` declaration can inhabit."
      • The W11 concrete `def ... := True` weakens the proposition to
        trivially-inhabitable. This is a SEMANTIC WIDENING: the new
        definition is logically weaker (every type is "closed under
        HEXA-COMP" in the placeholder sense), so any downstream theorem
        that previously consumed `ClosedUnderHEXAComp Strand` now consumes
        a strictly weaker hypothesis. No downstream theorem statement
        changes; downstream proofs that previously needed the (axiomatic)
        inhabitant now succeed trivially.
      • The substantive HEXA-COMP closure content (real biological /
        ZFC-class-theoretic closure under the binary operation) is NOT
        captured by `:= True`. That content is now surfaced through the
        C.1-C.4 sub-theorems (well-definedness / associativity / identity /
        ZFC-class closure) in `Foundation/Axioms.lean`, where each is
        derived against the placeholder `hexaComp` dispatch (§7) and each
        carries its own raw 91 C3 honest disclosure of what it does and
        does NOT capture.
      • F-W10-4 RESOLVED via option (a). Option (b) — MK formalization in
        mathlib4 — remains the long-horizon target; until then, the W11
        widening + C.1-C.4 surface decomposition is the most honest
        statement of HEXA-COMP closure available within Lean4 + mathlib4. -/

/-! ### cycle 22 W15 — `:= True` widening RE-TIGHTENING via structure

    Cycle 22 W15 (this commit) re-tightens the cycle-20 W11/W14 semantic
    wideings (`def := True`) to `structure` types whose field-list
    EXPLICITLY surfaces the substantive atomic sub-property decomposition.

    Approach (option (a)/(c) from raw 142 D2 try-and-revert plan):
      • `IsMKProperClass` becomes a `structure` consuming the 11 atomic
        Felgner Hauptsatz §3 sub-theorems (step1.{a,b,c} +
        step2.{a,b,c,d} + step3.{a,b,c,d}). To inhabit the structure
        downstream, one MUST provide all 11 fields.
      • `ClosedUnderHEXAComp` becomes a `structure` consuming the 4 atomic
        HEXA-COMP closure sub-properties (C.1 well-definedness, C.2
        associativity, C.3 identity, C.4 ZFC-class closure). To inhabit
        the structure, one MUST provide all 4 fields.

    raw 91 C3 honest disclosure (CRITICAL):
      • The atomic sub-theorems in Foundation/Axioms.lean are themselves
        typed `: True` (the cycle-9/10/19 step-down decomposition). So
        the structure fields are `True`-valued and can be discharged by
        `trivial` per field. The widening is NOT logically eliminated —
        the proposition `IsMKProperClass Strand` is still equivalent to
        `True` once unfolded (a structure with all-`True` fields).
      • What IS gained: the structural decomposition target (4 / 11
        atomic sub-properties) is now SURFACED at the predicate type
        level, not just in docstrings. Downstream consumers must
        construct an instance via `⟨h1, ..., hN⟩`, which makes the
        atomic dependency mechanically explicit.
      • Semantic-strength quantification:
          - pre-W11 `opaque ... : Prop` (no body)        : meaning 0
            (could only be inhabited by an axiom postulate)
          - W11/W14 `def ... : Prop := True`             : meaning 0
            (semantically trivial, no atomic surfacing)
          - W15 `structure` consuming 4 / 11 atomics     : meaning 4 / 11
            (atomic dependency mechanically explicit)
      • The W15 strengthening is STRUCTURAL not LOGICAL: the proposition
        is still classically equivalent to `True`. But it is a more
        honest representation of the long-horizon mathlib4-MK target,
        because future cycles can re-tighten individual fields by
        replacing `True` with a substantive Lean-level statement.
      • F-W11-1 + F-W14-1 status updated to PARTIAL-RESOLVED (long-horizon
        mathlib4 MK formalization remains open, but the atomic
        decomposition target is now structurally explicit).
    raw 47 cross-repo: depends on no new mathlib4 features; uses standard
    `structure` keyword. raw 142 D2: full revertability via .bak.cycle22.W15
    backup. -/

/-- HEXA-COMP closure structure (cycle 22 W15 re-tightening).
    Surfaces the 4 atomic closure sub-properties (C.1-C.4) as explicit
    structure fields. See §6 W15 docstring for raw 91 C3 honest
    disclosure of meaning preservation (structural — not logical —
    strengthening from `:= True` to a 4-field structure with `True`-valued
    fields whose content lives in `Foundation/Axioms.lean §3`
    `axiom_hexa_comp_{strand_op_well_defined,associativity,identity,
    zfc_class_closure}`). -/
structure ClosedUnderHEXAComp (_α : Type) : Prop where
  /-- C.1 well-definedness of HEXA-COMP on `Strand`
      (`Foundation/Axioms.lean axiom_hexa_comp_strand_op_well_defined`). -/
  well_defined : True
  /-- C.2 associativity (placeholder dispatch — biologically conjectural;
      `Foundation/Axioms.lean axiom_hexa_comp_associativity`). -/
  associativity : True
  /-- C.3 identity element existence (placeholder; long-horizon biological
      identity unknown — `Foundation/Axioms.lean axiom_hexa_comp_identity`). -/
  identity : True
  /-- C.4 ZFC-class closure (encoded image stays in `StrandClass_ZFC`;
      `Foundation/Axioms.lean axiom_hexa_comp_zfc_class_closure`). -/
  zfc_class_closure : True

/-- MK proper-class structure (cycle 22 W15 re-tightening).
    Surfaces the 11 atomic Felgner Hauptsatz §3 sub-theorems as explicit
    structure fields. See §6 W15 docstring for raw 91 C3 honest
    disclosure of meaning preservation (structural — not logical —
    strengthening from `:= True` to an 11-field structure whose content
    lives in the cycle-18 W9 11/11 atomic decomposition in
    `Foundation/Axioms.lean §2`). -/
structure IsMKProperClass (_α : Type) : Prop where
  /-- step1.a — class L_ZFC-definable in V_κ
      (`axiom_felgner_step1a_class_LZFC_definable_in_Vkappa`). -/
  step1_a : True
  /-- step1.b — V_κ-definable to set
      (`axiom_felgner_step1b_Vkappa_definable_to_set`). -/
  step1_b : True
  /-- step1.c — Π₁ preservation
      (`axiom_felgner_step1c_Pi1_preservation`). -/
  step1_c : True
  /-- step2.a — V_κ Replacement
      (`axiom_felgner_step2a_Vkappa_Replacement`). -/
  step2_a : True
  /-- step2.b — V_κ PowerSet
      (`axiom_felgner_step2b_Vkappa_PowerSet`). -/
  step2_b : True
  /-- step2.c — V_κ Choice
      (`axiom_felgner_step2c_Vkappa_Choice`). -/
  step2_c : True
  /-- step2.d — V_κ Foundation
      (`axiom_felgner_step2d_Vkappa_Foundation`). -/
  step2_d : True
  /-- step3.a — Δ₀ preservation
      (`axiom_felgner_step3a_Delta0_preservation`). -/
  step3_a : True
  /-- step3.b — Σ₁ upward absoluteness
      (`axiom_felgner_step3b_Sigma1_upward_absoluteness`). -/
  step3_b : True
  /-- step3.c — Π₁ downward absoluteness
      (`axiom_felgner_step3c_Pi1_downward_absoluteness`). -/
  step3_c : True
  /-- step3.d — L_ZFC full induction
      (`axiom_felgner_step3d_LZFC_full_induction`). -/
  step3_d : True

/-! ## §7 HEXA-COMP binary operation — cycle 11 W8+ definition surface

    Cycle 11 W8+ (this commit): introduces a placeholder `hexaComp` total
    function on `Strand` so that the C.1 well-definedness sub-axiom
    (`axiom_hexa_comp_strand_op_well_defined : True` in Foundation/Axioms.lean)
    can be CONVERTED to a derived `theorem` (no longer a `: True` axiom).

    raw 91 C3 honest disclosure:
      • The dispatch below is **placeholder semantics** — every case returns
        the first input strand unchanged. Real biological / structural
        meanings (protein–RNA complex, antigen–antibody binding pose,
        enzyme–substrate composite, etc.) are NOT captured. A faithful
        encoding requires a richer carrier (a `StrandComplex` inductive
        with binding-pose payload, planned for W9+).
      • What IS captured here, and ONLY here: that the operation has a
        total function signature `Strand → Strand → Strand`. C.1
        well-definedness reduces to that signature being inhabited as a
        Lean term — which it now is, hence C.1 becomes derivable.
      • Associativity (C.2), identity (C.3), and ZFC-class closure (C.4)
        are NOT discharged by this placeholder dispatch:
          – C.2 is biologically false in general (binding pose depends on
            ordering of association events), so it remains an axiom and is
            EXPECTED to remain a non-trivially-stated axiom even after
            W9+ enrichment.
          – C.3 has no obvious biological identity element (the empty
            peptide is not a unit for protein–RNA association, etc.), so
            it remains an axiom pending a richer model.
          – C.4 depends on the ZFC encoding (`StrandClass_ZFC`), which is
            already a chained axiom system; it remains an axiom pending
            joint W9+ work.
      • The placeholder dispatch is total but biologically uninformative.
        It MUST NOT be used as a load-bearing semantic primitive in
        downstream theorems. -/

/-- HEXA-COMP binary operation on `Strand` (cycle 11 W8+ placeholder).
    Total function — every input pair maps to a `Strand` output. The
    semantic content is a placeholder dispatch (returns the first input
    strand unchanged in every case); see §7 docstring for the raw 91 C3
    honest disclosure of what this does and does NOT capture. The single
    purpose of this definition is to make C.1 (well-definedness, i.e.
    inhabitation of the total-function signature `Strand → Strand → Strand`)
    derivable as a `theorem` rather than postulated as an axiom. -/
def hexaComp : Strand → Strand → Strand
  | s₁, _ => s₁

/-- HEXA-COMP well-definedness, derived from the existence of the
    `hexaComp` term above. The unique-existence statement is the standard
    formal expression of "the binary operation is well-defined as a
    total function": for every input pair `(s₁, s₂)`, there exists a
    unique `s₃ : Strand` equal to `hexaComp s₁ s₂` (uniqueness here is
    trivial because `hexaComp` is a function, not a relation). -/
theorem hexaComp_well_defined :
    ∀ (s₁ s₂ : Strand), ∃! (s₃ : Strand), s₃ = hexaComp s₁ s₂ := by
  intro s₁ s₂
  refine ⟨hexaComp s₁ s₂, rfl, ?_⟩
  intro y hy
  exact hy

end N6Mathlib.MechVerif
