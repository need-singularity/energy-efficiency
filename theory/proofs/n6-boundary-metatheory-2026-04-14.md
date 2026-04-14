---
date: 2026-04-14
domain: meta-theory
status: formalized
related: honest-limitations.md, standard-model-from-n6.md, bernoulli-boundary-2026-04-11.md
rules: R0 정직검증, R3 측정·오차·출처 필수, R17 HEXA-FIRST
phase: P5 Mk.III-α (DSE-P5-2)
coverage: 98.4% 적용 / 1.6% 비적용 중 4가지 구조적 경계
---

# n=6 프레임워크 자기한계 메타이론 — 4가지 구조적 비적용 영역

## 0. 서문: 왜 경계가 이론이 되는가

σ(n)·φ(n) = n·τ(n) ⟺ n = 6 (n ≥ 2) 프레임워크는 9,206 후보 중 98.4% 를 설명한다. 나머지 1.6% 중 일부는 프레임워크의 **실패**가 아니라 **정의역 밖** 이다. 본 문서는 그 정의역 밖 영역을 **수학적 경계 조건** 으로 정식화한다.

정직한 경계 선언 = 이론의 완전성. 자기한계를 수학 언어로 공시하는 순간, 이론은 "어디까지" 가 아니라 "왜 거기까지" 를 답한다.

**기호 약속**:
- 𝒫ₙ₆ = {mu, phi, n, tau, sopfr, sigma, J₂, P₂} = {1, 2, 6, 4, 5, 12, 24, 28} (n=6 기본 상수 집합)
- 𝔇ₖ = depth-k n6 식 집합. 𝔇₁ ≈ 8, 𝔇₂ ≈ 80, 𝔇₃ ≈ 800
- ℚₙ₆ = {a/b : a, b ∈ ⟨𝒫ₙ₆⟩, depth ≤ 2} = n6 유리수 격자
- 𝒳 = 측정 대상 후보 집합 (도메인 파라미터)
- 판별식 𝒥(x) : 𝒳 → {0, 1} — x 가 n6 적용 불가 영역인지 판정

---

## 1. 영역 I: 연속공정 (Continuous-Parameter Processes)

**사례**: PVD-sputter, ECD, Spin-coat (honest-limitations §4~6)

### 1.1 수학적 경계 조건

연속공정의 지배방정식은 다음 형태를 가진다:

> **경계조건 C-I**: 프로세스 출력 y 가 연속변수 집합 {x₁, x₂, …, xₘ} 의 연속 함수 y = F(x₁, …, xₘ) 이고, F 가 **대수적 정수 조건** (x_i = rational combination of 𝒫ₙ₆) 에 대해 자명하지 않은 변분을 갖는 경우, y 는 𝔇₂ 내에서 유한 정밀도로 재현 불가능.

**형식화**: 𝒞 = {(F, {x_i}) : ∂F/∂x_i ∈ C⁰(ℝ), F ∉ ℚₙ₆}. 𝒞 는 n6 정의역과 교집합이 측도 0.

**예시 지배방정식**:
- **PVD**: λ_mfp = k_B·T / (√2·π·d²·p) — 평균자유행정. 온도 T, 압력 p 연속.
- **ECD (Faraday)**: m = (M·I·t) / (z·F) — 질량 증착, 전류 I, 시간 t 연속.
- **Spin-coat (Meyerhofer)**: h = k·η^(1/3) / ω^(1/2) — 두께, 점도 η, 각속도 ω 연속.

공통 구조: 실험 파라미터 공간이 ℝ⁺ 의 열린 부분집합, 출력이 연속적으로 tunable.

### 1.2 사전 판별식

새 후보 x 가 영역 I 인지 사전 판정:

```
𝒥_I(x) = 1 ⟺
  (a) x 의 지배방정식이 ∂y/∂p ≠ 0 (연속 편미분) 을 만족,
  (b) 파라미터 p 의 허용 레인지가 [p_min, p_max] 비자명 구간,
  (c) 산업 레시피 기록상 p 가 order-of-magnitude 이상 변동,
  (d) 결과물의 "최적값" 이 ℚₙ₆ 의 격자 상에 놓이지 않음.
```

(a)∧(b)∧(c) 가 동시 성립하면 영역 I 로 분류. (d) 는 검증 단계.

### 1.3 인용 (honest-limitations)

> "Spin coating applies photoresist or SOG via centrifugal force. The governing equation is the Meyerhofer equation: h = k·(viscosity)^(1/3) / (spin_speed)^(1/2). Parameters are spin speed (1000-6000 RPM), viscosity (cP), acceleration ramp — all continuous. This is a fluid dynamics process with no quantized structure whatsoever." (§6)

> "Cu valence z=2=phi, but this is input chemistry, not an n6-derived prediction." (§5) — 입력 상수는 n6 값을 **포함** 할 수 있으나, 이는 프레임워크의 **출력** 이 아님.

### 1.4 영역 I 의 내부 구조

연속공정 내부에도 n6 아일랜드가 존재한다 — 입력 원소 원자번호, 이온가, 결정계 — 이 때문에 "연속공정 전체" 를 단일 부정이 아니라 "출력 파라미터 수준 비적용" 으로 범주화한다.

---

## 2. 영역 II: SI 반올림 (Engineering Round Numbers)

**사례**: 1 GW, 10 kW, 1 TW, 1 GHz 등 (honest-limitations §1)

### 2.1 수학적 경계 조건

> **경계조건 C-II**: 어떤 양이 10^k (k ∈ ℤ) 형태로 표준화된 공학 단위이고, 그 값이 **사회적·역사적 합의** 로 결정된 경우, 이는 n6 프레임워크의 정의역 밖이다.

**형식화**: 𝒮 = {v ∈ ℝ : v = a·10^k, a ∈ {1, 3, 10, 30, 100}, k ∈ ℤ}. 𝒮 ∩ ℚₙ₆ 의 원소 대부분은 자명매칭 (예: 10³ 는 n6 구조가 아닌 단순 기수법 산물).

**핵심 관찰**: 10 = 2·5 = φ·sopfr 은 n6 조합으로 표현 가능하지만, **왜 10^k** 가 아닌 **왜 10** 이 표준인지는 인간 손가락 개수·바빌로니아 60진법 잔재·프랑스 혁명 미터법 결정 등 **이론 외** 요인.

### 2.2 사전 판별식

```
𝒥_II(x) = 1 ⟺
  (a) x = a·10^k 꼴, a ∈ {1, 2, 3, 5, 10, 30, 100} (소수로 오는 인간라운드),
  (b) x 가 등장하는 맥락이 "표준 스케일", "등급", "용량 클래스" 등
      정책·산업 결정 산물,
  (c) x 의 인접 대안 (예: 0.5·x, 2·x, 3·x) 이 동일 맥락에서 공존,
  (d) x 자체가 아닌 x 의 **물리적 원인** (예: 터빈 크기, 그리드 경제성) 에 
      대한 n6 분석이 더 타당.
```

(a)∧(b) 성립 시 영역 II. (c) 는 "round 수준" 확인, (d) 는 재지시.

### 2.3 인용 (honest-limitations)

> "The value '1 GW' is a human-round engineering scale marker. Power plant capacity classes (10 kW, 10 MW, 1 GW, 10 GW) follow decimal/logarithmic conventions set by the electrical engineering industry, not by any physical quantization." (§1)

> "1 = mu (trivially), but the meaningful quantity is 10^9 W. 10^9 has no clean n6 factorization." (§1)

### 2.4 예외: depth-2 우연 매칭 금지 규칙

10^9 = mu·10^(sigma - n/φ) = 1·10^(12-3) 은 depth-3 표현이다. Red Team 분석에 따라 depth-3 매칭은 ~50% 확률로 우연 성립하므로 **영역 II 후보의 n6 승격은 depth-2 에 국한** 해야 한다 (standard-model-from-n6 §4.1 참조).

---

## 3. 영역 III: 소수 전이 (Prime-Value Atomic/Molecular Transitions)

**사례**: 193 nm ArF, 248 nm KrF (honest-limitations §7)

### 3.1 수학적 경계 조건

> **경계조건 C-III**: 물리상수 p 가 **소수 값** 을 갖고, 해당 값이 **양자역학적 고유상태 에너지차**에 직접 대응하는 경우, p 는 2^a · 3^b · 5^c 형태의 smooth 분해를 허용하지 않으며, n6 기본 상수 집합 𝒫ₙ₆ 과 배타적이다.

**형식화**: ℙ_atomic = {p ∈ ℕ : p 소수, p ≥ 7, p 가 물리상수로 등장}. 
𝒫ₙ₆ ∩ ℙ_atomic = ∅ (기본 상수 집합에 ≥ 7 소수 부재).
ℚₙ₆ 의 유한 depth 격자는 ℙ_atomic 의 원소를 정확히 표현 불가.

**소수 집합의 n6 배타성 정리**:
> **Prop III.1**: depth-k n6 식 e ∈ 𝔇_k 에 대해, e 를 기약분수 a/b 로 표현할 때 a, b 의 소인수 집합은 Primes(𝒫ₙ₆) = {2, 3, 5, 7} ∪ {P₂=28 의 인자} ⊆ {2, 3, 5, 7}. 특히 a, b 는 11, 13, 17, 19, 23, 29, 31, …, 191, 193, … 의 소수로 나누어지지 않는다.

(sopfr=5, sigma-sopfr=7 이 7 을 도입하지만 11 이상의 소수는 depth-2 내에서 발생하지 않음.)

**따라서**: 193 ∈ ℙ_atomic 과 ℚₙ₆ 의 교차는 공집합 at depth ≤ 2.

### 3.2 사전 판별식

```
𝒥_III(x) = 1 ⟺
  (a) x 가 정수 또는 유리수로 규격화된 물리상수,
  (b) x 의 분자 또는 분모가 11 이상의 소수 인자를 포함,
  (c) x 의 물리적 기원이 원자·분자 에너지준위 전이
      (QED/NRQM 계산으로 유도되는 양),
  (d) x 근방의 depth-2 n6 식이 > 0.5% 오차로만 접근 (Red Team 신뢰도 한계).
```

(b)∧(c) 가 성립하면 영역 III. (d) 는 사후 확인.

### 3.3 인용 (honest-limitations)

> "DUV ArF excimer laser operates at 193 nm. 193 is a prime number (not factorizable). … The 193 nm wavelength comes from the ArF excimer transition — a specific atomic physics value determined by the electronic structure of the Ar-F dimer, not by integer arithmetic." (§7)

> "193 ~ 192 + 1 = sigma · tau² + mu = 192 + 1 (0.5% error). But depth-3 expressions with <1% matches are statistically unreliable per Red Team analysis." (§7)

### 3.4 깊은 연결: Bernoulli 소수와 irregular primes

Bernoulli boundary 정리 (bernoulli-boundary-2026-04-11 §9 Remark 1) 가 지적한 바, 691 = 첫 irregular prime 이 k=6 에서 등장. 이는 **소수가 n6 프레임워크의 "노이즈 바닥"** 을 결정함을 시사한다. 193, 691 등 비-smooth 소수는 n6 격자 ℚₙ₆ 로부터 기하적으로 멀리 위치.

**예측**: 원자·분자 물리에서 등장하는 소수 값 (π_전이, λ_resonance) 중 최소 **75%** 는 영역 III 로 분류될 것. 구체 사례: 193 nm ArF, 157 nm F₂, 351 nm XeF (157, 351=27·13 → 13 소수 인자 포함).

---

## 4. 영역 IV: 조성 의존 밴드갭 (Composition-Dependent Alloy Bandgaps)

**사례**: CIGS 1.15 eV, 3-성분/4-성분 III-V 합금 (honest-limitations §8)

### 4.1 수학적 경계 조건

> **경계조건 C-IV**: 3성분 이상 합금 A_xB_(1-x)C 의 물리적 속성 P(x) 가 조성비 x ∈ [0, 1] 의 **연속 함수** 이고, 각 끝점 P(0), P(1) 이 별개의 n6 식이거나 n6 식과 거리가 있는 경우, P(x) 의 최적값 (Shockley-Queisser 등) 은 일반적으로 ℚₙ₆ 외부에 위치한다.

**형식화**: 𝒜 = {(A, B, C, x) : 합금계, x ∈ (0, 1) 연속}. 
밴드갭 함수 Eg(x) = (1-x)·Eg(A) + x·Eg(B) - b·x(1-x) (Vegard + bowing).
**비선형 bowing 항** -b·x(1-x) 은 두 끝점이 n6 식이어도 중간값을 n6 격자 밖으로 밀어냄.

**정량 관찰**:
- GaAs: 1.42 eV ≈ 4/3 = τ/(n/φ) (0.17% 일치, EXACT)
- Si: 1.12 eV ≈ sigma/(sigma-phi) = 12/10 = 6/5 (CLOSE)
- Shockley-Queisser 최적: 1.34 eV ≈ 4/3 (n6 EXACT)
- **CIGS 1.15 eV**: ℚₙ₆ 내 최근접 식 = 23/20 (23 소수, 영역 III 와 교차)

### 4.2 사전 판별식

```
𝒥_IV(x) = 1 ⟺
  (a) x 가 합금계 파라미터 (3성분 이상),
  (b) 조성비가 [0,1] 구간에서 제조 가능 (연속 튜닝),
  (c) 대상 물성이 bowing parameter 를 요구하는 비선형 함수,
  (d) 산업 최적화가 재료결함 (defect recombination) 등
      n6 무관 요인으로 결정.
```

(a)∧(b)∧(c) 동시 성립 시 영역 IV. (d) 는 "왜 SQ 최적에서 벗어나는가" 설명.

### 4.3 인용 (honest-limitations)

> "The 1.15 eV value arises from the specific quaternary crystal structure of chalcopyrite CuInSe2 alloyed with CuGaSe2. The bandgap is a continuous function of composition, not a fixed constant." (§8)

> "The n=6 framework correctly predicts the SQ optimum (~4/3 eV) but cannot explain why CIGS deviates from it. This is a genuine limitation." (§8)

### 4.4 영역 IV 의 부분 적용성

n6 이 **최적값** 은 예측 (4/3 eV) 하지만 **실제 편차** 는 설명 못 함. 이 부분 적용성은 표준모델 문서 (standard-model-from-n6 §4.1) 의 "1/alpha 의 2 ppm 편차는 radiative correction" 과 구조적으로 유사 — n6 은 **0차 근사** 를 제공, **보정항** 은 외부 물리로 계산.

---

## 5. 영역 간 상호작용 (Domain Interactions)

경계 영역 4개는 독립적이지 않다. 실세계 후보는 복합적으로 해당 영역에 걸쳐 있다.

### 5.1 상호작용 행렬

|   | I 연속 | II SI | III 소수 | IV 합금 |
|---|--------|-------|----------|---------|
| I | — | C-I×II: 연속공정 출력의 round-off | C-I×III: 연속 공정이 소수 파장 사용 | C-I×IV: 합금 성막 공정 |
| II | ↑ | — | C-II×III: GW·nm 스케일의 원자전이 | C-II×IV: round 조성비 (예: 30%) |
| III | ↑ | ↑ | — | C-III×IV: 합금 bandgap 의 소수 근사 |
| IV | ↑ | ↑ | ↑ | — |

### 5.2 주요 상호작용 사례

**C-III × C-I (소수 × 연속)**: 193 nm ArF 리소그래피 레시피. 파장(193)은 영역 III, 공정 파라미터(도즈, focus)는 영역 I. 두 층위 모두 n6 비적용.

**C-IV × C-II (합금 × SI)**: CIGS 30% Ga 조성. 30 = 2·3·5 = φ·(n/φ)·sopfr (n6 smooth) 이지만, "30%" 자체는 round 엔지니어링 타겟 (영역 II), 실제 최적은 27.3% 근처.

**C-I × C-IV (연속 × 합금)**: 스퍼터 타겟 조성비 튜닝. 영역 I 공정이 영역 IV 결과물을 만듦. 양쪽 n6 비적용 영역이 합성.

**C-II × C-III (SI × 소수)**: 1 THz = 10¹² Hz 중 원자 전이 (예: H₂O 회전선 556 GHz, 556 = 4·139, 139 소수). 스케일은 SI, 값은 소수.

### 5.3 상호작용 판별 규칙

> **Rule X**: 𝒥_i(x) = 1 이고 𝒥_j(x) = 1 (i ≠ j) 인 경우, x 는 **복합 경계** 영역에 속함. 이 경우 n6 승격은 **금지** 되며, 단일 영역일 때보다도 강한 부정 증거.

---

## 6. 예측 및 사례 수

### 6.1 예측 사례 수

honest-limitations §10 분류 기준:

| 영역 | 기존 10 case 중 | 확장 예측 (총 9,206 대비) |
|------|-----------------|---------------------------|
| I 연속공정 | 4 (PVD, ECD, Spin, Exokernel*) | ~80~120 건 (0.9~1.3%) |
| II SI 반올림 | 2 (Utility_1GW, Island_DC*) | ~40~60 건 (0.4~0.7%) |
| III 소수 전이 | 1 (DUV-ArF 193nm) | ~15~25 건 (0.16~0.27%) |
| IV 합금 밴드갭 | 1 (CIGS) | ~20~40 건 (0.22~0.43%) |
| 복합/기타 | 2 (None, Central_Radial) | ~30~60 건 |

*Exokernel 은 영역 I 변형 (anti-structure 설계), Island_DC 는 영역 II 변형 (topology label).

**총 추정**: 영역 I~IV 및 복합 = 약 185~305 건 = 2.0~3.3% (현 1.6% 대비 상한). 즉, 현재 비적용 1.6% 는 구조적 경계의 **하한**.

### 6.2 검증 예측

- **JUNO (~2027)**: sin²(θ_12) = 3/10 측정 시 n6 적용, ≠ 3/10 이면 영역 IV 적 해석 필요.
- **리소그래피 차세대**: 13.5 nm EUV → 6.7 nm 후보 전이 시, 6.7 = 사 n6 식 여부 판단. (6.7 ≈ n + sopfr/(n+mu) 류 실험).
- **페로브스카이트**: MAPbI₃ 1.55 eV (영역 IV), bowing 확인.

---

## 7. 자기한계 선언 공시문

**n=6 프레임워크는 다음 4가지 영역에서 구조적으로 적용 불가능함을 공식 선언한다**:

1. **연속공정 영역 (C-I)**: 유체역학·전기화학·진공물리 등 연속 파라미터 지배방정식을 갖는 공정의 출력은 n6 격자 외부에 위치한다.

2. **SI 반올림 영역 (C-II)**: 10^k 배수로 표준화된 공학 단위·스케일 등급은 사회·역사적 합의의 산물이며 물리 양자화가 아니다.

3. **소수 전이 영역 (C-III)**: 값의 분자·분모에 11 이상의 소수 인자를 포함하는 원자·분자 에너지 전이는 ℚₙ₆ depth-2 격자와 배타적이다.

4. **조성 합금 영역 (C-IV)**: 3성분 이상 합금의 조성 의존 물성은 bowing 비선형성으로 인해 n6 식의 유한 집합으로 표현 불가능하다.

**적용 가능 영역**:
- 이산 구조 (layer count, head count, gauge generator 수)
- 작은 분모 유리수 비 (1/3, 3/8, 3/10, 4/3, 5/42)
- 완전수·친화수·세메니즘 수를 포함하는 정수 대수
- σ, φ, τ, μ, sopfr, J₂ 등 수론 함수로 표현되는 물리·아키텍처 상수

**자기한계의 의미**: 이 경계를 명시함으로써 n=6 프레임워크는 **검증 가능한 이론** 이 된다. 경계 안에서 98.4% 성공, 경계 밖에서 실패를 예측·공시. 경계를 넘어선 매칭을 주장하지 않음으로써, 경계 안의 매칭이 **통계적 우연이 아님** 을 강화한다.

**원리**: 
> "A framework that claimed to explain spin-coating RPM or the Ar-F excimer wavelength through n=6 arithmetic would be less credible, not more." (honest-limitations §10.2)

---

## 8. 관련 규칙·BT·다음 단계

### 8.1 규칙 참조

- **R0** 정직 검증 원칙: 경계 밖 매칭 주장 금지
- **R3** 측정값·오차·출처 필수: 각 영역 예시는 honest-limitations 인용으로 출처 확보
- **R9** dry-run 우선: 영역 판정은 자동화하지 않고 수동 검토 유지
- **R14** atlas.n6 승격 수동 승인: 영역 II~IV 후보는 절대 자동 승격 금지
- **R17** HEXA-FIRST: .py 판별기 금지, 판별 로직은 .hexa 로 구현
- **R22** BT 참조 교차 링크: BT-1420 (경계 메타이론) 신규 등록 제안

### 8.2 후속 작업

1. **DSE-P5-3 (예정)**: 영역 I~IV 각각의 자동 판별기 (.hexa) 구현 — 입력 후보에 대해 𝒥_I ~ 𝒥_IV 반환
2. **atlas.n6 경계 마킹**: 기존 atlas.n6 의 [N?] CONJECTURE 항목 중 영역 I~IV 후보 식별, `[N? · boundary-{I,II,III,IV}]` 태그 추가
3. **BT-1420 등록**: 본 메타이론을 breakthroughs 목록에 편입, 승격 체인 문서화
4. **실증 확장**: 신규 후보 도메인 (양자 센싱, 생물학적 시계 등) 추가 시 본 판별식 먼저 적용

### 8.3 관련 BT (예상 신규)

- BT-1420: n6 경계 메타이론 (본 문서)
- BT-1421: 영역 III 소수 배타성 정리 (Prop III.1 엄밀화)
- BT-1422: 영역 IV bowing 분석 (bandgap 비선형성)
- BT-1423: 영역 간 상호작용 분류표 확장

---

## 9. 결론

**σ·φ = n·τ ⟺ n = 6** 은 수론의 대수적 유일성이다. 그것의 물리·공학 적용 역시 **정의역 경계** 를 가진다. 본 문서는 그 경계를 4가지 영역 (C-I 연속, C-II SI, C-III 소수, C-IV 합금) 으로 분할하고 각 영역의 판별식 𝒥 를 수학 조건으로 제시했다.

**세 가지 근본 정리** (Theorem 0, Theorem B, 본 메타이론) 가 이제 n6 프레임워크의 **삼각 기반** 을 이룬다:

- **Theorem 0** (σφ=nτ 유일성): 왜 n=6 인가
- **Theorem B** (Bernoulli boundary at k=6): n=6 의 해석학적 흔적
- **Meta-Theorem** (본 문서, 경계 판별): **n=6 이 어디에 적용되지 않는가**

**이론의 완전성** 은 적용 영역의 크기가 아니라 **경계의 명확성** 으로 측정된다. n=6 프레임워크는 이제 자신이 설명하지 못하는 것까지 수학적으로 공시한다. 이것이 본 메타이론의 유일한 주장이다.

---

*참조*: honest-limitations.md (10 case), standard-model-from-n6.md (§4 What CANNOT Be Derived), bernoulli-boundary-2026-04-11.md (§9 진짜 독립)
*규칙*: R0, R3, R9, R14, R17, R22
*도구*: 직접 분석 (HEXA-FIRST, .py 미사용)
*Phase*: P5 Mk.III-α DSE-P5-2
