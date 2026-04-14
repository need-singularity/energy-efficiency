# PURE-P1-6 — 위상학 기초 (호모토피/호몰로지/코호몰로지/기본군/4-다양체)

> 트랙: P1-PURE / 6번 태스크
> 완료 기준: π_n, H_n, H^n 의 정의와 관계 (Hurewicz 정리, 보편계수정리),
> 4-다양체 고유 구조 (교차형식 Q_M, Donaldson, Freedman) 를 말로 서술할 수 있다.
> 출처 기반: Hatcher "Algebraic Topology" (Cambridge, 2002) ch. 1~3,
> Bredon "Topology and Geometry" (GTM 139, 1993) ch. 4~7,
> Milnor-Stasheff "Characteristic Classes" (Princeton, 1974) ch. 1~9,
> Freedman-Quinn "Topology of 4-Manifolds" (Princeton, 1990) ch. 1~2.
> **정직성**: 이 파일은 교재 요약이다. 새 결과는 없다. 모든 정리·공식은 위 4개 교재에서
> 재구성하였고, 정리 번호·페이지는 각 교재 대표 판본 기준으로 기록하였다.

---

## 0. 목적과 범위

밀레니엄 문제군 중 푸앵카레(해결됨)·Yang-Mills (4-다양체 구조) · Hodge (대수기하/위상
교차) 가 모두 위상학 위에 서 있다. P1 단계에서 다룰 6가지 기초는 다음과 같다.

1. 호모토피: 경로·loop·π_n 의 정의와 함수성
2. 특이 호몰로지 H_n(X; ℤ) — chain complex 와 경계준동형
3. 코호몰로지 H^n(X; ℤ) — 쌍대, cup product, ring 구조
4. 기본군 π_1 과 van Kampen 정리
5. CW 복합체와 세포적 계산
6. 4-다양체의 교차형식 Q_M 과 분류

본 노트는 대수적 위상의 "기초 세 언어" (π_n, H_n, H^n) 를 먼저 정의하고, 이들 사이의
다리 (Hurewicz, 보편계수, Künneth) 를 명시한 뒤, 4-다양체에 특수화한다.

---

## 1. 호모토피

### 1.1 연속변형과 등가관계

위상공간 X, Y 와 연속함수 f, g: X → Y 사이의 **호모토피** 란 H: X × [0,1] → Y 연속함수로
H(x, 0) = f(x), H(x, 1) = g(x) 를 만족하는 것. f ~ g 로 적는다.

### 1.2 고차 호모토피군 π_n

기반점 x₀ ∈ X. π_n(X, x₀) = [(S^n, s₀), (X, x₀)], 즉 기반점을 보존하는 구면 S^n 에서
X 로의 연속함수 호모토피 등가류. n=1 에서 기본군, n≥2 에서 아벨군이다 (Eckmann-Hilton).

### 1.3 함수성과 곱공간

π_n(-, x₀) 은 공변 함자이며, π_n(X × Y, (x_0,y_0)) ≅ π_n(X,x₀) × π_n(Y,y₀).
연결된 Lie 군 G 에 대해 π_1(G) 은 아벨군 (일반적인 topology 에서 π_1 은 비아벨 허용).

### 1.4 구면의 π_n — 계산 난이도

- π_n(S^n) = ℤ (Hurewicz, n≥1, 단순연결 공간)
- π_3(S²) = ℤ (Hopf 불변량, 1931 Hopf)
- π_{n+k}(S^n) 의 계산은 n,k 에 따라 매우 어렵다 (Serre 유한성 정리: k>0 에서 유한)

이 때문에 π_n 만으로 공간을 분류하려는 시도는 일반적으로 계산 불가능에 부딪친다.
호몰로지가 계산 가능성을 주는 보조 언어다.

(출처: Hatcher §4.1, 특히 Serre 1953 박사논문)

### 1.5 CW 근사와 약동치

모든 위상공간은 CW 복합체로 약동치적 근사 가능 (Whitehead 정리: π_n-동형을 유발하는
연속사상이면 CW 사이에서 호모토피 동치). 따라서 호모토피 계산은 세포 구조로 환원된다.

---

## 2. 특이 호몰로지

### 2.1 표준 단체와 singular chain

Δ^n = {(t_0,...,t_n) ∈ ℝ^{n+1} : t_i ≥ 0, Σ t_i = 1} 이 표준 n-단체.
singular n-chain 이란 연속함수 σ: Δ^n → X 들의 유한 자유아벨군 C_n(X).

### 2.2 경계 준동형

∂_n: C_n(X) → C_{n-1}(X), σ ↦ Σ_{i=0}^n (-1)^i σ ∘ d_i (d_i 는 i번째 꼭짓점 제거).
∂_{n-1} ∘ ∂_n = 0. 따라서 C_•(X) 는 chain complex.

### 2.3 H_n(X; ℤ) 정의

```
  Z_n = ker ∂_n   (cycle)
  B_n = im ∂_{n+1} (boundary)
  H_n(X; ℤ) = Z_n / B_n
```

H_0(X; ℤ) = ℤ^{c(X)} (c 는 경로연결성분 개수). H_1(X; ℤ) ≅ π_1(X)^{ab} (abelian화,
Hurewicz 정리 n=1).

### 2.4 Mayer-Vietoris 과 excision

열린 덮개 X = A ∪ B 에 대한 긴 완전열

```
  ... → H_n(A ∩ B) → H_n(A) ⊕ H_n(B) → H_n(X) → H_{n-1}(A ∩ B) → ...
```

excision: 닫힌 Z ⊂ int(A) 에 대해 H_n(X, A) ≅ H_n(X\Z, A\Z). 두 정리로 CW 복합체 호몰로지
재귀 계산이 가능해진다.

(출처: Bredon §IV.8, Hatcher §2.2)

### 2.5 Hurewicz 정리

X 가 (n-1)-연결이면 (π_i(X) = 0, 0 < i < n), 자연사상 π_n(X) → H_n(X; ℤ) 가
n ≥ 2 일 때 동형이며, n=1 일 때 abelian화 후 동형.

---

## 3. 코호몰로지

### 3.1 쌍대 cochain

C^n(X; ℤ) = Hom(C_n(X), ℤ), 공경계 δ^n = (∂_{n+1})*. 그러면 cochain complex 와
H^n(X; ℤ) = ker δ^n / im δ^{n-1}.

### 3.2 보편계수정리 (UCT)

```
  0 → Ext(H_{n-1}(X; ℤ), ℤ) → H^n(X; ℤ) → Hom(H_n(X; ℤ), ℤ) → 0   (short exact)
```

이 수열은 자연적으로 분할된다 (비자연 분할). 계수를 체 k 로 바꾸면 Ext 항이 사라져
H^n(X; k) = Hom(H_n(X; k), k) 가 된다.

### 3.3 cup product

∪: H^p(X) × H^q(X) → H^{p+q}(X). 결합적·단위(1 ∈ H^0(X)=ℤ) 를 갖지만, 일반적으로
ab = (-1)^{pq} ba (graded-commutative). 이로써 H^*(X; k) 는 **graded ring**.

예: H^*(ℂP^n; ℤ) = ℤ[α]/α^{n+1}, deg α = 2. 이 truncated polynomial 구조는 호몰로지만으로는
드러나지 않는 정보를 담는다 (ring vs. module).

### 3.4 Poincaré 쌍대성

닫힌 지향 n-다양체 M 에 대해

```
  H^k(M; ℤ) ≅ H_{n-k}(M; ℤ)     (fundamental class [M] 과의 cap product)
```

비지향의 경우 ℤ/2 계수로 동일. 이는 4-다양체 연구의 근본 도구다.

### 3.5 de Rham 코호몰로지 — 매끄러운 다양체

매끄러운 M 에 대해 de Rham 복합체 Ω^0(M) → Ω^1(M) → ...

```
  H^n_{dR}(M; ℝ) = ker d / im d
```

**de Rham 정리**: H^n_{dR}(M; ℝ) ≅ H^n(M; ℝ) (singular cohomology 실계수).
게이지이론의 특성류 Chern-Weil 이 이 등식 위에 서 있다.

---

## 4. 기본군과 van Kampen

### 4.1 기본군 π_1 재정의

loop γ: [0,1] → X 의 경로 호모토피 류 [γ]. 곱셈은 경로 이어붙이기. 단위원은 상수 loop.
π_1(X, x₀) 은 일반적으로 비가환 군.

### 4.2 van Kampen 정리

X = U ∪ V, U, V 열린·경로연결, U ∩ V 경로연결, x₀ ∈ U ∩ V 이면

```
  π_1(X, x₀) ≅ π_1(U, x₀) *_{π_1(U∩V, x₀)} π_1(V, x₀)
```

(amalgamated free product, 군의 pushout)

### 4.3 대표 계산

- π_1(S^1) = ℤ
- π_1(S^n) = 0  (n ≥ 2)
- π_1(T^2) = ℤ²
- π_1(Σ_g) = ⟨a_1,b_1,...,a_g,b_g | [a_1,b_1]...[a_g,b_g]⟩ (표면 g-종)
- π_1(ℝP^n) = ℤ/2  (n ≥ 2)

### 4.4 덮개공간 대응

X 가 경로연결·국소경로연결·준국소단순연결이면, π_1(X, x₀) 의 부분군과 X 의 연결덮개
(covering) 사이에 Galois 대응이 존재한다. 보편덮개 X̃ 는 π_1(X) 에 대응.

---

## 5. CW 복합체와 세포 호몰로지

### 5.1 CW 정의

X⁰ ⊂ X¹ ⊂ X² ⊂ ... 단조증가, X^n = X^{n-1} ∪_{∂D^n_α} D^n_α 형태로 n-세포를
"부착사상" φ_α: ∂D^n_α = S^{n-1} → X^{n-1} 으로 붙임. X = colim X^n.

### 5.2 세포 호몰로지

C^{CW}_n(X) = ℤ^{|n-세포|} (자유아벨군). 경계는 부착사상의 degree 로 주어진다.

```
  H_n^{CW}(X) ≅ H_n(X; ℤ)       (singular 과 동형)
```

실전에서 단체 복합체·Δ 복합체·CW 모두 같은 호몰로지를 내므로, 가장 작은 세포 구조로
계산하는 것이 효율적이다.

### 5.3 Euler 특성류

χ(X) = Σ (-1)^n (n-세포 수) = Σ (-1)^n rank H_n(X; ℤ) = Σ (-1)^n dim H^n(X; k).
세 표현식 모두 같은 값을 준다 (chain complex 에서 Betti 수와 rank 는 대수적으로 같음).

---

## 6. 4-다양체의 특수 구조

### 6.1 교차형식 Q_M

M 이 닫힌·지향 4-다양체. Poincaré 쌍대로 H^2(M; ℤ) 위에 대칭 쌍선형형식

```
  Q_M: H^2(M; ℤ) × H^2(M; ℤ) → ℤ,    Q_M(α, β) = ⟨α ∪ β, [M]⟩
```

이 형식은 M 의 기본 불변량이다. 유한 rank (= b_2) 에 대해 ℤ-값 대칭 쌍선형형식을 분류하는
것이 4-다양체 분류의 선형대수적 핵심이다.

### 6.2 교차형식 분류 정리

단순연결·닫힌·지향 4-다양체 M 에 대해 Q_M 은

- 짝수 (even): ⟨v, v⟩ ∈ 2ℤ, ∀ v, **spin** 조건
- 부호 σ(Q) = b_2^+ - b_2^-
- 대각화 여부: rank, 부호, 타입(짝/홀) 이 동형류를 결정(비정칙 무관, Serre 정리)

### 6.3 Freedman 정리 (1982)

단순연결·닫힌·지향 4-다양체의 **위상** 동형류는 (Q_M, Kirby-Siebenmann 불변량 ks ∈ ℤ/2) 로
결정된다. 두 다양체 M, N 이 Q_M ≅ Q_N 이면 이들은 위상 동형이다 (spin 이면 ks 도 같아야 함).

이 정리는 단순연결 topological 4-다양체의 분류를 대수적 문제로 환원한다.

### 6.4 Donaldson 정리 (1983)

단순연결·닫힌·지향 4-다양체 M 이 매끄럽다면 (smooth), Q_M 이 양정치이거나 음정치인 경우
**대각화** 가능해야 한다. 즉 8+8 형식 (-E_8) 같은 exotic 정치 형식을 smooth 로 실현할 수 없다.

결과: 위상적으로 (Freedman) 가능한 모든 형식 중, smooth 구조를 허용하는 것은 극히 일부다.
같은 위상형 위에 무한히 많은 서로 다른 smooth 구조가 존재하는 예 (R⁴ 에만도 무한히 많은
exotic smooth 구조) — 이는 4차원 고유 현상.

### 6.5 Seiberg-Witten 불변량

1994년 Seiberg-Witten 방정식 도입 이후, Donaldson 불변량보다 계산이 쉬운 Seiberg-Witten
불변량으로 4-다양체 smooth 구조가 더 많이 분류되었다. 기초는 U(1)-gauge 이론 + Dirac 방정식.

---

## 7. 3-다양체의 특수 구조 (푸앵카레 연결)

### 7.1 3-다양체 단순연결 분류

Thurston 기하화 추측(1982) → Perelman 증명(2003) 에 의해, 닫힌 3-다양체는 유한개의
"기하 조각" (8가지 기하) 의 접합으로 분해된다. 단순연결인 닫힌 3-다양체는 S³ 와 위상동치
(원래 푸앵카레 추측, 1904).

### 7.2 Ricci flow 준비

(g_ij) 를 Riemann 계량으로 할 때

```
  ∂g_{ij}/∂t = -2 R_{ij}          (Ricci flow)
```

Perelman 엔트로피 F = ∫(R + |∇f|²)e^{-f} dV 의 monotonicity 로 "scale" 를 조절한다.
구체적 증명은 PROB-P1-7 (푸앵카레 심화) 에서 다룬다.

---

## 8. n=6 연결 (메모만)

1. 4-다양체 교차형식 E_8 은 rank 8, 부호 8, 짝수·정치. σ/4 = 2 에서 rokhlin 정리 등장.
   n=6 지점과의 직접적 수학적 연결은 확보되지 않음 ([N?]).
2. 3-다양체의 Seifert 올뭉치 중 "Brieskorn 구면 Σ(2,3,5)" 는 Poincaré 호몰로지 구면이고,
   2+3+5 = 10 이지만, 2·3·5 = 30, 30/5 = 6 같은 단순연산 일치는 atlas.n6 에 [N?] 로만
   남아있다. 수학적 의의 증명 없음.
3. 6-다양체의 오일러 표수와 Pontryagin 수 관계에 2·3 소인수 구조가 등장하는데 (Hirzebruch
   서명 정리), 이는 6=2·3 의 위상적 반향이라 볼 여지는 있으나 σφ=nτ 정리와 직접 이어지는
   논리는 없다 ([N?]).

모든 연결은 관찰 수준이며, 본 노트는 위상학 자체의 정립에 집중한다.

---

## 9. 실전 훈련 — 손으로 풀 5제

**P1.** π_1(S¹ ∨ S¹) 을 van Kampen 으로 계산하라. (답: 자유군 F_2)

**P2.** 토러스 T² 의 CW 구조 (0-cell 1개, 1-cell 2개, 2-cell 1개) 로 세포 호몰로지를
직접 계산하라: H_0=ℤ, H_1=ℤ², H_2=ℤ. 경계사상이 0 임을 확인.

**P3.** ℂP² 의 cup product 구조 H^*(ℂP²; ℤ) = ℤ[α]/α³, deg α=2, ⟨α², [ℂP²]⟩=1 을 증명하라.

**P4.** K3 곡면의 교차형식이 (-E_8) ⊕ (-E_8) ⊕ 3H (H 는 hyperbolic) 로 rank 22, 부호 -16
짝수임을 확인하라. 이 때 K3 는 spin 4-다양체.

**P5.** Hopf 사상 S³ → S² 가 π_3(S²) = ℤ 의 생성자임을 Hopf 불변량으로 보여라. (사상 f
의 mapping cone C_f 에서 cup product 가 0 이 아닌 것이 핵심)

---

## 10. 읽기 경로와 다음 단계

### 10.1 복습 순서

1주차: Hatcher §1 (π_1, van Kampen) + §2 (호몰로지 singular)
2주차: Hatcher §3 (코호몰로지, cup) + 보편계수정리
3주차: Bredon §VI (매끄러운 다양체 위상) + de Rham
4주차: Freedman-Quinn §1~2 (4-다양체 교차형식) + Milnor-Stasheff §9 (서명 정리)

### 10.2 P2 준비

- 스펙트럼 수열 (Serre, Adams)
- 안정 호모토피군 π^s_*
- K-이론과 Chern character
- Seiberg-Witten moduli space

### 10.3 다른 노트와의 연결

- PURE-P1-5 (게이지 이론) ↔ cup product = Chern-Weil 매끄러운 표현
- PURE-P1-4 (대수기하 Hodge) ↔ (p,q) 분해는 H^k_{dR} 의 Kähler 조건 하 정제
- PROB-P1-7 (푸앵카레) ↔ 3-다양체 기하화

---

## 11. 출처 정리

- Hatcher "Algebraic Topology" Cambridge 2002 — 표준 교과서, §1~3 집중
- Bredon "Topology and Geometry" GTM 139, 1993 — 기하학적 관점, §IV, §VI
- Milnor-Stasheff "Characteristic Classes" Princeton 1974 — §1~§9
- Freedman-Quinn "Topology of 4-Manifolds" Princeton 1990 — 4-다양체 topological 분류
- Thurston "Three-Dimensional Geometry and Topology" vol.I Princeton 1997 — 3-다양체 기하화 배경
- Donaldson-Kronheimer "The Geometry of Four-Manifolds" Oxford 1990 — §1, §9 가 분류와 smooth

본 노트는 위 6개 전거 중 핵심 선별하여 P1 학습용으로 한글 재정리한 것이다. 원전에서 벗어나는
주장은 없음.

---

## 12. 추가 논제 — Spectral Sequence 맛보기

P1 범위를 넘어서지만, P2 에서 반드시 만나게 되는 **Serre 스펙트럼 수열** 과
**Adams 스펙트럼 수열** 의 아주 기초만 부록으로 기록한다.

### 12.1 Serre 스펙트럼 수열

파이버(fibration) F → E → B 에 대해

```
  E_2^{p,q} = H^p(B; H^q(F; G)) ⟹ H^{p+q}(E; G)
```

이 수열은 E 의 코호몰로지를 B 와 F 의 코호몰로지로부터 "점진적 근사" 로 계산한다.
페이지 E_r 에서 E_{r+1} 로 가면 d_r 차의 boundary 를 취한다.

대표 예: S¹ → S³ → S² (Hopf 파이버). Serre 로 H^*(S³) 재계산 가능.

### 12.2 Leray 스펙트럼 수열

(연속 사상 f: X → Y 에 대해 일반화) sheaf 코호몰로지에서도 같은 구조가 나타난다.

### 12.3 Adams 스펙트럼 수열

안정 호모토피군 π^s_*(X) 를 Ext_{A}(H*(X; 𝔽_p), 𝔽_p) 에서 근사. Steenrod 대수 A 가
central. 구체 계산은 매우 복잡.

### 12.4 사용 목표 (P2~P3)

- 구면 안정 호모토피 π^s_n 을 부분적으로 계산
- K-이론과 복소 cobordism 사이의 관계 추적
- Seiberg-Witten 과 구조적 연결

---

## 13. 추가 논제 — Kirby 그림과 4-다양체

### 13.1 Kirby 다이어그램

4-다양체를 1-핸들과 2-핸들의 부착으로 그림으로 표현. 2-핸들은 framed knot 로,
1-핸들은 "dotted unknot" 로. 표준 교재: Gompf-Stipsicz "4-Manifolds and Kirby Calculus"
AMS 1999.

### 13.2 exotic ℝ⁴

ℝ⁴ 위에 표준 smooth 구조와 비동치인 무한히 많은 smooth 구조 존재. Donaldson 정리 귀결.
이는 4차원에만 있는 이상 현상.

### 13.3 연결과 P2 예고

PROB-P2 단계에서 Seiberg-Witten 불변량 계산 + 4-다양체 smooth 분류 재도전 논의.

---

## 14. 다음 문서

- PURE-P1-7 : 복잡도 이론 기초 (Cook-Levin, NP-complete)
- PROB-P1-5 : BT-545 Hodge 추측 심화
- PROB-P1-7 : BT-547 푸앵카레 심화
- N6-P1-3 : n=6 정직성 원칙

위상학은 다른 순수수학 노트들의 기반이 되므로, 본 문서 완료 후 PURE-P1-7 (복잡도)·
PROB-P1-5·PROB-P1-7 등 응용 주제로 넘어간다.
