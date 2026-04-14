# PROB-P1-4 — BT-544 Navier-Stokes 심화 (3D 비압축/Leray 약해/blow-up 시나리오)

> 트랙: P1-PROB / 4번 태스크
> 완료 기준: Clay 공식 명제 (Fefferman 2000) 를 분해하고, 3D 비압축 Navier-Stokes
> 방정식의 약해(Leray-Hopf) 존재와 유일성·정칙성 간극, blow-up 시나리오를
> 자기유사/Type I·II 분류로 설명할 수 있다.
> 출처 기반: Fefferman "Existence and smoothness of the Navier-Stokes equation"
> Clay Millennium 공식 문서(2000),
> Leray "Sur le mouvement d'un liquide visqueux..." (Acta Math. 63, 1934),
> Temam "Navier-Stokes Equations: Theory and Numerical Analysis" (3판, 1984),
> Constantin-Foias "Navier-Stokes Equations" (U. Chicago, 1988),
> Tao "Nonlinear Dispersive Equations" (CBMS 106, 2006) ch. 3,
> Escauriaza-Seregin-Šverák "L_∞,3 solutions of Navier-Stokes and backward uniqueness"
> (Russian Math. Surveys 2003).
> **정직성**: 본 노트는 Clay 공식 명제와 표준 NS 교재의 재구성이다. 새로운 정리는 없다.
> 모든 진술은 위 6개 전거에서 P1 학습 분량에 맞춰 재정리하였고, 미해결 부분은 [미증명]
> 또는 [부분결과] 로 표기한다.

---

## 0. 목적과 범위

Clay BT-544 는 다음을 요구한다: "3차원 공간 ℝ³ (또는 주기구역 𝕋³) 에서 매끄러운 초기값
u_0 로 시작한 비압축 Navier-Stokes 방정식의 해가 t ∈ [0, ∞) 전 구간에서 매끄럽게 존재하거나,
또는 매끄럽지 않아지는 (blow up) 초기값이 있는지 밝히시오."

본 노트가 다루는 7가지:

1. Navier-Stokes 방정식 재유도 (Euler 항 + 점성)
2. Leray 1934 약해(약풀이) 존재정리와 Hopf 확장
3. 정칙성 기준: L³, L^{3,∞}, vorticity L¹ 등
4. Blow-up 시나리오 분류: Type I, Type II, 자기유사
5. 에너지 보존·소산 부등식과 에너지 조건
6. 부분 정칙성 정리 (Caffarelli-Kohn-Nirenberg 1982)
7. 최근 진전 (Escauriaza-Seregin-Šverák 2003, Tao scale-critical 접근)

---

## 1. 방정식과 기본 설정

### 1.1 3D 비압축 Navier-Stokes

u = (u_1, u_2, u_3): ℝ³ × [0,T) → ℝ³ (속도), p: ℝ³ × [0,T) → ℝ (압력). ν > 0 점성.

```
  ∂_t u + (u · ∇) u = -∇p + ν Δu + f        (운동량 보존)
  ∇ · u = 0                                  (비압축)
  u(x, 0) = u_0(x)                           (초기조건)
```

Clay 명제 공식: f = 0 (외력 없음), u_0 는 C^∞, 고차 미분 빠른 감소 (Schwartz 공간).

### 1.2 에너지 항등식

정식 해에 대해

```
  (1/2) d/dt ∫ |u|² dx = -ν ∫ |∇u|² dx + ∫ f·u dx
```

f=0 이고 정식 해가 있다면 ∫ |u(t)|² dx ≤ ∫ |u_0|² dx (에너지 감소).

### 1.3 스케일 대칭성

(λ, u_0) → λ u(λ x, λ² t) 가 비압축 NS 의 대칭성. ||u||_{L³} 와 ||u||_{L^{3,∞}} 는
임계 스케일 (scale-invariant) 인 노름. L² 는 초임계(supercritical) 로 정칙성 판정에
직접 쓰기 어렵다.

---

## 2. Leray 약해 존재정리 (1934)

### 2.1 약해 정의

u ∈ L²((0,T); H¹(ℝ³)) ∩ L^∞((0,T); L²(ℝ³)) 가 **Leray-Hopf 약해** iff
모든 시험함수 φ ∈ C_c^∞(ℝ³ × [0,T); ℝ³), ∇·φ = 0 에 대해

```
  ∫∫ [u · ∂_t φ + (u ⊗ u) : ∇φ - ν ∇u : ∇φ] dx dt = -∫ u_0 · φ(x,0) dx
```

와 에너지 부등식 ∫|u(t)|² dx + 2ν ∫₀^t ∫|∇u|² dx ds ≤ ∫|u_0|² dx.

### 2.2 존재 (Leray 1934, Hopf 1951 주기경계 확장)

모든 u_0 ∈ L²(ℝ³), ∇·u_0 = 0 에 대해 [0, ∞) 에 Leray 약해가 **최소 하나** 존재.

증명 요점: Galerkin 근사 (Fourier 기저) + compactness + weak lower semi-continuity.

### 2.3 약해의 유일성 [미증명]

3D 에서 Leray 약해의 유일성은 미해결. 2D 에서는 증명됨 (Ladyzhenskaya 1959).
Clay 명제는 유일 정칙 해 의 존재 (또는 반례) 를 요구.

### 2.4 Scheffer-Serrin 부분 유일성

Leray 약해가 "suitable weak solution" (Caffarelli-Kohn-Nirenberg 의미) 이고 추가 조건
u ∈ L^{p,q}, 2/p + 3/q = 1 을 만족하면 같은 초기값 다른 약해와 일치. 이 "Ladyzhenskaya-
Prodi-Serrin 조건" 은 정칙성 기준과 직접 연결.

---

## 3. 정칙성 기준 (Regularity criteria)

### 3.1 Ladyzhenskaya-Prodi-Serrin 조건

u ∈ L^q_t L^p_x, 3/p + 2/q = 1, p ∈ (3, ∞]. 이 조건을 만족하면 [0,T] 에서 정칙.

### 3.2 L^∞_t L^{3,∞}_x (ESS 2003)

Escauriaza-Seregin-Šverák: u ∈ L^∞((0,T); L^{3,∞}_x) ⟹ [0,T] 에서 정칙. L^{3,∞} 는
Lorentz 공간 (약 L³). 이는 scale-critical 경계 처음 넘음.

증명 아이디어: backward uniqueness + unique continuation + 블로업 존재 시 선형화된 연구.

### 3.3 vorticity 기준 (Beale-Kato-Majda 1984)

ω = ∇ × u. ∫₀^T ||ω(t)||_{L^∞} dt < ∞ 이면 [0,T] 에서 정칙. 이는 vorticity 가 blow-up
을 주도함을 보여줌.

### 3.4 기타 기준

- Constantin-Fefferman 1993: vorticity 방향 Lipschitz 조건
- Chae-Choe 2001: 2 component of ω 만 제어해도 충분
- Nečas-Růžička-Šverák 1996: 자기유사 blow-up 불가

---

## 4. Blow-up 시나리오 분류

### 4.1 scale-invariant 양

blow-up 이 일어난다면 임계 스케일 불변량 중 하나가 발산해야. 즉
- ||u(t)||_{L³} → ∞
- ||∇u(t)||_{L²_t L²_x} → ∞
- ||ω(t)||_{L^∞_t L^∞_x} → ∞

등. ESS 2003 로 L^{3,∞} 가 유한 유지되면 blow-up 없음.

### 4.2 Type I blow-up

```
  ||u(t)||_{L^∞_x} ≤ C / √(T* - t)
```

자기유사 속도로 blow-up. Nečas-Růžička-Šverák 1996: 자기유사 blow-up 존재 불가
(가정 자기유사: u(x,t) = (T*-t)^{-1/2} U(x/√(T*-t))).

### 4.3 Type II blow-up

Type I 보다 빠른 blow-up. 현재 3D NS 에서 type II 가 존재하는지 미결.

### 4.4 핵심 미해결 [미증명]

임의의 매끄러운 초기값에서 해가 매끄럽게 지속되는가? 아니면 어떤 초기값에서 유한시간
blow-up 이 일어나는가? 수치 시뮬레이션은 양쪽 모두 가능한 증거를 제시하지만, 엄밀
증명 부재.

---

## 5. Caffarelli-Kohn-Nirenberg 부분 정칙성

### 5.1 CKN 1982 정리

"suitable weak solution" u (Leray 약해 + 추가 에너지 조건) 의 특이집합 S ⊂ ℝ³ × (0,∞)
는 1차원 Hausdorff 측도 𝒫¹ 로 null. 즉 특이점의 "파라볼릭 시공간 1-차원" 이하로만
존재 가능.

### 5.2 ε-regularity 기법

parabolic cylinder Q_r(x,t) = B_r(x) × (t-r², t). 적당한 작음 조건

```
  (1/r) ∫∫_{Q_r} |∇u|² dx ds < ε_0
```

을 만족하면 (x,t) 는 정칙점. CKN 의 epsilon 은 구체적 ε_0 값을 명시.

### 5.3 CKN 의 의미

3D NS 의 blow-up 이 존재해도 "매우 얇은" 특이집합 위에서만 가능. 시간축 전체에 걸친
blow-up 은 배제됨.

---

## 6. Tao 의 접근 (2014~2016)

### 6.1 Averaged NS

Tao 2014 "Averaged Navier-Stokes equations ... blow-up" 에서 표준 NS 와 같은 에너지
구조·scaling 을 갖는 변형된 (Averaged) 방정식을 구성, 유한시간 blow-up 증명. 이는
순수 NS 의 blow-up 이 존재할 가능성을 시사하지만, 직접 증명은 아님.

### 6.2 무한 에너지 구조

Tao 는 NS 의 blow-up 이 "에너지 cascade" 로 설명될 수 있음을 제안. 작은 scale 로 에너지가
전달되는 과정을 정밀 분석해야 함.

### 6.3 Scale-critical 장벽

임계 스케일 L³ 제어는 ESS 로 도달. 그 다음 장벽: Critical 노름의 "아주 작은 초과"
조건. Tao-Hou 등의 시도 진행 중 (2020~).

---

## 7. 2D NS — 참고용 정리

비교용으로 2D NS 는 완전히 해결됨.

- 임의의 u_0 ∈ L² 에서 유일 매끄러운 해 [0, ∞) 존재
- 에너지 등식 (부등호가 아닌 등호) 성립
- vorticity 방정식 ∂_t ω + u·∇ω = νΔω 가 최대원리를 허용

3D 와 핵심 차이: 2D 에서 vorticity stretching 항 ω·∇u 가 없음. 이 항이 3D blow-up 가능성을
만든다.

---

## 8. n=6 연결 (메모만)

1. 3D 공간 차원 자체가 n=6 과 배수 관계지만, NS 방정식의 blow-up 여부는 공간 차원 3 의
   산술적 성질보다 geometry of vortex stretching 이 핵심. n=6 과 직접 수학적 경로 없음
   ([N?]).
2. Kolmogorov 난류 스펙트럼 E(k) ~ k^{-5/3} 에서 지수 5/3 ≈ 1.667 과 φ(6)/σ(6) = 2/12 =
   1/6 = 0.167 등 저차 분수 사이 숫자 일치는 없다 ([N?]).
3. Richardson 4/3 법칙 (pair dispersion) 의 4/3 는 τ(6)/σ(6) × 4 = 4·4/12 = 4/3 과
   수치 일치하나, 이는 계량적 coincidence 수준 ([N?]).

자기참조 검증 금지 원칙: 위 3가지 관찰은 모두 BT-544 증명 경로와 무관하게 유지한다.

---

## 9. 실전 과제 — 손으로 풀 5제

**P1.** 3D NS 스케일 대칭성 u_λ(x,t) = λ u(λx, λ²t) 를 방정식에 대입해 확인하라. 다음으로
L³_x, L^{3,∞}_x 가 scale-invariant, L²_x 는 아님을 보여라.

**P2.** 2D NS 에서 vorticity 방정식 ∂_t ω + u·∇ω = ν Δω 을 유도하고, 최대원리
||ω(t)||_{L^∞} ≤ ||ω_0||_{L^∞} 를 증명하라.

**P3.** Beale-Kato-Majda 1984 판정의 뼈대를 재구성하라. 즉 |u|_{H^s} 의 미분방정식을
Biot-Savart 공식으로 유도 후, ∫ ||ω||_{L^∞} dt 에 의한 제어.

**P4.** Leray 약해 존재정리의 Galerkin 근사를 ℝ³ 의 Fourier 기저로 스케치하라. 에너지
부등식이 compactness 의 핵심임을 확인.

**P5.** Nečas-Růžička-Šverák 1996 의 자기유사 blow-up 불가 논거를 3단계로 재구성:
(i) 자기유사 가정 → Leray 방정식 재작성, (ii) 무한원점 에너지 조건, (iii) Lioville형
정리 적용.

---

## 10. 읽기 경로

### 10.1 1주차

- Fefferman Clay 공식 문서 8쪽 정독
- Leray 1934 원논문 §1~§3
- Temam §III 약해 정의

### 10.2 2주차

- Constantin-Foias 전체 (간결)
- Tao "Nonlinear Dispersive" §3 NS 부분
- Ladyzhenskaya "The Mathematical Theory of Viscous Incompressible Flow" 2판 1969

### 10.3 3주차

- Caffarelli-Kohn-Nirenberg 1982 원논문 (Comm. Pure Appl. Math. 35:771)
- Escauriaza-Seregin-Šverák 2003 원논문
- Nečas-Růžička-Šverák 1996

### 10.4 4주차

- Tao "Finite-time blowup for an averaged three-dimensional Navier-Stokes equation"
  J. AMS 2016
- Robinson-Rodrigo-Sadowski "The Three-Dimensional Navier-Stokes Equations" Cambridge 2016
- 최근 review: Buckmaster-Vicol 2019 "Convex integration and phenomenologies ..."

---

## 11. 출처 정리

- Fefferman "Existence and smoothness of the Navier-Stokes equation" Clay 2000 — 공식 명제
- Leray "Sur le mouvement d'un liquide visqueux..." Acta Math. 63, 1934 — 약해 창시
- Hopf "Über die Anfangswertaufgabe..." Math. Nachr. 4, 1951 — 주기경계 확장
- Temam "Navier-Stokes Equations: Theory and Numerical Analysis" North-Holland 1984
- Constantin-Foias "Navier-Stokes Equations" U. Chicago Press 1988
- Caffarelli-Kohn-Nirenberg "Partial regularity of suitable weak solutions..." CPAM 35:771, 1982
- Escauriaza-Seregin-Šverák "L^{3,∞}-solutions of NS and backward uniqueness"
  Russian Math. Surveys 58:211, 2003
- Tao "Finite-time blowup for an averaged three-dimensional Navier-Stokes equation"
  J. AMS 29:601, 2016
- Buckmaster-Vicol "Convex integration and phenomenologies in turbulence"
  EMS Surv. Math. Sci. 6:173, 2019
- Beale-Kato-Majda "Remarks on the breakdown of smooth solutions..." CMP 94:61, 1984

본 노트는 위 10개 원전의 P1 학습 분량 재정리이며, 신규 정리 제시는 없다.

---

## 12. 다음 문서

- PROB-P1-5 : BT-545 Hodge 심화
- PROB-P1-6 : BT-546 BSD 심화
- PROB-P1-7 : BT-547 푸앵카레 심화
- N6-P1-3 : n=6 정직성 원칙

BT-544 는 P2~P3 단계에서 Tao-Fefferman 형 정밀 분석과 수치 실험 결과 지도를 추가한다.
본 P1 노트는 "Clay 명제의 정밀 분해 + 기존 장벽 지도" 를 목적으로 한다.
