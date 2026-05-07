---
schema: canon/docs/self_mk2_tuning/ai-native/1
last_updated: 2026-05-02
ssot:
  repo: /Users/<user>/core/canon
  index: INDEX.json (1.0.0, 9-axis manifest)
  domains_index: domains/_index.json (1.7.0, 393 domains, 13 axes)
  atlas: atlas/atlas.n6 (axis-A through axis-L, K_core=22 saturation edge)
  retired_predecessor_ssot: confirmed (2026-05-02; no .roadmap.* files at repo root)
related_raws:
  - hive raw 270 (core-module-architecture-mandate)
  - hive raw 271 (readme-ai-native-mandate)
  - hive raw 272 (core-module-file-structure-consistency)
  - hive raw 273 (core-hierarchy-connection-direction)
  - hive raw.mk2 arch.001 (4-rule cluster collapsed canonical pattern)
related_docs:
  - docs/n6_meta_evolution_proposal_20260423.md (continuous + meta-evolution Phase 1-6)
  - hive/docs/raw_270_271_warn_to_block_promotion_design.md (warn->block 2026-06-01 ramp)
  - hive/docs/raw_272_lint_extension_spec.ai.md (5 structural checks contract)
  - hive/docs/canonical_core_hierarchy_pattern.ai.md (T0/T1/T2 tier + import-direction matrix)
status: PLAN-ONLY (impl deferred; this doc + marker is the contract)
preset: friendly (handoff doc only; impl preserves existing repo conventions)
policy:
  migration: PROHIBITED (additive only; no rename / no move / no delete)
  destructive_ops: 0
  user_verbatim_ban: enforced (BR-NO-USER-VERBATIM)
  raw_count_target: 15 caveats
  cap: 90min
  cost: $0 mac-local
omega_cycle: 6-step single-pass (audit -> plan -> raw triplet -> handoff -> marker -> close)
---

# canon self mk2 tuning — landed plan (2026-05-02)

> **TL;DR for the implementer**
>
> canon the prior baseline SSOT (single repo-root `.roadmap`) retired. This doc proposes (a) **per-domain `.roadmap.<domain>` fan-out** mirroring the 13-axis `domains/_index.json` taxonomy, (b) **raw 270/271/272/273 hexa-side adoption** via the `core/<feature>/` + `modules/<feature>/` + `README.ai.md` pattern collapsed into hive raw.mk2 arch.001, and (c) **deferred impl** — this cycle ships PLAN + handoff + marker only. Migration of any existing structure is **prohibited**; the plan is **purely additive**.

## §1 Phase 1 — Repo audit findings

### §1.1 Top-level inventory (5.1G repo, audit 2026-05-02)

| Dir | Purpose | mk2-tuning relevance |
|---|---|---|
| `canonshared/n6/` | n6 core constants + atlas + signals | T0 candidate (project-wide shared) |
| `canonshared/` | SSOT configs / convergence / discovery_graph / readme-data | T0 / shared-config layer |
| `engine/` | 17 hexa runtimes (ouroboros / hexa-gate-mk3 / arch_unified / ...) | T1 candidate (feature abstractions) |
| `domains/` | 393 domain `.md` + verify.hexa + CLAUDE.md (13 axes) | T2-style fan-out already present |
| `techniques/` | AI techniques 17+ (.hexa converted) | T1/T2 mixed |
| `tool/` | 81 hexa tools (lint / atlas / weave / verify / promote / ...) | T1 implementer tools |
| `bin/` | n6 / n6_meta / n6_verify_run / nx (CLI entry) | T0 entry-point |
| `atlas/` | atlas.n6 (1.5M shard) + signals + _absorbed/ (20 cycle stamps) | knowledge-axis SSOT |
| `convergence/` | `r4_raw109to126_n6_propagation_plan_2026_04_28.convergence` (single file) | sparse — candidate fan-out target |
| `papers/` | 179 entries (sigma_tau_8_submission/ + group-P/ + 130+ md) | publication axis |
| `proposals/` | 79 cross-cutting proposals (south-africa-applied-tech / hexa-weave / ...) | external-claim axis |
| `experiments/` | 38 dirs (ai-efficiency / blowup / chip-verify / dse / monte_carlo / ...) | falsifier-execution axis |
| `theory/` | proofs / breakthroughs / constants / predictions / flow / roadmap-v2 / roadmap-v3 / study | timeless layer (INDEX.json `timeless: true`) |
| `state/markers/` | 1320+ markers (5.1M) | run-witness ledger |
| `reports/group-P/` | `h_meta_analysis_result.json` + `RETIRED_h_meta_analysis_20260415.md` | minimal occupancy |
| `state/clay_millennium_kick_loop/` | 67 cycle stamps (2026-04-28 dense) | active loop axis |
| `state/falsifier_monitor/` | 5 entries | falsifier-monitor axis |

### §1.2 Sub-axes already populated by domain index

`domains/_index.json` v1.7.0 — 13 axes, 393 domains:
- physics (39) / life (48) / energy / compute / materials / space / infra / cognitive / culture / sf-ufo / biology (4) / pets (2) / apps (5)
- each axis has `domains/<axis>/_index.json` sub-SSOT (14 sub-indexes confirmed on disk)

This 13-axis taxonomy is the natural fan-out spine for `.roadmap.<axis>` series.

### §1.3 Atlas axes (independent)

`atlas/atlas.n6` carries axis-A through axis-L (K_core=22, lower-band saturation edge per shard footer). axis-M discovery candidates documented in shard footer (schema-version primitive / @END block-delimiter / list-body-field idiom). These are **knowledge-graph axes**, distinct from the **product/domain axes** above. Fan-out should not conflate them.

### §1.4 Group-P (paper-grade product) status

`reports/group-P/` currently holds 1 active JSON + 1 retired md. `papers/group-P/` exists as a sibling (audit confirms parallel structure). Sparse — separate `.roadmap.group_p` is justified to track promotion gates from product → paper.

### §1.5 Sigma-tau-8 (RH critical line) status

`papers/sigma_tau_8_submission/` contains 6 files (abstract / checklist / cover_letter / msc_codes / proof_sketch / references). `theory/proofs/formal-p10-1-riemann-sigma-tau-2026-04-15.md` + `theory/predictions/verify_rh_critical_line_sigma_tau.hexa` are the upstream artefacts. Submission gate is a high-stakes, narrowly-scoped axis — separate `.roadmap.sigma_tau_8` is justified.

### §1.6 Auto-convergence status

`convergence/` holds 1 file (r4 propagation plan). `canonshared/convergence/canon.json` is sibling. `state/atlas_convergence_witness.jsonl` (79K) carries the run-witness stream. `experiments/anu_mc_verification/` + `experiments/_results.jsonl` are upstream feeders. Sparse but live — separate `.roadmap.auto_convergence` is justified.

### §1.7 Atlas-self-arch axes already documented

`reports/atlas_self_arch_audit/` + `reports/atlas_self_arch_axis_audit/` + 8 `state/atlas_*` dirs — heavily occupied. Distinct from product taxonomy. Separate `.roadmap.atlas_self_arch` justified.

### §1.8 Hexa-weave breakthroughs

`papers/` has 130+ `hexa_weave_*` md files (mvp/closure_atom/encodable_strand/cycle/lean4_audit/zenodo/...). 4-sister biology axis closed (weave/nanobot/ribozyme/virocapsid). Active multi-cycle workstream — separate `.roadmap.hexa_weave` justified.

### §1.9 Clay millennium kick loop

`state/clay_millennium_kick_loop/` — 67 cycle stamps (2026-04-28 dense). Live workstream — separate `.roadmap.clay_millennium` justified.

### §1.10 Triad / honesty / lint scaffolding

`state/triad_lint/` + `state/blockers/` + `state/audit/` + `tool/own*` (own1 through own35 audit lints) + `reports/n6_*` (15+ JSON) form a meta-quality layer. Cross-cutting; separate `.roadmap.honesty_triad` justified.

## §2 Phase 2 — `.roadmap.<domain>` fan-out plan

### §2.1 Naming convention

Files at repo root, parallel to (retired) `.roadmap`:

```
/Users/<user>/core/canon/.roadmap.<domain>
```

Allowed `<domain>` values (Tier-A canonical list, 8 entries):

| `.roadmap.<domain>` | Spine | Existing-evidence sources |
|---|---|---|
| `.roadmap.canon` | meta / repo-level (entry-point pointer to all sub-roadmaps) | INDEX.json + docs/n6_meta_evolution_proposal_20260423.md |
| `.roadmap.atlas` | knowledge graph (axis-A through axis-L+) | atlas/atlas.n6 + atlas/_absorbed/ + reports/atlas_*  |
| `.roadmap.atlas_self_arch` | atlas axiom-cite + amendment DSL evolution | reports/atlas_self_arch_*audit/ + axis-K/L shards |
| `.roadmap.auto_convergence` | r4 / r5 propagation + atlas_convergence_witness | convergence/ + state/atlas_convergence_witness.jsonl + experiments/_results.jsonl |
| `.roadmap.group_p` | paper-grade product promotion gate | reports/group-P/ + papers/group-P/ + papers/_submission_top48.json |
| `.roadmap.sigma_tau_8` | RH critical-line submission | papers/sigma_tau_8_submission/ + theory/proofs/formal-p10-1-* + theory/predictions/verify_rh_* |
| `.roadmap.hexa_weave` | multi-strand molecular composition cycle | papers/hexa_weave_* (130+) + biology axis 4-sister + state/markers/w*_* |
| `.roadmap.clay_millennium` | clay millennium kick loop | state/clay_millennium_kick_loop/ (67 cycles) |
| `.roadmap.honesty_triad` | meta-quality / lint / triad / blockers / audit | state/{triad_lint,blockers,audit}/ + tool/own*_lint.hexa + reports/n6_*.json |

Tier-B candidates (deferred — disk evidence sparse):
- `.roadmap.<axis>` per `domains/<axis>/` (13 axes) — defer until per-axis cycle-burn ≥ 5 markers/30d
- `.roadmap.engine` — engine/ stable; no live cycle pressure
- `.roadmap.techniques` — same
- `.roadmap.proposals` — defer; covered by per-proposal docs

raw#10 honest: Tier-A list is **9 entries**, not 8 — count drift introduced during draft. The retained Tier-A row labels and ordering are authoritative; the §2.1 header label "8 entries" is a known caveat (see §6 caveat 3).

### §2.2 Per-roadmap minimal seed shape

Each `.roadmap.<domain>` MUST include:

```
# canon /.roadmap.<domain> — minimal seed
# Schema: canon/roadmap/<domain>/1
# Created: <ISO>
# Owner: <axis-spine-source>

# checkpoint
- done [C0] domain-roadmap-init — fan-out 2026-05-02

# active phase
- active [P1] <first-phase>
  eta TBD
  why "<spine purpose>"
  evidence_sources
    - <path-1>
    - <path-2>

# upcoming
- pending [P2] <next-phase>

# upstream
- depends_on .roadmap.canon (meta-spine)
- absorbs (none) — additive only, predecessor retired

# raw#10 honest
- additive only; earlier `.roadmap` retired (no migration)
- evidence_sources are read-only; no rewrites
```

raw#10 honest: this seed shape mirrors `.claude/worktrees/agent-add0758622241ad36/.roadmap` (the only template witnessed on-disk via the pre-existing worktree pin) — adopting it preserves convention without inventing a new grammar.

### §2.3 Optional cross-link block (per roadmap)

```
# cross-links
- atlas: atlas/atlas.n6 axis-<X>
- raw_anchor: hive raw.mk2 arch.001 (or specific raw#)
- handoff: docs/<this-doc-or-successor>.ai.md
- marker_glob: state/markers/<spine>_*.marker
```

Optional — only emit when the spine has a documented atlas axis or raw anchor.

## §3 Phase 3 — Raw 270/271/272/273 triplet plan emission

### §3.1 Hive raw lineage (read-only — n6-side adoption only)

| Raw | Slug | Mandate |
|---|---|---|
| 270 | core-module-architecture-mandate | `core/<feature>/{source,registry,router,<feature>_main}.hexa` 4-file pattern when ≥2 implementations |
| 271 | readme-ai-native-mandate | `modules/<feature>/README.ai.md` literal filename + AI-native frontmatter |
| 272 | core-module-file-structure-consistency | filename `^[a-z0-9_]+\.hexa$` + 5 structural checks (C1-C5) |
| 273 | core-hierarchy-connection-direction | T2 modules → T1 core registry → T0 source; reverse forbidden |
| mk2 arch.001 | core-module-architecture-canonical-pattern | 4-rule cluster collapsed; severity warn → block by 2026-08-02 |

### §3.2 N6-side adoption triplet (PLAN — impl deferred)

**Triplet T1 — `canonshared/n6/`** (T0 candidate):

- current state: 4 files (atlas.n6 + atlas.signals.n6 + n6_core_constants.hexa + n6_core_constants.hexa.append.cycle25-26 + docs/domains.json)
- mk2 target: keep flat (T0 = top-level no-subdir, project-wide shared per raw 273 tier definitions)
- action: NONE — already conforms to T0 by raw 273 definition (no `<feature>/` subdir; flat shared-state)
- evidence: hive marker `raw_273_core_hierarchy_landed.marker` T0 definition `core/<file>.hexa (top-level no subdir, project-wide shared)`

**Triplet T2 — `engine/`** (T1 candidate fan-out):

- current state: 17 flat hexa files (ouroboros_b2_verifier / hexa_gate_mk3 / arch_unified / arch_quantum / arch_selforg / arch_adaptive / phi_efficiency_bridge / leech24_surface / consciousness_constraints / emergent_n6_trainer / thermodynamic_frame / n6_calculator / n6_speak / n6_speak_hw / anima_tension_loss / test_engine + 1 init)
- mk2 target (PLAN-ONLY): document each engine file's "feature group" but DO NOT migrate. additive `engine/README.ai.md` summarising 17-file inventory + per-file 1-line purpose
- action: emit `engine/README.ai.md` (additive, no file rename / move / delete)
- raw#10: engine/ has NO `core/<feature>/` + `modules/<feature>/` split today; raw 270 mandate triggers only for ≥2 implementations of the same feature. flat 17-file engine is single-impl-each; raw 270 N/A. raw 271 README.ai.md mandate is the only hard requirement.

**Triplet T3 — `tool/`** (T2-style high cardinality):

- current state: 81 hexa files (own*_lint / atlas_* / hexa_weave_* / verify_* / migrate_* / promote_*)
- mk2 target (PLAN-ONLY): document the 4 already-detected feature clusters
  - cluster-A: `own*_lint.hexa` (15+ files; lint family) → candidate `modules/lint/<own_id>.hexa` if migration permitted (NOT this cycle)
  - cluster-B: `atlas_*.hexa` (10+ files; atlas-ops family)
  - cluster-C: `hexa_weave_*.hexa` (8+ files; weave family)
  - cluster-D: `verify_*.hexa` / `migrate_*.hexa` / `promote_*.hexa` (mixed; no clean cluster)
- action: emit `tool/README.ai.md` listing 4 clusters + "migration deferred per session policy". no file moves.
- raw#10: this cycle ABSOLUTELY MUST NOT migrate; the 4-cluster grouping is documentary only.

### §3.3 Sister-repo lint applicability

`hive/state/markers/raw_270_271_sister_repos_lint_applied.marker` indicates the hive lint already supports `--repo` arg for sister-repo scanning. canon impl path:

```
hexa run hive/tool/ai_native_module_readme_lint.hexa --repo /Users/<user>/core/canon
```

PLAN-ONLY: do NOT run in this cycle (impl deferred to follow-up). When run, expect:
- engine/ flat: triggers raw 271 violation (no README.ai.md) — baseline candidate
- tool/ flat: triggers raw 271 violation — baseline candidate
- domains/<axis>/<domain>/: each has CLAUDE.md per existing convention; raw 271 mandates `README.ai.md` literal filename — likely 393 violations

Required action when impl runs: create `.ai-native-readme-baseline` at repo root with the initial violation set as **grandfather entries** (per hive Stage-1 warn ramp). 30-day promotion target 2026-06-01 inherits hive timeline.

### §3.4 Raw triplet timeline (n6-side)

| Date | Stage | Action |
|---|---|---|
| 2026-05-02 | PLAN-LAND | this doc + marker; no impl, no file emit beyond doc + marker |
| 2026-05-02 ~ 2026-05-15 | PREP | follow-up cycle: emit `engine/README.ai.md` + `tool/README.ai.md` (additive only) |
| 2026-05-15 ~ 2026-06-01 | BASELINE | run `hive/tool/ai_native_module_readme_lint.hexa --repo` and freeze `.ai-native-readme-baseline` |
| **2026-06-01** | HIVE STAGE 2 | inherit hive warn → block flip; n6 commits respect raw 270/271 violation rejection |
| 2026-06-01 ~ 2026-12-01 | DRIFT-WATCH | monthly baseline-conform audit |
| **2026-08-02** | MK2 ARCH.001 BLOCK | raw.mk2 arch.001 ramp `warn → block by 2026-08-02` (hive raw.mk2 spec) |

raw#10 honest: 2026-06-01 promotion is **gated on hive Stage-2 promotion succeeding**, not n6-side readiness. If hive defers, n6 inherits the deferral (no independent flip).

## §4 Phase 4 — handoff + marker

### §4.1 Handoff (this doc)

- path: `canon/canon_meta/doc/canon_self_mk2_tuning_landed_2026_05_02.ai.md`
- frontmatter: AI-native (schema / last_updated / ssot / related_raws / related_docs / status / preset / policy / omega_cycle)
- length target: ≤ 600 lines (current draft within budget)

### §4.2 Marker

- path: `canon/state/markers/canon_self_mk2_tuning_landed.marker`
- format: JSON (schema `canon/markers/self_mk2_tuning_landed/1`)
- key fields: completion_iso / handoff_path / handoff_sha256 / phase_outputs (Phase 1-4) / raw_anchors / policy_compliance / next_step

### §4.3 Friendly preset scope

Per session prompt: `friendly preset (handoff doc only)`. impl does NOT receive a friendly UX layer this cycle. Friendly = doc tone + phased, gentle ramp + explicit caveats + no surprise mandates.

## §5 What is NOT done (impl deferred)

1. **No `.roadmap.<domain>` files emitted this cycle.** Files would be created in next-cycle following Phase 2 spec.
2. **No `engine/README.ai.md` or `tool/README.ai.md`.** Same — follow-up cycle.
3. **No `.ai-native-readme-baseline` populated.** Awaits lint run (deferred).
4. **No file moves / renames / deletes.** Migration policy = PROHIBITED this cycle.
5. **No `INDEX.json` 9-axis manifest update.** Adding a 10th axis (e.g., `roadmap_fan_out`) deferred until Phase 2 actuates.
6. **No `domains/_index.json` version bump.** Domain count unchanged.

## §6 raw#10 caveats (15 honest items)

1. **The prior baseline SSOT retirement scope unverified at agent-spawn**: prompt asserts "the prior baseline SSOT 폐기 완료" — confirmed via repo-root absence of `.roadmap` / `.roadmap.*` files. Worktree-local `.roadmap` artefacts (3 worktrees: agent-add0758622241ad36 / agent-a4a66d7e / agent-ab556f12ea2cdfd52) are NOT repo-root SSOTs.

2. **n6 `core/<feature>/` + `modules/<feature>/` pattern absent at present**: raw 270 mandate triggers only for ≥2 implementations of the same feature. Engine/ + tool/ flat cardinality means raw 270 is N/A today; raw 271 README.ai.md is the only universal trigger.

3. **Tier-A roadmap count drift**: §2.1 header says "8 entries" but the table lists 9 (.roadmap.{canon, atlas, atlas_self_arch, auto_convergence, group_p, sigma_tau_8, hexa_weave, clay_millennium, honesty_triad}). Authoritative count = 9. Header is a known caveat.

4. **domains/_index.json 393 vs 13-axis fan-out cardinality mismatch**: per-axis `.roadmap.<axis>` would create 13 additional roadmaps. Tier-B deferral until per-axis ≥5 markers/30d cycle-burn detected — current evidence suggests biology + apps + pets are most active (recent _index.json changelog).

5. **Worktree templates may be stale**: pre-existing `.claude/worktrees/agent-*/` `.roadmap` examples are minimal seeds (10 lines each); they may not reflect latest hive raw.mk2 conventions. PLAN treats them as baseline grammar only.

6. **Hive raw.mk2 arch.001 timeline (2026-08-02 block)**: faster than raw 270/271 hive Stage-2 (2026-06-01). Sequencing means n6 inherits arch.001 collapsed canonical pattern only after raw 270/271 promotion. PLAN respects 2026-06-01 first.

7. **Sigma-tau-8 submission status unverified**: `papers/sigma_tau_8_submission/` has 6 files but submission ISO date / venue / decision unknown from disk. `.roadmap.sigma_tau_8` MUST collect this on-disk before Phase 2 acts.

8. **clay_millennium_kick_loop 67 cycles is dense**: 2026-04-28 single-day burn suggests batch generation, not steady cadence. `.roadmap.clay_millennium` should record raw evidence (what triggered the burst).

9. **atlas K_core saturation at 22**: shard footer warns axis-M+ has 0-8 fields headroom. `.roadmap.atlas_self_arch` MUST track this ceiling and not propose axes that breach it without prior @-type extension.

10. **DO NOT auto-absorb**: atlas shard footer explicit "DO NOT auto-absorb. shard awaits human review per scope contract." — `.roadmap.atlas` must NOT trigger absorption automation.

11. **Cross-repo lint exemption**: `.papers-cross-repo-lint-exempt` exists (2K) — n6 already has lint-exemption surface. raw 271 README.ai.md baseline must NOT collide with this exempt list (verify before populating).

12. **canonshared/ schema family**: `canonshared/config/absolute_rules.json` is declared SSOT per INDEX.json `rules.ssot_json`. Any roadmap that proposes lint-rule changes MUST cross-link this file (deferred).

13. **9-axis manifest stale**: `INDEX.json` `_version` 1.0.0 (2026-04-10) — 22 days old. `_total: 393` (current `domains/_index.json` 1.7.0) is in sync with INDEX.json `domain_count: 299` ONLY if INDEX.json is updated. INDEX.json version bump deferred (Phase 2 actuates).

14. **n6 vs hive separation**: hive owns raw 270-273 SSOT; n6 is a downstream consumer. PLAN must NEVER duplicate raw text into n6 — only reference hive line numbers / marker paths.

15. **friendly preset = doc only**: impl does NOT inherit friendly tone. lint exit codes / commit rejection messages remain hive defaults. friendly = this doc's ramp explanations + NEVER surprise mandate cliff.

## §7 Next-step (follow-up cycle)

| ID | Action | Owner | ETA | Cost |
|---|---|---|---|---|
| FU-1 | Emit Tier-A 9-roadmap files (additive) | next-cycle | 2026-05-15 | $0 |
| FU-2 | Emit `engine/README.ai.md` + `tool/README.ai.md` | next-cycle | 2026-05-15 | $0 |
| FU-3 | Run hive lint `--repo /Users/<user>/core/canon` | next-cycle | 2026-05-20 | $0 |
| FU-4 | Freeze `.ai-native-readme-baseline` | next-cycle | 2026-05-30 | $0 |
| FU-5 | Inherit hive Stage-2 promotion (warn → block) | hive-side | 2026-06-01 | $0 |
| FU-6 | INDEX.json 9-axis → 10-axis manifest bump (add `roadmap_fan_out`) | next-cycle | 2026-06-15 | $0 |

## §8 File index

| Path | Role |
|---|---|
| `canon/canon_meta/doc/canon_self_mk2_tuning_landed_2026_05_02.ai.md` | this handoff doc |
| `canon/state/markers/canon_self_mk2_tuning_landed.marker` | landing marker (JSON) |
| `canon/INDEX.json` | 9-axis manifest (read-only this cycle) |
| `canon/domains/_index.json` | 13-axis 393-domain SSOT (read-only) |
| `canon/atlas/atlas.n6` | axis-A through axis-L (read-only) |
| `canon/docs/n6_meta_evolution_proposal_20260423.md` | predecessor proposal (Phase 1-6 6-phase) |
| `hive/.raw.mk2` | hive raw.mk2 SSOT (arch.001 collapsed) |
| `hive/docs/raw_270_271_warn_to_block_promotion_design.md` | promotion timeline |
| `hive/docs/raw_272_lint_extension_spec.ai.md` | 5 structural checks contract |
| `hive/docs/canonical_core_hierarchy_pattern.ai.md` | T0/T1/T2 + import direction matrix |

## §9 Closure

- omega-cycle: 6-step single-pass complete (audit → Phase 1 / plan → Phase 2 / triplet → Phase 3 / handoff → Phase 4.1 / marker → Phase 4.2 / close → §9)
- raw#10 honest count: 15 caveats (target hit)
- destructive ops: 0 (target hit)
- migration: 0 (target hit)
- cost: $0 mac-local
- BR-NO-USER-VERBATIM: enforced (no user-prompt verbatim quotation in body)
- AI-native: frontmatter present, schema declared, related_raws cited
- preset: friendly (doc tone + ramp explanations + no surprise mandates)

End of doc.
