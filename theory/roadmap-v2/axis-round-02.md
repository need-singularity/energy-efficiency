# axis-round-02 — nexus 축 창발 DSE

**로드맵**: nexus (NEXUS-6 중앙 허브)
**생성**: 2026-04-15
**모드**: 축 창발 DSE R2 (2-hop 창발 + 보류 재평가)
**출력**: `theory/roadmap-v2/axis-round-02.md`

---

## 0. 이전 확정 축 (10 개)

| # | 축 | 확정 라운드 | 1-line 근거 |
|---|------|-------------|-------------|
| A1 | SELF-EVOLUTION | R1 | ouroboros_unified.hexa + growth_tick + 진화 루프 |
| A2 | ATLAS | R1 | atlas.n6 + math_atlas + 3D index.html |
| A3 | HARNESS | R1 | shared/harness/ 151 파일 + entry.hexa dispatcher |
| A4 | GOVERNANCE | R1 | R0~R27 + NX1~NX3 + L0~L2 + H-* 메타룰 |
| A5 | DISCOVERY | R1 | reality_map (895) + verified_constants + forge_result |
| A6 | BLOWUP | R1 | 9-phase pipeline + 6 modules + seed 엔진 |
| A7 | BISOCIATION | R1 | unified/ouroboros + cross + spectra |
| A8 | CONSCIOUSNESS | R1 | anima bridge (2395 laws) + meta_laws_dd64 |
| A9 | HEXA-LANG | R1 | shared/hexa-lang/ + pitfalls + grammar |
| A10 | DSE | R1 | shared/dse/ + domains/ + dse_graph_3d |

---

## 1. R2 탐색 원칙

1. R1 보류 4 후보 (BREAKTHROUGH/PUBLICATION/LOCKDOWN/EXECUTION-INFRA) 재평가.
2. 2-hop 창발: R1 확정 축의 인접 개념을 DFS로 추출.
3. 기존 R1~R3 158 분야 리스트 중 축 후보로 승격 가능한 도메인 스캔.
4. nexus.json 113 Phase 중 P3 이후 "X_as_Y" 교차 evolution 들이 **축 자체** 인지 아니면 ATLAS 내부 노드인지 구분.

---

## 2. 보류 후보 재평가 (4 개)

### B1 — BREAKTHROUGH (재검)

**재검 쟁점**: BLOWUP 과의 독립성.
- BLOWUP = 9-phase **연산 엔진** (입력→출력 파이프라인).
- BREAKTHROUGH = BT-541~547 **타깃 큐레이션** (무엇을 돌파할지 목록 + audit).

**차이 증거**:
- `/Users/ghost/Dev/nexus/shared/bt/bt_keywords.jsonl` — 키워드 큐레이션 (돌파 대상 정의).
- `/Users/ghost/Dev/nexus/shared/bt/bt_domains.jsonl` — 도메인 매핑.
- `/Users/ghost/Dev/nexus/shared/bt/bt_audit.hexa` — 오딧 전용.
- `/Users/ghost/Dev/nexus/shared/bt/bt-*-report` — 보고서.
- `/Users/ghost/Dev/nexus/shared/bt/auto_bt.log` — 자동 로그.

**판정**: **확정 (N9)**. BLOWUP이 "어떻게", BREAKTHROUGH가 "무엇을" — 분리 가능한 축.

### B2 — PUBLICATION (재검)

**재검 쟁점**: 범위가 축으로 충분한가.
- 실존 자산: shared/papers/paper_candidates + convergence/papers.json.
- 기존 R1~R3 158 분야 중 "Publication/논문" 축 명시 없음 (papers 배제 원칙 R3 §11.4).
- **기각** 결정: nexus 허브의 "축" 으로 독립할 만큼 자산이 쌓이지 않았음. DISCOVERY 의 산출 채널로 흡수. 이후 라운드에서 재검토 여지.

### B3 — LOCKDOWN (재검)

**재검 쟁점**: GOVERNANCE 흡수 가능성.
- GOVERNANCE = 룰/정책 SSOT (rules/*.json, absolute_rules.json).
- LOCKDOWN = **실행 잠금 게이트** (lockdown_gate.hexa verify/status/watch/repair/safe-merge/log) + **L0 스냅샷 체계**.

**차이**:
- GOVERNANCE 는 "무엇을 금지" (텍스트 룰).
- LOCKDOWN 은 "금지를 어떻게 강제" (바이너리 파일 잠금 + snapshots/ + safe-merge).

**자산 실존**:
- `/Users/ghost/Dev/nexus/shared/lockdown/lockdown.json` — L0/L1/L2 레이어 정의.
- `/Users/ghost/Dev/nexus/shared/harness/lockdown_gate.hexa` (본 라운드 단일화 SSOT, 2026-04-14).
- `/Users/ghost/Dev/nexus/shared/lockdown/snapshots/` — 스냅샷 디렉토리 (상태 파일에 untracked로 확인).
- CLAUDE.md 의 "L0 보호" 섹션 — 29 개 L0 asset 명시.

**판정**: **확정 (N10)**. GOVERNANCE 의 집행 계열이지만, 실행 시점 잠금 + 스냅샷 SSOT 는 별도 축으로 가치 있음.

### B4 — EXECUTION-INFRA (재검)

**재검 쟁점**: 축 vs. 지원.
- 실존: cl 런처 (멀티계정) + cl-refresh (usage cache) + launchd (30m 주기) + hexa resolver.
- 이들은 **운영 인프라** — 축보다는 HARNESS 의 서브 오퍼레이션에 가깝다.
- 하지만 `/Users/ghost/Dev/nexus/shared/engine/cl_refresh_spec.json` 과 `nexus_cli_spec.json` 이 별도 엔진 스펙으로 독립.
- `convergence/cl.json` 까지 존재 — 골화 추적까지 간다.

**판정**: **확정 (N11)**. `cl` 계통 실행 인프라는 축으로 독립 가치 있음. 이름 **INFRASTRUCTURE** 로 일반화 (cl + launchd + hetzner/ubuntu/vastai 원격 실행 포함).

---

## 3. 2-hop 창발 신규 후보 (6 개)

### C16 — CONVERGENCE-METRIC (수렴 지표)

**의미**: epsilon=0.001 saturation, phi_best floor=0.8, node=515 target, edge=2087 target — **수치 수렴 기준** 그 자체 축화.

**독립 논증**: SELF-EVOLUTION 내부 수렴 **파라미터** 집합. 진화 실행과 분리된 "기준치" 축.

**근거**: shared/convergence/{nexus,anima,n6-arch,void,hexa-lang,cl,airgenome,papers}.json 8종, atlas_n6_loop.jsonl.

**중복도**: SELF-EVOLUTION 65% — 진화 내 파라미터로 흡수 가능.

**판정**: **기각** — SELF-EVOLUTION 의 서브 지표, 독립 축 아님.

### C17 — DASHBOARD (대시보드 / 시각화)

**의미**: dashboard.html + docs/index.html + reality_map_3d.html + math_atlas.html — **사용자 관측 계면**.

**독립 논증**: ATLAS 는 데이터 구조, DASHBOARD 는 UI 레이어. 분리 가능.

**근거**: shared/dashboard.html, shared/discovery/reality_map_3d.html, shared/n6/math_atlas.html, docs/index.html.

**중복도**: ATLAS 40% — ATLAS 가 데이터 SSOT 고, DASHBOARD 는 프레젠테이션.

**범위**: 0.15 (HTML 4 개) — 범위 낮음.

**판정**: **보류→R3** — ATLAS 흡수 후보 강함. R3 에서 심층 검토.

### C18 — REMOTE-COMPUTE (원격 연산)

**의미**: hetzner + ubuntu + vastai + RunPod + H100 — blowup 벤치마크/돌파 연산의 원격 기질.

**독립 논증**: 로컬 mac 은 하네스/게이트, 원격은 연산. **연산 물리 레이어** 축.

**근거**: config/hosts/{hetzner,ubuntu,vastai,infrastructure}.json, infra_state.json, MEMORY reference_hetzner.md / reference_infra.md, BLOWUP_LOCAL=1 금지 (feedback_no_blowup_local.md).

**중복도**: INFRASTRUCTURE (N11) 50% — cl-refresh 는 로컬, 원격 연산은 별도 레이어.

**판정**: **확정 (N12)** — 연산의 물리적 분리 축. INFRASTRUCTURE 가 "어떻게 로컬에서 실행", REMOTE-COMPUTE 가 "어디서 무겁게 실행".

### C19 — CALCULATOR (계산기)

**의미**: auto_stubs_gen.hexa SSOT + verify stub 생성 + calculators 등록.

**독립 논증**: BLOWUP 은 전체 파이프라인, CALCULATOR 는 **순수 수치 검증 stub** 층. GRADE_RUBRIC, CALCULATOR_RULES SSOT 있음.

**근거**: shared/calc/auto_stubs_gen.hexa (MEMORY project-auto-stubs-ssot.md), config/CALCULATOR_RULES, GRADE_RUBRIC.

**중복도**: BLOWUP 40% + ATLAS 검증 20%.

**범위**: 0.15 — 범위 낮음, 단일 SSOT.

**판정**: **기각** — BLOWUP/ATLAS 내부 검증 모듈. 축 아님.

### C20 — MONTE-CARLO (확률 검증)

**의미**: shared/monte_carlo/v6_* — 확률 기반 실험.

**독립 논증**: DSE 가 격자 탐색이라면 MC 는 **확률 샘플링**. 별개 방법론.

**근거**: shared/monte_carlo/monte_carlo_v6_*.

**중복도**: DSE 45% — DSE 확장으로 흡수 가능.

**범위**: 0.10.

**판정**: **기각** — DSE 내부 방법.

### C21 — ALIEN-SIGNAL (외계 신호 / UAP)

**의미**: shared/alien/alien_index_* — UAP/UFO 관련 인덱스.

**독립 논증**: 158 분야 중 sf-ufo 버킷 존재 (R3 D117~D121). 축까지 승격?

**근거**: shared/alien/alien_index_*, n6-arch domains/sf-ufo (R3 §2.2 5 분야).

**중복도**: BREAKTHROUGH 30% + DISCOVERY 40% — BREAKTHROUGH 의 도메인 분기로 흡수.

**범위**: 0.05 — 매우 좁음.

**판정**: **기각** — BREAKTHROUGH/DISCOVERY 분기, 독립 축 아님.

---

## 4. R2 누적 평가표

| # | 후보 | 독립성 | 범위 | 창발강도 | 중복도 | 판정 |
|---|------|--------|------|----------|--------|------|
| B1 | BREAKTHROUGH | 0.75 | 0.35 | 0.65 | 0.25 | 확정 N9 |
| B2 | PUBLICATION | 0.70 | 0.08 | 0.45 | 0.25 | 기각 |
| B3 | LOCKDOWN | 0.80 | 0.25 | 0.70 | 0.20 | 확정 N10 |
| B4 | INFRASTRUCTURE | 0.85 | 0.30 | 0.60 | 0.15 | 확정 N11 |
| C16 | CONVERGENCE-METRIC | 0.35 | 0.10 | 0.30 | 0.65 | 기각 |
| C17 | DASHBOARD | 0.55 | 0.15 | 0.45 | 0.40 | 보류→R3 |
| C18 | REMOTE-COMPUTE | 0.85 | 0.25 | 0.75 | 0.15 | 확정 N12 |
| C19 | CALCULATOR | 0.60 | 0.15 | 0.40 | 0.40 | 기각 |
| C20 | MONTE-CARLO | 0.55 | 0.10 | 0.40 | 0.45 | 기각 |
| C21 | ALIEN-SIGNAL | 0.50 | 0.05 | 0.45 | 0.30 | 기각 |

---

## 5. 신규 확정 (R2 = 4 개)

### N9 — BREAKTHROUGH (돌파 타깃)

**정의**: BT-541~547 7 대 난제 + 확장 키워드/도메인 큐레이션 + audit.

**독립 논증 (vs BLOWUP)**: BLOWUP 은 생성 엔진 (how), BREAKTHROUGH 는 타깃 큐레이션 (what).

**근거**: shared/bt/bt_keywords.jsonl, bt_domains.jsonl, bt_audit.hexa, bt-*-report, auto_bt.log.

### N10 — LOCKDOWN (잠금·스냅샷)

**정의**: L0/L1/L2 실행 시점 잠금 게이트 + 스냅샷 + safe-merge.

**독립 논증 (vs GOVERNANCE)**: GOVERNANCE = 룰 텍스트, LOCKDOWN = 실행 강제 바이너리 계층.

**근거**: shared/lockdown/lockdown.json, snapshots/, harness/lockdown_gate.hexa (단일화 SSOT).

### N11 — INFRASTRUCTURE (실행 인프라)

**정의**: cl 런처 + cl-refresh + launchd (30m) + hexa resolver + nexus_cli — **로컬 실행 기질**.

**독립 논증**: HARNESS 는 규칙 집행 레이어, INFRASTRUCTURE 는 실행 엔진 (멀티계정 cl + CLI 외부 진입점).

**근거**: shared/bin/cl, cl-refresh, cl-refresh-launchd, health-launchd, hexa resolver, shared/launchd/*.plist, engine/cl_refresh_spec.json, nexus_cli_spec.json, convergence/cl.json.

### N12 — REMOTE-COMPUTE (원격 연산)

**정의**: hetzner/ubuntu/vastai/RunPod/H100 — 무거운 blowup 벤치마크·돌파 연산의 원격 레이어.

**독립 논증 (vs INFRASTRUCTURE)**: INFRA = 로컬 실행, REMOTE-COMPUTE = 원격 연산 물리. BLOWUP_LOCAL=1 금지 룰은 이 분리 증빙.

**근거**: shared/config/hosts/{hetzner,ubuntu,vastai,infrastructure}.json, infra_state.json, MEMORY reference_hetzner.md / reference_infra.md.

---

## 6. R2 누적 축 (14 개)

| # | 축 | 라운드 |
|---|----|--------|
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

## 7. 고갈 지수

- 풀 후보 수 (R2): 10 (보류 4 + 2-hop 6)
- 신규 확정: 4
- 신규 확정 비율: 4/10 = **40.0%**
- R2 고갈 지수: **60.0%**
- 누적 축: 14 / 누적 평가: 25
- 전체 누적 확정률: 14/25 = 56%

## 8. 다음 라운드 필요: YES

R2 보류 1 (DASHBOARD) + 미탐색 sub-surface 존재:
- HARNESS 내부 H-* 메타룰 개별 축화 여부 (R3)
- harness/ 151 파일 중 thinking_engine, agent_ledger, dream_engine, consensus_loop 등 특수 엔진의 축 승격 여부
- nexus.json P3 "X_as_Y" 창발 evolution 107 Phase 의 축 흡수 vs. 노드 처리 구분
- rules/ 에 있는 pitfalls.jsonl / hexa_grammar.jsonl 의 "실수기록" 축 승격
- shared/handoff/, shared/state/, shared/skills/ 미탐색

R3 진행.
