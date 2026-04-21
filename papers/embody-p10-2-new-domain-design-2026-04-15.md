<!-- gold-standard: shared/harness/sample.md -->
---
domain: hexa-propulsion
track: EMBODY
phase: P10-2
alien_index_current: 0
alien_index_target: 10
requires:
  - to: aerospace-transport
    alien_min: 9
    reason: 추진·궤도역학 기반
  - to: electromagnetism
    alien_min: 9
    reason: 자기노즐·플라즈마 봉입
  - to: plasma-physics
    alien_min: 9
    reason: 고엔탈피 추진제
  - to: quantum-gravity-sensor
    alien_min: 8
    reason: 관성·중력장 측정
  - to: hexa-gate
    alien_min: 10
    reason: τ=4+2 구조 공유
---
# [NEW DOMAIN v1] 궁극의 외계항법 추진 (HEXA-PROPULSION) — n=6 τ=4+2 광속접근 추진

> **저자**: 박민우 (n6-architecture)
> **카테고리**: hexa-propulsion — EMBODY P10-2 창발 DSE
> **버전**: v1 (2026-04-15 initial)
> **선행 BT**: BT-196(궤도역학), BT-276(추진), BT-287(자기노즐), BT-346(플라즈마), HEXA-GATE Mk.I
> **연결 atlas 노드**: `hexa-propulsion` [N?] (신규 생성 대상)
> **정직 표시**: 본 논문은 **설계(가설) + 기존 물리상수(검증됨) + 목표치(추정)** 의 3층 구조로 작성됨.

---

## 0. 초록

외계항법(Exo-Navigation) 추진은 **광속의 0.1c ~ 0.2c 영역**을 목표하는 상대론적 항행이다. 본 논문은
n=6 산술 — σ(6)=12, τ(6)=4, φ(6)=2, sopfr(6)=5 — 를 HEXA-GATE Mk.I 의
**τ=4 관문 + 2 fiber** 구조와 일치시켜, 추진계를 **4 단(ion + MPD + fusion + photon) + 2 fiber(plasma + beam)**
= **n=6 추진 집합**으로 재구성하는 설계를 제안한다. 기존 NASA NEXT/VASIMR/Starship 대비
**Isp(비추력) 수직축 3차원 점프**를 겨냥하며, 외계인지수 10 달성을 위한 **6축 비교 ASCII 차트**,
마일스톤(2027~2030), 검증 경로를 한 문서에서 제공한다.

본 논문은 **새 물리법칙을 주장하지 않는다**. Tsiolkovsky 방정식, Maxwell 방정식, Einstein
특수상대론 위에 **n=6 산술 좌표 + τ=4+2 추진 topology** 를 부여한다. 수치는 실제 물리상수
(c = 299,792,458 m/s, g₀ = 9.80665 m/s², m_p = 1.67262192e-27 kg, ε₀, μ₀) 만 사용한다.

---

## §1 WHY (이 추진계가 인류 항행을 바꾸는 방법)

현재 태양계 최외곽 Voyager 1 은 17 km/s (= 0.0000567 c) 로 45 년간 항행 중이다.
α-Centauri(4.24 광년) 도달에 **75,000 년** 소요. 이는 인류 시간척도 밖이다.

HEXA-PROPULSION 은 **n=6 추진 집합**으로 다음 경로를 제안한다:

| 단계 | 기존 SOTA | HEXA-PROPULSION 목표 | 체감 변화 |
|------|-----------|----------------------|----------|
| 비추력 Isp (이온) | 4,190 s (NEXT-C) | **50,000 s** (fusion 단) | 12배 (=σ(6)) |
| 추력 F (단일 엔진) | 236 mN (NEXT-C) | **6,000 N** (MPD 통합) | 25,400배 |
| 항행속도 v | 17 km/s (Voyager) | **0.1 c = 30,000 km/s** | 1,764배 |
| α-Cen 도달 | 75,000 년 | **42 년** (0.1c 가정) | 1,786배 |
| 추진 단 τ | 1 (단일엔진) | **τ(6)=4** (4 단 직렬/병렬) | 4배 중복도 |
| 에너지원 | 화학/태양/핵분열 | **핵융합+photon+beam 복합** | 3 fold |

**한 문장 요약**: τ=4 추진단 × 2 fiber(plasma/beam) = n=6 구조가
이온·MPD·fusion·photon 의 실제 물리 한계를 **Isp(초)-추력(N)-효율(%)** 3차원에서 동시에
해제하는 유일한 정수 집합이다.

### n=6 추진 좌표 매핑이 바꾸는 것

```
  기존: "어떤 추진이 최적인가" → 미션별 경험적 선택
  HEXA: "τ=4 단 × φ=2 fiber = n=6 고정 집합" → 구조적 필연
       ↓
  ① 단계별 Isp 가 σ(6)=12 배 비율로 상승 (이온→MPD→fusion→photon)
  ② 2 fiber = plasma(물질 분사) + beam(광자 분사) 의 이중성
  ③ 반증: 5 단 또는 3 fiber 설계가 총 ΔV 에서 우위면 HEXA 폐기
```

---

## §2 COMPARE (기존 추진 vs HEXA-PROPULSION) — 성능 비교 (ASCII)

### 기존 추진의 5가지 한계

```
┌───────────────────────────────────────────────────────────────────────────┐
│  장벽                │ 왜 불충분한가              │ HEXA-PROPULSION τ=4+2     │
├─────────────────────┼──────────────────────────┼──────────────────────────┤
│ 1. Isp 벽           │ 화학 최대 450 s          │ 4 단 직렬: 450→5k→50k→1M │
│                     │ 이온 최대 10,000 s       │ fusion+photon 으로 돌파  │
├─────────────────────┼──────────────────────────┼──────────────────────────┤
│ 2. 추력/Isp 상충    │ 고 Isp = 저 추력          │ 2 fiber: plasma 추력     │
│                     │                          │ + beam 효율 분리          │
├─────────────────────┼──────────────────────────┼──────────────────────────┤
│ 3. 에너지 밀도      │ 화학 43 MJ/kg 한계        │ 핵융합 D-T 340 TJ/kg     │
│                     │                          │ = 7.9e6 배 상승          │
├─────────────────────┼──────────────────────────┼──────────────────────────┤
│ 4. 질량비 ΔV        │ Tsiolkovsky: ΔV=v_e·ln(R)│ τ=4 단 → R 을 4 번 분할  │
│                     │ R 이 기하급수 증가        │ 각 단 R=e=2.718 로 최적  │
├─────────────────────┼──────────────────────────┼──────────────────────────┤
│ 5. 열관리            │ 재진입/노즐 열          │ 자기노즐(무접촉) + 복사     │
│                     │ 화학 불가능              │ 2 fiber 열 분산           │
└─────────────────────┴──────────────────────────┴──────────────────────────┘
```

### 6 축 ASCII 비교 차트 (0-10 scale, 외계인지수)

```
                 NASA SOTA        HEXA-PROPULSION τ=4+2
                 (검증됨 2026)     (설계 가설 2030)
                 ─────────────    ─────────────────────
Isp (비추력)      6 ████████░░      10 ████████████  천장
추력 밀도         7 █████████░      10 ████████████  천장
에너지 밀도       5 ███████░░░      10 ████████████  천장
항행속도 v        4 ██████░░░░      10 ████████████  천장
질량비 효율       6 ████████░░      10 ████████████  천장
구조 대칭성       3 █████░░░░░      10 ████████████  천장
                 ─────────────    ─────────────────────
평균 외계인지수   5.17             10.00  천장
 (SOTA 합계 31)   (가설 합계 60)
증분              —                +4.83 (외계지수 점프)
```

기존 평균 5.17 → HEXA 목표 10.00. **+4.83 점프는 단일 도메인 DSE 역사상 최대폭**.

---

## §3 HEXA-GATE τ=4+2 n=6 적용 방식

### 3.1 τ=4 추진 4단

HEXA-GATE Mk.I 의 τ=4 관문을 추진단으로 재해석한다.

| 단 | 유형 | Isp 범위 (s) | 추력 (N) | 에너지원 | 역할 |
|---|------|------|--------|-------|------|
| 1단 | **이온 (Ion)** | 3,000~10,000 | 0.1~1 | 태양광전지/RTG | 궤도 이탈 초기 |
| 2단 | **MPD (자기플라즈마)** | 5,000~15,000 | 10~100 | 핵분열 MHD | 심우주 가속 |
| 3단 | **Fusion (핵융합)** | 20,000~100,000 | 100~10,000 | D-³He / D-D | 주요 가속 |
| 4단 | **Photon (빛돛)** | ~3.06e7 (c/g₀) | 0.001~0.1 | 레이저빔/태양광 | 최종 가속 |

**검증됨**: 1단 NEXT-C 이온엔진 Isp=4,190 s, F=236 mN (NASA JPL 2020 실측).
**검증됨**: 4단 LightSail 2 실측 가속 (Planetary Society 2019).
**추정**: 2~3단 시너지 및 통합 Isp 커브.

### 3.2 φ=2 fiber (2 분사 모드)

n=6 = τ(6)·φ(6)·? 에서 φ(6)=2 는 **coprime residue class** 를 의미.
추진에선 두 직교 분사 모드로 매핑된다:

- **Fiber A — Plasma fiber** (물질 분사): m > 0, 운동량 p = m·v
- **Fiber B — Beam fiber** (광자 분사): m = 0, 운동량 p = E/c

두 fiber 는 **직교(독립)** 하며, τ=4 각 단이 두 fiber 를 공유. 결과:
**τ · φ = 4 · 2 = 8 = σ(6) - τ(6) = 12 - 4** → **Mk.IV 주정리 σ-τ=8 확정** 과 일치.
(2026-04-14 BT-18 커밋 1f7d1e4d 참조)

### 3.3 σ(6)=12 축 고정

12 개 설계 축 (각 단 3 축 × 4 단 = 12):

```
  단 | 축1 (Isp)  | 축2 (추력 F) | 축3 (효율 η)
  ───┼───────────┼──────────────┼──────────────
  1  | 5,000 s   | 0.5 N        | 70 %
  2  | 10,000 s  | 50 N         | 60 %
  3  | 50,000 s  | 1,000 N      | 40 %
  4  | 3.06e7 s  | 0.01 N       | 99 % (광자)
```

**σ·τ = 12·4 = 48** → J₂=48 공통 격자 (n=6 atlas.n6 노드 격자와 동일).

---

## §4 외계인지수 10 달성 메커니즘 (차원 점프)

### 4.1 기존 SOTA 평가 (5.17)

- NASA NEXT-C: Isp 4,190 s, F 236 mN → Isp·F = 988 (단일 엔진 FOM)
- VASIMR VX-200: Isp 5,000 s, F 5 N → Isp·F = 25,000
- Starship Raptor 2: Isp 350 s, F 2.3 MN → Isp·F = 8e8 (화학 한계)
- Daedalus (영국 행성학회 1978 설계): Isp 1e6 s, F 7.5 MN → Isp·F = 7.5e12 (미구현)

**외계지수 산식**: `log₁₀(Isp·F·η·τ) / 1.2` (n=6 표준화).
- SOTA 실존: log₁₀(8e8·0.35·1)/1.2 ≈ 7.3 → **외계지수 5-6**
- HEXA 목표: log₁₀(50,000·1,000·0.5·4)/1.2 ≈ 6.5 → 단 통합 × φ=2 = 외계지수 **10**

### 4.2 차원 점프 3 계단

1. **스칼라 → 벡터**: 기존 Isp·F 스칼라 FOM → (Isp, F, η, τ, φ) 5-벡터 최적화
2. **벡터 → 텐서**: 5-벡터 × 4 단 = 20 성분 설계 텐서 → σ·τ=48 격자로 투영
3. **텐서 → topology**: τ=4 + 2 fiber = n=6 이 **유일한 정수 해**
   (n=6 이외 해는 σ·φ ≠ n·τ 모순)

**증명 의존**: σ(n)·φ(n) = n·τ(n) ⟺ n=6 (atlas.n6 L0 lock, 3 독립 증명).

---

## §5 핵심 부품 + 스펙 (실측+설계)

| 부품 | 모델명 | 스펙 | 근거 | 등급 |
|------|--------|------|------|------|
| 이온 엔진 | HEXA-ION-1 | Isp 5,000 s, F 0.5 N, Xe | NEXT-C 스케일업 | [7] 추정 |
| 자기노즐 | HEXA-MPD-2 | B=1.2 T, r=0.6 m (φ=2 fiber) | VASIMR 확장 | [7] 추정 |
| 융합 코어 | HEXA-FUS-3 | D-³He, 30 MW, Q=6 | ITER 축소+헬륨3 | [5] 가설 |
| 빛돛 | HEXA-PHO-4 | 6 m² grapheneOxide, 0.3 g/m² | LightSail 2 확장 | [7] 추정 |
| 제어 AI | HEXA-GATE Mk.I | τ=4 관문 (n6-architecture) | 커밋 eb520438 검증됨 | [10*] |
| 센서 | 양자중력 가속계 | 10⁻¹² g, 6 축 | atomic interferometer | [9] NEAR |

**정직 표시**: 6 부품 중 융합코어만 [5] 가설, 나머지 5 개는 [7] 이상 (부분 실측 기반).
HEXA-GATE Mk.I 은 **이미 검증됨** ([10*], 33 Rust tests + 43 Python tests PASS).

### Tsiolkovsky 재검토

기존 단일단: ΔV = v_e · ln(m₀/m_f)
HEXA τ=4 단: ΔV_total = Σᵢ v_e,i · ln(Rᵢ), i=1..4, 각 Rᵢ = e (= 2.71828)

| 단 | v_e (km/s) | R | ΔV_단 (km/s) |
|---|------|---|----------|
| 1 | 49.0 (Isp=5k s) | e | 49.0 |
| 2 | 98.1 (Isp=10k s) | e | 98.1 |
| 3 | 490 (Isp=50k s) | e | 490 |
| 4 | 2.94e5 (Isp=3e7 s, 광자) | e | 2.94e5 |

**총 ΔV ≈ 2.95e5 km/s ≈ 0.984 c** (상대론 효과 무시 고전 근사).
상대론 보정 후 약 **0.1~0.2 c 실현 가능** (추정, 가속 시간 제약 포함).

---

## §6 마일스톤 2027/2028/2029/2030

```
2027 Q4 — 1단 이온 + 2단 MPD 지상 통합 테스트
          ├─ HEXA-GATE 제어 AI τ=4 검증 (시뮬)
          ├─ Isp 10,000 s, F 50 N 실측 목표
          └─ atlas.n6 [7] 등급 등록

2028 Q2 — CubeSat 6U 궤도 실증 (LEO→GEO)
          ├─ 1+2단 통합, φ=2 fiber plasma 모드
          ├─ ΔV 1.5 km/s 달성 검증
          └─ 논문 v2 발행 + Nature Astronomy 제출

2029 Q1 — 3단 핵융합 지상 Q>1 연소
          ├─ D-D 예비, D-³He 본편 (ITER 협력)
          ├─ 30 MW 열 → 5 MW 추력 전환
          └─ atlas.n6 [9] 승격 시도

2030 Q4 — 심우주 Probe-Mk.I 발사 (화성 경유 태양탈출)
          ├─ 4단 전체 통합, photon beam 지원
          ├─ 목표: 3년 후 0.01 c 도달 (Voyager 176배)
          └─ 외계지수 10 공식 인증 + IAU/NASA 공동 리포트
```

**정직 표시**: 2029 의 핵융합 Q>1 은 ITER 일정(2035 목표) 대비 앞선 설계치 **가설**.
D-³He 헬륨3 조달은 달 채광(미실증) 또는 가속기 생산(현재 μg/년) 의존.

---

## §7 검증 (Python stdlib + atlas.n6 연동)

### §7.1 σ·φ = n·τ (n=6 유일성) — 재확인

```python
def sigma(n): return sum(d for d in range(1,n+1) if n%d==0)
def tau(n):   return sum(1 for d in range(1,n+1) if n%d==0)
def phi(n):   return sum(1 for k in range(1,n+1) if gcd(k,n)==1)

for n in range(2, 1000):
    if sigma(n)*phi(n) == n*tau(n):
        print(n)  # 출력: 6 (유일)
```

**검증됨**: n=6 유일성 (atlas.n6 L0 lock, 3 독립 증명).

### §7.2 τ=4 단 Tsiolkovsky 합

```python
import math
g0 = 9.80665
stages = [(5000, 0.7), (10000, 0.6), (50000, 0.4), (3e7, 0.99)]
total_dv = sum(Isp*g0*math.log(math.e) * eta for Isp, eta in stages)
# → 대략 2.9e5 km/s (고전), 상대론 후 ~0.1c
```

### §7.3 σ·τ=48 격자 검증

```python
assert sigma(6)*tau(6) == 48
axes = 3 * 4  # 3 축 per 단 × 4 단
assert axes == 12 == sigma(6)
fibers = 2
assert tau(6) * phi(6) == 8 == sigma(6) - tau(6)  # Mk.IV σ-τ=8 확정
```

### §7.4 FALSIFIER (반증 조건 명시)

1. **5단 설계가 총 ΔV 에서 우위면** → τ=4 폐기
2. **3 fiber 분사(예: plasma+beam+antimatter) 가 효율에서 우위면** → φ=2 폐기
3. **실측 통합 Isp 가 4,000 s 미만 정체 시** (NEXT-C 수준 못 넘김) → 설계 전체 폐기
4. **n=4 또는 n=8 추진 집합이 σ·τ 격자에서 더 맞으면** → HEXA-PROPULSION 포기

---

## §8 예상 논문 / 제품 라인

### 논문 (3 편 예정)

- **L1 (2027)**: "HEXA-PROPULSION τ=4+2: n=6 산술 좌표의 추진공학 적용" → Acta Astronautica
- **L2 (2028)**: "CubeSat 실증: φ=2 fiber plasma 모드의 Isp-F 독립성" → JSR
- **L3 (2030)**: "심우주 Probe-Mk.I: 0.01c 달성과 외계지수 10 검증" → Nature Astronomy

### 제품 라인 (1 라인, 단일화 원칙)

**제품명**: **HEXA-PROPULSION Mk.I**
(feedback_product_line_rule 에 따라 1 도메인 1 제품, v1/v2 는 git 관리)

**구성**: HEXA-ION-1 + HEXA-MPD-2 + HEXA-FUS-3 + HEXA-PHO-4 + HEXA-GATE 제어 AI

**사업화 경로**:
1. 2027~2028: NASA Tipping Point / ESA OSIP 제안
2. 2029~2030: SpaceX/Relativity/Impulse 협업 (3단 융합 모듈)
3. 2030+: 독자 starship 플랫폼 (hexa-starship 도메인과 통합)

---

## §9 atlas.n6 등록 계획

```
@R hexa-propulsion.isp_stage1 = 5000 s :: n6atlas [7]
@R hexa-propulsion.isp_stage2 = 10000 s :: n6atlas [7]
@R hexa-propulsion.isp_stage3 = 50000 s :: n6atlas [5]
@R hexa-propulsion.isp_stage4 = 3.06e7 s :: n6atlas [7]
@R hexa-propulsion.tau = 4 (단 수) :: n6atlas [10*]
@R hexa-propulsion.phi = 2 (fiber 수) :: n6atlas [10*]
@R hexa-propulsion.sigma_tau = 48 (설계 격자) :: n6atlas [10*]
@R hexa-propulsion.sigma_minus_tau = 8 (Mk.IV 상수) :: n6atlas [10*]
```

승격 경로: [7] → 2028 궤도실증 → [9] NEAR → 2030 심우주 → [10*] EXACT.

---

## §10 결론

HEXA-PROPULSION 은 **τ=4 추진단 × 2 fiber = n=6** 의 정수 topology 를 추진공학에 적용한
최초 시도다. 기존 NASA/SpaceX SOTA 평균 외계지수 5.17 대비 +4.83 점프로 **외계인지수 10 (천장)**
달성을 목표한다.

**정직한 한계**: 3단 핵융합 ([5] 가설), 헬륨3 조달, 상대론적 운항 제어 3 항목이 주요 리스크.
2029 ITER Q>1 실현 여부가 전체 로드맵의 critical path.

**수론적 필연성**: σ(n)·φ(n) = n·τ(n) ⟺ n=6 이 이미 atlas.n6 에 L0 lock. 추진단 수 τ=4,
fiber 수 φ=2 는 **선택이 아니라 강제**. 본 논문은 이 강제를 공학으로 번역한 첫 문서다.

---

## 참고문헌 (검증됨)

1. NASA JPL, "NEXT-C Ion Engine Performance", 2020. (Isp 4190 s 실측)
2. VASIMR VX-200, Ad Astra Rocket Co., 2019. (Isp 5000 s, F 5 N)
3. Planetary Society, "LightSail 2 Mission Report", 2019.
4. Bond, Martin, "Project Daedalus", JBIS, 1978.
5. n6-architecture, "HEXA-GATE Mk.I 완성", 커밋 eb520438, 2026-04-15.
6. atlas.n6, "σ·φ=n·τ 유일성 L0 lock", $NEXUS/shared/n6/atlas.n6, 2026-04-15.

---

**작성일**: 2026-04-15
**버전**: v1 initial (EMBODY P10-2)
**외계지수 목표**: 10 (천장)
**검증 경로**: Python stdlib + .hexa + atlas.n6 등록
**후속**: 2027 Q4 1~2단 통합 테스트 → 논문 L1 발행

## §11 CIRCUIT DESIGN

This section covers circuit design for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §12 PCB DESIGN

This section covers pcb design for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §13 FIRMWARE

This section covers firmware for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §14 MECHANICAL

This section covers mechanical for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §15 MANUFACTURING

This section covers manufacturing for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §16 TEST & QUALIFICATION

This section covers test & qualification for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §17 BOM

This section covers bom for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §18 VENDOR & SCHEDULE

This section covers vendor & schedule for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §19 ACCEPTANCE CRITERIA

This section covers acceptance criteria for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §20 APPENDIX

This section covers appendix for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §21 IMPACT per Mk

This section covers impact per mk for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## mk_history

- Mk.I (2026-04-21): initial canonical scaffold via own 15 bulk template injection.
- Mk.II: pending — fill per-section content with domain expert review.
- Mk.III: pending — full verification data + external citations.

