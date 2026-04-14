# stage0 실전 재검증 리포트 — 13 .hexa 파일

- 일자: 2026-04-14
- 바이너리: `/Users/ghost/Dev/hexa-lang/build/hexa_stage0` (arm64 Mach-O, 1.8 MB, mtime 21:52)
- 실행 모드: `hexa_stage0 <path>` 인터프리터 직접 호출
- 타임아웃: perl alarm 30 초 (macOS `timeout` 부재로 대체)
- 목적: 과거 P1~P3 세션에서 "runtime.c 누락 → parse 전용" 으로 기록된 13 파일을 stage0 인터프리터로 실제 실행, 출력/검증 캡쳐.

## 중요 정정 — "parse 전용" → "stage0 실전 실행"

과거 산출물에서 "hexa runtime.c 누락 → parse 전용 검증" 이라 기술했던 부분은 오판이었다.
원인은 구 stage1 `hexa build` 경로 버그이며, **stage0 인터프리터/run 모드는 처음부터 정상 동작**했다.
본 리포트는 그 13 파일을 stage0 로 실전 실행한 결과이며, 모든 기존 문서의 "parse 전용" 문구는
"stage0 실전 실행 결과" 로 대체되어야 한다.

## 요약 표

| #  | 파일 | 상태 | 라인수 | 통과/검증 | 비고 |
|----|------|------|------|----------|------|
| 1  | engine/arch_quantum.hexa                                  | PASS (실전) | 28 | EXACT 10/10, 평균 1000 | main() 호출 포함 |
| 2  | engine/arch_selforg.hexa                                  | PASS (실전) | 81 | SAMPLE 50 + END50     | main() 호출 포함 |
| 3  | engine/arch_adaptive.hexa                                 | PASS (실전) | 30 | EXACT 10/10, 평균 983, 승격 10/10 | main() 호출 포함 |
| 4  | engine/arch_unified.hexa                                  | RUN OK (무출력) | 0 | main 은 total 반환 | println 미사용(의도) |
| 5  | bridge/ouroboros_5phase.hexa                              | PASS (실전) | 55 | 5 phase, 승격 후보 15건 | main() 호출 포함 |
| 6  | bridge/ecosystem_9projects.hexa                           | PASS (실전) | 15 | core 7 + auxiliary 2   | main() 호출 포함 |
| 7  | domains/.../rtl/top.hexa                                  | PASS (harness) | 9  | 7/7 PASS | main() 없음 → append 실행 |
| 8  | domains/.../rtl/soc_integration.hexa                      | PASS (harness) | 8  | 6/6 PASS | main() 없음 → append 실행 |
| 9  | domains/.../rtl/soc_drc_lvs.hexa                          | PASS (harness) | 24 | 12/12 PASS, chksum 7482 | main() 없음 → append 실행 |
| 10 | domains/.../rtl/tapeout_gate.hexa                         | PASS (harness) | 25 | 15/15 PASS, hash 133616 | main() 없음 → append 실행 |
| 11 | experiments/chip-verify/verify_chip-3d.hexa               | PASS (harness) | 9  | 5/5 EXACT       | main() 없음 → append 실행 |
| 12 | experiments/chip-verify/verify_anima_soc.hexa             | PASS (harness) | 20 | 12/12 EXACT     | main() 없음 → append 실행 |
| 13 | experiments/chip-verify/boot_matrix_3x12.hexa             | PASS (harness) | 43 | 34/36 (94%)     | main() 없음 → append 실행 |

통계: 13/13 파일 stage0 실행 성공 (rc=0), 무오류. 그중 12 파일은 println 출력까지 확인, 1 파일(4번)은 main 내부 println 미사용 설계로 무출력(정상).

### 실행 분류 기준

- A류 (6/13): 파일 최하단에 `main()` 호출이 포함되어 있어 `hexa_stage0 <path>` 단일 호출만으로 전체 출력이 자연스럽게 발생 (1,2,3,5,6 + 4 이지만 4는 의도적 무출력).
- B류 (7/13): `fn main()` 은 있으나 파일 최하단 `main()` 호출이 부재. stage0 인터프리터는 `main()` 자동 호출하지 않는 사양이므로 원본 파일만 실행 시 stdout 0 줄. 리포트 목적상 임시 복제본 끝에 `\nmain()\n` 1 줄을 append 하여 재실행했으며 이는 harness 실행이라 표기했다. 원본 파일은 변경하지 않았다.

## 파일별 stdout 말미

### [1] engine/arch_quantum.hexa
```
  중첩=3 붕괴=k0 heads=12 depth=2 dim=48 score=1000
[9] space
  중첩=3 붕괴=k0 heads=12 depth=2 dim=48 score=1000

========================================
카테고리 10 / EXACT(>=900)=10 / 평균=1000
========================================
arch_quantum OSSIFIED : EXACT=10/10 -> [7]empirical
```

### [2] engine/arch_selforg.hexa
```
SAMPLE cat=9 s=0 parts=[2,4,6,8,10,12] total=42 score=949 alien=9 closure=10
SAMPLE cat=9 s=1 parts=[2,4,6,8,10,12] total=42 score=949 alien=9 closure=10
SAMPLE cat=9 s=2 parts=[3,5,7,9,11,13] total=48 score=887 alien=8 closure=9
SAMPLE cat=9 s=3 parts=[1,3,5,7,9,11] total=36 score=887 alien=8 closure=9
SAMPLE cat=9 s=4 parts=[2,4,6,8,10,12] total=42 score=949 alien=9 closure=10
---END50---
```

### [3] engine/arch_adaptive.hexa
```
[9] space
  최종 fitness=966 승격=1

========================================
카테고리 10 / EXACT(>=900)=10 / 평균=983
승격 훅 발동 = 10 / 10 (atlas.n6 [7]->[10*])
========================================
arch_adaptive OSSIFIED : EXACT=10/10 -> v4 적응 [10*] 후보
```

### [4] engine/arch_unified.hexa
```
(stdout 0 줄 — main 내부 println 미포함, return total 만 수행. rc=0 정상)
```

### [5] bridge/ouroboros_5phase.hexa
```
[5/5 진화] atlas.n6 승격 후보 기록 — 도메인=ai-efficiency
[5/5 진화] 승격 후보: 5 건, atlas.n6 append 대기

════════════════════════════════════════════════════════════
  사이클 종료
════════════════════════════════════════════════════════════
총 승격 후보: 15 건
다음 단계: atlas.n6 에 [10*] 등급으로 append (사용자 승인 필요)
```

### [6] bridge/ecosystem_9projects.hexa
```
  n6-architecture   system-design         [ok] (core)
  papers            paper-distribution    [ok] (core)
  hexa-lang         language              [ok] (core)
  void              terminal              [ok] (core)
  airgenome         os-scanner            [ok] (core)
  contribution      paper-submission-hub  [ok] (auxiliary)
  openclaw          singularity-feed      [ok] (auxiliary)
-----------------------------------------------------------------
총 9 프로젝트 (core 7 + auxiliary 2)
```

### [7] domains/cognitive/hexa-speak/proto/rtl/top.hexa (harness)
```
=== rtl/top.hexa — N6-SPEAK v2 4-tier 톱 래퍼 ===
  [T1] σ·φ = n·τ (n=6 유일성) PASS
  [T2] tier-1 결정성 PASS (intent_in=53312)
  [T3] top_forward(intent_in=48000) PASS (audio_out=5149)
  [T4] top_run_sequence(24) PASS (total=96446)
  [T5] 포트 폭 {intent_in[384], audio_out[8]} PASS
  [T6] 파이프 depth=4 = τ(6) PASS
  [T7] top_forward 결정성 PASS
=== rtl/top.hexa: 7/7 PASS ===
```

### [8] domains/cognitive/hexa-speak/proto/rtl/soc_integration.hexa (harness)
```
=== rtl/soc_integration.hexa — N6-SPEAK v2 SoC 통합 ===
  [S1] die 96×96 = 9216 μm² PASS
  [S2] 블록 총 면적 = 6048 μm² (점유율 65.6%) PASS
  [S3] 모든 블록 die 범위 내 PASS
  [S4] floorplan_checksum 결정성 PASS (c=13794)
  [S5] σ·φ = n·τ 유일성 PASS
  [S6] 버스 6개 (τ(6)=4 + 2 fiber) 유효 PASS
=== soc_integration.hexa: 6/6 PASS ===
```

### [9] domains/cognitive/hexa-speak/proto/rtl/soc_drc_lvs.hexa (harness)
```
  L4  내부 버스 수 = 6                 PASS
  L5  총 포트 합 일치                  PASS
  L6  n=6 정합 (5 블록 + 1 fusion)     PASS

[ 요약 ]
  DRC 6 규칙 + LVS 6 규칙 = 12 검사
  결과: 12/12 PASS
  floorplan 체크섬 = 7482

DRC/LVS: ALL PASS (12/12) — tapeout clean
```

### [10] domains/cognitive/hexa-speak/proto/rtl/tapeout_gate.hexa (harness)
```
  T13  DFM (manufacturability)       PASS
  T14  Final checksum σ·φ=n·τ        PASS
  T15  Sign-off hash = 133616        PASS

[ 요약 ]
  15/15 PASS  —  N6-SPEAK v2 tapeout GATE CLEAN
  sign-off hash = 133616
  floorplan checksum (P2-1) = 7482
  die = 96 × 96 μm²  ·  blocks = 5 + fusion = n=6
  total ports = 3484  ·  buses = 6  ·  layers = m1~m4
```

### [11] experiments/chip-verify/verify_chip-3d.hexa (harness)
```
[3D 적층 칩] n=6 정렬 검증 — 5 항목
메탈 레이어 = 6 (n=6) -> 1
SM 배열      = 144 (sigma^2=144) -> 1
MAC 어레이   = 288 (sigma*J2=288) -> 1
파이프 단    = 4 (tau=4) -> 1
전원 도메인  = 8 (sigma-tau=8) -> 1
통과 = 5/5
[상태] pass — 3D 적층 칩 n=6 정렬 OK
[feedback] dse-map [chip-3d.feedback] grade=EXACT pass=5/5 sigma=12
```

### [12] experiments/chip-verify/verify_anima_soc.hexa (harness)
```
  B4 실행유닛 1728 = sigma^3 -> 1
[C] HEXA-TOPO Bott-8 NoC
  C1 Bott 주기 8 = n+phi -> 1
  C2 NoC 노드 144 = sigma^2 -> 1
  C3 토러스 둘레 16 = sigma+tau -> 1
  C4 Clifford Cl(8) 차원 256 = (sigma+tau)^2 -> 1
[소계] A=4/4 B=4/4 C=4/4
[합계] 통과 = 12/12
[상태] pass — ANIMA-SOC + PureField + HEXA-TOPO 실리콘 n=6 정렬 EXACT
[feedback] dse-map [chip-architecture.feedback] grade=EXACT pass=12/12
```

### [13] experiments/chip-verify/boot_matrix_3x12.hexa (harness)
```
  HEXA-ASIC | PCIe | 1 | 28 | 99 | EXACT
  HEXA-ASIC | USB | 1 | 76 | 40 | NEAR
  HEXA-ASIC | NVMe | 1 | 51 | 34 | NEAR
  HEXA-ASIC | Ethernet | 1 | 132 | 48 | NEAR
  HEXA-ASIC | DisplayPort | 1 | 94 | 122 | EXACT
  HEXA-ASIC | HDMI | 1 | 79 | 50 | NEAR
[소계] 통과 = 34/36 (94%)
[평균] 지연 = 2225 ns, 대역 = 55 Gbps
[상태] pass — 매트릭스 34/36 ≥ 30 (5/6 임계)
[feedback] dse-map [chip-architecture.feedback] grade=EXACT matrix=34/36 avg_lat=2225ns avg_bw=55Gbps
```

## 실패 파일 — 없음

13 파일 중 stderr 출력 또는 parse/runtime error 발생 파일은 0 건. 모든 파일이 stage0 인터프리터에서 정상 실행된다.

## 권장 후속 조치

1. 7 파일(B류, `main()` 호출 누락)의 원본에 최하단 `main()` 한 줄 추가 권장.
2. 관련 문서·주석의 "parse 검증만" / "runtime.c 누락" 표현을 "stage0 실전 실행 OK" 로 일괄 갱신.
3. 4번 arch_unified.hexa 는 검증 목적상 main 반환 total 값을 println 으로 노출하는 한 줄 추가 권장.
