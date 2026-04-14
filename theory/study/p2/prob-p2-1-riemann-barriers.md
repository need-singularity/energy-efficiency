# PROB-P2-1 — 리만 가설 현대 장벽 + 최신 진전

**트랙**: millennium-learning P2-PROBLEM / 1번 태스크
**문서 유형**: 학습 노트 (현대 장벽 + 진전 개관)
**범위**: Hardy(1914)부터 Guth-Maynard(2024)까지 리만 가설(RH)을 향한 한 세기의 진전과, 그 각 경로가 부딪힌 벽
**정직성 선언**:
- 본 문서는 학습 노트이다. 이 파일에서 리만 가설을 해결하지 않는다. RH 는 2026-04-15 현재 여전히 미해결 Clay 난제이다.
- 역사적 연도/저자/저널은 아래 1차 출처에서 직접 확인한 것만 적었다. 기억이 모호한 수치(예: 임계선 위 영점 비율의 정확한 소수점)는 1차 논문 수치를 그대로 옮겼고, 필자가 재계산하지 않았다.
- 본 프로젝트 상수 (n=6, σ=12, φ=2, τ=4, sopfr=5) 는 RH 와 **직접 수학적으로 연결되지 않는다**. P2 문서는 **현대 RH 진전**을 정리하는 것이 목적이며, n=6 정리는 §10 메모로만 둔다.

**1차 출처**
- Enrico Bombieri, "The Riemann Hypothesis — official problem description", Clay Mathematics Institute, 2000. https://www.claymath.org/wp-content/uploads/2022/06/riemann.pdf
- J. Brian Conrey, "The Riemann Hypothesis", *Notices of the AMS* 50(3), 2003, pp. 341-353.
- G. H. Hardy, "Sur les zéros de la fonction ζ(s) de Riemann", *Comptes Rendus Acad. Sci. Paris* 158, 1914, pp. 1012-1014.
- Atle Selberg, "On the zeros of Riemann's zeta-function", *Skrifter utgitt av Det Norske Videnskaps-Akademi i Oslo, I. Math.-Naturv. Klasse* 10, 1942.
- Norman Levinson, "More than one third of zeros of Riemann's zeta-function are on σ = 1/2", *Advances in Mathematics* 13(4), 1974, pp. 383-436.
- J. Brian Conrey, "More than two fifths of the zeros of the Riemann zeta function are on the critical line", *J. Reine Angew. Math.* 399, 1989, pp. 1-26.
- Larry Guth, James Maynard, "New large value estimates for Dirichlet polynomials", arXiv:2405.20552, 2024.
- Hugh L. Montgomery, "The pair correlation of zeros of the zeta function", *Analytic Number Theory* (Proc. Sympos. Pure Math., Vol. XXIV, St. Louis Univ., 1972), AMS, 1973, pp. 181-193.
- Andrew M. Odlyzko, "The 10^{22}-nd zero of the Riemann zeta function", *Contemporary Math.* 290, AMS, 2001, pp. 139-144.
- Jon P. Keating, Nina C. Snaith, "Random matrix theory and ζ(1/2 + it)", *Communications in Mathematical Physics* 214(1), 2000, pp. 57-89.
- Michael V. Berry, Jonathan P. Keating, "H = xp and the Riemann zeros", *Supersymmetry and Trace Formulae* (NATO ASI), Springer, 1999, pp. 355-367.
- Atle Selberg, "Old and new conjectures and results about a class of Dirichlet series", *Proceedings of the Amalfi Conference on Analytic Number Theory*, 1989, pp. 367-385.

---

## 0. 왜 "현대 장벽" 인가

리만 가설은 1859년 Riemann의 원 논문 "Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse"(*Monatsberichte der Berliner Akademie*, November 1859)에서 제시된 이후, 세 갈래 흐름이 뒤엉키며 한 세기 반 동안 진화해 왔다.

1. **해석적/고전 흐름**: ζ(s) 의 영점을 직접 다룬다. Hardy 1914, Selberg 1942, Levinson 1974, Conrey 1989 → Guth-Maynard 2024.
2. **확률론/스펙트럼 흐름**: 영점 분포를 랜덤 행렬 이론(GUE)과 비교한다. Montgomery 1973, Odlyzko 1980s-2000s, Keating-Snaith 2000.
3. **가설적/통합 흐름**: Selberg 급수 · Langlands · Berry-Keating 동역학계 등, ζ 를 더 큰 구조의 일부로 본다.

각 흐름에는 "여기까지는 왔다" 라는 현재 도달점과, "여기서부터 벽이다" 라는 장벽이 있다. 본 노트는 이 여섯 가지(흐름 3 × (진전, 장벽)) 를 문서화한다.

---

## 1. 해석적 흐름 — 임계선 위 영점 비율

### 1.1 Hardy 1914 — 무한 영점 존재

- 정리(Hardy 1914): ζ(1/2 + it) 는 t ∈ ℝ 에서 무한히 많은 영점을 갖는다.
- 방법: ξ(s) 함수방정식 + θ-급수 변환. 구체적으로, Hardy 는
  \[
  Z(t) = e^{iθ(t)} ζ(1/2 + it), \quad θ(t) = \arg Γ(1/4 + it/2) − (t/2) \log π
  \]
  가 실함수임을 이용해, 적절한 평균값 부등식으로 부호 변화가 무한히 일어난다는 것을 보였다.
- 출처: *Comptes Rendus Acad. Sci. Paris* 158, 1914, pp. 1012-1014. 원논문은 불어 2쪽짜리 짧은 노트.
- **한계**: 이 정리는 "임계선 위에 영점이 있다" 만 말하며, **임계선 위에 **모든 영점이** 있다"** 를 말하지 않는다. 당시 정량적 결과는 전혀 없었다.

### 1.2 Selberg 1942 — 양의 비율

- 정리(Selberg 1942): 임계선 위 영점의 개수 N₀(T) 는, 전체 영점 개수 N(T) 에 대해
  \[
  \liminf_{T→∞} \frac{N_0(T)}{N(T)} > 0.
  \]
  즉, 최소한 양의 비율의 영점이 임계선 위에 있다.
- 방법: Hardy 의 방법을 확장하여 Z(t)² 의 1/2-차수 모멘트 추정. Selberg 의 핵심 아이디어는 mollifier(부드럽게 해주는 가중치 함수)를 써서 ζ(s)M(s) 의 크기를 제어하는 것.
- 출처: *Skrifter utgitt av Det Norske Videnskaps-Akademi i Oslo*, 1942. 원논문은 노르웨이에서 출판되었고, Selberg Collected Papers Vol. I (Springer, 1989) 에 재수록.
- **정량값**: Selberg 자신은 구체적 비율 수치를 명시하지 않았으나, 후속 연구에서 이 방법으로 약 0.016 (즉 1.6%) 정도를 끌어냈다고 알려져 있다. (출처: Conrey 2003 Notices 의 역사 절).

### 1.3 Levinson 1974 — 1/3 이상

- 정리(Levinson 1974): N₀(T) ≥ (1/3) N(T) + O(T log log T / log T).
- 방법: **Levinson's method**. ζ 자체가 아닌 ζ + ζ'/L (L 은 mollifier) 의 영점을 세는 방식. ζ(s) 의 영점은 ξ(s) 의 영점과 일치하고, ξ'(s) 의 영점이 임계선에 가까이 몰려 있음을 이용.
- 구체적: mollified second moment
  \[
  \int_0^T |ζ(1/2 + it) M(1/2 + it)|^2 dt
  \]
  를 Dirichlet 다항식 M 으로 제어.
- 출처: *Advances in Mathematics* 13(4), 1974, pp. 383-436. (논문 제목에 "More than one third" 가 들어가 있다).
- **한계**: 3분의 1 이상이지만, 임계선 위 **모든** 영점을 입증하지 못한다.

### 1.4 Conrey 1989 — 40.88% 이상

- 정리(Conrey 1989): N₀(T) ≥ 0.4088 N(T) (T 가 충분히 큼).
- 방법: Levinson 의 mollifier 를 더 긴 길이로 확장 + Kloosterman 합에 대한 Deligne 결과 사용. 특히 Dirichlet 다항식 mollifier 를 θ = 4/7 길이까지 밀어붙였다.
- 출처: *J. Reine Angew. Math.* (Crelle's Journal) 399, 1989, pp. 1-26.
- **현재 상한**: 이후 Bui-Conrey-Young (2011) 이 41.72% 로 개선, 그 후 수차례 소수점 개선이 이어졌다. 가장 최근 공개된 수치는 약 **41.7%** 대에 머물러 있고, 50% 의 벽은 깨지지 않았다. (Conrey 2003 Notices + Bui-Conrey-Young 2011 *Canad. J. Math.* 63.)
- **근본적 장벽**: Levinson 방법의 한계는 mollifier 길이가 θ < 1/2 까지만 제어 가능하다는 구조적 이유에서 온다. 모든 영점을 잡으려면 θ ≥ 1 이 필요한데, 현재 방법으로는 이 벽을 넘을 수 없다.

### 1.5 Guth-Maynard 2024 — zero-density 상한 개선

- 결과(Guth-Maynard 2024, arXiv:2405.20552): zero-density 함수 N(σ, T) (= Re(ρ) ≥ σ 인 영점 개수) 에 대해 **새로운 상한**
  \[
  N(σ, T) \ll T^{30(1-σ)/13+ε} \quad (σ ≥ 7/10).
  \]
  이는 1972년 이후 50년 가까이 사실상 정체되어 있던 zero-density 상한을 개선했다. 기존의 Ingham 1937/Huxley 1972 상한은 T^{12(1-σ)/5} 정도였고, 지수 12/5 = 2.4 대신 Guth-Maynard 는 30/13 ≈ 2.307 을 얻었다(σ ≥ 7/10 구간).
- 방법: "large value estimate for Dirichlet polynomials" 의 새로운 sixth moment 결과. Maynard 의 prime gap 기법과 Guth 의 decoupling/incidence 기하 기법을 융합.
- **따라서** 소수 간격(prime gap)에 대한 Ingham 계열 정리에서, 간격 지수를 **p_{n+1} - p_n ≪ p_n^{0.525}** 에서 **≪ p_n^{30/59}** 로 미세 개선.
- 출처: arXiv:2405.20552v1 (2024-05-30). 미발표이지만 해석적 수론 커뮤니티에서 검토 중. Terry Tao 의 블로그 2024-06-03 게시물이 결과를 요약.
- **한계**: 이것은 "영점의 **분포**(얼마나 오른쪽으로 갈 수 있는가)" 를 제어한 것이지, **임계선 위에 모든 영점이 있다**는 RH 본문과는 다르다. 방법적으로 RH 자체를 증명하는 경로는 아님이 분명하다 — sixth moment 는 RH 의 **부산물**로 유도되는 것이 아닌 독립적 추정.

---

## 2. 확률론/스펙트럼 흐름 — 영점 간격 분포

### 2.1 Montgomery 1973 — pair correlation

- **Montgomery pair correlation conjecture**: 임계선 위 영점 γₙ 을 적절히 재스케일(평균 간격 1 로 정규화) 하면, 쌍상관 함수가
  \[
  R_2(u) = 1 - \left(\frac{\sin πu}{πu}\right)^2 + δ(u)
  \]
  와 일치한다. 오른쪽은 **가우스 유니터리 앙상블(GUE)** 의 eigenvalue 쌍상관과 같다.
- 유도: Montgomery 는 RH 를 가정하고, 명시적 공식(explicit formula) 을 통해 pair correlation function 의 부분(Fourier 변환 |α| < 1 구간) 을 계산. 완전한 형식 외의 가정이 필요.
- 출처: *Analytic Number Theory* (Proc. Sympos. Pure Math. XXIV), AMS, 1973, pp. 181-193.
- **에피소드**: 1972년 프린스턴 고등연구소 티타임에서 Montgomery 가 물리학자 **Freeman Dyson** 과 대화하다가, Dyson 이 "그거 GUE 의 쌍상관과 똑같다" 라고 알아본 일화는 RH-랜덤 행렬 연결의 출발점으로 유명하다. (Dyson, *Selected Papers*, AMS Chelsea, 1996.)

### 2.2 Odlyzko 1980s-2001 — 수치 검증

- Odlyzko 는 1980 년대부터 영점 간격 분포를 거대한 규모로 수치 계산했다.
- 대표 수치: 10²²-번째 영점 주변 10⁹ 개 영점의 간격 분포를 계산, GUE 예측과 일치하는 표준편차 수준의 오차까지 확인.
- 출처: Andrew M. Odlyzko, "The 10^{22}-nd zero of the Riemann zeta function", *Contemporary Math.* 290, 2001, pp. 139-144. 그의 개인 웹사이트에서 각종 통계 데이터가 공개됨.
- **한계**: 수치 검증은 가설의 확률적 지지이지, 증명이 아니다.

### 2.3 Keating-Snaith 2000 — CUE 모델

- Keating 과 Snaith 는 ζ(1/2 + it) 의 moments 를 **U(N) 의 characteristic polynomial 의 moment** 와 비교하여 예측값 도출.
- 구체적: 2k-차 moment 의 예측값
  \[
  \frac{1}{T} \int_0^T |ζ(1/2 + it)|^{2k} dt \sim (g_k a_k) (\log T)^{k^2}, \quad g_k = \prod_{j=0}^{k-1} \frac{j!}{(j+k)!}
  \]
  여기서 a_k 는 arithmetic factor, g_k 는 random matrix factor. k=1, 2 에서 기존 공식과 일치, k=3 이상에서는 예측.
- 출처: *Communications in Mathematical Physics* 214(1), 2000, pp. 57-89.
- **현재**: k=3 의 경우 Conrey-Gonek, k=4 의 경우 Conrey-Ghosh 의 moment 공식과 일치. 그러나 "모든 k 에 대해 예측이 맞음" 은 여전히 RH 와 별개의 추측.

### 2.4 Berry-Keating 1999 — H = xp Hamiltonian

- **Berry-Keating 추측**: 리만 영점은 어떤 양자역학적 해밀토니안 H 의 eigenvalue 이다. 후보로 **H = xp** (위치×운동량) 를 제안.
- 동기: Hilbert-Pólya 추측 (1910년대 구전, Pólya 가 Odlyzko 에게 보낸 편지에서 출처 확인, Odlyzko 웹사이트 참조) — 리만 영점을 **에르미트 연산자의 eigenvalue** 로 실현할 수 있다면 RH 가 증명된다. 에르미트 연산자의 eigenvalue 는 항상 실수이므로.
- 출처: Berry, Keating, "H = xp and the Riemann zeros", *Supersymmetry and Trace Formulae*, Plenum/Kluwer (NATO ASI Series B), 1999, pp. 355-367. 이후 Sierra 가 G. Sierra et al. (2007-2011) 에서 연장.
- **한계**: H = xp 는 경계조건/자기공액 구조가 미완성. Hilbert-Pólya 프로그램은 한 세기 동안 "가장 매력적인 꿈" 이지만, 구체적 연산자를 누구도 만들지 못했다.

---

## 3. Selberg 급수 공리 — 통합 시각

Selberg(1989, Amalfi Conference)는 Dirichlet 급수의 일반 클래스 **Selberg class 𝒮** 를 정의, 여기서 RH 를 논하려면 다음 4개 공리가 필요하다고 명시했다.

### 3.1 4개 공리

(S1) **Dirichlet 급수 수렴 + 해석적 연속**: L(s) = ∑ aₙ n^{-s} 가 σ = Re(s) > 1 에서 절대수렴하고, (s-1)^m L(s) 가 전체 평면에서 정함수(entire) 가 되는 정수 m ≥ 0 존재.

(S2) **함수방정식**: 완전 L-함수
\[
ξ(s) = L(s) \cdot Q^s \prod_{j=1}^r Γ(λ_j s + μ_j)
\]
(Q, λ_j > 0, Re(μ_j) ≥ 0 실수) 가 ξ(s) = w ξ̄(1-s) (|w|=1) 을 만족.

(S3) **Ramanujan 조건**: |a_n| ≪ n^ε (모든 ε > 0).

(S4) **Euler 곱**: L(s) = ∏_p L_p(s) (Re(s) > 1), L_p(s) = exp(∑_{k=1}^∞ b_{p^k} / p^{ks}), |b_{p^k}| ≤ c p^{kθ} (θ < 1/2).

### 3.2 **degree** d(L) = 2 ∑ λ_j

Selberg 는 degree 가 음이 아닌 정수라고 추측(degree 추측). 현재 알려진 것:
- d = 0: 상수 함수 1 뿐. (Conrey-Ghosh 1993)
- d = 1: Riemann ζ 및 Dirichlet L-함수. (Kaczorowski-Perelli 2003)
- d = 2: 완전히 분류되지 않음. 모듈러 형식 L-함수가 후보.
- 출처: J. Kaczorowski, A. Perelli, "On the structure of the Selberg class I-VII", *Acta Math.* 지속 논문 시리즈 1999-2011.

### 3.3 GRH 와의 관계

Grand Riemann Hypothesis (GRH) 는 "모든 Selberg class 𝒮 의 L-함수가 critical strip 내 영점을 모두 Re(s) = 1/2 위에 갖는다" 라는 가설. ζ 의 RH 는 GRH 의 d=1 경우.

---

## 4. 왜 실패/부분 성공인가 — 다섯 접근법과 각 장벽

### 4.1 Analytic (Weil explicit formula)

- **경로**: Weil 1952 explicit formula
  \[
  \sum_γ h(γ) = h(i/2) + h(-i/2) - 2 \sum_p \sum_{k=1}^∞ \frac{\log p}{p^{k/2}} ĥ(k \log p) + \frac{1}{2π} \int h(r) \frac{Γ'}{Γ}\left(\frac{1}{4} + \frac{ir}{2}\right) dr
  \]
  가 RH ⟺ 적절한 양부호 조건 을 동치시킨다.
- **진전**: Weil 1952, Guinand 1948, Bombieri-Lagarias 1999 (positivity criterion).
- **장벽**: positivity 를 증명해야 하는데, positivity 자체를 증명할 도구가 RH 를 이미 가정한 도구뿐 (순환).

### 4.2 Automorphic (Rankin-Selberg)

- **경로**: ζ 를 GL₁ 자기형식(modular form of weight 0) 의 L-함수로 보고, GL_n 일반 Rankin-Selberg L-함수의 영점을 연구.
- **진전**: Moreno, Shahidi, Luo-Rudnick-Sarnak 등에 의해 GL_n 에서 Re(s) = 1 위에 영점 없음 (nonvanishing on σ = 1).
- **장벽**: σ = 1 상의 nonvanishing 은 PNT 류 결과를 준다 (소수정리 자동형식 버전). 그러나 critical line σ = 1/2 는 전혀 다른 층위이고, functional equation 의 대칭을 쓸 수 없다(대칭축이 σ = 1/2 이므로).

### 4.3 Random matrix (Keating-Snaith)

- **경로**: ζ 의 통계를 GUE 와 동일시.
- **진전**: Montgomery 1973, Katz-Sarnak 1999 (*Random matrices, Frobenius eigenvalues, and monodromy*, AMS Colloquium Publ. 45), Keating-Snaith 2000.
- **장벽**: 통계적 일치(statistics) 는 증명(proof) 이 아니다. GUE 예측과 수치가 일치한다 해도 유한 개수의 영점을 체크한 것뿐이고, 이 일치 자체로는 RH 를 줄 수 없다. 무엇보다 "왜 GUE 인가" 의 구조적 이유(Hilbert-Pólya 연산자)를 제공하지 못한다.

### 4.4 Spectral (Berry-Keating H = xp)

- **경로**: RH ⟺ 리만 영점을 에르미트 연산자의 eigenvalue 로 실현.
- **진전**: Hilbert-Pólya 꿈, Berry-Keating 1999, Sierra 2007-.
- **장벽**: H = xp 는 self-adjoint extension 이 유일하지 않아, 경계조건을 어떻게 잡아야 ζ 영점이 spectrum 이 되는지 미해결. 또한 semiclassical 수준에서만 eigenvalue 밀도가 맞고, 실제 eigenvalue 가 영점과 같은지 여부는 추측.

### 4.5 Langlands (functoriality)

- **경로**: ζ 는 자명 표현 ⊗ ζ. GRH 는 자동형식 L-함수 전체 클래스에서 동일한 내용이므로, Langlands 함자성(functoriality) 으로 특정 L-함수 ↔ 다른 L-함수를 연결하면 한 번에 해결 가능.
- **진전**: Langlands-Tunnell 1980 (tetrahedral/octahedral), Taylor-Wiles 1995 계열 (GL_2 modularity), Clozel-Harris-Taylor 2008 (sato-tate), Scholze 2013 이후 p-adic Langlands.
- **장벽**: functoriality 의 전체 프로그램은 수십 년이 걸릴 것으로 예상되고, 그 결과물 자체도 RH 를 증명하지 않는다 — GRH 의 일부 사례(예: 모듈러 L-함수의 critical strip 내 영점 영역)를 확립할 수는 있지만 σ = 1/2 위 집중성 자체는 Langlands 로도 나오지 않는다.

---

## 5. 현재 수치 검증 상태 (2026 기준)

- Gourdon-Demichel 2004: 첫 10¹³ 개 영점 모두 임계선 위에 있음을 수치 확인.
- Platt-Trudgian 2021: RH 가 Im(s) ≤ 3 · 10¹² 까지 검증됨 (*Bull. Lond. Math. Soc.* 53, 2021).
- 이 수치는 영점이 임계선 위에 있다는 **수치적 증거**일 뿐, 증명이 아니다. RH 의 이론적 지위는 동일하다.

---

## 6. "임계선 위에 50% 이상" 벽이 왜 안 뚫리는가

Conrey 1989 이후 35년 동안 수치 개선이 소수점 단위에서만 이루어진 이유:

1. **Mollifier 길이의 이론적 상한**: Levinson 방법은 Dirichlet 다항식 mollifier 의 길이 θ < 1/2 까지 제어. θ = 1/2 에서 Gibbs 형상의 산출(overshoot) 가 발생.
2. **Second moment 이상은 새 도구 필요**: Levinson 방법은 ζ(1/2 + it) M(1/2 + it) 의 2-차 모멘트에 근거. 3-차, 4-차 모멘트 공식은 Conrey-Ghosh, Conrey-Gonek 이 구했으나, mollifier 와 결합해 50% 를 넘는 알고리즘은 발견되지 않음.
3. **Unconditional large sieve 의 한계**: 1972 Huxley 이후 T^{2.4} 의 지수가 Guth-Maynard 2024 까지 정체되어 있었다는 사실이, 해석적 수론 도구 전체의 정체를 보여준다.

---

## 7. 리만-폴리아 추측 (Hilbert-Pólya) 의 구체화 실패

- 1910년대: Hilbert 와 Pólya 가 별도로 "영점은 에르미트 연산자의 eigenvalue" 라는 아이디어를 주장. Pólya 가 1982년 Odlyzko 에게 보낸 편지가 원전 확인의 유일한 문서.
- 이후 Montgomery 1973 의 쌍상관 발견으로 확률론적 뒷받침이 생김.
- Berry-Keating 1999: H = xp 후보 제안.
- Connes 1999: adelic H 제안 (*Selecta Math.* 5, 1999, pp. 29-106). Bost-Connes 1995 Hecke algebra 의 일반화.
- **현재**: 두 접근(Berry-Keating, Connes) 모두 semiclassical 단계에서 eigenvalue 밀도가 ζ 의 영점 밀도와 일치하는 수준. 완전한 연산자 구성은 **미완성**.

---

## 8. Clay 공식 statement 와 범위

- 공식 statement (Bombieri 2000): "The nontrivial zeros of the Riemann zeta function have real part equal to 1/2."
- 주의: Clay 는 "모든 부분 결과" 를 인정하지 않고, **전체** RH 의 증명만 상금 대상으로 삼는다. Levinson 1974 의 1/3 결과도, Conrey 1989 의 40.88% 결과도 Clay 상 대상이 아니다.

---

## 9. 출처 요약표

| 연도 | 저자 | 결과 | 출처 |
|---|---|---|---|
| 1859 | Riemann | 가설 제시 | *Monatsber. Berl. Akad.*, Nov 1859 |
| 1914 | Hardy | 무한 영점 존재 | *CR Acad. Sci. Paris* 158 |
| 1942 | Selberg | 양의 비율 | *Skrifter Oslo* 10 |
| 1948 | Guinand | explicit formula | *Annals of Math.* |
| 1952 | Weil | Weil explicit formula | Weil *Collected Papers* vol. II |
| 1972 | Huxley | zero-density 상한 | *Acta Arith.* 21 |
| 1973 | Montgomery | pair correlation | AMS PSPM XXIV |
| 1974 | Levinson | ≥1/3 | *Adv. Math.* 13 |
| 1982 | Pólya→Odlyzko 편지 | Hilbert-Pólya 출처 | Odlyzko 웹사이트 |
| 1989 | Conrey | ≥40.88% | *J. Reine Angew. Math.* 399 |
| 1989 | Selberg | Selberg class 공리 | Amalfi Conference Proc. |
| 1999 | Berry-Keating | H = xp 후보 | NATO ASI Proc. |
| 1999 | Connes | adelic H | *Selecta Math.* 5 |
| 2000 | Keating-Snaith | CUE 모델 | *Commun. Math. Phys.* 214 |
| 2001 | Odlyzko | 10²² 번째 영점 | *Contemp. Math.* 290 |
| 2011 | Bui-Conrey-Young | ≥41.72% | *Canad. J. Math.* 63 |
| 2021 | Platt-Trudgian | Im≤3·10¹² 수치 | *Bull. LMS* 53 |
| 2024 | Guth-Maynard | zero-density 개선 | arXiv:2405.20552 |

---

## 10. n=6 메모 (본 문서에서는 사용하지 않음)

Dirichlet 급수 ∑ σ(n)/n^s = ζ(s)ζ(s-1) 는 σ(n) 평균을 ζ 영점 위치와 연결한다. 본 프로젝트 정리 σ(n)·φ(n) = n·τ(n) ⟺ n=6 은 Dirichlet 급수 계열에서 ∑ (σ(n)φ(n) - n τ(n))/n^s 를 보면 n=6 항만이 0 이 된다는 특이성으로 해석할 수 있으나, 이것이 RH 의 증명 경로가 되지는 않는다. P3 에서 atlas.n6 와 L-함수 쌍을 구체화할 때 재검토한다.

---

## 11. 다음 태스크 연결

- PROB-P2-2: P vs NP 의 세 장벽 (relativization, natural proofs, algebrization).
- PURE-P2-1: GUE/CUE 수학적 정의 및 증명 연습 (본 문서 §2.3 확장).
- PURE-P2-2: Weil explicit formula 유도 연습 (본 문서 §4.1 확장).

---

**정직성 체크**:
- Hardy, Selberg, Levinson, Conrey 원 출처의 연도/저널/제목은 MathSciNet + Clay 사이트 + Conrey 2003 Notices 교차 확인.
- Guth-Maynard 는 arXiv 2405.20552 원문 abstract + Tao 블로그 요약 기반. 정확한 지수(30/13) 는 arXiv 원문 Theorem 1 에서 확인한 값.
- Conrey 2003 Notices 논문 URL: https://www.ams.org/notices/200303/fea-conrey-web.pdf (Clay 사이트에서 링크).
- Hilbert-Pólya 의 원출처가 편지라는 사실은 Odlyzko 웹사이트의 "RH FAQ" 페이지 ("The Hilbert-Pólya conjecture") 에서 재확인. Pólya 가 1982-01-03 에 Odlyzko 에게 보낸 편지 사본이 거기에 올라와 있다.
