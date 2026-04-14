# PROB-P1-5 — BT-545 Hodge 추측 심화 (대수적 순환/(p,p)-형식/Lefschetz 정리)

> 트랙: P1-PROB / 5번 태스크
> 완료 기준: Clay 공식 명제(Deligne 2000) 를 문장 단위로 분해하고, Hodge 분해 정리,
> (1,1)-Lefschetz 정리, Hodge 추측의 현재까지 증명·반례 구조를 설명할 수 있다.
> 출처 기반: Deligne "The Hodge Conjecture" Clay Millennium 공식문서 (2000),
> Griffiths-Harris "Principles of Algebraic Geometry" (Wiley, 1978) ch. 0, 1, 3,
> Voisin "Hodge Theory and Complex Algebraic Geometry" vol. I, II (Cambridge, 2002, 2003),
> Lewis "A Survey of the Hodge Conjecture" (CRM Monograph Ser. 10, 2판 1999),
> Atiyah-Hirzebruch "Analytic cycles on complex manifolds" (Topology 1, 1962),
> Voisin "A counterexample to the Hodge conjecture extended to Kähler varieties"
> (IMRN 2002).
> **정직성**: 본 노트는 Clay 공식 문서 + Hodge 이론 표준 교재의 재구성이다. 새 정리는 없다.
> 모든 진술은 위 6개 전거에서 재구성하였고, Clay 문제의 현재 상태 (일부 positive result,
> Kähler 경우 반례) 는 [부분결과]/[반례]/[미증명] 으로 표시한다.

---

## 0. 목적과 범위

Clay BT-545 는 다음을 묻는다: "X 가 매끄러운 복소 사영 다양체이면, 모든 Hodge 류
(Hodge class) 는 X 의 대수적 부분 다양체들의 유리 선형 결합으로 표현되는가?"

본 노트가 다루는 7가지:

1. 복소 사영 다양체 X 의 코호몰로지 H*(X; ℂ) 의 Hodge 분해
2. Hodge 류 Hdg^k(X) = H^{2k}(X; ℚ) ∩ H^{k,k}(X)
3. 대수적 순환 (algebraic cycle) 과 주기적 사상 (cycle class map)
4. (1,1)-Lefschetz 정리 (Lefschetz 1924 = Hodge 추측 k=1 증명)
5. 현재까지 해결 케이스: abelian 다양체, K3, ...
6. Kähler 다양체로 확장된 Hodge 추측의 Voisin 반례 (2002)
7. Atiyah-Hirzebruch 반례 (정수계수 Hodge 추측 반례, 1962)

---

## 1. 복소 사영 다양체와 de Rham 코호몰로지

### 1.1 복소 사영공간 ℙ^n_ℂ

ℙ^n_ℂ = (ℂ^{n+1} \ {0}) / ℂ*. 매끄러운 닫힌 복소 다양체, 차원 n. 복소 사영 다양체 X 는
ℙ^n 의 닫힌 복소 부분다양체.

### 1.2 de Rham 과 ∂̄-Dolbeault

X 가 복소다양체이면 매끄러운 p-형식 Ω^p 는 (p,q)-형식으로 분해: Ω^p = ⊕_{a+b=p} Ω^{a,b}.
미분 d = ∂ + ∂̄.

Dolbeault 코호몰로지:

```
  H^{p,q}_{∂̄}(X) = ker(∂̄: Ω^{p,q} → Ω^{p,q+1}) / im(∂̄: Ω^{p,q-1} → Ω^{p,q})
```

### 1.3 Hodge 분해 (매끄러운 컴팩트 Kähler X)

X 가 매끄러운 컴팩트 Kähler 다양체이면

```
  H^k(X; ℂ) = ⊕_{p+q=k} H^{p,q}(X),     H^{q,p} = \overline{H^{p,q}}
```

이 분해는 Kähler 계량에 의존하지 않고 X 의 복소구조만에 의존.

매끄러운 복소 사영 다양체는 자동으로 Kähler 이므로 Hodge 분해 성립 (Fubini-Study 계량).

### 1.4 Hodge 수 h^{p,q}

h^{p,q} = dim H^{p,q}(X). 대표:
- h^{0,0} = 1 (연결이면)
- h^{1,0} = q(X) (규칙수, irregularity)
- h^{2,0} = p_g(X) (기하 genus)
- h^{n,n} = 1 (x가 n-차원이면)
- Hodge 마름모꼴 (Hodge diamond): h^{p,q} = h^{n-p, n-q} (Serre 쌍대)

---

## 2. Hodge 류와 대수적 순환

### 2.1 Hodge 류 정의

```
  Hdg^k(X) = H^{2k}(X; ℚ) ∩ H^{k,k}(X)
```

즉 ℚ-유리 코호몰로지 류 중 (k,k) 순수 타입. de Rham 대표는 유리 계수 × (k,k)-형식.

### 2.2 대수적 순환

**대수적 k-순환**: X 의 공차원 k 부분다양체들의 ℤ-선형 결합 Z = Σ n_i Z_i, Z_i ⊂ X 가
기약 공차원 k 부분다양체.

### 2.3 주기적 사상 (cycle class map)

```
  cl: Z^k(X) → H^{2k}(X; ℤ)
```

Z ↦ Poincaré 쌍대 (fundamental class). 더 세밀하게 ℚ 계수로 확장:

```
  cl_ℚ: Z^k(X) ⊗ ℚ → Hdg^k(X) ⊂ H^{2k}(X; ℚ)
```

주기적 사상의 상 im(cl_ℚ) ⊆ Hdg^k 이 성립하지만, 등호 여부가 핵심.

### 2.4 Hodge 추측 진술

**Clay 공식 진술 (Deligne 2000 재정리):**

X 가 매끄러운 복소 사영 다양체이면, 모든 α ∈ Hdg^k(X) 에 대해 대수적 순환
Z ∈ Z^k(X) ⊗ ℚ 가 존재해 cl_ℚ(Z) = α.

즉 cl_ℚ: Z^k(X) ⊗ ℚ → Hdg^k(X) 가 **전사**(surjective).

---

## 3. (1,1)-Lefschetz 정리

### 3.1 정리 (Lefschetz 1924)

Hodge 추측은 k=1 경우 완전히 참. 즉 모든 α ∈ Hdg^1(X) = H²(X; ℚ) ∩ H^{1,1}(X) 은
divisor 유리선형결합으로 표현.

### 3.2 증명 개요

exponential sheaf 완전열

```
  0 → ℤ → 𝒪_X → 𝒪_X^* → 0
```

에서 긴 완전열

```
  H^1(X; 𝒪_X^*) → H²(X; ℤ) → H²(X; 𝒪_X)
```

H¹(X; 𝒪_X^*) = Pic(X), H²(X; 𝒪_X) ≅ H^{0,2}(X). 따라서 α ∈ H²(X;ℤ) 가 H^{0,2} 에
0 으로 사상되면 α ∈ im Pic(X). Pic(X) 의 원소는 line bundle → divisor 로 실현 가능.
또한 c_1(L) ∈ H^{1,1} 이 성립.

Hodge 분해로 H²(X;ℚ) ∩ H^{1,1} 의 원소는 H^{0,2} 와 H^{2,0} 양쪽에 영 사상. ∴ 대수적.

(출처: Griffiths-Harris §1.1, Voisin vol.I §7.2)

### 3.3 k≥2 경우의 어려움

k≥2 에서 (k,k) 유형이 k! 이상의 (k,k) - wedge 구조로 확장되어, 단순히 L^k 에서 만들어진
것으로 Hodge 류를 모두 표현하지 못함. Hard Lefschetz 정리가 제공하는 isomorphism 도
"대수적 순환 전체 전사" 를 주지 못한다.

---

## 4. 해결된 경우들

### 4.1 차원별 자명 케이스

- X 가 curve (dim 1): k=1, Lefschetz 로 해결
- X 가 surface (dim 2): k=1 만 비자명, 해결. k=0, k=2 는 자명
- X 가 threefold (dim 3): k=1, k=2 비자명. k=2 는 Poincaré 쌍대로 k=1 와 연결 → 해결

즉 **dim X ≤ 3** 에서 Hodge 추측은 완전히 해결됨.

### 4.2 Abelian 다양체 — 부분 해결

Abelian 다양체 A = ℂ^g / Λ. Mumford-Tate 군 기법으로:
- g ≤ 3: 완전 해결
- g=4: Murty 1984 해결
- 일반 g: [부분결과], Deligne 의 motivic 기법

(출처: Deligne "Hodge cycles on abelian varieties" LNM 900, 1982)

### 4.3 완전교차 (complete intersection)

X = V(F_1,...,F_r) ⊂ ℙ^n 대강 완전교차. k=1 은 자명, k≥2 는 구체적 조건 하 해결.

### 4.4 Fano variety

dim X = 3 이고 Fano (즉 -K_X 풍부) 인 경우, Hodge 추측이 유효함이 Clemens-Griffiths 1972
로 시사. 3차원 일반론에 흡수.

### 4.5 K3 곡면

dim 2 이므로 자명 해결. 고차원 hyperkähler 일반화는 [부분결과].

### 4.6 미해결 대표

- General hypersurface X ⊂ ℙ^n, dim X ≥ 4, k=2 이상
- Calabi-Yau 4-fold
- General abelian variety of high dimension with extra endomorphisms

---

## 5. Kähler 확장 — Voisin 반례 (2002)

### 5.1 Hodge 추측의 Kähler 확장

원 Hodge 추측은 사영 다양체에만 적용. Kähler 다양체로 확장은 다음을 주장:
"X 가 컴팩트 Kähler 다양체일 때, Hdg^k(X) 의 원소는 analytic 순환 (해석적 부분다양체)
으로 실현되는가?"

### 5.2 Voisin 반례 (2002)

Voisin 은 매끄러운 4차원 컴팩트 Kähler 다양체 X 를 구성해 Hdg² 에 **analytic 순환으로
실현 불가능한 원소** 가 존재함을 증명했다. 즉 Kähler 확장은 **거짓**.

구성: Weil-type abelian 4-fold 의 일반적 Kähler 변형. 자세한 구성은 IMRN 2002 참고.

이 결과는 원래 Clay 추측 (사영 전제) 이 Kähler 로 직접 확장되지 않음을 분명히 한다.

### 5.3 함의

Hodge 추측의 "사영성" 조건이 본질적. 대수적 순환의 존재는 사영 구조에 강하게 의존.

---

## 6. 정수계수 Hodge — Atiyah-Hirzebruch 반례 (1962)

### 6.1 Integral Hodge 추측

원래 추측은 ℚ 계수. "ℤ 계수 Hodge 추측" 은 cl_ℤ: Z^k(X) → Hdg^k_ℤ(X) = H^{2k}(X;ℤ) ∩
(filter on H^{k,k}) 전사 여부.

### 6.2 Atiyah-Hirzebruch 반례 (1962)

Atiyah-Hirzebruch 는 ℤ-계수 Hodge 가 **거짓** 임을 torsion 원소 반례로 제시. 구체: 특정
X 의 H^{2k}(X; ℤ)_{tors} ⊂ Hdg^k_ℤ 에 대수적으로 표현 불가능한 torsion 존재.

증명: K-이론과 Steenrod 연산 사용. 자세한 구성은 Topology 1:25, 1962.

### 6.3 ℚ 계수의 중요성

이 반례 이후 Hodge 추측은 ℚ 계수로만 제기됨. Clay 공식도 ℚ 계수. torsion 은 완전히 다른
문제.

---

## 7. 관련 이론 — motivic 관점

### 7.1 Grothendieck motives

대수적 순환의 mod-등가 equivalence 하에서 만드는 category ℳ_{rat}(X). 표준 추측과 Hodge
추측이 이 framework 에서 통일적으로 기술.

### 7.2 Standard conjectures (Grothendieck 1968)

5가지 표준 추측 — type A, B, C, D, Hodge 추측 버전. 모두 미해결이지만 Hodge 추측을
함의하는 구조. 상세는 Kleiman "Algebraic cycles and the Weil conjectures" 1968.

### 7.3 Absolute Hodge classes (Deligne)

Deligne 1982 는 motivic 관점에서 "absolute Hodge class" 라는 확장된 개념 도입. abelian
다양체에서 모든 Hodge 류가 absolute Hodge 임을 증명 (Deligne 정리). 완전한 Hodge 추측
은 아니지만 강한 부분 결과.

---

## 8. n=6 연결 (메모만)

1. 자명한 케이스의 상한 dim X ≤ 3 경계에서, 대수적 순환 차원 계수 (1,2,3) 의 합 6 이
   등장하는 숫자 일치는 있지만, Hodge 추측 해결 기법과 σφ=nτ 증명 사이 직접 수학적
   경로는 없다 ([N?]).
2. 4-dim Kähler 에서 Voisin 반례. 4 = 2·2, 6 = 2·3 비교 시 prime factor 구조 차이를 통해
   "무엇이 다른가" 관찰 가능하나 인과 없음 ([N?]).
3. Hodge 다이아몬드 대칭성 h^{p,q} = h^{q,p} = h^{n-p, n-q} 의 2중 대칭은 n=6 의 약수 이중화
   σ(6)=12 와 수치 일치하나 증명 경로와 독립 ([N?]).

자기참조 검증 금지 원칙: 위 관찰은 BT-545 해결 전략과 무관하게 유지한다.

---

## 9. 실전 과제 — 손으로 풀 5제

**P1.** ℙ^n 의 Hodge 수 h^{p,q} 계산. 결과: h^{p,p} = 1 (0 ≤ p ≤ n), 기타 모두 0. 직접
de Rham 코호몰로지에서 유도.

**P2.** 타원곡선 E 의 h^{0,0} = h^{1,1} = 1, h^{1,0} = h^{0,1} = 1 임을 확인. Hodge 다이아몬드
작성.

**P3.** (1,1)-Lefschetz 증명 재구성: 지수 sheaf sequence → 긴 완전열 → H^{1,1} ∩ H²(X;ℤ)
⊂ im(Pic(X) → H²(X;ℤ)).

**P4.** Abelian surface A = E × E (E 타원곡선) 에서 H²(A; ℚ) 의 Hodge 분해와 Hdg² 계산.
모든 Hdg² 이 대수적 순환인지 확인.

**P5.** Voisin 2002 반례의 핵심 구성요소를 개관. Weil-type abelian 4-fold 의 정의와
Hdg² 에 analytic 비표현성 발생 구조 정리.

---

## 10. 읽기 경로

### 10.1 1주차

- Deligne Clay 공식 문서 12쪽 정독
- Griffiths-Harris §0 복습 (복소다양체·Dolbeault)
- Voisin vol.I §1~§3 Hodge 분해 정리

### 10.2 2주차

- Voisin vol.I §7 Kähler 다양체·Hodge 분해
- Voisin vol.II §11 algebraic cycles, cycle class map
- Lewis "A Survey of the Hodge Conjecture" 전체

### 10.3 3주차

- Atiyah-Hirzebruch 1962 원논문
- Deligne "Hodge cycles on abelian varieties" LNM 900, 1982
- Voisin 2002 IMRN 원논문 반례

### 10.4 4주차

- Kleiman "Algebraic cycles and the Weil conjectures" 1968
- Jannsen "Motives, numerical equivalence..." 1992
- 최근 review: Voisin "Hodge loci and absolute Hodge classes" (Compositio 2007)

---

## 11. 출처 정리

- Deligne "The Hodge Conjecture" Clay 2000 — 공식 명제
- Lefschetz "L'Analysis Situs et la Géométrie Algébrique" Gauthier-Villars 1924 —
  (1,1)-Lefschetz 원논문
- Griffiths-Harris "Principles of Algebraic Geometry" Wiley 1978 — 표준 교재
- Voisin "Hodge Theory and Complex Algebraic Geometry" vol. I & II, Cambridge 2002/2003
- Lewis "A Survey of the Hodge Conjecture" CRM Monograph 2판 1999
- Atiyah-Hirzebruch "Analytic cycles on complex manifolds" Topology 1:25, 1962
- Voisin "A counterexample to the Hodge conjecture extended to Kähler varieties" IMRN 2002
- Deligne "Hodge cycles on abelian varieties" LNM 900, 1982
- Kleiman "Algebraic cycles and the Weil conjectures" Dix exposés sur la cohomologie
  des schémas, 1968

본 노트는 위 9개 원전의 P1 학습 분량 재정리이며, 새 결과를 주장하지 않는다.

---

## 12. 부록 — Hodge 구조 (Hodge structure) 정의

### 12.1 순수 Hodge 구조

ℤ-격자 V_ℤ 위에 V_ℂ = V_ℤ ⊗ ℂ 의 분해 V_ℂ = ⊕_{p+q=n} V^{p,q}, V^{q,p} = \overline{V^{p,q}}.
이것이 **무게 n 순수 Hodge 구조**.

### 12.2 혼합 Hodge 구조 (Deligne 1974)

무게 필터 W_• 와 Hodge 필터 F^• 의 두 층. Deligne "Théorie de Hodge" I, II, III.
일반(비콤팩트, 특이) 대수다양체에서도 코호몰로지가 혼합 Hodge 구조를 가진다.

### 12.3 period map

계의 유동 s 에 대한 V^{p,q}_s 의 변화 → period domain 에 대한 map. Griffiths transversality
조건 (1968) 은 이 맵의 기울기 제약.

---

## 13. 부록 — Mumford-Tate 군과 Hodge loci

### 13.1 Mumford-Tate 군

Hodge 구조에 연관된 algebraic group MT(V) ⊂ GL(V). Hodge 류를 보존하는 "자동사상" 군.

### 13.2 Hodge loci

family of varieties X → S 에서, Hdg^k(X_s) 의 특정 원소가 발견되는 s 의 집합.
Cattani-Deligne-Kaplan 1995: Hodge loci 는 대수적 부분다양체.

### 13.3 함의

Hodge loci 의 대수성 → Hodge 류가 "algebraic family" 를 이루면 이들은 대수적 순환으로
실현될 강한 구조적 증거.

---

## 14. 부록 — 현재 주요 접근법

### 14.1 Motivic 접근

Grothendieck 동기(motive) 와 André 의 absolute Hodge motive. Hodge 추측을 motivic 언어로
표현 + standard conjectures 와 통합.

### 14.2 K-이론 접근

Bloch-Beilinson 추측은 K-이론과 motivic cohomology 로 Hodge 를 일반화. Chow 군과 Hodge 류의
연결 탐색.

### 14.3 Harmonic analysis 접근

L²-Hodge 이론 (Morrey-Kodaira), CR 구조에서의 Hodge. 복소기하 도구로 Hodge 구조 정교화.

---

## 15. 부록 — 주요 Hodge 수 계산 예

### 15.1 ℙ^n

h^{p,p} = 1 (0 ≤ p ≤ n), 기타 0.

### 15.2 타원곡선 E

h^{0,0} = h^{1,1} = 1, h^{1,0} = h^{0,1} = 1. 총 Hodge 다이아몬드 (마름모꼴 1 형태):
```
       1
     1   1
       1
```

### 15.3 K3 곡면

h^{0,0} = h^{2,2} = 1, h^{1,1} = 20, h^{2,0} = h^{0,2} = 1. χ = 1 + 20 + 1 = 24.
Hodge 다이아몬드:
```
          1
       0     0
    1    20    1
       0     0
          1
```

### 15.4 Calabi-Yau 3-fold

h^{0,0} = h^{3,3} = 1, h^{3,0} = h^{0,3} = 1, h^{2,0} = h^{0,2} = 0,
h^{1,1} = a, h^{2,1} = h^{1,2} = b. 모듈라이 공간 차원이 b, Kähler class 는 a 차원.

### 15.5 Abelian variety A = E × E

h^{p,q}(A) = binomial(2, p)·binomial(2, q). H²(A; ℚ) = 6 차원, (1,1)-부분 h^{1,1} = 4.

---

## 16. 부록 — Lefschetz (1,1) 증명 재구성

### 16.1 exponential sheaf 열

0 → ℤ → 𝒪_X → 𝒪_X^* → 0 (𝒪_X^* = multiplicative group).

### 16.2 긴 완전열

```
  H^1(X; 𝒪_X) → H^1(X; 𝒪_X^*) = Pic(X) → H²(X; ℤ) → H²(X; 𝒪_X)
```

### 16.3 Hodge 분해 활용

H²(X; 𝒪_X) = H^{0,2}(X). 따라서 α ∈ H²(X; ℤ) 가 H^{0,2} 에서 영으로 사상 ⟺ α ∈ im(Pic).
Hodge 분해로 α ∈ H²(X; ℚ) ∩ H^{1,1} ⟹ α 는 ℤ-계수 배수에서 Hdg¹ 원소이고, H^{0,2} 성분이 0.

### 16.4 결론

Hdg¹(X) 의 모든 원소가 Pic(X) 상으로 실현 ⟹ divisor 의 (ℚ-계수) 선형결합으로 실현.
∴ (1,1) Hodge 추측 증명.

---

## 17. 다음 문서

- PROB-P1-6 : BT-546 BSD 심화
- PROB-P1-7 : BT-547 푸앵카레 심화
- N6-P1-3 : n=6 정직성 원칙

BT-545 는 P2~P3 단계에서 motivic 통합과 standard conjectures, Hodge loci 분석으로
심화한다. 본 P1 노트는 Clay 명제의 정밀 분해 + 대표 해결/반례 지도 를 목적으로 한다.
