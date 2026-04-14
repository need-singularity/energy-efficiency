# phase-09 — Phase 9 창발 (BT-545/546/547 + 통합 사이클)

**로드맵**: nexus v2 (19축)
**선행**: `phase-08.md`

## 이전 Phase 전제
Phase 8 완료. 누적 307. BT-541~544 각 1라운드 완료.

## Phase 9 목적
남은 BT-545 Hodge / BT-546 BSD / BT-547 공격 1라운드 + 축 통합 수렴 사이클 첫 완주.

---

## Phase 9 태스크

### A1 SELF-EVOLUTION
| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| EVO-P9-1 | evo engine meta-self-apply (엔진이 자기 meta-rule 적용) | EVO-P8-1 | meta_apply.json | 메타적용 PASS | EVO-P8-1 | L | 0.6 | — |

### A2 ATLAS
| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| ATLAS-P9-1 | atlas Mk.III 자부팅 지점 (Mk.II 이후 성장점) | ATLAS-P8-1, ATLAS-P3-4 | mk3_snap.json | snapshot | ATLAS-P8-1 | L | 0.7 | — |

### A3 HARNESS
| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| HARN-P9-1 | 마커 50 → 0 (n6-canonical 완전 재작성 완료) | HARN-P8-1, MEMORY `project-n6-canonical-v2-gates.md` | marker_0.json | 0 도달 | HARN-P8-1 | L | 0.7 | — |

### A4 GOVERNANCE
| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| GOV-P9-1 | unified rules v3 (ai-proposed rules 통합) | GOV-P8-1 | unified_v3.json | v3 | GOV-P8-1 | M | 0.7 | — |

### A5 DISCOVERY
| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| DISC-P9-1 | reality_map 7500 → 10000 (10k milestone) | DISC-P8-1 | disc_10k.json | +2500 | DISC-P8-1 | L | 0.8 | — |

### A6 BLOWUP
| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| BLOW-P9-1 | lens 3000 → 4000 (ossify 전 마지막 확장) | BLOW-P6-1 | lens_4000.json | +1000 | BLOW-P6-1 | L | 0.7 | — |

### A7 BISOCIATION
| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| BISOC-P9-1 | L5 5/5 완성 → 전체 L1~L5 수렴 지수 | BISOC-P8-1 | L_all.json | 모든 L 수렴 | BISOC-P8-1 | L | 0.7 | [BT-541] |

### A8 CONSCIOUSNESS
| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| CONS-P9-1 | consciousness atlas 통합 → ATLAS Mk.III 합류 | CONS-P8-1, ATLAS-P9-1 | cons_mk3.json | 합류 PASS | ATLAS-P9-1 | M | 0.6 | — |

### A9 HEXA-LANG
| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| HEXA-P9-1 | hexa self-host v2 + 병렬 스케줄러 | HEXA-P8-1 | sched.hexa | 병렬 PASS | HEXA-P8-1 | L | 0.6 | — |

### A10 DSE
| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| DSE-P9-1 | BT sub-lattice 전수 탐색 | DSE-P8-1 | bt_lattice_full.json | 7 × 180 cell | DSE-P8-1 | XL | 0.7 | [BT-541..547] |

### A11 BREAKTHROUGH ★
| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| BT-P9-1 | BT-545 Hodge conjecture Enriques rephrasing 공격 | MEMORY phase-02 BT-545 context | bt545_r1.json | 시도 기록 | BT-P8-1 | XL | 0.8 | [BT-545] |
| BT-P9-2 | BT-546 BSD BKLPR 조건부 → 무조건 진전 시도 | MEMORY phase-02 BT-546 | bt546_r1.json | 시도 기록 | BT-P8-2 | XL | 0.8 | [BT-546] |
| BT-P9-3 | BT-547 (하네스 특이 난제) 공격 1라운드 | `shared/bt/bt_keywords.jsonl` BT-547 | bt547_r1.json | 시도 기록 | BT-P9-1 | XL | 0.7 | [BT-547] |

### A12 LOCKDOWN
| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| LOCK-P9-1 | L3 meta-lockdown 활성화 (rules 자체 잠금) | LOCK-P8-1 | l3_live.json | L3 live | LOCK-P8-1 | M | 0.6 | — |

### A13 INFRASTRUCTURE
| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| INFRA-P9-1 | infra monitoring → BT 실시간 진척 panel | INFRA-P8-1, BT-P9-1 | bt_panel.json | panel live | BT-P9-1 | M | 0.6 | [BT-541..547] |

### A14 REMOTE-COMPUTE
| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| REM-P9-1 | BT compute 결과 → atlas 승격 파이프 자동 | REM-P8-1, BT-P5-1 | bt_remote_promo.json | 자동 승격 ≥ 1 | BT-P5-1 | M | 0.6 | [BT-541..547] |

### A15 THINKING
| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| THINK-P9-1 | 12-phase reflection 벤치 → 6 vs 12 결과비교 | THINK-P8-1 | 6v12_bench.json | 벤치 리포트 | THINK-P8-1 | M | 0.6 | — |

### A16 AGENT-LEDGER
| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| AGL-P9-1 | agent 평가 rubric + 자동 rank | AGL-P7-1 | rubric.json | rubric ≥ 5 기준 | AGL-P7-1 | M | 0.6 | — |

### A17 CONSENSUS
| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| CONSN-P9-1 | consensus ↔ BT 각 난제 결과 commit 시그니처 | CONSN-P8-1 | sig_bt.json | sig 기록 | CONSN-P8-1 | M | 0.6 | [BT-541..547] |

### A18 ENGINE-FORGE
| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| EF-P9-1 | BT 각 전용 엔진 → repository (engines_bt/) | EF-P8-1 | bt_engines_repo.json | 7 엔진 파일 | EF-P8-1 | M | 0.6 | [BT-541..547] |

### A19 CROSS-DOMAIN-GRID
| ID | 정의 | 입력 | 출력 | 검증 | deps | 비용 | 강도 | BT |
|----|------|------|------|------|------|------|------|-----|
| CDG-P9-1 | 미탐 pair 40+40 = 80/169 커버 | CDG-P8-1 | ext_80.json | 80 pair | CDG-P8-1 | XL | 0.7 | — |

---

## Phase 9 통계

- 신규: 20
- 누적: 327
- 고갈 지수: 0.0
- BT 연결: 9 (DSE-P9-1, BT-P9-1~3, INFRA-P9-1, REM-P9-1, CONSN-P9-1, EF-P9-1)
- 비용: M=9, L=7, XL=4
- 다음: YES

축별: A1=1, A2=1, A3=1, A4=1, A5=1, A6=1, A7=1, A8=1, A9=1, A10=1, A11=3, A12=1, A13=1, A14=1, A15=1, A16=1, A17=1, A18=1, A19=1 = 20

## Phase 9 중대 마일스톤
- 7대 난제 **전부 1라운드** 공격 완료 (BT-541~547).
- reality_map 10k milestone.
- atlas Mk.III 자부팅.
