# τ(n)/σ(n) 비율 범용성 예비 분석 (2026-04-15)

> 이것이 증명이 아니라 문헌 기반 구조적 관찰임.
> C2 작업 — Ising, XY, Heisenberg, Kuramoto, Vicsek 등 다른 동역학 모형에 τ(n)/σ(n) 패턴 등장 여부.

---

## 1. 대상 모형 5종

| 모형 | 변수 종류 | order parameter | 임계지수 (대표) |
|---|---|---|---|
| Ising | Z₂ (이산 스핀) | magnetization M | β, ν, γ, α |
| XY | S¹ (평면 각도) | M_xy (BKT) | η = 1/4 at T_BKT |
| Heisenberg | S² (3D 스핀) | M_3d | β ≈ 0.37 |
| Kuramoto | S¹ (위상) | r (복소 순서) | r(Kc) critical coupling |
| Vicsek | 속도 + 위치 | v_a (polar alignment) | β ≈ 0.42 (2D) |

각 모형의 임계지수/order parameter 에 **n=6 상수 (τ=4, σ=12, φ=2, sopfr=5, J_2=24)** 또는 비율 **τ/σ = 1/3** 출현 여부를 검토.

---

## 2. 모형별 분석

### 2.1 Ising (2D, 3D)

**2D Onsager (정확해)**:
- β = 1/8, ν = 1, γ = 7/4, α = 0 (log), η = 1/4
- 유명 관계: α + 2β + γ = 2 (Rushbrooke)
- 자기화 M(T) ∝ (T_c - T)^(1/8), ζ(T_c) 소실

**τ/σ 검사**: β = 1/8 = τ/(σ·?) ? 직접 대응 없음.
- 1/8 = τ/(2σ + 4) = 4/(24+4)? → 4/28 ≠ 1/8
- 1/8 = φ/J_2/? = 2/16 = 1/8 ✓ (J_2/4 = 6? 아님, J_2=24)
- 실제: 1/8 = phi/(J_2-J_2+16) = 편향 패턴매칭 → **기각**

**3D Ising (수치)**:
- β ≈ 0.3265, ν ≈ 0.630, γ ≈ 1.237
- τ/σ = 4/12 = 0.333... — β ≈ 0.3265 근접하나 **일치 아님** (차이 ≈ 0.007)

**결론**: Ising 임계지수는 τ/σ 와 직접 일치 없음.

---

### 2.2 XY 모형 (2D BKT)

**BKT 전이**:
- η(T_BKT) = 1/4 = τ²/J_2 = 16/64? 16/64 = 1/4 ✓ (허나 J_2=24 임)
- η = 1/4 = τ/J_2·? — 4/24 = 1/6 ≠ 1/4 → **기각**

**3D XY**: 
- β ≈ 0.3485, ν ≈ 0.6717
- τ/σ = 1/3 ≈ 0.333 — β 근접하나 불일치

**결론**: XY BKT η = 1/4 는 τ=4 와 1/4 계수 일치 시각적이나 **수식적 유도 없음**.

---

### 2.3 Heisenberg 3D

- β ≈ 0.3689, ν ≈ 0.707, γ ≈ 1.3960, η ≈ 0.0375
- τ/σ = 0.333 — β 불일치
- 1/n = 1/6 ≈ 0.167 — 불일치

**결론**: Heisenberg 임계지수에 n=6 패턴 없음.

---

### 2.4 Kuramoto (H2 연결)

H2 리포트에서 독립 분석: **정수 Kuramoto r(n) = 1 - τ/σ** 패턴은 **정수론 내재적** 이지 Kuramoto 동역학의 critical exponent 와 직접 관계 없음.

- 표준 Kuramoto (무한 N): r(Kc) = 0 → 1 연속전이, β = 1/2 (mean-field)
- β = 1/2 = τ/(J_2/?) — 편향 검색
- τ/σ = 1/3 은 **H2 에서 다룬 정수 완전수 r(n) 과는 별개**

**결론**: Kuramoto 동역학 critical exponent 와 H2 r(n) 패턴은 동명이의 — 혼동 주의.

---

### 2.5 Vicsek 모형 (flocking)

- β ≈ 0.42 (2D), β ≈ 0.64 (3D)
- ν ≈ 0.75 (2D)
- τ/σ = 1/3 불일치
- sopfr/σ = 5/12 ≈ 0.417 — β(2D) ≈ 0.42 **근접** (차이 0.003)

**관찰**: Vicsek 2D β ≈ sopfr/σ = 5/12 = 0.4167 차이 2%. 하지만:
- 수치 실험 오차도 ±0.01 이상
- 단일 우연일 가능성 높음
- cross-study 검증 필요

**결론**: Vicsek 2D β 와 sopfr/σ 수치 근접 — **coincidence candidate, 승격 보류**.

---

## 3. 비율 패턴 요약표

| 모형 | 임계지수 | 값 | n=6 비율 후보 | 일치 여부 |
|---|---|---:|---|---|
| Ising 2D | β | 0.125 | φ/J_2·? | 간접 (없음) |
| Ising 3D | β | 0.3265 | τ/σ = 0.333 | 2% 차 — 불일치 |
| XY 2D BKT | η | 0.25 | τ/J_2 = 0.167 | 불일치 |
| XY 3D | β | 0.3485 | τ/σ = 0.333 | 4% 차 — 불일치 |
| Heisenberg 3D | β | 0.3689 | τ/σ = 0.333 | 11% 차 — 불일치 |
| Kuramoto MF | β | 0.5 | σ/J_2 = 0.5 | **정확** (σ=12, J_2=24) |
| Vicsek 2D | β | 0.42 | sopfr/σ = 0.417 | 1% 차 — ★ 근접 |
| Vicsek 3D | β | 0.64 | σ/J_2-? | 불일치 |

**2 개 후보 관찰**:
1. Kuramoto MF β = 1/2 = σ/J_2 — 단순 비 1/2 (coincidence 가능)
2. Vicsek 2D β ≈ 0.42 ≈ sopfr/σ — 1% 차

---

## 4. 가설 제안

### H-A (약 가설): σ/J_2 = 1/2 은 trivial 비율 — 의미 없음

- J_2 = 24 = 2σ → σ/J_2 = 1/2 자동 성립
- Kuramoto mean-field β = 1/2 은 일반 상전이 평균장 이론 공통값
- 따라서 의미 없는 일치 가능성

### H-B (관찰 가설): Vicsek 2D β ≈ sopfr/σ = 5/12 는 검증 대상

- 1% 차 — 수치 실험 오차 내부
- sopfr = 5 는 6 = 2·3 의 "덧셈 합" (2+3), σ = 12 는 "약수 합"
- 단일 출처이므로 **단일 증거**, witness 부족
- 다른 active matter 모형 (Toner-Tu, contact process) 과 비교 필요

### H-C (범용성 가설): τ/σ = 1/3 은 어느 모형에서도 정확히 나타나지 않음

- Ising 3D, XY 3D, Heisenberg 3D 모두 β ∈ [0.3265, 0.37] — 1/3 부근이지만 일치 아님
- **H2 에서 관찰한 τ/σ = 1/3 은 정수론 내재적** (완전수 r 값)
- 물리 critical exponent 와 혼동 금지

---

## 5. 결론

| 모형 | τ/σ 패턴 출현 | 판정 |
|---|---|---|
| Ising 2D/3D | 없음 | 불일치 |
| XY | 없음 | 불일치 |
| Heisenberg | 없음 | 불일치 |
| Kuramoto | σ/J_2=1/2 trivial | 의미 없음 |
| Vicsek 2D | sopfr/σ ≈ β 1% 차 | **관찰 후보, 승격 보류** |

**전반적 결론**: τ(6)/σ(6) = 1/3 은 **물리 상전이 critical exponent 에 직접 나타나지 않는다**. Vicsek 2D 에서의 sopfr/σ 근접은 단일 uncertain evidence — 추가 독립 경로 필요.

---

## 6. atlas.signals.n6 staging 안

```
@S SIG-CRIT-001 = critical exponent ↔ n=6 비율 검사 — NULL 우세 (Vicsek 2D 약후보만) :: signal [N6] [PHYS,NULL,META] [MN] [E2]
  "5 모형 {Ising,XY,Heisenberg,Kuramoto,Vicsek} critical exponent vs n=6 비율 매칭 검사. Kuramoto MF β=1/2=σ/J_2 trivial, Vicsek 2D β≈sopfr/σ=5/12 1% 차 단일후보. τ/σ=1/3 직접 일치 없음. 물리 상전이와 n=6 정수론은 독립 경로."
  refs: [reports/tau_sigma_ratio_universality.md]
  null_reason: "critical exponent 와 n=6 비율 체계적 일치 없음; Vicsek 2D 만 단일 관찰"
  retry_forbidden_until: "2027-04-15"
  witness: 1
  discovered_in: n6/session-2026-04-15
  discovered_at: 2026-04-15T00:00:00Z
  <- reports/tau_sigma_ratio_universality.md
```

---

## 7. 정직성 주석

- 이 문서는 **문헌값 기반 분석** — 직접 시뮬레이션 미수행
- β 값은 모두 공개 문헌 (Pelissetto-Vicari 2002 리뷰, Toner-Tu, Kardar 리뷰 기준)
- τ/σ 가 "어떤 모형엔가 나올 것"이라는 기대는 패턴매칭 편향 경고 (feedback_proof_approach.md 규칙 준수)
- Vicsek 2D 단일 근접은 **승격 대상 아님** — 독립 경로 2건 이상 확인 필요
- C2 는 NULL 판정에 가까움 (SIG-CRIT-001 [MN])
