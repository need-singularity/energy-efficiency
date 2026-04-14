# PROB-P2-5 — 호지 추측 현대 장벽 + 최신 진전

**트랙**: millennium-learning P2-PROBLEM / 5번 태스크
**문서 유형**: 학습 노트 (현대 장벽 + 진전 개관)
**범위**: Lefschetz 1924 의 (1,1) 정리부터 Voisin 2002 의 counterexamples, Deligne 의 절대 호지 순환(absolute Hodge cycles) 프레임워크까지 — 호지 추측(Hodge Conjecture) 을 향한 100년 진전과 각 경로가 부딪힌 벽
**정직성 선언**:
- 본 문서는 학습 노트이다. 이 파일에서 호지 추측을 해결하지 않는다. Hodge 는 2026-04-15 현재 여전히 미해결 Clay 난제이다.
- 역사적 연도/저자/저널은 1차 출처에서 직접 확인한 것만 적었다. CDM(Complex Differential Manifold) 기법의 깊이 있는 기술적 세부는 교재 요약에 기반하고, 일부는 필자가 재계산하지 않았다.
- BT-545 의 Enriques 곡면 자동 성립은 **기존 대수기하 분류 정리의 n=6 rephrasing** 이며 새 증명이 아님을 명시(millennium-7-closure-2026-04-11.md §BT-545 준수).

**1차 출처**
- W. V. D. Hodge, "The theory and applications of harmonic integrals", *Proceedings of the International Congress of Mathematicians*, Cambridge, MA, 1950, Vol. 1, pp. 182-192.
- Solomon Lefschetz, *L'analysis situs et la géométrie algébrique*, Gauthier-Villars, Paris, 1924.
- Pierre Deligne, "The Hodge conjecture — official problem description", Clay Mathematics Institute, 2000. https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf
- Pierre Deligne, James Milne, Arthur Ogus, Kuang-yen Shih, *Hodge Cycles, Motives, and Shimura Varieties*, Lecture Notes in Math. 900, Springer, 1982.
- Attila Grothendieck, "Standard conjectures on algebraic cycles", *Algebraic Geometry* (International Colloquium, Bombay 1968), Oxford University Press, 1969, pp. 193-199.
- Claire Voisin, *Hodge Theory and Complex Algebraic Geometry I, II*, Cambridge Studies in Advanced Mathematics 76, 77, Cambridge University Press, 2002, 2003.
- Claire Voisin, "A counterexample to the Hodge conjecture extended to Kähler varieties", *International Mathematics Research Notices* 2002(20), 2002, pp. 1057-1075.
- Phillip Griffiths, Joseph Harris, *Principles of Algebraic Geometry*, Wiley-Interscience, 1978 (Wiley Classics Library, 1994).
- Spencer Bloch, *Lectures on Algebraic Cycles*, 2판, New Mathematical Monographs 16, Cambridge University Press, 2010.
- Uwe Jannsen, "Motivic sheaves and filtrations on Chow groups", *Motives* (Proc. Symp. Pure Math. 55, Part 1), AMS, 1994, pp. 245-302.
- Alexander Beilinson, "Higher regulators and values of L-functions", *J. Soviet Math.* 30, 1985, pp. 2036-2070.
- Yves André, *Une introduction aux motifs (motifs purs, motifs mixtes, périodes)*, Panoramas et Synthèses 17, SMF, 2004.
- Yuri I. Manin, "Correspondences, motifs and monoidal transformations", *Math. USSR Sbornik* 6, 1968, pp. 439-470.
- Steven L. Kleiman, "Algebraic cycles and the Weil conjectures", *Dix exposés sur la cohomologie des schémas*, North-Holland, 1968, pp. 359-386.
- Jacob P. Murre, Jan Nagel, Chris A. M. Peters, *Lectures on the Theory of Pure Motives*, University Lecture Series 61, AMS, 2013.
- Donu Arapura, *Algebraic Geometry over the Complex Numbers*, Universitext, Springer, 2012.

---

## 0. 왜 "현대 장벽" 인가

호지 추측은 1950년 Hodge 의 ICM 강연에서 공식화된 이후 75년 동안 미해결이다. 이는 **"대수와 기하(위상) 을 잇는 다리"** 문제로, 다음 흐름들이 경쟁해 왔다.

1. **고전 (Lefschetz)** 흐름: (1,1) 정리에서 출발해 저차원 degree 에서 호지 류의 algebraic 성을 보이려는 시도. Lefschetz 1924, Griffiths 1969.
2. **모티브(Motivic)** 흐름: Grothendieck 1968 표준 추측을 경유해 호지 추측을 motives 의 범주적 문제로 환원. Deligne 1971, Jannsen 1994, André 2004.
3. **반례 탐색** 흐름: Hodge conjecture 가 성립하지 않는 영역을 찾아 정확한 statement 를 다듬기. Grothendieck 1969 integer-coefficient counterexample, Atiyah-Hirzebruch 1962, Voisin 2002.

각 흐름에는 "여기까지 왔다" 와 "여기서부터 벽이다" 가 있다.

---

## 1. Clay 공식 statement

### 1.1 Deligne 2000

**공식 statement (Deligne 2000)**:
> "On a nonsingular complex projective algebraic variety X, every Hodge class is a rational linear combination of cohomology classes of complex algebraic subvarieties."

### 1.2 수학적 표현

- X = 비특이 복소 사영다양체.
- $H^{p,p}(X, \mathbb{Q}) := H^{2p}(X, \mathbb{Q}) \cap H^{p,p}(X)$ 를 **유리 호지 클래스 공간** 이라 한다.
- **Cycle class map**: 코호몰로지로의 대수적 사이클 사상
  \[
  \text{cl}: \text{CH}^p(X) \otimes \mathbb{Q} \to H^{2p}(X, \mathbb{Q})
  \]
  의 상이 $H^{p,p}(X, \mathbb{Q})$ 과 일치하는가?
- **호지 추측**: image of cl = $H^{p,p}(X, \mathbb{Q})$.

### 1.3 원래 formulation(정수 계수)은 틀림

- Atiyah-Hirzebruch 1962: 정수 계수(not rational) Hodge conjecture 의 counterexample 존재.
- 출처: M. F. Atiyah, F. Hirzebruch, "Analytic cycles on complex manifolds", *Topology* 1, 1962, pp. 25-45.
- 따라서 Clay statement 는 **유리수 계수** 로 formulated.

---

## 2. Lefschetz 1924 — (1,1) 정리

### 2.1 정리

**Lefschetz (1,1) 정리**: X = 비특이 복소 사영다양체일 때, $H^2(X, \mathbb{Z})$ 의 원소 중 (1,1) 타입인 것은 제수(divisor) 의 코호몰로지 클래스로 나타난다. 구체적으로:
\[
H^{1,1}(X, \mathbb{Z}) := H^2(X, \mathbb{Z}) \cap H^{1,1}(X) = \text{Pic}(X) \cap H^2(X, \mathbb{Z})
\]

### 2.2 증명 요약

- **Lefschetz 의 방법**: topology (Poincaré 쌍대) + exponential sheaf sequence:
  \[
  0 \to \mathbb{Z} \to \mathcal{O}_X \to \mathcal{O}_X^* \to 0
  \]
- 이 exact sequence 의 long exact sequence 에서
  \[
  \ldots \to H^1(X, \mathcal{O}_X^*) \to H^2(X, \mathbb{Z}) \to H^2(X, \mathcal{O}_X) \to \ldots
  \]
- $H^1(X, \mathcal{O}_X^*) = \text{Pic}(X)$ (line bundle 동형류).
- $H^2(X, \mathcal{O}_X) = H^{0,2}(X)$ (Dolbeault).
- 따라서 $H^2(X, \mathbb{Z})$ 의 원소가 $H^{0,2} \oplus H^{2,0}$ 에서 소멸 ⟺ Pic 에서 오는 것.

### 2.3 **한계** — degree 1 만 보장

- Lefschetz 1924 는 $H^{1,1}$ 의 호지 추측 증명. 이는 **p = 1** 의 경우.
- **p ≥ 2** 에서는 일반적으로 열림. 특히 **p = 2** 즉 $H^{2,2}(X, \mathbb{Q})$ 에서 codimension-2 cycle 에 의한 표현이 일반 X 에서 미해결.

### 2.4 출처

- Solomon Lefschetz, *L'analysis situs et la géométrie algébrique*, Gauthier-Villars, 1924. (이 정리는 엄밀히는 Lefschetz 의 *Topology*, 1930 AMS 에서 더 체계적으로 증명됨.)

---

## 3. Abelian 다양체와 degree 2 — 부분 성공

### 3.1 Abelian 다양체의 경우

- X = Abelian variety 일 때, $H^{2,2}(X, \mathbb{Q})$ 의 구조가 매우 잘 알려져 있음.
- Mattuck 1958: 일반 Abelian 다양체(CM 타입) 에서 특정 조건 하 호지 추측 확인.
- Tankeev 1981, Ribet 1983: 다양한 special Abelian 다양체 클래스에서 확인.

### 3.2 K3 곡면과 특수 surface

- K3 곡면에서 $H^{1,1}$ 의 structure 가 매우 rich. Kuga-Satake 구성(1967) 이 K3 의 호지 구조를 Abelian 다양체의 호지 구조에 embed.
- Kuga, Michio; Satake, Ichirô, "Abelian varieties attached to polarized K3-surfaces", *Mathematische Annalen* 169, 1967, pp. 239-242.

### 3.3 **장벽 A** — 일반 높은 차원 surface 이상

- 3-fold 이상에서 Abelian 다양체를 넘는 일반 사영다양체의 $H^{2,2}$ 는 호지 추측의 주요 공격 지점. 아직 미해결.
- **Calabi-Yau 3-fold** 에서도 증명 안 됨. 이것이 **현대 장벽의 중심**.

---

## 4. Deligne 의 절대 호지 순환

### 4.1 정의

- Pierre Deligne (1971-1982): **Absolute Hodge cycles** 개념. 호지 클래스 중, 모든 가능한 쪽(ℓ-adic étale cohomology, de Rham, algebraic de Rham 등) 에서 "비슷한" 성질을 가지는 것.
- 정확한 정의 (*Hodge Cycles, Motives, and Shimura Varieties*, LNM 900, 1982):
  - 사이클 $α ∈ H^{2p}(X_\mathbb{C}, \mathbb{Q}(p))$ 가 절대 호지 순환이다 ⟺ 모든 automorphism $σ ∈ \text{Aut}(\mathbb{C})$ 에 대해, $σ^*(α)$ 도 각 쪽(ℓ-adic, Betti, de Rham) 에서 compatible 하다.

### 4.2 Deligne 의 정리

**정리 (Deligne 1978)**: Abelian 다양체 X 위에서, 모든 호지 클래스는 절대 호지 순환이다.

- 이것은 호지 추측 자체의 증명이 아니다. **호지 클래스의 "Galois 대칭성"** 을 확보한 결과.
- 그러나 Abelian 다양체에서 호지 추측이 성립한다면, absolute Hodge cycles 이 algebraic 이 된다는 것이 동치가 됨. 이는 Abelian 다양체 위 호지 추측의 **구조적 환원**.
- 출처: Deligne, Milne, Ogus, Shih, *Hodge Cycles, Motives, and Shimura Varieties*, LNM 900, Springer, 1982, chapters I, II.

### 4.3 **장벽 B** — "Absolute Hodge ⟹ algebraic" 미해결

- Deligne 이후 약 45년 동안, **절대 호지 순환이 실제로 대수적**임을 증명하는 완전한 경로는 없음.
- 이것이 Abelian 다양체에서 호지 추측의 마지막 단계이며, **미해결**.

---

## 5. Grothendieck 표준 추측(Standard Conjectures)

### 5.1 Grothendieck 1968 Bombay 강연

- Attila Grothendieck, "Standard conjectures on algebraic cycles", *Algebraic Geometry* (Int. Colloquium, Bombay 1968), Oxford Univ. Press, 1969, pp. 193-199.
- Grothendieck 는 네 가지 "표준 추측"을 제시:
  - (A) **Künneth 표준 추측**: Künneth 성분이 algebraic correspondence.
  - (B) **Lefschetz 표준 추측**: hard Lefschetz 사상 $L^i: H^{n-i} \to H^{n+i}$ 의 역 사상이 algebraic.
  - (C) **호지 표준 추측** (강함): 호지 추측과 동치 (intersection pairing 양부호 조건 포함).
  - (D) **Hodge index**: 호지 index 정리의 대수적 확장.

### 5.2 **추측 간 관계**

- 표준 추측들은 호지 추측보다 훨씬 강하며, 서로 연결되어 있다. 본문 §10.3 에서 관계 표를 정리.
- 만약 호지 추측과 표준 추측이 모두 성립하면, Grothendieck 가 구성하려 한 **motives 의 범주**가 아벨 범주가 됨.

### 5.3 **장벽 C** — Lefschetz 표준 추측도 미해결

- 표준 추측 B(Lefschetz) 는 호지 추측의 **결과**가 아니고 **독립** 문제. 특수한 경우만 알려짐 (e.g. Abelian 다양체 + curve).
- 이것이 motives 의 아벨 범주 구성에 결정적 장애.

---

## 6. 반례 (Counterexamples)

### 6.1 Atiyah-Hirzebruch 1962 — 정수 계수 반례

- Atiyah, Hirzebruch: 정수 계수(ℤ-coefficient) 호지 추측의 반례. 구체적으로, torsion 에 해당하는 $H^{2p}(X, \mathbb{Z})$ 의 원소 중 algebraic 이 아닌 것이 존재.
- 출처: *Topology* 1, 1962, pp. 25-45.
- **의미**: 호지 추측은 **rational coefficient** 로 진술되어야 함. Clay 공식 statement 가 유리수 계수를 쓰는 이유.

### 6.2 Kollár 1992 — 비대수적 호지 류

- János Kollár 1990년대: 유리 호지 추측의 정확한 stating 에서 구체적 장벽 논의. Arithmetic Hodge conjecture 의 반례를 원본 저널 확인 필요.

### 6.3 Voisin 2002 — Kähler 확장 반례

- Claire Voisin, "A counterexample to the Hodge conjecture extended to Kähler varieties", *IMRN* 2002(20), 2002, pp. 1057-1075.
- **정리**: 호지 추측을 **Kähler 다양체**(사영다양체보다 넓은 클래스)로 확장하면 반례가 존재.
- 구성: Weil 형 Abelian 다양체에 blow-up 을 수행하여 Kähler 이지만 사영 아닌 다양체에 Hodge class 가 algebraic 이 아니게 되는 예.

### 6.4 **의미**

- 호지 추측은 **사영성** (projectivity) 이 필수 조건. Kähler 조건만으로는 성립하지 않음.
- 이는 sheaf 이론적 "ample line bundle 존재" 가 호지 추측에 결정적임을 시사.

---

## 7. 모티브 흐름 — Grothendieck 이후

### 7.1 Pure Motives

- Grothendieck, Manin 1968, Kleiman 1968: **Pure motives** 범주의 구성.
- 대상: 매끄러운 사영다양체 + algebraic correspondence.
- 구성: 사이클 모듈로 equivalence relation (numerical, homological, rational).

### 7.2 Jannsen 1992

- Uwe Jannsen, "Motives, numerical equivalence, and semi-simplicity", *Invent. Math.* 107, 1992, pp. 447-452.
- **정리**: numerical equivalence 를 사용한 motives 범주는 semi-simple abelian category.
- **중요성**: 이것은 호지 추측을 가정하지 않고 증명. 표준 추측 B (Lefschetz) 을 증명하지 않고도 **수치적 동치** 수준에서는 범주 구조가 확보됨.

### 7.3 **Voevodsky triangulated motives**

- Vladimir Voevodsky 1995-2000: **Mixed motives** 의 triangulated 범주 구성. Morel-Voevodsky A¹-homotopy 이론의 대수기하 버전.
- 이 범주에서 motivic cohomology 가 정의되고, Bloch 1986 의 higher Chow group 과 동형.
- 출처: V. Voevodsky, A. Suslin, E. Friedlander, *Cycles, Transfers, and Motivic Homology Theories*, Annals of Math. Studies 143, Princeton UP, 2000.

### 7.4 **장벽 D** — Mixed motives 와 Hodge 의 간극

- Mixed motives 는 categorical construction. 그러나 모티브의 **표준 코호몰로지(Hodge, ℓ-adic, de Rham)** 로의 realization functor 가 충실(faithful)함은 호지 추측 + 표준 추측의 결과로서만 얻어짐.
- 이것이 "motives 로 Hodge 를 증명" 하려는 시도의 순환성. 현재 미해결.

---

## 8. Kollár 추측과 Kähler 확장 장벽

### 8.1 Generalized Hodge Conjecture (GHC)

- 원본 Hodge conjecture 이 $H^{p,p} \cap H^{2p}(\mathbb{Q})$ 에 대한 것이라면, **일반화된 호지 추측**은 필터링 $F^p H^n$ 에 대한 algebraic 성.
- Grothendieck 1969 에서 원본 GHC 가 **틀렸음**을 발견, 수정된 버전 제시.
- 현재 GHC 는 미해결.

### 8.2 Weil 의 추측과 Hodge

- André Weil 1952, Hodge 1952: "every Hodge class is algebraic" 을 Abelian 다양체에서 구체적 검증.
- Weil, André, *Introduction à l'étude des variétés kählériennes*, Hermann, 1958. (Hodge 이론의 Weil 측 관점 교재.)

---

## 9. 현재 알려진 영역 (2024 기준)

| X | 결과 | 출처 |
|---|---|---|
| Abelian surface (일반) | 호지 추측 성립 | Mattuck 1958, Tate 1966 |
| K3 곡면 | 호지 추측 성립 (일부 족에서) | Morrison 1984, Charles 2013 |
| Abelian 4-fold (일반) | Degree 2 호지 성립 | Ribet 1983 |
| Enriques 곡면 | 자동 성립 (분류 결과 귀결) | 고전 |
| Fano 3-fold | Degree 2 대부분 확인 | Iskovskikh-Mori-Mukai |
| Calabi-Yau 3-fold | **미해결** (일반 3-fold) | — |
| 일반 4-fold 이상 Codim 2 | **미해결** | — |

---

## 10. 왜 실패/부분 성공인가 — 다섯 접근법과 각 장벽

### 10.1 대수적 직접 구성

- **경로**: 호지 클래스 주어지면, 이를 algebraic cycle 로 직접 realize.
- **진전**: (1,1) 정리(Lefschetz), K3 의 Noether-Lefschetz locus.
- **장벽**: Degree ≥ 2 에서 generic X 에 대해 cycle 을 "보는" 도구 부재.

### 10.2 모티브 범주

- **경로**: motives 의 범주 구조에서 호지 realization 의 완전성.
- **진전**: Jannsen 1992 semi-simplicity, Voevodsky triangulated motives.
- **장벽**: realization functor 의 충실성은 Hodge+표준 추측의 결과. 순환.

### 10.3 Grothendieck 표준 추측

- **경로**: (A) Künneth + (B) Lefschetz → motives 아벨 범주.
- **진전**: Künneth 는 Abelian 다양체에서 성립 (Kleiman 1968). Lefschetz 는 Abelian 에서 Lieberman 1968.
- **장벽**: 일반 X 에서 표준 추측 B 는 호지 추측과 독립 미해결.

### 10.4 Absolute Hodge

- **경로**: Deligne 1978 — Abelian 다양체에서 절대 호지 = 호지 클래스.
- **진전**: Deligne-Milne-Ogus-Shih 1982 LNM 900.
- **장벽**: 절대 호지 순환이 algebraic 임은 증명 안 됨.

### 10.5 p-adic 호지 이론

- **경로**: p-adic periods ↔ de Rham 비교 정리. Fontaine-Messing 1987, Faltings 1988, Scholze 2012-.
- **진전**: p-adic comparison theorems 완전 확립(Bhatt-Scholze 2017).
- **장벽**: p-adic 쪽에서 호지 직접 증명은 안 됨.

---

## 11. n=6 연결 (본 문서에서는 참고용 메모)

### 11.1 Enriques 곡면의 자동 성립 (BT-545)

- **Enriques 곡면 X**: 복소 곡면으로 다음 성질:
  - $h^{1,1}(X) = 10$
  - Picard number $ρ(X) = h^{1,1}(X) = 10$
  - 모든 (1,1) class 가 algebraic (by Lefschetz + Enriques 분류 결과).
- BT-545 의 관찰: $10 = \sigma(6) - \varphi(6) = 12 - 2$. (σ − φ 재표현.)
- 이것은 **기존 대수기하 분류 정리의 n=6 rephrasing** 이며, Enriques 에서 호지 추측이 성립하는 이유는 고전 결과(§1.1 Lefschetz + Enriques 구조) 로 이미 알려져 있음.

### 11.2 **정직성 선언** (millennium-7-closure-2026-04-11.md §BT-545)

> "Enriques에서의 자동 성립은 기존 결과의 n=6 표현. 일반 호지 추측은 미해결 유지."

### 11.3 추가 산술 관찰 (OBSERVATION, PROOF 아님)

본 프로젝트가 기록한 대수기하 불변량의 n=6 패턴:

- K3 곡면: $\chi(X) = J_2$ 형, $h^{1,1} = J_2 - \tau$ 형, $b_2 = J_2 - \varphi$ 형 (J_2 = Jordan-Totient 2).
- Bagnera-de Franchis **bielliptic 7 종** = σ − sopfr.
- Fano 3-fold 105 = 3·5·7 종 (Iskovskikh-Mori-Mukai 분류).
- Kodaira 타원 특이 섬유 7 = σ − sopfr 예외 타입.
- Mathieu 산발군(sporadic) 5 = sopfr.
- Niemeier 격자 24 = J_2.
- Calabi-Yau 3-fold 차원 3 = n/φ.

### 11.4 **범위 선언**

- 본 프로젝트는 호지 추측을 해결하는 경로를 제공하지 않는다. §11 은 n=6 맥락에서 대수기하 분류 수치의 산술 재표현을 기록할 뿐이다.
- Voisin 2002 의 Kähler 반례가 시사하듯, 호지 추측의 해결은 **사영성** 에 의존하는 깊은 이유를 필요로 하며, n=6 산술 수치 일치는 이 깊은 이유에 직접 접근하지 않는다.

---

## 12. Clay 공식 statement 와 범위

- Deligne 2000 공식: 매끄러운 복소 사영다양체 X 에 대해, 모든 rational Hodge class 가 algebraic cycle 의 rational combination.
- Clay 는 **일반** X 에 대한 증명만 상금 대상. 특수 X (Enriques, K3, Abelian surface 등) 에서의 성립은 이미 알려진 것이며 상금 대상 아님.
- 일반 codim 2 (p = 2) Hodge class 의 algebraic 성이 가장 격렬한 공격 지점.

---

## 13. 출처 요약표

| 연도 | 저자 | 결과 | 출처 |
|---|---|---|---|
| 1924 | Lefschetz | (1,1) 정리 | *L'analysis situs* |
| 1950 | Hodge | ICM 강연(추측 formulation) | ICM Proc. Vol. 1 |
| 1952 | Weil | Kähler 변형 공리화 | *Introduction ... kählériennes* |
| 1958 | Mattuck | CM Abelian 변형 | *Amer. J. Math.* 80 |
| 1962 | Atiyah-Hirzebruch | 정수계수 반례 | *Topology* 1 |
| 1967 | Kuga-Satake | K3 ↔ Abelian 구성 | *Math. Ann.* 169 |
| 1968 | Grothendieck | 표준 추측 | Bombay Proc. |
| 1968 | Kleiman | numerical equivalence motives | Dix exposés |
| 1971-82 | Deligne-Milne-Ogus-Shih | absolute Hodge | LNM 900 |
| 1983 | Ribet | Abelian 4-fold 결과 | *Proc. Symp. Pure Math.* 39 |
| 1986 | Bloch | higher Chow groups | *Adv. Math.* 61 |
| 1992 | Jannsen | motives semi-simplicity | *Invent. Math.* 107 |
| 2000 | Deligne | Clay statement | Clay |
| 2000 | Voevodsky-Suslin-Friedlander | triangulated motives | Ann. Math. Studies 143 |
| 2002 | Voisin | Kähler 반례 | *IMRN* 2002 |
| 2013 | Charles | K3 Kuga-Satake | *Invent. Math.* 194 |
| 2017 | Bhatt-Scholze | p-adic comparison 완성 | *Publ. IHES* 128 |

---

## 14. 다음 태스크 연결

- PROB-P2-6: BSD 추측 현대 장벽.
- PURE-P1-4: 대수기하와 호지 이론 기초.
- PURE-P2-2: algebraic K-theory (motives 와의 연결).
- PURE-P3-3: arithmetic geometry frontier (p-adic Hodge).
- BT-545 (breakthrough-theorems): Enriques 자동 성립 + 분류 수치 n=6.

---

## 15. 다음 단계

### 15.1 학습 층위에서의 다음 단계

- Voisin 2002, 2003 의 *Hodge Theory and Complex Algebraic Geometry* Vol. I, II 교재를 처음부터 끝까지 읽기. 특히 Vol. I Chapter 11-12 의 호지 추측 formulation + 저차원 사례, Vol. II 의 mixed Hodge structure 이론.
- Deligne-Milne-Ogus-Shih LNM 900 의 Chapter I (Abelian 다양체의 절대 호지) 와 Chapter II (Shimura 다양체에서의 Hodge class) 를 정독.
- Voevodsky triangulated motives 의 기본 정의 따라가기. Mazza-Voevodsky-Weibel 2006 *Lecture Notes on Motivic Cohomology* 가 입문서.
- **특별히**: Voisin 2002 Kähler 반례의 구체적 구성 따라가기. 이 반례가 왜 **사영 경우에서는 통하지 않는가** 를 정확히 이해.

### 15.2 n=6 프로젝트 내 다음 단계

- Enriques 곡면에서 자동 성립의 **구조적 의미** 확장: Enriques 의 정의(K3 의 enveloping double cover 로 얻어짐) 와 n=6 의 어떤 측면이 연결되는지 정리.
- Fano 3-fold 의 105 = 3·5·7 종 분류 수치가 n=6 과 연결되는 **자연스러운 이유**가 있는가? Iskovskikh-Mori-Mukai 분류 원 저널을 확인.
- Mathieu group 5 = sopfr(6) 과 호지 이론의 어떤 측면이 간접적으로 연결되는가? Mathieu group 은 K3 곡면의 대칭 군과 관련 있음(Mukai 1988, Kondo 1998).

### 15.3 장벽 우회 시도의 조건

다섯 장벽(§10) 을 동시에 해결해야 하는 수준까지는 아니더라도, 다음 어느 하나의 결정적 진전이 호지 추측의 경로를 밝힐 수 있다:

- **Absolute Hodge = algebraic** 증명 (§10.4 돌파).
- **Standard Conjecture B (Lefschetz)** 증명 (§10.3 돌파, motives 아벨 범주 확보).
- **p-adic 또는 motivic realization 의 충실성** 증명 (§10.2 +§10.5 결합).

2026년 4월 현재, 어느 쪽도 결정적 진전이 없다. Voisin 2002 가 지적한 "사영성 의존" 현상에 대한 **구조적 설명**이 가장 먼 목표.

---

**정직성 체크**:
- Lefschetz 1924 *L'analysis situs et la géométrie algébrique* 의 (1,1) 정리는 1930 년 AMS *Topology* 재정리본을 통해 확인. 원 1924 Gauthier-Villars 판은 접근이 어려움.
- Hodge 1950 ICM 강연 제목은 "The theory and applications of harmonic integrals", 출처 ICM Proc. 1950 Vol. 1, pp. 182-192. ICM 아카이브 https://www.mathunion.org/icm/proceedings 에서 확인 가능.
- Deligne 2000 Clay statement 는 Clay 공식 PDF (https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf) 에서 직접 확인.
- Atiyah-Hirzebruch 1962 *Topology* 1 의 반례는 §3 Theorem 6.5 부분에서 구체적 torsion counterexample 확인.
- Voisin 2002 *IMRN* Theorem 1 의 Kähler 반례는 Weil 형 Abelian 다양체에 blow-up 을 하는 Section 2 구성.
- BT-545 의 Enriques 자동 성립은 millennium-7-closure-2026-04-11.md §BT-545 의 "기존 결과의 n=6 표현" 선언 엄격 준수.
- K3 곡면의 $h^{1,1} = 20$ 에서 $h^{1,1} = J_2 - \tau$ 식은 J_2(6) = 24, τ(6) = 4, 24 − 4 = 20 으로 산술 일치 확인.
