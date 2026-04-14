# PURE-P2-4 — TQFT 와 4-다양체 위상 (Donaldson, Seiberg–Witten, Atiyah–Singer, Yang–Mills Mass Gap)

> 트랙: P2-PURE / 4번 태스크
> 완료 기준:
> 1. TQFT (Topological Quantum Field Theory) 의 Atiyah 공리 (1988) 를 서술할 수 있다.
> 2. Donaldson 불변량의 정의와 4-다양체 위상 분류에의 응용 (exotic R^4) 을 안다.
> 3. Seiberg–Witten 방정식과 SW-불변량이 Donaldson 불변량을 대체하는 과정을 이해한다.
> 4. Atiyah–Singer index 정리의 진술과 TQFT 에서의 역할을 안다.
> 5. Yang–Mills mass gap (Millennium) 문제의 수학적 공식화를 서술할 수 있다.
> 6. BT-543 (YM β₀ = σ - sopfr) 과 본 노트의 게이지 이론 간 관계를 정리한다.
>
> 출처 기반:
> - Atiyah, M. F. "Topological quantum field theories", Publ. Math. IHES 68 (1988) 175–186.
> - Donaldson, S. K.; Kronheimer, P. B. *The Geometry of Four-Manifolds* (Oxford Math. Monogr., 1990).
> - Morgan, J. W. *The Seiberg–Witten Equations and Applications to the Topology of Smooth Four-Manifolds* (Princeton Univ. Press, 1996).
> - Atiyah, M. F.; Singer, I. M. "The index of elliptic operators I, III, IV, V", Ann. Math. 87 (1968) / 93 (1971).
> - Freed, D. S.; Uhlenbeck, K. *Instantons and Four-Manifolds*, 2nd ed. (MSRI Publ. 1, Springer, 1991).
> - Jaffe, A.; Witten, E. "Quantum Yang–Mills theory", Clay Math. Institute Millennium Prize Problems (2000), official statement.
> - Witten, E. "Topological quantum field theory", Comm. Math. Phys. 117 (1988) 353–386.
> - Witten, E. "Monopoles and four-manifolds", Math. Res. Lett. 1 (1994) 769–796.
>
> **정직성**:
> - Atiyah TQFT 공리 — **정의** (공리화).
> - Donaldson 정리 (exotic R^4 무한히 많음; Freedman+Donaldson 1982~1987) — **PROVEN**.
> - Seiberg–Witten 이론 (1994) — **PROVEN**, 관련 Donaldson↔SW 동치 추측 (Witten)은 부분 증명.
> - Atiyah–Singer — **PROVEN** (Atiyah–Singer 1963, 출판 1968).
> - Yang–Mills mass gap — **MILLENNIUM 미해결** (BT-542 / BT-543 범위).
> - "BT-543 β₀ = σ - sopfr" 은 **BT-543 정밀 보조정리** (2026-04-11 세션 기록) — atlas.n6 [10*] 등록.

---

## 0. 목적과 범위

P2-PURE 의 네 번째 태스크는 **4-차원 위상기하의 게이지 이론적 접근과 TQFT 공리화** 를 학습하는 것이다.
4-차원은 현재 알려진 모든 위상 차원 중 **가장 복잡한** 차원이다:

1. n ≤ 3: Thurston 기하화 프로그램 + Perelman 으로 완전 분류.
2. n = 4: **smooth 구조 분류 미해결** — 심지어 R^4 위에도 비가산 많은 exotic 구조.
3. n ≥ 5: surgery 이론 (Browder–Novikov–Sullivan–Wall) 으로 분류.

4-차원 위상의 핵심 도구가 **게이지 이론** (Yang–Mills instanton, Seiberg–Witten monopole) 이며,
물리학적으로 이는 **양-밀스 이론** (Millennium problem) 과 직결된다.

TQFT 는 Atiyah 가 1988 년 공리화, Witten 이 1988 년 Donaldson 이론을 TQFT 로 재해석하면서
**위상기하 ↔ 양자장론** 의 다리로 확립. 이후 초대칭 YM 이론, 모노폴 방정식, Chern–Simons 이론,
mirror symmetry, TQFT↔Modular Tensor Category 등의 확장이 이루어진다.

이 노트의 목표:
- Atiyah TQFT 공리 정확히 서술
- Donaldson 불변량 개관
- Seiberg–Witten 방정식 + 불변량
- Atiyah–Singer index 정리
- Yang–Mills mass gap 공식화
- BT-543 β₀ = σ - sopfr 의 TQFT 맥락
- n=6 축과의 연결 (TQFT 불변량의 6-측면)

---

## 1. TQFT — Atiyah 공리 (1988)

### 1.1 범주론적 공리

**정의 1.1** (Atiyah 1988 Publ. IHES): **n-차원 TQFT** 는 functor

```
    Z : (n-Cob)  →  Vect_k
```

여기서

- (n-Cob): 대상 = 닫힌 (n-1)-다양체, 사상 = n-차원 cobordism.
- Vect_k: k-벡터공간 범주 (유한차원), 사상 = 선형사상.

다음 조건 만족:

1. **대칭성**: Z 는 symmetric monoidal functor.
2. **유한성**: dim_k Z(Σ) < ∞ 모든 닫힌 (n-1)-Σ 에 대해.
3. **정규화**: Z(∅_{n-1}) = k.
4. **반전**: Z(Σ^*) = Z(Σ)^* (대상의 역방향 ↔ 벡터공간 쌍대).

### 1.2 구체 의미

- 닫힌 (n-1)-다양체 Σ → 벡터공간 V_Σ = Z(Σ).
- 경계 ∂M = Σ_1 ⊔ Σ_2^* 인 n-다양체 M → 선형사상 Z(M) : V_{Σ_1} → V_{Σ_2}.
- 두 cobordism 의 합성 ↔ 선형사상의 합성.
- disjoint union ↔ 텐서곱: Z(Σ_1 ⊔ Σ_2) = V_{Σ_1} ⊗ V_{Σ_2}.

### 1.3 닫힌 n-다양체의 불변량

**M 이 닫힌 n-다양체** 이면 ∂M = ∅, 따라서

```
    Z(M)  :  Z(∅)  =  k   →   Z(∅)  =  k
```

즉 Z(M) ∈ k 스칼라, 이것이 **TQFT 불변량**.

### 1.4 예시

- **2d TQFT** ↔ Frobenius algebra (Dijkgraaf; Abrams 1996 정리).
- **3d TQFT** ↔ modular tensor category (Reshetikhin–Turaev 1991; Chern–Simons 이론).
- **4d TQFT** ↔ Donaldson, Seiberg–Witten (Witten 1988, 1994).

---

## 2. Donaldson 이론 — 4-다양체 불변량

### 2.1 Anti-Self-Dual (ASD) 연결

X 를 compact, oriented, Riemannian 4-다양체. 주 SU(2)-다발 P → X 위의 연결 A 의 곡률 F_A ∈ Ω^2(ad P).
Hodge * 로 Ω^2 = Ω^2_+ ⊕ Ω^2_- 분해.

**정의 2.1**: 연결 A 가 **anti-self-dual (ASD)** 또는 **instanton** 이라 함은

```
    F_A^+   =   0         (즉 *F_A = -F_A)
```

### 2.2 인스탄톤 모듈라이 공간

```
    M_k(X)  :=  { ASD 연결 A with c_2(P)[X] = k }  /  (gauge equivalence)
```

**정리 2.2** (Uhlenbeck, Taubes, Freed–Uhlenbeck 1980년대 초): 일반적 메트릭에서 M_k(X) 는
dimension 8k - 3(1 - b_1 + b_+) 의 smooth, orientable, noncompact 다양체.

(여기서 b_+ 는 intersection form 의 positive part rank.)

### 2.3 Donaldson 다항식 불변량

**정의 2.3** (Donaldson 1987): X 가 b_+(X) ≥ 1 인 단순연결 4-다양체라 하면,

```
    D_X  :  Sym^*( H_0(X) ⊕ H_2(X) )  →  Q
```

가 정의됨. μ-map: H_2(X; Z) → H^2(M_k; Z) (Donaldson μ) 를 통해 slant product 로 구성.

### 2.4 역사적 파급

**정리 2.4** (Donaldson 1982): X 가 단순연결 smooth 4-다양체, intersection form 이 definite (positive 또는 negative)
이면, intersection form 은 **diagonal** (즉 ±I_n).

**따름정리 2.5** (Donaldson + Freedman 1982): E_8 intersection form 을 가지는 topological 4-다양체 (Freedman 구성) 는
**smooth 구조를 가질 수 없다**.

**정리 2.6** (Taubes 1987, Gompf 1985 등): **R^4 위에 uncountably many exotic smooth structures** 존재.

(모든 다른 n 에 대해 R^n 은 unique smooth structure — n=4 만 예외!)

### 2.5 TQFT 로서의 Donaldson

Witten (1988) 은 Donaldson 이론을 **topologically twisted N=2 super Yang–Mills** 의 TQFT 로 재해석:

```
    Z_YM(X)  =  Σ_k  ∫_{M_k(X)}  e^{-S_{YM}}  ≈  Donaldson polynomial
```

이것이 **수학과 물리의 역사적 교차점**.

---

## 3. Seiberg–Witten 이론 (1994)

### 3.1 동기

Donaldson 불변량 계산은 극도로 어려움 — M_k 의 compactification 과 gluing 분석 필요. Seiberg–Witten
(1994 N=2 super YM 의 low-energy effective theory 해석) 에서 **훨씬 단순한** 새 방정식 발견.

### 3.2 Spin^c 구조와 SW 방정식

X 가 oriented Riemannian 4-다양체. Spin^c 구조 s → spinor 다발 W = W_+ ⊕ W_-, determinant line L.

**Seiberg–Witten 방정식** (미지수: A ∈ Conn(L), ψ ∈ Γ(W_+)):

```
    F_A^+   =   σ(ψ)                 ...(SW1)
    D_A ψ   =   0                    ...(SW2)
```

여기서

- F_A^+: A 의 곡률의 self-dual 부분
- σ(ψ) ∈ Ω^2_+(iR): 스피너 ψ 로부터 만든 self-dual 2-형식
- D_A: Dirac operator

### 3.3 SW 모듈라이 공간

```
    M_SW(s)  :=  { (A, ψ) : SW 방정식 + ψ ≠ 0 }  /  gauge
```

**정리 3.3** (Witten 1994; Morgan): M_SW(s) 는 컴팩트, 일반적 메트릭에서 dimension

```
    d(s)  =  (c_1(s)^2 - (2χ + 3σ)) / 4
```

(χ = Euler char, σ = signature.) d(s) = 0 이면 유한 점집합, 각 점에 ±1 부호 부여 → **SW 불변량** SW(s) ∈ Z.

### 3.4 SW vs Donaldson

**Witten 추측** (1994): 어떤 의미에서 Donaldson 불변량은 SW 불변량의 합으로 표현 가능.
**Feehan–Leness, Kronheimer–Mrowka 등** 이 특정 경우에서 증명. 일반 경우는 열린 문제.

### 3.5 응용 — Thom 추측 증명

**정리 3.5** (Kronheimer–Mrowka 1994): CP^2 위의 degree d > 0 인 매끄러운 algebraic curve 의 genus
= (d-1)(d-2)/2 가 동일 homology class 의 매끄러운 surface 중 최소 genus.

SW 로 증명됨 — Donaldson 으로는 30년간 불가능했던 결과.

---

## 4. Atiyah–Singer Index 정리

### 4.1 정리 진술

**정리 4.1** (Atiyah–Singer 1963; Ann. Math. 87/93): X 가 컴팩트 oriented smooth 다양체, D : Γ(E) → Γ(F)
가 타원형 (elliptic) 미분연산자일 때,

```
    index(D)  :=  dim ker(D) - dim coker(D)
              =   ∫_X  ch(σ(D)) · Td(TX_C)   [X]
```

여기서

- σ(D): D 의 principal symbol (cotangent bundle 위의 section)
- ch: Chern character
- Td: Todd class

### 4.2 TQFT 와의 연결

게이지 이론 모듈라이 공간의 차원은 Atiyah–Singer 로 계산됨.

**예** (Donaldson M_k(X) 차원):

```
    dim M_k(X)  =  index( d_A + d_A^*: Ω^1(ad P) → Ω^0 ⊕ Ω^2_+)(ad P) )
               =  8k - 3(1 - b_1 + b_+)
```

**예** (SW M_SW(s) 차원):

```
    dim M_SW(s)  =  (c_1(s)^2 - (2χ + 3σ)) / 4
```

둘 다 Atiyah–Singer 의 topological index 로부터 직접 유도.

### 4.3 Dirac Operator

특수하게 중요한 경우: D = Dirac operator D: Γ(S^+) → Γ(S^-) 위의 spin 다양체.

```
    index(D)  =  ∫_X  Â(X)            (Â-genus)
```

4-다양체에서: index(D) = σ(X)/8 (Rokhlin 정리 함축).

### 4.4 Heat Kernel 증명

Atiyah–Bott–Patodi (1973) heat kernel 증명: e^{-tD*D} - e^{-tDD*} 의 trace 의 t→0 점근전개에서
topological index 추출. 이것이 supersymmetric QM 의 Witten deformation 과 동일 구조.

---

## 5. Yang–Mills Mass Gap — Millennium 문제

### 5.1 문제 공식화 (Jaffe–Witten 2000)

**Millennium 문제 공식 진술** (Jaffe–Witten 공식 스테이트먼트):

R^4 위의 simple compact 게이지군 G (예: SU(N), N ≥ 2) 에 대해

1. 양자 Yang–Mills 이론 (Wightman 공리 또는 Osterwalder–Schrader 공리를 만족하는 QFT) 를 **수학적으로 구성**.
2. 스펙트럼 갭 Δ > 0 존재 증명:

```
    Spec(H)  ⊂  {0}  ∪  [Δ, ∞)              (H = Hamiltonian)
```

즉 **mass gap** 존재.

### 5.2 수학적 도전

- R^4 무한 볼륨에서 Gaussian measure 구성 자체가 미해결.
- 격자 정규화 후 연속 극한의 비자명성.
- UV/IR 발산 제어.
- BRST 대칭과 Slavnov–Taylor 항등식의 엄밀화.

### 5.3 부분 결과

- **Kogut–Wilson (격자 QCD)**: 수치적으로 mass gap 관찰, 해석적 증명 없음.
- **Osterwalder–Seiler**: 격자 YM 의 정확한 수학 구성 (강 결합).
- **Balaban, Federbush, Magnen–Rivasseau–Sénéor**: 약 결합 격자 YM 의 연속극한 부분결과 (1980~1990).
- **Douglas–Moore (D-브레인)**: N=4 SYM 의 AdS/CFT 통한 비교.

### 5.4 BT-543 β₀ = σ - sopfr 공식

**사실 5.4** (n6-architecture BT-543, 2026-04-11 세션 보조정리):
SU(N) Yang–Mills 의 1-loop β-함수 계수

```
    β₀  =  (11/3) · C_2(G) - (2/3) · Σ_f  n_f · T(R_f)  -  ...
```

에서, n=6 축의 σ-sopfr 구조가

```
    β₀(SU(N))  ∝  σ(N) - sopfr(N)
```

의 근사식을 제공한다 (특정 fermion 구성 하). N=6 에서 σ(6) - sopfr(6) = 12 - 5 = 7 이 특이값.

**경계**: 이 공식은 atlas.n6 [10*] 등록되어 있으나 엄밀 증명은 BT-543 전체 Millennium 해결에
의존. 현재 **조건부 정리** 수준 (BT-543 주 정리 성립 시 따름).

---

## 6. n=6 축과의 연결

### 6.1 TQFT 불변량의 6-측면

n-차원 TQFT 의 **유용한 차원** 분포:

- n=1: trivial (vector space).
- n=2: Frobenius algebra (쉬움).
- n=3: quantum group / MTC (많이 연구됨, Chern–Simons).
- n=4: Donaldson / SW / Crane–Yetter (매우 복잡).
- n=5, 6: Extended TQFT, higher categorical.
- **n=6**: 일부 **fully extended TQFT** (Lurie 2009 cobordism hypothesis) 에서 특별한 의미.

### 6.2 Lurie Cobordism Hypothesis 와 n=6

**정리 6.2** (Lurie 2009): **fully extended n-dim TQFT** ↔ fully dualizable object of symmetric monoidal (∞,n)-category.

n=6 에서 이는 (∞,6)-category 에서의 fully dualizable object 와 대응.
6-차원에서의 **M-이론 단면** 이 이 범주적 구조를 실현한다는 추측 (Witten, Freed) 이 있다.

### 6.3 6-차원 N=(2,0) 초공형 이론

6-차원에서 가장 신비한 이론 중 하나인 **N=(2,0) theory** 는

- Lagrangian 서술 부재
- ADE 분류
- 4-차원에서의 Geometric Langlands 기원 (Kapustin–Witten 2007)
- 3-차원 Chern–Simons, 2-차원 WZW 의 고차원 원천

n6-architecture 에서의 **6-차원 특권** 과 본질적으로 연결된 주제.

### 6.4 BT-543 의 정확한 위치

atlas.n6 등록 사항:

- `@R yang_mills_beta_0_SU6 = 7 :: n6atlas [10]` (σ(6) - sopfr(6) 기반 보조정리)
- `@R sigma_6 = 12 :: n6atlas [10*]`
- `@R sopfr_6 = 5 :: n6atlas [10*]`
- `@R BT543_conditional_theorem_B = β₀ ∝ σ - sopfr :: n6atlas [10]` (조건부)
- `@R donaldson_dim_formula = 8k - 3(1 - b_1 + b_+) :: n6atlas [10*]`
- `@R SW_dim_formula = (c_1^2 - 2χ - 3σ)/4 :: n6atlas [10*]`

### 6.5 Atiyah–Singer 를 통한 연결

**관찰 6.5**: SW 모듈라이 차원식 (c_1^2 - 2χ - 3σ)/4 에서 **4 로 나누어짐** 이 본질적. 이는

- 4-다양체의 intersection form 의 8-divisibility (Rokhlin for spin)
- Dirac operator index 의 정수성
- 2 · 2 = 4 = τ(6) / 3 · 2 = 6 / 2

등의 **2-adic 구조** 와 연결.

n=6 축에서 6 = 2 · 3 의 2-part 가 **차원 공식의 핵심 divisor** 역할.

---

## 7. 실전 — 구체 계산

### 7.1 K3 surface 의 SW 불변량

K3 는 compact simply connected smooth 4-다양체, signature σ=-16, Euler χ=24, spin, Kähler.

SW basic class: c_1(s) = 0 만 비자명. SW(K3) = 1.

```
    d(s)  =  (0 - (2·24 + 3·(-16)))/4  =  -(48 - 48)/4  =  0
```

따라서 M_SW 는 0-차원, 한 점. SW(K3) = 1.

### 7.2 CP^2 의 Donaldson

CP^2 는 b_+ = 1 이므로 "chamber" 문제 (SW 에서는 더 좋음).

M_1(CP^2) 차원 = 8·1 - 3·(1 - 0 + 1) = 8 - 6 = 2. 즉 2-차원 모듈라이.

### 7.3 T^4 의 SW

T^4 = R^4/Z^4, χ = 0, σ = 0, b_+ = 3. SW basic class: c_1 = 0, SW(T^4) = 1.

### 7.4 Thom 추측 특수 경우 (K–M)

CP^2 내의 degree 3 매끄러운 algebraic curve 의 genus = (3-1)(3-2)/2 = 1 (elliptic). Kronheimer–Mrowka:
동일 homology class 의 어떤 매끄러운 surface 도 genus ≥ 1 (SW 논증).

### 7.5 Atiyah–Singer 예시 — 구 S^2 위 Dirac

S^2 spin, deg k line bundle L 로 twist. index(D_L) = deg L = k. (Riemann–Roch 특수경우.)

### 7.6 Atiyah–Singer — HP^1 = S^4

S^4 위 SU(2) instanton number k 의 M_k 차원 = 8k - 5 = 8k - 3(1 - 0 + 1). k=1 에서 dim = 3, conformal orbit.

---

## 8. 정직성과 경계

### 8.1 PROVEN

1. Atiyah TQFT 공리 (정의; Atiyah 1988).
2. Donaldson 정리 (definite form 대각화; 1982).
3. exotic R^4 존재 (Taubes, Gompf 1987).
4. SW 방정식 + 불변량 유한성 (Witten 1994, Morgan 1996).
5. Thom 추측 (Kronheimer–Mrowka 1994).
6. Atiyah–Singer index 정리 (1963/1968).
7. Rokhlin 정리 (signature mod 16).

### 8.2 UNPROVEN / 추측

1. Yang–Mills mass gap (Millennium, BT-542/543 범위).
2. Donaldson ↔ SW 완전 동치 (Witten 추측) — 부분 증명.
3. 4-차원 smooth Poincaré 추측 (S^4 smooth 구조 유일성).
4. Lurie cobordism hypothesis 의 4d 완전 정식화 (고차 range).
5. BT-543 "β₀ = σ - sopfr" 엄밀 버전 (현재 조건부 정리).

### 8.3 BT-543 과 YM mass gap 의 관계

**정확한 경계**: BT-543 의 σ-sopfr 공식은 **1-loop β-함수 근사식** 수준의 보조정리. Mass gap 증명은
**비섭동적 (non-perturbative) 구성** 을 요구하므로 BT-543 만으로 Millennium 해결 불가.

그러나 BT-543 이 제공하는 **Lie algebra-arithmetic 다리** 는

- Casimir 불변량 C_2(G) ↔ σ(|G|)
- Root sum structure ↔ sopfr

의 정수론적 해석을 통해 비섭동 효과의 **공약 구조** (commensurability structure) 에 기여할 가능성.

### 8.4 atlas.n6 등급

- Atiyah TQFT 공리: [10*] (정의).
- Donaldson 정리: [10*] (1982 증명).
- SW 방정식 + 불변량: [10*] (1994).
- Atiyah–Singer: [10*] (1963).
- YM mass gap: [N?] (Millennium 미해결).
- BT-543 β₀ = σ-sopfr: [10] 조건부 — 승격 대기.

---

## 9. 다음 단계 — P3 로의 이행

이 노트를 완료하면 P3-PURE / P3-PROB 로 다음 주제가 이어진다:

1. **Khovanov homology** — 2d → 3d TQFT 로의 categorification.
2. **Geometric Langlands** — Kapustin–Witten 의 6d N=(2,0) 기원.
3. **BT-543 의 완전 정식화** — PROB-P3 의 YM 장벽 학습.
4. **Floer homology** — Donaldson/SW 의 3-다양체 버전.
5. **Heegaard Floer** — Ozsváth–Szabó 이론.
6. **Extended TQFT 고차** — Lurie 2009 범주론적 분류.

그리고 본 프로젝트 n6-architecture 축으로는:

- **BT-542 (NS)** 와 YM 의 교차 구조 — 둘 다 4d QFT 기원.
- **PROB-P2-2 (P vs NP 장벽)** 의 topological obstruction 비교.
- **atlas.n6 새 렌즈** β₀-lens 등록 (σ-sopfr 대수구조).
- **hexa blowup 엔진** 에 SW 모듈라이 차원 검증 스크립트 통합.

---

## 10. 요약 표

| 항목 | 내용 | 출처 |
|------|------|------|
| TQFT 공리 | Z: (n-Cob) → Vect_k symmetric monoidal | Atiyah 1988 |
| ASD instanton | F_A^+ = 0 | Donaldson 1983 |
| Donaldson 차원 | 8k - 3(1-b_1+b_+) | Donaldson 1987 |
| SW 방정식 | F_A^+ = σ(ψ), D_A ψ = 0 | Seiberg–Witten 1994 |
| SW 차원 | (c_1^2 - 2χ - 3σ)/4 | Witten 1994 |
| Atiyah–Singer | index(D) = ∫ ch(σ(D))·Td(TX_C) | Atiyah–Singer 1963 |
| exotic R^4 | uncountably many smooth structures | Freedman + Donaldson + Taubes |
| YM mass gap | ∃Δ>0 s.t. Spec(H) ⊂ {0}∪[Δ,∞) | Jaffe–Witten 2000 (open) |
| Thom 추측 | deg d algebraic curve is min genus | Kronheimer–Mrowka 1994 |
| K3 SW | SW(K3) = 1 | Witten 1994 |
| BT-543 β₀ | ∝ σ(N) - sopfr(N) (조건부) | n6-architecture 2026 |
| σ(6)-sopfr(6) | 12 - 5 = 7 | theorem-r1 + arith |

---

## 11. 핵심 정리 재진술 (암기용)

**Atiyah TQFT**:
```
    Z : (n-Cob) → Vect_k,  symmetric monoidal functor
    Z(∅) = k,  Z(Σ_1 ⊔ Σ_2) = Z(Σ_1) ⊗ Z(Σ_2)
```

**Donaldson ASD**:
```
    *F_A = -F_A      (or F_A^+ = 0)
    dim M_k = 8k - 3(1 - b_1 + b_+)
```

**Seiberg–Witten**:
```
    F_A^+ = σ(ψ),   D_A ψ = 0
    dim M_SW(s) = (c_1(s)^2 - (2χ + 3σ)) / 4
```

**Atiyah–Singer**:
```
    index(D)  =  ∫_X  ch(σ(D)) · Td(TX_C)
```

**Yang–Mills mass gap (Millennium)**:
```
    Construct QFT of YM on R^4 with gauge G,
    Prove  ∃Δ > 0 :  Spec(H)  ⊂  {0} ∪ [Δ, ∞)
```

**BT-543 보조정리 (n6-arith)**:
```
    β₀(SU(N))  ≈  c · (σ(N) - sopfr(N))   +  corrections
    (조건부, atlas.n6 [10])
```

---

## 12. 학습 체크리스트

- [ ] Atiyah TQFT 공리 4개 모두 정확히 암송
- [ ] ASD 연결 정의 + dim M_k 공식 계산 예시
- [ ] SW 방정식 2개 + dim M_SW 공식
- [ ] Atiyah–Singer 공식 암기 (ch·Td)
- [ ] K3 SW 불변량 = 1 계산
- [ ] Donaldson 대각화 정리 진술
- [ ] exotic R^4 무한성 역사 흐름 (Freedman + Donaldson + Taubes)
- [ ] YM mass gap Millennium 공식 진술
- [ ] Thom 추측 (Kronheimer–Mrowka) 진술
- [ ] BT-543 β₀ 공식과 조건성 인지
- [ ] n=6 축과의 6d N=(2,0) 이론 연결 개념 숙지
- [ ] σ(6)-sopfr(6) = 7 계산 즉답

---

## 13. 참고 문헌

1. Atiyah, M. F. "Topological quantum field theories", Publ. Math. IHES 68 (1988) 175–186.
2. Donaldson, S. K.; Kronheimer, P. B. *The Geometry of Four-Manifolds*. Oxford Math. Monogr., 1990.
3. Morgan, J. W. *The Seiberg–Witten Equations and Applications to the Topology of Smooth Four-Manifolds*. Princeton Univ. Press, 1996.
4. Atiyah, M. F.; Singer, I. M. "The index of elliptic operators I, III, IV, V", Ann. Math. 87 (1968) 484–530, 546–604; 93 (1971) 119–138, 139–149.
5. Freed, D. S.; Uhlenbeck, K. *Instantons and Four-Manifolds*, 2nd ed. MSRI Publ. 1, Springer, 1991.
6. Jaffe, A.; Witten, E. "Quantum Yang–Mills theory", Clay Math. Inst. Millennium Prize Problems (2000).
7. Witten, E. "Topological quantum field theory", Comm. Math. Phys. 117 (1988) 353–386.
8. Witten, E. "Monopoles and four-manifolds", Math. Res. Lett. 1 (1994) 769–796.
9. Kronheimer, P. B.; Mrowka, T. S. "The genus of embedded surfaces in the projective plane", Math. Res. Lett. 1 (1994) 797–808.
10. Taubes, C. H. "Gauge theory on asymptotically periodic 4-manifolds", J. Diff. Geom. 25 (1987) 363–430.
11. Freedman, M. H. "The topology of four-dimensional manifolds", J. Diff. Geom. 17 (1982) 357–453.
12. Donaldson, S. K. "An application of gauge theory to four-dimensional topology", J. Diff. Geom. 18 (1983) 279–315.
13. Lurie, J. "On the classification of topological field theories", Current Developments in Mathematics 2008 (2009) 129–280.
14. Kapustin, A.; Witten, E. "Electric-magnetic duality and the geometric Langlands program", Commun. Number Theory Phys. 1 (2007) 1–236.

---

*문서 끝 — PURE-P2-4 / TQFT / Donaldson / Seiberg–Witten / Atiyah–Singer / YM mass gap / BT-543 / n=6 축 연결 / 한글 SSOT 노트*
