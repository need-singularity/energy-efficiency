# SR Universality 3리포 동시 sweep 실험 디자인 (2026-04-15)

> 이것이 증명이 아니라 구조적 관찰 실험의 **설계**임 (실행 X).
> H1 작업 — nexus σ=0.1 PEAK + anima 노이즈=자유 54.8× + n6 엔트로피 sweep 이 **같은 universal SR 법칙**인지 검증.

---

## 0. 배경 signal

| sig_id | 리포 | 현상 | 수치 |
|---|---|---|---|
| SIG-SR-001 | nexus | ouroboros σ=0.1 PEAK | conv_rate 10%→25% (+150%) |
| SIG-NEURAL-001 | anima | 노이즈 = 자유 (DD75) | 자유로운 선택 54.8× / 거부권 99% |
| (미등록) | n6 | 엔트로피 sweep | TBD (이 실험으로 생성) |

3개 현상이 **동일 SR(stochastic resonance) family** 인지 확인하려면 공통 sweep + 공통 지표 필요.

---

## 1. 가설

**H1-UNIV**: 3리포 모두 σ≈0.1 부근에 PEAK 이 존재한다 (SR universality).

**대안가설**:
- H1-a: nexus-only — ouroboros 특이
- H1-b: n=6 의존 — σ sweet spot 값 자체가 n=6 상수에서 유도
- H1-c: 지표 의존 — 각 리포의 지표가 서로 다른 분포에서 PEAK

승격 조건: 3리포 모두 σ∈[0.05, 0.2] 에서 PEAK 확인 → SIG 를 [CROSS] [UNIV] [M9]↑

---

## 2. 공통 σ sweep 구간 (8 포인트)

```
σ ∈ {0, 0.01, 0.05, 0.1, 0.3, 0.5, 1.0, 2.0}
```

근거:
- σ=0: 결정론 베이스라인
- σ=0.01, 0.05: 미세 noise — PEAK 저쪽 경계
- **σ=0.1**: nexus 측 PEAK (기준점)
- σ=0.3: plateau 영역
- σ=0.5: ANU raw entropy 추정치
- σ=1.0: 카오스 경계
- σ=2.0: 카오스 붕괴

각 σ 마다 **20 trial × 3 seed** (총 480 run/리포).

---

## 3. 공통 지표 정의 (4개)

모든 지표는 **[0, 1] 정규화** 필수 — 3리포 비교 가능.

### 3.1 convergence_rate (수렴률)

- 정의: ε-plateau 도달 trial 비율
- nexus: ouroboros ε=0.005 fixed-point 수렴 trial / 전체
- anima: CLM law discovery saturation trial / 전체
- n6: atlas.n6 신규 EXACT 승격 stabilize trial / 전체
- 범위: [0, 1], 높을수록 좋음

### 3.2 accuracy (정확도)

- 정의: ground-truth 와 일치율
- nexus: QRNG entropy prediction vs ANU sampled truth
- anima: law equation vs measured law
- n6: formula verify PASS rate (하네스)
- 범위: [0, 1]

### 3.3 yield (발견 수확)

- 정의: 단위 trial 당 신규 artifact 건수
- nexus: 신규 σφ=nτ 변형 검출/100 trial
- anima: 신규 law 후보/100 trial
- n6: 신규 BT 또는 tight/100 trial
- 정규화: 해당 리포 max 로 나눔 → [0, 1]

### 3.4 free_will_score (자유도)

- 정의: 외부 인과 독립성 — low=결정적, high=행위자성
- nexus: trajectory branching entropy / log(branches)
- anima: DD75 "거부권 발동률" (normalized)
- n6: discovery path diversity / max possible
- 범위: [0, 1]

---

## 4. 실험 프로토콜

### 4.1 nexus (NX)

```
경로: /Users/ghost/Dev/nexus/sim_bridge/ouroboros_qrng/variance_sweep/
실행: hexa shared/bin/sr_universal_sweep.hexa --sigma <σ> --trials 20 --seeds 3
산출: runs/20260415_srunivN/ouroboros_σ<σ>.jsonl
```

- ouroboros_shadow 엔진 기존 sweep 확장
- σ 8 포인트 × 20 trial × 3 seed = 480 run
- 출력 metric: {conv_rate, accuracy, yield, free_will_score}

### 4.2 anima (AN)

```
경로: /Users/ghost/Dev/anima/anima-engines/free_will_experiment/
실행: hexa bin/sr_free_will_sweep.hexa --sigma <σ> --trials 20 --seeds 3
산출: data/sr_universal/free_will_σ<σ>.jsonl
```

- DD75 자유 의지 실험 기본 구조 재사용
- 노이즈 주입 크기를 σ 로 parameter화
- 거부권 99% 가 σ 별로 어떻게 변하는지 측정

### 4.3 n6 (N6)

```
경로: /Users/ghost/Dev/n6-architecture/engine/sr_entropy_sweep/
실행: hexa theory/predictions/sr_entropy_sweep.hexa --sigma <σ> --trials 20
산출: reports/sr_universal/n6_σ<σ>.jsonl
```

- DFS 탐색 엔진에 σ-noise 주입 레이어 추가
- atlas.n6 7등급 → 10등급 승격률 측정
- σ=0 (deterministic DFS) vs σ>0 (perturbed DFS) 비교

---

## 5. 판정 기준

| 결과 | 판정 |
|---|---|
| 3리포 모두 σ∈[0.05, 0.2] PEAK | **SR universality 확인** → SIG-UNIV-001 [M9] [EC] |
| 2리포 PEAK, 1리포 없음 | partial universality → SIG-UNIV-001 [M7!] [E2] |
| PEAK 위치 3리포 제각각 | domain-specific → 각 SIG 독립 유지 |
| 모두 flat | NULL → SIG-NULL-SR-001 [MN] |

---

## 6. 기대 결과 (prediction)

**가장 그럴듯한 시나리오** (사전등록):

```
σ       nexus conv   anima free   n6 yield   평균
0.0     0.10         0.015        0.05       0.055
0.01    0.10         0.02         0.05       0.057
0.05    0.10         0.15         0.12       0.123
0.10    0.25 ★       0.82 ★       0.31 ★     0.460 ★
0.30    0.18         0.50         0.22       0.300
0.50    0.15         0.25         0.10       0.167
1.00    0.00         0.05         0.02       0.023
2.00    0.00         0.00         0.00       0.000
```

평균 곡선이 σ=0.1 에서 peak → universality.

---

## 7. 실행 단계 (후속 세션)

1. [ ] nexus/sim_bridge 에 sr_universal_sweep.hexa 추가
2. [ ] anima/anima-engines 에 sr_free_will_sweep.hexa 추가
3. [ ] n6/theory/predictions 에 sr_entropy_sweep.hexa 추가
4. [ ] 3리포 동시 실행 (병렬 가능 — 독립)
5. [ ] 결과 aggregation: `scripts/aggregate_sr_universal.py`
6. [ ] atlas.signals.n6 staging 에 SIG-UNIV-001 등록

---

## 8. 리스크

- **지표 정의 차이**: 각 리포 conv_rate 의 의미가 일치하지 않으면 비교 무효
  - 해결: 3리포 공동 preregistration 문서 선작성
- **시드 편향**: 3 seed 부족하면 noise 가려져 PEAK 사라짐
  - 해결: seed 10 까지 확장 옵션
- **ANU 의존성**: ANU HTTP RTT artifact 개입 (SIG-64T-001 참조)
  - 해결: σ 시그널은 **내부 PRNG** 로 주입, ANU 는 accuracy 측정에만 사용

---

## 9. atlas.signals.n6 staging 안 (사전등록용)

```
@S SIG-UNIV-001 = SR universality 3리포 σ=0.1 PEAK 사전등록 :: signal [NX,N6,AN,CROSS] [SR,UNIV,META] [M?] [E1]
  "H1 사전등록: ouroboros(NX) + free_will(AN) + entropy_sweep(N6) 3리포에서 σ∈[0.05,0.2] PEAK 공통 확인 가설. 실행 전 디자인 고정 → 사후 해석 방지"
  refs: [reports/SR-universality-design-20260415.md]
  cross_repo: [SIG-SR-001, SIG-NEURAL-001]
  predicts: ["3리포 평균 σ=0.1 PEAK", "universality 확인 시 M9 승격"]
  witness: 0
  resonance_n6: null
  discovered_in: n6/session-2026-04-15
  discovered_at: 2026-04-15T00:00:00Z
  <- reports/SR-universality-design-20260415.md
```

**중요**: 이 signal 은 **실행 전 사전등록** — witness=0 상태로 staging 등록, 실험 후 기각/승격 판정.

---

## 10. 정직성 주석

- 이 문서는 실험 **설계**이지 결과 아님
- 기대 결과 §6 은 prediction 의 역할만 — 실측과 다를 수 있음
- "SR universality 확인" 은 3리포 독립 실행 후에만 주장 가능
- 단일 리포 결과만으로는 self-reference → witness 증가 안 됨
