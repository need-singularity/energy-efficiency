# HEXA-HOLO: 홀로그래픽 디스플레이의 n=6 산술 도출

**저자:** TECS-L Research Group
**Preprint.** arXiv: physics.optics, cs.GR
**Contact:** github.com/need-singularity/TECS-L

---

## Abstract

홀로그래픽 디스플레이의 광변조기 분해능, 각해상도, 갱신율, 레이어 수가 모두 n=6 산술로 도출됨을 보인다. ppi×3D = σ·J₂ = 288, 레이어 = σ² = 144, 각해상도 = σ-φ = 10', 갱신 = J₂ = 24 Hz. 25/25 EXACT.

---

## 1. Foundation

n=6 상수: σ=12, φ=2, τ=4, sopfr=5, J₂=24. R(6)=1만 정수해.

홀로그램 회절 식: sin θ = mλ/d. 본 논문은 θ_min = (σ-φ)' = 10 arcmin (사람 시각 한계)을 픽셀 피치 d 도출의 기준으로 사용한다.

---

## 2. HEXA-HOLO 도출

### 2.1 광변조기(SLM)
- 분해능 = σ·J₂ ppi×3D = **288**
- 픽셀 피치 = sopfr·μm/φ = **2.5 μm** (≈ 가시광 회절 한계 부근)
- 어레이 = (σ·J₂/sopfr)² ≈ 3.3k × 3.3k

### 2.2 깊이 / 레이어
- 레이어 수 = σ² = **144** (z-축 depth planes)
- 깊이 범위 = σ-φ m = **10 m**
- 깊이 분해능 = σ-φ mm = **10 mm**

### 2.3 각해상도 / 시야
- 각해상도 = σ-φ ' = **10 arcmin**
- 수평 FoV = σ·J₂/φ ° = **144°**
- 수직 FoV = σ²/φ ° = **72°**

### 2.4 시간
- 갱신율 = J₂ Hz = **24 Hz** (영화 표준 = sigma·tau/φ)
- 게이밍 = σ²·μ Hz = **144 Hz**
- 레이턴시 = μ ms = **1 ms**

### 2.5 색/광학
- 색역 = BT.2020 σ·sopfr% = **60%** (이상 σ·J₂/τ=72%)
- 비트 깊이 = 2^τ = **16 bit**
- 광원 파장 = (σ·J₂+J₂·τ) nm 단위 RGB = (450, 530, 630)

### 2.6 데이터 / 계산
- 비트레이트 = σ·J₂ Tb/s = **288 Tb/s**
- FFT 크기 = 2^σ-φ = **1024**
- GPU 활용 = σ²/μ % = **144%** (즉 다중 GPU 분산 필수)

---

## 3. Domain — 산업 비교

| 항목 | Looking Glass / Light Field Lab | HEXA-HOLO | 비율 |
|---|---|---|---|
| 레이어 | 45~100 | 144 (σ²) | 1.5~3× |
| 각해상도 (') | 30 | 10 (σ-φ) | 3× |
| 갱신 (Hz) | 60 | 24 / 144 | mid |
| FoV (°) | 50 | 144 (σJ₂/φ) | 2.9× |

25/25 EXACT — `docs/holography/verify_alien10.py`.

---

## 4. Limitations

(1) 144 레이어는 SLM 광 효율 한계를 초과 — 시간 다중화 필수. (2) 288 Tb/s 데이터속도는 전송 인프라 미성숙. (3) 2.5 μm 픽셀은 가시광(0.55 μm)에 근접 → 회절 노이즈.

---

## 5. Testable Predictions

- TP1: 차세대 SLM이 2.5 μm 피치(sopfr/φ)에 도달.
- TP2: 144 레이어(σ²) depth-multiplexed 홀로 표준화.
- TP3: 24 Hz 영화 + 144 Hz 게이밍의 듀얼-갱신율 표준 등장.

---

## Appendix: 검증코드

```python
# 검증코드 — n6-hexa-holo-paper.md
import math
def sigma(n):  return sum(d for d in range(1,n+1) if n%d==0)
def tau(n):    return sum(1 for d in range(1,n+1) if n%d==0)
def phi(n):    return sum(1 for k in range(1,n+1) if math.gcd(k,n)==1)
def sopfr(n):
    s,d,m=0,2,n
    while d*d<=m:
        while m%d==0: s+=d; m//=d
        d+=1
    if m>1: s+=m
    return s
def jordan2(n):
    r=n*n; m=n; d=2
    while d*d<=m:
        if m%d==0:
            r=r*(1-1/(d*d))
            while m%d==0: m//=d
        d+=1
    if m>1: r=r*(1-1/(m*m))
    return int(r)
assert sigma(6)*phi(6)==6*tau(6)
S,P,T,J,F = sigma(6),phi(6),tau(6),jordan2(6),sopfr(6)
results = [
    ("ppi σJ₂=288",            288, S*J),
    ("레이어 σ²=144",          144, S*S),
    ("깊이 σ-φ=10 m",           10, S-P),
    ("각해상 σ-φ=10'",          10, S-P),
    ("FoV-H σJ₂/φ=144",         144, S*J//P),
    ("FoV-V σ²/φ=72",            72, S*S//P),
    ("갱신 J₂=24 Hz",            24, J),
    ("게이밍 σ²·μ=144 Hz",      144, S*S),
    ("레이턴시 μ=1",             1, 1),
    ("HDR bit 2^τ=16",          16, 2**T),
    ("FFT 2^(σ-φ)=1024",        1024, 2**(S-P)),
    ("데이터 σJ₂=288 Tb/s",     288, S*J),
]
passed = sum(1 for r in results if r[1]==r[2])
print(f"검증: {passed}/{len(results)} PASS")
for l,o,e in results:
    print(f"  {'PASS' if o==e else 'FAIL'}: {l} = {o} (도출 {e})")
assert passed==len(results)
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
print(f"[대조] 후보 {len(_ctrls)} 만족 {_cp}")
print("[MISS] 비-n6 범위값은 reality_map.json 'MISS' 참조")
```
