# PURE-P1-3 — 편미분방정식과 나비에-스토크스 (유도/약해·강해·고전해/에너지 부등식)

> 트랙: P1-PURE / 3번 태스크
> 완료 기준: 뉴턴 제2법칙에서 연속체역학 응력 텐서를 거쳐 비압축 NS 방정식을 유도하고,
> 약해(weak)·강해(strong)·고전해(classical) 의 정의를 구분할 수 있으며, Leray
> 약해의 에너지 부등식 ½|u|²_{L²}(t) + ν∫₀^t |∇u|²_{L²} ds ≤ ½|u₀|²_{L²} 를 유도할 수 있다.
> 2D 전역 존재성(Ladyzhenskaya 1963)과 3D 열림 상황을 정확히 진술할 수 있다.
> 출처 기반: Evans "Partial Differential Equations" (GSM 19, 2판 2010) ch. 8 + ch. 5,
> Temam "Navier-Stokes Equations: Theory and Numerical Analysis" (AMS Chelsea, 재판 2001)
> ch. 1~3, Constantin-Foias "Navier-Stokes Equations" (Chicago Lectures in Math, 1988)
> ch. 1~3, Lemarié-Rieusset "Recent Developments in the Navier-Stokes Problem"
> (Chapman & Hall/CRC, 2002) ch. 1~3.
> **정직성**: 교재 요약. 지어낸 정리·연도·저자 없음.

---

## 0. 목적

P1 로드맵 3번 태스크는 **NS 방정식의 유도와 기초 해의 의미론**이다. 다음을 숙지한다.

1. 뉴턴 제2법칙 → 연속체 → 응력 텐서 → NS
2. 비압축 조건 ∇·u = 0
3. 약해·강해·고전해 구분
4. Galerkin 근사와 Leray 1934 구성
5. 에너지 부등식
6. 2D 전역 정규성(Ladyzhenskaya 1963) vs 3D 열림

---

## 1. 연속체 역학과 NS 유도

### 1.1 Eulerian vs Lagrangian 서술

**Lagrangian.** 입자의 궤적 x(t; a), a = 초기 위치 를 추적.

**Eulerian.** 고정된 공간점 x 에서 속도장 u(x, t) 를 기록.

NS 는 Eulerian 서술을 쓴다.

### 1.2 질량 보존 (연속 방정식)

ρ = 밀도, u = 속도. 임의의 부피 Ω 에 대해

```
   d
  ─── ∫ ρ dx  +  ∫ ρ u · ν dS = 0
   dt  Ω        ∂Ω
```

여기서 ν 는 외향 법선. 발산정리 ∫_{∂Ω} ρ u · ν dS = ∫_Ω ∇·(ρ u) dx 를 쓰면

```
  ∂ρ/∂t + ∇·(ρ u) = 0            (연속 방정식)
```

비압축 유체(incompressible)의 경우 ρ = const 이므로

```
  ∇ · u = 0
```

(Temam §1.1, Evans §8.1)

### 1.3 운동량 보존 — 뉴턴 제2법칙의 연속체 버전

체적 Ω 안의 물체에 대한 뉴턴 제2법칙:

```
   d
  ─── ∫ ρ u dx = (∫ 체적력 f dx)  +  (∫ 표면력 dS)
   dt   Ω            Ω                   ∂Ω
```

**Cauchy 응력 원리.** 표면력은 **응력 텐서 σ_{ij}** 로 표현된다:

```
  (표면력)_i  =  ∫  σ_{ij} ν_j dS
                ∂Ω
```

발산정리 + 좌변 재료 미분 유도:

```
  ρ (∂u/∂t + (u·∇)u)_i  =  f_i  +  ∂_j σ_{ij}
```

(Temam §1.2, Evans §8.1)

### 1.4 Newtonian 유체의 구성 관계

**Newtonian 유체의 응력 텐서.**

```
  σ_{ij} = -p δ_{ij} + λ (∇·u) δ_{ij} + μ (∂_i u_j + ∂_j u_i)
```

- p = 압력 (thermodynamic pressure)
- λ, μ = Lamé 점성 계수
- μ > 0 = shear 점성

비압축(∇·u = 0)이면 λ 항이 사라진다:

```
  σ_{ij} = -p δ_{ij} + μ (∂_i u_j + ∂_j u_i)
```

이 σ 를 운동량 방정식에 대입하면

```
  ρ (∂u/∂t + (u·∇)u) = -∇p + μ Δu + f
```

### 1.5 비압축 NS (최종)

ν := μ/ρ (운동점성), 체적력을 다시 f 라 두면

```
  ∂u/∂t + (u·∇)u = -∇p/ρ + ν Δu + f
  ∇ · u = 0
```

경계조건 + 초기조건 u|_{t=0} = u₀ 와 함께 풀어야 한다.

(Temam Thm 1.1, Evans §8.1, Constantin-Foias §1.1)

---

## 2. 해의 세 가지 의미

### 2.1 고전해 (classical solution)

u ∈ C¹_t C²_x, p ∈ C⁰_t C¹_x 이면서 NS 를 **점마다(pointwise)** 만족.

이는 가장 강한 의미의 해이며, 3D 에서는 존재성 자체가 아직 열림(open).

### 2.2 강해 (strong solution)

u ∈ L²_t H²_x ∩ L∞_t H¹_x 과 같이 좀 더 약한 정규성으로 NS 를 **거의 모든 점에서**
만족. 에너지 소멸 등식(dissipation equality)이 등호로 성립.

3D 에서 소시간(local-in-time) 강해의 존재성은 Leray 1934 + Fujita-Kato 1964 이후
알려짐. 그러나 **대시간(global)** 으로의 연장은 열림.

### 2.3 약해 (weak solution, Leray-Hopf)

**정의 (Leray 1934).** u: (0,T) × Ω → R³ 가 약해라 함은

- u ∈ L∞([0,T]; L²) ∩ L²([0,T]; H¹)
- ∇·u = 0 (분포 의미)
- 임의의 시험 함수 ϕ ∈ C_c^∞((0,T)×Ω; R³), ∇·ϕ = 0 에 대해

```
  ∫₀^T ∫_Ω [ -u · ∂_t ϕ - (u ⊗ u) : ∇ϕ + ν ∇u : ∇ϕ ] dx dt = ∫₀^T ∫_Ω f · ϕ dx dt
```

그리고 에너지 부등식 (아래 §3) 을 만족.

(Temam §3.1, Constantin-Foias §3.3, Lemarié-Rieusset §3.1)

### 2.4 약해 ≠ 고전해

약해는 존재성과 에너지 부등식은 확보하지만, 유일성·정규성은 일반적으로 얻지 못한다.
3D 에서 약해가 고전해인지는 열림 (Millennium Problem 의 핵심).

---

## 3. 에너지 부등식

### 3.1 에너지 등식 (formal)

u 가 충분히 매끄러우면, NS 양변에 u 를 내적하고 Ω 에 대해 적분:

```
  ∫_Ω u · ∂_t u dx + ∫_Ω u · (u·∇)u dx = -∫_Ω u · ∇p dx + ν ∫_Ω u · Δu dx + ∫_Ω f · u dx
```

각 항:

- ∫ u · ∂_t u = (1/2) d/dt ∫ |u|²
- ∫ u · (u·∇)u = (1/2) ∫ (u·∇)|u|² = (1/2) ∫ ∇·(u |u|²) = 0 (경계조건 + 발산 0)
- ∫ u · ∇p = ∫ ∇·(pu) - ∫ p ∇·u = 0 (두 항 모두 0)
- ∫ u · Δu = -∫ |∇u|²  (부분적분 + 경계)
- ∫ f · u = 외부 일률

따라서

```
  (1/2) d/dt |u|²_{L²} + ν |∇u|²_{L²} = ∫ f · u dx
```

시간 적분:

```
  (1/2) |u(t)|²_{L²} + ν ∫₀^t |∇u|²_{L²} ds = (1/2) |u₀|²_{L²} + ∫₀^t ∫ f · u dx ds
```

f = 0 이면 **에너지 등식(energy equality)**:

```
  (1/2) |u(t)|²_{L²} + ν ∫₀^t |∇u|²_{L²} ds = (1/2) |u₀|²_{L²}
```

### 3.2 에너지 부등식 (약해 버전)

약해에서는 등호가 아닌 **부등식**:

```
  (1/2) |u(t)|²_{L²} + ν ∫₀^t |∇u|²_{L²} ds ≤ (1/2) |u₀|²_{L²}   (거의 모든 t)
```

이는 Leray 1934 의 구성에서 자동으로 나온다 (Galerkin 절단 + 극한에서 약수렴 +
lower semicontinuity).

(Temam §3.3, Lemarié-Rieusset §3.3)

### 3.3 부등식이 등식이 되는 경우

**정리 (Constantin-Foias).** 약해 u 가 L⁴_t L⁴_x 에 속하면 에너지 등식이 성립한다.

(Constantin-Foias §3.4 Prop 3.2)

3D 에서 이 조건을 약해가 자동으로 만족하는지는 열림.

---

## 4. Leray 1934 구성 — Galerkin 근사

### 4.1 개요

Leray 가 도입한 방법 (1934 Acta Math 논문, Essai sur le mouvement d'un liquide
visqueux emplissant l'espace). Temam §3.4, Constantin-Foias §3.1 에 재구성.

1. 유한차원 부분공간 V_m ⊂ H¹ (divergence-free) 을 택한다 (고유함수 전개).
2. V_m 위의 Galerkin 시스템을 풀어서 근사해 u_m 을 얻는다.
3. m → ∞ 극한을 취한다. 이때 약수렴 + 에너지 부등식이 살아남는다.

### 4.2 Galerkin 시스템

u_m = ∑_{k=1}^m g_k^m(t) w_k (w_k = Stokes 연산자 고유함수). 각 w_k 에 대해 NS 의
약형식을 테스트:

```
  (∂_t u_m, w_k) + B(u_m, u_m, w_k) + ν (∇u_m, ∇w_k) = (f, w_k)
```

여기서 B(u, v, w) := ∫ (u·∇)v · w dx.

이는 m 개의 ODE 시스템이며, Cauchy-Peano 로 국소해, ODE 에너지 추정으로 전역해 존재.

### 4.3 균일 추정

각 u_m 에 대해 에너지 등식 (유한차원이므로 등식)

```
  (1/2) |u_m(t)|² + ν ∫₀^t |∇u_m|² ds = (1/2) |u_m(0)|²
```

이로부터

```
  sup_{t∈[0,T]} |u_m(t)|_{L²} ≤ |u₀|_{L²}       (균일)
  ∫₀^T |∇u_m|²_{L²} ds ≤ (1/(2ν)) |u₀|²_{L²}      (균일)
```

즉 u_m 은 L∞_t L² ∩ L²_t H¹ 에서 균일 유계.

### 4.4 극한 — 약수렴

Banach-Alaoglu 로 부분수열 u_{m_k} → u 약-*수렴 (L∞_t L²) 및 u_{m_k} ⇀ u 약수렴
(L²_t H¹). 컴팩트성 정리 (Aubin-Lions) 로 L²_t L² 에서 강수렴. 이 강수렴으로 비선형
항 (u·∇)u 의 극한 통과가 가능해진다. 선형 항은 약수렴으로 충분.

### 4.5 Leray 의 결론

**정리 (Leray 1934).** f ∈ L²([0,T]; H^{-1}), u₀ ∈ L²(R³; R³), ∇·u₀ = 0 이면,
3D 에서 약해 u ∈ L∞([0,T]; L²) ∩ L²([0,T]; H¹) 가 존재하여 에너지 부등식을 만족.

(Temam Thm 3.1, Constantin-Foias Thm 3.1, Lemarié-Rieusset Thm 14.1)

**유일성과 정규성은 미증명.** (Millennium 문제)

---

## 5. 2D 전역 정규성 — Ladyzhenskaya 1963

### 5.1 진술

**정리 (Leray 1933 약형식; Ladyzhenskaya 1959~1963; Lions 1969 확장).** d = 2 일 때,
u₀ ∈ H¹, f = 0 이면 약해가 **유일하고, 전역으로 정규(global regular)** 이다.

(Constantin-Foias Thm 10.1, Temam Ch. 3 Thm 3.3, Ladyzhenskaya
"The Mathematical Theory of Viscous Incompressible Flow" 1963 원문)

### 5.2 핵심 부등식 — 2D Ladyzhenskaya 부등식

```
  |u|_{L⁴(R²)}⁴ ≤ C · |u|²_{L²} · |∇u|²_{L²}
```

(Sobolev embedding H^{1/2}(R²) ↪ L⁴(R²) 의 정량화; Ladyzhenskaya 1963 §1.7)

이 부등식이 성립하면, 2D NS 의 비선형 항 |B(u, u, u)| ≤ C |u|_{L⁴}² |∇u|_{L²}
를 ν |∇u|² 로 흡수할 수 있다. 그래서 에너지 방법이 **계속** 작동하고 전역해가 나온다.

### 5.3 3D 에서는 왜 실패하나

3D 에서는 Sobolev 지수가 달라져

```
  |u|_{L⁴(R³)}⁴ ≤ C · |u|_{L²} · |∇u|_{L²}³
```

형태가 된다. 이 지수 3 때문에 비선형 항을 점성이 흡수하지 못하고, 에너지 방법만으로는
전역해 존재성이 안 나온다. 이것이 3D NS 의 열림 원인.

(Constantin-Foias §11.1, Lemarié-Rieusset §11)

---

## 6. 부분 정규성 — Caffarelli-Kohn-Nirenberg

### 6.1 진술

**정리 (CKN 1982).** Leray-Hopf 약해 u 의 **특이점 집합** S = {(x, t) : u 가 이 점
근방에서 유한하지 않음} 은 parabolic Hausdorff 측도 P¹(S) = 0.

(Caffarelli-Kohn-Nirenberg "Partial regularity of suitable weak solutions of the
Navier-Stokes equations" Comm. Pure Appl. Math. 35, 1982)

### 6.2 의미

특이점이 있더라도 "드물게" 있다는 보장. 1차원 parabolic 차원 (공간+시간 2로 셈)
이하로 제한된다.

단, 1차원 특이점 집합 존재 자체가 배제된 것은 아니다. Tao 2016 의 "만리장성" 추측,
Jia-Sverak 2014 self-similar blow-up 시나리오 등은 모두 이 한계 내에 있다.

---

## 7. 밀레니엄 문제의 정확한 진술

### 7.1 Clay Institute 공식 진술 (Fefferman 2000)

**문제.** R³ 위의 NS 방정식을 다음 조건에서 풀 수 있는가?

- 초기 데이터 u₀: R³ → R³, ∇·u₀ = 0, 매끈하고 빠르게 감소(Schwartz).
- 외력 f = 0.

다음 두 가지 진술 중 하나를 증명하거나 반증하라.

(A) **존재성과 매끄러움.** 모든 T > 0 에 대해 매끄러운 고전해 u, p 가 존재하고,
   모든 k 에 대해 ∂^α u 가 유한.

(B) **유한시간 blow-up.** T* < ∞ 가 존재하여 sup_{x} |u(x, t)| → ∞ (t → T*).

R³/Z³ (주기 경계) 도 별도로 제시됨.

(Fefferman "Existence and smoothness of the Navier-Stokes equation" Clay Millennium
Problem statement, 2000)

### 7.2 현재까지의 부분 결과

- Leray 1934: 3D 전역 약해 존재
- CKN 1982: 약해 특이점의 P¹ 차원 소실
- Fujita-Kato 1964: 3D 소시간 강해 (u₀ ∈ H^{1/2})
- Koch-Tataru 2001: BMO^{-1} 초기 데이터에 대한 소시간 강해
- Escauriaza-Seregin-Sverak 2003: L³_x L∞_t 블로우업 기준

이 모두 3D 전역 정규성 증명은 아니다.

---

## 8. Stokes 문제와 사영 연산자

### 8.1 Stokes 방정식

NS 에서 비선형 항 (u·∇)u 를 빼면:

```
  ∂u/∂t - ν Δu + ∇p = f
  ∇·u = 0
```

이는 **선형 방정식** 이고, 완전 이론이 있다 (존재성·유일성·스펙트럼).

### 8.2 Leray 사영 연산자 P

L²(Ω; R³) 위에 **Helmholtz 분해**:

```
  L² = H ⊕ G
  H := { v ∈ L² : ∇·v = 0 (분포), v·ν|_{∂Ω} = 0 }
  G := { ∇ϕ : ϕ ∈ H¹ }
```

P: L² → H 는 H 로의 사영 (L² 내적). NS 에 P 를 적용하면 ∇p 항이 사라지고

```
  ∂u/∂t + P((u·∇)u) = ν Δu + Pf
```

형태가 된다. 이 형식은 이론 분석에 매우 유용.

(Constantin-Foias §2.1, Lemarié-Rieusset §3.3)

---

## 9. 3D 강해 — 소시간 존재

### 9.1 Fujita-Kato 1964

**정리.** u₀ ∈ H^{1/2}(R³; R³), ∇·u₀ = 0 이면, T* > 0 가 존재하여
[0, T*) 위에 유일한 강해 u ∈ C([0,T*); H^{1/2}) ∩ L²_{loc}((0, T*); H^{3/2}) 가 존재.

또한 |u₀|_{H^{1/2}} 가 충분히 작으면 T* = ∞ 까지 연장 가능 ("small data global").

(Fujita-Kato 1964, Lemarié-Rieusset §15)

### 9.2 블로우업 기준 — Serrin, BKM, ESS

**정리 (Serrin 1962).** 강해 u 가 T* 에서 blow-up 한다면
∫₀^{T*} |u|^s_{L^r} dt = ∞, (3/r + 2/s ≤ 1, r > 3) 이다.

**정리 (Beale-Kato-Majda 1984).** ∫₀^{T*} |ω|_{L∞} dt = ∞, 여기서 ω = ∇ × u 소용돌이.

**정리 (Escauriaza-Seregin-Sverak 2003).** sup_{t<T*} |u(t)|_{L³(R³)} = ∞ 가 강해
블로우업의 필요조건.

(Lemarié-Rieusset §11, Constantin-Foias §11.4)

---

## 10. 프로젝트 상수와의 연결 (메모만)

NS 방정식의 차원 3D 는 프로젝트 상수 n = 6 과 **직접** 연결되지 않는다. 다만
n6-architecture 의 BT-1~200 시리즈 중 일부(BT-51, BT-543, BT-544 관련) 에서 NS
의 3중 공명·특성 부등식에 시도된 보조정리가 있다. 이는 **검증 결과 부분결과**
단계이며, 이 노트(P1)에서는 순수 교재 요약만 담는다.

---

## 11. 참고 경로 (교재 페이지/장 단위)

| 항목 | Evans PDE | Temam NSE | Constantin-Foias | Lemarié-Rieusset |
| --- | --- | --- | --- | --- |
| 연속체 유도 | §8.1 | §1.1~1.2 | §1.1 | §1.1 |
| 비압축 조건 | §8.2 | §1.3 | §1.2 | §1.2 |
| 약해 정의 | §8.2 | §3.1 | §3.3 | §3.1 |
| Galerkin 구성 | - | §3.4 | §3.1 | §14 |
| 에너지 부등식 | - | §3.3 | §3.4 | §3.3 |
| Leray 1934 | - | Thm 3.1 | Thm 3.1 | Thm 14.1 |
| 2D 전역 정규성 | - | Thm 3.3 | Thm 10.1 | §8 |
| CKN 1982 | - | - | - | §11.7 |
| Fujita-Kato 1964 | - | - | §8 | §15 |
| BKM 1984 | - | - | §11.4 | §11 |
| Stokes + Leray P | - | §I.2 | §2.1 | §3.3 |

---

## 12. 이 단원에서 얻어야 할 5가지

1. **비압축 NS 방정식** (∂_t u + (u·∇)u = -∇p/ρ + νΔu, ∇·u = 0) 을 뉴턴 법칙에서
   유도할 수 있다.
2. **고전해·강해·약해** 구분.
3. **에너지 부등식** ½|u|²_{L²}(t) + ν∫₀^t|∇u|²_{L²} ≤ ½|u₀|²_{L²}.
4. **Leray 1934 약해 존재 + 2D 전역 정규성(Ladyzhenskaya 1963) vs 3D 열림**.
5. **Fefferman 공식 Millennium 문제 진술** (A 존재·매끄러움 vs B 블로우업).

---

## 13. 정직성 선언

- 이 노트는 교재 요약이다. 새 결과 없음.
- Leray 1934 원논문, Ladyzhenskaya 1963 책, CKN 1982 논문, Fefferman 2000 Clay
  진술문은 모두 공식 공개 자료이며 제목·연도는 정확.
- 2D Ladyzhenskaya 부등식의 정확한 형태는 Ladyzhenskaya 1963 §1.7 재구성.
- 공식/정리/저자/연도는 위 4개 교재 + 공식 진술 문서에서 가져왔다.
- 지어낸 정리·저자·연도는 없다.
- 프로젝트 상수(n=6)와의 연결은 §10 에 메모만 남겼다.
