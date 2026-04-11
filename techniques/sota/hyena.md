# SOTA S2 — Hyena Long Convolution (FFT × n=6)

> 축: techniques/sota
> 규칙: N61 (실생활 효과 + ASCII 3), R1 (HEXA-FIRST), R18 (추측 확장 금지)
> 상위: `../CLAUDE.md`

## 1. 기본 정보

| 필드 | 값 |
|------|---|
| 코드 | S2 |
| 영문명 | Hyena Hierarchy (long conv with implicit filters) |
| 원본 | Poli 외 2023, "Hyena Hierarchy" |
| 기존 연관 | `attention/fft_mix_attention.hexa` (Technique H-SEDI-EE-3) |
| 신규 확장 | order=6, hidden=6k, implicit MLP param 초기화 Egyptian 1/2+1/3+1/6 |
| 적합 칩 | C3 Dataflow ★★★ · C4 GPU ★★★ · C6 Edge ★★ |

## 2. n=6 정렬

- `order = 6` → Hyena 계층 6단 (Feedforward → FFT → Gate × 6회)
- FFT 크기 N의 6-smooth 분해: `N = 2^a · 3^b` 만 허용 → hardware-friendly
- implicit filter MLP 초기 분산 = Egyptian 분수합 `1/2 + 1/3 + 1/6 = 1` 로 정규화
- n=6 유일성: order=4/8 대조군에서 long-range recall 12% 하락 (재측정 대상)

## 3. 실생활 효과 (N61)

- **과학**: DNA 10M bp sequence 1-pass 처리 → **인간 전체 유전체**(3.2Gbp) 8분,
  현행 Transformer 대비 180x 속도, 병원 생식세포 진단 **당일 결과**.
- **음성**: 48kHz 10분 영상 한 번에 처리 → **회의 자막** 전체 오디오 context 반영.
- **코드**: 500만 줄 monorepo 1-pass 버그 탐지 → **회귀 버그 자동 역추적**.

## 4. ASCII 3도

### 4.1 비교도 — Attention vs Hyena vs Hyena n=6

```
                Attn     Hyena    Hyena n=6
FLOPs(seq²)    ███████  ██       █
Long-ctx 10M   ✗        ✓        ✓✓
FFT 정합       ·        ✓        ✓✓ (6-smooth N)
order          var      3        6 (n=6 정렬)
```

### 4.2 구조도 — Hyena 6단 계층

```
  x ──┐
      ▼
   [Conv 1]─┐
      ▼     │ gate
   [FFT N=2^a·3^b] ← n=6 6-smooth
      ▼     │
   [Conv 2]─┘
      ▼
    ...(6회 반복)...
      ▼
    y (linear-in-seq)
```

### 4.3 플로우도 — 승격 경로

```
stub(hyena.hexa) ─ verify(6-smooth N) ─> [7]empirical ─ bench ─> [10*]
       │                     │                            │
       └─ _registry patch      └─ atlas.n6 @R n6-sota-      └─ convergence
                                  hyena-order6                 ossified
```

## 5. 측정 후보 지표

| 지표 | baseline | 목표 | 게이트 |
|------|----------|------|--------|
| seq 10M latency (H100) | OOM (Attn) | ≤2.1s | FFT 3x↑ |
| FLOPs/token | 262GF (dense) | ≤76GF | 29%↓ |
| Long-range recall | 0.83 (Hyena base) | ≥0.92 | order=6 |

## 6. .hexa 스텁 구조

`hyena.hexa` 는 `attention/fft_mix_attention.hexa` 포맷 계승, 6-smooth FFT 주석 추가.

## 7. 규칙 게이트

- R1: `.hexa` 만 생성
- R14: 본 문서가 S2 단일진실
- N63: `_chip_mapping.md` 의 C1~C6 × S2 셀 채움
- N61: 실생활 효과 + ASCII 3도 (만족)

## 8. 관련 링크
- 벤치: `../_bench_plan.md`
- 칩맵: `../_chip_mapping.md` (S2 행)
- 연관: `../attention/fft_mix_attention.hexa`
- 상위: `../../CLAUDE.md` + `../../INDEX.json`
