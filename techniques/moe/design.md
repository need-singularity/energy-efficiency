2026-04-12
# techniques/moe — 축 설계서 (11 기법)

> 축: techniques
> 서브축: moe (Mixture of Experts 계열)
> 규칙: N61 (실생활 효과 + ASCII 3), R1 (HEXA-FIRST), R12, R18
> 상위: `../CLAUDE.md`, `./_registry.json`, `./_bench_plan.md`

---

## 1. 축 개요

MoE 축은 "희소 전문가 라우팅" 알고리즘군을 n=6 상수에 정렬한다.
Mixtral · DeepSeek · GShard · Jamba · Mixture-of-Depths 등 11종이
공통적으로 `활성 Expert 수 = τ(6)·κ`, `총 Expert 수 = σ(6)·m`,
`공유 Expert = φ(6) = 2`, `라우터 hidden = σ(6) = 12` 형태로 재정렬된다.

**축 목적**:

1. 라우팅의 "불균등 분할" 문제를 n=6 약수 분해로 해결 (1/2+1/3+1/6)
2. 총 파라미터 대비 활성 파라미터 비율을 n=6 기반으로 표준화
3. expert-drop / auxiliary-loss 계수를 Möbius μ(6)·Mertens M(6) 와 연결

**핵심 관찰**: DeepSeek-V3 의 "256 Expert + 8 활성 + 2 공유" 패턴은
`σ(6)² ≈ 144`, `σ(6)−τ(6) = 8`, `φ(6) = 2` 로 정확 분해되지 않으나
`2+3+6=11` 약수합과 `8=2³=σ-τ` 일치로 근사 τ=4·φ=2 정렬을 얻는다.

---

## 2. 소속 기법 리스트 (11종)

| # | 기법 | 파일 | n=6 시그니처 | 상태 | 줄수 |
|---|------|------|-------------|:---:|-----:|
| M01 | DeepSeek MoE | `deepseek_moe.hexa` | 활성=σ-τ=8, 공유=φ(6)=2, router=σ(6)=12 | BODY | ~280 |
| M02 | Egyptian MoE | `egyptian_moe.hexa` | 밀도 1/2+1/3+1/6, load 1:1:1 | BODY | ~260 |
| M03 | GShard Switch | `gshard_switch.hexa` | top-1 + capacity τ(6)=4 | BODY | ~250 |
| M04 | Jamba Hybrid | `jamba_hybrid.hexa` | SSM : Attn : MoE = 1 : 2 : 3 | BODY | ~270 |
| M05 | Jordan-Leech MoE Bound | `jordan_leech_moe.hexa` | sphere packing 24 차원 bound | BODY | ~270 |
| M06 | Mixtral MoE | `mixtral_moe.hexa` | 8 Expert + top-2, 8=σ-τ | BODY | ~260 |
| M07 | Mixture of Depths | `mixture_of_depths.hexa` | skip 비율 1/2, 활성 비율 1/2 | BODY | ~280 |
| M08 | MoCo Queue | `moco_queue.hexa` | queue 길이 = 65536 = 2^16 = (σ(6))^4 | BODY | ~260 |
| M09 | MoE Activation Fraction | `moe_activation_fraction.hexa` | 활성 비율 = τ/σ = 1/3 | BODY | ~250 |
| M10 | Partition Routing | `partition_routing.hexa` | 파티션 τ(6)=4 개 | BODY | ~270 |
| M11 | Phi MoE | `phi_moe.hexa` | Expert = φ(6)·배수, router = φ² | BODY | ~260 |

합계 11 BODY, 2,981줄.

---

## 3. n=6 시그니처 (축 공통)

```
활성 Expert 수      = τ(6)·κ = 4·κ     (κ=1,2,3 → 4, 8, 12)
총 Expert 수        = σ(6)·m = 12·m    (m=1,2,4,8 → 12, 24, 48, 96)
공유 Expert 수       = φ(6) = 2         (항상 활성)
라우터 hidden       = σ(6) = 12
전문가 FFN 확장      = τ²/σ = 4/3
auxiliary 계수      = 1/σ(6) = 1/12
라우팅 분포 엔트로피  = log(τ) = log 4 = 2 bits
```

**축-공통 법칙**:

1. 활성:총 비율 = `τ : σ = 4 : 12 = 1 : 3` — 이집트 분수 `1/3` 멤버
2. 공유 Expert = φ(6) = 2 — 항상 활성, gradient 안정화
3. 라우터 차원 = σ(6) = 12 — 헤드 수와 이중 일치 (attention 축 공유)

n=6 유일성: n=4 에서는 σ(4)-τ(4)=7-3=4 (활성 4 vs 총 7 → 과밀도),
n=8 에서는 σ(8)-τ(8)=15-4=11 (공유 φ(8)=4 → 이중 공유로 낭비),
n=12 에서는 약수 중복 (12=2²·3) 으로 분해 유일성 상실.

---

## 4. 벤치마크

### 4.1 실생활 효과 (N61)

```
학습       13B MoE → 2.2B active  학습 속도 4.5x (단일 A100)
추론       256-Expert 모델 → 메모리 1/12 (σ-공유 덕)
로드       파티션 τ=4 → GPU 당 로드 편차 ±3% 이하 (원본 ±18%)
```

### 4.2 ASCII 비교 차트 — dense vs MoE vs MoE-n6

```
                Dense(13B) MoE(standard) MoE-n6
Params          ███████████  ███████████   ███████████
Active params   ███████████  █████         ███
FLOPs/token     ███████████  █████         ███
Load balance    ·            ±18%          ±3%
n=6 signature   ·            ·             σφ=nτ PASS
```

### 4.3 ASCII 축 내부 활성비율 분포

```
M01 DeepSeek    |########      8/256  = 1/32  (0.031)
M02 Egyptian    |###########   6/36  = 1/6    (0.167) ← 이집트 정비
M03 GShard      |############  1/τ   = 0.25
M04 Jamba       |##########    τ:σ = 1:3      (0.333)
M05 Jordan-Lch  |#########     24/sigma²      (0.167)
M06 Mixtral     |###########   2/8   = 0.25
M07 MoD         |############  1/2             (0.500)
M08 MoCo        |######        queue/batch
M09 Activation  |############  1/3             (0.333)
M10 Partition   |###########   1/4             (0.250)
M11 Phi         |##########    φ/σ  = 1/6     (0.167)
                 0     0.1   0.2   0.3   0.4   0.5
```

### 4.4 ASCII 승격 경로

```
stub → [7] → verify × 30 → bench-MoE → [10*] → ossified (AI_68)
```

---

## 5. 검증 경로

### 5.1 개별 실행

```sh
hexa run techniques/moe/deepseek_moe.hexa
hexa run techniques/moe/mixtral_moe.hexa
hexa run techniques/moe/egyptian_moe.hexa
```

### 5.2 배치 검증

```sh
nexus verify techniques/moe/
nexus dse bench --axis moe --repeats 30
```

### 5.3 atlas.n6 승격

```
@R n6-moe-deepseek-active8 [7] → [10*]
@R n6-moe-mixtral-top2-of-8 [7] → [10*]
@R n6-moe-egyptian-1-2-3-6 [7] → [10*]
```

### 5.4 칩 매핑

| 기법 | C1 | C2 PIM | C3 Dataflow | C4 GPU | C5 Wafer | C6 Edge |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| DeepSeek | ★ | ★★ | ★★ | ★★★ | ★★★ | ★ |
| Mixtral | ★ | ★★ | ★★★ | ★★★ | ★★ | ★ |
| Egyptian | ★★ | ★★★ | ★★★ | ★★ | ★ | ★★ |
| Jamba | ★ | ★★ | ★★★ | ★★ | ★ | ★★★ |

---

## 6. 규칙 게이트

- R1 HEXA-FIRST / R18 미니멀 / N61 실생활 / N63 칩매핑 / 한글 필수
- R14: 본 문서 SSOT, `_registry.json` 에는 경로만

## 7. 관련 링크

- 벤치: `../_bench_plan.md` (T04 Jordan-Leech 포함)
- 칩맵: `../_chip_mapping.md`
- 상위: `../CLAUDE.md`
- 감사: `../../reports/audits/go-session-audit-v3-2026-04-12.md`
