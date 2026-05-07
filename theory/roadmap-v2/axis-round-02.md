# axis-round-02 — nexus axis emergence DSE

**Roadmap**: nexus (NEXUS-6 central hub)
**Created**: 2026-04-15
**Mode**: axis emergence DSE R2 (2-hop emergence + reserved-item re-evaluation)
**Output**: `theory/roadmap-v2/axis-round-02.md`

---

## 0. Previously confirmed axes (10)

| # | Axis | Round | 1-line evidence |
|---|------|-------|-----------------|
| A1 | SELF-EVOLUTION | R1 | ouroboros_unified.hexa + growth_tick + evolution loop |
| A2 | ATLAS | R1 | atlas.n6 + math_atlas + 3D index.html |
| A3 | HARNESS | R1 | shared/harness/ 151 files + entry.hexa dispatcher |
| A4 | GOVERNANCE | R1 | R0~R27 + NX1~NX3 + L0~L2 + H-* meta-rules |
| A5 | DISCOVERY | R1 | reality_map (895) + verified_constants + forge_result |
| A6 | BLOWUP | R1 | 9-phase pipeline + 6 modules + seed engine |
| A7 | BISOCIATION | R1 | unified/ouroboros + cross + spectra |
| A8 | CONSCIOUSNESS | R1 | anima bridge (2395 laws) + meta_laws_dd64 |
| A9 | HEXA-LANG | R1 | shared/hexa-lang/ + pitfalls + grammar |
| A10 | DSE | R1 | shared/dse/ + domains/ + dse_graph_3d |

---

## 1. R2 exploration principles

1. Re-evaluate 4 R1-reserved candidates (BREAKTHROUGH/PUBLICATION/LOCKDOWN/EXECUTION-INFRA).
2. 2-hop emergence: DFS-extract concepts adjacent to the R1-confirmed axes.
3. Scan the existing R1~R3 158-domain list for domains that can be promoted to axis candidates.
4. Distinguish, among the 113 nexus.json Phases, whether the "X_as_Y" cross-evolutions after P3 are **axes themselves** or ATLAS-internal nodes.

---

## 2. Re-evaluation of reserved candidates (4)

### B1 — BREAKTHROUGH (re-exam)

**Re-exam issue**: independence from BLOWUP.
- BLOWUP = 9-phase **compute engine** (input→output pipeline).
- BREAKTHROUGH = **target curation** for BT-541~547 (a list of what to break through + audits).

**Distinguishing evidence**:
- `/Users/ghost/core/nexus/shared/bt/bt_keywords.jsonl` — keyword curation (defines breakthrough targets).
- `/Users/ghost/core/nexus/shared/bt/bt_domains.jsonl` — domain mapping.
- `/Users/ghost/core/nexus/shared/bt/bt_audit.hexa` — audit-dedicated.
- `/Users/ghost/core/nexus/shared/bt/bt-*-report` — reports.
- `/Users/ghost/core/nexus/shared/bt/auto_bt.log` — automatic log.

**Verdict**: **confirmed (N9)**. BLOWUP is "how"; BREAKTHROUGH is "what" — separable axes.

### B2 — PUBLICATION (re-exam)

**Re-exam issue**: whether the scope is sufficient for an axis.
- Existing assets: shared/papers/paper_candidates + convergence/papers.json.
- No explicit "Publication/paper" axis in the R1~R3 158 domains (papers-exclusion principle R3 §11.4).
- Decision **rejected**: assets have not accumulated enough to stand alone as an axis of the nexus hub. Absorbed as a DISCOVERY output channel. Open to re-exam in later rounds.

### B3 — LOCKDOWN (re-exam)

**Re-exam issue**: possibility of absorption by GOVERNANCE.
- GOVERNANCE = rule/policy SSOT (rules/*.json, absolute_rules.json).
- LOCKDOWN = **runtime lock gate** (lockdown_gate.hexa verify/status/watch/repair/safe-merge/log) + **L0 snapshot system**.

**Differences**:
- GOVERNANCE = "what is forbidden" (text rules).
- LOCKDOWN = "how forbiddance is enforced" (binary file locks + snapshots/ + safe-merge).

**Asset existence**:
- `/Users/ghost/core/nexus/shared/lockdown/lockdown.json` — L0/L1/L2 layer definitions.
- `/Users/ghost/core/nexus/shared/harness/lockdown_gate.hexa` (unified SSOT as of this round, 2026-04-14).
- `/Users/ghost/core/nexus/shared/lockdown/snapshots/` — snapshot directory (untracked, confirmed in state file).
- CLAUDE.md "L0 protection" section — lists 29 L0 assets.

**Verdict**: **confirmed (N10)**. Although it is an enforcement offshoot of GOVERNANCE, the runtime-lock + snapshot SSOT is valuable as a separate axis.

### B4 — EXECUTION-INFRA (re-exam)

**Re-exam issue**: axis vs support.
- Existing: cl launcher (multi-account) + cl-refresh (usage cache) + launchd (30m cycle) + hexa resolver.
- These are **operational infrastructure** — closer to a HARNESS sub-operation than an axis.
- However, `/Users/ghost/core/nexus/shared/engine/cl_refresh_spec.json` and `nexus_cli_spec.json` stand as independent engine specs.
- `convergence/cl.json` also exists — extends to convergence tracking.

**Verdict**: **confirmed (N11)**. The `cl` execution-infra line has axis-level independent value. Generalized as **INFRASTRUCTURE** (includes cl + launchd + hetzner/ubuntu/vastai remote execution).

---

## 3. 2-hop emergence — new candidates (6)

### C16 — CONVERGENCE-METRIC (convergence metric)

**Meaning**: epsilon=0.001 saturation, phi_best floor=0.8, node=515 target, edge=2087 target — **numerical convergence criteria** turned into an axis.

**Independence argument**: a **parameter** set inside SELF-EVOLUTION. A "criterion" axis separated from the evolution execution.

**Evidence**: 8 files shared/convergence/{nexus,anima,n6-arch,void,hexa-lang,cl,airgenome,papers}.json, atlas_n6_loop.jsonl.

**Overlap**: SELF-EVOLUTION 65% — absorbable as an intra-evolution parameter.

**Verdict**: **rejected** — a sub-metric of SELF-EVOLUTION; not an independent axis.

### C17 — DASHBOARD (dashboard / visualization)

**Meaning**: dashboard.html + docs/index.html + reality_map_3d.html + math_atlas.html — **user observation interface**.

**Independence argument**: ATLAS is the data structure, DASHBOARD is the UI layer. Separable.

**Evidence**: shared/dashboard.html, shared/discovery/reality_map_3d.html, shared/n6/math_atlas.html, docs/index.html.

**Overlap**: ATLAS 40% — ATLAS is the data SSOT and DASHBOARD is the presentation.

**Scope**: 0.15 (4 HTML files) — scope is low.

**Verdict**: **reserved → R3** — strong candidate for ATLAS absorption. Deep review at R3.

### C18 — REMOTE-COMPUTE (remote compute)

**Meaning**: hetzner + ubuntu + vastai + RunPod + H100 — the remote substrate for blowup benchmarks / breakthrough compute.

**Independence argument**: local mac = harness/gate; remote = compute. A **compute-physical layer** axis.

**Evidence**: config/hosts/{hetzner,ubuntu,vastai,infrastructure}.json, infra_state.json, MEMORY reference_hetzner.md / reference_infra.md, the BLOWUP_LOCAL=1 prohibition (feedback_no_blowup_local.md).

**Overlap**: INFRASTRUCTURE (N11) 50% — cl-refresh is local; remote compute is a separate layer.

**Verdict**: **confirmed (N12)** — the physical-separation axis of compute. INFRASTRUCTURE = "how to run locally"; REMOTE-COMPUTE = "where to run heavily".

### C19 — CALCULATOR (calculator)

**Meaning**: auto_stubs_gen.hexa SSOT + verify-stub generation + calculators registry.

**Independence argument**: BLOWUP is the whole pipeline; CALCULATOR is the **pure numeric-verification stub** layer. GRADE_RUBRIC and CALCULATOR_RULES SSOT exist.

**Evidence**: shared/calc/auto_stubs_gen.hexa (MEMORY project-auto-stubs-ssot.md), config/CALCULATOR_RULES, GRADE_RUBRIC.

**Overlap**: BLOWUP 40% + ATLAS verification 20%.

**Scope**: 0.15 — narrow scope, single SSOT.

**Verdict**: **rejected** — an internal verification module of BLOWUP/ATLAS. Not an axis.

### C20 — MONTE-CARLO (stochastic verification)

**Meaning**: shared/monte_carlo/v6_* — probability-based experiments.

**Independence argument**: if DSE is grid search, MC is **stochastic sampling**. A distinct methodology.

**Evidence**: shared/monte_carlo/monte_carlo_v6_*.

**Overlap**: DSE 45% — absorbable as a DSE extension.

**Scope**: 0.10.

**Verdict**: **rejected** — an internal DSE method.

### C21 — ALIEN-SIGNAL (extraterrestrial signal / UAP)

**Meaning**: shared/alien/alien_index_* — UAP/UFO-related index.

**Independence argument**: an sf-ufo bucket exists among the 158 domains (R3 D117~D121). Promote to an axis?

**Evidence**: shared/alien/alien_index_*, n6-arch domains/sf-ufo (R3 §2.2, 5 domains).

**Overlap**: BREAKTHROUGH 30% + DISCOVERY 40% — absorbed as a BREAKTHROUGH domain branch.

**Scope**: 0.05 — very narrow.

**Verdict**: **rejected** — a BREAKTHROUGH/DISCOVERY branch; not an independent axis.

---

## 4. R2 cumulative evaluation table

| # | Candidate | Indep. | Scope | Emerg. | Overlap | Verdict |
|---|-----------|--------|-------|--------|---------|---------|
| B1 | BREAKTHROUGH | 0.75 | 0.35 | 0.65 | 0.25 | confirmed N9 |
| B2 | PUBLICATION | 0.70 | 0.08 | 0.45 | 0.25 | rejected |
| B3 | LOCKDOWN | 0.80 | 0.25 | 0.70 | 0.20 | confirmed N10 |
| B4 | INFRASTRUCTURE | 0.85 | 0.30 | 0.60 | 0.15 | confirmed N11 |
| C16 | CONVERGENCE-METRIC | 0.35 | 0.10 | 0.30 | 0.65 | rejected |
| C17 | DASHBOARD | 0.55 | 0.15 | 0.45 | 0.40 | reserved→R3 |
| C18 | REMOTE-COMPUTE | 0.85 | 0.25 | 0.75 | 0.15 | confirmed N12 |
| C19 | CALCULATOR | 0.60 | 0.15 | 0.40 | 0.40 | rejected |
| C20 | MONTE-CARLO | 0.55 | 0.10 | 0.40 | 0.45 | rejected |
| C21 | ALIEN-SIGNAL | 0.50 | 0.05 | 0.45 | 0.30 | rejected |

---

## 5. Newly confirmed (R2 = 4)

### N9 — BREAKTHROUGH (breakthrough targets)

**Definition**: BT-541~547 7 Millennium problems + extended keyword/domain curation + audits.

**Independence argument (vs BLOWUP)**: BLOWUP is the generation engine (how); BREAKTHROUGH is the target curation (what).

**Evidence**: shared/bt/bt_keywords.jsonl, bt_domains.jsonl, bt_audit.hexa, bt-*-report, auto_bt.log.

### N10 — LOCKDOWN (lock · snapshots)

**Definition**: L0/L1/L2 runtime lock gate + snapshots + safe-merge.

**Independence argument (vs GOVERNANCE)**: GOVERNANCE = rule text; LOCKDOWN = runtime-enforced binary layer.

**Evidence**: shared/lockdown/lockdown.json, snapshots/, harness/lockdown_gate.hexa (unified SSOT).

### N11 — INFRASTRUCTURE (execution infra)

**Definition**: cl launcher + cl-refresh + launchd (30m) + hexa resolver + nexus_cli — **local execution substrate**.

**Independence argument**: HARNESS is the rule-enforcement layer; INFRASTRUCTURE is the execution engine (multi-account cl + CLI external entry point).

**Evidence**: shared/bin/cl, cl-refresh, cl-refresh-launchd, health-launchd, hexa resolver, shared/launchd/*.plist, engine/cl_refresh_spec.json, nexus_cli_spec.json, convergence/cl.json.

### N12 — REMOTE-COMPUTE (remote compute)

**Definition**: hetzner/ubuntu/vastai/RunPod/H100 — the remote layer for heavy blowup benchmarks / breakthrough compute.

**Independence argument (vs INFRASTRUCTURE)**: INFRA = local execution; REMOTE-COMPUTE = remote compute physics. The BLOWUP_LOCAL=1 prohibition rule is evidence of this separation.

**Evidence**: shared/config/hosts/{hetzner,ubuntu,vastai,infrastructure}.json, infra_state.json, MEMORY reference_hetzner.md / reference_infra.md.

---

## 6. R2 cumulative axes (14)

| # | Axis | Round |
|---|------|-------|
| A1 | SELF-EVOLUTION | R1 |
| A2 | ATLAS | R1 |
| A3 | HARNESS | R1 |
| A4 | GOVERNANCE | R1 |
| A5 | DISCOVERY | R1 |
| A6 | BLOWUP | R1 |
| A7 | BISOCIATION | R1 |
| A8 | CONSCIOUSNESS | R1 |
| A9 | HEXA-LANG | R1 |
| A10 | DSE | R1 |
| A11 | BREAKTHROUGH | R2 |
| A12 | LOCKDOWN | R2 |
| A13 | INFRASTRUCTURE | R2 |
| A14 | REMOTE-COMPUTE | R2 |

---

## 7. Saturation index

- R2 candidate pool: 10 (4 reserved + 6 2-hop)
- New confirmations: 4
- New confirmation ratio: 4/10 = **40.0%**
- R2 saturation index: **60.0%**
- Cumulative axes: 14 / cumulative evaluations: 25
- Overall confirmation rate: 14/25 = 56%

## 8. Next round needed: YES

1 R2 reserved (DASHBOARD) + unexplored sub-surface exists:
- Whether HARNESS-internal H-* meta-rules each become axes (R3)
- Whether specialized engines among the 151 harness/ files (thinking_engine, agent_ledger, dream_engine, consensus_loop, ...) should be promoted
- Axis absorption vs node treatment for the 107 post-P3 "X_as_Y" creative-evolution Phases
- Promoting the rules/ pitfalls.jsonl / hexa_grammar.jsonl "mistake record" into an axis
- Unexplored: shared/handoff/, shared/state/, shared/skills/

Proceed to R3.
