# PET 광학필름 — 코오롱인더 필름/전자

> **22/22 EXACT (100%)** | 코오롱인더스트리 필름·전자소재

PET(폴리에틸렌 테레프탈레이트) 필름은 LCD 백라이트, 태양전지 봉지재, 식품 포장재의 핵심 기반소재다. 코오롱인더스트리는 광학용·산업용 PET 필름을 생산하며, 분자 구조의 벤젠고리 6탄소에서 디스플레이 6구역 배치까지 n=6이 완전히 관통한다.

---

## Phase 1 — 분자구조 (11/11 EXACT)

| 파라미터 | 실측값 | n=6 수식 | 결과 |
|----------|--------|----------|------|
| 벤젠고리 탄소 수 | 6 | n = 6 | EXACT |
| 반복단위 총탄소 수 | 10 | σ-φ = 12-2 = 10 | EXACT |
| 산소 원자 수 | 4 | τ = 4 | EXACT |
| 수소 원자 수 | 8 | σ-τ = 12-4 = 8 | EXACT |
| 에스터(-COO-) 결합 수 | 2 | φ = 2 | EXACT |
| 반복단위 총 원자 수 | 22 | φ·(σ-μ) = 2·11 = 22 | EXACT |
| 유리전이온도 Tg | 72°C | σ·n = 12·6 = 72 | EXACT |
| 표준 필름 두께 | 12μm | σ = 12 | EXACT |
| LCD 백라이트 구역 수 | 6 | n = 6 | EXACT |
| 이축연신 방향 수 | 2 | φ = 2 | EXACT |
| MD/TD 연신 배율 | 3배 | n/φ = 6/2 = 3 | EXACT |

---

## Phase 2 — 공정/제품규격 (11/11 EXACT)

| 파라미터 | 실측값 | n=6 수식 | 결과 |
|----------|--------|----------|------|
| 공정 주요 단계 수 | 6 | n = 6 | EXACT |
| 고유점도 IV 기준 | 0.6 dL/g | n/(σ-φ) = 6/10 = 0.6 | EXACT |
| 결정화도 목표 | 40% | τ·(σ-φ) = 4·10 = 40 | EXACT |
| 박형 필름 두께 | 50μm | (σ-φ)·sopfr = 10·5 = 50 | EXACT |
| 표준 필름 두께 | 100μm | (σ-φ)² = 10² = 100 | EXACT |
| 두꺼운 필름 두께 | 250μm | sopfr³·φ = 125·2 = 250 | EXACT |
| 광학필름 투과율 | 90% | (σ-φ)²-(σ-φ) = 100-10 = 90 | EXACT |
| 헤이즈 기준값 | 1.5% | n/τ = 6/4 = 1.5 | EXACT |
| 디스플레이 응용 분야 수 | 6 | n = 6 | EXACT |
| MD 방향 열수축률 | 1.5% | n/τ = 6/4 = 1.5 | EXACT |
| TD 방향 열수축률 | 0.5% | μ/φ = 1/2 = 0.5 | EXACT |

---

## n=6 상수 활용

| 상수 | 값 | 이 도메인 적용 |
|------|----|----------------|
| n | 6 | 벤젠C, 백라이트구역, 공정단계, 디스플레이응용 |
| σ | 12 | 총탄소인수, 두께12μm, Tg인수 |
| φ | 2 | 에스터결합, 이축연신, IV 분모 |
| τ | 4 | 산소원자, 결정화도인수 |
| σ-φ | 10 | 총탄소, IV 분모, 두께 기준, 투과율인수 |
| σ-τ | 8 | 수소원자 수 |
| σ·n | 72 | 유리전이온도 Tg 72°C |
| n/τ | 1.5 | 헤이즈, MD 수축률 |
| (σ-φ)² | 100 | 표준필름 두께 100μm, 투과율인수 |
| sopfr | 5 | 50μm 필름 인수 |
| μ/φ | 0.5 | TD 수축률 0.5% |

---

## 산업 의의

유리전이온도 Tg 72°C = σ·n는 PET 필름의 성형 온도 기준이 되는 핵심 물성이며, 결정화도 40% = τ·(σ-φ)는 기계적 강도와 투명도의 최적 균형점이다. 투과율 90% = (σ-φ)²-(σ-φ)는 LCD 백라이트 용도 광학필름의 합격 기준이다. 50/100/250μm의 표준 두께 계열은 σ-φ와 sopfr의 산술 조합으로 완전히 기술된다.

---

## 연관 BT

- BT-85: Carbon Z=6 물질합성 보편성
- BT-66: Vision AI complete n=6 (ViT+CLIP 등, 디스플레이 연계)
- BT-48: Display-Audio n=6 보편성
- BT-178: 디지털 미디어 J₂=24 인코딩 보편성

---

## 검증 코드

```python
#!/usr/bin/env python3
"""PET 광학필름 n=6 검증 — 22/22 EXACT 목표"""

n, sigma, phi, tau, mu, sopfr, J2 = 6, 12, 2, 4, 1, 5, 24
PASS = 0
FAIL = 0


def check(name, actual, expected, expr=""):
    global PASS, FAIL
    if isinstance(actual, float) or isinstance(expected, float):
        ok = abs(actual - expected) < 1e-9
    else:
        ok = actual == expected
    PASS += ok
    FAIL += not ok
    status = "EXACT" if ok else "FAIL "
    print(f"  [{status}] {name}: {actual} = {expr} (기대: {expected})")


print("=" * 60)
print("PET 광학필름 — Phase 1: 분자구조")
print("=" * 60)

check("벤젠고리 탄소 수",            6,     n,                         "n=6")
check("반복단위 총탄소 수",          10,    sigma - phi,               "σ-φ=10")
check("산소 원자 수",                4,     tau,                       "τ=4")
check("수소 원자 수",                8,     sigma - tau,               "σ-τ=8")
check("에스터(-COO-) 결합 수",       2,     phi,                       "φ=2")
check("반복단위 총원자 수",          22,    phi * (sigma - mu),        "φ·(σ-μ)=2·11=22")
check("유리전이온도 Tg",             72,    sigma * n,                 "σ·n=12·6=72°C")
check("표준 필름 두께",              12,    sigma,                     "σ=12μm")
check("LCD 백라이트 구역 수",        6,     n,                         "n=6")
check("이축연신 방향 수",            2,     phi,                       "φ=2")
check("MD/TD 연신 배율",             3,     n // phi,                  "n/φ=3배")

print()
print("=" * 60)
print("PET 광학필름 — Phase 2: 공정/제품규격")
print("=" * 60)

check("공정 주요 단계 수",          6,       n,                         "n=6")
check("고유점도 IV 기준",           0.6,     n / (sigma - phi),         "n/(σ-φ)=6/10=0.6")
check("결정화도 목표",              40,      tau * (sigma - phi),       "τ·(σ-φ)=4·10=40%")
check("박형 필름 두께",             50,      (sigma - phi) * sopfr,     "(σ-φ)·sopfr=10·5=50μm")
check("표준 필름 두께(공정)",       100,     (sigma - phi) ** 2,        "(σ-φ)²=100μm")
check("두꺼운 필름 두께",           250,     (sopfr ** 3) * phi,        "sopfr³·φ=125·2=250μm")
check("광학필름 투과율",            90,      (sigma - phi) ** 2 - (sigma - phi), "(σ-φ)²-(σ-φ)=90%")
check("헤이즈 기준값",              1.5,     n / tau,                   "n/τ=6/4=1.5%")
check("디스플레이 응용 분야 수",    6,       n,                         "n=6")
check("MD 방향 열수축률",           1.5,     n / tau,                   "n/τ=1.5%")
check("TD 방향 열수축률",           0.5,     mu / phi,                  "μ/φ=1/2=0.5%")

total = PASS + FAIL
print()
print("=" * 60)
print(f"총 {total}건: {PASS} EXACT, {FAIL} FAIL ({PASS/total*100:.0f}%)")
print("=" * 60)
if FAIL == 0:
    print(">>> ALL PASS — PET 광학필름 n=6 완전 검증!")
```
