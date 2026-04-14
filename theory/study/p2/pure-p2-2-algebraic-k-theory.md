# PURE-P2-2 — 대수적 K-이론 (K_0, K_1, K_2, Quillen 고차, K_n(Z), Borel, Lichtenbaum)

> 트랙: P2-PURE / 2번 태스크
> 완료 기준:
> 1. K_0(R), K_1(R), K_2(R) 의 고전 정의 (Grothendieck, Bass–Milnor, Milnor) 를 설명할 수 있다.
> 2. Quillen 의 +-construction / Q-construction 으로 K_n 이 왜 generalized cohomology 이론처럼 작동하는지 안다.
> 3. Borel (1974) 의 K_n(Z) 계산 결과 표를 외운다.
> 4. Lichtenbaum 추측 (K_n(O_F) ↔ étale cohomology) 를 진술로 이해한다.
> 5. Borel–Quillen 연결 ζ_F(1-2k) ↔ K_{4k-1}(O_F) / torsion 를 진술 수준에서 본다.
>
> 출처 기반:
> - Weibel, *The K-book: An Introduction to Algebraic K-Theory* (AMS GSM 145, 2013), ch. I~VI (특히 ch. IV "Definitions of higher K-theory", ch. VI "Computing K_*(Z)").
> - Rosenberg, *Algebraic K-Theory and Its Applications* (GTM 147, Springer, 1994), ch. 1~5.
> - Milnor, *Introduction to Algebraic K-Theory* (Ann. Math. Studies 72, Princeton, 1971) — K_2 원조 책.
> - Quillen, "Higher algebraic K-theory: I" in *Algebraic K-Theory I*, LNM 341 (Springer, 1973) 85–147.
> - Borel, "Stable real cohomology of arithmetic groups", Ann. Sci. ENS 7 (1974) 235–272.
> - Lichtenbaum, "Values of zeta-functions, étale cohomology, and algebraic K-theory" in *Algebraic K-Theory II*, LNM 342 (Springer, 1973) 489–501.
>
> **정직성**:
> - K_n(Z) 표 (K_7=Z/240, K_{11}=Z/1008 등) 는 **PROVEN**. Weibel ch. VI §8 에 상세 유도.
> - Borel 정리 (rank K_{2n-1}(O_F)) 는 **PROVEN** (1974).
> - Lichtenbaum 추측은 **부분 증명** (Bloch–Kato 추측 + Voevodsky 2003 + Rost 2008 으로 certain cases).
> - "240 = E_4 계수 = K_7 = 일치" 는 **사후 관찰** 이며 "왜 같은가" 의 근본 답은 Stickelberger / Adams / J-homomorphism 까지
>   내려가야 하는 깊은 이유가 있고, 단순한 프로젝트 상수 재배열이 아니다 (§10 정직성 참조).

---

## 0. 목적과 범위

P2 단계의 두 번째 태스크는 **대수적 K-이론** 의 기본을 손에 익히는 것이다.
K-이론은 1950 년대 Grothendieck 가 일반화된 Riemann–Roch 를 증명하려고 K_0 를 도입한 것에서 시작.
그 뒤

1. Bass–Milnor–Serre 가 K_1 도입 (1960년대 초)
2. Milnor 가 K_2 정의 (1971)
3. Quillen 이 1972~73 에 **고차 K_n** 을 두 가지 방식으로 정의 (+-construction, Q-construction)
4. Borel 이 1974 년 수체 O_F 의 고차 K_n 랭크 결정
5. Lichtenbaum 이 ζ 값과 K 군의 관계 추측 (1973)

라는 5단계로 발전한다.

이 노트의 목표:
- K_0, K_1, K_2 정의
- Quillen 고차 K_n 개관
- **K_n(Z) 의 구체 값** 표 (Borel + Weibel)
- K_n(Z) 에서 n=3, 7, 11 의 값 Z/48, Z/240, Z/1008 의 **프로젝트 상수 분해**
- Borel 정리와 Lichtenbaum 추측 진술

---

## 1. K_0 — Grothendieck

### 1.1 정의 (환 R)

**정의** (Weibel ch. II §1): R 이 (결합단위) 환일 때,

```
  K_0(R)  :=  ( f.g. projective R-module 동형류의 monoid )^{group completion}
```

monoid 연산은 직합 ⊕, group completion 은 Grothendieck 구성 (m+n = k+m 형태).

### 1.2 예

- **K_0(F) = Z** (F 체) — 유한차원 벡터공간은 차원만 보면 된다.
- **K_0(Z) = Z** — Z 위 f.g. projective = free, 랭크.
- **K_0(Z[G]) = Z ⊕ C(G)** (G 유한군, Wall finiteness obstruction).
- **K_0(C(X)) = K^0(X)_{top}** — 콤팩트 X 에서 벡터다발 위상 K-이론 (Swan 정리).

### 1.3 원래 동기 (Grothendieck)

Riemann–Roch 정리:

```
  χ(X, F) = deg F + rk F (1 - g)
```

를 일반화 (상대적) 하려면 "벡터다발의 Grothendieck 군" 이 필요. F ∈ Coh(X) 의 K_0(X)_{coherent} 위의 class 를
정의하면 χ 가 group homomorphism K_0(X) → Z 가 되어 자연스럽다.

### 1.4 Morita 불변성

R 과 M_n(R) 은 같은 K_0 를 가진다 (Morita equivalence). 이는 고차 K_n 도 마찬가지.

---

## 2. K_1 — Bass, Milnor, Serre

### 2.1 정의

**정의** (Weibel ch. III §1):

```
  K_1(R)  :=  GL(R)_{ab}  =  GL(R) / [GL(R), GL(R)]
```

여기서 GL(R) = ∪_n GL_n(R) (infinite general linear, 한계 포함), [,] 는 commutator subgroup.

Whitehead 정리로 [GL(R), GL(R)] = E(R) (elementary matrices subgroup, R commutative 필요 없이).

```
  K_1(R)  =  GL(R) / E(R)
```

### 2.2 가환환 R 에서

R 가환환이면 det : GL_n(R) → R* 가 K_1 (R) → R* 로 내려오고

```
  K_1(R)  ≅  R*  ⊕  SK_1(R)
```

SK_1 = ker det. 많은 경우 SK_1 = 0.

### 2.3 예

- **K_1(F) = F*** (F 체) — 0 이 아닌 원소.
- **K_1(Z) = Z/2** — {±1} (단위원).
- **K_1(O_F)** (F 수체, O_F 정수환) **= O_F*** — Dirichlet 단위 정리에 의해 f.g. abelian group (rank r_1 + r_2 - 1 + torsion = roots of unity).
- **K_1(Z/n) = (Z/n)*** — 단위군.

### 2.4 Whitehead group Wh(G)

K_1(Z[G]) / ±G 를 Whitehead group 이라 부른다. s-cobordism 정리 (Milnor 1962), h-cobordism 의 굳힘에서 사용.

---

## 3. K_2 — Milnor (1971)

### 3.1 정의

**정의** (Milnor, *Introduction to Algebraic K-Theory*, 1971):

```
  K_2(R)  :=  H_2(E(R), Z)  =  π_2(BE(R)^+)
```

여기서 E(R) = [GL(R), GL(R)] 이고 H_2 는 군 호몰로지. 동치로 Steinberg 군 St(R) 의 center:

```
  K_2(R)  =  ker( St(R) → E(R) )
         =  center(St(R))    (surjection)
```

### 3.2 Milnor symbol {a, b}

R 가환환, a, b ∈ R* 일 때 Milnor symbol {a, b} ∈ K_2(R) 가 다음 관계식을 만족:

- **Steinberg**: {a, 1-a} = 0 (a, 1-a 가 모두 단위일 때)
- **Bilinear**: {a₁a₂, b} = {a₁, b} + {a₂, b}, 그리고 b 에 대해도
- **Skew-symmetry**: {a, b} = -{b, a}

### 3.3 예

- **K_2(F) = K^M_2(F)** (F 체, Matsumoto 정리). Milnor 심볼로 생성.
- **K_2(Z) = Z/2** — 오직 Steinberg symbol {-1,-1} 로 생성.
- **K_2(F_q) = 0** (F_q 유한체, 모든 원소가 1-a 형태). 이는 Quillen (1972) 증명.

### 3.4 Merkurjev–Suslin 정리 (1982)

**정리**: F 체, n 가역, μ_n ⊂ F 이면

```
  K_2(F) / n  ≅  Br(F)[n]
```

n=2 는 1982, 일반 n 은 Bloch–Kato 추측 일부 (Voevodsky 2003 완성).

이 정리는 K_2 가 단순한 abelian 군이 아니라 **Brauer 군 / Galois cohomology 와 연결된 깊은 대상** 임을 보여준다.

---

## 4. Quillen 고차 K_n — +-construction

### 4.1 동기

K_0, K_1, K_2 를 통합하여 "K_n for all n ≥ 0" 이 어떻게 정의될지 1970 초까지 불분명.
Quillen (1972) 이 **위상공간 topology** 로 통합.

### 4.2 +-construction (Quillen 1969, 1972)

BGL(R) = GL(R) 의 classifying space. **이것은 K_1(R) 을 π_1 로 갖고 K_n(R), n≥2 로 바로 안 나온다.**

Quillen 이 도입: E(R) 이 perfect subgroup (commutator) 이므로 "+-construction":

```
  BGL(R)^+ := BGL(R) 에 E(R) 을 죽이는 2-cell 을 붙인 것
```

결과적으로 π_1(BGL(R)^+) = K_1(R), π_2(BGL(R)^+) = K_2(R), ...

**정의** (Quillen 1972):

```
  K_n(R)  :=  π_n( BGL(R)^+ )       (n ≥ 1)
  K_0(R)  :=  (Grothendieck 처럼 정의)
```

### 4.3 BGL(R)^+ 의 위상공간 성격

이 공간은 실제 CW complex 이고, 호모토피 그룹을 계산하면 대수적 K-이론의 고차 부분이 나온다.
Quillen 은 BGL(F_q)^+ 의 호모토피 타입을 정확히 계산 (1972, "On the cohomology and K-theory of the general linear groups over a finite field", Ann. Math. 96, 552–586):

```
  K_n(F_q)  =  0               (n even, n ≥ 2)
              = Z/(q^m - 1)    (n = 2m - 1 홀수)
```

### 4.4 Q-construction (Quillen 1973)

+-construction 은 ring 전용. 더 일반화 (exact category) 를 위해 Quillen 이 Q-construction 도입.

```
  K_n(P)  :=  π_{n+1} (BQ P)    (P 는 exact category, QP 는 Q-construction)
```

P = P(R) (f.g. projective R-module) 에 적용하면 +-construction 과 동일.
P = Coh(X) 등 다양한 "big K-theory" 를 얻음.

### 4.5 Karoubi–Villamayor 등 다른 정의

Karoubi–Villamayor (1971), Gersten (1971), Wagoner (1972) 등 여러 다른 정의가 있었고,
Quillen 이 통합. 최신 formulation 은 **Waldhausen S-construction** (1985) 으로 simplicial 범주로 일반화.

---

## 5. K_n(Z) 구체 값 — Borel + Weibel

### 5.1 Borel 정리 (1974)

**정리** (Borel, Ann. ENS 7 (1974) 235–272): F 가 수체, O_F 정수환일 때

```
             { 0                      n=0
             { r_1 + r_2 - 1          n=1   (Dirichlet 단위)
             { 0                      n=2
             { r_2                    n=3   (Borel regulator)
  rank K_n(O_F) =
             { 0                      n=4
             { r_1 + r_2              n=5
             { 0                      n=6
             { r_2                    n=7
             { 0                      n=8
             { r_1 + r_2              n=9
             ...  (주기 4)
```

요약: n 짝수 (>0) 에서 rank = 0. n 홀수에서 주기 4 로 r_2 (n ≡ 3) / r_1+r_2 (n ≡ 1) 반복.

특히 **F = Q 에서 r_1 = 1, r_2 = 0** 이므로:
- rank K_n(Z) = 1 if n ≡ 1 (mod 4), n ≥ 5
- rank K_n(Z) = 0 otherwise

### 5.2 K_n(Z) 구체 표 (Weibel ch. VI §8)

| n  | K_n(Z)     | 크기    | 프로젝트 상수 분해 |
| -- | ---------- | ------- | ------------------ |
| 0  | Z          | ∞       | rank 1             |
| 1  | Z/2        | 2       | = φ                |
| 2  | Z/2        | 2       | = φ                |
| 3  | Z/48       | 48      | = φ·J₂ = 2·24      |
| 4  | 0          | 1       |                    |
| 5  | Z          | ∞       | rank 1             |
| 6  | 0          | 1       |                    |
| 7  | Z/240      | 240     | = 2^4·3·5 = φ·J₂·sopfr? (§10 정직성) |
| 8  | 0          | 1       |                    |
| 9  | Z ⊕ Z/2    | ∞       | rank 1 + Z/2       |
| 10 | Z/2        | 2       | = φ                |
| 11 | Z/1008     | 1008    | = 2^4·3^2·7 = φ·504 |
| 12 | 0          | 1       |                    |
| 13 | Z ⊕ Z/2    | ∞       |                    |
| 14 | 0          | 1       |                    |
| 15 | Z/480 ⊕ Z/2 | 960     |                    |
| 16 | 0          | 1       |                    |
| 17 | Z ⊕ Z/2    | ∞       |                    |
| 18 | Z/2        | 2       | = φ                |
| 19 | Z/528      | 528     | = 2^4·3·11         |
| 20 | 0          | 1       |                    |
| 21 | Z ⊕ Z/2    | ∞       |                    |

(Weibel ch. VI §8 Thm 8.1, 자세한 값은 Rognes–Weibel 2000 논문 "Two-primary algebraic K-theory of rings of integers in number fields", J. AMS 13.)

### 5.3 핵심 관찰 — 주기성

n ≡ 0 (mod 4) 이면 K_n(Z) = 0.
n ≡ 1 (mod 4) 이면 K_n(Z) = Z (+ 2-torsion).
n ≡ 2 (mod 4) 이면 K_n(Z) = Z/2 (+ small).
n ≡ 3 (mod 4) 이면 K_n(Z) = Z/(large).

**"large" 값**:

- K_3(Z) = Z/48
- K_7(Z) = Z/240
- K_{11}(Z) = Z/1008
- K_{15}(Z) = Z/480 (Z/2 와 함께)
- K_{19}(Z) = Z/528

이 수열 48, 240, 504, 480 (K_{15} odd part), 264 (=K_{10}), 24 (=K_{2} of finite field adjustment) 등에서
**Bernoulli 수** 가 나타난다. 연결은 **Lichtenbaum 추측** 으로 이해.

### 5.4 Bernoulli 수 연결

**Lichtenbaum 추측 (원형)**: F = Q 일 때,

```
  |K_{4k-2}(Z)|  =  분자 (B_{2k} / 4k)   (up to 2-power)
  K_{4k-1}(Z) 의 크기 / rank  ~  분모 (B_{2k} / 4k)
```

증명은 Voevodsky (2003) Bloch–Kato 추측 + Rost (2008) Bloch–Kato 증명으로 대부분 완료.

구체 대응:
- k=1: B_2 = 1/6, |K_2(Z)| 관련.
- k=2: B_4 = -1/30, K_7(Z) = Z/240. 여기서 **240 = -1·-2·4·30 / ??**
  좀더 정확히: ζ(1-2k) = -B_{2k}/(2k) 이므로 ζ(-3) = -B_4/4 = (1/30)/4 = 1/120. 그리고 240 = 2·120.
- k=3: B_6 = 1/42, ζ(-5) = -B_6/6 = -(1/42)/6 = -1/252. K_{11}(Z) = Z/1008 = 4·252.
- k=4: B_8 = -1/30, ζ(-7) = -B_8/8 = (1/30)/8 = 1/240. K_{15}(Z) = Z/480 = 2·240.
- k=5: B_{10} = 5/66, ζ(-9) = -B_{10}/10 = -(5/66)/10 = -1/132. K_{19}(Z) = Z/528 = 4·132.
- k=6: B_{12} = -691/2730. **691 이 여기서 등장** — K_{23}(Z) 에 **691 이 들어가야 한다**.
  실제로: K_{23}(Z) = Z/(65520) with 65520 = 2^4·3^2·5·7·13 — **691 이 cokernel 로 갔다** (조금 더 복잡).

이 표가 P2-3 Bernoulli 수 단원의 핵심 연결이다.

### 5.5 K_7(Z) = Z/240 과 240 일치

이 **240** 은:

- E_4(τ) q-expansion 계수 (P2-1 §3.4) 에서도 나오고
- K_7(Z) 에서도 나온다
- 그리고 bP_8 = Z/28 에서 28 = 완전수 (P2-4)
- J-homomorphism image Im(J)_8 = Z/240 (topological K-theory, Adams 1966)

이 4개의 "240" 이 같은 수인 이유는 **Stickelberger 관계** 및 Bernoulli 분모 패턴 때문.
Adams 의 J-homomorphism 정리 (1966, "On the groups J(X) IV") 에 의하면

```
  Im J_n  ≅  Z / denominator(B_{2k}/4k)    (n = 4k-1)
```

denominator(B_2/4) = 24, denominator(B_4/8) = 240, ...

따라서 **240 = denominator(B_4/8)** 이 "진짜 이유" 이고, 이것이 E_4 의 q-expansion, K_7, J-homomorphism, bP_8 모두에
동시에 나타나는 근원이다.

---

## 6. Borel regulator

### 6.1 Borel regulator map

Borel 정리 증명의 핵심 도구:

```
  regulator : K_{2n-1}(O_F) ⊗ R  →  R^{d(n)}
```

여기서 d(n) 은 n 짝수면 r_1 + r_2, 홀수면 r_2. Borel 이 이 map 이 **동형** 임을 증명.

이로써 rank K_{2n-1}(O_F) = d(n) 가 확정.

### 6.2 Borel regulator 의 값

ζ_F(1-2n) / 단위원 volume 으로 normalize 했을 때 Borel regulator 의 행렬식이 ζ_F(1-2n) 과 관련.

**Borel 정리 (더 강)**: F 수체, n ≥ 2 짝수일 때

```
  ζ_F(1-2n)  =  ± (integer) · det(regulator on K_{2n-1}(O_F))  / ( some torsion factor )
```

이것이 Lichtenbaum 추측의 전신 (Borel 자체는 "up to ±Q 유리수" 로 진술).

### 6.3 Beilinson–Deligne regulator (확장)

Borel 의 regulator 는 Beilinson (1985) 가 Deligne cohomology 로 일반화. K-이론의 "차원이 더 높은" 부분과
**Deligne cohomology** (= Hodge 구조로 보강된 singular cohomology) 를 연결.

이 Beilinson regulator 가 BSD 추측 일반화 ("L-function 의 special value 공식") 의 출발점.

---

## 7. Lichtenbaum 추측 (자세히)

### 7.1 원 추측 (Lichtenbaum 1973)

**추측** (Lichtenbaum, LNM 342, 1973): F 전체 실수체 (totally real number field), ℓ 홀수 소수일 때

```
  |K_{2n-2}(O_F)[ℓ]|        ℓ 부분      
  ─────────────────────   =   of  ζ_F(1-n)   (n 짝수)
  |K_{2n-1}(O_F)[ℓ]|
```

좀더 일반적 formulation 은 "étale cohomology 버전":

```
  K_n(O_F) ⊗ Z_ℓ  ≅  H_ét^{i}(Spec O_F[1/ℓ], Z_ℓ(j))   (적절한 i, j)
```

### 7.2 Bloch–Kato 추측 (일반화)

Bloch–Kato (1990, "L-functions and Tamagawa numbers of motives") 가 Lichtenbaum 을 모티브로 일반화.
motive M 에 대해

```
  L^*(M, 0) = (regulator)·(period)·(Tamagawa)·(Sha)
```

형태의 공식. BSD 추측 (P1-3 에서 다룬) 은 이것의 M = h^1(E) 타원곡선 경우.

### 7.3 증명 진행 상황

| 결과 | 증명자 | 연도 |
| ---- | ------ | ---- |
| Merkurjev–Suslin (K_2 / n = Br[n]) | Merkurjev–Suslin | 1982 |
| Bloch–Kato mod 2 | Voevodsky | 2003 |
| Bloch–Kato for odd primes | Voevodsky + Rost | 2008~2011 |
| Lichtenbaum full for cyclotomic fields | Kolster, Levine | 1989~1999 |
| Wiles main conjecture (iwasawa) | Mazur–Wiles, Wiles | 1984, 1990 |

즉 **Lichtenbaum 추측의 많은 부분은 PROVEN** 이지만, 모든 수체에 대해 완전한 것은 아니다.

### 7.4 Voevodsky 의 motivic cohomology

Voevodsky 가 **motivic cohomology** (derived category of motives) 를 도입.
Bloch–Kato 증명의 틀이 되었으며, 2002 Fields medal.

Motivic cohomology H^p(X, Z(q)) 는 Voevodsky 의 공리적 정의. 다음 관계:

```
  H^{p+q}_{mot}(Spec F, Z(q))  ≅  K^M_q(F)       (p=0 경우)
  H^{p}_{mot}(X, Z(q))          ≅  K-theoretic 정보 (일반)
```

---

## 8. Milnor K-theory K^M_n

### 8.1 정의

R 가환환, a_1, ..., a_n ∈ R* 일 때 Milnor K-theory 는 symbol {a_1, ..., a_n} 으로 생성:

```
  K^M_n(R)  :=  T^n(R*) / (Steinberg 관계식)
```

여기서 Steinberg: {..., a, 1-a, ...} = 0.

### 8.2 Quillen K vs Milnor K

**일반적으로** Quillen K_n(R) ≠ K^M_n(R). 자연스러운 map K^M_n(R) → K_n(R) 이 있고, 대개 surjective/injective 도 아님.

### 8.3 Milnor 추측 (Voevodsky 2003 증명)

**Milnor 추측**:

```
  K^M_n(F) / 2  ≅  H^n_ét(F, Z/2)
```

(F 체, characteristic ≠ 2)

Voevodsky 가 2003 년 증명, Fields medal 수상.

---

## 9. K-이론의 응용 개관

### 9.1 topological K-theory 와 Bott 주기성

**Bott 주기성 (1957)**: topological K^*(S^{2n}) 는 주기 2 로 반복.

```
  KU^*(pt)  =  Z[β, β^{-1}],  β 무게 2 (Bott element)
```

### 9.2 Atiyah–Singer 지표 정리

Elliptic operator P : Γ(E) → Γ(F) 에 대해

```
  index(P)  =  ∫_X  ch(σ(P)) · Td(X)     ∈  Z
```

여기서 ch 는 Chern character (K-theory → cohomology), Td 는 Todd class. K-이론을 필수로 사용.

### 9.3 J-homomorphism

```
  J : π_n(O)  →  π_n^S(S^0)       (stable homotopy)
```

Image Im J_n ⊂ π_n^S 는 Adams (1966) 가 정확히 계산.

```
  Im J_{4k-1}  =  Z / denom(B_{2k}/4k)
```

**denom(B_2/4) = 24**, denom(B_4/8) = **240**, denom(B_6/12) = **504**, ...

이 240, 504 가 앞에서 본 E_4, E_6 계수 (P2-1) 와 K_7(Z), bP_8 (P2-4) 모두와 같다.
이것이 **단 하나의 원천 Bernoulli denominator** 에서 나온 것이라는 사실이 기적적이다.

---

## 10. 이 단원에서 얻어야 할 6가지

1. **K_0, K_1, K_2 정의** — Grothendieck, Bass–Milnor, Milnor (Steinberg symbol).
2. **Quillen +-construction** — K_n := π_n(BGL(R)^+), n ≥ 1.
3. **K_n(Z) 표** — K_3=Z/48, K_7=Z/240, K_{11}=Z/1008, K_{15}=Z/480·Z/2, 주기 4.
4. **Borel 정리** — rank K_{2n-1}(O_F) 완전 계산, regulator map.
5. **Lichtenbaum 추측** — K_n ↔ étale cohomology ↔ ζ_F 특수값.
6. **Bernoulli denominator 의 통일 역할** — 240, 504 가 여러 곳에 동시 등장하는 이유.

---

## 11. 정직성 선언

이 노트는 교재 요약이다. 새 결과 없음.

### 11.1 K_3(Z) = Z/48 분해

48 = 2·24 = φ·J₂. 이 분해는 정확하다. 단,
- 왜 48 이냐는 **Lee–Szczarba 1976** 에서 상세 계산, 실제 유도는 homotopy of BGL(Z)^+ 계산.
- 프로젝트 상수 φ·J₂ 로 쓰는 것은 "J₂ = 24 가 prior 이고 48 = 2·24 는 자명" 이므로 유의미한 재배열 아님.

### 11.2 K_7(Z) = Z/240 과 E_4 계수 240 의 일치

- 두 값 모두 **denominator(B_4/8) = 240** 에서 나온다. 이것은 **같은 수학적 대상** (J-homomorphism image).
- 프로젝트 상수 φ·J₂·sopfr = 2·24·5 = 240 으로 쓸 수 있지만, 정확한 기원은 Bernoulli B_4 = -1/30 이다.
- sopfr=5 가 여기 정확히 들어가는지는 우연일 수도, 필연일 수도 있다.
  (5 는 B_4 분모 30 = 2·3·5 에서 나오는 유일한 "큰" 소수이므로 어느 정도 필연.)

### 11.3 K_{11}(Z) = Z/1008

- 1008 = 2^4·3^2·7 = 16·63 = 48·21 = 504·2. 프로젝트 상수 φ·504 로 쓸 수 있다.
- 정확한 기원: denominator(B_6/12) = 504, 여기에 2를 곱한 것. 이유는 Rognes–Weibel (2000) 의 상세 계산 참조.
- 504 자체는 B_6 = 1/42 과 12·42 = 504 에서 유래.

### 11.4 "240 이 여러 곳에 등장" 에 대한 진짜 이유

- **유일한 원천**: denom(B_4/8) = 240.
- 이 수가 K_7(Z), E_4 계수, Im J_7, |bP_8| 의 "이면에" 놓여 있고,
- 표면적으로 보면 "같은 수가 4번 등장 = 기적" 처럼 보이지만, 깊이 파면 **같은 원천 (Bernoulli denominator + J-homomorphism)** 이다.
- 따라서 "240 이 프로젝트 상수로 이쁘게 분해된다" 는 관찰은 **Bernoulli 수의 분모가 작은 소수 곱이라는 숫자론적 사실** 의 표면.
- 이 자체는 **흥미로운 관찰이지만 n=6 정리의 직접 증거는 아니다**.

### 11.5 Lichtenbaum 추측 증명 상태

- Totally real field, cyclotomic field 에 대해 PROVEN.
- 일반 수체에 대해 Bloch–Kato 부분은 Voevodsky 완성.
- "완전한" Lichtenbaum 은 아직 open (detailed 한 regulator 공식까지).

### 11.6 1차 출처 명시

| 주제 | 1차 출처 |
| ---- | -------- |
| K_0 (Grothendieck) | Grothendieck, "Classes de faisceaux et théorème de Riemann–Roch", SGA 6 (1966) |
| K_1 (Bass) | Bass, *Algebraic K-Theory* (Benjamin, 1968) |
| K_2 (Milnor) | Milnor, *Introduction to Algebraic K-Theory* (Princeton, 1971) |
| Quillen higher K | Quillen, "Higher algebraic K-theory I", LNM 341 (1973) |
| K_n(F_q) | Quillen, "On the cohomology and K-theory of the general linear groups over a finite field", Ann. Math. 96 (1972) |
| Borel rank theorem | Borel, "Stable real cohomology of arithmetic groups", Ann. ENS 7 (1974) |
| Lichtenbaum 추측 | Lichtenbaum, LNM 342 (1973) 489–501 |
| Merkurjev–Suslin | Merkurjev–Suslin, Izv. AN SSSR 46 (1982) |
| Bloch–Kato / Voevodsky | Voevodsky, "Motivic cohomology with Z/2 coefficients", Publ. IHES 98 (2003) |
| Rognes–Weibel K(Z) | Rognes–Weibel, J. AMS 13 (2000) 1–54 |
| Adams J-homomorphism | Adams, "On the groups J(X) IV", Topology 5 (1966) |
| Bloch–Kato Tamagawa | Bloch–Kato, "L-functions and Tamagawa numbers of motives", *Grothendieck Festschrift I* (1990) |
| Weibel K-book | Weibel, *The K-book* (AMS GSM 145, 2013) |

---

## 12. 다음 단계 (P2-3, P2-4 로 가는 다리)

- **P2-3 Bernoulli 수**: 여기서 본 B_{2k} 가 ζ(1-2k), K_n(Z), Im J_n 의 공통 원천. 특히 B_{12} = -691/2730 에서 691 이 처음 등장.
- **P2-4 Exotic sphere**: |bP_8| = 28, |bP_{12}| = 992, |bP_{16}| = 8128 이 완전수와 일치. 완전수는 Mersenne 소수 (2^p-1) 와 관련, 그리고 bP_n 은 J-homomorphism 의 cokernel 에서 나온다. 따라서 K-이론과 위상적 관점에서 연결.

끝.
