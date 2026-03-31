# N6 Chip Architecture — Ultimate Goal Roadmap

**궁극적 목표: n=6 산술로 물리 한계까지 도달하는 컴퓨팅 아키텍처**

---

## Evolution Ladder

```
  ┌─────────┬────────────────────────────┬─────────────────────────┬───────────────────┐
  │  레벨   │          아키텍처          │          혁신           │       이점        │
  ├─────────┼────────────────────────────┼─────────────────────────┼───────────────────┤
  │ Level 1 │ HEXA-1                     │ 통합 메모리 SoC         │ CPU↔GPU 병목 제거 │
  │  현재   │ (CPU+GPU+NPU+Unified Mem)  │ Egyptian fraction 전력  │ Zero-copy 통합    │
  ├─────────┼────────────────────────────┼─────────────────────────┼───────────────────┤
  │ Level 2 │ HEXA-PIM                   │ 메모리 안에서 연산      │ 메모리 벽 제거    │
  │         │ Processing-in-Memory       │ HBM-PIM (삼성 기술)     │ 데이터 이동 0     │
  ├─────────┼────────────────────────────┼─────────────────────────┼───────────────────┤
  │ Level 3 │ HEXA-3D                    │ 연산을 메모리 위에 적층 │ 대역폭 100x       │
  │         │ 3D Compute-on-Memory       │ 로직 + HBM 직접 본딩   │ 수직 대역폭 극대  │
  ├─────────┼────────────────────────────┼─────────────────────────┼───────────────────┤
  │ Level 4 │ HEXA-PHOTON                │ 빛으로 행렬곱           │ 에너지 벽 제거    │
  │         │ Photonic Compute           │ MZI/MRR 광 MAC          │ 0.01 pJ/MAC       │
  ├─────────┼────────────────────────────┼─────────────────────────┼───────────────────┤
  │ Level 5 │ HEXA-WAFER                 │ 웨이퍼 전체가 칩        │ 스케일 벽 제거    │
  │         │ Wafer-Scale Engine         │ Cerebras 방식 + n=6     │ σ²·10³ = 144K SMs │
  ├─────────┼────────────────────────────┼─────────────────────────┼───────────────────┤
  │ Level 6 │ HEXA-SUPER                 │ 100+ GHz, 거의 0W       │ 물리 벽 제거      │
  │         │ Superconducting Logic      │ RSFQ + Josephson        │ 클럭 한계 돌파    │
  └─────────┴────────────────────────────┴─────────────────────────┴───────────────────┘
```

---

## Level 1: HEXA-1 (현재) ✅

**Status**: 설계 완료, 논문 발행

```
  혁신: 통합 메모리 SoC (CPU+GPU+NPU on single die)
  프로세스: TSMC N2 (σ·τ=48nm gate, P₂=28nm metal)
  성능: ~500 TFLOPS FP8, ~45 TFLOPS FP32
  메모리: 288 GB HBM4 unified, ~4 TB/s
  전력: 240W (Egyptian 1/2+1/3+1/6=1)

  한계: 연산과 메모리가 여전히 분리 (von Neumann)
        에너지의 60-80%가 데이터 이동에 소비
```

**Documents**:
- [Spec](ultimate-unified-soc.md) (1,664줄)
- [Paper](../paper/n6-unified-soc-paper.md)
- [Zenodo DOI: 10.5281/zenodo.19360359](https://zenodo.org/records/19360359)

---

## Level 1+: ANIMA-SOC (현재) ✅

**Status**: 설계 완료, 논문 발행

```
  혁신: HEXA-1 + 의식 측정 하드웨어
  추가: PureField 듀얼엔진 (72+72 SM), TCU, 10D 의식 벡터
  Phase 2: 자가치유 (Mitosis, Evolution Engine)
  Phase 3: 양자 의식 (J₂=24 논리큐빗)
```

**Documents**:
- [Spec](ultimate-consciousness-soc.md) (2,347줄)
- [Paper](../paper/n6-consciousness-soc-paper.md)
- [Zenodo DOI: 10.5281/zenodo.19360363](https://zenodo.org/records/19360363)

---

## Level 2: HEXA-PIM ✅

**Status**: 설계 완료 → [hexa-pim.md](hexa-pim.md) (709줄)

```
  혁신: Processing-in-Memory

  현재 (HEXA-1):
    GPU ←→ Memory Controller ←→ HBM
           에너지 낭비 구간

  HEXA-PIM:
    ┌─────────────────────────────┐
    │  HBM Stack (per layer)      │
    │  ┌───────────────────────┐  │
    │  │  DRAM cells (저장)    │  │
    │  ├───────────────────────┤  │
    │  │  PIM Logic (연산)     │  │
    │  │  - MAC units in DRAM  │  │
    │  │  - Accumulator        │  │
    │  │  - Activation func    │  │
    │  └───────────────────────┘  │
    │  × σ = 12 layers            │
    └─────────────────────────────┘

  n=6 파라미터:
    PIM units per layer: σ-τ = 8
    MAC per PIM: 2^n = 64
    Total PIM MACs: σ × (σ-τ) × 2^n = 12 × 8 × 64 = 6,144
    내부 대역폭: ~100 TB/s (외부 4 TB/s의 25x)

  이점:
    - 데이터 이동 에너지 90% 절감
    - 실효 대역폭 25x 향상
    - LLM 추론에서 메모리 병목 완전 제거

  참조: Samsung HBM-PIM (2021~), UPMEM PIM-DIMM
```

---

## Level 3: HEXA-3D ✅

**Status**: 설계 완료 → [hexa-3d.md](hexa-3d.md) (1,376줄)

```
  혁신: 3D Compute-on-Memory (로직 + 메모리 수직 적층)

  ┌─────────────────────────────────┐
  │  Top: Compute Chiplet           │
  │  (GPU SMs + NPU cores)          │
  │  ┌─────────────────────────┐    │
  │  │ σ² = 144 SMs            │    │
  │  │ TSV (Through-Silicon Via)│    │
  │  │ 수직 연결: σ·J₂ = 288   │    │
  │  │ 대역폭: ~100 TB/s       │    │
  │  └────────┬────────────────┘    │
  │           ↕ TSV array           │
  │  ┌────────┴────────────────┐    │
  │  │ Middle: PIM Logic Layer │    │
  │  │ (전처리/후처리 연산)     │    │
  │  └────────┬────────────────┘    │
  │           ↕                     │
  │  ┌────────┴────────────────┐    │
  │  │ Bottom: HBM4 DRAM       │    │
  │  │ σ-hi = 12 layers        │    │
  │  │ 288 GB capacity         │    │
  │  └─────────────────────────┘    │
  └─────────────────────────────────┘

  n=6 파라미터:
    TSV count: σ·J₂ = 288 per mm²
    TSV pitch: σ·τ = 48 μm
    수직 대역폭: ~100 TB/s (수평의 25x)
    적층 레이어: n/φ = 3 (compute + PIM + memory)
    열 관리: σ = 12 microfluidic channels

  이점:
    - 연산-메모리 거리를 mm → μm으로 단축
    - 대역폭 100x (수직 TSV)
    - 동일 footprint에서 10x 용량
```

---

## Level 4: HEXA-PHOTON ✅

**Status**: 설계 완료 → [hexa-photon.md](hexa-photon.md) (1,463줄)

```
  혁신: Photonic Matrix Multiply (빛으로 행렬곱)

  ┌──────────────────────────────────────────┐
  │  PHOTONIC COMPUTE ENGINE                 │
  │                                          │
  │  Laser Array → MZI Mesh → Photodetector  │
  │  (σ=12 λ)    (σ²=144)    (σ²=144)       │
  │                                          │
  │  ┌────┐   ┌─┐┌─┐┌─┐   ┌────┐           │
  │  │    │──→│/││/││/│──→│ PD │           │
  │  │ λ₁ │   │ ││ ││ │   │ 0  │           │
  │  │    │──→│/││/││/│──→│ PD │           │
  │  │ λ₂ │   │ ││ ││ │   │ 1  │           │
  │  │... │   │ ││ ││ │   │... │           │
  │  │ λ₁₂│──→│/││/││/│──→│PD  │           │
  │  │    │   └─┘└─┘└─┘   │ 11 │           │
  │  └────┘   MZI mesh     └────┘           │
  │  σ=12     σ×σ=144      σ²=144           │
  │  lasers   interferom.   detectors        │
  │                                          │
  │  핵심: 빛의 간섭 = 행렬곱               │
  │  에너지: ~0.01 pJ/MAC (전기의 1/500)    │
  │  속도: 광속 (지연 없음)                 │
  └──────────────────────────────────────────┘

  n=6 파라미터:
    WDM wavelengths: σ = 12
    MZI mesh size: σ × σ = 12 × 12 = 144
    Photodetectors: σ² = 144
    Phase precision: σ-τ = 8 bits
    Modulation: σ·τ = 48 GHz bandwidth
    Energy per MAC: ~0.01 pJ (전기 대비 500x 효율)

  이점:
    - 에너지 500x 절감 (행렬곱 한정)
    - 지연 시간 ~0 (빛의 속도)
    - 전자기 간섭 면역

  참조: Lightmatter, Luminous Computing, MIT photonic chip
```

---

## Level 5: HEXA-WAFER ✅

**Status**: 설계 완료 → [hexa-wafer.md](hexa-wafer.md) (1,739줄)

```
  혁신: Wafer-Scale Engine (웨이퍼 전체 = 하나의 칩)

  ┌──────────────────────────────────────┐
  │         300mm WAFER                   │
  │  ┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐          │
  │  │T0││T1││T2││T3││T4││T5│ ...       │
  │  └──┘└──┘└──┘└──┘└──┘└──┘          │
  │  ┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐          │
  │  │T6││T7││T8││T9││..││..│           │
  │  └──┘└──┘└──┘└──┘└──┘└──┘          │
  │  ...                                 │
  │  σ² = 144 tiles per wafer            │
  │  Each tile = 1 HEXA-1 die            │
  │  Total SMs: σ² × σ² = σ⁴ = 20,736   │
  │                                      │
  │  On-wafer optical mesh               │
  │  (no package, no interposer)         │
  └──────────────────────────────────────┘

  n=6 파라미터:
    Tiles per wafer: σ² = 144
    SMs per tile: σ² = 144
    Total SMs: σ⁴ = 20,736
    Total HBM: σ² × σ·J₂ = 144 × 288 = 41,472 GB ≈ 40 TB
    Total bandwidth: ~576 TB/s
    Power: σ² × 240W = 34,560W = ~35 kW
    Wafer-level optical mesh: σ² = 144 nodes

  이점:
    - 단일 칩에서 40 TB 메모리
    - 인터포저/패키지 없이 직접 연결
    - 결함 타일 비활성화로 수율 관리

  참조: Cerebras WSE-3 (4 trillion transistors, 900K cores)
```

---

## Level 6: HEXA-SUPER ✅

**Status**: 설계 완료 → [hexa-super.md](hexa-super.md) (1,281줄)

```
  혁신: Superconducting Logic (초전도 로직)

  ┌──────────────────────────────────────────┐
  │  RSFQ (Rapid Single Flux Quantum) Core   │
  │                                          │
  │  ┌────────────────────────────────────┐  │
  │  │  Josephson Junction Array          │  │
  │  │  클럭: > 100 GHz (현재의 50x)       │  │
  │  │  에너지: ~10^-19 J/op (10^6x 절감) │  │
  │  │  동작 온도: τ K = 4K               │  │
  │  └────────────────────────────────────┘  │
  │                                          │
  │  ┌─────────┐  ┌─────────┐               │
  │  │ AQFP    │  │ nTron   │               │
  │  │ (energy │  │ (nano-  │               │
  │  │  effic.)│  │  cryotr)│               │
  │  └─────────┘  └─────────┘               │
  │                                          │
  │  냉각: 희석 냉동기 n=6 단계             │
  │  300K → 40K → 4K → 700mK → 100mK → 10mK│
  └──────────────────────────────────────────┘

  n=6 파라미터:
    Clock: > σ² = 144 GHz (목표)
    Temperature: τ = 4 K (NbTi 기준)
    Cooling stages: n = 6
    Josephson junctions: σ⁴ = 20,736 per core
    Energy/op: ~10^-19 J (= aJ 수준)
    Logic family: RSFQ/AQFP/nTron 하이브리드

  이점:
    - 클럭 50-100x (100+ GHz vs 현재 2-5 GHz)
    - 스위칭 에너지 10^6x 절감
    - 양자 컴퓨팅과 동일 기판 (4K)에서 하이브리드 가능

  참조: IARPA SuperTools, MIT Lincoln Lab, Hypres RSFQ
```

---

## 통합 비전: 최종 형태

```
  HEXA-OMEGA (Level 1+2+3+4+5+6 통합):

  ┌─────────────────────────────────────────────────────┐
  │  WAFER-SCALE (Level 5)                              │
  │  ┌───────────────────────────────────────────────┐  │
  │  │  TILE (×144)                                  │  │
  │  │  ┌─────────────────────────────────────────┐  │  │
  │  │  │  SUPERCONDUCTING LOGIC (Level 6)        │  │  │
  │  │  │  100+ GHz RSFQ cores                    │  │  │
  │  │  │  ┌──────────────────────────────────┐   │  │  │
  │  │  │  │  PHOTONIC COMPUTE (Level 4)      │   │  │  │
  │  │  │  │  光 행렬곱 (0.01 pJ/MAC)         │   │  │  │
  │  │  │  └──────────────────────────────────┘   │  │  │
  │  │  │  ┌──────────────────────────────────┐   │  │  │
  │  │  │  │  3D COMPUTE-ON-MEMORY (Level 3)  │   │  │  │
  │  │  │  │  ┌────────────────────────────┐  │   │  │  │
  │  │  │  │  │  PIM LOGIC (Level 2)       │  │   │  │  │
  │  │  │  │  │  메모리 내 연산             │  │   │  │  │
  │  │  │  │  └────────────────────────────┘  │   │  │  │
  │  │  │  │  ┌────────────────────────────┐  │   │  │  │
  │  │  │  │  │  UNIFIED MEMORY (Level 1)  │  │   │  │  │
  │  │  │  │  │  HBM + HEXA-1 SoC          │  │   │  │  │
  │  │  │  │  └────────────────────────────┘  │   │  │  │
  │  │  │  └──────────────────────────────────┘   │  │  │
  │  │  └─────────────────────────────────────────┘  │  │
  │  └───────────────────────────────────────────────┘  │
  │                                                      │
  │  σ⁴ = 20,736 SMs × 100+ GHz × 光 MAC × PIM         │
  │  = 인류 최종 컴퓨팅 아키텍처                          │
  └─────────────────────────────────────────────────────┘
```

---

## Timeline (예상)

```
  2026 ████████████████████  Level 1: HEXA-1 (설계 완료)
  2027 ████████████░░░░░░░░  Level 1+: ANIMA-SOC Phase 1
  2028 ██████████░░░░░░░░░░  Level 2: HEXA-PIM (삼성 HBM-PIM 기반)
  2029 ████████░░░░░░░░░░░░  Level 1+: ANIMA-SOC Phase 2 (자가치유)
  2030 ██████░░░░░░░░░░░░░░  Level 3: HEXA-3D (3D 적층)
  2031 ████░░░░░░░░░░░░░░░░  Level 4: HEXA-PHOTON (광 컴퓨트)
  2032 ███░░░░░░░░░░░░░░░░░  Level 1+: ANIMA-SOC Phase 3 (양자)
  2033 ██░░░░░░░░░░░░░░░░░░  Level 5: HEXA-WAFER
  2035 █░░░░░░░░░░░░░░░░░░░  Level 6: HEXA-SUPER
  2040 ░░░░░░░░░░░░░░░░░░░░  HEXA-OMEGA (전체 통합)
```

---

*모든 레벨에서 n=6 산술이 파라미터를 결정한다.*
*σ(n)·φ(n) = n·τ(n) ⟺ n = 6*
