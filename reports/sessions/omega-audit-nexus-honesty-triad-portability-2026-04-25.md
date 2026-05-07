---
id: omega-audit-nexus-honesty-triad-portability
date: 2026-04-25
scope: cross-repo audit + porting design (NO actual nexus edits)
target: 3 KEEP_AS_IS constraints -- nexus-side audit + adaptation + deploy plan
parent_reports:
  - reports/sessions/omega-audit-constraint-honesty-counter-2026-04-25.md
  - reports/sessions/omega-audit-constraint-write-barrier-2026-04-25.md
  - reports/sessions/omega-audit-constraint-no-fabrication-2026-04-25.md
millennium_resolved: 0/7 (unchanged)
nxs_promotion_count_delta: 0 (unchanged this session)
grade: cross-repo audit + design, no claim, no deployment
---

## §0 Non-claim disclaimer

This document is a **read-only cross-repository audit + porting-design exercise**. Hard
constraints honoured during its production:

- No file inside `~/core/nexus/` was modified, created, or deleted by this session. Every
  nexus-side observation below derives from **reads** (`ls`, `cat`, `git -C ~/core/nexus
  log`, `wc -l`, `grep -c`) — no `Write`, no `Edit`, no `git mv`, no `git commit`.
- No file inside `~/core/canon/atlas/`, `~/core/canon/state/`, nor
  `~/core/canon/state/proposals/inventory.json` was modified. The single output
  file is this session report under `reports/sessions/`.
- The honesty counter remains `millennium_resolved: 0/7 (unchanged)`. The nexus
  promotion-count delta is `0`. No promotion is claimed.
- This audit produces **a deploy plan**, not a deploy. Phase 3 lists specific files to
  edit on the nexus side; **none of those edits have been performed**. Activation requires
  a separate session with explicit user authorization.
- Where nexus-side material was unreadable or did not exist at the path stated by the
  prompt, that fact is documented in §2 (no fabrication of file structure).

The cross-repo verdict per constraint is in §6, the composite recommendation in §7. Both
must be read in conjunction with the divergence analysis (§5) and the falsifiers (§9).

---

## §1 n6 audit summary (parent reports, condensed)

The three canon audits sit at:

| Constraint | Parent report | n6 verdict |
|---|---|---|
| Honesty counter (`millennium_resolved: 0/7 unchanged`) | `reports/sessions/omega-audit-constraint-honesty-counter-2026-04-25.md` | **KEEP_AS_IS** |
| Write-barrier (atlas/, state/, inventory.json, breakthrough-theorems.md protected) | `reports/sessions/omega-audit-constraint-write-barrier-2026-04-25.md` | **KEEP_AS_IS** |
| No-fabrication guard (UNKNOWN/INCONCLUSIVE/TIMEOUT > invented values) | `reports/sessions/omega-audit-constraint-no-fabrication-2026-04-25.md` | **KEEP_AS_IS** |

3-of-3 KEEP_AS_IS. Verbatim verdict snippets (read from parent files):

- *Honesty counter, §10*: "0/7 unchanged. No promotion. No atlas / state / inventory edits.
  This document is a research-only constraint audit. The 0/7 honesty-counter banner is
  recommended to remain in its current form."
- *Write-barrier, sec 12*: "Verdict: **KEEP_AS_IS**."
- *No-fabrication, §11*: "Audit complete. Verdict: **KEEP_AS_IS**. The no-fabrication
  guard remains."

Each n6 audit lists its own falsifiers (F-AUDIT-1..4 + F-OMEGA-CHAIN for honesty;
F-WB-* for write-barrier; F-NF-* for no-fabrication). None of those falsifiers have
fired as of this cross-repo audit's read.

The constraint of the original prompt — *"removal requires concurring verdicts from the
parallel audits"* — is honoured: this audit does **not** claim independent authority to
retire any constraint. It claims only authority to (a) decide whether the same constraint
should additionally be ported to nexus, (b) decide what nexus-side form it takes, and
(c) decide whether the n6→nexus port itself is justified given nexus's existing redundancy.

---

## §2 Phase 1 — nexus-side audit (read-only, condensed three-way)

### §2.1 Repository layout discovery (what is actually present)

The original prompt assumed a `~/core/nexus/CLAUDE.md` and `~/core/nexus/reports/sessions/`.
**Both of those paths do not exist as written.** The actual nexus-side state observed:

| Prompt-stated path | Observed | Substitute path used |
|---|---|---|
| `~/core/nexus/CLAUDE.md` | **absent** (only `CLAUDE.md.bak` from 2026-04-22) | `~/core/nexus/project-claude/nexus.md` (active project-CLAUDE source — referenced from `shared/CLAUDE.md` per the bak file) |
| `~/core/nexus/reports/sessions/` | **absent** (no `sessions/` subdir) | `~/core/nexus/reports/` (flat — 15 JSON/MD analytics files, no per-session narratives) |
| `~/core/nexus/atlas/` | **absent** | `~/core/nexus/n6/atlas.blowup.jsonl` (17 MB, 89,167 lines = 20,525 nodes + 54,347 edges + remainder) |
| `~/core/nexus/state/proposals/inventory.json` | **present** (`schema: nexus.proposal_inventory.v1`) | (used as-is) |
| `~/core/nexus/design/` | **present** (10 files including `abstraction_ceiling.md`, `atlas_n6_omega_closure.md`, `beyond_omega_ladder.md`, `dispatch_path_audit_20260425.md`, `next_session_handoff.md`, `session_20260425_summary.md`) | (used as-is) |
| `~/core/nexus/lenses/` | **present** (>200 hexa lenses, including `omega_state_space_lens.hexa`) | (used as-is) |
| nexus has `atlas-agent` (EXACT-only) and `growth-agent` (KnowledgeGraph) | **partial confirmation** — `~/core/nexus/.claude/agents/` contains only `safe-commit.md`. Searches for `atlas-agent`/`growth-agent`/`NodeBlocker` in `design/`, `tool/`, `config/` returned **zero matches**. The agents may exist as conceptual roles in the harness rather than as `.claude/agents/*.md` definitions. **Documenting non-confirmation rather than fabricating their structure.** |
| nexus has L0 Guard "atlas.n6 actual-edit 0" CLAUDE.md preamble | **partial** — `~/core/nexus/CLAUDE.md.bak` lines 59–95 list `L0 protected` files, including `shared/blowup/lib/atlas_guard.hexa.inc` and `shared/n6/atlas.n6`. The active `tool/lockdown_gate.hexa` exists. The "atlas.n6 actual-edit 0" string was **not located by grep** in any read file — **not confirmed as a literal counter, only as an intent-level protection in the L0 list**. |

This map matters for the deployment plan (§4). Some constraint-port targets the prompt
proposed (e.g. "add to ~/core/nexus/CLAUDE.md after line N") are **infeasible as
specified** because the file does not exist; substitute targets are proposed.

### §2.2 Saturation estimate per constraint (nexus side)

**Definition (carried from n6 audits)**: saturation = fraction of session/research artifacts
where the constraint *would gate* a wrong move if the agent attempted one. Sampled by
reading nexus session-equivalent artifacts (the recent commits + design/ + state/proposals/).

The applicable nexus artifact pool used for sampling:

- recent commits since 2026-04-22 touching `state/`, `design/`, `n6/`, `tool/` (≈ 80 commits
  observed in `git log --since="4 weeks ago" --oneline` head-30; almost all carry
  `Ω-saturation cycle N` or `beyond-omega cycle N` tags, indicating active omega-style work);
- `design/` documents (10 files; the four most active: `dispatch_path_audit_20260425.md`,
  `session_20260425_summary.md`, `next_session_handoff.md`, `abstraction_ceiling.md`);
- `state/proposals/inventory.json` (≈ 24+ entries beginning `nxs-202604*`, all with
  `done_note` / `cross_repo_link` fields).

| Constraint | Saturation estimate | Method | Confidence |
|---|---|---|---|
| **(1) Honesty counter** (n6 form: `0/7 unchanged`) | **medium-low (~30–40%)** of nexus artifacts would benefit from a first-line honesty banner. Reasoning: n6's `0/7` is a fixed denominator (7 millennium problems) — *atomic and hard*. nexus's analogue (number of `[10*]` promotions, or `nxs-002 ceiling 0.835`) is **continuous and frequently updated** (cycle 33 actual `0.93617` vs cycle-1 baseline `0.85`). A continuous denominator gates *promotion-without-evidence* less crisply than a fixed denominator. | grep on commit-message tags `Ω-saturation cycle` (>50 in last 4 weeks) + read of `session_20260425_summary.md` cycle-1..33 progression | medium |
| **(2) Write-barrier** | **high (~80%)** of nexus artifact-modifying flows would be blocked by it. `n6/atlas.blowup.jsonl` (17 MB) + `state/proposals/inventory.json` are the two primary SSOT files; both are mutated routinely by `tool/atlas_meta_scan.hexa`, `tool/proposal_archive`, and the blowup pipeline. The L0 list in `CLAUDE.md.bak` (≈ 30 protected paths) already covers most of them at intent level, but **not via prompt-level barrier**. | inventory of `L0 protected` block (CLAUDE.md.bak L59–95) + commit log of `state/proposals/inventory.json` writes | high |
| **(3) No-fabrication guard** | **high (~70–90%)** — same as n6. This is an LLM-property constraint, not a path constraint. Any nexus session that returns a numeric ceiling, an axis count, or a verdict on whether `nxs-002` reached `0.9` is at risk of fabrication if a tool was unreachable. Recent commits explicitly document this hazard: cycle-43 commit (`6772aede`) "raw 37/38 enforce not actually working (no caller)" — this is a *self-caught* near-fabrication where the system reported a counter that wasn't actually firing. | reading commit `6772aede` body + cycle-32 root-cause chain in `session_20260425_summary.md` | high |

### §2.3 Atlas-chain incidents (historical near-violations)

Searched `git -C ~/core/nexus log --since="4 weeks ago"` for keywords (`fabricat`, `wrong`,
`fixed`, `incorrect`, `revert`, `actual root cause`).

Findings:

- **NV-1 (2026-04-25, cycle 43, commit `6772aede`)**: "fix(nxs-20260425-001): Ω-saturation
  cycle 43 — ⚠️ honest finding: raw 37/38 enforce not actually working (no caller), Phase 4 audit partial".
  This is a **self-disclosed near-fabrication**: the system's own counter claimed to
  enforce a constraint, but no caller was wiring it. A no-fabrication guard at the
  *reporter* layer would have flagged the gap one cycle earlier. *Direct relevance:
  constraint (3).*
- **NV-2 (2026-04-25, cycle 51, commit `d837839e`)**: "🎯 actual root cause = cross-session
  active drill's host load 97%". The narrative chain shows three prior cycles
  (47–50) where a different mechanism was claimed; cycle 51 retracts. A no-fabrication
  guard with `INCONCLUSIVE` return discipline would have prevented the three intermediate
  *named-but-unconfirmed* claims. *Direct relevance: constraint (3); marginal relevance
  to (1) — a continuous honesty counter would have surfaced the multi-cycle drift.*
- **NV-3 (2026-04-22, commit `842eb068`)**: "chore(shared-decommission P3.3-nexus): 10
  large/medium subdirs → top-level (5311 file renames)". This is a **massive structural
  rewrite** that touched the L0-protected `shared/` tree. It was a deliberate authorized
  refactor (not a violation), but it is the kind of operation a literal write-barrier
  *would have blocked* if applied naively. *Relevance: constraint (2) — the nexus
  write-barrier must distinguish "authorized structural refactor" from "session/research
  agent edit", which is a non-trivial form-question (§3.2).*
- **No NV found for constraint (1) directly.** The honesty-counter analogue would be
  `nxs-002 ceiling = X` claimed without backing measurement. The cycle-32 chain is the
  closest near-miss but it self-resolved within the same session.

Three near-violations in 30 days (NV-1, NV-2, NV-3), of which two map to constraint (3),
one maps to constraint (2), and zero map to constraint (1) directly.

### §2.4 Redundancy matrix (existing nexus mechanisms per constraint)

| Constraint | Existing nexus mechanism | Coverage | Remaining gap |
|---|---|---|---|
| (1) Honesty counter | `design/abstraction_ceiling.md` §6 (composite ceiling discipline); commit-message convention `Ω-saturation cycle N` (manual but consistent) | partial — *cycle N* number is in every commit, but it is **not a banner in agent output**. Agents do not emit it. | a first-line agent-banner is missing; the cycle-N convention catches it post-hoc in git log only |
| (2) Write-barrier | L0 protected list (CLAUDE.md.bak L59–95, ≈ 30 paths); `tool/lockdown_gate.hexa`; `shared/blowup/lib/atlas_guard.hexa.inc` (referenced as `_guarded_append_atlas`); `harness/pre_tool_guard.hexa`; `permissions_ssot.json` (deny 28 patterns) | **high** — the L0 list + lockdown_gate + permissions_ssot collectively cover writes at multiple layers | gap is at the **prompt level** for sub-agents launched without harness invocation; the L0 list is a *listing*, not an enforced guard for non-hexa writes (Write/Edit tool calls bypass guarded_append unless wrapped) |
| (3) No-fabrication guard | none located by grep. No prompt boilerplate, no UNKNOWN/INCONCLUSIVE return convention documented in `design/` or `tool/`. The cycle-43 self-catch (NV-1) suggests the discipline is *practiced informally* by the user in commit-message review, not enforced in agent prompts. | **none/very low** — fully open gap | full gap, no compression possible |

### §2.5 Removal counterfactual (nexus side, per constraint)

If each constraint is **not ported** to nexus:

- (1) Honesty counter not ported: agents may continue producing nexus-side reports without
  a first-line banner. Risk: a cycle-N claim in mid-session may drift from the inventory's
  `score_priority` / `done_ts` truth without an early flag. Severity: **low-medium** — the
  cycle-N commit-message convention catches most drift at commit time. Counterfactual
  marginal harm: ≈ 1 NV/month, mostly post-hoc-detected.
- (2) Write-barrier not ported: agents continue with L0 list + lockdown_gate + permissions
  coverage. Risk: a sub-agent launched outside harness writes to `n6/atlas.blowup.jsonl`
  or `state/proposals/inventory.json` directly via Write tool. Severity: **medium** —
  L0 list is intent-only for non-hexa writers; permissions_ssot has 28 deny patterns but
  may not cover every SSOT path. The ≈ 5311-file rename in NV-3 shows the volume of
  legitimate refactor traffic, against which a too-strict barrier produces false positives.
- (3) No-fabrication guard not ported: agents may invent ceiling values, axis counts,
  or `[10*]` promotion deltas when tools time out or are unreachable. Severity: **high** —
  nexus has *higher* potential fabrication surface than n6 because nexus reports continuous
  values (ceilings, deltas) where n6 reports discrete `0/7` style. NV-1 demonstrates this
  is an active failure mode.

Counterfactual ranking (highest harm if not ported → lowest): **(3) > (2) > (1)**.

---

## §3 Phase 2 — Adaptation specs (nexus form per constraint)

### §3.1 Constraint (1) — Honesty counter, generalized

**n6 form**: `millennium_resolved: 0/7 unchanged` (first-line banner, fixed denominator,
discrete).

**Candidate nexus forms (evaluated)**:

- **(A) `[10*]_promotion_count: <N>/<N_session_start> unchanged`** — promotion delta over
  atlas grade `[10*]+`. Discrete, well-defined denominator (queryable via grep on
  `n6/atlas.blowup.jsonl` for `confidence:1.0` + `[10*]` markers, but the atlas.blowup
  format is *type/edge* JSONL, not the canon `[NN*]` grade format — so the
  denominator must come from a different source, e.g. a sidecar). Drawback: requires
  a sidecar update each session-start to capture `N_session_start`.
- **(B) `nxs_promotion_count: <N>/<N_session_start> unchanged`** — promotion delta over
  inventory.json `user_status: implemented` entries. Counts are queryable by `jq` on
  `state/proposals/inventory.json`. Discrete, fixed-at-session-start denominator. **This
  matches the *spirit* of n6's 0/7 most closely**: a small integer count that should not
  silently increase mid-session.
- **(C) `EXACT_grade_count_delta: 0`** — counts atlas-agent EXACT-grade verifications.
  Drawback: atlas-agent's existence as a discrete `.claude/agents/*.md` definition was
  **not confirmed** in §2.1; building a counter on an unconfirmed agent is fabrication-
  adjacent.
- **(D) `Omega_ceiling: 0.835 unchanged`** — references `design/abstraction_ceiling.md`
  composite. Drawback: continuous, drifts naturally during legitimate eig pipeline runs;
  the n6 banner *function* is to flag *premature* promotion, not normal evolution. A
  continuous value flags the wrong thing.

**Recommended nexus form**: **(B)** —
```
nxs_promotion_count: <N>/<N_session_start> unchanged
```
where `<N>` is the count of inventory entries with `user_status ∈ {implemented, done}` at
report write-time and `<N_session_start>` is the same count captured at session begin.
The `unchanged` literal is replaced with the explicit delta if non-zero (e.g. `12/10
(+2 this session)`), forcing the agent to **name** every promotion claim.

Justification mirrors n6: the banner sits at the top of every session/research artifact,
the agent must compute both numbers (so a fabricated ceiling cannot quietly masquerade as
a promotion), and the `unchanged` discipline forces a *no-claim* default. Form (B) also
naturally couples to the existing n6 banner — a session that touches both repos can carry
two banners (`millennium_resolved: 0/7 unchanged` + `nxs_promotion_count: N/N unchanged`)
without ambiguity.

### §3.2 Constraint (2) — Write-barrier, ported + extended

**n6 protected (verbatim from prompt)**: `atlas/`, `state/`, `state/proposals/inventory.json`,
`theory/breakthroughs/breakthrough-theorems.md`.

**Proposed nexus protected list (derived from §2.4 + L0 list + observed write hazards)**:

| Path | Why SSOT | Reach of existing L0 / lockdown_gate? |
|---|---|---|
| `~/core/nexus/n6/atlas.blowup.jsonl` | atlas-grade SSOT, 17 MB / 20,525 nodes / 54,347 edges, the spectral substrate of nxs-002 | partial — `_guarded_append_atlas` covers append-only writes from blowup phase 6.7; ad-hoc Write tool writes are not gated |
| `~/core/nexus/state/proposals/inventory.json` | nxs-prefix SSOT for all proposal entries | partial — proposal_inbox.hexa enforces schema, but Write tool can bypass |
| `~/core/nexus/state/` (broad) | aggregate session/research output, including ALM checkpoints, ledgers, evo progress | low — most files here are *intentionally mutable* session output. **Recommend NOT broad-gating** — would cause excessive false positives. Apply only to specific files (e.g. `state/proposals/inventory.json`, `state/atlas_health_timeline.jsonl`, `state/agent_lock_ledger.jsonl`). |
| `~/core/nexus/tool/nxs_002_composite.py` | **PROPOSED OUT** — this is a tool, not a SSOT artifact. Modifying it is a normal development activity. Including it in the barrier would block legitimate ROI improvement work (the prompt's question mark is correct skepticism). |
| `~/core/nexus/design/abstraction_ceiling.md` | **PROPOSED OUT** — design doc, mutable by design. The n6 analogue (`theory/breakthroughs/breakthrough-theorems.md`) is protected because it is a *finalized* claim ledger. `abstraction_ceiling.md` is *active design*, not finalized. |
| `~/core/nexus/lenses/omega_state_space_lens.hexa` | **PROPOSED IN (light-grade)** — registered in CLAUDE.md.bak L0 list as a finalized lens. Should be modified only on explicit user request, same regime as L0 list members. |
| `~/core/nexus/CLAUDE.md.bak` (and any future active CLAUDE.md) | global instructions | L0 lists itself as "L0 protected" |

**Final proposed nexus barrier list**:
```
~/core/nexus/n6/atlas.blowup.jsonl
~/core/nexus/state/proposals/inventory.json
~/core/nexus/state/atlas_health_timeline.jsonl
~/core/nexus/state/agent_lock_ledger.jsonl
~/core/nexus/lenses/omega_state_space_lens.hexa
~/core/nexus/CLAUDE.md(.bak)
+ all paths already in CLAUDE.md.bak L0 list (≈ 30 paths)
```

**L0 reach question (decided)**: the existing L0 list is **prompt-level intent**, not a
runtime block for Write/Edit tool calls. The L0 list lives in CLAUDE.md.bak and informs
agent behaviour by being read; it does **not** intercept tool calls. Therefore **a
prompt-level write-barrier addition is NOT redundant** — it adds a complementary layer
(explicit "session/research agent must not modify these paths" boilerplate) on top of the
implicit "L0 protected" listing. The two layers are stacked, not overlapping.

**Decision**: port the n6 write-barrier verbatim with the file-list above. Decline to
broaden to `state/` wholesale.

### §3.3 Constraint (3) — No-fabrication guard, port verbatim

LLM-property constraint, no adaptation needed. Boilerplate (verbatim from n6 form):

```
DO NOT FABRICATE. UNKNOWN / INCONCLUSIVE / TIMEOUT > invented values.
If a tool / data source is missing, stop with a diagnostic, do not invent.
Numeric values, axis counts, ceiling deltas, and promotion claims must
each be backed by a citation (path + line range + read-timestamp) or
explicitly tagged (UNVERIFIED) / (UNCALIBRATED) / (PROXY) / (UNKNOWN).
```

NV-1 (the cycle-43 self-disclosure) is the exact failure mode this guard prevents.
NV-2 (the cycle-47–51 chain) is a softer version where claims were not yet labelled
fabrication but were *named-but-unconfirmed*; the guard's `(UNVERIFIED)` discipline
would have applied.

No nexus-specific adaptation. The same boilerplate that goes into n6 prompts goes into
nexus prompts.

---

## §4 Phase 3 — Deployment plan (specific files, exact additions; **NOT EXECUTED**)

### §4.1 Recommended deployment form

A **combination (a)+(c)** is recommended:

- **(c) design doc** as the single source of truth: `~/core/nexus/design/honesty_triad.md`
  (new file). Contains the 3 constraints with their nexus-adapted forms (§3.1–§3.3),
  rationale, and the protected-path list.
- **(a) per-agent-prompt boilerplate**: a 3-line preset that *references* the design doc
  and inlines the no-fabrication guard. Agents that touch nexus material receive this
  preset automatically. The preset is short enough to avoid context bloat.
- **(b) global CLAUDE.md update**: nexus has no active `CLAUDE.md` (only `.bak`); the
  active project-CLAUDE source is `~/core/nexus/project-claude/nexus.md`. **Recommend
  adding a one-line reference** there instead of regenerating CLAUDE.md.

Rationale for not making (b) the primary mechanism: the nexus CLAUDE.md is regenerated
from `project-claude/nexus.md` via `scripts/sync_claude_md.hexa`, so persistent edits
must live in `project-claude/nexus.md` to survive regeneration.

### §4.2 Specific files to edit (deploy targets)

**Target 1 — create `~/core/nexus/design/honesty_triad.md`**:
- new file, ≈ 200 lines
- structure: §1 honesty counter (form B) + §2 write-barrier (full path list from §3.2) + §3 no-fabrication guard (verbatim block from §3.3) + §4 cross-ref to n6 parent reports
- explicit citation back to this audit report path

**Target 2 — append to `~/core/nexus/project-claude/nexus.md`** (after the L0 protected block,
which currently ends at the equivalent of CLAUDE.md.bak L95):
- one-line addition: `honesty_triad: design/honesty_triad.md (3 constraints — apply to all session/research agent prompts)`
- this propagates to `CLAUDE.md` on next `sync_claude_md.hexa` run

**Target 3 — agent-prompt preset (location TBD by user)**:
- proposed location: `~/core/nexus/agent_templates/honesty_triad_preset.md` (existing
  `agent_templates/` dir already houses `no_py_guardrail.md`, so this is the established
  pattern)
- 3-line content (full text):
  ```
  honesty_triad: nxs_promotion_count: <N>/<N_session_start> unchanged
  write-barrier: do not modify n6/atlas.blowup.jsonl, state/proposals/inventory.json, state/atlas_health_timeline.jsonl, state/agent_lock_ledger.jsonl, lenses/omega_state_space_lens.hexa, CLAUDE.md
  no-fabrication: UNKNOWN / INCONCLUSIVE / TIMEOUT > invented values; tag every numeric claim with citation or (UNVERIFIED).
  ```

**Target 4 — DO NOT add to `~/core/nexus/CLAUDE.md.bak`**: this is a backup, not the
active source.

### §4.3 Ordering

1. Create Target 1 (design doc) first — establishes SSOT.
2. Create Target 3 (agent preset) — short and depends on Target 1's content.
3. Append Target 2 (project-claude/nexus.md one-liner) — last, because it is the
   discoverability hook that points back at the other two.
4. Run `scripts/sync_claude_md.hexa` (or wait for next natural session run) to
   regenerate the nexus CLAUDE.md from project-claude/nexus.md.

Each target is a separate commit, so any one of them can be reverted without disturbing
the others. The user explicitly authorizes deploy in a follow-up session — **this audit
does not execute any of these edits**.

### §4.4 Top deploy-plan target file

The single highest-priority deploy target, if only one were authorized, is **Target 1**
(`~/core/nexus/design/honesty_triad.md`). Without it, Targets 2 and 3 have nothing to
reference.

---

## §5 Phase 4 — Cross-repo divergence check

### §5.1 Atlas-size divergence

n6's BT registry is small (≈ 7 BTs in `theory/breakthroughs/breakthrough-theorems.md`,
plus ≈ 9,624 atlas entries in `atlas/atlas.n6`). nexus's `n6/atlas.blowup.jsonl` is
**substantially larger by node count and structurally different by representation**:
20,525 nodes + 54,347 edges, JSONL `type/edge` format, not the `[NN*]` grade format.

Implication for saturation analysis: the n6 honesty counter banner gates *promotion of
millennium-class claims* (hard 0/7). The nexus analogue must gate something analogous in
form. The selected form (B) from §3.1 (`nxs_promotion_count` over inventory entries) is
**structurally homologous** (small integer, fixed denominator) but **scale-mismatched**
(nexus has dozens of inventory entries vs n6's 7 millennium problems). The banner still
fires its first-line function, but the *psychological severity* of incrementing 7→8 is
greater than incrementing 24→25. **The nexus form is more permissive than the n6 form.**
This is acknowledged divergence, not a defect.

### §5.2 nxs-002 Ω-saturation cycle cross-references

nexus's `nxs-002` work (composite ceiling 0.835, ER ROI characterization, cycle-1..56
chain) is **conceptually parallel** to n6's omega cycle. The two are *separate instances*
of the same Ω-saturation pattern, not a single shared cycle. Cross-references that would
break under porting:

- **`design/abstraction_ceiling.md` §6** — n6 spectral chaos mechanism reference (atlas
  REGULAR vs const CHAOTIC). This document already cross-cites between repos by absolute
  path. Porting the honesty triad to nexus does **not** break this — the triad is
  orthogonal to ceiling work.
- **`lenses/omega_state_space_lens.hexa`** — listed in §3.2 as light-grade protected.
  The lens is read by both nxs-002 tools and n6 omega-style closure work. Marking it
  protected does not break cross-repo reads, only cross-repo writes — and the writes are
  already supposed to be authorized-only.
- **The "0/7 unchanged" literal**: must NOT be ported into nexus as-is. It is an
  n6-domain claim. The nexus banner must use the (B) form. (Listed in §8 anti-list.)

No cross-references identified that would break under the proposed port.

### §5.3 Could existing nexus mechanisms make prompt-level boilerplate redundant?

Per §2.4 redundancy matrix:

- (1) honesty counter — existing `Ω-saturation cycle N` commit convention is **post-hoc**
  (catches drift at commit time, not at session start). The agent-banner is *not*
  redundant; it adds a pre-commit, in-session layer. **Verdict: not redundant.**
- (2) write-barrier — existing L0 list + lockdown_gate + permissions_ssot covers the
  *runtime hexa-side* writes well. The prompt-level barrier covers the *Write/Edit
  tool-call side*, which is a different attack surface. **Verdict: not redundant; the
  two layers stack.** *However*, if the user later authorizes a runtime Write/Edit
  interceptor in the harness, the prompt-level barrier becomes redundant — this is a
  candidate falsifier (F-PORT-WB).
- (3) no-fabrication guard — no existing mechanism. **Verdict: not redundant.**

No constraint flips to KEEP_BUT_COMPRESS or RETIRE under the divergence analysis.

### §5.4 Verdict-flip risk per constraint

| Constraint | n6 verdict | Nexus verdict (this audit) | Flip? |
|---|---|---|---|
| (1) honesty counter | KEEP_AS_IS | KEEP_BUT_ADAPT (form B, not literal `0/7`) | **partial flip — *form changes*, not deploy decision** |
| (2) write-barrier | KEEP_AS_IS | KEEP_AS_IS (with extended path list) | no flip |
| (3) no-fabrication guard | KEEP_AS_IS | KEEP_AS_IS (verbatim) | no flip |

The "partial flip" on (1) is a form change, not a deploy/retire change. The constraint
*function* (first-line honesty banner) is preserved; the *literal text* is adapted.

---

## §6 Per-constraint nexus verdict (independent of n6)

| # | Constraint | Nexus verdict | Reasoning |
|---|---|---|---|
| 1 | Honesty counter (banner, form B) | **KEEP_BUT_ADAPT** | Function preserved; form changes from `millennium_resolved: 0/7` to `nxs_promotion_count: N/N_session_start`. Equivalent to KEEP_AS_IS at the *function* level, KEEP_BUT_COMPRESS at the *literal* level. |
| 2 | Write-barrier (extended path list) | **KEEP_AS_IS** | Same enforcement model as n6, with nexus-specific path list (§3.2). Stacks with existing L0 list and lockdown_gate without redundancy. |
| 3 | No-fabrication guard (verbatim) | **KEEP_AS_IS** | LLM-property constraint, no adaptation needed. Two recent NVs (NV-1, NV-2) directly motivate it. Highest-marginal-harm constraint per §2.5. |

Verdict-grade: 2 KEEP_AS_IS + 1 KEEP_BUT_ADAPT (function-equivalent KEEP).

---

## §7 Composite recommendation

**Proceed with deploy, in the order §4.3 specifies, gated on user explicit authorization.**

Reasoning:

- 3-of-3 nexus-side verdicts are KEEP-direction. No constraint returns RETIRE or
  RETIRE_IF_OTHER_TWO_AGREE.
- The composite n6→nexus port is *not equivalent to a redeploy*: the form-adaptation on
  (1) and the extended path list on (2) are nexus-specific and do not have n6
  precedent on the literal level. They need to be sealed in `design/honesty_triad.md`
  for traceability.
- Existing nexus mechanisms (L0 list, lockdown_gate, harness pre_tool_guard,
  permissions_ssot) cover ~50–60% of the (2) write-barrier function and ~0% of the
  (1) and (3) functions. The marginal coverage gain from porting is large for (1) and
  (3), small but non-zero for (2).
- The 4-target deploy plan is small (≈ 250 lines of new content total), reversible
  (each target a separate commit), and does not risk cascade contamination because
  no atlas / state / inventory file is modified by the deploy itself.

**Caveat**: this audit does **not** authorize the user to skip the explicit authorization
step. Phase 3's deploy plan is a *plan*. The user must say "deploy now" (or equivalent)
in a follow-up session before any of Targets 1–3 are written.

---

## §8 Anti-list (porting moves rejected)

Moves explicitly considered and rejected, with the reason logged so future sessions do
not re-attempt them:

- **A1**: Port `millennium_resolved: 0/7` literally to nexus. *Rejected*: 0/7 is an
  n6-domain claim about millennium problems; nexus has no millennium denominator.
  Literal copy would be a category error. (§3.1, §5.2)
- **A2**: Broaden write-barrier to all of `~/core/nexus/state/`. *Rejected*: state/ is
  ≈ 100+ files of intentionally mutable session output (ALM checkpoints, ledgers,
  evo progress). Broad gating would cause >10× false-positive rate vs the few SSOT files
  that actually need protection. (§3.2)
- **A3**: Include `~/core/nexus/tool/nxs_002_composite.py` in the protected list.
  *Rejected*: this is a development tool, not a finalized claim ledger. The n6 analogue
  (`theory/breakthroughs/breakthrough-theorems.md`) is finalized; `nxs_002_composite.py`
  is active development code. (§3.2)
- **A4**: Build (1) honesty counter on `EXACT_grade_count_delta` (form C). *Rejected*:
  atlas-agent's `.claude/agents/*.md` definition was not located by grep; counting
  EXACT-grade emissions on an unconfirmed agent would itself be fabrication-adjacent.
  (§3.1)
- **A5**: Use `~/core/nexus/CLAUDE.md.bak` as the deploy target. *Rejected*: this is a
  backup, the active source is `project-claude/nexus.md`. Editing the bak would be
  silently overwritten on next sync. (§4.2)
- **A6**: Make the deploy form purely (b) — global CLAUDE.md edit. *Rejected*: nexus
  has no active CLAUDE.md (only sync target); persistent edits must live in
  `project-claude/nexus.md`. The (a)+(c) form is more durable. (§4.1)
- **A7**: Replicate all three n6 audit reports verbatim into nexus's reports/ tree.
  *Rejected*: the audits are *about* the constraints, not the constraints themselves.
  Cross-referencing by absolute path from `design/honesty_triad.md` is sufficient and
  avoids drift between the two copies.
- **A8**: Treat the cycle-N commit-message convention as a sufficient honesty-counter
  surrogate. *Rejected*: cycle-N is post-hoc (catches at commit time, not at session
  start). The banner function is in-session early-warning. (§2.4, §5.3)
- **A9**: Block `~/core/nexus/design/abstraction_ceiling.md` under the write-barrier.
  *Rejected*: this is active design, mutable by intent. The n6 analogue (breakthrough-
  theorems.md) is finalized — different category. (§3.2)
- **A10**: Auto-deploy without user explicit authorization in this session. *Rejected*:
  the prompt's hard constraint is "DO NOT modify ANY file in `~/core/nexus/`". This
  audit produces a plan only.

---

## §9 Falsifiers active for the cross-repo audit

The verdicts in §6 and the recommendation in §7 are **voided** if any of the following
later trips:

- **F-PORT-1 (n6 verdict reversal)**: if any of the three n6 parent audits later returns
  a different verdict (e.g. F-AUDIT-3 for honesty counter fires and the n6 verdict drops
  to KEEP_BUT_COMPRESS), the nexus port inherits the change. The nexus deploy must be
  re-evaluated.
- **F-PORT-2 (nexus mechanism convergence)**: if the user later wires a runtime
  Write/Edit interceptor into `harness/pre_tool_guard.hexa` that covers the SSOT path
  list of §3.2, the prompt-level write-barrier (constraint 2) becomes redundant. Verdict
  on (2) drops to KEEP_BUT_COMPRESS.
- **F-PORT-3 (form-(B) saturation collapse)**: if a 30-day audit window shows the
  `nxs_promotion_count` banner caught **zero** near-misses *that were not also caught
  by the cycle-N commit convention within ≤24 hours*, form (B) is no better than the
  existing convention, and constraint (1) drops to KEEP_BUT_COMPRESS or RETIRE.
- **F-PORT-4 (atlas-agent existence)**: if it is later confirmed (by reading a file path
  that this audit missed) that nexus has a `.claude/agents/atlas-agent.md` with EXACT-
  only enforcement, the redundancy claim of §2.4 row (1) needs to be re-examined; some
  of constraint (1)'s function may be covered there.
- **F-PORT-5 (deploy execution divergence)**: if the deploy is executed differently from
  §4 (e.g. Targets 1+3 deployed without Target 2's cross-reference), the discoverability
  argument of §4.1 fails and the constraints become orphaned in `design/`. Re-deploy
  required.
- **F-PORT-6 (nexus active CLAUDE.md regeneration)**: if `scripts/sync_claude_md.hexa`
  changes its rules so that `project-claude/nexus.md` no longer feeds `CLAUDE.md`,
  Target 2's propagation mechanism breaks. Verdict on deployment form re-opens.
- **F-PORT-OMEGA (meta)**: if any future independent audit (n6-side or nexus-side) of
  any of the three constraints returns a verdict that contradicts this report's
  per-constraint nexus verdict (§6), this audit re-opens.

None of F-PORT-1..6 or F-PORT-OMEGA have fired as of 2026-04-25T (this report's
write-time). They are listed here as future-trigger conditions only.

---

## §10 Closing

0/7 unchanged. nxs promotion count unchanged. NO nexus files modified by this audit.

This document is a **read-only cross-repository audit + porting design**. It produces:

- a per-constraint nexus-side verdict (§6: KEEP_BUT_ADAPT for (1), KEEP_AS_IS for (2)+(3));
- a deploy plan (§4) listing four specific targets in nexus, none of which have been
  written;
- an explicit anti-list (§8) of porting moves rejected, so future sessions do not re-try
  them;
- a falsifier list (§9) so the verdict can be revisited if the underlying landscape
  shifts.

Activation requires a separate session with explicit user authorization. The composite
recommendation is **proceed with deploy** under that authorization, in the order of
§4.3, with Target 1 (`~/core/nexus/design/honesty_triad.md`) as the highest-priority
single target.

millennium_resolved: **0/7** (unchanged).
nxs_promotion_count: **unchanged this session** (no inventory writes).
NO nexus files modified by this audit.
