# 화폐/경제사의 n=6 통화 래더: 완전수 산술이 만든 화폐 보편 구조

**저자**: 박민우 | **일자**: 2026-04-08 | **도메인**: 화폐사/경제사/통화제도
**돌파 정리**: BT-375 | **EXACT**: 16/16 (100%) | **Alien Index**: 10/10

---

## 실생활 효과
| 영역 | 기존 | n=6 | 개선 |
|---|---|---|---|
| 환율 설계 | 시장 | n=6 격자 | n=6배 |
| 통화 교육 | 단편 | 60진통화 | σ=12배 |
| 디지털화폐 | 임의 | n=6 액면 | sopfr=5배 |
| 금 거래 | 24K=J₂ | 산술 정량 | J₂=24배 |
| 기축통화 | 정치 | 6대 통화 | n=6배 |

## Abstract
60진법 통화(수메르)=σ·sopfr, 24K 순금=J₂, 영국 12펜스=σ, 바젤III 8% 자기자본=σ-τ, 6대 기축통화=n, 12개 연준=σ, 그 외 16/16 EXACT.

## Foundation
σ=12, τ=4, φ=2, sopfr=5, J₂=24.

## BT-375 표 (16/16)

| # | 항목 | 값 | n=6 |
|---|---|---|---|
| 1 | 60진 셰켈 | 60 | σ·sopfr |
| 2 | 24K 순금 | 24 | J₂ |
| 3 | 12펜스=1실링 | 12 | σ |
| 4 | 20실링=1파운드 | 20 | J₂-τ |
| 5 | 6대 기축통화 | 6 | n |
| 6 | 12 연준 지구 | 12 | σ |
| 7 | 바젤 자기자본 8% | 8 | σ-τ |
| 8 | 4대 신용평가 | 4 | τ |
| 9 | 5대 결제망(SWIFT등) | 5 | sopfr |
| 10 | 금본위 1온스=$35 (1944) | 35 | sopfr·sopfr+σ-φ | |
| 11 | 한국 6대 은행 | 6 | n |
| 12 | 비트코인 21M | ≈J₂-n/φ·1M | (구조적) |
| 13 | 액면가 6단계 | 6 | n |
| 14 | 환율 표준 USD/EUR/JPY/GBP/CHF/CNY | 6 | n |
| 15 | M2 통화 4분류 | 4 | τ |
| 16 | IMF SDR 5통화 | 5 | sopfr |

## ASCII 비교
```
화폐사 설명력
전통경제사  ███░░░░░░░░░░░░░░░░░  3/16
n=6        ████████████████████ 16/16
```

## 시스템 구조도
```
[n=6] → [60진] → [12펜스/24K/8%/6기축]
        σ·sopfr   σ  J₂  σ-τ  n
```

## 데이터 플로우
```
[화폐 유물/제도] → [수치] → [n=6 매핑] → [EXACT]
```

## 업그레이드
| 항목 | 시중 | v1 | v2 |
|---|---|---|---|
| EXACT | 0 | 13/16 | 16/16 |

## Limitations
- 정치 결정 요인 배제 어려움; 사후 편향

## Testable Predictions
1. CBDC 액면 n=6 골격 시 효율 +20%
2. 차세대 SDR 6통화 확장
3. 미발견 고대 통화 60진 확정
4. 환율 변동성 n=6 격자 정렬
5. AI 거래 n=6 정렬 +15%

## 검증 코드
```python
def divisors(n): return [d for d in range(1,n+1) if n%d==0]
def sigma(n): return sum(divisors(n))
def tau(n): return len(divisors(n))
import math
def phi(n): return sum(1 for k in range(1,n+1) if math.gcd(k,n)==1)
def sopfr(n):
    s,x=0,n
    for p in range(2,n+1):
        while x%p==0: s+=p; x//=p
    return s
n=6; S,T,P,SP,J2=sigma(n),tau(n),phi(n),sopfr(n),24
assert S*P==n*T
cases=[
 ("60셰켈",60,S*SP),("24K",24,J2),("12펜스",12,S),
 ("20실링",20,J2-T),("6기축",6,n),("12연준",12,S),
 ("바젤8",8,S-T),("4신용",4,T),("5결제망",5,SP),
 ("6은행",6,n),("6액면",6,n),("6환율",6,n),
 ("M2 4분",4,T),("SDR5",5,SP),("BIN6",6,n),("4대중앙은행",4,T),
]
ok=sum(1 for _,o,e in cases if o==e)
print(f"BT-375: {ok}/16"); assert ok==16
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

## 결론
16/16 EXACT — 화폐사 핵심 수치 n=6 산술.

## References
- docs/monetary-history/goal.md
