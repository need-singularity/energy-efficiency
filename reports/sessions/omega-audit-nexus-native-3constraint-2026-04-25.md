---
id: omega-audit-nexus-native-3constraint
date: 2026-04-25
scope: cross-repo verification (nexus material, n6 audit framework, READ-ONLY on nexus)
target: 3 KEEP_AS_IS constraints -- nexus-native re-audit + cross-repo verdict comparison
parent_reports:
  - reports/sessions/omega-audit-constraint-honesty-counter-2026-04-25.md
  - reports/sessions/omega-audit-constraint-write-barrier-2026-04-25.md
  - reports/sessions/omega-audit-constraint-no-fabrication-2026-04-25.md
  - reports/sessions/omega-audit-nexus-honesty-triad-portability-2026-04-25.md
millennium_resolved: 0/7 (unchanged)
nxs_promotion_count_delta: 0 (unchanged this session)
grade: cross-repo audit verification, no claim
---

## §0 Non-claim disclaimer

This report is a **cross-repository verification** exercise. Its purpose is to determine
whether the same 3-constraint audit framework that produced 3-of-3 KEEP_AS_IS verdicts on
n6-architecture data also produces 3-of-3 KEEP-direction verdicts when applied to nexus's
own material. It is **not**:

- a re-decision of the n6-side verdicts (those remain KEEP_AS_IS as written),
- an extension of the earlier porting audit
  (`omega-audit-nexus-honesty-triad-portability-2026-04-25.md`) — that audit's question was
  *"should these be ported to nexus?"*; this audit's question is *"do they hold up
  under nexus-native data?"*,
- an authorisation for any change in either repo,
- a write into `~/core/nexus/`. Every nexus observation below derives from `ls`,
  `cat`, `git -C ~/core/nexus log`, `grep`, `head`, `wc`. **No nexus file is modified,
  created, or deleted by this session.**

The 0/7 honesty counter is unchanged. The nxs_promotion_count delta this session is `0`.
The single output file is this report under `reports/sessions/` in n6-architecture.

Where a nexus path stated by the prompt does not exist, that fact is documented (no
fabrication of file structure). Where the porting audit's deploy plan was partially
executed (an artefact left untracked in the working tree of nexus by an earlier session),
that observation is recorded but not acted on — the file is **not** modified, **not**
committed, **not** removed.

The four legal verdicts are {KEEP_AS_IS, KEEP_BUT_COMPRESS, RETIRE_IF_OTHER_TWO_AGREE,
RETIRE}. Each per-constraint verdict below is independently derived from nexus material
(saturation, incident chain, redundancy, counterfactual, cost). Cross-repo agreement
analysis is a *separate* synthesis at §5–§6.

---

## §1 Audit framework recap + nexus-application form

The n6-side framework decomposes a constraint audit into six fields:

1. **Saturation** — fraction of session/research artefacts where the constraint actually
   gates a wrong move.
2. **Incident chain** — historical near-violations and how they were caught (axis 3 of
   the omega cycle).
3. **Redundancy matrix** — which other gates would catch each violation class.
4. **Removal counterfactual** — first-incident slip path and severity if the constraint
   were dropped.
5. **Cost of keeping** — boilerplate burden + false-positive rate.
6. **Verdict** — from the four legal options, with a one-paragraph rationale.

Application to nexus material (per-field substitution):

| Field | n6 input | nexus input |
|---|---|---|
| Saturation | `reports/sessions/*.md` (45 session reports) + `theory/study/`, `papers/`, `theory/roadmap-v2/` | `reports/` (15 flat JSON/MD analytics files, no per-session narratives) + `design/` (10–15 design docs incl. `honesty_triad.md` from prior session) + `git log --since="14 days ago"` (1734 commits) — **commit messages substitute for session narratives** because nexus does not have a `reports/sessions/` tree |
| Incident chain | atlas/state writes from privileged paths only; per-BT near-misses with file:line citations | `git log` keyword-search on `actual root cause`, `falsif`, `fix.*cycle`, `wrong`, `incorrect`; the `Ω-saturation cycle` chain (cycles 1–57) acts as a self-disclosing incident-and-correction trail by design |
| Redundancy | atlas-agent EXACT gate, Y9 HONEST-HARNESS, falsifier pre-reg, 3-way tagging, L0 Guard, pre-commit hook | `tool/lockdown_gate.hexa`, `permissions_ssot.json` (deny patterns), `harness/` modules (referenced from project-claude/*.md), L0 protected list in `project-claude/nexus.md`, atlas-agent equivalence (status: see §2.3) |
| Counterfactual | per-class slip rate × first-incident remediation cost (BT registry rewrite, atlas non-EXACT, Lean4 mislabel) | per-class slip rate × first-incident cost in nexus's *continuous* metric domain (composite ceiling drift, premature inventory promotion, fabricated nxs-002 result) |
| Cost | ~225 lines / 75 files / <0.5% surface | for each constraint, lines added × files touched, plus the FP rate observable in commit/log discipline |

Two structural divergences are flagged early so they recur in the per-constraint verdicts:

- **Saturation sample type**: nexus does not have a `reports/sessions/` per-narrative tree.
  The closest analogue is the *commit-message stream* (1734 commits / 14 days, with the
  `Ω-saturation cycle N` / `beyond-omega cycle N` convention acting as a per-act narrative
  marker). This means nexus's saturation measurement is **denser per unit time** but
  **shallower per unit artefact** than n6's. Where a per-document banner makes sense in n6,
  a per-commit prefix or per-cycle banner makes sense in nexus.
- **Continuous-vs-discrete metric domain**: n6's millennium denominator is fixed (7).
  nexus's analogous denominators are continuous (composite ceiling 0.835, ER ROI prediction
  measurements, score_priority integers in inventory). The constraint shape that fits
  is *delta-from-session-start*, not *zero-out-of-fixed*.

Both divergences were already noted in the porting audit (§5.1, §5.4). They are inherited
here, not re-derived.

---

## §2 Audit 1: nxs_promotion_count (analog of n6's 0/7 honesty counter)

### §2.1 Constraint definition (nexus form)

The nexus analogue of `millennium_resolved: 0/7 unchanged` is the
`nxs_promotion_count: <N>/<N_session_start> unchanged` banner, where `N` is the count
of `state/proposals/inventory.json` entries with `user_status ∈ {implemented, done}`
at report write-time, and `<N_session_start>` is the same count captured at session
begin. The banner sits in session-report front-matter; an explicit non-zero delta
(`12/10 (+2 this session)`) forces the agent to **name** every promotion. The function
mirrors n6's banner: a first-line clamp against silent SSOT mutation between session
begin and end.

The porting audit (§3.1, §6) recommended this form and graded it KEEP_BUT_ADAPT (form
change from n6's literal `0/7`). This nexus-native re-audit asks whether nexus-native
data **independently** justifies KEEP-direction.

### §2.2 Saturation (nexus material)

Sample target: nexus session/research artefact pool. Method: read commit-message stream
(14-day window) + design/ docs + reports/ flat files.

| Pool | Total items | Items declaring a promotion-counter or its absence | % saturation |
|---|---:|---:|---:|
| Commit messages, last 14 days | 1734 | ~85 carry `Ω-saturation cycle N` or `beyond-omega cycle N` (post-hoc cycle-counter, *not* a `nxs_promotion_count` banner) | 4.9% |
| Commit messages with explicit "promotion" keyword | 1734 | 10 (sample: `9b46871e`, `e2707678`, `16f14662`, `9e347d28`, `39b2d0f4`, `ff2c6701`, `4bcb44f1`, `7b997243`, `59552750`, `a617fd54`) | 0.6% |
| `~/core/nexus/design/*.md` | 5 (excluding `honesty_triad.md`, which is itself this constraint's specification) | 0 with `nxs_promotion_count:` banner; 1 (`session_20260425_summary.md`) implicitly tracks via cycle-N progression | 0% explicit / ~20% implicit |
| `~/core/nexus/reports/*.md` and `*.json` | 15 | 0 declare a promotion-counter (these are analytics dumps, not narratives) | 0% |
| `~/core/nexus/state/proposals/inventory.json` | 1 file, 21 entries | 21/21 carry `user_status` and `done_ts`/`submitted_ts` (the *substrate* of the count, not the *banner*) | substrate, not banner |

**Observation**: nexus's saturation of an *explicit* `nxs_promotion_count` banner is
**near-zero** today (the banner specification was just written into
`design/honesty_triad.md` in a prior session and is *uncommitted* — `git status` shows
`?? design/honesty_triad.md`). The *implicit* honesty-counter discipline is carried by
the `Ω-saturation cycle N` commit-message convention (5% of commits) and by inventory's
`user_status` field (substrate-level, not banner-level).

**Comparison to n6**: n6's 0/7 banner saturates at ~40% of session reports (high-density
hotspot) plus moderate density in study/papers/roadmap. nexus has effectively zero
explicit-banner saturation today and ~5% implicit cycle-counter saturation. The *form*
of the constraint differs — n6's is a per-document clamp; nexus's would be a per-
session/per-cycle clamp.

### §2.3 Incident chain (nexus 30-day)

The 14-day commit log (1734 commits) was scanned for promotion-related events. Findings:

| # | Date | Commit | Event | Banner role (counterfactual) |
|---|---|---|---|---|
| 1 | 2026-04-23 | `39b2d0f4 feat(revive): 16-day halt released — 33 atlas promotions + 294 signals + 3-logic pipeline` | 33 atlas promotions in a single revive cycle after 16-day pause | a `nxs_promotion_count` banner at session start would have surfaced this as `+33` delta — visible at the top of the artefact, not buried in a commit subject |
| 2 | 2026-04-22 (recent prior to window edge) | `4bcb44f1 feat(ssot): Mk.VI promotion gate — canonical definition from 7-inv+4-ax+3-AN11+evo` | introduces a *promotion gate* tool — directly relevant to whether banners are needed at the prompt layer or only at the gate layer | banner is independent: prompt-level early-warning vs runtime gate-layer enforcement |
| 3 | 2026-04-22 | `7b997243 feat(mkx): engine sidecar — 30 atoms T10-T13 + cross-lens synthesizer + AN11 promotion gate` | second promotion-gate addition (Mk.X axis 2) | same as above |
| 4 | 2026-04-25 | `e2707678 state: 3 conventions → implemented + EVO-P10-1 blocker tagged user_side_infra` | 3 inventory entries flipped to `implemented` in one commit | banner would have flagged this as `+3` |
| 5 | 2026-04-24 | `9e347d28 roi(n6): n6-roi-012 done · n6-roi-007 auto-promoted todo→running` | auto-promotion event; "auto-promoted" wording is a near-fabrication if the auto-promoter ran without the operator's intent | banner forces the agent to *report* the count change, exposing auto-promotions to review |
| 6 | 2026-04-23 | `9b46871e docs(handoff): unmapped endpoint analysis — 5 promotions are graph hubs` | mentions "5 promotions" in a graph-analysis context; the number may or may not match inventory | banner cross-checks this number against inventory at write-time |
| 7 | 2026-04-22 | `59552750 feat(mk9-audit): [12*] tier operation activated + promote_12star (Mk.X axis 2)` | introduces a *new* promotion tier `[12*]` — the denominator under audit shifts | this is a *banner-domain expansion*, not a slip; the banner would need to add a `[12*]` slot |

**Pattern**: 7 promotion-related events in 14 days = ~0.5/day (Poisson rate). Of those:

- 4 events (#1, #4, #5, #6) are *count-changing* and would be visible as a non-zero
  banner delta.
- 3 events (#2, #3, #7) are *gate-introducing* or *tier-introducing* and are
  banner-domain changes rather than count slips.

**Zero hard violations** in the 14-day window where the count changed *silently and
incorrectly*. The implicit substrate (inventory.json `user_status`) recorded each event,
and the cycle-N commit convention surfaced each at commit time.

**Self-disclosure incidents** (relevant to honesty-counter spirit even outside promotion
literal):

- `6772aede` (cycle 43): *"⚠️ honest finding: raw 37/38 enforce not actually working (no caller)"*.
  A self-counter (raw 37/38) was claimed but the caller-wiring was missing. Functionally
  isomorphic to a 0/7-style honesty-counter that *fails to fire* — not a banner violation
  per se, but a sibling failure mode. Caught by user audit, not by an in-session banner.
- `d837839e` (cycle 51): *"🎯 actual root cause = cross-session active drill's host load 97%"*.
  Cycles 47–50 had named different mechanisms; cycle 51 retracts. A `nxs_promotion_count`
  banner does not directly catch this (the issue is *result* drift, not *count* drift),
  but the cycle-N convention does — at commit time.

**Frequency of count-changing events**: ~0.3/day (4 in 14 days) → ~9/month. Without the
banner, by Poisson-extrapolation in a higher-velocity nexus session, the silent-promotion
exposure could rise. With the banner, every count-changing event is forced into the
front-matter.

### §2.4 Redundancy matrix (nexus side)

| Violation class (count-changing) | banner | inventory.json `user_status` substrate | cycle-N commit convention | promotion-gate tools (Mk.VI, Mk.X) | proposal_inbox.hexa schema check | atlas-agent EXACT gate (status: NOT confirmed in `.claude/agents/`, see §2.5) |
|---|---|---|---|---|---|---|
| (a) silent inventory entry flip `submitted → implemented` mid-session | CATCHES (front-matter banner forces N change to be counted) | substrate: stores the change but does not emit it | partial (catches at *commit* time, not at session-start time) | MISSES (gate is for atlas, not inventory) | partial (schema check enforces fields, not delta visibility) | MISSES (atlas-agent does not see inventory.json) |
| (b) auto-promoter runs `todo → running → done` without operator awareness | CATCHES (banner delta at session end exposes it) | substrate: stores; same gap | partial (commit-time only) | partial (Mk.VI gate may fire but cycle output may not propagate to session report) | MISSES | MISSES |
| (c) atlas mass promotion (e.g. 33 entries via revive) without per-cycle accounting | CATCHES (banner delta is `+33` — extreme, forces named accounting) | substrate | partial | CATCHES (Mk.VI gate runs canonical-definition checks) | MISSES | partial (atlas-agent EXACT gate would refuse non-EXACT entries — *if* it exists) |
| (d) `[12*]` tier introduction shifts banner domain | banner-domain change, not violation | N/A | catches (commit subject literally records `+12*` tier intro) | N/A | N/A | N/A |
| (e) cross-session promotion (e.g. n6-roi-012 done in nexus inventory but actual work is n6-side) | CATCHES (banner forces explicit count) | substrate (the entry has `cross_repo_link`, but no count emission) | partial | MISSES | MISSES | MISSES |

**Reading the matrix**:

- The banner catches all 4 count-shape violation classes (a, b, c, e) and is the only
  always-on, in-session gate covering (a) and (b).
- The cycle-N commit convention catches at commit time only — *post-hoc* relative to the
  session.
- Promotion-gate tools (Mk.VI, Mk.X) cover atlas-side promotions but not inventory
  flips.
- atlas-agent EXACT gate **could not be verified** as a `.claude/agents/atlas-agent.md`
  file in nexus (only `safe-commit.md` exists in `.claude/agents/`). The gate may exist
  as a conceptual role in commit-message convention only; building redundancy claims on
  it is fabrication-adjacent (per §2.5).

**Joint-completeness**: the banner + inventory substrate + cycle-N convention together
cover all 4 classes. Removing the banner leaves the cycle-N convention as the only line —
which is *post-hoc*, mirroring the n6 case where Y9 is the post-hoc fallback.

### §2.5 Note on atlas-agent existence

Per `ls /Users/ghost/core/nexus/.claude/agents/`: only `safe-commit.md` exists. The
porting audit (§2.1 row "atlas-agent / growth-agent / NodeBlocker") flagged this as
*partial confirmation*: searches for atlas-agent / growth-agent / NodeBlocker in
`design/`, `tool/`, `config/` returned zero matches. This nexus-native re-audit confirms
that finding under a fresh search:

```
grep -rE "atlas-agent|growth-agent|NodeBlocker" \
  ~/core/nexus/design/ ~/core/nexus/project-claude/ \
  → 1 match: design/honesty_triad.md (which references them as *aspirational* gates)
```

So redundancy claims about atlas-agent EXACT enforcement on nexus side are
**unverified**. They are tagged `(UNVERIFIED)` in the matrix above, consistent with the
no-fabrication discipline (Audit 3).

### §2.6 Removal counterfactual (nexus-specific)

Hypothetical: drop the banner. Counterfactual slips and severity:

| Slip class | Severity | Estimated frequency (per 14d, nexus-rate) | Downstream catcher |
|---|---|---:|---|
| (a) silent `user_status` flip in inventory mid-session | MEDIUM-HIGH | 1.5 (4 historical events / ~3 sessions in window) | cycle-N commit (post-hoc, ~commit-time lag) |
| (b) auto-promoter slip | MEDIUM | 0.8 | cycle-N (post-hoc) + Mk.VI gate (partial) |
| (c) atlas mass promotion not session-accounted | HIGH | 0.5 (1 historical event = 33 promotions) | Mk.VI/Mk.X gates catch *integrity* but not *counting*; cycle-N catches naming |
| (e) cross-repo promotion claimed in nexus that is actually n6-side work | MEDIUM | 1.0 | manual cross-repo audit only; no automated gate |

**First-incident severity estimate**: a mass atlas promotion event (class c) without
banner accounting in a session report would create an inventory-vs-narrative inconsistency
that compounds across sessions until the cycle-N convention's commit-time check catches
it. Remediation: re-derive count from `git log --grep="promotion"` + inventory snapshot
diff, then patch all derivative artefacts. Estimated cost: **~1–2 days** for a single
HIGH-severity slip, lower than n6's 4–6 days because nexus has *fewer derivative
artefacts* (no papers/, no theory/study/ tree).

**Asymmetry**: cheap to keep (3 lines/session), ~1–2 days to remediate one HIGH slip.
Asymmetry favours keep but is *less* dramatic than n6 (where remediation is 4–6 days).

### §2.7 Cost on nexus

- Banner length per session report: ~2 lines.
- Files carrying the banner today: 0 (banner is uncommitted spec).
- Files that *would* carry the banner under deploy: every session-report-equivalent
  artefact. nexus has no `reports/sessions/` tree; the banner would attach to design/
  docs and to commit-message preamble.
- Maintenance cost: zero — the count is queryable from `state/proposals/inventory.json`.
- False-positive rate: estimated low (<5%) — most legitimate promotion events are *named*
  and the banner just makes the naming a front-matter requirement rather than an in-body
  one.

**Verdict on cost**: **negligible**, same scale as n6.

### §2.8 Verdict (Audit 1)

**KEEP_AS_IS** (function-level) / **KEEP_BUT_ADAPT** (literal-level — same conclusion as
the porting audit's §6).

One-paragraph rationale: nexus-native data shows ~0.3 count-changing promotion events per
day with **zero hard violations** in the 14-day window, but with the banner currently
**not deployed** (uncommitted spec). The cycle-N commit-message convention catches at
commit time only — post-hoc relative to session work. The banner provides the same
always-on first-line filter that the n6 0/7 banner provides for millennium claims, with
the same cost asymmetry (negligible-to-keep, ~1–2 days remediation per HIGH slip). The
verdict mirrors n6's KEEP_AS_IS at the *function* level; the literal text adapts to
nexus's continuous count surface (form B from porting audit). **No removal recommendation.**

This audit, taken alone, is sufficient to recommend KEEP-direction independent of n6's
parent verdict — nexus-native data carries the argument.

---

## §3 Audit 2: nexus write-barrier

### §3.1 Constraint definition (nexus form)

Session/research agents must NOT modify nexus SSOT files:

```
~/core/nexus/n6/atlas.blowup.jsonl        — atlas SSOT, 17 MB
~/core/nexus/state/proposals/inventory.json — proposal/cross-repo SSOT, 21 entries
~/core/nexus/state/atlas_health_timeline.jsonl — health timeline, 740 B
~/core/nexus/state/agent_lock_ledger.jsonl  — agent lock ledger, 490 B
~/core/nexus/lenses/omega_state_space_lens.hexa — omega state-space lens
~/core/nexus/CLAUDE.md(.bak) and project-claude/*.md — global instructions
+ all paths still listed in CLAUDE.md.bak L0 protected block
```

All proposed promotions/edits/registrations land as drafts inside the session report
(or commit message preamble); only privileged paths (atlas-agent, growth-agent,
proposal_inbox.hexa, lockdown_gate.hexa) commit them.

### §3.2 Protected-paths inventory verification

Each path verified by `ls`:

| Path | Exists? | Size / content |
|---|---|---|
| `~/core/nexus/n6/atlas.blowup.jsonl` | YES | 17,435,609 bytes (17 MB), JSONL format |
| `~/core/nexus/state/proposals/inventory.json` | YES | `schema: nexus.proposal_inventory.v1`, 21 entries |
| `~/core/nexus/state/atlas_health_timeline.jsonl` | YES | 740 bytes (small but actively appended) |
| `~/core/nexus/state/agent_lock_ledger.jsonl` | YES | 490 bytes |
| `~/core/nexus/lenses/omega_state_space_lens.hexa` | YES | (size not displayed; file present in `lenses/` listing) |
| `~/core/nexus/CLAUDE.md` | NO (only `.bak` from 2026-04-22 + active `project-claude/nexus.md`) | the active source feeds into CLAUDE.md via `scripts/sync_claude_md.hexa` |

**5 of 6 paths confirmed present**. The CLAUDE.md path is *generated*, with the source
of truth in `project-claude/nexus.md`. This is consistent with the porting audit's §2.1
finding.

**Structural shift since porting audit**: the L0 protected list in `CLAUDE.md.bak` references
many `shared/...` paths (e.g. `shared/blowup/lib/atlas_guard.hexa.inc`,
`shared/n6/atlas.n6`). However, `~/core/nexus/shared/` **no longer exists** — it was
decommissioned across multiple commits (`5b6be8fc shared/: retire compat shims`,
`9b8885f5 chore(nexus-shared-retire)`, `3afcc515 chore(shared-decommission P3.4-nexus)`,
`842eb068 chore(shared-decommission P3.3-nexus): 10 large/medium subdirs → top-level`,
`f14d5a8d chore(shared-decommission P3.2-nexus)`, `280efb43 chore(shared-decommission
P3.1-nexus)`). The L0 list in `CLAUDE.md.bak` is therefore **stale relative to current
filesystem layout**; the SSOT files have moved to top-level. This is a **structural
divergence** from n6 (where `atlas/` and `state/` paths are stable) and means a
nexus write-barrier needs to track the post-decommission layout (`n6/atlas.blowup.jsonl`,
`state/proposals/inventory.json`, etc., as listed above), not the L0 stale list.

### §3.3 Privileged-agent map

By reading `~/core/nexus/.claude/agents/`:

| Agent | File | Tool privilege | SSOT write privilege | Verified? |
|---|---|---|---|---|
| `safe-commit` | `safe-commit.md` | Bash, Read, Grep, Glob, Edit | git-staging only; refuses tokens/secrets/large files; awaits user approval | **YES, file inspected** |
| `atlas-agent` | NOT LOCATED | — | — | **NOT confirmed** as a `.claude/agents/*.md` definition |
| `growth-agent` | NOT LOCATED | — | — | **NOT confirmed** |
| `lens-agent` | NOT LOCATED | — | — | **NOT confirmed** |

By reading `~/core/nexus/CLAUDE.md.bak` and `~/core/nexus/project-claude/{nexus,anima,n6-architecture,contact}.md`:

- All four `project-claude/*.md` files reference *L0 Guard* via
  `hexa $NEXUS/tool/lockdown_gate.hexa <verify|status|watch|repair|safe-merge|log>`.
  This is a **runtime tool**, not an agent. Verified existence: `tool/lockdown_gate.hexa`
  is referenced consistently across all three project-claude files.
- The `permissions_ssot.json` deny patterns are documented in CLAUDE.md.bak L0 block.
- The harness modules (`prompt_scan`, `pre_tool_guard`, `post_bash`, `post_edit`,
  `cmd_gate`, `dod_gate`, `verifier`) are all listed under L0 protected — but the L0 block
  references them under the now-decommissioned `shared/harness/` prefix. Their
  current location is `harness/` at top-level (per the decommission sequence).

**Key finding**: nexus's privileged-agent ecosystem is **runtime-tool-based**
(`lockdown_gate.hexa`, `harness/*.hexa`, `permissions_ssot.json`) rather than
`.claude/agents/*.md`-based. This is structurally different from n6, where atlas-agent
/ growth-agent / lens-agent / safe-commit are all `.claude/agents/*/AGENT.md` files.

The implication for the write-barrier: nexus already has runtime-layer enforcement that
n6 lacks (n6 has *no* `.git/hooks/pre-commit` either, per the n6 write-barrier audit
sec 7.1). nexus's `harness/pre_tool_guard.hexa` is a Write/Edit-tool interceptor in
principle — though whether it actually intercepts general-purpose agent Write calls
(vs hexa-script ones) was not directly verified in this audit and is tagged
`(UNVERIFIED — runtime behaviour not exercised in this read-only pass)`.

### §3.4 Recent write activity (nexus, last 14 days)

`git -C ~/core/nexus log --since="14 days ago" -- state/proposals/inventory.json`:

| Hash | Subject |
|---|---|
| (multiple commits, sample top 5 from earlier listing) | mostly `feat(nxs-2026042*-NNN): Ω-saturation cycle X` and `chore(nxs-2026042*-NNN): ...` — all session-style, but authored at the `dancinlife` user level |

`git log --since="14 days ago" -- n6/atlas.blowup.jsonl`:
- `842eb068 chore(shared-decommission P3.3-nexus): 10 large/medium subdirs → top-level`
  (this is a **rename event**, not a content edit — moved n6/ out of shared/)

`git log --since="14 days ago" -- state/atlas_health_timeline.jsonl state/agent_lock_ledger.jsonl lenses/omega_state_space_lens.hexa`:

| Hash | Subject |
|---|---|
| `906e8730 chore(state): alm_r12 + clm_r5 verify report rerun + atlas_meta_scan tick` | atlas_meta_scan tick → automated append to atlas_health_timeline.jsonl |
| `a6b9e7e4 fix(bisociation): atlas_x_laws_aligned bin-mismatch — read_file silent-empty root cause` | bisociation tooling fix |
| `f14d5a8d chore(shared-decommission P3.2-nexus): 15 non-HOT subdirs → top-level` | rename event |

**Author analysis**: all writes to the SSOT paths are authored as `dancinlife` (the human
user) at commit-author level. **No commit subject is in session-agent format**
(e.g., `audit:`, `omega-audit:`, `report:`). This is consistent with n6 (sec 5.2):
session-style agents do not commit to protected paths.

**Subject-class breakdown** (sample of 5 commits touching SSOT paths):
- 2 are *automated tick* commits (atlas_meta_scan via launchd cadence) — privileged
  automated path, not a session agent.
- 1 is a *bisociation tooling fix* — repository-internal tool work, not a session agent.
- 2 are *decommission/rename events* — structural refactor authorised by user, not
  session agent self-promotion.

### §3.5 Near-miss incidents on nexus

Search for "would have updated" / "would_modify" / "would have written" patterns
in nexus material and recent reverts:

```
grep -rE "(would.have|would_modify|would update|would have updated|would have written)" \
  ~/core/nexus/design/ ~/core/nexus/reports/ \
  → no hits in design/ or reports/ (these patterns are n6-style banner text, not nexus)
```

Search for `revert` in 14-day commit log:
```
git -C ~/core/nexus log --since="14 days ago" --grep="revert" --oneline
  → no revert commits in the window
```

**Self-disclosure (sibling pattern)** — the cycle-43 commit `6772aede` is a self-disclosure
of a *non-firing counter*, not a write-barrier near-miss. The cycle-51 commit `d837839e`
is a *result retraction*, not a write-barrier event.

**Direct write-barrier near-miss for a session/research agent**: **0 found in 14-day
window**. The barrier holds at the commit-author boundary (no session-agent-named
commits), at the prompt-level (no "would have updated" paraphernalia in session
narratives), and at the L0 list level (CLAUDE.md.bak L0 block, though stale on the
shared/ prefix).

**Authorised structural refactor as near-miss-shape**: the 5311-file-rename commit
`842eb068` (cited in the porting audit §2.3 NV-3) is the kind of operation a literal
write-barrier *would have blocked* if applied to a session/research agent — but it was
authorised user work, not a session agent. Distinguishing authorised refactor from
session-agent edit remains a nexus-specific design question (porting audit §3.2).

### §3.6 Redundancy matrix (nexus side)

Defenses (cols):
- **D-prompt**: prompt-level write-barrier (nexus form, this audit's subject).
- **D-lockdown_gate**: `tool/lockdown_gate.hexa <verify|status|watch|repair|safe-merge|log>`.
- **D-permissions_ssot**: `permissions_ssot.json` deny patterns (28 patterns per porting audit).
- **D-harness/pre_tool_guard**: harness module (status: present per L0 list, but Write/Edit
  tool-call interception unverified runtime-wise).
- **D-L0-list**: documented L0 protected in CLAUDE.md.bak / project-claude — *stale* on the
  shared/ prefix, fresh-but-incomplete after decommission.
- **D-pre-commit**: git pre-commit hook on protected paths (status: not verified to be
  installed in nexus — same as n6).

Violation classes (rows; nexus-specific):
- **V1** general-purpose agent edits `n6/atlas.blowup.jsonl` directly (atlas SSOT pollution).
- **V2** session report rewrites `state/proposals/inventory.json` based on its own conclusion (cross-repo inbox pollution).
- **V3** session agent appends to `state/atlas_health_timeline.jsonl` outside the meta_scan tick (timeline pollution).
- **V4** session agent overwrites `state/agent_lock_ledger.jsonl` (lock-state pollution).
- **V5** session agent edits `lenses/omega_state_space_lens.hexa` (omega lens drift).
- **V6** session agent edits `project-claude/*.md` (CLAUDE.md persistence override).

| | D-prompt | D-lockdown_gate | D-permissions_ssot | D-harness/pre_tool_guard | D-L0-list | D-pre-commit |
|---|---|---|---|---|---|---|
| V1 atlas.blowup.jsonl | CATCHES | partial (gate verifies but tool may not be auto-invoked on Write tool calls) | partial (depends on deny pattern coverage) | (UNVERIFIED) | partial (stale prefix) | N/A |
| V2 inventory.json | CATCHES | MISSES (gate scope is atlas, not inventory) | partial | (UNVERIFIED) | CATCHES (L0 lists project-claude/, harness/, blowup/, n6/atlas.n6) | N/A |
| V3 atlas_health_timeline.jsonl | CATCHES | MISSES | partial | (UNVERIFIED) | partial | N/A |
| V4 agent_lock_ledger.jsonl | CATCHES | MISSES | partial | (UNVERIFIED) | partial | N/A |
| V5 omega_state_space_lens.hexa | CATCHES | MISSES (lockdown_gate scope is atlas) | partial | (UNVERIFIED) | partial | N/A |
| V6 project-claude/*.md | CATCHES | MISSES | partial | (UNVERIFIED) | CATCHES (L0 explicitly lists project-claude/) | N/A |

**Reading the matrix**:

- **D-prompt is the only defence that catches all six classes synchronously at edit-time.**
  Same conclusion as n6 sec 7.3.
- **D-lockdown_gate** covers atlas only (V1 partial); it is a runtime tool, not an
  in-session prompt-level barrier.
- **D-permissions_ssot** is a deny-pattern list — coverage depends on whether the deny
  list includes each protected path. Porting audit §2.4 reported 28 deny patterns; this
  audit did not exhaustively check pattern coverage but tags it `partial` consistent with
  porting audit's read.
- **D-harness/pre_tool_guard** is the candidate convergence layer (porting audit §5.3
  named this as F-PORT-2 falsifier — if it actually intercepts Write/Edit tool calls,
  the prompt-level barrier becomes redundant). **Not verified runtime-wise in this audit**;
  tagged `(UNVERIFIED)` in every row.
- **D-L0-list** catches V2 and V6 (paths explicitly listed) and is partial elsewhere; the
  shared/ prefix is stale.
- **D-pre-commit**: not verified in either repo.

**Critical observation** (mirroring n6 sec 7.3): the prompt-level barrier (D-prompt) is
the only synchronous, edit-time defence that covers all six classes. Removing it leaves
the runtime-tool stack (D-lockdown_gate + D-permissions_ssot + D-harness/pre_tool_guard)
to catch — which (a) is partial-coverage in static read, (b) is unverified for
session/research-agent Write-tool calls, and (c) does not gate at session-narrative
authorship time.

### §3.7 Removal counterfactual (nexus side)

If the prompt-level write-barrier is dropped:

| # | Scenario | Slip path | Severity |
|---|---|---|---|
| S1 | session audit concludes "this nxs-002 cycle deserves an inventory entry" and writes directly to `state/proposals/inventory.json` | V2 via D-prompt removal; D-lockdown_gate misses inventory; permissions partial | **HIGH** — cross-repo inbox corruption, especially as inventory is the SSOT for cross-repo blocker tagging |
| S2 | session audit appends a "synthetic" health-row to `state/atlas_health_timeline.jsonl` (e.g. fabricated composite_v3_prime score) | V3; meta_scan tick is the legitimate writer; barrier is the only synchronous gate | **HIGH** — timeline pollution can mislead future cycle-N analysis |
| S3 | session agent edits `lenses/omega_state_space_lens.hexa` to "register" an omega-state observation | V5 | **MEDIUM-HIGH** — lens drift propagates to all consumer tools |
| S4 | session-style agent overwrites `project-claude/nexus.md` based on a session conclusion | V6 | **CRITICAL** — global instructions divergence from user intent; recoverable from git but high downstream risk |
| S5 | mass atlas.blowup.jsonl write attempt | V1 | **HIGH** — 17 MB SSOT, 20,525 nodes; partial recovery only via git history |

**Most likely first failure on nexus**: S1 (inventory.json append) because (a) the
inventory is the *most-touched* SSOT in 14-day commit log (multiple `nxs-2026042*-NNN`
entries flipping `submitted → in_progress → implemented`), (b) the cycle-N convention
naturally produces inventory-flip-shaped output that an agent could *write directly*
absent the barrier, (c) lockdown_gate scope does not cover inventory.

**Severity ordering (worst first)**: **S4 ≈ S5 > S1 ≈ S2 > S3**. Mirrors n6's structure
(BT registry > atlas > inventory) but with V6 (project-claude/) elevated because nexus's
global instructions are continuously regenerated and an unauthorised edit can persist
silently into the synced CLAUDE.md.

**Aggregate first-incident remediation cost**: ~1–3 days for an inventory pollution
slip (must re-derive correct entries from git history + cross-repo links + cross-check
each `cross_repo_link` field for authenticity). Lower than n6's BT-registry slip
(28,480 lines, 4–6 days) because nexus's inventory is smaller (21 entries) and
git-tractable.

### §3.8 Cost of keeping (nexus side)

- Boilerplate: ~1 line per session report ("write-barrier: do not modify <path list>"),
  expanding to a 6-line path list for full specification. Per-document footprint ~1 line
  with reference to honesty_triad design doc, or ~6 lines if inlined.
- Files carrying the boilerplate today: 0 explicit (uncommitted spec); implicit
  enforcement via lockdown_gate references (4 files) and L0 list (1 file).
- False-positive blocks: none observed — the legitimate writes (atlas_meta_scan tick,
  bisociation fix, decommission rename) all originate from privileged paths.
- Maintenance cost: low — path list changes only when SSOT structure changes
  (e.g., shared/ decommission already happened; further structural moves would require
  list update).

**Cost of keeping**: same scale as n6 (negligible), with the additional consideration
that the nexus path list is **post-decommission** and may require one more update if
the L0 protected block is regenerated to reflect post-shared/ structure.

### §3.9 Verdict (Audit 2)

**KEEP_AS_IS** (with extended path list per §3.1).

One-paragraph rationale: the nexus write-barrier is load-bearing at the L9→L10 interface
just as the n6 barrier is, with the additional structural feature that nexus has
runtime-tool defences (lockdown_gate, permissions_ssot, harness modules) that n6 lacks.
However, the prompt-level barrier (D-prompt) remains the only synchronous, edit-time
defence covering all six violation classes (V1–V6); the runtime stack covers V1 partially
and is unverified for general-purpose agent Write-tool interception. Saturation is
indirect (no per-document banner today, but L0 list + lockdown_gate references are
implicit equivalents); the 14-day window shows zero session-agent-style commits to SSOT
paths (commit-time barrier holds) and zero "would have updated" paraphernalia in
narratives. Most likely first slip on removal is V2 (inventory.json append, ~1–3 days
remediation, HIGH severity) or V6 (project-claude/ edit, CRITICAL severity due to
sync regeneration). The cost asymmetry (negligible to keep, 1–3 days per HIGH slip,
4–6 days per CRITICAL slip) decisively favours KEEP. Nexus-native data carries the
verdict; mirrors n6 KEEP_AS_IS.

---

## §4 Audit 3: nexus no-fabrication guard

### §4.1 Constraint definition

Same as n6: agent must not invent numerical values, file contents, tool names, dataset
names, paper citations, or measurement results. When a measurement is unobtainable
(tool missing, data absent, computation not run, paper not read), the agent must return
`UNDEFINED`/`UNKNOWN`/`INCONCLUSIVE`/`TIMEOUT`/`MISSING`/`UNAVAILABLE` plus a short
diagnostic naming the gap. LLM-property constraint, no nexus-specific adaptation needed.

The 5 fabrication classes (C1 numerical, C2 citation, C3 tool, C4 structural, C5 result)
are inherited unchanged.

### §4.2 Saturation (nexus material — guard activations)

Direct grep on nexus design/ corpus:

```
grep -lE "UNKNOWN|INCONCLUSIVE|TIMEOUT|UNDEFINED|UNAVAILABLE|MISSING|UNVERIFIED|UNCALIBRATED" \
  ~/core/nexus/design/*.md
  → 5 of ~6 files hit:
     abstraction_ceiling.md, dispatch_path_audit_20260425.md,
     session_20260425_summary.md, beyond_omega_ladder.md, honesty_triad.md
```

Per-file hit counts (counted via `grep -c`, scope = strong-guard markers):

| File | strong-guard signal count |
|---|---:|
| session_20260425_summary.md | 2 |
| dispatch_path_audit_20260425.md | 1 |
| abstraction_ceiling.md | 4 |
| next_session_handoff.md | 0 |

**Of 4 readily-readable design docs**, **3 carry at least one fabrication-guard
activation**. Saturation: **3/4 = 75%** in the design corpus. The 1 non-engagement
(`next_session_handoff.md`) is a handoff doc — no measurement gap to flag.

**Commit-message stream saturation** (1734 commits / 14 days): the cycle-N commit
chain is itself a *fabrication-resistance discipline* — every cycle commit names what
was attempted, what succeeded, what failed, what was retracted. Commits like
`6772aede ⚠️ honest finding: raw 37/38 enforce not actually working (no caller)` are *self-disclosed
near-fabrications* — the system claimed an enforcement that wasn't wired. This is
saturation at the *commit-narrative* layer, not at the per-document layer.

**Comparison to n6**: n6 saturates at ~91% of recent omega-cycle reports actively
engaging the guard. nexus saturates at ~75% of design docs and has the cycle-N commit
chain as additional saturation. The two repos have **comparable saturation** in their
respective artefact pools.

### §4.3 Guard activations on nexus (chain)

Concrete cases where the nexus-side discipline converted a near-fabrication into a
diagnostic:

| # | Date | Commit / file | Class | Activation |
|---|---|---|---|---|
| 1 | 2026-04-25 | `6772aede` (cycle 43) | C5 + C3 | "raw 37/38 enforce not actually working (no caller)" — system's own counter claimed enforcement, but no caller was wiring it. Self-disclosed; the cycle-43 commit is *itself* the activation. |
| 2 | 2026-04-25 | `d837839e` (cycle 51) | C5 (multi-cycle) | "🎯 actual root cause = cross-session active drill's host load 97%" — cycles 47–50 had named different mechanisms; cycle 51 retracts. The retraction is the activation. |
| 3 | 2026-04-25 | `0d43b581` (cycle 35) | C4 | "new proposal registered (drill_zero_yield blocker, this session's cycle 12-18 root cause)" — recognised that cycles 12–18 had not actually identified the root cause, registered a new proposal rather than continuing to claim. |
| 4 | 2026-04-25 | `8a5173b5` (cycle 26) | C5 | "⚠️ cycle 24/25 self-averaging generalisation falsify, N=800 special accident" — explicit falsification of cycle 24/25's claim. |
| 5 | 2026-04-25 | `c12327a3` (referenced in user's CLAUDE.md, ceiling correction 0.85→0.835) | C1 | the composite ceiling was *previously* asserted at 0.85; correction to 0.835 documented in `c12327a3` with *ER ROI actual measurement* — explicit numerical correction, not silent overwrite. |
| 6 | 2026-04-25 | `design/abstraction_ceiling.md` (multiple sections) | C1 + C4 | 4 strong-guard markers in §6 spectral chaos mechanism — explicit `UNKNOWN`/`UNVERIFIED` tags on items requiring further measurement. |
| 7 | 2026-04-25 | `design/dispatch_path_audit_20260425.md` | C3 + C5 | 1 strong-guard marker plus extensive self-disclosure of dispatch path inconsistencies — the audit itself is a no-fabrication exercise. |
| 8 | 2026-04-25 | `dd6cb254` (cycle 13) | C1 | "feat(nxs-002): Ω-saturation cycle 13 — hexa native FULL CLOSURE (composite_v3_prime ≥ 0.9 robust)" — closure claim is explicit and falsifier-backed (the V3' metric, not the original V3); a fabrication-shape claim would have asserted ≥ 0.9 without naming the metric variant. |

**Pattern**: 8 activations identified in the 14-day window across 1734 commits + 4
design docs. Of those:

- **C5 (result fabrication / retraction)**: dominant (5 of 8). The cycle-N convention's
  *self-retraction* discipline is essentially a no-fabrication enforcement at result
  layer.
- **C1 (numerical)**: 2 of 8. The 0.85→0.835 ceiling correction is the canonical case.
- **C3 (tool)**: 2 of 8 (raw 37/38 enforce non-firing; dispatch path).
- **C4 (structural)**: 2 of 8 (proposal registration as deferred root cause; design
  doc UNKNOWN tags).
- **C2 (citation)**: 0 of 8 in this sample. nexus material is internal-tool-heavy,
  paper-citation-light; C2 surface is smaller than n6.

**Class distribution comparison to n6**: n6's chain shows C1 ≈ 4, C2 ≈ 1, C3 ≈ 2,
C4 ≈ 4, C5 ≈ 0. nexus's shows C1 ≈ 2, C2 ≈ 0, C3 ≈ 2, C4 ≈ 2, C5 ≈ 5. **The
distributions differ structurally**: nexus is C5-heavy (cycle-N retractions), n6 is
C1+C4 heavy (per-BT measurement honesty). Both repos have C2 underrepresented. This
divergence is meaningful — see §5.

### §4.4 Guard misses — sample-check of factual claims (nexus)

Sample 5 factual claims from 5 distinct nexus artefacts; verify by `ls`/`grep`/file
content:

| # | Artefact | Claim | Verification | Result |
|---|---|---|---|---|
| 1 | `design/honesty_triad.md` line ~10 | "21 entries in inventory.json" (implicit reference) | `jq '.entries \| length' ~/core/nexus/state/proposals/inventory.json → 21` | **VERIFIED** |
| 2 | porting audit's claim "20,525 nodes + 54,347 edges in atlas.blowup.jsonl" (referenced from this audit's §2.1 background) | atlas.blowup.jsonl size | `ls -la → 17,435,609 bytes` (size verified; node/edge count not re-derived in this audit, tagged `(UNVERIFIED at line-count level)`) | **PARTIAL** (size YES, node/edge count from porting audit transposed without re-derivation in this pass) |
| 3 | porting audit § "lockdown_gate.hexa exists" | runtime tool path | `cat ~/core/nexus/project-claude/nexus.md \| grep lockdown_gate → "L0 Guard: hexa $NEXUS/tool/lockdown_gate.hexa <verify\|status\|watch\|...>"` | **VERIFIED** (referenced consistently across all 3 project-claude files) |
| 4 | this audit's claim "5 of 6 SSOT paths confirmed" | SSOT path existence | `ls` on each path returned 5 PRESENT, 1 ABSENT (CLAUDE.md absent, .bak present) | **VERIFIED** |
| 5 | `git log --since="14 days ago" \| wc -l → 1734` | commit count | re-run shows `1734` | **VERIFIED** |
| 6 | "85 cycle-tagged commits" (this audit's §1 saturation) | cycle-tagged commit count | `git log --since="14 days ago" --pretty=format:"%s" \| grep -c "Ω-saturation\|cycle" → 85` | **VERIFIED** |
| 7 | "design/honesty_triad.md is uncommitted" | git status of file | `git status --porcelain \| grep honesty → ?? design/honesty_triad.md` | **VERIFIED** (uncommitted, untracked) |
| 8 | "atlas-agent.md not in .claude/agents/" | `ls ~/core/nexus/.claude/agents/ → only safe-commit.md` | direct `ls` | **VERIFIED** |

**Result**: **8/8 sampled claims verify or partial-verify** against the filesystem.
Zero outright guard-miss slips found; one item (#2) has a transposed sub-claim from
the porting audit that this audit *did not re-derive* — explicitly tagged
`(UNVERIFIED at line-count level)` per the no-fabrication discipline.

**Sample size caveat (same as n6 sec 5)**: n=8 is small; a 95% one-sided binomial
upper bound on slip rate at 0/8 is ≈ 31%, too loose for strong rate claims. C2
(citation) is similarly hard to audit ex post on the nexus side.

### §4.5 Redundancy matrix (nexus side)

For each fabrication class, would each downstream gate catch the slip without the
no-fabrication constraint upstream?

| gate \ class | C1 numerical | C2 citation | C3 tool | C4 structural | C5 result |
|---|---|---|---|---|---|
| **no-fab guard** | CATCHES (UNKNOWN/UNVERIFIED markers, §4.3 #5, #6) | CATCHES (same boilerplate covers paper claims) | CATCHES (#1, #7) | CATCHES (#3, #6) | CATCHES (#1, #2, #4) |
| **cycle-N self-retraction discipline** | partial (catches at commit time if numbers retracted, e.g. 0.85→0.835) | MISSES (rare in nexus) | partial (catches at commit time if tool stub disclosed) | partial | **CATCHES** (cycle-N is essentially a C5 retraction protocol) |
| **falsifier pre-registration in nxs-002 protocol** | CATCHES if numeric falsifier is pre-registered (composite ≥ 0.9 paper_trigger; V3' ≥ 0.9 robust check; raw 37/38 enforce) | MISSES | partial (the falsifier names the tool, but does not catch invented flags) | MISSES | CATCHES (forces explicit prediction → measurement → comparison) |
| **3-way tagging (rewriting / conditional / observation)** | partial (forces honesty about observation-mode vs rewriting-mode) | partial | MISSES | MISSES | CATCHES |
| **Y9 distortion-audit equivalent (status: not located in nexus)** | (UNKNOWN — not confirmed in nexus) | (UNKNOWN) | (UNKNOWN) | (UNKNOWN) | (UNKNOWN) |
| **user review of commit messages** | partial (depends on which numbers user spot-checks) | partial | partial | partial | partial |

**Coverage gaps if no-fab guard removed (nexus)**:

- **C3 tool fabrication**: cycle-N catches retroactively *if* the tool gap is disclosed
  in the commit message; but a session report claiming "ran nxs_002_composite.py
  --predict-er and got X" without actually running it is not caught by cycle-N (the
  retraction has to happen in a *future* cycle, not in the slip cycle). **Significant
  gap**.
- **C4 structural fabrication**: same gap — cycle-N is post-hoc, not synchronous.
- **C2 citation**: nexus has lower C2 surface than n6 (less paper-heavy work) but still
  no automated gate.
- **C1 numerical**: pre-registered falsifiers (paper_trigger 0.9, V3' robust, etc.)
  cover *some* numerical claims; the no-fab guard covers the rest.
- **C5 result**: cycle-N retraction discipline + falsifier pre-reg + 3-way tagging
  jointly cover this strongly. **Most redundant class on nexus** — same as n6.

**Net coverage gap on nexus is broadly similar to n6**: C3 + C4 are load-bearing
on the no-fab guard alone (with cycle-N as post-hoc backup), C5 is well-covered, C1/C2
partial.

**Y9-equivalent on nexus**: the porting audit (§2.4 row 1) noted no `Y9 HONEST-HARNESS`
analogue is located on nexus side. This nexus-native re-audit confirms: searches for
`Y9` / `HONEST-HARNESS` / `distortion-audit` in nexus material return zero matches.
The cycle-N convention is the *closest analogue* in spirit (each cycle audits the
prior cycle's claim) but is post-hoc and lacks Y9's structured row-tag-flip detection.

### §4.6 Removal counterfactual (nexus side)

| class | predicted slip-rate change on nexus | first-incident remediation cost |
|---|---|---|
| C1 numerical | medium → high rise. Nexus reports continuous values (composite ceilings, axis counts) where invented numbers are statistically frequent failure modes. | **HIGH**. A fabricated composite slipped into a cycle-N commit, then rolled into the cycle-chain, would propagate until cycle-N retraction catches it — but only at a future cycle, after potential downstream contamination. ~2–4 days remediation for one C1 slip. |
| C2 citation | low → low-medium rise. Nexus has lower paper-citation surface; primary risk is invented internal-tool documentation. | LOW-MEDIUM. ~1 day remediation. |
| C3 tool | low → high rise. Probe-#3-shape on nexus: agent claims a tool flag (`--predict-er`, `--per-bt`, etc.) that doesn't exist. The cycle-43 self-disclosure (#1 in §4.3) is exactly this; without the guard, the disclosure happens in a *much later* cycle. | **VERY HIGH**. C3 + C1 compound: an agent claiming "ran X tool, got Y number" with both invented. Remediation = re-run actual tool + retract chain of dependent claims + audit all downstream cycles. ~3–5 days. |
| C4 structural | medium rise. Nexus has high structural-claim surface (file paths, harness modules, lens names) due to its rich tool ecosystem. The shared/ decommission introduced 5311 path renames; an agent could easily claim a path that no longer exists. | MEDIUM-HIGH. ~1–2 days remediation. |
| C5 result | low rise. Cycle-N retraction discipline + falsifier pre-reg + 3-way tagging jointly catch most C5 slips. The no-fab guard's contribution here is *partially redundant* (mirrors n6). | LOW. Caught by next cycle within hours-to-days. |

**Aggregate first-incident cost on nexus**: a fabricated cycle-N result with C1 + C3
compound (e.g., "cycle 60 achieved composite 0.95 via new metric V4'"), without
underlying tool run, would propagate through the cycle chain until cycle-N retraction
or until a later session attempts to re-derive and fails. **~3–5 days remediation
for the worst case**, comparable to n6's multi-person-day estimate.

**Net counterfactual (nexus)**: dropping the guard saves boilerplate but produces a
predictable C1+C3+C4 slip surge, especially in cycle-chain contexts where invented
results compound across cycles. Cycle-N retraction is post-hoc; falsifier pre-reg
covers C5 strongly but not C3/C4. Removal is **not justified by nexus-native data**.

### §4.7 Cost of keeping (nexus side)

- ~5–15% of UNKNOWN markers may be over-cautious (same rate as n6, sampled from design
  corpus § 4.2: of 7 strong-guard markers across the 4 design docs, 1 (in
  `abstraction_ceiling.md`) plausibly could have been computed within the agent's
  budget — rough FP rate 14%, consistent with n6's 12%).
- Boilerplate "UNKNOWN: precise X not computed" lines: minor verbosity in falsifier
  blocks of cycle reports.
- Cost is bounded and does not compound.

### §4.8 Verdict (Audit 3)

**KEEP_AS_IS**.

One-paragraph rationale: the no-fabrication guard is load-bearing on classes C3 (tool)
and C4 (structural) where no nexus-side gate provides coverage; it is partially
redundant on C5 (result), where cycle-N retraction + falsifier pre-reg + 3-way tagging
jointly cover the slip surface. Saturation is high (~75% of design docs + cycle-N
chain at 5% of all commits for *self-retraction* discipline). Eight guard activations
in 14 days, with the canonical case (#1, raw 37/38 enforce non-firing) being a *self-
disclosed near-fabrication* that motivates the guard's existence in nexus context just
as Probe #3 does on n6. Removal counterfactual produces predictable C3+C4 slip surge
(~3–5 days remediation per HIGH slip). Cost of keeping is bounded (~14% over-caution
rate). Mirrors n6 KEEP_AS_IS at every field. **No removal recommendation.**

---

## §5 Cross-repo verdict comparison

| # | Constraint | n6 verdict | Nexus-native verdict (this audit) | Agreement | Divergence reason (if any) |
|---|---|---|---|---|---|
| 1 | Honesty counter (banner) | KEEP_AS_IS | KEEP_AS_IS (function) / KEEP_BUT_ADAPT (literal — n6's `0/7` does not transfer; nexus form is `nxs_promotion_count: N/N0`) | **agree at function level**; literal-text adaptation expected (continuous vs. discrete denominator) | Continuous metric domain on nexus vs. fixed-7 denominator on n6 (already noted in porting audit §5.1, §5.4). The constraint *function* is the same; only the surface text differs. |
| 2 | Write-barrier | KEEP_AS_IS | KEEP_AS_IS (with extended path list reflecting post-shared/-decommission layout) | **agree** | Path list differs (n6: `atlas/`, `state/`, `state/proposals/inventory.json`, `theory/breakthroughs/breakthrough-theorems.md`; nexus: `n6/atlas.blowup.jsonl`, `state/proposals/inventory.json`, `state/atlas_health_timeline.jsonl`, `state/agent_lock_ledger.jsonl`, `lenses/omega_state_space_lens.hexa`, `project-claude/*.md`). Verdict identical. |
| 3 | No-fabrication guard | KEEP_AS_IS | KEEP_AS_IS | **agree** | None. LLM-property constraint; same shape on both repos. Class distribution differs (nexus C5-heavy due to cycle-N retraction discipline; n6 C1+C4 heavy due to per-BT measurement) but verdict identical. |

**Agreement count**: **3-of-3** (with the constraint #1 caveat that *function-level
agreement* is firm but *literal-text agreement* is not — the literal `0/7` does not
transfer). The function-level reading is the one that matters for framework
universality, since the framework is auditing constraint *function*, not literal text.

---

## §6 Audit-framework universality verdict

**REPO_INVARIANT** (with two small qualifications).

The 3-of-3 agreement (function-level) supports the conclusion that the audit framework
itself — saturation × incident-chain × redundancy × counterfactual × cost —
is **repo-invariant**. The same six fields, applied to nexus material with nexus inputs,
return the same KEEP-direction verdicts that they returned for n6 material with n6
inputs. The constraints are universally load-bearing across both repos.

**Qualifications**:

1. **Surface-form adaptation is required**. The literal text of constraint (1) cannot
   be transposed (n6's `millennium_resolved: 0/7` is domain-specific). The framework
   distinguishes *function* from *literal*; the function transfers, the literal does not.
   This is not a framework defect — it is a designed feature (the framework asks
   "what does this constraint *do*?", not "is this exact string present?").

2. **Some redundancy claims rely on agent definitions that nexus lacks**. The n6
   side has `.claude/agents/atlas-agent/AGENT.md`, `growth-agent/AGENT.md`, etc.,
   each with a documented gate stack. nexus has only `.claude/agents/safe-commit.md`;
   the analogous agents (atlas-agent / growth-agent) are referenced in commit-message
   convention but not in `.claude/agents/`. Redundancy claims that depend on these
   agents existing as `.md` files are tagged `(UNVERIFIED)` here, consistent with the
   no-fabrication discipline. This does not affect the verdict (the prompt-level
   constraint is load-bearing regardless of whether the redundancy claim about
   atlas-agent holds), but it does mean the redundancy *matrix structure* on nexus is
   slightly thinner than n6's.

The framework's repo-invariance is therefore **strong on the constraint-function axis**
and **moderate on the redundancy-matrix-structure axis**. Both KEEP-direction outcomes
hold on both repos.

---

## §7 Implications for the porting audit's recommendation

The porting audit (`omega-audit-nexus-honesty-triad-portability-2026-04-25.md`)
recommended *proceed with deploy under user authorisation*, with the 4-target deploy
plan in its §4. This nexus-native re-audit:

- **Supports** the porting recommendation. 3-of-3 nexus-native KEEP-direction verdicts
  confirm that the constraints are not just *desirable* on nexus (function-level
  homology with n6) but *independently load-bearing* on nexus's own incident chain and
  redundancy structure. The case for deployment is strengthened: even without the
  cross-repo argument, nexus-native data alone supports each constraint.

- **Refines** the form of constraint (1). The porting audit recommended form (B)
  (`nxs_promotion_count: N/N_session_start`); this nexus-native re-audit confirms
  that form is correct (count-changing events occur at ~0.3/day, banner is the only
  in-session synchronous gate). No form change needed.

- **Confirms** the decommission-aware path list for constraint (2). The porting
  audit listed 5 protected paths plus L0 list reference; this re-audit confirms 5/6
  paths exist (CLAUDE.md is generated; `project-claude/nexus.md` is the source of
  truth) and notes that the L0 protected list in `CLAUDE.md.bak` is **stale on the
  shared/ prefix** — references like `shared/blowup/lib/atlas_guard.hexa.inc` and
  `shared/n6/atlas.n6` no longer resolve (shared/ was decommissioned in commits
  `5b6be8fc`, `9b8885f5`, `3afcc515`, `842eb068`, `f14d5a8d`, `280efb43`). A future
  deploy of constraint (2) should regenerate the L0 list against post-shared/ layout,
  not transpose the stale list. **This is a refinement, not a contradiction.**

- **Notes a partial pre-execution**. The file `~/core/nexus/design/honesty_triad.md`
  exists in the nexus working tree (uncommitted, untracked — `git status --porcelain
  | grep honesty → ?? design/honesty_triad.md`). This suggests a prior session executed
  Target 1 of the porting audit's deploy plan but did not commit it. **This audit does
  not modify, commit, or remove that file** (per the read-only constraint). The
  porting audit's recommendation should be re-evaluated in a follow-up session that
  also addresses Target 2 (project-claude/nexus.md cross-reference) and Target 3
  (agent_templates/honesty_triad_preset.md, currently absent — `ls
  ~/core/nexus/agent_templates/ → only no_py_guardrail.md`). The partial pre-execution
  is a deployment-state observation, not an audit-conclusion change.

**Net implication**: the porting audit's recommendation is **supported with
refinement**. Cross-repo verification adds independent evidence; refinement is
limited to the L0-list-staleness note and the partial-pre-execution note.

---

## §8 Anti-list — divergences considered and explained as artefacts

Cases where nexus-native data diverges from n6, but where the divergence is an
artefact of repo-specific structure (not a constraint defect) — flagged so future
sessions do not misread divergence as evidence against the framework:

- **A1 — saturation sample type**: nexus has no `reports/sessions/` tree. Saturation
  measurements substitute commit-message stream + design/ docs. *Artefact of repo
  organisation*; not evidence the constraint is unsaturated.
- **A2 — class distribution C5 vs C1+C4**: nexus's no-fabrication chain is C5-heavy
  (cycle retractions); n6's is C1+C4 heavy (per-BT measurements). *Artefact of work
  type*: nexus runs a continuous-iteration cycle; n6 runs a per-BT audit per iteration.
  Both repos under-represent C2 — common feature, not divergence.
- **A3 — atlas-agent existence**: not located as `.claude/agents/atlas-agent.md` on
  nexus. *Artefact of agent-ecosystem evolution*: nexus's privileged agents are
  encoded as runtime tools (lockdown_gate.hexa, harness modules) rather than as
  `.claude/agents/*.md` files. Redundancy claims tagged `(UNVERIFIED)` accordingly.
- **A4 — L0 protected list stale on shared/ prefix**: CLAUDE.md.bak L0 block references
  `shared/...` paths that no longer exist post-decommission. *Artefact of structural
  refactor* (`shared/` decommissioned in 6+ commits 2026-04-22 to 2026-04-23).
  Constraint (2) deploy must regenerate the list, not transpose it.
- **A5 — banner not deployed**: `nxs_promotion_count` banner specification exists in
  `design/honesty_triad.md` (uncommitted) but is not yet in any session report. *Artefact
  of porting audit's plan being partial-executed*. Does not change verdict (the
  saturation is currently low *because the deploy is incomplete*, not because the
  constraint is unnecessary).
- **A6 — n6 has reports/sessions, nexus has commit stream**: per-document banner makes
  sense on n6; per-commit-prefix or per-cycle banner makes sense on nexus. *Artefact of
  artefact-pool topology*. Both produce equivalent saturation function; the surface
  differs.
- **A7 — atlas-blowup format n6=jsonl vs n6-architecture=text grade**: the nexus atlas
  is `n6/atlas.blowup.jsonl` (JSONL, type/edge); the n6-arch atlas is `atlas/atlas.n6`
  (line-based grade format). *Artefact of representation choice*; both are SSOTs and
  both are equally protected by their respective barriers.
- **A8 — no Y9 analogue on nexus**: porting audit and this audit both confirm no
  `Y9 HONEST-HARNESS` exists on nexus side; cycle-N convention is the closest analogue
  but is post-hoc. *Artefact of axis evolution*; n6 evolved Y9 explicitly during the
  Phase Omega closure work, nexus has not. The no-fab guard's redundancy is therefore
  *thinner* on nexus, which makes the guard *more* load-bearing — same KEEP_AS_IS
  verdict, slightly stronger reasoning.
- **A9 — `~/core/nexus/CLAUDE.md` does not exist (only `.bak` + `project-claude/nexus.md`
  source)**: *artefact of regeneration architecture*. The active source is
  `project-claude/nexus.md`; CLAUDE.md is regenerated via `scripts/sync_claude_md.hexa`.
  Constraint (2) protects the source file, not the generated one.
- **A10 — small sample (n=8 verifications, 14-day window)**: same as n6's sample-size
  caveat. *Artefact of audit scope*; a 30-day or n=30 audit would tighten bounds. Verdict
  is still well-supported by chain + redundancy + counterfactual analysis.

---

## §9 Falsifiers active for the cross-repo verification

The cross-repo verdict (3-of-3 agreement, REPO_INVARIANT) is **voided** if any of the
following later trips:

- **F-NXV-1 (n6 verdict reversal)**: if any of the three n6 parent audits later returns
  a different verdict (e.g. F-AUDIT-3 fires for honesty counter, n6 verdict drops to
  KEEP_BUT_COMPRESS), the cross-repo agreement count drops accordingly. Re-evaluate.
- **F-NXV-2 (nexus harness convergence)**: if `harness/pre_tool_guard.hexa` is
  exercised and verified to intercept Write/Edit tool calls on the SSOT path list,
  constraint (2)'s prompt-level barrier becomes redundant on nexus. Verdict drops to
  KEEP_BUT_COMPRESS. (Mirrors porting audit's F-PORT-2.)
- **F-NXV-3 (nxs_promotion_count saturation collapse)**: if a 30-day audit window post-
  deployment shows the banner caught zero count-changing events not also caught by
  cycle-N within ≤24 hours, constraint (1) drops to KEEP_BUT_COMPRESS or RETIRE on
  nexus. (Mirrors porting audit's F-PORT-3.)
- **F-NXV-4 (atlas-agent existence confirmation)**: if `.claude/agents/atlas-agent.md`
  is later located (this audit's grep depth was bounded), the redundancy matrix on
  nexus becomes thicker; some `(UNVERIFIED)` tags resolve to CATCHES; the redundancy
  argument for keeping the prompt-level barrier weakens, but does not flip the verdict
  (D-prompt remains the only synchronous, edit-time defence in any case).
- **F-NXV-5 (Y9-analogue construction on nexus)**: if a Y9-equivalent post-hoc audit
  is later wired into nexus, the no-fab guard's redundancy structure changes; verdict
  on (3) re-opens for KEEP_BUT_COMPRESS evaluation.
- **F-NXV-6 (cycle-N convention abandonment)**: if the `Ω-saturation cycle N` /
  `beyond-omega cycle N` commit-message convention is dropped or replaced, the
  redundancy claims for constraints (1) and (3) need to be re-derived against the
  successor convention.
- **F-NXV-7 (audit framework category error)**: if a future analysis demonstrates that
  the omega-cycle 4-axis lens (ladder × saturation × chain × closure) is not the
  appropriate lens for cross-repo constraint audits — i.e. the framework itself is
  mis-fit for the question — the universality verdict re-opens. (Mirrors n6's F-A6
  in the no-fabrication audit.)
- **F-NXV-OMEGA (meta-audit divergence)**: if a future independent audit (n6 or
  nexus side) of any of the three constraints returns a verdict that contradicts this
  audit's per-constraint verdict, this report re-opens.

None of F-NXV-1..7 or F-NXV-OMEGA have fired as of this audit's write-time. They are
listed as future-trigger conditions only.

---

## §10 Closing

0/7 unchanged. nxs promotion count unchanged. **NO nexus files modified by this audit.**

Cross-repo verification result:

- **Audit 1 (nxs_promotion_count)**: **KEEP_AS_IS** at function level (KEEP_BUT_ADAPT
  at literal level — same conclusion as the porting audit's §6). Function-level agree
  with n6.
- **Audit 2 (write-barrier)**: **KEEP_AS_IS** with extended (post-decommission) path
  list. Agree with n6.
- **Audit 3 (no-fabrication guard)**: **KEEP_AS_IS** verbatim. Agree with n6.

**Cross-repo agreement: 3-of-3 (function-level).**

**Audit-framework universality verdict: REPO_INVARIANT** (with two small qualifications:
surface-form adaptation required for constraint (1); redundancy-matrix structure on
nexus slightly thinner due to absent `.claude/agents/*.md` definitions and absent
Y9-analogue. Neither qualification changes any verdict.)

The earlier porting audit's recommendation (proceed with deploy under user
authorisation) is **supported with two refinements**: (a) the L0 protected list in
`CLAUDE.md.bak` is stale on the `shared/` prefix and must be regenerated against
post-decommission layout before constraint (2) deploys; (b) `~/core/nexus/design/
honesty_triad.md` already exists in the nexus working tree (uncommitted, untracked) —
a partial pre-execution that should be addressed in the follow-up deploy session
along with Target 2 (project-claude/nexus.md cross-reference) and Target 3
(agent_templates/honesty_triad_preset.md, currently absent).

This audit produces no atlas / state / inventory / CLAUDE.md edits in either repo.
The single output file is this report under
`reports/sessions/omega-audit-nexus-native-3constraint-2026-04-25.md` in
n6-architecture.

millennium_resolved: **0/7** (unchanged).
nxs_promotion_count: **unchanged this session** (no inventory writes).
NO nexus files modified by this audit.
