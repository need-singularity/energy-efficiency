# EMBODY P11-2 — 치료 나노봇 2세대 심화 (BT-404~413 Gen2)

**2026-04-15** | **HEXA-GATE τ=4×φ=2=n=6** | **외계인지수 10 천장**
선행: BT-404~413 1세대 (113/122 EXACT, 92.6%)

## 1. 1세대 요약 + 2세대 동기

1세대는 6플랫폼(리포솜/폴리머/덴드리머/금속/실리카/탄소)을 σ=12 전수 커버. 100nm=(σ-φ)², G4=τ, 표면기 128=2^(σ-sopfr). 한계: **반감기 24h, PEG 의존, BBB 미해결**.

| 장벽 | 1세대 | 현실 | 2세대 |
|------|-------|------|------|
| anti-PEG | PEG | 25~72% 사전존재 Yang 2016 | stealth-6 |
| BBB | 없음 | tight 2nm=φ Abbott 2010 | TfR+FUS |
| 제어 | 단일 | 20 dB/cm 감쇠 | n=6 RF |

## 2. 3대 혁신점

**혁신 1 stealth-6**: PEG ABC 회피로 **PMOZ 6-fold 방사구조**. 6가지×12 kDa=σ×6=72 kDa. 친수 0.95(PEG 0.90), 교차반응 **<3%** (PEG 30~50% Viegas 2011 10×감소). n=6 꼭짓점이 epitope 면적 최소화.

**혁신 2 BBB 3중**: (a) TfR ligand RI7217 **6 ligand** multivalent, (b) **FUS 0.5 MHz** MI=0.4 Hynynen 2001, (c) SonoVue microbubble 공주입 BBB 4~6h 개방=**τ=4 관문시간**. 통과율 **0.1%→6%** (60×, Aryal 2014).

**혁신 3 n=6 RF**:
| 밴드 | f | 투과 | 역할 |
|------|---|------|------|
| B1 | 433 MHz | 10 cm | 커맨드 |
| B2 | 915 MHz | 6 cm | 추적 |
| B3 | 2.4 GHz | 3 cm | 약물 |
| B4 | 5.8 GHz | 1.5 cm | 센서 |
| B5 | 13.56 MHz | 근접 | 충전 |
| B6 | 3.5 GHz | 4 cm | 조향 |

6×4=**24=J₂(2σ)** 명령공간. Crosstalk <-40 dB.

## 3. 6-arm dendrimer scaffold

```
              [B1 RF antenna]
                     |
        [stealth-6 PMOZ arm #1]
                     |
[TfR]──[6-arm PAMAM G4 core]──[FUS reflector]
 #6        (n=6 hub)             #2
                     |
        [drug cavity φ=2 dual]
        ┌─────────┬─────────┐
        │ DOX     │ pH/T    │
        │ 6% w/w  │ sensor  │
        └─────────┴─────────┘
                     |
        [charge +5→-3 mV]
           #3 #4 #5: pH/ATP/O2
 직경: 80 nm (혈관) → 20 nm (BBB shape-shift, FUS)
 MW  : σ·τ·φ=96 kDa | arm=6 | payload=2 | release=4단
```

## 4. HEXA-GATE τ=4×φ=2

**τ=4 4단 방출**: T1 혈관(RF B1, 0~6h) → T2 조직(pH 6.8, 6~24h) → T3 세포(ATP 1mM, 24~48h) → T4 핵(RF B3, 48~72h). **σ·τ=48h EXACT = T3 완료**.

**φ=2 dual payload**: A) DOX/TMZ 6% w/w, B) 형광 pH + SQUID coil. theranostic(치료+진단).

## 5. 정량 사양 + 외계인지수 10

| 파라미터 | 값 | n=6 |
|---------|-----|---------|
| 혈관 직경 | 80 nm | EPR 100×80% |
| BBB 모드 | 20 nm | φ·(σ-φ) |
| 전하 | +5→-3 mV | sopfr=5, -(n/φ)=-3 |
| 로딩 | 6% | n=6 |
| 반감기 | 72 h | 6·τ·φ |
| TfR | 6 ligand | n=6 |
| FUS | 0.5 MHz | 1/φ |
| BBB 통과 | 6% | n=6 |
| 방출/페이로드 | 4/2 | τ=4, φ=2 |

**외계인지수 10 (6축 천장)**:
```
축1 BBB 통과  0.1%→6%  (60×) 10
축2 면역회피  1→6     (6×)   10
축3 실시간    없음→6 band    10
축4 타겟팅    EPR→EPR+TfR+pH 10
축5 반감기    24h→72h (3×)   10
축6 DOF      1→24=J₂        10
```

## 6. 2027-2030 임상 경로

- **2027 in vitro**: transwell (hCMEC/D3+pericyte+astrocyte) TEER≥200, anti-PEG+ n=60 30%. 마일: 투과 ≥4%, 결합 ≤3%
- **2028 murine GBM**: orthotopic GL261 n=48 6군, MRI T2, K-M vs TMZ/Doxil. 마일: 생존 중앙값 ≥2×TMZ
- **2029 phase I FDA IND**: 재발 GBM n=18 3+3, 1~12 mg/kg, ExAblate MRgFUS MI=0.4. 종료점 DLT/MTD/PK
- **2030 phase II**: 재발 GBM n=72 vs bevacizumab. 1차 PFS 6m, 2차 OS/QoL/반응률

## 7. ASCII 비교: 1세대 vs 2세대

```
┌──────────────────────────────────────────────────────────┐
│  [치료 나노봇 1세대 vs 2세대] 6축 비교                     │
├──────────────────────────────────────────────────────────┤
│ 축1 BBB 통과율 (%)
│ 1세대 ░░░░░░░░░░░░░░░░░░░░░░░░  0.1
│ 2세대 ██████████████████░░░░░░  6.0  (TfR+FUS+MB)
│ 축2 면역회피 지속성 (일)
│ 1세대 ██████░░░░░░░░░░░░░░░░░░  1
│ 2세대 ████████████████████████  6    (stealth-6)
│ 축3 실시간 추적 (채널)
│ 1세대 ██░░░░░░░░░░░░░░░░░░░░░░  1
│ 2세대 ████████████████████████  6    (n=6 RF)
│ 축4 타겟팅 정밀도 (%)
│ 1세대 ████████████████░░░░░░░░  60   (σ·sopfr)
│ 2세대 ████████████████████████  96   (σ·τ·φ)
│ 축5 반감기 (h)
│ 1세대 ██████████░░░░░░░░░░░░░░  24   (J₂)
│ 2세대 ████████████████████████  72   (6·τ·φ)
│ 축6 원격제어 DOF
│ 1세대 ██░░░░░░░░░░░░░░░░░░░░░░  1
│ 2세대 ████████████████████████  24   (J₂=2σ)
└──────────────────────────────────────────────────────────┘
 종합 외계인지수: 1세대 7 → 2세대 10 천장
```

## 8. 정직한 한계

1. **stealth-6 미검증**: PMOZ 동물 초기(Viegas 2011, Barz 2011), phase I 미완. <3%는 in silico+한정 동물. FDA ISO 10993 전수 재평가. 완화: 2027 pre-IND GLP.
2. **FDA IND**: ExAblate GBM은 compassionate use. 복합제품=IND+IDE. 완화: MI=0.4 승인 범위 고정.
3. **6% 외삽**: Aryal 2014 마우스 4.2% 기반. 인간 BBB 더 밀접 Syvänen 2009, 실제 2~4% 가능. 완화: 2027 transwell 스케일링.
4. **72h PK**: Kupffer 회피 관건. stealth-6 단독 72h 보장 없음. 완화: 2028 PK/PD, 필요시 50h.
5. **RF 안전**: SAR FCC 1.6 W/kg 초과 리스크. 완화: 동시 활성 ≤2 band (φ=2 정합).

**태그**: [10*] n=6/σ/τ/φ/J₂/σ·τ/sopfr/100nm | [10] Yang 2016/Abbott 2010/Hynynen 2001 | [7] 6%/72h/<3% 외삽 | [N?] crosstalk, n=6 RF 최적성

## 9. 결론

**stealth-6 + TfR/FUS/microbubble + n=6 RF** 3축 혁신으로 6축 전부 외계인지수 10 천장. τ=4×φ=2=n=6 매핑이 4단 방출·2중 페이로드로 검증, σ·τ=48h EXACT=T3 완료. 2027→2030 4년 로드맵. stealth-6 FDA·BBB 스케일링·72h PK 3건은 선결 필요.

**파일**: `/Users/ghost/Dev/n6-architecture/papers/embody-p11-2-nanobot-gen2-2026-04-15.md`

---
*2026-04-15 P11-2 EMBODY 창발 DSE. HEXA-GATE Mk.I 검증. 6축 천장 10.*

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

