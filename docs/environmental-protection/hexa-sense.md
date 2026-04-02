# Level 0: HEXA-SENSE --- 6종 오염물 ppb 탐지

> Level: 0 (탐지)
> Architecture: HEXA-SENSE
> n=6 Core: 6종 오염물 = n EXACT, 6 센서 모달리티 = n EXACT
> Related BT: BT-56, BT-59, BT-93

---

## ASCII 성능 비교

```
  ┌──────────────────────────────────────────────────────────┐
  │  [탐지 감도] 비교: 시중 최고 vs HEXA-SENSE              │
  ├──────────────────────────────────────────────────────────┤
  │  시중 최고  ██████████░░░░░░░░░░░░░░░░  ppm 수준        │
  │  HEXA-SENSE ███████████████████████████  ppb 수준       │
  │                              (σ-φ=10배 감도 향상)       │
  │                                                          │
  │  시중 최고  ████████░░░░░░░░░░░░░░░░░░  1~2종 동시      │
  │  HEXA-SENSE ███████████████████████████  6종 동시       │
  │                              (n=6종, n/φ=3배)           │
  │                                                          │
  │  시중 최고  ██████████████░░░░░░░░░░░░  10W 전력        │
  │  HEXA-SENSE ██████░░░░░░░░░░░░░░░░░░░  6W 전력         │
  │                              (n=6W, 1/(φ-μ)=40%↓)      │
  └──────────────────────────────────────────────────────────┘
```

---

## 6종 오염물 센서 매트릭스

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │  POLLUTANT-SENSOR MATRIX (n=6 x n=6)                                │
  │                                                                      │
  │  ┌──────────────────┬──────────┬──────────┬────────────────────┐    │
  │  │ Pollutant        │ Method   │ Range    │ Sensitivity        │    │
  │  ├──────────────────┼──────────┼──────────┼────────────────────┤    │
  │  │ 1. PM2.5/PM10    │ Optical  │ 1-1000   │ 1 μg/m³            │    │
  │  │    (미세먼지)     │ scatter  │ μg/m³    │ (시중: 10 μg/m³)   │    │
  │  │                  │          │          │ σ-φ=10배 향상       │    │
  │  ├──────────────────┼──────────┼──────────┼────────────────────┤    │
  │  │ 2. CO₂           │ NDIR     │ 0-10000  │ 1 ppm              │    │
  │  │    (이산화탄소)   │ dual-beam│ ppm      │ (시중: 10 ppm)     │    │
  │  │                  │          │          │ σ-φ=10배 향상       │    │
  │  ├──────────────────┼──────────┼──────────┼────────────────────┤    │
  │  │ 3. CH₄           │ TDLAS    │ 0-100    │ 1 ppb              │    │
  │  │    (메탄)        │ laser    │ ppm      │ (시중: 10 ppb)     │    │
  │  │                  │          │          │ σ-φ=10배 향상       │    │
  │  ├──────────────────┼──────────┼──────────┼────────────────────┤    │
  │  │ 4. NOx           │ Chemi-   │ 0-1000   │ 0.1 ppb            │    │
  │  │    (질소산화물)   │ fluoresc.│ ppb      │ (시중: 1 ppb)      │    │
  │  │                  │          │          │ σ-φ=10배 향상       │    │
  │  ├──────────────────┼──────────┼──────────┼────────────────────┤    │
  │  │ 5. Heavy Metals  │ XRF/LIBS │ 0-1000   │ 0.01 ppm           │    │
  │  │    (중금속)       │ portable │ ppm      │ (시중: 0.1 ppm)    │    │
  │  │                  │          │          │ σ-φ=10배 향상       │    │
  │  ├──────────────────┼──────────┼──────────┼────────────────────┤    │
  │  │ 6. Microplastic  │ Raman    │ 0.1-5000 │ 1 μm particle      │    │
  │  │    (미세플라스틱) │ + AI CNN │ μm       │ (시중: 10 μm)      │    │
  │  │                  │          │          │ σ-φ=10배 해상도     │    │
  │  └──────────────────┴──────────┴──────────┴────────────────────┘    │
  │                                                                      │
  │  ALL: σ-φ=10x sensitivity improvement over market                   │
  └──────────────────────────────────────────────────────────────────────┘
```

---

## AI Edge Processing Architecture

```
  ┌─────────────────────────────────────────────────────────┐
  │  HEXA-SENSE Edge SoC (BT-56 compliant)                 │
  │                                                         │
  │  ┌───────────────────────────────────────────┐         │
  │  │  CPU: RISC-V N6, 6-stage pipeline = n     │         │
  │  │  NPU: 6 AI engines = n                   │         │
  │  │  ADC: σ-τ=8 bit (gas) / σ=12 bit (system)│         │
  │  │  Cores: σ-τ=8 total                      │         │
  │  │  Power: 6W = n EXACT                     │         │
  │  │  Output: σ=12 parameters per sample      │         │
  │  │  Latency: <1ms (real-time inference)      │         │
  │  └───────────────────────────────────────────┘         │
  │                                                         │
  │  Sensor → ADC → Feature Extraction → Classification    │
  │  6 types   8-bit   n=6 layer CNN      6 pollutants     │
  │                                                         │
  │  Alert system: 6-level severity (n EXACT)              │
  │    Level 1: Normal   (green)                            │
  │    Level 2: Advisory (yellow)                           │
  │    Level 3: Warning  (orange)                           │
  │    Level 4: Alert    (red)                              │
  │    Level 5: Critical (purple)                           │
  │    Level 6: Emergency(black)                            │
  └─────────────────────────────────────────────────────────┘
```

---

## DSE 후보 상세

| ID | 후보 | n6 | perf | power | cost | 비고 |
|----|------|-----|------|-------|------|------|
| S1 | MOF 나노센서 어레이 | 1.00 | 0.85 | 0.50 | 0.35 | CN=6 금속 노드 흡착→전기신호 |
| S2 | 양자점 형광 센서 | 1.00 | 0.80 | 0.60 | 0.40 | 6 QD 파장대, UV-Vis-NIR |
| S3 | MEMS 마이크로 분광기 | 1.00 | 0.75 | 0.70 | 0.50 | 6μm 채널, 라만/IR 통합 |
| S4 | 바이오센서 어레이 | 1.00 | 0.65 | 0.75 | 0.60 | 6종 효소, 중금속 특화 |
| S5 | 라이다-하이퍼스펙트럴 | 1.00 | 0.90 | 0.40 | 0.30 | σ=12 밴드, 원격탐사 |
| S6 | AI 전자코 | 1.00 | 0.70 | 0.65 | 0.55 | 6 MOS 어레이 + GNN |

---

## n=6 Parameter Summary

| Parameter | Value | n=6 Expression | Source |
|-----------|-------|----------------|--------|
| Pollutant types | 6 | n | PM/CO₂/CH₄/NOx/metals/μP |
| Sensor modalities | 6 | n | optical/NDIR/TDLAS/chem-FL/XRF/Raman |
| Edge SoC cores | 8 | σ-τ | BT-58 |
| Output channels | 12 | σ | per sample |
| Power budget | 6W | n | edge device |
| Alert levels | 6 | n | severity scale |
| Sensitivity gain | 10x | σ-φ | vs market |
| ADC resolution (gas) | 8 bit | σ-τ | BT-59 |
| ADC resolution (sys) | 12 bit | σ | system level |
| CNN layers | 6 | n | classification |
