---
id: omega-meta-synthesis-repo-invariant-honesty-audit
date: 2026-04-25
scope: methodological synthesis (NOT proposing constraints for new repos; characterizing pattern)
target: 6-of-6 KEEP_AS_IS across n6+nexus -- portable triad pattern + preconditions + predictions
parent_reports:
  - reports/sessions/omega-audit-constraint-honesty-counter-2026-04-25.md
  - reports/sessions/omega-audit-constraint-write-barrier-2026-04-25.md
  - reports/sessions/omega-audit-constraint-no-fabrication-2026-04-25.md
  - reports/sessions/omega-audit-nexus-native-3constraint-2026-04-25.md (REPO_INVARIANT)
  - reports/sessions/omega-audit-nexus-honesty-triad-portability-2026-04-25.md (porting audit)
  - reports/sessions/omega-deploy-nexus-honesty-triad-2026-04-25.md (deploy)
millennium_resolved: 0/7 (unchanged)
nxs_promotion_count_delta: 0
grade: methodological synthesis, no claim
---

## §0 Non-claim disclaimer

This report is a **methodological synthesis**, not a constraint-promotion exercise. Its
purpose is to take the six independent audits already produced (3 on n6-architecture,
3 on nexus, all returning KEEP-direction verdicts) and ask one narrow question: **is
the 3-constraint honesty triad a portable pattern, and what preconditions does a repo
need to satisfy for the triad to apply?** The answer is structured as a portable text-
only specification, a list of preconditions, three counterfactual cases, and three
testable predictions.

What this report is **not**:

- **Not** a deployment of the triad to any third repo. The synthesis discusses what
  *would be needed* in a hypothetical port; it does not perform one.
- **Not** a re-derivation of the six parent verdicts. Each parent verdict stands on its
  own evidence; this report cites them but does not re-audit them.
- **Not** a claim that the triad is universal across all LLM workflows. §4 explicitly
  identifies workflow types where one or more preconditions are absent and the pattern
  must be modified or dropped.
- **Not** an action — no atlas / state / inventory / CLAUDE.md edit follows from this
  document in either n6 or nexus. The single output is this report under
  `reports/sessions/`.

The 0/7 honesty counter is unchanged. The nxs_promotion_count delta is `0`. n=2 repos
is a small sample (§6 limitations). Every n6 / nexus claim below is cited from a real
audit file path; no value is invented.

---

## §1 6-of-6 result summary

The six independent audits and their verdicts, each cited verbatim from the parent
files:

| # | Repo | Constraint | Audit file (absolute path) | Verdict |
|---|---|---|---|---|
| 1 | n6-architecture | Honesty counter (`millennium_resolved: 0/7 unchanged`) | `/Users/ghost/core/n6-architecture/reports/sessions/omega-audit-constraint-honesty-counter-2026-04-25.md` | **KEEP_AS_IS** (§8 line 236: "**KEEP_AS_IS**") |
| 2 | n6-architecture | Write-barrier (atlas/, state/, inventory.json, breakthrough-theorems.md) | `/Users/ghost/core/n6-architecture/reports/sessions/omega-audit-constraint-write-barrier-2026-04-25.md` | **KEEP_AS_IS** (sec 10 line 478: "Verdict: `KEEP_AS_IS`") |
| 3 | n6-architecture | No-fabrication guard (UNKNOWN > invented) | `/Users/ghost/core/n6-architecture/reports/sessions/omega-audit-constraint-no-fabrication-2026-04-25.md` | **KEEP_AS_IS** (§9 line 284: "**KEEP_AS_IS**") |
| 4 | nexus (native) | nxs_promotion_count banner | `/Users/ghost/core/n6-architecture/reports/sessions/omega-audit-nexus-native-3constraint-2026-04-25.md` (Audit 1) | **KEEP_AS_IS** (function) / **KEEP_BUT_ADAPT** (literal) — §2.8 |
| 5 | nexus (native) | nexus write-barrier (extended path list) | same file (Audit 2) | **KEEP_AS_IS** — §3.9 |
| 6 | nexus (native) | nexus no-fabrication guard | same file (Audit 3) | **KEEP_AS_IS** — §4.8 |

**6-of-6 KEEP-direction.** The single literal-level adaptation (#4) is a *form change*
from `0/7` to `nxs_promotion_count: N/N0` — the constraint *function* (first-line clamp
against silent SSOT mutation) is preserved. The function-level agreement count is **3-of-3
across both repos**. The nexus-native audit's §6 explicitly graded this as **REPO_INVARIANT**
(line 762).

The porting audit (`omega-audit-nexus-honesty-triad-portability-2026-04-25.md` §6) and the
deploy log (`omega-deploy-nexus-honesty-triad-2026-04-25.md` §3-§4) confirm that nexus's
form of the triad has been deployed at the design-doc + project-claude layer (Target 1
created at `~/core/nexus/design/honesty_triad.md`, Target 2 appended to
`~/core/nexus/project-claude/nexus.md`; Target 3 agent-prompt preset deferred).

---

## §2 Triad preconditions (5)

For the 3-constraint honesty triad to apply, the workflow must satisfy five
preconditions. Each is described in generic form, then instantiated in n6 and nexus.

### §2.1 Precondition (a) — Promotion path

**Generic**: there must exist some discrete, named operation by which a result can be
*officially* marked solved/EXACT/done. Without a promotion operation, there is nothing
to silently mutate, and the honesty counter has no denominator.

| Repo | Instantiation |
|---|---|
| n6-architecture | The 7 Clay Millennium Problems form a fixed-7 denominator; "promotion" = transitioning a BT (e.g. BT-541 ρ_n) from `[5*]` structural to `[10*]+ EXACT` registration in `atlas/atlas.n6` after external verification (cite: write-barrier audit sec 1.2, sec 1.3 atlas-agent EXACT-only gate). |
| nexus | Promotion = transitioning a `state/proposals/inventory.json` entry's `user_status` from `submitted` → `in_progress` → `implemented`, and/or atlas-grade promotion in `n6/atlas.blowup.jsonl` (e.g. commit `39b2d0f4`: "33 atlas promotions in a single revive cycle", cited in nexus-native audit §2.3 incident #1). |

### §2.2 Precondition (b) — SSOT (single source of truth)

**Generic**: there must be a canonical registry that the promotion operation writes to,
and that registry must be distinct from the working files where research/exploration
occurs. Without an SSOT, "modifying X is forbidden" has no target.

| Repo | Instantiation |
|---|---|
| n6-architecture | `atlas/atlas.n6` (21,800 lines), `atlas/atlas.signals.n6` (4,205 lines), `state/proposals/inventory.json` (151 lines), `theory/breakthroughs/breakthrough-theorems.md` (28,480 lines). Total protected ≈ 54,691 lines / 12 files (cite: write-barrier audit sec 1.2). |
| nexus | `n6/atlas.blowup.jsonl` (17 MB / 20,525 nodes / 54,347 edges), `state/proposals/inventory.json` (21 entries, schema `nexus.proposal_inventory.v1`), `state/atlas_health_timeline.jsonl`, `state/agent_lock_ledger.jsonl`, `lenses/omega_state_space_lens.hexa`, `project-claude/*.md` (cite: nexus-native audit §3.1, §3.2). |

### §2.3 Precondition (c) — Research/reflection layer separate from SSOT

**Generic**: there must exist a writable path for session output (audits, exploration,
drafts) that is *not* the SSOT. Without such a layer, write-barrier removal is the only
way to capture session work; the barrier becomes incoherent.

| Repo | Instantiation |
|---|---|
| n6-architecture | `reports/sessions/` (45 session reports as of audit window), `theory/study/p0-p3/`, `theory/roadmap-v2/`, `papers/` — all are writable by general-purpose agents (cite: honesty-counter audit §3 saturation table). |
| nexus | `design/` (10 files), `reports/` (15 flat JSON/MD analytics files; no `sessions/` subdir, per nexus-native audit §1 framework table), commit-message stream (1734 commits / 14 days as the per-cycle narrative substrate). |

### §2.4 Precondition (d) — Tool ecosystem with measurable values

**Generic**: there must be tools that produce numeric / structural outputs, and tool gaps
that an agent could "fill" by inventing a value. Without a tool ecosystem, the
no-fabrication guard has no surface to defend.

| Repo | Instantiation |
|---|---|
| n6-architecture | `tool/` directory; per-BT lemma audits; `theory/predictions/verify_*.hexa` files; `data/cremona/allbsd/` (169 MB, 27 shards verified in no-fabrication audit §5 row 3). The Probe #3 case (`omega-probe-nxs002-predict-er-2026-04-25.md` §1.4) is the canonical fabrication-risk activation: tool lacked per-BT mode, agent returned 5×UNAVAILABLE rather than 5 fabricated composites (cite: no-fabrication audit §4 row 1). |
| nexus | `tool/nxs_002_composite.py --predict-er`, `tool/lockdown_gate.hexa`, `tool/atlas_meta_scan.hexa`, harness modules. Cycle-43 commit `6772aede` ("raw 37/38 enforce not actually working, no caller") is a self-disclosed near-fabrication: a counter claimed to enforce something but no caller wired it (cite: nexus-native audit §4.3 row 1). |

### §2.5 Precondition (e) — LLM agents performing research/promotion

**Generic**: the agents writing/promoting must be LLM-driven (not pure-deterministic
scripts). Fabrication risk is an LLM-property; honesty counters are an
LLM-output-discipline; write-barriers are needed because LLMs can ignore policy unless
prompted. Without LLM agents, deterministic checks suffice and the triad is overkill.

| Repo | Instantiation |
|---|---|
| n6-architecture | `.claude/agents/atlas-agent/AGENT.md`, `growth-agent/AGENT.md`, `lens-agent/AGENT.md` (deprecated 2026-04-11), `safe-commit.md` — each with explicit tool privileges and gate stacks (cite: write-barrier audit sec 2.1). General-purpose agents constitute ~88% of recent invocations (cite: write-barrier audit §4.2). |
| nexus | `.claude/agents/safe-commit.md` only; atlas-agent / growth-agent referenced in commit-message convention but not as `.md` definitions (cite: nexus-native audit §3.3 — "atlas-agent / growth-agent / lens-agent: NOT located, NOT confirmed"). Privileged-agent function is encoded as runtime tools (`lockdown_gate.hexa`, `harness/`) rather than as prompt definitions. **Same precondition is satisfied via different mechanism.** |

**Generic preconditions checklist (5)**:
1. promotion path exists,
2. SSOT exists and is distinct from research layer,
3. research/reflection layer exists and is distinct from SSOT,
4. tool ecosystem produces measurable values with gap risk,
5. LLM agents perform the research/promotion work.

All 5 are satisfied in both n6 and nexus, with nexus showing **structural divergence
on (e)** (runtime tools instead of `.md` agents). The triad still applies because the
*function* of (e) — namely, having LLM agents whose outputs need disciplining — is met.

---

## §3 Generic portable triad pattern (text-only)

This is the portable specification. It is not deployable as-is in any new repo without
first verifying the 5 preconditions; it is the *target shape* once preconditions are met.

```
## Honesty Triad (generic)

For LLM-driven research workflows with promotion paths + SSOT + research layer + tools
+ LLM agents:

(1) Promotion-counter banner.
    At session start, record promotion_count_baseline := count(SSOT entries with
    promoted-status). At session end, assert promotion_count == promotion_count_baseline
    UNLESS an explicit privileged-agent promotion has occurred during the session.
    Banner format in session-report front-matter:

        [counter_name]: <N>/<N_baseline> unchanged

    Non-zero delta is named explicitly:

        [counter_name]: <N>/<N_baseline> (+<k> this session: <list of names>)

    The banner appears in front-matter AND in closing — repetition is the clamp. Boilerplate
    cost ≈ 3 lines / artifact; expected fraction of project surface < 0.5%.

(2) Write-barrier.
    Session/research/general-purpose agents MUST NOT modify SSOT paths. Privileged
    agents only — named explicitly per workflow (e.g. atlas-agent with EXACT-only gate;
    promotion-script with dedup check; explicit user commit). Mutable session output
    goes to research-layer paths only. Proposed promotions land as DRAFTS inside the
    session report itself, awaiting privileged-agent commit. The barrier appears as a
    one-line constraint in agent prompts AND as a closing affirmation
    ("no SSOT/state/inventory edits") in each session artifact.

(3) No-fabrication guard.
    Agents return UNKNOWN / INCONCLUSIVE / TIMEOUT / UNAVAILABLE / UNCALIBRATED /
    UNVERIFIED — instead of fabricating values — when (a) a tool is missing, (b) data is
    absent, (c) computation was not run, (d) a paper was not actually read, or (e) a
    measurement is otherwise unobtainable. The diagnostic must name the gap (which tool,
    which data, which paper). Numeric values, axis counts, ceiling deltas, and promotion
    claims must each be backed by a citation (path + line range + read-timestamp) or
    explicitly tagged.
```

The triad is **5 fabrication classes × 6+ violation classes × 12 ladder rungs deep** in
its native n6 instantiation (cite: no-fabrication audit §1 / §2; write-barrier audit
sec 3 / sec 7), but its portable form is the three statements above. Each statement
*generalizes* the n6 / nexus instantiations, dropping the repo-specific
denominator/path/tool details.

---

## §4 Where the triad does NOT apply (counterfactuals)

The five preconditions of §2 are not always present. Workflow types that lack one or
more preconditions need a *modified* pattern (or no pattern at all). Three cases:

### §4.1 Pure pair-programming with no promotion path

**Missing precondition**: (a) promotion path.

**Example workflows**: an LLM-assisted IDE session writing code for a single feature,
with no concept of "marking this feature solved" beyond commit-and-push. There is no
fixed denominator and no privileged-agent gate.

**Modified triad**:
- **(1) honesty-counter** is irrelevant — no count to track, no first-line clamp
  against silent SSOT mutation.
- **(2) write-barrier** is also irrelevant in its triad form. The functional analog is
  *test-coverage* / *CI-gate* / *review-required-before-merge* — distinct mechanisms,
  not the same constraint.
- **(3) no-fabrication guard** *still applies* and is the only triad component that
  ports cleanly. An LLM in a coding session can still fabricate a function name,
  package version, API signature, or test result. The guard form is identical: return
  UNKNOWN / `# UNVERIFIED` instead of inventing.

**Net**: only (3) survives. The "triad" reduces to a single guard.

### §4.2 Workflows where SSOT IS the working file

**Missing precondition**: (b) SSOT distinct from working files. (Equivalently: (c) is
also absent — there is no separate research layer.)

**Example workflows**: a single-file knowledge-base maintenance loop where the LLM
edits the canonical document directly (e.g. updating a wiki page in place), or a
single-shot data-cleaning script that overwrites its input. There is no
research/reflection layer because *all* output IS the SSOT update.

**Modified triad**:
- **(1) honesty-counter** is partially viable but degenerate — the "count" is
  effectively *every change made this session*, which collapses into "did anything
  change?" — too coarse to be a clamp.
- **(2) write-barrier** is impossible in its triad form. There is no path to forbid
  SSOT modification because SSOT modification *is the work*. The functional analog is
  *transaction discipline* — `git add -p`, structured-edit boundaries, atomic-commit
  patterns — which are different mechanisms.
- **(3) no-fabrication guard** still applies, with the same form as §4.1.

**Net**: (3) survives; (1) collapses to a coarse "diff count" that adds no value;
(2) is replaced by transaction discipline.

### §4.3 Read-only research (literature review, doc summarization)

**Missing precondition**: (d) tool ecosystem with measurable values is reduced. The
agent reads but does not measure; tool gaps are not the primary failure mode. Citation
fabrication (C2) is the dominant risk, not tool/result fabrication (C3/C5).

**Example workflows**: a literature-review agent summarizing a paper corpus; a
documentation-question-answering agent over a fixed knowledge base; a
read-only-IDE-explainer agent.

**Modified triad**:
- **(1) honesty-counter**: irrelevant if there is no promotion path (likely; literature
  reviews rarely have a "promoted-to-truth" mechanism). If a promotion path exists
  (e.g. "approved citations vs candidate citations"), constraint (1) does apply.
- **(2) write-barrier**: applies only if there is an SSOT (e.g. a citation-approval
  registry); otherwise irrelevant.
- **(3) no-fabrication guard** is *strongly load-bearing*, with the C2 (citation)
  class becoming the dominant defended class instead of C1+C3+C4 in n6 or C5 in nexus.

**Net**: (3) is the dominant component; (1) and (2) apply only conditionally on
whether a promotion path / SSOT exist within the read-only workflow.

### §4.4 Summary of counterfactual cases

| Case | Missing precondition | (1) banner | (2) write-barrier | (3) no-fab guard |
|---|---|---|---|---|
| Pair-programming, no promotion | (a) | drops | replaced by CI/review | KEEP — class C1+C3 dominant |
| SSOT = working file | (b), (c) | degenerate / coarse | impossible — replaced by transaction discipline | KEEP — class C1 dominant |
| Read-only research | (d) reduced | conditional | conditional | KEEP — class C2 dominant |

The no-fabrication guard (constraint 3) is the **only** triad component that survives
all three counterfactuals. Constraints (1) and (2) require all five preconditions; (3)
requires only (e) (LLM agents) plus a non-trivial output surface.

---

## §5 Three testable predictions for other repos

For repos that satisfy all 5 preconditions but have **different structural shapes**,
the triad ports with adaptation. Three predictions, each falsifiable.

### §5.1 Prediction P1 — Lean4 mathematics repo

**Repo type**: a Lean4 / Coq / Isabelle formal-mathematics repository where LLM agents
generate proof candidates, run the proof checker, and propose theorems for inclusion in
a curated Mathlib-style canonical library.

**Preconditions satisfied?** All 5: (a) "promoted to Mathlib" is the promotion path,
(b) Mathlib trunk is the SSOT, (c) per-PR work directories are the research layer,
(d) Lean4 kernel + tactics ecosystem produces measurable proof-status values, (e) LLM
agents generate proof candidates.

**Prediction**:
- **(1) Honesty counter** ports with adaptation. Form: `mathlib_promoted_count: N/N0
  unchanged`. *Adaptation*: the denominator is not fixed (Mathlib grows), so the form
  is delta-from-baseline (analogous to nexus's adaptation, not n6's literal `0/7`).
- **(2) Write-barrier** ports cleanly with the SSOT replaced by Mathlib trunk path
  + canonical-theorem-registry. Privileged-agent gate is the existing PR-review +
  CI-Lean-check stack, which is *stronger* than n6's atlas-agent EXACT gate (because
  the kernel itself enforces a deterministic check). Prediction: prompt-level barrier
  becomes **partially redundant** because Lean4-kernel-fail ≈ "synchronous edit-time
  defense covering the result-class" already exists. Verdict on (2) likely
  **KEEP_BUT_COMPRESS** rather than KEEP_AS_IS — the prompt-level layer adds
  in-narrative discipline but the runtime kernel covers most of (2)'s function.
- **(3) No-fabrication guard** ports verbatim. Class distribution shifts: C5 (result
  fabrication, "I proved X") is *aggressively caught by the kernel* and becomes the
  *most redundant* class; C2 (citation of theorems) becomes load-bearing because
  invented lemma names are not kernel-caught (the kernel will fail-by-name, but the
  failure mode is "lemma not found", not "fabrication detected").

**Falsifier**: if a Lean4 repo with the triad ported shows (2) is *NOT* compressible
(i.e. the prompt-level barrier catches things the kernel does not), prediction P1's
"compressible" claim is wrong.

### §5.2 Prediction P2 — Rust formal-verification repo

**Repo type**: a Rust crate with `kani` / `prusti` / `creusot` formal-verification
annotations, where LLM agents propose annotated functions, the verifier checks them,
and verified-and-reviewed annotations are merged to a canonical "verified-API" set.

**Preconditions satisfied?** All 5, with (e) split: LLM agents *generate* annotations,
deterministic verifier *checks* them.

**Prediction**:
- **(1) Honesty counter** ports cleanly with form: `verified_api_count: N/N0 unchanged`.
  Verdict: **KEEP_AS_IS at function level** (delta-from-baseline form). Closer to nexus
  than to n6.
- **(2) Write-barrier** ports with the SSOT being the verified-API registry + crate
  root. Verdict: **KEEP_AS_IS** — the prompt-level barrier is needed because the
  verifier runs on a per-function basis and does *not* gate writes to the canonical
  registry; analogous to atlas-agent EXACT-gate vs the prompt-level barrier on n6.
- **(3) No-fabrication guard** ports verbatim. Class distribution: C3 (tool —
  invented `cargo` flags, invented `kani` attributes) is HIGH because Rust's
  attribute ecosystem is rich and an LLM can plausibly invent attributes. C1 (numeric
  bounds in proof obligations) is HIGH. C4 (struct field names in `#[invariant(...)]`
  annotations) is HIGH. **All three of C1+C3+C4 are load-bearing** — closer to n6's
  distribution than to nexus's C5-heavy.

**Falsifier**: if a Rust formal-verification repo with the triad shows that the
verifier alone catches >80% of all five fabrication classes (i.e. compresses (3)), the
prediction's "verbatim port" claim is wrong.

### §5.3 Prediction P3 — Multi-author SaaS codebase

**Repo type**: a production SaaS codebase with multiple human committers, LLM
agents performing PR review / code generation / documentation, a feature-flag SSOT,
and a release-tracking registry.

**Preconditions satisfied?** Partial:
- (a) promotion path = "feature shipped to production" — yes, with the release
  registry as the marker.
- (b) SSOT = feature-flag config + release-tracking registry +
  `package.json`-equivalents — yes.
- (c) research layer = PR-branch worktrees, draft docs — yes.
- (d) tool ecosystem with measurable values — yes (CI, test results, performance
  benchmarks).
- (e) LLM agents performing research/promotion — yes, but heavily mixed with
  human commits.

The mixed-authorship is the structural variable.

**Prediction**:
- **(1) Honesty counter** ports with adaptation. Form: `feature_shipped_count_delta: 0
  unchanged-by-LLM-this-session`. *Critical refinement*: the banner must distinguish
  LLM-attributed promotions from human-attributed ones, because human commits are not
  bound by the triad. Verdict: **KEEP_BUT_ADAPT** (form B variant).
- **(2) Write-barrier** ports as a *narrower* constraint — LLM agents should not
  modify the feature-flag SSOT or release-tracking registry, but humans can (they
  pass through normal review). Verdict: **KEEP_AS_IS** with an explicit "for LLM
  agents only" scope.
- **(3) No-fabrication guard** ports verbatim. Class distribution: C2 (citation of
  package versions, of past commits, of documentation URLs) is HIGH. C4 (file paths
  / directory structure) is HIGH because production codebases have many directories
  and an LLM can claim a file at `src/utils/foo.ts` that does not exist. C3 (tool /
  CLI flags / npm scripts) is HIGH. C1 (numeric — performance numbers, version
  numbers) is MEDIUM-HIGH.

**Falsifier**: if a multi-author SaaS repo with the triad ported shows that the
LLM-vs-human attribution discipline (constraint 1's refinement) is *unenforceable*
in practice — e.g. attribution leaks across the boundary — prediction P3's "narrower
scope" claim fails and the triad either does not port or requires a more
sophisticated attribution mechanism.

### §5.4 Prediction summary table

| # | Repo type | Preconditions | (1) banner | (2) barrier | (3) no-fab | Most novel feature |
|---|---|---|---|---|---|---|
| P1 | Lean4 math | all 5, (e) split | KEEP_AS_IS / form-B | KEEP_BUT_COMPRESS | KEEP_AS_IS, C2 dominant | Kernel makes (2) partially redundant |
| P2 | Rust formal-verif | all 5 | KEEP_AS_IS / form-B | KEEP_AS_IS | KEEP_AS_IS, C1+C3+C4 dominant | Verifier scoped to functions, not registry |
| P3 | Multi-author SaaS | all 5, mixed | KEEP_BUT_ADAPT (LLM-scoped) | KEEP_AS_IS (LLM-scoped) | KEEP_AS_IS, C2+C3+C4 dominant | Attribution discipline (LLM vs human) |

---

## §6 Limitations of this synthesis

The synthesis itself has clear limits. Acknowledging them is itself an instance of
constraint (3) (no-fabrication: do not over-claim universality from n=2).

### §6.1 n=2 repos is small

The 6-of-6 result is across **two repos only** (n6-architecture and nexus). A sample
of two cannot establish strong cross-repo invariance; it can only establish that the
pattern holds in two cases and is *not falsified* by either. Predictions P1-P3 (§5)
are projections, not observations.

### §6.2 Both repos share a design philosophy (omega-cycle / Ω-saturation)

Both n6 and nexus were constructed under the same author (the user) using the omega-
cycle methodology and the Ω-saturation discipline. The two repos are not independent
in the way a Lean4 community repo and a Rust SaaS codebase would be. Selection bias is
real: the audits were *designed* under a methodological lens that makes the triad
appear natural. A Lean4 / Rust / SaaS repo authored under different cultural
assumptions might not satisfy precondition (e)'s function (LLM-agent discipline as a
designed object) even if they technically satisfy it (LLMs are present).

### §6.3 The audit framework is itself an artifact of n6 work

The 6-field audit framework (saturation × incident chain × redundancy matrix ×
counterfactual × cost × verdict) was developed in the n6 omega-cycle audits and then
applied to nexus. The framework is not repo-neutral by construction; it was *generalized*
from n6 to nexus. A third application would need to verify that the framework itself
generalizes, not just the verdicts (the nexus-native audit's §6 qualifications already
flag this — "redundancy matrix structure on nexus slightly thinner due to absent
`.claude/agents/*.md` definitions and absent Y9-analogue").

### §6.4 Time window is short (14-30 days per repo)

The n6 audits sample a 14-day window for incident chains; the nexus audit samples 14
days. A 90-day or 365-day window might surface different incident classes (e.g.
slow-drift fabrications, multi-cycle citation slips) that the current sample misses.
Each parent audit explicitly flags this in its falsifier section (e.g. honesty-counter
audit F-AUDIT-1: "30-day audit window... if zero near-misses caught by the banner that
were not also caught by Y9 within ≤24 hours").

### §6.5 Predictions are not yet tested

P1-P3 are *predictions*, not measurements. They are listed as falsifiable so future
work (an actual port to a Lean4 / Rust / SaaS repo) can confirm or refute them. The
synthesis does not claim P1-P3 are correct; it claims they are *coherent extrapolations
from the n6+nexus pair*.

### §6.6 The "function vs. literal" distinction is a tool, not a verdict

The 6-of-6 result distinguishes *function-level* agreement (3-of-3 across both repos)
from *literal-text* agreement (5-of-6, with n6's `0/7` literal not transferring to
nexus). The function-level reading is the load-bearing one for synthesis purposes, but
some readers may correctly object that "function-level" is doing a lot of work.
Acknowledged: the distinction is robust here (continuous vs. fixed denominator is a
clean axis) but may not always be in other cases.

---

## §7 Anti-list — patterns considered and rejected

Patterns that were considered as candidate generic forms but were rejected for being
either too narrow (over-fitted to n6+nexus details) or too broad (would apply to
workflows lacking the preconditions). Each is logged so future synthesis attempts do
not re-attempt them.

- **AL1 — "the literal `0/7` is the universal counter"**. *Rejected*: it is an
  n6-millennium-specific denominator; nexus's continuous-denominator analogue (form B,
  `nxs_promotion_count: N/N0`) is structurally homologous but literally divergent.
  (Cite: porting audit §3.1, §5.1; nexus-native §2.1.) Universal forms must be
  function-level, not literal.
- **AL2 — "the protected path list is universal"**. *Rejected*: n6 protects
  `atlas/`, `state/`, `state/proposals/inventory.json`,
  `theory/breakthroughs/breakthrough-theorems.md`. Nexus protects
  `n6/atlas.blowup.jsonl`, `state/proposals/inventory.json`,
  `state/atlas_health_timeline.jsonl`, `state/agent_lock_ledger.jsonl`,
  `lenses/omega_state_space_lens.hexa`, `project-claude/*.md`. The path lists do not
  intersect except in spirit. Universal write-barriers must abstract over the path
  list.
- **AL3 — "atlas-agent / EXACT gate / privileged-agent map is universal"**. *Rejected*:
  n6 has `.claude/agents/atlas-agent/AGENT.md`; nexus has only `safe-commit.md`. Same
  privileged-agent function is implemented via different mechanism on nexus
  (runtime tools `lockdown_gate.hexa` + `harness/` modules). Universal triad must
  not depend on `.claude/agents/*.md` definitions specifically.
- **AL4 — "Y9 HONEST-HARNESS / cycle-N / falsifier-pre-registration as a *fourth*
  triad component"**. *Rejected*: each of Y9 (n6) and cycle-N (nexus) is a
  *post-hoc* discipline, not a synchronous edit-time gate. Triad components (1)+(2)+(3)
  are all synchronous, agent-prompt-level. Adding a 4th post-hoc component would
  conflate two enforcement timings. (The post-hoc disciplines exist and are
  load-bearing in §5 redundancy matrices but are *complements* to the triad, not part
  of it.)
- **AL5 — "the 12-rung omega ladder is the universal occupancy axis"**. *Rejected*:
  the ladder is internal to the omega-cycle methodology shared by n6 and nexus. Other
  repos (Lean4, Rust, SaaS in P1-P3) do not have a 12-rung abstraction ladder.
  Universal preconditions must be ladder-independent.
- **AL6 — "treat the triad as a 6-tuple of (constraint × repo)"**. *Rejected*: the
  6-of-6 count is a *result*, not a structure. The triad is a 3-tuple of constraints
  (function-level), with each constraint instantiated per repo. Conflating the result
  count with the structure inflates the apparent dimensionality.
- **AL7 — "expand the triad to include 'cross-repo verification discipline' as
  constraint (4)"**. *Rejected*: cross-repo verification is what the porting audit and
  nexus-native audit *did*; it is meta-process about the triad, not a triad component.
  Including it would fold the auditor's own discipline into the auditee, breaking
  separation.
- **AL8 — "the triad implies a particular agent ecosystem (e.g. atlas-agent +
  growth-agent + lens-agent)"**. *Rejected*: nexus's structural divergence on (e)
  (runtime tools instead of `.md` agents) explicitly demonstrates that the agent
  ecosystem can vary widely while preserving the function. Universal triad must
  abstract over agent-ecosystem details.
- **AL9 — "literal `0/7` should be globally banned and replaced with a
  domain-neutral counter"**. *Rejected*: the literal `0/7` IS load-bearing within n6
  because the millennium-7 denominator is a culturally-recognized clamp. Domain-
  neutralizing it would weaken its psychological force on the n6 reader. The triad
  pattern is "function-level invariant, literal-level adapt"; not "literal-level
  enforce a single shared form".
- **AL10 — "make the synthesis itself a deployable spec for new repos"**. *Rejected*
  per the prompt's hard constraint (synthesis-only, not deployment). The
  generic pattern in §3 is text-only; deploying it to any new repo requires a
  separate audit verifying the 5 preconditions, an adaptation pass, and explicit user
  authorization in that repo's context.

---

## §8 Falsifiers active for the synthesis itself

The synthesis claims (REPO_INVARIANT, 5 preconditions, generic pattern in §3,
counterfactuals in §4, predictions in §5) are **voided** if any of the following later
trips:

- **F-SYN-1 (parent verdict reversal)**: if any of the 6 parent audits later returns a
  changed verdict (e.g. n6 honesty-counter F-AUDIT-3 fires and verdict drops to
  KEEP_BUT_COMPRESS), the 6-of-6 count fails and the synthesis must be re-evaluated.
  The synthesis inherits **all** falsifier dependencies of all 6 parent reports.
- **F-SYN-2 (third-repo audit returning RETIRE)**: if a future audit on a third repo
  satisfying all 5 preconditions returns a RETIRE verdict on any of the 3 constraints,
  the REPO_INVARIANT claim is refuted by counterexample.
- **F-SYN-3 (precondition under-determination)**: if a future case shows a workflow
  satisfying all 5 preconditions but where the triad is *not* load-bearing (e.g. all
  three constraints return KEEP_BUT_COMPRESS or RETIRE), the preconditions are
  necessary but not sufficient. §2 must be expanded with additional preconditions.
- **F-SYN-4 (counterfactual case violated)**: if a workflow lacking precondition (a) /
  (b) / (d) is shown to have the triad applying *anyway* (e.g. a pure pair-programming
  workflow benefits from constraint (1) for some reason §4.1 misses), §4 is wrong and
  the counterfactual cases are not as cleanly separated as claimed.
- **F-SYN-5 (P1 / P2 / P3 prediction-falsified)**: if any of P1-P3 is tested by an
  actual port and falsified at its named falsifier (Lean4 (2) is NOT compressible /
  Rust verifier covers >80% of fabrication classes / SaaS attribution discipline is
  unenforceable), the corresponding prediction is wrong. A single P-failure does not
  void the synthesis but reduces extrapolation confidence; two or more P-failures
  reopen the synthesis.
- **F-SYN-6 (n=2 selection bias)**: if a future independent analysis demonstrates
  that the 6-of-6 result is an artefact of shared design philosophy (omega-cycle /
  Ω-saturation methodology) rather than of the triad's intrinsic portability, the
  synthesis's universality claim is reduced to "the triad is invariant *within*
  omega-cycle workflows" — a much narrower claim.
- **F-SYN-7 (framework category error)**: if the 6-field audit framework
  (saturation × incident-chain × redundancy × counterfactual × cost × verdict)
  is later shown to be mis-fit for some workflow class — i.e. the framework itself
  generates spurious KEEP-direction verdicts because of how it weights its inputs —
  the synthesis's reliance on parent-audit verdicts is undermined. Mirrors n6's
  F-A6 in the no-fabrication audit and the nexus-native F-NXV-7.
- **F-SYN-OMEGA (meta)**: if any future independent meta-audit on this synthesis
  itself (e.g. a critique of its precondition list, its counterfactual cases, or its
  predictions) returns a substantively different conclusion, this report re-opens.

None of F-SYN-1..7 or F-SYN-OMEGA have fired as of this report's write-time. They are
listed as future-trigger conditions only.

---

## §9 Closing

0/7 unchanged. nxs promotion count unchanged. **No atlas/state/inventory edits in
either repo.** No CLAUDE.md changes. No `.claude/agents/*` changes. The single output
file is this report under
`/Users/ghost/core/n6-architecture/reports/sessions/omega-meta-synthesis-repo-invariant-honesty-audit-2026-04-25.md`.

Synthesis result:

- **6-of-6 KEEP-direction across n6+nexus** (3-of-3 function-level agreement; one
  literal-level adaptation on constraint 1).
- **REPO_INVARIANT** (cite: nexus-native audit §6) confirmed under the 5-precondition
  characterization (§2): promotion-path × SSOT × research-layer × tool-ecosystem ×
  LLM-agents.
- **Generic portable triad pattern** (§3) abstracted from the n6+nexus instances, with
  text-only spec for the three constraints.
- **Three counterfactual cases** (§4) where the triad does not apply or applies
  partially: pair-programming-no-promotion, SSOT-is-working-file, read-only-research.
- **Three testable predictions** (§5) for hypothetical Lean4 / Rust / SaaS repos, each
  with explicit falsifiers.
- **Limitations** (§6) — n=2 sample, shared design philosophy (omega-cycle), framework
  is itself an n6 artefact, 14-30-day window, predictions untested.
- **Anti-list** (§7) of 10 over-narrow / over-broad pattern candidates rejected.
- **Falsifiers** (§8) for the synthesis itself.

This document does **not** propose deploying the triad to any third repo. It
characterizes when the triad applies and predicts how it would adapt; deployment
requires a separate per-repo audit verifying the 5 preconditions, plus explicit user
authorization in that repo's context.

millennium_resolved: **0/7** (unchanged).
nxs_promotion_count: **unchanged this session** (no inventory writes).
NO atlas/state/inventory edits in n6 or nexus. NO CLAUDE.md changes.
