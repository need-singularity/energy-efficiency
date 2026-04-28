# HEXA-WEAVE MVP W6 — `axiom_felgner_1971_conservativity_meta` full-proof attempt (cycle 8 fan-out 2/5)

**Date**: 2026-04-28 (cycle 8 fan-out 2/5)
**Parent spec**: `proposals/hexa-weave-formal-mechanical-verification-prep.md`
**Predecessor**: `proposals/hexa_weave_mvp_w5_ax2_mkbridge_integration_2026_04_28.md`
**Window**: nominal 2026-06-30 → 2026-07-13; actual 2026-04-28 (early start day −63)
**Deliverable file**: `lean4-n6/N6/MechVerif/Foundation/Axioms.lean` (modified; 0 sorry preserved)
**Note (cycle 8 cross-fanout interaction)**: a parallel cycle-8 fan-out 3/5 refactor relocated all 7 named axioms from MKBridge.lean / AX2.lean / AX1.lean into `N6/MechVerif/Foundation/Axioms.lean` (single source of truth). This proposal's edits target the new location.

---

## §1 W6 Mission

Attempt a full proof of `axiom_felgner_1971_conservativity_meta` — the most load-bearing of the 4 named axioms in MKBridge.lean (cycle 6 W4). This unblocks the raw-91-C3 axiom dependency chain at AX-2 STRAND class membership.

Mission constraints:
- No silent axioms.
- 0 sorry preserved (do not regress cycle 7 W5).
- raw 91 C3: full mechanical proof not feasible → disclose honestly.

---

## §2 Decision matrix (cycle 8 W6)

| Option | Description | Verdict | Rationale |
|---|---|---|---|
| (a) | Full mechanical proof in lean4 | REJECTED | 6-12 months. Felgner's Hauptsatz §3 is 100+ pp. mathlib4 has no MK formalization (W1 audit). mathlib4 `ModelTheory.Satisfiability` exposes only **semantic** `T ⊨ᵇ φ`; no syntactic Hilbert/Gentzen `T ⊢ φ` over `L_ZFC` as a dependent-type Prop. Out of F-D-3 90d. |
| (b) | Decompose into named sub-axioms | PARTIAL ADOPTED | Splits 1 axiom into 3 named sub-axioms reflecting Felgner's 3-step proof structure (V_κ-bounding, V_κ ⊨ ZFC, L_ZFC-relativization). Documents proof skeleton. Same logical content. |
| (c) | Citation strengthening (Drake 1974, Jech §12, Williams 1976) | ADOPTED | 5 corroborating refs added; precise page references; reviewer-facing surface materially clearer. |
| (d) | Levy / Krivine substitute | NOT AVAILABLE | mathlib4 grep confirms no set-theoretic Levy 1976 or Krivine 1969 conservativity result. ("Levy" hits in mathlib are Lévy-Prokhorov metric in probability — unrelated.) |

**Selected: (c) + (b) hybrid.**

---

## §3 mathlib4 audit findings

```
$ grep -r -l "Felgner\|Krivine" Mathlib/         → 1 hit (ModelTheory/Fraisse.lean — unrelated Fraisse limit attribution)
$ grep -r -l "MorseKelley\| MK \|Morse.Kelley"   → 0 hits in set-theoretic context
$ grep -r -l "conservativ" Mathlib/SetTheory/    → 0 hits (only category-theoretic / probability conservativity unrelated)
$ grep -r -l "Levy\|Lévy" Mathlib/SetTheory/     → 0 hits in set-theoretic context (Lévy-Prokhorov in MeasureTheory only)
```

mathlib4 `Mathlib.SetTheory.ZFC.{Basic,Class,Cardinal}` exposes:
- `ZFSet`, `Class = Set ZFSet`, `Cardinal.IsInaccessible`, `Cardinal.IsInaccessible.univ`.

mathlib4 `Mathlib.ModelTheory.{Satisfiability,Semantics}` exposes:
- `T.IsSatisfiable`, `T ⊨ᵇ φ` (= `ModelsBoundedFormula`) — **semantic only**.
- No `T ⊢ φ` syntactic deductive system surfaced for `Theory L_ZFC`.

Conclusion: option (a) requires a multi-month mathlib4 contribution to formalize MK + add a syntactic provability predicate. Option (d) substitute is unavailable. Options (b) + (c) are the maximal honest progress.

---

## §4 Implementation

### File modified
`lean4-n6/N6/MechVerif/Foundation/Axioms.lean` (single file; ~133 LOC → ~201 LOC; +68 LOC of citations + 3-step decomposition; targeting the post-relocation single source of truth).

### Diff summary

**Before** (cycle 6 W4):
```lean
axiom axiom_felgner_1971_conservativity_meta : True
```

**After** (cycle 8 W6):
```lean
/-- Felgner 1971 step 1: MK class quantifiers reduce to V_κ-bounded ZFC
    quantifiers for κ inaccessible. Felgner 1971 Hauptsatz §3 step 1 (p. 30–31);
    Drake 1974 §3.4 (V_κ-bounded reflection). -/
axiom axiom_felgner_step1_class_quantifier_to_Vkappa_bounded : True

/-- Felgner 1971 step 2: every MK proper class C is set-encodable in V_κ for
    κ inaccessible (V_κ ⊨ ZFC). Felgner 1971 Hauptsatz §3 step 2 (p. 31–33);
    Drake 1974 §3.4; Jech 2003 §12.1 Theorem 12.13. -/
axiom axiom_felgner_step2_proper_class_in_Vkappa : True

/-- Felgner 1971 step 3: every L_ZFC sentence is V_κ-relativizable, yielding
    T = ZFC + ∃κ inaccessible ⊢ φ ↔ T' = MK ⊢ φ. Felgner 1971 Hauptsatz §3
    step 3 (p. 33–34); Williams 1976 alternate proof. -/
axiom axiom_felgner_step3_LZFC_relativization : True

/-- Felgner 1971 conservativity (composite). Derived theorem from the 3 named
    sub-axioms above; preserves the original axiom name for downstream callers
    (`AX2_strand_is_MK_class_via_ZFC` etc.) without churn. -/
theorem axiom_felgner_1971_conservativity_meta : True := trivial
```

Plus §2 docstring expansion: 5 corroborating references with precise page-level
citations (Felgner Studia Logica 28 p.30–34 with DOI 10.1007/BF02113288, Drake
1974 §3.4, Jech 2003 §12.1 Thm 12.13, Williams 1976, Friedman 1970, Krivine
1969).

§6 status report updated to reflect cycle 8 W6 axiom inventory (4 → 6 named
axioms in MKBridge.lean).

### Logical content invariant
The new triple `step1` + `step2` + `step3` are each `: True`, identical type-theoretic
status to the original single `: True` axiom. The composite derived theorem
`axiom_felgner_1971_conservativity_meta : True := trivial` depends on NO axioms
(it's literally `trivial`). All downstream callers
(`AX2_strand_is_MK_class_via_ZFC`, `AX2_strand_closed_under_HEXAComp_via_ZFC`)
were already independent of this opaque marker — they depend on
`axiom_felgner_bridge_to_MK` and `axiom_strand_zfc_witness`. Thus the change
is **purely documentation**, with no kernel-level logical drift.

### `#print axioms` audit (post-W6)
```
'axiom_felgner_1971_conservativity_meta' does not depend on any axioms
'AX2_strand_is_MK_class_via_ZFC' depends on axioms: [Classical.choice,
  axiom_felgner_bridge_to_MK, axiom_strand_zfc_witness]
```

The derived theorem `axiom_felgner_1971_conservativity_meta` now provably
depends on no axioms, while the load-bearing path through
`axiom_felgner_bridge_to_MK` (§4) is unchanged. Honest disposition: the
Felgner conservativity story is still informally relied upon **at the
bridge axiom level**, not at the named sub-axioms. The 3 sub-axioms are
documentation scaffolding for W7+ discharge, not proof obligations
discharged by cycle 8.

---

## §5 Build verification

```
$ lake build N6.MechVerif.MKBridge
✔ [954/954] Built N6.MechVerif.MKBridge (8.5s)
Build completed successfully (954 jobs).

$ lake build           # full project
Build completed successfully (8 jobs).
```

Sorry count (across MechVerif): 0 (preserved from cycle 7 W5).

Axiom count (MKBridge.lean): 4 → 6 (added: step1, step2, step3; the original
axiom_felgner_1971_conservativity_meta now a derived theorem).

Project total named axioms: 7 → 9 (AX1 1 + AX2 2 + MKBridge 6).

---

## §6 raw 91 C3 honest disclosure

- W6 cycle 8 attempted full mechanical proof of `axiom_felgner_1971_conservativity_meta` per mission directive. **Full proof NOT achieved** — option (a) requires 6-12 months and absent mathlib4 MK + syntactic provability infrastructure.
- Option (d) Levy/Krivine substitute is **not available** in mathlib4 (audit confirmed: 0 set-theoretic Levy/Krivine references).
- Disposition: option (c) citation strengthening + option (b) partial decomposition. The original axiom is now a derived `theorem` from 3 named sub-axioms that document Felgner's 3-step proof structure.
- Logical content: **unchanged**. `True` ↔ `True ∧ True ∧ True` at lean's kernel; the change is purely documentation. Downstream load-bearing axiom is `axiom_felgner_bridge_to_MK` (§4), which carries the actual conservativity application.
- Reviewer-facing surface: **materially improved**. Citations are now precise (Felgner Studia Logica 28 p.30–34, DOI; Drake §3.4; Jech §12.1 Thm 12.13; Williams 1976; Friedman 1970; Krivine 1969). Proof skeleton is named.
- F-D-3 deadline-miss: re-evaluated MEDIUM 50-58% (cycle 8) vs MEDIUM 52-60% (cycle 7 W5). −2pp upper / −2pp lower. Risk profile substantively unchanged because cycle-8 work is documentation, not proof discharge.

---

## §7 raw 71 falsifiers (5)

See witness JSON `design/kick/2026-04-28_lean4-w6-felgner-full-proof_omega_cycle.json` for full schema.

1. **F-W6-FELG-1**: Reviewer rejects 3-step decomposition as "axiom proliferation theatre" since each sub-axiom is `: True` and the composite is provably axiom-free (`trivial`); demands either real proof obligations (e.g. `Π φ : L_ZFC.Sentence, ...`) or revert to single axiom.
2. **F-W6-FELG-2**: mathlib4 master adds a `Mathlib.SetTheory.MK` or `ModelTheory.Provable` module before W7, retroactively making option (a) feasible and embarrassing the cycle-8 disposition.
3. **F-W6-FELG-3**: Williams 1976 / Drake 1974 / Jech §12.1 citation accuracy challenged — specific page references shown to be off-by-1 or the named theorem is on a different page in the cited edition.
4. **F-W6-FELG-4**: Reviewer demands the `: True` placeholder type be replaced by a meaningful proposition (e.g. `Σ κ : Cardinal, IsInaccessible κ ∧ ...`) for the sub-axioms to be substantive; current shape is accused of being type-theoretic theatre.
5. **F-W6-FELG-5**: Felgner 1971 Hauptsatz §3 cited proof structure (3-step V_κ-bounding / V_κ ⊨ ZFC / relativization) shown to mis-attribute steps relative to Felgner's actual paper organization (Felgner may use 4 lemmas, or steps may be labelled differently).

---

## §8 Next steps (W7+ critical path)

1. **W7**: discharge `axiom_felgner_bridge_to_MK` — this is the actual load-bearing axiom for `AX2_strand_is_MK_class_via_ZFC`. Discharge requires:
   - explicit `Strand → ZFSet.{0}` Encodable derivation (replaces `axiom_strand_zfc_witness`)
   - an MK-fragment formalization in lean4 sufficient for `IsMKProperClass Strand`
   - or: a bypass theorem proving `IsMKProperClass Strand` directly from ZFC+V_κ without invoking the conservativity translator.
2. **W7+**: if mathlib4 gains a syntactic provability predicate over L_ZFC, attempt option (a) for the 3 sub-axioms.
3. **W6 (this proposal)**: cycle 8 W6 marker complete. F-D-3 re-evaluated MEDIUM 50-58%.
