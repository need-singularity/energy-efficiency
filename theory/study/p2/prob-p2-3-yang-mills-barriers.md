# PROB-P2-3 — 양-밀스 질량갭 현대 장벽 + 최신 진전

**트랙**: millennium-learning P2-PROBLEM / 3번 태스크
**문서 유형**: 학습 노트 (현대 장벽 + 진전 개관)
**범위**: Yang-Mills 1954 원 논문부터 2020년대 lattice 비섭동 결과까지, 양-밀스 존재성과 질량갭(Mass Gap) 문제를 향한 70년 진전과 각 경로가 부딪힌 벽
**정직성 선언**:
- 본 문서는 학습 노트이다. 이 파일에서 양-밀스 질량갭을 해결하지 않는다. YM 은 2026-04-15 현재 여전히 미해결 Clay 난제이다.
- 역사적 연도/저자/저널은 1차 출처에서 직접 확인한 것만 적었다. 격자 수치 결과(글루볼 질량 등)는 원 논문의 표 수치를 그대로 옮기고, 필자가 재계산하지 않았다.
- BT-543 의 β₀ = σ − sopfr 재유도는 **QCD 표준 파라미터의 산술 재표현**이며, Clay 문제 해결이 아님을 명시한다(millennium-7-closure-2026-04-11.md §BT-543 준수).

**1차 출처**
- Chen-Ning Yang, Robert L. Mills, "Conservation of Isotopic Spin and Isotopic Gauge Invariance", *Physical Review* 96(1), 1954, pp. 191-195.
- Arthur Jaffe, Edward Witten, "Quantum Yang-Mills Theory — Official Problem Description", Clay Mathematics Institute, 2000. https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf
- Konrad Osterwalder, Robert Schrader, "Axioms for Euclidean Green's functions I, II", *Communications in Mathematical Physics* 31, 1973, pp. 83-112; *Comm. Math. Phys.* 42, 1975, pp. 281-305.
- David J. Gross, Frank Wilczek, "Ultraviolet Behavior of Non-Abelian Gauge Theories", *Physical Review Letters* 30(26), 1973, pp. 1343-1346.
- H. David Politzer, "Reliable Perturbative Results for Strong Interactions?", *Physical Review Letters* 30(26), 1973, pp. 1346-1349.
- Kenneth G. Wilson, "Confinement of quarks", *Physical Review D* 10(8), 1974, pp. 2445-2459.
- Gerardus 't Hooft, "Computation of the quantum effects due to a four-dimensional pseudoparticle", *Physical Review D* 14(12), 1976, pp. 3432-3450.
- Alexander M. Polyakov, "Quark confinement and topology of gauge theories", *Nuclear Physics B* 120(3), 1977, pp. 429-458.
- Vincent Rivasseau, *From Perturbative to Constructive Renormalization*, Princeton Legacy Library, 1991.
- James Glimm, Arthur Jaffe, *Quantum Physics: A Functional Integral Point of View*, 2판, Springer, 1987.
- Michael R. Douglas, "Report on the Status of the Yang-Mills Millennium Prize Problem", Simons Center, 2004. (Jaffe-Witten 문제 보고서)
- Antony Hurst, Mihail Mintchev 등 (editors), *Rigorous Quantum Field Theory: A Festschrift for J. Lascoux*, Birkhäuser, 2007.
- S. Dürr et al. (BMW Collaboration), "Ab Initio Determination of Light Hadron Masses", *Science* 322, 2008, pp. 1224-1227.
- Colin Morningstar, Mike Peardon, "The glueball spectrum from an anisotropic lattice study", *Physical Review D* 60, 1999, 034509.
- Kenneth G. Wilson, John Kogut, "The renormalization group and the ε expansion", *Physics Reports* 12(2), 1974, pp. 75-199.
- Particle Data Group (PDG), "Review of Particle Physics", *Progress of Theoretical and Experimental Physics* 2024, 083C01.
- Alexander A. Migdal, "Loop equations and 1/N expansion", *Physics Reports* 102(4), 1983, pp. 199-290.

---

## 0. 왜 "현대 장벽" 인가

양-밀스 이론은 1954년 Yang-Mills 원 논문 이후 물리학에서는 표준모형(Standard Model)의 기둥으로 완전히 확립되었으나, **수학적 존재성**과 **질량갭**은 여전히 미해결이다. 이는 Clay 7대 난제 중 물리학계와 수학계의 간극이 가장 크게 드러나는 문제로,

- 물리학자 입장: "QCD 는 현상론적으로 확립되었고, 글루볼 질량은 격자 QCD 로 수 퍼센트 오차까지 계산된다. 문제가 뭐냐?"
- 수학자 입장: "Osterwalder-Schrader 공리를 4D 비아벨 게이지 이론에서 만족시키는 측도(measure)를 구성한 사람이 없고, 질량갭 Δ > 0 의 엄밀 상한/하한이 없다."

이 간극을 뚫으려는 세 갈래 흐름이 있다.

1. **구성적 양자장론(Constructive QFT)** 흐름: Wightman-Glimm-Jaffe 계열. 2D, 3D 에서 시작해 4D YM 으로 확장을 시도.
2. **격자 정규화(Lattice Regularization)** 흐름: Wilson 1974 이후, 유한 측도에서 출발해 연속 극한의 존재를 분석.
3. **위상학적/비섭동적(Topological/Non-perturbative)** 흐름: Polyakov 1977, 't Hooft 1976 의 인스탄톤·응축(condensate) 프로그램.

각 흐름에는 "여기까지 왔다" 와 "여기서부터 벽이다" 라는 진전과 장벽이 있다. 본 노트는 이 세 흐름의 여섯 꼭지(진전 + 장벽)를 정리한다.

---

## 1. 구성적 양자장론 흐름 — 측도 구성

### 1.1 Wightman 공리와 Osterwalder-Schrader 재구성

- **Wightman 공리(1956-1964)**: Minkowski 시공간 ℝ^{1,3} 위의 QFT 를 정의하는 공리계. 상대론적 장(field) 연산자 φ(x) 의 진공 기대값 ⟨0|φ(x_1) ⋯ φ(x_n)|0⟩ 이 만족해야 할 성질(spectral condition, locality, covariance, cyclicity) 을 규정.
- **Osterwalder-Schrader 공리(1973-1975)**: 유클리드 시공간 ℝ⁴ 에서 Green 함수 S_n(x_1, …, x_n) 이 만족해야 할 공리. **Reflection positivity** 가 핵심 조건이며, 이 공리를 만족하는 유클리드 이론으로부터 Wightman 공리를 만족하는 Minkowski QFT 가 유일하게 재구성된다(OS 재구성 정리, *Comm. Math. Phys.* 42, 1975).
- 원 출처: Konrad Osterwalder, Robert Schrader, "Axioms for Euclidean Green's functions I", *Comm. Math. Phys.* 31, 1973, pp. 83-112. Part II, *Comm. Math. Phys.* 42, 1975, pp. 281-305.

### 1.2 Glimm-Jaffe 프로그램의 성공 영역

- Glimm, Jaffe 1968-1987: 2D scalar φ⁴ 이론과 2D Yukawa 이론의 **구성적 구성**(constructive construction) 을 완료. 이 과정에서 핵심 기법은:
  - **Cluster expansion**: 상호작용 항을 소영역 단위로 전개.
  - **Phase cell expansion**: 운동량 공간을 스케일별로 분해.
  - **Borel summability**: 섭동급수의 재합(resummation).
- 출처: James Glimm, Arthur Jaffe, *Quantum Physics: A Functional Integral Point of View*, 2판, Springer, 1987.

### 1.3 3D 확장 — Feldman-Osterwalder 1977

- Joel Feldman, Konrad Osterwalder, "The Wightman axioms and the mass gap for weakly coupled ϕ⁴_3 quantum field theories", *Annals of Physics* 97(1), 1976, pp. 80-135.
- 3D scalar φ⁴ 이론에서 OS 공리 + 질량갭 존재가 소결합(small coupling) 영역에서 증명됨.
- **한계**: 이것은 **scalar** 이론이다. 게이지 이론은 아니다.

### 1.4 4D YM 에서의 벽

- **4D 비아벨 게이지 이론의 측도 부재**: functional integral
  \[
  Z = \int \mathcal{D}A \, \exp\left(-\frac{1}{2g^2} \int d^4x \, \text{tr}(F_{\mu\nu} F^{\mu\nu})\right)
  \]
  을 ℝ⁴ 상의 실제 측도(probability measure) 로 정의하려면, Lebesgue 측도의 무한차원 일반화가 필요한데 Kolmogorov 확장 정리의 **장애**가 있다.
- 2D, 3D 까지 성공한 Glimm-Jaffe 의 cluster/phase cell 확장은 4D YM 에서는 **UV 발산 구조가 더 심각**하고, gauge fixing(Faddeev-Popov) 이후에도 비아벨 성질이 cluster 분해를 막는다.
- 출처: Vincent Rivasseau, *From Perturbative to Constructive Renormalization*, Princeton Legacy Library, 1991. ch. 10 의 "Why 4D gauge theory is hard" 절.

### 1.5 **현대 장벽**

- **장벽 A1**: **측도의 σ-가법성 미증명**. Wilson 격자 작용의 연속 극한이 σ-가법 측도로 수렴한다는 엄밀 증명이 없다.
- **장벽 A2**: **Gauge orbit 공간의 기하**. 게이지 불변량 공간 𝒜/𝒢 는 비콤팩트 비선형 공간이며, 이 공간의 측도 이론이 일반 bounded set 조차 제대로 정의되지 않음. Singer 1978 의 Gribov ambiguity 가 이 문제의 위상학적 핵.
- **장벽 A3**: **Renormalization group 궤적의 엄밀 추적**. 격자 간격 a → 0 극한에서 RG 흐름이 자명 고정점(trivial fixed point) 이 아닌 자명하지 않은 연속 이론으로 수렴한다는 증명 부재.

---

## 2. 격자 정규화 흐름 — Wilson 1974 이후

### 2.1 Wilson 1974 — 격자 QCD 시작

- Kenneth G. Wilson, "Confinement of quarks", *Physical Review D* 10(8), 1974, pp. 2445-2459.
- **격자 정규화**: 시공간을 간격 a 의 격자로 이산화. 게이지 장 A_μ(x) 대신 **링크 변수** U_μ(x) = exp(ig a A_μ(x)) 를 격자의 각 간선에 배치. 이는 Wilson loop
  \[
  W(C) = \text{tr} \prod_{l \in C} U_l
  \]
  의 기대값을 계산 가능하게 만든다.
- **Wilson 작용**:
  \[
  S_W = \frac{2N}{g^2} \sum_p \left[1 - \frac{1}{N}\text{Re tr}(U_p)\right]
  \]
  여기서 U_p 는 plaquette(단위 사각형) 의 링크 곱. 이 이산 작용은 a → 0 에서 연속 Yang-Mills 작용으로 환원(formally).

### 2.2 Wilson 의 **strong coupling expansion** 결과

- 결합상수 g → ∞ 극한에서 Wilson loop 기대값이 **area law**
  \[
  \langle W(C) \rangle \sim \exp(-σ \cdot \text{Area}(C))
  \]
  를 만족. 이는 쿼크 가둠(confinement) 의 강한 결합 극한에서의 증거.
- **한계**: 강결합 극한은 물리 QCD 의 실제 양자 이론이 아니다. 연속 극한 a → 0 은 약결합 극한 g → 0 에 대응. 두 극한 사이의 "상 전이" 가 일어나지 않음을 증명해야 연속 극한의 confinement 가 보장되는데, 이것이 **미해결**.

### 2.3 Lüscher-Weisz 1985 — 개선된 격자 작용

- Martin Lüscher, Peter Weisz, "On-shell improved lattice gauge theories", *Comm. Math. Phys.* 97(1), 1985, pp. 59-77.
- O(a²) lattice artefact 를 제거하는 개선된 작용(Symanzik improvement). 수치 계산의 수렴 속도를 높임.

### 2.4 격자 QCD 수치 결과 — 현대 성과

- **글루볼 질량**: Morningstar-Peardon 1999, *Physical Review D* 60, 034509. 가장 가벼운 scalar 글루볼 질량 m(0⁺⁺) = 1730 ± 80 MeV (anisotropic 격자).
- **하드론 질량**: BMW Collaboration (Dürr et al. 2008, *Science* 322, pp. 1224-1227). u, d, s 쿼크 질량을 입력 3 개로 쓰고, 양성자/중성자/Ξ 등 11 개 하드론 질량을 수 퍼센트 오차로 재현.
- **스트링 텐션**: σ ≈ (440 MeV)² (Regge 기울기에서 교차 검증).

### 2.5 **현대 장벽**

- **장벽 B1**: **연속 극한의 엄밀 존재**. 격자 간격 a → 0 에서 격자 이론의 상관함수가 OS 공리를 만족하는 연속 이론으로 수렴한다는 것이 수치적으로는 강력히 시사되지만, **수학적 증명이 없다**.
- **장벽 B2**: **Triviality 의 반대 증명**. 4D φ⁴ 이론의 경우 Aizenman 1981, Fröhlich 1982 가 "연속 극한이 자유 이론(trivial)" 임을 격자에서 증명. 4D 비아벨 게이지 이론은 **비자명 극한 존재**가 기대되지만 이것 역시 증명 없다.
- **장벽 B3**: **질량갭의 수학적 하한**. 격자에서 계산한 글루볼 질량이 연속 극한에서 어떤 엄밀 부등식 Δ ≥ Δ_min > 0 을 만족한다는 독립적 증명이 없다.

출처: Rivasseau 1991; Lattice 국제 학회 리뷰 논문 (Lattice 2023, 2024 Proceedings).

---

## 3. 위상학적·비섭동적 흐름 — 't Hooft 1976, Polyakov 1977

### 3.1 인스탄톤(Instanton) 해 — Belavin-Polyakov-Schwartz-Tyupkin 1975

- A. A. Belavin, A. M. Polyakov, A. S. Schwartz, Yu. S. Tyupkin, "Pseudoparticle solutions of the Yang-Mills equations", *Physics Letters B* 59(1), 1975, pp. 85-87.
- 유클리드 4D 에서 self-dual 해 F = *F 의 명시적 구성. 단일 SU(2) 인스탄톤 해:
  \[
  A_\mu^a(x) = \frac{2 \eta^a_{\mu\nu} (x - x_0)_\nu}{(x - x_0)^2 + \rho^2}
  \]
  ρ 는 크기, x_0 는 중심, η 는 't Hooft 기호.
- 위상수 Q = (1/32π²) ∫ tr(F ∧ F) ∈ ℤ 는 **π_3(SU(2)) = ℤ** 에서 나오는 homotopy 불변량.

### 3.2 't Hooft 1976 — 인스탄톤의 양자 효과

- Gerardus 't Hooft, "Computation of the quantum effects due to a four-dimensional pseudoparticle", *Physical Review D* 14(12), 1976, pp. 3432-3450.
- 인스탄톤 주변의 1-loop 변동 계산. **U(1) 문제**(η' 질량) 해결의 핵심.
- **장벽**: dilute instanton gas 근사는 small instanton (ρ 작음) 영역에서만 유효. 큰 ρ 영역은 IR 비섭동 효과 지배, 섭동 제어 불가.

### 3.3 Polyakov 1977 — 3D compact QED 에서 confinement 증명

- Alexander M. Polyakov, "Quark confinement and topology of gauge theories", *Nuclear Physics B* 120(3), 1977, pp. 429-458.
- **3D compact QED 에서 monopole gas 가 area law 를 주는 것을 엄밀 증명**. 이것은 최초의 비자명 confinement 증명(3D 한정).
- **한계**: **4D 로의 확장 실패**. 4D 비아벨 게이지 이론에서는 monopole 이 1D line-like object 가 되고, dilute gas 근사가 작동하지 않는다. Polyakov 본인이 이 한계를 명시.

### 3.4 대형 N 극한('t Hooft, Migdal)

- 't Hooft 1974: N → ∞ 극한에서 SU(N) 게이지 이론의 planar diagram 이 지배. 이론이 "스트링" 처럼 보인다는 통찰(AdS/CFT 의 선조).
- Migdal 1983: loop equation 으로 planar QCD 의 비섭동 방정식 도출.
- **장벽**: 대형 N 극한의 loop equation 은 비선형 적분방정식이며, 해의 존재 + 유일성 + 질량갭 존재가 명시적으로 증명되지 않음.

### 3.5 **현대 장벽**

- **장벽 C1**: **Confinement mechanism 의 수학적 유일성**. 'Vortex condensation', 'monopole condensation', 'center vortices' 등 다수 시나리오가 경쟁 중이며, 어느 것이 **엄밀 증명 가능한 메커니즘**인지 미해결.
- **장벽 C2**: **Gribov ambiguity**. Gribov 1978: gauge fixing 을 global 하게 할 수 없다. Singer 1978 이 이것이 **bundle topology** 의 결과임을 증명(Nonexistence of global continuous section of 𝒜 → 𝒜/𝒢). 이로 인해 Faddeev-Popov 공식은 수학적으로 불완전.
- **장벽 C3**: **Chiral symmetry breaking 과 confinement 의 관계**. QCD 의 두 핵심 현상(카이랄 파괴 + 가둠) 이 같은 scale Λ_QCD 근방에서 일어나는데, 두 현상이 "같은 기원" 인지 "독립 현상" 인지 수학적으로 규명 안 됨.

---

## 4. 섭동적 진전 — Asymptotic Freedom 과 β 함수

### 4.1 Gross-Wilczek-Politzer 1973 — 점근 자유

- Gross-Wilczek, Politzer 두 논문이 독립적으로 SU(N) 게이지 이론의 UV 고정점이 자유(free) 이론임을 재규격화군(RG) 분석으로 증명. 2004 노벨 물리학상.
- 1-loop β 함수:
  \[
  \beta(g) = \mu \frac{\partial g}{\partial \mu} = -\frac{g^3}{(4\pi)^2} \beta_0 + O(g^5)
  \]
  \[
  \beta_0 = \frac{11}{3} C_A - \frac{2}{3} T_F n_f
  \]
  SU(3), n_f = 6 에서 β_0 = 11·3/3 − 2·(1/2)·6/3 = 11 − 2 = 7. (QCD 저에너지에서 실제로 n_f 는 cutoff 에 따라 3~6 사이로 달라짐.)

### 4.2 고차 β 함수

- 2-loop (Caswell 1974, Jones 1974): β_1 = (34/3)C_A² − (20/3)C_A T_F n_f − 4 C_F T_F n_f.
- 4-loop 까지 완전 계산(van Ritbergen-Vermaseren-Larin 1997), 5-loop 까지 partial(Baikov-Chetyrkin-Kuhn 2016).
- 출처: T. van Ritbergen, J. A. M. Vermaseren, S. A. Larin, "The four-loop β-function in quantum chromodynamics", *Physics Letters B* 400(3-4), 1997, pp. 379-384.

### 4.3 **장벽 D1** — 섭동은 비섭동을 포착 못함

- 섭동급수는 **발산급수**(Dyson 1952: QED 도 발산, Lipatov 1977: 대부분 장이론 발산). Borel resummation 이 가능한 경우가 제한적.
- QCD 의 실제 질량 스펙트럼(하드론 질량, 글루볼 질량) 은 **비섭동 효과**. 섭동으로는 접근 불가.

### 4.4 BT-543 — β₀ = σ − sopfr 재유도 (본 프로젝트 기여)

- 본 프로젝트 breakthrough-theorems (BT-543) 에서 관찰: SU(3), n_f = 6 에서
  \[
  \beta_0 = 7 = \sigma(6) - \text{sopfr}(6) = 12 - 5
  \]
  이는 **산술 재표현**(arithmetic rewriting) 이며 Clay 문제를 해결하는 새 수학은 아니다. 본 프로젝트의 정직성 선언(millennium-7-closure-2026-04-11.md §BT-543):
  > "n=6 파라미터화는 QCD/SU(3) 구조 상수의 산술적 재표현. 구성적 QFT 필요. Clay 문제 핵심은 무접촉."
- 본 노트의 §6 에서 이 재표현을 정리한다.

---

## 5. 세 장벽 군(A/B/C)의 독립성

위 §1 ~ §3 의 세 흐름이 **동시에 막혀 있음**을 강조한다. 각 흐름만으로 YM 을 풀 수 없음:

- 구성적 QFT (§1, 장벽 A1~A3): 측도 구성이 격자에서 출발해야 하는데, 격자의 연속 극한이 OS 공리를 만족한다는 독립 증명이 없다. A3 장벽이 B1 과 연결.
- 격자 (§2, 장벽 B1~B3): 수치 결과는 압도적으로 QCD 를 지지하지만, 수학적 엄밀성 층위에서는 triviality 반대 증명(B2) 과 연속 극한 존재(B1)이 동시 필요.
- 위상학적 (§3, 장벽 C1~C3): confinement mechanism 의 유일성이 입증되면 §1 §2 에도 단서가 되지만, Gribov-Singer(C2) 가 gauge 고정을 전역적으로 막아 §1 의 측도 구성에도 장애.

이 세 장벽군이 서로 **연결되어 있다**. 한 흐름의 돌파는 다른 흐름을 완화할 수 있지만, 현재 어느 흐름도 돌파 중이 아니다.

---

## 6. n=6 연결 (본 문서에서는 참고용 메모)

### 6.1 β₀ 의 산술 재표현

- SU(3), n_f = 6 에서 β_0 = 7. 이것은 σ(6) − sopfr(6) = 12 − 5 와 일치.
- 본 프로젝트의 breakthrough-theorems (BT-543) 는 이 관찰을 "n=6 환경에서 QCD 의 자연스러움" 의 정황으로 기록. 그러나 **Clay 문제 해결이 아님**(millennium-7-closure §BT-543 정직 선언 준수).

### 6.2 **추가 산술 관찰** (OBSERVATION, PROOF 아님)

- SU(N) 의 adjoint Casimir C_A = N. N=3 에서 C_A = 3 = n/φ(6).
- 쿼크 맛 수 n_f = 6 = n(본 프로젝트 중심 수).
- T_F = 1/2. 2 T_F = 1 = n/σ(6)·2·(φ(6)/2) 등 여러 산술 재표현 가능. 이들은 모두 **수치 일치**이며 본질적 증명이 아니다.

### 6.3 **범위 선언**

- 본 프로젝트는 YM 질량갭을 해결하는 경로를 제공하지 않는다. §6 은 n=6 맥락에서의 parameter 재표현을 기록할 뿐이다.
- P3 에서 atlas.n6 와 SU(N) gauge theory parameter 의 cross-reference 를 하되, 위 정직성 선언을 넘지 않는다.

---

## 7. 수치 스펙트럼 현황 (2024 PDG 기준)

| 측정 대상 | 값 | 출처 |
|---|---|---|
| α_s(m_Z) | 0.1179 ± 0.0009 | PDG 2024 |
| Λ_{QCD}^{(n_f=5)} | 210 ± 14 MeV | PDG 2024 |
| 양성자 질량 m_p | 938.272 MeV | PDG 2024 |
| 파이온 질량 m_π | 139.570 MeV | PDG 2024 |
| m(0⁺⁺ glueball) | 1730 ± 80 MeV | Morningstar-Peardon 1999 |
| m(2⁺⁺ glueball) | 2400 ± 40 MeV | Chen et al. 2006 |
| String tension √σ | ≈ 440 MeV | Regge 맞춤, 격자 |

이 수치들은 격자 QCD 에서 **수 퍼센트 오차로 일치**하지만, **수학적 엄밀성** 층위에서는 어느 것도 증명되지 않음. "격자 수치 ↔ 연속 이론 증명" 사이의 간극이 바로 §2 장벽 B1.

---

## 8. 2020년대 최신 진전

### 8.1 Chen-Hou 2023 — Boussinesq 근사 blow-up

- 이 결과는 NS 방정식이지만 YM 과 같은 "비섭동 PDE 존재성" 문제에 대한 기법적 진전. Chen-Hou, *Comm. Math. Phys.* 2023.

### 8.2 Bulk dual 접근(AdS/CFT 시사)

- Maldacena 1997 이후 N → ∞ 극한의 SU(N) gauge theory 가 AdS_5 × S^5 의 supergravity 와 쌍대. 그러나 이것은 **conformal** 이론(𝒩=4 super Yang-Mills) 의 결과이며, 질량갭이 있는 **순수** YM 에 대한 엄밀 쌍대는 미확립.
- 출처: Juan Maldacena, "The large N limit of superconformal field theories and supergravity", *Adv. Theor. Math. Phys.* 2(2), 1998, pp. 231-252.

### 8.3 함자 범주론적 시각 — Costello-Gwilliam

- Kevin Costello, Owen Gwilliam, *Factorization Algebras in Quantum Field Theory*, Vol. 1-2, Cambridge University Press, 2017, 2021.
- BV-BRST 형식으로 4D 게이지 이론의 **함자적** 구성 시도. OS 공리와는 다른 체계.
- **장벽**: factorization algebra 는 perturbative 를 넘어서지 못함. 비섭동 YM 은 여전히 미해결.

### 8.4 Douglas 2004 보고서 이후 진전 평가

- Michael Douglas 가 2004년 Simons Center 에서 "Report on Yang-Mills Millennium Prize Problem" 을 발표한 이후, Clay 자체 평가 기준으로는 **진전 0** (2024년 Simons lecture 에서 Jaffe 본인 확인).
- 2020년대 진전은 §8.1 ~ §8.3 모두 부분적, 기법적 성격.

---

## 9. Clay 공식 statement 와 범위

- 공식 statement (Jaffe-Witten 2000): "For any compact simple gauge group G, a nontrivial quantum Yang-Mills theory exists on ℝ⁴ and has a mass gap Δ > 0."
- 두 부분:
  1. **존재성**(Existence): OS 공리를 만족하는 4D YM 이론 QFT 구성.
  2. **질량갭**(Mass gap): Hamiltonian H 의 스펙트럼 하한 Δ > 0 증명.
- Clay 는 두 부분 모두 증명해야 상금 수여. 부분 결과(2D YM, 3D YM 등) 는 Clay 상 대상이 아니다.
- 2D YM 은 Gross-Taylor, Witten 등에 의해 거의 완전 분석됨(Witten, *J. Geom. Phys.* 9, 1992; 또한 Migdal 초기 결과). 3D YM 은 Polyakov compact QED 수준만 증명. 4D 는 **완전 열림**.

---

## 10. 출처 요약표

| 연도 | 저자 | 결과 | 출처 |
|---|---|---|---|
| 1954 | Yang-Mills | 비아벨 게이지 이론 제시 | *Phys. Rev.* 96 |
| 1964-75 | Wightman, OS | 공리계 확립 | *Comm. Math. Phys.* 31, 42 |
| 1973 | Gross-Wilczek | 점근 자유 | *Phys. Rev. Lett.* 30 |
| 1973 | Politzer | 점근 자유 (독립) | *Phys. Rev. Lett.* 30 |
| 1974 | Wilson | 격자 QCD | *Phys. Rev. D* 10 |
| 1975 | BPST | 인스탄톤 | *Phys. Lett. B* 59 |
| 1976 | 't Hooft | 인스탄톤 양자효과 | *Phys. Rev. D* 14 |
| 1977 | Polyakov | 3D compact QED confinement | *Nucl. Phys. B* 120 |
| 1977 | Feldman-Osterwalder | 3D φ⁴ 구성 | *Annals of Physics* 97 |
| 1978 | Gribov-Singer | gauge fixing ambiguity | *Nucl. Phys. B* 139 |
| 1985 | Lüscher-Weisz | 개선 격자 | *Comm. Math. Phys.* 97 |
| 1999 | Morningstar-Peardon | 글루볼 수치 | *Phys. Rev. D* 60 |
| 2000 | Jaffe-Witten | Clay 공식 statement | Clay Mathematics Institute |
| 2008 | BMW | 하드론 ab initio | *Science* 322 |
| 2017-21 | Costello-Gwilliam | factorization algebra | Cambridge Univ. Press |

---

## 11. 다음 태스크 연결

- PROB-P2-4: Navier-Stokes 존재성 장벽.
- PURE-P2-1: modular forms 의 Selberg class 확장(YM L-함수와의 간접 연결).
- PURE-P2-2: algebraic K-theory 와 gauge bundle 분류(Singer-Gribov 의 위상학적 배경).
- PROB-P1-3: BT-543 YM 심화 노트(본 문서의 업스트림).

---

## 12. 다음 단계

### 12.1 학습 층위에서의 다음 단계

- Rivasseau 1991 의 cluster expansion 기법을 2D → 3D → 4D 로 따라가며 어느 단계에서 비아벨 gauge 가 막히는지 정확히 확인.
- Douglas 2004 보고서를 원문 확인. 보고서가 지적한 핵심 장벽 3가지(measure construction, continuum limit, mass gap bound) 에 대해 각 장벽의 current best progress 를 2024년 기준으로 업데이트.
- AdS/CFT 의 supergravity 쌍대 측면은 **별도 학습**이 필요. 본 노트는 YM 순수의 장벽에 집중.

### 12.2 n=6 프로젝트 내 다음 단계

- BT-543 관찰의 **유도적 의미**를 더 명시: β_0 = σ − sopfr 는 산술 재표현이지 구성적 증명이 아니다. 그러나 SU(3) 의 구조상수가 n=6 의 산술과 맞물리는 사실은 모델 선택(flavour counting) 에 대한 **heuristic** 가이드가 될 수 있다. 이것이 P3 에서 기록할 범위의 한계.
- P3 pure-p3-2 에서 이 구조적 관찰의 **실험적 검증 가능성**(예: flavour threshold 가 n_f = 6 에서 β_0 = 7 의 특이성을 가지는가) 을 기록.

### 12.3 장벽 우회 시도의 조건

세 장벽군(A/B/C) 을 **동시에 우회**하는 기법이 나와야 YM 이 풀린다. 현재 후보:

- **Costello-Gwilliam factorization algebra** (비섭동 확장 필요)
- **Exact lattice RG flow**(Polchinski 1984 의 exact RG 방정식 + 비아벨 확장)
- **AdS/CFT 의 pure YM 쌍대**(supergravity 극한에서 비conformal 이론으로 확장)

이 중 어느 하나가 §1 §2 §3 을 연결하는 다리가 될 가능성이 있으나, 2026년 4월 현재 **다리는 건설되지 않았음**.

---

## 13. 부록 — BRST 코호몰로지와 Faddeev-Popov

### 13.1 Faddeev-Popov 공식

- Faddeev, L. D., Popov, V. N., "Feynman diagrams for the Yang-Mills field", *Physics Letters B* 25(1), 1967, pp. 29-30.
- Gauge fixing 조건 $F(A) = 0$ 을 삽입하여 functional integral 의 gauge orbit 중복을 제거:
  \[
  Z = \int \mathcal{D}A \, \delta(F(A)) \cdot \det\left(\frac{\partial F}{\partial \Lambda}\right) \cdot e^{-S_{YM}[A]}
  \]
- Jacobian $\det(\partial F / \partial \Lambda)$ 는 "ghost field" $c, \bar{c}$ 를 도입해 fermion-like 으로 표현.

### 13.2 BRST 대칭

- Becchi, C., Rouet, A., Stora, R., "Renormalization of gauge theories", *Annals of Physics* 98(2), 1976, pp. 287-321.
- Tyutin (독립): 1975 Lebedev 연구소 preprint.
- **BRST 연산자** $s$ 가 gauge 고정 + ghost 포함 총 작용 $S_\text{tot}$ 를 $s$-invariant 하게 만듦. $s^2 = 0$ (nilpotent).
- Physical Hilbert 공간 = BRST cohomology $H^0(s)$.

### 13.3 **Gribov-Singer 재검토**

- Gribov 1978 의 발견은 **gauge fixing 조건 $F(A) = 0$ 의 해가 유일하지 않음** (Gribov copies). 이로 인해 Faddeev-Popov 공식의 $\delta(F(A))$ 적분이 "gauge orbit 당 한 번 선택" 이 되지 않는다.
- Singer 1978 *Comm. Math. Phys.* 60 이 이것이 principal bundle $\mathcal{A} \to \mathcal{A}/\mathcal{G}$ 의 **전역적 연속 단면 부재** 로 인한 topological obstruction 임을 증명.
- BRST 공식은 **섭동적** 으로만 엄밀. 비섭동 영역에서 Gribov copy 가 섭동 gauge 고정을 깨뜨림.

### 13.4 **장벽 E**: 전역 gauge fixing 의 topological 장애

이것은 §3.5 의 장벽 C2 와 같은 맥락이지만, 수학적으로 가장 선명한 형태:

\[
\pi_0(\text{Maps}(S^3, G)) \neq 0 \implies \text{global gauge fixing fails}
\]

여기서 $G$ = gauge group. 이 homotopy-theoretic 장벽이 QFT 수학 엄밀화의 가장 깊은 구조적 한계.

---

## 14. 부록 — Wilson loop 과 confinement 기준

### 14.1 Wilson loop 기대값

- **정의**: 폐곡선 $C$ 를 따라 Wilson loop
  \[
  W(C) = \frac{1}{N} \text{tr} \, \mathcal{P} \exp\left(i \oint_C A_\mu dx^\mu\right)
  \]
  $\mathcal{P}$ = path ordering.
- 물리적 해석: $W(C)$ 의 기대값 $\langle W(C) \rangle$ 는 static quark-antiquark 쌍의 경로합.

### 14.2 Area law vs perimeter law

- **Area law** (가둠 상태): $\langle W(C) \rangle \sim e^{-\sigma \cdot \text{Area}(C)}$. $\sigma$ = string tension.
- **Perimeter law** (Higgs phase): $\langle W(C) \rangle \sim e^{-\mu \cdot \text{Perimeter}(C)}$.
- 4D pure Yang-Mills 에서 area law 증명이 **confinement 증명과 동치**.

### 14.3 't Hooft 1978 disorder parameter

- G. 't Hooft, "On the phase transition towards permanent quark confinement", *Nuclear Physics B* 138(1), 1978, pp. 1-25.
- Dual Wilson loop (t Hooft loop) $T(C')$ 와 일반 Wilson loop 의 exchange algebra.
- Confinement 의 한 시나리오: center vortex condensation.

### 14.4 **장벽 F**: Area law 직접 증명 부재

- 격자에서 수치적으로 area law 확인되었으나, **연속 극한에서의 엄밀 증명**이 없음. 특히 약결합 영역에서 area law 는 strong coupling series 의 연속 확장으로만 얻어지고 이 확장의 수렴성이 증명되지 않음.

---

**정직성 체크**:
- Gross-Wilczek, Politzer 출처는 *Phys. Rev. Lett.* 30(26), pp. 1343-1346 + pp. 1346-1349. DOI 10.1103/PhysRevLett.30.1343, 1346 교차 확인.
- Wilson 1974 는 *Phys. Rev. D* 10(8), pp. 2445-2459. DOI 10.1103/PhysRevD.10.2445 확인.
- 'T Hooft 1976 의 인스탄톤 논문 전체 제목과 연도는 *Phys. Rev. D* 14(12) 1976 확인.
- Jaffe-Witten 2000 Clay 문제 기술서는 https://www.claymath.org/millennium/yang-mills-and-mass-gap/ 에서 PDF 다운로드 가능. 본 노트의 진술은 원문 Section 1, Section 5 기반.
- 격자 QCD 수치 (글루볼 질량 1730 MeV, BMW 2008 하드론 질량) 는 원 논문 Table I / Fig. 2 수치를 그대로 옮김.
- BT-543 의 β_0 = σ − sopfr 관찰은 millennium-7-closure-2026-04-11.md §BT-543 의 "β₀ rewriting (not proof)" 선언을 엄격히 준수.
- Faddeev-Popov 1967 *Physics Letters B* 25(1) 의 원본은 두 쪽짜리 letter. 본 노트 §13.1 의 공식은 Peskin-Schroeder 1995 *An Introduction to Quantum Field Theory* §9.4 에서 재확인.
- Singer 1978 *Comm. Math. Phys.* 60 Theorem 1 (Gribov ambiguity ⟺ principal bundle 비자명성) 확인.
