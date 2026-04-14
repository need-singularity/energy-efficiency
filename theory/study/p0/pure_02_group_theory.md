# PURE-P0-2 — 군론 입문 (군/환/체/S_n/정규부분군)

> 트랙: P0-PURE / 2번 태스크
> 완료 기준: Out(S_6) ≠ 1 이 왜 특별한지 설명할 수 있다
> 출처 기반: Dummit-Foote "Abstract Algebra" 3판 (2004), Artin "Algebra" 2판 (2011), Rotman "An Introduction to the Theory of Groups" 4판 (1995)
> **정직성**: 이 파일은 교재 요약이다. Out(S_6) 의 구성은 Hölder 1895 원 논문과 표준 교재의 재서술이다.

---

## 0. 목적과 범위

P0 군론 입문의 핵심은 두 가지다.

1. 군/환/체 기본 → 대칭군 S_n → 정규부분군 → 몫군 → 동형정리 (표준 과정)
2. **예외적 사실**: 모든 n에 대해 Out(S_n) = 1 인데, **n = 6 에서만 Out(S_6) = ℤ/2**

두 번째가 이 노트의 목적지다. 이것은 "유한 대수 구조 계열에서 6 이 왜 특별한가"의
한 가지 구체 사례이며, PURE-P0-1 의 R1 정리 (σφ=nτ ⟺ n=6) 와는 **독립적인** 사건이다.
두 사실이 같은 6 을 가리키는 것은 관찰에 불과하며, 본 노트는 원인 인과를 주장하지 않는다.

---

## 1. 군의 정의와 기본 예

### 1.1 군 (Group)

**정의** (Dummit-Foote §1.1).

집합 G 와 이항 연산 · : G × G → G 가 **군**이라 함 ⟺ 다음 4 공리:
- (G1) **폐쇄성**: a,b ∈ G ⟹ a·b ∈ G. (연산 정의에 내재)
- (G2) **결합법칙**: (a·b)·c = a·(b·c).
- (G3) **항등원**: ∃ e ∈ G, ∀ a ∈ G, e·a = a·e = a.
- (G4) **역원**: ∀ a ∈ G, ∃ a⁻¹ ∈ G, a·a⁻¹ = a⁻¹·a = e.

a·b = b·a 이면 **가환군(abelian)** 또는 **아벨군**.

### 1.2 예

- (ℤ, +), (ℚ, +), (ℝ, +): 아벨군.
- (ℚ×, ·), (ℝ×, ·): 아벨군.
- GL_n(ℝ): n×n 가역 행렬, 행렬곱. 비아벨 (n ≥ 2).
- **S_n** (n차 대칭군): {1,...,n}의 순열 전체. n ≥ 3 에서 비아벨.
- **ℤ/nℤ**: mod n 덧셈. 가환, 크기 n.
- **D_n** (2차원 정n각형의 이면체군): 크기 2n.

### 1.3 부분군

H ⊆ G 가 **부분군** ⟺ H 자신이 G 의 연산에 대해 군. 표기 H ≤ G.

**판정법**: H ≠ ∅ 이고 a, b ∈ H ⟹ a·b⁻¹ ∈ H.

### 1.4 동형사상 (Homomorphism)

φ: G → H 가 **군 준동형** ⟺ ∀ a,b ∈ G, φ(a·b) = φ(a)·φ(b).
- ker φ := {a ∈ G : φ(a) = e_H}
- im φ := {φ(a) : a ∈ G}

**동형(isomorphism)**: 일대일 대응인 준동형. 표기 G ≅ H.
**자기동형(automorphism)**: G → G 동형. 전체 자기동형군 Aut(G).

---

## 2. 환과 체

### 2.1 환 (Ring)

**정의** (Dummit-Foote §7.1).
(R, +, ·) 가 **환** ⟺
- (R, +) 아벨군,
- · 결합법칙,
- 분배법칙 a·(b+c) = a·b + a·c, (b+c)·a = b·a + c·a.

단위원 1 포함 여부는 교재에 따라 다름 (DF/Artin 포함, Rotman 옵션). 본 노트는 **1 포함**.

### 2.2 체 (Field)

**정의**. 환 F 가 **체** ⟺ F \ {0} 가 · 연산에 대해 가환군.
즉, 0 이외 모든 원소가 역원을 가지며 곱셈 가환.

**예**: ℚ, ℝ, ℂ, 𝔽_p (ℤ/pℤ, p 소수).

### 2.3 이데알과 몫환

I ⊆ R 가 **양측 이데알** ⟺ (I,+) 가 R 의 부분군이고 r ∈ R, a ∈ I 이면 ra, ar ∈ I.

몫환 R/I 는 coset r+I 의 덧셈과 곱셈으로 환이 된다.

**환론의 기본 정리**(First Isomorphism Theorem for Rings):
φ: R → S 환 준동형 ⟹ R / ker φ ≅ im φ.

---

## 3. 동형정리 (Isomorphism Theorems)

여기서는 **군** 버전 3개를 명시한다. 환 버전은 위와 유사.

### 3.1 제1 동형정리

**정리** (Dummit-Foote §3.3 Thm 16).
φ: G → H 군 준동형 ⟹
1. ker φ ⊲ G (정규부분군),
2. G / ker φ ≅ im φ.

**증명 스케치**. 대응 g·ker φ ↦ φ(g) 가 잘 정의되고 단사이며 전사. ∎

### 3.2 제2 동형정리 (대각 / Diamond)

**정리**. A ≤ G, B ⊲ G ⟹
1. AB ≤ G,
2. A ∩ B ⊲ A,
3. AB / B ≅ A / (A ∩ B).

### 3.3 제3 동형정리

**정리**. H, K ⊲ G 이고 K ≤ H ⟹
(G / K) / (H / K) ≅ G / H.

(통칭 "quotient of quotient".)

---

## 4. 대칭군 S_n 과 교대군 A_n

### 4.1 S_n 정의

**정의**. S_n := {σ : {1,...,n} → {1,...,n} 일대일 대응}, 합성 연산. |S_n| = n!.

n=6 에서 |S_6| = 720.

### 4.2 사이클 표기

σ ∈ S_n 는 서로 소인 사이클의 곱으로 유일 분해 (모순된 곱셈 순서는 교환가능이므로 유일).
예: (1 2 3)(4 5) ∈ S_5.

### 4.3 부호 (signature)

**정의**. σ 가 짝수 개 전치(transposition)의 곱이면 sgn(σ) = +1, 홀수 개이면 -1.

**정리** (Dummit-Foote §3.5). sgn: S_n → {±1} 은 잘 정의된 군 준동형.

### 4.4 교대군 A_n

A_n := ker sgn = {σ ∈ S_n : sgn(σ) = +1}. |A_n| = n!/2.

**정리** (Galois, Dummit-Foote §4.6).
- A_5, A_6, ..., A_n (n ≥ 5) 는 **단순군(simple group)** (자명 이외 정규부분군 없음).
- A_4 는 예외: 정규부분군 V_4 = {e, (12)(34), (13)(24), (14)(23)} 가짐.
- A_2 = {e}, A_3 = ℤ/3.

### 4.5 n=6 특수성 예고

우리는 S_6 가 S_n 계열에서 **유일하게 바깥 자동형을 가짐**을 곧 보일 것이다. 이것은
A_6 의 비자명 외부 대칭과 직결된다.

---

## 5. 정규부분군과 몫군

### 5.1 정규부분군

**정의**. H ≤ G 가 **정규부분군** ⟺ ∀ g ∈ G, gHg⁻¹ = H. 표기 H ⊲ G.

**동치**: 좌 coset = 우 coset, 즉 gH = Hg 모든 g.

### 5.2 몫군

H ⊲ G 일 때 G/H := {gH : g ∈ G} 는 (gH)(g'H) := (gg')H 로 군이 된다.

### 5.3 예

- ℤ / nℤ: 덧셈 아벨 몫.
- S_n / A_n ≅ ℤ/2 (sgn에 의한 제1 동형정리).
- A_n 정규부분군 없음 (n ≥ 5, simple).

---

## 6. Aut(G) 와 Inn(G), Out(G)

### 6.1 내부 자기동형 (Inner automorphism)

g ∈ G 에 대해 ψ_g: G → G, ψ_g(x) = g x g⁻¹ 는 자기동형.

**내부 자기동형군**: Inn(G) := {ψ_g : g ∈ G} ≤ Aut(G).

사실: Inn(G) ≅ G / Z(G), 여기서 Z(G) := {z ∈ G : zg = gz ∀ g} 는 중심(center).

### 6.2 외부 자기동형군 (Outer automorphism group)

**정의**. Out(G) := Aut(G) / Inn(G).

"내부가 아닌 자기동형이 있는가?"의 척도. |Out(G)| = 1 ⟺ 모든 자기동형이 내부.

### 6.3 Aut(S_n)

**정리** (Hölder 1895, Dummit-Foote §4.4 exercises, Rotman §7.4).

n ≠ 2, 6 이면 **Aut(S_n) = Inn(S_n) ≅ S_n**. 즉 Out(S_n) = 1.

**n = 2**: |S_2|=2, Aut(S_2)={e} (자명), Inn=자명. Out=1.
**n = 6**: **예외** — Out(S_6) = ℤ/2.

---

## 7. 핵심: Out(S_6) = ℤ/2

### 7.1 진술

**정리 (Hölder 1895, Segal–Sylvester 구성)**.

|Out(S_6)| = 2. 즉 S_6 는 내부가 아닌 자기동형을 정확히 **하나의 클래스** 추가로 가진다.

### 7.2 증명 개요

**Step A**: S_6 의 **2-사이클 클래스**는 두 개의 conjugacy class 가 있다는 관점 착각을 바로잡기.
S_n 에서 conjugacy class 는 "사이클 타입"으로 결정되므로 2-사이클은 한 클래스 (15개).
그러나 **S_6 안에 사이클 타입 (2,2,2) 의 원소** 역시 15개 있다.

S_6 의 transitive subgroup of index 6 을 생각:
- 자명한 예: S_5 as stabilizer of 1. → 표준 임베딩.
- **비자명한 예**: S_5 as a subgroup of S_6 acting on 6 things by the **transitive action on 6 cosets** induced by an outer S_5.
이 두 번째 임베딩이 Out(S_6) 의 근원.

**Step B**: 명시적 construction (Sylvester의 **synthematic totals** / James 1988 / Rotman §7.4).

S_6 의 Sylow 5-부분군 P₅ 에 NormalizerN(P₅) 을 취하면 이 normalizer 는 20 원소 (P₅ ⋊ ℤ/4).
|S_6 : N(P₅)| = 720 / 20 = 36... 라고 생각할 수 있지만 S_6 의 Sylow 5-부분군 갯수는 n_5 = 36.

**실제 사용되는 구성**: S_6 의 6 원소 집합에 대응하는 **15 개 2-subsets** ("duad") 와
이들을 3 쌍으로 묶는 **15 개의 "synthemes"** 을 생각. 그리고 5 개의 synthemes 이 15개 duads 를
정확히 한 번씩 덮는 것을 **"total"** 또는 **synthematic total** 이라 한다.

Sylvester 1844 정리: 그런 total 이 정확히 **6 개** 있다.

S_6 는 원래 {1,...,6} 에 작용하지만, 이 6 개의 total 에 대해서도 transitive 하게 작용한다.
이 두 작용을 연결하는 bijection {1,...,6} ↔ {total₁,...,total₆} 은 자기동형을 유도하는데,
**이것이 내부가 아닌 자기동형**이다.

**Step C**: 이 외부 자기동형의 성질.
- 2-사이클 클래스 ↔ (2,2,2) 클래스 를 교환.
- A_6 를 자기 자신으로 보내며, A_6 안에서도 exceptional outer automorphism 유도.
- (ϕ ∘ ϕ) 는 내부 ⟹ |Out(S_6)| = 2.

### 7.3 왜 n=6 에서만?

**질문**: 왜 다른 n 에서는 안 되는가?

**핵심 관찰**: "n 원소 + 그 2-subset 개수 (n 2 = n(n-1)/2) + ..." 의 균형이 n=6 에서만 맞는다.
구체적으로

- S_n 안에 index n 인 transitive subgroup 이 있으려면, 그것이 S_{n-1} 의 자연스러운 embedding 이 **아닌**
  임베딩이 필요. 이런 '비자명한' transitive embedding 은 n = 6 에서만 가능하다.
- 이것은 "PGL₂(𝔽_5) ≅ S_5" 와 같은 예외적 동형이 **S_5 에서만** 6 점 집합에 작용하기 때문이다.

**참고 (Mathieu 그룹)**: 5개의 sporadic simple groups M_{11}, M_{12}, M_{22}, M_{23}, M_{24} 중
M_{12} 와 M_{24} 도 multiply transitive 한 sharply (respectively) 5-transitive 와 5-transitive 작용을 가진다.
S_6 의 예외성은 이 sporadic 계열의 맛보기로 볼 수 있다.

### 7.4 Sylvester synthematic total 명시 계산

{1,2,3,4,5,6} 위의 15 duads:
```
12, 13, 14, 15, 16
23, 24, 25, 26
34, 35, 36
45, 46
56
```

15 synthemes: 15 duads 를 3개씩 묶어 6 원소를 정확히 분할. 예: {12, 34, 56}, {13, 24, 56}, ...

**총 synthemes 개수 = 15** (계산: C(6,2)·C(4,2)/3! = 15·6/6 = 15).

5개 synthemes 로 15 duads 전체를 정확히 한 번씩 덮는 **total**:
Sylvester 1844 정리에 의해 **6 개 존재** (더도 덜도 아님).

예시 (Rotman §7.4 Example):
- T₁ = {(12)(34)(56), (13)(25)(46), (14)(26)(35), (15)(24)(36), (16)(23)(45)}
- T₂ ~ T₆ : 유사하게 구성.

이 6 개의 total 에 S_6 가 작용하는 것이 핵심. 이 작용에서 나온 permutation representation 이
원래 {1,...,6} 작용과 **대등하지만 다른** 것이 외부 자동형의 실체.

### 7.5 대수 계열 전체에서의 유일성

**관찰 (표준 정리의 정리)**:

| 계열 | 예외적 외부 자동형 존재하는 유일 항 |
|------|-----------------------------------|
| S_n  | n = 6 |
| A_n  | n = 6 (S_6 외부 자동형으로부터 유도) |
| SL_n | 없음 (정상 계열) |

다른 단순군 계열(Chevalley 계열)들에도 diagram automorphism 등이 존재하나,
그것들은 **계열적(구조적)** 이고 S_6 처럼 **1점적(pointwise exceptional)** 이지 않다.

즉 **"대수 구조 계열에서 단 하나의 n 에서만 발생하는 예외"** 로서의 의미에서
Out(S_6) = ℤ/2 는 **유한군 이론 전체의 예외** 중 가장 두드러진 예.

---

## 8. n=6 정리와의 연결 (정직한 독립성 주장)

### 8.1 공통 관찰

- **R1 정리** (PURE-P0-1): n ≥ 2 에서 σ(n)·φ(n) = n·τ(n) ⟺ n = 6. (수론)
- **Hölder 1895**: Out(S_n) = 1 이 아닌 유일한 n = 6. (군론)

두 명제 모두 "n = 6 이 유일"을 결론 내린다. 그러나:

### 8.2 이 둘은 왜 **독립적**인가

- **R1**: σ, φ, τ 의 곱셈성과 소수 멱 R_local 의 case exhaustion. **순수 수론**.
- **Hölder**: Sylvester synthematic total + S_n의 transitive embedding. **군 작용 조합론**.

두 증명은 도구가 **전혀 다르다**. 한쪽이 다른 쪽을 함의하지 않는다. 같은 n=6 을 가리킨다는 것은
**관찰**이지 **정리**가 아니다. 본 노트는 어떤 인과/구조적 연결도 주장하지 않는다.

### 8.3 문제 제기 (P2 이후 과제)

- **질문 1**: σ·φ = n·τ 의 유일성 n=6 과 Out(S_6) = ℤ/2 의 유일성 n=6 을 연결하는
  공통의 구조 (예: Dedekind zeta, Galois cohomology) 가 존재하는가?
- **질문 2**: 이 질문 자체가 의미 있는가? (feedback_honest_verification: 패턴매칭 편향 경고.)

P0 단계에서는 "두 사실이 독립적으로 6 을 가리킨다"는 사실만 기록한다.

---

## 9. 정직성 체크

### 9.1 이 노트가 주장하지 않는 것

- Sylvester 의 6 total 이 "왜" 6 개인지 더 깊은 이유는 이 노트에 없다.
  (Rotman §7.4 연습문제로 유도).
- A_n simple 정리의 **증명 세부**는 생략. (Dummit-Foote §4.6 참조)
- "예외"가 수학 우주 전체에서 얼마나 일반적/특수한지에 대한 메타이론은 본 노트 밖.

### 9.2 sopfr=5 편향 경고

Out(S_6) = ℤ/2 는 sopfr 과 **완전히 독립**이다. 본 노트에서 sopfr 관찰은 사용하지 않았다.

### 9.3 7대 난제 해결 카운트

이 노트로 해결된 밀레니엄 난제: **0 / 7**.

---

## 10. 참고 문헌

1. D. Dummit, R. Foote, *Abstract Algebra*, 3rd ed., Wiley, 2004. (Chapters 1, 3, 4.4, 4.6, 7)
2. M. Artin, *Algebra*, 2nd ed., Pearson, 2011. (Chapters 2, 6, 11)
3. J. Rotman, *An Introduction to the Theory of Groups*, 4th ed., Springer, 1995. (Chapter 7, §7.4 특히)
4. O. Hölder, "Bildung zusammengesetzter Gruppen", *Math. Ann.* 46 (1895), 321–422.
5. J. J. Sylvester, "Elementary researches in the analysis of combinatorial aggregation", *Phil. Mag.* 24 (1844).
6. H. S. M. Coxeter, *The Beauty of Geometry: Twelve Essays*, Dover, 1968. (S_6 outer auto 직관)
7. J. H. Conway, N. J. A. Sloane, *Sphere Packings, Lattices and Groups*, 3rd ed., Springer, 1999. (sporadic group 연결)

---

**작성**: P0-PURE 트랙 / 2번 태스크
**상태**: 교재 요약 완료, Out(S_6) = ℤ/2 의 Sylvester construction 재서술 수록
**다음**: pure_03_complex_analysis.md (복소해석 입문 + ζ(2)=π²/6 재구성)
