---
category: operational
umbrella: formal-verification
parent_spec: proposals/hexa-weave-formal-mechanical-verification-prep.md
w1_completed: true
w1_completed_at: 2026-04-28
---

# HEXA-WEAVE MVP — W1 lean4 + mathlib4 Audit

> **W1 deliverable** for `proposals/hexa-weave-formal-mechanical-verification-prep.md` Task D Spec §3.
>
> **Date**: 2026-04-28 (early start; W1 nominal window 2026-04-28 → 2026-05-04).
>
> **Audit basis**: mathlib4 master @ rev `19c497800a418208f973be74c9f5c5901aac2f54` (pinned via `lean4-n6/lake-manifest.json`).
>
> **Auditor scope**: grep-based source inspection only; no `lake build` re-run, no `#check` evaluation.

---

## §1 Environment status

| Component | Status | Version | Path |
|-----------|--------|---------|------|
| `elan` | INSTALLED | 4.2.1 | `/opt/homebrew/bin/elan` |
| `lean` | INSTALLED | 4.30.0-rc1 (arm64-apple-darwin24.6.0) | `/opt/homebrew/bin/lean` |
| toolchain match | YES | matches Task D Spec §2 | `lean4-n6/lean-toolchain` declares `leanprover/lean4:v4.30.0-rc1` |
| `lean4-n6` sister repo | EXISTS | `/Users/ghost/core/n6-architecture/lean4-n6/` | NOT at `~/core/lean4-n6/` (Spec §2 wording is technically correct: relative `../lean4-n6/` from `proposals/`) |
| mathlib4 source | PRESENT | rev `19c497800a418208f973be74c9f5c5901aac2f54` | `lean4-n6/.lake/packages/mathlib/Mathlib/` |
| supporting packages | PRESENT | plausible, LeanSearchClient, importGraph, ProofWidgets4, aesop, batteries, Cli, Qq | `lean4-n6/.lake/packages/` |

**No installation actions taken** — environment was already complete before W1 started. Per safety guard, `elan` install and `lean4-n6` `lake update` were NOT executed without user authorization; both turned out to be unnecessary.

---

## §2 Existing `lean4-n6` content (relevant to W1)

`lean4-n6/N6/` contains:

- `Basic.lean`, `MathlibBasic.lean`, `Verification.lean`
- `TheoremB_Capstone.lean` + 30+ `TheoremB_Case*.lean` shards (existing AX-1-related case-split work; not reviewed in this audit)

`Main.lean` already prints `σ(6), φ(6), τ(6), σ·φ, n·τ` and acknowledges Theorem B full proof carries `sorry` under Mathlib v4. AX-1 `decide` work appears partially staged.

No `MechVerif/` directory exists yet. W1 milestone does NOT require it (W1 produces audit only; W2 starts AX-1 mechanization in `MechVerif/AX1.lean`).

---

## §3 Mathlib4 7-theorem audit

| # | Prerequisite | Status | Module path | Theorem / def name | Statement form | Action |
|---|--------------|--------|-------------|--------------------|----------------|--------|
| 1 | **Hartogs ordinal** | INDIRECT | `Mathlib/SetTheory/Cardinal/Aleph.lean` (and `Cardinal/Basic.lean`) | NO `Ordinal.hartogs` symbol; surrogate via `Order.succ` on `Cardinal` (`succ_aleph`, `aleph_succ`) | `theorem aleph_succ (o : Ordinal) : ℵ_ (succ o) = succ (ℵ_ o)` | USE-AS-IS w/ rename: `κ⁺ := Order.succ κ` for `(κ : Cardinal)`. Spec §3 reference to `Ordinal.hartogs` is INACCURATE — no such named symbol exists in master rev. |
| 2 | **V_κ rank hierarchy** | PRESENT | `Mathlib/SetTheory/ZFC/VonNeumann.lean` (V_o), `Mathlib/SetTheory/ZFC/Rank.lean` (rank) | `noncomputable def vonNeumann (o : Ordinal) : ZFSet := …` (notation `V_ o`); `noncomputable def ZFSet.rank : ZFSet → Ordinal` | `V_ o = ⋃ a < o, powerset (V_ a)` | USE-AS-IS. Note: Spec §3 cites `Mathlib.SetTheory.ZFC.Basic` for ranking — actual rank lives in `ZFC/Rank.lean`, V_κ lives in `ZFC/VonNeumann.lean`. Add to spec corrigendum. |
| 3 | **σ / φ / τ arithmetic functions** | PRESENT | `Mathlib/NumberTheory/ArithmeticFunction/Misc.lean` (sigma); `Mathlib/Data/Nat/Totient.lean` (totient) | `def sigma (k : ℕ) : ArithmeticFunction ℕ` (notation `σ`); `def Nat.totient (n : ℕ) : ℕ`; **NO standalone `tau`** — encoded as `σ 0 n = #n.divisors` (`sigma_zero_apply`) | `theorem sigma_zero_apply (n : ℕ) : σ 0 n = #n.divisors` | USE-AS-IS. AX-1 statement should be `σ 1 n * Nat.totient n = n * σ 0 n ↔ n = 6`. Note: Spec §3 mentions `Nat.ArithmeticFunction.tau`; that path does NOT exist — use `ArithmeticFunction.sigma 0`. |
| 4 | **Tarski undefinability** | PARTIAL | `Mathlib/ModelTheory/Definability.lean` + `Mathlib/ModelTheory/Encoding.lean` + `Mathlib/ModelTheory/ElementaryMaps.lean` | `Set.Definable`, `Set.Definable₁/₂`, `FirstOrder.Language.DefinableSet`; `Tarski-Vaught Test` (substructure elementarity, NOT truth-undefinability); NO named `truth_undefinable` theorem | `Set.Definable L A s : Prop` (def); `Tarski-Vaught Test` (lemma in `ElementaryMaps.lean:245`) | EXTEND. The "Tarski" hits in master refer to Tarski-Vaught test for elementary substructures, NOT Tarski's 1936 truth-undefinability result. Diagonal-lemma scaffolding must be built on top of `ModelTheory/Encoding.lean` `BoundedFormula.encoding` + `card_le`. |
| 5 | **Gödel incompleteness** | PARTIAL (β-function only) | `Mathlib/Logic/Godel/GodelBetaFunction.lean` | `Nat.beta`, `Nat.unbeta` (β-function for arithmetization of finite-sequence quantification) | provides `Nat.beta` lemmas only; First Incompleteness theorem itself NOT stated | EXTEND. Spec §3 reference to `Mathlib.ModelTheory.Arithmetic` `Q.consistent_iff` does NOT exist in master (`ModelTheory/Arithmetic/` only contains `Presburger/`). Foundations exist (β-function + Chinese remainder + `ModelTheory/Encoding`) but composition into First/Second Incompleteness is NOT present. |
| 6 | **Inaccessible cardinal** | PRESENT (predicate); ABSENT (existence axiom) | `Mathlib/SetTheory/Cardinal/Regular.lean` | `structure IsInaccessible (c : Cardinal) : Prop where (aleph0_lt : ℵ₀ < c) (isRegular : IsRegular c) (isStrongLimit : IsStrongLimit c)`; theorem `IsInaccessible.univ : IsInaccessible univ.{u, v}` | `theorem isInaccessible_def : IsInaccessible c ↔ ℵ₀ < c ∧ IsRegular c ∧ IsStrongLimit c` | USE-AS-IS for predicate; ADD `axiom exists_inaccessible : ∃ κ : Cardinal, Cardinal.IsInaccessible κ` to sealed dev branch. Note: `IsInaccessible.univ` proves the *universe* cardinal is inaccessible — this is a Lean foundations fact, not the Tarski-Grothendieck axiom; it does NOT supply `∃ κ ∈ V, IsInaccessible κ` (which is what AX-3..4 + κ⁺ Hartogs require). |
| 7 | **Morse-Kelley class theory** | ABSENT | n/a | n/a (no `MK`, `MorseKelley`, `NBG`, `vonNeumann.Bernays.Gödel` symbols anywhere in mathlib4 master) | n/a | PORT (high risk) OR fallback to ZFC-encoding via `Mathlib/SetTheory/ZFC/Class.lean` (`Class := Set ZFSet`). The fallback path (Spec §2) is enabled: `ZFC/Class.lean` provides `Class.iota` and proper-class machinery sufficient to encode T_MK-HW under MK-conservativity (Felgner 1971). |

### §3.1 Summary distribution

- **USE-AS-IS**: 3 (V_κ rank, σ/φ/τ via `sigma 0`, IsInaccessible predicate)
- **USE-AS-IS w/ rename**: 1 (Hartogs → `Order.succ` on Cardinal)
- **EXTEND**: 2 (Tarski undefinability, Gödel First/Second incompleteness — both require composition of existing foundations)
- **EXTEND-AXIOM**: 1 (`axiom exists_inaccessible` to sealed branch)
- **PORT or FALLBACK**: 1 (MK class theory; fallback via `ZFC.Class` available)

### §3.2 Corrigenda to Task D Spec §3

The following Spec §3 module-path references are **inaccurate** vs. mathlib4 master rev `19c497…`:

1. `Ordinal.hartogs` — does NOT exist; use `Order.succ : Cardinal → Cardinal` instead.
2. `Mathlib.SetTheory.ZFC.Basic` rank — actual location is `Mathlib.SetTheory.ZFC.Rank.lean` and `Mathlib.SetTheory.ZFC.VonNeumann.lean`.
3. `Mathlib.NumberTheory.ArithmeticFunction.tau` — no standalone `tau`; use `ArithmeticFunction.sigma 0`.
4. `Mathlib.ModelTheory.Arithmetic Q.consistent_iff` — `ModelTheory/Arithmetic/` only has `Presburger/`; Q-arithmetic / consistency lemma absent.
5. `Mathlib.Logic.Incomplete` — does NOT exist; only `Logic/Godel/GodelBetaFunction.lean`.
6. `IsInaccessible.univ` — exists, but does NOT supply an in-V inaccessible (Lean's universe inaccessibility is meta, not object-level).

These corrections do NOT invalidate the §3 audit conclusions — the EXTEND / PORT / USE-AS-IS classifications hold; only the citations are tightened. Task D Spec §9 C3 caveat already noted estimates not measurements; this audit converts §3 from estimate to measurement.

---

## §4 F-D-3 (90-day deadline) re-evaluation

Spec §9 set F-D-3 probability HIGH (60-75%). After W1 audit:

- **Reduces F-D-3 risk** (modestly):
  - Environment is fully ready (lean4 + mathlib4 + lean4-n6 sister repo present). Saves ~3-7 days of W1 nominal budget.
  - W1 starting on Day 0 of the 90-day window (vs. Day 7) buys 1 week safety margin.
  - 3 of 7 prerequisites are USE-AS-IS without modification.
- **Increases F-D-3 risk**:
  - Spec §3 had 6 incorrect module-path references; this means the Spec authoring relied on stale or imagined mathlib structure. The 22-34 person-day estimate in Spec §4 was anchored to those (incorrect) citations and may be optimistic by ~15-25%.
  - Tarski undefinability + Gödel First/Second incompleteness COMPOSITION is more work than Spec §3 implied: mathlib has `Nat.beta` foundations only, NOT `Q.consistent_iff`. The diagonal-lemma + arithmetization layer must be built ground-up from `ModelTheory/Encoding.lean` + `Logic/Godel/GodelBetaFunction.lean`.
- **Net F-D-3 re-estimate**: **HIGH 65-75%** (was 60-75%). Lower bound moves up from 60% → 65% reflecting the Tarski/Gödel composition gap; upper bound unchanged. Spec §9 honest-disclosure language remains valid.

**Mitigation strengthened**: Fallback path (ZFC + `axiom exists_inaccessible` + `Class := Set ZFSet`) becomes the de-facto primary path; MK-direct-port is now formally deprecated for W4-5.

---

## §5 Falsifiers (raw 71 ≥5 for this W1 audit)

Five strong falsifiers preregistered for **THIS W1 AUDIT** (separate from Spec §8 F-D-1..5):

- **F-W1-1** — *audit reports a USE-AS-IS theorem that does not actually compile in lean4-n6 N6/MechVerif/Audit.lean*
  - condition: by 2026-05-04 (W1 end), a stub `import Mathlib.SetTheory.Cardinal.Regular; #check @Cardinal.IsInaccessible` fails in lean4-n6
  - experiment: write `lean4-n6/N6/MechVerif/Audit.lean` with one `#check` per USE-AS-IS prerequisite; run `lake build N6.MechVerif.Audit`
  - expected outcome: F-W1-1 does NOT fire — all 4 USE-AS-IS items are vanilla mathlib symbols

- **F-W1-2** — *Spec §3 corrigenda list misses an additional inaccuracy that surfaces in W2*
  - condition: during W2 AX-1 work, a NEW Spec §3 path-reference error emerges (e.g. `decide` performance pathology, missing `Coprime` lemma)
  - experiment: track W2 build log; cross-reference any FAIL against this audit's §3.2 corrigenda
  - expected outcome: F-W1-2 may fire on minor lemma names (low severity); no major missing-module inaccuracy expected since this audit grep'd 100% of cited modules

- **F-W1-3** — *Hartogs `Order.succ` surrogate does NOT match the Spec §1 κ⁺ semantics*
  - condition: `Order.succ (κ : Cardinal)` for `κ` inaccessible is NOT equal to `Hartogs(V_κ)` in the sense Spec §1 intends
  - experiment: prove `(Order.succ κ).ord = Hartogs (V_κ)` lemma in `lean4-n6/N6/MechVerif/PhiHW.lean` (W7)
  - expected outcome: F-W1-3 does NOT fire; classical result Hartogs(V_κ) = κ⁺ for κ inaccessible (Jech 2003 ch. 17), and Cardinal succ on initial ordinal coincides

- **F-W1-4** — *`IsInaccessible.univ` is sufficient for Spec §1 κ purposes (and `axiom exists_inaccessible` is unnecessary)*
  - condition: lean4 universe-level inaccessibility (`IsInaccessible.univ`) admits internal-to-V_κ mechanical use without adding a new axiom
  - experiment: attempt to derive `∃ κ : Cardinal.{0}, IsInaccessible κ` from `IsInaccessible.univ.{0,1}` in W4
  - expected outcome: F-W1-4 FIRES negative — Lean's universe-level inaccessibility is meta and CANNOT be internalized to `Cardinal.{0}` without Tarski-Grothendieck-style axiom; `axiom exists_inaccessible` remains required

- **F-W1-5** — *MK-fallback via `Class := Set ZFSet` is too weak for AX-2 STRAND class comprehension*
  - condition: encoding STRAND as `Class := Set ZFSet` cannot accommodate impredicative class comprehension required by `T_MK-HW` AX-2
  - experiment: in W4, attempt to express `STRAND := {x : ZFSet | ∃ s, encodes_strand x s}` via `Class.iota` + verify class-existence under impredicative quantifier
  - expected outcome: F-W1-5 may fire (medium severity) — `Class.iota` is definite-description-only; impredicative comprehension may need `Classical.choice` + `Set ZFSet` lift; fallback-to-fallback: drop AX-2 to predicative ZFC + reflection schema

---

## §6 raw 91 C3 honest disclosure

- **Sandbox-permission caveat (HONEST)**: this audit is grep-only. NO `lake build` was invoked; NO `#check` was run against mathlib4. The "PRESENT / ABSENT" classifications are based on lexical presence of identifiers in `.lean` source — they do NOT verify (a) public-export status, (b) typeclass-resolution success at use-site, or (c) elaborator timeout behavior. F-W1-1 covers conversion of grep-evidence to `#check`-evidence in W1's residual budget.
- **No system mutation**: `elan` was NOT installed (already present); `lake update` was NOT invoked; `lake build` was NOT invoked; user authorization for any system change was not requested because no change was needed. If `lake update` becomes desirable to advance to a newer mathlib rev, **explicit user approval** is required before invocation.
- **Spec §3 estimate ⇒ measurement promotion is partial**: this audit confirms 3 USE-AS-IS items by source inspection, but the "Tarski extends" and "Gödel extends" classifications still depend on engineering judgment about how cleanly `Nat.beta` + `BoundedFormula.encoding` compose into a diagonal lemma. The 22-34 person-day Spec §4 estimate is NOT promoted to measurement until W6-W7 yields a working `thm.Phi_HW_tarski_independence` proof skeleton.
- **Spec §3 inaccuracies disclosed**: 6 incorrect module-path references in the parent Spec §3 are flagged in §3.2. This is a quality concern about the Spec authoring process; a Spec-revision pass on §3 should fold these corrections back. Recommended action: append a §3-bis corrigendum to `proposals/hexa-weave-formal-mechanical-verification-prep.md` cross-linking this audit.
- **F-D-3 reassessment NOT a green light**: even with W1 environment-already-ready savings, F-D-3 remains HIGH (65-75%). The Spec §9 raw 91 C3 honest acknowledgment ("90 days is aggressive") still holds. Plan-for-failure path: at W6 mid-point checkpoint, if `thm.AX1_n6_uniqueness` + MK-fallback scaffolding are NOT both green-CI, escalate to either Isabelle/HOL pivot (Spec §2) or 90-day-extension request (raw 142 D2 retroactive defer).

---

## §7 Cross-links

- **Parent Spec**: [`hexa-weave-formal-mechanical-verification-prep.md`](./hexa-weave-formal-mechanical-verification-prep.md)
- **W1 omega-cycle witness**: [`../design/kick/2026-04-28_hexa-weave-mvp-w1-lean4-audit_omega_cycle.json`](../design/kick/2026-04-28_hexa-weave-mvp-w1-lean4-audit_omega_cycle.json)
- **L5 FORMAL closure witness (parent)**: [`../design/kick/2026-04-28_hexa-weave-mk-x-formal-closure_omega_cycle.json`](../design/kick/2026-04-28_hexa-weave-mk-x-formal-closure_omega_cycle.json)
- **lean4-n6 sister repo**: [`../lean4-n6/`](../lean4-n6/)
- **Mathlib4 audited rev**: `19c497800a418208f973be74c9f5c5901aac2f54` (recorded in `lean4-n6/lake-manifest.json`)
- **F-CL-FORMAL-4 falsifier**: registry entry in L5 witness `raw_71_falsifiers_for_F-MX-6_construction[3]`
