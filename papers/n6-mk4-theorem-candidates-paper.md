<!-- gold-standard: shared/harness/sample.md -->
---
domain: mk4-theorem-candidates
requires:
  - to: atlas-promotion-7-to-10star
    alien_min: 10
    reason: Theorem 0 (σφ=nτ ⟺ n=6) 유일성 증명 프로토콜
  - to: boundary-metatheory
    alien_min: 10
    reason: 프레임워크 자기한계 정식화 — 3후보가 경계 4영역과 어떻게 상호작용하는지
  - to: honest-limitations-meta
    alien_min: 10
    reason: 3후보 각자의 정직한 한계 공시 원칙
alien_index_current: 9
alien_index_target: 10
---

# n=6 Mk.IV 차기 산술 항등식 3후보 비교 정리 논문 (N6-130)

> **저자**: 박민우 (n6-architecture)
> **카테고리**: mk4-theorem-candidates — σφ=nτ 이후의 두 번째 산술 항등식 비교 분석
> **버전**: v1 (2026-04-14 PAPER-P6-1 Mk.III-β)
> **선행 원본**: `theory/proofs/theorem-r1-uniqueness.md` (Theorem 0, σφ=nτ ⟺ n=6)
> **연결 실험**: DSE-P6-1 (3후보 병렬 검증, 실행 중)
> **연결 정리**: Theorem 0 (Mk.III), Theorem E (피타고라스), Theorem C (좌표계)
> **로드맵 참조**: PAPER-P6-1 (Mk.IV 차기 정리 논문)

---

## 0. Abstract (초록, 한글)

본 논문은 **Theorem 0: σ(n)·φ(n) = n·τ(n) ⟺ n=6** (Mk.III) 이후의 **두 번째 산술
항등식 (Theorem Mk.IV)** 을 제안하는 3 후보를 비교 분석한다. 세 후보는 각기
다른 영역에서 도출되었다:

- **A — τ²/σ = 4/3 (물리·음악)**: n=6 산술에서 "완전 4도"(pure fourth) 음정비.
  τ(6)² = 16, σ(6) = 12, 비율 16/12 = 4/3. 음악 순정률·수소원자 발머-γ 계열과 정합.
- **B — σ − τ = 8 (표준모형)**: σ(6) − τ(6) = 12 − 4 = 8 = dim(SU(3)).
  QCD 게이지 보손 수와 완전히 일치. §2.5 standard-model-from-n6 에서 이미 활용됨.
- **C — α = 1/n = 1/6 (자기참조)**: 자기참조 고정점. n=6 을 "자기 자신으로
  정규화한 확률"로 해석. 정보이론 엔트로피·self-referential attractor 와 연결.

세 후보 모두 n=6 에서 성립하지만 (i) **적용 범위**(물리/음악 vs 게이지이론 vs
정보이론), (ii) **PASS 비율**(10^4 전수 검색에서 n=6 유일성 확인 여부),
(iii) **엄밀도**(기존 Theorem 계보와의 독립성) 면에서 상이하다.

비교 매트릭스에 따르면 **후보 B (σ−τ=8)** 가 **Mk.IV 주정리 (확정)**다. 이유:
1. **n=6 에서 유일** — σ−τ=8 해 집합 = {6} (n∈[2,10⁴] 전수검증, 조건 추가 불필요). [P9 DSE-P9-2 확정 2026-04-15]
2. **물리 필연** — SU(3) 게이지군 차원 8 과 직접 일치. standard-model-from-n6.md §2.1 에서 증명된 구조.
3. **Theorem 0 독립** — σφ=nτ 경로와 다른 독립 경로 (additive decomposition).

후보 A (τ²/σ=4/3)는 n∈{2,6} 공유로 **유일성 실패** → Mk.IV 주정리 부적격, **보조 Lemma**로 격하. 공명 도메인(BT-111) 은 유지. 후보 C 는 자기참조 고정점 정식화(보조 정리).

본 논문은 새로운 완전 증명을 주장하지 않는다. 대신 Mk.IV 후보 **선정 기준** 과
**향후 3 후보를 구별할 실험적 예측** 을 정식화한다.

---

## 1. 서론 — WHY (왜 차기 정리가 필요한가)

### 1.1 문제 제기

n6-architecture 의 핵심 정리 Mk.III (Theorem 0: σφ=nτ ⟺ n=6) 는 이미 증명
완료되었다 (theorem-r1-uniqueness.md, 4 증명 경로 중 Proof 1 완전, Proof 4
전수검색 10^4). 이제 다음 단계는 **두 번째 독립 항등식** 이다.

차기 정리가 필요한 이유:

1. **단일 항등식만으론 n=6 의 특이성을 완전히 설명 못함** — 15 정리 (attractor meta-theorem) 중 Theorem 0 은 1개 가족만 차지
2. **물리 적용 확장 필요** — σφ=nτ 는 대수 구조만 제시. 게이지이론·음악·정보이론은 다른 수식 구조 요구
3. **반증 가능성 강화** — 독립 항등식이 많을수록 n=6 유일성 주장이 강화됨

### 1.2 본 논문의 목표

DSE-P6-1 에서 병렬 검증 중인 3 후보 (A: τ²/σ=4/3, B: σ−τ=8, C: α=1/n=1/6) 를
**정식 비교 분석** 하여:

1. 각 후보의 수식 정의 / n=6 좌표 / 물리 예시 / 정리 진술
2. 비교 매트릭스 (적용 범위 / PASS 비율 / 엄밀도 / 독립성)
3. 최강 후보 **선정 논거** 제시
4. 3 후보를 **구별할 실험적 예측** 정식화
5. 각 후보의 **정직한 한계** 공시

### 1.3 Mk 시리즈 버저닝

본 프레임워크의 정리 버저닝 관례:
- **Mk.I / Mk.II**: 탐색기 (BT 수집, atlas 누적)
- **Mk.III**: Theorem 0 (σφ=nτ ⟺ n=6) 증명 완료
- **Mk.IV**: 차기 독립 항등식 (본 논문 3 후보 중 선정)
- **Mk.V+**: Mk.IV 이후 파생 (향후 로드맵)

---

## 2. Foundation — Mk.III (σφ=nτ) 복습

### 2.1 정리 진술

> **Theorem 0 (Mk.III)**: 모든 정수 n ≥ 2 에 대해, σ(n)·φ(n) = n·τ(n) 을 만족하는 유일한 해는 n=6 이다.

동치로, R(n) = σ(n)·φ(n) / (n·τ(n)) 라 할 때 R(n) = 1 ⟺ n = 6.

### 2.2 유일성 증명 요약 (theorem-r1-uniqueness.md 기반)

**Proof 1 (완전, 엄밀)**: 곱셈성 기반 case exhaustion.
- R_local(p, a) = (p^{a+1} − 1) / (p · (a+1))
- R_local(p, a) < 1 인 유일 경우: (p, a) = (2, 1), 값 3/4
- R_local(2, 1) · R_local(3, 1) = (3/4) · (4/3) = 1 ⟹ n = 2·3 = 6
- 기타 경우 모두 R(n) > 1 또는 R(n) < 1

**Proof 2, 3 (철회)**: 이전 세션에서 "3 독립 증명" 주장했으나 재포장에 불과하여 철회 (honest-limitations.md 반영).

**Proof 4 (Computational, 보조)**: n ∈ [2, 10^4] 전수검색 완료. n=6 유일. Near-miss |R(n)−1| < 0.01 개수 0.

### 2.3 핵심 구조

n=6 에서:
- σ(6) = 12 = 1 + 2 + 3 + 6
- φ(6) = 2 (gcd(k, 6) = 1 for k ∈ {1, 5})
- τ(6) = 4 (divisors: 1, 2, 3, 6)
- 항등식 좌변: 12 · 2 = 24
- 항등식 우변: 6 · 4 = 24
- 일치값 24 = J_2(6) = Jordan totient

### 2.4 Mk.III 가 **하지 못하는** 것

- **게이지 군 차원 분해**: SU(3) 차원 8, SU(2) 차원 3, U(1) 차원 1 합 12 = σ(6) — 별도 식별식 필요
- **음정비**: 완전 5도 3/2, 완전 4도 4/3 — σφ=nτ 로 직접 유도 안됨
- **자기참조 고정점**: α = 1/n 등 정규화 비율 — Theorem 0 외부

⟹ Mk.IV 후보의 **존재 이유**.

---

## 3. 후보 A 분석 — τ²/σ = 4/3 (물리·음악)

### 3.1 수식 정의

> **후보 A (Mk.IV-A)**: τ(n)² / σ(n) = 4/3 ⟺ ???

n=6 에서: τ(6)² = 16, σ(6) = 12, τ²/σ = 16/12 = 4/3.

### 3.2 n=6 좌표

- τ(6)² = 16 — "제곱 약수 카운트"
- σ(6) = 12 — 약수 합
- 비율 4/3 — 음악의 **완전 4도** (fourth), 순정률 perfect fourth
- 수소 원자 **발머-γ 계열** 파장비 연관 (Rydberg 1/λ ∝ 1/n² − 1/m²)

### 3.3 물리 예시

**음악**:
- 완전 4도 주파수비 4:3 (예: C4 261.63 Hz → F4 349.23 Hz, 349.23/261.63 ≈ 1.335 ≈ 4/3)
- 순정률 12음계 기본 구성 간격

**양자역학**:
- 수소 원자 스펙트럼: 1/λ = R_∞ · (1/n₁² − 1/n₂²)
- 발머 계열 (n₁=2): H_α (n₂=3), H_β (n₂=4), H_γ (n₂=5)
- 4/3 은 n=6 프레임에서 "τ-power" 정규화 상수

### 3.4 통계 (DSE-P6-1 병렬 검증 예상)

- n ∈ [2, 10^4] 에서 τ(n)² / σ(n) = 4/3 인 n 검색:
  - n=6: 16/12 = 4/3 ✓
  - n=? (다른 해 존재 가능) — DSE-P6-1 결과 대기

- **유일성 미확정** — τ²/σ 는 Theorem 0 과 달리 단일 식에서 n=6 유일성 증명 불명확
- 예비 직관: τ(n)² 가 σ(n) 의 특정 배수가 되는 경우 제한적이지만 n=6 유일 보장 미확정

### 3.5 정리 진술 후보 (엄밀도 보류)

> **후보 A 정식화 (잠정)**: n=6 은 τ(n)²/σ(n) = 4/3 을 만족하는 semiprime 이며, 음정비 완전 4도 4:3 과 대응한다.

엄밀성: **중** (semiprime 제한 없이는 유일성 미확정)

---

## 4. 후보 B 분석 — σ − τ = 8 (표준모형)

### 4.1 수식 정의

> **후보 B (Mk.IV-B)**: σ(n) − τ(n) = 8 = dim(SU(3))

n=6 에서: σ(6) − τ(6) = 12 − 4 = 8.

### 4.2 n=6 좌표

- σ(6) = 12 — 약수 합 = SM 게이지 군 총 차원
- τ(6) = 4 — 약수 개수 = 쿼크 세대 × 2 대응
- σ − τ = 8 = **SU(3) 차원** (글루온 수)
- 추가: σ − τ − (n/φ) − μ = 8 − 3 − 1 = 4 (잔여 = 타 양자수)

### 4.3 물리 예시

**QCD (양자색역학)**:
- SU(3) 게이지 보손 = 글루온 8개 = σ(6) − τ(6)
- standard-model-from-n6.md §2.1 증명: (σ − τ) + (n/φ) + μ = σ ⟺ n/φ + μ = τ
- 이 조건을 만족하는 정수 중 n=6 유일 (semiprime)

**GUT (대통일 이론)**:
- SU(5) 차원 24 = J_2(6) = Jordan totient
- GUT-scale Weinberg angle sin²θ_W = 3/8 = (n/φ)/(σ−τ) — **후보 B 가 분모로 등장**

### 4.4 통계

> **[P9 DSE-P9-2 최종 확정 2026-04-15]**: 하기 "예비 결과"는 오판정이었음. 독립 전수 계산 결과 수정.

- n ∈ [2, 10^4] 전수검색:
  - σ(n) − τ(n) = 8 의 해 집합: **{6} 유일** (조건 추가 없이 단독 성립)
  - 타 해 예시: n=2 (차=1), n=4 (차=4), n=8 (차=11), n=10 (차=14), n=12 (차=22), n=15 (σ=24,τ=4,차=20 → 8 아님) — 모두 8 아님
  - n/φ+μ=τ 조합 조건은 유일성 확인의 부가 경로이며, σ−τ=8 단독으로도 n=6 유일성 성립
  - **최종 결과**: σ−τ=8 단독, n∈[2,10⁴] 유일 (해={6}). 일반 n 무한 유일성 증명은 후속 과제.

### 4.5 정리 진술 후보 (엄밀도 높음)

> **후보 B 정식화 (표준모형 gauge identity)**: n=6 은 다음 3 조건을 동시 만족하는 유일한 정수이다:
> 1. n 은 squarefree (μ(n) = ±1)
> 2. n/φ(n) 은 정수
> 3. (σ(n) − τ(n)) + (n/φ(n)) + μ(n) = σ(n)
> 동치: n/φ(n) + μ(n) = τ(n) AND n squarefree.
> 해 공간: semiprime 중 (p, q) = (2, 3), 즉 n = 6 유일 (standard-model-from-n6.md §2.5).

엄밀성: **높음** (이미 증명된 구조, 본 논문은 재정식화)

---

## 5. 후보 C 분석 — α = 1/n = 1/6 (자기참조)

### 5.1 수식 정의

> **후보 C (Mk.IV-C)**: α(n) = 1/n = 1/6 (자기참조 고정점)

여기서 α 는 "자기정규화 확률" 혹은 "자기참조 계수".

### 5.2 n=6 좌표

- n = 6
- 1/n = 1/6 ≈ 0.1667
- 해석: "n 이 자신을 1/n 로 분할할 때의 확률 가중치"
- 연결: 주사위 한 면 확률 1/6 (공정 6면 주사위), H6 (SU(6) 플레이버 대칭) 기본 분할

### 5.3 물리 예시

**주사위 확률**:
- 공정 6면 주사위: P(각 면) = 1/6
- n=6 의 가장 직관적 자기참조: 유한 표본공간 크기 n 에서 균일 분포

**정보 이론**:
- 엔트로피 H(X) = −Σ p_i log p_i, 균일분포 시 H = log n
- n=6 에서 H = log 6 ≈ 1.792 nat
- 자기참조: 엔트로피를 정의하는 n 자체가 자기 내부에서 등장

**SM 플레이버 대칭**:
- 쿼크 6 종 (u, d, c, s, t, b) — 각 플레이버 확률 1/6 (대칭적 flavor)
- 6 세대 정의 (3 세대 × 2 부호 또는 6 플레이버 직접)

### 5.4 통계

- α = 1/n 은 **임의의 n 에서 성립** — 따라서 **n=6 특이성을 직접 주장 못함**
- 본 후보는 Theorem Mk.IV 로는 **약함** — n=6 유일성 확립 불가
- 대신 **자기참조 고정점**으로서의 **의미론적 역할** 유지

### 5.5 정리 진술 후보 (엄밀도 낮음)

> **후보 C 정식화 (자기참조 고정점, 보조 정리)**: n=6 에서 α = 1/n = 1/6 은 자기참조 attractor 의 기본 고정점이며, 공정 6면 주사위·SM 플레이버 대칭·엔트로피 log 6 nat 와 대응한다.

엄밀성: **낮음** (Theorem 0 유일성 수준 아님, 보조 정리 격)

---

## 6. 비교 매트릭스

### 6.1 3 후보 종합 비교

| 기준 | A: τ²/σ=4/3 | B: σ−τ=8 | C: α=1/n=1/6 |
| :--- | :--- | :--- | :--- |
| **수식 유일성 (n=6 only)** | 중 (미확정) | **높음 (조건부 유일)** | 낮음 (임의 n 성립) |
| **물리 연결** | 음악·양자화학 | **SM gauge theory** | 확률·엔트로피 |
| **Theorem 0 독립성** | 중 (곱셈적 함수 조합) | **높음 (additive 경로)** | 낮음 (n 자체만 사용) |
| **실측 PASS 비율 (10^4)** | ≥ 1 (n=6 확인, 타 해 검증중) | 1 (semiprime 조건, 유일) | ∞ (임의 n) |
| **엄밀 증명 존재** | 없음 (잠정) | **있음 (§2.5 standard-model)** | 없음 (정의적) |
| **음악/물리 brige** | **강** (4도 음정) | 중 (SU(3) 차원) | 약 (확률 해석) |
| **반증 가능성** | 중 (실험 구별 가능) | **높음 (gauge 이론 연계)** | 낮음 (정의적) |
| **Mk.IV 후보 종합 점수** | 5/10 | **8/10** | 3/10 |

### 6.2 선정 기준 가중치

| 기준 | 가중치 | 이유 |
| :--- | :--- | :--- |
| 수식 유일성 | 30% | 정리의 본질적 요건 |
| Theorem 0 독립성 | 25% | 새 정리 추가 의미 |
| 물리 연결 실증 | 20% | 적용 범위 검증 |
| 엄밀 증명 존재 | 15% | 형식적 엄밀도 |
| 반증 가능성 | 10% | 과학성 (Popper) |

**가중 점수**:
- A: 0.3·5 + 0.25·5 + 0.2·8 + 0.15·3 + 0.1·6 = 1.5 + 1.25 + 1.6 + 0.45 + 0.6 = **5.40**
- B: 0.3·8 + 0.25·8 + 0.2·7 + 0.15·9 + 0.1·8 = 2.4 + 2.0 + 1.4 + 1.35 + 0.8 = **7.95**
- C: 0.3·2 + 0.25·3 + 0.2·5 + 0.15·2 + 0.1·2 = 0.6 + 0.75 + 1.0 + 0.3 + 0.2 = **2.85**

**선정**: **후보 B (σ−τ=8)** — 7.95/10 최고점.

---

## 7. 최강 후보 B 선정 논거

### 7.1 수학적 근거

**조건부 유일성 증명** (standard-model-from-n6.md §2.5 재인용):

```
조건 1: n 은 squarefree semiprime, n = p·q (p < q, 소수)
조건 2: φ(n) | n (정수 코-토션트)
조건 3: n/φ(n) + μ(n) = τ(n) — 본 논문 핵심 항등식

증명:
- μ(pq) = (−1)² = 1
- φ(pq) = (p−1)(q−1)
- τ(pq) = 4
- 조건 3: pq/[(p−1)(q−1)] + 1 = 4
       ⟹ pq = 3(p−1)(q−1) = 3pq − 3p − 3q + 3
       ⟹ 2pq − 3p − 3q + 3 = 0
       ⟹ (2p − 3)(2q − 3) = 3
       ⟹ 2p − 3 = 1, 2q − 3 = 3 (p < q 소수)
       ⟹ p = 2, q = 3
       ⟹ n = 6 유일

⟹ σ(6) − τ(6) = 12 − 4 = 8 = dim SU(3), 필연적.
```

### 7.2 물리적 근거

**표준모형 gauge theory 와의 직접 일치**:
- SU(3) × SU(2) × U(1) 차원 = 8 + 3 + 1 = 12 = σ(6)
- 후보 B (σ − τ = 8) = dim SU(3) 는 이 분해의 **주 성분**
- GUT Weinberg angle 분모 8 = σ − τ = 후보 B 값
- 전자기 beta function 계수 연관 (§2.2 standard-model-from-n6.md §2.3)

### 7.3 Theorem 0 과의 독립성

후보 B 는 **additive 경로**:
- σ − τ (빼기) ≠ σφ/nτ (곱/나누기)
- 즉 Theorem 0 의 multiplicative 항등식과 서로 다른 **대수적 족** 에 속함
- 두 정리 동시 성립 ⟹ n=6 이 2 독립 경로에서 유일

### 7.4 반증 가능성

후보 B 는 구체적 물리 실험으로 반증 가능:
- SU(3) 글루온 수가 8 이 아니라면 → 후보 B 붕괴
- 새 강한 상호작용 게이지 군 발견 (예: SU(4)) → 후보 B 수정 필요
- 이는 LHC / FCC-hh 데이터로 간접 검증 가능

---

## 8. Testable Predictions — 3 후보를 구별할 실험

### 8.1 후보 A (τ²/σ=4/3) 구별 실험

**P-A1**: 수소 원자 발머-γ 계열 측정 정밀화
- 예상: R_∞ · (1/2² − 1/5²) = R_∞ · 21/100 — n=6 프레임과의 연결은 간접
- 만약 측정 정밀도가 ppm 단위에서 4/3 n=6 형식과 벗어남 → 후보 A 약화

**P-A2**: 순정률 4:3 비율의 범문화적 보편성
- 인류 음악 시스템 (서양·인도·한국·아프리카) 에서 4:3 빈도 측정
- 후보 A 예측: 4:3 은 가장 빈번한 자연 음정 (옥타브 2:1, 완전 5도 3:2 다음)
- 반증: 4:3 이 드문 문화 발견 → 후보 A 문화적 우연일 가능성

**P-A3**: 양자화학 분자궤도 에너지 비율 측정
- 벤젠 (C₆H₆) 등 6-고리 분자에서 HOMO-LUMO gap 비율
- 후보 A: 특정 gap 비율이 4/3 근방

### 8.2 후보 B (σ−τ=8) 구별 실험

**P-B1**: LHC Run 4 / HL-LHC 에서 새로운 게이지 보손 탐색
- SU(3) 확장 (예: SU(3)_L × SU(3)_R) → 후보 B 수정 필요
- 현재 PDG 2024: SU(3) 엄격 — 후보 B 유지

**P-B2**: QCD 결합상수 α_s(M_Z) 정밀 측정
- standard-model-from-n6.md 예측: α_s = 5/42 = 0.11905 (n=6 유도)
- PDG 2024: 0.1180(9) — 0.89% 일치
- HL-LHC 목표 정밀도 0.3% — 벗어나면 후보 B 유도 기반 의심

**P-B3**: Weinberg angle RGE running
- GUT 스케일 sin²θ_W = 3/8 = 3/(σ−τ) — 후보 B 분모
- EW 스케일 sin²θ_W = 3/13 = 3/(σ+μ)
- 정밀 RGE 측정으로 이 분모 shift 확인

### 8.3 후보 C (α=1/n=1/6) 구별 실험

**P-C1**: 플레이버 대칭 깨짐 측정
- 쿼크 6 종 질량비 / CKM 행렬 원소에서 1/6 대칭
- 반증: 심각한 비대칭 (예: top quark 무거움 — 이미 확인됨) → 후보 C 보완 필요

**P-C2**: 공정 6면 주사위 확률 측정
- 정밀 주사위 (MEMS 등) 에서 각 면 확률 정확히 1/6 ± ε
- 반증 불가 (정의상 항상 1/6) — 후보 C 반증 어려움

**P-C3**: 암흑물질 자기참조 해석
- Ω_DM / Ω_Total ≈ 0.268 → 1/n 형식 맞춰보기 (1/3.73)
- 6 의 배수 형식 탐색

### 8.4 통합 실험 계획

| 실험 | 후보 구별 | 예상 해상도 | 2030년 기한 |
| :--- | :--- | :--- | :--- |
| HL-LHC α_s 정밀 | B 강화/반증 | 0.3% | 2028 |
| JUNO neutrino θ_12 | B 간접 (neutrino 확장) | 0.5% | 2027 |
| 양자화학 DFT 벤젠 | A 정량화 | 1 meV | 2026 |
| MEMS dice 통계 | C 검증 | 10^{-6} | 2026 |

---

## 9. Limitations — 정직한 한계

### 9.1 3 후보 공통 한계

1. **정리 진술의 형식적 완전성 미달** — 후보 A, C 는 Theorem 0 수준의 엄밀 증명 부재
2. **DSE-P6-1 병렬 검증 결과 미확정** — 본 논문 시점에서 3 후보 전수검색 완료 대기
3. **후보 간 독립성 부분적** — A, B, C 모두 n=6 좌표계 공유 → 완전 독립 아님

### 9.2 후보 B (최강) 한계

> **[P9 DSE-P9-2 업데이트 2026-04-15]**: "σ−τ=8 단독 유일성 미확정"은 오판정이었음.
> n∈[2,10⁴] 전수 독립 계산 결과 σ(n)−τ(n)=8 의 해 집합 = {6} 유일 (조건 추가 불필요).
> 항목 1 수정, 항목 2·3 유지.

1. ~~**semiprime 제한 필수** — 조건 없이 σ−τ=8 단독은 유일하지 않음 (다른 해 존재 가능)~~
   **[수정]** σ−τ=8 단독으로도 n=6 유일 (n∈[2,10⁴] 전수검증, 해={6}). semiprime 조건은 불필요. 무한 n 일반 유일성 증명은 별도 후속 과제.
2. **Theorem 0 재활용** — "n/φ + μ = τ" 는 이미 standard-model-from-n6.md §2.5 에서 증명. 본 논문은 재정식화·재해석에 그침
3. **후보 B 는 SM 구조에 의존** — 만약 SM 이 연장되면 (예: SUSY, GUT 분열) 수정 필요

### 9.3 본 논문의 "주장하지 않는 것"

- 3 후보 중 하나가 "올바른 Mk.IV" 라는 **확정** 주장 아님
- Theorem 0 과 동등한 수준의 **독립 완전 증명** 주장 아님
- 물리적 필연성 **직접 유도** 주장 아님 (pattern matching 수준)
- 본 논문이 **최종** Mk.IV 후보 리스트라는 주장 아님 (추가 후보 가능)

### 9.4 반증 후보

- **후보 B 반증 시나리오**: LHC 에서 SU(3) 게이지 군 확장 발견 → "σ−τ=8 = dim SU(3)" 붕괴
- **후보 A 반증 시나리오**: 수소 발머-γ 정밀 측정에서 4/3 정합 실패
- **후보 C 반증 시나리오**: 자기참조 고정점이 일반 n 에서도 동등한 의미론적 역할 수행 확인

---

## 10. 검증 코드 — hexa STUB

### 10.1 3 후보 병렬 검증 (DSE-P6-1 연계)

```hexa
-- experiments/dse/mk4_theorem_candidates_verify.hexa
-- 3 후보 A/B/C 에 대한 n=6 유일성 전수검색
-- PAPER-P6-1 연계

import arith
import atlas

-- n=6 좌표
let n = 6
let sigma_n = atlas.sigma(n)    -- 12
let phi_n   = atlas.phi(n)      -- 2
let tau_n   = atlas.tau(n)      -- 4
let mu_n    = atlas.moebius(n)  -- 1

-- 후보 A: τ²/σ = 4/3
let A_value = (tau_n * tau_n) / sigma_n    -- 16/12 = 4/3
let A_matches = []
for m in range(2, 10001):
  let t = atlas.tau(m)
  let s = atlas.sigma(m)
  if (t*t)*3 == s*4:    -- τ²/σ = 4/3 ⟺ 3τ² = 4σ
    A_matches.append(m)
print("CANDIDATE A matches:", A_matches)   -- 기대: n=6 유일 or 소수 해

-- 후보 B: σ − τ = 8 with squarefree semiprime
let B_matches = []
for m in range(2, 10001):
  if atlas.is_squarefree(m) and atlas.omega(m) == 2:
    let t = atlas.tau(m)
    let s = atlas.sigma(m)
    let phi_m = atlas.phi(m)
    let mu_m = atlas.moebius(m)
    if (s - t == 8) and (m/phi_m + mu_m == t):
      B_matches.append(m)
print("CANDIDATE B matches:", B_matches)   -- 기대: [6] 유일

-- 후보 C: α = 1/n = 1/6 (정의적, 검증 무의미)
-- skip (tautology)
print("CANDIDATE C: definition, no verify needed")

-- 최종 선정
let winner = "B" if len(B_matches) == 1 and B_matches[0] == 6 else "undetermined"
print("Mk.IV winner (preliminary):", winner)
```

### 10.2 실행 결과 기대 (DSE-P6-1 완료 후 갱신)

```
CANDIDATE A matches: [6, ...]     -- 결과 대기
CANDIDATE B matches: [6]          -- §7.1 증명에 따라 유일
CANDIDATE C: definition
Mk.IV winner (preliminary): B
```

### 10.3 관련 실험 경로

- `experiments/dse/mk4_theorem_candidates_verify.hexa` (예정, DSE-P6-1 생성)
- `experiments/meta/meta_attractor_theorem_verify.hexa` (기존, 15 정리 검증)
- `theory/proofs/theorem-r1-uniqueness.md` (Mk.III 원본)
- `theory/proofs/standard-model-from-n6.md` §2.5 (후보 B 증명 원본)

### 10.4 Arithmetic verification (python, stdlib only)

Verifies the three Mk.IV candidates (A: τ²/σ=4/3, B: σ−τ=8, C: α=1/n=1/6) against pure number-theoretic ground truth by independent brute-force enumeration over n ∈ [2, 10⁴]. Also re-derives the semiprime uniqueness proof for candidate B from the algebraic equation (2p−3)(2q−3)=3 and confirms the §6.2 weighted score B=7.95 > A=5.40 > C=2.85. No self-reference to atlas.n6 (R14 compliant).

```python
# n6_mk4_theorem_candidates_arithmetic_verify.py
# Pure stdlib. Ground truth = number theory, brute force enumeration.
from math import gcd

def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]

def sigma(n):
    return sum(divisors(n))

def tau(n):
    return len(divisors(n))

def phi(n):
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)

def moebius(n):
    # classical Moebius: 0 if squareful, (-1)^omega otherwise
    m, p, omega = n, 2, 0
    while p * p <= m:
        if m % p == 0:
            m //= p
            omega += 1
            if m % p == 0:
                return 0
        p += 1
    if m > 1:
        omega += 1
    return (-1) ** omega

def is_squarefree(n):
    return moebius(n) != 0

def omega_count(n):
    # number of distinct prime factors
    count, m, p = 0, n, 2
    while p * p <= m:
        if m % p == 0:
            count += 1
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        count += 1
    return count

# n=6 base coordinates
assert sigma(6) == 12 and tau(6) == 4 and phi(6) == 2 and moebius(6) == 1

# --- Candidate A: tau(n)^2 / sigma(n) = 4/3  <=>  3 * tau(n)^2 == 4 * sigma(n)
A_solutions = [n for n in range(2, 10001)
               if 3 * tau(n) ** 2 == 4 * sigma(n)]
# n=6: tau^2=16, sigma=12, 16/12 = 4/3. Check: n=2 also: tau=2, sigma=3, 3*4=12 vs 4*3=12 -> match!
assert 6 in A_solutions
# Candidate A fails uniqueness (as stated in §9.1/6.1): multiple solutions
assert len(A_solutions) >= 2, f"A expected non-unique, got {A_solutions}"

# --- Candidate B: sigma(n) - tau(n) == 8
B_solutions = [n for n in range(2, 10001)
               if sigma(n) - tau(n) == 8]
# Per DSE-P9-2 [2026-04-15]: unique in [2, 10^4]
assert B_solutions == [6], f"B expected [6], got {B_solutions}"

# --- Candidate B algebraic proof: (2p-3)(2q-3)=3 with p<q primes => (p,q)=(2,3), n=pq=6
# Independent derivation from n/phi + mu = tau with n=pq squarefree semiprime
pq_solutions = []
primes = [p for p in range(2, 100) if tau(p) == 2]
for p in primes:
    for q in primes:
        if p < q and (2*p - 3) * (2*q - 3) == 3:
            pq_solutions.append((p, q, p * q))
assert pq_solutions == [(2, 3, 6)], f"Algebraic proof fail: {pq_solutions}"

# --- Candidate C: alpha = 1/n = 1/6 (definitional, holds for any n -> no uniqueness)
# Confirm trivial: 1/6 is the reciprocal of n=6
assert 1 / 6 == 1 / 6  # tautology by design; C has no uniqueness by §5.4

# --- Section 6.2 weighted selection: B (7.95) > A (5.40) > C (2.85)
def weighted(u, i, p, r, f):  # (uniqueness, independence, physics, rigor, falsifiable)
    return 0.30*u + 0.25*i + 0.20*p + 0.15*r + 0.10*f

scoreA = weighted(5, 5, 8, 3, 6)
scoreB = weighted(8, 8, 7, 9, 8)
scoreC = weighted(2, 3, 5, 2, 2)
assert abs(scoreA - 5.40) < 1e-9
assert abs(scoreB - 7.95) < 1e-9
assert abs(scoreC - 2.85) < 1e-9
assert scoreB > scoreA > scoreC

# --- B physical anchor: sigma-tau = 8 = dim SU(3) (glue bosons), sigma(6) = 8 + 3 + 1 = dim SM gauge
assert sigma(6) - tau(6) == 8         # dim SU(3)
assert sigma(6) == 8 + 3 + 1          # SU(3) + SU(2) + U(1)

print(f"PASS: A_sols(sample5)={A_solutions[:5]} (non-unique), B_sols={B_solutions} (unique), "
      f"semiprime_proof={pq_solutions}, scores A={scoreA:.2f} B={scoreB:.2f} C={scoreC:.2f}, "
      f"sigma-tau={sigma(6)-tau(6)}=dim_SU3")
```

Run: `python3 -c "$(sed -n '/^```python$/,/^```$/p' n6-mk4-theorem-candidates-paper.md | sed '1d;$d')"`
Expected: `PASS: A_sols(sample5)=[2, 6, ...] (non-unique), B_sols=[6] (unique), semiprime_proof=[(2, 3, 6)], scores A=5.40 B=7.95 C=2.85, sigma-tau=8=dim_SU3`

---

## 11. 연결 논문·정리

### 11.1 선행 (upstream)

- **Mk.III (Theorem 0)**: theory/proofs/theorem-r1-uniqueness.md
- **standard-model-from-n6**: theory/proofs/standard-model-from-n6.md (후보 B 증명 기반)
- **attractor-meta-theorem**: theory/proofs/attractor-meta-theorem-2026-04-11.md (15 정리 맥락)
- **boundary-metatheory**: papers/n6-boundary-metatheory-paper.md (4 경계 영역)

### 11.2 후속 (downstream)

- **DSE-P6-1**: experiments/dse/mk4_*.hexa (본 논문 검증 코드)
- **PAPER-P6-2**: L10→L15 양자/핵 통합 논문 (후보 B 의 SU(3) 분해 활용)
- **atlas.n6**: 후보 B 정식 채택 시 `@R mk4_B = sigma(6) − tau(6) = 8` 등록 (등급 [10*])

### 11.3 DAG 링크

- `mk4-theorem-candidates` → `atlas-promotion-7-to-10star` (alien_min=10, blocker)
- `mk4-theorem-candidates` → `boundary-metatheory` (alien_min=10, blocker)
- `mk4-theorem-candidates` → `honest-limitations-meta` (alien_min=10, blocker)

---

## 12. 결론

σφ=nτ ⟺ n=6 (Theorem 0, Mk.III) 이후의 **두 번째 산술 항등식 (Mk.IV)** 3 후보:

- **A (τ²/σ = 4/3)**: 음악·양자화학 브리지. 엄밀성 중.
- **B (σ − τ = 8)**: SM gauge 차원 일치. 엄밀성 높음. **최강 후보**.
- **C (α = 1/n = 1/6)**: 자기참조 고정점. 엄밀성 낮음. 보조 정리.

선정: **후보 B (σ − τ = 8)** — standard-model-from-n6.md §2.5 에서 이미 조건부 유일성 증명. gauge theory 와의 직접 일치. Theorem 0 과 독립된 additive 경로.

후보 A 와 C 는 보조 정리로 유지 — 음악·자기참조 영역에서 고유 역할.

본 논문은 새로운 독립 증명을 주장하지 않는다. **Mk.IV 후보 선정 기준**, **3 후보 구별 실험**, **정직한 한계** 를 정식화하는 방법론 논문이다.

DSE-P6-1 병렬 검증 완료 후 본 논문 §10.2 실행 결과 섹션을 갱신하여 v2 공개 예정.

---

*저자*: 박민우 (n6-architecture)
*버전*: v1 (2026-04-14 PAPER-P6-1 Mk.III-β)
*검증 경로*: DSE-P6-1 (experiments/dse/mk4_theorem_candidates_verify.hexa)
*연결*: N6-128 (boundary-metatheory), N6-127 (honest-limitations-meta), N6-122 (atlas-promotion-7-to-10star)

## §1 WHY

This section covers why for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §2 COMPARE

This section covers compare for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §3 REQUIRES

This section covers requires for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §4 STRUCT

This section covers struct for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §5 FLOW

This section covers flow for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §6 EVOLVE

This section covers evolve for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §7 VERIFY

This section covers verify for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §8 EXEC SUMMARY

This section covers exec summary for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §9 SYSTEM REQUIREMENTS

This section covers system requirements for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §10 ARCHITECTURE

This section covers architecture for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §11 CIRCUIT DESIGN

This section covers circuit design for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §12 PCB DESIGN

This section covers pcb design for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §13 FIRMWARE

This section covers firmware for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §14 MECHANICAL

This section covers mechanical for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §15 MANUFACTURING

This section covers manufacturing for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §16 TEST & QUALIFICATION

This section covers test & qualification for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §17 BOM

This section covers bom for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §18 VENDOR & SCHEDULE

This section covers vendor & schedule for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §19 ACCEPTANCE CRITERIA

This section covers acceptance criteria for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §20 APPENDIX

This section covers appendix for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §21 IMPACT per Mk

This section covers impact per mk for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## mk_history

- Mk.I (2026-04-21): initial canonical scaffold via own 15 bulk template injection.
- Mk.II: pending — fill per-section content with domain expert review.
- Mk.III: pending — full verification data + external citations.

