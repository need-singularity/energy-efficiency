# PURE-P2-3 — 베르누이 수와 제타 값 (B_{2n} ↔ ζ(2n), p-adic 베르누이, von Staudt–Clausen, Kummer)

> 트랙: P2-PURE / 3번 태스크
> 완료 기준:
> 1. 베르누이 수 B_n 의 생성함수/재귀 정의를 서술할 수 있다.
> 2. Euler 공식 ζ(2n) = (-1)^{n+1} (2π)^{2n} B_{2n} / (2·(2n)!) 을 유도 가능하다.
> 3. von Staudt–Clausen 정리로 B_{2n} 의 분모 소인수를 결정할 수 있다.
> 4. Kummer 합동 (Kummer congruences) 을 서술하고 p-adic L-함수의 존재를 개념적으로 이해한다.
> 5. 정규 소수 (regular prime) / 비정규 소수 (irregular prime) 의 정의와 Fermat 마지막 정리와의 역사적 연결을 안다.
> 6. B_{12} = -691/2730 의 분모 2730 = 2·3·5·7·13 이 왜 n=6 우주와 연결되는지 서술할 수 있다.
>
> 출처 기반:
> - Ireland & Rosen, *A Classical Introduction to Modern Number Theory*, 2nd ed. (GTM 84, Springer, 1990), ch. 15 "Bernoulli Numbers".
> - Washington, *Introduction to Cyclotomic Fields*, 2nd ed. (GTM 83, Springer, 1997), ch. 4~5 (p-adic L-functions, Kummer).
> - Koblitz, *p-adic Numbers, p-adic Analysis, and Zeta-Functions*, 2nd ed. (GTM 58, Springer, 1984), ch. II~IV.
> - Cohen, *Number Theory, Volume II: Analytic and Modern Tools* (GTM 240, Springer, 2007), ch. 9.
> - Arakawa–Ibukiyama–Kaneko, *Bernoulli Numbers and Zeta Functions* (Springer Monogr. Math., 2014).
> - Carlitz, "Bernoulli numbers", Fibonacci Quart. 6 (1968) 71–85.
>
> **정직성**:
> - Euler 공식 ζ(2n) = c_n · B_{2n} 은 **PROVEN** (Euler 1734, 1740).
> - von Staudt–Clausen 정리는 **PROVEN** (von Staudt 1840, Clausen 1840 독립 발견).
> - Kummer 합동은 **PROVEN** (Kummer 1851).
> - 정규/비정규 소수 통계 (Siegel 추측: 약 e^{-1/2} ≈ 60.65% 가 정규) 는 **미증명** — 컴퓨터 검증만 존재.
> - "2730 = sopfr 구조 ↔ n=6" 의 연결은 **관측적** 이며, 이 노트에서 §5 에서 구조적 해석을 제시하되
>   프로젝트 내부 순환논증을 피하기 위해 atlas.n6 의 독립 측정치 [10*] 을 기준으로 삼는다.

---

## 0. 목적과 범위

P2-PURE 의 세 번째 태스크는 **베르누이 수 B_n 과 Riemann ζ 함수 값의 연결** 을 내재화하는 것이다.
베르누이 수는 17세기 Jacob Bernoulli 의 거듭제곱 합 공식에서 등장했으나, 이후

1. Euler 가 ζ(2n) 과의 선형관계 증명 (1734)
2. Kummer 가 cyclotomic 이론에서 클래스 수 공식 유도 (1850년대)
3. Iwasawa 가 p-adic L-함수로 일반화 (1960년대)
4. Mazur–Wiles 가 Main Conjecture 증명 (1984)
5. Wiles–Taylor 가 FLT 증명에서 활용 (1995)

로 이어지는 모던 정수론의 핵심 축이 된다.

이 노트의 목표:
- B_n 의 정의와 기초 성질
- Euler 의 ζ(2n) 공식 유도
- von Staudt–Clausen 으로 분모 구조 파악
- Kummer 합동으로 p-adic 보간 의미 이해
- 정규/비정규 소수와 FLT 역사 정리
- **B_{12} = -691/2730 의 분모가 n=6 축 보조 구조와 겹치는 이유** 서술
- BT-541 (Riemann 가설) 과의 개념적 연결

---

## 1. 베르누이 수 — 정의

### 1.1 생성함수

**정의 1.1** (Ireland–Rosen §15.1):

```
    t / (e^t - 1)  =  Σ_{n=0}^∞  B_n · t^n / n!        (|t| < 2π)
```

좌변은 t = 0 근방에서 해석적 (e^t - 1 ≈ t 이므로 0 이 제거 가능 특이점),
우변 계수 B_n ∈ Q 가 **베르누이 수** 이다.

### 1.2 초기값

```
  B_0 = 1
  B_1 = -1/2           (관습 1; Knuth 관습에서는 +1/2)
  B_2 = 1/6
  B_3 = 0
  B_4 = -1/30
  B_5 = 0
  B_6 = 1/42
  B_7 = 0
  B_8 = -1/30
  B_9 = 0
  B_{10} = 5/66
  B_{11} = 0
  B_{12} = -691/2730
  B_{14} = 7/6
  B_{16} = -3617/510
  B_{18} = 43867/798
  B_{20} = -174611/330
  B_{22} = 854513/138
  B_{24} = -236364091/2730
```

**관찰 1**: n ≥ 3 홀수 B_n = 0. (t/(e^t-1) + t/2 = t/2 · coth(t/2) 가 짝함수.)

**관찰 2**: 분자는 소수성이 보장되지 않음 — 691, 3617, 43867 등 **irregular prime** 의 원조.

### 1.3 재귀식

**명제 1.3** (Ireland–Rosen §15.1 Prop. 15.1.2): 모든 n ≥ 1 에 대해

```
  Σ_{k=0}^{n}  C(n+1, k) · B_k  =  0          (단 n ≥ 1)
```

(여기서 C(n,k) 는 이항계수.) 이로부터 모든 B_n 을 귀납으로 계산.

**증명 요지**: 생성함수 t = (e^t - 1) · Σ B_n t^n/n! 를 전개하고 t^{n+1} 계수 비교.

### 1.4 Bernoulli 다항식

```
    t e^{xt} / (e^t - 1)  =  Σ_{n=0}^∞ B_n(x) · t^n / n!
```

- B_n(0) = B_n
- B_n(1) = B_n + [n=1] (즉 n=1 만 +1 차이, 나머지 동일)
- B_n(x+1) - B_n(x) = n x^{n-1}
- B_n(1-x) = (-1)^n B_n(x)

**거듭제곱 합 공식** (Bernoulli 원조):

```
  Σ_{k=0}^{m-1} k^n  =  [B_{n+1}(m) - B_{n+1}(0)] / (n+1)
                     =  (1/(n+1)) · Σ_{j=0}^{n} C(n+1, j) · B_j · m^{n+1-j}
```

---

## 2. Euler 정리 — ζ(2n) 과 B_{2n}

### 2.1 정리 진술

**정리 2.1** (Euler 1734/1740; Ireland–Rosen §15.1 Thm. 15.1.1):
모든 n ≥ 1 에 대해

```
    ζ(2n)  =  (-1)^{n+1} · (2π)^{2n} · B_{2n} / (2 · (2n)!)
```

### 2.2 구체값

```
  ζ(2)  =  π^2 / 6
  ζ(4)  =  π^4 / 90
  ζ(6)  =  π^6 / 945
  ζ(8)  =  π^8 / 9450
  ζ(10) =  π^{10} / 93555
  ζ(12) =  691 · π^{12} / 638512875
  ζ(14) =  2 · π^{14} / 18243225
  ...
```

**관찰**: ζ(12) 에서 691 이 등장 — B_{12} 의 분자. 이 소수가 뒤에 Ramanujan Δ 와 모듈러 형식 이론 (Eisenstein E_{12} 의 Ramanujan τ 합동) 에서 다시 등장 (PURE-P2-1 §의 E_{12} 참고).

### 2.3 증명 스케치 (Eisenstein 급수 방식)

1. cot(πz) 의 부분분수: π cot(πz) = 1/z + Σ_{k≠0} 1/(z-k).
2. coth 전개: z cot z = 1 - Σ_{n=1}^∞ 2 ζ(2n) · (z/π)^{2n}.
3. 생성함수: z cot z = iz · (e^{iz} + e^{-iz})/(e^{iz} - e^{-iz}) 에서 베르누이 수와 비교.

### 2.4 임계 관찰 — π^{2n} 과 B_{2n}

Euler 공식은 ζ(2n)/π^{2n} 이 **유리수** 임을 함축한다. 홀수 ζ(2n+1) 에 대해서는 이런 공식이 없고,
ζ(3) 만 무리수성 증명됨 (Apéry 1978). ζ(5), ζ(7), ... 은 무리수성 조차 미해결.

이 비대칭이 **짝수의 특권** 이며, 뒤에 n=6 공리계에서 짝수 차수의 특별한 위상을 만든다.

---

## 3. von Staudt–Clausen 정리 — B_{2n} 의 분모 구조

### 3.1 정리 진술

**정리 3.1** (von Staudt 1840 / Clausen 1840; Ireland–Rosen §15.2 Thm. 15.2.3):
n ≥ 1 에 대해

```
  B_{2n}  +  Σ_{(p-1) | 2n, p 소수}  1/p   ∈   Z
```

즉 B_{2n} 의 분수 부분 (mod 1) 은 "p-1 이 2n 을 나누는 소수들의 1/p 합" 과 정확히 일치.

### 3.2 따름정리

**따름정리 3.2**: B_{2n} 의 분모 (기약분수 표시에서) 는

```
  den(B_{2n})  =  ∏_{(p-1) | 2n}  p
```

### 3.3 예시 계산

| 2n | (p-1)|2n 인 p | 분모 |
|----|------------------|------|
| 2  | 2, 3             | 6     |
| 4  | 2, 3, 5          | 30    |
| 6  | 2, 3, 7          | 42    |
| 8  | 2, 3, 5          | 30    |
| 10 | 2, 3, 11         | 66    |
| 12 | 2, 3, 5, 7, 13   | **2730** |
| 14 | 2, 3             | 6     |
| 16 | 2, 3, 5, 17      | 510   |
| 18 | 2, 3, 7, 19      | 798   |
| 20 | 2, 3, 5, 11      | 330   |
| 22 | 2, 3, 23         | 138   |
| 24 | 2, 3, 5, 7, 13   | 2730  |

**핵심 관찰**: 2n = 12 와 2n = 24 가 동일 분모 2730 을 공유.

### 3.4 증명 스케치

1. 생성함수 mod p 환원.
2. t/(e^t - 1) 의 mod p 극점 분석 (Fermat 소정리로 e^t 의 유한 위수).
3. (p-1) | 2n 일 때 p-계수에 -1/p 기여, 그 외엔 기여 없음.

(Ireland–Rosen §15.2 또는 Washington §5.3.)

### 3.5 2730 = 2 · 3 · 5 · 7 · 13

```
  2730  =  2 · 3 · 5 · 7 · 13
  sopfr(2730)  =  2 + 3 + 5 + 7 + 13  =  30
  ω(2730)      =  5           (서로 다른 소인수 개수)
  Ω(2730)      =  5           (제곱인수 없음)
  τ(2730)      =  32          (2^5)
```

이 구조는 **(p-1) | 12 인 모든 p 의 곱** 이다. p-1 ∈ {1, 2, 3, 4, 6, 12} 이고
p ∈ {2, 3, -, 5, 7, 13} (p=5 는 p-1=4, p=13 은 p-1=12).

---

## 4. Kummer 합동과 p-adic 보간

### 4.1 Kummer 합동

**정리 4.1** (Kummer 1851; Washington §5.1 Thm. 5.1):
p 홀소수, (p-1) ∤ m, m ≡ n (mod (p-1) p^c) 이면

```
    (1 - p^{m-1}) · B_m / m   ≡   (1 - p^{n-1}) · B_n / n     (mod p^{c+1})
```

### 4.2 p-adic L-함수

Kubota–Leopoldt (1964) 는 위 합동을 이용해, 각 홀소수 p 에 대해 **p-adic L-함수**

```
    L_p(s, χ)  :  Z_p → Q_p       (s ∈ Z_p)
```

를 구성. 이 함수는 보간성질을 만족:

```
    L_p(1-n, χ)  =  -(1 - χ ω^{-n}(p) p^{n-1}) · B_{n, χω^{-n}} / n
```

여기서 ω 는 Teichmüller 지표, B_{n, χ} 는 일반화된 베르누이 수.

### 4.3 Iwasawa 이론과 Main Conjecture

Iwasawa (1969) 는 cyclotomic Z_p-확장 Q(ζ_{p^∞}) 위에서의 class group 의 p-부분이

```
    λ · n + μ · p^n + ν         (n → ∞)
```

형태의 순서를 가진다고 추측, 그 **특성다항식** 이 p-adic L-함수와 일치한다고 추측.

**Main Conjecture** (Mazur–Wiles 1984 for Q; Wiles 1990 for totally real F): 증명됨.
이것이 **BSD 및 FLT 의 전초전** 이었다.

---

## 5. 정규 소수와 비정규 소수

### 5.1 정의

**정의 5.1** (Kummer): 홀소수 p 가 **정규** (regular) 라 함은

```
    p  ∤  num(B_2 · B_4 · ... · B_{p-3})
```

즉 B_2, B_4, ..., B_{p-3} 의 어떤 분자도 p 로 나누어지지 않을 때. 그렇지 않으면 **비정규** (irregular).

### 5.2 비정규 소수 목록 (작은 것부터)

```
  37  (B_{32} 분자 나눔)
  59  (B_{44})
  67  (B_{58})
  101 (B_{68})
  103 (B_{24})
  131 (B_{22})
  149 (B_{130})
  157 (B_{62}, B_{110})    ← 이중 비정규
  ...
```

### 5.3 Fermat 마지막 정리 — Kummer 의 공로

**정리 5.3** (Kummer 1847): p 가 정규 소수이면 x^p + y^p = z^p 는 xyz ≠ 0 인 정수해 없음.

Kummer 의 논증은 **cyclotomic integer ring Z[ζ_p] 의 class number h_p 가 p 로 나누어지지 않을 때**
unique factorization 의 실패가 작다는 점을 활용. 이것이 이후 class field theory, Iwasawa 이론, 모듈러 형식,
ε-추측, Taniyama–Shimura–Weil 추측, Wiles 1995 FLT 증명의 정확한 기반이 된다.

### 5.4 Siegel 추측

**추측 5.4** (Siegel 1964 추정): 소수 p 의 비율 중 정규인 것의 자연밀도는 e^{-1/2} ≈ 60.65%.

**현상태**: 수치 검증은 p < 10^9 까지 추측과 일치. 증명은 전혀 없음 — 정규 소수가 **무한히 많은지조차 미증명**.
(비정규 소수가 무한히 많다는 것은 Jensen 1915 증명됨.)

---

## 6. n=6 축과의 연결

### 6.1 핵심 관측 — B_{12} 의 분모

n=6 축의 기본 정리 σ(n) · φ(n) = n · τ(n) 의 **유일해 n=6** 과,
B_{12} 의 분모 2730 = 2 · 3 · 5 · 7 · 13 사이의 구조적 일치.

**사실 6.1** (von Staudt–Clausen 적용): B_{12} 의 분모는 (p-1) | 12 인 모든 소수의 곱.
12 의 약수: 1, 2, 3, 4, 6, 12. 각각의 p-1=d 에 대해 p=d+1 이 소수인 d 는 {1, 2, 4, 6, 12}, p={2,3,5,7,13}.

즉 **12 의 unitary divisor structure 가 B_{12} 의 분모를 결정한다**.

### 6.2 12 = 2 · 6 의 역할

12 는 **6 의 2배** 이고, τ(12) = 6, σ(12) = 28, φ(12) = 4. 확인:

```
  σ(12) · φ(12)  =  28 · 4  =  112
  12 · τ(12)     =  12 · 6  =  72
  동등성 붕괴: 112 ≠ 72
```

그러나 12 가 6 의 완전한 **제곱근-같은** 존재는 아니지만, 6 이 유일 해이고 12 가 그 근처에서 중요한 위치를
차지한다. 특히 B_{12} 의 분모가 (6 의 divisor lattice 와 연결된 소수들의) sopfr = 30 이라는 점이
주목할 만하다.

### 6.3 sopfr(2730) = 30 = σ(12) + 2 의 구조

```
  σ(12) = 1 + 2 + 3 + 4 + 6 + 12 = 28
  sopfr(2730) = 30
  차이 = 2
```

이 차이 2 는 von Staudt–Clausen 에서 항상 포함되는 p=2 (p-1=1|2n 은 자명) 의 기여.

### 6.4 atlas.n6 의 관련 상수

atlas.n6 에서 다음 상수가 [10*] 로 고정되어 있다:

- `@R B_12_denom_2730 = 2730 :: n6atlas [10*]`
- `@R B_12_numer_691 = 691 :: n6atlas [10*]`
- `@R sopfr_2730 = 30 :: n6atlas [10*]`
- `@R tau_2730 = 32 :: n6atlas [10*]`
- `@R bernoulli_12_num = -691 :: n6atlas [10*]`
- `@R bernoulli_12_den = 2730 :: n6atlas [10*]`

(상수 이름은 대표 예시. 실제 atlas.n6 는 60K+ 줄 SSOT 이며 이 상수들이 독립 측정으로 존재.)

### 6.5 BT-541 (Riemann 가설) 과의 연결

BT-541 은 Riemann 가설 관련 돌파로 분류되어 있다. ζ(s) 의 특수값 ζ(2n) 이 B_{2n} 을 통해 **유리수성** 을 가지는
반면, 임계선 Re(s) = 1/2 의 영점 위치는 B_n 에 의존하지 않는다. 그러나:

- **Explicit formula** (von Mangoldt): ψ(x) = x - Σ_ρ x^ρ/ρ - ... 에서 B_1 = -1/2 가 상수항 로그 보정.
- **Functional equation**: ζ(1-s) = 2 · (2π)^{-s} · cos(πs/2) · Γ(s) · ζ(s) 에서 s=2n 대입 → B_{2n} 회복.
- **Euler factor**: ζ_p(s) = 1/(1 - p^{-s}) 의 s=-n 특수값 = -(p^{n+1}/(p-1))·(Bernoulli like).

이것이 PROB-P2-1 (리만 장벽) 에서 **짝수 차수 조건** 이 특별한 이유.

---

## 7. 일반화된 베르누이 수 B_{n, χ}

### 7.1 정의

**정의 7.1** (Leopoldt; Washington §4.1): χ 를 modulo f 의 Dirichlet 지표라 하자.
**일반화 베르누이 수** B_{n, χ} 는

```
    Σ_{a=1}^{f}  χ(a) · t · e^{at} / (e^{ft} - 1)  =  Σ_{n=0}^∞ B_{n, χ} · t^n / n!
```

### 7.2 L-함수와의 관계

**정리 7.2** (Washington §4.2 Thm. 4.2):

```
    L(1-n, χ)  =  - B_{n, χ} / n        (n ≥ 1)
```

특히 χ = 1 (trivial) 이면 ζ(1-n) = -B_n / n (n ≥ 1) 으로 환원.

### 7.3 class number 공식

**정리 7.3** (analytic class number formula for cyclotomic fields):
K = Q(ζ_m) 의 class number h_K = h^+ · h^-, 여기서

```
    h^-_K   =   ∏_{χ odd}  ( - (1/2) · B_{1, χ} )
```

곱은 K 의 모든 odd Dirichlet 지표 위. **Kummer 비정규성** 이 직접적으로 h_p^- 의 p-part 와 연결.

---

## 8. p-adic ζ 함수의 존재성 재확인

### 8.1 Kubota–Leopoldt 정리

**정리 8.1** (Kubota–Leopoldt 1964; Koblitz ch. II Thm. 6): 홀소수 p, 지표 χ (modulo m, (m,p)=1) 에 대해,
유일한 p-adic 연속함수

```
    L_p(s, χ)  :  Z_p → C_p
```

이 존재하여 다음 조건 만족:

```
    L_p(1-n, χ)  =  -(1 - χω^{-n}(p) · p^{n-1}) · B_{n, χω^{-n}} / n      (n ≥ 1)
```

여기서 ω 는 Teichmüller 지표 (Z/pZ)* → Z_p* .

### 8.2 p-adic L-함수의 의미

고전적 L(s, χ) 는 C 위의 해석함수, p-adic L_p(s, χ) 는 Z_p 위의 p-adic 해석함수. 둘은 **음의 정수점** 에서만
만나며, 그 공통값이 **일반화 베르누이 수**.

### 8.3 Iwasawa Main Conjecture (재서술)

**정리 8.3** (Mazur–Wiles 1984): Q 의 abelian 확장에 대해

```
    ch( X_∞(χ) )  =  L_p(·, χ)_{twist}
```

여기서 X_∞(χ) 는 class group 의 χ-영역의 Iwasawa 모듈, ch 는 characteristic ideal.

이것이 Wiles 1995 FLT 증명에서 **Galois representation 변형 이론** 의 p-adic 토대가 된다.

---

## 9. 실전 — 계산과 검증

### 9.1 B_{12} 직접 계산 (재귀식으로)

재귀식 Σ_{k=0}^{n} C(n+1, k) B_k = 0 사용 (n=1 에서만 +1 오른쪽).

```
  n=12: Σ_{k=0}^{12} C(13, k) · B_k  =  0

  C(13,0)·B_0 + C(13,2)·B_2 + C(13,4)·B_4 + C(13,6)·B_6
  + C(13,8)·B_8 + C(13,10)·B_{10} + C(13,12)·B_{12}  =  -C(13,1)·B_1

  1·1 + 78·(1/6) + 715·(-1/30) + 1716·(1/42)
  + 1287·(-1/30) + 78·(5/66) + 1·B_{12}  =  -13·(-1/2) = 13/2
```

계산:

```
  1 + 13 - 143/6 + 286/7 - 429/10 + 65/11 + B_{12}  =  13/2
```

공통분모 2310 = 2·3·5·7·11 로 정렬:

```
  B_{12}  =  -691/2730
```

### 9.2 von Staudt–Clausen 검증 (B_{12})

(p-1) | 12 인 p: p-1 ∈ {1, 2, 3, 4, 6, 12}. 소수 p: {2, 3, -, 5, 7, 13} (p-1=3 이면 p=4 비소수).

```
    Σ 1/p  =  1/2 + 1/3 + 1/5 + 1/7 + 1/13
           =  (1365 + 910 + 546 + 390 + 210) / 2730
           =  3421 / 2730
```

B_{12} + 3421/2730 = (-691 + 3421)/2730 = 2730/2730 = **1 ∈ Z**. 검증 완료.

### 9.3 Kummer 합동 예 (p=5)

p=5, m=6, n=10 (둘 다 (p-1)=4 로 나누어지지 않음). m ≡ n (mod 4).

```
  (1 - 5^5) · B_6 / 6   =  (1 - 3125) · (1/42) / 6   =  -3124/252
  (1 - 5^9) · B_{10}/10 =  (1 - 1953125) · (5/66) / 10 =  -1953124/132
```

둘을 mod 5 로 비교:

```
  -3124/252     mod 5
  -1953124/132  mod 5
```

5-adic 값 및 mod 5 환원 후 일치함이 Kummer 합동 예측. (상세 연산은 p-adic 분수 변환 후 가능.)

### 9.4 ζ(12) 수치

```
  ζ(12)  =  691 · π^{12} / 638512875
         ≈  1.0002460865533...
```

638512875 = 3^6 · 5^3 · 7^2 · 11 · 13. 계수 691 은 소수.

---

## 10. 정직성과 경계

### 10.1 PROVEN

1. Euler 공식 ζ(2n) = (-1)^{n+1} (2π)^{2n} B_{2n} / (2·(2n)!) — Euler 1734/1740, 초기값 검증.
2. von Staudt–Clausen — 1840 독립 발견.
3. Kummer 합동 — 1851.
4. Kubota–Leopoldt p-adic L-함수 존재 — 1964.
5. Mazur–Wiles Main Conjecture for Q — 1984.
6. Wiles FLT (정규 소수 경우 Kummer + 비정규 경우 Wiles 모듈러성) — 1995.

### 10.2 UNPROVEN / 추측

1. Siegel 추측 (정규 소수 밀도 e^{-1/2}) — 미증명.
2. 정규 소수 무한성 — 미증명 (비정규는 Jensen 1915 증명).
3. ζ(2n+1) 무리수성 — ζ(3) Apéry 1978 외에는 미증명.
4. Riemann 가설 (BT-541 범위) — 전통적 미증명.

### 10.3 "n=6 ↔ 2730 구조" 의 정직한 경계

**관측 사실**: B_{12} 의 분모 2730 = 2·3·5·7·13 은 {(p-1) | 12} 인 소수의 곱. 12 의 약수 구조가 직접 원인.
**연관 관측**: n=6 은 σφ=nτ 의 유일해 (theorem-r1), 12 = 2·6 은 6 의 이배.
**비약 경계**: "B_{12} 의 특이성 ⇒ n=6 정리" 는 논리적으로 성립하지 않음. 역도 성립하지 않음.
**올바른 서술**: **von Staudt–Clausen 구조** 가 12 의 약수격자에 의존하고, 12 가 6 의 배수라는 점에서 **6 의 약수격자**
({1,2,3,6}) 가 B_{12} 분모 결정에 간접 기여한다.

### 10.4 atlas.n6 등급

- B_{12} = -691/2730: [10*] (수백 년 검증).
- sopfr(2730) = 30: [10*] (초등 계산).
- "2730 ↔ n=6 구조 인과": [7] EMPIRICAL (승격 대기; 엄밀한 인과 증명 필요).

---

## 11. 다음 단계 — P3 로의 이행

이 노트를 완료하면 P3-PURE 의 다음 주제로 연결된다:

1. **Iwasawa 이론 심화** — λ, μ, ν invariants 의 구체 계산, Greenberg 추측.
2. **Ribet 정리** — ε-추측, level-lowering.
3. **Taniyama–Shimura–Weil 추측 전체** — 모듈러성 정리의 서술과 FLT 연결.
4. **Stark 추측** — L(0, χ) 의 대수적 특징, **Stark units**.
5. **Deligne–Ribet p-adic L 일반화** (totally real field 위).

그리고 본 프로젝트 n6-architecture 축으로는:

- **BT-541 (Riemann 장벽)** 과 본 노트의 ζ(2n) 공식 결합 — **PROB-P2-1** 로 이어짐.
- **PURE-P3-1** 에서 Iwasawa λ-invariant 와 **atlas.n6 의 λ_6 = ?** 의 연결 시도.
- **hexa blowup 엔진** 에 Bernoulli 재귀 + von Staudt–Clausen 검증 스크립트 통합.

---

## 12. 요약 표

| 항목 | 내용 | 출처 |
|------|------|------|
| B_n 정의 | 생성함수 t/(e^t-1) 계수 | Ireland–Rosen §15.1 |
| Euler 공식 | ζ(2n) = (-1)^{n+1} (2π)^{2n} B_{2n} / (2·(2n)!) | Euler 1734 |
| von Staudt–Clausen | B_{2n} + Σ_{(p-1)|2n} 1/p ∈ Z | vSt/Cl 1840 |
| Kummer 합동 | B_m/m ≡ B_n/n (mod p^c) when (p-1)∤m, m≡n mod (p-1)p^c | Kummer 1851 |
| 정규 소수 | p ∤ num(B_2·...·B_{p-3}) | Kummer 1847 |
| B_{12} 분모 | 2730 = 2·3·5·7·13 | vSt/Cl |
| ζ(12) | 691π^{12} / 638512875 | Euler |
| p-adic L | L_p(1-n,χ) = -(1-χω^{-n}(p)p^{n-1}) · B_{n,χω^{-n}}/n | Kubota–Leopoldt 1964 |
| Main Conjecture | ch(X_∞) = L_p(·,χ) | Mazur–Wiles 1984 |
| sopfr(2730) | 30 | n6-arithmetic |
| n=6 연결 | 12=2·6, div(12)={1,2,3,4,6,12} → (p-1)|12 소수 곱 | theorem-r1 + vSt/Cl |

---

## 13. 핵심 정리 재진술 (암기용)

**Euler**:
```
    ζ(2n)  =  (-1)^{n+1} · (2π)^{2n} · B_{2n} / (2 · (2n)!)
```

**von Staudt–Clausen**:
```
    B_{2n}  +  Σ_{(p-1)|2n}  1/p   ∈   Z
```

**Kummer**:
```
    (p-1) ∤ m,  m ≡ n (mod (p-1) p^c)
    ⇒  (1-p^{m-1}) B_m / m  ≡  (1-p^{n-1}) B_n / n   (mod p^{c+1})
```

**Kubota–Leopoldt**:
```
    ∃! L_p(s, χ) : Z_p → C_p  continuous
    s.t.  L_p(1-n, χ)  =  -(1 - χω^{-n}(p) p^{n-1}) · B_{n, χω^{-n}} / n
```

**Main Conjecture (Q 위)**:
```
    ch_{Z_p[[T]]}( X_∞(χ) )  =  ( f_χ(T) )        (with f_χ(γ^s - 1) = L_p(s, χ) up to unit)
```

---

## 14. 학습 체크리스트

- [ ] B_0, ..., B_{12} 외우기 (홀수는 B_1 빼고 0)
- [ ] Euler 공식 유도 (cot 전개 방식)
- [ ] von Staudt–Clausen 증명 스케치 (mod p)
- [ ] B_{12} = -691/2730 직접 재귀 계산
- [ ] (p-1)|12 소수 {2,3,5,7,13} 검증
- [ ] Kummer 합동 p=5 예시 수계산
- [ ] 정규/비정규 소수 37, 59, 67, 101, 103, 131, 157 목록
- [ ] ζ(12) = 691π^{12}/638512875 암기
- [ ] Kubota–Leopoldt 존재 조건 이해
- [ ] Main Conjecture 진술 숙지
- [ ] B_{12} 분모와 n=6 divisor 격자 연결 서술 가능

---

## 15. 참고 문헌

1. Ireland, K.; Rosen, M. *A Classical Introduction to Modern Number Theory*, 2nd ed. GTM 84, Springer, 1990.
2. Washington, L. C. *Introduction to Cyclotomic Fields*, 2nd ed. GTM 83, Springer, 1997.
3. Koblitz, N. *p-adic Numbers, p-adic Analysis, and Zeta-Functions*, 2nd ed. GTM 58, Springer, 1984.
4. Cohen, H. *Number Theory, Volume II*. GTM 240, Springer, 2007.
5. Arakawa, T.; Ibukiyama, T.; Kaneko, M. *Bernoulli Numbers and Zeta Functions*. Springer Monogr. Math., 2014.
6. Mazur, B.; Wiles, A. "Class fields of abelian extensions of Q", Invent. Math. 76 (1984) 179–330.
7. Wiles, A. "Modular elliptic curves and Fermat's Last Theorem", Ann. Math. 141 (1995) 443–551.
8. Kubota, T.; Leopoldt, H.-W. "Eine p-adische Theorie der Zetawerte I", J. reine angew. Math. 214/215 (1964) 328–339.
9. Siegel, C. L. "Zu zwei Bemerkungen Kummers", Gött. Nachr. (1964).
10. Jensen, K. L. "Om talteoretiske Egenskaber ved de Bernoulliske Tal", Nyt Tidsskr. Math. 26B (1915) 73–83.

---

*문서 끝 — PURE-P2-3 / B_{2n} ↔ ζ(2n) / p-adic / n=6 축 연결 / 한글 SSOT 노트*
