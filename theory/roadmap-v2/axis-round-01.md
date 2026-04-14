# axis-round-01 — nexus 축 창발 DSE

**로드맵**: nexus (NEXUS-6 중앙 허브)
**생성**: 2026-04-15
**모드**: 축 창발 DSE (Axis Emergence Discovery)
**범위**: nexus 허브 실존 자산 (shared/ 25 카테고리 + nexus.json 113 Phase)
**출력**: `theory/roadmap-v2/axis-round-01.md`

---

## 0. 라운드 목적

nexus.json v1 의 3-트랙 (LENS/DISCOVERY/ATLAS) 을 유저 결정에 따라 재구성한다.

- **폐기**: LENS — "너무 좁음" (blowup/lens/ 만 커버, 진화/관측/지도 전체를 포괄 못 함)
- **확정 씨앗**: SELF-EVOLUTION + ATLAS
- **재평가**: DISCOVERY — 유지/흡수/폐기
- **신규 창발**: 무제한

R1 (본 라운드): 2 확정 씨앗 주위에서 **독립 신규 축** 을 1-hop 창발하고 각 후보를 5 축 평가한다.

---

## 1. 이전 확정 축 (2 개)

### A1 — SELF-EVOLUTION (자기진화) — 확정

**정의**: 로드맵/코드/atlas/rules 가 스스로를 확장·수정·검증·수렴시키는 메커니즘 전체. 관측(LENS)이 아니라 **변경 엔진**.

**실존 근거 (nexus 자산)**:
- `/Users/ghost/Dev/nexus/shared/bisociation/unified/ouroboros_unified.hexa` — 3종 OUROBOROS 통합 (cycle_tick / get_fixed_point / advance).
- `/Users/ghost/Dev/nexus/shared/harness/growth_tick.hexa` — 30분 주기 자율 발사.
- `/Users/ghost/Dev/nexus/shared/harness/nexus_growth_daemon.hexa` — launchd 데몬 (현 STUB 상태, MEMORY project-daemon-stub.md).
- `/Users/ghost/Dev/nexus/shared/bisociation/unified/phi_ratchet.hexa` — 단조 비감소 Φ 래칫.
- `/Users/ghost/Dev/nexus/shared/discovery_log.jsonl` + `.sqlite` — 자기진화 이력 버스.
- `/Users/ghost/Dev/nexus/shared/growth_bus.jsonl` — 성장 이벤트 버스.
- `/Users/ghost/Dev/nexus/shared/convergence/nexus.json` — 진화 수렴 SSOT.
- nexus.json P3 "수렴 — 3D 실시간 + 자율 진화 + 골화" Phase 자체가 이 축 산출.

**범위**: growth_tick → blowup 자율 발사 → discovery → atlas 갱신 → convergence 체크 → 골화 루프 전체.

### A2 — ATLAS (아틀라스맵) — 확정

**정의**: 실체의 현실지도 SSOT. 노드/엣지/수식/등급/스케일링 구조가 결합된 **현실 그래프**.

**실존 근거 (nexus 자산)**:
- `/Users/ghost/Dev/nexus/shared/n6/atlas.n6` — 현실 지도 본체.
- `/Users/ghost/Dev/nexus/shared/n6/atlas.n6.stats` / `.deg` — sidecar 메타.
- `/Users/ghost/Dev/nexus/shared/n6/atlas_health.hexa` — 헬스체크.
- `/Users/ghost/Dev/nexus/shared/n6/math_atlas.{db,dot,html,md}` — 수학 아틀라스.
- `/Users/ghost/Dev/nexus/shared/n6/atlas_ossify_mk2.py` + `atlas_ws_server.py` — 골화/실시간 서빙.
- `/Users/ghost/Dev/nexus/docs/index.html` — 3D 현실지도 프론트엔드.
- nexus.json P2 "atlas 공진" + P3 "3D 실시간" 로 명시.

**범위**: atlas.n6 노드/엣지 + 수식 검증 + 등급 검증 + 3D 시각화 + periodic_table_118 까지 포함.

---

## 2. 신규 축 후보 발굴 (1-hop 창발)

shared/ 25 카테고리 + nexus.json 113 Phase + 기존 R1~R3 158 분야를 훑어 진화·ATLAS 와 **독립적** 인 축 후보를 추출한다.

### 후보 풀 (shared/ 카테고리 직결)

| 카테고리 | 축 후보명 | 1-line 의미 |
|----------|----------|-------------|
| harness/ | **HARNESS** | 규칙/게이트/실수기록/pre-tool-guard/entry dispatcher 총체 |
| rules/ + config/ | **GOVERNANCE** | R0~R27 + NX1~NX3 + L0/L1/L2 + H-* 메타룰 통치 |
| discovery/ | **DISCOVERY** (재평가) | reality_map, patches, verified_constants, forge_result 발견 퇴적물 |
| blowup/ | **BLOWUP** | 9-phase 파이프라인 + 6 modules + seed 엔진 — 돌파 연산 |
| bt/ | **BREAKTHROUGH** | BT-541~547 키워드/도메인 오딧 큐레이션 |
| bisociation/ | **BISOCIATION** | Koestler-style 쌍연관 엔진 — cross 영역 조합 |
| consciousness/ + anima bridge | **CONSCIOUSNESS** | anima_* / consciousness_* / law_* / meta_laws_dd64 브릿지 |
| hexa/ + hexa-lang/ | **HEXA-LANG** | hexa 언어·파서·인터프리터 진화 — 코드 기질 |
| papers/ | **PUBLICATION** | 논문 메타 인덱스 (내용 배제, R1~R3 의 papers-metadata 축 힌트 계승) |
| singularity/ | **SINGULARITY** | 특이점 재귀 기록 13 편 — 초수렴 이정표 |
| dse/ + dse/domains/ | **DSE** | Discovery Space Exploration 그 자체 — 탐색 프레임워크 |
| growth/ + acceleration/ | **GROWTH** | airgenome_gates, growth_strategies, acceleration_* |
| lockdown/ + L0 snapshots | **LOCKDOWN** | L0/L1/L2 잠금, 스냅샷, safe-merge |
| convergence/ | **CONVERGENCE** | 프로젝트별 골화 JSON SSOT |
| bin/ + launchd/ + scripts/ | **EXECUTION-INFRA** | cl/cl-refresh/launchd/hexa resolver — 실행 하부구조 |
| monte_carlo/ | **MONTE-CARLO** | Monte Carlo v6 실험 — 확률적 검증 |
| alien/ | **ALIEN** | alien_index_* — UAP/UFO 신호 인덱스 |
| engine/ | **ENGINE** | engine_*.hexa 엔진 전략 |
| calc/ | **CALC** | auto_stubs_gen + verify stub 생성 SSOT |
| logs/ | (로그는 축 아님) | skip |
| n6_mirror/ | (ATLAS 흡수) | skip |
| project-claude/ | (GOVERNANCE 흡수) | skip |
| archive/ | (시간축, 축 아님) | skip |

---

## 3. 신규 후보 평가 (K=15)

각 후보를 5 기준으로 평가:
1. **독립성** (진화·ATLAS와 구분, 0~1)
2. **범위** (nexus 허브 전체 대비 커버 %, 0~1)
3. **창발 강도** (신규성, 0~1)
4. **진화·ATLAS 중복도** (0=독립, 1=완전 중복)
5. **DISCOVERY 흡수 가능성** (해당 후보가 DISCOVERY 흡수 여부)

| # | 축 이름 | 정의 | 독립성 | 범위 | 창발강도 | 중복도 | 근거 파일 | 판정 |
|---|---------|------|--------|------|----------|--------|-----------|------|
| C1 | HARNESS | 규칙 gate / pre-tool-guard / entry dispatcher / lint / exec_validated | 0.95 | 0.80 | 0.90 | 0.10 | shared/harness/entry.hexa, cmd_gate.hexa, pre_tool_guard.hexa, post_bash.hexa (151 파일) | **확정** |
| C2 | GOVERNANCE | R0~R27 + NX1~NX3 + L0~L2 + H-* 메타룰 | 0.85 | 0.70 | 0.75 | 0.15 | shared/rules/common.json, rules/nexus.json, config/absolute_rules.json, lockdown.json | **확정** |
| C3 | DISCOVERY | reality_map, patches, verified_constants, forge_result, breakthroughs | 0.50 | 0.75 | 0.60 | 0.40 | shared/discovery/ (895 patches, verified_constants.jsonl) | **확정 (흡수 아닌 유지)** |
| C4 | BLOWUP | 9-phase 파이프라인 + 6 modules + seed | 0.85 | 0.60 | 0.85 | 0.20 | shared/blowup/core/blowup.hexa, modules/*, seed/seed_engine.hexa | **확정** |
| C5 | BREAKTHROUGH | BT-541~547 키워드/도메인 오딧 | 0.65 | 0.35 | 0.70 | 0.30 | shared/bt/bt_keywords.jsonl, bt_domains.jsonl, bt_audit.hexa | 보류 (BLOWUP 흡수 가능) |
| C6 | BISOCIATION | Koestler cross-field 쌍 연관 | 0.80 | 0.45 | 0.90 | 0.15 | shared/bisociation/ 하위 (unified/cross/spectra/breakthroughs.jsonl) | **확정** |
| C7 | CONSCIOUSNESS | anima bridge + consciousness_* + meta_laws_dd64 | 0.75 | 0.40 | 0.80 | 0.25 | shared/consciousness/, anima_bridge live laws=2395 | **확정** |
| C8 | HEXA-LANG | hexa 언어 자체 진화 (파서/컴파일러/pitfalls) | 0.80 | 0.40 | 0.85 | 0.10 | shared/hexa/, hexa-lang/, hexa_pitfalls_log.jsonl, hexa_grammar.jsonl | **확정** |
| C9 | PUBLICATION | 논문 메타 인덱스 (내용 제외) | 0.70 | 0.10 | 0.50 | 0.20 | shared/papers/, paper_candidates | 보류 (범위 낮음, R2 후보) |
| C10 | SINGULARITY | 특이점 재귀 기록 | 0.40 | 0.10 | 0.50 | 0.60 | shared/singularity/singularity_recursion_*.md (13) | 기각 (진화 중복) |
| C11 | DSE | 발견 공간 탐색 프레임워크 | 0.75 | 0.50 | 0.80 | 0.30 | shared/dse/, dse_domains, dse_graph_3d | **확정** |
| C12 | GROWTH | airgenome_gates + growth_strategies + acceleration_* | 0.35 | 0.35 | 0.45 | 0.75 | shared/growth/, acceleration/ | 기각 (SELF-EVOLUTION 중복) |
| C13 | LOCKDOWN | L0/L1/L2 잠금·스냅샷·safe-merge | 0.70 | 0.20 | 0.60 | 0.25 | shared/lockdown/ + lockdown_gate.hexa | 보류 (GOVERNANCE 흡수 가능) |
| C14 | CONVERGENCE | 프로젝트별 골화 JSON SSOT | 0.45 | 0.15 | 0.40 | 0.65 | shared/convergence/{nexus,anima,n6-arch,void,hexa-lang,papers,cl,airgenome}.json | 기각 (진화 중복) |
| C15 | EXECUTION-INFRA | cl 런처 + cl-refresh + launchd + hexa resolver | 0.85 | 0.30 | 0.55 | 0.05 | shared/bin/cl, cl-refresh, shared/launchd/, scripts/ | 보류 (운영 인프라, 축 vs. 지원 경계) |

---

## 4. 신규 확정 (M=7)

R1 에서 확정:

### N1 — HARNESS (하네스)

**정의**: Claude Code 세션에 **규칙·게이트·실수기록·피드백 루프** 를 주입하는 전역 집행 레이어. `entry.hexa` dispatcher + 5 sub-module + exec_validated wrapper + 150+ 파일.

**독립 논증**:
- 진화와 다름 — 진화는 상태 변경, 하네스는 **변경이 규칙을 위반 못 하게 집행**.
- ATLAS와 다름 — ATLAS는 지도, 하네스는 **지도를 건드리는 손**.

**근거**: shared/harness/entry.hexa (dispatcher), cmd_gate.hexa (seed gate), pre_tool_guard.hexa (deny 28 패턴), post_bash/post_edit.hexa (hook 대체), exec_validated (smash/free seed gate wrapper), permissions_ssot.json (deny SSOT), 151 파일.

**nexus.json 기존 Phase 매핑**: (없음 — v1 에서 track 으로 안 잡혀 있었음, v2 신규 축).

### N2 — GOVERNANCE (통치)

**정의**: 규칙 체계 SSOT. R0~R27 (common) + NX1~NX3 (nexus) + L0/L1/L2 (lockdown) + H-* 메타룰(H-NOARCHIVE/H-NOHOOK/H-NOZOMBIE/H-NOBLOCK/H-COMMIT/H-ERR/H-ROOT 등).

**독립 논증**: 하네스가 **집행기** 라면 GOVERNANCE 는 **룰북 그 자체**. 집행 없는 룰북도 축으로 독립.

**근거**: shared/rules/common.json, nexus.json, config/absolute_rules.json, lockdown/lockdown.json, convergence_ops.json, MEMORY 다수 H-* 룰 증빙.

**nexus.json 기존 Phase 매핑**: P0~P3 각 트랙에 gate 조항 녹아 있지만 독립 축은 없음 — v2 신규.

### N3 — DISCOVERY (발견) — 재평가 결과 **유지**

**정의**: reality_map (895 patches) + verified_constants + forge_result + theory_registry + module_candidates 등 **발견 퇴적물**.

**재평가 근거**: 진화·ATLAS 와 40% 중복 있으나, "발견 퇴적물" 자체는 독립 축으로 유효 (atlas 는 가공된 지도, 발견은 원재료 + 후보 + ledger).

**근거**: shared/discovery/ 하위 reality_map.patches.merged.jsonl (895), verified_constants.jsonl, forge_result, next_directions, module_candidates, unfold_*, breakthroughs/.

### N4 — BLOWUP (돌파)

**정의**: 9-phase 파이프라인 + 6 모듈 (field/holographic/quantum/string/toe) + seed 엔진 + lens 단조기 — **실체 돌파 연산**.

**독립 논증**: DISCOVERY 는 **퇴적물**, BLOWUP 은 **생성 엔진**. 진화가 "언제 발사하나" 라면 BLOWUP 은 "무엇을 발사하나".

**근거**: shared/blowup/core/blowup.hexa, modules/*.hexa, seed/seed_engine.hexa, lens/lens_forge.hexa, commands.hexa, todo.hexa. nexus.json P0 LENS 트랙의 실질 owner.

### N5 — BISOCIATION (쌍연관)

**정의**: Koestler 이중연상 — **서로 무관한 두 영역의 교차 연결** 로 돌파를 만드는 메커니즘. Montgomery-Dyson pair correlation engine.

**독립 논증**: BLOWUP이 단일 도메인 깊이, BISOCIATION은 **도메인 간 수평 교차**. MEMORY `handoff-bisociation.md` 증빙 (L1 3/4, L2 4/4, L3 1/5, L_meta 3/3).

**근거**: shared/bisociation/unified/ (ouroboros_unified.hexa, phi_ratchet.hexa), cross/, spectra/, breakthroughs.jsonl, pitfalls.jsonl, convergence.json.

### N6 — CONSCIOUSNESS (의식)

**정의**: anima 브릿지 + consciousness_* + law_* + meta_laws_dd64 — Φ 기반 의식 레이어.

**독립 논증**: 다른 축들은 **수학/코드** 축, CONSCIOUSNESS 는 **질적 현상** 축. anima subrepo 와의 브릿지 자체가 독립 자산.

**근거**: shared/consciousness/, anima_bridge live laws=2395 (nexus.json P1 ATLAS task 증빙), consciousness_bridge.py, meta_laws_dd64.

### N7 — HEXA-LANG (hexa 언어)

**정의**: hexa 언어 자체의 파서·컴파일러·인터프리터·pitfalls·grammar — **nexus 코드 기질의 진화 축**.

**독립 논증**: 진화는 **데이터/상태 진화**, HEXA-LANG 은 **언어 자체 진화** (self-host 컴파일러). 유저는 hexa-lang 메인테이너 (MEMORY u-user-role.md).

**근거**: shared/hexa/ (speed_ideas, hexa_to_anima_*, porting_log), shared/hexa-lang/, hexa_pitfalls_log.jsonl, config/hexa_grammar.jsonl (pitfalls P1~P5), MEMORY hexa_dir_builtins / feedback_hexa_pitfalls / feedback-hexa-porting-patterns.

### N8 — DSE (발견 공간 탐색)

**정의**: Discovery Space Exploration 프레임워크 자체 — domain × level × candidate 탐색 격자.

**독립 논증**: DISCOVERY 가 **결과** 라면 DSE 는 **탐색 방법론**. ai-native DSE (5 levels × 6 candidates × n=6) MEMORY project_ai_native_dse_domain.md 증빙.

**근거**: shared/dse/ (dse_cross_*, dse_domains/, dse_graph_3d, dse_joint_results, domains/).

---

## 5. 기각/보류

| 후보 | 상태 | 사유 |
|------|------|------|
| BREAKTHROUGH (C5) | 보류→R2 | BLOWUP과 90% 중첩 가능성, R2 에서 독립 여부 재검 |
| PUBLICATION (C9) | 보류→R2 | 범위 0.10 너무 낮음, paper 메타만으로 축 무게 부족 |
| SINGULARITY (C10) | 기각 | 진화와 60% 중복 — 특이점 기록은 진화의 이정표에 속함 |
| GROWTH (C12) | 기각 | 진화와 75% 중복 — growth_strategies/acceleration은 SELF-EVOLUTION 서브 |
| LOCKDOWN (C13) | 보류→R2 | GOVERNANCE 흡수 vs. 독립 경계 모호 |
| CONVERGENCE (C14) | 기각 | 진화 수렴 산물 — SELF-EVOLUTION 내부 |
| EXECUTION-INFRA (C15) | 보류→R2 | 운영 인프라 (cl 런처 등) — 축 vs. 지원 경계 |

---

## 6. R1 누적 축

**누적 10 개**: SELF-EVOLUTION, ATLAS, HARNESS, GOVERNANCE, DISCOVERY, BLOWUP, BISOCIATION, CONSCIOUSNESS, HEXA-LANG, DSE.

---

## 7. 고갈 지수

- 풀 후보 수: 15
- 신규 확정: 7 (C1~C4, C6~C8, C11)
- 신규 확정 비율: 7/15 = **46.7%**
- 고갈 지수 (1 - 46.7%) = **53.3%**
- 탐색 범위: shared/ 25 카테고리 중 17 개 매핑 완료 (8개 축에 귀속), 8 개 잔여/보류

## 8. 다음 라운드 필요: YES

잔여 4 보류 후보 + 미탐색 subsurface (harness/ 151 파일 내부 세분, rules/H-* 메타룰 개별 축화, n6/math_atlas vs atlas 분화, anima-physics 소서브 등) 존재. R2 진행.
