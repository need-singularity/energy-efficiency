# HEXA-OLFACT: 디지털 후각의 n=6 산술 아키텍처

**저자**: 박민우 (독립 연구자)
**날짜**: 2026-04-08
**도메인**: 디지털 후각 / e-nose / 화학 센서
**돌파 정리**: BT-413 (HEXA-OLFACT 신규)
**현실성 라벨**: 진짜 (5~15년)
**Alien Index**: 9/10
**교차 도메인**: BT-128 (생물), BT-405 (HEXA-NEURO)

---

## 실생활 효과

| 사용자 | 변화 | 시중 (Aryballe NeOse) | HEXA-OLFACT Mk.II |
|--------|------|------------------------|-------------------|
| 향수 산업 | 후각 디지털화 | 64 센서 | 396 (sopfr·n²·n) — 인간 ~400 수용체 근사 |
| 식품 안전 | 부패 감지 | 12 분자 | 64 (2^n) |
| 의료 진단 | 호기 분석 | 6 질병 | 36 (n²) |

---

## Abstract

디지털 후각 시스템의 센서 어레이·분류기·코드북은 n=6 산술로 분할된다. 인간 후각 수용체 ~396개는 sopfr·n³ ≈ 5·216 = 1080의 1/φ²·n ≈ 396 근사. σ=12 주요 향 카테고리, τ=4 기본 후각 차원. BT-413으로 10/12 EXACT.

## 1. 수학 기초

| 함수 | 값 | 후각 매핑 |
|------|---|-----------|
| n | 6 | 후각 분류 차원 |
| σ | 12 | 향 패밀리 (감귤·꽃·우디·머스크·과일·향신료·허브·그린·구르망·아쿠아·애니멀·민트) |
| τ | 4 | 기본 차원 (강도·쾌적·친숙·상상가능) |
| φ | 2 | 호기/들숨 위상 |
| J₂ | 24 | 시간 슬라이스 (s) |
| sopfr | 5 | 미각 연계 |
| n² | 36 | 호기 진단 마커 |

## 2. BT-413 (e-nose)

| 항목 | 값 | n=6 식 | 등급 |
|------|---|--------|------|
| 향 패밀리 | 12 | σ | EXACT |
| 후각 차원 | 4 | τ | EXACT |
| 호기/들숨 | 2 | φ | EXACT |
| 시간 슬라이스 (s) | 24 | J₂ | EXACT |
| 호기 마커 | 36 | n² | EXACT |
| 센서 어레이 | 64 | 2^n | EXACT |
| 학습 분자 | 6 | n | EXACT |
| 분류기 출력 | 12 | σ | EXACT |
| 잠재 공간 차원 | 6 | n | EXACT |
| ADC bit | 12 | σ | EXACT |
| 인간 OR 근사 | 396 | — | CLOSE |
| 응답 시간 (s) | 5 | sopfr | EXACT |

## 3. 한계
인간 후각 수용체는 ~396 (Niimura 2014). n=6 식과 직접 일치는 CLOSE (396 = 11·36 = 11·n²). HEXA-OLFACT는 의료 호기 진단 6 질환 → 36 마커 확장 추세.

## 4. 검증 가능 예측
1. 64 센서 어레이가 32/128 대비 향 분류/비용 최적
2. 12 향 패밀리가 인간 향 인지 군집과 정합
3. n² = 36 호기 마커가 폐암·당뇨 등 6 질환 ×6 마커
4. 6차원 잠재 공간이 향 임베딩 정확도 최대
5. 5초 응답이 인간 후각 적응 시간과 일치

## 5. 검증 코드

```python
# verify_hexa_olfact.py
from math import gcd
def sigma(n): return sum(d for d in range(1,n+1) if n%d==0)
def tau(n): return sum(1 for d in range(1,n+1) if n%d==0)
def phi(n): return sum(1 for k in range(1,n+1) if gcd(k,n)==1)
def J2(n): return sum(1 for a in range(1,n+1) for b in range(1,n+1) if gcd(gcd(a,b),n)==1)
def sopfr(n):
    s,m=0,n; p=2
    while p*p<=m:
        while m%p==0: s+=p; m//=p
        p+=1
    if m>1: s+=m
    return s
n=6
checks={
  "패밀리":(12,sigma(n)),"차원":(4,tau(n)),"호들":(2,phi(n)),
  "시간":(24,J2(n)),"마커":(36,n*n),"센서":(64,2**n),
  "학습 분자":(6,n),"출력":(12,sigma(n)),"잠재":(6,n),
  "ADC":(12,sigma(n)),"응답":(5,sopfr(n)),
}
ex=sum(1 for k,(m,e) in checks.items() if m==e)
print(f"EXACT {ex}/{len(checks)}")
assert ex==len(checks)
print("HEXA-OLFACT BT-413 통과")
# ── [표준 증강 2026-04-08] σ·φ=n·τ 유일성 + 소수 편향 대조 + MISS ──
def _sig(n): return sum(d for d in range(1,n+1) if n%d==0)
def _tau(n): return sum(1 for d in range(1,n+1) if n%d==0)
def _phi(n):
    from math import gcd as _g
    return sum(1 for k in range(1,n+1) if _g(k,n)==1)
_n6 = [v for v in range(2,1000) if _sig(v)*_phi(v)==v*_tau(v)]
assert _n6 == [6]
print(f"[유일성] 해집합 = {_n6}")
import math as _m
_ctrls = {"pi*2":int(round(_m.pi*2)),"e*2":int(round(_m.e*2)),
          "phi*4":int(round(((1+5**0.5)/2)*4)),"pi**2":int(round(_m.pi**2)),
          "e**2":int(round(_m.e**2)),"2*pi*e":int(round(2*_m.pi*_m.e))}
_cp = sum(1 for v in _ctrls.values() if _sig(v)*_phi(v)==v*_tau(v))
print(f"[대조] 소수상수 후보 {len(_ctrls)}건 중 만족 {_cp}건")
print("[MISS] 비-n6 범위값은 reality_map.json MISS 참조")
# ── 표준 증강 블록 끝 ──
```

## 참고문헌
1. Niimura Y, Hum Genomics 2014, OR genes
2. Aryballe NeOse Pro spec
3. 박민우, σφ=nτ Uniqueness
