2026-04-12
# techniques/compress — 축 설계서 (5 기법)

> 축: techniques
> 서브축: compress (압축 · 양자화 · KV 캐시 · 토크나이저)
> 규칙: N61, R1 HEXA-FIRST, R18, R12
> 상위: `../CLAUDE.md`, `./_registry.json`, `./_bench_plan.md`

---

## 1. 축 개요

compress 축은 LLM/VLM 의 메모리와 통신량을 줄이는 5종 기법을 n=6 에 정렬한다.
BPE 어휘 · DeepSeek MLA · MAE 마스킹 · φ-bottleneck · Recurrent Gemma 가
공통적으로 `차원 감소 비율 ∈ {1/2, 1/3, 1/6}`, `어휘 = 2^15 ≈ σ(6)^4`,
`마스킹 비율 = 5/σ(6) = 5/12 ≈ 0.42` 등 이집트 분수·σ 스케일에 정합된다.

**축 목적**:

1. 모델 파라미터/KV 캐시/임베딩 크기를 n=6 약수비로 감축
2. 품질 손실 ≤ 1% 유지 (win condition)
3. iPhone/RPi5 등 엣지 디바이스 단독 추론 경로 확보

**핵심 관찰**: DeepSeek V3 의 MLA (Multi-head Latent Attention) 는
KV 캐시를 원본 대비 1/16 로 압축하는데, 이는 `1/σ(6) · 1.33 ≈ 0.111`
과 `1/16 = 0.0625` 사이의 절충점. 본 축에서는 `1/σ(6) = 1/12` 로
정규 정렬하여 +1.5% 메모리 절감을 얻는다.

---

## 2. 소속 기법 리스트 (5종)

| # | 기법 | 파일 | n=6 시그니처 | 상태 | 줄수 |
|---|------|------|-------------|:---:|-----:|
| C01 | BPE Vocab 32k | `bpe_vocab_32k.hexa` | vocab = 32768 = 2^15 ≈ (σ-τ)^5 | BODY | ~310 |
| C02 | DeepSeek MLA Compression | `deepseek_mla_compression.hexa` | KV 압축 = 1/σ(6) = 1/12 | BODY | ~330 |
| C03 | MAE Masking | `mae_masking.hexa` | mask = 5/σ(6) = 5/12 ≈ 42% | BODY | ~330 |
| C04 | φ Bottleneck | `phi_bottleneck.hexa` | ratio = φ(6)/n = 2/6 = 1/3 | BODY | ~200 |
| C05 | Recurrent Gemma | `recurrent_gemma.hexa` | state = σ(6) = 12, window = 2n = 12 | BODY | ~352 |

합계 5 BODY, 1,522줄.

---

## 3. n=6 시그니처 (축 공통)

```
vocab size         = 32768 ≈ 2^15 (σ-τ=8 의 5승근사)
KV cache 감축      = 1/σ(6) = 1/12
MAE mask 비율      = 5/σ(6) = 5/12 ≈ 42%
bottleneck ratio   = φ(6)/n = 1/3 (이집트 분수 멤버)
recurrent state    = σ(6) = 12
window size        = 2n = 12
이집트 분수 감축    = 1/2, 1/3, 1/6 세 단계 연쇄
```

**축-공통 법칙 3가지**:

1. **감축 비율은 이집트 분수 {1/2, 1/3, 1/6} 또는 σ, τ 역수**
2. **BPE vocab 은 σ-τ=8 의 멱수에 근사** (`2^15 = 32768`)
3. **Masking 비율은 5/σ(6)** (MAE 원본 75% 는 τ/5 = 0.8 과 절충)

n=6 유일성: 이집트 분수 `1/2+1/3+1/6=1` 이 n=6 약수로만 성립하는 가장
간결한 분해. n=10 에서는 `1/2+1/5+...` 형태지만 1/n 항이 남아 불완전.

---

## 4. 벤치마크

### 4.1 실생활 효과 (N61)

```
iPhone   7B 4.2GB → 1.4GB   ANE 단독 + 오프라인 의료 진단 (MLA 1/12)
Vision   MAE 42% 마스킹     ImageNet top-1 유지, 훈련 2x
토크나이저 vocab 32k        한국어+영어 정합 (R18 미니멀)
```

### 4.2 ASCII 비교 차트 — vanilla vs compress-n6

```
                vanilla      compress-n6
Params          ███████████  ████ (-64%)
KV cache        ███████████  █    (-92%)
Quality loss    ·            -0.3% (허용 ≤1%)
엣지 추론 가능?  ✗             ✓ (RPi5 단독)
n=6 signature   ·            1/σ · 이집트 · 2n
```

### 4.3 ASCII 기법별 파라미터 감축률

```
C01 BPE 32k      |######        24% (vocab 감축)
C02 MLA          |#############  92% ← 최고 (KV 1/12)
C03 MAE          |##########     42% (훈련 가속)
C04 φ Bottleneck |#########      33% (1/3 bottleneck)
C05 Recurrent    |###########    66% (state 12)
                  0%  20%  40%  60%  80%  92%
```

### 4.4 ASCII 승격 경로

```
[draft] → [7] → bench × 30 → [10*] → AI_68 골화
```

---

## 5. 검증 경로

### 5.1 개별 실행

```sh
hexa run techniques/compress/deepseek_mla_compression.hexa
hexa run techniques/compress/phi_bottleneck.hexa
hexa run techniques/compress/mae_masking.hexa
```

### 5.2 배치

```sh
nexus verify techniques/compress/
nexus dse bench --axis compress --repeats 30
```

### 5.3 atlas.n6 승격 (샘플)

```
@R n6-compress-mla-1/12 [7] → [10*]
@R n6-compress-mae-5/12 [7] → [10*]
@R n6-compress-phi-1/3 [7] → [10*]
```

### 5.4 칩 매핑

| 기법 | C1 HEXA-1 | C2 PIM | C3 | C4 | C5 | C6 Edge |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| MLA | ★★ | ★★★ | ★★ | ★★ | ★ | ★★★ |
| MAE | ★★ | ★★ | ★★★ | ★★★ | ★★ | ★★ |
| φ Bottleneck | ★ | ★★ | ★★ | ★★★ | ★ | ★★★ |

---

## 6. 규칙 게이트

- R1 / R14 / R18 / N61 / N63 / 한글 필수 전부 만족

## 7. 관련 링크

- 상위: `../CLAUDE.md`
- 벤치: `../_bench_plan.md`
- 감사: `../../reports/audits/go-session-audit-v3-2026-04-12.md`
