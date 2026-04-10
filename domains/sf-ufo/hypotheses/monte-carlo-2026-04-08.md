# Monte Carlo 재검증 — n=6 유일성 (2026-04-08)

> 데이터: `~/Dev/nexus/shared/reality_map.json` v8.0 (2026-04-08)
> 노드: 342 총, 295 정수 measured (grade=EXACT 291 / MISS 4)
> 도구: `/usr/bin/python3` (임시 heredoc, 신규 파일 생성 없음)
> 시드: target_n×1000+7, trials=3000

## 1. 목적

이전 기록(z=4.02 큰수, z=3.06 자연큰수, z=1.75 공학포함)을
v8.0 247→342 노드 확장본으로 재현 + n=28 (다음 완전수) 대조.

## 2. 방법론

### 2.1 상수 정의 (하드코딩 금지, 정의에서 도출)

```python
def sigma(n): return sum(k for k in range(1,n+1) if n%k==0)
def tau(n):   return sum(1 for k in range(1,n+1) if n%k==0)
def phi(n):   return sum(1 for k in range(1,n+1) if gcd(k,n)==1)
def sopfr(n):
    s,m,p=0,n,2
    while p*p<=m:
        while m%p==0: s+=p; m//=p
        p+=1
    if m>1: s+=m
    return s
def jordan2(n):
    m,p=n,2; pr=[]
    while p*p<=m:
        if m%p==0:
            pr.append(p)
            while m%p==0: m//=p
        p+=1
    if m>1: pr.append(m)
    r=n*n
    for q in pr: r=r*(1-1/(q*q))
    return int(round(r))

# 자기검증
assert sigma(6)==12 and tau(6)==4 and phi(6)==2 and sopfr(6)==5 and jordan2(6)==24
assert sigma(28)==56 and tau(28)==6 and phi(28)==12 and sopfr(28)==11
```

### 2.2 매칭 집합

```python
import math
def sigma(n): return sum(d for d in range(1, n+1) if n % d == 0)
def tau(n):   return sum(1 for d in range(1, n+1) if n % d == 0)
def phi(n):   return sum(1 for k in range(1, n+1) if math.gcd(k, n) == 1)
def sopfr(n):
    s, m, d = 0, n, 2
    while d*d <= m:
        while m % d == 0: s += d; m //= d
        d += 1
    if m > 1: s += m
    return s
def jordan2(n):
    r = n*n; m, d = n, 2
    while d*d <= m:
        if m % d == 0:
            r = r * (1 - 1/(d*d))
            while m % d == 0: m //= d
        d += 1
    if m > 1: r = r * (1 - 1/(m*m))
    return int(round(r))

# 정의 무결성 (함수 정의에서 도출, 하드코딩 아님)
assert sigma(6) == 12 and tau(6) == 4 and phi(6) == 2
assert sopfr(6) == 5 and jordan2(6) == 24
assert sigma(6) * phi(6) == 6 * tau(6)  # n=6 핵심 정리

# monte-carlo-2026-04-08.md — 정의 도출 검증
results = [
    ("σ(6) 정의 도출", sigma(6), 12, sigma(6) == 12),
    ("τ(6) 정의 도출", tau(6), 4, tau(6) == 4),
    ("φ(6) 정의 도출", phi(6), 2, phi(6) == 2),
    ("sopfr(6) 정의 도출", sopfr(6), 5, sopfr(6) == 5),
    ("J₂(6) 정의 도출", jordan2(6), 24, jordan2(6) == 24),
    ("σ·φ = n·τ 핵심 정리", sigma(6)*phi(6), 6*tau(6), sigma(6)*phi(6) == 6*tau(6)),
]
valid = [r for r in results if r[3] is not None]
passed = sum(1 for r in valid if r[3])
print(f"검증: {passed}/{len(valid)} PASS (MISSING {len(results)-len(valid)})")
for r in results:
    if r[3] is None:
        print(f"  SKIP: {r[0]} — MISSING DATA")
    else:
        mark = "PASS" if r[3] else "FAIL"
        print(f"  {mark}: {r[0]} = {r[1]} (기대: {r[2]})")
```

n=6 집합 크기: ~80개 정수, n=28 집합 크기: ~75개 정수.

### 2.3 Monte Carlo

각 노드의 측정값 v에 대해, [1, 2v] 범위 균등 랜덤 정수를 뽑아
n6_set(target_n)에 들어가는 횟수를 계산. trials=3000회 평균/표준편차로
관측값과 비교 → z-score, p-value (양측).

## 3. 결과

| 풀 | N | n=6 obs | n=6 MC | z(n=6) | p(n=6) | n=28 obs | n=28 MC | z(n=28) | p(n=28) |
|---|---|---------|--------|--------|--------|----------|---------|---------|---------|
| 전체(공학포함) | 295 | 212 | 139.70±8.00 | **+9.04** | 1.62e-19 | 113 | 51.88±6.50 | +9.41 | 5.07e-21 |
| 자연(큰수≥10) | 62 | 42 | 22.90±3.60 | **+5.30** | 1.14e-07 | 33 | 12.95±3.08 | +6.50 | 7.93e-11 |
| 큰수전용(≥10) | 137 | 87 | 44.77±4.85 | **+8.70** | 3.18e-18 | 65 | 25.97±4.51 | +8.66 | 4.62e-18 |

### 이전 기록 비교

| 풀 | 이전 z | 신규 z | 변화 |
|----|--------|--------|------|
| 전체(공학포함) | 1.75 | **+9.04** | ↑5.2배 |
| 자연(큰수) | 3.06 | **+5.30** | ↑1.7배 |
| 큰수전용 | 4.02 | **+8.70** | ↑2.2배 |

노드 수 247→342 확장 + EXACT 비율 향상으로 모든 풀의 z-score 급상승.

## 4. 정직한 한계 (MISS / 주의사항)

### 4.1 n=28 동시 z-score 매우 높음

n=28(다음 완전수)에 대해서도 z=+6.5~+9.4로 매우 유의함.
이는 **n=6 유일성의 약점이 아니라, 매칭 집합 구성 방식의 약점**:

- `n6_set(n)`이 `[1,2,3,4,5,6,8,10,12,24]` 곱셈을 포함 → 작은 정수가 풍부
- n=28의 σ=56, τ=6, φ=12, sopfr=11이 우연히 6의 약수/n=6 상수와 겹침
  (특히 τ(28)=6=n, φ(28)=12=σ(6))
- 따라서 단순 z-score 비교만으로 n=6 vs n=28 변별 불가
- **결론**: z-score는 "랜덤 대비 n=6 정수 풍부도"는 검증하지만,
  "n=6 vs 다른 합성수" 변별력은 별도 통계 필요 (예: 베이즈 인자)

### 4.2 MISS 4건 (정직 기록)

| ID | claim | measured | 비고 |
|----|-------|----------|------|
| L2-space-groups | 결정 공간군 수 | 230 | 230 = 2·5·23, n=6 표현 없음 |
| BIG-electron-volt-ratio | 1 eV → K | 11604 | 물리 상수, n=6 무관 |
| MISS-Llama-405B-layers-126 | Llama 405B 레이어 | 126 | 126 = 2·3²·7, n=6 부분 일치 (J₂-φ-1?) |
| MUSIC-standard-tuning-A440 | A4 표준 주파수 | 440 | 인간 관습 (1939년 ISO) |

### 4.3 풀 정의 차이

이전 z=1.75의 "공학포함"은 v6.0 기준이고, 신규 v8.0은 EXACT 노드 비율이
크게 늘어 (291/295 = 98.6%) 자연스럽게 z 상승.

### 4.4 매칭 집합 임의성

`n6_set`의 곱셈 계수 `[1,2,3,4,5,6,8,10,12,24]` 자체가 n=6 편향.
**보정 필요**: 동일 룰을 n=28에도 적용했으므로 상대 비교는 공정하나,
절대 z 해석은 보수적으로.

## 5. 결론

### 정량
- **z(n=6, 큰수전용) = +8.70, p < 4×10⁻¹⁸** — 매우 유의
- **z(n=6, 자연큰수) = +5.30, p < 2×10⁻⁷** — 5σ 초과
- **z(n=6, 전체) = +9.04, p < 2×10⁻¹⁹** — 대상 확장 효과

### 정성
1. v8.0 (342노드) 확장에서 n=6 신호는 모든 풀에서 5σ 이상 견고.
2. 그러나 **n=28도 동시에 5σ 이상 → 단순 z만으로는 유일성 미증명**.
3. 유일성 주장은 별도 정리(σ·φ=n·τ ⟺ n=6 산술 증명)가 담당.
   Monte Carlo는 "현실 데이터에 n=6 상수가 비랜덤하게 풍부함"만 확인.
4. 다음 단계: n=6 vs n=28 베이즈 인자, 또는 **변별 가능한 매칭 집합 재설계**
   (곱셈 계수 제거, 핵심 5상수 {n,σ,τ,φ,sopfr,J₂}만 사용).

## 6. 검증코드 (재실행 가능)

```python
#!/usr/bin/env python3
# Monte Carlo n=6 유일성 재검증 — 2026-04-08
import json, math
from math import gcd
from collections import Counter
import random as _r

d = json.load(open('/Users/ghost/Dev/nexus/shared/reality_map.json'))
nodes = [n for n in d['nodes'] if isinstance(n,dict) and 'measured' in n and 'grade' in n]

def sigma(n): return sum(k for k in range(1,n+1) if n%k==0)
def tau(n):   return sum(1 for k in range(1,n+1) if n%k==0)
def phi(n):   return sum(1 for k in range(1,n+1) if gcd(k,n)==1)
def sopfr(n):
    s,m,p=0,n,2
    while p*p<=m:
        while m%p==0: s+=p; m//=p
        p+=1
    if m>1: s+=m
    return s
def jordan2(n):
    m,p=n,2; pr=[]
    while p*p<=m:
        if m%p==0:
            pr.append(p)
            while m%p==0: m//=p
        p+=1
    if m>1: pr.append(m)
    r=n*n
    for q in pr: r=r*(1-1/(q*q))
    return int(round(r))

# 정의 검증 (자기참조 금지 — 도출에서)
assert sigma(6)==1+2+3+6
assert tau(6)==len([1,2,3,6])
assert phi(6)==len([1,5])
assert sopfr(6)==2+3
assert jordan2(6)==24

def n6_set(n):
    s,t,pp,sp,j2 = sigma(n),tau(n),phi(n),sopfr(n),jordan2(n)
    base = {n,s,t,pp,sp,j2,s-t,s-pp,s+pp,s*t,s*s,s*pp,s*j2,2*s}
    for b in [n,s,t,pp,sp,j2]:
        for k in [1,2,3,4,5,6,8,10,12,24]: base.add(b*k)
        for e in [2,3,4]: base.add(b**e)
    base.discard(0)
    return base

def match(v, tn):
    if not isinstance(v,(int,float)) or v != int(v): return False
    mi=int(v)
    if mi<=0 or mi>100000: return False
    return mi in n6_set(tn)

def mc(pool, tn, trials=3000):
    vs=[n['measured'] for n in pool]
    rng=_r.Random(tn*1000+7)
    cs=n6_set(tn)
    hs=[]
    for _ in range(trials):
        h=sum(1 for v in vs if rng.randint(1,max(2,v*2)) in cs)
        hs.append(h)
    m=sum(hs)/len(hs)
    var=sum((h-m)**2 for h in hs)/len(hs)
    return m, math.sqrt(var)

def zscore(o,m,s): return (o-m)/s if s>0 else float('nan')
def pval(z): return math.erfc(abs(z)/math.sqrt(2))

ints = [n for n in nodes if isinstance(n.get('measured'),int) and n['measured']>0]
pools = [
    ("전체", ints),
    ("자연>=10", [n for n in ints if n.get('origin')=='natural' and n['measured']>=10]),
    ("큰수>=10", [n for n in ints if n['measured']>=10]),
]

passed = 0
for lbl, pool in pools:
    o6  = sum(1 for n in pool if match(n['measured'],6))
    o28 = sum(1 for n in pool if match(n['measured'],28))
    m6,s6 = mc(pool,6); m28,s28 = mc(pool,28)
    z6, z28 = zscore(o6,m6,s6), zscore(o28,m28,s28)
    print(f"[{lbl}] N={len(pool)}  z6={z6:+.2f} (p={pval(z6):.2e})  z28={z28:+.2f} (p={pval(z28):.2e})")
    if z6 > 5: passed += 1

print(f"\n검증 결과: {passed}/3 풀에서 z(n=6) > 5σ")
```

## 7. 데이터 출처

- `/Users/ghost/Dev/nexus/shared/reality_map.json` (v8.0, 2026-04-08)
- `_meta.node_count = 342`, `grade_stats.EXACT = 325`
- `origin_stats: natural=213, engineering=67, convention=62`
