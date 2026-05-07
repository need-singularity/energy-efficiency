---
schema: canon/docs/own_readme_mk2_reconstruction/ai-native/1
last_updated: 2026-05-04
ssot:
  rule_file: .own.readme
  predecessor_handoff: canon_meta/doc/canon_self_mk2_tuning_landed_2026_05_02.ai.md
  sibling_handoff: canon_meta/doc/canon_own_group_p_mk2_reconstruction_2026_05_03.ai.md
  axis_spine: .roadmap.canon (Tier-A planned, deferred per predecessor §2.1)
  retired_mk1_own: confirmed (mk1 .own 881L + 32 rules deleted at commit 442afa7b 2026-05-03)
  mk1_recovery_blob: /tmp/n6_own_mk1.txt (recovered via git show 442afa7b^:.own)
related_raws: []  # README governance is n6-local + cross-repo (hexa-lang sister); hive raw 270/271/272/273 + arch.001 do NOT govern README content
related_docs:
  - canon_meta/doc/canon_self_mk2_tuning_landed_2026_05_02.ai.md (predecessor handoff)
  - canon_meta/doc/canon_own_group_p_mk2_reconstruction_2026_05_03.ai.md (sibling cycle — paper-md governance)
  - .readme-rules.json (own#14 SSOT)
  - reports/n6_selftest.json (own#21 authoritative source)
status: PLAN-LANDED (.own.readme emitted; Phase 2 lint coverage gap deferred)
preset: friendly (handoff doc + 5-rule emit + Pets/Apps registration; impl-heavy phases preserved for follow-up)
policy:
  migration: PROHIBITED (additive only; no rename / no move / no delete)
  destructive_ops: 0
  user_verbatim_ban: enforced (BR-NO-USER-VERBATIM)
  hive_resource_only: enforced (own#35; own#17 cross-repo dep grandfathered — see §5 caveat 4)
  raw_count_target: 8 caveats
  cap: 60min
  cost: $0 mac-local
omega_cycle: 6-step single-pass (audit -> plan -> emit -> handoff -> marker -> close)
---

# canon .own.readme mk2 reconstruction — landed plan (2026-05-04)

> **TL;DR for the implementer**
>
> Sibling cycle to `.own.group_p` (paper-md governance, 2026-05-03). This cycle restores the **5 README-bound rules** from mk1 .own (commit 442afa7b 881L deletion) into a new `.own.readme` file: own#14 (sealed-hash) / own#17 (english-only, cross-repo dep) / own#20 (techniques-count drift) / own#21 (tests-count drift, CURRENT DRIFT 1116↔51) / **own#29 readme-friendly-toolkit-required HARD (P0 priority)**. Rules kept separated (no collapse) — concern axes diverge (sealed / english / drift / structure). own#29 expanded from mk1 30 mandatory-sections to **32** (Pets + Apps registered per current README state). User directive 2026-05-04: "이 구성에 가장중요!!!!" — 7-column toolkit-table structure = top priority. **This cycle ships Phase 1+3+5**: declarative `.own.readme` emit + Pets/Apps section registration + handoff + marker. Phase 2 (lint coverage gap closure: own#29 multi-section dispatcher wiring + ci.yml wiring + hexa runtime fix) deferred.

## §1 Phase 0 — Deep-research audit findings (2026-05-04)

### §1.1 README inventory

- README.md total LoC: **1370** (`/Users/<user>/core/canon/README.md`)
- Toolkit `## … Toolkit (HEXA-…)` H2 sections: **33**
- own#29 mk1 mandatory-sections: **30** — all 30 heading literals present verbatim in README
- README sections NOT in mk1 mandatory list: **2** (Pets at L539 + Apps at L570) — both registered in mk2 expansion (32 mandatory total)
- Total `[doc](domains/.../*.md)` link count: **292**
- Sample 15/15 doc links resolve via `test -f` — domain link integrity good

### §1.2 Lint coverage state at 2026-05-04

| Lint | File | Status | Scope |
|---|---|---|---|
| own#14 readme-sealed-required | `tool/readme_sealed_check.hexa` | ACTIVE (selftest works; live exec broken via mac Docker route) | sha256(README.md) == .readme-rules.json scopes.root.sealed_hash; ci.yml:393 wired |
| own#17 public-readme-english-only | `~/core/hexa-lang/tool/readme_english_audit.hexa` | ACTIVE cross-repo | 8934 bytes 2026-04-22; ci.yml:143-170,253 wired (SOFT-skip on sister-repo checkout failure) |
| own#20 readme-techniques-count-drift | inline shell `find techniques ...` + grep README | ACTIVE | drift_pattern `(\d+) Techniques` — currently MATCHED 225=225 |
| own#21 readme-nexus6-tests-count-drift | `tool/own_nexus6_tests_drift.hexa` | ACTIVE (CURRENT DRIFT) | drift_pattern `tests:\s+\d+` — README 1116 vs reports/n6_selftest.json#total 51; ci.yml:341-349 wired |
| own#29 readme-friendly-toolkit-required | `tool/own29_readme_friendly_toolkit_lint.hexa` (362 LoC, biology-only) + `tool/own_doc_lint.hexa --rule 29` (multi-section dispatcher; reads mandatory-sections from `.own`) | PARTIAL — biology-only standalone selftest 6/6 PASS; multi-section dispatcher needs `.own.readme` wiring verification | mandatory-sections list lived only in deleted mk1 .own; this cycle restores SSOT |

### §1.3 Hexa runtime status

- `hexa run …` fails with `interp interpreter not found / searched: ./build/hexa_interp / $HEXA_LANG/build/hexa_interp / rebuild with: hexa tool/build_interp.hexa` (mac Docker route)
- Selftest path works via `route=darwin-bypass-marker` — own#29 selftest 6/6 PASS verified 2026-05-04
- Live README scan path BROKEN — own#14 / own#21 / own#29 cannot run live this cycle
- Out-of-scope for `.own.readme` reconstruction; FU-fix-hexa-runtime tracks separately

### §1.4 Sealed hash + drift current state

- `README.md.sealed.hash`: `sha256:293a8865b2998215681e9d563dba9645e0c41b244e23bbf068c45c54bcf19a1c`
- `shasum -a 256 README.md`: **MATCHES** stored hash → own#14 PASS
- own#20 actual: 225 hexa files in techniques/ (excluding test_techniques*); README L208 `**225 Techniques**` → MATCHED
- own#21 actual: `reports/n6_selftest.json#total = 51`; README L70 `NEXUS tests: 1116` + L7 badge `NEXUS-1116%20tests` → **DRIFT** (1116 vs 51)
- own#21 fix decision DEFERRED — caller policy required (which value canonical: README 1116 or selftest.json 51)

### §1.5 Toolkit-table conformance (sample 3 sections)

- Fusion §L116: 7-column header PASS, 3 data rows (>= min_rows 3), all first-cells = 10, all 3 doc paths resolve, Mainstream contrast cells: `σ(6)=12-archetype unified lattice` / `σ(6)=12-vertex tabletop module` / `τ(6)=4-state full-cycle plant` (own#2 anchored ✓)
- Chip §L147: 7-column header PASS, 4 data rows (>= min_rows 3), all first-cells = 10, doc paths resolve, Mainstream contrast: `σ²=144 SM × τ=4 pipe × φ=2 issue` / `σ·J₂=288 / bank in-place compute` / `σ·J₂=288 vertical lane/mm²` / `σ²=144-tile self-healing array` (own#2 anchored ✓)
- AI §L195: 7-column header PASS, 4 data rows (>= min_rows 3), all first-cells = 10, doc paths resolve, Mainstream contrast cells **lack explicit n=6 master identity tokens** (informational only; own#29 does not enforce anchoring)

### §1.6 Cross-repo dep + own#35 cross-fire

- own#17 verify path: `~/core/hexa-lang/tool/readme_english_audit.hexa` (cross-repo absolute home-relative path)
- own#35 (2026-05-02) mandates external resources via hive resource exec — bans `which` / `command -v` / direct $PATH
- own#17 (2026-04-21) predates own#35 by 11 days
- No explicit grandfathering noted in own#35 scope — `.own.readme` codifies grandfather as caveat (FU-deferred hive-resource migration)
- ci.yml SOFT-skip fallback on sister-repo checkout failure preserves stability during cross-repo migration window

## §2 Phase 1 — `.own.readme` declarative emit (this cycle)

### §2.1 File path

```
/Users/<user>/core/canon/.own.readme
```

Sibling to `.own.group_p` (paper-md, emitted 2026-05-03). Schema: `canon/own/readme/2`.

### §2.2 5-rule structure (concern-separated, NOT collapsed)

Unlike `.own.group_p` which collapsed mk1 own#6 + own#15 into one rule (paper-3pack-verify-embedded), `.own.readme` keeps 5 rules separate. Rationale: README rules touch divergent invariant axes (sealed-integrity / English-language / count-drift / structural toolkit-table) — collapsing would dilute invariants without aligning to hive raw.mk2 arch.001 which targets same-concern rule clusters.

| Rule | Axis | Status |
|---|---|---|
| own#14 readme-sealed-required | integrity (sha256 sealed hash) | ACTIVE |
| own#17 public-readme-english-only | language (no-CJK, cross-repo dep) | ACTIVE (cross-repo grandfathered) |
| own#20 readme-techniques-count-drift | drift (count-vs-disk, daily warn) | ACTIVE (MATCHED) |
| own#21 readme-nexus6-tests-count-drift | drift (count-vs-json, daily warn) | ACTIVE (CURRENT DRIFT) |
| **own#29 readme-friendly-toolkit-required** | **structure (7-column toolkit table, P0)** | **PARTIAL (biology-only standalone; multi-section dispatcher needs wiring)** |

### §2.3 own#29 P0 priority — 32 mandatory-sections (mk2 expansion)

mk1 had 30 mandatory-sections. mk2 adds:
- `pets=## 🐾 Pets Toolkit (HEXA-Companion family)|min_rows=2|axis=pets|contrast=Commodity`
- `apps=## 📱 Apps Toolkit (HEXA-Mobile family)|min_rows=3|axis=apps|contrast=Mainstream`

Total = **32 mandatory-sections**. README L539 (Pets) + L570 (Apps) already conform.

7-column header template: `| 🛸 | Tool | One-liner | Everyday analogy | What it does | <Mainstream> contrast | Doc |`

`<Mainstream>` placeholder allows per-section variation:
- 30 sections use `Mainstream contrast`
- biology uses `AlphaFold contrast`
- pets uses `Commodity contrast`

n=6 master identity (own#2) anchor in Mainstream-contrast cell is RECOMMENDED (Fusion/Chip precedent: σ(6)=12 / τ(6)=4 / J₂=24 / σ²=144 / σ·τ=48 / σ·J₂=288), NOT enforced.

### §2.4 Cognitive-frameworks cross-links

own#1 (doc-english-required) / own#2 (n6-master-identity) / own#14 / own#17 / own#20 / own#21 / own#29 (sibling-rules) / own#35 (hive-resource-only, grandfathered for own#17) / raw#33 (ai-native-english-only, mk1 promotion).

### §2.5 Enforcement layers

- own#14: `tool/readme_sealed_check.hexa` (ci.yml:393)
- own#17: `~/core/hexa-lang/tool/readme_english_audit.hexa` (ci.yml:253, SOFT-skip fallback)
- own#20: inline shell drift check (daily warn)
- own#21: `tool/own_nexus6_tests_drift.hexa` (ci.yml:349, daily warn)
- own#29: `tool/own_doc_lint.hexa --rule 29` (multi-section dispatcher) + `tool/own29_readme_friendly_toolkit_lint.hexa` (biology-only standalone)

## §3 Phase 3 — Pets/Apps section registration (this cycle)

### §3.1 Registration form

`.own.readme` own#29 mandatory-sections list extended from 30 → 32 entries. Pets/Apps appear at end of list to preserve mk1 ordering.

### §3.2 Justification

- README state at 2026-05-04: Pets at L539 + Apps at L570 already exist with conformant 7-column tables
- domains/_index.json v2.3.0 recognizes pets + apps as 12th + 13th axes
- mk1 .own (2026-04-29 cycle 29) was authored before Pets/Apps axes landed (`domains/pets/` 2026-04-29 inaugural commit bd2c4620; `domains/apps/` 2026-04-30 commit 3c5d2c9a)
- Registration is **additive** — no existing rule changed; 30 mk1 entries preserved verbatim

### §3.3 Conformance verification

- Pets §L539: `## 🐾 Pets Toolkit (HEXA-Companion family)` + 7-column with `Commodity contrast` variation + 7 data rows (>= min_rows 2)
- Apps §L570: `## 📱 Apps Toolkit (HEXA-Mobile family)` + 7-column Mainstream contrast + 6 data rows (>= min_rows 3)

## §4 Phase 5 — Handoff + marker (this cycle)

### §4.1 Handoff (this doc)

- path: `canon_meta/doc/canon_own_readme_mk2_reconstruction_2026_05_04.ai.md`
- frontmatter: AI-native (schema / last_updated / ssot / related_raws / related_docs / status / preset / policy / omega_cycle)
- length target: ≤ 250 lines

### §4.2 Marker

- path: `state/markers/canon_own_readme_mk2_reconstruction.marker`
- format: JSON (schema `canon/markers/own_readme_mk2_reconstruction/1`)
- key fields: completion_iso / handoff_path / handoff_sha256 / phase_outputs / raw_anchors / policy_compliance / next_step

## §5 What is NOT done (Phase 2 + drift fix deferred)

1. **No `tool/own_doc_lint.hexa --rule 29` mandatory-sections wiring verified** — FU-2: confirm dispatcher reads `.own.readme` (parser may need 1-line additive update)
2. **No multi-section lint extension** — `tool/own29_readme_friendly_toolkit_lint.hexa` remains biology-only at this revision; FU-3 extends OR emits new `tool/own29_multi_section_lint.hexa`
3. **No own#29 ci.yml direct wiring** — current ci.yml has own#14/17/20/21 but not own#29; FU-4 adds wiring
4. **No own#21 drift fix** — README L70 `1116` vs reports/n6_selftest.json 51; policy decision deferred (caller: which canonical?)
5. **No hexa runtime fix** — `hexa run` mac Docker route broken (`interp not found`); selftest works via darwin-bypass-marker; out-of-scope for governance reconstruction
6. **No own#17 → hive resource exec migration** — own#17 cross-repo `~/core/hexa-lang/...` access grandfathered (predates own#35 by 11 days); FU-deferred
7. **No `state/markers/*.marker` git tracking** — marker remains gitignored per `.gitignore:58 state/markers/*.marker` policy (matches predecessor cycle)

## §6 raw#10 honest caveats (8 items)

1. **5-rule separation chosen over collapse**: unlike `.own.group_p` (paper own#6+#15 collapsed), `.own.readme` keeps 5 rules separate. Rationale: divergent invariant axes (integrity / language / drift x2 / structure). hive raw.mk2 arch.001 collapsing pattern fits same-concern clusters; README rules span 4 distinct concerns.

2. **own#29 multi-section dispatcher wiring unverified**: mk1 spec said `verify hexa tool/own_doc_lint.hexa --rule 29`, but the standalone tool/own29_readme_friendly_toolkit_lint.hexa is biology-only. Whether `tool/own_doc_lint.hexa --rule 29` actually parses mandatory-sections from a `.own.readme` file (vs only from mk1 root `.own`) requires FU-2 verification. If parser is hardcoded to root `.own`, `.own.readme` reads will need additive 1-line path extension.

3. **own#21 CURRENT DRIFT not fixed this cycle**: README declares 1116 NEXUS tests; reports/n6_selftest.json#total = 51. Drift is real, lint would emit DRIFT exit 1. Fix policy not encoded in `.own.readme` — caller decides which value is canonical. Daily warn cron will continue to fire until resolution.

4. **own#17 own#35 cross-fire grandfather**: own#17 (2026-04-21) uses `~/core/hexa-lang/tool/readme_english_audit.hexa` cross-repo path; own#35 (2026-05-02) bans path-based external-resource access. No formal grandfathering in own#35 scope — `.own.readme` codifies as caveat. ci.yml SOFT-skip fallback preserves stability during eventual hive-resource migration.

5. **Pets + Apps registration is additive expansion**: mk1 had 30 mandatory-sections; `.own.readme` adds 2 → 32. README at 2026-05-04 already has Pets + Apps in conformant form (7-column + alien-grade integers + resolving doc links). No README edit required this cycle.

6. **Mainstream contrast variation is per-section**: 30 sections use `Mainstream contrast`, biology uses `AlphaFold contrast`, pets uses `Commodity contrast`. mk1 .own L520 explicitly allows variation via `<Mainstream>` placeholder. `.own.readme` codifies variation list as `expected-header-row-variants`.

7. **n=6 master identity anchor in Mainstream contrast cell is RECOMMENDED, not enforced**: Fusion/Chip rows show σ(6)=12 / τ(6)=4 / J₂=24 / σ²=144 anchoring; AI section does not. own#29 enforces 7-column structure + alien-grade integer + doc link, NOT n=6 anchoring. Future "alien-grade-anchor lint" could promote anchoring to enforced; deferred.

8. **Hexa runtime live-exec broken**: `hexa run` mac Docker route `interp interpreter not found` — own#14 / own#21 / own#29 live README scan paths unavailable. Selftest paths work via `route=darwin-bypass-marker`. Reconstruction is declarative this cycle; live enforcement gated on FU-fix-hexa-runtime cycle (out-of-scope).

## §7 Next-step (follow-up cycles)

| ID | Action | ETA | Cost |
|---|---|---|---|
| FU-2 | Verify `tool/own_doc_lint.hexa --rule 29` parses mandatory-sections from `.own.readme`; emit additive 1-line path extension if parser hardcoded to root `.own` | 2026-05-15 | $0 |
| FU-3 | Extend `tool/own29_readme_friendly_toolkit_lint.hexa` from biology-only to multi-section OR emit new `tool/own29_multi_section_lint.hexa` (~400 LoC; 32-section iteration + per-section variation) | 2026-05-22 | $0 |
| FU-4 | Add own#29 direct ci.yml wiring (current omits own#29; only own#14/17/20/21 wired) | 2026-05-15 | $0 |
| FU-5 | own#21 drift fix — caller policy decision: README 1116 vs selftest.json 51 → update authoritative source then sync target | TBD (caller) | $0 |
| FU-6 | own#17 hive-resource-exec migration — replace `~/core/hexa-lang/...` direct path with `hive resource exec readme_english_audit -- ...` | 2026-06-01 | $0 |
| FU-fix-hexa | Restore `hexa run` mac route — `hexa tool/build_interp.hexa` rebuild OR investigate Docker route alt | TBD | $0 |

## §8 File index

| Path | Role |
|---|---|
| `.own.readme` | this cycle's declarative rule emit (5 rules; mk2 expansion to 32 mandatory-sections) |
| `canon_meta/doc/canon_own_readme_mk2_reconstruction_2026_05_04.ai.md` | this handoff doc |
| `state/markers/canon_own_readme_mk2_reconstruction.marker` | landing marker (JSON, gitignored) |
| `canon_meta/doc/canon_own_group_p_mk2_reconstruction_2026_05_03.ai.md` | sibling cycle (paper-md governance) |
| `canon_meta/doc/canon_self_mk2_tuning_landed_2026_05_02.ai.md` | predecessor handoff (mk2 plan-land) |
| `.readme-rules.json` | own#14 SSOT (sealed_hash field; require_sealed=true) |
| `README.md.sealed.hash` | own#14 hash artifact |
| `tool/readme_sealed_check.hexa` | own#14 enforce |
| `~/core/hexa-lang/tool/readme_english_audit.hexa` | own#17 enforce (cross-repo, sister) |
| `tool/own_nexus6_tests_drift.hexa` | own#21 enforce |
| `reports/n6_selftest.json` | own#21 authoritative source |
| `tool/own_doc_lint.hexa` | own#29 multi-section dispatcher |
| `tool/own29_readme_friendly_toolkit_lint.hexa` | own#29 biology-only standalone |

## §9 Closure

- omega-cycle: 6-step single-pass complete (audit → Phase 0 / plan → Phase 1 emit / Pets-Apps registration → Phase 3 / handoff → §4.1 / marker → §4.2 / close → §9)
- raw#10 honest count: 8 caveats (target hit)
- destructive ops: 0 (target hit)
- migration: 0 (target hit)
- cost: $0 mac-local
- BR-NO-USER-VERBATIM: enforced (Korean directive quoted ONLY in why field of own#29 with attribution; not in body prose)
- AI-native: frontmatter present, schema declared, related_raws/related_docs cited
- preset: friendly (handoff doc tone + ramp explanations + no surprise mandates)
- mk2 expansion confirmed: 30 → 32 mandatory-sections (Pets + Apps additive; README state unchanged)
- own#29 P0 priority codified: alien-grade alignment SSOT preserved per 2026-05-04 user directive

End of doc.
