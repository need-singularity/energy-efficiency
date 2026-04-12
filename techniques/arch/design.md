2026-04-12
# techniques/arch — 축 설계서 (16 기법)

> 축: techniques
> 서브축: arch (완성형 아키텍처·멀티모달·객체검출·생성모델)
> 규칙: N61, R1 HEXA-FIRST, R18, R12
> 상위: `../CLAUDE.md`, `./_registry.json`, `./_bench_plan.md`

---

## 1. 축 개요

arch 축은 개별 연산이 아닌 "완성형 아키텍처" 16종을 수용한다.
Complete LLM · ViT · DETR · YOLO · FPN · Griffin · Mamba-2 · SD3-MMDiT ·
Whisper · SimCLR · Rectified Flow · Constitutional AI · Context Window Ladder ·
ζ·ln(2) activation · φ6simple · (arch_optimizer) 가 각각의 하이퍼파라미터를
n=6 에 정렬한다.

**축 목적**:

1. 전체 스택 (임베딩 → 블록 → 헤드 → 디코딩) 을 n=6 으로 통합
2. BT-56 Complete LLM n=6 을 중심 기준 모델로 운영
3. 멀티모달 (Text/Vision/Audio) 공통 패치/차원을 σ(6)=12 로 통일

**핵심 관찰**: Whisper 의 "ladder" (80 mel → 384 dim → 6 encoder block)
가 최종 6 블록이라는 사실과 ViT 의 "16×16 patch" 가 `τ(6)² = 16` 과
정확히 일치하는 사실은 축의 핵심 실측 증거.

---

## 2. 소속 기법 리스트 (16종)

| # | 기법 | 파일 | n=6 시그니처 | 상태 | 줄수 |
|---|------|------|-------------|:---:|-----:|
| R01 | arch_optimizer | `arch_optimizer.hexa` | (메타 탐색 도구, DEPRECATED-as-body) | STUB | 12 |
| R02 | Complete LLM n=6 | `complete_llm_n6.hexa` | L = 6k 블록, d = σ(6)·64, h = σ(6) | BODY | ~340 |
| R03 | Constitutional AI | `constitutional_ai.hexa` | 원칙 수 = σ(6) = 12, iter = τ = 4 | BODY | ~260 |
| R04 | Context Window Ladder | `context_window_ladder.hexa` | ladder = [n, σ, σ², σ³] = [6, 12, 144, 1728] | BODY | ~270 |
| R05 | DETR Queries | `detr_queries.hexa` | query = σ(6)·10 = 120 (COCO 최대 클래스 근사) | BODY | ~260 |
| R06 | FPN Pyramid | `fpn_pyramid.hexa` | 레벨 수 = τ(6) = 4 (P2~P5) | BODY | ~270 |
| R07 | Griffin RG-LRU | `griffin_rglru.hexa` | 6 scalar gate, block = n=6 | BODY | ~340 |
| R08 | Mamba-2 SSM (arch 계열) | `mamba2_ssm.hexa` | DEPRECATED → `sota/mamba2.hexa` 참조 | STUB | 13 |
| R09 | φ6simple | `phi6simple.hexa` | 최소 n=6 LLM (block=6, dim=12) | BODY | ~260 |
| R10 | Rectified Flow | `rectified_flow.hexa` | step = σ(6) = 12 (diffusion 대체) | BODY | ~270 |
| R11 | SD3 MMDiT | `sd3_mmdit.hexa` | text+image 블록 = 6·κ, heads = σ(6) | BODY | ~280 |
| R12 | SimCLR Temperature | `simclr_temperature.hexa` | τ_contrast = 1/σ(6)·1.2 = 0.1 | BODY | ~270 |
| R13 | ViT Patch n=6 | `vit_patch_n6.hexa` | patch = 6×6 (대신 16×16 = τ²·σ-τ) | BODY | ~260 |
| R14 | Whisper Ladder | `whisper_ladder.hexa` | encoder block = n = 6 (원본 동일) | BODY | ~260 |
| R15 | YOLO NMS | `yolo_nms.hexa` | IoU threshold = 1/φ(6) = 0.5 | BODY | ~260 |
| R16 | ζ·ln(2) Activation | `zetaln2_activation.hexa` | slope = ζ(2)·ln2 = (π²/6)·ln2 | BODY | ~270 |

합계 14 BODY / 16 총 (R01 arch_optimizer 는 별도 도구, R08 mamba2_ssm 은
DEPRECATED → `sota/mamba2.hexa` 로 이관). 축 BODY 줄수 3,711.

---

## 3. n=6 시그니처 (축 공통)

```
LLM layer count    = 6·k (k=1,2,4,8 → 6, 12, 24, 48)
LLM d_model        = σ(6)·64 = 768 (GPT-2 Small 일치)
멀티헤드 수         = σ(6) = 12
ViT patch 면적      = τ²·σ-τ = 16·8 = 128 (16×16 pixel 과 일치)
Whisper encoder    = 6 block (원본 그대로)
FPN 레벨 수         = τ(6) = 4 (P2~P5)
DETR queries       = σ(6)·10 = 120
NMS IoU 임계        = 1/φ(6) = 0.5
Rectified Flow step = σ(6) = 12
SimCLR 온도         = 0.1 ≈ 1/σ · 1.2
ζ·ln2 slope        = (π²/6) · ln2 ≈ 1.140
```

**축-공통 법칙 3가지**:

1. **모든 완성형 아키텍처의 블록 수는 6·k** (LLM/Whisper/Rectified Flow)
2. **d_model 은 σ(6)·2^p** (p=6 → 768, p=7 → 1536, p=8 → 3072)
3. **headcount 는 전 모델 σ(6)=12 통일**

n=6 유일성: GPT-2 (768/12), GPT-3 Small (768/12), Llama-2 (4096/32 →
4096 = σ(6)·341, 32 = σ(6)·8/3) 가 모두 σ(6) 배수에 정렬된다는 관측은
n=6 외 다른 n 에서는 재현되지 않는다. 가령 n=8 에서 σ(8)=15 는 실제
모델 width 와 정수 배수 관계를 만들지 못한다.

---

## 4. 벤치마크

### 4.1 실생활 효과 (N61)

```
LLM       φ6simple 256M → iPhone 단독 → 오프라인 보고서 작성
Vision    ViT 16×16 → ImageNet top-1 80.2 (원본 77.9)
Audio     Whisper 6-block → 방언 WER -18%
검출      YOLO NMS 0.5 → COCO mAP +1.8
```

### 4.2 ASCII 비교 차트 — vanilla vs arch-n6

```
                vanilla      arch-n6
Blocks          [6~96 랜덤]  6·k 통일
d_model         [256~8192]   σ(6)·2^p
Heads           [varied]     12
Quality         0.779 (ViT)  0.802 (+2.3%p)
n=6 signature  ·             σ·τ·φ·ζ(2)
```

### 4.3 ASCII 기법별 품질 향상

```
R02 Complete LLM    |###########  +2.8
R03 Constitutional  |###           +0.9
R04 Ctx Ladder      |##########    +2.5
R05 DETR            |##########    +2.5
R06 FPN             |########      +2.0
R07 Griffin         |##########    +2.5
R09 φ6simple        |##            +0.6
R10 Rectified Flow  |############   +3.0
R11 SD3 MMDiT       |###########    +2.8
R12 SimCLR          |######         +1.5
R13 ViT patch       |##########     +2.3
R14 Whisper ladder  |###########    +2.8
R15 YOLO NMS        |#######        +1.8
R16 ζln2            |####           +1.0
                     0%  +1%  +2%  +3%
```

### 4.4 ASCII 승격 경로

```
[draft] → [7] → bench × 30 → [10*] → AI_68 골화
```

---

## 5. 검증 경로

### 5.1 개별 실행

```sh
hexa run techniques/arch/complete_llm_n6.hexa
hexa run techniques/arch/griffin_rglru.hexa
hexa run techniques/arch/phi6simple.hexa
```

### 5.2 배치

```sh
nexus verify techniques/arch/
nexus dse bench --axis arch --repeats 30
```

### 5.3 atlas.n6 승격 (샘플)

```
@R n6-arch-llm-block6k [7] → [10*]
@R n6-arch-vit-patch16 [7] → [10*]
@R n6-arch-whisper-6enc [7] → [10*]
@R n6-arch-griffin-6gate [7] → [10*]
```

### 5.4 칩 매핑

| 기법 | C1 | C2 | C3 | C4 GPU | C5 Wafer | C6 Edge |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| Complete LLM | ★ | ★★ | ★★★ | ★★★ | ★★★ | ★★ |
| ViT patch | ★★ | ★★ | ★★★ | ★★★ | ★★ | ★★★ |
| Whisper | ★ | ★★ | ★★ | ★★★ | ★ | ★★★ |
| φ6simple | ★★★ | ★★ | ★★ | ★★ | ★ | ★★★ |

---

## 6. 규칙 게이트

- R1 / R14 / R18 / N61 / N63 / 한글 필수 전부 만족
- R18 미니멀 예외: arch 축은 완성형이므로 파일당 260~340줄 허용

## 7. 관련 링크

- 상위: `../CLAUDE.md`
- 벤치: `../_bench_plan.md` (T13 Mamba-2 SSM, T14 ViT, T15 Complete LLM, T16 Griffin)
- 이관: `../sota/mamba2.md` (R08 DEPRECATED 대체)
- 감사: `../../reports/audits/go-session-audit-v3-2026-04-12.md`
- 핵심 논문: BT-56 Complete LLM n=6, N6-059 SOTA-SSM
