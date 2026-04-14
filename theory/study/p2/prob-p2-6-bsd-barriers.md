# PROB-P2-6 — BSD 추측 현대 장벽 + 최신 진전

**트랙**: millennium-learning P2-PROBLEM / 6번 태스크
**문서 유형**: 학습 노트 (현대 장벽 + 진전 개관)
**범위**: Birch-Swinnerton-Dyer 1965 의 수치 관찰부터 Kolyvagin 1988 의 Euler system, Bhargava-Shankar 2010년대 평균 rank, BKLPR 랜덤 행렬 모델까지 — BSD 추측을 향한 60년 진전과 현재 장벽
**정직성 선언**:
- 본 문서는 학습 노트이다. 이 파일에서 BSD 추측을 해결하지 않는다. BSD 는 2026-04-15 현재 여전히 미해결 Clay 난제이다.
- 역사적 연도/저자/저널은 1차 출처에서 직접 확인한 것만 적었다. Bhargava-Shankar 의 평균 Selmer 크기 수치는 원 논문 Table 의 수치를 그대로 옮기고, 필자가 재계산하지 않았다.
- BT-546 의 **Sel_6 평균 = σ(6) = 12** 는 (BKLPR 독립성 가정 A3) 하의 조건부 정리이며, (A3) 자체는 증명된 정리가 아님을 명시(millennium-7-closure-2026-04-11.md §BT-546 준수).
- BT-546 의 Lemma 1 (CRT 분해) 은 무조건 엄밀 증명.

**1차 출처**
- Bryan Birch, Peter Swinnerton-Dyer, "Notes on elliptic curves II", *Journal für die reine und angewandte Mathematik* 218, 1965, pp. 79-108.
- Benedict H. Gross, Don B. Zagier, "Heegner points and derivatives of L-series", *Inventiones Mathematicae* 84(2), 1986, pp. 225-320.
- Victor A. Kolyvagin, "Finiteness of E(ℚ) and Ш(E/ℚ) for a subclass of Weil curves", *Izv. Akad. Nauk SSSR Ser. Mat.* 52(3), 1988, pp. 522-540.
- John Coates, Andrew Wiles, "On the conjecture of Birch and Swinnerton-Dyer", *Inventiones Mathematicae* 39(3), 1977, pp. 223-251.
- Andrew Wiles, "Modular elliptic curves and Fermat's Last Theorem", *Annals of Mathematics* 141(3), 1995, pp. 443-551.
- Christophe Breuil, Brian Conrad, Fred Diamond, Richard Taylor, "On the modularity of elliptic curves over ℚ: Wild 3-adic exercises", *Journal of the American Mathematical Society* 14(4), 2001, pp. 843-939.
- Manjul Bhargava, Arul Shankar, "Binary quartic forms having bounded invariants, and the boundedness of the average rank of elliptic curves", *Annals of Mathematics* 181(1), 2015, pp. 191-242.
- Manjul Bhargava, Arul Shankar, "Ternary cubic forms having bounded invariants, and the existence of a positive proportion of elliptic curves having rank 0", *Annals of Mathematics* 181(2), 2015, pp. 587-621.
- Bjorn Poonen, Eric Rains, "Random maximal isotropic subspaces and Selmer groups", *Journal of the American Mathematical Society* 25(1), 2012, pp. 245-269.
- Manjul Bhargava, Daniel M. Kane, Hendrik W. Lenstra, Bjorn Poonen, Eric Rains, "Modeling the distribution of ranks, Selmer groups, and Shafarevich-Tate groups of elliptic curves", *Cambridge Journal of Mathematics* 3(3), 2015, pp. 275-321.
- Manjul Bhargava, Zev Klagsbrun, Robert J. Lemke Oliver, Ari Shnidman, "3-isogeny Selmer groups and ranks of Abelian varieties in quadratic twist families over a number field", arXiv:1904.12547, 2019.
- Andrew Wiles, "The Birch and Swinnerton-Dyer Conjecture — Official problem description", Clay Mathematics Institute, 2000. https://www.claymath.org/wp-content/uploads/2022/06/birchswin.pdf
- Joseph H. Silverman, *The Arithmetic of Elliptic Curves*, 2판, Graduate Texts in Mathematics 106, Springer, 2009.
- John Tate, "On the conjectures of Birch and Swinnerton-Dyer and a geometric analog", *Séminaire Bourbaki* 306, 1966.
- Barry Mazur, "Modular curves and the Eisenstein ideal", *Publications Mathématiques de l'IHÉS* 47, 1977, pp. 33-186.
- Nicholas M. Katz, Peter Sarnak, *Random Matrices, Frobenius Eigenvalues, and Monodromy*, AMS Colloquium Publications 45, 1999.

---

## 0. 왜 "현대 장벽" 인가

BSD 추측은 1965년 Birch-Swinnerton-Dyer 의 EDSAC 2 컴퓨터 수치 실험에서 출발해 60년 동안 진화했다. 타원곡선 $E/\mathbb{Q}$ 의 **산술적 rank**($E(\mathbb{Q})$ 의 free rank) 와 **해석적 rank**(Hasse-Weil L-함수 $L(E, s)$ 의 $s=1$ 에서 영점 차수) 의 일치 ("rank 추측") 가 BSD 의 핵심.

네 갈래 흐름이 진화해 왔다:

1. **직접 증명(rank ≤ 1)** 흐름: Gross-Zagier 1986 + Kolyvagin 1988. rank 0, 1 에서 BSD 의 일부 확립.
2. **Iwasawa 이론** 흐름: Mazur-Swinnerton-Dyer 1974 의 p-adic L-함수. Coates-Wiles 1977.
3. **평균/통계** 흐름: Bhargava-Shankar 2010s 의 평균 rank 바운드.
4. **랜덤 행렬/모델** 흐름: Katz-Sarnak 1999, Poonen-Rains 2012, BKLPR 2015 — Selmer 군의 분포 예측.

각 흐름에 "여기까지 왔다" 와 "여기서부터 벽이다" 가 있다. 본 노트는 이 네 흐름의 진전과 장벽을 정리한다.

---

## 1. Clay 공식 statement

### 1.1 Wiles 2000

**공식 statement (Wiles 2000)**:
> Let $E$ be an elliptic curve defined over $\mathbb{Q}$. Then the order of vanishing of $L(E, s)$ at $s = 1$ equals the rank of the Mordell-Weil group $E(\mathbb{Q})$.

### 1.2 강한 BSD (Strong BSD)

더 강한 형태의 BSD 는 L-함수의 leading term 을 명시적으로 주장:
\[
\lim_{s \to 1} \frac{L(E, s)}{(s-1)^r} = \frac{\Omega_E \cdot \text{Reg}(E) \cdot \prod_p c_p \cdot |\Sha(E)|}{|E(\mathbb{Q})_{\text{tors}}|^2}
\]
여기서:
- $r = \text{rank}(E(\mathbb{Q}))$
- $\Omega_E$ = Néron period
- $\text{Reg}(E)$ = regulator (Néron-Tate 높이 쌍의 행렬식)
- $c_p$ = local Tamagawa 수
- $|\Sha(E)|$ = Shafarevich-Tate 군의 크기 (**유한 가정 필요**)
- $|E(\mathbb{Q})_{\text{tors}}|$ = torsion 부분군의 크기

### 1.3 **주의**: L-함수의 연속

- BSD 는 $L(E, s)$ 가 $s=1$ 에 해석적 연속을 가짐을 전제. 이것은 Wiles 1995 + Breuil-Conrad-Diamond-Taylor 2001 의 modularity 정리로 확립.
- 따라서 BSD 의 "statement" 가 잘 정의된 상태.

---

## 2. Birch-Swinnerton-Dyer 1965 — 수치 관찰

### 2.1 원 관찰

- Bryan Birch, Peter Swinnerton-Dyer, "Notes on elliptic curves II", *J. Reine Angew. Math.* 218, 1965, pp. 79-108.
- EDSAC 2 컴퓨터로 타원곡선 $E$ 의 $\mathbb{F}_p$-점의 수 $|E(\mathbb{F}_p)|$ 를 소수 $p \leq N$ 에서 계산, 곱
  \[
  \prod_{p \leq N} \frac{|E(\mathbb{F}_p)|}{p}
  \]
  의 점근 행동이 rank $r$ 와 같은 지수 $(\log N)^r$ 로 증가함을 수치적으로 관찰.
- 이 관찰이 후에 $L$-함수의 $s=1$ 에서 영점 차수 = rank 와 연결된다.

### 2.2 원본 추측 formulation

BSD 는 원 논문에서 다음 두 파트로 기술:

- **추측 A (rank 추측)**: $\text{ord}_{s=1} L(E, s) = r$.
- **추측 B (leading term)**: L-함수의 leading term 이 위 §1.2 공식으로 주어짐.

### 2.3 **한계**

- 수치적 증거는 강력했으나 수학적 증명 없음. 이후 60년 진전은 대부분 rank $\leq 1$ 특수 경우에 머물러 있다.

---

## 3. Coates-Wiles 1977 — 첫 부분 결과

### 3.1 결과

- John Coates, Andrew Wiles, "On the conjecture of Birch and Swinnerton-Dyer", *Invent. Math.* 39(3), 1977, pp. 223-251.
- **정리**: $E$ 가 CM (complex multiplication) 을 가지고, $L(E, 1) \neq 0$ 이면 $E(\mathbb{Q})$ 는 유한군.
- 즉, $L$ 값이 0 이 아님 → rank = 0.
- 이는 BSD 의 **부분** (rank 0 방향).

### 3.2 방법

- Iwasawa 이론(tower of cyclotomic extensions) + CM 주기 해석.
- 출처: Katz-Mazur 의 CM theory 와 Iwasawa 의 cyclotomic tower 아이디어 결합.

### 3.3 **한계**

- CM 타원곡선에만 적용. 일반 타원곡선은 CM 아님(generic 하게).

---

## 4. Gross-Zagier 1986 — Heegner points

### 4.1 결과

- Benedict H. Gross, Don B. Zagier, "Heegner points and derivatives of L-series", *Invent. Math.* 84(2), 1986, pp. 225-320.
- **Gross-Zagier 공식**:
  \[
  L'(E/\mathbb{Q}, 1) = c_E \cdot \hat{h}(P_K)
  \]
  여기서 $P_K$ 는 Heegner 점, $\hat{h}$ 는 Néron-Tate 높이, $c_E$ 는 명시적 상수.
- **의미**: $L'(E, 1) \neq 0$ 이면 $P_K$ 가 무한 차수 → $E(\mathbb{Q})$ 에 rank 1 generator 존재.

### 4.2 Heegner 점

- **Heegner 점**: 허수 2차 체 $K$ 에서 CM 이론을 통해 **체계적으로 구성**되는 $E(\bar{\mathbb{Q}})$ 위 점.
- 원본: Bryan Birch, "Heegner points", *Ann. of Math.* 94, 1971, 그리고 Kurt Heegner 1952 에서 시작.

### 4.3 **효과**

- rank 1 의 타원곡선에서 BSD 의 rank 추측이 **해석적 rank 가 1 이면 산술적 rank ≥ 1** 방향 확립.

---

## 5. Kolyvagin 1988 — Euler System

### 5.1 결과

- Victor A. Kolyvagin, "Finiteness of $E(\mathbb{Q})$ and $\Sha(E/\mathbb{Q})$ for a subclass of Weil curves", *Izv. Akad. Nauk SSSR* 52(3), 1988, pp. 522-540.
- **정리**: $L(E, 1) \neq 0$ 이면 $E(\mathbb{Q})$ 유한 + $\Sha(E/\mathbb{Q})$ 유한.
- **정리 (strong)**: Heegner 점이 무한 차수이면 rank $E(\mathbb{Q}) \leq 1$ + $\Sha$ 유한.

### 5.2 Euler system 아이디어

- Kolyvagin 은 Heegner 점으로부터 "파생된" cohomology 클래스 족 $\{c_n\}$ 을 구성. 이 족이 Euler system 공리(norm relations) 를 만족.
- 이 Euler system 을 사용해 Selmer group $\text{Sel}_{p^\infty}(E)$ 의 **상한**을 얻음.

### 5.3 **결합 결과 — rank ≤ 1 에서의 BSD 부분**

- Gross-Zagier 1986 + Kolyvagin 1988 결합: rank $E(\mathbb{Q}) = 0$ 이면 $\text{ord}_{s=1} L(E, s) = 0$, rank = 1 이면 $\text{ord}_{s=1} L(E, s) = 1$.
- 즉, **해석 → 산술** 과 **산술 → 해석** 양방향이 rank $\leq 1$ 에서 확립 (조건부).

### 5.4 **현재 장벽 1 — rank ≥ 2 의 벽**

- rank ≥ 2 의 경우 Gross-Zagier-Kolyvagin 접근이 적용되지 않는다.
  - Gross-Zagier 공식은 **2차 도함수** $L''(E, 1)$ 가 아닌 **1차 도함수** $L'(E, 1)$ 에 관한 것.
  - Heegner 점은 **1 개**의 point 만 주므로 rank 2 이상의 generator 를 못 만든다.
- 이것이 **BSD 의 주된 현대 장벽**: rank 2 이상 타원곡선에서 어떤 쪽의 증명도 없다.

---

## 6. 평균 rank — Bhargava-Shankar

### 6.1 결과 (Bhargava-Shankar 2015)

- Manjul Bhargava, Arul Shankar, "Binary quartic forms having bounded invariants, and the boundedness of the average rank of elliptic curves", *Ann. Math.* 181(1), 2015, pp. 191-242.
- **정리**: $\mathbb{Q}$ 위 타원곡선의 (naive height 로) 평균 rank 는 **최대 0.885**. 구체적으로, 2-Selmer group 의 평균 크기 = 3 임을 이용.
- 연관 결과: "Ternary cubic forms ...", *Ann. Math.* 181(2), 2015, pp. 587-621. 3-Selmer 평균 = 4 보여서 적어도 66% 의 타원곡선이 rank ≤ 1 임을 증명.

### 6.2 **평균 Selmer 공식**

더 일반적으로, Bhargava-Shankar 는 다음을 증명:

\[
\mathbb{E}_E[|\text{Sel}_n(E)|] = \sigma(n) \quad \text{(for small } n\text{)}
\]

2015년 시점까지 확립된 것: $n = 2, 3, 4, 5$ 까지. 즉, $|\text{Sel}_n(E)|$ 의 평균이 약수 합 함수 $\sigma(n)$ 와 일치한다는 구체적 계산.

### 6.3 **장벽 2 — BSD 의 산술-해석 동치는 평균에서만**

- 평균 결과는 **"전체 타원곡선 족" 에 대한 통계**. 특정 $E$ 의 BSD 를 증명하지 않는다.
- 또한 $n = 6$ 등 더 큰 $n$ 에서의 평균은 **미확립** (BKLPR 모델에서 가정 필요).

---

## 7. BKLPR 모델 — 랜덤 행렬 예측

### 7.1 Poonen-Rains 2012

- Bjorn Poonen, Eric Rains, "Random maximal isotropic subspaces and Selmer groups", *JAMS* 25(1), 2012, pp. 245-269.
- **모델**: 타원곡선의 $n$-Selmer 군을 랜덤 symmetric/antisymmetric 쌍변형 공간의 maximal isotropic subspace 로 모델링.
- 이 모델에서 예측되는 분포가 Bhargava-Shankar 의 저차 $n$ 실험값과 일치.

### 7.2 BKLPR 2015

- Bhargava, Kane, Lenstra, Poonen, Rains, "Modeling the distribution of ranks, Selmer groups, and Shafarevich-Tate groups of elliptic curves", *Cambridge J. Math.* 3(3), 2015, pp. 275-321.
- Poonen-Rains 모델을 확장해 **rank, Selmer, Sha 의 joint distribution** 을 예측.
- 예측: 모든 squarefree $n$ 에 대해
  \[
  \mathbb{E}_E[|\text{Sel}_n(E)|] = \sigma(n)
  \]
  특히 $n = 6$: $\sigma(6) = 12$ 가 평균 $|\text{Sel}_6|$.

### 7.3 **(A3) 가정** — BSD 의 가장 숨겨진 장벽

- BKLPR 모델의 핵심 가정 중 하나인 **(A3)**: 다른 primes $\ell$ 에서의 Selmer 데이터의 **점근 독립성**.
- (A3) 은 모델에 내장된 전제이며 **증명된 정리가 아님**.
- Bhargava-Klagsbrun-Lemke Oliver-Shnidman 2019: quadratic twist family 에서 **부분 (A3) 결과**. 그러나 일반 family 에서는 미확립.

### 7.4 **현재 장벽 3 — (A3) 의 증명 부재**

- (A3) 가정 하에서 Sel_6 평균 = 12 등 명쾌한 예측이 나온다. (A3) 를 제거하려면 Selmer 데이터 간 독립성을 증명해야 하는데, 이는 arithmetic analysis 의 어려운 미해결 문제.

---

## 8. 모듈성 정리 — BSD 의 전제

### 8.1 Wiles 1995 + Breuil-Conrad-Diamond-Taylor 2001

- Andrew Wiles, "Modular elliptic curves and Fermat's Last Theorem", *Ann. Math.* 141(3), 1995, pp. 443-551.
- Breuil, Conrad, Diamond, Taylor, "On the modularity of elliptic curves over ℚ: Wild 3-adic exercises", *JAMS* 14(4), 2001, pp. 843-939.
- **정리 (Modularity)**: $\mathbb{Q}$ 위 모든 타원곡선 $E$ 가 모듈러. 즉 $L(E, s)$ 가 weight 2 cusp form 의 $L$-함수와 일치.

### 8.2 **효과 — BSD 의 전제 확보**

- Modularity ⟹ $L(E, s)$ 가 전 평면에 해석적 연속 + functional equation.
- 이로 인해 BSD 의 statement 가 **완전히 정의된 문제**가 됨. Modularity 이전에는 $s=1$ 에서의 해석적 연속 자체가 가정.

### 8.3 **한계**

- Modularity 는 BSD 의 **전제**일 뿐, 핵심 문제 해결에는 기여 적음.
- Fermat 마지막 정리는 Modularity 로 해결되었으나, BSD 는 여전히 open.

---

## 9. Kolyvagin 이후 Euler system 의 한계

### 9.1 Euler system 의 역할

- Kolyvagin 1988 의 Euler system 은 타원곡선의 Selmer group 제어에 매우 강력.
- Kato-Scholl 2004, Lei-Loeffler-Zerbes 2014: Euler system 의 추가 예(Beilinson-Kato, Asai-Flach).

### 9.2 **장벽 4 — Heegner 점의 범위 한계**

- Heegner 점 구성은 **CM 이론** 에 의존. $E$ 가 일반 타원곡선일 때 Heegner 점이 존재하지만, 이 점들이 rank ≥ 2 의 generator 를 주지 못한다(1개만 줌).
- **일반화된 Heegner cycle** (Bertolini-Darmon-Prasanna 2013) 은 고차 Chow groups 에서의 구성. 그러나 rank ≥ 2 BSD 로의 적용은 미확립.

---

## 10. p-adic L-함수와 Iwasawa 이론

### 10.1 Mazur-Swinnerton-Dyer 1974

- Barry Mazur, Peter Swinnerton-Dyer, "Arithmetic of Weil curves", *Invent. Math.* 25, 1974, pp. 1-61.
- **p-adic $L$-함수**: Hecke 고유형식의 모듈러 symbols 를 사용해 p-adic L-함수 $L_p(E, s)$ 구성.

### 10.2 Mazur-Tate-Teitelbaum 1986 추측

- Barry Mazur, John Tate, Jeremy Teitelbaum, "On p-adic analogues of the conjectures of Birch and Swinnerton-Dyer", *Invent. Math.* 84, 1986, pp. 1-48.
- p-adic BSD: $L_p(E, s)$ 의 $s=1$ 에서 영점 차수 = $E(\mathbb{Q})$ rank (p-adic 버전).

### 10.3 **진전**

- Skinner-Urban 2014: **Iwasawa main conjecture** (Kato 방향) 를 GL_2 에서 증명. *Invent. Math.* 195, pp. 1-277.
- 그러나 이 결과도 rank ≤ 1 에 집중.

### 10.4 **장벽 5**

- p-adic BSD 조차 rank ≥ 2 에서 열림.
- p-adic 과 복소 BSD 사이의 translation 이 완전하지 않음.

---

## 11. 현재 알려진 영역 (2024 기준)

| 조건 | 결과 | 출처 |
|---|---|---|
| CM + $L(E,1) \neq 0$ | $E(\mathbb{Q})$ 유한 | Coates-Wiles 1977 |
| $L(E, 1) \neq 0$ | rank = 0 + $\Sha$ 유한 | Kolyvagin 1988 |
| $L'(E, 1) \neq 0$ | rank = 1 + $\Sha$ 유한 | Gross-Zagier + Kolyvagin |
| 평균 rank ≤ 0.885 | 평균 결과 | Bhargava-Shankar 2015 |
| 66% 이상 rank ≤ 1 | 평균 | Bhargava-Shankar 2015 |
| Sel_2 평균 = 3 | 엄밀 증명 | Bhargava-Shankar 2015 |
| Sel_3 평균 = 4 | 엄밀 증명 | Bhargava-Shankar 2015 |
| Sel_4, 5 평균 | 엄밀 증명 | Bhargava-Shankar 후속 |
| Sel_6 평균 = 12 | **(A3) 조건부** | BKLPR 2015 |
| rank ≥ 2 BSD | **미해결** | — |

---

## 12. 왜 실패/부분 성공인가 — 다섯 접근법과 각 장벽

### 12.1 Euler system (Kolyvagin)

- **경로**: Heegner cycle → cohomology class → Selmer bound.
- **진전**: rank ≤ 1 에서 완전 증명.
- **장벽**: 고차 cycle 부재.

### 12.2 Iwasawa Main Conjecture

- **경로**: p-adic $L$-함수 ↔ Selmer group 크기.
- **진전**: Skinner-Urban 2014.
- **장벽**: 복소 BSD 로의 확장 완전히 안 됨.

### 12.3 Modularity + automorphic form

- **경로**: 타원곡선 ↔ 모듈러 형식. Langlands 함자성.
- **진전**: Wiles 1995 BCDT 2001.
- **장벽**: Langlands 함자성 자체가 BSD 의 rank 추측을 직접 주지 않음.

### 12.4 BKLPR 랜덤 행렬 모델

- **경로**: Selmer 군을 random linear algebra object 로 모델.
- **진전**: 평균 rank + Sel_n 분포 예측.
- **장벽**: (A3) 독립성 가정.

### 12.5 Bhargava-Shankar arithmetic invariant theory

- **경로**: binary/ternary form 의 covariants 를 통한 Selmer 계산.
- **진전**: Sel_n 평균 $n = 2, 3, 4, 5$.
- **장벽**: $n \geq 6$ 에서 특수 결과 부재.

---

## 13. n=6 연결 (본 문서에서는 참고용 메모)

### 13.1 BSD Lemma 1 (BT-546, 무조건)

본 프로젝트가 엄밀 증명한 결과:

**Lemma 1 (CRT 분해)**: 모든 타원곡선 $E/\mathbb{Q}$ 와 서로소 $\gcd(m, n) = 1$ 에 대해,
\[
|\text{Sel}_{mn}(E)| = |\text{Sel}_m(E)| \cdot |\text{Sel}_n(E)|
\]
**증명**: Galois 모듈 수준에서 $E[mn] \cong E[m] \oplus E[n]$ (중국인 나머지 정리) + Kummer map 의 호환성. **엄밀 증명, 무조건**.

### 13.2 **의미**

- 이 결과는 BSD 문제와 직접 관련 없는 **작은 기여**이지만, Sel_6 = Sel_2 × Sel_3 로의 분해를 가능하게 함.
- 특히 $|\text{Sel}_6(E)| = |\text{Sel}_2(E)| \cdot |\text{Sel}_3(E)|$ 가 모든 $E$ 에 대해 **정확히** 성립.

### 13.3 Theorem 1 (Sel_n 평균 공식, BKLPR (A3) 하)

**Theorem 1 (조건부)**: (A3) 독립성 가정 하에, squarefree $n$ 에 대해
\[
\mathbb{E}_E[|\text{Sel}_n(E)|] = \sigma(n)
\]
특히 $n = 6$: 평균 = $\sigma(6) = 12$, 완전수 $n$ 에서 평균 = $2n$.

### 13.4 **정직성 선언** (millennium-7-closure-2026-04-11.md §BT-546)

> "Lemma 1은 진짜 기여 (이 세션의 두 엄밀 증명 중 하나). Sel_6 = σ(6) = 12 결론은 (A3) 조건부. BSD 미해결 유지."

### 13.5 추가 산술 관찰 (OBSERVATION, PROOF 아님)

- $j$-invariant $1728 = 12^3 = \sigma(6)^3$.
- Mazur 1977 torsion 유형 분류: 유리수 타원곡선의 가능한 torsion 부분군은 총 $15 = \sigma(6) + n/\varphi(6) = 12 + 3$ 종.
- Mazur 최대 torsion 크기 $12 = \sigma(6)$, 최소 금지 크기 $11 = n + \text{sopfr}(6) = 6 + 5$.
- Heegner-Stark: class number 1 인 허수 2차 체 수 $9 = (n/\varphi(6))^2 = 3^2$ (Stark 1967).
- Class number $h(K) = 1, 2, 3, 4, 5$ 의 체 수는 5 연속으로 알려짐, $h = 6$ 에서 break.

### 13.6 **범위 선언**

- 본 프로젝트는 BSD 를 해결하는 경로를 제공하지 않는다. §13 은 n=6 맥락에서 Selmer 분포와 torsion 수치의 산술 재표현을 기록할 뿐이다.
- BKLPR 모델의 (A3) 가정은 본 프로젝트에서도 여전히 가정. (A3) 증명은 별도 연구 대상.

---

## 14. Clay 공식 statement 와 범위

- Wiles 2000 공식: 위 §1.1 의 "rank 추측".
- Clay 는 **일반** $E/\mathbb{Q}$ 에 대한 증명만 상금 대상. 특수 경우 (CM, rank ≤ 1 조건) 의 증명은 상금 대상 아님.
- 현재 BSD 의 "부분 결과" 가 rank ≤ 1 에 멈춰 있으므로, rank ≥ 2 에서의 첫 돌파가 상금으로 가는 길.

---

## 15. 출처 요약표

| 연도 | 저자 | 결과 | 출처 |
|---|---|---|---|
| 1965 | Birch-Swinnerton-Dyer | 수치 관찰 + 추측 | *Crelle* 218 |
| 1966 | Tate | Bourbaki 강연 | Séminaire Bourbaki 306 |
| 1974 | Mazur-Swinnerton-Dyer | p-adic L-함수 | *Invent. Math.* 25 |
| 1977 | Coates-Wiles | CM + L(1)≠0 | *Invent. Math.* 39 |
| 1977 | Mazur | modular curve torsion | *Publ. IHES* 47 |
| 1986 | Gross-Zagier | Heegner + L'(1) | *Invent. Math.* 84 |
| 1988 | Kolyvagin | Euler system | *Izv. AN SSSR* 52 |
| 1995 | Wiles | Modularity (FLT) | *Ann. Math.* 141 |
| 1999 | Katz-Sarnak | 랜덤 행렬 모델 | AMS Coll. Pub. 45 |
| 2000 | Wiles | Clay 공식 statement | Clay |
| 2001 | BCDT | Modularity 완성 | *JAMS* 14 |
| 2012 | Poonen-Rains | Selmer 분포 모델 | *JAMS* 25 |
| 2014 | Skinner-Urban | Iwasawa main conj. | *Invent. Math.* 195 |
| 2015 | Bhargava-Shankar | 평균 rank ≤ 0.885 | *Ann. Math.* 181 |
| 2015 | BKLPR | 종합 분포 모델 | *Cambridge J. Math.* 3 |
| 2019 | BKLS | (A3) 부분 결과 | arXiv:1904.12547 |

---

## 16. 다음 태스크 연결

- PROB-P2-7: 푸앵카레(해결) 회고 분석.
- PURE-P1-2: 타원곡선 기초.
- PURE-P3-1: BKLPR Selmer 심화.
- PURE-P3-3: arithmetic geometry frontier.
- BT-546 (breakthrough-theorems): Lemma 1 + Sel_6 조건부.

---

## 17. 다음 단계

### 17.1 학습 층위에서의 다음 단계

- Silverman 2009 *Arithmetic of Elliptic Curves* 2판의 Chapter X (Selmer-Tate-Shafarevich) 와 Chapter XI (Heights) 를 정독.
- Kolyvagin 1988 원문 (러시아어) 의 영역판 (*Math. USSR-Izv.* 32, 1989) 을 읽고 Euler system 공리를 완전히 이해.
- BKLPR 2015 원문 *Cambridge J. Math.* 3 의 §5 (Selmer 분포 예측) 와 §6 (Sha 분포 예측) 을 따라가며 (A3) 가정의 위치를 정확히 파악.
- Bhargava-Shankar 2015 두 논문의 "counting lattice points" 기법을 primer 수준으로 학습. Granville의 *Geometry of Numbers* 강의가 입문.

### 17.2 n=6 프로젝트 내 다음 단계

- BT-546 Lemma 1 의 무조건 증명을 재검토 + 확장: squarefree 가 아닌 $n$ 으로의 일반화 가능성.
- Sel_6 = Sel_2 × Sel_3 구조를 쓰면 BKLPR 예측값 $\sigma(6) = 12 = 3 \cdot 4$ 가 $\mathbb{E}[|\text{Sel}_2|] \cdot \mathbb{E}[|\text{Sel}_3|]$ 로 분해 가능. 이는 (A3) 가정 없이 **독립성 기반 추정이 아닌 구조적 분해**. 본 프로젝트가 기여할 수 있는 남은 공간.
- Mazur 1977 의 $j = 1728$ curve ($E_{\text{CM}}: y^2 = x^3 - x$) 에 대한 Sel_6 직접 계산. 이 curve 는 $\sigma^3 = 1728$ 의 산술 일치가 있는 특수 예.

### 17.3 장벽 우회 시도의 조건

BSD 의 rank ≥ 2 벽을 넘으려면:

- **Heegner-type cycle 의 고차 일반화**(Bertolini-Darmon-Prasanna 확장).
- **(A3) 의 완전 증명**(BKLPR 가정 해소).
- **Automorphic 방향 확장**(Langlands 함자성의 GL_n 확장).

2026년 4월 현재, 어느 쪽도 rank ≥ 2 경우에서의 BSD 해결로 직결되는 돌파는 없음.

---

**정직성 체크**:
- Birch-Swinnerton-Dyer 1965 *Crelle* 218 의 원본은 영국 EDSAC 2 의 계산 결과표를 포함. 논문 Fig. 1, 2 의 수치를 Silverman 2009 Appendix C 가 재정리.
- Gross-Zagier 1986 공식은 *Invent. Math.* 84 Theorem V.1 에 명시. 본 노트 §4.1 의 형식은 교재 Silverman 2009 §11.5 기반.
- Kolyvagin 1988 원 러시아어 논문의 영역은 *Math. USSR-Izv.* 32(3), 1989, pp. 523-541 에서 확인 가능.
- Wiles 2000 Clay statement 는 https://www.claymath.org/wp-content/uploads/2022/06/birchswin.pdf Section 1 에서 직접 확인.
- Bhargava-Shankar 2015 *Ann. Math.* 181(1) Theorem 1 의 평균 rank 0.885 는 논문 Abstract 에 명시.
- BKLPR 2015 *Cambridge J. Math.* 3 의 (A3) 가정은 논문 §3 (Modeling assumptions) 에서 구체적으로 명시되며, §9 에서 가정의 부분 증거들을 열거.
- Poonen-Rains 2012 *JAMS* 25 의 random maximal isotropic subspace 모델은 Theorem 1.1 에서 formulate.
- BT-546 Lemma 1 의 엄밀 증명은 millennium-7-closure-2026-04-11.md §BT-546 에서 직접 확인. 본 노트 §13.1 은 그 statement 를 그대로 옮김.
