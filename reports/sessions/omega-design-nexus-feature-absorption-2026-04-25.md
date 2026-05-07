---
id: omega-design-nexus-feature-absorption
date: 2026-04-25
scope: cross-repo absorption design (NOT executing absorption; READ-ONLY on nexus)
target: 10 n6-session features -- absorption verdicts + design + deploy ranking
parent_reports:
  - reports/sessions/omega-deploy-nexus-honesty-triad-2026-04-25.md (honesty triad already deployed)
  - reports/sessions/omega-cycle-backtrace-strategy-2026-04-25.md
  - reports/sessions/omega-probe-l9-molt-trigger-2026-04-25.md
  - reports/sessions/omega-meta-audit-l9-catalogue-design-2026-04-25.md
millennium_resolved: 0/7 (unchanged)
nxs_promotion_count_delta: 0 (unchanged)
grade: cross-repo absorption design, no claim, no deployment
---

# Omega Design -- Nexus Feature Absorption (2026-04-25)

## §0 Non-claim disclaimer

This is a **design-only, read-only audit**. Concretely:

- ZERO files in `~/core/nexus/` are modified by this report. All
  references to nexus are read-only inspections (file paths, content
  excerpts, lens/tool inventory). The single output of this session is
  the present markdown file in `~/core/canon/reports/sessions/`.
- ZERO files in canon's `atlas/`, `state/`, `inventory/`,
  `theory/canon/`, or any L9/D1/D2/D3 source are modified.
- NO Millennium claim is made. The 10 features under audit include
  several that produced 0/4 FAIL verdicts on Millennium BTs (F-MOLT-A);
  audit of *generic-method* absorbability does not retract any FAIL.
- NO promotion is requested or executed. n6 atlas grade markers and
  nexus `state/proposals/inventory.json` `nxs_promotion_count` are
  unchanged.
- The 5 verdict labels {ABSORB, ABSORB_GAP, SKIP_LOW_LEVERAGE,
  SKIP_REDUNDANT, SKIP_INCOMPATIBLE} are the *only* verdicts used; no
  other classification leaks in.
- The "honesty triad" (already deployed at
  `~/core/nexus/design/honesty_triad.md`, 2026-04-25, present-and-read
  at this session start) is **excluded** from this audit's 10 features
  -- it is the prior session's deliverable and forms the deployment
  precedent that this report extends.

Millennium tally: **0/7 unchanged.**
nxs promotion count: **N/N0 unchanged** (no nexus inventory write).

---

## §1 Feature inventory (10 entries)

The 10 features generated during the canon 2026-04-25
session, beyond the 3 honesty-triad constraints already deployed:

| #  | Feature                                  | One-line description                                                                                            | Source artefacts                                                                                          |
|----|------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| 1  | Omega 4-axis framework                   | ladder L1..L_ω + Ω-saturation cycle + atlas omega chain + closure ceiling -- generic 4-axis applied to 7 BTs    | `omega-cycle-{bt541..bt547}-2026-04-25.md`, `nexus/design/abstraction_ceiling.md`                         |
| 2  | L9 molt-trigger framework                | 5-clause boolean gate + per-BT frame-shift catalogue + validation discriminators for L9 (engine-rewrite) entry  | `omega-probe-l9-molt-trigger-2026-04-25.md`, `omega-meta-audit-l9-catalogue-design-2026-04-25.md`         |
| 3  | Backward-chaining synthesis              | closure target -> chain gap -> ladder EMPTY rung -> root cause -> ROI probe ranking (top-down strategy)         | `omega-cycle-backtrace-strategy-2026-04-25.md`                                                            |
| 4  | F-MOLT meta-falsifier                    | F-MOLT-A (4 BT 0/4 PASS on the molt-validation criterion) + F-MOLT-D (catalogue exhaustion) self-falsification   | `omega-meta-audit-l9-catalogue-design-2026-04-25.md`, `omega-exec-bt54{1..6}-*-molt-validation-*.md`      |
| 5  | Seed-trial pattern (D1/D2/D3)            | exhaustion-recovery: D1 atlas-scan / D2 L_ω axiom-recast / D3 mechanism-decouple as 3 orthogonal recovery seeds | `omega-seed-bt544-d{1,2,3}-*-2026-04-25.md`, `omega-exec-bt544-d{1,2,3}-*-2026-04-25.md`                  |
| 6  | Discriminator-type bias diagnostic       | distributional/structural-import (PASS family) vs discrete-equality/numerical-interval/vacuous (FAIL family)    | `omega-meta-audit-discriminator-type-bias-2026-04-25.md`                                                  |
| 7  | Honesty-amendment protocol               | append-only scope-caveat block format for amending past reports without rewrites                                | `omega-amend-perbt-honesty-2026-04-25.md`                                                                 |
| 8  | Fabrication-refusal cascade              | when tool/data is absent, return UNKNOWN/INCONCLUSIVE/TIMEOUT *with diagnostic*; the diagnostic enables next step | `omega-audit-constraint-no-fabrication-2026-04-25.md`, `nexus/design/honesty_triad.md` (constraint #3)    |
| 9  | Cross-repo graph mismatch finding        | `nexus/n6/atlas.blowup.jsonl` (graph) ≠ `canon/atlas/atlas.n6` (canonical entries) -- separate objects | `nexus/design/next_session_handoff.md` §nxs-002 graph diagnostics; nexus 2026-04-25 update block          |
| 10 | Patched n6 tools (per-BT)                | `cremona_joint_covariance.py --per-stratum` (28-stratum), `bt541_leadB_sle6_gue.py`, `bt544_q1_molt_validation.py`, etc. | `tool/cremona_joint_covariance.py`, `tool/bt5{4*}_*.py`                                                   |

The 3 KEEP_AS_IS honesty-triad constraints (promotion-counter,
write-barrier, no-fabrication) are *not* in this list -- they were
deployed in a separate session and are the precedent for this audit.

---

## §2 Phase 1 -- Nexus-side analog scan

Read-only scan of `~/core/nexus/{design,lenses,tool,project-claude,state,docs,.claude/agents}`
for each feature. Verdict cell summary:
{PRESENT | PARTIAL | ABSENT | INCOMPATIBLE}.

### 2.1 Feature 1 -- Omega 4-axis framework

**Nexus-side analogs found:**

- `~/core/nexus/design/abstraction_ceiling.md` (485 lines, est.) -- the
  full L1..L_ω ladder definition + commands (`cmd_omega`, `cmd_surge`,
  `cmd_canon`, `cmd_forge`, `cmd_molt`, `cmd_wake`, `cmd_swarm`,
  `cmd_reign`, `cmd_dream`). This is the **canonical ladder source**.
  The n6 4-axis usage *applies* this ladder to BT diagnosis, but the
  ladder definition itself originates in nexus.
- `~/core/nexus/design/atlas_n6_omega_closure.md` -- already maps the
  ladder onto atlas.n6 entries (L1 smash entry-verify, L2 drill round,
  ..., L_ω apex). Section 3 + §5 are the closure ceiling tables.
- `~/core/nexus/state/proposals/inventory.json` -- `nxs-20260424-002`
  is the Ω-saturation cycle entry (composite 0.83379, ER-ROI mechanism,
  fixpoint marker `omega-saturation:fixpoint`). The session note in
  `next_session_handoff.md` 2026-04-25 update block contains the full
  ROI table (random hub vs ER vs subgraph vs cumulative-batch).
- `~/core/nexus/lenses/omega_state_space_lens.hexa` -- n=6 universal
  resonance scoring lens (Leech 24D, J2/sigma/phi). This is *not* the
  4-axis framework -- it is a mathematical resonance scorer. It does
  not score BT axes against ladder/saturation/chain/closure.
- `~/core/nexus/cli/run.hexa` (referenced indirectly) -- contains
  `cmd_omega()`, `cmd_surge()`, etc. These are *executors*, not the
  4-axis framework that the n6 session built.

**Gap:** the four axes are present *separately* in nexus (ladder in
abstraction_ceiling.md; saturation in inventory.json; chain in
canon/forge logs; closure in atlas_n6_omega_closure.md). The n6
contribution is the *unified per-BT scorecard* that asks "where does
this BT sit on each of the four axes?" -- which is a *method*, not a
new artefact. The method is documented across 7 omega-cycle reports
(BT-541..547) but has no nexus-side counterpart that fuses the four.

**Classification:** PARTIAL (ladder fully nexus-side; saturation in
nxs-002; chain/closure in canon design; the 4-axis-fusion method is
ABSENT and is what would absorb).

### 2.2 Feature 2 -- L9 molt-trigger framework

**Nexus-side analogs found:**

- `~/core/nexus/design/abstraction_ceiling.md` §1 has L9 = molt =
  "self-rewrite, engine-code evolution" (placeholder; cmd_molt
  implemented). The *trigger condition* (when to enter L9) is not
  specified in any nexus doc.
- `grep -iE "molt|frame.shift" ~/core/nexus/design/*.md` returns only
  ladder *names* (molt as level), not *molt-trigger logic* (5-clause
  boolean gate, per-BT frame-shift catalogue, validation
  discriminators). No 5-clause gate exists.
- `~/core/nexus/lenses/` -- `grep -i molt` returns nothing; no L9 lens.
- No frame-shift catalogue file exists in nexus design/ or docs/.

**Gap:** the trigger gate (under what 5 conditions is L9 entry
warranted?) is the n6 contribution. nexus has the *level name* but no
*entry criteria*. This makes nexus's `cmd_molt` a black-box launcher
without admission control.

**Classification:** ABSENT (the 5-clause gate + per-BT catalogue +
discriminators are fully n6-originated).

### 2.3 Feature 3 -- Backward-chaining synthesis

**Nexus-side analogs found:**

- `grep -iE "backward|backchain" ~/core/nexus/design/*.md` returns
  matches only inside `abstraction_ceiling.md` and
  `dispatch_path_audit_20260425.md`, but in both cases the term is
  *backward-induction* of ladder semantics (L_ω <- L11 <- L10 ...) for
  *naming*, not for *strategy synthesis* (target -> chain gap -> EMPTY
  rung -> root cause -> ROI probes).
- nexus's standard pattern is forward-driven (drill -> absorb ->
  promote). The n6 backward-chaining (closure first, then probe)
  inverts this. No nexus design document codifies the inverted flow.

**Gap:** nexus is forward-flow; the n6 backward strategy is novel.
However it is *style-of-thought* documentation rather than tooling --
absorption surface is a single design doc.

**Classification:** ABSENT.

### 2.4 Feature 4 -- F-MOLT meta-falsifier

**Nexus-side analogs found:**

- `~/core/nexus/lenses/falsification_lens.hexa`,
  `n6_falsification.hexa`, `cross_four_domain_falsification.hexa`,
  `hexa_sim_falsifier.hexa` -- all four are n=6 resonance *scorers*
  using fixed constants (sigma=12, phi=2, J2=24, ...). Read-through
  shows they all share the same template: emit a hit-count score 0..1.
  None of them implement *framework self-falsification* (a falsifier
  that can fire against the framework that built it).
- `~/core/nexus/docs/self_correction_chain_paper_20260425.md` exists
  but is, per filename, an *output paper draft*, not a meta-falsifier
  protocol.

**Gap:** the F-MOLT meta-falsifier (where the framework provides
falsifiers F-MOLT-A and F-MOLT-D that can fire *on the framework
itself*, with F-MOLT-A actually firing 4/4 on BT54{1,2,3,4}) has no
nexus equivalent. The nexus falsification lenses are scoring devices,
not framework-self-tests.

**Classification:** ABSENT.

### 2.5 Feature 5 -- Seed-trial pattern (D1/D2/D3)

**Nexus-side analogs found:**

- `grep -iE "seed.trial|axiom.recast|mechanism.decoupl" ~/core/nexus/`
  returns *nothing*. nexus has `seed_engine.hexa` (drill seed pool
  generation), `cmd_dream` (L5 self-seed), `_dream_next_seed` (200-cap
  helper) -- all are *generative* seed mechanisms, not *exhaustion-recovery*
  seed trials.
- nexus's `cmd_drill` retries with parameter sweeps (depth/fast/sigma
  grid), which is parameter-space search; it is not the n6 D1/D2/D3
  *axis-orthogonal recovery* (D1 widen catalogue / D2 weaken target
  via L_ω axiom recast / D3 detach proxy axes).

**Gap:** the 3-axis recovery protocol (atlas-scan / axiom-recast /
mechanism-decouple) is the n6 contribution. It is portable as a method
template that any L9-eligible BT can apply.

**Classification:** ABSENT.

### 2.6 Feature 6 -- Discriminator-type bias diagnostic

**Nexus-side analogs found:**

- `grep -iE "discriminator|distributional|structural.import"
  ~/core/nexus/` returns matches only in
  `beyond_omega_epsilon_zero_boundary.md` and
  `beyond_omega_ladder.md`, where the term is *proof-theoretic
  discriminator* (Gentzen ordinal-style), not the n6 PASS/FAIL family
  classifier (distributional / structural-literature / discrete-equality
  / numerical-interval / vacuous-magnitude / axiom-recast).
- No 2x2 contingency template, no PASS-family/FAIL-family vocabulary.

**Gap:** the diagnostic vocabulary is fully n6-originated. It is a
small portable artefact (one taxonomy table + one contingency
construction recipe).

**Classification:** ABSENT.

### 2.7 Feature 7 -- Honesty-amendment protocol

**Nexus-side analogs found:**

- `~/core/nexus/design/honesty_triad.md` (deployed earlier today,
  2026-04-25) is the *substantive* honesty content but does NOT
  prescribe an *amendment* style for past reports. It prescribes
  *new-session* preset lines.
- `grep -iE "amend|append.only|scope.caveat" ~/core/nexus/` returns
  nothing format-related. nexus's standard for past report correction
  is *git history* (write a new session report that supersedes), not
  in-place append-only blocks.
- The n6 contribution: a frozen format for `## §X Amendment (date)
  -- scope-caveat`, append-only, no rewrites of prior numbered §s.

**Gap:** small but real. It is one paragraph of style guidance.

**Classification:** ABSENT (low surface area, but ABSENT, not PARTIAL).

### 2.8 Feature 8 -- Fabrication-refusal cascade

**Nexus-side analogs found:**

- `~/core/nexus/design/honesty_triad.md` constraint #3 is precisely
  this: "DO NOT FABRICATE ... return UNKNOWN/INCONCLUSIVE/TIMEOUT with
  diagnostic." It is **already deployed**. ✓
- The "diagnostic enables next step" elaboration is the n6 *cascade*
  refinement: not just "refuse and return UNKNOWN" but "refuse, and
  the refusal payload should be informative enough that the next agent
  can pick up". This *cascade* step is implicit in honesty_triad #3
  ("with diagnostic") but not made explicit as a *cascade pattern*.

**Gap:** honesty_triad #3 says "with diagnostic". The n6 cascade
pattern (which kinds of diagnostic, and how the next agent picks up)
is one extra paragraph -- it sits inside the existing constraint.

**Classification:** PARTIAL (constraint #3 is PRESENT; cascade
elaboration is the gap and is small).

### 2.9 Feature 9 -- Cross-repo graph mismatch finding

**Nexus-side analogs found:**

- `~/core/nexus/design/next_session_handoff.md` (2026-04-25 update
  block, "core_lockdown" + "ATLAS_VERIFICATION_75" sections + the long
  composite/sensitivity sections) ALREADY contains the full finding:
  "5 [10*] promotion (n6@98a23750) ... atlas.n6 metadata ≠
  atlas.blowup.jsonl graph (already-confirmed separation)". This is verbatim the
  n6 finding.
- `~/core/nexus/state/proposals/inventory.json` `nxs-20260424-002`
  carries the same finding implicitly (composite gap requires graph
  rebuild, not metadata promotion).

**Gap:** the finding is **PRESENT** in nexus, just buried inside
session-handoff text rather than promoted to a standalone design doc.
The n6 session re-derived it independently which strengthens
provenance, but does not add a new artefact.

**Classification:** PRESENT (already in nexus; absorption would be
*lifting* it from handoff text to a named design doc, which is
cosmetic).

### 2.10 Feature 10 -- Patched n6 tools

**Nexus-side analogs found:**

- `ls ~/core/nexus/tool/ | grep -iE "cremona|sle6|gue|q1.molt|leadB|hirahara|hodge|bsd|riemann|onsager"`
  returns **nothing**. The n6 BT-specific tools (cremona_joint_covariance,
  bt541_leadB_sle6_gue, bt544_q1_molt_validation, etc.) are not in
  nexus tool/.
- These tools are *Millennium-BT-specific*: cremona stratification is
  for BSD elliptic-curve probes; SLE6/GUE coupling is for RH boundary
  layer; Q1 6-soliton Gram lattice is for KdV. nexus has no Millennium
  workflow -- it operates atlas.blowup graph + n=6 resonance + drill.
- **Cross-repo principle (`atlas_n6_omega_closure.md` §6):** "n6
  body direct modification is canon-side work. This nexus
  repo is tooling + diagnostics + proposals only." -- BT-specific tools are explicitly outside
  nexus scope.

**Gap:** none -- these tools belong in n6.

**Classification:** SKIP_INCOMPATIBLE (n6-side scope, not transferable
without violating cross-repo policy).

---

## §3 Phase 2 -- Per-feature absorption verdicts

The 5 verdict labels are the *only* allowed values. Each verdict is
justified by one Phase-1 evidence row.

| #  | Feature                                | Verdict             | Reason (1 line)                                                                                          |
|----|----------------------------------------|---------------------|----------------------------------------------------------------------------------------------------------|
| 1  | Omega 4-axis framework                 | ABSORB_GAP          | Ladder/saturation/chain/closure each present separately; the 4-axis-fusion method is ABSENT             |
| 2  | L9 molt-trigger framework              | ABSORB              | cmd_molt exists in nexus without admission control; 5-clause gate fully n6-originated                   |
| 3  | Backward-chaining synthesis            | ABSORB              | Inverted-flow strategy doc has no nexus counterpart; one-doc absorption                                 |
| 4  | F-MOLT meta-falsifier                  | ABSORB              | nexus falsification lenses are scorers; framework-self-falsification is ABSENT                          |
| 5  | Seed-trial pattern (D1/D2/D3)          | ABSORB              | Exhaustion-recovery axes orthogonal to nexus's parameter-sweep retries; no analog                       |
| 6  | Discriminator-type bias diagnostic     | ABSORB              | Vocabulary fully n6-originated; small portable taxonomy artefact                                        |
| 7  | Honesty-amendment protocol             | ABSORB              | nexus has no append-only scope-caveat format for past reports                                           |
| 8  | Fabrication-refusal cascade            | SKIP_LOW_LEVERAGE   | honesty_triad #3 already covers the constraint; cascade is one paragraph inside existing doc            |
| 9  | Cross-repo graph mismatch finding      | SKIP_REDUNDANT      | Finding is PRESENT in nexus next_session_handoff.md; lifting it to standalone is cosmetic               |
| 10 | Patched n6 tools                       | SKIP_INCOMPATIBLE   | n6-side BT-specific scope; cross-repo policy says n6 body work in n6                                    |

**Tally:** 6 ABSORB(_GAP) / 4 SKIP. Specifically:
- 1 ABSORB_GAP: feature 1.
- 5 ABSORB: features 2, 3, 4, 5, 6, 7. (six total ABSORB-class)
- 1 SKIP_LOW_LEVERAGE: feature 8.
- 1 SKIP_REDUNDANT: feature 9.
- 1 SKIP_INCOMPATIBLE: feature 10.

(Six ABSORB-class total: 1 ABSORB_GAP + 5 ABSORB.)

---

## §4 Phase 3 -- Absorption design (per ABSORB / ABSORB_GAP)

Six designs follow. Each specifies target path, form, dependency, and
cost. **No file is created in this session** -- the specs below are
for next-session deployment.

### 4.1 Feature 1 -- Omega 4-axis framework (ABSORB_GAP)

- **Target nexus location:**
  `~/core/nexus/design/omega_4axis_scorecard.md` (NEW, sibling of
  existing `abstraction_ceiling.md` and `atlas_n6_omega_closure.md`).
- **Form:** doc (markdown). One scorecard template + worked example
  pointing to the n6 BT-541..547 series as exemplars.
- **Dependency:** READS `abstraction_ceiling.md` (ladder), `nxs-002`
  inventory entry (saturation), `atlas_n6_omega_closure.md` (closure).
  Does NOT modify any of those.
- **Cost:** **low**.
  - Files added: 1.
  - Lines added: ~80-120 (one table + one worked example + 4-axis
    definition list).
  - Reference cascade: 0 incoming references modified; the doc adds
    outgoing references only (to the 3 existing nexus designs +
    cross-repo pointer to n6 reports).

### 4.2 Feature 2 -- L9 molt-trigger framework (ABSORB)

- **Target nexus location:**
  `~/core/nexus/design/l9_molt_trigger.md` (NEW). Optionally a
  companion `lenses/l9_molt_trigger_lens.hexa` *only if* the lens-form
  resonance scorer pattern is wanted (it is not strictly necessary --
  see cost note).
- **Form:** doc (markdown), with the 5-clause gate as a checklist;
  per-BT frame-shift catalogue is **not** absorbed (it is BT-specific
  and lives in n6); the *gate* and *discriminator slots* are absorbed.
- **Dependency:** Feature 6 (discriminator-type vocabulary) is
  referenced by the gate's clause #5 ("discriminator-type test"). If
  feature 6 is not absorbed yet, gate clause #5 is left as a TODO
  pointer.
- **Cost:** **low-medium**.
  - Files added: 1 (or 2 if lens companion).
  - Lines added: ~120-180 (5-clause gate + 5 discriminator slots +
    "when to enter L9" decision tree + 1 worked example).
  - Reference cascade: `abstraction_ceiling.md` §1 L9 line could
    optionally back-reference; that is one *paragraph* edit, not
    structural.

### 4.3 Feature 3 -- Backward-chaining synthesis (ABSORB)

- **Target nexus location:**
  `~/core/nexus/design/backward_chaining_synthesis.md` (NEW).
- **Form:** doc (markdown). 5-step recipe: closure target -> chain gap
  -> ladder EMPTY rung -> root cause -> ROI probe ranking. One worked
  example pointing to `omega-cycle-backtrace-strategy-2026-04-25.md`.
- **Dependency:** none required. Reads `abstraction_ceiling.md` for
  ladder vocabulary.
- **Cost:** **low**.
  - Files added: 1.
  - Lines added: ~80-120.
  - Reference cascade: 0.

### 4.4 Feature 4 -- F-MOLT meta-falsifier (ABSORB)

- **Target nexus location:**
  `~/core/nexus/design/f_molt_meta_falsifier.md` (NEW). The n6 reports
  are pointed-to as the empirical ground (4/4 FAIL on BT54{1..4} for
  F-MOLT-A; catalogue exhaustion for F-MOLT-D).
- **Form:** doc (markdown). The two falsifiers are stated *abstractly*
  (framework-self-test pattern), then n6-instantiated. **No new lens
  is added** -- existing nexus falsification_lens.hexa family is
  scorer-shaped and would not match this protocol; absorbing as doc
  avoids polluting the lens namespace.
- **Dependency:** Feature 1 (4-axis framework) -- F-MOLT fires when
  the 4-axis scorecard reaches a specific configuration, so the
  scorecard doc must exist for F-MOLT to be statable. Feature 2 (L9
  trigger) is also referenced because F-MOLT-A is the gate that fired
  vs molt-validation criterion.
- **Cost:** **medium**.
  - Files added: 1.
  - Lines added: ~140-200 (two falsifier definitions + firing
    conditions + worked example with 4 BT firings).
  - Reference cascade: depends on features 1 and 2 -- if those are
    absorbed first, this is straight reference; if not, this doc
    holds inline definitions and is independent (+50 lines).

### 4.5 Feature 5 -- Seed-trial pattern (D1/D2/D3) (ABSORB)

- **Target nexus location:**
  `~/core/nexus/design/seed_trial_d1d2d3.md` (NEW). Optionally a
  companion `tool/seed_trial_dispatcher.py` *only if* the user wants
  command-line dispatch (not strictly needed for absorption; the doc
  is the load-bearing artefact).
- **Form:** doc (markdown). Three orthogonal recovery axes named, each
  with a one-paragraph spec + a one-line "when to apply" trigger.
- **Dependency:** Feature 2 (L9 trigger -- the *exhaustion* signal
  that calls D1/D2/D3 is generated by the L9 gate's failure modes).
- **Cost:** **low**.
  - Files added: 1.
  - Lines added: ~100-140.
  - Reference cascade: depends on feature 2 if absorbed; otherwise
    inline triggers.

### 4.6 Feature 6 -- Discriminator-type bias diagnostic (ABSORB)

- **Target nexus location:**
  `~/core/nexus/design/discriminator_type_bias.md` (NEW). Small file.
- **Form:** doc (markdown). Vocabulary table (PASS family vs FAIL
  family) + 2x2 contingency template + one worked example pointer.
- **Dependency:** none. This is a vocabulary primitive that other
  features (2 -- L9 gate clause #5; 4 -- F-MOLT-D) reference *into*,
  not out of.
- **Cost:** **lowest** (smallest of the six).
  - Files added: 1.
  - Lines added: ~50-80.
  - Reference cascade: 0 outgoing; 2 incoming (features 2 and 4
    optionally reference back).

### 4.7 Feature 7 -- Honesty-amendment protocol (ABSORB)

- **Target nexus location:** *append-section* into existing
  `~/core/nexus/design/honesty_triad.md` as a new sub-section "## (4)
  Amendment style" (not a new file). This keeps honesty content
  consolidated.
- **Form:** doc (markdown sub-section). One paragraph of format
  (append-only, scope-caveat block, no rewrites) + one example.
- **Dependency:** EXTENDS `honesty_triad.md` (already present).
- **Cost:** **lowest**.
  - Files added: 0 (in-place edit on existing nexus design doc).
  - Lines added: ~25-40.
  - Reference cascade: 0.
  - Caveat: the user's protocol is to NOT modify nexus files in this
    session. The *deployment* (next session) would be a small edit
    that respects honesty_triad's own write-barrier (honesty_triad.md
    is NOT in the write-barrier list -- design/ is mutable per
    constraint #2). Confirmed read of honesty_triad.md §2 in §2.8.

---

## §5 Phase 4 -- Deploy ranking (top-3 deploy-ready)

Ranking criteria as specified:
- **Leverage** = how many future nexus sessions benefit;
- **Independence** = low cross-feature dependency;
- **Cost** = file + line + cascade size.

Ranking table (all six ABSORB-class candidates):

| Rank | Feature # | Name                              | Leverage | Independence       | Cost     | Combined |
|------|-----------|-----------------------------------|----------|--------------------|----------|----------|
| 1    | 6         | Discriminator-type bias diagnostic| medium   | high (zero deps)   | lowest   | **top**  |
| 2    | 7         | Honesty-amendment protocol        | medium   | high (extends honesty_triad only) | lowest | **top** |
| 3    | 3         | Backward-chaining synthesis       | high     | high (zero deps)   | low      | **top**  |
| 4    | 1         | Omega 4-axis scorecard            | high     | medium (reads 3 nexus designs) | low      |          |
| 5    | 2         | L9 molt-trigger framework         | high     | medium (refs feat 6) | low-med  |          |
| 6    | 5         | Seed-trial D1/D2/D3 pattern       | medium   | medium (refs feat 2) | low      |          |
| 7    | 4         | F-MOLT meta-falsifier             | high     | low (refs feat 1+2)| medium   |          |

**Top-3 deploy-ready (next-session candidates) -- full spec:**

#### Rank 1 -- Feature 6 (Discriminator-type bias diagnostic)

```
target_path:  ~/core/nexus/design/discriminator_type_bias.md
form:         design doc (markdown)
deps:         none (primitive vocabulary)
cost:         lowest (1 file, 50-80 lines, 0 cascade)
content:
  - PASS family taxonomy: distributional, structural-literature
  - FAIL family taxonomy: discrete-equality, numerical-interval,
                          vacuous-magnitude
  - separate row: axiom-recast (acceptability, not molt-validation)
  - 2x2 contingency template (PASS x FAIL on the discriminator-type
    axis vs molt verdict axis)
  - worked example pointer:
    canon/reports/sessions/omega-meta-audit-discriminator-type-bias-2026-04-25.md
  - non-claim disclaimer: this is a *diagnostic vocabulary*, not a
    proof technique
falsifier on the absorption itself:
  - if a future BT verdict is encountered that does not fit any of
    the 5 labels, the taxonomy is INCOMPLETE and must be amended
    (using feature-7 amendment style, if that lands)
deploy precedent: honesty_triad.md
```

#### Rank 2 -- Feature 7 (Honesty-amendment protocol)

```
target_path:  ~/core/nexus/design/honesty_triad.md  (in-place edit,
              new sub-section "(4) Amendment style")
form:         doc sub-section (markdown)
deps:         EXTENDS existing honesty_triad.md (must already exist
              -- it does, deployed earlier 2026-04-25)
cost:         lowest (0 new files, 25-40 lines, 0 cascade)
content:
  - amendment block format:
      ## §X Amendment (YYYY-MM-DD) -- <scope caveat label>
      <one paragraph: what was unclear or under-scoped in original>
      <one paragraph: corrected reading>
  - rule: append-only; never rewrite numbered §s of past report
  - rule: amendment block goes at the END of the report, not inline
  - one worked example pointer:
    canon/reports/sessions/omega-amend-perbt-honesty-2026-04-25.md
falsifier on the absorption itself:
  - if an amendment ever needs to *retract* (not narrow) a past
    claim, the format is INSUFFICIENT and a separate retraction
    protocol is required (out of scope for this absorption)
deploy precedent: honesty_triad.md (the file being edited)
```

#### Rank 3 -- Feature 3 (Backward-chaining synthesis)

```
target_path:  ~/core/nexus/design/backward_chaining_synthesis.md
form:         design doc (markdown)
deps:         none (reads abstraction_ceiling.md vocabulary only)
cost:         low (1 file, 80-120 lines, 0 cascade)
content:
  - 5-step recipe:
      (1) state closure target (which ceiling/closure goal)
      (2) identify chain gap (which ladder rung is empty)
      (3) ladder EMPTY rung detection (which L_k has no progress)
      (4) root cause hypothesis
      (5) ROI probe ranking (cost vs gap-closure)
  - inverted-flow note: nexus default is forward (drill->absorb->
    promote); this protocol inverts (target->probe selection)
  - worked example pointer:
    canon/reports/sessions/omega-cycle-backtrace-strategy-2026-04-25.md
falsifier on the absorption itself:
  - if a closure target is reached *without* the 5-step chain
    being applicable (e.g., a discovery is found without backward
    planning), the protocol is OPTIONAL not REQUIRED, and the
    doc should label it as such (it should already)
deploy precedent: honesty_triad.md
```

---

## §6 Cross-feature dependencies map

```
                                    +---------------------------+
                                    |  honesty_triad.md (EXISTS) |
                                    +-------------+-------------+
                                                  |
                                                  | EXTENDS
                                                  v
                                    +---------------------------+
                                    | (7) Amendment protocol    |  <-- rank 2
                                    +---------------------------+

       +---------------------------+
       | (6) Discriminator types   |  <-- rank 1   (zero deps)
       +-------------+-------------+
                     |
                     | referenced by
                     v
       +---------------------------+        +---------------------------+
       | (2) L9 molt trigger gate  |  ----> | clause #5 calls feat 6    |
       +-------------+-------------+        +---------------------------+
                     |
                     | exhaustion-signal
                     v
       +---------------------------+
       | (5) Seed-trial D1/D2/D3   |
       +---------------------------+

       +---------------------------+
       | abstraction_ceiling.md    |  (EXISTS, ladder source)
       +-------------+-------------+
                     |
                     | reads
                     v
       +---------------------------+
       | (1) Omega 4-axis          |  reads atlas_n6_omega_closure.md
       |     scorecard             |        + nxs-002 inventory
       +-------------+-------------+
                     |
                     | scored by
                     v
       +---------------------------+
       | (4) F-MOLT meta-falsifier |   also references (2)
       +---------------------------+

       +---------------------------+
       | (3) Backward-chaining     |  <-- rank 3   (zero deps)
       +---------------------------+
```

**Independence ranking** (low-dep = absorb first):
- **Zero deps:** features 6, 3, 7 -- all top-3 (matches §5 ranking).
- **One dep:** features 1 (3 reads), 5 (refs 2), 7 (extends honesty
  triad which already exists -- the dep is *trivial-satisfied*).
- **Two deps:** feature 4 (refs 1 and 2).
- **Many reads (no writes):** feature 1 reads 3 existing nexus
  designs but writes none -- so its "dependency" is just *vocabulary*,
  satisfied by reading.

**Recommended absorption order (next-session and beyond):**
1. Feature 6 (rank 1) -- primitive vocabulary; unblocks 2 and 4.
2. Feature 7 (rank 2) -- amendment style; unblocks future correction
   protocol for *all* features.
3. Feature 3 (rank 3) -- standalone strategy doc.
4. Feature 1 (rank 4) -- 4-axis scorecard (after 6 lands).
5. Feature 2 (rank 5) -- L9 trigger gate (after 1 and 6 land).
6. Feature 5 (rank 6) -- seed-trial pattern (after 2 lands).
7. Feature 4 (rank 7) -- F-MOLT (after 1 and 2 land).

---

## §7 Anti-list -- features considered and rejected

Features explicitly considered for absorption and rejected:

### Anti-1. Feature 8 -- Fabrication-refusal cascade (SKIP_LOW_LEVERAGE)

- The *constraint* is already in `honesty_triad.md` constraint #3.
- The *cascade refinement* (which kinds of diagnostic, how next agent
  picks up) is one paragraph and naturally lives inside constraint #3
  rather than as a new doc.
- Adding it as a new file would split honesty content; adding as a
  sub-section is acceptable but is incremental on top of the
  Amendment-style sub-section (feature 7), and the marginal lift over
  what `with diagnostic` already implies is small.
- Recommendation if revisited: append a one-paragraph *example* under
  honesty_triad.md constraint #3 in the same edit pass that lands
  feature 7's Amendment sub-section. Cost would round to zero.

### Anti-2. Feature 9 -- Cross-repo graph mismatch finding (SKIP_REDUNDANT)

- The finding is *already in nexus*, in `next_session_handoff.md`'s
  2026-04-25 update block. The exact statement "atlas.n6 metadata ≠
  atlas.blowup.jsonl graph (already-confirmed separation)" is verbatim there.
- Lifting it to a standalone design doc would be a *cosmetic*
  re-presentation, not a content addition.
- The finding's *implication* (composite gap requires graph rebuild,
  not metadata promotion) is already encoded in `nxs-20260424-002`
  user_status=in_progress with explicit "fresh atlas eig pipeline
  rebuild" task description.
- Recommendation: leave as-is. If standalone doc desired later, lift
  out of handoff after `nxs-002` resolves.

### Anti-3. Feature 10 -- Patched n6 tools (SKIP_INCOMPATIBLE)

- These tools are Millennium-BT-specific (cremona for BSD, SLE6/GUE
  for RH, Q1 6-soliton for KdV-NS). nexus operates atlas.blowup graph
  + n=6 resonance + drill -- it has no Millennium workflow.
- The cross-repo principle in
  `~/core/nexus/design/atlas_n6_omega_closure.md` §6 explicitly says
  "n6 body direct modification is canon-side work". Tooling for n6 BTs
  belongs in n6.
- Absorbing them would create dead code in nexus tool/ that nothing in
  nexus calls.
- Recommendation: keep in n6. If a *generic pattern* emerges from the
  three patched tools (e.g., "per-stratum confidence interval" as a
  reusable helper), absorb that *pattern* (not the tool) -- but at
  this writing no such pattern is generic enough.

### Anti-4. (Optional) lenses-form embodiment of features 1, 2, 4

- Considered: should features 1, 2, or 4 be embodied as `.hexa`
  lenses in `~/core/nexus/lenses/`?
- Read-through of existing lenses (`omega_state_space_lens.hexa`,
  `falsification_lens.hexa`, `n6_falsification.hexa`,
  `cross_four_domain_falsification.hexa`,
  `hexa_sim_falsifier.hexa`) confirms they share a single template:
  emit a 0..1 hit-count score against a fixed target list (sigma=12,
  phi=2, J2=24, ...).
- This *scorer-shape* is incompatible with features 1, 2, 4, which
  are *protocols* (multi-step recipes), not single-number scorers.
- Forcing them into lens-shape would either degrade them to a useless
  resonance score or violate the lens-template convention.
- Recommendation: doc-form for features 1, 2, 4. No lens additions.

---

## §8 Falsifiers active for the absorption design

The absorption design is itself a falsifiable proposal. The following
events would falsify portions of it:

- **F-ABS-1** (Feature 6 falsifier). If a future BT verdict is encountered
  that does not fit any of the 5 discriminator labels (PASS family:
  distributional, structural-literature; FAIL family: discrete-equality,
  numerical-interval, vacuous-magnitude), the taxonomy in
  `discriminator_type_bias.md` is INCOMPLETE. Trigger: amend per
  feature-7 protocol; do NOT silently extend the table.
- **F-ABS-2** (Feature 7 falsifier). If an amendment ever needs to
  *retract* (not narrow) a past claim, the append-only scope-caveat
  block format is INSUFFICIENT. Trigger: open a separate retraction
  protocol design proposal (out of current scope).
- **F-ABS-3** (Feature 3 falsifier). If a closure is reached without
  the 5-step backward chain being applicable, the protocol is
  OPTIONAL, not REQUIRED. Trigger: re-label as "default strategy
  template" rather than "synthesis protocol".
- **F-ABS-4** (Feature 1 falsifier). If a BT scorecard yields a
  4-tuple where one axis is *non-applicable* (rather than empty), the
  scorecard schema is too rigid. Trigger: add a NA cell convention to
  the scorecard template.
- **F-ABS-5** (Feature 2 falsifier). If a future BT enters L9
  (engine-rewrite) without all 5 clauses of the gate being satisfied,
  the gate is over-strict (false negative). Trigger: review gate
  clauses; possibly relax to 4-of-5.
- **F-ABS-6** (Feature 4 falsifier). If F-MOLT-A or F-MOLT-D fires on
  a 5th, 6th, ... BT in the same configuration as BT-541..544, the
  framework's *catalogue exhaustion* prediction is confirmed and a
  framework-revision (not just a new BT-row) is required.
- **F-ABS-7** (Feature 5 falsifier). If a 4th orthogonal recovery axis
  (D4) emerges in a future session, the seed-trial pattern is
  INCOMPLETE. Trigger: append D4 spec to `seed_trial_d1d2d3.md` with
  an amendment block.
- **F-ABS-8** (Anti-list falsifier). If a generic pattern *does*
  emerge across the 3 patched n6 tools (cremona / SLE6-GUE /
  Q1-soliton), the SKIP_INCOMPATIBLE verdict on feature 10 is wrong;
  the pattern (not the tools) becomes ABSORB-eligible. Trigger:
  specific generic pattern identified by name, with at least 2 of the
  3 tools instantiating it.

These falsifiers are *active*, meaning they should be tested in any
future session that touches the corresponding feature. They are
recorded here so the absorption design itself is not exempt from the
no-fabrication / honesty-triad regime that the n6 session deployed.

---

## §9 Closing

- **0/7 unchanged.** No Millennium claim made or implied. F-MOLT-A's
  4/4 FAIL on BT-541..544 is *not* retracted; absorption of the
  framework is orthogonal to those FAIL verdicts.
- **nxs promotion count unchanged.** This session does not modify
  `~/core/nexus/state/proposals/inventory.json` or any state file.
  `nxs-20260424-002` (`Ω_saturation_cycle`) ack=in_progress as before.
- **NO nexus files modified by this design (read-only).** Verified by
  the constraint that all bash invocations in this session are reads
  (ls/grep/cat) on nexus/ paths and only the canon-side
  output file is `Write`-created.
- The 6 ABSORB-class candidates (1 ABSORB_GAP + 5 ABSORB) are
  next-session deploy targets in the order given in §5 and §6.
- The 4 SKIP candidates have explicit reasons in §7 anti-list and
  should not be revisited unless their falsifier triggers fire.
- Output file:
  `~/core/canon/reports/sessions/omega-design-nexus-feature-absorption-2026-04-25.md`
  (this file).
