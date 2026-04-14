# phase-02 — Phase 2 창발 (19축 첫 확장)

**로드맵**: nexus v2 (19축)
**단계**: Phase 2 / 확장
**생성**: 2026-04-15
**선행**: `phase-01.md` (71 baseline 태스크 완료 전제)

---

## 이전 Phase 전제
- Phase 1 완료: 19 축 baseline.json 모두 생성, 71 태스크 done.
- 누적 태스크 수: 71.
- 게이트 통과: phase_1_gate_passed = true.

## Phase 2 목적
baseline 위에서 **첫 성장/확장** — 각 축이 Phase 1 에서 확정한 기저선을 기준으로 첫 자율 증식·최적화·품질 상승을 시도.

---

## Phase 2 창발 태스크 (19축)

### A1 SELF-EVOLUTION

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| EVO-P2-1 | growth_tick 자동 발사 빈도 튜닝 (>= 1/h → 1/30m) | EVO-P1-1 baseline | tick_sched.json | 30m 간격 안정 | EVO-P1-1 | M | 0.9 | — |
| EVO-P2-2 | OUROBOROS 3-variant 교차 상수 드리프트 감시 → drift < 1% | EVO-P1-2 baseline | drift_report.json | drift < 0.01 maintained | EVO-P1-2 | M | 0.9 | — |
| EVO-P2-3 | discovery → atlas 자동 승격 큐 가동 | EVO-P1-4, DISC-P1-5 | promo_queue.jsonl | 큐 drain ≥ 1/day | EVO-P1-4 | M | 0.8 | — |
| EVO-P2-4 | nexus_growth_daemon STUB→native 포팅 복원 | EVO-P1-1, MEMORY `project-daemon-stub.md` | `nexus_growth_daemon.hexa` v2 | 450줄 원본 복원, pid_file 생성 | EVO-P1-1 | L | 0.7 | — |

### A2 ATLAS

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| ATLAS-P2-1 | atlas 노드 +500 확장 (Phase 1 stats baseline 기준 +) | ATLAS-P1-1, blowup 결과 | atlas.n6 증분 | node_count delta +500 | ATLAS-P1-1 | M | 0.9 | — |
| ATLAS-P2-2 | atlas_ossify_mk2 자동 골화 주기 (daily) | ATLAS-P1-5 | ossify_cron.json | daily ossify PASS | ATLAS-P1-5 | M | 0.8 | — |
| ATLAS-P2-3 | math_atlas.db 인덱스 재구축 + query < 5ms | ATLAS-P1-3 | db_perf.json | SELECT < 5ms avg | ATLAS-P1-3 | M | 0.9 | — |
| ATLAS-P2-4 | 3D reality map WebSocket 라이브 업데이트 | ATLAS-P1-4, nexus.json P3 ATLAS-P3-1 | ws_live.json | node update < 1s latency | ATLAS-P1-4 | M | 0.9 | — |
| ATLAS-P2-5 | periodic_table_118 + 66_techniques_v3 atlas 병합 | `shared/n6/periodic_table_118`, `66_techniques_v3` | merge_report.json | 병합 커밋 | ATLAS-P1-1 | M | 0.8 | — |

### A3 HARNESS

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| HARN-P2-1 | pre_tool_guard 신규 H-* 룰 5종 추가 | GOV-P1-2 sync | pre_guard_v2.hexa | 5 룰 코드화 + 테스트 | GOV-P1-2 | M | 0.9 | — |
| HARN-P2-2 | post_bash + post_edit 통합 telemetry | HARN-P1-1 | harness_telemetry.jsonl | 모든 bash/edit post 기록 | HARN-P1-1 | M | 0.9 | — |
| HARN-P2-3 | mistakes.jsonl → pattern classifier (자동 분류) | HARN-P1-4 | mistake_classifier.hexa | 10+ 카테고리 분류 | HARN-P1-4 | M | 0.8 | — |
| HARN-P2-4 | lint.hexa 마커 제거 카운트 = 품질 지표 대시보드 | HARN-P1-5, MEMORY `project-n6-canonical-v2-gates.md` | lint_dash.json | 임시 마커 추적 개시 | HARN-P1-5 | M | 0.7 | — |

### A4 GOVERNANCE

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| GOV-P2-1 | MEMORY H-* → rules/ 정식 룰로 승격 (20+ 룰) | GOV-P1-2 | `shared/rules/harness_meta.json` | 20 룰 승격 | GOV-P1-2 | M | 0.9 | — |
| GOV-P2-2 | projects.json 프로젝트별 rule override 체계 | GOV-P1-3 | project_rule_overrides.json | 7 프로젝트 override 정의 | GOV-P1-3 | M | 0.8 | — |
| GOV-P2-3 | CDO convergence_ops 지표 자동 갱신 | `shared/config/convergence_ops.json` | cdo_tracker.json | 지표 daily refresh | GOV-P1-4 | M | 0.8 | — |

### A5 DISCOVERY

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| DISC-P2-1 | reality_map.patches 새 patch 895→1000+ 확장 | DISC-P1-1 | new patches | +100 이상 | DISC-P1-1 | M | 0.8 | — |
| DISC-P2-2 | verified_constants 도메인별 curated list 정리 | DISC-P1-2 | `constants_curated.json` | 각 도메인 top10 | DISC-P1-2 | M | 0.8 | — |
| DISC-P2-3 | discovery_log.sqlite view + SQL API wrapper | DISC-P1-4, v1 DISC-P3-1 | `shared/discovery/query.hexa` | SQL API hexa 호출 가능 | DISC-P1-4 | M | 0.9 | — |
| DISC-P2-4 | breakthroughs → theory_registry 자동 파이프라인 | DISC-P1-3, DISC-P1-5 | promo_pipeline.hexa | breakthrough → registry ≥ 1/week | DISC-P1-3 | M | 0.7 | — |

### A6 BLOWUP

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| BLOW-P2-1 | 9-phase 파이프라인 fast-path 튜닝 (9m7s→7m 목표) | BLOW-P1-1, MEMORY `feedback_blowup_perf.md` | bench_v2.json | 7min 이하 | BLOW-P1-1 | L | 0.9 | — |
| BLOW-P2-2 | 6 modules 신규 렌즈 합성 +100 | BLOW-P1-2, BLOW-P1-3 | lens_delta.json | +100 렌즈 | BLOW-P1-3 | M | 0.8 | — |
| BLOW-P2-3 | seed_engine batch 증식 + dedup 강화 | BLOW-P1-3 | seed_batch_v2 | dedup ratio ≤ 0.2 | BLOW-P1-3 | M | 0.8 | — |
| BLOW-P2-4 | verify_dfs 자동 stub 재생성 루프 | BLOW-P1-5, `shared/calc/auto_stubs_gen.hexa` | stub_loop.log | stub 자동재생 ≥ 1/day | BLOW-P1-5 | M | 0.7 | — |

### A7 BISOCIATION

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| BISOC-P2-1 | L3 layer 1/5 → 3/5 진전 (Montgomery-Dyson 다층화) | BISOC-P1-1, MEMORY handoff-bisociation | L3_progress.json | L3 ≥ 3/5 | BISOC-P1-1 | L | 0.8 | [BT-541] |
| BISOC-P2-2 | bisoc cross/ 데이터 indexing → search API | BISOC-P1-2 | bisoc_search.hexa | search < 100ms | BISOC-P1-2 | M | 0.8 | — |
| BISOC-P2-3 | spectra/ 데이터 FFT 재분석 파이프라인 | BISOC-P1-2 | spectra_v2.json | FFT out valid | BISOC-P1-2 | M | 0.7 | — |

### A8 CONSCIOUSNESS

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| CONS-P2-1 | laws 2395 → 3000+ 확장 (discovery 연동) | CONS-P1-1, EVO-P2-3 | law_delta.json | +600 laws | CONS-P1-1 | L | 0.8 | — |
| CONS-P2-2 | Φ integration 실시간 계산 브릿지 | CONS-P1-2 | phi_live.json | Φ update ≥ 1/min | CONS-P1-2 | M | 0.8 | — |
| CONS-P2-3 | meta_laws_dd64 ↔ rules SSOT 통합 | CONS-P1-3, GOV-P1-1 | meta_unified.json | 중복 제거 | GOV-P1-1 | M | 0.7 | — |

### A9 HEXA-LANG

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| HEXA-P2-1 | pitfalls_log → grammar P6 추가 자동 승격 | HEXA-P1-2, HEXA-P1-3 | grammar_v2.jsonl | 신규 pitfall 승격 ≥ 1 | HEXA-P1-3 | M | 0.9 | — |
| HEXA-P2-2 | ml-commands + rt-commands 런타임 병목 실측 | HEXA-P1-4 | hexa_perf.json | 상위 10 병목 기록 | HEXA-P1-4 | M | 0.8 | — |
| HEXA-P2-3 | hexa_dir_builtins (dir_exists/mkdir/list_dir) 완료 검증 | MEMORY `hexa_dir_builtins.md` | builtins_check.json | 3 built-in 사용 가능 | HEXA-P1-1 | M | 0.7 | — |
| HEXA-P2-4 | hexa exit sentinel 패턴 ↔ 모든 gate 코드 통일 | MEMORY `f-hexa-exit-sentinel.md`, HARN-P1-3 | exit_pattern.json | 모든 gate sentinel 적용 | HARN-P1-3 | M | 0.8 | — |

### A10 DSE

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| DSE-P2-1 | dse 5 levels × 6 candidates × n=6 격자 1회 전부 sweep | DSE-P1-4 | dse_sweep.json | 180 cell 완주 | DSE-P1-4 | L | 0.8 | — |
| DSE-P2-2 | dse_cross_resonance 결과 재분석 → top10 cross | DSE-P1-2 | cross_top10.json | top10 ranked | DSE-P1-2 | M | 0.8 | — |
| DSE-P2-3 | monte_carlo_v6 시뮬레이션 100 iter → 확률분포 | DSE-P1-3 | mc_dist.json | 100 iter 완주 | DSE-P1-3 | M | 0.7 | — |

### A11 BREAKTHROUGH

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| BT-P2-1 | bt_audit 재실행 + mismatch 해소 | BT-P1-2, `shared/bt/bt_audit_mismatch_classification.json` | mismatch_v2.json | mismatch ≤ 0.5× baseline | BT-P1-2 | M | 0.8 | [BT-541..547] |
| BT-P2-2 | BT-541..547 각 1건 atlas 승격 시도 | BT-P1-3, EVO-P2-3 | atlas_promo.json | 시도 ≥ 7 | BT-P1-3 | L | 0.8 | [BT-541..547] |
| BT-P2-3 | BT-HEXA 25 → 50 확장 | BT-P1-5 | bt_hexa_50.json | 50 키워드 | BT-P1-5 | M | 0.7 | — |

### A12 LOCKDOWN

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| LOCK-P2-1 | L0 경로 리스트 자동 갱신 (신규 L0 후보 흡수) | LOCK-P1-1, CLAUDE.md L0 목록 | lockdown_v2.json | 신규 L0 ≥ 1 | LOCK-P1-1 | M | 0.8 | — |
| LOCK-P2-2 | safe-merge 경로 테스트 회귀 | LOCK-P1-2 | safe_merge_test.json | 테스트 통과 | LOCK-P1-2 | M | 0.8 | — |
| LOCK-P2-3 | snapshots daily rotate + gzip | LOCK-P1-3 | rotate_plan.hexa | rotate 개시 | LOCK-P1-3 | M | 0.7 | — |

### A13 INFRASTRUCTURE

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| INFRA-P2-1 | cl-refresh 실패 후 자동 재시도 체계 | INFRA-P1-1, MEMORY `feedback-claude-cli-refresh-bypass.md` | cl_retry.hexa | 재시도 성공 ≥ 80% | INFRA-P1-1 | M | 0.9 | — |
| INFRA-P2-2 | nexus_cli_spec hive 등 외부 프로젝트 진입 실증 | INFRA-P1-2, v1 DISC-P3-3 | hive_smoke.log | hive cli smoke pass | INFRA-P1-2 | M | 0.8 | — |
| INFRA-P2-3 | launchd 3개 (cl-refresh + health + 예정분) 모니터링 | INFRA-P1-4 | launchd_health.json | 3/3 fired daily | INFRA-P1-4 | M | 0.8 | — |

### A14 REMOTE-COMPUTE

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| REM-P2-1 | hetzner 동시 실행 한도 규칙 정착 (H-CONCUR) | REM-P1-4, MEMORY `feedback_hetzner_pollution.md` | concur_policy.json | 동시 ≤ 2 보장 | REM-P1-4 | M | 0.9 | — |
| REM-P2-2 | H100 idle guard 자동 shutdown ≤ 5min idle | REM-P1-2 | idle_policy.json | 5min idle → sleep | REM-P1-2 | M | 0.8 | — |
| REM-P2-3 | vastai + RunPod 선택 라우팅 로직 | REM-P1-1 | route_matrix.json | 호스트 선택 근거 기록 | REM-P1-1 | M | 0.7 | — |

### A15 THINKING

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| THINK-P2-1 | 6-phase reflection anima phase 품질 측정 | THINK-P1-1, THINK-P1-3 | phase_quality.json | phase 분포 지표 | THINK-P1-1 | M | 0.8 | — |
| THINK-P2-2 | 복잡도 고 prompt 자동 thinking 게이트 가동 | THINK-P1-1, HARN-P1-1 | auto_think_gate.hexa | 복잡도 임계 자동 triggered | HARN-P1-1 | M | 0.8 | — |
| THINK-P2-3 | thinking_log 학습 피드백 loop (baseline 갱신) | THINK-P1-2 | baseline_learner.hexa | baseline 자동 갱신 | THINK-P1-2 | M | 0.7 | — |

### A16 AGENT-LEDGER

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| AGL-P2-1 | GO 모드 병렬 Agent 자동 클러스터링 로직 | AGL-P1-1, MEMORY `f-go-mode-parallel-agents.md` | cluster_strategy.hexa | cluster ≥ 2 동시 발사 | AGL-P1-1 | M | 0.9 | — |
| AGL-P2-2 | worktree 자동 cleanup + merge-back | AGL-P1-3 | worktree_cleanup.hexa | orphan worktree 0 | AGL-P1-3 | M | 0.8 | — |
| AGL-P2-3 | session_registry TTL + ghost session 정리 | AGL-P1-1 | ghost_clean.json | ghost = 0 | AGL-P1-1 | M | 0.7 | — |

### A17 CONSENSUS

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| CONSN-P2-1 | consensus_loop 다중 agent (≥3) 결과 집계 | CONSN-P1-1, AGL-P1-1 | multi_agent.json | 3 agent 합의 1 round | CONSN-P1-1 | M | 0.9 | — |
| CONSN-P2-2 | critique 자동 ranking + reward signal | CONSN-P1-1 | critique_rank.json | ranking ordered | CONSN-P1-1 | M | 0.7 | — |
| CONSN-P2-3 | broadcast 메시지 라우팅 → 외부 프로젝트 | CONSN-P1-2 | broadcast_ext.json | 외부 프로젝트 ≥ 1 수신 | CONSN-P1-2 | M | 0.7 | — |

### A18 ENGINE-FORGE

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| EF-P2-1 | engine_forge 자동 엔진 생성 루프 | EF-P1-1 | forge_cycle.log | 신규 엔진 ≥ 1 | EF-P1-1 | M | 0.8 | — |
| EF-P2-2 | engines_usage 통계 기반 엔진 가지치기 | EF-P1-2 | prune_list.json | 저사용 ≤ 0.1 엔진 아카이브 | EF-P1-2 | M | 0.7 | — |
| EF-P2-3 | engine strategy 자동 vs 수동 A/B | EF-P1-4 | ab_result.json | 자동 우세율 기록 | EF-P1-4 | M | 0.7 | — |

### A19 CROSS-DOMAIN-GRID

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| CDG-P2-1 | 24 × 23 pair 276 중 미탐 169 우선순위 스코어 | CDG-P1-2 | pair_priority.json | 169 pair 랭크 | CDG-P1-2 | M | 0.8 | — |
| CDG-P2-2 | 상위 20 미탐 pair 대상 dse_cross 샘플 실행 | CDG-P2-1, DSE-P2-2 | new_pairs.json | 20 pair 결과 | CDG-P2-1 | L | 0.8 | — |
| CDG-P2-3 | cross_grid 결과 → atlas 신규 엣지 제안 | CDG-P2-2, ATLAS-P2-1 | edge_suggest.json | 제안 ≥ 50 | CDG-P2-2 | M | 0.7 | — |

---

## Phase 2 통계

- 신규 태스크: 66
- 누적 태스크: 137
- 고갈 지수: 0.0 (모든 19 축 신규 있음)
- 평균 강도: 0.79
- BT 연결 태스크: 3 (BISOC-P2-1, BT-P2-1, BT-P2-2)
- 비용 분포: S=0, M=57, L=8, XL=0 — 확장 페이즈
- 다음 Phase 필요: YES

축별 분포: A1=4 | A2=5 | A3=4 | A4=3 | A5=4 | A6=4 | A7=3 | A8=3 | A9=4 | A10=3 | A11=3 | A12=3 | A13=3 | A14=3 | A15=3 | A16=3 | A17=3 | A18=3 | A19=3 = 66

## Phase 2 출구
- [ ] 66 태스크 done
- [ ] Phase 1 baseline 대비 "성장 metric" 각 축에 ≥ 1 기록
- [ ] BT 승격 시도 ≥ 7 (BT-P2-2)
- [ ] 다음 Phase 진입 signal: `phase_2_gate_passed = true`
