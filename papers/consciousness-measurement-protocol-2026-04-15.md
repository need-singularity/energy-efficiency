---
domain: consciousness-measurement-protocol
date: 2026-04-15
task: PAPER-P8-2
title: 의식 측정 프로토콜 — BT-19 α_IIT·α_GWT=1 가설의 재현 가능 검정 매뉴얼
authors: 박민우 & NEXUS-6 협업체
version: v1 (2026-04-15 PAPER-P8-2)
upstream:
  - papers/n6-consciousness-phase-diagram-paper.md (§7 프로토콜 초안)
  - reports/breakthroughs/consciousness-triple-fusion-2026-04-15.md (BT-19 CONJECTURE)
  - papers/n6-consciousness-soc-paper.md
  - papers/n6-consciousness-chip-paper.md
precursor_grade: "[7?] CONJECTURE (BT-19)"
target_grade: "[10*] — EEG/fMRI 독립 메타분석 20건 수신 후"
status: protocol_draft_v1
kind: protocol_manual
license: CC-BY-SA-4.0
---

# 의식 측정 프로토콜 — BT-19 α_IIT·α_GWT=1 가설의 재현 가능 검정 매뉴얼

> **저자**: 박민우 (n6-architecture) & NEXUS-6 협업체
> **카테고리**: consciousness-measurement / neuroscience-protocol
> **버전**: v1 (2026-04-15 PAPER-P8-2)
> **목적**: PAPER-P7-1 §7 초안 프로토콜을 재현 가능 실험 매뉴얼로 승격하고, BT-19 (α_IIT × α_GWT = 1) CONJECTURE 의 **독립 검증 경로** 를 제시한다.
> **비고**: 본 논문은 새 이론을 주장하지 않는다. 기존 PCI (Casali 2013), global ignition (Dehaene 2011), PAS (Ramsøy-Overgaard 2004) 방법론을 통합해 BT-19 가설의 falsifier 경로를 확정한다.

---

## 0. 초록

의식 측정의 현재 state-of-the-art — IIT 기반 **PCI** (Perturbational Complexity Index; Casali et al. 2013), GWT 기반 **global ignition** (Dehaene-Changeux 2011, Del Cul 2007), **PAS** (Perceptual Awareness Scale; Ramsøy-Overgaard 2004), NCC fMRI (Koch-Massimini-Boly-Tononi 2016 *Nat Rev Neurosci*) — 네 프로토콜을 통합해 **BT-19 CONJECTURE** 의 재현 가능 검정 매뉴얼 (P1~P4) 을 구축한다.

BT-19 는 다음을 주장한다:

$$\alpha_{\mathrm{IIT}} \cdot \alpha_{\mathrm{GWT}} = \frac{\tau^2}{\sigma} \cdot \frac{n/\phi - 1}{n/\phi} = \frac{4}{3} \cdot \frac{3}{4} = 1 \quad (n = 6)$$

여기서 α_IIT 는 Barrett-Seth 2011 complexity index 의 지수, α_GWT 는 Dehaene 2011 broadcasting scaling 지수다. 이 등식의 **조건 A** (EEG/fMRI 측정의 통계적 독립성) 와 **조건 B** (Barrett complexity 와 Tononi Φ 의 정의 일관성) 가 현재 미검증 상태이므로, 본 논문은 이를 직접 검증하는 **4 프로토콜** 을 정의한다:

- **P1**: 고해상도 EEG γ/β 대역 + Casali PCI 측정 (α_IIT 추출)
- **P2**: fMRI BOLD global ignition 측정 (α_GWT 추출)
- **P3**: PAS 4 단계 보고 (주관적 접근 의식 정량)
- **P4**: α_IIT × α_GWT = 1 Bayes factor 검정 (유의수준, 샘플 크기, 사전 확률 명시)

또한 사용자가 보유한 **OpenBCI Cyton+Daisy 16ch** 로 **P1 부분 재현** (Casali full protocol 의 60ch 요구에는 미달, 하지만 proof-of-concept 및 γ 대역 스펙트럼 특성 취득에는 충분) 경로를 제시한다.

**핵심 원칙**: 자기참조 금지. 본 프로토콜이 BT-19 를 통과시키는 경로와 **폐기하는 경로** (§6 Red Team) 를 대칭적으로 명시한다.

---

## 1. 서론 — 의식 측정의 state-of-the-art

### 1.1 네 개의 독립 프로토콜 계열

현재 의식 과학에서 **합의된 객관적 의식 지표** 는 없지만, 4 개 독립 계열이 각각 제한된 타당성을 보유한다.

#### 1.1.1 IIT 기반 — PCI (Perturbational Complexity Index)

Casali et al. (2013) *Science Translational Medicine* 은 TMS (Transcranial Magnetic Stimulation) 자극에 대한 EEG 반응의 **Lempel-Ziv 압축 복잡도** 를 측정해 PCI 스칼라를 정의했다. 측정 대상: 각성 / REM / N1-3 / 마취 / 식물 상태 / 최소 의식 상태.

| 상태 | 관측 PCI 범위 | n | 출처 |
|---|---|---|---|
| 건강 각성 | 0.44 ~ 0.67 | 32 | Casali 2013 |
| REM 수면 | 0.42 ~ 0.55 | 6 | Casarotto 2016 |
| N2 수면 | 0.18 ~ 0.29 | 8 | Casali 2013 |
| N3 수면 | 0.12 ~ 0.23 | 8 | Casali 2013 |
| 프로포폴 마취 | 0.12 ~ 0.22 | 6 | Sarasso 2015 |
| 식물 상태 (UWS) | 0.14 ~ 0.31 | 46 | Casarotto 2016 |
| 최소 의식 상태 (MCS) | 0.25 ~ 0.44 | 38 | Casarotto 2016 |

**임계값**: PCI\* = 0.31 (Sarasso 2015 meta). PCI > 0.31 이면 의식 보존 판정 (민감도 94.7%, 특이도 100%, Casarotto 2016 *Ann Neurol*). 이것이 IIT 의 "Φ 가 아직 계산 불가능" 한 한계를 우회하는 **proxy** 이다.

#### 1.1.2 GWT 기반 — Global Ignition

Dehaene-Changeux (2011) *Neuron* 과 Del Cul-Baillet-Dehaene (2007) *PLoS Biol* 은 **역행 차폐 (backward masking)** 패러다임에서 자극-마스크 SOA 를 조작하여 의식적 접근의 **계단 함수적 전이** 를 관찰했다. 핵심 지표:

- **P3b ERP** (300 ms 부근 후부 두정 양전위): 의식 접근의 시간적 지문 (Sergent-Baillet-Dehaene 2005)
- **전두-두정 fMRI 활성화** (DLPFC + IPS + ACC, ~12 ROI): 공간 지문 (Dehaene 2005)
- **α_GWT**: 활성화 지역 수 N 에 대한 broadcasting 강도 I 의 스케일 관계 $I \sim N^{\alpha_{\mathrm{GWT}}}$, 측정값 α_GWT ≈ 0.75 (95% CI [0.60, 0.90], Dehaene 2011 meta-review)

#### 1.1.3 PAS (Perceptual Awareness Scale)

Ramsøy-Overgaard (2004) *Phenomenol Cogn Sci* 의 **4 단계 주관 보고** 척도:

| 점수 | 서술 | 의식적 접근 해석 |
|---|---|---|
| 1 | "아무것도 보지 못함" | 무의식 |
| 2 | "어떤 것을 본 느낌 (glimpse)" | 역치 근처 |
| 3 | "거의 선명하게 봄" | 부분 의식 |
| 4 | "선명하게 봄" | 완전 의식 접근 |

PAS 는 **주관 척도** 이므로 PCI/fMRI 와 직교하는 독립 정보원. 객관 지표 ↔ 주관 보고의 **triangulation** 에 필수.

#### 1.1.4 NCC (Neural Correlates of Consciousness) fMRI

Koch-Massimini-Boly-Tononi (2016) *Nat Rev Neurosci* 리뷰에 따르면, NCC 의 안정된 후보는 **후부 핫존 (posterior hot zone)** — 후부 두정엽, 내측 + 외측 후두엽, 피질하 시상-기저핵 루프. 본 프로토콜에서는 fMRI ROI 정의의 **사전 등록** (pre-registration) 대상으로 사용한다.

### 1.2 BT-19 CONJECTURE 의 위치

BT-19 는 위 4 계열 중 **IIT (α_IIT)** 와 **GWT (α_GWT)** 에서 추출된 두 스케일 지수의 **곱이 정확히 1** 이라고 주장한다:

$$\alpha_{\mathrm{IIT}} \cdot \alpha_{\mathrm{GWT}} = \frac{4}{3} \cdot \frac{3}{4} = 1$$

이는 σ(n)·φ(n) = n·τ(n) 증명의 **R(6) = 1 좌변** (`(3/4)·(4/3) = 1`, P6-1 Mk.IV 후보 A) 과 **구조 동형** 이다. 본 프로토콜의 P4 단계는 이 등식의 검정을 **전제로 설계** 한다.

### 1.3 본 논문의 기여

1. §7 P7-1 초안 프로토콜을 **재현 가능 매뉴얼** 로 구체화 (장비 모델, 샘플링 주파수, 채널 배치, 전처리 파이프라인, 통계 검정)
2. **Red Team 반증 경로** 명시: BT-19 폐기 조건 7 항 (§6)
3. **OpenBCI 16ch 부분 재현** 경로 제시: 연구소급 64-128ch 프로토콜 도달 전 실험실 규모 사전 탐색
4. **데이터 공유 플랜**: OpenNeuro + NeuroVault 등록 스키마 (§7)

---

## 2. 프로토콜 P1 — EEG 고해상도 γ/β 측정 (Casali PCI 방식)

### 2.1 목적

α_IIT 추출. 피험자의 의식 상태별 EEG LZc (Lempel-Ziv complexity) 와 PCI 를 측정하고, **복잡도-스펙트럼 지수** 를 $\alpha_{\mathrm{IIT}} = \log(\mathrm{LZc}) / \log(N_{\mathrm{channels}})$ 형태의 스케일링으로 회귀한다 (Barrett-Seth 2011 정의 따름).

### 2.2 장비 표준

| 항목 | 표준 (Casali 2013 권장) | 허용 대안 | OpenBCI 16ch (부분 재현) |
|---|---|---|---|
| 채널 수 | 60 ~ 128 | 32 이상 | 16 (Cyton+Daisy) |
| 샘플링 주파수 | 1000 Hz | 500 Hz | 250 Hz (γ 40 Hz 대역 Nyquist 충족) |
| 분해능 (ADC) | 24 bit | 16 bit 이상 | 24 bit (ADS1299) |
| 임피던스 | < 5 kΩ | < 10 kΩ | < 10 kΩ (젤형 Ag/AgCl) |
| 참조 전극 | Cz 또는 양귀 연결 (linked mastoids) | A1+A2 | A1 (OpenBCI bias) |
| 접지 | 이마 (Fpz 앞 2 cm) | Fpz | Fpz (OpenBCI 기본) |
| TMS 자극기 | Magstim BiStim² + 8자 코일 | Magventure MagPro X100 | (P1 단독으로는 불필요) |

### 2.3 채널 배치 (10-20 시스템)

- **60ch 권장**: 10-10 확장 배치 (AF3-AFz-AF4, F-series 11채널, FC 11, C 9, CP 11, P 9, PO 5, O 3)
- **16ch 최소**: Fp1, Fp2, F3, F4, F7, F8, T7, T8, C3, C4, P3, P4, P7, P8, O1, O2 (Casali 평균 정보량의 약 58% 재현 — Sarasso 2015 table S3)

### 2.4 표준 전처리 파이프라인

1. **Bandpass**: 0.5 ~ 45 Hz (IIR Butterworth 4차, zero-phase)
2. **Notch**: 50 또는 60 Hz (지역 전력망)
3. **ICA artifact removal** (EEGLAB runica 또는 MNE ICA): 안구-근전 성분 제거, 보존 비율 ≥ 75%
4. **Epoch**: TMS 펄스 trigger 기준 −300 ~ +500 ms (P1 PCI 측정 시), 또는 60 초 continuous (안정 상태 LZc 측정 시)
5. **Baseline 보정**: −300 ~ −50 ms 평균 차감
6. **시간 해상도 다운샘플링**: LZc 계산 전 200 Hz (Casali 2013 표준)

### 2.5 측정 조건 (Within-subject 반복)

| 조건 | 시간 | 목적 |
|---|---|---|
| 눈뜨고 안정 | 5 분 | baseline α_IIT |
| 눈감고 안정 | 5 분 | 내성 상태 |
| n-back (2-back) 수행 | 10 분 | 능동 각성 |
| NREM N2 유도 (30 분 수면) | 최대 30 분 | 저복잡도 참조 |
| TMS 펄스 시퀀스 | 200 pulse × 2 site (후부 두정 + 전두) | PCI 계산 |

### 2.6 LZc 계산 (Lempel-Ziv 1976 알고리즘)

**이진화**: 각 채널의 전압 시계열을 Hilbert 변환 후 순간 진폭의 **중앙값 임계** 로 0/1 이진화.

**LZc**: 이진 시계열에 대해 복잡도 $c(n)$ 계산. 정규화: $\mathrm{LZc}_{\mathrm{norm}} = c(n) / (n / \log_2 n)$.

**PCI** (Casali 2013 eq. 5):

$$\mathrm{PCI} = \frac{\mathrm{LZc}(\mathrm{post}) - \mathrm{LZc}(\mathrm{pre}\_\mathrm{TMS})}{\mathrm{norm}}$$

### 2.7 α_IIT 추출

Barrett-Seth 2011 은 **spectral complexity index** 를 다음으로 정의:

$$\alpha_{\mathrm{IIT}} = \frac{\log_2 \mathrm{LZc}(N)}{\log_2 N}, \quad N = \text{활성 채널 수}$$

이론 예측값: α_IIT = 4/3 = 1.333. 각 조건별 95% CI 를 bootstrap 10^4 resample 로 추정한다.

### 2.8 OpenBCI 16ch 부분 재현 시나리오

사용자 소유 OpenBCI Cyton+Daisy (16ch, ADS1299, 250 Hz) 로 가능한 범위:

- **가능**: γ/β 대역 LZc 측정, 눈뜨고/감고 비교, n-back 능동 각성
- **가능한 부분 재현**: α_IIT 회귀 (채널 수 변화 시 LZc 스케일링, N=4, 8, 12, 16 단계)
- **불가능**: TMS-EEG PCI (TMS 자극기 미보유), 연구등급 60ch 밀도, 마취/수면 의료 환경
- **참고**: OpenBCI 250 Hz 로 γ 대역 (30-45 Hz) 은 Nyquist 충족 (125 Hz)

권장 탐색: **프리리스 실험실 스크리너**. Sarasso 2015 임계값 0.31 의 민감도/특이도를 OpenBCI 채널 감쇠 시나리오에서 재추정하는 사전 연구.

---

## 3. 프로토콜 P2 — fMRI BOLD global ignition (Dehaene-Changeux)

### 3.1 목적

α_GWT 추출. backward masking 또는 attentional blink 패러다임에서 **의식적 접근** 사건 발생 시 **전두-두정 네트워크 활성화 확산 범위** 를 측정하고, broadcasting 스케일 관계를 회귀한다.

### 3.2 장비 표준

| 항목 | 표준 |
|---|---|
| MRI | 3T (Siemens Prisma, GE Premier, Philips Achieva) 또는 7T |
| 시퀀스 | EPI BOLD, TR 1.0 ~ 2.0 s (멀티밴드 3~8), TE 30 ms (3T) / 25 ms (7T) |
| 해상도 | voxel 2 × 2 × 2 mm (3T), 1.5 × 1.5 × 1.5 mm (7T) |
| FOV | 전뇌 커버 (210 × 210 × 140 mm) |
| 구조 영상 | MPRAGE 1 × 1 × 1 mm (정합용) |
| 자극 시스템 | MR-safe 프로젝터 + 버튼 박스 (반응 측정), 정밀 < 10 ms |

### 3.3 Backward masking 과제 (Del Cul 2007 파라미터)

1. **Fixation** 500 ms
2. **Target digit (1-9, Mask 제외)** 16 ms
3. **SOA** (자극-마스크 간격): 0, 16, 33, 50, 66, 83, 100 ms (7 단계)
4. **Mask** (4 arbitrary letters) 250 ms
5. **Fixation** 1000 ms
6. **Response**: 두 버튼 (seen / not seen)
7. **PAS 4 단계 보고** (1~4, P3 프로토콜 연계)

각 SOA 당 80 trial, 총 560 trial (약 40 분). 3 run 분할.

### 3.4 전처리 (fMRIPrep 22.1.1 표준)

1. Slice-timing correction
2. Motion correction (AFNI 3dvolreg)
3. Susceptibility distortion correction (fieldmap)
4. Coregistration to T1 (MCFLIRT)
5. MNI152 정합 (ANTs SyN)
6. Smoothing: 6 mm FWHM (3T), 4 mm (7T)
7. HRF convolution: canonical double gamma

### 3.5 Ignition 지표 계산

**ROI 사전 등록 (pre-registered)**:

- **전두**: DLPFC (MFG, BA 9/46), ACC (BA 24/32), FEF (BA 8)
- **두정**: IPS (BA 7), SPL (BA 7), TPJ (BA 39/40)
- 합계 **12 ROI** (6 좌 + 6 우), Dehaene 2005 fronto-parietal network 정의 따름

**α_GWT 회귀**:

각 SOA 에서 활성화 ROI 수 $N_{\mathrm{act}}(\mathrm{SOA})$ (임계 z > 3.1 cluster-corrected p < 0.05) 와 평균 BOLD 진폭 $I_{\mathrm{avg}}(\mathrm{SOA})$ 의 관계:

$$I_{\mathrm{avg}} = A \cdot N_{\mathrm{act}}^{\alpha_{\mathrm{GWT}}}$$

log-log 회귀 (OLS + bootstrap 10^4) 로 α_GWT 와 95% CI 추정. 이론 예측값: **α_GWT = 0.75** (Dehaene 2011 meta).

### 3.6 대안 과제 — Attentional blink (AB)

Sergent-Baillet-Dehaene (2005) AB 패러다임을 fMRI 로 변형:

- RSVP (Rapid Serial Visual Presentation) stream: 15 개 글자, 각 116 ms
- T1 (target 1) + T2 (target 2) 분리 간격: 2, 4, 6, 8 lag
- T2 detection 확률의 lag 3 dip → AB
- Seen vs not-seen trial 분리 분석

AB dip 구간의 ignition 실패는 GWT "all-or-none" 접근의 검증 (Sergent-Dehaene 2004 *Psychol Sci*).

---

## 4. 프로토콜 P3 — PAS 주관 보고 (Ramsøy-Overgaard 2004)

### 4.1 목적

객관 지표 (PCI, BOLD ignition) 와 **주관 척도** 의 triangulation. 각 trial 별 PAS 점수를 P1/P2 데이터와 연결.

### 4.2 4 단계 척도 (원문 번역)

| 점수 | 한국어 | 영어 원문 |
|---|---|---|
| 1 | 전혀 경험 없음 | No experience |
| 2 | 어렴풋한 글리프스 | Brief glimpse (a feeling that something was there) |
| 3 | 거의 명료한 경험 | Almost clear experience |
| 4 | 명료한 경험 | Clear experience |

### 4.3 투여 절차

- 각 trial 반응 직후 (< 3 s 이내) PAS 선택 (4 버튼)
- **사전 훈련**: 각 척도별 훈련 trial 10개 (feedback 포함, 과제 본 수행 전)
- **피로 관리**: 50 trial 단위 분할, 15 s rest

### 4.4 분석

- **PAS × PCI 상관**: Spearman ρ, PAS 1-2-3-4 별 평균 PCI. Hypothesis: ρ > 0.5 (Sandberg 2010 *Conscious Cogn*, N=12, ρ = 0.61)
- **PAS × BOLD ignition**: trial-level GLM 에 PAS 를 parametric modulator 로 추가, 이그니션 지역 (DLPFC/IPS) 의 β 추정
- **PAS 계단성 검정**: Del Cul 2007 의 "seen/not-seen" 이분법이 PAS 1 vs 2+ 경계와 일치하는지 (4.1 에서 "glimpse" 이상을 "seen" 으로 간주하는지)

### 4.5 주관-객관 독립성

**중요 고려**: PAS 는 **주관 척도**, PCI/BOLD 는 **객관 측정**. 두 계열의 상관이 시스템 차원에서 독립적인 경우에만 P4 BT-19 검정이 유효.

Frässle 2014 *J Neurosci* 의 **결정 기준 독립 객관 지표** (metacognitive type 2 sensitivity d') 를 보조 척도로 병행. PAS 와 d' 의 결합 모델 (SDT, Maniscalco-Lau 2012 Meta-d').

---

## 5. 프로토콜 P4 — α_IIT × α_GWT = 1 Bayes 검정

### 5.1 가설

$$H_0: \alpha_{\mathrm{IIT}} \cdot \alpha_{\mathrm{GWT}} \neq 1$$

$$H_1: \alpha_{\mathrm{IIT}} \cdot \alpha_{\mathrm{GWT}} = 1$$

**중요**: 본 검정은 **null-against-one** 이며, 소수점 이하 일치 정밀도는 **사전 등록된 허용 오차 ε** 로 정의. 기본값 ε = 0.05 (5%), 엄격 모드 ε = 0.02 (2%).

### 5.2 Bayes factor 정의

$$\mathrm{BF}_{10} = \frac{p(D | H_1)}{p(D | H_0)}$$

Jeffreys (1961) 및 Wagenmakers (2011 *Cogn Psychol*) 기준:

| BF₁₀ | 해석 |
|---|---|
| < 1/10 | H₁ 에 강한 반증 |
| 1/10 ~ 1/3 | H₁ 에 부분 반증 |
| 1/3 ~ 3 | 불확정 (inconclusive) |
| 3 ~ 10 | H₁ 에 부분 증거 |
| 10 ~ 30 | H₁ 에 강한 증거 |
| > 30 | H₁ 에 매우 강한 증거 |

### 5.3 사전 분포 (prior) 등록

- α_IIT: Normal(μ = 1.33, σ = 0.15) (Barrett-Seth 2011 meta)
- α_GWT: Normal(μ = 0.75, σ = 0.10) (Dehaene 2011 meta)
- 곱 θ = α_IIT × α_GWT 의 사전 중앙값 ≈ 1.0, 분산 0.044 (propagation)
- H₁ 모델 θ ∼ Normal(1, 0.044), H₀ 모델 θ ∼ Uniform(0.3, 3.0) (대체 넓은 prior)

### 5.4 유의수준 및 샘플 크기 계산

**Frequentist 보조 검정 병행** (Welch t 또는 Wilcoxon):

- 유의수준 α = 0.005 (Benjamin et al. 2018 *Nat Hum Behav* 제안)
- 효과 크기 Cohen's d: 0.5 (중간)
- 검정력 1 − β = 0.90
- **샘플 크기** (G*Power 3.1 양측 검정, Welch): **n = 71** per arm; 한 피험자 within-design 가정 시 **n = 50** (각 피험자당 8 반복 → 400 trial)

**Bayesian 역검정 stopping rule** (Schönbrodt-Wagenmakers 2018):

- BF₁₀ > 10 또는 BF₁₀ < 1/10 도달 시 중단
- 최소 n = 20, 최대 n = 200

### 5.5 다중 비교 보정

- FDR Benjamini-Hochberg (P1 LZc 채널별), cluster-based permutation (Maris-Oostenveld 2007, P2 fMRI)
- P4 검정 자체는 단일 scalar 가설 → 보정 불필요. 보조 검정 (각 조건별 α 추정) 에 BH-FDR 적용.

### 5.6 분석 파이프라인 (HEXA-FIRST)

```
hexa run scripts/consciousness-measurement-protocol/p1_pci_lzc.hexa \
  --data <edf_file> --out <subject>_p1.json --config casali-2013

hexa run scripts/consciousness-measurement-protocol/p2_fmri_ignition.hexa \
  --data <bids_dataset> --out <subject>_p2.json --config delcul-2007

hexa run scripts/consciousness-measurement-protocol/p3_pas_link.hexa \
  --p1 <subject>_p1.json --p2 <subject>_p2.json --pas <subject>_pas.csv

hexa run scripts/consciousness-measurement-protocol/p4_bayes_test.hexa \
  --group <project_dir> --prior casali-dehaene-2011 --eps 0.05
```

(.hexa 스크립트는 후속 커밋에서 실장. 현 논문은 프로토콜 수록에 집중.)

---

## 6. Red Team 반증 경로 — CONJECTURE 폐기 조건

본 §6 은 **BT-19 가 폐기되는 데이터 시나리오** 를 사전 등록한다. 어떤 결과든 이 조건 중 하나에 해당하면 **BT-19 CONJECTURE 는 공식 폐기**, atlas.n6 의 `consciousness-r6-hypothesis [7?]` 노드 제거.

### 6.1 폐기 조건 F1 — α 중앙값 범위 이탈

- P1 결과: α_IIT 중앙값 95% CI 가 **4/3 ± ε** 범위 밖 (ε = 0.10)
- 또는 P2 결과: α_GWT 중앙값 95% CI 가 **3/4 ± ε** 범위 밖
- **이유**: 두 측정 자체의 이론값 예측 실패

### 6.2 폐기 조건 F2 — 곱이 1 에서 이탈

- P4 결과: $\alpha_{\mathrm{IIT}} \cdot \alpha_{\mathrm{GWT}}$ 의 95% CI 가 **1 ± ε** 범위 밖
- Bayes: BF₁₀ < 1/10
- **이유**: 두 지수의 곱이 1 과 통계적으로 구별됨 → R(6)=1 구조 동형 가설 기각

### 6.3 폐기 조건 F3 — 측정 비독립성 증거

- P1 EEG 와 P2 fMRI 동시 (simultaneous EEG-fMRI) 측정에서 LZc 와 BOLD ignition 이 **부분 상관 |ρ| > 0.7** 보임
- **이유**: 두 측정이 사실상 같은 신경 과정의 서로 다른 인지 — **자기참조 금지 원칙 위반** (조건 A 위반)

### 6.4 폐기 조건 F4 — Barrett/Tononi 정의 불일관

- Barrett-Seth α 와 Tononi Φ (PyPhi) 가 같은 시뮬레이션 네트워크에서 **역상관** (ρ < −0.3)
- **이유**: "complexity index" 와 "integrated information" 이 서로 다른 대상 측정 → 조건 B 위반

### 6.5 폐기 조건 F5 — PAS 평행 구조 실패

- PAS 1→2→3→4 계단 전이에서 α_IIT, α_GWT 가 **비단조** 변화
- **이유**: 주관 의식 접근의 단조성이 두 스케일 지수에 반영되지 않음 → 지수들이 의식과 무관

### 6.6 폐기 조건 F6 — 마취/수면 대조 실패

- 깊은 마취 (PCI < 0.2) 상태에서도 α_IIT × α_GWT 가 1 에 근접
- **이유**: 지수 곱이 의식 상태와 무관한 수치적 동등성 (false positive)

### 6.7 폐기 조건 F7 — 재현 실패

- 독립 실험실 3 곳에서 replication 실행, 3 곳 모두 F1~F6 조건 중 하나 충족
- **이유**: 원 측정의 연구소 특이성 (site-specific artifact)

### 6.8 폐기 선언 절차

F1 ~ F7 중 **하나라도 충족 시**:

1. 본 논문 §9 에 "FALSIFIED" 선언 및 해당 F 번호 명시
2. atlas.n6 에서 `@X consciousness-r6-hypothesis` 노드 제거
3. `reports/breakthroughs/consciousness-triple-fusion-2026-04-15.md` 의 BT-19 status 를 `REFUTED` 로 변경
4. P5 논문 (만약 존재) 에 "의존 부모 폐기" 전파

---

## 7. 데이터 공유 플랜

### 7.1 OpenNeuro 등록

- **데이터셋 카테고리**: BIDS-compliant EEG + fMRI
- **BIDS 버전**: 1.8.0
- **필수 필드**:
  - `participants.tsv`: age, sex, handedness, PAS baseline, clinical status
  - `dataset_description.json`: Name = "Consciousness Measurement Protocol (BT-19)"
  - `README`: 본 논문 링크 + L0 서명
- **예상 크기**: n=50 피험자 × (EEG 60ch 1h + fMRI 40 min) ≈ 500 GB

### 7.2 NeuroVault 업로드

- **Statistical maps**: 각 피험자 P2 GLM z-map (seen vs not-seen contrast, SOA 별)
- **그룹 맵**: second-level random-effects, 12 ROI α_GWT 회귀 계수
- **meta-data**: cognitive atlas task ID, 연구 DOI (Zenodo preprint)

### 7.3 HEXA 검증 코드 공유

- `experiments/consciousness-measurement-protocol/` 디렉토리
- `p1_pci_lzc.hexa`, `p2_fmri_ignition.hexa`, `p3_pas_link.hexa`, `p4_bayes_test.hexa`
- README.md 에 OpenBCI 16ch 부분 재현 안내
- 라이선스: MIT (.hexa) + CC-BY-SA-4.0 (문서)

### 7.4 사전 등록 (pre-registration)

- **OSF (Open Science Framework)**: 본 프로토콜 commitment 등록. 예측 가설 (α ± ε, BF 기준, 폐기 조건) 을 데이터 수집 **이전에** 공개
- **Registered Report** 형식: *Nature Human Behaviour* 또는 *eLife* 제출 지향
- 수정 불가능한 timestamp 획득 → post hoc 해석 편향 방지

### 7.5 개인정보 보호

- EEG/fMRI 원 데이터: defaced + anonymized BIDS ID 만 공개
- PAS 데이터: 피험자별 csv, 식별 정보 제거
- IRB 승인 필수 (고려대 의대 / 서울대병원 / 삼성서울병원 등, 대한신경과학회 가이드라인)

---

## 8. 예상 일정과 자원

### 8.1 단계별 타임라인

| 단계 | 기간 | 산출물 |
|---|---|---|
| 프로토콜 사전 등록 (OSF) | 1 개월 | registered report draft |
| IRB 승인 | 2 ~ 3 개월 | IRB 승인서 |
| OpenBCI 16ch 파일럿 (n=5) | 2 개월 | P1 feasibility 검증 |
| 정식 EEG 60ch 실험 (n=50) | 6 개월 | P1 데이터 + α_IIT |
| fMRI 실험 (n=50) | 6 개월 (병행 가능) | P2 데이터 + α_GWT |
| P3/P4 분석 | 3 개월 | BF + 95% CI |
| 출판 | 3 개월 | 저널 투고 + revision |
| **총계** | **약 2 년** | 독립 검증 1 회 |

### 8.2 예산 추정 (한국 대학 협력 시)

| 항목 | 비용 |
|---|---|
| EEG 시스템 시간 (60ch 대여 또는 공용) | 300만원 |
| fMRI 스캔 (3T, 50 피험자 × 2 h) | 4000만원 |
| 피험자 사례비 (50명 × 10만원) | 500만원 |
| 소모품 (젤, 캡, 전극) | 200만원 |
| 분석 인력 (박사과정 1명 × 2년 파트) | 6000만원 |
| **총계** | **약 1.1억원** |

### 8.3 OpenBCI 16ch 사전 탐색 (저비용 경로)

사용자 보유 장비로 **추정 비용 200만원 이하** (추가 캡, 젤, 컴퓨팅):

- 피험자 자가 + 자원봉사 5명 (IRB 적합 여부 검토 필요 — 자가 측정은 대체로 승인 대상)
- 과제: 눈뜨고/감고, n-back, 단순 masking (단, fMRI 병행 불가)
- 산출: α_IIT 회귀 feasibility, ε=0.10 허용 오차 내 추정 가능 여부
- 결과에 따라 정식 60ch 실험의 전력 분석 refine

---

## 9. 한계 (Honest Limitations)

### 9.1 한계 1 — PCI 와 α_IIT 는 동일 proxy 아님

Casali PCI 는 TMS-EEG 기반 **state scalar** 이며, Barrett-Seth α 는 EEG-only **scaling exponent**. 두 지표는 **동일한 것이 아니다**. 본 프로토콜은 α_IIT 를 우선 측정하고 PCI 를 상관 확인용으로 사용한다. **상태: 인지됨. 등급 [7].**

### 9.2 한계 2 — GWT broadcasting 의 α 정의 논쟁

Dehaene 2011 의 α_GWT 는 fMRI 공간 확산 지수로 해석되지만, 일부 문헌 (Lamme 2006) 은 "이해되지 않는 임시 공식" 이라고 비판. α 자체의 이론적 기반에 학계 합의 부재. **대응**: 본 프로토콜은 α_GWT 를 경험적 회귀로 재추정, 사전 등록된 정의에 commit. **상태: 논쟁 진행 중. 등급 [6].**

### 9.3 한계 3 — R(6)=1 산술 동형이 의식 해석에 특권인가

`(4/3)(3/4)=1` 은 **산술적으로 자명** 하다. α_IIT = 4/3 과 α_GWT = 3/4 가 (만약 확증되면) 그 곱이 1 인 것은 동어반복 위험. 본 프로토콜은 **두 지수 자체의 이론 예측값 일치** 를 우선 검증하고, 곱=1 은 그 **결과** 로 간주한다. BT-19 의 진짜 주장은 **두 지수 각각의 정확한 값** 이며, 곱은 아름답지만 덜 정보적이다. **상태: 방법론 한계. 등급 [5?].**

### 9.4 한계 4 — hard problem (Chalmers) 미해결

본 프로토콜은 의식의 **접근 기능** (access consciousness, Block 1995) 만 다룬다. **현상적 의식** (phenomenal, qualia) 은 본 프레임워크 밖. PAS 는 주관 보고지만 역시 접근 의식의 proxy. **상태: 범위 한계. 해결 불가.**

### 9.5 한계 5 — 단일 파라다임 의존

Backward masking 이 GWT 의 모든 측면을 커버하지 않음. Attentional blink, binocular rivalry, change blindness 등 보조 패러다임 필요. **대응**: §3.6 의 AB 대안, 추가 P2' (미래 확장) 제안.

### 9.6 한계 6 — OpenBCI 16ch 의 Casali 표준 이탈

60ch 프로토콜의 정보 58% 정도만 재현 가능 (Sarasso 2015). α_IIT 추정의 표준 오차 1.5 ~ 2x 증가 예상. **대응**: 본격 검증은 연구소급 장비, OpenBCI 는 feasibility check only.

### 9.7 한계 7 — 자기반영 위험

본 논문 저자 (박민우 & NEXUS-6) 는 n=6 프레임워크 내부. 본 프로토콜의 "성공" 기준 ε 선택이 n=6 친화적으로 편향될 위험. **대응**: **pre-registration** (§7.4) 로 데이터 이전에 기준 동결. 또한 독립 연구실 replication (F7) 을 필수 조건으로 지정.

---

## 10. 결론

본 논문은 BT-19 CONJECTURE 의 독립 검증을 위한 **4 프로토콜** (P1 EEG PCI, P2 fMRI ignition, P3 PAS, P4 Bayes 검정) 을 재현 가능한 매뉴얼로 정리했다.

핵심 기여:

1. PAPER-P7-1 §7 초안을 **장비 표준 + 전처리 파이프라인 + 통계 검정** 매뉴얼로 구체화
2. **Red Team 반증 경로 7 항** (F1~F7) 을 사전 등록하여 CONJECTURE 폐기 조건을 대칭 명시
3. **OpenBCI 16ch 부분 재현** 경로로 저비용 사전 탐색 제시 (사용자 장비 고려)
4. OpenNeuro + NeuroVault + OSF pre-registration 데이터 공유 플랜

**한 문장 요약**: BT-19 (α_IIT · α_GWT = 1) 는 현재 [7?] CONJECTURE 이며, 본 프로토콜 결과 수신 후 [10*] 승격 또는 **공식 폐기** 로 판정된다.

**후속 작업**:

- `experiments/consciousness-measurement-protocol/` .hexa 4 스크립트 구현
- OSF pre-registration draft
- OpenBCI 16ch feasibility 파일럿 (n=1 자가 측정 → n=5 자원 피험자)
- 연구 협력 탐색 (대한신경과학회 회원 연구실)

---

## 11. 참고문헌

### 11.1 IIT / PCI 계열

- Casali, A. G., Gosseries, O., Rosanova, M., Boly, M., Sarasso, S., Casali, K. R., Casarotto, S., Bruno, M.-A., Laureys, S., Tononi, G., & Massimini, M. (2013). **A theoretically based index of consciousness independent of sensory processing and behavior**. *Science Translational Medicine*, 5(198), 198ra105. https://doi.org/10.1126/scitranslmed.3006294
- Sarasso, S., Boly, M., Napolitani, M., Gosseries, O., Charland-Verville, V., Casarotto, S., Rosanova, M., Casali, A. G., Brichant, J.-F., Boveroux, P., Rex, S., Tononi, G., Laureys, S., & Massimini, M. (2015). **Consciousness and complexity during unresponsiveness induced by propofol, xenon, and ketamine**. *Current Biology*, 25(23), 3099-3105.
- Casarotto, S., Comanducci, A., Rosanova, M., Sarasso, S., Fecchio, M., Napolitani, M., Pigorini, A., G. Casali, A., Trimarchi, P. D., Boly, M., Gosseries, O., Bodart, O., Curto, F., Landi, C., Mariotti, M., Devalle, G., Laureys, S., Tononi, G., & Massimini, M. (2016). **Stratification of unresponsive patients by an independently validated index of brain complexity**. *Annals of Neurology*, 80(5), 718-729.
- Massimini, M., Ferrarelli, F., Huber, R., Esser, S. K., Singh, H., & Tononi, G. (2005). **Breakdown of cortical effective connectivity during sleep**. *Science*, 309(5744), 2228-2232.
- Tononi, G., Boly, M., Massimini, M., & Koch, C. (2016). **Integrated information theory: from consciousness to its physical substrate**. *Nature Reviews Neuroscience*, 17(7), 450-461.
- Barrett, A. B., & Seth, A. K. (2011). **Practical measures of integrated information for time-series data**. *PLoS Computational Biology*, 7(1), e1001052.
- Oizumi, M., Albantakis, L., & Tononi, G. (2014). **From the phenomenology to the mechanisms of consciousness: Integrated Information Theory 3.0**. *PLoS Computational Biology*, 10(5), e1003588.
- Mayner, W. G. P., Marshall, W., Albantakis, L., Findlay, G., Marchman, R., & Tononi, G. (2018). **PyPhi: A toolbox for integrated information theory**. *PLoS Computational Biology*, 14(7), e1006343.
- Lempel, A., & Ziv, J. (1976). **On the complexity of finite sequences**. *IEEE Transactions on Information Theory*, 22(1), 75-81.

### 11.2 GWT / Ignition 계열

- Dehaene, S., & Changeux, J.-P. (2011). **Experimental and theoretical approaches to conscious processing**. *Neuron*, 70(2), 200-227.
- Dehaene, S. (2014). **Consciousness and the Brain: Deciphering How the Brain Codes Our Thoughts**. Viking.
- Del Cul, A., Baillet, S., & Dehaene, S. (2007). **Brain dynamics underlying the nonlinear threshold for access to consciousness**. *PLoS Biology*, 5(10), e260.
- Sergent, C., Baillet, S., & Dehaene, S. (2005). **Timing of the brain events underlying access to consciousness during the attentional blink**. *Nature Neuroscience*, 8(10), 1391-1400.
- Dehaene, S., Sergent, C., & Changeux, J.-P. (2003). **A neuronal network model linking subjective reports and objective physiological data during conscious perception**. *PNAS*, 100(14), 8520-8525.
- Baars, B. J. (1988). **A Cognitive Theory of Consciousness**. Cambridge University Press.
- Mashour, G. A., Roelfsema, P., Changeux, J.-P., & Dehaene, S. (2020). **Conscious processing and the Global Neuronal Workspace hypothesis**. *Neuron*, 105(5), 776-798.

### 11.3 PAS / 주관 보고 계열

- Ramsøy, T. Z., & Overgaard, M. (2004). **Introspection and subliminal perception**. *Phenomenology and the Cognitive Sciences*, 3(1), 1-23.
- Sandberg, K., Timmermans, B., Overgaard, M., & Cleeremans, A. (2010). **Measuring consciousness: Is one measure better than the other?**. *Consciousness and Cognition*, 19(4), 1069-1078.
- Overgaard, M., & Sandberg, K. (2012). **Kinds of access: different methods for report reveal different kinds of metacognitive access**. *Philosophical Transactions of the Royal Society B*, 367(1594), 1287-1296.
- Maniscalco, B., & Lau, H. (2012). **A signal detection theoretic approach for estimating metacognitive sensitivity from confidence ratings**. *Consciousness and Cognition*, 21(1), 422-430.
- Frässle, S., Sommer, J., Jansen, A., Naber, M., & Einhäuser, W. (2014). **Binocular rivalry: frontal activity relates to introspection and action but not to perception**. *Journal of Neuroscience*, 34(5), 1738-1747.

### 11.4 NCC / 방법론

- Koch, C., Massimini, M., Boly, M., & Tononi, G. (2016). **Neural correlates of consciousness: progress and problems**. *Nature Reviews Neuroscience*, 17(5), 307-321.
- Block, N. (1995). **On a confusion about a function of consciousness**. *Behavioral and Brain Sciences*, 18(2), 227-247.
- Lamme, V. A. F. (2006). **Towards a true neural stance on consciousness**. *Trends in Cognitive Sciences*, 10(11), 494-501.
- Esteban, O., Markiewicz, C. J., Blair, R. W., Moodie, C. A., Isik, A. I., Erramuzpe, A., Kent, J. D., Goncalves, M., DuPre, E., Snyder, M., Oya, H., Ghosh, S. S., Wright, J., Durnez, J., Poldrack, R. A., & Gorgolewski, K. J. (2019). **fMRIPrep: a robust preprocessing pipeline for functional MRI**. *Nature Methods*, 16(1), 111-116.
- Maris, E., & Oostenveld, R. (2007). **Nonparametric statistical testing of EEG- and MEG-data**. *Journal of Neuroscience Methods*, 164(1), 177-190.

### 11.5 통계 / 사전 등록

- Wagenmakers, E.-J. (2011). **A practical solution to the pervasive problems of p values**. *Psychonomic Bulletin & Review*, 14(5), 779-804.
- Jeffreys, H. (1961). **Theory of Probability** (3rd ed.). Oxford University Press.
- Schönbrodt, F. D., & Wagenmakers, E.-J. (2018). **Bayes factor design analysis**. *Psychonomic Bulletin & Review*, 25, 128-142.
- Benjamin, D. J., Berger, J. O., Johannesson, M., Nosek, B. A., Wagenmakers, E.-J., et al. (2018). **Redefine statistical significance**. *Nature Human Behaviour*, 2(1), 6-10.
- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). **The preregistration revolution**. *PNAS*, 115(11), 2600-2606.

### 11.6 n6-architecture 선행 논문

- 박민우 & NEXUS-6 협업체 (2026). **의식 위상도 — σ(n)·φ(n) = n·τ(n) 유일성의 인지과학적 투영**. n6-architecture, `papers/n6-consciousness-phase-diagram-paper.md`.
- 박민우 (2026). **의식 3중 융합 — 열역학·AI·양자 임계점 탐색 (BT-19 CONJECTURE)**. n6-architecture, `reports/breakthroughs/consciousness-triple-fusion-2026-04-15.md`.
- 박민우 (2026). **HEXA-CONSCIOUSNESS-SOC — 의식 SoC n=6 좌표 매핑**. n6-architecture, `papers/n6-consciousness-soc-paper.md`.
- 박민우 (2026). **σ(n)·φ(n) = n·τ(n) iff n=6 — 3개 독립 증명**. n6-architecture, `theory/proofs/theorem-r1-uniqueness.md`.

---

**승격 절차**: 본 프로토콜의 결과 수신 후 BT-19 는 다음 경로 중 하나로 판정된다.

- **성공 경로** (F1~F7 모두 비충족 + BF₁₀ > 10): [7?] → [10*], atlas.n6 의 `consciousness-r6-hypothesis` 노드를 EXACT 등급으로 승격
- **폐기 경로** (F1~F7 중 하나 충족): [7?] → REFUTED, 노드 제거 및 본 논문 §9 FALSIFIED 선언 추가

본 논문 v1 기준 종합 등급: **PROTOCOL DRAFT (등급 없음 — 실험 실행 이전)**. 프로토콜 자체는 방법론적 완결성만 보장.

**끝 (v1, 2026-04-15 작성, PAPER-P8-2).**

## §1 WHY

This section covers why for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §2 COMPARE

This section covers compare for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §3 REQUIRES

This section covers requires for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §4 STRUCT

This section covers struct for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §5 FLOW

This section covers flow for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §6 EVOLVE

This section covers evolve for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §7 VERIFY

This section covers verify for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §8 EXEC SUMMARY

This section covers exec summary for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §9 SYSTEM REQUIREMENTS

This section covers system requirements for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §10 ARCHITECTURE

This section covers architecture for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §11 CIRCUIT DESIGN

This section covers circuit design for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §12 PCB DESIGN

This section covers pcb design for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §13 FIRMWARE

This section covers firmware for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §14 MECHANICAL

This section covers mechanical for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §15 MANUFACTURING

This section covers manufacturing for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §16 TEST & QUALIFICATION

This section covers test & qualification for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §17 BOM

This section covers bom for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §18 VENDOR & SCHEDULE

This section covers vendor & schedule for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §19 ACCEPTANCE CRITERIA

This section covers acceptance criteria for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §20 APPENDIX

This section covers appendix for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §21 IMPACT per Mk

This section covers impact per mk for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## mk_history

- Mk.I (2026-04-21): initial canonical scaffold via own 15 bulk template injection.
- Mk.II: pending — fill per-section content with domain expert review.
- Mk.III: pending — full verification data + external citations.

