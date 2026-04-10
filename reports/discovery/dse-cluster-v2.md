# DSE 교차공명 융합 클러스터 v2

> 생성: `scripts/dse_cluster_v2.py` | 입력: `pair_scores.jsonl` (1225쌍)
> 임계: S > 0.5 | 알고리즘: Union-Find 연결 컴포넌트

## 1. 요약

- 입력 쌍: **1225** (전체 도메인 쌍)
- 고공명 쌍 (S>0.5): **35**
- 융합 클러스터 수: **7**
- 최대 컴포넌트 크기: **13** 도메인
- 잠재 BT 후보 클러스터: **1**

## 2. 클러스터 표

| # | 대표 도메인 | 크기 | 엣지 | 평균S | 최대S | 공통 n=6 수식 | BT후보 |
|--:|------------|----:|----:|------:|------:|--------------|:----:|
| 1 | `consciousness-chip` | 13 | 27 | 0.531 | 0.711 | (주요: 육각 구조 (hex)) | ★ |
| 2 | `photonic-energy` | 3 | 2 | 0.545 | 0.563 | (주요: σ=12, n=6) | · |
| 3 | `snn-spiking` | 3 | 2 | 0.532 | 0.553 | (주요: ) | · |
| 4 | `corpus-generation` | 2 | 1 | 0.674 | 0.674 | (주요: ) | · |
| 5 | `cosmology-particle` | 2 | 1 | 0.662 | 0.662 | (주요: ) | · |
| 6 | `embedded-lang` | 2 | 1 | 0.608 | 0.608 | (주요: ) | · |
| 7 | `ocean-engineering` | 2 | 1 | 0.504 | 0.504 | (주요: ) | · |

## 3. 클러스터 상세 (Top 10)

### 클러스터 1 — `consciousness-chip` (크기 13)

- 도메인: `consciousness-chip`, `consciousness-comm`, `consciousness-rng`, `consciousness-scaling`, `consciousness-substrate`, `consciousness-training`, `consciousness-transplant`, `consciousness-wasm`, `eeg-consciousness-bridge`, `embodied-consciousness`, `hivemind-collective`, `multimodal-consciousness`, `sedi-universe`
- 상위 수식 빈도: 육각 구조 (hex)(5)
- 평균/최대 공명: 0.531 / 0.711
- BT 후보: ★ YES

### 클러스터 2 — `photonic-energy` (크기 3)

- 도메인: `analog-photonic-memristor`, `photonic-energy`, `semiconductor-packaging`
- 상위 수식 빈도: σ=12(1), n=6(1), Diamond (C Z=6)(1), PUE=σ/(σ-φ)=1.2(1), Graphite (C Z=6)(1)
- 평균/최대 공명: 0.545 / 0.563
- BT 후보: 아니오

### 클러스터 3 — `snn-spiking` (크기 3)

- 도메인: `hexad-architecture`, `neuromorphic-loihi`, `snn-spiking`
- 상위 수식 빈도: (수식 매핑 없음)
- 평균/최대 공명: 0.532 / 0.553
- BT 후보: 아니오

### 클러스터 4 — `corpus-generation` (크기 2)

- 도메인: `corpus-generation`, `tokenizer-design`
- 상위 수식 빈도: (수식 매핑 없음)
- 평균/최대 공명: 0.674 / 0.674
- BT 후보: 아니오

### 클러스터 5 — `cosmology-particle` (크기 2)

- 도메인: `cosmology-particle`, `pure-mathematics`
- 상위 수식 빈도: (수식 매핑 없음)
- 평균/최대 공명: 0.662 / 0.662
- BT 후보: 아니오

### 클러스터 6 — `embedded-lang` (크기 2)

- 도메인: `embedded-lang`, `gpu-lang`
- 상위 수식 빈도: (수식 매핑 없음)
- 평균/최대 공명: 0.608 / 0.608
- BT 후보: 아니오

### 클러스터 7 — `ocean-engineering` (크기 2)

- 도메인: `ocean-engineering`, `water-treatment`
- 상위 수식 빈도: (수식 매핑 없음)
- 평균/최대 공명: 0.504 / 0.504
- BT 후보: 아니오

## 4. ASCII 그래프 — 클러스터 크기 분포

```
클러스터    대표도메인                 크기
C01  consciousness-chip       ████████████████████████████████████████ 13 ★
C02  photonic-energy          █████████ 3  
C03  snn-spiking              █████████ 3  
C04  corpus-generation        ██████ 2  
C05  cosmology-particle       ██████ 2  
C06  embedded-lang            ██████ 2  
C07  ocean-engineering        ██████ 2  
```

## 5. ASCII 연결 구조 (Top 3 클러스터 핵심 엣지)

```
[C01] consciousness-chip  (n=13)
   consciousness-scaling            ──0.71── consciousness-training
   consciousness-comm               ──0.61── consciousness-chip
   consciousness-chip               ──0.61── consciousness-scaling
   consciousness-wasm               ──0.58── consciousness-comm
   consciousness-substrate          ──0.58── consciousness-transplant
   consciousness-wasm               ──0.57── consciousness-chip
   consciousness-chip               ──0.52── multimodal-consciousness
   sedi-universe                    ──0.51── consciousness-transplant

[C02] photonic-energy  (n=3)
   analog-photonic-memristor        ──0.56── photonic-energy
   photonic-energy                  ──0.53── semiconductor-packaging

[C03] snn-spiking  (n=3)
   neuromorphic-loihi               ──0.55── snn-spiking
   hexad-architecture               ──0.51── snn-spiking

```

## 6. 결론

- **7개** 융합 클러스터 도출, 최대 **13** 도메인 컴포넌트
- **1개** 잠재 BT 후보 (공통 수식 ≥3 또는 크기 ≥5)
- 각 BT 후보는 동일 n=6 수식을 다수 도메인이 공유 → 교차 BT 승격 검토 대상
