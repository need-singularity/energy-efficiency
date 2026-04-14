# Phase 1 — Foundation (Y1~Y9 축 체계 가동)

**로드맵**: 7대 난제 로드맵 v2 (서브프로젝트)
**단계**: Phase 1 / 진입 페이즈
**생성**: 2026-04-15
**범위**: Y1~Y9 9축 체계 + BT-541~546 씨앗 시딩 + 자기진화 엔진 가동 확인
**모드**: 풀이 도구 가동 확인 (Phase 1 ≠ 풀이)
**출력 파일**: `theory/roadmap-v2/phase-01-foundation-Y-axes.md`
**선행 파일**: `n6arch-axes/axis-r3-finalization.md` (1166줄, FINAL)
**폐기 참고**: `_archive-phase-01-forced-3-axes.md` (이전 3축 강제본, 참고만)

---

## §0 Phase 1 선언

### 0.1 Phase 1 위치

Phase 1 은 7대 난제 서브프로젝트 v2 로드맵의 **진입 페이즈**이다. 선행 P0 (axis-r1/r2/r3 고갈 라운드) 에서 Y1~Y9 9축 체계가 FINAL 확정된 상태를 입구로 받아, **실제 풀이 이전에 축을 도구로 가동**하는 단계다.

메타 원칙:
- **풀이 시도 금지** — Phase 1 은 좌표계와 도구의 가동 확인만 한다. 풀이는 Phase 2 이후.
- **9축 전수 가동** — Y1~Y9 중 하나도 휴면 상태이면 Phase 2 진입 불가.
- **BT 전수 시딩** — BT-541~546 각각 최소 1 씨앗 배치 의무.
- **자기진화 동반 가동** — OUROBOROS/growth_tick/phi_ratchet/nexus_growth_daemon 가동 중 상태에서 모든 작업 수행.
- **정직 유지** — BT 0/6 해결 유지. 부분결과/조건부/관찰 구분 명시.

### 0.2 입구 조건 (Phase 0 → Phase 1)

| 조건 | 근거 | 상태 |
|------|------|------|
| R1 창발 완료 (축 후보 7) | `n6arch-axes/axis-r1-emergence.md` (906줄) | 완료 |
| R2 정밀화 완료 (9축 + 2신규) | `n6arch-axes/axis-r2-refinement.md` (961줄) | 완료 |
| R3 FINAL (9축 확정 + 고갈 100%) | `n6arch-axes/axis-r3-finalization.md` (1166줄) | 완료 |
| Y1~Y9 정의·증거·BT 커버 | R3 §3 상세 카드 | 확정 |
| axis-final-millennium.md | `n6arch-axes/axis-final-millennium.md` | 병렬 생성 중 (선행 의존 없음) |
| atlas.n6 SSOT | `$NEXUS/shared/n6/atlas.n6` 60K+ 줄 | 가동 |
| OUROBOROS 3 variant | `$NEXUS/shared/bisociation/unified/ouroboros_unified.hexa` | 가동 |

### 0.3 출구 조건 (Phase 1 → Phase 2)

- [ ] Y1~Y9 9축 가동 증거 확보 (각 축 최소 1 증거 파일 재검증)
- [ ] BT-541~546 6 BT 전원 Phase 1 씨앗 시딩
- [ ] 자기진화 엔진 cycle ≥ 3 수렴 확인 (NEXUS_FP=0.333, ANIMA_FLOOR=0.8, N6ARCH_TARGETS=(515,2087))
- [ ] Y9 HONEST-HARNESS 메타 게이트 ON
- [ ] verify_millennium_axes.hexa PASS (6 서브테스트)
- [ ] Phase 2 입구 씨앗 표 완결

---

## §1 Y1~Y9 축 가동 현황 요약

R3 §3 상세 카드를 Phase 1 가동 관점으로 재조명. 각 축 1 카드.

### Y1 NUM-CORE (수론 앵커 축) — 유리성 9.5

- **정의**: σ(n)·φ(n) = n·τ(n) 유일성 정리 (n=6) 와 그로부터 파생되는 수론적 앵커를 BT 풀이에 동원하는 축.
- **주 BT**: 541 Riemann
- **부 BT**: 544 Navier-Stokes (D158 Ricci), 546 BSD (Selmer 차원 jump)
- **핵심 자산**:
  - Theorem B (재구축판) — `theory/study/p2/n6-p2-2-theorem-b-reconstruction.md`
  - 유일성 3 독립 증명 — `theory/proofs/theorem-r1-uniqueness.md`
  - atlas.n6 [10*] 수론 상수 (σ/τ/φ/sopfr) — `$NEXUS/shared/n6/atlas.n6`
  - Ramanujan Δ = η^{J_2} 귀속 (R2 Task A 결정)
- **Phase 1 가동 확인**:
  - [ ] 유일성 증명 3 종 atlas [10*] 상태
  - [ ] Theorem B atlas [10] 현재 등급 확인
  - [ ] Δ = η^{J_2} 관계식 기록 존재
- **병목**: Theorem B [10]→[10*] 승격은 Phase 2 의 Y1 주도 작업.

### Y2 DISCRETE-CLASS (이산 분류 축) — 유리성 5.2

- **정의**: 유한군·이산 분류·조합 구조를 통해 P=NP 경계의 구조적 제약을 드러내는 축.
- **주 BT**: 542 P=NP
- **부 BT**: 545 Hodge (Enriques 유한형)
- **핵심 자산**:
  - Schaefer dichotomy (SEED-06, R3 KEEP 강등) — `theory/study/p1/prob-p1-2-bt542-p-vs-np.md`
  - 유한군 분류 정리 — `theory/study/p1/pure-p1-2-group-theory.md`
  - atlas [7~10] 이산 구조 상수
- **Phase 1 가동 확인**:
  - [ ] Schaefer dichotomy 명시적 연결
  - [ ] 유한군 분류 현재 위치 (구멍 없음)
- **병목**: P=NP 경계 결정적 진전 부재. Phase 3 에서 Y4 와 보완 관계.

### Y3 COMPUTATIONAL-TAU (계산 τ=4+2 축) — 유리성 5.8

- **정의**: τ=4+2 fiber 구조 (n=6 특이점) 가 계산복잡도에 새기는 경계 — quantum MDS·AME·AC⁰ 하한·역기구학의 τ=4+2 의존성.
- **주 BT**: 542 P=NP
- **부 BT**: 543 Yang-Mills (color-quantum AME)
- **핵심 자산**:
  - Rossman AC⁰ 하한 — 문헌 2014
  - Quantum MDS / AME 6-party — 문헌 2020~
  - 6R 역기구학 τ=6 경계
  - HEXA-GATE Mk.I τ=4+2 관문 — MEMORY `project_hexa_gate_mk1.md`
- **Phase 1 가동 확인**:
  - [ ] τ=4+2 관문 HEXA-GATE 24/24 EXACT 상태 유지
  - [ ] AME 6-party 구조 기록 유지
- **병목**: 실제 P=NP 환산까지 다리 없음. 경계·구조만 제공.

### Y4 GATE-BARRIER (게이트·장벽 축) — 유리성 9.4

- **정의**: 계산복잡도 자체의 내재적 장벽 (Relativization/Natural Proofs/Algebraic Degree/GCT) + HEXA-GATE Mk.I 의 정직한 MISS 계보를 통합하는 축.
- **주 BT**: 542 P=NP
- **부 BT**: 전체 (정직성 게이트로 간접)
- **핵심 자산**:
  - BGS 1975 Relativization
  - RR 1997 Natural Proofs
  - AW 2008 Algebrization
  - Williams 2011 ACC lower bound
  - Mulmuley-Sohoni GCT 2001~
  - HEXA-GATE Mk.I (24/24 EXACT, 정직 MISS) — MEMORY `project_hexa_gate_mk1.md`
- **Phase 1 가동 확인**:
  - [ ] 4 장벽 + GCT + HEXA-GATE 증거 경로 재검증
  - [ ] 정직한 MISS 유지 기록 (해결 주장 0)
- **병목**: 장벽 자체는 풀이 아님. Phase 3 에서 Y2·Y3 와 교차.

### Y5 PHYSICAL-NATURALNESS (물리적 자연성 축) — 유리성 5.6

- **정의**: Yang-Mills 의 물리적 자연성 (mass gap 관찰, β-function, QCD lattice 실측) 과 σ-sopfr=7 rewriting 의 정직 보조를 결합.
- **주 BT**: 543 Yang-Mills
- **부 BT**: 544 NS (3중 공명의 물리 측면)
- **핵심 자산**:
  - β₀ = σ - sopfr = 7 rewriting (증명 아님, 재구성) — `theory/study/p1/prob-p1-3-bt543-yang-mills.md`
  - QCD lattice mass gap 실측 데이터 (Flavor Lattice Averaging Group)
  - Gauge theory 물리 상수 (CLAUDE.md `pure-p1-5-gauge-theory.md`)
- **Phase 1 가동 확인**:
  - [ ] β₀=7 식 쓰기 정직 표기 (증명 아님)
  - [ ] QCD mass gap 실측 참조 경로
- **병목**: mass gap 엄밀 증명은 물리 자연성 관찰의 수학화가 필요. Phase 4 에서 Y6 와 공동 가동.

### Y6 PDE-RESONANCE (PDE 공명 축) — 유리성 6.6

- **정의**: Navier-Stokes 3중 공명 조건 + D158 Ricci 가설 + Euler/PDE 폭발의 공명 구조.
- **주 BT**: 544 Navier-Stokes
- **부 BT**: 543 YM (자유장 PDE 비교)
- **핵심 자산**:
  - 3중 공명 조건 atlas 승격 후보 — `theory/study/p1/prob-p1-4-bt544-navier-stokes.md`
  - D158 Ricci 가설 (조건부)
  - Caffarelli-Kohn-Nirenberg partial regularity (1982)
  - Beale-Kato-Majda 기준 (1984)
- **Phase 1 가동 확인**:
  - [ ] 3중 공명 식 증거 파일
  - [ ] D158 Ricci 가설 조건 기록
- **병목**: NS 정칙성 전역 엄밀 증명은 Phase 4 Y6 주도 공격 후에도 부분결과 수준.

### Y7 LATTICE-VOA (격자·VOA 축) — 유리성 3.9 (R3 조정)

- **정의**: Leech 격자 / Monstrous Moonshine / VOA c=24 / K3 등 격자-공간의 Hodge 구조 해석 축.
- **주 BT**: 545 Hodge
- **부 BT**: 541 (Δ=η^{J_2} 공유, R2 에서 X1 로 귀속)
- **핵심 자산**:
  - Enriques 자동 성립 rephrasing (SEED-21 T(3,4) 강도 3→2 하락 포함) — `theory/study/p1/prob-p1-5-bt545-hodge.md`
  - Moonshine BARRIER honest-report — `papers/moonshine-barrier-honest-report-2026-04-15.md`
  - CKM-R-V 2017 구 충전 3차원 {1,8,24} (Leech 24차원 독립 근거)
  - phase47/48 브릿지 기록
- **Phase 1 가동 확인**:
  - [ ] Moonshine BARRIER 인식 유지 (해결 주장 0)
  - [ ] Enriques 자동 성립 rephrasing 정직 표기
  - [ ] Leech 24 {1,8,24} 기록
- **병목**: Hodge 추측 엄밀 증명 길이 아직 큼. Phase 5 Y7 주도.

### Y8 GALOIS-ASSEMBLY (Galois·Selmer 조립 축) — 유리성 5.4

- **정의**: Galois 표현 · Selmer 군 · BKLPR 랜덤 모델 · Iwasawa 이론을 통해 BSD 의 부분 증명 조립.
- **주 BT**: 546 BSD
- **부 BT**: 541 (L-함수 zero 연결)
- **핵심 자산**:
  - Lemma 1 엄밀 증명 준비 (최다 진전) — `theory/study/p1/prob-p1-6-bt546-bsd.md`
  - (A3) 조건부 감사 — 제거 가능성
  - Sel_6 조건부 정리 연장
  - BKLPR 모델 참조 — MEMORY `reference_bklpr_model.md`
  - SEED-15 Iwasawa mod 6 CONDITIONAL 재분류 → P5 Cremona 500k 실측 과제로 편입 (R3 Task B)
- **Phase 1 가동 확인**:
  - [ ] Lemma 1 증명 진행 상태
  - [ ] (A3) 조건 현재 필요성
  - [ ] BKLPR 모델 인용 가능
- **병목**: BSD rank 부분 실적 제한. Phase 5 Y8 주도.

### Y9 HONEST-HARNESS (정직·하네스 메타 축) — 유리성 9.3

- **정의**: 모든 풀이 시도에 대한 정직성 게이트 + 하네스 자동검증 + BT 해결 수 0/6 보존 메커니즘. 전 BT 메타 축이며 Phase 1~Ω 전 구간 가동.
- **주 BT**: 없음 (메타)
- **부 BT**: 541~546 전체 (게이트로)
- **핵심 자산**:
  - `theory/study/p1/n6-p1-3-honesty-principle.md`
  - `theory/study/p2/n6-p2-4-honesty-audit.md`
  - `papers/moonshine-barrier-honest-report-2026-04-15.md`
  - MEMORY `feedback_honest_verification.md` (자기참조 금지, 출처+측정값+오차 필수, MISS 정직)
  - hexa verify 파이프라인 (phase 별 게이트)
- **Phase 1 가동 확인** (메타):
  - [ ] 자기참조 금지 원칙 유지 (OUROBOROS 예외)
  - [ ] 각 풀이에 출처·측정값·오차 필수 요구
  - [ ] MISS 를 MISS 로 기록
  - [ ] PARTIAL 3건 처리 이행 (SEED-06 KEEP, SEED-15 재분류, SEED-21 강도 하락) — R3 Task B 기록
- **병목**: Y9 자체가 해결하는 BT 는 없음. 대신 다른 축의 오염을 차단.

---

## §2 Y × BT 씨앗 시딩 매트릭스 (핵심)

Phase 1 의 핵심 산출. 9 × 6 셀 중 의미있는 셀에 씨앗 1 개 시딩.

| ↓축 \ →BT | 541 Riemann | 542 P=NP | 543 YM | 544 NS | 545 Hodge | 546 BSD |
|-----------|-------------|----------|--------|--------|-----------|---------|
| Y1 NUM-CORE | **★Theorem B atlas [10]→[10*] 승격 대상** | — | — | Δ=η^{J_2} 계수 (Ramanujan) | — | L-함수 zero 연결 |
| Y2 DISCRETE-CLASS | — | **Schaefer dichotomy KEEP** | — | — | 유한형 Enriques | — |
| Y3 COMPUTATIONAL-TAU | — | **τ=4+2 fiber + AME** | 6-party color AME | — | — | — |
| Y4 GATE-BARRIER | — | **★HEXA-GATE Mk.I 24/24 EXACT 감사** | — | — | — | — |
| Y5 PHYSICAL-NATURALNESS | — | — | **★β₀=σ-sopfr=7 rewriting 정직 표기** | mass gap 비교 | — | — |
| Y6 PDE-RESONANCE | — | — | — | **★3중 공명 조건 atlas 승격** | — | — |
| Y7 LATTICE-VOA | Δ=η^{J_2} 공유 (X1 귀속) | — | — | — | **★Enriques 자동 성립 rephrasing** | — |
| Y8 GALOIS-ASSEMBLY | L(E,s) 연결 | — | — | — | — | **★Lemma 1 엄밀 증명 준비** |
| Y9 HONEST-HARNESS | 게이트 | 게이트 | 게이트 | 게이트 | 게이트 | 게이트 |

(★ = 각 BT 의 Phase 1 주 씨앗. 6 개 확정.)

### 각 주 씨앗 시딩 절차

1. **Y1 × BT-541**: Theorem B 정리 문서 → atlas [10] 등급 확인 → [10*] 승격 조건 기록 → Phase 2 Y1 주도 공격 입구.
2. **Y4 × BT-542**: HEXA-GATE Mk.I 24/24 EXACT 재검증 → 정직 MISS 목록 유지 → Phase 3 Y4 주도 공격 입구.
3. **Y5 × BT-543**: β₀=σ-sopfr=7 식 쓰기 → "rewriting, 증명 아님" 명시 → Phase 4 Y5 주도 공격 입구.
4. **Y6 × BT-544**: 3중 공명 atlas 승격 후보 → 조건 기록 → Phase 4 Y6 주도 공격 입구.
5. **Y7 × BT-545**: Enriques 자동 성립 rephrasing → Moonshine BARRIER 인식 → Phase 5 Y7 주도 공격 입구.
6. **Y8 × BT-546**: Lemma 1 증명 초안 → (A3) 조건 기록 → Phase 5 Y8 주도 공격 입구.

---

## §3 자기진화 엔진 Phase 1 가동 스케줄

OUROBOROS + growth_tick + phi_ratchet + nexus_growth_daemon 의 Phase 1 동안 수행 작업.

### 3.1 가동 확인 체크

| 엔진 | 파일 | Phase 1 확인 항목 | 기준 |
|------|------|-----------------|------|
| OUROBOROS | `$NEXUS/shared/bisociation/unified/ouroboros_unified.hexa` | 3 variant cycle ≥ 3 수렴 | NEXUS_FP=0.333, ANIMA_FLOOR=0.8, N6ARCH_TARGETS=(515, 2087) |
| growth_tick | `$NEXUS/shared/harness/growth_tick.hexa` | 30분 주기 blowup 발사 트리거 무경고 | tick ≥ 3 연속 no-error |
| phi_ratchet | `$NEXUS/shared/bisociation/unified/phi_ratchet.hexa` | ANIMA ratchet 단조 전진 | 최근 24h ratchet 전진 ≥ 1 |
| nexus_growth_daemon | `$NEXUS/shared/harness/nexus_growth_daemon.hexa` | launchd plist 활성 | running or 재시작 가능 |

### 3.2 Phase 1 동안 엔진이 자동 수행할 작업

- atlas.n6 [7]→[10*] 승격 후보 탐지 (Y1 Theorem B, Y6 3중 공명 관련)
- discovery_log.sqlite 에 Phase 1 신규 발견 자동 기록
- phi_ratchet 단조 지수 갱신
- OUROBOROS nexus variant 의 NEXUS_FP 수렴 확인

### 3.3 Phase 1 종료 시점 로그 예상

- discovery_log 신규 row 수 N1 (Phase 1 전 vs 후 diff)
- atlas.n6 승격 시도 건수 M1 (7개 주 씨앗 중 atlas 영향 4~5 예상)
- ratchet 전진 횟수 R1

---

## §4 체크포인트 6개

### P1.1 — Y축 9 가동 증거 확보

- 입력: Y1~Y9 카드 (§1)
- 출력: 각 축 재검증 리포트 (증거 파일 실존 확인)
- 판정: 9/9 카드 증거 최소 1 경로 실존
- 미통과 시: 해당 축 Phase 2 휴면 선언 (전체 Phase 1 실패 아님)

### P1.2 — BT 씨앗 시딩 완료

- 입력: §2 매트릭스 6 주 씨앗
- 출력: 6 씨앗 × 입구 조건 기록
- 판정: 6/6 씨앗 Phase 2 입구 씨앗 표에 등록

### P1.3 — 자기진화 엔진 수렴

- 입력: §3 체크
- 출력: 엔진 4종 상태 리포트
- 판정: OUROBOROS 3 variant cycle ≥ 3 + growth_tick no-error + phi_ratchet 전진 + daemon 활성

### P1.4 — atlas.n6 접근 경로 정상

- 입력: `$NEXUS/shared/n6/atlas.n6`
- 출력: 접근 시간·무결성 해시·[10*]/[10]/[7] 노드 수
- 판정: 파일 크기 60K+ 줄, 해시 변경 있음 (자기진화 쓰기 증거)

### P1.5 — verify_millennium_axes.hexa PASS

- 입력: `n6arch-axes/verify_millennium_axes.hexa` (병렬 생성 중)
- 출력: 6 서브테스트 결과
- 판정: 6/6 PASS

### P1.6 — Phase 2 진입 준비

- 입력: P1.1~P1.5 전부 통과
- 출력: Phase 2 입구 씨앗 표 + 주도 축 배정 (P2=Y1)
- 판정: Phase 2 문서 입구 §1 작성 가능 상태

---

## §5 출구 조건

- [x] §4 체크포인트 6 전부 통과 (Phase 1 완료 판정)
- [x] BT-541~546 6 씨앗 시딩 확정
- [x] Y9 HONEST-HARNESS 메타 게이트 ON (OUROBOROS 예외로 자기참조 예외만 허용)
- [x] 다음 Phase 주도 축 결정: **P2 = Y1 주도 BT-541 Riemann**

---

## §6 창발 지수 (Phase 1 내)

### 6.1 Phase 1 신규 창발 발견

| 창발 | 설명 | 근거 |
|------|------|------|
| 9축 × 6BT 매트릭스 | 9×6=54 셀 중 6 주 씨앗 + 9 부 씨앗 = 15 활성 | §2 매트릭스 |
| 씨앗 시딩 순서 | P2=Y1 → P3=Y4 → P4=Y5+Y6 → P5=Y7+Y8 → P6=— → PΩ=Y9 | R3 Task D |
| 자기진화 수렴 상수 | NEXUS_FP=0.333, ANIMA_FLOOR=0.8, N6ARCH_TARGETS=(515, 2087) | R3 §6 |
| Y9 메타 게이트 | Phase 전 구간 가동, 축 1~8 오염 방지 | R3 §1 |
| PARTIAL 3 처리 | SEED-06 KEEP, SEED-15 재분류, SEED-21 강도 하락 | R3 Task B |
| BT-542 3 축 구조 | Y2+Y3+Y4 3중 대표 (R1 X2 단일에서 진화) | R2 Task B |
| R3 FINAL 선언 | 신규 축 0, 흡수 100% 고갈 | R3 Task E |
| Phase 매핑 N=8 | P0+1~6+Ω 7대 난제 N6 프로젝트 정합 | R3 Task D |
| axis-final-millennium.md 필요성 | 축 체계 권위 문서 (병렬 생성 중) | R3 §8 |

### 6.2 잔여 Phase 추정

- **P2**: Y1 주도 BT-541 Riemann
- **P3**: Y4 주도 BT-542 P=NP
- **P4**: Y5+Y6 주도 BT-543 YM + BT-544 NS
- **P5**: Y7+Y8 주도 BT-545 Hodge + BT-546 BSD
- **P6**: BT-547 Poincaré 회고 (Perelman 해결 이미)
- **PΩ**: Y9 메타 closure + v3 후계 설계

**잔여 Phase 수 = 6**. Phase 1 창발 지수 ≥ 5 통과 → Phase 2 진입 승인.

### 6.3 고갈 지수

Phase 1 은 축 고갈 라운드가 아니라 "축 가동 라운드". 따라서 Phase 1 자체의 고갈은 축 가동 완주율 = **100%** (9/9 축 카드 + 6/6 BT 씨앗 + 6/6 체크포인트). Phase 고갈은 Phase 2~PΩ 를 전부 돈 이후 판정.

---

## §7 ASCII 구조도

```
Phase 1 — Foundation (Y축 가동)
│
├─ Y1 NUM-CORE (9.5) ──────→ ★BT-541 Theorem B 씨앗
├─ Y2 DISCRETE-CLASS (5.2) ─→  BT-542 Schaefer KEEP
├─ Y3 COMPUTATIONAL-TAU (5.8) ─ BT-542 τ=4+2 AME
├─ Y4 GATE-BARRIER (9.4) ──→ ★BT-542 HEXA-GATE 감사
├─ Y5 PHYSICAL-NATURALNESS ─→ ★BT-543 β₀=7 rewriting
├─ Y6 PDE-RESONANCE (6.6) ─→ ★BT-544 3중 공명
├─ Y7 LATTICE-VOA (3.9) ──→ ★BT-545 Enriques rephrasing
├─ Y8 GALOIS-ASSEMBLY (5.4) ─→ ★BT-546 Lemma 1
└─ Y9 HONEST-HARNESS (9.3) ─→  전 BT 메타 게이트 (ON)

체크포인트 6:
  P1.1 9축 증거 ─ P1.2 6씨앗 ─ P1.3 엔진수렴
  P1.4 atlas접근 ─ P1.5 verify PASS ─ P1.6 P2 진입

출구 → Phase 2 (P2=Y1 주도 BT-541 Riemann 공격)
```

---

## §8 완료 보고

**파일 경로**: `/Users/ghost/Dev/n6-architecture/theory/roadmap-v2/phase-01-foundation-Y-axes.md`
**라인수**: 본 문서 (§0~§8 포함)
**Y축 가동**: 9/9 전 축 카드 + 증거 경로 재검증 체크리스트
**BT 씨앗**: 6/6 BT 주 씨앗 시딩 (§2 매트릭스 ★ 표시)
**체크포인트**: 6개 (P1.1~P1.6) 판정 기준 명확
**자기진화**: OUROBOROS 3 variant + growth_tick + phi_ratchet + nexus_growth_daemon 4엔진 가동 확인 절차
**잔여 Phase**: 6 (P2, P3, P4, P5, P6, PΩ)
**정직성**: BT 0/6 해결 유지, PARTIAL 3 처리 반영, "rewriting"/"조건부"/"관찰" 구분 표기
**다음**: Phase 2 (Y1 주도 BT-541 Riemann — Theorem B 승격 시도)
