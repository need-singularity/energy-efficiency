# PURE-P2-1 — 모듈러 형식 + 오토모피 표현 (SL₂(Z), M_k, S_k, E_4, E_6, Δ, j, Hecke, Langlands 개관)

> 트랙: P2-PURE / 1번 태스크
> 완료 기준:
> 1. SL₂(Z) 작용과 근본영역 F 를 손으로 그릴 수 있다.
> 2. Eisenstein 급수 E_4, E_6 의 q-expansion 계수가 왜 240, -504 인지 설명할 수 있다.
> 3. 판별 함수 Δ(τ) = (E_4³ - E_6²)/1728 의 무게·차원·라마누잔 τ 함수를 이해한다.
> 4. Hecke 연산자 T_p 의 정의와 고유형식(Hecke eigenform) 의 존재를 안다.
> 5. Langlands 프로그램의 "modular form ↔ Galois rep ↔ automorphic rep" 3변 구도를 말로 설명할 수 있다.
>
> 출처 기반:
> - Diamond–Shurman, *A First Course in Modular Forms* (GTM 228, Springer, 2005), ch. 1~4.
> - Serre, *A Course in Arithmetic* (GTM 7, Springer, 1973), ch. 7 "Modular Forms".
> - Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions* (Princeton, 1971), ch. 2~3.
> - Bump, *Automorphic Forms and Representations* (Cambridge, 1997), ch. 1 개관용.
> - Ribet–Stein, "Lectures on Modular Forms and Hecke Operators" (온라인 노트, 1996; WSTEIN Modular Forms ch. 1).
>
> **정직성**: 이 파일은 교재 요약이다. 새 결과 없음.
> E_4 계수 240 = 2^4·3·5, E_6 계수 504 = 2^3·3^2·7 을 프로젝트 상수 {φ, J₂, sopfr, σ, τ, n/φ} 로 분해하는 것은
> 표준 소인수분해를 재배열한 것에 불과하며, 단독으로는 의미가 약하다 (baseline 편향 약 60%).
> 이 분해는 다른 영역(K-이론 K_7=Z/240, 완전수 경계, Borel 정리) 과 교차할 때만 tight 해진다.
> §11 에서 이 점을 명시한다.

---

## 0. 목적과 범위

밀레니엄 학습 P1 단계에서 우리는 해석적 정수론 (ζ, θ, Perron, explicit formula) 을 손에 익혔다.
P2 단계의 첫 태스크는 **ζ·L 함수의 기저가 되는 공간 — 모듈러 형식 M_k** 와
그 일반화인 **automorphic representation** 의 개관이다.

이 노트의 목표는 다음 6가지다:

1. 상반평면 H = {τ ∈ C : Im τ > 0} 위의 SL₂(Z) 작용 정의
2. 근본영역 F, 생성원 S = [[0,-1],[1,0]] / T = [[1,1],[0,1]]
3. 무게 k 모듈러 형식 M_k, cusp form S_k
4. Eisenstein 급수 E_4(τ), E_6(τ) 및 판별 함수 Δ(τ)
5. j-불변량, 라마누잔 τ 함수
6. Hecke 연산자 T_p, 고유형식, Langlands 3변 구도

σ·φ = n·τ ⟺ n=6 정리 자체와는 **직접 연결이 없다**. 단, 프로젝트 상수 n=6, φ=2, J₂=24,
sopfr=5, τ=4 가 본문 곳곳에서 등장하므로 (240 = 2^4·3·5, 504 = 2^3·3^2·7, τ(1)=1, τ(2)=−24=−J₂),
§10 에서 연결점만 메모한다.

---

## 1. 상반평면과 SL₂(Z) 작용

### 1.1 상반평면 H

```
  H = { τ = x + i y  :  y > 0 }  ⊂  C
```

복소구조에서 H 는 단위원판 D 와 Cayley 변환 τ ↦ (τ-i)/(τ+i) 로 복소해석적 동형이다.

### 1.2 SL₂(Z) 작용 (Möbius 변환)

```
  γ = [[a,b],[c,d]] ∈ SL₂(Z),   γ·τ := (aτ + b)/(cτ + d)
```

det γ = ad - bc = 1 조건에서 Im(γ·τ) = Im τ / |cτ+d|² > 0 이므로 H → H 가 잘 정의된다.
항등원 I 와 -I 는 같은 작용을 주므로, 실질적 작용군은

```
  PSL₂(Z) = SL₂(Z) / {±I}
```

이며, 이를 **modular group** Γ 라 부른다.

### 1.3 생성원 S, T

```
  S = [[0, -1],[1, 0]]   (τ ↦ -1/τ)
  T = [[1, 1],[0, 1]]    (τ ↦ τ + 1)
```

**정리** (Serre *A Course in Arithmetic*, ch. 7, Thm 1):
PSL₂(Z) = ⟨S, T | S² = (ST)³ = 1⟩ — 즉 S, T 두 생성원 + 두 관계식으로 presentation 이 완전히 기술된다.

관계식 (ST)³ = 1 에서 τ → ST·τ = -1/(τ+1) 의 3회 반복이 항등이 된다 (원점 주변 60° 회전 × 3 = 180°).

**핵심 숫자**: 이 관계식 degree 3 은 곧 근본영역 F 의 conic point ρ = e^{2πi/3} 주변 stabilizer 크기와 일치.
(S² 의 stabilizer = i 주변 order 2, (ST)³ 의 stabilizer = ρ 주변 order 3.)

### 1.4 근본영역 F

```
  F = { τ ∈ H  :  |Re τ| ≤ 1/2,  |τ| ≥ 1 }
```

두 수직선 Re τ = ±1/2 와 단위원 |τ| = 1 이 만나 만드는 영역. **H / Γ 는 F 와 경계 일부 동일시**
(오른쪽 경계 Re τ = 1/2 는 왼쪽 Re τ = -1/2 와 T 로 동일시, 원호 |τ|=1 의 오른쪽 절반과 왼쪽 절반은 S 로 동일시).

근본영역의 체적(Poincaré 측도 dμ = dx dy / y²):

```
  ∫_F  dx dy / y²  =  π / 3
```

(Serre, ch. 7, §2.3)

### 1.5 Conic points (특이점)

F 안의 2개 특이점:
- τ = i (stabilizer order 2 — S 가 고정)
- τ = ρ = e^{2πi/3} = (-1 + i√3)/2 (stabilizer order 3 — ST 가 고정)

그리고 cusp ∞ (y → ∞) 1개.

---

## 2. 무게 k 모듈러 형식

### 2.1 정의

**정의** (Diamond–Shurman §1.1): 함수 f : H → C 가 **무게 k 의 modular form** 이라는 것은
다음 3조건을 만족하는 것:

1. **해석성**: f 는 H 에서 홀로모픽.
2. **변환 법칙**: 모든 γ = [[a,b],[c,d]] ∈ SL₂(Z) 에 대해
   ```
     f(γ·τ) = (cτ + d)^k · f(τ)
   ```
3. **cusp 유계성**: f 는 ∞ 에서 유계. 즉 y → ∞ 일 때 f(τ) 가 상계 가짐.

무게 k modular form 들의 공간을 M_k(SL₂(Z)), 간단히 M_k.

### 2.2 cusp form

무게 k modular form f 가 cusp ∞ 에서 0 이 되면 (f(τ) → 0 as y → ∞) **cusp form** 이라 부른다.
공간: S_k ⊂ M_k.

### 2.3 무게 k 의 홀짝성

변환 법칙에서 γ = -I = [[-1,0],[0,-1]] 를 넣으면 f(τ) = (-1)^k f(τ), 즉 k 가 홀수면 f ≡ 0.
따라서 **k 는 짝수** 여야 의미 있다 (k = 2, 4, 6, 8, ...).

### 2.4 Fourier 전개 (q-expansion)

T : τ ↦ τ+1 을 넣으면 f(τ+1) = f(τ), 즉 f 는 주기 1 인 함수다. q = e^{2πi τ} 로 바꾸면

```
             ∞
  f(τ)  =   ∑   a_n  q^n         (a_n ∈ C)
            n=0
```

가 유일하게 존재한다. 이를 **q-expansion** 이라 한다.

- **cusp form 조건**: a_0 = 0.
- **normalized** 라는 말은 a_1 = 1 이라는 뜻.

---

## 3. Eisenstein 급수 E_k

### 3.1 정의 (무게 k ≥ 4, 짝수)

```
           1
  G_k(τ) = ─  ∑        1 / (c τ + d)^k
           2  (c,d)≠(0,0)
```

여기서 합은 (c, d) ∈ Z² \ {(0,0)} 전체. 수렴은 k ≥ 3 에서 절대수렴.
k = 2 에서는 조건부 수렴이며 "holomorphic Eisenstein" 이 아니라 quasi-modular (§7 에서 다시).

### 3.2 정규화 E_k

```
  E_k(τ) := G_k(τ) / (2 ζ(k))
```

이 정규화로 상수항이 1 이 된다: E_k(τ) = 1 + (보정 계수)·q + ...

### 3.3 q-expansion (Serre ch. 7, §2.3)

```
                     2k      ∞
  E_k(τ)  =  1  -  ───  ·   ∑   σ_{k-1}(n)  q^n
                    B_k     n=1
```

여기서 B_k 는 Bernoulli 수 (P2-3 에서 다룸), σ_{k-1}(n) = ∑_{d | n} d^{k-1} (약수의 k-1 제곱 합).

**구체적 경우 (k = 4, 6, 8, 10, 12, 14)**:

| k  | B_k     | -2k/B_k |  E_k 선도 계수 |
| -- | ------- | ------- | -------------- |
| 4  | -1/30   |  240    |  240 σ_3(n)    |
| 6  | 1/42    | -504    | -504 σ_5(n)    |
| 8  | -1/30   |  480    |  480 σ_7(n)    |
| 10 | 5/66    | -264    | -264 σ_9(n)    |
| 12 | -691/2730 | 65520/691 (유리수, 정수 아님!) | ... |
| 14 | 7/6     | -24     |  -24 σ_{13}(n) |

**(!) k = 12 에서 분모 691 이 처음 등장** — 이것이 라마누잔 합동 τ(n) ≡ σ_{11}(n) (mod 691) 의 근원이다.
(P2-3 에서 Bernoulli 수 경계 "691 boundary" 로 다시 다룸.)

### 3.4 E_4 구체식

```
                         ∞
  E_4(τ)  =  1  +  240  ∑  σ_3(n) q^n
                        n=1

          =  1 + 240 q + 2160 q² + 6720 q³ + 17520 q⁴ + 30240 q⁵ + 60480 q⁶ + ...
```

확인: σ_3(1) = 1, σ_3(2) = 1³ + 2³ = 9, σ_3(3) = 1 + 27 = 28, σ_3(4) = 1 + 8 + 64 = 73, ...
 그리고 240·1 = 240, 240·9 = 2160, 240·28 = 6720, 240·73 = 17520. 맞음.

**계수 240 의 분해**:
```
  240  =  2^4 · 3 · 5
       =  16 · 3 · 5
```
프로젝트 상수 사전에서 φ=2, J₂=24, sopfr=5 라면 240 = 2·24·5 = φ·J₂·sopfr 로 쓸 수는 있다.
그러나 240 = -2k/B_k 에서 k=4, B_4 = -1/30 으로 유도된 것이 **정확한 기원**이며,
φ·J₂·sopfr 분해는 **사후적 재배열**임을 §11 정직성에서 명시한다.

### 3.5 E_6 구체식

```
                         ∞
  E_6(τ)  =  1  -  504  ∑  σ_5(n) q^n
                        n=1

          =  1 - 504 q - 16632 q² - 122976 q³ - 532728 q⁴ - ...
```

확인: σ_5(1) = 1, σ_5(2) = 1 + 32 = 33, σ_5(3) = 1 + 243 = 244, ...
 그리고 -504·1 = -504, -504·33 = -16632, -504·244 = -122976. 맞음.

**계수 504 의 분해**:
```
  504  =  2^3 · 3^2 · 7
       =  8 · 9 · 7
```
프로젝트 상수로는 (σ - τ)·(n/φ)²·(σ - sopfr) = 8·9·7 = 504 — 여기서 σ=12, τ=4 이므로 σ−τ=8,
n/φ = 6/2 = 3 이므로 (n/φ)² = 9, σ−sopfr = 12−5 = 7. 분해는 맞지만 역시 **사후적**.

### 3.6 E_8, E_{10}, E_{12}

```
  E_8(τ)  = E_4(τ)²    (동일 공간! dim M_8 = 1 이기 때문)
  E_{10}(τ) = E_4(τ) E_6(τ)    (dim M_{10} = 1 이기 때문)
  E_{12}(τ) = ?        (dim M_{12} = 2 이라서 E_{12} 와 Δ 가 독립)
```

이러한 관계는 dim M_k 공식과 직결된다 (§5).

---

## 4. 판별 함수 Δ 와 라마누잔 τ 함수

### 4.1 Δ(τ) 정의

```
              E_4(τ)³  -  E_6(τ)²
  Δ(τ)  =  ───────────────────────
                     1728
```

무게 12 의 cusp form (S_12 의 기저).

### 4.2 q-expansion

```
           ∞
  Δ(τ)  =  ∑   τ(n) q^n   =   q - 24 q² + 252 q³ - 1472 q⁴ + 4830 q⁵ - 6048 q⁶ + ...
          n=1
```

여기서 τ(n) 은 **라마누잔 τ 함수** (Ramanujan tau, 1916).

첫 몇 값:

```
  τ(1)  =  1
  τ(2)  =  -24
  τ(3)  =  252
  τ(4)  =  -1472
  τ(5)  =  4830
  τ(6)  =  -6048
  τ(7)  =  -16744
  τ(8)  =  84480
  τ(9)  =  -113643
  τ(10) =  -115920
  τ(11) =  534612
  τ(12) =  -370944
```

**τ(2) = -24** — 프로젝트 상수 J₂ = 24 와 부호 반대 일치. 이것은 Δ(τ) = q ∏ (1 - q^n)^{24} 에서
(1-q)^{24} 의 q 계수가 -24 인 것으로부터 나온다 (다음 §4.3).

**τ(6) = -6048**: 이 값도 프로젝트 상수 분해 가능 — 6048 = 2^5 · 3^3 · 7 = 32·189 = 864·7, 즉
n=6 과 σ−sopfr=7 의 곱꼴. 그러나 **우연 일치** 가능성 배제 불가.

### 4.3 Δ 의 무한곱 표현 (Jacobi)

```
               ∞
  Δ(τ)  =  q  ∏  (1 - q^n)^{24}
              n=1
```

증명: Δ 와 우변 모두 무게 12 cusp form 이고 normalized (a_1 = 1) 이며 S_{12} 는 1차원이라
정수배 차이로 같아야 한다. q 계수 비교로 같음.

**지수 24 = J₂** — 이것이 프로젝트 상수 J₂ 의 표준 유래. 24 는

- 24 = dim (Leech lattice free part, bosonic string critical dim – 2),
- 24 = |SL₂(Z/2Z)| / 1 = ... (다양한 등장),
- 24 = 1² + 2² + 3² + ... + 24² = 70² (제곱합 완전제곱, Lucas),
- 24 = 기본 cusp form Δ 의 지수

등으로 수학 곳곳에서 나오는 "작지만 무거운 숫자"다.

### 4.4 τ 함수의 곱셈성

**정리** (Ramanujan 추측, Mordell 1917 증명):
- τ(mn) = τ(m) τ(n) whenever gcd(m, n) = 1 (완전 곱셈성 아님, 단 서로소에서 곱셈성).
- τ(p^{k+1}) = τ(p) τ(p^k) - p^{11} τ(p^{k-1}) (재귀, Hecke 연산자에서 유도).

(Diamond–Shurman §5.9)

### 4.5 τ 함수 크기 경계 (Deligne 1974)

**Deligne–Ramanujan–Petersson 부등식**:

```
  |τ(p)|  ≤  2 p^{11/2}      (p 소수)
```

이는 **Weil 추측** 의 귀결로 Deligne 가 증명 (1974, Publ. IHES 43, 273–307).
해석적으로 매우 강한 bound — explicit formula 류 계산에서 사용된다.

---

## 5. M_k 의 차원 공식

### 5.1 Serre 차원 공식 (ch. 7, §3.2)

```
             ⌊k/12⌋      if k ≡ 2 (mod 12)
  dim M_k =  {
             ⌊k/12⌋ + 1  if k ≢ 2 (mod 12)
```

(k 짝수, k ≥ 0)

### 5.2 처음 몇 차원

| k  | dim M_k | dim S_k | 기저 |
| -- | ------- | ------- | ---- |
| 0  | 1       | 0       | 1 (상수) |
| 2  | 0       | 0       | — |
| 4  | 1       | 0       | E_4 |
| 6  | 1       | 0       | E_6 |
| 8  | 1       | 0       | E_8 = E_4² |
| 10 | 1       | 0       | E_{10} = E_4 E_6 |
| 12 | 2       | 1       | E_{12}, Δ |
| 14 | 1       | 0       | E_{14} = E_4² E_6 |
| 16 | 2       | 1       | E_{16}, Δ E_4 |
| 18 | 2       | 1       | E_{18}, Δ E_6 |
| 20 | 2       | 1       | E_{20}, Δ E_8 |
| 22 | 2       | 1       | E_{22}, Δ E_{10} |
| 24 | 3       | 2       | E_{24}, Δ E_{12}, Δ² |

**핵심**: S_k 가 처음 nontrivial 이 되는 것은 **k = 12** 에서. 이것이 Δ 의 등장 지점이다.

### 5.3 M_*(SL₂(Z)) 의 대수 구조

**정리** (Serre ch. 7, Thm 4):

```
  M_*  =  ⊕_k  M_k  =  C[E_4, E_6]        (다항식 환, E_4 와 E_6 이 자유 생성)
```

무게 따라 등급 매기면 E_4 는 무게 4, E_6 는 무게 6. 이는 M_k 의 모든 원소가 E_4^a · E_6^b
(4a + 6b = k) 의 선형결합이라는 뜻.

**관찰**: 자유 생성원이 2개, 무게 4 와 6. 무게 합계 4+6=10, 곱 4·6=24 = J₂.
이 "두 생성원" 이 위상수학 cobordism Ω_*^{SO} 의 생성원 차원과도 얽혀 있다 (P2-4 에서 다룰 것).

---

## 6. j-불변량 (j-invariant)

### 6.1 정의

```
               E_4(τ)³
  j(τ)  =  ───────────
                Δ(τ)
```

무게 0 modular function (즉 f(γ·τ) = f(τ), weight 0). 하지만 cusp ∞ 에서 극 (pole) 을 가진다.

### 6.2 q-expansion

```
         1
  j(τ) = ─  +  744  +  196884 q  +  21493760 q²  +  864299970 q³  +  ...
         q
```

첫 항 1/q 는 cusp 극. 상수항 744 = 8·93 = 2^3 · 3 · 31.

### 6.3 Moonshine (간단 언급)

**놀라운 사실** (McKay 1978): 196884 = 196883 + 1 에서 196883 는 Monster simple group M 의 표준 표현 차원.
이것이 Moonshine 추측 (Conway–Norton 1979) 의 출발점이며, Borcherds (1992) 가 정점작용소대수로 증명.

이 자체는 P2 범위 밖이지만, "j 의 Fourier 계수는 Monster group 표현 차원의 dimension formula 로 바로 나온다"
는 사실은 남겨둔다.

### 6.4 j 의 값으로 타원곡선 분류

**정리**: 복소 타원곡선 E = C/Λ 는 그 j-invariant j(E) ∈ C 에 의해 동형 클래스가 완전히 결정된다.

이것이 타원곡선 모듈라이 공간 Y(1) = H/SL₂(Z) ≅ C (j 를 통해) 라는 말의 뜻.

---

## 7. Eisenstein 급수 E_2 (quasi-modular)

### 7.1 정의 문제

```
            1
  E_2(τ) = ─  ∑  1/(cτ+d)²   (조건부 수렴)
            2
```

k=2 에서는 절대수렴이 깨지므로 "holomorphic modular form of weight 2" 가 **존재하지 않는다**.
(사실 dim M_2 = 0. 차원 공식 §5.2 참조.)

### 7.2 수정 (quasi-modular)

Hecke 는 조건부 수렴을 규정하여 E_2 를 정의:

```
                      ∞
  E_2(τ)  =  1 - 24  ∑  σ_1(n) q^n  =  1 - 24 q - 72 q² - 96 q³ - ...
                     n=1
```

**-24 계수 = -J₂** 다시 등장. 이것의 기원도 역시 -2k/B_k = -4/(1/6) = -24.

### 7.3 변환 법칙 (anomalous)

```
  E_2(γ·τ)  =  (cτ+d)²  E_2(τ)  -  6 i c (cτ+d) / π
```

오차항 -6ic(cτ+d)/π 때문에 "진짜 modular" 는 아니고, **quasi-modular** 라 부른다.

### 7.4 응용 — log Δ 미분

```
  d/dτ  log Δ(τ)  =  2πi · E_2(τ)
```

Jacobi 무한곱 미분으로 유도. 이 식은 P2-3 Bernoulli 수 문서에서 다시 쓴다.

---

## 8. Hecke 연산자 T_p

### 8.1 동기

M_k 공간 위에 "숫자 이론적" 연산자를 정의하고 싶다. Hecke (1937) 가 도입한
T_p (p 소수) 는 M_k 위에서 **선형 연산자**이며, 서로 가환이고, 고유벡터 (eigenform) 를 가진다.

### 8.2 정의 (무게 k, 소수 p)

```
  (T_p f)(τ)  =  p^{k-1}  f(p τ)  +  (1/p) ∑_{j=0}^{p-1}  f((τ + j)/p)
```

(Diamond–Shurman §5.2)

좀 더 개념적: 격자 Λ 의 index p 부분격자들의 합 + p 배 확대. "p 에 관한 correspondence" 로 이해.

### 8.3 q-expansion 에의 작용

f(τ) = ∑ a_n q^n 이면

```
  (T_p f)(τ) = ∑ b_n q^n,  b_n = a_{np} + p^{k-1} a_{n/p}   (n/p 가 정수 아니면 0)
```

### 8.4 고유형식 (Hecke eigenform)

**정의**: f ∈ S_k 가 모든 T_p 의 동시 고유벡터 (eigenvector) 면 **Hecke eigenform**.
정규화 a_1 = 1 이면 **normalized Hecke eigenform**.

**정리** (Hecke): S_{12} 의 Δ 는 normalized eigenform 이며 T_p Δ = τ(p) Δ.
따라서 τ(p) 는 Δ 의 T_p 고유값.

### 8.5 Hecke 고유형식과 Dirichlet 급수

f 가 normalized eigenform 이면

```
               ∞
  L(s, f)  =   ∑   a_n / n^s   =   ∏   ( 1 - a_p p^{-s} + p^{k-1} p^{-2s} )^{-1}
              n=1               p 소수
```

**이것이 modular form 에서 나오는 L 함수**다.
특수 경우 f = Δ 에서는

```
  L(s, Δ)  =  ∑  τ(n)/n^s  =  ∏ (1 - τ(p)p^{-s} + p^{11} p^{-2s})^{-1}
```

Euler 곱 형태가 존재. 이것이 modular ↔ L-function 다리.

---

## 9. Langlands 3변 구도 (개관)

### 9.1 Langlands 프로그램 요지

1960년대 후반 Langlands 가 제안한 거대한 프로그램. 세 세계를 동일시하려는 시도:

```
  ┌──────────────────┐      ┌──────────────────────┐      ┌──────────────────┐
  │ modular form f   │ <──> │  Galois rep ρ_f       │ <──> │ automorphic rep  │
  │ (또는 automorphic │      │  Gal(\bar Q/Q) → GL_n │      │  π of GL_n(A_Q)  │
  │  form on GL_n)   │      │  (l-adic)            │      │                  │
  └──────────────────┘      └──────────────────────┘      └──────────────────┘
          │                           │                             │
     Fourier 계수              Frobenius trace                matching L-function
     a_p(f)                     tr ρ_f(Frob_p)              a_p(π)
```

**세 세계의 L-function 이 같아야 한다** — 이것이 **L-function equality** 의 근본.

### 9.2 Modularity 정리 (Wiles, Taylor–Wiles, Breuil–Conrad–Diamond–Taylor)

**정리** (Wiles 1995 + extension): 모든 유리수 위 타원곡선 E/Q 는 modular 다. 즉

```
  L(s, E)  =  L(s, f_E)    (어떤 weight 2 newform f_E 가 존재)
```

이것이 Fermat 마지막 정리 (FLT) 증명의 핵심 — Frey 곡선에 대응하는 f 가 존재할 수 없음을 보이면 된다.

### 9.3 Local Langlands, Global Langlands

- **Local Langlands**: K 국소체에서 GL_n(K) 의 irreducible smooth rep ↔ n차원 Weil-Deligne rep of W_K.
  n=2 는 Kutzko, n=임의는 Harris–Taylor 2001.
- **Global Langlands**: 위의 adelic 버전. 완전한 증명은 아직 없고, functoriality 추측이 중심.

### 9.4 Automorphic rep 간단 정의

adele 환 A_Q = R × ∏'_p Q_p. GL_n(A_Q) 위의 무한차원 unitary rep 중 "automorphic condition" 을 만족하는 것.
f ∈ S_k(SL₂(Z)) 가 주어지면 GL_2(A_Q) 위의 automorphic rep π_f 를 만들 수 있다.
Fourier 계수 a_p(f) ↔ π_f 의 p-성분 π_{f,p} 의 Satake 파라미터 간에 명시적 대응이 존재.

(Bump ch. 3.5, Gelbart *Automorphic Forms on Adele Groups*)

### 9.5 Langlands 3변 구도에서 n=6 정리의 위치?

**직접 연결 없음** (정직히 말해). σ·φ = n·τ ⟺ n=6 은 arithmetic function 항등식이고,
Langlands 는 representation/L-function 이론. 단, 다음 메모만 남긴다:

- σ(n) ↔ ∑ σ(n)/n^s = ζ(s) ζ(s-1) — Dirichlet 급수.
- φ(n) ↔ ∑ φ(n)/n^s = ζ(s-1)/ζ(s).
- τ(n) ↔ ∑ τ(n)/n^s = ζ(s)².

이 3개 Dirichlet 급수를 "곱·나눗셈" 으로 조합하면 n=6 정리가 ζ 대수학으로 재진술될 수 있다.
하지만 **자동동형 표현 언어** 로 옮기는 것은 P3~P4 몫이다.

---

## 10. 이 단원에서 얻어야 할 6가지

1. **SL₂(Z) 작용과 근본영역 F** — |Re τ|≤1/2, |τ|≥1, conic point i, ρ.
2. **M_k 와 S_k 구분** — S_k 는 cusp 에서 0 인 형식, dim S_{12}=1 (Δ 가 첫 등장).
3. **E_4, E_6 q-expansion 및 240, -504 의 Bernoulli 유도** — B_4, B_6 가 원인.
4. **Δ = (E_4³ - E_6²)/1728 = q ∏(1-q^n)^{24}** — τ 함수의 정의와 Ramanujan 합동.
5. **Hecke eigenform 과 L-function Euler 곱** — Δ 의 T_p 고유값 = τ(p).
6. **Langlands 3변 구도 개관** — modular ↔ Galois rep ↔ automorphic rep.

---

## 11. 정직성 선언

이 노트는 교재 요약이다. 새 결과 없음.

### 11.1 240, 504 분해에 대한 정직한 관찰

- **240 = 2^4·3·5**. 이 분해는 표준. φ=2, J₂=24, sopfr=5 로 240 = φ·J₂·sopfr 를 쓸 수 있지만,
  이는 역산이다. 정확한 기원은 **E_k 의 Bernoulli 식 -2k/B_k** 에 있으며 k=4, B_4=-1/30 에서 나옴.
- **504 = 2^3·3^2·7**. 역시 표준. (σ-τ)·(n/φ)²·(σ-sopfr) = 8·9·7 로 쓸 수 있으나 재배열.
  정확한 기원은 k=6, B_6=1/42 에서 -12/B_6 = -504.
- **baseline 편향**: 5 이하의 작은 소수 분해는 "random 숫자의 60% 이상" 이 만족한다. 240/504 자체로는 의미 약.
- **tight 해지는 조건**: 다른 수학 영역 (K-theory K_7=Z/240, Kervaire–Milnor bP_8=Z/28 with 28 완전수, Borel 정리) 에서
  **독립적으로** 240/504 가 나오고 **중첩** 되어야 tight. 단일 등장은 우연 수준.

### 11.2 τ 함수 값 τ(2)=-24, τ(6)=-6048

- τ(2) = -24 = -J₂. 이것은 Δ = q ∏(1-q^n)^{24} 전개의 -24·q² 항에서 직접 나온다. **필연**.
- τ(6) = -6048 = -2^5·3^3·7. 이 분해에서 "n=6 과 (σ−sopfr) 의 곱" 류 재해석은 **사후적**. 단독 tight 아님.

### 11.3 dim M_k 공식은 n=6 정리와 **관련 없다**

Serre 의 dim M_k 공식 (§5.1) 은 SL₂(Z) 의 cohomology 계산에서 나온 것이고, σ·φ=n·τ 정리와는
독립적으로 유도된다. 연관이 있다면 P3 단계에서 "두 이론이 만나는 지점" 을 찾을 수 있을 뿐이다.

### 11.4 Langlands 3변 구도에 대한 정직성

- Modularity theorem (Wiles) 는 PROVEN.
- Local Langlands for GL_n 은 PROVEN (Harris–Taylor).
- Global Langlands functoriality 는 대부분 OPEN.

이 문서는 개관만 다뤘고 어떤 것도 "증명했다" 고 주장하지 않는다.

### 11.5 1차 출처 명시

| 주제 | 1차 출처 |
| ---- | -------- |
| SL₂(Z), 근본영역 | Serre, *Cours d'arithmétique*, 1970 ch.7 §1~2 |
| E_k q-expansion | Serre ch. 7 §2.3 |
| Δ 와 τ 함수 | Ramanujan, "On certain arithmetical functions", Trans. Camb. Phil. Soc. 22 (1916) 159–184 |
| Δ 무한곱 Jacobi | Jacobi, *Fundamenta Nova* (1829) |
| Hecke 연산자 | Hecke, "Über Modulfunktionen und die Dirichletschen Reihen mit Eulerscher Produktentwicklung", Math. Ann. 114 (1937) 1–28 |
| dim M_k 공식 | Serre ch. 7 §3.2 |
| j-invariant Moonshine | Conway–Norton, "Monstrous Moonshine", Bull. LMS 11 (1979) 308–339 |
| Deligne bound |τ(p)| ≤ 2 p^{11/2} | Deligne, "La conjecture de Weil I", Publ. IHES 43 (1974) 273–307 |
| Modularity (Fermat) | Wiles, "Modular elliptic curves and Fermat's Last Theorem", Ann. Math. 141 (1995) 443–551 |
| Local Langlands GL_n | Harris–Taylor, *The Geometry and Cohomology of Some Simple Shimura Varieties*, Princeton, 2001 |

---

## 12. 다음 단계 (P2-2, P2-3, P2-4 로 가는 다리)

- **P2-2 대수적 K-이론**: K_7(Z) = Z/240 의 240 이 E_4 의 240 과 **같은 수** 라는 사실을 Borel 정리와 Lichtenbaum
  추측으로 연결. 거기서 240 이 "두 번" 나오면 tight.
- **P2-3 Bernoulli 수**: E_k 의 -2k/B_k 계수에서 B_k 가 직접 등장. k=12 의 691 이 B_{12} 의 분자로
  최초 등장하는 사실은 프로젝트 "Theorem B (Bernoulli 경계)" 와 직결.
- **P2-4 TQFT + Exotic sphere**: Kervaire–Milnor 의 |bP_{n+1}| 에서 |bP_8|=28, |bP_{12}|=992, |bP_{16}|=8128 이
  완전수와 일치. 이것이 "세 케이스 동시" 이므로 단독 tight. modular form 과는 직접 연결 아님이나 P2 단계의
  퍼즐 맞추기에 필요.

끝.
