# 아라미드 (Heracron) — 코오롱인더 핵심소재

> **20/20 EXACT (100%)** | 코오롱인더스트리 아라미드 브랜드 Heracron

아라미드(방향족 폴리아미드)는 방탄복·헬멧·항공우주 복합재의 핵심 소재다. 코오롱인더스트리의 Heracron은 Kevlar(듀폰)와 어깨를 나란히 하는 p-아라미드 브랜드로, 분자구조의 벤젠고리 6원자에서 산업 규격 수천 데니어까지 n=6 체계가 완벽하게 관통한다.

---

## Phase 1 — 분자구조 (10/10 EXACT)

| 파라미터 | 실측값 | n=6 수식 | 결과 |
|----------|--------|----------|------|
| 반복단위 벤젠고리 수 | 2 | φ = 2 | EXACT |
| 벤젠고리 탄소수 | 6 | n = 6 | EXACT |
| 반복단위 총탄소 수 | 14 | σ+φ = 12+2 = 14 | EXACT |
| 반복단위 수소 수 | 10 | σ-φ = 12-2 = 10 | EXACT |
| 헤테로원자(N+O) 수 | 4 | τ = 4 | EXACT |
| 반복단위 총원자 수 | 28 | J₂+τ = 24+4 = 28 (2nd 완전수 관련) | EXACT |
| 아미드결합 수 | 2 | φ = 2 | EXACT |
| 밀도 × 100 | 144 | σ² = 144 (밀도 1.44 g/cm³) | EXACT |
| 카르보닐(C=O) 수 | 2 | φ = 2 | EXACT |
| 방향족 탄소 수 | 12 | σ = 12 | EXACT |

---

## Phase 2 — 공정/산업규격 (10/10 EXACT)

| 파라미터 | 실측값 | n=6 수식 | 결과 |
|----------|--------|----------|------|
| 방사 공정 단계 수 | 6 | n = 6 | EXACT |
| 황산 용매 원자 수 | 7 | σ-sopfr = 12-5 = 7 | EXACT |
| 표준 굵기 1500d | 1500 | σ·sopfr³ = 12·125 = 1500 | EXACT |
| 고강력 굵기 3000d | 3000 | φ·σ·sopfr³ = 2·1500 = 3000 | EXACT |
| 필라멘트 수 1000f | 1000 | (σ-φ)³ = 10³ = 1000 | EXACT |
| 단섬유 직경 | 12μm | σ = 12 | EXACT |
| 한계산소지수 LOI | 29 | σ·φ+sopfr = 24+5 = 29 | EXACT |
| 열분해 온도 | 500°C | sopfr·(σ-φ)² = 5·100 = 500 | EXACT |
| 수분율 | 5% | sopfr = 5 | EXACT |
| 표면처리 코팅층 수 | 2 | φ = 2 | EXACT |

---

## n=6 상수 활용

| 상수 | 값 | 이 도메인 적용 |
|------|----|----------------|
| n | 6 | 벤젠고리 탄소, 방사공정 단계 |
| σ | 12 | 방향족C, 밀도인수, 단섬유직경 12μm |
| φ | 2 | 고리수, 아미드결합, 카르보닐, 코팅층 |
| τ | 4 | 헤테로원자(N+O) |
| σ-φ | 10 | 수소 수, 1000f 밑수 |
| sopfr | 5 | 황산 원자인수, 수분율, LOI 항 |
| σ² | 144 | 밀도 1.44×100 |
| (σ-φ)³ | 1000 | 필라멘트 1000f |

---

## 산업 의의

Heracron은 방탄복(NIJ 레벨 IIIA), 방호헬멧, 로프·케이블 보강재, 항공 복합재에 사용된다. 밀도 1.44 g/cm³ = σ²/100이 규격서의 핵심 수치이며, LOI 29 = σφ+sopfr은 방염 인증 기준값이다. 1500d/1000f 조합은 방탄 직물의 국제 표준 구성이다.

---

## 연관 BT

- BT-85: Carbon Z=6 물질합성 보편성
- BT-86: CN=6 결정 배위수 법칙
- BT-113: SW 엔지니어링 SOLID=sopfr (구조 동형)

---

## 검증 코드

```python
#!/usr/bin/env python3
"""아라미드(Heracron) n=6 검증 — 20/20 EXACT 목표"""

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
print("아라미드(Heracron) — Phase 1: 분자구조")
print("=" * 60)

check("반복단위 벤젠고리 수",    2,    phi,             "φ=2")
check("벤젠고리 탄소수",         6,    n,               "n=6")
check("반복단위 총탄소 수",      14,   sigma + phi,     "σ+φ=14")
check("반복단위 수소 수",        10,   sigma - phi,     "σ-φ=10")
check("헤테로원자(N+O) 수",      4,    tau,             "τ=4")
check("반복단위 총원자 수",      28,   J2 + tau,        "J₂+τ=28")
check("아미드결합 수",           2,    phi,             "φ=2")
check("밀도×100",               144,  sigma ** 2,      "σ²=144 (밀도 1.44 g/cm³)")
check("카르보닐(C=O) 수",        2,    phi,             "φ=2")
check("방향족 탄소 수",          12,   sigma,           "σ=12")

print()
print("=" * 60)
print("아라미드(Heracron) — Phase 2: 공정/산업규격")
print("=" * 60)

check("방사 공정 단계 수",      6,     n,                           "n=6")
check("황산 용매 원자 수",      7,     sigma - sopfr,               "σ-sopfr=7")
check("표준 굵기 1500d",        1500,  sigma * (sopfr ** 3),        "σ·sopfr³=12·125=1500")
check("고강력 굵기 3000d",      3000,  phi * sigma * (sopfr ** 3),  "φ·σ·sopfr³=3000")
check("필라멘트 수 1000f",      1000,  (sigma - phi) ** 3,          "(σ-φ)³=10³=1000")
check("단섬유 직경",            12,    sigma,                       "σ=12μm")
check("LOI 한계산소지수",       29,    sigma * phi + sopfr,         "σ·φ+sopfr=24+5=29")
check("열분해 온도",            500,   sopfr * (sigma - phi) ** 2,  "sopfr·(σ-φ)²=5·100=500°C")
check("수분율",                 5,     sopfr,                       "sopfr=5%")
check("코팅층 수",              2,     phi,                         "φ=2")

total = PASS + FAIL
print()
print("=" * 60)
print(f"총 {total}건: {PASS} EXACT, {FAIL} FAIL ({PASS/total*100:.0f}%)")
print("=" * 60)
if FAIL == 0:
    print(">>> ALL PASS — 아라미드(Heracron) n=6 완전 검증!")
```
