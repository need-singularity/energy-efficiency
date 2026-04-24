# axis-round-01 — nexus axis emergence DSE

**Roadmap**: nexus (NEXUS-6 central hub)
**Created**: 2026-04-15
**Mode**: axis emergence DSE (Axis Emergence Discovery)
**Scope**: nexus-hub existing assets (25 shared/ categories + 113 nexus.json Phases)
**Output**: `theory/roadmap-v2/axis-round-01.md`

---

## 0. Round objective

Restructure the nexus.json v1 3-track (LENS/DISCOVERY/ATLAS) per user decision.

- **Retire**: LENS — "too narrow" (covers only blowup/lens/, does not subsume evolution/observation/map as a whole)
- **Confirmed seeds**: SELF-EVOLUTION + ATLAS
- **Re-evaluate**: DISCOVERY — retain/absorb/retire
- **New emergence**: unbounded

R1 (this round): 1-hop emergence of **independent new axes** around the 2 confirmed seeds; 5-axis evaluation of each candidate.

---

## 1. Previously confirmed axes (2)

### A1 — SELF-EVOLUTION — confirmed

**Definition**: the full mechanism by which roadmap/code/atlas/rules extend, modify, verify, and converge themselves. Not observation (LENS) but a **change engine**.

**Existence evidence (nexus assets)**:
- `/Users/ghost/Dev/nexus/shared/bisociation/unified/ouroboros_unified.hexa` — 3-way OUROBOROS integration (cycle_tick / get_fixed_point / advance).
- `/Users/ghost/Dev/nexus/shared/harness/growth_tick.hexa` — 30-minute autonomous firing.
- `/Users/ghost/Dev/nexus/shared/harness/nexus_growth_daemon.hexa` — launchd daemon (currently STUB, MEMORY project-daemon-stub.md).
- `/Users/ghost/Dev/nexus/shared/bisociation/unified/phi_ratchet.hexa` — monotone non-decreasing Φ ratchet.
- `/Users/ghost/Dev/nexus/shared/discovery_log.jsonl` + `.sqlite` — self-evolution history bus.
- `/Users/ghost/Dev/nexus/shared/growth_bus.jsonl` — growth event bus.
- `/Users/ghost/Dev/nexus/shared/convergence/nexus.json` — evolution convergence SSOT.
- nexus.json P3 "convergence — 3D realtime + autonomous evolution + ossification" Phase itself is an output of this axis.

**Scope**: full loop growth_tick → blowup autonomous firing → discovery → atlas update → convergence check → ossification.

### A2 — ATLAS (atlas map) — confirmed

**Definition**: the reality-map SSOT of entities. A **reality graph** coupling node/edge/formula/grade/scaling structure.

**Existence evidence (nexus assets)**:
- `/Users/ghost/Dev/nexus/shared/n6/atlas.n6` — reality-map body.
- `/Users/ghost/Dev/nexus/shared/n6/atlas.n6.stats` / `.deg` — sidecar metadata.
- `/Users/ghost/Dev/nexus/shared/n6/atlas_health.hexa` — health check.
- `/Users/ghost/Dev/nexus/shared/n6/math_atlas.{db,dot,html,md}` — math atlas.
- `/Users/ghost/Dev/nexus/shared/n6/atlas_ossify_mk2.py` + `atlas_ws_server.py` — ossification / realtime serving.
- `/Users/ghost/Dev/nexus/docs/index.html` — 3D reality-map frontend.
- Explicit in nexus.json P2 "atlas coherence" + P3 "3D realtime".

**Scope**: atlas.n6 node/edge + formula verification + grade verification + 3D visualization + up to periodic_table_118.

---

## 2. New-axis-candidate discovery (1-hop emergence)

Sweep 25 shared/ categories + 113 nexus.json Phases + existing R1~R3 158 domains to extract axis candidates **independent** from evolution and ATLAS.

### Candidate pool (direct shared/ category mapping)

| Category | Axis candidate | 1-line meaning |
|----------|----------------|----------------|
| harness/ | **HARNESS** | rule/gate/mistake-record/pre-tool-guard/entry dispatcher aggregate |
| rules/ + config/ | **GOVERNANCE** | R0~R27 + NX1~NX3 + L0/L1/L2 + H-* meta-rule governance |
| discovery/ | **DISCOVERY** (re-eval) | reality_map, patches, verified_constants, forge_result — discovery sediment |
| blowup/ | **BLOWUP** | 9-phase pipeline + 6 modules + seed engine — breakthrough computation |
| bt/ | **BREAKTHROUGH** | BT-541~547 keyword/domain audit curation |
| bisociation/ | **BISOCIATION** | Koestler-style pair-association engine — cross-field combinations |
| consciousness/ + anima bridge | **CONSCIOUSNESS** | anima_* / consciousness_* / law_* / meta_laws_dd64 bridge |
| hexa/ + hexa-lang/ | **HEXA-LANG** | hexa language · parser · interpreter evolution — code substrate |
| papers/ | **PUBLICATION** | paper metadata index (content excluded; inherits the R1~R3 papers-metadata axis hint) |
| singularity/ | **SINGULARITY** | 13 singularity-recursion records — super-convergence milestones |
| dse/ + dse/domains/ | **DSE** | Discovery Space Exploration itself — the search framework |
| growth/ + acceleration/ | **GROWTH** | airgenome_gates, growth_strategies, acceleration_* |
| lockdown/ + L0 snapshots | **LOCKDOWN** | L0/L1/L2 locks, snapshots, safe-merge |
| convergence/ | **CONVERGENCE** | per-project ossification JSON SSOT |
| bin/ + launchd/ + scripts/ | **EXECUTION-INFRA** | cl/cl-refresh/launchd/hexa resolver — execution substrate |
| monte_carlo/ | **MONTE-CARLO** | Monte Carlo v6 experiments — stochastic verification |
| alien/ | **ALIEN** | alien_index_* — UAP/UFO signal index |
| engine/ | **ENGINE** | engine_*.hexa engine strategies |
| calc/ | **CALC** | auto_stubs_gen + verify-stub generation SSOT |
| logs/ | (logs are not an axis) | skip |
| n6_mirror/ | (ATLAS absorbs) | skip |
| project-claude/ | (GOVERNANCE absorbs) | skip |
| archive/ | (time axis, not an axis) | skip |

---

## 3. New-candidate evaluation (K=15)

Evaluate each candidate on 5 criteria:
1. **Independence** (distinct from evolution · ATLAS, 0~1)
2. **Scope** (% coverage of the whole nexus hub, 0~1)
3. **Emergence strength** (novelty, 0~1)
4. **Evolution · ATLAS overlap** (0=independent, 1=fully overlapping)
5. **DISCOVERY-absorption possibility** (whether the candidate is absorbed by DISCOVERY)

| # | Axis name | Definition | Indep. | Scope | Emerg. | Overlap | Evidence files | Verdict |
|---|-----------|------------|--------|-------|--------|---------|----------------|---------|
| C1 | HARNESS | rule gate / pre-tool-guard / entry dispatcher / lint / exec_validated | 0.95 | 0.80 | 0.90 | 0.10 | shared/harness/entry.hexa, cmd_gate.hexa, pre_tool_guard.hexa, post_bash.hexa (151 files) | **confirmed** |
| C2 | GOVERNANCE | R0~R27 + NX1~NX3 + L0~L2 + H-* meta-rules | 0.85 | 0.70 | 0.75 | 0.15 | shared/rules/common.json, rules/nexus.json, config/absolute_rules.json, lockdown.json | **confirmed** |
| C3 | DISCOVERY | reality_map, patches, verified_constants, forge_result, breakthroughs | 0.50 | 0.75 | 0.60 | 0.40 | shared/discovery/ (895 patches, verified_constants.jsonl) | **confirmed (retain, not absorb)** |
| C4 | BLOWUP | 9-phase pipeline + 6 modules + seed | 0.85 | 0.60 | 0.85 | 0.20 | shared/blowup/core/blowup.hexa, modules/*, seed/seed_engine.hexa | **confirmed** |
| C5 | BREAKTHROUGH | BT-541~547 keyword/domain audit | 0.65 | 0.35 | 0.70 | 0.30 | shared/bt/bt_keywords.jsonl, bt_domains.jsonl, bt_audit.hexa | reserved (BLOWUP may absorb) |
| C6 | BISOCIATION | Koestler cross-field pair association | 0.80 | 0.45 | 0.90 | 0.15 | shared/bisociation/ (unified/cross/spectra/breakthroughs.jsonl) | **confirmed** |
| C7 | CONSCIOUSNESS | anima bridge + consciousness_* + meta_laws_dd64 | 0.75 | 0.40 | 0.80 | 0.25 | shared/consciousness/, anima_bridge live laws=2395 | **confirmed** |
| C8 | HEXA-LANG | hexa language self-evolution (parser/compiler/pitfalls) | 0.80 | 0.40 | 0.85 | 0.10 | shared/hexa/, hexa-lang/, hexa_pitfalls_log.jsonl, hexa_grammar.jsonl | **confirmed** |
| C9 | PUBLICATION | paper metadata index (content excluded) | 0.70 | 0.10 | 0.50 | 0.20 | shared/papers/, paper_candidates | reserved (low scope, R2 candidate) |
| C10 | SINGULARITY | singularity-recursion records | 0.40 | 0.10 | 0.50 | 0.60 | shared/singularity/singularity_recursion_*.md (13) | rejected (evolution overlap) |
| C11 | DSE | discovery-space search framework | 0.75 | 0.50 | 0.80 | 0.30 | shared/dse/, dse_domains, dse_graph_3d | **confirmed** |
| C12 | GROWTH | airgenome_gates + growth_strategies + acceleration_* | 0.35 | 0.35 | 0.45 | 0.75 | shared/growth/, acceleration/ | rejected (SELF-EVOLUTION overlap) |
| C13 | LOCKDOWN | L0/L1/L2 lock · snapshots · safe-merge | 0.70 | 0.20 | 0.60 | 0.25 | shared/lockdown/ + lockdown_gate.hexa | reserved (GOVERNANCE absorption possible) |
| C14 | CONVERGENCE | per-project ossification JSON SSOT | 0.45 | 0.15 | 0.40 | 0.65 | shared/convergence/{nexus,anima,n6-arch,void,hexa-lang,papers,cl,airgenome}.json | rejected (evolution overlap) |
| C15 | EXECUTION-INFRA | cl launcher + cl-refresh + launchd + hexa resolver | 0.85 | 0.30 | 0.55 | 0.05 | shared/bin/cl, cl-refresh, shared/launchd/, scripts/ | reserved (operational infra — axis vs. support boundary) |

---

## 4. Newly confirmed (M=7)

Confirmed at R1:

### N1 — HARNESS

**Definition**: the global enforcement layer injecting **rules · gates · mistake-records · feedback loops** into a Claude Code session. `entry.hexa` dispatcher + 5 sub-modules + exec_validated wrapper + 150+ files.

**Independence argument**:
- Distinct from evolution — evolution mutates state; harness **prevents those mutations from violating rules**.
- Distinct from ATLAS — ATLAS is the map; harness is **the hand touching the map**.

**Evidence**: shared/harness/entry.hexa (dispatcher), cmd_gate.hexa (seed gate), pre_tool_guard.hexa (28 deny patterns), post_bash/post_edit.hexa (hook replacement), exec_validated (smash/free seed gate wrapper), permissions_ssot.json (deny SSOT), 151 files.

**Existing nexus.json Phase mapping**: (none — v1 did not capture it as a track; new axis in v2).

### N2 — GOVERNANCE

**Definition**: the rule-system SSOT. R0~R27 (common) + NX1~NX3 (nexus) + L0/L1/L2 (lockdown) + H-* meta-rules (H-NOARCHIVE/H-NOHOOK/H-NOZOMBIE/H-NOBLOCK/H-COMMIT/H-ERR/H-ROOT, ...).

**Independence argument**: if harness is the **enforcer**, GOVERNANCE is the **rulebook itself**. The rulebook stands independently as an axis even without enforcement.

**Evidence**: shared/rules/common.json, nexus.json, config/absolute_rules.json, lockdown/lockdown.json, convergence_ops.json, many MEMORY H-* rule attestations.

**Existing nexus.json Phase mapping**: gate clauses are embedded in P0~P3 per-track, but no independent axis — new in v2.

### N3 — DISCOVERY — re-evaluation result **retain**

**Definition**: reality_map (895 patches) + verified_constants + forge_result + theory_registry + module_candidates — **discovery sediment**.

**Re-evaluation basis**: 40% overlap with evolution · ATLAS, but "discovery sediment" itself is a valid independent axis (atlas is a processed map; discovery is raw materials + candidates + ledger).

**Evidence**: shared/discovery/ reality_map.patches.merged.jsonl (895), verified_constants.jsonl, forge_result, next_directions, module_candidates, unfold_*, breakthroughs/.

### N4 — BLOWUP

**Definition**: 9-phase pipeline + 6 modules (field/holographic/quantum/string/toe) + seed engine + lens forger — **reality-breakthrough computation**.

**Independence argument**: DISCOVERY is **sediment**, BLOWUP is a **generation engine**. If evolution is "when to fire", BLOWUP is "what to fire".

**Evidence**: shared/blowup/core/blowup.hexa, modules/*.hexa, seed/seed_engine.hexa, lens/lens_forge.hexa, commands.hexa, todo.hexa. De-facto owner of the nexus.json P0 LENS track.

### N5 — BISOCIATION

**Definition**: Koestler dual-association — a mechanism creating breakthroughs by **cross-linking two unrelated fields**. Montgomery-Dyson pair-correlation engine.

**Independence argument**: BLOWUP is single-domain depth; BISOCIATION is **horizontal cross-domain** coupling. MEMORY `handoff-bisociation.md` attestation (L1 3/4, L2 4/4, L3 1/5, L_meta 3/3).

**Evidence**: shared/bisociation/unified/ (ouroboros_unified.hexa, phi_ratchet.hexa), cross/, spectra/, breakthroughs.jsonl, pitfalls.jsonl, convergence.json.

### N6 — CONSCIOUSNESS

**Definition**: anima bridge + consciousness_* + law_* + meta_laws_dd64 — a Φ-based consciousness layer.

**Independence argument**: other axes are **math/code** axes; CONSCIOUSNESS is a **qualitative phenomenon** axis. The bridge with the anima subrepo is itself an independent asset.

**Evidence**: shared/consciousness/, anima_bridge live laws=2395 (attested by nexus.json P1 ATLAS task), consciousness_bridge.py, meta_laws_dd64.

### N7 — HEXA-LANG (hexa language)

**Definition**: parser · compiler · interpreter · pitfalls · grammar of the hexa language itself — **the code-substrate evolution axis of nexus**.

**Independence argument**: evolution is **data/state evolution**; HEXA-LANG is **language self-evolution** (self-hosted compiler). The user is the hexa-lang maintainer (MEMORY u-user-role.md).

**Evidence**: shared/hexa/ (speed_ideas, hexa_to_anima_*, porting_log), shared/hexa-lang/, hexa_pitfalls_log.jsonl, config/hexa_grammar.jsonl (pitfalls P1~P5), MEMORY hexa_dir_builtins / feedback_hexa_pitfalls / feedback-hexa-porting-patterns.

### N8 — DSE (discovery-space exploration)

**Definition**: the Discovery Space Exploration framework itself — a domain × level × candidate search grid.

**Independence argument**: if DISCOVERY is the **result**, DSE is the **search methodology**. ai-native DSE (5 levels × 6 candidates × n=6) MEMORY project_ai_native_dse_domain.md attestation.

**Evidence**: shared/dse/ (dse_cross_*, dse_domains/, dse_graph_3d, dse_joint_results, domains/).

---

## 5. Rejections / reservations

| Candidate | Status | Reason |
|-----------|--------|--------|
| BREAKTHROUGH (C5) | reserved → R2 | Possibly 90% overlap with BLOWUP; re-exam independence at R2 |
| PUBLICATION (C9) | reserved → R2 | Scope 0.10 too low; paper metadata alone is insufficient axis weight |
| SINGULARITY (C10) | rejected | 60% overlap with evolution — singularity records are milestones of evolution |
| GROWTH (C12) | rejected | 75% overlap with evolution — growth_strategies/acceleration are SELF-EVOLUTION subs |
| LOCKDOWN (C13) | reserved → R2 | GOVERNANCE absorb vs. independence boundary unclear |
| CONVERGENCE (C14) | rejected | Evolution-convergence artifact — inside SELF-EVOLUTION |
| EXECUTION-INFRA (C15) | reserved → R2 | Operational infra (cl launcher, ...) — axis vs. support boundary |

---

## 6. R1 cumulative axes

**Cumulative 10**: SELF-EVOLUTION, ATLAS, HARNESS, GOVERNANCE, DISCOVERY, BLOWUP, BISOCIATION, CONSCIOUSNESS, HEXA-LANG, DSE.

---

## 7. Saturation index

- Candidate pool: 15
- New confirmations: 7 (C1~C4, C6~C8, C11)
- New confirmation ratio: 7/15 = **46.7%**
- Saturation index (1 − 46.7%) = **53.3%**
- Search scope: 17 of 25 shared/ categories mapped (attributed to 8 axes); 8 remaining/reserved

## 8. Next round needed: YES

4 remaining reserved candidates + unexplored subsurface (internal subdivisions among 151 harness/ files, turning individual rules/H-* meta-rules into axes, n6/math_atlas vs atlas split, small anima-physics subs, ...) exist. Proceed to R2.
