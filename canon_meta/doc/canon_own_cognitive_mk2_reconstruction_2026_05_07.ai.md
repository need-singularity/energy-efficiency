---
schema: canon/docs/own_cognitive_mk2_reconstruction/ai-native/1
last_updated: 2026-05-07
ssot:
  rule_file: .own.cognitive
  predecessor_handoff: canon_meta/doc/canon_own_readme_mk2_reconstruction_2026_05_04.ai.md
  sibling_handoffs:
    - canon_meta/doc/canon_own_readme_mk2_reconstruction_2026_05_04.ai.md (.own.readme)
    - canon_meta/doc/canon_own_group_p_mk2_reconstruction_2026_05_03.ai.md (.own.group_p)
  retired_mk1_own: confirmed (mk1 .own 881L + 35 rules deleted at commit 442afa7b 2026-05-03)
  mk1_recovery_blob: git show 442afa7b^:.own (881 LoC, source-of-truth for mk1 own#32 reconstruction)
related_raws:
  - raw 0 (root-ssot — .raw + .own + .guide triad)
  - raw 91 (honest-c3-disclosure — process-quality + honest C1-C5)
  - raw 95 (triad-mandate — hive-agent + cli-lint + advisory tri-layer)
related_docs:
  - canon_meta/doc/canon_own_group_p_mk2_reconstruction_2026_05_03.ai.md (sibling — paper-md governance + .own.group_p own#6 collapsing precedent mirrored here)
  - canon_meta/doc/canon_own_readme_mk2_reconstruction_2026_05_04.ai.md (sibling — README governance)
  - canonshared/config/absolute_rules.json (durable SSOT; predates `.own` reconstruction)
status: PLAN-LANDED (.own.cognitive emitted; FU-1/FU-2/FU-3 deferred — see §5)
preset: friendly (handoff doc + minimal rule emit; lint coverage gap deferred)
policy:
  migration: PROHIBITED (additive only; no rename / no move / no delete)
  destructive_ops: 0
  user_verbatim_ban: enforced (BR-NO-USER-VERBATIM)
  hive_resource_only: enforced (own#35 mandate; no host python3 detection)
  raw_count_target: minimal
  cap: 30min
  cost: $0 mac-local
omega_cycle: 6-step single-pass (audit -> plan -> emit -> handoff -> marker -> close)
---

# canon .own.cognitive mk2 reconstruction — landed plan (2026-05-07)

> **TL;DR for the implementer**
>
> mk1 `.own` (881 LoC, 35 rules) was deleted at commit 442afa7b on 2026-05-03 as part of mk2 plan-land. Sibling cycles already restored README governance (`.own.readme`, 5 rules, 2026-05-04) and paper-md governance (`.own.group_p`, 1 unified rule, 2026-05-03). This cycle restores **cross-domain cognitive / design / framing governance** as a unified mk2 rule (`own 32 n6-no-fixation-design-and-count` in `.own.cognitive`), absorbing mk1 own#32 (`physical-limit-alternative-framing`, 2026-05-01 design-constant scope) + 2026-05-07 user directive ("n=6 집착금지 / 6개를 한계로 두는 케이스가 너무 많아") into one canonical rule mirroring `.own.group_p` own#6 (mk1 own#6 + mk1 own#15 collapsing) precedent + hive raw.mk2 arch.001 4-rule-cluster→1-canonical-pattern. **This cycle ships Phase 1 + Phase 5 only**: declarative `.own.cognitive` emit (146 LoC) + handoff + marker. Phase 2 (lint extension to enumeration cap-fixation grep heuristic), Phase 3 (audit baseline measurement of existing 6-cap incidents), Phase 4 (witness ledger bootstrap) deferred to follow-up cycle.

## §1 Phase 0 — Deep-research audit findings (2026-05-07)

### §1.1 mk1 own#32 lineage

- mk1 own#32 promoted 2026-05-01 commit `f138c9c7` "feat(.own own#32): physical-limit-alternative-framing — n=6 force-fit no longer mandatory for domain design constants"
- Original directive (Korean preserved): "own 에 반영 => n=6 집착 할필요없음 / 한계가 있으면 안됨 / n=6 force-fit 제거"
- Inaugural live counter-example: `domains/pets/cat-litter/cat-litter.md` §7 VERIFY Blocks A-G (commit 5fd6825e) — own#2 master-identity Block A + 6 physical-limit Blocks B-F + 6-precursor Block G; alien-grade 10
- mk1 own#32 body retrieved from `git show 442afa7b^:.own` (881 LoC blob) — 60 LoC rule entry; full content preserved verbatim in mk2 absorption per BR-NO-USER-VERBATIM

### §1.2 2026-05-07 user directive (current cycle trigger)

- Korean preserved (turn 1-3): "own 등록 => n=6 집착금지 / 더 나은게 발견될 수 있는데 / 6개를 한계로 두는 케이스가 너무 많아"
- Korean preserved (turn 4): "피드백 말고 .own 등록"
- Korean preserved (turn 5): "hive mk2 기준 .own"
- Korean preserved (turn 6-7): "합병" + "mk2 own 으로 흡수 합병"
- Resolved scope: design-constant force-fit ban (mk1 own#32) + enumeration count-cap fixation ban (2026-05-07 extension) → single unified rule

### §1.3 mk2 own state pre-cycle

| File | Scope | Rules | Status |
|---|---|---|---|
| `.own.readme` | README.md governance | own#14 / #17 / #20 / #21 / #29 (P0) | live (2026-05-04) |
| `.own.group_p` | papers/*.md governance | own#6 (mk2 unified, absorbs mk1 #6+#15) | live (2026-05-03) |
| `.own.cognitive` | cross-domain cognitive/framing | (this cycle: own#32 mk2 unified) | EMIT THIS CYCLE |

### §1.4 mk1 own count audit

mk1 `.own` 881L = 35 rules. mk2 reconstruction status post-this-cycle:
- Restored: own#6 (group_p) + own#14/17/20/21/29 (readme) + own#32 (cognitive) = **7 of 35** rules in mk2
- Implicit-restore via cross-link: own#1 / own#2 / own#13 / own#31 / own#33 / own#34 / own#35 (referenced as `cognitive-frameworks` from restored rules) = **7 additional**
- Unrestored: 21 rules — deferred to future scope-files (`.own.<scope>` per topic; no consolidation back to monolithic `.own`)

### §1.5 Hive raw alignment

- raw 0 (root-ssot) `.raw + .own + .guide` triad — `.own.cognitive` extends `.own` plurality, additive
- raw 91 (honest-c3-disclosure) — §6 caveats list applies
- raw 95 (triad-mandate) — own#32 mk2 unified declares hive-agent + cli-lint + advisory tri-layer

### §1.6 own#36 collapsing decision

- Initially drafted as separate own#36 (`n6-count-cap-no-fixation`) in turn 5-6
- User directive turn 7 ("합병") → collapsed into mk1 own#32 number, extended scope (design-constant + enumeration-count) — same invariant axis = "n=6 false ceiling 금지"
- User directive turn 8 ("mk2 own 으로 흡수 합병") + turn 9 (recommendation accepted = (b) keep `.own.cognitive` own#32 mk2 unified) → confirmed final form
- Pattern parity: `.own.group_p` own#6 (mk1 #6+#15 collapse) ↔ `.own.cognitive` own#32 (mk1 #32 + 2026-05-07 directive collapse)

## §2 Phase 1 — `.own.cognitive` emit (this cycle)

### §2.1 File metadata

- Path: `.own.cognitive`
- LoC: 146
- sha256: `ad4d87b139da757e8ca41c6e7510a38a92b167e7e99f3ee3199e2a1ba8d3845b`
- Frontmatter form: yaml in `#` comment block (DSL parser skips `#` lines, hive `.own` mk2 style)
- Schema: `project/own/v1` (hive-aligned); canon mk2 sibling files use `canon/own/<scope>/2` — divergence intentional per "hive mk2 기준" user directive turn 5
- Format: hive `.own` mk2 frontmatter (lighter than `.own.readme`/`.own.group_p` n6-local frontmatter) + raw-format body

### §2.2 own 32 mk2 unified rule body

- Rule slug: `n6-no-fixation-design-and-count`
- Status: `live`
- Since: `2026-05-01` (mk1 promotion preserved)
- Unified-at: `2026-05-07` (mk2 absorption of 2026-05-07 directive)
- Scope: HARD-OPT-IN (design-constant) + advisory (enumeration-count)
- bans-design-constant: 4 clauses (force-fit / rejection-without-own2 / precursor-cap / axis-restriction)
- bans-enumeration-count: 5 clauses (truncate-to-6 / pad-to-6 / hard-cap-without-domain-fact / default-N=6 / "n=6 이라서 6개" 정당화)
- exceptions: 4 clauses (own#2 master-identity block / theory n=6 subject / chip-* HARD scope / Atlas natural-mapping)
- cognitive-frameworks: own#2 / raw 91 / raw 117 / own#31 / own#13
- counter-examples: cat-litter / hexa-dream / hexa-ufo
- proofs: cat-litter §7 / commit 5fd6825e / `tool/own_doc_lint.hexa --rule 32` (forward-spec)
- measurement-axes: 6 (physical-limit-adoption-rate / precursor-inheritance-depth / own2-block-presence-rate / force-fit-incidence / cap-fixation-incidence / natural-n-adoption-rate)
- falsifiers: F-OWN32-1..6 (6th added for mk2 enumeration-count scope)
- enforce-layer tri: hive-agent + cli-lint + advisory (raw 95 compliant)
- follow-ups: 3 (witness ledger bootstrap / `--rule 32` lint extension / 6-cap baseline audit)

### §2.3 absorbs / collapses

| Source | Date | Status pre-cycle | mk2 absorption |
|---|---|---|---|
| mk1 own#32 `physical-limit-alternative-framing` | 2026-05-01 | retired (442afa7b 2026-05-03) | own#32 mk2 unified design-constant scope (Block A — bans-design-constant clauses) |
| 2026-05-07 user directive (count-cap fixation ban) | 2026-05-07 | new | own#32 mk2 unified enumeration-count scope (Block B — bans-enumeration-count clauses) |

Both absorbed under single canonical rule per `.own.group_p` own#6 collapsing precedent + hive raw.mk2 arch.001 pattern.

## §3 Phase 5 — handoff + marker (this cycle)

### §3.1 Handoff doc

- This file: `canon_meta/doc/canon_own_cognitive_mk2_reconstruction_2026_05_07.ai.md`
- AI-native frontmatter: 12 keys (schema / last_updated / ssot / related_raws / related_docs / status / preset / policy / omega_cycle)
- Sections: 9 (TL;DR + §1-§9)

### §3.2 Marker

- Path: `state/markers/canon_own_cognitive_mk2_reconstruction.marker`
- Schema: `canon/markers/own_cognitive_mk2_reconstruction/1`
- Format: JSON (sibling-aligned with `canon_own_readme_mk2_reconstruction.marker` + `canon_own_group_p_mk2_reconstruction.marker`)

## §4 Phase 5 commit

Target commit message:
```
feat(.own own#32 mk2 unified): n6-no-fixation-design-and-count — design-constant + enumeration-count force-fit ban 통합 (.own.cognitive 신설)
```

## §5 NOT done — explicit deferred follow-ups (per `.own.cognitive` own#32 follow-up clauses)

- **FU-1** witness ledger bootstrap — `reports/own32_physical_limit_framing.json` per raw 77 audit ledger schema (per-doc row: ts + doc_path + framing_kind + own2_block_present + precursor_count + precursor_axes + alien_index + cap_fixation_incidents). Deferred — schema-only definition in rule body sufficient for this cycle.
- **FU-2** lint extension — extend `tool/own_doc_lint.hexa` `--rule 32` subcommand: detect physical-limit framing declaration (heuristic: §7 contains Block A own#2 + Blocks B+ precursor citations) + verify own#2 block presence + grep heuristic for enumeration cap patterns (`max(:|=)\s*6\b` / `최대\s*6\b` / `6\s*cap\b` / `top(:|=)\s*6\b`). Deferred — lint surface design needed; advisory-layer 1차 게이트는 코드 리뷰 + 사용자 플래그.
- **FU-3** baseline audit — measure existing 6-cap incidents across Atlas constants registry / axis 정의 / slot 설계 / README enumeration / engine buffer cap / gradient norm / etc. Establish `cap-fixation-incidence` measurement-axis baseline. Deferred — quick survey performed in turn 6 (15-line grep result classified mostly EXEMPT under natural-mapping exceptions; full classification report deferred to next cycle).

## §6 raw 91 C3 honest disclosure

1. **Lint coverage gap (mk2 unified)**: `--rule 32` enforce path 는 mk1 forward-spec 그대로 — design-constant 영역 own#2 block presence check 만 actively wired in older lint code; mk2 enumeration-count grep heuristic 는 미구현. own#32 자체는 declarative SSOT 로 valid; runtime enforcement 는 FU-2 까지 advisory.
2. **Frontmatter divergence**: `.own.cognitive` 는 hive `.own` 형식 (`schema_version: project/own/v1` + `mk: 2`) 채택, sibling `.own.readme` / `.own.group_p` 의 n6-local 형식 (`schema: canon/own/<scope>/2` + ssot/policy nested keys) 와 다름. 사용자 directive turn 5 ("hive mk2 기준") 직접 결과. 향후 schema 정합성 follow-up 후보.
3. **mk1 own#32 enforcement**: mk1 own#32 자체의 lint enforcement (`tool/own_doc_lint.hexa --rule 32`) 가 mk1 retire 시점에 함께 dormant 되었는지 verify 안 됨. mk2 unified 에서 동일 path 재선언; 실제 wiring 상태는 FU-2 에서 검증.
4. **Audit grep heuristic 한계**: turn 6 의 quick grep (15 hits) 은 `(max[[:space:]:=]+6\b|최대[[:space:]]*6\b|cap[[:space:]:=]+6\b|6[[:space:]]*개[[:space:]]*한계|limit[[:space:]:=]+6\b|top[[:space:]:=]+6\b)` 패턴만 — 의미론적 force-fit (예: 도메인 요구치 무시하고 6에 맞춘 흔적) 탐지 불가. AST-level 또는 LLM-assist 분류 필요.
5. **collapsing decision reversibility**: own#32 mk2 unified 합병은 사용자 directive turn 7 ("합병") + turn 8 ("mk2 own 으로 흡수 합병") + turn 9 (recommendation (b) 수락) 로 확정. 향후 design-constant scope 와 enumeration-count scope 의 enforcement footprint 가 충돌하는 case 발견 시 separation 재검토 가능 (additive_only 정책 하에서는 own#32-A / own#32-B 변형 분기 또는 새 own 번호 생성).
6. **own#2 mk2 미복원**: own#2 (n6-master-identity) 본문이 mk2 어느 파일에도 등록되지 않음 — `.own.cognitive` own#32 본문이 own#2 를 cognitive-framework 로 cross-link 하므로 own#32 의 separable verify 의무는 명시되어 있으나, own#2 자체의 SSOT 는 mk1 retired 상태. Future cycle 에서 `.own.<core>` 또는 `.own.cognitive` 에 own#2 mk2 복원 필요.
7. **`.own.cognitive` 단일 rule 운영**: 현재 1 rule 만 (own#32). future cognitive/framing 룰 (예: own#2 mk2 복원) 추가 시 동일 파일에 누적; scope_drift_ban 정책 유지.
8. **Atlas EXACT 자연 매핑 면제 의미**: own#32 mk2 의 Atlas 면제 절은 σ(6)=12 / J₂=24 / 144 등 자연 일치를 허용하나, "자연" 의 판정 기준은 advisory — 사용자 플래그 의존. AST-level 의 force-fit detector 도입 전까지 코드 리뷰 1차.

## §7 Next-step pointer

- FU-1/FU-2/FU-3 follow-up cycle planned ETA `2026-05-21` (2주 후) — quick scope, witness ledger + lint extension + baseline audit 배치 처리
- own#2 mk2 복원 cycle 별도 — `.own.cognitive` own#2 추가 또는 신규 `.own.core` scope file 결정 후
- mk1 35-rule audit cycle — 미복원 21 rule 의 mk2 reconstruction priority 매트릭스 작성 (P0/P1/P2 분류)

## §8 File index

| Path | Role | Cycle action |
|---|---|---|
| `.own.cognitive` | mk2 own SSOT (cognitive/framing scope) | NEW (146 LoC, sha256 ad4d87b1) |
| `canon_meta/doc/canon_own_cognitive_mk2_reconstruction_2026_05_07.ai.md` | this handoff | NEW |
| `state/markers/canon_own_cognitive_mk2_reconstruction.marker` | omega_cycle close marker | NEW |
| `.own.readme` | sibling mk2 SSOT (README scope) | unchanged |
| `.own.group_p` | sibling mk2 SSOT (paper-md scope) | unchanged |
| `canonshared/config/absolute_rules.json` | durable SSOT | unchanged |

## §9 Closure

omega_cycle 6-step single-pass complete:
1. **audit** — §1 (mk1 own#32 lineage + 2026-05-07 directive + mk2 own state + collapsing decision)
2. **plan** — turn 4-9 user dialogue + recommendation (b) acceptance
3. **emit** — `.own.cognitive` 146 LoC own#32 mk2 unified
4. **handoff** — this doc
5. **marker** — `state/markers/canon_own_cognitive_mk2_reconstruction.marker`
6. **close** — commit + push (this cycle final action)

cycle CLOSED 2026-05-07.
