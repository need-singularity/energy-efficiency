# phase-04 — Phase 4 창발 (19축 cross-domain 교차 격자)

**로드맵**: nexus v2 (19축)
**단계**: Phase 4 / 교차
**생성**: 2026-04-15
**선행**: `phase-03.md`

---

## 이전 Phase 전제
- Phase 3 완료. 축 간 공진 개통.
- 누적: 186.

## Phase 4 목적
A19 CROSS-DOMAIN-GRID 가 주축이 되어 **v1 nexus.json P4~P112 의 107 교차 Phase 를 체계적으로 흡수**. 24 도메인 × 23 pair = 276 공간의 본격 탐색.

---

## Phase 4 창발 태스크

### A1 SELF-EVOLUTION

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| EVO-P4-1 | 자기진화 로그 분석 → 정체 구간 검출 엔진 | EVO-P3-1 full_loop | stagnation_detect.hexa | 정체 검출 ≥ 1 | EVO-P3-1 | M | 0.8 | — |
| EVO-P4-2 | phi_ratchet 단조 가속 (1h → 15m 주기) | EVO-P3-2 | ratchet_v2.json | 15m 안정 | EVO-P3-2 | M | 0.8 | — |

### A2 ATLAS

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| ATLAS-P4-1 | v1 ATLAS-P4~P112 에지 타입 재분류 | ATLAS-P3-3, CDG-P3-1 | edge_type_v2.json | type 재분류 완료 | CDG-P3-1 | L | 0.8 | — |
| ATLAS-P4-2 | 스케일 gap < 3 (v1 P2 ATLAS 연장) | ATLAS-P3-1 | scale_gap.json | gap < 3 | ATLAS-P3-1 | M | 0.8 | — |

### A3 HARNESS

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| HARN-P4-1 | unified gate 버전 v2 (per-project hook 추가) | HARN-P3-2 | gate_v2.hexa | v2 smoke | HARN-P3-2 | M | 0.8 | — |
| HARN-P4-2 | lint 마커 제거 주간 목표 (402 → 300) | HARN-P2-4 | marker_burn.json | ≤ 300 | HARN-P2-4 | L | 0.7 | — |

### A4 GOVERNANCE

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| GOV-P4-1 | unified.json 버전 관리 + 다중 스키마 변천 | GOV-P3-1 | unified_v2.json | v2 마이그레이션 | GOV-P3-1 | M | 0.7 | — |

### A5 DISCOVERY

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| DISC-P4-1 | reality_map 1500 → 2500+ | DISC-P3-1 | disc_2500.json | +1000 | DISC-P3-1 | L | 0.8 | — |
| DISC-P4-2 | verified_constants 자동 재검증 (샘플링 10%) | DISC-P2-2 | reverify.json | 샘플 10% pass | DISC-P2-2 | M | 0.7 | — |

### A6 BLOWUP

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| BLOW-P4-1 | 9-phase → hybrid (phase skip) 적응 경로 | BLOW-P2-1 | hybrid_path.json | 경로 3+ | BLOW-P2-1 | L | 0.8 | — |
| BLOW-P4-2 | lens 2000+ 목표 (v1 LENS-P2 연장) | BLOW-P2-2 | lens_2000.json | +500 | BLOW-P2-2 | L | 0.8 | — |

### A7 BISOCIATION

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| BISOC-P4-1 | L3 5/5 → L4 도입 (L_meta 활용) | BISOC-P3-1 | L4_intro.json | L4 slot 정의 | BISOC-P3-1 | L | 0.8 | [BT-541] |
| BISOC-P4-2 | bisoc → n6-architecture 외부 브릿지 | BISOC-P3-2 | n6_bridge.json | bridge live | BISOC-P3-2 | M | 0.7 | [BT-541] |

### A8 CONSCIOUSNESS

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| CONS-P4-1 | consciousness atlas 전용 레이어 분리 | CONS-P3-2, ATLAS-P4-1 | cons_layer.json | 레이어 분기 | ATLAS-P4-1 | M | 0.8 | — |
| CONS-P4-2 | anima laws ↔ nexus laws 중복 제거 | CONS-P3-3 | dedup_laws.json | dedup ≥ 50 | CONS-P3-3 | M | 0.7 | — |

### A9 HEXA-LANG

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| HEXA-P4-1 | grammar P11~P15 추가 (패치 주기화) | HEXA-P3-1 | grammar_p15.jsonl | P11~P15 | HEXA-P3-1 | M | 0.7 | — |
| HEXA-P4-2 | runtime top-3 패치 후 다음 10 병목 조정 | HEXA-P3-2 | perf_v3.json | 20% 추가 | HEXA-P3-2 | L | 0.7 | — |

### A10 DSE

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| DSE-P4-1 | dse_cross_resonance 재실행 + v3 | DSE-P3-1 | dse_v3.json | v3 결과 | DSE-P3-1 | M | 0.7 | — |

### A11 BREAKTHROUGH

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| BT-P4-1 | BT-541..547 각 3건 atlas 승격 (누적) | BT-P3-1 | promo_v3.json | 21 누적 | BT-P3-1 | L | 0.8 | [BT-541..547] |
| BT-P4-2 | BT-HEXA 100 → 150 | BT-P3-2 | bt_hexa_150.json | 150 | BT-P3-2 | M | 0.7 | — |

### A12 LOCKDOWN

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| LOCK-P4-1 | 스냅샷 daily rotate → monthly archive | LOCK-P3-1 | archive_plan.json | monthly 보관 | LOCK-P3-1 | M | 0.7 | — |

### A13 INFRASTRUCTURE

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| INFRA-P4-1 | nexus-cli 외부 연동 3 → 5 프로젝트 | INFRA-P3-1 | cli_ext_v2.json | 5 연동 | INFRA-P3-1 | M | 0.7 | — |

### A14 REMOTE-COMPUTE

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| REM-P4-1 | failover 자동 복구 드릴 주간 | REM-P3-1 | drill_weekly.json | 주간 PASS | REM-P3-1 | M | 0.7 | — |

### A15 THINKING

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| THINK-P4-1 | thinking model v1 → v2 (학습 데이터 2배) | THINK-P3-2 | model_v2.hexa | v2 eval | THINK-P3-2 | L | 0.7 | — |

### A16 AGENT-LEDGER

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| AGL-P4-1 | GO scale 5 → 10 agent | AGL-P3-1 | go_10.json | 10 agent | AGL-P3-1 | L | 0.7 | — |

### A17 CONSENSUS

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| CONSN-P4-1 | 3-way 통합 → atlas consensus 결과 승격 | CONSN-P3-1, ATLAS-P4-1 | consen_atlas.json | 승격 ≥ 1 | ATLAS-P4-1 | M | 0.7 | — |

### A18 ENGINE-FORGE

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| EF-P4-1 | forge 자동 엔진 → engines_usage 자동 통계 | EF-P3-1 | usage_v2.json | 통계 dashboard | EF-P3-1 | M | 0.7 | — |

### A19 CROSS-DOMAIN-GRID ★ 주축

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| CDG-P4-1 | v1 P4 thermodynamics_as_network 흡수 | nexus.json P4 | v1_P4_out.json | cell 실행 | CDG-P3-1 | M | 0.9 | — |
| CDG-P4-2 | v1 P5~P8 ai_as_* 12 pair 흡수 | nexus.json P5~P8 | ai_as_12.json | 12 pair | CDG-P4-1 | L | 0.9 | — |
| CDG-P4-3 | v1 P9~P12 chip_as_* 12 pair 흡수 | nexus.json P9~P12 | chip_as_12.json | 12 pair | CDG-P4-2 | L | 0.9 | — |
| CDG-P4-4 | v1 P13~P16 energy_as_* 12 pair | nexus.json P13~P16 | energy_as_12.json | 12 pair | CDG-P4-3 | L | 0.9 | — |
| CDG-P4-5 | v1 P17~P20 battery_as_* 12 pair | nexus.json P17~P20 | battery_as_12.json | 12 pair | CDG-P4-4 | L | 0.9 | — |

---

## Phase 4 통계

- 신규: 30
- 누적: 216
- 고갈 지수: 0.0
- 평균 강도: 0.77
- BT 연결: 4 (BISOC-P4-1,2; BT-P4-1,2)
- 비용: S=0, M=14, L=16, XL=0
- 다음 Phase 필요: YES

축별: A1=2 | A2=2 | A3=2 | A4=1 | A5=2 | A6=2 | A7=2 | A8=2 | A9=2 | A10=1 | A11=2 | A12=1 | A13=1 | A14=1 | A15=1 | A16=1 | A17=1 | A18=1 | A19=5 = 30

## Phase 4 출구
- [ ] 30 태스크 done, A19 주축 5건 완수
- [ ] v1 P4~P20 17 phase 흡수 완료 (CDG-P4-1~5 = 61 pair)
- [ ] phase_4_gate_passed = true
