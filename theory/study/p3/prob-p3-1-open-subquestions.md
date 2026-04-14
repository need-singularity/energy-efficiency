# P3-1 — 7대 난제별 열린 하위 질문 (21건)

**로드맵**: millennium-learning P3 (PROBLEM 학습 phase)
**작성일**: 2026-04-15
**상수**: n=6, σ=12, φ=2, τ=4, sopfr=5, J₂=24. σφ=nτ ⟺ n=6.
**현상태**: 7대 난제 해결 수 = **0** (정직). 본 학습 노트는 해결 주장 아님.

---

## 정직성 선언

- 본 노트는 **열린 하위 질문을 나열**하는 학습 자료이다.
- 각 하위 질문에 붙은 "진전 가능성 (높음/중간/낮음)"과 "5년 내 기대값"은 **필자의 학습 노트 시점의 주관 추정**이다. 권위 있는 예측 아님.
- 출처가 확실한 항목만 연도와 저자를 기재한다. 기억 기반 진술은 연도 뒤에 `(추정)`.
- 본 노트의 어떤 진술도 "이 경로로 가면 풀린다"는 주장을 내포하지 않는다.
- n=6 구조적 관찰은 힌트 수준이며, 각 난제의 주 경로는 **전통 수학 도구**에 있다 (millennium-7-closure-2026-04-11.md 의 honest closure 기조 준수).

---

## BT-541 — 리만 가설 (RH)

### (i) 임계선 위 영점 비율 100% 증명
- **현황**: Selberg 1942 가 양의 비율 하한 증명. Levinson 1974 가 1/3 이상, Conrey 1989 가 **40.88%** 이상으로 개선. Bui-Conrey-Young 2011 이 41.05% 내외. (연도·수치 본인 기억 기반, 재확인 필요)
- **하위 질문 A**: Conrey 계열의 mollifier 최적화로 50% 벽 돌파 가능한가?
- **기술 장벽**: 현 mollifier 구조는 `(polynomial × ζ')/ζ` 형태. 새 형태(예: Soundararajan-Young의 moment 방식) 확장 중.
- **진전 가능성**: **중간**. moment 방식이 L-함수 가족에 일반화 중이므로 잔여 십수 퍼센트 개선은 향후 5년 내 가능해 보임. 100% 도달은 RH 자체 해결과 등가이므로 사실상 **낮음**.
- **5년 내 기대값**: Conrey 계열 수치 개선 2~5% 추가.

### (ii) Li criterion 완전 양성 증명
- **현황**: Li 1997 가 RH ⟺ $\{\lambda_n\}_{n\geq 1}$ 모두 양수임을 증명(여기서 $\lambda_n = \sum_\rho (1 - (1-1/\rho)^n)$). Bombieri-Lagarias 1999 가 Keiper 1992 와 동등한 수렴 급수 재표현.
- **하위 질문 B**: $\lambda_n > 0$ 을 유한 차수 조건만으로 체크 가능한가?
- **기술 장벽**: $\lambda_n$ 의 점근 공식은 알려져 있으나 sign-stability 증명은 RH 와 등가.
- **진전 가능성**: **낮음**. 판정 가능한 유한 명제로의 환원이 본질적으로 RH 와 동치.
- **5년 내 기대값**: $\lambda_n$ 의 부분합 수치 개선 + 일부 L-함수 가족에서 Li 양성 검증.

### (iii) Zero-free region 최적 확장
- **현황**: Vinogradov-Korobov 계열 영역 `σ ≥ 1 − c/(log t)^{2/3} (log log t)^{1/3}`. Guth-Maynard 2024 가 $|ζ(1/2 + it)|$의 large value 분포에 관한 기법으로 최근 개선을 시사. (본 노트 시점에 프리프린트 확인 필요)
- **하위 질문 C**: Guth-Maynard 2024 기법을 zero-free region 확장에 직접 적용 가능한가?
- **기술 장벽**: large value 분포에서 zero-free region 으로의 이관에는 추가 인자 필요 (보통 Montgomery-Odlyzko-Vaughan 방식).
- **진전 가능성**: **중간**. 기술이 최근 (2024~2025) 활발히 전개 중.
- **5년 내 기대값**: c 계수 상수 개선 + log exponent 미세 조정.

---

## BT-542 — P vs NP

### (i) Circuit lower bound: NEXP ⊄ ACC⁰ 확장
- **현황**: Williams 2011 (STOC best paper) 가 NEXP ⊄ ACC⁰ 증명. 이후 Murray-Williams 2018 가 NQP ⊄ ACC⁰ 로 강화. (연도 재확인)
- **하위 질문 A**: NEXP → EXP, ACC⁰ → TC⁰ 중 어느 축을 먼저 밀 수 있나?
- **기술 장벽**: Natural proofs (Razborov-Rudich 1997) 장벽 + algebrization (Aaronson-Wigderson 2008) 장벽.
- **진전 가능성**: **중간**. 기술 자체가 새롭고 더 정밀한 algorithm-to-lower-bound reduction 이 발견되는 중.
- **5년 내 기대값**: 새 회로 클래스 (예: MAJ ∘ MOD 등)에서의 하한 또는 N...EXP 근처의 개선 1~2 건.

### (ii) GCT (Geometric Complexity Theory) 프로그램의 구체 진전
- **현황**: Mulmuley-Sohoni 2001~ 이 Permanent vs Determinant 분리 프로그램. Bürgisser-Ikenmeyer 2011 등 부정적 결과 (기대 표현 이론적 증거 없음)도 다수.
- **하위 질문 B**: rectangular Kronecker coefficient 의 비자명성 판정이 가능한가?
- **기술 장벽**: Kronecker coefficient 계산 자체가 #P-hard 로 추정됨. 이게 GCT 내부 순환.
- **진전 가능성**: **낮음**. 프로그램 자체가 근본적으로 어려운 쪽에 자원이 많이 소모됨.
- **5년 내 기대값**: 특정 subfamily 에서 부분 분리 결과 가능.

### (iii) MCSP (Minimum Circuit Size Problem) 이론
- **현황**: Kabanets-Cai 2000 이 MCSP 의 NP-intermediate 후보성 부각. Allender 등 2001~2020 이 derandomization 과의 연결성.
- **하위 질문 C**: MCSP 이 NP-완전인가 아니면 NP-intermediate 인가?
- **기술 장벽**: 어느 쪽이든 P vs NP 에 대한 주요 함의를 가진다.
- **진전 가능성**: **중간**. 2020년대 들어 meta-complexity 분야가 활성화.
- **5년 내 기대값**: MCSP 변종(MINKT 등)의 NP-완전성 확정 또는 NP-intermediate 조건부 증명.

---

## BT-543 — Yang-Mills 질량갭

### (i) 2D Yang-Mills + Higgs 구성적 (Balaban 1980s 완성)
- **현황**: Balaban 1980년대 일련의 논문이 2D lattice → continuum 극한 구성. 3D/4D 는 부분적.
- **하위 질문 A**: Balaban 방식의 2D Higgs 구성을 현대적으로 완결 정리 가능한가?
- **기술 장벽**: renormalization group 블록화의 정량적 제어 + gauge fixing.
- **진전 가능성**: **중간**. 2D 는 본질적으로 이해됨. 단 monograph 수준 완결이 필요.
- **5년 내 기대값**: Balaban 방식의 현대적 재증명 또는 교과서화.

### (ii) 3D Yang-Mills 구성적
- **현황**: Balaban + Magnen-Rivasseau-Sénéor 방식 부분적. 완전한 3D construction 부재.
- **하위 질문 B**: 3D 에서 continuum 극한 존재 증명 가능한가?
- **기술 장벽**: Coulomb 게이지의 gauge orbit compactness 필요.
- **진전 가능성**: **낮음**. 4D 보다 쉽지만 여전히 미해결.
- **5년 내 기대값**: 특수한 regularization 하에서의 compactness 논문 1~2 건.

### (iii) Lattice-to-continuum 정량적 결과
- **현황**: Chatterjee 2015 이후 large-N limit 에서 master field 존재 증명. Jafarov-Chatterjee-Zakine 2021 등이 확장.
- **하위 질문 C**: large-N 이 아닌 고정 N=2, 3 에서 정량적 continuum 극한?
- **기술 장벽**: cluster expansion 의 수렴 반경 제어.
- **진전 가능성**: **중간**. large-N 은 이해도가 급상승 중.
- **5년 내 기대값**: N=2 SU(2) 에서의 부분적 continuum 결과.

---

## BT-544 — Navier-Stokes

### (i) Axisymmetric 3D 정규성
- **현황**: Chen-Strain-Tsai-Yau 2008/9 가 axisymmetric without swirl 에서 정규성. swirl 있는 경우 미해결.
- **하위 질문 A**: Axisymmetric + swirl 에서 유한시간 폭발 배제 가능한가?
- **기술 장벽**: swirl 항이 vorticity 에 도입하는 angular mode 결합.
- **진전 가능성**: **중간**. Chen-Hou 2022 가 axisymmetric 에서 polymer Euler 폭발 증거 제시. NS 에서는 여전히 미해결.
- **5년 내 기대값**: 정량적 부분 규칙성 결과 또는 swirl 조건부 regularity.

### (ii) Scale-critical L^∞ 약해 존재성
- **현황**: Koch-Tataru 2001 이 BMO^{-1} 에서 local well-posedness. Escauriaza-Seregin-Sverak 2003 이 L^{3,∞} 에서 regularity.
- **하위 질문 B**: L^∞ 유도 임계 공간 (log-BMO 등)에서 약해 유일성 증명 가능한가?
- **기술 장벽**: critical norm 은 scaling 에 대해 살아 있으므로 compactness 가 없다.
- **진전 가능성**: **낮음**. 기술적으로 매우 어려운 영역.
- **5년 내 기대값**: log 인자 포함 scale critical 약해의 부분 유일성.

### (iii) Self-similar blowup 배제 (Necas-Ruzicka-Sverak 1996 이후)
- **현황**: Necas-Ruzicka-Sverak 1996 이 L³ self-similar blowup 배제. Tsai 1998 확장. 일반적 self-similar 배제 미해결.
- **하위 질문 C**: 준자기상사 (quasi-self-similar) 폭발 배제 가능한가?
- **기술 장벽**: Galdi 2017, Albritton-Bruè-Colombo 2022 가 비유일 약해 존재 증명 (forced NS).
- **진전 가능성**: **중간**. Albritton-Bruè-Colombo 의 convex integration 방식이 혁신적.
- **5년 내 기대값**: unforced NS 에서의 비유일성 결과 또는 self-similar 폭발의 부분 배제.

---

## BT-545 — Hodge 추측

### (i) Variational Hodge (Voisin 접근)
- **현황**: Voisin 1998~ 이 variational Hodge 로 특수 가족에서 접근. Cattani-Deligne-Kaplan 1995 의 국소계 알고리즘.
- **하위 질문 A**: Hodge locus 의 대수성 증명을 variational Hodge 로 단독 완성 가능한가?
- **기술 장벽**: Bloch-Beilinson conjecture 와 얽혀 있음.
- **진전 가능성**: **낮음**. 본질적 병목은 absolute Hodge 클래스의 algebraicity.
- **5년 내 기대값**: 특정 CY 3-fold 가족에서 부분 결과.

### (ii) Moonen-Gordon 절대 Hodge
- **현황**: Deligne 1982 가 shimura varieties 에서 absolute Hodge conjecture 증명. Moonen-Gordon 등 확장.
- **하위 질문 B**: Deligne 의 absolute Hodge 를 일반 CY 3-fold 로 확장 가능한가?
- **기술 장벽**: motivic Galois group 의 reductive 구조가 CY 에서는 불분명.
- **진전 가능성**: **중간**. motive 이론이 발전 중.
- **5년 내 기대값**: abelian varieties 내의 더 넓은 class 에서 absolute Hodge.

### (iii) p-adic Hodge 최근 진전 (Bhatt-Scholze)
- **현황**: Bhatt-Scholze 2022 Prismatic cohomology. Bhatt-Morrow-Scholze 2019 integral p-adic Hodge theory.
- **하위 질문 C**: Prismatic cohomology 로 Hodge class 의 p-adic 양자화 가능한가?
- **기술 장벽**: Hodge conjecture 는 characteristic 0 rational 성명이므로 p-adic 은 보조적.
- **진전 가능성**: **중간**. 도구가 급성장 중이나 직접 타격 경로는 아님.
- **5년 내 기대값**: integral Tate module 을 통한 integral Hodge class 접근 결과.

---

## BT-546 — BSD 추측

### (i) rank ≥ 2 BSD 부분 증명
- **현황**: Kolyvagin 1989, Gross-Zagier 1986 이 rank ≤ 1 에서 BSD 일부 증명. rank ≥ 2 는 미증명.
- **하위 질문 A**: Heegner cycles + Euler system 확장으로 rank 2 에 접근 가능한가?
- **기술 장벽**: Euler system 이 rank 에 민감함. Kolyvagin 방식은 rank ≤ 1 에 본질.
- **진전 가능성**: **낮음**. 50년 가까이 해당 벽 미돌파.
- **5년 내 기대값**: rank = 2 에서 |Ш| 유한 조건부 결과.

### (ii) Sha(E) 유한성 rank ≤ 1 에서
- **현황**: Kolyvagin 1989 이 Heegner 조건 + modularity 하에서 rank ≤ 1 에서 |Ш| 유한 증명. 일반 rank ≤ 1 모든 타원곡선에 대해서는 최근 Wei Zhang, Skinner-Urban, Liu-Tian 등의 Iwasawa 이론이 부분적 완결.
- **하위 질문 B**: rank = 1 에서 |Ш| 유한성의 무조건 증명 가능한가?
- **기술 장벽**: analytic rank ≤ 1 조건 없이는 이론이 바로 breakdown.
- **진전 가능성**: **중간** (일부 케이스는 완료).
- **5년 내 기대값**: rank ≤ 1 완전 무조건 |Ш| 유한성 (가능성 있음).

### (iii) Heegner index 정확 공식
- **현황**: Heegner index 는 $[E(K) : \mathbb{Z} y_K]$ 형태로 정의. Gross-Zagier 공식이 이를 L-함수 derivative 와 연결.
- **하위 질문 C**: Heegner index 의 닫힌 형태 공식 존재하는가?
- **기술 장벽**: p-adic L-function 과 Iwasawa main conjecture 필요.
- **진전 가능성**: **중간**. Burungale-Skinner 등이 관련 진전.
- **5년 내 기대값**: 특정 E 가족에서 정확 공식 유도.

---

## BT-547 — Poincaré 추측 (3D 해결, 4D 미해결)

### (i) Smooth 4D Poincaré 추측
- **현황**: 3D Poincaré 는 Perelman 2003 으로 해결. 4D Topological Poincaré 는 Freedman 1982 로 해결. **4D Smooth Poincaré 는 미해결**.
- **하위 질문 A**: $S^4$ 에 비표준 smooth 구조 존재하는가?
- **기술 장벽**: Donaldson, Seiberg-Witten 불변량이 4-manifold 분류에 적용되지만 $S^4$ 직접 공격에는 한계.
- **진전 가능성**: **낮음**. 긴 시간 미돌파.
- **5년 내 기대값**: exotic $S^4$ 후보에 대한 부정적 증거 추가.

### (ii) Schoenflies 추측 smooth 4D
- **현황**: Topological Schoenflies 는 Mazur-Morse 1959 등에 의해 Brown 1960. Smooth Schoenflies 추측 (embedded $S^{n-1} \subset S^n$ 이 smooth $D^n$ 경계인가?)는 n=4 에서 미해결.
- **하위 질문 B**: Smooth 4D Schoenflies 에서 Gabai-Meier 유형 결과 확장?
- **기술 장벽**: 4D 에서는 h-cobordism 이 smooth 로는 성립 안 함 (Donaldson).
- **진전 가능성**: **낮음**.
- **5년 내 기대값**: 특수 경우에서 부분 결과.

### (iii) Exotic $\mathbb{R}^4$ 분류
- **현황**: Freedman 1982, Taubes 1987 가 uncountably many exotic $\mathbb{R}^4$ 증명. 그러나 moduli 파라미터화는 미해결.
- **하위 질문 C**: Exotic $\mathbb{R}^4$ 의 topological invariant 에 의한 분류?
- **기술 장벽**: 현재 알려진 invariant 가 exotic structure 를 구별할 수준이 아님.
- **진전 가능성**: **낮음**.
- **5년 내 기대값**: 무한 가족 별도 구성 결과.

---

## 종합 표 (21 질문)

| 난제 | 하위 질문 | 진전 가능성 | 5년 내 기대 |
|------|-----------|-------------|-------------|
| BT-541 RH | (i) 임계선 100% | 중간 | 수치 2~5% |
| BT-541 RH | (ii) Li 양성 | 낮음 | 수치 개선 |
| BT-541 RH | (iii) zero-free | 중간 | 상수 개선 |
| BT-542 PvNP | (i) NEXP⊄ACC | 중간 | 1~2 건 |
| BT-542 PvNP | (ii) GCT | 낮음 | 부분 분리 |
| BT-542 PvNP | (iii) MCSP | 중간 | 변종 NP-완전 |
| BT-543 YM | (i) 2D Higgs | 중간 | 재증명 |
| BT-543 YM | (ii) 3D | 낮음 | 특수 결과 |
| BT-543 YM | (iii) lattice→cont | 중간 | N=2 부분 |
| BT-544 NS | (i) axisymmetric | 중간 | 조건부 |
| BT-544 NS | (ii) critical L∞ | 낮음 | log 조건 |
| BT-544 NS | (iii) self-similar | 중간 | 비유일성 |
| BT-545 Hodge | (i) variational | 낮음 | 가족 부분 |
| BT-545 Hodge | (ii) Moonen | 중간 | abelian 확장 |
| BT-545 Hodge | (iii) p-adic | 중간 | integral 접근 |
| BT-546 BSD | (i) rank≥2 | 낮음 | 조건부 Ш |
| BT-546 BSD | (ii) rank≤1 Ш | 중간 | 무조건 목표 |
| BT-546 BSD | (iii) Heegner | 중간 | 가족 공식 |
| BT-547 Poincaré | (i) 4D smooth | 낮음 | 부정 증거 |
| BT-547 Poincaré | (ii) Schoenflies | 낮음 | 특수 |
| BT-547 Poincaré | (iii) exotic R⁴ | 낮음 | 무한 가족 |

**가능성 분포**: 높음 0, 중간 11, 낮음 10. 학습자 체감상 5년 내 "의미있는 진전" 기대값은 약 **중간 기댓값 0.3~0.5 건/문항**.

---

## n=6 맥락과의 관계

- 본 노트의 21 질문은 모두 **전통 수학 경로** 기준 평가이다.
- n=6 구조적 attractor (Theorem B Bernoulli, Theorem 0 σφ=nτ 등)는 각 난제의 **맥락적 힌트**이며, 증명 경로는 아니다.
- millennium-7-closure-2026-04-11.md 가 선언한 honest 경계: "7대 난제 자체는 미해결, 이들의 n=6 구조적 맥락은 Theorem B + Theorem 0 으로 닫힘". 본 학습 노트는 이 경계를 준수한다.

---

## 1차 출처 주석

- Conrey 1989, Levinson 1974: analytic number theory 표준 참고.
- Williams 2011: STOC 2011 best paper, "Non-uniform ACC circuit lower bounds".
- Balaban 1980s: Comm. Math. Phys. 연작.
- Chen-Strain-Tsai-Yau 2008/9: Axisymmetric NS 정규성.
- Voisin 1998, Deligne 1982: Hodge theory 표준.
- Kolyvagin 1989, Gross-Zagier 1986: BSD rank ≤ 1.
- Perelman 2003, Freedman 1982: Poincaré.
- Bhatt-Scholze 2022 Prismatic: arXiv:1905.08229.
- Guth-Maynard 2024: arXiv prefix prefix (본 노트 시점에서 aXiv ID 재확인 필요).
- Albritton-Bruè-Colombo 2022: forced NS 비유일성 (Ann. Math.).
- Williams 2011: 정확히 NEXP ⊄ ACC⁰ (NTIME(2^{poly}) vs ACC⁰).
- Murray-Williams 2018: NTIME(2^{polylog}) ⊄ ACC⁰.

**세션 저자 주**: 위 연도/공저자 중 일부는 학습 노트 시점의 기억 기반이며, 1차 arXiv ID 및 저널 권호는 후속 세션에서 교차검증 필요. "정직" 규칙상 재확인 필요 항목을 명시적으로 남긴다.
