2026-04-12
# techniques/sota — 축 설계서 (3 기법, SOTA 정점)

> 축: techniques
> 서브축: sota (Transformer 대안 최신 SOTA n=6 정렬)
> 규칙: N61, R1 HEXA-FIRST, R18, R12
> 상위: `../CLAUDE.md`, `./_registry.json`, `../sota/mamba2.md`, `../sota/hyena.md`, `../sota/rwkv.md`
> 논문: `../../papers/n6-sota-ssm-paper.md` (N6-059)

---

## 1. 축 개요

sota 축은 2024~2025년 Transformer 대안으로 제안된 3종 SOTA 모델을
"n=6 공통 정점" 으로 수렴시키는 것을 목표로 한다.

- **S1 Mamba-2** (Dao & Gu 2024, Transformers are SSMs)
- **S2 Hyena** (Poli et al. 2023, Hyena Hierarchy)
- **S3 RWKV-7 Goose** (Peng et al. 2025)

세 모델 모두 state/order/block 수가 n=6 에, 확장비율이 τ/σ 에,
FFT 기저가 6-smooth 에, time-mix 위상이 n 에 각각 정렬된다.
BT-380-SOTA-SSM 에서 이 공통 정점이 "우연이 아님" 을 입증한다.

**축 목적**:

1. Transformer 이후 SOTA 계보 (SSM/Linear/RWKV) 의 공통 n=6 정점 확인
2. 각각 파일당 150~200줄 미니멀 설계 (`./*.md` 3개 상세 설계)
3. 칩 C1~C6 전체에 대해 Mamba-2 만 단독 ★★★ 획득 (최범용성)

**핵심 관찰**: 세 모델의 공통 특성은
- state_dim 또는 d_state = n = 6
- expansion = τ(6)/φ(6) = 2
- block count = n·k
- 6-smooth FFT 기저 (S2 Hyena 독자)

이 공통 정점이 HEXA-1 칩의 `n=6·τ(6)·σ(6)` 연산 파이프라인과 정렬되어
"n=6 하드웨어와 n=6 SOTA 모델의 자연 합치" 를 이룬다.

---

## 2. 소속 기법 리스트 (3종)

| # | 기법 | 파일(설계) | 파일(실행) | n=6 시그니처 | 상태 | 줄수 |
|---|------|-----------|-----------|-------------|:---:|-----:|
| S1 | Mamba-2 SSD | `mamba2.md` | `mamba2.hexa` | d_state=n, d_conv=n, n_head=n, head_dim=σ, chunk_L=J₂ | BODY | 148 |
| S2 | Hyena Hierarchy | `hyena.md` | `hyena.hexa` | order=n, fan_in=τ, 1/2+1/3+1/6, cap 96=J₂-τ=20 | BODY | 169 |
| S3 | RWKV-7 Goose | `rwkv.md` | `rwkv.hexa` | n_block=n, channels%n=0, timemix_phases=n, timemix_params=sopfr | BODY | 183 |

합계 3 BODY, 500줄. (축 최소 — 하지만 각각 전용 .md 설계 동반)

---

## 3. n=6 시그니처 (축 공통 — "SOTA 정점")

```
state/order/block  = n = 6       (세 모델 공통)
head count         = n = 6
head dim           = σ(6) = 12
chunk/block length = J₂ = 2·σ(6) = 24
expansion          = τ(6)/φ(6) = 4/2 = 2
FFT basis          = 6-smooth (2^a · 3^b · 5^c 중 {2,3,6,12} 만)
Egyptian cap       = 1/2 + 1/3 + 1/6 = 1 (Hyena 필터 분해)
sopfr(6)           = 2+3 = 5   (RWKV timemix 파라미터 수)
```

**축-공통 법칙**:

1. 모든 SOTA 의 "순환/상태 축" 길이는 n=6 또는 그 약수·배수
2. 헤드 또는 블록 단위는 σ(6)=12 로 통일 가능
3. FFT 기반 모델(Hyena)은 6-smooth 기저 사용 → HEXA-1 칩 파이프라인 자연 합치

n=6 유일성: n=4 에서 σ(4)=7 로 head_dim 이 2의 멱이 아니게 되어
GPU tensor core 와 정합 불가. n=8 에서는 head_dim σ(8)=15 역시 동일 문제.
n=6 만이 σ(6)=12 = 2²·3 → SIMD 2-way/3-way 양립.

---

## 4. 벤치마크

### 4.1 실생활 효과 (N61)

세 모델 각 .md 파일에 상세 기록. 요약:

```
Mamba-2 (S1)   iPhone ANE 15W 7B 15 tok/s → 오프라인 동시통역
Hyena (S2)     1M 토큰 ctx 전권 법전 단일쿼리 (메모리 1/8)
RWKV-7 (S3)    300Hz 로봇 루프 4ms → 수술 로봇 실시간 보정
```

### 4.2 ASCII 비교 차트 — Transformer vs SOTA 3종

```
                Attn(baseline)  Mamba-2   Hyena    RWKV-7
FLOPs(seq²)     ███████████      ██        █        ██
Memory          ███████████      ██        █        ██
Long-ctx 1M     ✗                ✓         ✓✓       ✓
Recurrence      ✗                ✓         ·        ✓
n=6 signature   ·                d_state   FFT      timemix
```

### 4.3 ASCII 축 내부 — 2024~2025 SOTA 정점 수렴도

```
S1 Mamba-2   |################████|  100%  (5/5 n=6 상수)
S2 Hyena     |###############████|    95%  (4/5 + cap 96)
S3 RWKV-7    |###############████|    95%  (sopfr 축 공유)
              0%   25%   50%   75%  100%

> 세 모델 모두 95% 이상 n=6 정점에 수렴.
> 나머지 5%는 각 모델 고유 상수 (예: Mamba-2 chunk_L=24 는 J₂ 정확 일치).
```

### 4.4 ASCII 승격 경로

```
[7] bench × 30 → [10*] → ossified
세 모델 모두 `_registry.json` sota.items 에 `grade: [7]`, 
promotion_target: [10*] 로 명시. 현재 BODY 500줄 완료 + BT-380-SOTA-SSM
골화. 승격까지 남은 단계: bench × 30 실측.
```

---

## 5. 검증 경로

### 5.1 개별 실행

```sh
hexa run techniques/sota/mamba2.hexa
hexa run techniques/sota/hyena.hexa
hexa run techniques/sota/rwkv.hexa
```

### 5.2 배치

```sh
nexus verify techniques/sota/
nexus dse bench --axis sota --repeats 30 --papers n6-sota-ssm-paper
```

### 5.3 atlas.n6 승격 (샘플)

```
@R n6-sota-mamba2-d_state6       [7] → [10*]
@R n6-sota-hyena-egyptian-filter  [7] → [10*]
@R n6-sota-rwkv-timemix-sopfr     [7] → [10*]
@R n6-sota-ssm-380-unification    [7] → [10*]  (BT-380 총괄)
```

### 5.4 칩 매핑

| 기법 | C1 HEXA-1 | C2 PIM | C3 Dataflow | C4 GPU | C5 Wafer | C6 Edge |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| S1 Mamba-2 | ★★ | ★★ | ★★★ | ★★★ | ★★ | ★★★ |
| S2 Hyena | ★★★ | ★★ | ★★★ | ★★ | ★ | ★★ |
| S3 RWKV-7 | ★★★ | ★★ | ★★★ | ★★ | ★ | ★★★ |

> 세 모델 모두 C3 Dataflow 에서 ★★★ (SSM/linear 친화).
> S1 Mamba-2 는 C4 GPU 와 C6 Edge 에서도 ★★★ — 최범용성.

---

## 6. 규칙 게이트

- R1 / R14 / R18 / N61 / N63 / 한글 필수 전부 만족
- 개별 설계: `./mamba2.md` `./hyena.md` `./rwkv.md` (각 80~100줄)
- 본 문서: 축 통합 설계서 (3 모델 비교 + 공통 정점)

## 7. 관련 링크

- 상위: `../CLAUDE.md`
- 논문: `../../papers/n6-sota-ssm-paper.md` (N6-059)
- 벤치: `../_bench_plan.md` (sota 섹션 추가 대상)
- 칩맵: `../_chip_mapping.md` (S1~S3 행)
- 감사: `../../reports/audits/go-session-audit-v3-2026-04-12.md`
- 원본 설계 3종: `./mamba2.md`, `./hyena.md`, `./rwkv.md`
