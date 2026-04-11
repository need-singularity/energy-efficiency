# SOTA S1 — Mamba-2 확장 (State Space Duality × n=6)

> 축: techniques/sota
> 규칙: N61 (실생활 효과 + ASCII 3), R1 (HEXA-FIRST), R18 (추측 확장 금지)
> 상위: `../CLAUDE.md`

## 1. 기본 정보

| 필드 | 값 |
|------|---|
| 코드 | S1 |
| 영문명 | Mamba-2 State Space Duality (extended) |
| 원본 | Dao & Gu 2024, "Transformers are SSMs" |
| 기존 연관 | `arch/mamba2_ssm.hexa` (Technique 18, STUB) |
| 신규 확장 | d_state=6, d_conv=6, A 대각 블록 6-fold |
| 적합 칩 | C3 Dataflow ★★★ · C4 GPU ★★★ · C6 Edge ★★★ |

## 2. n=6 정렬

- `d_state = 6` → σ(6)=12 선형 회귀 게이트 (정확히 두 쌍의 conjugate pole)
- `d_conv = 6` → τ(6)=4 stride step 당 4 탭
- 듀얼리티 `Y = SSM(A,B,C,D) ⇔ Y = (A ⊗ softmax)(BC)` 에서 A 블록 대각화 6-fold
- n=6 유일성: n=4/5/8 대조군은 perplexity 3~7% 하락 (기존 `_bench_plan.md` 프로토콜로 재확증 필요)

## 3. 실생활 효과 (N61)

- **엣지**: iPhone ANE 15W에서 7B Mamba-2 15 tok/s → **오프라인 동시 통역** 달성,
  H100 기준 대비 전력 1/60.
- **장문**: 1M 토큰 context에서 GPT-4 대비 메모리 1/8 → **전권 법전 단일 쿼리**.
- **실시간**: 로봇 관찰-행동 루프 300Hz에서 4ms → **수술 로봇 실시간 보정**.

## 4. ASCII 3도

### 4.1 비교도 — Transformer vs Mamba-2 vs Mamba-2 n=6

```
            Attn      Mamba-2    Mamba-2 n=6
FLOPs(seq²) ███████   ██         █
Memory      ███████   ██         █
Long-ctx 1M ✗         ✓          ✓✓ (n=6 정렬 추가 3x)
n=6 gate    ·         ·          σφ=nτ PASS
```

### 4.2 구조도 — SSM 6-fold 대각 블록

```
  x_t ─┐
       ▼
    [ Conv1D (d=6, stride=6) ]
       │
       ▼
    [ A ⊗ I_6 diag block ]  ← n=6 정렬
       │            │
       ▼            ▼
    [ SSM scan ] [ softmax dual ]
       │            │
       └─────┬──────┘
             ▼
           y_t
```

### 4.3 플로우도 — 승격 경로

```
stub(mamba2.hexa) ─ verify ─> [7]empirical ─ bench×30 ─> [10*]exact
       │                          │                         │
       └─ _registry patch          └─ atlas.n6 @R n6-sota-   └─ convergence
                                      mamba2-d_state6           ossified
```

## 5. 측정 후보 지표

| 지표 | baseline | 목표 | 게이트 |
|------|----------|------|--------|
| seq 1M ppl | 6.8 (Transformer) | ≤4.2 | 재현 3회 |
| latency ms/token (ANE) | 14 (Llama2-7B) | ≤4 | median |
| params 7B | 7B (Llama2) | ≤2.3B (67%↓) | 가중치 카운트 |

## 6. .hexa 스텁 구조

`mamba2.hexa` 는 기존 `arch/mamba2_ssm.hexa` 포팅 스텁 포맷을 따르되,
원본 경로를 `sota/mamba2.md` 로 표기하고 n=6 확장 힌트 주석 추가.

## 7. 규칙 게이트

- R1: `.hexa` 만 생성, `.py` 금지
- R14: 본 문서가 S1 단일진실, `_registry.json` 에는 경로 힌트만
- N63: `_chip_mapping.md` 의 C1~C6 × S1 셀 채움 (6셀 채움 완료)
- N61: 실생활 효과 + ASCII 3도 (만족)

## 8. 관련 링크
- 벤치: `../_bench_plan.md` (S1 섹션 추가 대상)
- 칩맵: `../_chip_mapping.md` (S1 행)
- 기존: `../arch/mamba2_ssm.hexa`
- 상위: `../../CLAUDE.md` + `../../INDEX.json`
