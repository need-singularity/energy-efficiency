# axis-round-04 — nexus 축 창발 DSE

**로드맵**: nexus (NEXUS-6 중앙 허브)
**생성**: 2026-04-15
**모드**: 축 창발 DSE R4 (최종 보류 정리 + 수렴 임박)
**출력**: `theory/roadmap-v2/axis-round-04.md`

---

## 0. 이전 확정 축 (15 개)

R1 (10): SELF-EVOLUTION / ATLAS / HARNESS / GOVERNANCE / DISCOVERY / BLOWUP / BISOCIATION / CONSCIOUSNESS / HEXA-LANG / DSE
R2 (4): BREAKTHROUGH / LOCKDOWN / INFRASTRUCTURE / REMOTE-COMPUTE
R3 (1): THINKING

---

## 1. R4 탐색 원칙

1. R3 보류 4 후보 (AGENT-LEDGER / CONSENSUS / ENGINE-FORGE / CROSS-DOMAIN-GRID) 최종 정리.
2. 직관적 잔여 후보 (LOGS / ARCHIVE / STATE / CALC) 3-hop 창발로 추가 점검.
3. 유저의 원본 shared/ 카테고리 맵 (monte_carlo, singularity, alien 등) 중 이미 결정된 것 확인.
4. 신규 창발 0 ~ 저조 시 고갈 판정, R5 준비.

---

## 2. R3 보류 4 후보 최종 정리

### B6 — AGENT-LEDGER (최종)

**심층 자산**:
- shared/harness/agent_ledger.hexa
- shared/harness/session_registry.{hexa,jsonl}
- shared/harness/work_registry.jsonl
- shared/harness/session_worktree.hexa
- MEMORY f-go-mode-parallel-agents.md — GO 모드 병렬 Agent 원칙

**독립 논증 심화**:
- HARNESS = 단일 세션 내 **Tool 호출 게이트**.
- AGENT-LEDGER = **병렬 세션/에이전트 간** 원장 + worktree 관리.
- **분리 근거 추가**: session_worktree.hexa 가 git worktree 기반 분기 세션 지원. 자체 방법론.

**중복도 재계산**: HARNESS 35%, SELF-EVOLUTION 15% → 독립성 0.60.

**판정**: **확정 (N14)** — 병렬 에이전트 오케스트레이션은 독립 축.

### B7 — CONSENSUS (최종)

**심층 자산**:
- shared/harness/consensus_loop.hexa
- shared/harness/critique.hexa + critique_log.jsonl
- shared/harness/curiosity.hexa + curiosity_log.jsonl
- shared/harness/cross_feed.hexa + cross_feed.jsonl
- shared/harness/governance.jsonl
- shared/harness/broadcast.hexa + broadcast.jsonl

**독립 논증 재검**:
- THINKING (N13) = 단일 Agent 6-phase 반성.
- CONSENSUS = 다중 Agent/모델 **cross-critique + curiosity + broadcast** 합의.
- 분리 가능하지만, 자산 중복도 THINKING 과 45%.
- **결정 기준**: 실행 주기·목적 차별화 여부.
  - THINKING: 질문 전 (pre-prompt).
  - CONSENSUS: 질문 후 (post-answer cross-check + broadcast).

**판정**: **확정 (N15)** — 사후 cross-검증 + broadcast 는 독립 기능.

### B8 — ENGINE-FORGE (최종)

**심층 자산**:
- shared/harness/engine_forge.hexa
- shared/harness/engine_candidates.jsonl
- shared/harness/engines_usage.jsonl
- shared/engine/engine_*.hexa 전체
- shared/engine/cl_refresh_spec.json + nexus_cli_spec.json
- shared/engine/engine_{anima,nexus}_strategy

**독립 논증**:
- SELF-EVOLUTION = 상태 진화.
- ENGINE-FORGE = **엔진 자체를 생성** 하는 메타 엔진.
- 자산 풍부 (engine/ 카테고리 독립 존재 + harness 3 파일).
- 차이: SELF-EVOLUTION 이 "데이터/atlas 진화" 라면 ENGINE-FORGE 는 "코드 엔진 단조" — 코드 생성 레이어.

**중복도 재계산**: SELF-EVOLUTION 40% (상태 vs. 코드 구분 명확) + BLOWUP 25%. 독립성 0.55.

**판정**: **확정 (N16)** — 메타 엔진 생성 레이어는 독립. engine/ 카테고리 실존이 결정적.

### B9 — CROSS-DOMAIN-GRID (최종)

**심층 자산**:
- nexus.json P4~P112 (107 Phase) X_as_Y 교차 evolution.
- shared/dse/dse_cross_* 산출물.
- shared/bisociation/cross/.
- 24 도메인 × 쌍 격자 (ai, chip, energy, battery, solar, fusion, superconductor, quantum, biology, cosmology, robotics, materials, blockchain, network, cryptography, display, audio, environment, mathematics, software, plasma, compiler, consciousness, thermodynamics).

**독립 논증 재검**:
- BISOCIATION (A7) = 쌍연관 메커니즘.
- CROSS-DOMAIN-GRID = **타깃 격자** (24 × 23 / 2 = 276 가능 pair 공간).
- nexus.json 에서 실제 Phase 이름으로 드러나 있음 — 실행 격자 자체가 축.
- DSE (A10) 과 다른가? — DSE 는 discovery 방법론, CROSS-DOMAIN-GRID 는 **도메인 격자 구조**.

**중복도 재계산**: BISOCIATION 50% + DSE 25% + ATLAS 20%. 독립성 0.45.

**판정**: **확정 (N17)** — 107 Phase 대규모 자산 근거로 독립 축 승격. BISOCIATION의 타깃 공간이지만 격자 구조 자체가 축 자격.

---

## 3. 추가 후보 3-hop 점검

### C33 — LOGS (로그 계열)

**자산**: shared/logs/ (cmd_router.log, cl-refresh.stdout/stderr.log).

**판정**: 기각 — 운영 로그 저장소, 축 아님.

### C34 — ARCHIVE (아카이브)

**자산**: shared/archive/ (hooks-20260414, superseded-20260414 등).

**판정**: 기각 — 시간축 백업, 축 아님. MEMORY H-NOARCHIVE 룰도 있음.

### C35 — STATE (상태 파일)

**자산**: shared/state/h100_heartbeat, shared/infra_state.json, bridge_state.json, dispatch_state.json.

**판정**: 기각 — 다른 축 (INFRASTRUCTURE / REMOTE-COMPUTE) 의 상태 스냅샷.

### C36 — CALC (계산기 SSOT) 재검

**자산**: shared/calc/auto_stubs_gen.hexa.

**R2 에서 기각했으나 재검**: auto_stubs_gen 은 SSOT, verify stub 생성 단일 엔진.

**판정**: 기각 유지 — BLOWUP/ATLAS 검증 서브.

### C37 — LOOP (반복 엔진)

**자산**:
- shared/harness/loop/ (SSOT)
- shared/harness/loop.hexa
- shared/harness/loop-guard.hexa
- shared/harness/loop_controller.hexa
- shared/harness/loop_state.jsonl
- shared/harness/loop_hooks
- shared/harness/loop_report
- 전역 ~/.claude/skills/loop
- CLAUDE.md: "loop: 글로벌 ~/.claude/skills/loop + 엔진 shared/harness/loop (SSOT) — roadmap shared/roadmaps/nexus.json 3-track×phase×gate 자동"

**독립 논증**: roadmap 3-track × phase × gate 자동화는 SELF-EVOLUTION 의 핵심 메커니즘. 하지만 loop 엔진 자체는 독립 자산 클러스터.

**중복도**: SELF-EVOLUTION 65% + HARNESS 20%.

**판정**: **기각** — SELF-EVOLUTION 의 실행 루프로 흡수. 독립 미달.

---

## 4. R4 평가표

| # | 후보 | 독립성 | 범위 | 창발강도 | 중복도 | 판정 |
|---|------|--------|------|----------|--------|------|
| B6 | AGENT-LEDGER | 0.60 | 0.12 | 0.55 | 0.35 | **확정 N14** |
| B7 | CONSENSUS | 0.55 | 0.15 | 0.60 | 0.45 | **확정 N15** |
| B8 | ENGINE-FORGE | 0.55 | 0.18 | 0.60 | 0.45 | **확정 N16** |
| B9 | CROSS-DOMAIN-GRID | 0.45 | 0.35 | 0.65 | 0.55 | **확정 N17** |
| C33 | LOGS | 0.30 | 0.05 | 0.20 | 0.70 | 기각 |
| C34 | ARCHIVE | 0.20 | 0.05 | 0.10 | 0.80 | 기각 |
| C35 | STATE | 0.30 | 0.08 | 0.25 | 0.70 | 기각 |
| C36 | CALC (재검) | 0.55 | 0.10 | 0.35 | 0.50 | 기각 |
| C37 | LOOP | 0.35 | 0.15 | 0.40 | 0.65 | 기각 |

---

## 5. 신규 확정 (R4 = 4 개)

### N14 — AGENT-LEDGER (병렬 에이전트 원장)

**정의**: 병렬 세션/에이전트 간 작업 분배 + 중복 방지 + worktree 분기.

**독립 논증**: HARNESS 가 단일 세션 Tool 게이트, AGENT-LEDGER는 다중 세션 간 원장.

**근거**: shared/harness/agent_ledger.hexa, session_registry.{hexa,jsonl}, work_registry.jsonl, session_worktree.hexa, MEMORY f-go-mode-parallel-agents.md.

### N15 — CONSENSUS (합의/크로스-크리틱)

**정의**: 사후 cross-critique + curiosity + broadcast 다중 Agent 합의 루프.

**독립 논증 (vs THINKING)**: THINKING = 사전 단일 6-phase 반성. CONSENSUS = 사후 다중 합의. 실행 주기 구분.

**근거**: shared/harness/consensus_loop.hexa, critique.hexa, curiosity.hexa, cross_feed.hexa, broadcast.hexa.

### N16 — ENGINE-FORGE (엔진 단조)

**정의**: 엔진 자체를 생성하는 메타 엔진 레이어.

**독립 논증 (vs SELF-EVOLUTION)**: 진화 = 데이터·atlas·상태, ENGINE-FORGE = 코드 엔진 단조 (engine_*.hexa 자동 생성).

**근거**: shared/harness/engine_forge.hexa, engine_candidates.jsonl, engines_usage.jsonl, shared/engine/engine_*.hexa, cl_refresh_spec.json, nexus_cli_spec.json.

### N17 — CROSS-DOMAIN-GRID (도메인 교차 격자)

**정의**: 24 도메인 × 쌍 교차 evolution 격자 (X_as_Y, 276 가능 pair / 107 실행).

**독립 논증 (vs BISOCIATION)**: BISOCIATION = 메커니즘, GRID = 타깃 구조.

**근거**: nexus.json P4~P112 (107 Phase), shared/dse/dse_cross_*, shared/bisociation/cross/.

---

## 6. R4 누적 축 (19 개)

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
| A15 | THINKING | R3 |
| A16 | AGENT-LEDGER | R4 |
| A17 | CONSENSUS | R4 |
| A18 | ENGINE-FORGE | R4 |
| A19 | CROSS-DOMAIN-GRID | R4 |

---

## 7. 고갈 지수

- R4 풀 후보 수: 9 (보류 4 + 추가 5)
- 신규 확정: 4
- 신규 확정 비율: 4/9 = **44.4%**
- R4 고갈 지수: **55.6%**
- 누적 축: 19 / 누적 평가: 46
- 전체 누적 확정률: 19/46 = 41.3%

**발견률 곡선**:
- R1: 46.7% (7/15)
- R2: 40.0% (4/10)
- R3: 8.3% (1/12)
- R4: 44.4% (4/9)

R3 에서 8.3% 로 저점 찍고 R4 에서 보류 일괄 확정으로 반등 — 하지만 **새 후보 발굴이 점점 어려워짐**. 남은 자산 영역 대부분이 이미 축 매핑됨.

## 8. 다음 라운드 필요: YES (최종 확인용)

R5 에서 **신규 창발 0 을 확인** 해야 최종 고갈 선언 가능. 남은 영역:
- GOVERNANCE 내부 세분 (R0~R27 개별 축 vs. 하위).
- CONSCIOUSNESS 내부 (anima subrepo 개별 모듈).
- BLOWUP 내부 (6 modules 개별 축 vs 서브).
- ATLAS 내부 (math_atlas vs. periodic_table_118 분리).

이들은 **내부 세분** 이지 신규 축 후보로 보기 어려움. R5 에서 공식 확인 후 종료 예상.
