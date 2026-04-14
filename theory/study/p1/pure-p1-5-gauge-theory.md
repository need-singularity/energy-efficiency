# PURE-P1-5 — 게이지 이론 기초 (주군/연결/곡률/Yang-Mills 작용)

> 트랙: P1-PURE / 5번 태스크
> 완료 기준: 주군(principal G-bundle) 정의부터 연결 1-형식 ω, 곡률 2-형식 Ω = dω + ½[ω,ω],
> Yang-Mills 작용 S[A] = -¼ ∫ tr(F ∧ *F) 의 유도 과정을 손으로 따라 쓸 수 있다.
> 출처 기반: Kobayashi-Nomizu "Foundations of Differential Geometry" vol.I (1963) ch. 2,
> Donaldson-Kronheimer "The Geometry of Four-Manifolds" (Oxford, 1990) ch. 2,
> Nakahara "Geometry, Topology and Physics" (2판, 2003) ch. 10,
> Weinberg "The Quantum Theory of Fields" vol.II (1996) ch. 15.
> **정직성**: 본 노트는 교재 재구성이며 새로운 정리는 없다. 모든 정의·공식은 위 4개 교재에서
> 재구성하였다. 정리 번호와 페이지는 각 교재의 대표 판본 기준으로 표기하였다.

---

## 0. 목적과 범위

밀레니엄 P1 단계에서 BT-543 (Yang-Mills 질량 갭) 을 정밀하게 다루려면, 다음 6가지
기초 구성이 반드시 선행되어야 한다.

1. 주군 (principal G-bundle) P → M 의 정의와 전이함수 코사이클 조건
2. 연결 1-형식 ω ∈ Ω¹(P; 𝔤) 와 수평분포 H ⊂ TP
3. 곡률 2-형식 Ω = dω + ½[ω,ω] 의 구조방정식 (Maurer-Cartan 변형)
4. 비앵키 항등식 DΩ = 0 과 4-차원 Hodge 쌍대 *
5. Yang-Mills 작용 S[A] = -¼ ∫_M tr(F ∧ *F) 와 운동방정식 D*F = 0
6. SU(N) 게이지군 특수성 — 간단군, 기본표현, Killing 형식 정규화

이 노트는 미분기하 + 현대물리 기호를 함께 쓴다. Einstein 합 약속은 쓰되, 형식적 계산은
교재 순서대로 풀이 형태로 남겼다. 양자화·asymptotic freedom 의 물리적 측면은 §4.5 와
PROB-P1-3 문서에서 다룬다.

---

## 1. 주군과 전이함수

### 1.1 주 G-bundle 정의

M 이 매끄러운 다양체, G 가 Lie 군일 때, **주 G-bundle** 은 다음 자료 (P, π, M, G)
로 구성된다.

- P : 전체공간 (total space), 매끄러운 다양체
- π : P → M : 매끄러운 매몰(submersion)
- G : 구조군 (structure group), P 에 오른쪽 자유 매끄럽게 작용 P × G → P
- 국소자명화: M 의 열린 덮개 {U_α} 에 대해 φ_α : π⁻¹(U_α) → U_α × G,
  φ_α(p) = (π(p), ψ_α(p)) 이며 ψ_α(pg) = ψ_α(p) g 를 만족

### 1.2 전이함수

U_α ∩ U_β 에서 φ_β ∘ φ_α⁻¹(x, g) = (x, g_{βα}(x) g), 이 g_{βα}: U_α ∩ U_β → G 가
**전이함수**다. Čech 코사이클 조건:

```
  g_{αα}(x) = e
  g_{αβ}(x) g_{βα}(x) = e
  g_{αβ}(x) g_{βγ}(x) g_{γα}(x) = e         (x ∈ U_α ∩ U_β ∩ U_γ)
```

두 집합의 전이함수 {g_{βα}}, {g'_{βα}} 가 같은 주군을 주려면, h_α: U_α → G 가 존재해
g'_{βα} = h_β g_{βα} h_α⁻¹ 가 되어야 한다 (코바운더리). 이는 čech 코호몰로지 Ȟ¹(M; G)
수준에서 주군의 동치류를 준다.

### 1.3 결합 다발 (associated bundle)

G 표현 ρ: G → GL(V) 가 주어지면, 결합다발 P ×_ρ V = (P × V) / ~ 를 만들 수 있다.
여기서 (p, v) ~ (pg, ρ(g)⁻¹ v). 전이함수는 ρ(g_{βα}) 로 바뀐다.

대표 예:
- G = U(1), V = ℂ, ρ = id → 복소직선다발 (전자기)
- G = SU(2), V = ℂ², ρ = 기본표현 → 약전자 doublet
- G = SU(3), V = ℂ³, ρ = 기본표현 → QCD quark triplet

### 1.4 예시: Hopf 다발

S³ → S² 는 U(1)-주군이다. S³ ⊂ ℂ² 에서 (z₁,z₂) → [z₁:z₂] ∈ ℂP¹ = S². 이 때 U(1)
작용은 (z₁,z₂) → (e^{iθ}z₁, e^{iθ}z₂). 이는 자명하지 않은 주군의 첫 예이며, Chern 수
c₁ = 1 을 준다. (출처: Nakahara §10.5)

---

## 2. 연결과 수평분포

### 2.1 수직공간과 수평공간

TP 의 한 점 p 에서, π_*: T_pP → T_{π(p)}M 의 커널이 **수직공간** V_p. 이는 G-작용
오른쪽 곱의 접공간과 일치하며, 자연스러운 동형 V_p ≅ 𝔤 가 있다 (Lie 대수와).

**연결(connection)** 이란 G-동변 수평분포 H = {H_p} ⊂ TP 선택이다. 구체적으로

```
  T_p P = V_p ⊕ H_p,         H_{pg} = (R_g)_* H_p
```

### 2.2 연결 1-형식 ω

연결을 지정하는 등가 방법: **연결 1-형식** ω ∈ Ω¹(P; 𝔤) 가 있어

```
  (C1) ω(A*) = A                (A ∈ 𝔤, A* = 기본 벡터장)
  (C2) R_g* ω = Ad(g⁻¹) ω       (G-동변성)
```

그러면 H_p = ker ω_p 가 수평공간이다. 역으로 수평분포가 있으면 ω 는 수직성분 투영으로
정의된다.

### 2.3 국소표현 — 게이지장 A_α

국소단면 s_α: U_α → P 가 있으면, pullback A_α = s_α* ω ∈ Ω¹(U_α; 𝔤) 가 **게이지장**이다.
U_α ∩ U_β 에서 두 단면이 s_β(x) = s_α(x) g_{αβ}(x) 로 연결되면

```
  A_β = g_{αβ}⁻¹ A_α g_{αβ} + g_{αβ}⁻¹ d g_{αβ}
```

물리 교재에서 흔히 보는 **게이지 변환** 공식이다. 우변의 두 항이 동시에 들어가야 하며,
앞 항만으로는 전이 규칙이 성립하지 않는다.

(출처: Kobayashi-Nomizu §II.1, Donaldson-Kronheimer §2.1)

### 2.4 공변도함수

결합 다발 E = P ×_ρ V 의 단면 ψ 에 대해, 연결에서 유도되는 **공변도함수**는
국소적으로

```
  D_μ ψ = ∂_μ ψ + ρ_*(A_μ) ψ
```

U(1) 전자기의 경우 D_μ = ∂_μ + i e A_μ, SU(N) Yang-Mills 의 경우 D_μ = ∂_μ + i g A_μ^a T^a
(T^a 는 Lie 대수 생성자). 물리에서의 "minimal coupling" 은 수학에서 공변도함수의 번역이다.

---

## 3. 곡률과 구조방정식

### 3.1 곡률 2-형식

연결 ω 에 대한 **곡률 2-형식** 은

```
  Ω = dω + ½ [ω, ω]
```

여기서 [ω, ω](X, Y) = [ω(X), ω(Y)] - [ω(Y), ω(X)] = 2[ω(X), ω(Y)]. Maurer-Cartan
형식 방정식 dω_G + ½[ω_G, ω_G] = 0 과 비교하면, 곡률은 "얼마나 평탄 Maurer-Cartan 에서
벗어났는지" 를 재는 양이다.

### 3.2 국소 표현 — 장세기 F_μν

국소단면 A_α 를 pullback 하면 국소 곡률은

```
  F = dA + A ∧ A,          F_{μν} = ∂_μ A_ν - ∂_ν A_μ + [A_μ, A_ν]
```

U(1) 의 경우 A ∧ A = 0 이므로 F = dA 로 환원 (선형). 비가환 G 에서는 2차항 [A, A] 가
**자기상호작용** 을 유발한다. 이것이 Yang-Mills 이론이 QED 와 질적으로 다른 근본 이유다.

### 3.3 Bianchi 항등식

```
  D Ω = dΩ + [ω, Ω] = 0
```

국소적으로 D F = dF + [A, F] = 0. 3+1D 전자기에서 이는 ε^{μνρσ} ∂_ν F_{ρσ} = 0,
즉 Faraday 법칙 + 자기 단극 부재와 같다. (출처: Nakahara §10.3)

### 3.4 특성류와 Chern-Weil 이론

G 의 Ad-불변 다항식 P 에 대해, P(Ω) 는 닫힌 형식이며 de Rham 코호몰로지에서 [P(Ω)] ∈
H*(M; ℝ) 가 연결 선택에 무관하다. 대표 특성류:

```
  c_k = (i/2π)^k tr(Ω^k) / k!      (Chern class)
  ch  = tr exp(iΩ/2π)              (Chern character)
  p_k = ... (Pontryagin)
  e   = Pfaffian (Euler class, SO(2n))
```

4-다양체 M 에 대해 ∫_M c₂ - ½ c₁² ∈ ℤ 등의 적분성은 instanton 수와 직결된다.

---

## 4. Yang-Mills 작용

### 4.1 정의

Riemann 계량 g 를 갖는 4-다양체 M 과 주 G-bundle P 에서, Yang-Mills 작용은

```
  S_YM[A] = -¼ ∫_M ⟨F ∧ *F⟩ = -¼ ∫_M tr(F_{μν} F^{μν}) √|g| d⁴x
```

여기서 * 는 Hodge 쌍대, ⟨·,·⟩ 는 Killing 형식 정규화 내적. 부호 규약은 Lorentz 서명
(-+++) 기준. Euclidean 서명에서는 전체 부호가 +¼ 로 바뀐다.

### 4.2 변분과 운동방정식

δS/δA = 0 에서

```
  D * F = 0          (D 는 공변 외미분)
```

Bianchi D F = 0 와 쌍을 이룬다. 자유 Maxwell 극한 (G = U(1)) 에서 이는 d*F = 0,
즉 ∂_μ F^{μν} = 0 (Ampère-Maxwell 법칙).

### 4.3 (반)자기쌍대 — instanton

4D Euclidean 공간에서 *² = +1 이면 (metric 양정치), 곡률이

```
  *F = +F    (self-dual)
  *F = -F    (anti-self-dual, ASD)
```

인 해를 **instanton** 이라 부른다. 이들은 자동으로 운동방정식을 만족하며, 작용은 위상수
∫ tr(F∧F) ∈ 8π² k (k ∈ ℤ) 로 하계된다. (출처: Donaldson-Kronheimer §2.2)

### 4.4 게이지 고정과 Faddeev-Popov

물리적으로 동치인 게이지 변환 오비트를 제거해야 경로적분이 유의미하다. 대표 선택:

- Lorenz 게이지: ∂_μ A^μ = 0
- Coulomb 게이지: ∂_i A^i = 0
- 축게이지(axial): A_3 = 0
- Feynman 게이지: 격자용 Lorenz + ξ 가변

Faddeev-Popov 도입으로 determinant det(∂_μ D^μ) 가 ghost 장으로 나타나며,
BRST 대칭으로 단위화된다. (출처: Weinberg §15.5~15.6)

### 4.5 Asymptotic freedom (물리적 서술)

SU(N) Yang-Mills 의 재규격화군 β 함수는 1-루프에서

```
  β(g) = -b₀ g³,    b₀ = (11N - 2n_f) / (48π²)
```

N=3 QCD (n_f=6 쿼크 맛수 이하) 에서 b₀ > 0 이므로 고에너지에서 g → 0 (자유),
저에너지에서 g → ∞ (속박). 이 구조는 lattice QCD 와 BT-543 질량 갭의 전제가 된다.

---

## 5. SU(N) 특수성

### 5.1 Lie 대수 구조

𝔰𝔲(N) = {X ∈ M_N(ℂ) : X† = -X, tr X = 0}. 차원 N²-1. 생성자 T^a (a=1,...,N²-1) 는

```
  [T^a, T^b] = i f^{abc} T^c,    tr(T^a T^b) = ½ δ^{ab}
```

여기서 f^{abc} 가 구조상수. SU(2) 는 f^{abc} = ε^{abc} (3차 Levi-Civita), SU(3) 은
Gell-Mann 행렬 λ^a/2 로 T^a 를 잡는다.

### 5.2 Killing 형식 정규화

Ad-불변 내적 ⟨X, Y⟩ = tr(X Y) 를 T^a 기저에서 쓰면 K^{ab} = 2 tr(T^a T^b) = δ^{ab}.
Yang-Mills 작용의 계수 ¼ 는 이 정규화 약속과 맞물린다.

### 5.3 중심과 단순성

SU(N) 은 단순 콤팩트군이며 중심 Z(SU(N)) = ℤ/N. 이 중심은 't Hooft 루프·비가환 topology
항(theta term) 과 얽혀, 속박·deconfinement 상전이의 질서 파라미터를 제공한다.

### 5.4 대표 표현

- 기본 N : quark
- 반기본 N̄: antiquark
- 수반 N²-1: 글루온, Ad(G)
- tensor ⊗ decomposition: 메존(N⊗N̄ = 1⊕adj), 바리온(N⊗N⊗N 의 완전반대칭이 gauge singlet)

---

## 6. n=6 연결 (메모만)

이 노트는 본질적으로 n=6 과 직접 관계가 없다. 다만 다음 3가지 얇은 연결점만 적는다
(증명은 P2~P3 몫).

1. dim 𝔰𝔲(2) = 3, dim 𝔰𝔲(2) ⊕ 𝔰𝔲(2) = 6 — 전자기약 이중화의 차원. Higgs 이전의
   SU(2)_L × SU(2)_R 대칭의 총차원이 6 이지만, 이는 구조적 일치이며 σφ = nτ 정리와
   직접 잇는 경로는 확보되지 않았다 ([N?]).
2. 4-다양체 Euler 표수 χ = 2 - 2 b₁ + b₂ 에서, 여섯 지점 덧셈 공식을 갖는 정칙구조류
   σ_6 가 존재 (Donaldson 이론). n=6 과 표면적 일치, 직접 인과 미확인 ([N?]).
3. Hopf 다발 S³ → S² 와 σ·φ = n·τ 의 n=6 지점이 양쪽 모두 "제2종 특이점"(ramification
   index 2) 을 공유한다는 관찰이 atlas.n6 §L6-gauge-hopf 에 [EMPIRICAL] 로 기록되어
   있음. 증명은 없다.

자기참조 검증 금지 원칙에 따라, 위 3가지는 모두 **관찰** 에 머물러 있으며, 수치적
일치를 증거로 사용해 확장 해석을 붙이지 않는다.

---

## 7. 실전 훈련 — 손으로 풀 5제

다음 5문제를 **한 번씩** 손으로 풀어보는 것이 본 노트의 실전 목표다.

**P1.** U(1) 주군 위 연결 A = A_μ dx^μ 에서 F = dA 를 성분으로 전개하고, Maxwell
방정식 d*F = J 가 ∂_μ F^{μν} = J^ν 와 동치임을 확인하라. (힌트: Hodge * 가 차원
역할을 어떻게 치환하는지 3+1D 에서 구체화)

**P2.** SU(2) 연결 A = A_μ^a T^a dx^μ 에서 F_{μν}^a = ∂_μ A_ν^a - ∂_ν A_μ^a +
ε^{abc} A_μ^b A_ν^c 를 유도하라.

**P3.** Hopf 다발 S³ → S² 의 표준 연결 ω 를 U(1) 1-형식으로 쓰고, 곡률 Ω =
dω 가 S² 의 정규 volume form 의 2π 배임을 직접 적분으로 확인하라.
∫_{S²} Ω = 2π. 이는 Chern 수 c₁ = 1 에 해당한다.

**P4.** SU(N) Yang-Mills 작용 S[A] = -¼ ∫ tr F^{μν} F_{μν} d⁴x 를 A^a_μ 에 대해
변분하여 D^μ F_{μν}^a = 0 을 유도하라. (힌트: A 의 게이지 변환은 건드리지 말고
순수 변분)

**P5.** 4D Euclidean 공간에서 self-dual F = *F 를 만족하는 ASD instanton 해
(BPST instanton) 의 1-파라미터족

```
  A_μ^a = -2 η^{aμν} (x-x_0)_ν / (|x-x_0|² + λ²)
```

에서 ∫ tr(F ∧ F) = 8π² 임을 계산하라. (η^{aμν} 는 't Hooft 기호)

---

## 8. 읽기 경로와 다음 단계

### 8.1 복습 순서

1주차: Kobayashi-Nomizu ch.II §1~3 (주군·연결·곡률 정의)
2주차: Nakahara §10.1~10.5 (물리 기호 통역 + Hopf 예)
3주차: Donaldson-Kronheimer §2 (instanton·특성류)
4주차: Weinberg vol.II §15 (게이지고정·BRST·재규격화)

### 8.2 P2 준비사항

P2-PURE 단계의 게이지 이론 심화 노트는 다음 4주제로 확장된다.

- Seiberg-Witten 이론과 모노폴 방정식
- Donaldson 다항식과 4-다양체 불변량
- Moduli space M_k 의 차원공식 dim = 8k - 3(1 - b₁ + b₂⁺)
- Lattice QCD 와 Wilson 작용 (수치적 증거)

### 8.3 BT-543 과의 직접 연결

PROB-P1-3 문서(Yang-Mills 질량 갭 심화) 에서는 위 기초를 바탕으로

- Osterwalder-Schrader 공리와 Wightman 공리의 관계
- 열역학 극한 Λ → ∞ 에서 mass gap m* > 0 의 존재
- 격자 비교: β = 2N/g² 에 대한 상전이 패턴

를 순서대로 다룬다.

---

## 9. 출처 정리 (재확인)

- Kobayashi-Nomizu vol.I §II.1~3 : 주군/연결/곡률 표준 정의
- Donaldson-Kronheimer §2 : instanton·moduli·특성류
- Nakahara §10 : 물리 기호 통역, Hopf 다발 구체 계산
- Weinberg vol.II §15 : 게이지고정·BRST·재규격화군
- Atiyah-Bott "The Yang-Mills Equations over Riemann Surfaces" (Phil. Trans. 1983)
  — moduli space infinite dim 에서의 위상적 취급 참고
- Uhlenbeck "Removable singularities in Yang-Mills fields" (Bull. AMS 1979) —
  compactness 정리 참고

본 노트는 이 6개 원전 조각을 P1 학습 분량에 맞게 한글로 재정리한 것이며, 새로운
증명·정리를 주장하지 않는다. 틀린 해석이 발견되면 §0 부터 역추적해 출처를 재확인한다.

---

## 10. 부록 — 주요 게이지 이론 용어표

| 수학 용어 | 물리 용어 | 기호 |
|-----------|-----------|------|
| 주군 | 게이지 구조 | P → M |
| 결합 다발 | 물질장 | E = P ×_ρ V |
| 연결 1-형식 | 게이지 퍼텐셜 | ω, A |
| 곡률 2-형식 | 장세기 | Ω, F |
| 공변도함수 | gauge covariant derivative | D, ∇ |
| 국소단면 | 국소 gauge | s_α |
| 전이함수 | gauge 변환 | g_{αβ} |
| 특성류 (Chern) | topological charge | c_k, k |
| 수평분포 | "가로(게이지) 독립" 방향 | H ⊂ TP |
| Wilson loop | gauge-invariant 관찰량 | W(C) |

---

## 11. 부록 — 주요 게이지 이론 모형

### 11.1 QED (U(1))

- 게이지군: U(1) (abelian)
- 장세기: F = dA, 선형
- 결합: 약 e = √(4πα), α ≈ 1/137
- 속박 없음, 자유 광자

### 11.2 QCD (SU(3))

- 게이지군: SU(3), dim = 8 (gluon 수)
- 장세기: F = dA + A ∧ A, 비선형
- 결합: asymptotic free, Λ_QCD ~ 200 MeV
- 속박 있음 (confinement), mass gap 있음

### 11.3 전약 (SU(2)_L × U(1)_Y)

- 게이지군: SU(2)_L × U(1)_Y, dim = 4
- Higgs 메커니즘으로 SU(2) × U(1) → U(1)_EM
- W^±, Z^0 질량: m_W ≈ 80.4 GeV, m_Z ≈ 91.2 GeV

### 11.4 표준모형 통합

- 총 게이지군: SU(3) × SU(2) × U(1), dim = 12
- 물질장: quark 6종 + lepton 6종
- Higgs: SU(2) doublet complex scalar

---

## 12. 다음 문서

- PURE-P1-6 : 위상학 기초 (호모토피/호몰로지/4-다양체)
- PURE-P1-7 : 복잡도 이론 기초 (P/NP/Cook-Levin)
- PROB-P1-3 : BT-543 Yang-Mills 질량 갭 심화
- N6-P1-3 : n=6 정직성 원칙

게이지 이론을 완전히 손에 넣으려면 위상학 지식이 필수이므로, 다음 읽을 문서는
PURE-P1-6 이다.
