# PURE-P1-2 — 타원곡선과 모듈러 형식 (Weierstrass/Mordell-Weil/L-함수/모듈러성)

> 트랙: P1-PURE / 2번 태스크
> 완료 기준: Weierstrass 방정식에서 군법칙(chord-tangent) 유도, Mordell-Weil 정리
> E(Q) = Z^r ⊕ T 의 진술·증명 뼈대, L(E,s) 의 Euler 곱 정의, 타니야마-시무라-와일스
> 모듈러성 정리의 정확한 진술을 말할 수 있다.
> 출처 기반: Silverman "The Arithmetic of Elliptic Curves" (GTM 106, 2판 2009) ch. 1~5, 8,
> Diamond-Shurman "A First Course in Modular Forms" (GTM 228, 2005) ch. 1~5, 8,
> Koblitz "Introduction to Elliptic Curves and Modular Forms" (GTM 97, 2판 1993) ch. 1~3.
> **정직성**: 이 파일은 교재 요약이다. 모든 정리·공식·저자·연도는 위 3개 교재 기준.
> 프로젝트 상수(n=6 등)와의 연결은 §11 메모 수준이며 증명은 포함하지 않는다.
> 지어낸 정리·저자는 없다.

---

## 0. 목적

P1 학습 로드맵 2번 태스크는 **타원곡선 + 모듈러 형식** 을 다진다. BSD 추측(P3)·Fermat
마지막 정리(Wiles, 이미 증명)·Langlands 프로그램(P3)·Sato-Tate(P3) 등 모든 상위 주제의
공통 기반이므로, 아래 6가지를 숙지한다.

1. Weierstrass 방정식, 판별식 Δ, j-불변식
2. 군법칙 (chord-tangent), 단위원 O (무한점)
3. Mordell-Weil 정리 E(Q) = Z^r ⊕ T (r = rank, T = torsion)
4. L(E, s) 의 Euler 곱 정의와 해석적 연속
5. 모듈러 형식 M_k(Γ₀(N)), 신형식(newform)
6. 타니야마-시무라-와일스 모듈러성 정리

---

## 1. Weierstrass 방정식

### 1.1 아핀 좌표

체 K 위에서 **짧은(short) Weierstrass** 방정식:

```
  E:  y² = x³ + a x + b       (a, b ∈ K, char K ≠ 2, 3)
```

**판별식**

```
  Δ(E) = -16 (4 a³ + 27 b²)
```

**j-불변식**

```
  j(E) = -1728 · (4 a)³ / Δ = 1728 · 4 a³ / (4 a³ + 27 b²)
```

(Silverman §III.1 공식 III.1.1, III.1.2)

조건: Δ ≠ 0 이어야 곡선이 비특이(smooth). Δ = 0 이면 커스프나 노드가 생긴다.

### 1.2 일반 Weierstrass 방정식

char K ∈ {2, 3} 포함 일반형:

```
  E:  y² + a₁ x y + a₃ y = x³ + a₂ x² + a₄ x + a₆
```

a₁, a₂, a₃, a₄, a₆ ∈ K. 이 형태의 판별식은 훨씬 복잡하다 (Silverman §III.1 표).

### 1.3 사영완비화

사영 평면 P² 위의 동차 방정식:

```
  Y² Z = X³ + a X Z² + b Z³
```

무한점 O = [0 : 1 : 0] 이 유일한 무한점. E 의 군법칙 단위원이 바로 이 O.

---

## 2. 군법칙 — chord-tangent

### 2.1 기하 정의

E(K) 위의 두 점 P, Q 에 대해, **합 P + Q** 를 다음 절차로 정의한다.

1. P, Q 를 지나는 직선 ℓ 을 그린다 (P = Q 인 경우 P 에서의 접선).
2. ℓ 이 E 와 만나는 세 번째 교점을 R 이라 한다 (Bézout: 3차 곡선 × 직선 = 3점).
3. R 을 x축에 대해 반사(즉 y → -y). 그 결과가 P + Q.

### 2.2 대수 공식 — 짧은 Weierstrass

P = (x₁, y₁), Q = (x₂, y₂), P ≠ -Q 일 때:

x₁ ≠ x₂ (직선 기울기)
```
  λ = (y₂ - y₁) / (x₂ - x₁)
```

x₁ = x₂, y₁ = y₂ (접선 기울기)
```
  λ = (3 x₁² + a) / (2 y₁)
```

그리고

```
  x₃ = λ² - x₁ - x₂
  y₃ = λ (x₁ - x₃) - y₁
  P + Q = (x₃, y₃)
```

(Silverman §III.2, 정리 III.2.3)

### 2.3 군공리

**정리.** E(K) 는 이 연산 + 에 대해 **아벨 군** 이다. 단위원은 O, P 의 역원은
-P = (x, -y).

증명(결합법칙)은 기하로 Cayley-Bacharach 정리를 쓰거나, 대수로 유리함수 자코비안을
이용한다 (Silverman §III.3 Prop III.3.4).

### 2.4 Hasse 부등식

유한체 F_q 위의 타원곡선 E/F_q 에 대해

```
  |#E(F_q) - (q + 1)| ≤ 2 √q
```

a_p := p + 1 - #E(F_p) 라 놓으면 |a_p| ≤ 2 √p. 이 a_p 가 L-함수의 계수가 된다.
(Silverman §V.1 Thm V.1.1, Hasse 1934)

---

## 3. Mordell-Weil 정리

### 3.1 진술

**정리 (Mordell 1922; Weil 1928 일반체 일반화).** Q 위에 정의된 타원곡선 E 에 대해
E(Q) 는 유한 생성 아벨 군이다. 즉

```
  E(Q) = Z^r ⊕ E(Q)_tors
```

여기서 r ≥ 0 은 **랭크(rank)**, E(Q)_tors 는 유한 아벨 군 (**torsion 부분군**).

(Silverman §VIII.4 Thm VIII.4.1)

### 3.2 증명 뼈대

두 단계로 나뉜다.

1. **약한 Mordell-Weil 정리.** E(Q) / 2 E(Q) 는 유한군. (Kummer 이론 + 갈루아 코호몰로지)
2. **높이(height)의 descent.** 표준 높이 ĥ 를 정의하고 h(P) ≤ C · #{ ... } 와 같은
   descent 부등식을 써서 유한 생성을 결론.

(Silverman §VIII.1~VIII.4 참고, 4개 섹션 전체가 이 증명이다.)

### 3.3 torsion 부분군 — Mazur 정리

**정리 (Mazur 1977).** Q 위 타원곡선 E 의 torsion 부분군 E(Q)_tors 는 다음 15가지
중 정확히 하나와 동형이다:

```
  Z/n   (n = 1, 2, ..., 10, 12)
  Z/2 × Z/2n   (n = 1, 2, 3, 4)
```

(Silverman §VIII.7, 정리만 인용. 증명은 Mazur 의 깊은 모듈라 곡선 이론.)

### 3.4 rank — 미해결

**r 의 값은 각 E 에 대해 개별적으로 계산** 해야 하며, 일반적인 상한이나 분포 공식은
아직 없다. 알려진 최대 rank 예(2006 기준, Elkies) ≥ 28. 평균 rank (Bhargava-Shankar
2015) = 정확히 1 미만의 값이 알려짐 (0.885 이하 평균).

---

## 4. L-함수 L(E, s)

### 4.1 정의

각 소수 p 에 대해 local factor L_p(E, s) 를 정의한다.

**좋은 환원 (good reduction, p ∤ Δ 일 때):**

```
  L_p(E, s) = (1 - a_p p^{-s} + p^{1-2s})^{-1}
```

여기서 a_p = p + 1 - #E(F_p).

**나쁜 환원:**

- split multiplicative: L_p = (1 - p^{-s})^{-1}
- non-split multiplicative: L_p = (1 + p^{-s})^{-1}
- additive: L_p = 1

(Silverman §C.16 또는 "Advanced Topics in the Arithmetic of Elliptic Curves" §III.19)

### 4.2 global L-함수

```
  L(E, s) = ∏ L_p(E, s)
            p
```

**정리.** 이 곱은 Re(s) > 3/2 에서 절대수렴한다 (Hasse 부등식 |a_p| ≤ 2 √p 로부터).

### 4.3 conductor N

각 E 에 **conductor N(E) ∈ Z_{>0}** 이 정의된다:

- 좋은 환원 p ∤ N: L_p 는 위 공식대로
- multiplicative reduction: p ∥ N (정확히 한 번)
- additive reduction: p² | N (또는 더 큰 거듭제곱)

conductor 는 L-함수의 **functional equation 파라미터**.

### 4.4 completed L-함수

```
  Λ(E, s) = N^{s/2} (2π)^{-s} Γ(s) L(E, s)
```

**정리 (모듈러성의 귀결).** Λ(E, s) 는 전체 복소평면으로 해석적 연속하고

```
  Λ(E, s) = w · Λ(E, 2 - s)
```

를 만족한다. 여기서 w ∈ {±1} 은 **root number** (부호, 선택된 곡선에 따라 결정).

(Diamond-Shurman §5.10, Silverman "Advanced Topics" §C.16)

이 정리는 **모듈러성 정리의 직접적 결과**. 모듈러성 없이는 해석적 연속 자체도 알려지지
않았었다.

---

## 5. 모듈러 형식 기초

### 5.1 합동 부분군

```
  SL₂(Z) = { [[a,b],[c,d]] : a,b,c,d ∈ Z, ad - bc = 1 }

  Γ₀(N) = { [[a,b],[c,d]] ∈ SL₂(Z) : c ≡ 0 (mod N) }
```

N = 1 이면 Γ₀(1) = SL₂(Z).

### 5.2 모듈러 형식 정의

**정의.** 함수 f: H → C (H = 상반평면) 가 **무게 k, 수준 N 의 모듈러 형식** 이라 함은,
다음 세 조건을 만족할 때:

1. f 는 H 위에서 정칙(holomorphic).
2. 모든 γ = [[a,b],[c,d]] ∈ Γ₀(N) 에 대해
   ```
     f((a τ + b)/(c τ + d)) = (c τ + d)^k · f(τ)
   ```
3. f 는 cusp 에서 정칙(= 푸리에 전개가 유한한 negative 항을 가짐).

**cusp form.** cusp 에서의 값이 0 이면 cusp form 이라 부른다. 공간을 S_k(Γ₀(N)) 라고
쓴다.

(Diamond-Shurman §1.2, Koblitz §III.1)

### 5.3 푸리에 전개

τ ∈ H 일 때 q := e^{2π i τ}, 그러면 모듈러 형식은

```
          ∞
  f(τ) = ∑   a_n q^n
         n=0
```

형태의 q-전개. cusp form 은 a_0 = 0.

### 5.4 Hecke 연산자

각 소수 p 에 대해 T_p: S_k(Γ₀(N)) → S_k(Γ₀(N)) 가 정의된다 (Diamond-Shurman §5.2).
T_p 들은 서로 교환하며, 공통 고유벡터를 **고유형식(eigenform)** 이라 부른다.

**newform.** level N 의 고유형식 중에서 더 작은 level 에서 온 것이 아닌 것을
**신형식(newform)** 이라 한다.

신형식 f 에 대해 f 의 L-함수

```
          ∞
  L(f, s) = ∑   a_n n^{-s}   (a_n: f 의 푸리에 계수)
          n=1
```

는 Euler 곱을 갖는다:

```
  L(f, s) = ∏  (1 - a_p p^{-s} + p^{k-1-2s})^{-1}  ·  ∏  (1 - a_p p^{-s})^{-1}
         p∤N                                            p|N
```

(Diamond-Shurman Thm 5.9.2)

---

## 6. 모듈러성 정리 (Taniyama-Shimura-Weil)

### 6.1 진술

**정리 (Wiles 1995; Taylor-Wiles 1995; Breuil-Conrad-Diamond-Taylor 2001 완성).**
Q 위 모든 타원곡선 E 는 모듈러이다. 즉, conductor N(E) 인 신형식 f ∈ S_2(Γ₀(N(E)))
가 존재하여

```
  L(E, s) = L(f, s)
```

이 성립한다.

(Diamond-Shurman §8.8 참고, 증명은 인용만 하고 텍스트 자체는 본문)

### 6.2 역사 약사

- **Taniyama 1955.** 도쿄 국제수학자대회에서 "모든 타원곡선이 자기동형형식(automorphic
  form) 과 관련 있지 않을까" 를 질문 형태로 제시.
- **Shimura 1960 년대.** Taniyama 의 아이디어를 정리하고 엄밀화하여 **Shimura-Taniyama
  추측** 을 정식화.
- **Weil 1967.** L-함수 함수방정식 기준으로 재구성 (Weil 1967, 논문 'Über die
  Bestimmung Dirichletscher Reihen durch Funktionalgleichungen').
- **Frey 1986, Ribet 1986.** Frey 곡선 아이디어로 모듈러성이 Fermat 마지막 정리를
  함의한다는 것이 증명됨 (Ribet 의 level-lowering 정리).
- **Wiles 1994 (발표), 1995 (출간).** semistable 환경에서 모듈러성 증명. 이로써
  **Fermat 마지막 정리 증명**.
- **Taylor-Wiles 1995.** Wiles 증명의 갭(Hecke algebra argument) 완성.
- **Breuil-Conrad-Diamond-Taylor 2001.** 모든 타원곡선으로 확장하여 정리 완성.

(Diamond-Shurman §9 역사 섹션)

### 6.3 Fermat 마지막 정리와의 연결

**정리 (Fermat's Last Theorem, Wiles 1995).** n ≥ 3 에 대해 x^n + y^n = z^n 의 양의 정수해는
없다.

증명의 요지: 만약 a^p + b^p = c^p (p 홀수 소수, a, b, c 공배수 1) 해가 있다면,
**Frey 곡선** E_{a,b,c} : y² = x (x - a^p) (x + b^p) 을 만들 수 있다. Ribet 정리로
이 곡선이 모듈러라면 level 2 의 가중 2 cusp form 이 존재해야 하는데, S_2(Γ₀(2)) = 0
이므로 모순. 따라서 E_{a,b,c} 는 모듈러 아님. 하지만 Wiles 정리(semistable 모듈러성)는
이러한 곡선도 모듈러라고 말하므로, 모순이 생긴다. 따라서 해가 없다.

(Diamond-Shurman §9.4 스케치; Wiles 1995 원논문)

---

## 7. BSD 추측 (Birch-Swinnerton-Dyer)

### 7.1 약한 BSD

**추측.** E(Q) 의 rank r 는 L(E, s) 의 s = 1 에서의 영점 차수와 같다:

```
  r = ord_{s=1} L(E, s)
```

### 7.2 강한 BSD

**추측 (full BSD).**

```
                                                Ω_E · Reg_E · #Ш(E)
  lim (s-1)^{-r} L(E, s)  =  ─────────────────────────────── · ∏ c_p
  s → 1                                        #E(Q)_tors²                p|N
```

여기서
- Ω_E: real period,
- Reg_E: Néron-Tate regulator,
- Ш(E): Tate-Shafarevich 군,
- c_p: Tamagawa 수.

(Clay Mathematics Institute 공식 진술, Wiles 의 공식 밀레니엄 문제 기술서)

### 7.3 알려진 부분 결과

- **Coates-Wiles 1977.** CM 타원곡선에 대해 L(E, 1) ≠ 0 이면 rank r = 0.
- **Gross-Zagier 1986.** L(E, s) 가 s = 1 에서 단순 영점이면 ĥ(Heegner point) 와
  L'(E, 1) 관계식 성립.
- **Kolyvagin 1990.** ord_{s=1} L(E,s) ≤ 1 인 경우 약한 BSD 참 (모듈러 E 에 대해).
- **Bhargava-Shankar 2010~2015.** 평균 rank 유한 추정, 양의 비율 E 가 rank 0 또는 1.

(Silverman §X.5, Diamond-Shurman §9.5)

---

## 8. 합동수 문제 (connection to n=6?)

### 8.1 합동수 정의

양의 정수 n 이 **합동수(congruent number)** 라 함은 세 변 길이가 모두 유리수이고
넓이가 정확히 n 인 직각삼각형이 존재할 때.

(예: 5, 6, 7 은 합동수. 5 는 변 3/2, 20/3, 41/6. 6 은 변 3, 4, 5 — 넓이 6.)

### 8.2 타원곡선과의 등가

**정리.** n 이 합동수 ⟺ 타원곡선 E_n: y² = x³ - n² x 의 rank ≥ 1.

(Koblitz §I.1, Tunnell 1983)

### 8.3 Tunnell 정리

**정리 (Tunnell 1983).** BSD 를 가정하면, n 이 합동수인지 판별하는 **다항시간 알고리즘**
이 존재한다.

이 정리는 BSD 의 실용적 강력함을 보여준다.

---

## 9. complex multiplication (CM)

### 9.1 정의

타원곡선 E/K 가 **complex multiplication (CM)** 을 가진다 함은, End(E) ⊗ Q 가 유리수체 Q
보다 크고, 어떤 허수 이차체 K 와 동형일 때.

### 9.2 예

- y² = x³ - x : End = Z[i] (Gauss 정수), CM.
- y² = x³ - 1 : End = Z[ω] (ω = e^{2π i/3}), CM.

### 9.3 CM 곡선의 L-함수

CM 곡선의 L-함수는 **Hecke 지표 L-함수** 와 같아진다. 이를 통해 해석적 연속·함수방정식이
Deuring 정리(1950 년대)로 Wiles 없이 증명된다.

(Silverman "Advanced Topics" ch. II)

---

## 10. isogeny 와 동치류

### 10.1 정의

**isogeny** φ: E → E' 는 유한 kernel 을 가진 군 준동형 (regular map). 차수 deg(φ)
= |ker φ|.

### 10.2 dual isogeny

**정리.** deg(φ) = n 인 isogeny φ 에 대해 dual isogeny φ̂ : E' → E 가 존재하고
φ ∘ φ̂ = [n] (곱셈 n) 이 성립.

(Silverman §III.6)

### 10.3 ℓ-adic Tate 모듈

```
  T_ℓ(E) := lim_{←} E[ℓ^n]       (inverse limit over E[ℓ^n] = {ℓ^n-torsion})
```

T_ℓ(E) 는 Z_ℓ 위 rank 2 자유 모듈. Galois 군 G_Q = Gal(Q̄/Q) 가 T_ℓ(E) 위에 작용.

Tate 모듈은 L-함수의 Galois 표현 해석의 기초.

---

## 11. 프로젝트 상수와의 연결 (메모만)

프로젝트 상수 σ(6) = 12, φ(6) = 2, τ(6) = 4, sopfr(6) = 5, J₂(6) = 24 는 타원곡선과
**직접** 관련이 없다. 다만 다음 간접 연결이 P2·P3 노트의 연구 대상이 될 수 있다.

- **합동수 6.** n = 6 은 가장 작은 합동수 (Koblitz §I.1). 삼각형 (3, 4, 5) 의 넓이
  = 6. 이 사실은 타원곡선 E_6 : y² = x³ - 36 x 의 rank ≥ 1 과 등가. 실제 rank = 1.
- **Siegel 모듈러 형식의 가중 6.** cusp form 공간 S_6(SL₂(Z)) 의 차원, Ramanujan Δ
  의 가중 12 (= 2 × 6) 등에서 6 이 자주 등장하지만, 이는 **관측일 뿐 정리의 함축은
  아님**.

이 절은 추측·관측 수준이며 증명·정리는 P2·P3 몫이다.

---

## 12. 참고 경로 (교재 페이지/장 단위)

| 항목 | Silverman GTM 106 | Diamond-Shurman GTM 228 | Koblitz GTM 97 |
| --- | --- | --- | --- |
| Weierstrass, Δ, j | §III.1 | §7.1 | §I.2 |
| 군법칙, 유리 공식 | §III.2, III.3 | §7.2 | §I.4 |
| Mordell-Weil | §VIII.4 | - | - |
| Mazur torsion | §VIII.7 | - | - |
| Hasse 부등식 | §V.1 | §1.4 | §II.5 |
| L(E, s) | §C.16 (Adv. Topics) | §5.10 | §III.3 |
| 모듈러 형식 기본 | - | §1.1 | §III.1 |
| Hecke 연산자 | - | §5.2 | §III.5 |
| 모듈러성 정리 | - | §8.8, §9 | - |
| Wiles 역사 | - | §9.1 | §IV |
| BSD 추측 | §X.5 | §5.10 | §III.6 |
| CM 곡선 | Adv.Topics ch. II | - | §II |
| isogeny | §III.6 | §1.5 | §I.7 |
| Tate 모듈 | §III.7 | §9.5 | - |

---

## 13. 이 단원에서 얻어야 할 5가지

1. **Weierstrass 방정식 + 판별식 + j-불변식.**
2. **군법칙** (chord-tangent, 유리 공식 λ 두 경우).
3. **Mordell-Weil 정리** E(Q) = Z^r ⊕ T (정확한 진술).
4. **L(E, s) Euler 곱**과 **모듈러성에 의한 해석적 연속**.
5. **Taniyama-Shimura-Wiles 정리** + Fermat 마지막 정리 유도 경로.

이 5가지가 손에 익으면 P3 단계에서 BSD·GRH·Langlands·Sato-Tate 로 직접 갈 수 있다.

---

## 14. 정직성 선언

- 이 노트는 교재 요약이다. 새로운 결과는 없다.
- 모든 정리·공식·연도·저자는 위 3개 교재 (Silverman, Diamond-Shurman, Koblitz) 에서
  가져왔다.
- Mazur 정리의 15가지 torsion 목록은 Silverman §VIII.7 의 정확한 리스트.
- Bhargava-Shankar 평균 rank 결과(0.885 이하) 는 Diamond-Shurman 텍스트가 아닌
  Bhargava-Shankar 2010 논문 요약 (교재 범위 밖이라 각주 수준으로만 기록).
- 프로젝트 상수(n=6)와의 연결은 §11 에 "메모" 로만 남겼고 증명·정리는 포함 안 함.
- 지어낸 정리·저자·연도는 없다.
