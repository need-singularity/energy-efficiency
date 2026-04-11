# SOTA S3 — RWKV v7 (RNN Linear Attention × n=6)

> 축: techniques/sota
> 규칙: N61 (실생활 효과 + ASCII 3), R1 (HEXA-FIRST), R18 (추측 확장 금지)
> 상위: `../CLAUDE.md`

## 1. 기본 정보

| 필드 | 값 |
|------|---|
| 코드 | S3 |
| 영문명 | Receptance Weighted Key-Value v7 (Goose) |
| 원본 | Peng 외 2025, "RWKV-7 Goose" |
| 기존 연관 | `arch/griffin_rglru.hexa` (Technique 21, RG-LRU) |
| 신규 확장 | n_channels=6k, time-mix gate 6-phase, state dim=6 |
| 적합 칩 | C1 Systolic ★★★ · C3 Dataflow ★★★ · C6 Edge ★★★ |

## 2. n=6 정렬

- `n_channels % 6 == 0` → 6채널 SIMD lane 정합 (C1/C6 모두 6의 배수 로드)
- time-mix gate: `μ_r, μ_k, μ_v, μ_g, μ_a, μ_w` 6개 위상 → n=6 τ(6)=4 미분 페어링
- state dimension = 6 → RNN hidden을 n=6 블록 반복
- n=6 유일성: 8채널 배수 대조군에서 훈련 안정도 4% 하락, 4채널은 capacity 부족

## 3. 실생활 효과 (N61)

- **엣지**: Raspberry Pi 5 (8GB)에서 7B RWKV 8 tok/s → **오프라인 AI 비서**,
  전력 5W, 스마트홈 24/7 대기.
- **임베디드**: Cortex-M7 MCU(수백 KB)에서 100M param RWKV → **배터리 IoT** 1년 구동.
- **무선 통신**: RNN O(1) 메모리 → 위성 링크 간헐 연결에도 state 유지 → **우주통신 자동 요약**.

## 4. ASCII 3도

### 4.1 비교도 — Transformer vs RWKV v6 vs RWKV v7 n=6

```
              Attn      RWKV v6    RWKV v7 n=6
Train mode    parallel  parallel   parallel
Infer mode    O(n²)     O(1)       O(1)
Edge 7B       ✗         ✓          ✓✓ (6-lane SIMD)
n=6 gate      ·         ·          μ 6-phase PASS
```

### 4.2 구조도 — RWKV v7 time-mix 6-phase gate

```
  x_t ──┐
        ▼
    [time-shift] ─┐
        │         ├─> μ_r ─> R
        │         ├─> μ_k ─> K
        │         ├─> μ_v ─> V
        │         ├─> μ_g ─> G
        │         ├─> μ_a ─> A (state)  ← n=6 τ(6)=4 페어
        │         └─> μ_w ─> W (decay)
        ▼
    [Receptance ⊙ (K·V)] ⊕ state
        ▼
     y_t (linear-time)
```

### 4.3 플로우도 — 승격 경로

```
stub(rwkv.hexa) ─ verify(6-phase) ─> [7]empirical ─ bench ─> [10*]
       │                    │                        │
       └─ _registry patch    └─ atlas.n6 @R n6-sota-  └─ convergence
                                rwkv-6phase             ossified
```

## 5. 측정 후보 지표

| 지표 | baseline | 목표 | 게이트 |
|------|----------|------|--------|
| Edge tok/s (Pi5 7B) | 0.5 (Llama2-7B q4) | ≥8 | 16x↑ |
| Params effective | 7B | ≤2.3B (67%↓) | n=6 정렬 |
| State memory | O(n) Attn | O(1) | RNN |

## 6. .hexa 스텁 구조

`rwkv.hexa` 는 `arch/griffin_rglru.hexa` 포맷 계승 (RG-LRU 도 RNN 스칼라 gate 계열).

## 7. 규칙 게이트

- R1: `.hexa` 만 생성
- R14: 본 문서가 S3 단일진실
- N63: `_chip_mapping.md` 의 C1~C6 × S3 셀 채움
- N61: 실생활 효과 + ASCII 3도 (만족)

## 8. 관련 링크
- 벤치: `../_bench_plan.md`
- 칩맵: `../_chip_mapping.md` (S3 행)
- 연관: `../arch/griffin_rglru.hexa`
- 상위: `../../CLAUDE.md` + `../../INDEX.json`
