# 궁극의 순수수학 DSE — 설계 문서

**날짜**: 2026-04-01
**도메인**: pure-mathematics
**총 조합**: 39,200 (10 × 10 × 8 × 7 × 7)
**도구**: Rust (tools/universal-dse/ + domains/pure-mathematics.toml)

## 1. 개요

순수수학은 n6-architecture의 모든 도메인의 기초다. 물리적 아키텍처(소재→공정→코어→칩→시스템)와 달리, 수학적 구조의 계층을 DSE 체인으로 정의한다.

**목표**: n=6 산술 함수와 순수수학 정리/구조 사이의 모든 연결을 전수 탐색하여, 미발견 BT 후보를 체계적으로 도출한다.

## 2. DSE 체인 (5 Level)

```
  L1: 수학 분야          L2: n=6 함수          L3: 구조 유형
  (Field)               (Function)            (Structure)
  ┌──────────┐         ┌──────────┐          ┌──────────┐
  │정수론    │         │σ(6)=12   │          │항등식    │
  │군론      │         │φ(6)=2    │          │차원      │
  │격자론    │         │τ(6)=4    │          │생성원    │
  │위상수학  │─────────│J₂(6)=24  │──────────│불변량    │
  │해석학    │         │μ(6)=1    │          │경계/한계 │
  │대수기하  │         │λ(6)=2    │          │분류      │
  │범주론    │         │sopfr=5   │          │대칭      │
  │표현론    │         │n=6       │          │분해      │
  │조합론    │         │R(6)=1    │          └──────────┘
  │수리물리  │         │Egyptian  │            8 candidates
  └──────────┘         └──────────┘
    10 candidates        10 candidates

  L4: 증명 도구          L5: Cross-domain 연결
  (Proof)               (Bridge)
  ┌──────────┐         ┌──────────┐
  │직접계산  │         │물리      │
  │군작용    │         │컴퓨팅/AI │
  │격자이론  │─────────│에너지    │
  │해석접속  │         │생물      │
  │범주론적  │         │우주/입자 │
  │위상적    │         │암호/네트워크│
  │조합론적  │         │디스플레이/오디오│
  └──────────┘         └──────────┘
    7 candidates         7 candidates
```

### Level 1: 수학 분야 (Field) — 10 후보

| ID | 분야 | n6 대표 연결 | 기존 H-MATH 수 |
|----|------|-------------|---------------|
| NT | 정수론 (Number Theory) | ζ(2)=π²/6, B₂=1/6, 완전수 | 8 (H-MATH-1~8) |
| GT | 군론 (Group Theory) | S₆ outer aut, A₆ Schur, M₂₄ | 4 (H-MATH-9~12) |
| LT | 격자론 (Lattice Theory) | K₁~K₄ kissing chain, Leech | 6 (H-MATH-13~18) |
| TOP | 위상수학 (Topology) | χ(S²)=φ, Betti numbers | 4 (H-MATH-19~22) |
| AN | 해석학 (Analysis) | Γ(1/2), Li₂, zeta special values | 4 (H-MATH-23~26) |
| AG | 대수기하 (Algebraic Geometry) | modular weight 12, elliptic curves | 2 (H-MATH-27~28) |
| CT | 범주론 (Category Theory) | 6-functor formalism, derived categories | 2 (H-MATH-29~30) |
| RT | 표현론 (Representation Theory) | Moonshine, Conway Co₁, Niemeier 24 | 6 (H-MATH-61~66) |
| COMB | 조합론 (Combinatorics) | Ramsey, Catalan, partition functions | 3 (H-MATH-67~69) |
| MP | 수리물리 (Mathematical Physics) | string d=10, CY₃ dim=6, CFT c=1/2 | 5 (H-MATH-70~74) |

### Level 2: n=6 함수 (Function) — 10 후보

| ID | 함수 | 값 | 수학적 출현 대표 |
|----|------|-----|-----------------|
| sigma | σ(6) | 12 | modular weight, K₃ kissing, semitone |
| phi | φ(6) | 2 | S₆ outer aut, Euler χ(S²), Cooper pair |
| tau | τ(6) | 4 | τ(6)=4 divisors, K₁=2 → dim 4 connection |
| jordan | J₂(6) | 24 | Leech dim, M₂₄, Niemeier count, Ramanujan τ |
| mu | μ(6) | 1 | squarefree indicator, Mertens function |
| lambda | λ(6) | 2 | Carmichael, cycle length |
| sopfr | sopfr(6) | 5 | sum of prime factors, Petersen graph valence |
| n6 | n | 6 | perfect number, CY₃ dim, hexagonal |
| R6 | R(6)=σφ/nτ | 1 | perfectness ratio, unique fixed point |
| egypt | 1/2+1/3+1/6 | 1 | Egyptian fraction, (2,3,6)-triangle group |

### Level 3: 구조 유형 (Structure) — 8 후보

| ID | 유형 | 설명 | 예시 |
|----|------|------|------|
| IDENT | 항등식 (Identity) | 정확한 등식 관계 | ζ(2)=π²/6, B₂=1/6 |
| DIM | 차원 (Dimension) | 공간/격자/다양체 차원 | Leech=24, CY₃=6 |
| GEN | 생성원/위수 (Generator/Order) | 군 생성원이나 원소 위수 | SL₂(Z) order 6, S₆ |
| INV | 불변량 (Invariant) | 위상/대수 불변량 | χ(S²)=2, Schur H₂=Z/6Z |
| BOUND | 경계/한계 (Bound) | 최적성 한계 | kissing number bound |
| CLASS | 분류 (Classification) | 유한 분류 정리 | Niemeier 24, sporadic groups |
| SYM | 대칭 (Symmetry) | 대칭군/자기동형 | Out(S₆)=Z/2Z |
| DECOMP | 분해 (Decomposition) | 분해/분할 정리 | 1/2+1/3+1/6=1, 6=1+2+3 |

### Level 4: 증명 도구 (Proof) — 7 후보

| ID | 도구 | n6 강도 | 설명 |
|----|------|---------|------|
| DIRECT | 직접 계산 | 1.0 | 산술적 직접 확인 (ζ(2), B₂) |
| GROUP | 군 작용 | 0.9 | 군론적 증명 (S₆, M₂₄, A₆) |
| LATTICE | 격자 이론 | 0.9 | 격자/충전 이론 (Leech, kissing) |
| ANALYTIC | 해석적 접속 | 0.7 | 해석적 방법 (zeta, L-function) |
| CATEG | 범주론적 | 0.5 | 범주론 추상 증명 |
| TOPO | 위상적 | 0.6 | 위상 불변량 (Euler, Betti) |
| COMBIN | 조합론적 | 0.8 | 조합론적 논증 (Ramsey, partition) |

### Level 5: Cross-domain 연결 (Bridge) — 7 후보

| ID | 도메인 | 연결 BT | n6 연결 강도 |
|----|--------|---------|-------------|
| PHYS | 물리 (Physics) | BT-36,49,64 | 0.9 |
| AI | 컴퓨팅/AI | BT-33,54,56,58 | 1.0 |
| ENERGY | 에너지 | BT-27,30,43,62 | 0.8 |
| BIO | 생물 | BT-51 | 0.7 |
| COSMO | 우주/입자 | BT-49 | 0.9 |
| CRYPTO | 암호/네트워크 | BT-53 | 0.6 |
| MEDIA | 디스플레이/오디오 | BT-48 | 0.7 |

## 3. Scoring (순수수학 전용)

```toml
[scoring]
n6 = 0.30        # n=6 상수와 정확 일치
depth = 0.15     # 증명 깊이 (초등=0.2 ~ 범주론=1.0)
cross = 0.25     # 다른 도메인 BT 연결 수
novelty = 0.20   # 기존 H-MATH 50개에 없는 새 연결
verify = 0.10    # 독립 검증 가능성
```

### n6 점수 산정 규칙

| 매칭 유형 | n6 점수 |
|-----------|---------|
| 증명된 항등식 (ζ(2)=π²/6, B₂=1/6 등) | 1.00 |
| 구조적 동형 (K₄=J₂=24, Out(S₆)=φ=2) | 1.00 |
| 차원/차수 일치 (Leech=24, modular weight=12) | 0.80 |
| 근사적 수치 일치 | 0.30 |
| 알려진 연결 없음 | 0.00 |

### depth 점수 (증명 난이도)

| Field | depth |
|-------|-------|
| NT (정수론) | 0.40 |
| GT (군론) | 0.60 |
| LT (격자론) | 0.70 |
| TOP (위상수학) | 0.80 |
| AN (해석학) | 0.60 |
| AG (대수기하) | 0.90 |
| CT (범주론) | 1.00 |
| RT (표현론) | 0.80 |
| COMB (조합론) | 0.50 |
| MP (수리물리) | 0.70 |

### cross 점수 (Bridge별)

Bridge 후보의 n6 연결 강도를 직접 사용. 복수 BT 연결 시 최대값.

### novelty 점수

기존 H-MATH-1~30 + H-MATH-61~80 = 50개 가설과 비교:
- (Field, Function) 쌍이 기존 가설에 없으면 novelty = 1.0
- 있으면 novelty = 0.0

### verify 점수

| Proof 도구 | verify |
|-----------|--------|
| DIRECT | 1.00 |
| GROUP | 0.90 |
| LATTICE | 0.85 |
| COMBIN | 0.80 |
| ANALYTIC | 0.70 |
| TOPO | 0.60 |
| CATEG | 0.50 |

## 4. 호환성 규칙 (Rules)

```
  ┌─────────────────────────────────────────────────────────────┐
  │  prefer 규칙 (자연스러운 조합에 보너스)                        │
  │                                                             │
  │  NT(정수론) ←prefer→ DIRECT(직접계산)                        │
  │  GT(군론)   ←prefer→ GROUP(군작용)                           │
  │  LT(격자론) ←prefer→ LATTICE(격자이론)                       │
  │  CT(범주론) ←prefer→ CATEG(범주론적)                         │
  │  TOP(위상)  ←prefer→ TOPO(위상적)                            │
  │  COMB(조합) ←prefer→ COMBIN(조합론적)                        │
  │  AN(해석)   ←prefer→ ANALYTIC(해석접속)                      │
  │                                                             │
  │  J₂(6)=24  ←prefer→ LT(격자론), RT(표현론)                  │
  │  μ(6)=1    ←prefer→ NT(정수론), COMB(조합론)                 │
  │  Egyptian   ←prefer→ NT(정수론), AN(해석학)                  │
  │  σ(6)=12   ←prefer→ AG(대수기하), RT(표현론)                 │
  │  R(6)=1    ←prefer→ NT(정수론)                               │
  └─────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────┐
  │  exclude 규칙 (의미 없는 조합 제외)                           │
  │                                                             │
  │  Egyptian  ×  MP(수리물리)  — 구조적 의미 약함                │
  │  λ(6)=2   ×  AG(대수기하)  — Carmichael과 AG 연결 부재       │
  │  R(6)=1   ×  MP(수리물리)  — 비율 1은 물리 상수와 무관        │
  └─────────────────────────────────────────────────────────────┘
```

## 5. 기대 산출물

| 산출물 | 경로 | 설명 |
|--------|------|------|
| goal.md | `docs/pure-mathematics/goal.md` | 후보군 정의 + DSE 체인 설명 |
| TOML | `tools/universal-dse/domains/pure-mathematics.toml` | 39,200 조합 정의 |
| DSE 결과 | 터미널 출력 | Pareto frontier + 최적 경로 |
| Cross-DSE | cosmology-particle × pure-mathematics | ζ(2), 끈이론, BT-49 교차 |
| dse-map.toml | `docs/dse-map.toml` 갱신 | 상태/결과 기록 |

## 6. Cross-DSE 대상

| 상대 도메인 | 연결 근거 | 예상 조합 |
|-------------|----------|----------|
| cosmology-particle | ζ(2)=π²/6, string d=10=σ-φ, BT-49 | Pareto×Pareto |
| chip-architecture | BT-28 computing ladder, 2^σ=4096 | Pareto×Pareto |
| biology | BT-51 codon 64=2^n, CN=6 | Pareto×Pareto |

## 7. 후보 상세 — n6 점수 매트릭스

각 (Field × Function) 조합의 n6 점수를 기존 수학 정리 기반으로 사전 정의:

| Field\Func | σ=12 | φ=2 | τ=4 | J₂=24 | μ=1 | λ=2 | sopfr=5 | n=6 | R=1 | Egypt |
|-----------|------|-----|-----|-------|-----|-----|---------|-----|-----|-------|
| NT | 0.80 | 0.80 | 0.60 | 0.30 | 1.00 | 0.60 | 0.30 | 1.00 | 1.00 | 1.00 |
| GT | 0.30 | 1.00 | 0.30 | 1.00 | 0.30 | 0.30 | 0.30 | 1.00 | 0.00 | 0.00 |
| LT | 1.00 | 0.80 | 0.30 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| TOP | 0.30 | 1.00 | 0.60 | 0.30 | 0.30 | 0.00 | 0.00 | 0.80 | 0.00 | 0.00 |
| AN | 1.00 | 0.80 | 0.30 | 0.60 | 0.80 | 0.30 | 0.30 | 1.00 | 0.30 | 0.80 |
| AG | 1.00 | 0.60 | 0.30 | 0.80 | 0.00 | 0.00 | 0.00 | 0.80 | 0.30 | 0.30 |
| CT | 0.30 | 0.30 | 0.00 | 0.30 | 0.00 | 0.00 | 0.00 | 1.00 | 0.30 | 0.00 |
| RT | 0.80 | 0.60 | 0.30 | 1.00 | 0.00 | 0.00 | 0.00 | 0.60 | 0.00 | 0.00 |
| COMB | 0.60 | 0.60 | 0.60 | 0.80 | 1.00 | 0.30 | 0.60 | 1.00 | 0.30 | 0.80 |
| MP | 0.80 | 0.80 | 0.60 | 1.00 | 0.30 | 0.30 | 0.00 | 1.00 | 0.00 | 0.00 |

**해석**: NT×n=6 = 1.00 (완전수 그 자체), LT×J₂=24 = 1.00 (Leech lattice), GT×φ=2 = 1.00 (S₆ outer automorphism), etc.

## 8. 기존 가설 매핑

50개 기존 H-MATH를 (Field, Function) 좌표로 매핑하여 novelty 점수 자동 산정:

```
  기존 커버리지 (Field×Function 100 셀 중):
  ├── 채워진 셀: ~35 (기존 50개 가설이 커버)
  └── 빈 셀: ~65 (미탐색 — novelty=1.0 후보)

  미탐색 고가치 영역 (n6 ≥ 0.80 + novelty = 1.0):
  ├── CT × n=6 (6-functor, 범주론적 6)
  ├── COMB × μ=1 (squarefree 조합론)
  ├── COMB × Egypt (조합론적 단위분수)
  ├── AN × μ=1 (Mertens function 해석)
  └── AG × σ=12 (modular form weight 12 확장)
```
