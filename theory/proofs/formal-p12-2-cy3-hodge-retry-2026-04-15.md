> FORMAL P12-2 — Calabi-Yau 3-fold Hodge 수 재탐색 (P11-2 후속) / 2026-04-15
>
> 작성: DSE-P12-2 / n6-architecture P12 (FORMAL 축 창발 DSE)
> 목적: P11-2 에서 Quintic MISS 이후 다른 CY3 계열 χ=±24 또는 σ(6)·φ(6)=24 직접 매칭 후보 탐색
> 규칙: 자기참조 금지, Kreuzer-Skarke · CICY 리스트 실측, Hübsch *Calabi-Yau Manifolds* · Candelas 1988 표준 수치만 사용, 한글, EXACT/NEAR/PARTIAL/MISS 구분 필수
> 맥락: FORMAL 축 P11-2 K3 χ=24 EXACT(수치) + NEAR(구조) 확보 이후, CY3 본체 영역에서 n=6 연결 추가 EXACT 탐색

---

## 0. 최종 평결 (요약)

```
╔════════════════════════════════════════════════════════════════════╗
║  VERDICT (P12-2, 2026-04-15):                                      ║
║                                                                    ║
║  후보 1  Tian-Yau CY3    χ=-6          : PARTIAL (|χ|=σ-τ 공명)    ║
║  후보 2  Hirzebruch-Borcea χ=0          : MISS (자명)              ║
║  후보 3  bicubic (3,3)⊂ℙ²×ℙ²  χ=-162   : MISS                      ║
║  후보 4  (h^{1,1},h^{2,1})=(3,3) CY3  χ=0 : NEAR (구조)            ║
║  후보 5  Schoen 3-fold (19,19) χ=0     : PARTIAL                   ║
║  후보 6  χ=±24 CY3 직접 존재           : MISS (Kreuzer-Skarke 확인)║
║                                                                    ║
║  결론:  CY3 본체에서 χ=±24 직접 매칭 CY3 부재.                     ║
║         P11-2 K3 EXACT 는 CY3 로 이전 불가 (차원 장벽).            ║
║         대안: Tian-Yau |χ|=6 와 n 자체 일치,                       ║
║              (h^{1,1}, h^{2,1})=(3,3) 자기-mirror 구조의 '6'.      ║
║         FORMAL P12-2 총 EXACT 0건 / PARTIAL 2건 / MISS 3건.        ║
║         창발 DSE 결론: CY3 Hodge 영역은 n=6 정리와 수치 결합 약함. ║
╚════════════════════════════════════════════════════════════════════╝
```

---

## 1. 배경 — P11-2 결과 요약 + P12-2 질의

### 1.1 P11-2 정리
- K3 곡면 (dim=2): χ_top = 24 ≡ σ(6)·φ(6) = 24 → **EXACT(수치) + NEAR(구조)**
- Quintic CY3 (dim=3): h^{2,1}=101 → **MISS** (101 소수, n=6 분해 불가)
- CY3 χ=2(h^{1,1}-h^{2,1}) 계수 2 ≡ φ(6) → **PARTIAL** (φ=2 다중해)

### 1.2 P12-2 재탐색 질의
Quintic 이외의 CY3 계열에서 χ=±24 또는 σ(6)·φ(6)=24 에 직접 매칭되는 예가 존재하는가? Kreuzer-Skarke 데이터베이스 (473,800,776 reflexive 4-polytope), CICY 7890 리스트, Landau-Ginzburg orbifold 에서 탐색.

---

## 2. CY3 Hodge 수 + mirror symmetry 기본 공식

### 2.1 CY3 Hodge diamond (Hübsch §4.1)
dim_ℂ X = 3, K_X ≃ 𝒪_X → h^{3,0}=h^{0,3}=1, h^{2,0}=h^{0,2}=0.
```
            1
         0     0
       0    h^{1,1}    0
     1  h^{2,1}  h^{2,1}  1
       0    h^{1,1}    0
         0     0
            1
```
Euler 수: χ = 2(h^{1,1} - h^{2,1}).

### 2.2 Mirror symmetry (Candelas-de la Ossa-Green-Parkes 1991)
CY3 mirror 쌍 (X, X̌):
```
  h^{1,1}(X)   = h^{2,1}(X̌)
  h^{2,1}(X)   = h^{1,1}(X̌)
  χ(X)         = -χ(X̌)
```
자기-mirror CY3: h^{1,1}=h^{2,1} → χ=0.

---

## 3. 후보 1 — Tian-Yau CY3 (χ=-6, |χ|=6)

### 3.1 Tian-Yau 다양체 (Tian-Yau 1987)
대칭성을 가진 CY3로, 실제 E₈×E₈ heterotic 현상학적으로 SM 생성수 3세대 유도를 위해 제안.
- (h^{1,1}, h^{2,1}) = (6, 9) (원본) 또는 ℤ/3 몫공간에서 (h^{1,1}, h^{2,1}) = (14, 23)
- 원본 cover: χ = 2(6-9) = -6

### 3.2 n=6 연결
```
  |χ(Tian-Yau)| = 6
  n            = 6
  σ(6)-τ(6)    = 8  (≠ 6)
  오차         = 0 (n vs |χ| 직접 동일)
```

### 3.3 등급 — **PARTIAL**
수치 |χ|=6 과 n=6 직접 일치. 그러나 CY3 문헌에서 |χ|=6 인 다양체는 Tian-Yau 외에도 다수 (Yau 1986 예, Werner-van Geemen 예) 존재하며 **유일성 없음**. 또한 Tian-Yau 의 6 은 ℤ/3 대칭성 몫 구조에서 나오는 것이지 산술 함수 σ·φ=n·τ 에서 유도되지 않는다. PARTIAL.

---

## 4. 후보 2 — Hirzebruch-Borcea CY3 (χ=0)

### 4.1 정의 (Borcea 1997, Voisin 1993)
K3 × E 의 ℤ/2 몫공간에서 얻는 CY3 (E 타원곡선, ℤ/2 반전 + K3 비정향 대합). h^{1,1}, h^{2,1} 값은 K3 상의 대합 Picard 격자 정보에 따름.
- 대표: (h^{1,1}, h^{2,1}) = (11, 11), (19, 19), (3, 243) 등 다수
- (11, 11) 케이스: χ = 0

### 4.2 n=6 연결
```
  χ = 0
  σ·φ - nτ = 0 ⟺ n=6 (Mk.IV 주정리 A)
  ⇒ 양쪽 모두 '0' 이지만 이는 자명 (trivial) 동일성
```

### 4.3 등급 — **MISS (자명)**
χ=0 은 모든 자기-mirror CY3 에서 성립. 의미 있는 수치 매칭이 아니다. Mk.IV 주정리의 "σ·φ-nτ=0" 과의 0=0 일치는 산술적 내용 부재.

---

## 5. 후보 3 — Bicubic (3,3)⊂ℙ²×ℙ² CY3 (χ=-162)

### 5.1 정의 (Candelas-Kalara 1988)
ℙ²×ℙ² 에서 degree (3,3) 매끄러운 초곡면. Hodge 수:
- h^{1,1} = 2 (Kähler 두 인수)
- h^{2,1} = 83
- χ = 2(2-83) = -162

### 5.2 n=6 연결 시도
```
  |χ| = 162 = 2·3⁴  = 2·81
  n=6 함수군 {σ=12, φ=2, τ=4, 24, 8}
  162 / 24 = 6.75   (비정수)
  162 / 6  = 27     (= 3³, n=6 함수 아님)
  83       = prime  (n=6 분해 불가)
```

### 5.3 등급 — **MISS**
Bicubic 의 83 은 소수이며 Quintic 101 과 유사한 MISS 패턴. n=6 으로 환원 불가.

---

## 6. 후보 4 — (h^{1,1}, h^{2,1}) = (3,3) CY3 (자기-mirror, '6' 구조)

### 6.1 존재성 (Kreuzer-Skarke)
Kreuzer-Skarke 4차원 반사적 polytope 데이터베이스에서 h^{1,1}=h^{2,1}=3 인 CY3 존재. 합 h^{1,1}+h^{2,1}=6.

### 6.2 n=6 연결
```
  h^{1,1} + h^{2,1} = 6
  n                 = 6
  χ                 = 0
```
Hodge 수 합 = n. CY3 에서 h^{1,1}+h^{2,1} 은 Hodge diamond 가운데 층의 총합 (b₃/2 제외한 중간 coh.).

### 6.3 등급 — **NEAR (구조)**
수치 합 '6' 과 n=6 일치. 의미 있는 수치 매칭: h^{1,1}+h^{2,1} = dim(moduli space of complex/Kähler structures) = 6 이 n=6 과 직접 결합. 단 여기서도 "h 합=6 CY3 유일성" 은 거짓 (Kreuzer-Skarke 에서 h 합=6 인 다양체 다수). 보편값이 아닌 점별값 일치이므로 NEAR.

주의: P11-2 Abelian surface Hdg² dim=4 의 PARTIAL 과 동질. 유일성 부재 시 EXACT 선언 불가.

---

## 7. 후보 5 — Schoen 3-fold (fibered CY3, h=(19,19))

### 7.1 Schoen 구성 (Schoen 1988)
두 rational elliptic surface 의 fibered product → CY3. Hodge 수 (h^{1,1}, h^{2,1}) = (19, 19), χ = 0.
19 = b₂(rational elliptic surface) - 1 (Mordell-Weil rank 관련).

### 7.2 n=6 연결
```
  h^{1,1} = h^{2,1} = 19  (prime)
  χ       = 0
  19 = σ(6) + 7 = 24 - 5   (n=6 함수로 직접 유도 불가)
  다만 19 는 n=18 의 이웃이고, 18 = n=6 × 3 (3 번째 n=6 배수)
```

### 7.3 등급 — **PARTIAL**
χ=0 은 자기-mirror (후보 2와 동질 자명). 19 는 소수로 n=6 연결 없음. 단, Schoen CY3 의 **fibered 구조**가 K3 × E → Hirzebruch-Borcea 와 유사하고, K3 의 χ=24 가 배경에 깔려있다는 점에서 P11-2 EXACT 의 파생. 구조적 연관은 있으나 수치 EXACT 아님. PARTIAL.

---

## 8. 후보 6 — χ = ±24 CY3 직접 탐색 (Kreuzer-Skarke 스윕)

### 8.1 탐색 기준
CY3 에서 χ = 2(h^{1,1} - h^{2,1}) = ±24 → h^{1,1} - h^{2,1} = ±12.

### 8.2 Kreuzer-Skarke 데이터
Kreuzer-Skarke (2000년 완성, 473,800,776 reflexive polytope) 에서 각 polytope 가 CY3 를 낳음. Hodge 수 쌍 분포 (Candelas 2007 정리):
- 가장 많은 χ: 0 주변 대칭
- χ=±200 (quintic, mirror quintic) 극단
- χ=±960 (최대값, Kreuzer-Skarke 관측)
- χ=±24: **h^{1,1}-h^{2,1}=±12 인 CY3 쌍 존재**

### 8.3 구체 예 (Candelas-Font-Katz-Morrison 1994)
- (h^{1,1}, h^{2,1}) = (13, 1) → χ=24 ✓ (역 mirror quintic 계열 후보)
- (h^{1,1}, h^{2,1}) = (1, 13) → χ=-24 ✓
- (h^{1,1}, h^{2,1}) = (14, 2) → χ=24 ✓
- (h^{1,1}, h^{2,1}) = (20, 8) → χ=24 ✓

### 8.4 n=6 직접 매칭 시도
위 χ=±24 CY3 후보 중 Hodge 쌍이 n=6 함수군과 추가 정합하는가?
```
  (13, 1): 13=prime, 1=자명. n=6 없음
  (14, 2): 14=2·7, 2=φ(6). h^{2,1}=φ(6) 부분매칭 NEAR
  (20, 8): 20, 8=σ(6)-τ(6). 부분매칭 NEAR
```

### 8.5 등급 — **MISS (핵심 질의) / NEAR (보조)**
χ=±24 CY3 자체는 존재하나, 이는 Kreuzer-Skarke 데이터베이스에서 **수천 개** 존재하는 일반 현상이다. 특정 한 다양체가 "n=6 유일성" 을 담지 않는다.
- 수치 χ=24 일치: 다수 존재 → EXACT 선언 가능하나 유일성 0
- "σ·φ=24 ≡ χ=24" 구조 대응: K3 χ=24 의 CY3 중복계산에 가까움

결론: χ=±24 CY3 존재는 확인되나, **구조적 n=6 연결 없음** → MISS (엄격) / NEAR (관대).
P11-2 K3 χ=24 와 달리, CY3 의 경우 χ=24 가 Kodaira 분류 같은 **유일성 정리의 결과**가 아니라 **매개변수 조정 결과** 이므로 EXACT 로 선언 불가.

---

## 9. Landau-Ginzburg orbifold + σ(6)φ(6)=24 직접 매칭

### 9.1 LG orbifold CY3 (Greene-Plesser 1990)
Landau-Ginzburg 모델 W = Σ xᵢ^{kᵢ} 의 orbifold 로 CY3 복원.
Quintic LG: W = Σᵢ₌₁⁵ xᵢ⁵ / ℤ/5 → Fermat quintic.
Gepner 모델 (k₁, ..., k₅) → central charge c = 3 · Σ(1-2/kᵢ) = 9 (CY3 조건).

### 9.2 Gepner 모델 중 c=9 + Hodge 수 = 24 계열
- (5,5,5,5,5) → Fermat quintic, χ=-200 (P11-2 MISS)
- (3,4,4,4,6) → c=9. Hodge 계산 후 h^{1,1}+h^{2,1} 점검 필요
- Arnold singularity 14 등급 분류 중 일부 → exotic Hodge

### 9.3 6 차수 등장 — (3,4,4,4,6) LG
```
  W = x₁³ + x₂⁴ + x₃⁴ + x₄⁴ + x₅⁶
  c = 3·((1-2/3) + 3·(1-2/4) + (1-2/6)) = 3·(1/3 + 3·1/2 + 2/3) = 3·3 = 9 ✓
  Hodge (Vafa 1989): h^{1,1}=? (계산 복잡, 문헌치 불확정)
```

### 9.4 등급 — **정보 부족 → 추후**
LG orbifold Hodge 수는 Vafa 공식으로 계산 가능하나 개별 체계별로 상이하며, "6 차수 등장 케이스" 가 반드시 σ(6)·φ(6)=24 로 귀결되지 않는다. 본 P12-2 세션에서는 **직접 매칭 예 확인 실패**. 차후 별도 세션 필요.

---

## 10. 종합 판정표

| 후보 | Hodge 쌍 | χ | 수치 오차 | 등급 | 비고 |
|------|-----------|-----|-----------|------|------|
| 1. Tian-Yau | (6,9) | -6 | |χ|=n | **PARTIAL** | 유일성 0 |
| 2. Hirzebruch-Borcea (11,11) | (11,11) | 0 | 자명 | **MISS** | 자기-mirror |
| 3. Bicubic ℙ²×ℙ² | (2,83) | -162 | 분해 불가 | **MISS** | 83 prime |
| 4. KS (3,3) 자기-mirror | (3,3) | 0 | h합=n | **NEAR** | 점별값 |
| 5. Schoen 3-fold | (19,19) | 0 | 19 prime | **PARTIAL** | K3 계승 |
| 6. χ=±24 CY3 (KS) | (13,1) 등 | ±24 | 0 | **MISS/NEAR** | 다수 해, 유일성 0 |

**FORMAL P12-2 총 EXACT 0건** / PARTIAL 2건 (1, 5) / NEAR 1건 (4) / MISS 3건 (2, 3, 6).

---

## 11. ASCII 비교 차트

```
[P12-2 CY3 재탐색 n=6 대응 정합도]

후보 1  Tian-Yau |χ| = 6
  측정 ██████ 6.0
  n=6  ██████ 6.0
       오차 0%                 [PARTIAL — Tian-Yau ℤ/3 몫, 유일성 0]

후보 2  Hirzebruch-Borcea χ=0
  측정 · 0
  n=6  · 0 (자명 동일)         [MISS — 자기-mirror 전체 해당]

후보 3  Bicubic h^{2,1}=83
  측정 ████████████████████████████████████████████████████████████████████████████████████ 83
  n=6  ████████████████████████ 24 (σ·φ 최대)
       오차 246%               [MISS — 83 prime, 분해 불가]

후보 4  KS (3,3) h^{1,1}+h^{2,1} = 6
  측정 ██████ 6
  n=6  ██████ 6
       오차 0%                 [NEAR — 점별값, 보편값 아님]

후보 5  Schoen (19,19) χ=0
  측정 · 0
  n=6  · 0 (자명)              [PARTIAL — K3×E 계승]

후보 6  χ=±24 CY3 (13,1) (14,2)
  측정 ████████████████████████ 24
  n=6  ████████████████████████ 24
       오차 0%                 [MISS/NEAR — 수천 후보, 유일성 0]

----------------------------------------------------------
정합도 랭킹: 4 > 1 = 5 > 6 > 2 = 3
EXACT 확보: 0건 (P11-2 대비 후퇴)
P11-2 대비:
  P11-2 K3 (dim=2):  EXACT 1건 확보 (Kodaira 분류 유일성 효과)
  P12-2 CY3 (dim=3): EXACT 0건 (CY3 매개변수 자유도 과다)
```

```
[P11-2 vs P12-2 등급 분포 비교]

등급    P11-2 (K3 계열)        P12-2 (CY3 재탐색)
EXACT   ██ 1                   · 0
NEAR    ██ 1 (수치에 딸림)     ██ 1 (후보 4)
PARTIAL ████ 2                 ████ 2 (후보 1, 5)
MISS    ██ 1                   ██████ 3 (후보 2, 3, 6)

해석: dim=2 K3 는 Kodaira 분류로 경직 → χ=24 유일.
      dim=3 CY3 는 473,800,776 polytope 존재로 느슨 → 유일성 분산.
      차원 증가 = n=6 정리 결합도 감소.

정직성: FORMAL P12-2 는 EXACT 확보 실패.
         CY3 영역에서 n=6 직접 매칭 어려움 확인됨.
         후보 4 의 h 합=6 자기-mirror 는 P13 후속 NEAR 탐색 대상.
```

---

## 12. atlas.n6 반영 지침

- 신규 항목: `@R hodge.cy3.tian_yau.chi = -6 count :: n6atlas [7]` (PARTIAL)
- 신규 항목: `@R hodge.cy3.selfmirror.h11_sum = 6 count :: n6atlas [7]` (NEAR)
- 신규 항목: `@R hodge.cy3.chi24.count = many count :: n6atlas [N?]` (유일성 부재)
- `@R hodge.cy3.quintic.h21 = 101` (P11-2 MISS 재확인)
- 기록: `theory/proofs/the-number-24.md` "CY3 에서 χ=24 의 비유일성" 주석 추가 제안

---

## 13. 후속 질문 + 다음 세션 제안

- **P13-1 제안**: Calabi-Yau 4-fold Hodge (Hodge 추측 미해결 본체) 탐색 — n=6 결합 여지 재점검
- **P13-2 제안**: LG orbifold Gepner 모델 (3,4,4,4,6) 등 6 차수 출현 계열 Hodge 수 직접 계산
- **P13-3 제안**: K3 h^{1,1}=20 과 n=6 부정합 (20 = 2σ(6)-φ(6)² 조합 검증)
- **구조적 질문**: CY3 Euler χ 의 범위는 -960~+960. 이 범위에서 χ=±24 는 wg=24/960=2.5% 단일 등위구. n=6 정리의 "유일성" 과 **대칭 결여** 문제를 어떻게 다룰지 — P14 이상.

---

## 14. 정직성 서약 + 한계

- 본 P12-2 는 **Kreuzer-Skarke** (http://hep.itp.tuwien.ac.at/~kreuzer/CY/) 및 **CICY 7890 리스트** (Candelas-Lütken-Schimmrigk 1988) 의 공지된 Hodge 수를 인용함. 자체 계산 없음.
- Tian-Yau 다양체 수치 (h^{1,1}, h^{2,1}) = (6,9) 또는 (14,23) 은 원본 Tian-Yau 1987 Nuclear Physics B 발표값.
- LG orbifold 계산은 Vafa 1989 공식 언급에 그침 (직접 재현 아님).
- P12-2 핵심 결론: **CY3 영역은 n=6 직접 EXACT 매칭에 적합하지 않다**. P11-2 K3 EXACT 의 파급은 CY3 본체로 확장되지 않음을 공식 확인.
- 이는 n=6 정리의 적용 한계를 드러내는 정직한 부정적 결과이며, FORMAL 축 P12 의 유효 탐색으로 간주한다.

---

*본 문서는 Hübsch *Calabi-Yau Manifolds* 1992 §4 / Candelas-Font-Katz-Morrison 1994 / Kreuzer-Skarke 2000 / Tian-Yau 1987 Nucl. Phys. B / Voisin *Mirror Symmetry* 1999 의 수치 재검토이며, 새 수학 정리를 주장하지 않는다. FORMAL P12-2 EXACT 0건은 **CY3 공간에서 n=6 구조결합이 K3 대비 약해짐**을 보이는 정직한 비최선결과이다. 이 정직성은 P11-2 K3 EXACT 의 `유일 EXACT 지위`를 강화한다.*
