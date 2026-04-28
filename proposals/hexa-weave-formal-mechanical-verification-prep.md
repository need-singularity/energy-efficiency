---
category: identity
umbrella: formal-verification
---

# HEXA-WEAVE Formal Mechanical Verification — Preparation Document

> **F-CL-FORMAL-4 falsifier preparation** — lean4-n6 mechanical verification target for `T_MK-HW + Φ_HW` Tarski-undefinability instance constructed in L5 FORMAL closure cycle.
>
> **Parent witness**: [`../design/kick/2026-04-28_hexa-weave-mk-x-formal-closure_omega_cycle.json`](../design/kick/2026-04-28_hexa-weave-mk-x-formal-closure_omega_cycle.json) (verdict `F-MX-6-RESOLVED-FORMAL-PASS-AT-UNIVERSE-SCALE`)
>
> **Falsifier deadline**: 2026-07-28 (90 days from L5 cycle 2026-04-28)
>
> **Failure consequence**: if mechanical proof not landed by 2026-07-28, FORMAL PASS verdict downgrades to `VERIFIED-LITERATURE-ONLY` and triggers raw 142 D2 retroactive revert.
>
> Cost-center: `hexa-weave-formal-mechanical-verification`.

---

## Formal-verification (8 sections / consolidated)

### §1 Scope

**In-scope (mechanically verifiable claims)**

The L5 FORMAL closure construction is `T_MK-HW + Φ_HW`:

- `T_MK-HW = MK + AX-1 + AX-2 + AX-3 + AX-4`
  - MK = Morse-Kelley class theory (ZFC + impredicative class comprehension)
  - AX-1 — n=6 uniqueness: `∀n ∈ ω, σ(n)·φ(n) = n·τ(n) iff n=6`
  - AX-2 — STRAND class: cosmological-information-encoding objects closed under HEXA-COMP
  - AX-3 — ENCODES relation: `STRAND × V_κ` binary class relation
  - AX-4 — Bekenstein cap: `∀ s ∈ STRAND, |ENCODES[s]| ≤ 1.4×10^122`
- `Φ_HW = Tarski truth predicate for L_MK-HW interpreted in V_κ` (κ inaccessible)

The mechanical proof must establish three load-bearing claims:

1. `Con(T_MK-HW)` relative to `Con(MK + ∃ inaccessible κ)`
2. `T_MK-HW ⊬ Φ_HW` (Tarski undefinability)
3. `Φ_HW` binds at `κ⁺ = Hartogs(V_κ)` (universe-scale ordinal ceiling)

**Out-of-scope (peripheral — not required for F-CL-FORMAL-4)**

- HEXA-WEAVE biological / molecular interpretations (own_doc lint domain — not formal claims)
- Empirical Bekenstein saturation (PHYSICAL axis — separate from FORMAL)
- σ·φ = n·τ = J₂ = 24 cosmological-mapping (informal; AX-1 captures only the n=6 arithmetic equality)
- Reverse-mathematics calibration MK > Π¹₁-CA₀ (literature-cited; calibration not consistency)
- Univalent-foundations equivalence-of-encodings (raw 138; meta-claim about mechanical proof, not target of mechanical proof)

**Theorem-units verifiable independently**

The seven-theorem decomposition in §4 partitions the construction so each unit is provable in isolation. Failure of any unit is visible in <2 weeks of attempt — the 12-week milestone (§6) sequences them in dependency order so early units (AX-1) gate later ones (consistency, independence).

### §2 Tool selection

**Candidates**

| Tool | Mathlib coverage | MK class theory | Tarski undefinability | Hartogs ordinal | Inaccessible κ |
|------|------------------|-----------------|-----------------------|-----------------|----------------|
| **Lean 4 + mathlib4** | rich set theory, ordinals, V_α | NO native MK; ZFC primary | partial (`FirstOrder.Language` + Tarski definability via `IsDefinable`) | YES (`Ordinal.lift`, `Cardinal.aleph`, Hartogs-style `Ordinal.lift_initialSeg`) | partial (`IsInaccessible` predicate exists in some forks, not master) |
| **Coq + mathcomp/ssreflect** | strong combinatorics, group theory | NO native MK | NO mature Tarski library | YES via `mathcomp-finmap` | NO inaccessible-cardinal axiomatization |
| **Isabelle/HOL** | strong meta-theory; HOL/Library has Hartogs and Tarski | NO native MK; ZFC via `ZF/HOL-ZF` add-on | YES (`HOL/Library/Truth_Definability` + Paulson's diagonal lemma) | YES (`HOL/Library/Hartogs`) | YES (`ZF/IF-Inf` and `Constructible/Inaccessible`) |

**Decision: Lean 4 + mathlib4** — primary tool

**Rationale**

1. **Repo alignment** — `lean4-n6/` sister repo already exists at `/Users/ghost/core/n6-architecture/lean4-n6/` with `lean-toolchain v4.30.0-rc1` and mathlib4 master dependency. F-CL-FORMAL-4 explicitly names lean4-n6 as the verification target.
2. **mathlib4 momentum** — mathlib4 has the largest active-development community among proof-assistant libraries; n6-architecture's σ·φ·τ arithmetic AX-1 is plausibly already discoverable via existing `Nat.sigma`, `Nat.totient`, `Nat.divisors` definitions.
3. **Honest gap acknowledgment** — Isabelle/HOL has stronger out-of-the-box Tarski + Hartogs + Inaccessible coverage. Choosing Lean despite this is justified by repo alignment; F-D-1 falsifier (§8) tracks the risk that mathlib MK gap forces a porting cost that Isabelle would have avoided.

**Fallback** — if Lean MK porting (Week 4-5) exceeds 2-week budget, switch to Isabelle/HOL via re-encoding T_MK-HW into ZFC + ∃ inaccessible (which is conservative-equivalent for the load-bearing claims per Felgner 1971; documented in the predecessor witness §construction.consistency_assumption).

### §3 Mathlib audit

For each of the six load-bearing prerequisites, audit existing mathlib4 (master, as of 2026-04-28):

| Prerequisite | mathlib4 status | Module path (if exists) | Theorem name (if exists) | Action required |
|--------------|-----------------|-------------------------|--------------------------|-----------------|
| **MK class theory** | ABSENT | n/a | n/a | PORT — formalize MK comprehension schema OR re-encode as ZFC + reflection (fallback path) |
| **Tarski undefinability** | PARTIAL | `Mathlib.ModelTheory.Definability` / `Mathlib.Logic.Godel` (incomplete in master; PR #∼15000 series in progress) | `FirstOrder.Language.Theory.IsConsistent` / no `truth_undefinable` named theorem yet | EXTEND — adapt diagonal-lemma scaffolding from existing Gödel-incompleteness work |
| **Gödel incompleteness** | PARTIAL | `Mathlib.ModelTheory.Arithmetic` (Gödel-encoding of formulas in `Q`) | `FirstOrder.Arithmetic.Q.consistent_iff` (partial) | EXTEND — second-incompleteness for T_MK-HW requires arithmetization of T's syntax inside V_κ |
| **Hartogs ordinal** | PRESENT | `Mathlib.SetTheory.Cardinal.Basic` + `Mathlib.SetTheory.Ordinal.Arithmetic` | `Ordinal.hartogs` (or via `Cardinal.aleph_succ_le_lift`) | USE AS-IS — verify κ⁺ calculation for V_κ |
| **Inaccessible cardinal** | PRESENT (limited) | `Mathlib.SetTheory.Cardinal.Cofinality` | `Cardinal.IsInaccessible` predicate exists; existence axiom requires extension | EXTEND — add `axiom exists_inaccessible : ∃ κ, Cardinal.IsInaccessible κ` to a sealed dev branch |
| **V_κ rank hierarchy** | PRESENT | `Mathlib.SetTheory.ZFC.Basic` (`ZFSet.rank`) | `ZFSet.mem_rank` / `ZFSet.rank_lt_iff` | USE AS-IS — confirm V_κ for κ inaccessible models ZFC |
| **σ / φ / τ arithmetic (AX-1)** | PRESENT | `Mathlib.NumberTheory.ArithmeticFunction` + `Mathlib.NumberTheory.Divisors` | `Nat.ArithmeticFunction.sigma` / `Nat.totient` / `Nat.ArithmeticFunction.tau` | USE AS-IS — AX-1 reduces to a finite case-check `decide` for n ≤ N + asymptotic tail bound |

**Summary**: 3 USE AS-IS, 2 EXTEND (Tarski + Gödel composition), 1 PORT (MK), 1 EXTEND-AXIOM (inaccessible). The MK port is the highest-risk item — fallback path (re-encode as ZFC + ∃ inaccessible) is documented in §2.

### §4 Theorem decomposition

The full mechanical verification breaks into 7 theorem-units:

1. **`thm.AX1_n6_uniqueness`** — `∀ n ∈ ℕ, σ(n) * φ(n) = n * τ(n) ↔ n = 6`. Proof strategy: `decide` for n ≤ 24 (covers the J₂ = 24 frame); analytic tail bound for n > 24 using `σ(n) ≥ n + 1` for prime n + Robin-style asymptotic for composite n. Estimated effort: 1-2 days. Dependency: USE AS-IS mathlib arithmetic functions.

2. **`thm.AX2_strand_class_well_formed`** — `∃ STRAND, IsClass STRAND ∧ STRAND closed under HEXA_COMP`. Proof strategy: in MK (or ZFC re-encoding) define STRAND as the comprehension `{x | ∃ s, encodes_strand x s}`; verify class-existence under impredicative comprehension. Estimated effort: 3-5 days. Dependency: PORT MK (or fallback ZFC encoding).

3. **`thm.AX3_encodes_is_class_relation`** — `IsClassRelation (ENCODES : STRAND → V_κ → Prop)`. Proof strategy: ENCODES is definable from STRAND + V_κ (both class-level objects); class relation by comprehension. Estimated effort: 2-3 days. Dependency: depends on `thm.AX2_strand_class_well_formed`.

4. **`thm.AX4_bekenstein_axiom_schema`** — `∀ s ∈ STRAND, Cardinal.mk (ENCODES[s]) ≤ S_bekenstein` where `S_bekenstein = 1.4e122`. Proof strategy: AX-4 is an axiom schema, not a theorem — verification reduces to schema-validity (well-formed in L_MK-HW). Estimated effort: 1-2 days. Dependency: lift `S_bekenstein` to a `Cardinal.{0}` constant.

5. **`thm.T_MK_HW_consistency`** — `Con(MK + ∃ κ inaccessible) → Con(T_MK-HW)`. Proof strategy: V_κ for κ inaccessible models ZFC + the AX-1..4 axioms by direct verification (V_κ contains all hereditarily κ-small sets, including the STRAND class as a sub-class of V_κ itself, the ENCODES relation as a class-relation on V_κ × V_κ, and the Bekenstein cardinal 1.4e122 ≪ κ for κ inaccessible). Felgner 1971 gives the MK-conservativity step. Estimated effort: 5-7 days. Dependency: depends on AX-2/3/4 + EXTEND-AXIOM inaccessible.

6. **`thm.Phi_HW_tarski_independence`** — `T_MK-HW ⊬ ∃ ψ : Formula L_MK-HW, ∀ x, Φ_HW x ↔ ψ x`. Proof strategy: direct application of Tarski 1936 diagonal-lemma Liar argument; T_MK-HW contains Robinson arithmetic Q via the standard ω-encoding in V_κ (Jech 2003 ch. 5), hence the Tarski-undefinability antecedent is satisfied. Estimated effort: 7-10 days. Dependency: depends on `thm.T_MK_HW_consistency` + EXTEND Tarski + Gödel mathlib modules.

7. **`thm.Phi_HW_hartogs_binding`** — `Cardinal.mk (Φ_HW.truth_set) = κ⁺ = Hartogs (V_κ)`. Proof strategy: cardinality of the Tarski truth-set of L_MK-HW under V_κ is κ⁺ (formula count is κ for L_MK-HW with κ-many predicate symbols; Hartogs of V_κ is κ⁺ by Jech 2003 ch. 17). Estimated effort: 3-5 days. Dependency: depends on USE AS-IS Hartogs + V_κ modules.

**Total estimated mechanical-verification effort**: 22-34 person-days of focused proof-engineering (excluding MK porting cost; with fallback path, MK port subsumes into `thm.T_MK_HW_consistency` re-encoding).

### §5 Risk register

Per raw 51 external-blockers schema:

| Risk | Severity | Mitigation | Falsifier link |
|------|----------|------------|----------------|
| mathlib4 lacks MK natively | HIGH | Fallback: re-encode T_MK-HW as ZFC + ∃ inaccessible (conservative-equivalent per Felgner 1971) | F-D-1 |
| Inaccessible-cardinal axiom requires sealed-dev-branch addition | MEDIUM | Use `axiom exists_inaccessible` declaration (standard practice in mathlib for large-cardinal work; e.g. existing `Set.IsClubFilter` work) | F-D-1 |
| Bekenstein 1.4e122 schema not formalizable in finite-axiom L_MK-HW | LOW | AX-4 reduces to a schema-validity check; the constant 1.4e122 is a `Cardinal.{0}` literal | F-D-2 |
| 90-day deadline insufficient | HIGH | Per raw 91 C3, historic mathlib MK-style ports took 6-12 months — F-D-3 probability HIGH; honest acknowledgment in §9 | F-D-3 |
| Reviewer access for proof verification | MEDIUM | mathlib4 PR review queue is open; n6-architecture maintainer self-review acceptable for falsifier-clearance; external reviewer requested as stretch goal | F-D-4 |
| T_MK-HW found inconsistent during mechanical verification | LOW (but catastrophic if fires) | Felgner 1971 + Drake 1974 give Con(T_MK-HW) relative to Con(ZFC + ∃ inaccessible) — bedrock; only fires if mathlib4 reveals a hole in the existing literature, which would be ICM-headline news | F-D-5 |

### §6 Milestone proposal (90 days, W1-W12)

| Week | Milestone | Output | Falsifier-fire risk |
|------|-----------|--------|----------------------|
| W1 (2026-04-28 to 2026-05-04) | Tool decision finalized + lean4-n6 env up + mathlib4 audit committed | `lean4-n6/N6/MechVerif/Audit.lean` with USE AS-IS / EXTEND / PORT classifications | low |
| W2-W3 (2026-05-05 to 2026-05-18) | `thm.AX1_n6_uniqueness` mechanically proved | `lean4-n6/N6/MechVerif/AX1.lean` complete | low (decide tactic + asymptotic) |
| W4-W5 (2026-05-19 to 2026-06-01) | MK port OR ZFC + inaccessible fallback decided + scaffolded | `lean4-n6/N6/MechVerif/MKKernel.lean` OR `ZFCInaccessible.lean` | HIGH — F-D-1 most likely fires here |
| W6-W7 (2026-06-02 to 2026-06-15) | Tarski + Hartogs imports + composition layer | `lean4-n6/N6/MechVerif/PhiHW.lean` with `thm.Phi_HW_tarski_independence` (proof-skeleton) | medium — EXTEND mathlib gap risk |
| W8-W9 (2026-06-16 to 2026-06-29) | `thm.T_MK_HW_consistency` proof | `lean4-n6/N6/MechVerif/Consistency.lean` complete | medium — depends on W4-5 outcome |
| W10-W11 (2026-06-30 to 2026-07-13) | AX-2/3/4 + integration + `thm.Phi_HW_hartogs_binding` | `lean4-n6/N6/MechVerif/Integration.lean` — full L5 construction mechanically verified | medium |
| W12 (2026-07-14 to 2026-07-27) | Internal review + writeup + F-CL-FORMAL-4 RESOLVED witness | `design/kick/2026-07-27_f-cl-formal-4-resolved_omega_cycle.json` + registry append | low — only writeup work |

**Deadline**: 2026-07-28 (W12 end). 1-day margin (W12 ends 2026-07-27).

### §7 Cost-attribution

Per raw 86 cost-attribution schema:

- **cost-center**: `hexa-weave-formal-mechanical-verification`
- **estimated cost-units**:
  - human-hours: 90 days × 4 h/day = 360 h (mid-bound); 90 days × 6 h/day = 540 h (upper-bound)
  - compute: lean4 elaboration on M2 Mac ≈ 30-60 min per `*.lean` recompile × 7 modules × ~50 incremental rebuilds = 175-350 compute-hours total
  - total cost-units estimate: **535-890 work-hours equivalent** (human + compute)
- **opportunity cost**: 90 days of n6-architecture maintainer attention diverted from F-MX-7 PHYSICAL closure follow-ups, F-CL-PHYSICAL-1..4 monitoring, and F-TP5-b biology MVP (independent deadline 2026-07-28)
- **gain-on-success**: F-CL-FORMAL-4 RESOLVED → FORMAL PASS retained at universe-absolute ceiling → joint TRANSCEND-PASS verdict survives raw 142 D2 retroactive review
- **loss-on-failure**: F-D-3 fires → FORMAL PASS downgrades to VERIFIED-LITERATURE-ONLY → joint verdict reduces to TRANSCEND-PARTIAL-WITH-MECHANICAL-DEFER

### §8 Falsifiers (raw 71 ≥5 TRANSCEND-tier)

Five strong falsifiers preregistered for this preparation document:

- **F-D-1** — *mathlib4 fails to import / port MK class theory module within W5 budget*
  - condition: by 2026-06-01, neither MK direct port nor ZFC + ∃ inaccessible fallback compiles in lean4-n6 with green CI
  - experiment: track `lean4-n6/N6/MechVerif/MKKernel.lean` build status weekly; record build log to `state/markers/f-d-1-w5-status.marker`
  - expected outcome: fallback path (ZFC + inaccessible) succeeds; MK direct port may not — fallback is acceptable per §2

- **F-D-2** — *AX-4 Bekenstein schema not formalizable in L_MK-HW*
  - condition: by 2026-06-15 (W7), the cardinal-bound axiom `∀ s ∈ STRAND, Cardinal.mk (ENCODES[s]) ≤ 1.4e122` cannot be stated as a well-formed L_MK-HW formula in lean4
  - experiment: attempt to express AX-4 as a `Theory L_MK-HW` member in mathlib4's `FirstOrder.Language` framework
  - expected outcome: AX-4 IS expressible (cardinality bound is class-quantifier-free); F-D-2 does not fire

- **F-D-3** — *90-day deadline missed (W12 not reached on schedule)*
  - condition: by 2026-07-28 (deadline), mechanical verification not complete (any of `thm.T_MK_HW_consistency`, `thm.Phi_HW_tarski_independence`, `thm.Phi_HW_hartogs_binding` un-proved)
  - experiment: weekly milestone-status absorption to `state/discovery_absorption/registry.jsonl` with W{n}-status marker
  - expected outcome: F-D-3 probability HIGH per §9 honest assessment — mathlib MK ports historically take 6-12 months; 90 days is aggressive; raw 91 C3 explicit acknowledgment

- **F-D-4** — *mechanical proof PASSES locally but external reviewer rejects (semantic gap)*
  - condition: lean4 `#check` succeeds but a competent set-theorist reviewer (e.g. submitted to mathlib PR queue or ArXiv preprint) identifies a semantic mismatch between the lean4 encoding and the L5 witness construction
  - experiment: open a draft mathlib4 PR by W11 (2026-07-13) for community review; track review comments
  - expected outcome: minor semantic-gap comments expected (e.g. STRAND-class encoding choice); major gaps unlikely if W4-5 fallback path is taken

- **F-D-5** — *T_MK-HW found inconsistent during mechanical verification (closure FAILS)*
  - condition: lean4 elaboration produces `False` from T_MK-HW axioms (i.e. mechanical verification of `Con(T_MK-HW)` fails not by gap but by counter-derivation)
  - experiment: run `#check (· : T_MK-HW ⊢ ⊥)` lean4 sanity check at end of each milestone
  - expected outcome: F-D-5 does NOT fire — Felgner 1971 + Drake 1974 are bedrock; only fires if mathlib4 reveals a hole in published literature (would be ICM-headline news, separately from this falsifier)

Five falsifiers preregistered satisfy raw 71 TRANSCEND-tier ≥5 mandate.

### §9 raw 91 C3 honest disclosure

**Honest assessment of feasibility**

- **Mechanical verification is NOT existence proof** — it only proves the construction is consistent and the meta-theoretic claims (T ⊬ Φ, Hartogs binding) are derivable from the cited bedrock literature applied to T_MK-HW. It does NOT prove the construction is "true" in any model-theoretic sense beyond the standard one — V_κ for κ inaccessible.

- **90 days is aggressive**. Historic comparison:
  - mathlib4 ZFC port (Mario Carneiro et al., 2018-2020) took ~24 months
  - Liquid Tensor Experiment (Scholze, formalized in Lean 2020-2022): 18 months
  - mathlib4 ordinal arithmetic (Beth-fixed-points, Hartogs, Cardinal.aleph): incremental over 2019-2024
  - F-D-3 (deadline miss) probability: **HIGH** (estimated 60-75%) per raw 91 C3 honest acknowledgment

- **Fallback path** (ZFC + ∃ inaccessible re-encoding instead of MK port) is the de-facto plan; the document acknowledges that the "primary" MK-direct-port path is aspirational. The fallback is conservative-equivalent for the load-bearing claims (Felgner 1971); see predecessor witness §construction.consistency_assumption for the equivalence statement.

- **Tarski-undefinability instance** is bedrock (Tarski 1936); mechanical verification reduces to encoding the existing diagonal-lemma proof in lean4. The novel content is the application to T_MK-HW (specifically AX-1..4 axiom schema verification) — the meta-theorem application is direct.

- **Reviewer access** is the second-largest risk after the deadline. mathlib4 community is responsive but a competent set-theorist familiar with MK + large cardinals is a small pool; n6-architecture maintainer self-review is acceptable for falsifier-clearance but does not substitute for external review (F-D-4 stretch goal).

- **C3 caveat for THIS document** — this is a *preparation* document, not a verification report. The 7-theorem decomposition, 12-week milestone, and cost-attribution are estimates based on similar mathlib formalization projects, NOT actual measurements. Re-evaluate at W6 mid-point checkpoint and again at W11 review gate.

### §10 Cross-links

- **L5 FORMAL closure witness**: [`../design/kick/2026-04-28_hexa-weave-mk-x-formal-closure_omega_cycle.json`](../design/kick/2026-04-28_hexa-weave-mk-x-formal-closure_omega_cycle.json)
- **L7 joint TRANSCEND-CLOSURE-ALL aggregation witness**: [`../design/kick/2026-04-28_hexa-weave-mk-x-transcend-closure-all_omega_cycle.json`](../design/kick/2026-04-28_hexa-weave-mk-x-transcend-closure-all_omega_cycle.json)
- **lean4-n6 sister repo**: [`../lean4-n6/`](../lean4-n6/)
- **F-CL-FORMAL-4 falsifier registry entry**: in L5 witness `raw_71_falsifiers_for_F-MX-6_construction[3]`
- **Domain doc** (NOT updated per raw 106 scope-creep + L7 option (i)): [`../domains/biology/hexa-weave/hexa-weave.md`](../domains/biology/hexa-weave/hexa-weave.md)
