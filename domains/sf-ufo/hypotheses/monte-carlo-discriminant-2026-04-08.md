# 변별성 강화 Monte Carlo — 핵심 5상수 매칭집합

- 일자: 2026-04-08
- 데이터: `~/Dev/nexus/shared/reality_map.json` v8.0 (342 노드)
- 표본: `origin == "natural"` 노드만 사용 → 213개, 그 중 정수 measured = **177개**
- 시드: 20260408, 시행 횟수: 200,000

## 1. 동기

이전 Monte Carlo에서 z=9.04로 강했지만, 매칭집합이 `[1..24]`에 곱셈계수까지 포함해 너무 풍부했고
n=28 대조도 z=6.5~9.4로 나와 **변별력이 거의 없었다**. 본 실험은 매칭집합을 핵심 5상수로 좁혀 변별력을 회복할 수 있는지 정직하게 측정한다.

## 2. 매칭집합 (정의에서 도출, 하드코딩 없음)

각 후보 n에 대해 5개 상수만 사용: `{σ(n), τ(n), φ(n), sopfr(n), J₂(n)}`.
공학/관례 노드(67+62=129개)는 인간 설계 편향을 피하기 위해 제외.

| n | σ | τ | φ | sopfr | J₂ | 매칭집합 |
|---|---|---|---|-------|----|--------|
| 6 | 12 | 4 | 2 | 5 | 24 | {2,4,5,12,24} |
| 12 | 28 | 6 | 4 | 7 | 96 | {4,6,7,28,96} |
| 28 | 56 | 6 | 12 | 11 | 576 | {6,11,12,56,576} |
| 496 | 992 | 10 | 240 | 39 | 184320 | {10,39,240,992,184320} |

n=12는 반완전수, n=6/28/496은 완전수.

## 3. 결과

### 3.1 관측 적중률 (177 자연 정수 노드)

| n | 적중 | 비율 |
|---|------|------|
| **6** | **73** | **41.2%** |
| 12 | 70 | 39.5% |
| 28 | 51 | 28.8% |
| 496 | 4 | 2.3% |

### 3.2 귀무가설 vs 관측 (random size-5 set from [1..100])

| n | μ_null | σ_null | z | p(≥obs) |
|---|--------|--------|---|---------|
| **6** | 8.23 | 11.32 | **5.72** | 0.00028 |
| 12 | 8.26 | 11.35 | 5.44 | 0.00036 |
| 28 | 8.23 | 11.32 | 3.78 | 0.00581 |
| 496 | 8.26 | 11.36 | -0.38 | 0.46353 |

### 3.3 베이즈 인자

`BF(n vs random) = 1 / p_ge(n)`. 쌍별 BF는 두 BF의 비율.

| 가설 | BF vs random |
|------|-------------|
| n=6 | **3571** |
| n=12 | 2817 |
| n=28 | 172 |
| n=496 | 2.16 |

| 쌍 | BF(n=6 vs other) |
|----|------------------|
| n=6 vs n=12 | **1.27** (사실상 무차별) |
| n=6 vs n=28 | 20.75 (강한 선호) |
| n=6 vs n=496 | 1655 (압도적) |

## 4. 결론 — 정직 보고

1. **변별 강화 부분 성공**: 이전 실험에서 사실상 동등했던 n=28을 z=5.72 vs z=3.78, BF=20.75로
   유의하게 분리하는 데 성공했다.
2. **n=12 변별 실패**: n=6과 n=12는 BF=1.27로 통계적 무차별. 이유는 매칭집합이 겹치는 원소(`{4}`)와
   n=12의 자기 진약수가 매우 흔한 작은 정수({4,6}) 때문이다. 5상수 좁히기로는 한계가 있고,
   완전수 조건만으로는 반완전수를 배제할 수 없음을 다시 확인.
3. **n=496 압도**: 5상수 중 4개가 100을 넘는 큰 수라 자연 노드와 거의 안 맞는다. 완전수라도
   "작은 수에서의 풍부함"이라는 별도 성질이 필요함을 시사.
4. **현실 지도 자체의 의미**: random null 대비 n=6의 BF≈3571은 "지도 큐레이션 편향"을 부분 반영할
   가능성이 있다. 향후 대조군: 출처 당 1노드 캡, 반독립 표본 추출.

### 후속 작업 제안
- n=6 vs n=12 분리: 매칭집합에 `{n자체}` 또는 `{σ-φ, σ-τ}` 같은 결합 상수를 추가했을 때
  편향 없이 분리되는지 검증 (사전 등록 필요).
- 출처 다중 노드 디바이아싱 후 재측정.

## 5. 검증코드 (정의에서 도출)

```python
# 검증코드 — monte-carlo-discriminant-2026-04-08.md
import json, random, math
import numpy as np

def divisors(n): return [k for k in range(1,n+1) if n%k==0]
def sigma(n): return sum(divisors(n))
def tau(n): return len(divisors(n))
def phi(n): return sum(1 for k in range(1,n+1) if math.gcd(k,n)==1)
def sopfr(n):
    s,m,p=0,n,2
    while p*p<=m:
        while m%p==0: s+=p; m//=p
        p+=1
    if m>1: s+=m
    return s
def jordan2(n):
    r=n*n; m=n; ps=set(); p=2
    while p*p<=m:
        if m%p==0:
            ps.add(p)
            while m%p==0: m//=p
        p+=1
    if m>1: ps.add(m)
    for q in ps: r=r*(q*q-1)//(q*q)
    return r

# 정의에서 직접 도출된 상수 검증
assert sigma(6)==12 and tau(6)==4 and phi(6)==2 and sopfr(6)==5 and jordan2(6)==24
assert sigma(28)==56 and tau(28)==6 and phi(28)==12 and sopfr(28)==11 and jordan2(28)==576
assert sigma(496)==992 and tau(496)==10 and phi(496)==240 and sopfr(496)==2+2+2+2+31==39

def strict_set(n):
    return {sigma(n), tau(n), phi(n), sopfr(n), jordan2(n)}

d = json.load(open('/Users/ghost/Dev/nexus/shared/reality_map.json'))
nodes = [x for x in d['nodes'] if '_comment' not in x and x.get('origin')=='natural']
vals = []
for x in nodes:
    m = x.get('measured')
    if isinstance(m,int) and m>0: vals.append(m)
    elif isinstance(m,float) and m==int(m) and m>0: vals.append(int(m))

random.seed(20260408)
TRIALS = 200000
results = {}
for n in [6,12,28,496]:
    S = strict_set(n)
    obs = sum(1 for v in vals if v in S)
    null = np.array([sum(1 for v in vals if v in set(random.sample(range(1,101), len(S)))) for _ in range(TRIALS)])
    p = (null>=obs).sum()/TRIALS
    z = (obs-null.mean())/null.std()
    results[n] = (obs, z, p)
    print(f"n={n}: obs={obs}, z={z:.2f}, p={p:.5f}, BF={1/p if p>0 else float('inf'):.1f}")

# 쌍별 BF
bf = {n: 1/results[n][2] if results[n][2]>0 else float('inf') for n in results}
for n in [12,28,496]:
    print(f"BF(6 vs {n}) = {bf[6]/bf[n]:.3f}")

print("PASS: 정의 기반 검증 완료")
```
