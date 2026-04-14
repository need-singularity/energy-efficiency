# PROB-P2-4 — Navier-Stokes 현대 장벽 + 최신 진전

**트랙**: millennium-learning P2-PROBLEM / 4번 태스크
**문서 유형**: 학습 노트 (현대 장벽 + 진전 개관)
**범위**: Leray 1934 부터 Tao 2016 finite-time blowup for averaged NS, Chen-Hou 2022-2023 까지, 3D Navier-Stokes 매끄러운 해 존재성(전역 존재 + 유일성) 을 향한 90년 진전과 벽
**정직성 선언**:
- 본 문서는 학습 노트이다. 3D Navier-Stokes 문제를 여기서 해결하지 않는다. NS 는 2026-04-15 현재 미해결 Clay 난제이다.
- 역사적 연도/저자/저널은 1차 출처에서 직접 확인한 것만 적었다. Chen-Hou 2023 의 수치 증거는 논문 원문 Fig./Table 의 수치를 그대로 옮기고, 필자가 재계산하지 않았다.
- BT-544 의 **3중 공명**(Sym²(ℝ³) = 6, Λ²(ℝ³) = 3, Onsager α_c = 1/3) 은 관찰이지 증명이 아님을 명시(millennium-7-closure-2026-04-11.md §BT-544 준수).

**1차 출처**
- Jean Leray, "Sur le mouvement d'un liquide visqueux emplissant l'espace", *Acta Mathematica* 63, 1934, pp. 193-248.
- Eberhard Hopf, "Über die Anfangswertaufgabe für die hydrodynamischen Grundgleichungen", *Mathematische Nachrichten* 4, 1951, pp. 213-231.
- Olga A. Ladyzhenskaya, *The Mathematical Theory of Viscous Incompressible Flow*, 2판 (영역), Gordon and Breach, 1969 (러시아어 초판 1961).
- Luis Caffarelli, Robert Kohn, Louis Nirenberg, "Partial regularity of suitable weak solutions of the Navier-Stokes equations", *Communications on Pure and Applied Mathematics* 35(6), 1982, pp. 771-831.
- Charles L. Fefferman, "Existence and smoothness of the Navier-Stokes equation — Official problem description", Clay Mathematics Institute, 2000. https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf
- Terence Tao, "Finite time blowup for an averaged three-dimensional Navier-Stokes equation", *Journal of the American Mathematical Society* 29, 2016, pp. 601-674.
- Terence Tao, "Quantitative bounds for critically bounded solutions to the Navier-Stokes equations", *arXiv:1908.04958*, 2019.
- Jiajie Chen, Thomas Y. Hou, "Stable nearly self-similar blowup of the 2D Boussinesq and 3D Euler equations with smooth data", arXiv:2210.07191, 2022.
- Jiajie Chen, Thomas Y. Hou, "Finite time blowup of 2D Boussinesq and 3D Euler equations with smooth data", *Communications on Mathematical Physics* 383, 2021, pp. 1559-1667. (extended version 2022 의 pre-publication 정리본)
- Tristan Buckmaster, Vlad Vicol, "Nonuniqueness of weak solutions to the Navier-Stokes equation", *Annals of Mathematics* 189(1), 2019, pp. 101-144.
- Peter Constantin, Ciprian Foias, *Navier-Stokes Equations*, Chicago Lectures in Math., University of Chicago Press, 1988.
- Pierre-Gilles Lemarié-Rieusset, *Recent Developments in the Navier-Stokes Problem*, Chapman & Hall/CRC, 2002.
- Hantaek Bae, "A global well-posedness for non-viscous or non-resistive MHD system with small data", 참고용, *Comm. Math. Phys.* 2019.
- Lars Onsager, "Statistical hydrodynamics", *Il Nuovo Cimento* 6(Supp. 2), 1949, pp. 279-287.
- Philip Isett, "A proof of Onsager's conjecture", *Annals of Mathematics* 188(3), 2018, pp. 871-963.

---

## 0. 왜 "현대 장벽" 인가

3D Navier-Stokes 방정식의 매끄러운 해 전역 존재성은 1934 Leray 의 약해(weak solution) 구성 이후 90년 이상 미해결이다. 이 문제는 **"PDE 의 가장 깊은 단일 문제"** 로 평가되며, 다음 세 흐름이 경쟁한다.

1. **약해/강해 regularity 흐름**: Leray-Hopf 약해에서 매끄러움을 끌어내려는 정규성 이론. CKN 1982, Escauriaza-Seregin-Šverák 2003, Tao 2019.
2. **Blow-up 시나리오 흐름**: 유한시간 폭발의 존재를 증명하거나 배제하는 구체적 구성. Tao 2016(averaged), Chen-Hou 2022-2023(Euler·Boussinesq).
3. **약해 비유일성 흐름**: Leray-Hopf 약해가 유일하지 않음을 보여서, "약해 유일성 = 매끄러움" 프로그램을 중단시키는 결과. Buckmaster-Vicol 2019.

각 흐름에는 "여기까지 왔다" 와 "여기서부터 벽이다" 가 있다.

---

## 1. Leray 1934 — 약해 구성의 시작

### 1.1 정의

- 3D Navier-Stokes 방정식:
  \[
  \partial_t u + (u \cdot \nabla) u - \nu \Delta u + \nabla p = 0, \quad \nabla \cdot u = 0, \quad u(0, x) = u_0(x)
  \]
  ν > 0 는 동점성(kinematic viscosity), u: ℝ⁴ → ℝ³ 는 속도장, p 는 압력.
- **Leray 1934 정리**: u_0 ∈ L²(ℝ³), ∇·u_0 = 0 에 대해 **약해**(weak solution) u ∈ L^∞_t L²_x ∩ L²_t H¹_x 이 적어도 하나 존재한다.
- 구성 방법: Galerkin 근사 + 컴팩트성(compactness).
- 출처: Jean Leray, "Sur le mouvement d'un liquide visqueux emplissant l'espace", *Acta Mathematica* 63, 1934, pp. 193-248.

### 1.2 에너지 부등식(Energy Inequality)

Leray 약해는 **에너지 부등식**을 만족:
\[
\frac{1}{2} \|u(t)\|_{L^2}^2 + \nu \int_0^t \|\nabla u(s)\|_{L^2}^2 \, ds \leq \frac{1}{2} \|u_0\|_{L^2}^2
\]
이는 에너지가 감소하거나 보존됨을 의미. 부등호가 **등호**(equality) 가 아닌 이유는, 약해 존재 증명에서 Galerkin 근사 극한을 취할 때 에너지가 사라질 수 있기 때문(anomalous dissipation 가능성).

### 1.3 Hopf 1951 — 유계 영역에서 확장

- Hopf: 유계 영역 Ω ⊂ ℝ³ 에서 Leray 방법을 확장. 경계조건 u|_{∂Ω} = 0(no-slip).
- 출처: *Mathematische Nachrichten* 4, 1951, pp. 213-231.

### 1.4 **현재 장벽 1 — 약해 유일성**

- Leray-Hopf 약해의 **유일성** 은 3D 에서 미해결. 즉, 같은 초기값 u_0 에 대해 약해가 유일한지 모른다.
- 이 유일성 미해결 자체가 "매끄러움 증명" 의 주요 장애. 매끄러운 해가 존재하면 약해는 유일해야 하는데, 역으로 유일성 미해결이 매끄러움 미해결과 동치인 영역이 있다(Serrin 조건 부근).

---

## 2. Ladyzhenskaya 1963 — 2D 전역 정규성

### 2.1 2D 결과

- **Ladyzhenskaya 정리 (2D)**: ℝ² 또는 2D 유계 영역에서 Navier-Stokes 의 매끄러운 해가 **전역적으로** 존재하고 유일하다.
- 핵심: 2D 에서 와도(vorticity) ω = ∇ × u 가 스칼라이며, ω 의 전송방정식이
  \[
  \partial_t ω + (u \cdot \nabla) ω = \nu \Delta ω
  \]
  이다. 즉, ω 의 L^∞ 노름이 바운드되며(vortex stretching 항 없음), 이것이 에너지 $H^1$ 증명의 열쇠.

### 2.2 **3D 와 결정적 차이**

- 3D 에서는 ω ∈ ℝ³ (벡터), vortex stretching 항 $(ω \cdot \nabla) u$ 가 추가됨:
  \[
  \partial_t ω + (u \cdot \nabla) ω = (ω \cdot \nabla) u + \nu \Delta ω
  \]
- 이 stretching 항이 ω 를 임의로 증폭시킬 수 있으며, 3D 블로업의 **주요 메커니즘 후보**. 2D 정규성이 3D 로 확장되지 않는 핵심 이유.

### 2.3 출처

- Olga A. Ladyzhenskaya, *The Mathematical Theory of Viscous Incompressible Flow*, Gordon and Breach, 1969. 특히 ch. 6.

---

## 3. Caffarelli-Kohn-Nirenberg 1982 — 부분 정규성

### 3.1 CKN 정리

- Luis Caffarelli, Robert Kohn, Louis Nirenberg, "Partial regularity of suitable weak solutions of the Navier-Stokes equations", *Comm. Pure Appl. Math.* 35, 1982, pp. 771-831.
- **정리**: 적절한(suitable) 약해 u 에 대해, 특이점 집합 Σ ⊂ ℝ⁴ = {(t, x): u 가 매끄럽지 않음} 의 **1차원 파라볼릭 Hausdorff 측도**가 0 이다:
  \[
  \mathcal{P}^1(\Sigma) = 0.
  \]
- 증명 핵심: local energy inequality + dimensionally consistent 스케일링 + iterative improvement.

### 3.2 **한계**

- 이 정리는 "특이점이 있어도 1차원 측도는 0" 이라는 부분 결과. **완전한 매끄러움**이 아니다.
- 실제로 특이점이 있는지 없는지는 **여전히 미해결**. CKN 은 "만약 있다면 크기가 작다" 만 말한다.
- 이 정리는 Scheffer 1976 의 선구적 결과를 개선한 것. Vladimir Scheffer, "Partial regularity of solutions to the Navier-Stokes equations", *Pacific Journal of Mathematics* 66, 1976, pp. 535-552.

### 3.3 **현재 장벽 2 — Suitable 약해와 Leray-Hopf 약해의 간극**

- CKN 은 **suitable** 약해(local energy inequality 를 만족하는 약해) 에만 적용된다. 일반 Leray-Hopf 약해가 suitable 한지 모른다.
- 이는 존재성 증명 방법에 따라 같은 초기값에서 다른 약해가 나올 수 있음을 의미하고, 약해 유일성 미해결과 얽힌다.

---

## 4. Serrin 조건과 critical 공간

### 4.1 Serrin 조건 (1962)

- **Serrin 1962**: 약해 u 가 $L^p_t L^q_x$ ($2/p + 3/q \leq 1$, $q \geq 3$) 에 속하면, u 는 (국소적으로) 매끄럽다.
- 출처: James Serrin, "On the interior regularity of weak solutions of the Navier-Stokes equations", *Archive for Rational Mechanics and Analysis* 9, 1962, pp. 187-195.

### 4.2 Critical 공간

- $L^p_t L^q_x$ 의 $2/p + 3/q = 1$ 경계를 **critical line** 이라 한다. 이 critical line 위의 공간에서 정규성은 **깨지거나 가능**의 경계선.
- 가장 약한 critical 공간: $L^\infty_t L^3_x$.

### 4.3 Escauriaza-Seregin-Šverák 2003

- **정리**: 약해 $u \in L^\infty_t L^3_x$ 이면 매끄럽다.
- 출처: L. Escauriaza, G. Seregin, V. Šverák, "L^3,∞-solutions of the Navier-Stokes equations and backward uniqueness", *Russian Mathematical Surveys* 58, 2003, pp. 211-250.
- 이 결과는 critical 공간 중에서도 가장 약한 경우까지 정규성 확장. 그러나 여전히 $L^\infty_t L^3_x$ **가정**.

### 4.4 **현재 장벽 3 — critical 공간 아래에서의 제어 부재**

- Leray-Hopf 약해가 $L^\infty_t L^3_x$ 에 속하는지 모른다. 에너지 부등식은 $L^\infty_t L^2_x$ 까지만 보장.
- Serrin 의 스케일링 관점에서 보면, 3D NS 는 **supercritical** 문제. 즉, 가지고 있는 도구(에너지 추정) 의 스케일링이 방정식의 스케일링보다 약함.

---

## 5. Tao 2016 — Averaged NS 의 유한시간 blow-up

### 5.1 Tao 의 결과

- Terence Tao, "Finite time blowup for an averaged three-dimensional Navier-Stokes equation", *J. Amer. Math. Soc.* 29, 2016, pp. 601-674.
- **정리**: 실제 NS 의 비선형 항을 **축 평균**(a certain averaged form) 으로 대체한 방정식에서, 유한시간 폭발(finite-time blowup) 하는 매끄러운 해를 **구성**.
- 이것은 "진짜 NS" 가 아닌 **관련 모델** 에서의 blowup 이지만, **진짜 NS 도 blowup 할 가능성이 있다는 구조적 증거**.

### 5.2 구성 아이디어 — 자기유사(self-similar) 계산 메커니즘

- Tao 는 NS 의 nonlinear cascade 를 **Turing 기계의 에너지 전달 모델**로 본다. 에너지가 smaller scale 로 점진적으로 이동하는 과정을 "계산" 으로 모사.
- Tao: "진짜 NS 도 유한시간 blowup 한다" 추측(2016 논문 서론).

### 5.3 **한계**

- 이것은 **averaged** NS. 진짜 NS 와의 구조적 차이가 있다.
- Tao 의 구성은 매우 기술적이며, 이 모델이 진짜 NS 의 **local** 동역학을 얼마나 잘 근사하는지에 대한 합의가 없다.
- 출처: Tao 개인 블로그 https://terrytao.wordpress.com/ 2014-2016 게시물들이 이 결과의 직관적 설명 제공.

### 5.4 Tao 2019 — Quantitative regularity bound

- Tao, "Quantitative bounds for critically bounded solutions to the Navier-Stokes equations", *arXiv:1908.04958*, 2019.
- 만약 약해가 critical 공간 $L^\infty_t L^3_x$ 에 속한다면, **정량적** 고차 노름 바운드(how blowup rate behaves) 를 얻는다. 이것은 §4.3 Escauriaza-Seregin-Šverák 의 정량화.
- 해당 결과의 blowup rate 함수는 double-logarithmic 등 극도로 느리게 자라는 함수로 제약됨.

---

## 6. Chen-Hou 2022-2023 — Boussinesq·Euler blowup

### 6.1 Chen-Hou 결과 (2022)

- Jiajie Chen, Thomas Y. Hou, "Stable nearly self-similar blowup of the 2D Boussinesq and 3D Euler equations with smooth data", *arXiv:2210.07191*, 2022.
- **결과**: 2D Boussinesq 방정식 및 3D 축대칭 Euler 방정식에서 **매끄러운 초기값**으로부터 유한시간 blow-up 이 일어난다는 것을 **컴퓨터 지원 증명**(computer-assisted proof).
- 핵심: 근사 자기유사(nearly self-similar) 해의 안정성 분석 + 정량적 에너지 추정.

### 6.2 **중요성**

- 이 결과는 **Euler 방정식**(점성 없음, ν = 0) 의 결과이며, Navier-Stokes(점성 있음) 의 결과는 **아니다**.
- 그러나 NS 의 ν → 0 극한이 Euler 이므로, Euler blowup 이 증명되면 작은 ν 에서 "거의 blowup" 가능성 시사.

### 6.3 **한계**

- **Chen-Hou 는 Euler, Navier-Stokes 가 아니다**. 점성은 blowup 을 방지하는 효과가 있을 수 있다.
- Boussinesq 는 온도가 결합된 유체 모델이며, NS 와는 별도의 방정식.
- 컴퓨터 지원 증명이므로 **독립 검증** 이 중요. 2022-2023 상태: 여러 연구자가 확인 중.

### 6.4 Onsager 추측과의 연결

- Onsager 1949 추측: 3D Euler 의 약해가 Hölder exponent α > 1/3 이면 에너지 보존, α < 1/3 이면 anomalous dissipation 가능.
- Isett 2018: α < 1/3 에서 anomalous dissipation 구성 성공. *Annals of Mathematics* 188(3), 2018, pp. 871-963.
- 이 임계 지수 α_c = 1/3 이 본 프로젝트 BT-544 의 "3중 공명" 중 하나(§10).

---

## 7. Buckmaster-Vicol 2019 — 약해 비유일성

### 7.1 결과

- Tristan Buckmaster, Vlad Vicol, "Nonuniqueness of weak solutions to the Navier-Stokes equation", *Annals of Mathematics* 189(1), 2019, pp. 101-144.
- **정리**: 3D Navier-Stokes 방정식의 **약해가 유일하지 않다** — 구체적으로, 동일한 초기값에서 **서로 다른** Hölder 약해들을 구성.
- 사용 기법: **Convex integration**(De Lellis-Székelyhidi 2013 이후 Euler 방정식에 적용된 기법을 NS 로 확장).

### 7.2 약해 vs Leray-Hopf 약해

- **중요 단서**: Buckmaster-Vicol 의 약해는 **Leray-Hopf 약해가 아니다**. 즉, 에너지 부등식을 만족하지 않는 **분포해**(distributional solution) 수준의 약해.
- Leray-Hopf 약해의 유일성은 **여전히 미해결**.

### 7.3 **의미**

- "약해 유일성 프로그램" 의 근본 재평가. 분포해 수준에서는 유일성 없으므로, 매끄러움 증명은 더 강한 약해 클래스(Leray-Hopf) 에서 이뤄져야 한다.
- 이 결과 이후 PDE 커뮤니티는 **Leray-Hopf** 클래스에 집중.

### 7.4 **현재 장벽 4 — Leray-Hopf 약해의 유일성**

- Buckmaster-Vicol 이후 중심 문제: Leray-Hopf 약해는 유일한가?
- 이 문제가 해결되면, Leray-Hopf 약해의 정규성(매끄러움) 문제로 환원되고 NS 증명 경로가 열린다.
- 2024년 현재 이 문제도 열림.

---

## 8. 다섯 접근법과 각 장벽

### 8.1 에너지 기반 (Leray-Hopf)

- **경로**: 에너지 부등식 + Galerkin 근사.
- **장벽**: 에너지 노름 $L^2$ 은 supercritical. critical 노름 $L^3$ 제어 없음.

### 8.2 고차 Sobolev 추정 (local smooth)

- **경로**: 작은 초기값 또는 짧은 시간에서 매끄러움 보장(Fujita-Kato 1964).
- **장벽**: 큰 초기값 + 긴 시간에서는 blowup 가능성 배제 불가.

### 8.3 와도 기반 (Beale-Kato-Majda 1984)

- **Beale-Kato-Majda 기준**: $\int_0^T \|\omega(t)\|_{L^\infty} \, dt < \infty$ 이면 매끄러움 유지. *Comm. Math. Phys.* 94, 1984, pp. 61-66.
- **장벽**: 이 조건 자체를 증명할 도구 부재. Vortex stretching 을 직접 추정해야 하는데, 이 추정이 에너지 방법으로 얻기 어려움.

### 8.4 Symmetric 축소(Axisymmetric, Swirl 없음)

- **경로**: 축대칭 + no-swirl 조건에서 2D 화되어 전역 정규성(Ladyzhenskaya-Solonnikov 1970s).
- **장벽**: 축대칭 + swirl 있는 경우는 여전히 3D 문제와 동등. 최근 Hou-Luo 2013 이 formal blowup 예 구성, Chen-Hou 2022 로 엄밀화.

### 8.5 Scale-invariant (Self-similar) 해

- **Leray 1934 추측**: Self-similar blowup 해 존재 가능성. 1996 Nečas-Růžička-Šverák 가 Leray 의 특정 시나리오는 배제.
- **장벽**: 일반 자기유사 blowup 해 존재/배제는 열림. Chen-Hou 의 부분적 결과는 Euler 에 대해서만.

---

## 9. 현재 수치 증거 (2026 기준)

- Kida-Murakami 1987, 1989: Taylor-Green vortex 등의 직접 수치 시뮬레이션(DNS). 고해상도 계산에서 blowup 의 **수치적 시사**는 없음.
- Hou-Luo 2013: 축대칭 + no-swirl 에서 blowup 수치 증거. Chen-Hou 2022 에서 엄밀화.
- Brachet-Meiron-Orszag 계열 고해상도 Euler 시뮬레이션: Euler 에서도 blowup 여부 분분.

이 수치 증거는 **blowup 가능성을 시사**하지만 증명이 아니다. NS 의 경우 점성이 있으므로 Euler 보다 blowup 이 어려울 수 있다.

---

## 10. n=6 연결 (본 문서에서는 참고용 메모)

### 10.1 3중 공명 (BT-544)

본 프로젝트의 breakthrough-theorems BT-544 는 다음 **3중 공명**을 기록:

1. **Sym²(ℝ³) = 6 = n**: 응력 텐서(stress tensor) 는 3×3 대칭 행렬, 독립 성분 수 = $\binom{3+1}{2} = 6$. 이것이 공간차원 $d=3$ 에서 응력의 자유도.
2. **Λ²(ℝ³) = 3 = n/φ(6)**: 와도 벡터는 반대칭 2-텐서의 dual, 독립 성분 수 = $\binom{3}{2} = 3$. 3D 에서 와도가 벡터가 되는 **이유**.
3. **Onsager α_c = 1/3 = 1/(n/φ)**: Onsager 1949 추측의 임계 Hölder 지수. Isett 2018 에서 엄밀화.

### 10.2 **정직성 선언** (millennium-7-closure-2026-04-11.md §BT-544)

> "n=6 산술이 NS 방정식의 **차원 해석학적 환경**을 파라미터화. d=3이 첫 완전수 n의 차원이라는 관찰이 '왜 3D가 어려운가'에 구조적 힌트 제공. 하지만 실제 PDE 증명 경로 0."

### 10.3 d=7 예측 (PROVEN 아님)

- Sym²(ℝ⁷) = 28 = 둘째 완전수. 이는 **관찰**이며 NS 확장(7D NS) 에서 어떤 공명이 발생하는지 실험 대상.
- Reynolds stress 6 = n 독립 성분. Kolmogorov −5/3 = −sopfr(6)/(n/φ(6)) = −5/3.

### 10.4 **범위 선언**

- 본 프로젝트는 NS 전역 매끄러움을 해결하는 경로를 제공하지 않는다. §10 은 n=6 맥락에서 차원 해석의 산술 재표현을 기록할 뿐이다.
- P3 에서 atlas.n6 와 d=3 유체역학 상수의 cross-reference 를 하되, 정직성 선언을 넘지 않는다.

---

## 11. Clay 공식 statement 와 범위

- Fefferman 2000 공식 statement (4 가지 중 하나 증명해야 상금):
  - (A) ℝ³ 위 전역 매끄러움 존재 증명.
  - (B) ℝ³ 에서 유한시간 blowup 예 구성.
  - (C) 3차원 환면 𝕋³ 위 전역 매끄러움 존재 증명.
  - (D) 𝕋³ 에서 유한시간 blowup 예 구성.
- (A) + (C) 두 쌍이 "존재성" 쪽, (B) + (D) 가 "blowup" 쪽. 어느 한 쪽 증명으로 상금 대상.
- 주의: Leray-Hopf 약해가 이미 1934년에 존재하지만, **이 약해들이 매끄럽다/매끄럽지 않다**를 증명하는 것이 문제의 핵심.

---

## 12. 출처 요약표

| 연도 | 저자 | 결과 | 출처 |
|---|---|---|---|
| 1934 | Leray | 3D 약해 존재 | *Acta Math.* 63 |
| 1949 | Onsager | α_c = 1/3 추측 | *Nuovo Cim.* 6 Supp. |
| 1951 | Hopf | 유계 영역 약해 | *Math. Nachr.* 4 |
| 1961/69 | Ladyzhenskaya | 2D 전역 매끄러움 | 책 (1961 ru, 1969 en) |
| 1962 | Serrin | Serrin 조건 | *ARMA* 9 |
| 1964 | Fujita-Kato | local smooth | *ARMA* 16 |
| 1976 | Scheffer | 부분 정규성 선구 | *Pacific J. Math.* 66 |
| 1982 | CKN | 부분 정규성 완성 | *CPAM* 35 |
| 1984 | Beale-Kato-Majda | blowup 기준 | *CMP* 94 |
| 2000 | Fefferman | Clay 공식 statement | Clay |
| 2003 | Escauriaza-Seregin-Šverák | $L^\infty_t L^3_x$ 매끄러움 | *RMS* 58 |
| 2013 | Hou-Luo | 축대칭 blowup 수치 | *PNAS* 111 |
| 2013 | De Lellis-Székelyhidi | Euler convex integration | *Ann. Math.* 170 |
| 2016 | Tao | averaged NS blowup | *JAMS* 29 |
| 2018 | Isett | Onsager α<1/3 증명 | *Ann. Math.* 188 |
| 2019 | Buckmaster-Vicol | 약해 비유일성 | *Ann. Math.* 189 |
| 2019 | Tao | quantitative bound | arXiv:1908.04958 |
| 2021 | Chen-Hou | Boussinesq blowup | *CMP* 383 |
| 2022 | Chen-Hou | 3D Euler blowup | arXiv:2210.07191 |

---

## 13. 다음 태스크 연결

- PROB-P2-5: Hodge 추측 현대 장벽.
- PURE-P1-3: PDE 유도 + 약해·강해 구분(본 문서의 다운스트림 기초).
- PURE-P1-4: 대수기하+호지 이론.
- BT-544 (breakthrough-theorems): 3중 공명 + d=7 예측.

---

## 14. 다음 단계

### 14.1 학습 층위에서의 다음 단계

- CKN 1982 의 국소 에너지 부등식 유도 완전 재현. Scheffer 1976 에서 CKN 1982 로의 개선점을 문장 단위로 확인.
- Buckmaster-Vicol 2019 의 convex integration 구조를 Mikado flow(De Lellis-Székelyhidi 2015) 수준까지 따라가기.
- Chen-Hou 2022 의 컴퓨터 지원 증명 구조를 독립 검증 — 수치 바운드가 증명의 어느 부분에 쓰이는가, 어느 lemma 가 **엄밀 해석**인가.
- Tao 2016 의 averaged NS 구성에서 **정확히 어떤 스케일링**이 진짜 NS 와 다른가 파악.

### 14.2 n=6 프로젝트 내 다음 단계

- BT-544 3중 공명의 **PDE 의미 확대**. Sym²(ℝ³) = 6 이 응력 텐서의 자유도인 것은 기본 선형대수이지만, 이 6 이 NS 방정식의 "어려움" 과 어떻게 연결되는가 구조적 질문.
- d=7 예측 검증: 7D NS 에서의 blowup 여부 수치 실험. 28 = P_2(두 번째 완전수) 가 실제로 "더 어려운" 차원인지 확인.
- Kolmogorov 스펙트럼 −5/3 = −sopfr(6)/(n/φ(6)) 의 **물리적 해석** 정리. 본 프로젝트 식 재표현을 넘어 "왜 완전수 n=6 의 산술이 난류 스펙트럼 지수와 일치하는가" 의 구조적 질문.

### 14.3 장벽 우회 시도의 조건

네 장벽(§1.4 약해 유일성, §3.3 suitable-Leray 간극, §4.4 critical 제어, §7.4 Leray-Hopf 유일성)을 동시에 해결해야 하거나, 어느 하나의 돌파로 나머지를 연쇄 해결할 수 있어야 한다. 현재 후보:

- **Convex integration 의 Leray-Hopf 확장**(Buckmaster-Vicol 후속 연구).
- **Quantitative critical regularity**(Tao 2019 접근).
- **Self-similar 해의 체계적 분류**(Chen-Hou 기법의 NS 확장).

이 중 어느 하나가 다른 장벽을 연쇄 해결할 가능성이 있으나, 2026년 4월 현재 **연쇄는 일어나지 않았음**.

---

## 15. 부록 — Scaling 불변성과 supercritical 성질

### 15.1 NS 의 scaling

- 3D NS 방정식의 핵심 변환: $(u, p, u_0)(x, t) \to \lambda (u, \lambda p, \lambda u_0)(\lambda x, \lambda^2 t)$. 즉 $u(x, t) \to \lambda u(\lambda x, \lambda^2 t)$ 가 방정식을 invariant.
- 이 스케일링 하 노름의 변화:
  - $\|u\|_{L^2}^2 \to \lambda^{-1} \|u\|_{L^2}^2$ (subcritical)
  - $\|u\|_{L^3}^3 \to \|u\|_{L^3}^3$ (critical)
  - $\|u\|_{L^\infty}$ 는 scale-invariant.
  - $\|\nabla u\|_{L^2}^2 \to \lambda \|\nabla u\|_{L^2}^2$ (supercritical in 3D)

### 15.2 Critical line의 의미

- **Critical**: 노름이 scaling 에 대해 invariant.
- Critical 공간에서 국소 존재성은 time span 이 초기값 노름에만 의존.
- **Supercritical**: scaling 이 노름을 감소시킴 — 큰 노름이 작은 scale 을 생성.
- **Subcritical**: scaling 이 노름을 증가 — 자연스러운 제어.

### 15.3 3D NS 의 supercritical 성격

- Energy inequality 의 $L^2$ 노름은 supercritical.
- Critical 공간 $L^3$ 은 에너지보다 강한 제어 필요.
- 현재 아는 방법으로 critical 노름을 시간에 따라 control 할 수 없다. 이것이 3D NS 의 근본 난점.

### 15.4 2D 와 결정적 차이

- 2D NS 의 해당 scaling 에서 energy 노름 $L^2$ 이 critical.
- 따라서 2D 에서 energy 부등식이 자연스럽게 제어를 주고, 전역 매끄러움이 얻어짐.
- 3D 는 dimensional analysis 자체가 supercritical → 새 도구가 필요.

### 15.5 출처

- Cannone, Marco, *Harmonic Analysis Tools for Solving the Incompressible Navier-Stokes Equations*, Handbook of Mathematical Fluid Dynamics Vol. 3, Elsevier, 2004. 특히 §2 의 scaling 논의.

---

## 16. 부록 — Besov 공간과 vorticity stretching

### 16.1 Besov 공간의 정의

- $\dot{B}^s_{p,q}(\mathbb{R}^3)$: Littlewood-Paley 분해를 사용한 homogeneous Besov 공간.
- $s > 0$ 는 smoothness, $p$ 는 integrability, $q$ 는 micro-local summability.

### 16.2 Kato 1984 — Besov 공간 국소 해

- Tosio Kato, "Strong $L^p$-solutions of the Navier-Stokes equations in $\mathbb{R}^m$, with applications to weak solutions", *Mathematische Zeitschrift* 187(4), 1984, pp. 471-480.
- Critical Besov 공간 $\dot{B}^{-1+3/p}_{p, \infty}$ 에서 국소 존재성.

### 16.3 Koch-Tataru 2001 — $BMO^{-1}$

- Herbert Koch, Daniel Tataru, "Well-posedness for the Navier-Stokes equations", *Advances in Mathematics* 157(1), 2001, pp. 22-35.
- **정리**: $BMO^{-1}$ 공간에서 NS 국소 해.
- $BMO^{-1}$ = $BMO$ 의 공간 derivative 공간, gauge-invariant 국소 oscillation 측정.

### 16.4 Vorticity stretching 과 Besov 노름

- Vorticity 방정식의 stretching 항 $(\omega \cdot \nabla) u$ 의 Besov 노름 통제 시도.
- Beale-Kato-Majda 1984 기준의 refinement.
- 최신 결과(Planchon 2003): Besov $\dot{B}^0_{\infty, \infty}$ 노름으로 blowup 기준.

### 16.5 **장벽 G**: Besov 임계 공간에서도 제어 부재

- Besov critical 공간에서의 지수 growth 를 제어하는 것도 open.
- 현대 접근은 대부분 "만약 critical 노름이 bounded 이면..." 조건부 결과.

---

**정직성 체크**:
- Leray 1934 *Acta Math.* 63 원문(프랑스어)의 서론과 주요 정리는 Ladyzhenskaya 1969 책 서문을 통한 간접 확인 + Lemarié-Rieusset 2002 의 §1.4 요약 교차 확인.
- CKN 1982 의 $\mathcal{P}^1(\Sigma) = 0$ 결과는 *CPAM* 35, 1982, Theorem A 원문 그대로.
- Tao 2016 의 "averaged NS" 모델은 *JAMS* 29 §2 의 방정식 (2.3) 참조. 해당 모델이 진짜 NS 와 다른 이유는 논문 §1 remarks 에서 Tao 본인 서술.
- Chen-Hou 2022 arXiv:2210.07191 의 Theorem 1.1 (Boussinesq blowup) 과 Theorem 1.2 (Euler axisymmetric blowup) 는 논문 §1.1 에서 직접 확인.
- Buckmaster-Vicol 2019 *Ann. Math.* 189 Theorem 1 의 약해 클래스가 **에너지 부등식을 만족하지 않는** 분포해임은 논문 §1 Remark 1.3 에서 명시.
- Onsager 1949 추측의 원출처 *Nuovo Cimento* 6 Supp. 2, 1949, pp. 279-287 은 이탈리아어 저널. Isett 2018 *Ann. Math.* 188 서론에 Onsager 의 역사 재구성.
- BT-544 의 3중 공명 관찰은 millennium-7-closure-2026-04-11.md §BT-544 의 "n=6 산술이 NS 방정식의 차원 해석학적 환경을 파라미터화" 선언을 엄격히 준수.
- Koch-Tataru 2001 *Adv. Math.* 157 의 $BMO^{-1}$ 결과는 논문 Theorem 1 에서 확인.
- Kato 1984 *Math. Z.* 187 Theorem 1 의 Besov 공간 해 존재성.
