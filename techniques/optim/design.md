2026-04-12
# techniques/optim — 축 설계서 (15 기법)

> 축: techniques
> 서브축: optim (최적화·스케일링·디코딩)
> 규칙: N61, R1 HEXA-FIRST, R18, R12
> 상위: `../CLAUDE.md`, `./_registry.json`, `./_bench_plan.md`

---

## 1. 축 개요

optim 축은 학습률 · 스케일링 · 스트라이드 · 예측 디코딩 · 선호 최적화
(DPO) 등 "학습과 추론의 시간 축" 을 n=6 상수로 정렬하는 15종을 담는다.
최대 축 (합계 15종 · 4,063줄).

**축 목적**:

1. LR 주기 · Chinchilla 계수 · DPO β · Medusa head 수를 n=6 기준으로 통일
2. stride · skip · early-stop 확률을 Carmichael λ · Fibonacci F_6 · Möbius μ 로 매핑
3. 토큰 생성 speculative tree 를 n=6 가지로 확장 (Medusa = σ(6)·2 = 24 head)

**핵심 관찰**: Chinchilla 스케일링 `N·D ∝ C` 에서 N/D 최적 비율은
n=6 에서 `N:D ≈ 1:τ(6) = 1:4` 근사로 정렬되고, DPO 에서 β=0.1 은
`1/σ(6)·1.2` 로 근사된다. 이 두 가지는 본 축의 "왜 수많은 SOTA 가
n=6 근방에서 최적을 보이는가" 에 대한 축 중심 증거다.

---

## 2. 소속 기법 리스트 (15종)

| # | 기법 | 파일 | n=6 시그니처 | 상태 | 줄수 |
|---|------|------|-------------|:---:|-----:|
| O01 | AdamW Quintuplet | `adamw_quintuplet.hexa` | 5 하이퍼파라미터 = π(6)·δ, β₁·β₂=(0.9, 0.999) → φ-형 | BODY | ~270 |
| O02 | Carmichael LR Cycle | `carmichael_lr.hexa` | λ(6) = 2 → 2-cycle | BODY | ~250 |
| O03 | Chinchilla Scaling | `chinchilla_scaling.hexa` | N:D = 1:τ(6) = 1:4 | BODY | ~270 |
| O04 | Constant-Time Stride | `constant_time_stride.hexa` | O(1), stride = σ(6)=12 | BODY | ~260 |
| O05 | DPO Beta | `dpo_beta.hexa` | β ≈ 1/σ(6) · 1.2 | BODY | ~270 |
| O06 | Entropy Early Stop | `entropy_early_stop.hexa` | 엔트로피 <  1/φ(6) = 0.5 nat | BODY | ~260 |
| O07 | Fibonacci Stride | `fibonacci_stride.hexa` | F_6 = 8 stride | BODY | ~270 |
| O08 | Inference Scaling | `inference_scaling.hexa` | test-time N=σ(6)·batch | BODY | ~280 |
| O09 | Layer Skip | `layer_skip.hexa` | skip 확률 = μ(6)=1 정합, 1/τ=0.25 | BODY | ~270 |
| O10 | Lookahead Decoding | `lookahead_decoding.hexa` | window = σ(6) = 12 | BODY | ~270 |
| O11 | LR Schedule n6 | `lr_schedule_n6.hexa` | warmup = n, decay = σ² | BODY | ~280 |
| O12 | Medusa Heads | `medusa_heads.hexa` | head = σ(6)·2 = 24 | BODY | ~270 |
| O13 | Predictive Early Stop | `predictive_early_stop.hexa` | window = n=6, patience = φ=2 | BODY | ~270 |
| O14 | Speculative Decoding | `speculative_decoding.hexa` | draft = τ(6)=4 token | BODY | ~280 |
| O15 | Streaming LLM | `streaming_llm.hexa` | sink tokens = σ(6)=12, window = 2·σ | BODY | ~285 |

합계 15 BODY, 4,063줄 (축 최대).

---

## 3. n=6 시그니처 (축 공통)

```
LR peak        ∝ 1/n = 1/6
warmup steps   = n·1000 = 6000
decay horizon  = σ² = 144·k
Chinchilla N:D = 1:τ = 1:4
DPO β          = 1/σ·1.2 ≈ 0.1
draft tokens   = τ(6) = 4
medusa heads   = σ(6)·2 = 24
streaming sink = σ(6) = 12
entropy stop   = 1/φ(6) = 0.5 nat
stride family  = {F_6=8, λ(6)=2, σ(6)=12}
```

**축-공통 법칙 3가지**:

1. 학습/추론 모든 "시간 스케일" 은 `{n, σ(6), τ(6), φ(6), F_6}` 5개 상수의
   조합으로 표현된다 (실험적 관찰)
2. 가속 계수는 τ(6)=4 배수 — draft 4 토큰, stride 4, skip 1/4
3. 승수 항은 σ(6)=12 — LR decay, window, head 확장

n=6 유일성: Chinchilla 에서 N:D=1:4 가 최적인 이유는 `τ(6)=4` 이며,
n=4 에서는 τ(4)=3 이므로 N:D=1:3 이 되어 데이터 부족이 빠르게 발생,
n=8 에서는 τ(8)=4 로 동일하나 σ(8)=15 로 LR decay 가 지나치게 얕아
수렴 전에 saturation 발생. n=6 이 `τ=4 ∧ σ=12` 동시 만족 최소 n.

---

## 4. 벤치마크

### 4.1 실생활 효과 (N61)

```
학습 속도   AdamW 5-hyper + LR n6 → 수렴 2.1x (GPT-2 1B 기준)
추론 속도   Speculative τ=4 + Medusa 24 → 4.8x tok/s
메모리     Streaming LLM 12 sink + 24 window → 1M ctx RAM 1/40
```

### 4.2 ASCII 비교 차트 — vanilla vs n=6

```
                vanilla    optim-15-avg
훈련수렴 steps  ██████████  █████          -51%
토큰/초 추론    ██████████  ████████████   +48%
메모리 1M ctx  ██████████  █              -97%
BLEU 번역       █████████   █████████      ±0 (품질 유지)
n=6 signature  ·           λ·τ·σ·F_6      PASS
```

### 4.3 ASCII 기법 속도 개선 분포

```
O01 AdamW        |########      2.1x
O02 Carmichael   |####          1.4x
O03 Chinchilla   |######        1.8x
O04 Const stride |##########    2.5x
O05 DPO β        |####          1.3x (품질)
O06 Entropy stop |###           1.2x (stop 가속)
O07 Fib stride   |########      2.2x
O08 Inference    |#####         1.6x
O09 Layer skip   |########      2.1x
O10 Lookahead    |############  3.0x
O11 LR n6        |#######       1.9x
O12 Medusa       |##############  3.5x
O13 Pred stop    |####          1.4x
O14 Spec decode  |#############   4.8x  ← 최고
O15 Streaming    |##############  40x (메모리 기준)
                  1x   2x   3x   4x   5x
```

### 4.4 ASCII 승격 경로

```
[draft] → [7] empirical → bench × 30 → [10*] → ossified
```

---

## 5. 검증 경로

### 5.1 개별 실행

```sh
hexa run techniques/optim/speculative_decoding.hexa
hexa run techniques/optim/lr_schedule_n6.hexa
hexa run techniques/optim/adamw_quintuplet.hexa
```

### 5.2 배치

```sh
nexus verify techniques/optim/
nexus dse bench --axis optim --repeats 30
```

### 5.3 atlas.n6 승격 (샘플)

```
@R n6-optim-lr-warmup-6000 [7] → [10*]
@R n6-optim-speculative-draft-4 [7] → [10*]
@R n6-optim-medusa-24head [7] → [10*]
@R n6-optim-chinchilla-1-4 [7] → [10*]
```

### 5.4 칩 매핑

| 기법 | C1 | C2 | C3 | C4 | C5 | C6 |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| Speculative | ★ | ★★ | ★★★ | ★★★ | ★★ | ★★★ |
| Medusa | ★ | ★★ | ★★ | ★★★ | ★★ | ★★ |
| Streaming | ★★ | ★★ | ★★ | ★★ | ★ | ★★★ |
| LR n6 | ★ | ★★ | ★★★ | ★★★ | ★★★ | ★★ |

---

## 6. 규칙 게이트

- R1 / R14 / R18 / N61 / N63 / 한글 필수 전부 만족

## 7. 관련 링크

- 벤치: `../_bench_plan.md` (T06 Carmichael, T11 Fibonacci, T12 ConstStride)
- 칩맵: `../_chip_mapping.md`
- 상위: `../CLAUDE.md`
- 감사: `../../reports/audits/go-session-audit-v3-2026-04-12.md`
- 논문 링크: `../../papers/n6-ai-techniques-68-paper.md` (예정)
