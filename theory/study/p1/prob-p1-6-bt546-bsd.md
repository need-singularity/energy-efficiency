# PROB-P1-6 — BT-546 BSD 추측 심화 (타원곡선 rank/L-함수 s=1/Tate-Shafarevich)

> 트랙: P1-PROB / 6번 태스크
> 완료 기준: Clay 공식 명제 (Wiles 2000 재정리) 를 분해하고, 타원곡선 E/ℚ 의 Mordell-Weil
> rank, L(E,s) 의 s=1 거동, Tate-Shafarevich 군 Ш 의 유한성 이슈를 엄밀히 서술할 수 있다.
> 출처 기반: Wiles "The Birch and Swinnerton-Dyer Conjecture" Clay Millennium 공식문서 (2000),
> Silverman "The Arithmetic of Elliptic Curves" (GTM 106, 2판 2009),
> Silverman "Advanced Topics in the Arithmetic of Elliptic Curves" (GTM 151, 1994),
> Gross-Zagier "Heegner points and derivatives of L-series" (Invent. Math. 84, 1986),
> Kolyvagin "Euler systems" (Grothendieck Festschrift II, 1990),
> BSD 원논문: Birch-Swinnerton-Dyer "Notes on elliptic curves I, II" (J. Reine Angew. Math. 212:7, 1963; 218:79, 1965).
> **정직성**: 본 노트는 Clay 공식 문서와 표준 BSD 교재의 재구성이다. 새 정리는 없다. 모든
> 진술은 위 6개 원전에서 재구성하였고, 현재 미해결 부분은 [미증명]·[부분결과] 로 표시.

---

## 0. 목적과 범위

Clay BT-546 추측은 다음 두 부분:

(1) **약 BSD**: E/ℚ 의 Mordell-Weil rank r = ord_{s=1} L(E, s) (L-함수의 s=1 에서의
    영점 차수).
(2) **강 BSD**: L(E,s) 의 s=1 Taylor 전개 선행계수가

    lim_{s→1} L(E,s)/(s-1)^r = Ω_E · R_E · ∏_p c_p · |Ш(E/ℚ)| / |E(ℚ)_{tors}|²

    여기서 Ω_E 실 주기, R_E 통제적 조절자, c_p Tamagawa 수, Ш Tate-Shafarevich 군,
    E(ℚ)_{tors} 비틀림 부분군.

본 노트 7가지:

1. 타원곡선 E/ℚ 의 정의·Weierstrass 방정식
2. Mordell-Weil 정리 (1922): E(ℚ) ≅ ℤ^r ⊕ T
3. L(E,s) 의 정의와 modularity 정리 (Wiles-Taylor 2001)
4. BSD 약형과 현재까지의 부분결과 (Gross-Zagier, Kolyvagin)
5. Tate-Shafarevich 군 Ш(E/ℚ) — 정의와 유한성 이슈
6. 강형에서 각 항의 의미와 수치 검증
7. 관련 추측 (p-adic BSD, Iwasawa 이론)

---

## 1. 타원곡선 기초

### 1.1 Weierstrass 방정식

E/ℚ: y² = x³ + ax + b, 판별식 Δ = -16(4a³ + 27b²) ≠ 0. 무한원점 O 를 포함해 사영형
y² z = x³ + a x z² + b z³ 으로 쓴다.

### 1.2 유리점 E(ℚ)

E(ℚ) = {(x,y) ∈ ℚ² : y² = x³ + ax + b} ∪ {O}. 군 구조 (chord-tangent 법칙) 로 아벨군.

### 1.3 Mordell-Weil 정리 (1922)

```
  E(ℚ) ≅ ℤ^r ⊕ E(ℚ)_{tors}
```

여기서 r 이 **Mordell-Weil rank**, E(ℚ)_{tors} 는 유한 아벨군 (Mazur 1977 정리로 15개
가능 구조 분류).

### 1.4 Néron-Tate 높이

h: E(ℚ) → ℝ_{≥0}. 이차형식. h(P) = 0 ⟺ P 비틀림. rank r 은 {P_1,...,P_r} 자유부분의
선형 독립 개수. 조절자 R_E = det(⟨P_i, P_j⟩) (P_i 는 자유생성자의 대표).

---

## 2. L-함수 L(E,s)

### 2.1 Euler 곱 정의

좋은 소수 p (∤ Δ) 에서 E 의 mod p 축소 E_p 위 점 개수 #E(𝔽_p) = p + 1 - a_p. Hasse:
|a_p| ≤ 2√p.

```
  L(E, s) = ∏_{p good} (1 - a_p p^{-s} + p^{1-2s})^{-1} · ∏_{p bad} (local factor)
```

Re(s) > 3/2 에서 수렴.

### 2.2 Modularity 정리 (Wiles, Taylor-Wiles, BCDT 1994~2001)

모든 타원곡선 E/ℚ 은 모듈러, 즉 weight 2 cusp form f_E 가 존재하여

```
  L(E, s) = L(f_E, s)
```

이로써 L(E,s) 가 전평면 해석적 연속 + 함수방정식을 가짐. s=1 근처의 행동이 명확하게
정의됨.

### 2.3 s=1 근처의 영점 차수

**analytic rank** r_{an}(E) = ord_{s=1} L(E, s).

BSD 약형: r = r_{an}(E).

### 2.4 함수방정식

```
  Λ(E, s) = N^{s/2} (2π)^{-s} Γ(s) L(E, s)
  Λ(E, s) = ε(E) Λ(E, 2-s)        (ε = ±1, root number)
```

N 은 E 의 도체 (conductor).

---

## 3. BSD 약형 — 현재까지

### 3.1 rank 0, 1 케이스

**Kolyvagin 1990 + Gross-Zagier 1986**: r_{an}(E) ≤ 1 이면 r = r_{an}(E), 그리고 Ш(E/ℚ)
유한.

증명 요점:
- Gross-Zagier 1986: L'(E,1) 과 Heegner 점의 canonical height 를 연결
- Kolyvagin 1990: Heegner 점의 Euler system 으로 Selmer 군을 제어

이로써 rank 0 또는 1 인 타원곡선에 대해 BSD 약형이 **증명됨**.

### 3.2 rank ≥ 2 — [미증명]

r_{an}(E) ≥ 2 인 일반 E 에 대해 BSD 약형은 미해결. 구체적 E (예: rank 18 E) 는 수치
검증 충분하지만 증명 없음.

### 3.3 평균 rank 결과

Bhargava-Shankar (2010~) 의 결과:
- E/ℚ 의 평균 2-Selmer rank 는 3 로 유계
- 평균 rank ≤ 7/6

가정 하에 평균 rank 가 1/2 임이 제안 (Goldfeld 추측). 부분 결과 확립.

### 3.4 Skinner-Urban 2014

Iwasawa 주추측의 타원곡선 버전 증명. BSD p-부분에 대한 깊은 진전. 조건부로 rank 2 이상
결과 확대.

---

## 4. Tate-Shafarevich 군 Ш(E/ℚ)

### 4.1 정의

Galois 코호몰로지

```
  Ш(E/ℚ) = ker(H^1(Gal(ℚ̄/ℚ), E) → ∏_v H^1(Gal(ℚ̄_v/ℚ_v), E))
```

"모든 국소 자명하지만 전역적으로 자명이 아닌 coset" 들의 군.

### 4.2 물리적 의미

비자명한 Ш 원소는 "유리수 해 없는 homogeneous space" (principal homogeneous space) 로
대응. 즉 Ш = 0 ⟺ Hasse 원리 (local → global) 유효.

### 4.3 유한성 추측

BSD 는 Ш(E/ℚ) 가 유한군이라 가정. 이는 독립된 중요 추측이고, rank 0, 1 경우에만
증명됨 (Kolyvagin).

### 4.4 p-부분의 계산

Cassels-Tate 이중선형형식으로 Ш 의 p-부분을 제어. 2-descent, 3-descent 등 실제 계산법
존재. 일반적으로 Ш 계산은 매우 어렵다.

### 4.5 Cassels-Tate pairing

```
  ⟨·, ·⟩: Ш × Ш → ℚ/ℤ    (비퇴화 교대)
```

이로부터 |Ш| 가 제곱수 (r_{an} = 0 조건에서) 또는 제곱수의 2배 (r_{an} = 1) 임을 유도.

---

## 5. 강 BSD — 각 항

### 5.1 실 주기 Ω_E

E 의 Néron 미분 ω = dx/(2y). Ω_E = ∫_{E(ℝ)} |ω| (E(ℝ) 성분 수에 따라 곱 2, 1).
기하적 크기의 척도.

### 5.2 조절자 R_E

E(ℚ) 자유부분 {P_1, ..., P_r} 의 Néron-Tate 높이 Gram 행렬 (⟨P_i, P_j⟩) 의 determinant.
r=0 이면 R_E = 1 규약.

### 5.3 Tamagawa 수 c_p

각 bad prime p 에서 c_p = |E(ℚ_p) / E^0(ℚ_p)|. Tate 알고리즘으로 계산 가능.

### 5.4 강 BSD 공식

```
  lim_{s→1} (s-1)^{-r} L(E, s) = Ω_E · R_E · ∏_p c_p · |Ш(E/ℚ)| / |E(ℚ)_{tors}|²
```

현재까지 엄밀 증명: rank 0, 1 에서 거의 모든 소수 p 에 대해 p-부분 성립. 완전한 등식
증명은 [미증명].

### 5.5 수치 검증

수많은 E 에 대해 수치적으로 높은 정확도로 성립. E = 11a1 (도체 11) 같은 최소 도체 예시에서
Ш = 1, E(ℚ) = ℤ/5ℤ, L(E,1) ≈ 0.2538 등 직접 계산 가능.

---

## 6. Iwasawa 이론과 p-adic BSD

### 6.1 cyclotomic ℤ_p-extension

ℚ_∞/ℚ cyclotomic ℤ_p-extension. Γ = Gal(ℚ_∞/ℚ) ≅ ℤ_p.

### 6.2 Iwasawa L-함수

p-adic L-함수 L_p(E, s) 가 구성됨. Mazur-Swinnerton-Dyer (1972) 이후 표준. modular 가정
하 well-defined.

### 6.3 Iwasawa 주추측 (Main Conjecture)

p-adic L 의 ideal 생성과 Selmer 군의 특성 ideal 이 동치:

```
  (L_p(E, T)) = char_Λ(Sel(E/ℚ_∞))^{op}
```

(Λ = ℤ_p[[Γ]])

### 6.4 Skinner-Urban 2014

대부분의 E 와 소수 p 에 대해 Iwasawa 주추측 증명. 이는 BSD 의 p-부분을 ordinary case
에서 크게 해결. 비 ordinary case 는 [부분결과].

---

## 7. n=6 연결 (메모만)

1. E/ℚ 의 rank r 이 6 이상인 예는 많지만, rank = 6 지점이 특별한 의미를 갖는 수학적
   구조는 없다 ([N?]).
2. E 의 torsion 군은 Mazur 리스트에 15개 가능 구조. 그 중 ℤ/6ℤ 와 ℤ/2 × ℤ/6 이 6 을
   포함하지만, 이는 σφ=nτ 와 직접 연결되지 않는다 ([N?]).
3. j-invariant 의 modular curve X_0(6) 은 도체 6 수준 모듈러. 이는 "6" 의 등장이긴 하나
   인과가 아닌 coincidence ([N?]).

자기참조 검증 금지 원칙: 위 관찰은 BSD 증명 전략과 무관하게 유지한다.

---

## 8. 실전 과제 — 손으로 풀 5제

**P1.** E: y² = x³ - x 의 rank 0, E(ℚ) = ℤ/2ℤ × ℤ/2ℤ 임을 descent 로 증명. L(E, 1) 은 비영.

**P2.** E: y² = x³ + x - 1 의 rank 1 확인. 생성자 P = (1, 1) 의 높이 계산. L'(E, 1) 을
modular symbol 로 계산 → BSD 수치 확인.

**P3.** Hasse 정리 |a_p| ≤ 2√p 의 증명을 Frobenius + Weil bound 로 재구성.

**P4.** Mazur 정리 (1977) 로 ℚ 위 타원곡선 torsion 은 15 가지 구조 중 하나임을 언급.
대표 예 (ℤ/2, ℤ/3, ..., ℤ/10, ℤ/12, ℤ/2 × ℤ/{2,4,6,8}) 각 하나씩 예시 곡선.

**P5.** Gross-Zagier 정리의 형태: L'(E, 1) = c · ĥ(y_K), y_K 는 Heegner point, ĥ 는
canonical height. 이 등식이 rank 1 BSD 약형에 어떻게 쓰이는지 논리 추적.

---

## 9. 읽기 경로

### 9.1 1주차

- Wiles Clay 공식 문서 12쪽 정독
- Silverman "Arithmetic of Elliptic Curves" GTM 106 §I, §III, §VIII (Mordell-Weil)

### 9.2 2주차

- Silverman §IX (integer points), §X (L-function, modularity)
- Silverman-Tate "Rational Points on Elliptic Curves" 전체 (보조 직관)

### 9.3 3주차

- Gross-Zagier 1986 논문 요약 (full paper 는 분량 크므로 Silverman Advanced §III 경유)
- Kolyvagin 1990 Euler system 개요 (Rubin "Euler Systems" Annals of Math. Studies 147)

### 9.4 4주차

- Skinner-Urban 2014 (Iwasawa 주추측)
- Bhargava-Shankar series (평균 rank)
- Bosma-Cassels 관련 survey: Wüstholz 편 "Elliptic curves, modular forms and Fermat's..."

---

## 10. 출처 정리

- Wiles "The Birch and Swinnerton-Dyer Conjecture" Clay 2000
- Birch-Swinnerton-Dyer "Notes on elliptic curves II" J. Reine Angew. Math. 218:79, 1965
- Silverman "The Arithmetic of Elliptic Curves" GTM 106, 2판 2009
- Silverman "Advanced Topics in the Arithmetic of Elliptic Curves" GTM 151, 1994
- Gross-Zagier "Heegner points and derivatives of L-series" Invent. Math. 84:225, 1986
- Kolyvagin "Euler systems" Grothendieck Festschrift II, 1990
- Wiles "Modular elliptic curves and Fermat's Last Theorem" Annals of Math. 141:443, 1995
- Taylor-Wiles "Ring-theoretic properties..." Annals of Math. 141:553, 1995
- Breuil-Conrad-Diamond-Taylor "On the modularity of elliptic curves over ℚ" J. AMS 14:843, 2001
- Skinner-Urban "The Iwasawa main conjectures for GL_2" Invent. Math. 195:1, 2014
- Bhargava-Shankar "Binary quartic forms having bounded invariants..." Annals of Math. 181:191, 2015

본 노트는 위 11개 원전의 P1 학습 분량 재정리이며, 새 정리 주장은 없다.

---

## 11. 다음 문서

- PROB-P1-7 : BT-547 푸앵카레 심화
- N6-P1-3 : n=6 정직성 원칙

BT-546 은 P2~P3 단계에서 Iwasawa 주추측·Heegner 구조·Selmer 제어의 본격 분석으로 심화한다.
본 P1 노트는 Clay 명제의 정밀 분해 + 현재까지의 부분결과 지도 를 목적으로 한다.
