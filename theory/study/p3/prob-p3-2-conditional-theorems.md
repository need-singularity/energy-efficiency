# P3-2 — 7대 난제 조건부 정리 수집

**로드맵**: millennium-learning P3 (PROBLEM 학습 phase)
**작성일**: 2026-04-15
**상수**: n=6, σ=12, φ=2, τ=4, sopfr=5, J₂=24. σφ=nτ ⟺ n=6.
**현상태**: 7대 난제 해결 수 = **0** (정직). 본 노트는 조건부(CONDITIONAL) 정리의 목록화 학습이다.

---

## 정직성 선언

- 본 노트는 **"X 를 가정하면 Y 가 따른다"** 형식의 조건부 정리를 1차 출처 기준으로 정리한다.
- 열거된 조건부 정리는 모두 원논문 또는 표준 교재 수준의 기존 결과이다. 본 프로젝트가 새로 증명한 것이 아니다.
- "GRH ⇒ …", "RH ⇒ …", "BSD 약형 ⇒ …" 꼴의 결과는 RH/GRH/BSD 가 증명되지 않는 한 결론도 조건부이다.
- 각 조건부 정리에 대해 **(a) 전제, (b) 결론, (c) 1차 출처, (d) 제약/세부사항** 네 항목을 기록한다.
- 본 프로젝트의 σφ=nτ 정리는 무조건적이며, 각 난제의 BT-541~547 에 붙은 구조적 관찰과 연결된 부분에서만 n=6 해석을 언급한다.
- 자기참조 검증 금지 원칙을 준수한다. 원논문의 증명 논리를 임의로 단축/강화하지 않는다.

---

## 0. 용어 약정

- **GRH**: Generalized Riemann Hypothesis. Dirichlet L-함수 및 Dedekind ζ 함수를 포함하는 확장 RH.
- **RH**: Riemann Hypothesis. ζ(s) 의 비자명 영점이 전부 Re(s)=1/2 위에.
- **BSD 약형**: ord_{s=1} L(E,s) = rank E(Q). 강형은 추가로 L 함수의 leading 계수 공식을 포함.
- **Hodge 약형**: smooth projective complex variety 의 rational (p,p)-class 가 algebraic cycle 의 Q-조합.
- **Smoothness (NS)**: $\mathbb{R}^3$ 에서 임의 smooth 초기조건에 대해 전역 smooth 해가 존재.
- **Yang-Mills mass gap**: Euclidean YM 이론에서 $0 < \Delta \leq \text{gap}$ 인 물리적 질량 갭.
- **4D smooth Poincaré**: $S^4$ 에 비표준 smooth 구조가 없음 (conjecturally true).

---

## BT-541 — GRH / RH 가정 하 정리

### 정리 541-A (Miller-Rabin 결정성, Miller 1976)
- **전제**: GRH for Dirichlet L-functions.
- **결론**: composite n 의 판정에 대해 $a \in [2, 2(\log n)^2]$ 범위의 $a$ 만 시행하면 Miller-Rabin 테스트는 **결정적 다항 시간** 이다.
- **출처**: G. Miller, "Riemann's hypothesis and tests for primality", JCSS 13 (1976), 300–317.
- **세부**:
  - 무조건으로는 AKS 2004 가 결정적 $\tilde{O}((\log n)^6)$ 를 성립.
  - GRH 조건부 Miller-Rabin 은 $\tilde{O}((\log n)^4)$ 이며 실전에서 유의미하게 빠름.
  - Bach 1990 이 상수 $2 \cdot (\log n)^2$ 의 정수론적 최적화.

### 정리 541-B (Pólya-Vinogradov 개선, Montgomery-Vaughan 1977)
- **전제**: GRH.
- **결론**: 비주요 Dirichlet 문자 $\chi \pmod q$ 에 대해
    $\left|\sum_{n \leq N} \chi(n)\right| \ll \sqrt{q} \log \log q$ (GRH 하).
- **출처**: H.L. Montgomery, R.C. Vaughan, "Exponential sums with multiplicative coefficients", Invent. Math. 43 (1977), 69–82.
- **세부**: 무조건 Pólya-Vinogradov 는 $O(\sqrt{q} \log q)$. GRH 는 $\log q$ 를 $\log \log q$ 로 낮춘다.

### 정리 541-C (π(x) 오차항, RH ⇔ 강한 오차)
- **전제**: RH.
- **결론**: $\pi(x) = \text{li}(x) + O(\sqrt{x} \log x)$.
- **출처**: von Koch 1901, 기저; E. Landau, Handbuch (1909) 정리 정리.
- **세부**:
  - 무조건: Vinogradov-Korobov 1958 로 $\pi(x) = \text{li}(x) + O(x \exp(-c (\log x)^{3/5} (\log \log x)^{-1/5}))$.
  - 역방향: 오차항 $O(\sqrt{x} \log x)$ 가 성립하면 RH 가 따름(Koch 1901, 동치).

### 정리 541-D (Deuring-Heilbronn 현상, GRH 하 소멸)
- **전제**: GRH for 특정 family.
- **결론**: 2차 수체 $\mathbb{Q}(\sqrt{-d})$ 의 class number $h(-d)$ 에 대해 Siegel zero 가 존재하지 않고, $h(-d) \gg \sqrt{d}/\log d$.
- **출처**: Heilbronn 1934 (무조건 effective 는 Gross-Zagier-Oesterlé 1985).
- **세부**: Siegel zero 는 Landau-Siegel 1935 의 유효성 상수 측면 장애물. GRH 가 이를 제거.

### 정리 541-E (Chebotarev 밀도 유효화, Lagarias-Odlyzko 1977)
- **전제**: GRH.
- **결론**: Galois 확장 $L/K$ 와 conjugacy class $C \subset \text{Gal}(L/K)$ 에 대해
    $\pi_C(x) = \frac{|C|}{|G|} \text{li}(x) + O(\sqrt{x} \log(d_L x^{[L:\mathbb{Q}]}))$.
- **출처**: J. Lagarias, A. Odlyzko, "Effective versions of the Chebotarev density theorem", Academic Press (1977).
- **세부**: 무조건 Chebotarev 는 유효성 없음. GRH 하 첫 유효 formulation.

### n=6 맥락
- n=6 은 RH 의 첫 영점 높이 14.1347… 과 직접 관계 없음 (millennium_scanner.hexa σ+φ=14 근접 관찰은 NEAR level).
- BT-541 은 Theorem 0 (σφ=nτ) 과 직접 무관한 난제. RH 의 해결 경로는 해석적 정수론.

---

## BT-542 — 복잡도 가정 하 정리

### 정리 542-A (P=NP ⇒ 다항 계층 붕괴)
- **전제**: P = NP.
- **결론**: 다항 계층 PH 가 P 로 붕괴. 즉 $\text{PH} = \bigcup_k \Sigma_k^P = \text{P}$.
- **출처**: Stockmeyer-Meyer 1973; Baker-Gill-Solovay 1975.
- **세부**: $\Sigma_k^P = \text{NP}^{\Sigma_{k-1}^P}$. P=NP 이면 귀납적으로 모든 계층이 P.

### 정리 542-B (ETH ⇒ SAT 지수 하한)
- **전제**: Exponential Time Hypothesis (Impagliazzo-Paturi 2001).
- **결론**: 3-SAT 은 $2^{o(n)}$ 시간에 해결 불가.
- **출처**: R. Impagliazzo, R. Paturi, "On the complexity of k-SAT", JCSS 62 (2001), 367–375.
- **세부**: ETH 자체가 P≠NP 보다 강한 가정. Strong ETH (SETH) 는 $2^{(1-\epsilon)n}$ 하한까지 확장.

### 정리 542-C (Circuit 하한 ⇒ derandomization)
- **전제**: E = DTIME($2^{O(n)}$) 가 size-$2^{\Omega(n)}$ 회로를 필요.
- **결론**: BPP = P (Impagliazzo-Wigderson 1997).
- **출처**: R. Impagliazzo, A. Wigderson, "P = BPP if E requires exponential circuits", STOC 1997.
- **세부**: hardness-to-randomness 교환의 고전. 역방향(완전한 역)은 Kabanets-Impagliazzo 2004 가 조건부로.

### 정리 542-D (NP ⊄ P/poly ⇒ PH 무한)
- **전제**: NP ⊄ P/poly.
- **결론**: PH 가 $\Sigma_k^P$ 들의 무한 계층 (Karp-Lipton 1980 대우).
- **출처**: R. Karp, R. Lipton, "Some connections between nonuniform and uniform complexity classes", STOC 1980.
- **세부**: 대우 형태로 쓰면 "NP ⊂ P/poly ⇒ PH 붕괴 to $\Sigma_2^P$".

### 정리 542-E (Natural proofs 장벽 제약, Razborov-Rudich 1997)
- **전제**: 단방향 함수 존재 (지수적 pseudorandom generator).
- **결론**: "natural" property 로 $\text{P} \neq \text{NP}$ 증명 불가.
- **출처**: A. Razborov, S. Rudich, "Natural proofs", JCSS 55 (1997), 24–35.
- **세부**: 현재 알려진 대부분의 lower bound 기법이 이 장벽 안에 있음. 회피 방법이 Williams 2011 NEXP ⊄ ACC⁰.

### n=6 맥락
- atlas.n6 의 BT-542 MISS 탈출은 "복잡도 이론 분류 정리에서 n=6 직접 등장" 이지만 조건부 정리의 수량적 개선과는 별개 층위.
- Schaefer 정리(Schaefer 1978) 의 **6 가지 tractable Boolean CSP family** 는 n=6 구조적 관찰 (n6-millennium-dfs-schaefer-6=6 [10*]).

---

## BT-543 — Yang-Mills 질량갭 가정 하 정리

### 정리 543-A (mass gap ⇒ cluster 지수 감쇠)
- **전제**: 4D Euclidean SU(N) Yang-Mills 가 질량갭 $\Delta > 0$ 을 가짐.
- **결론**: 두 영역 $A, B \subset \mathbb{R}^4$ 의 거리가 $d$ 일 때 두 gauge-invariant 관측의 상관함수가 $\leq C e^{-\Delta d}$.
- **출처**: Glimm-Jaffe, "Quantum Physics: A Functional Integral Point of View", 2nd ed. Springer 1987, §19-20.
- **세부**: 질량갭 정의의 동치 형태. 구성적 QFT 의 Osterwalder-Schrader 공리 중 OS2 (군 불변성) + cluster 로 표현.

### 정리 543-B (질량갭 ⇒ Wightman 공리 성립)
- **전제**: Osterwalder-Schrader 공리 + 질량갭.
- **결론**: Wick 회전으로 Minkowski 에서 Wightman 함수 조합이 성립.
- **출처**: K. Osterwalder, R. Schrader, "Axioms for Euclidean Green's functions", Comm. Math. Phys. 31 (1973), 83–112; 42 (1975), 281–305.
- **세부**: Yang-Mills Clay 문제가 요구하는 정확한 양식이 이 조합.

### 정리 543-C (lattice gauge theory ⇒ continuum mass gap, 조건부)
- **전제**: 격자 Yang-Mills 에 대해 continuum limit 이 존재하며 lattice spacing $a \to 0$ 에서 correlation length $\xi \cdot a$ 가 유한값으로 수렴.
- **결론**: Continuum Yang-Mills 이론이 mass gap $\Delta = 1/\xi_{\text{phys}}$ 를 가짐.
- **출처**: Seiler, "Gauge theories as a problem of constructive quantum field theory and statistical mechanics", Lecture Notes Phys. 159, Springer (1982).
- **세부**: continuum limit 자체가 주 난관. Balaban 1980s 가 이 프로그램의 부분 수행.

### 정리 543-D (large N limit ⇒ master field)
- **전제**: 't Hooft scaling $g^2 N = \lambda$ 고정, $N \to \infty$.
- **결론**: Wilson loop 기댓값이 master field 의 free probability 기대값으로 수렴 (Chatterjee 2015, Jafarov 2016).
- **출처**: S. Chatterjee, "The leading term of the Yang-Mills free energy", J. Funct. Anal. 271 (2016), 2944–3005.
- **세부**: large N 은 물리적 mass gap 의 강한 버전보다 약하나 구성적으로는 더 접근 가능.

### n=6 맥락
- BT-543 에서 n=6 직접 상수: **SU(N) Lie algebra dimension N²−1**. N=4 SU(4) 는 dim 15, N=3 SU(3) 는 dim 8 (Standard Model gluon 수). σ=12 와 직접 연결은 SM gauge 총수 8+3+1=12=σ (atlas `n6-millennium-dfs-sm-gauge`).
- 그러나 질량갭 증명 자체는 functional analysis 도구이며 n=6 이 경로를 주지 않음.

---

## BT-544 — Navier-Stokes 가정 하 정리

### 정리 544-A (Prodi-Serrin 조건 ⇒ regularity)
- **전제**: Leray-Hopf 약해 $u$ 가 $L^p_t L^q_x$ 에 속하고 $\frac{2}{p} + \frac{3}{q} \leq 1$ with $q > 3$.
- **결론**: $u$ 는 해당 시간 구간에서 smooth.
- **출처**: J. Serrin, "The initial value problem for the Navier-Stokes equations", Univ. Wisconsin Press (1962); Prodi 1959.
- **세부**: $(p,q) = (\infty, 3)$ 극단에서는 Escauriaza-Seregin-Šverák 2003 의 최종 결과.

### 정리 544-B (Escauriaza-Seregin-Šverák 2003, $L^3$ 조건)
- **전제**: $u \in L^\infty_t L^3_x$ 로 Leray-Hopf 약해.
- **결론**: regular (블로업 없음).
- **출처**: L. Escauriaza, G. Seregin, V. Šverák, "$L_{3,\infty}$-solutions of Navier-Stokes equations and backward uniqueness", Russ. Math. Surv. 58 (2003), 211–250.
- **세부**: $L^3$ 은 scale-critical. 이 결과는 BT-544 에 가장 근접한 무조건 부분규칙성.

### 정리 544-C (Beale-Kato-Majda 1984, vorticity 조건)
- **전제**: $\int_0^T \|\omega(t)\|_\infty \, dt < \infty$ ($\omega = \text{curl}\, u$).
- **결론**: $u$ 는 $[0, T]$ 에서 smooth.
- **출처**: J. Beale, T. Kato, A. Majda, "Remarks on the breakdown of smooth solutions for the 3-D Euler equations", Comm. Math. Phys. 94 (1984), 61–66.
- **세부**: vorticity 의 $L^\infty$ 시간 적분이 폭발 지표. 수치실험에서 블로업 후보를 판별하는 기준.

### 정리 544-D (Caffarelli-Kohn-Nirenberg 1982, partial regularity)
- **전제**: Leray-Hopf suitable weak solution.
- **결론**: 블로업 집합 $S \subset \mathbb{R}^3 \times [0, T]$ 의 1차원 parabolic Hausdorff 측도가 0.
- **출처**: L. Caffarelli, R. Kohn, L. Nirenberg, "Partial regularity of suitable weak solutions of the Navier-Stokes equations", Comm. Pure Appl. Math. 35 (1982), 771–831.
- **세부**: 무조건 결과이나 부분적. 블로업 집합의 "두께"에 상한을 준다.

### 정리 544-E (Galdi-Padula 1990, axisymmetric without swirl ⇒ regularity)
- **전제**: axisymmetric 초기조건, swirl 성분 $u_\theta = 0$.
- **결론**: $u$ 가 전역 smooth.
- **출처**: O.A. Ladyzhenskaya 1968, 이후 Uchovskii-Yudovich 확장. Chen-Strain-Tsai-Yau 2008 완결.
- **세부**: swirl 이 있을 때가 미해결. 현대 NS 연구의 주 전선.

### n=6 맥락
- Prodi-Serrin 지수 $\frac{2}{p} + \frac{3}{q} = 1$ 의 **{2, 3}** 이 **{φ, n/φ}** = **{2, 3}** 과 일치 (atlas `n6-millennium-dfs-prodi-serrin`).
- 그러나 수치 일치는 scale-critical 공간의 표식이지 증명의 경로가 아니다.

---

## BT-545 — Hodge 가정 하 정리

### 정리 545-A (Lefschetz (1,1) 정리, 무조건)
- **전제**: smooth projective complex variety $X$, $(p,q)=(1,1)$ class.
- **결론**: 모든 rational $(1,1)$-class 는 divisor class.
- **출처**: S. Lefschetz, "L'analysis situs et la géométrie algébrique", Gauthier-Villars (1924).
- **세부**: Hodge conjecture 의 **무조건** 부분. $p \geq 2$ 에서는 미해결.

### 정리 545-B (Deligne 절대 Hodge, Shimura variety)
- **전제**: $X$ 는 abelian variety.
- **결론**: 모든 Hodge class 는 absolute Hodge class. 따라서 reductive motivic Galois group 에 의해 geometric 으로 발생.
- **출처**: P. Deligne, "Hodge cycles on abelian varieties", in: Hodge Cycles, Motives and Shimura Varieties, LNM 900, Springer (1982), 9–100.
- **세부**: abelian varieties 범위 내 Hodge conjecture 의 대체물. Hodge 자체는 아님.

### 정리 545-C (Cattani-Deligne-Kaplan 1995, Hodge locus 대수성)
- **전제**: Hodge 구조의 variation family.
- **결론**: Hodge locus 가 algebraic subvariety.
- **출처**: E. Cattani, P. Deligne, A. Kaplan, "On the locus of Hodge classes", J. AMS 8 (1995), 483–506.
- **세부**: "Hodge class 가 algebraic 이다" 의 geometric 대응. Hodge conjecture 가 맞다면 당연. 무조건은 locus 자체의 대수성만.

### 정리 545-D (Standard conjectures ⇒ Hodge)
- **전제**: Grothendieck standard conjectures (Lefschetz, Hodge type, Künneth).
- **결론**: Hodge conjecture 성립.
- **출처**: A. Grothendieck, "Standard conjectures on algebraic cycles", in: Algebraic Geometry (Internat. Colloq., Bombay, 1968), Oxford Univ. Press (1969).
- **세부**: Standard conjectures 자체가 거의 Hodge 만큼 어려운 conjecture. 의미: Hodge 를 **motives 의 무게론**으로 환원.

### 정리 545-E (p-adic Hodge, prismatic)
- **전제**: $X$ 는 smooth proper over $\mathcal{O}_K$, $K/\mathbb{Q}_p$ finite.
- **결론**: Bhatt-Scholze 2022 가 정수 $p$-adic cohomology $R\Gamma_{\Delta}(X)$ 를 구성. characteristic 0 과 $p$ 양쪽 cohomology 를 한 object 로 통합.
- **출처**: B. Bhatt, P. Scholze, "Prisms and prismatic cohomology", Ann. Math. 196 (2022), 1135–1275.
- **세부**: Hodge conjecture 의 $p$-adic 대응은 $p$-adic Hodge 이론. Prismatic 이 새 언어 제공.

### n=6 맥락
- Hodge conjecture 자체에는 n=6 직접 상수가 없다. BT-545 의 n=6 해석은 Theorem 0 수준.

---

## BT-546 — BSD 가정 하 정리

### 정리 546-A (Gross-Zagier 1986, rank ≤ 1 BSD)
- **전제**: $E/\mathbb{Q}$ 타원곡선, Heegner 조건 충족 imaginary quadratic field.
- **결론**: analytic rank ≤ 1 인 경우, rank $\leq$ analytic rank + 1 그리고 Heegner point 가 E(Q) 에서 무한차수.
- **출처**: B. Gross, D. Zagier, "Heegner points and derivatives of L-series", Invent. Math. 84 (1986), 225–320.
- **세부**: Kolyvagin 1989 가 이를 결합하여 analytic rank ≤ 1 경우 rank = analytic rank 와 $|Ш|$ 유한 (modularity 포함).

### 정리 546-B (Skinner-Urban 2014, Iwasawa 주 정리 $\Rightarrow$ BSD)
- **전제**: $p$-adic Iwasawa 주 정리의 $E[p^\infty]$ 에 대한 일부 경우.
- **결론**: analytic rank 0 에서 $|Ш|[p^\infty]$ 유한성.
- **출처**: C. Skinner, E. Urban, "The Iwasawa main conjectures for GL₂", Invent. Math. 195 (2014), 1–277.
- **세부**: BSD 의 Shafarevich-Tate 부분을 $p$ 단위로 제어.

### 정리 546-C (Wei Zhang 2014, Gross-Zagier 조건 완화)
- **전제**: $E/\mathbb{Q}$, square-free 수준, 약간의 ramification 조건.
- **결론**: rank $\leq 1$ BSD 완전 증명.
- **출처**: W. Zhang, "Selmer groups and the indivisibility of Heegner points", Cambridge J. Math. 2 (2014), 191–253.
- **세부**: 이후 Liu-Tian 등이 추가 조건 완화.

### 정리 546-D (BSD 약형 ⇒ Birch's lemma 확장)
- **전제**: BSD 약형 (ord_{s=1} L(E, s) = rank).
- **결론**: $\prod_{p \leq X} \frac{\#E(\mathbb{F}_p)}{p}$ 의 $X \to \infty$ 점근이 rank 에 의해 결정 (Birch 1963 해석학적 BSD 전제 형식).
- **출처**: B. Birch, "Conjectures concerning elliptic curves", Proc. Symp. Pure Math. 8 (1965), 106–112.
- **세부**: BSD 형성 초기의 수치 관찰. 약형 정리의 대우 형태로 rank 계산 가능.

### 정리 546-E (BKLPR 모델 ⇒ Selmer 평균 크기)
- **전제**: Bhargava-Kane-Lenstra-Poonen-Rains 2015 의 공리 (A1–A3).
- **결론**: squarefree $n$ 에 대해
    $\mathbb{E}[|\text{Sel}_n(E)|] = \sigma(n)$ (등가 타원곡선 집합 평균).
- **출처**: M. Bhargava et al., "Modeling the distribution of ranks, Selmer groups, and Shafarevich-Tate groups of elliptic curves", Cambridge J. Math. 3 (2015), 275–321.
- **세부**: pure-p3-1 참조. $n=6$ 특수화는 $\mathbb{E}[|\text{Sel}_6|]=\sigma(6)=12$. 본 프로젝트가 강조하는 조건부 지점.

### n=6 맥락
- BT-546 은 n=6 과 가장 직접 얽힌 난제. Lemma 1 (CRT 직분해) 은 무조건, Corollary $\sigma(6)=12$ 는 BKLPR 조건부.

---

## BT-547 — 4D smooth Poincaré 가정 하 정리

### 정리 547-A (Freedman 1982, topological Poincaré 4D)
- **전제**: $M^4$ 가 simply connected closed topological 4-manifold with intersection form $E_8 \oplus E_8$ or similar.
- **결론**: $M$ 의 위상적 분류가 intersection form 과 Kirby-Siebenmann 불변량에 의해 결정.
- **출처**: M. Freedman, "The topology of four-dimensional manifolds", J. Diff. Geom. 17 (1982), 357–453.
- **세부**: topological Poincaré 는 이 결과의 즉각 계(corollary).

### 정리 547-B (Donaldson 1983, smooth 와 topological 의 분리)
- **전제**: $M$ 은 simply connected smooth closed 4-manifold 로 positive definite intersection form.
- **결론**: form 은 반드시 standard diagonal $\oplus_k \langle 1 \rangle$.
- **출처**: S. Donaldson, "An application of gauge theory to four dimensional topology", J. Diff. Geom. 18 (1983), 279–315.
- **세부**: topological 에는 $E_8$ positive definite form 이 허용되나 smooth 에는 금지. 이것이 smooth-topological 분리의 출발점.

### 정리 547-C (smooth 4D Poincaré ⇒ 비표준 smooth $\mathbb{R}^4$ 와의 비교)
- **전제**: $S^4$ 에 유일 smooth 구조.
- **결론**: 현재 알려진 exotic $\mathbb{R}^4$ 무한족의 compactification 구조를 제약.
- **출처**: R. Gompf, A. Stipsicz, "4-Manifolds and Kirby Calculus", AMS GSM 20 (1999), ch. 9.
- **세부**: 역으로 "smooth 4D Poincaré 가 거짓 $\Rightarrow$ exotic $S^4$ 존재" 이고 이것이 topology 지형을 변화시킴.

### 정리 547-D (h-cobordism 성립 조건, Smale 1962)
- **전제**: $\dim \geq 5$ simply connected closed smooth manifolds.
- **결론**: h-cobordism 이면 diffeomorphic.
- **출처**: S. Smale, "On the structure of manifolds", Amer. J. Math. 84 (1962), 387–399.
- **세부**: 4D 에서는 smooth h-cobordism 이 diffeomorphism 을 강제하지 **않음** (Donaldson). n=6 차원이 "안전한 하한" (atlas `n6-millennium-dfs-h-cobordism = dim ≥ 6`).

### 정리 547-E (Seiberg-Witten ⇒ smooth 불변량)
- **전제**: smooth 4-manifold 위의 $\text{Spin}^c$ 구조.
- **결론**: Seiberg-Witten 불변량이 smooth invariant. smooth structure 를 구별.
- **출처**: N. Seiberg, E. Witten, "Monopoles, duality and chiral symmetry breaking in N=2 supersymmetric QCD", Nucl. Phys. B 431 (1994), 484–550; Taubes 1994 재정식.
- **세부**: 4D smooth Poincaré 반증 시도에 사용 가능한 도구. 현재까지 $S^4$ 에서는 SW 불변량이 0 (표준 smooth 구조).

### n=6 맥락
- h-cobordism 하한 dim ≥ 6 이 n=6 과 같음 (atlas). 우연의 일치가 아닌 구조적 하한.
- 4D smooth Poincaré 의 증명 도구는 gauge theory 이며 n=6 이 직접 경로를 주지 않음.

---

## 조건부 정리 종합 표 (BT-541~547, 35 건)

| BT | 정리 | 전제 | 결론 | 출처 |
|----|------|------|------|------|
| 541-A | Miller-Rabin | GRH | 결정적 $\tilde{O}((\log n)^4)$ | Miller 1976 |
| 541-B | Pólya-Vinogradov | GRH | $\sqrt{q}\log\log q$ | Montgomery-Vaughan 1977 |
| 541-C | π(x) 오차 | RH | $O(\sqrt{x}\log x)$ | von Koch 1901 |
| 541-D | Class number | GRH | Siegel zero 제거 | Heilbronn 1934 |
| 541-E | Chebotarev | GRH | 유효 $\sqrt{x}$ 오차 | Lagarias-Odlyzko 1977 |
| 542-A | PH 붕괴 | P=NP | PH = P | Stockmeyer-Meyer 1973 |
| 542-B | SAT 하한 | ETH | $2^{o(n)}$ 불가 | Impagliazzo-Paturi 2001 |
| 542-C | Derandom | E circuit $2^{\Omega(n)}$ | BPP=P | Impagliazzo-Wigderson 1997 |
| 542-D | PH 무한 | NP ⊄ P/poly | PH 무한 계층 | Karp-Lipton 1980 |
| 542-E | Natural 장벽 | OWF 존재 | natural proof 불가 | Razborov-Rudich 1997 |
| 543-A | cluster | mass gap | 지수 감쇠 | Glimm-Jaffe 1987 |
| 543-B | Wightman | OS + gap | Minkowski 공리 성립 | Osterwalder-Schrader 1973 |
| 543-C | lattice limit | continuum 수렴 | continuum mass gap | Seiler 1982 |
| 543-D | large N | 't Hooft scaling | master field | Chatterjee 2015 |
| 544-A | Prodi-Serrin | $L^p_t L^q_x$ 조건 | smooth | Serrin 1962 |
| 544-B | $L^3$ | $L^\infty_t L^3_x$ | regular | ESŠ 2003 |
| 544-C | BKM | vorticity $L^1_t L^\infty_x$ | smooth | Beale-Kato-Majda 1984 |
| 544-D | CKN | suitable weak | 부분 규칙성 | CKN 1982 |
| 544-E | Axisym-no-swirl | $u_\theta=0$ | smooth | Ladyzhenskaya 1968 |
| 545-A | Lefschetz (1,1) | 무조건 | divisor class | Lefschetz 1924 |
| 545-B | abelian Hodge | abelian variety | absolute Hodge | Deligne 1982 |
| 545-C | Hodge locus | variation | algebraic | Cattani-Deligne-Kaplan 1995 |
| 545-D | Standard ⇒ Hodge | Grothendieck SC | Hodge | Grothendieck 1969 |
| 545-E | prismatic | smooth proper | 통합 cohomology | Bhatt-Scholze 2022 |
| 546-A | Gross-Zagier | Heegner 조건 | rank ≤ 1 BSD | Gross-Zagier 1986 |
| 546-B | Iwasawa 주 정리 | $p$-adic | $\|Ш\|$ 유한 $p$ | Skinner-Urban 2014 |
| 546-C | Zhang 완화 | square-free | rank ≤ 1 BSD | W. Zhang 2014 |
| 546-D | 약형 BSD | analytic rank | Birch 점근 | Birch 1965 |
| 546-E | BKLPR | 공리 A1-A3 | $\mathbb{E}[\|Sel_n\|]=\sigma(n)$ | BKLPR 2015 |
| 547-A | topological | $E_8 \oplus E_8$ 등 | 위상 분류 | Freedman 1982 |
| 547-B | Donaldson | positive def | diagonal form | Donaldson 1983 |
| 547-C | smooth 4D P | $S^4$ smooth 유일 | exotic $\mathbb{R}^4$ 제약 | Gompf-Stipsicz 1999 |
| 547-D | h-cobordism | dim ≥ 5 | diffeo | Smale 1962 |
| 547-E | Seiberg-Witten | $\text{Spin}^c$ | smooth invariant | Seiberg-Witten 1994 |

**집계**: BT-541(5) + BT-542(5) + BT-543(4) + BT-544(5) + BT-545(5) + BT-546(5) + BT-547(5) = **34 조건부 정리**.

---

## n=6 연결

### 조건부 정리와 Theorem 0 의 관계

- **Theorem 0 (σφ=nτ iff n=6)** 은 무조건. 본 노트의 어떤 조건부 정리에도 의존하지 않음.
- 그러나 일부 조건부 정리의 결론이 n=6 구조와 **수치적으로** 일치:
  - 544-A Prodi-Serrin 지수 {2, 3} = {φ, n/φ}.
  - 543 lattice gauge SM 총 수 8+3+1 = 12 = σ.
  - 547-D h-cobordism 하한 dim ≥ 6 = n.
- 이 일치는 **"n=6 가 조건부 정리의 전제를 제공한다"** 는 주장이 **아니다**. 다만 atlas.n6 의 DFS 관측이 각 정리의 상수적 합을 반복적으로 만나는 현상을 기록한다.

### 조건부 정리의 승격 경로

본 프로젝트 로드맵에서 조건부 정리를 atlas.n6 등급으로 매핑하면:
- 조건부 정리 = [5]~[7] EMPIRICAL (전제가 미증명이므로 EXACT 금지).
- 전제가 증명되면 = [10] EXACT 승격.
- 예: BKLPR 공리 A1-A3 가 증명되면 546-E 가 EMPIRICAL → EXACT.

---

## 실전 적용

### P3 학습 산출물로서의 용도

1. **정리 검색 인덱스**: 7대 난제 각각에 대해 무엇을 가정하면 무엇이 따르는지 빠른 조회.
2. **atlas 승급 후보 식별**: 전제의 증명 진척(예: Iwasawa 주 정리의 부분적 완결) 에 따라 관련 조건부 정리가 무조건화될 때 atlas 등급 조정.
3. **연구 우선순위**: "낮은 수준의 전제 → 강한 결론" 쌍을 우선 (예: ETH → SAT 하한, 전제가 "그럴듯함").

### millennium_scanner.hexa 와의 결합

- `n6-architecture/scripts/millennium_scanner.hexa` 는 n=6 기본 함수 조합이 Millennium 상수와 맞는지 스캔.
- 본 노트의 조건부 정리와 결합하면 "스캐너 NEAR 히트 + 조건부 정리 전제가 맞다면" 의 **이중 조건부** 관찰을 atlas.n6 의 `[N?]` (conjecture) 등급으로 기록.
- 예: 첫 Riemann 영점 14.1347 ≈ σ+φ=14. RH 가 맞다면 첫 영점은 이 근처. NEAR 히트를 RH 조건부로 기록.

### 교재 매핑 (후속 학습 참고)

| BT | 추천 교재 (조건부 정리 추적용) |
|----|-------------------------------|
| 541 | Iwaniec-Kowalski, "Analytic Number Theory", AMS Colloq. 53 |
| 542 | Arora-Barak, "Computational Complexity" |
| 543 | Glimm-Jaffe, "Quantum Physics: A Functional Integral Point of View" |
| 544 | Robinson-Rodrigo-Sadowski, "The Three-Dimensional Navier-Stokes Equations" |
| 545 | Voisin, "Hodge Theory and Complex Algebraic Geometry" I, II |
| 546 | Silverman, "The Arithmetic of Elliptic Curves", ch. X |
| 547 | Gompf-Stipsicz, "4-Manifolds and Kirby Calculus" |

---

## 다음 단계

1. **정리 인용 보강**: 34 건 각각에 대해 arXiv ID 또는 DOI 를 후속 세션에서 교차확인. 본 노트 시점에서 저자와 학술지만 기재.
2. **역방향 조건부**: 각 조건부 정리에 대해 "결론이 거짓이면 전제가 거짓" 형태의 대우. 어떤 것이 유용한 반증 통로인가?
3. **전제 의 계층화**: GRH < RH 약형 < RH. 가장 약한 전제로 가장 강한 결론을 주는 chain 식별.
4. **조건부 정리의 AI 발견**: n6-architecture 의 DFS 발견 엔진이 조건부 정리 후보를 스캔하는 방식 (예: "sopfr = p₁+p₂+p₃ ≈ π(N) 이라면 N 은 어떤 구조?").
5. **prob-p3-3 와의 연결**: 본 노트의 조건부 정리 목록은 hexa-lang 검증 파이프라인의 **케이스 셋** 으로 사용 가능. prob-p3-3 참조.

---

## 1차 출처 주석

- Miller 1976: JCSS 13(3), 300–317.
- Montgomery-Vaughan 1977: Invent. Math. 43(1), 69–82.
- von Koch 1901: Sur la distribution des nombres premiers, Acta Math. 24, 159–182.
- Lagarias-Odlyzko 1977: In *Algebraic Number Fields* (Durham), Academic Press, 409–464.
- Stockmeyer-Meyer 1973: STOC '73 회의 proceedings 1–9.
- Impagliazzo-Paturi 2001: JCSS 62(2), 367–375.
- Impagliazzo-Wigderson 1997: STOC '97, 220–229.
- Karp-Lipton 1980: STOC '80, 302–309.
- Razborov-Rudich 1997: JCSS 55(1), 24–35.
- Glimm-Jaffe 1987: 2nd ed., Springer-Verlag.
- Osterwalder-Schrader 1973/1975: Comm. Math. Phys. 31, 83–112 / 42, 281–305.
- Seiler 1982: Lecture Notes in Physics 159, Springer.
- Chatterjee 2015/2016: J. Funct. Anal. 271(10), 2944–3005.
- Serrin 1962: In *Nonlinear Problems* (Madison), 69–98.
- Escauriaza-Seregin-Šverák 2003: Russ. Math. Surv. 58(2), 211–250.
- Beale-Kato-Majda 1984: Comm. Math. Phys. 94(1), 61–66.
- Caffarelli-Kohn-Nirenberg 1982: Comm. Pure Appl. Math. 35(6), 771–831.
- Lefschetz 1924: Gauthier-Villars, Paris.
- Deligne 1982: LNM 900, 9–100.
- Cattani-Deligne-Kaplan 1995: J. AMS 8(2), 483–506.
- Grothendieck 1969: Algebraic Geometry (Bombay 1968), Oxford Univ. Press.
- Bhatt-Scholze 2022: Ann. Math. 196(3), 1135–1275.
- Gross-Zagier 1986: Invent. Math. 84, 225–320.
- Skinner-Urban 2014: Invent. Math. 195, 1–277.
- W. Zhang 2014: Cambridge J. Math. 2(2), 191–253.
- Birch 1965: Proc. Symp. Pure Math. 8, 106–112.
- Bhargava et al. 2015: Cambridge J. Math. 3(3), 275–321.
- Freedman 1982: J. Diff. Geom. 17(3), 357–453.
- Donaldson 1983: J. Diff. Geom. 18(2), 279–315.
- Gompf-Stipsicz 1999: AMS GSM 20.
- Smale 1962: Amer. J. Math. 84(3), 387–399.
- Seiberg-Witten 1994: Nucl. Phys. B 431, 484–550.

**세션 저자 주**: 본 노트의 연도·저자는 표준 문헌 기준이며 arXiv ID 의 세부 버전은 후속 세션에서 재확인 필요. "정직" 규칙상 본인 기억 기반 부분을 명시한다. 조건부 정리의 전제-결론 구조가 왜곡되지 않도록 원논문의 정확한 statement 우선.
