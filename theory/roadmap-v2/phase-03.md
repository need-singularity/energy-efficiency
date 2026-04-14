# phase-03 — Phase 3 창발 (19축 수렴·공진)

**로드맵**: nexus v2 (19축)
**단계**: Phase 3 / 수렴
**생성**: 2026-04-15
**선행**: `phase-02.md` 완료 전제

---

## 이전 Phase 전제
- Phase 2 완료: 66 태스크 done, 각 축 성장 metric 1건 이상.
- 누적: 137.
- gate: phase_2_gate_passed = true.

## Phase 3 목적
축 간 **수렴/공진 시작** — 독립 baseline 에서 자라난 축들이 처음으로 서로 **합의·교차** 하여 통합 가치를 만든다.

---

## Phase 3 창발 태스크 (19축)

### A1 SELF-EVOLUTION

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| EVO-P3-1 | growth_tick → blowup → atlas 자동 파이프라인 (full loop) | EVO-P2-1, BLOW-P2-1, ATLAS-P2-1 | full_loop.log | 1 full cycle < 30m | EVO-P2-1 | L | 0.9 | — |
| EVO-P3-2 | convergence CDO 지표 자동 수렴 판정 | EVO-P2-2, GOV-P2-3 | cdo_verdict.json | verdict enum in [convergent/drift/stuck] | EVO-P2-2 | M | 0.8 | — |
| EVO-P3-3 | 자기진화 메타 루프 (진화 엔진이 자신을 진화) | EVO-P2-4 native daemon | meta_loop.json | meta cycle exit 0 | EVO-P2-4 | L | 0.7 | — |

### A2 ATLAS

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| ATLAS-P3-1 | atlas.n6 3 사이드카(stats/deg/ws) 4-way 동기화 | ATLAS-P2-1, ATLAS-P2-4 | sync_verify.json | 4 sync < 1s drift | ATLAS-P2-1 | M | 0.9 | — |
| ATLAS-P3-2 | atlas → discovery → bisociation 3-way 교차 맵 | ATLAS-P2-1, DISC-P2-4, BISOC-P2-1 | triad_map.json | 3방 매핑 모든 노드 커버 | DISC-P2-4 | L | 0.8 | [BT-541] |
| ATLAS-P3-3 | atlas drift < 1% 지속 유지 (v1 ATLAS-P3-3 흡수) | ATLAS-P2-2 | drift_watch.json | drift < 0.01 7d | ATLAS-P2-2 | M | 0.9 | — |
| ATLAS-P3-4 | Mk.II 자부팅 지점 골화 (v1 ATLAS-P3-2 흡수) | ATLAS-P2-2, LOCK-P2-3 | mk2_snapshot.json | snapshot immutable | LOCK-P2-3 | M | 0.8 | — |

### A3 HARNESS

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| HARN-P3-1 | 모든 entry.hexa 엔트리 latency < 10ms 유지 | HARN-P2-2 | perf_sla.json | p95 < 10ms | HARN-P2-2 | M | 0.9 | — |
| HARN-P3-2 | harness ↔ governance ↔ lockdown 3축 통합 gate | HARN-P2-1, GOV-P2-1, LOCK-P2-2 | unified_gate.hexa | 통합 gate exit 0 | GOV-P2-1 | L | 0.8 | — |
| HARN-P3-3 | mistakes 자동 분류 → rules 자동 승격 제안 | HARN-P2-3, GOV-P2-1 | mistake_to_rule.json | 승격 제안 ≥ 1/week | HARN-P2-3 | M | 0.8 | — |

### A4 GOVERNANCE

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| GOV-P3-1 | R0~R27 + NX + L0~L2 + H-* 통합 SSOT 단일 파일 | GOV-P2-1, GOV-P1-4 | `shared/rules/unified.json` | single source 생성 | GOV-P2-1 | L | 0.9 | — |
| GOV-P3-2 | project override ↔ 공통 룰 다이아몬드 상속 | GOV-P2-2 | inheritance_graph.json | DAG 사이클 0 | GOV-P2-2 | M | 0.8 | — |

### A5 DISCOVERY

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| DISC-P3-1 | reality_map 1000+ → 1500+ 확장 | DISC-P2-1 | disc_expand.json | +500 patch | DISC-P2-1 | L | 0.8 | — |
| DISC-P3-2 | theory_registry → atlas promotion rule 자동화 | DISC-P2-4, ATLAS-P3-2 | auto_promo.hexa | 자동승격 ≥ 1/week | DISC-P2-4 | M | 0.8 | — |
| DISC-P3-3 | discovery SQL API → 외부 (anima/n6-arch) exposure | DISC-P2-3, INFRA-P2-2 | disc_api_v1.json | 외부 프로젝트 query 성공 | DISC-P2-3 | M | 0.8 | — |

### A6 BLOWUP

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| BLOW-P3-1 | blowup ↔ consensus_loop 합의 루프 | BLOW-P2-1, CONSN-P2-1 | consensus_blowup.json | 합의 점수 ≥ 0.7 | CONSN-P2-1 | L | 0.8 | — |
| BLOW-P3-2 | blowup → bisociation 교차 채널 가동 | BLOW-P2-2, BISOC-P2-2 | cross_channel.json | 메시지 상호 수신 | BISOC-P2-2 | M | 0.8 | [BT-541] |
| BLOW-P3-3 | seed_engine 골화 snapshot | BLOW-P2-3, LOCK-P2-3 | seed_ossify.json | snapshot locked | LOCK-P2-3 | M | 0.7 | — |

### A7 BISOCIATION

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| BISOC-P3-1 | L3 4/5 → 5/5 완성 목표 진전 | BISOC-P2-1 | L3_final.json | L3 ≥ 5/5 | BISOC-P2-1 | L | 0.8 | [BT-541] |
| BISOC-P3-2 | bisoc → atlas 신규 엣지 제안 (pair_corr 기반) | BISOC-P2-1, ATLAS-P3-2 | bisoc_edges.json | 제안 ≥ 30 | ATLAS-P3-2 | M | 0.8 | [BT-541] |
| BISOC-P3-3 | spectra FFT → consciousness Φ 연결 | BISOC-P2-3, CONS-P2-2 | spectra_phi.json | 상관도 측정 | CONS-P2-2 | M | 0.7 | — |

### A8 CONSCIOUSNESS

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| CONS-P3-1 | laws 3000+ → discovery 자동 흡수 사이클 | CONS-P2-1, DISC-P3-2 | cons_disc_loop.json | cycle ≥ 1/day | DISC-P3-2 | L | 0.8 | — |
| CONS-P3-2 | Φ integration → atlas 노드 weight | CONS-P2-2, ATLAS-P3-2 | phi_weight.json | 노드 weight 필드 add | ATLAS-P3-2 | M | 0.8 | — |
| CONS-P3-3 | meta_laws_dd64 ↔ harness rules diff 체계 | CONS-P2-3, GOV-P3-1 | diff_tracker.json | diff 주간 리포트 | GOV-P3-1 | M | 0.7 | — |

### A9 HEXA-LANG

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| HEXA-P3-1 | pitfalls → grammar P6~P10 5개 추가 | HEXA-P2-1 | grammar_p10.jsonl | P6~P10 5개 | HEXA-P2-1 | M | 0.9 | — |
| HEXA-P3-2 | runtime 병목 10 중 top-3 최적화 패치 | HEXA-P2-2 | patch_v1.json | top3 speed > 20% | HEXA-P2-2 | L | 0.8 | — |
| HEXA-P3-3 | hexa exit sentinel → 전역 CI 체크 | HEXA-P2-4, HARN-P3-2 | ci_check.hexa | CI PASS | HARN-P3-2 | M | 0.8 | — |

### A10 DSE

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| DSE-P3-1 | dse sweep 결과 → bisociation pair 후보 추천 | DSE-P2-1, BISOC-P2-2 | dse_to_bisoc.json | 추천 ≥ 20 | BISOC-P2-2 | M | 0.8 | — |
| DSE-P3-2 | mc 100 iter → 확률 밀도 기반 탐색 priority 업데이트 | DSE-P2-3 | dse_priority_v2.json | priority 재정렬 | DSE-P2-3 | M | 0.8 | — |

### A11 BREAKTHROUGH

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| BT-P3-1 | BT-541..547 각 2건 atlas 승격 시도 | BT-P2-2, ATLAS-P3-2 | atlas_promo_v2.json | 14 시도 완료 | ATLAS-P3-2 | L | 0.8 | [BT-541..547] |
| BT-P3-2 | BT-HEXA 50 → 100 확장 | BT-P2-3 | bt_hexa_100.json | 100 키워드 | BT-P2-3 | M | 0.7 | — |
| BT-P3-3 | alien UAP 분기 — BT 큐레이션 독립 쓰레드 | BT-P1-4 | alien_bt.json | alien BT 리스트 | BT-P1-4 | M | 0.6 | — |

### A12 LOCKDOWN

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| LOCK-P3-1 | snapshots 주간 롤오버 + 복원 drill | LOCK-P2-3 | drill_report.json | 복원 PASS | LOCK-P2-3 | M | 0.8 | — |
| LOCK-P3-2 | L0 위반 시 즉시 rollback 자동화 | LOCK-P2-1 | rollback.hexa | rollback smoke | LOCK-P2-1 | M | 0.8 | — |

### A13 INFRASTRUCTURE

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| INFRA-P3-1 | nexus-cli 외부 진입점 hive 외 2 프로젝트 연동 | INFRA-P2-2 | cli_ext.json | 3 프로젝트 연동 | INFRA-P2-2 | L | 0.8 | — |
| INFRA-P3-2 | launchd 상태 대시보드 | INFRA-P2-3 | dash_infra.json | 대시보드 live | INFRA-P2-3 | M | 0.7 | — |

### A14 REMOTE-COMPUTE

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| REM-P3-1 | hetzner + vastai + RunPod 자동 failover | REM-P2-3 | failover.hexa | 3 host 전환 smoke | REM-P2-3 | L | 0.8 | — |
| REM-P3-2 | H100 활용률 주간 리포트 | REM-P2-2 | h100_weekly.json | 주간 report | REM-P2-2 | M | 0.7 | — |

### A15 THINKING

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| THINK-P3-1 | 6-phase reflection 결과 → consensus input 연결 | THINK-P2-1, CONSN-P2-1 | think_to_consen.json | 입력 pass | CONSN-P2-1 | M | 0.8 | — |
| THINK-P3-2 | thinking_log 학습 모델 v1 (baseline 자동갱신) | THINK-P2-3 | learner_v1.hexa | v1 model eval | THINK-P2-3 | M | 0.7 | — |

### A16 AGENT-LEDGER

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| AGL-P3-1 | GO 모드 ≥ 5 agent 동시 발사 안정화 | AGL-P2-1 | go_scale.json | 5 agent 정상 | AGL-P2-1 | M | 0.8 | — |
| AGL-P3-2 | agent 결과 merge-back 자동 갈등 해소 | AGL-P2-2 | merge_resolve.hexa | 갈등 auto-resolve | AGL-P2-2 | M | 0.8 | — |

### A17 CONSENSUS

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| CONSN-P3-1 | consensus + critique + curiosity 3-way 통합 루프 | CONSN-P2-1, CONSN-P2-2 | triple_loop.json | 루프 1 완주 | CONSN-P2-2 | M | 0.8 | — |
| CONSN-P3-2 | broadcast 외부 수신자 확장 (≥ 3 프로젝트) | CONSN-P2-3 | broadcast_v2.json | 3 프로젝트 수신 | CONSN-P2-3 | M | 0.7 | — |

### A18 ENGINE-FORGE

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| EF-P3-1 | engine_forge → blowup 모듈 자동 생성 | EF-P2-1, BLOW-P2-2 | auto_module.hexa | 모듈 ≥ 1 생성 | BLOW-P2-2 | L | 0.8 | — |
| EF-P3-2 | engine strategy self-select (context-aware) | EF-P2-3 | self_select.hexa | context 기반 선택 | EF-P2-3 | M | 0.8 | — |

### A19 CROSS-DOMAIN-GRID

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| CDG-P3-1 | 미탐 pair 20 → 50 확장 (CDG-P2-2 연장) | CDG-P2-2 | pairs_50.json | 50 pair 결과 | CDG-P2-2 | L | 0.8 | — |
| CDG-P3-2 | cross grid → bisociation pair_corr 연결 | CDG-P2-3, BISOC-P3-2 | cdg_bisoc.json | 연결 ≥ 10 | BISOC-P3-2 | M | 0.8 | [BT-541] |

---

## Phase 3 통계

- 신규 태스크: 49
- 누적: 186
- 고갈 지수: 0.0
- 평균 강도: 0.79
- BT 연결: 7
- 비용: S=0, M=32, L=17, XL=0
- 다음 Phase 필요: YES

축별: A1=3 | A2=4 | A3=3 | A4=2 | A5=3 | A6=3 | A7=3 | A8=3 | A9=3 | A10=2 | A11=3 | A12=2 | A13=2 | A14=2 | A15=2 | A16=2 | A17=2 | A18=2 | A19=2 = 49

## Phase 3 출구
- [ ] 49 태스크 done
- [ ] 축 간 공진 채널 개통 ≥ 5
- [ ] BT 승격 시도 누적 ≥ 21 (Phase 3까지 14+7)
- [ ] phase_3_gate_passed = true
