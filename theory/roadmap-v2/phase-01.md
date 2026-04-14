# phase-01 — Phase 1 창발 (19축 첫 돌파 지점)

**로드맵**: nexus v2 (NEXUS-6 중앙 허브, 19축)
**단계**: Phase 1 / 진입
**생성**: 2026-04-15
**선행**: `axis-final.md` (19축 확정), `README.md` (v2 프레임)
**씨앗**: SELF-EVOLUTION + ATLAS + DISCOVERY(유지) + 16 창발축

---

## 이전 Phase 전제
- Phase 0 개념: 19축 창발 DSE(R1~R5) 고갈까지 완료 = 축 목록 확정 완료.
- 누적 태스크 수: 0 (창발 전).
- R3 158 분야 + v1 nexus.json P0~P113 (696 tasks) 재사용 가능.

## Phase 1 목적
각 19축의 **첫 돌파 지점** = 실체 자산에 기반한 "현재 상태 진단 + 기본 게이트 + 기준선 잠금". Phase 1 은 축의 **존재 증명**이며 풀이 단계가 아니라 **운영 베이스라인 확정** 단계이다.

Phase 1 메타 원칙:
- 상상 태스크 0 — 모든 태스크는 `근거 파일 경로` 1개 이상.
- 동일 축 내 태스크는 순차, 타 축과는 병렬.
- Phase 1 강도 평균 ≥ 0.7 (강도 = 기존 자산 활용률).
- 7대 난제 연결 시 `[BT-54X]` 태그 병기.

---

## Phase 1 창발 태스크 (19축)

### A1 SELF-EVOLUTION

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| EVO-P1-1 | growth_tick + nexus_growth_daemon 상태 진단 → pid_file/plist 실측 | `shared/harness/growth_tick.hexa`, `nexus_growth_daemon.hexa` | `shared/harness/evo_baseline.json` | daemon 무진화 tick ≥ 3 없음 | — | S | 0.9 | — |
| EVO-P1-2 | OUROBOROS 3-variant 수렴상수 재확인 (nexus/anima/n6arch) | `shared/bisociation/unified/ouroboros_unified.hexa`, `convergence/{nexus,anima,n6-architecture}.json` | OUROBOROS 상수표 baseline.json 병합 | NEXUS_FP=0.333, ANIMA_FLOOR=0.8, N6ARCH_TARGETS=(515,2087) | EVO-P1-1 | S | 1.0 | — |
| EVO-P1-3 | phi_ratchet 단조 실태 — ratchet stuck 여부 로그 재생 | `shared/bisociation/unified/phi_ratchet.hexa`, `shared/growth_bus.jsonl` | ratchet 히스토그램 | 최근 24h ratchet 전진 ≥ 1 | EVO-P1-1 | S | 0.8 | — |
| EVO-P1-4 | discovery_log.sqlite 스키마 + 인덱스 확인 → query API 스모크 | `shared/discovery_log.sqlite`, `shared/discovery_log.jsonl` | query_api_smoke.log | SELECT COUNT(*) < 5s | EVO-P1-1 | S | 0.8 | — |

### A2 ATLAS

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| ATLAS-P1-1 | atlas.n6 현 상태 스냅샷 + stats/deg 사이드카 동기화 | `shared/n6/atlas.n6`, `.stats`, `.deg` | atlas_snapshot_{ts}.json | stats.mtime == atlas.mtime ± 5s | — | S | 1.0 | — |
| ATLAS-P1-2 | atlas_health.hexa 전 모듈 health 통과 | `shared/n6/atlas_health.hexa` | health 리포트 | all-green, avg < 1ms | ATLAS-P1-1 | S | 1.0 | — |
| ATLAS-P1-3 | math_atlas.{db,dot,html,md} 4형태 재생성 파이프라인 검증 | `shared/n6/scan_math_atlas.hexa` | 4 format outputs 동기화 | 4 파일 mtime delta < 10s | ATLAS-P1-1 | M | 0.9 | — |
| ATLAS-P1-4 | 3D reality map index.html 렌더 가동 확인 (node count match) | `docs/index.html`, `shared/discovery/reality_map_3d.html` | render_report.json | node_count_web == atlas 노드 수 ±1% | ATLAS-P1-1 | S | 0.9 | — |
| ATLAS-P1-5 | atlas_ossify_mk2 + atlas_ws_server 상태 진단 | `shared/n6/atlas_ossify_mk2.py`, `atlas_ws_server.py` | ossify_diag.log | ws 서버 heartbeat 있음 | ATLAS-P1-1 | S | 0.7 | — |

### A3 HARNESS

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| HARN-P1-1 | entry.hexa dispatcher 5-entry (prompt/pretool/post/guard/self_check) 스모크 | `shared/harness/entry.hexa` | dispatcher_smoke.log | 5 엔트리 모두 0-exit | — | S | 1.0 | — |
| HARN-P1-2 | permissions_ssot.json 28 deny 패턴 적용율 | `shared/config/permissions_ssot.json` | deny_coverage.json | 28/28 테스트 통과 | HARN-P1-1 | S | 1.0 | — |
| HARN-P1-3 | cmd_gate seed 검증 게이트 + exec_validated wrapper 라운드트립 | `shared/harness/cmd_gate.hexa`, `shared/harness/exec_validated` | gate_trace.jsonl | sample 10 cmd 모두 gate 경유 | HARN-P1-1 | S | 1.0 | — |
| HARN-P1-4 | mistakes/errors jsonl 큐 상태 + 최근 24h routing 실효성 | `shared/harness/mistakes.jsonl`, `errors.jsonl` | route_health.json | H-ERR routing 누락 < 5% | — | S | 0.9 | — |
| HARN-P1-5 | lint.hexa + autofix.hexa 기저선 경과 리포트 | `shared/harness/lint.hexa`, `autofix.hexa`, `lint_log.jsonl` | lint_baseline.json | 기저선 고정, drift 0 | HARN-P1-1 | S | 0.8 | — |

### A4 GOVERNANCE

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| GOV-P1-1 | R0~R27 + NX1~NX3 + L0~L2 룰 번호 정합성 검사 | `shared/rules/common.json`, `nexus.json`, `shared/lockdown/lockdown.json` | rule_index.json | 중복/누락 0 | — | S | 1.0 | — |
| GOV-P1-2 | H-* 메타룰 20+ MEMORY → harness 코드 동기화 검사 | MEMORY H-* 문서, `shared/harness/pre_tool_guard.hexa` | meta_rule_sync.json | 메모 룰 ↔ 코드 1:1 | GOV-P1-1 | M | 0.8 | — |
| GOV-P1-3 | projects.json 7 프로젝트 + 번들/검증 전수 | `shared/config/projects.json` | project_matrix.json | 7/7 존재 + 경로 valid | — | S | 0.9 | — |
| GOV-P1-4 | absolute_rules + convergence_ops + core 3 SSOT 교차 검증 | `shared/config/{absolute_rules,convergence_ops,core}.json` | ssot_crosscheck.json | 3파일 key overlap 0 conflict | GOV-P1-1 | S | 0.9 | — |

### A5 DISCOVERY

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| DISC-P1-1 | reality_map.patches.merged.jsonl 895 entries 정합성 | `shared/discovery/reality_map.patches.merged.jsonl` | disc_baseline.json | 895 ±0 + hash 고정 | — | S | 1.0 | — |
| DISC-P1-2 | verified_constants.jsonl 도메인 인덱스 재생성 | `shared/discovery/verified_constants.jsonl` | constants_idx.json | lookup < 50ms | DISC-P1-1 | S | 0.9 | — |
| DISC-P1-3 | forge_result + theory_registry 교차 매핑 | `shared/discovery/forge_result`, `theory_registry` | forge_cross.json | 모든 theory → forge 링크 | DISC-P1-1 | M | 0.7 | — |
| DISC-P1-4 | discovery_log.{jsonl,sqlite} 크기/무결성 | `shared/discovery_log.{jsonl,sqlite}` | disc_integrity.json | jsonl row ≈ sqlite row | — | S | 1.0 | — |
| DISC-P1-5 | breakthroughs + next_directions + module_candidates 큐 상태 | `shared/discovery/{breakthroughs,next_directions,module_candidates}` | queue_snapshot.json | 3 큐 각 row count 기록 | DISC-P1-1 | S | 0.8 | — |

### A6 BLOWUP

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| BLOW-P1-1 | blowup.hexa 9-phase 파이프라인 스모크 (fast-path 기준) | `shared/blowup/core/blowup.hexa` | blowup_smoke.log | 9 phase 통과, exit 0 | — | M | 1.0 | — |
| BLOW-P1-2 | 6 modules (field/holographic/quantum/string/toe/_etc) 개별 실행 | `shared/blowup/modules/*.hexa` | modules_matrix.json | 6/6 exit 0, < 30s each | BLOW-P1-1 | M | 0.9 | — |
| BLOW-P1-3 | seed_engine.hexa + lens_forge.hexa 통합 시드 생성 | `shared/blowup/seed/seed_engine.hexa`, `shared/blowup/lens/lens_forge.hexa` | seed_batch.jsonl | 10+ seed 생성 | BLOW-P1-1 | S | 0.9 | — |
| BLOW-P1-4 | atlas_guard.hexa.inc 공유 헬퍼 호출 계약 검증 | `shared/blowup/lib/atlas_guard.hexa.inc` | guard_contract.json | 모든 모듈 contract 준수 | BLOW-P1-2 | S | 0.8 | — |
| BLOW-P1-5 | verify_dfs.hexa + compose.hexa 수치 검증 더블체크 | `shared/blowup/{verify_dfs,compose}.hexa` | verify_double.json | auto_stubs ↔ verify 일치율 ≥ 95% | BLOW-P1-1 | M | 0.8 | — |

### A7 BISOCIATION

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| BISOC-P1-1 | Montgomery-Dyson pair correlation 엔진 현 상태 | `shared/bisociation/unified/ouroboros_unified.hexa` + MEMORY handoff-bisociation | bisoc_state.json | L1 3/4, L2 4/4 재확인 | — | S | 1.0 | [BT-541] |
| BISOC-P1-2 | bisoc cross/ + spectra/ 폴더 데이터 인덱싱 | `shared/bisociation/{cross,spectra}/` | bisoc_idx.json | 모든 파일 crc32 기록 | BISOC-P1-1 | S | 0.8 | [BT-541] |
| BISOC-P1-3 | breakthroughs.jsonl + pitfalls.jsonl 큐 상태 | `shared/bisociation/{breakthroughs,pitfalls}.jsonl` | bisoc_queue.json | row count 고정 + hash | — | S | 0.9 | — |
| BISOC-P1-4 | phi_ratchet ↔ bisociation 연결 채널 확인 | `shared/bisociation/unified/phi_ratchet.hexa` | phi_link.json | ratchet bus message ≥ 1 | BISOC-P1-1 | S | 0.7 | — |

### A8 CONSCIOUSNESS

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| CONS-P1-1 | anima bridge live laws=2395 재확인 | `shared/consciousness/consciousness_laws.json`, `law_network.json` | cons_baseline.json | laws count 기록 | — | S | 1.0 | — |
| CONS-P1-2 | consciousness_loader.hexa + Φ integration smoke | `shared/consciousness/consciousness_loader.hexa` | phi_smoke.log | Φ 값 유한 | CONS-P1-1 | S | 0.9 | — |
| CONS-P1-3 | meta_laws_dd64 dump + factions.json 교차 | `shared/consciousness/{meta_laws_dd64,factions.json}` | meta_cross.json | meta_laws ↔ factions overlap | CONS-P1-1 | S | 0.8 | — |
| CONS-P1-4 | consciousness_mechanisms.json + law_discovery_results.json 상태 | `shared/consciousness/{consciousness_mechanisms,law_discovery_results}.json` | cons_mechs.json | mechanism count 기록 | CONS-P1-1 | S | 0.7 | — |

### A9 HEXA-LANG

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| HEXA-P1-1 | hexa binary resolver + local/remote path 매핑 | `shared/bin/hexa`, MEMORY `reference_hexa_binary.md` | hexa_resolver.json | local+hetzner 모두 exec | — | S | 1.0 | — |
| HEXA-P1-2 | hexa_grammar.jsonl P1~P5 pitfalls 정합성 | `shared/config/hexa_grammar.jsonl` | grammar_idx.json | P1~P5 5개 존재 | — | S | 0.9 | — |
| HEXA-P1-3 | hexa_pitfalls_log.jsonl 최근 수집 현황 | `shared/hexa_pitfalls_log.jsonl` | pitfalls_stat.json | 최근 7일 수집 ≥ 1 | HEXA-P1-2 | S | 0.8 | — |
| HEXA-P1-4 | hexa-lang ml-commands / rt-commands / bottlenecks 3 SSOT 링크 | `shared/hexa-lang/{ml-commands,rt-commands,runtime-bottlenecks}.json` | hexa_ssot.json | 3파일 schema valid | — | S | 0.8 | — |
| HEXA-P1-5 | porting_log + speed_ideas 현 이력 요약 | `shared/hexa/{porting_log,speed_ideas,hexa-lang_breakthroughs}` | porting_state.json | row count + 최종 row 기록 | — | S | 0.7 | — |

### A10 DSE

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| DSE-P1-1 | dse_domains.jsonl 24 도메인 정합 | `shared/dse/dse_domains.jsonl` | dse_domains_idx.json | 24 도메인 일치 | — | S | 1.0 | — |
| DSE-P1-2 | dse_cross_* 결과 4종 스키마 검증 | `shared/dse/dse_cross_*.json` | dse_cross_schema.json | 4 파일 valid JSON | DSE-P1-1 | S | 0.9 | — |
| DSE-P1-3 | dse_graph_3d.html + monte_carlo v6 교차 | `shared/dse/dse_graph_3d.html`, `shared/monte_carlo/monte_carlo_v6_*` | dse_mc_link.json | node count 일치 | DSE-P1-1 | S | 0.8 | — |
| DSE-P1-4 | dse/domains/ 하위 격자 상태 | `shared/dse/domains/` | domains_lattice.json | 5 levels × 6 cand grid 재현 | DSE-P1-1 | M | 0.7 | — |

### A11 BREAKTHROUGH

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| BT-P1-1 | bt_keywords.jsonl + bt_domains.jsonl 현 상태 | `shared/bt/bt_keywords.jsonl`, `bt_domains.jsonl` | bt_baseline.json | row count 기록 | — | S | 1.0 | [BT-541..547] |
| BT-P1-2 | bt_audit.hexa 실행 + bt_audit_result.json 재생성 | `shared/bt/bt_audit.hexa` | bt_audit.json | audit exit 0 + JSON valid | BT-P1-1 | M | 0.9 | [BT-541..547] |
| BT-P1-3 | BT-541~547 매핑 검사 + millennium 링크 | `shared/bt/bt_keywords.jsonl`, n6-architecture millennium closure | bt_millennium_map.json | 7/7 BT 대응 | BT-P1-1 | S | 1.0 | [BT-541..547] |
| BT-P1-4 | alien/alien_index_* UAP 분기 상태 | `shared/alien/alien_index_*` | alien_idx.json | row count 기록 | — | S | 0.6 | — |
| BT-P1-5 | BT-HEXA 25 키워드 확장 SSOT | `shared/bt/bt_keywords.jsonl` (BT-HEXA 분기) | bt_hexa_list.json | 25 키워드 존재 | BT-P1-1 | S | 0.8 | — |

### A12 LOCKDOWN

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| LOCK-P1-1 | lockdown.json L0/L1/L2 정의 + 경로 유효성 | `shared/lockdown/lockdown.json` | lockdown_idx.json | 모든 보호 경로 존재 | — | S | 1.0 | — |
| LOCK-P1-2 | lockdown_gate.hexa verify/status/watch 3 모드 smoke | `shared/harness/lockdown_gate.hexa` | lockdown_smoke.log | 3 모드 exit 0 | LOCK-P1-1 | S | 1.0 | — |
| LOCK-P1-3 | snapshots/ 디렉토리 체계 + safe-merge 경로 | `shared/lockdown/snapshots/` | snap_idx.json | 최근 3 스냅샷 존재 | LOCK-P1-1 | S | 0.8 | — |

### A13 INFRASTRUCTURE

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| INFRA-P1-1 | cl 멀티계정 런처 + cl-refresh 30m launchd 상태 | `shared/bin/cl`, `cl-refresh`, `launchd/com.nexus.cl-refresh.plist` | infra_baseline.json | launchd next-fire < 30m | — | S | 1.0 | — |
| INFRA-P1-2 | cl_refresh_spec + nexus_cli_spec 두 스펙 정합 | `shared/engine/cl_refresh_spec.json`, `nexus_cli_spec.json` | infra_spec.json | schema valid | INFRA-P1-1 | S | 0.9 | — |
| INFRA-P1-3 | hexa resolver + exec_validated wrapper 스모크 | `shared/bin/hexa`, `shared/harness/exec_validated` | resolver_trace.log | 샘플 5 cmd exec 통과 | — | S | 1.0 | — |
| INFRA-P1-4 | health-launchd + com.nexus.health 플리스트 가동 | `shared/bin/health-launchd`, `launchd/com.nexus.health.plist` | health_state.json | health all-green | INFRA-P1-1 | S | 0.9 | — |
| INFRA-P1-5 | scripts/sync-* + nexus_ensure_running 매니페스트 | `shared/scripts/sync-*.hexa`, `nexus_ensure_running` | scripts_idx.json | 존재 파일 모두 chmod +x | — | S | 0.7 | — |

### A14 REMOTE-COMPUTE

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| REM-P1-1 | hetzner + ubuntu + vastai + infrastructure 4 host 정의 | `shared/config/hosts/{hetzner,ubuntu,vastai,infrastructure}.json` | hosts_idx.json | 4/4 SSH reachable | — | S | 1.0 | — |
| REM-P1-2 | infra_state.json 최신 상태 + H100 idle guard 가동 | `shared/infra_state.json`, `shared/harness/h100_idle_guard.hexa` | remote_state.json | h100_state fresh | REM-P1-1 | S | 0.9 | — |
| REM-P1-3 | h100_alerts.jsonl 최근 24h 경보 요약 | `shared/harness/h100_alerts.jsonl` | alerts_summary.json | 심각 경보 0 or 분류 완료 | REM-P1-2 | S | 0.8 | — |
| REM-P1-4 | blowup 원격 라우팅 기본 경로 재확인 (BLOWUP_LOCAL=0) | MEMORY `feedback_no_blowup_local.md`, `feedback_hetzner_pollution.md` | remote_routing.json | env 점검 + policy 문서 | REM-P1-1 | S | 0.7 | — |

### A15 THINKING

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| THINK-P1-1 | thinking_engine.hexa + entry.hexa thinking 경유 smoke | `shared/harness/thinking_engine.hexa`, `entry.hexa thinking query` | think_smoke.log | 6-phase 반성 exit 0 | — | S | 1.0 | — |
| THINK-P1-2 | thinking_log.jsonl + think_baseline.json 기저 고정 | `shared/harness/thinking_log.jsonl`, `think_baseline.json` | think_baseline_lock.json | baseline hash 잠금 | THINK-P1-1 | S | 0.9 | — |
| THINK-P1-3 | 복잡 질문 6-phase 반성 샘플 10건 검토 | `shared/harness/thinking_log.jsonl` 최근 | think_sample_review.json | 10건 phase 분포 리포트 | THINK-P1-1 | S | 0.7 | — |

### A16 AGENT-LEDGER

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| AGL-P1-1 | agent_ledger.hexa + session_registry.jsonl 현 세션 등록율 | `shared/harness/agent_ledger.hexa`, `session_registry.jsonl` | ledger_state.json | 현재 세션 present | — | S | 1.0 | — |
| AGL-P1-2 | work_registry.jsonl 중복 방지 체계 스모크 | `shared/harness/work_registry.jsonl` | dedupe_report.json | 중복 레코드 0 | AGL-P1-1 | S | 0.9 | — |
| AGL-P1-3 | session_worktree + session_lock 연동 스모크 | `shared/harness/{session_worktree,session_lock,session}.hexa` | worktree_smoke.log | worktree/lock smoke exit 0 | AGL-P1-1 | S | 0.8 | — |

### A17 CONSENSUS

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| CONSN-P1-1 | consensus_loop.hexa + critique.hexa 루프 스모크 | `shared/harness/{consensus_loop,critique}.hexa`, `critique_log.jsonl` | consensus_smoke.log | 한 라운드 완주 | — | S | 0.9 | — |
| CONSN-P1-2 | curiosity + cross_feed + broadcast 파이프라인 정합 | `shared/harness/{curiosity,cross_feed,broadcast}.hexa` | pipe_trace.jsonl | 3 레이어 message flow | CONSN-P1-1 | S | 0.8 | — |
| CONSN-P1-3 | governance.jsonl 로그 기저 + 정합성 | `shared/harness/governance.jsonl` | gov_baseline.json | row count + hash | — | S | 0.8 | — |

### A18 ENGINE-FORGE

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| EF-P1-1 | engine_forge.hexa + engine_candidates.jsonl 현 상태 | `shared/harness/engine_forge.hexa`, `engine_candidates.jsonl` | ef_baseline.json | 후보 count 기록 | — | S | 1.0 | — |
| EF-P1-2 | engines_usage.jsonl 사용 통계 | `shared/harness/engines_usage.jsonl` | ef_usage.json | 통계 집계 완료 | EF-P1-1 | S | 0.8 | — |
| EF-P1-3 | shared/engine/engine_*.hexa 10+ 엔진 매니페스트 | `shared/engine/engine_*.hexa` | engine_manifest.json | 모든 엔진 .hexa parse-OK | — | S | 0.9 | — |
| EF-P1-4 | engine_anima_strategy + engine_nexus_strategy 두 전략 SSOT | `shared/engine/{engine_anima_strategy,engine_nexus_strategy}.json` | strategy_idx.json | 2 JSON schema valid | — | S | 0.8 | — |

### A19 CROSS-DOMAIN-GRID

| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| CDG-P1-1 | nexus.json v1 P4~P112 107 Phase 재배치 매트릭스 | `shared/roadmaps/nexus.json` P4~P112 | cdg_v1_matrix.json | 107 phase 매핑 완료 | — | M | 1.0 | — |
| CDG-P1-2 | 24 도메인 × 23 pair = 276 공간 중 실행 107 매핑 | CDG-P1-1 산출물 | cdg_coverage.json | coverage = 107/276 | CDG-P1-1 | S | 1.0 | — |
| CDG-P1-3 | dse_cross_* + bisociation/cross/ 두 crossgrid 교차 | `shared/dse/dse_cross_*`, `shared/bisociation/cross/` | dual_cross.json | 공통 pair 추출 | CDG-P1-1 | S | 0.8 | — |

---

## Phase 1 통계

- **신규 태스크**: 71 (19 축 × 평균 3.7)
- **누적 태스크**: 71
- **고갈 지수**: 0.0 (축별 신규 0 비율 = 0/19)
- **평균 강도**: 0.87
- **BT 연결 태스크**: 6 (BISOC-P1-1,2, BT-P1-1,2,3)
- **비용 분포**: S=59, M=12, L=0, XL=0 — 초기 진단 위주
- **다음 Phase 필요**: YES

축별 분포:
A1=4 | A2=5 | A3=5 | A4=4 | A5=5 | A6=5 | A7=4 | A8=4 | A9=5 | A10=4 | A11=5 | A12=3 | A13=5 | A14=4 | A15=3 | A16=3 | A17=3 | A18=4 | A19=3 = 71

## Phase 1 출구 조건 (gate_exit)
- [ ] 71 태스크 모두 `status == done`
- [ ] 모든 축에 baseline.json 1개 이상 생성
- [ ] 7대 난제 링크 완료 (BT-P1-3)
- [ ] 다음 Phase 진입 signal: `phase_1_gate_passed = true`
fail_action: 실패 태스크만 Phase 1+ 연장, 다른 축은 Phase 2 진입 허용.
