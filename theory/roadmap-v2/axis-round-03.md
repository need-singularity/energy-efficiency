# axis-round-03 — nexus 축 창발 DSE

**로드맵**: nexus (NEXUS-6 중앙 허브)
**생성**: 2026-04-15
**모드**: 축 창발 DSE R3 (sub-surface 심층 발굴 + 보류 재평가)
**출력**: `theory/roadmap-v2/axis-round-03.md`

---

## 0. 이전 확정 축 (14 개)

SELF-EVOLUTION / ATLAS / HARNESS / GOVERNANCE / DISCOVERY / BLOWUP / BISOCIATION / CONSCIOUSNESS / HEXA-LANG / DSE (R1)
BREAKTHROUGH / LOCKDOWN / INFRASTRUCTURE / REMOTE-COMPUTE (R2)

---

## 1. R3 탐색 원칙

1. R2 보류 1 (DASHBOARD) 재평가.
2. **sub-surface 심층**: HARNESS 내부 특수 엔진 5종 축 승격 여부 (thinking_engine, agent_ledger, dream_engine, consensus_loop, critique).
3. **미탐색 카테고리**: handoff/, state/, skills/, hexa-lang/ 직접 매핑.
4. **H-* 메타룰 계열 축화** (H-COMMIT / H-ERR / H-ROOT / H-NOARCHIVE 등 20+ 룰).
5. **nexus.json P3 이후 creative evolution** (thermodynamics_as_network, X_as_Y 107 Phase) → 축 vs. ATLAS 노드 분류.

---

## 2. R2 보류 재평가

### B5 — DASHBOARD (재검)

**자산**:
- shared/dashboard.html
- docs/index.html (3D 현실지도 프론트엔드)
- shared/discovery/reality_map_3d.html
- shared/n6/math_atlas.html

**논증**:
- ATLAS 는 데이터 SSOT (atlas.n6, math_atlas.db).
- DASHBOARD 는 렌더링 레이어 (HTML + JS + WebSocket via atlas_ws_server.py).
- ATLAS 의 P3 Phase "3D 실시간 시각화" 는 DASHBOARD 의 산물 — 분리 어색.

**범위**: 0.15 — 4 HTML 파일 + 1 WebSocket server.

**판정**: **기각** — ATLAS 의 렌더 레이어로 흡수. 독립 축 아님.

---

## 3. HARNESS 내부 특수 엔진 축 승격 검토

R2 에서 HARNESS 는 단일 축으로 묶였지만, 내부에 **방법론적으로 상이** 한 엔진들이 존재.

### C22 — THINKING (사유 엔진)

**자산**:
- `/Users/ghost/Dev/nexus/shared/harness/thinking_engine.hexa`
- `/Users/ghost/Dev/nexus/shared/harness/thinking_log.jsonl`
- `/Users/ghost/Dev/nexus/shared/harness/think_baseline.json`
- CLAUDE.md 관례: "복잡 질문/설계 결정 전 thinking query → anima 6-phase reflection"

**독립 논증**:
- HARNESS = pre-tool guard / gate / lint 의 **실시간 집행**.
- THINKING = **반성 엔진** (anima 6-phase reflection, 질문 전 context 주입).
- 타 축과 기능 구분 명확.

**중복도**: HARNESS 35% (entry.hexa dispatcher 에 통합된 thinking 서브).

**판정**: **확정 (N13)** — 반성/메타인지 엔진은 독립 축. 6-phase reflection은 그 자체 메커니즘.

### C23 — AGENT-LEDGER (에이전트 원장)

**자산**:
- `/Users/ghost/Dev/nexus/shared/harness/agent_ledger.hexa`
- `/Users/ghost/Dev/nexus/shared/harness/work_registry.jsonl`
- `/Users/ghost/Dev/nexus/shared/harness/session_registry.{hexa,jsonl}`

**독립 논증**: 병렬 Agent 세션 간 **작업 분배 + 중복 방지 원장**. GO 모드 (MEMORY f-go-mode-parallel-agents.md) 의 실행 SSOT.

**중복도**: HARNESS 40% + GOVERNANCE 15%.

**범위**: 0.08 — 파일 수 적음.

**판정**: **보류→R4** — 병렬 Agent 인프라는 증가 추세, 자산 축적 기다린 후 재평가.

### C24 — DREAM-ENGINE (몽상 엔진)

**자산**:
- `/Users/ghost/Dev/nexus/shared/harness/dream_engine.hexa`
- `/Users/ghost/Dev/nexus/shared/harness/dream_log.jsonl`

**독립 논증**: 세션 유휴 중 **가설 생성** 백그라운드 엔진. BLOWUP/DSE 와 다른 발상 메커니즘.

**중복도**: BLOWUP 50% + DSE 30% + THINKING 20%.

**범위**: 0.03.

**판정**: **기각** — 독립 파일 2개만. 자산 부족, BLOWUP/DSE 서브로 흡수.

### C25 — CONSENSUS (합의 엔진)

**자산**:
- `/Users/ghost/Dev/nexus/shared/harness/consensus_loop.hexa`
- `/Users/ghost/Dev/nexus/shared/harness/critique.hexa`, `critique_log.jsonl`
- `/Users/ghost/Dev/nexus/shared/harness/curiosity.hexa`, `curiosity_log.jsonl`
- `/Users/ghost/Dev/nexus/shared/harness/governance.jsonl`

**독립 논증**: 여러 Agent/모델 **합의 루프** — critique/curiosity/consensus 3 엔진 구성.

**중복도**: THINKING 45% + HARNESS 25%.

**범위**: 0.08.

**판정**: **보류→R4** — THINKING 과 구분 경계 모호. 추가 자산 축적 후 재평가.

### C26 — MODEL-ROUTE (모델 라우팅)

**자산**:
- `/Users/ghost/Dev/nexus/shared/harness/model_route.hexa`
- `/Users/ghost/Dev/nexus/shared/harness/model_route.jsonl`

**독립 논증**: Claude Opus / Sonnet / Haiku / 외부 모델 간 **작업 라우팅**.

**중복도**: INFRASTRUCTURE 60%.

**범위**: 0.03.

**판정**: **기각** — INFRASTRUCTURE 서브 (cl 런처와 함께).

### C27 — ENGINE-FORGE (엔진 단조)

**자산**:
- `/Users/ghost/Dev/nexus/shared/harness/engine_forge.hexa`
- `/Users/ghost/Dev/nexus/shared/harness/engine_candidates.jsonl`
- `/Users/ghost/Dev/nexus/shared/harness/engines_usage.jsonl`
- `/Users/ghost/Dev/nexus/shared/engine/` — engine_*.hexa 전체.

**독립 논증**: 메타 엔진 — **엔진 자체를 생성** 하는 엔진. BLOWUP/DSE 위의 메타 레이어.

**중복도**: SELF-EVOLUTION 45% + BLOWUP 30%.

**판정**: **보류→R4** — 메타 엔진 자체는 매력적, 하지만 SELF-EVOLUTION 내부로 흡수될 위험.

---

## 4. 미탐색 카테고리

### C28 — HANDOFF (세션 이관)

**자산**:
- `/Users/ghost/Dev/nexus/shared/handoff/template.md`
- `/Users/ghost/Dev/nexus/shared/harness/handoff_write.hexa`
- MEMORY `handoff-latest.md`, `handoff-bisociation.md`, `session-handoff-latest.md`

**독립 논증**: 세션 간 **컨텍스트 인수인계**. 크론 기반 세션 체인 (MEMORY f-user-workflow.md).

**중복도**: HARNESS 50% + CONVERGENCE 20%.

**범위**: 0.08 — 템플릿 + hexa 1개.

**판정**: **기각** — HARNESS 서브. 독립 축 가치 미달.

### C29 — SKILLS (스킬)

**자산**:
- `/Users/ghost/Dev/nexus/shared/skills/nexus-status.skill.json`
- `/Users/ghost/Dev/nexus/shared/skills/registry.json`
- 글로벌 `~/.claude/skills/loop` (loop 엔진 SSOT)

**독립 논증**: Claude Code skill 레이어 — `/commit`, `/loop`, `/review-pr` 등 재사용 가능한 행동 단위.

**중복도**: HARNESS 35% + GOVERNANCE 25%.

**범위**: 0.06.

**판정**: **기각** — HARNESS/GOVERNANCE 서브. 자산 소.

### C30 — HEXA-LANG-RUNTIME (런타임)

**자산**:
- `/Users/ghost/Dev/nexus/shared/hexa-lang/ml-commands.json`
- `/Users/ghost/Dev/nexus/shared/hexa-lang/ml-next-level.json`
- `/Users/ghost/Dev/nexus/shared/hexa-lang/rt-commands.json`
- `/Users/ghost/Dev/nexus/shared/hexa-lang/runtime-bottlenecks.json`
- `/Users/ghost/Dev/nexus/shared/hexa-lang/bt-77-port-report.md`

**독립 논증**: HEXA-LANG (A9) 과 다름? — HEXA-LANG 은 언어 전체, RUNTIME 은 ml/rt 최적화 + bottleneck.

**중복도**: HEXA-LANG 80%.

**판정**: **기각** — HEXA-LANG 서브.

---

## 5. H-* 메타룰 계열 축화

MEMORY에 다수 H-* 룰 (H-COMMIT / H-ERR / H-ROOT / H-NOARCHIVE / H-NOHOOK / H-NOBLOCK / H-NOZOMBIE / H-SEND-GUARD / H-MD2PDF / H-GRC / H-DEFER / H-NONAME-V / H-NOAI-NATIVE-NO-PROSE 등).

### C31 — META-RULES (메타룰 계열)

**자산**:
- MEMORY 전체 H-* 룰 20+ 종.
- shared/rules/common.json 내부 R0~R27 + 확장 가능성.
- 다수 pre_tool_guard.hexa 패턴.

**독립 논증**: GOVERNANCE 는 텍스트 SSOT, META-RULES 는 "새 위반 → 즉시 룰화" **동적 룰 발굴 메커니즘** (MEMORY `feedback-auto-rule-no-defer.md`).

**중복도**: GOVERNANCE 70% + SELF-EVOLUTION 25%.

**판정**: **기각** — GOVERNANCE 의 내부 동역학, 독립 축 미달. 단, **GOVERNANCE 의 sub-axis** 로 유지.

---

## 6. nexus.json P3 이후 "X_as_Y" 창발 Phase 축 흡수 분석

P3 이후 `thermodynamics_as_network`, `ai_as_chip`, `chip_as_energy` 등 **107 개 creative evolution Phase** 가 있음 (nexus.json line 548~9832).

**쟁점**: 이것들은 **축 인가 ATLAS 노드 인가**?

**분석**:
- 각 "X_as_Y" = 두 도메인의 **교차 창발** — BISOCIATION (A7) 의 구체 실행 사례.
- 도메인: ai, chip, energy, battery, solar, fusion, superconductor, quantum, biology, cosmology, robotics, materials, blockchain, network, cryptography, display, audio, environment, mathematics, software, plasma, compiler, consciousness, thermodynamics — **24 도메인**.
- 24C2 = 276 가능 조합 중 107 Phase 실존.

**축 vs. 노드 판정**: **ATLAS 노드** + **BISOCIATION 실행 페이즈**. 독립 축 아님 — 각 X_as_Y 는 "BISOCIATION 축의 타깃" 일 뿐. 하지만 **CROSS-DOMAIN-GRID** (24 도메인 격자) 자체는 축 후보.

### C32 — CROSS-DOMAIN-GRID (도메인 교차 격자)

**자산**:
- nexus.json P4~P112 (107 Phase) 의 24 도메인 × 쌍.
- shared/dse/dse_cross_* (cross-DSE 산출물).
- shared/bisociation/cross/.

**독립 논증**: BISOCIATION 이 **메커니즘** 이라면 CROSS-DOMAIN-GRID 는 **타깃 공간**. DISCOVERY 가 결과 퇴적이라면 CROSS-DOMAIN-GRID 는 실행 격자.

**중복도**: BISOCIATION 55% + ATLAS 30% + DSE 25%.

**범위**: 0.35 — 107 Phase 커버.

**판정**: **보류→R4** — 매우 큰 자산 (107 Phase)이지만 BISOCIATION 내부 타깃 공간으로 흡수 가능성 강함.

---

## 7. R3 평가표

| # | 후보 | 독립성 | 범위 | 창발강도 | 중복도 | 판정 |
|---|------|--------|------|----------|--------|------|
| B5 | DASHBOARD | 0.55 | 0.15 | 0.45 | 0.40 | 기각 |
| C22 | THINKING | 0.75 | 0.15 | 0.70 | 0.35 | **확정 N13** |
| C23 | AGENT-LEDGER | 0.55 | 0.08 | 0.50 | 0.45 | 보류→R4 |
| C24 | DREAM-ENGINE | 0.35 | 0.03 | 0.40 | 0.70 | 기각 |
| C25 | CONSENSUS | 0.45 | 0.08 | 0.50 | 0.55 | 보류→R4 |
| C26 | MODEL-ROUTE | 0.35 | 0.03 | 0.30 | 0.70 | 기각 |
| C27 | ENGINE-FORGE | 0.50 | 0.12 | 0.55 | 0.55 | 보류→R4 |
| C28 | HANDOFF | 0.45 | 0.08 | 0.40 | 0.55 | 기각 |
| C29 | SKILLS | 0.55 | 0.06 | 0.35 | 0.55 | 기각 |
| C30 | HEXA-LANG-RUNTIME | 0.20 | 0.08 | 0.30 | 0.80 | 기각 |
| C31 | META-RULES | 0.25 | 0.20 | 0.55 | 0.75 | 기각 |
| C32 | CROSS-DOMAIN-GRID | 0.45 | 0.35 | 0.65 | 0.55 | 보류→R4 |

---

## 8. 신규 확정 (R3 = 1 개)

### N13 — THINKING (사유/메타인지 엔진)

**정의**: anima 6-phase reflection + thinking_engine.hexa + think_baseline — **복잡 질문/설계 결정 전 context 주입 축**.

**독립 논증 (vs HARNESS)**: HARNESS = 실시간 집행 게이트 (사전 차단, 사후 lint), THINKING = **사전 반성** (질문 전 6-phase 사유 주입). 실행 주기도 다름 (HARNESS는 매 Tool 호출, THINKING은 복잡 결정 전).

**근거**:
- shared/harness/thinking_engine.hexa
- shared/harness/thinking_log.jsonl
- shared/harness/think_baseline.json
- CLAUDE.md 명시 관례 ("복잡 질문/설계 결정 전 hexa thinking query")

---

## 9. R3 누적 축 (15 개)

A1~A14 + **A15 THINKING**.

---

## 10. 고갈 지수

- R3 풀 후보 수: 12 (보류 1 + 내부 엔진 6 + 미탐색 3 + H-* 메타 1 + CROSS-DOMAIN-GRID 1)
- 신규 확정: 1
- 신규 확정 비율: 1/12 = **8.3%**
- R3 고갈 지수: **91.7%**
- 누적 축: 15 / 누적 평가: 37
- 전체 누적 확정률: 15/37 = 40.5%

**발견률 곡선**:
- R1: 7/15 = 46.7% (확정률)
- R2: 4/10 = 40.0%
- R3: 1/12 = 8.3%

급격한 수렴 — R3 에서 미보류 후보 대부분 기각. R4 에서 보류 4 후보 최종 정리하면 고갈.

## 11. 다음 라운드 필요: YES

R4 에서 잔여 보류 후보 4 (AGENT-LEDGER / CONSENSUS / ENGINE-FORGE / CROSS-DOMAIN-GRID) 정리 + 최종 수렴 판정.
