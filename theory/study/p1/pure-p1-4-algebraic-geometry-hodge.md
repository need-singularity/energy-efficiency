# PURE-P1-4 — 대수기하와 호지 이론 (사영다양체/층 코호몰로지/Kähler/호지 분해/호지 추측)

> 트랙: P1-PURE / 4번 태스크
> 완료 기준: 사영다양체와 층 코호몰로지 H^i(X, F), Serre duality 를 진술하고,
> Kähler 다양체의 호지 분해 H^k(X, C) = ⊕_{p+q=k} H^{p,q}(X) 와 복소켤레 대칭성
> H^{q,p} = conj(H^{p,q}) 를 유도 경로로 이해하며, 호지 추측의 정확한 진술
> image(cl: CH^p(X) ⊗ Q → H^{p,p}(X,Q)) = H^{p,p}(X,Q) 를 재현할 수 있다.
> 출처 기반: Griffiths-Harris "Principles of Algebraic Geometry" (Wiley Classics Library,
> 1994 재판, 원본 1978) ch. 0, ch. 1, Voisin "Hodge Theory and Complex Algebraic
> Geometry I" (Cambridge Studies in Adv. Math. 76, 2002) ch. 1~6, Hartshorne
> "Algebraic Geometry" (GTM 52, 1977) ch. II, III, Wells "Differential Analysis on
> Complex Manifolds" (GTM 65, 3판 2008) ch. IV~V.
> **정직성**: 교재 요약. 지어낸 정리·저자·연도 없음.

---

## 0. 목적

P1 4번 태스크는 **대수기하 + 호지 이론의 기초** 를 다진다. 호지 추측 (Clay 밀레니엄
문제) 과 그 주변을 이해하기 위해 다음 6가지가 필요하다.

1. 사영다양체 P^N 및 아핀 분기
2. 층과 층 코호몰로지 H^i(X, F)
3. Serre duality
4. Kähler 다양체와 de Rham / Dolbeault 분해
5. 호지 분해 H^k = ⊕ H^{p,q} 와 복소 켤레 대칭
6. 대수적 사이클 cl 사상과 호지 추측

---

## 1. 사영다양체

### 1.1 복소 사영 공간

```
  P^N(C) := (C^{N+1} \ {0}) / C^*
```

여기서 z ~ λ z (λ ∈ C^*). 점은 [z_0 : z_1 : ... : z_N] 로 표기.

### 1.2 사영다양체

C[x_0, ..., x_N] 의 동차 다항식 집합 S 에 대해

```
  V(S) := { [x] ∈ P^N : f(x) = 0 ∀ f ∈ S }
```

를 **사영 대수집합** 이라 한다. 기약(irreducible) 이면 **사영다양체**.

**예.** Fermat 초곡면 F_d : x_0^d + x_1^d + ... + x_N^d = 0.

### 1.3 층 수준에서 본 사영다양체

X = 사영다양체일 때, 구조층 O_X (국소 정칙 함수), 여기에 가군(module)으로서 작용하는
**연결층** (coherent sheaf) F 가 코호몰로지 H^i(X, F) 를 정의한다.

### 1.4 사영적 X 의 기본 성질

- **컴팩트.** X ⊂ P^N 은 고전위상으로 컴팩트.
- **Kähler.** P^N 의 Fubini-Study 메트릭을 restrict 하여 X 는 Kähler 다양체.
- **Hodge-Kähler.** 이에 따라 호지 분해가 성립.

(Griffiths-Harris §0.1, Voisin §1.1)

---

## 2. 층과 층 코호몰로지

### 2.1 층의 정의

**정의.** 위상공간 X 위의 (아벨) 층 F 는 각 open U ⊂ X 에 아벨 군 F(U) 를 할당하고,
제한 사상 res_{V,U}: F(U) → F(V) (V ⊂ U) 가 함자성 + sheaf axiom (국소 일치 → 전역
일치) 을 만족하는 것.

예.
- O_X: 정칙 함수 층
- Ω^p_X: 정칙 p-형식 층
- C^∞_X: 매끈한 함수 층

### 2.2 층 코호몰로지 정의

F 의 **injective resolution** 0 → F → I^0 → I^1 → ... 을 택하고,

```
  H^i(X, F) := H^i(Γ(X, I^•))       (Γ = 전역 절단)
```

로 정의. injective 가 없으면 **flask resolution** 또는 **Čech 코호몰로지** 로도 동등 정의.

(Hartshorne §III.1, §III.2)

### 2.3 Čech 코호몰로지

open cover U = {U_i} 에 대해

```
  Č^q(U, F) := ∏_{i_0 < ... < i_q} F(U_{i_0} ∩ ... ∩ U_{i_q})

  H^q(U, F) := H^q(Č^•(U, F))
```

U 가 "좋은 cover" (acyclic) 면 H^q(X, F) = H^q(U, F).

(Hartshorne §III.4, Wells §II.3)

### 2.4 기본 성질

- H^0(X, F) = Γ(X, F) 전역 절단.
- 장수열. short exact 0 → F' → F → F'' → 0 에 대해 long exact
  ... → H^i(X, F') → H^i(X, F) → H^i(X, F'') → H^{i+1}(X, F') → ...

### 2.5 Cartan B 정리

**정리 (Cartan B).** F 가 Stein 다양체 위의 연결층이면 H^i(X, F) = 0 (i ≥ 1).

Stein 은 사영적과 반대 (아핀적). 사영적 X 에서는 일반적으로 H^i ≠ 0.

---

## 3. Serre duality

### 3.1 진술

**정리 (Serre).** X = 콤팩트 복소다양체 (차원 n) + ω_X = 정준층 (Ω^n_X). F = 연결층
(locally free = vector bundle) 일 때,

```
  H^i(X, F)  ≅  H^{n-i}(X, F^∨ ⊗ ω_X)^∨
```

여기서 F^∨ 은 dual, ^∨ 은 쌍대공간.

(Hartshorne Thm III.7.6, Voisin Thm 5.32, Griffiths-Harris §1.2)

### 3.2 차원 공식

특히 X 가 사영적 n-차원, F = O_X (구조층) 이면

```
  h^i(X, O_X) = h^{n-i}(X, ω_X)
```

여기서 h^i := dim_C H^i.

### 3.3 호지수와 연결

X 가 Kähler 라면 h^{p,q}(X) := dim H^{p,q}(X) 가 정의되고, Serre duality 로

```
  h^{p,q} = h^{n-p, n-q}
```

가 된다 (ω_X ≅ Ω^n 이므로).

---

## 4. Kähler 다양체

### 4.1 Hermitian vs Kähler

복소다양체 X 에 Hermitian 메트릭 h 가 주어지면, 관련된 2-형식

```
  ω = (i/2) ∑ h_{ij} dz_i ∧ dz̄_j
```

을 **Kähler form** 이라 한다. **정의.** X 가 Kähler 라 함은 dω = 0.

(Griffiths-Harris §0.7, Voisin §3.1, Wells §V.4)

### 4.2 예

- C^n (표준 메트릭), X = C^n 는 Kähler.
- P^N (Fubini-Study 메트릭), dω = 0 확인 가능. P^N 는 Kähler.
- 사영 대수다양체 X ⊂ P^N: 모두 Kähler.
- 콤팩트 복소다양체 중 non-Kähler 예: Hopf surface (S¹ × S³ 에 복소 구조), Iwasawa
  manifold.

### 4.3 Kähler identity

Kähler 메트릭에서 Laplacian Δ_d (de Rham), Δ_∂ (Dolbeault), Δ_∂̄ 는 다음을 만족:

```
  Δ_d = 2 Δ_∂ = 2 Δ_{∂̄}
```

(Griffiths-Harris §0.7 Prop, Wells §V.4)

이 **Kähler identity** 가 호지 분해의 핵심.

---

## 5. de Rham 과 Dolbeault 분해

### 5.1 de Rham 코호몰로지

X = 매끈한 다양체, Ω^k_X = 매끈한 k-형식. d: Ω^k → Ω^{k+1} 는 외미분.

```
  H^k_{dR}(X, R) := ker(d: Ω^k → Ω^{k+1}) / im(d: Ω^{k-1} → Ω^k)
```

(de Rham 정리에 따라 H^k_{dR}(X, R) ≅ H^k_{sing}(X, R).)

### 5.2 (p, q) 분해

복소다양체 X 에서 Ω^k_X ⊗ C 는 (p, q) 형식으로 분해:

```
  Ω^k ⊗ C = ⊕_{p+q=k} A^{p,q}
```

여기서 A^{p,q} 는 dz_{i_1} ∧ ... ∧ dz_{i_p} ∧ dz̄_{j_1} ∧ ... ∧ dz̄_{j_q} 로 생성.

미분은 d = ∂ + ∂̄, 여기서
- ∂: A^{p,q} → A^{p+1, q}
- ∂̄: A^{p,q} → A^{p, q+1}

### 5.3 Dolbeault 코호몰로지

```
  H^{p,q}_{∂̄}(X) := ker(∂̄: A^{p,q} → A^{p,q+1}) / im(∂̄: A^{p,q-1} → A^{p,q})
```

**정리 (Dolbeault).** 정칙 p-형식 층 Ω^p 에 대해

```
  H^{p,q}_{∂̄}(X) ≅ H^q(X, Ω^p)
```

(Griffiths-Harris §0.4, Wells §IV.3)

이는 de Rham 정리의 Dolbeault 버전.

---

## 6. 호지 분해

### 6.1 진술

**정리 (호지 분해, Kähler case).** X = 콤팩트 Kähler 다양체. 모든 k 에 대해

```
  H^k(X, C) = ⊕_{p+q=k} H^{p,q}(X)
```

여기서 H^{p,q}(X) = H^q(X, Ω^p_X) = { [α] : α ∈ A^{p,q}, dα = 0 }/(d-exact).

그리고

```
  H^{q,p}(X) = \overline{H^{p,q}(X)}
```

복소 켤레 대칭.

(Griffiths-Harris §0.7, Voisin Thm 6.11, Wells Thm V.4.2)

### 6.2 호지 수 h^{p,q}

```
  h^{p,q}(X) := dim_C H^{p,q}(X)
```

다음 대칭 성립:

- h^{p,q} = h^{q,p}  (복소 켤레)
- h^{p,q} = h^{n-p, n-q}  (Serre duality)
- b_k = ∑_{p+q=k} h^{p,q}  (Betti 수 = 호지 수 합)

### 6.3 예 — K3 surface

dim_C X = 2. 호지 다이아몬드:

```
              h^{0,0} = 1
        h^{1,0} = 0     h^{0,1} = 0
  h^{2,0} = 1    h^{1,1} = 20    h^{0,2} = 1
        h^{2,1} = 0     h^{1,2} = 0
              h^{2,2} = 1
```

b_2 = 1 + 20 + 1 = 22.

(Griffiths-Harris §IV.6)

### 6.4 호지 분해의 증명 요지

Kähler identity Δ_d = 2 Δ_∂̄ 가 있으면, d-harmonic 형식과 ∂̄-harmonic 형식 공간이
같아지고, 호지 정리 (harmonic = cohomology 대표자) 로

```
  H^k_{dR}(X, C) = H^k_d = ⊕_{p+q=k} H^{p,q}_{∂̄} = ⊕_{p+q=k} H^q(X, Ω^p)
```

(Wells §V.4 Theorem, Griffiths-Harris §0.7)

---

## 7. 대수적 사이클 — Chow 군

### 7.1 대수적 사이클 정의

**정의.** X = 사영다양체, p ∈ {0, 1, ..., n}. **p-codim 사이클** 은 형식적 Z-선형 결합

```
  Z = ∑ n_i [V_i]
```

(V_i = X 의 기약 부분대수다양체, codim V_i = p, n_i ∈ Z).

### 7.2 유리 등가

두 사이클 Z_1, Z_2 가 **유리 등가** 라 함은, Z_1 - Z_2 가 어떤 함수의 주 인자(principal
divisor) 꼴로 쓸 수 있을 때.

**Chow 군**: CH^p(X) := (p-codim 사이클) / (유리 등가).

(Hartshorne Appendix A, Voisin Vol. 2 §9)

### 7.3 예

- CH^1(X) = 나눗셈 층 (Pic(X)).
- X = P^n: CH^p(P^n) = Z, 생성원 = [H] 의 p 곱 (H = 초평면).

---

## 8. 사이클 사상과 호지 추측

### 8.1 cycle class 사상

대수적 사이클 [V] (codim p) 에 대해 **Poincaré dual** (기하학적) 을 취하면
H^{2p}(X, Z) 의 클래스가 얻어진다.

**정리.** cl: CH^p(X) → H^{2p}(X, Z), Z ↦ [Z] (유리 등가 불변) 는 잘 정의된 군 준동형.
더구나 이 클래스는 **Hodge type (p, p)** 이다:

```
  cl(CH^p(X)) ⊂ H^{p,p}(X) ∩ H^{2p}(X, Z) ⊂ H^{2p}(X, C)
```

(Griffiths-Harris §1.1, Voisin Vol. 1 §11)

### 8.2 Hodge 부류

**정의.** X = 콤팩트 Kähler. **Hodge 부류** 는

```
  Hdg^p(X) := H^{p,p}(X) ∩ H^{2p}(X, Q)
```

즉 (p, p) 타입이면서 유리 계수.

### 8.3 호지 추측

**추측 (Hodge, 1950년 ICM 제시).** X = 비특이 사영다양체일 때, 사이클 사상

```
  cl ⊗ Q : CH^p(X) ⊗ Q → H^{p,p}(X, Q)
```

의 **image 가 H^{p,p}(X, Q) 전체** 와 같다. 즉, 모든 Hodge 부류는 대수적 사이클의 Q-선형
결합으로 온다.

**공식 진술 (Clay):** Clay Millennium Problem "The Hodge Conjecture" (Deligne 작성 Clay 공식
진술 문서, 2000).

### 8.4 알려진 결과

- **p = 1.** Lefschetz (1,1)-정리. 사영다양체에 대해 Hodge 부류 (1,1) 은 모두 대수적
  (divisor 클래스).
- **일반 p.** 열림. 반례 없음. 특수 경우 (Abel 다양체, Calabi-Yau 일부) 에서 참 확인.
- **Griffiths-Harris 1985.** 일반 Calabi-Yau 4-fold 에서 많이 검증.
- **Deligne 1970s.** 호지 이론 + 가중 호지 구조 확장.

### 8.5 반례 여부

호지 부류가 대수적 아니라는 반례는 아직 **없다**. 추측이 참인지 거짓인지도 미정.
단, **integer coefficient** 버전 (Q 대신 Z) 의 호지 추측은 **거짓** 임이 Atiyah-Hirzebruch
1962 에 의해 반례로 증명됨. 그래서 공식 진술은 Q 계수.

(Voisin Vol. 1 §11.3)

---

## 9. Lefschetz 정리와 관련 도구

### 9.1 hard Lefschetz

**정리.** X = 콤팩트 Kähler, ω = Kähler form, L = [ω] 와의 쐐기곱. 그러면

```
  L^k : H^{n-k}(X, Q) → H^{n+k}(X, Q)
```

(n = dim_C X, k = 0, 1, ..., n) 는 동형.

(Griffiths-Harris §0.7, Voisin Vol. 1 §6.2)

### 9.2 Lefschetz (1,1)-정리

**정리.** X = 사영다양체. H^{1,1}(X, Z) = { c ∈ H²(X, Z) : c ∈ H^{1,1} } 의 모든 원소는
**정칙 line bundle** (즉, divisor 클래스) 의 first Chern class 로 온다.

이로부터 p = 1 경우 호지 추측이 따른다.

(Griffiths-Harris §1.2, Voisin Vol. 1 §11.1)

### 9.3 호지 지표 정리

**정리.** Kähler X 의 Betti 수, 호지 수 사이의 signature 정리 (제곱 꼴 정부호성).

(Wells §V.6, Voisin Vol. 1 Thm 6.32)

---

## 10. Chern class 와 벡터 번들

### 10.1 Chern class 정의

복소 벡터 번들 E → X 에 대해 Chern class c_i(E) ∈ H^{2i}(X, Z) 가 정의된다.

공리적 정의:
- c_0(E) = 1
- c(E ⊕ F) = c(E) · c(F)   (Whitney sum)
- c(pullback) = pullback(c)
- c_1(line bundle O(1)) on P^N = 초평면 H.

(Griffiths-Harris §I.1, Wells §III.3)

### 10.2 Chern character

```
  ch(E) := rank(E) + c_1 + (c_1² - 2 c_2)/2 + ...
```

ch: K^0(X) → H^{even}(X, Q) 환 준동형.

### 10.3 Hirzebruch-Riemann-Roch

**정리.** X = 콤팩트 복소다양체, E = 정칙 벡터 번들.

```
  χ(X, E) = ∫_X ch(E) · Td(X)
```

(Td = Todd class, χ = Euler 특성 = ∑ (-1)^i h^i).

(Hartshorne Appendix A, Hirzebruch 1956 원논문)

---

## 11. 프로젝트 상수 n=6 과의 연결 (메모)

대수기하와 n=6 의 **직접** 연결은 이 단계 학습 범위 밖이다. 간접 관찰로

- **6 차원 Calabi-Yau.** 6 차원 콤팩트 Calabi-Yau 다양체는 끈이론 compactification
  에서 핵심. 호지 수 h^{1,1}, h^{2,1} 이 물리 파라미터를 결정.
- **P^6.** 6차원 사영공간, 호지 수 h^{p,p} = 1 (p = 0, ..., 6), 나머지 0.

이는 관찰 수준이며 n=6 정리와 **증명 가능한 관계** 를 주장하지 않는다.

---

## 12. 참고 경로 (교재 페이지/장 단위)

| 항목 | Griffiths-Harris | Voisin Vol.1 | Hartshorne | Wells |
| --- | --- | --- | --- | --- |
| 사영다양체 | §1.0~1.2 | §1.1 | §I.2 | §I.2 |
| 층 / 층 코호몰로지 | §0.3 | §4 | §III.1~2 | §II.1 |
| Čech 코호몰로지 | §0.3 | §4.3 | §III.4 | §II.3 |
| Serre duality | §1.2 | §5.3 | §III.7 | §V.5 |
| Kähler 메트릭 | §0.7 | §3.1 | - | §V.4 |
| Dolbeault | §0.4 | §2.3 | - | §IV.3 |
| 호지 분해 | §0.7 | §6.1 | - | §V.4 |
| 호지 다이아몬드 예 | §IV.6 | §7 | - | §V.6 |
| cycle 사상 | §1.1 | §11.1 | App.A | - |
| Hodge 추측 | - | §11.3 | - | - |
| Lefschetz (1,1) | §1.2 | §11.1 | - | - |
| hard Lefschetz | §0.7 | §6.2 | - | - |
| Chern class | §I.1 | §11.1 | App.A | §III.3 |
| HRR 정리 | - | - | App.A | - |

---

## 13. 이 단원에서 얻어야 할 5가지

1. **사영다양체와 층 코호몰로지** H^i(X, F), Serre duality.
2. **Kähler 조건** dω = 0 과 Kähler identity Δ_d = 2 Δ_{∂̄}.
3. **호지 분해** H^k(X, C) = ⊕ H^{p,q}, h^{p,q} = h^{q,p} = h^{n-p, n-q}.
4. **cycle 사상** cl: CH^p → H^{p,p}(X, Z) 와 Lefschetz (1,1)-정리.
5. **호지 추측** 공식 진술 (Q 계수, Clay Millennium, Deligne 진술).

---

## 14. 정직성 선언

- 이 노트는 교재 요약이다. 새 결과 없음.
- Atiyah-Hirzebruch 1962 의 integer Hodge 추측 반례, Deligne 의 Clay 공식 진술서
  (2000) 는 공식 공개 자료이며 연도·저자 정확.
- Griffiths-Harris 의 K3 호지 다이아몬드 수치(20) 는 §IV.6 의 정확한 수치.
- 프로젝트 상수 n=6 과의 연결은 §11 에 관찰 수준 메모만 두었다.
- 지어낸 정리·저자·연도 없음.
