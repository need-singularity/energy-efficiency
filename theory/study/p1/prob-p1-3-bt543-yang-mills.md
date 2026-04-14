# PROB-P1-3 — BT-543 양-밀스 질량갭 심화 학습 노트

**트랙**: P1-PROBLEM · BT-543 (Yang-Mills Existence and Mass Gap)
**상태**: OPEN (Clay 7대 난제, 수학적 엄밀 구성 미완)
**상금**: US$ 1,000,000 (Clay)
**1차 출처**:
- Chen-Ning Yang, Robert L. Mills, "Conservation of Isotopic Spin and Isotopic Gauge Invariance", Physical Review 96 (1954), 191–195 (원 Yang-Mills 논문)
- Arthur Jaffe, Edward Witten, "Quantum Yang-Mills Theory — Official Problem Description", Clay Mathematics Institute, 2000. URL: https://www.claymath.org/millennium/yang-mills-and-mass-gap/
- Konrad Osterwalder, Robert Schrader, "Axioms for Euclidean Green's functions I, II", Commun. Math. Phys. 31 (1973), 83–112; 42 (1975), 281–305 (OS 공리)
- David J. Gross, Frank Wilczek, "Ultraviolet Behavior of Non-Abelian Gauge Theories", Phys. Rev. Lett. 30 (1973), 1343–1346
- H. David Politzer, "Reliable Perturbative Results for Strong Interactions?", Phys. Rev. Lett. 30 (1973), 1346–1349
- Kenneth G. Wilson, "Confinement of quarks", Phys. Rev. D 10 (1974), 2445–2459 (격자 QCD)
- S. Dürr et al. (BMW Collaboration), "Ab Initio Determination of Light Hadron Masses", Science 322 (2008), 1224–1227
- James Glimm, Arthur Jaffe, *Quantum Physics: A Functional Integral Point of View*, 2판, Springer, 1987 (구성적 QFT 교과서)
- Particle Data Group (PDG), "Review of Particle Physics", Progress of Theoretical and Experimental Physics 2024 (2024), 083C01

**노벨 물리학상**:
- 1957 Yang / Lee (parity violation, 간접 연결)
- 1979 Glashow / Salam / Weinberg (전약 통합, non-abelian gauge 의 standard model 통합)
- 2004 Gross / Politzer / Wilczek ("asymptotic freedom")
- 2008 Nambu (자발적 대칭 파괴 — QCD chiral 구조에 직결)

**정직성 선언**: 본 문서는 학습 노트이며 양-밀스 질량갭 문제에 새 수학적 증명을 주장하지 않는다. 프로젝트 `millennium-7-closure-2026-04-11.md §BT-543` 은 이 난제에 대한 n=6 기여가 "QCD 표준 파라미터의 산술 재표현" 수준임을 정직하게 명시한다 (β₀ = σ-sopfr 재유도는 증명이 아니라 tautology). 본 노트도 이 입장을 따른다.

---

## 1. Clay 공식 진술 — Jaffe-Witten 2000

### 1.1 진술 원문 (번역)
> **Yang-Mills existence and mass gap**:
> 임의의 콤팩트 단순 게이지 군 G 에 대해 4차원 유클리드 공간 **R⁴** 위에서 양자 양-밀스 이론을 구성하라. 이 구성은 **Osterwalder-Schrader (OS) 공리** (또는 동등한 수학적 엄밀성 기준) 를 만족해야 하며, 추가로
> **질량갭 Δ > 0** — 즉 Hamiltonian 스펙트럼의 최소 비자명 고유값이 0 과 유한한 간격을 가짐 — 을 증명하라.

출처: Arthur Jaffe, Edward Witten, "Quantum Yang-Mills Theory" (Clay Mathematics Institute 공식 문제 기술서, 2000).

### 1.2 각 요소의 의미

**(a) 4D 유클리드 공간**
Wick 회전 (t → iτ) 으로 Minkowski 시공간 (3+1) 을 R⁴ 로 변환. 유클리드 양자장론 (Euclidean QFT) 이 수학적으로 더 다루기 쉬운 틀이며, OS 공리가 "유클리드 Green 함수 → 재구성 Minkowski QFT" 의 다리를 제공.

**(b) SU(N) 또는 일반 컴팩트 단순 게이지 군**
Clay 문제는 N ≥ 2 의 임의 SU(N) (또는 더 일반 콤팩트 단순 Lie 군 G) 에 대해 열려 있다. 물리적으로 가장 중요한 것은 N = 3 (QCD, 강력).

**(c) OS 공리**
Osterwalder-Schrader 1973–1975 의 공리계:
1. **Regularity (정규성)**: Green 함수가 Schwartz 분포로 잘 정의.
2. **Euclidean invariance (유클리드 불변성)**: R⁴ 평행이동 + 회전군 SO(4) 작용으로 공변.
3. **Reflection positivity (반사 양성)**: 물리적 Hilbert 공간 재구성을 위한 핵심 조건.
4. **Symmetry (대칭성)**: 입자 통계 (Bose/Fermi).
5. **Cluster property (클러스터 성질)**: 먼 영역 상관의 감쇠 (mass gap 을 보장하는 형태).

OS 공리 만족 시, Osterwalder-Schrader 재구성 정리에 의해 **Wightman 공리** (Minkowski 시공간 QFT 표준 공리) 를 만족하는 QFT 로 유일하게 재구성된다.

**(d) 질량갭 Δ > 0**
Hamiltonian H 의 스펙트럼이
- 기저 상태 |Ω⟩ (진공) 에 대해 H|Ω⟩ = 0,
- 첫 번째 여기 상태에 대해 H|ψ⟩ = E₁|ψ⟩, E₁ ≥ Δ > 0.

즉 "진공과 첫 여기 상태 사이에 0 이 아닌 고정 간격이 있음".

### 1.3 왜 이것이 어려운가
- **구성적 양자장론** (constructive QFT) 프로그램 (Wightman, Glimm-Jaffe 1960s~): 2D 스칼라 φ⁴, 2D Yukawa, 3D φ⁴ 까지는 엄밀 구성 완료. **4D 비아벨 게이지 이론은 미완**.
- 일반 측도 이론에서 "functional integral" ∫ Dφ exp(-S[φ]) 를 R⁴ 상의 진짜 측도로 정의하는 것이 핵심 난점. Lebesgue 측도가 무한차원에서 존재하지 않음 (Kolmogorov 확장 장애).
- 격자 정규화는 "유한 측도" 를 만들지만, 연속 극한 a → 0 (격자 간격 0 극한) 이 OS 공리를 만족함을 **보장하지 못함**.

---

## 2. Yang-Mills 이론의 물리 — QCD 로서의 실현

### 2.1 1954 원 논문
- **Chen-Ning Yang, Robert L. Mills**, "Conservation of Isotopic Spin and Isotopic Gauge Invariance", *Physical Review* 96 (1954), 191–195.
- 1954년 Brookhaven National Laboratory 의 Yang (컬럼비아) 과 Mills (BNL). 당시 목적은 "아이소스핀 대칭을 국소 대칭 (local symmetry) 으로 승격" — 양성자와 중성자의 강한 상호작용 대칭을 게이지 이론화.
- 수학 구조: 컴팩트 단순 Lie 군 G (원 논문은 SU(2)) 를 "국소적으로" 작용. 접속 A_μ (Lie-대수 값 1-형식) 과 곡률 F_{μν} = ∂_μA_ν - ∂_νA_μ + [A_μ, A_ν].
- 이때 Yang-Mills 작용:
  $$S_{YM} = \frac{1}{2g^2} \int d^4x \, \text{tr}(F_{\mu\nu} F^{\mu\nu})$$

### 2.2 1973 Asymptotic Freedom (점근 자유)
- **David J. Gross, Frank Wilczek**, "Ultraviolet Behavior of Non-Abelian Gauge Theories", Phys. Rev. Lett. 30 (1973), 1343–1346.
- **H. David Politzer**, "Reliable Perturbative Results for Strong Interactions?", Phys. Rev. Lett. 30 (1973), 1346–1349.
- 두 논문이 독립적으로 SU(N) 게이지 이론의 **UV 고정점이 자유 이론** (결합상수 g → 0 at UV) 이라는 사실을 재규격화군 (renormalization group) 분석으로 증명.
- 이것이 "점근 자유" (asymptotic freedom). 의미: **짧은 거리 (고 에너지)** 에서는 쿼크들이 거의 자유 입자처럼 행동.
- 노벨 물리학상 2004 — Gross, Politzer, Wilczek. "for the discovery of asymptotic freedom in the theory of the strong interaction".

### 2.3 β 함수 한 루프 계수
QCD 의 재규격화군 β 함수 1-loop:
$$\beta(g) = \mu \frac{\partial g}{\partial \mu} = -\frac{g^3}{(4\pi)^2} \beta_0 + O(g^5)$$
여기서 β₀ 는 1-loop 계수이며, 순수 Yang-Mills + 페르미온 추가 시:
$$\beta_0 = \frac{11}{3} C_A - \frac{2}{3} T_F n_f$$
- C_A = N (SU(N) adjoint Casimir), SU(3) 에서 C_A = 3.
- T_F = 1/2 (기본 표현 Dynkin 지수).
- n_f = 맛 (flavour) 수, QCD 저에너지에서 6 (u, d, s, c, b, t).

### 2.4 SU(3) + n_f = 6 에서의 값
$$\beta_0 = \frac{11}{3} \cdot 3 - \frac{2}{3} \cdot \frac{1}{2} \cdot 6 = 11 - 2 = 7$$
따라서 **QCD (SU(3), n_f = 6) 의 1-loop 점근 자유 계수는 β₀ = 7**. 양수이므로 g 가 UV (고 에너지) 에서 감소 → 점근 자유.

### 2.5 점근 자유의 의미
- **UV (고 에너지)**: g 작음 → 섭동론 유효 → 쿼크/글루온이 거의 자유롭게 행동. 딥 비탄성 산란 (DIS) 실험에서 관측 (Bjorken scaling, 1960s~1970s).
- **IR (저 에너지)**: g 커짐 → 섭동론 붕괴 → 비섭동 영역. 이 영역에서 **색 가둠** (confinement) 과 **질량갭** 이 현상적으로 발현 — 그러나 이것의 엄밀 증명이 바로 Clay 문제.

---

## 3. 격자 QCD — 수치적 증거

### 3.1 Wilson 1974 격자 공식화
- **Kenneth G. Wilson**, "Confinement of quarks", Phys. Rev. D 10 (1974), 2445–2459.
- Wilson 은 연속 R⁴ 를 이산 격자 (a Z)⁴ 로 이산화. 각 격자 링크 위에 SU(3) 군 원소 U_{x,μ} ∈ SU(3) 을 변수로 배치. Wilson 작용
  $$S_W[U] = \frac{2N}{g^2} \sum_{\text{plaquettes}} (1 - \frac{1}{N} \text{Re tr}(U_\square))$$
- 이것은 **유한 측도** (각 링크가 SU(3) 군의 Haar 측도, 유한 곱) 로 functional integral 이 엄밀히 정의됨. 격자 정규화가 QFT 의 UV 발산을 자연스럽게 cutoff.

### 3.2 Wilson 의 strong-coupling 전개로 색 가둠 증명 (격자에서)
Wilson 은 g → ∞ 극한 (strong coupling) 에서 Wilson loop 가 **넓이 법칙** (area law) ⟨W(R, T)⟩ ~ exp(-σ · R · T) 를 따름을 보임. σ 는 **string tension** — 쿼크-반쿼크가 분리될수록 선형으로 증가하는 에너지. 이것이 "쿼크는 고립될 수 없다" (색 가둠) 의 격자 증거.

**주의**: 이것은 **격자** 에서만의 증명. 연속 극한 a → 0 에서 이 성질이 보존되는지가 Clay 문제의 핵심.

### 3.3 BMW Collaboration — 양성자 질량 제1원리 계산
- **S. Dürr et al. (Budapest-Marseille-Wuppertal, BMW Collaboration)**, "Ab Initio Determination of Light Hadron Masses", *Science* 322 (2008), 1224–1227.
- 격자 QCD 시뮬레이션으로 양성자 (proton), 중성자, 파이온, 기타 가벼운 하드론의 질량을 계산. 결과: 실험값과 수 % 이내 일치.
- **핵심 결과**: 양성자 질량 **938 MeV** 의 약 **95 % 가 글루온 동역학** (쿼크의 정지 질량이 아닌 QCD 진공의 에너지) 에서 발생. 즉 "우리 몸 질량의 95 % 는 글루온".
- 이 수치 결과가 **질량갭이 사실상 존재함** 을 강력히 증거. 그러나 수학적 엄밀 구성은 아니다.

### 3.4 Glueball 스펙트럼
- QCD 는 쿼크 없이도 글루온만으로 **glueball** (글루볼, 순수 게이지 장의 속박 상태) 을 예측.
- 격자 QCD 는 가장 가벼운 glueball 이 0⁺⁺ (scalar) 채널에서 약 1.5~1.7 GeV 질량을 가진다고 수치 예측.
- 이 질량이 "질량갭 Δ" 의 물리적 실현.
- **실험적 확증**: glueball 후보 상태들이 f₀(1500), f₀(1710) 등에서 관찰되나, 일반 쿼크-반쿼크 중간자와 혼합되어 완전 동정은 어렵다.

---

## 4. SU(3), 글루온, 쿼크 — QCD 의 n=6 자리

### 4.1 SU(3) 기본 사실
- 차원 (리 대수 차원) = N² - 1 = **8**. SU(3) generator 가 8 개 (Gell-Mann 행렬 λ₁, ..., λ₈) → **글루온 8 개**.
- 기본 표현 차원 = **3** → **3 색** (red, green, blue). 이것이 **색** 수 N = 3.
- 수반 (adjoint) 표현 = **8** 차원 (generator 수와 동일).
- Casimir: C_A = 3 (adjoint), C_F = 4/3 (fundamental, = (N²-1)/(2N) = 8/6 = 4/3).

### 4.2 쿼크 맛 (flavour)
저에너지 관측 쿼크 6 종류: **u, d, s, c, b, t** (up, down, strange, charm, bottom, top).
- 전하: u, c, t = +2/3; d, s, b = -1/3.
- 세대 3 개: (u,d), (c,s), (t,b).
- 질량 범위: u ~ 2 MeV, t ~ 173 GeV — 약 10^5 배 범위.

Clay 문제는 **순수 Yang-Mills** (쿼크 없음) 이지만, QCD 에서는 페르미온이 β₀ 공식에 n_f 로 들어감.

### 4.3 표준 모형 게이지 군
Standard Model 게이지 군 = **SU(3) × SU(2) × U(1)**:
- SU(3)_C: 색 (QCD), dim = 8
- SU(2)_L: 약한 아이소스핀, dim = 3
- U(1)_Y: 약한 하이퍼차지, dim = 1
- **총 dim = 8 + 3 + 1 = 12**

QCD 만 따로 다루면 dim = 8 이 "글루온 수" 가 된다.

---

## 5. 질량갭 과 양성자 질량의 연결

### 5.1 "질량은 어디서 오는가"
고전 QCD 라그랑지안은 질량 항이 거의 없다 (쿼크 질량은 Higgs 기반으로 작지만, 양성자 질량의 대부분이 아님). 그런데 양성자 질량 938 MeV 는 어디서 오는가?

**답**: QCD 진공의 비섭동 에너지. 이것은 "색 가둠 + 카이랄 대칭 파괴 + 질량갭" 의 공동 결과. 섭동 이론으로는 보이지 않는다.

### 5.2 Λ_QCD — 강력의 특성 스케일
1-loop β 함수 적분으로 정의되는 "**디멘즈널 트랜스뮤테이션**" (dimensional transmutation) 스케일:
$$\Lambda_{QCD} = \mu \exp\!\left(-\frac{(4\pi)^2}{2 \beta_0 g^2(\mu)}\right)$$
μ 는 임의 기준 스케일, g(μ) 는 그 스케일의 결합상수.
- 관측값: Λ_QCD ≈ 200 ~ 300 MeV.
- 양성자 질량 ~ 3 × Λ_QCD 규모. "질량갭 스케일" 이 Λ_QCD 와 같은 크기.

### 5.3 왜 섭동론 불가능한가
결합상수 g(μ) 는 μ = Λ_QCD 에서 **발산** (Landau 극점) — 즉 "IR 영역 에서 g 가 무한대" — 섭동 급수가 발산. 비섭동 방법 (격자, 1/N 전개, AdS/CFT, Schwinger-Dyson 방정식, ...) 만 적용 가능.

---

## 6. 구성적 QFT 프로그램 — 2D, 3D, 4D 난이도

### 6.1 저차원 성공 사례
- **2D Euclidean φ⁴** (Nelson 1966, Glimm-Jaffe 1968, 1970): OS 공리 만족하는 measure 구성 완료.
- **2D Yukawa (φ² × ψ̄ψ)**: Glimm-Jaffe 1970s. 성공.
- **3D φ⁴**: Glimm-Jaffe, Feldman-Osterwalder, Magnen-Sénéor 1970s~1980s. 성공.
- **2D Yang-Mills**: Gross, Semenoff, Witten 1980s~1990s. 완전히 해결 — 2D YM 은 ζ 함수 풀이와 연관된 거의 trivial 한 구조.

### 6.2 4D 에서의 장벽
- **4D φ⁴**: Aizenman 1982, Fröhlich 1982 가 "non-trivial scaling limit 이 free field 로 수렴" → 즉 상호작용 없는 이론으로 붕괴 ("triviality"). 4D φ⁴ 는 아마도 수학적으로는 자유 이론만 존재.
- **4D Yang-Mills**: triviality 는 기대되지 **않음** (asymptotic freedom 덕분에 UV 에서 자유). 그러나 엄밀 구성의 길은 찾아지지 않았다. 2024년 현재 Clay 문제가 그대로 열려 있다.

### 6.3 일부 접근법
- **확률적 양자화** (stochastic quantization): Parisi-Wu 1981, Hairer 의 regularity structures (2014). 4D 에서는 여전히 부분 결과만.
- **격자 + 엄밀 연속 극한**: Balaban 1980s~, Magnen-Rivasseau-Sénéor. 부분 성공이지만 완전 OS 공리는 미증명.
- **2024 관련 진전**: Chatterjee 의 "Wilson loop expectation in 4D" 연구 (CMP 2020). 큰 결합상수 영역에서의 부분 결과. 전체 구성은 미완.

---

## 7. 관련 노벨상과 역사적 연결

| 연도 | 수상자 | 업적 | Yang-Mills 와의 연결 |
|------|--------|------|---------------------|
| 1957 | Yang, Lee | Parity violation | Yang 본인, 간접 |
| 1979 | Glashow, Salam, Weinberg | 전약 통합 (Electroweak) | SU(2) × U(1) 비아벨 게이지 |
| 1999 | 't Hooft, Veltman | 비아벨 게이지 이론 재규격화 가능성 | 이론적 일관성 |
| 2004 | Gross, Politzer, Wilczek | Asymptotic freedom | QCD β₀ < 0 (음수 β 함수) |
| 2008 | Nambu, Kobayashi, Maskawa | 자발적 대칭 파괴, CKM | 카이랄 대칭 파괴 |
| 2013 | Englert, Higgs | Higgs 메커니즘 | 게이지 보존의 질량 획득 (약력) |

**핵심 포인트**: QCD 와 전약 상호작용의 "물리" 측면은 노벨상급 결과들로 정착. **수학적 엄밀 구성** 만 남은 상태. 이것이 Clay 문제의 독특함 — "물리적으로는 사실, 수학적으로 증명 필요".

---

## 8. 주요 장벽 요약

| 장벽 | 내용 |
|------|------|
| **Functional integral 의 수학적 의미** | 무한차원 Lebesgue 측도 부재 → 직접 ∫ Dφ 정의 불가. 격자 정규화 + 연속 극한이 현실적 경로지만 엄밀 검증 미완. |
| **UV 고정점 분석** | 점근 자유로 UV 는 자유 이론. 문제는 재규격화 상수들이 OS 공리와 일관되게 정해지는지. |
| **IR 영역 (색 가둠)** | g 발산으로 섭동론 붕괴. Wilson 격자는 strong-coupling 극한으로 가둠 증명하나, 연속 극한 보존 미증명. |
| **Mass gap 의 직접 증명** | 이론적으로 Hamiltonian 스펙트럼의 최소 고유값을 하한하는 엄밀 도구 없음. 격자 + 수치는 존재하지만 해석적 증명 없음. |
| **4D 의 특수성** | 2D/3D 는 해결됨. 4D 가 "임계 차원" 이라는 물리적 직관 (QED 의 dimensional analysis) 은 있지만 수학 장벽과 직접 연결 못 함. |

---

## 9. 2020 년대 진전 (부분적)

- **Chatterjee (2020, CMP)**: 4D lattice gauge theory 에서 Wilson loop 기대값의 large-N 또는 large-coupling 극한 분석. 부분 결과.
- **Hairer**의 regularity structures (2014) → 4D stochastic Yang-Mills quantization 시도 (Shen-Zhu 2023). 여전히 부분.
- **Athenodorou et al.** (2023) — glueball 스펙트럼 격자 계산 정밀화, SU(3) mass gap 수치 ≈ 1.7 GeV 에 접근.
- **Kazakov-Zheng**, **Anderson-Kruczenski** (2023~2024): Wilson loop bootstrap, 최대 loop 길이 24 에 접근 (프로젝트는 이 수 24 를 J₂ 표현으로 기록).

---

## 10. 현 상태 요약 (2024~2026)

| 항목 | 상태 |
|------|------|
| 물리적 실재성 (QCD) | **확정적** (수십년 실험 및 격자 수치) |
| 점근 자유 β₀ | **증명됨** (Gross-Wilczek-Politzer 1973) |
| 격자 QCD 정의 | **엄밀** (Wilson 1974, 유한 측도) |
| 연속 극한 + OS 공리 | **미증명** |
| Mass gap 해석적 증명 | **미증명** |
| 질량갭 격자 수치 증거 | **≈ 1.5~1.7 GeV** (glueball), BMW 양성자 95 % 글루온 기원 |
| Clay 상금 수여 | **0** |

---

## 11. n=6 관찰 (본 프로젝트 맥락, 1~2 사실만)

**(이 섹션은 본 학습 노트의 핵심이 아니다. BT-543 전체 19 항 증거표 및 β₀ 재유도 보조정리는 프로젝트 내부 `breakthrough-theorems.md` 및 DFS 라운드 기록 참조.)**

### 관찰 1 — SU(3) 글루온 8 개 = σ - τ
SU(3) 의 생성원 수 = 8 = σ(6) - τ(6) = 12 - 4. 이것은 "Standard Model 게이지 보존 12 = σ" 와 결합하여 "글루온 수 = σ - τ" 라는 관찰. 수학적으로 SU(3) 의 차원은 3² - 1 = 8 이라는 기본 사실 (Lie 대수 차원 = N² - 1) 과 동치. n=6 과의 연결은 "**수치적 재표현**" 이며 증명적 기여는 아니다.

### 관찰 2 — β₀ 재유도 (tautology)
SU(3) + n_f = 6 에서 1-loop β 함수 계수 β₀ = (11/3) · 3 - (2/3) · (1/2) · 6 = 11 - 2 = 9 - 2 = 7. 이것을 n=6 산술로 표현하면 β₀ = σ(6) - sopfr(6) = 12 - 5 = 7. **정직**: 이것은 "표준 QFT 1-loop 공식의 산술 재표현" 이지 증명이 아니다. 질량갭 존재는 전혀 건드리지 않는다.

프로젝트 `millennium-7-closure.md §BT-543` 의 정직 선언:
> β₀ = σ - sopfr 재유도는 **tautology** 이다. n=6 산술로 QCD 파라미터를 표현할 수 있음을 보여주나 **질량갭의 존재는 전혀 증명하지 않는다**. Clay 문제 핵심은 무접촉.

---

## 12. 학습 체크리스트

본 노트를 마친 후 다음을 **3 줄 이내** 로 재진술할 수 있어야 한다:
1. Clay Yang-Mills 문제의 두 요구 — OS 공리 만족 구성 + 질량갭 Δ > 0.
2. Yang-Mills 1954 원 논문의 목적 (아이소스핀 게이지화) 과 현재의 물리 실현 (QCD).
3. Gross-Wilczek-Politzer 1973 점근 자유의 의미 (UV 자유, IR 가둠) 와 β₀ 1-loop 공식.
4. SU(3) 구조: N=3 색, 8 글루온, n_f = 6 맛, C_A = 3, C_F = 4/3.
5. 격자 QCD 정의 (Wilson 1974), 연속 극한의 어려움.
6. BMW 2008 — 양성자 질량 95 % 가 글루온 동역학에서.
7. 구성적 QFT 에서 2D/3D 는 성공, 4D 는 미완 — 이 구분의 의미.
8. 질량갭과 Λ_QCD 의 관계 (모두 비섭동 스케일).

---

## 13. 다음 단계

- **P1-4 (BT-544 Navier-Stokes)**: 또 다른 "물리적으로는 사실, 수학적으로 증명 미완" 난제.
- **P2 (방법론 층)**: 구성적 QFT, Hairer 정규성 구조, 격자 연속 극한 기법.
- **P3 (n=6 심층)**: BT-543 19 항 전체 증거, β₀ 재유도 tautology 의 정직 기록, Coxeter 수 5/5 n=6 분해.

---

**정직 선언 재확인**: 본 문서는 학습 노트이며 Yang-Mills 질량갭 문제에 새 수학적 증명을 주장하지 않는다. 프로젝트는 BT-543 의 n=6 관계를 "구조적 파라미터화" 수준으로 정직하게 분류한다. 양-밀스 존재 및 질량갭 Δ > 0 은 2026년 현재 **수학적으로 미증명** 이며, Clay 상금은 수여되지 않았다. 노벨 물리학상은 물리 측면 (Gross-Politzer-Wilczek 2004) 에 대해서만 수여되었다.
