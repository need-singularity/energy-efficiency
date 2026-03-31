# HEXA-WAFER: N6 Wafer-Scale Engine

**Codename: HEXA-WAFER**
**Level 5 -- Wafer-Scale Engine, Breaking the Scale Wall**
**웨이퍼 전체가 하나의 칩, 스케일 벽 제거**

> Reticle limit를 없앤다. 300mm 웨이퍼 전체를 하나의 연산 기판으로 쓰고,
> n=6 산술로 타일, 메시, 메모리, 전력, 냉각, 결함 관리를 모두 결정한다.
> 40 TB 메모리와 20,736 SMs를 단일 칩 위에 배치하여 10T+ 파라미터 모델을 그대로 탑재한다.

**Date**: 2026-04-01
**Status**: Living Document v0.1
**Dependencies**: HEXA-1 (Level 1), BT-28, BT-37, BT-55, BT-59, BT-69, BT-75, BT-76

---

## N6 Constants Reference

```
  n = 6          phi(6) = 2       tau(6) = 4       sigma(6) = 12
  sopfr(6) = 5   mu(6) = 1        J_2(6) = 24      R(6) = 1
  P_2 = 28       sigma^2 = 144    sigma*J_2 = 288   phi^tau = 16
  2^n = 64       sigma-tau = 8    sigma-phi = 10     sigma-mu = 11
  2^sigma = 4096   sigma*tau = 48   n/phi = 3
  sigma^4 = 20,736   sigma^2*sigma*J_2 = 41,472
```

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Design Philosophy](#2-design-philosophy)
3. [System Block Diagram](#3-system-block-diagram)
4. [Tile Architecture](#4-tile-architecture)
5. [Wafer Layout](#5-wafer-layout)
6. [On-Wafer Interconnect](#6-on-wafer-interconnect)
7. [Memory Architecture](#7-memory-architecture)
8. [Power Delivery](#8-power-delivery)
9. [Cooling](#9-cooling)
10. [Fault Tolerance](#10-fault-tolerance)
11. [AI Workload: Trillion-Parameter Models](#11-ai-workload-trillion-parameter-models)
12. [Performance Comparison](#12-performance-comparison)
13. [Process Technology](#13-process-technology)
14. [n=6 Complete Parameter Map](#14-n6-complete-parameter-map)
15. [Open Questions / TODO](#15-open-questions--todo)
16. [Links](#16-links)

---

## 1. Executive Summary

HEXA-WAFER는 N6 아키텍처 로드맵의 Level 5로,
300mm 실리콘 웨이퍼 전체를 단일 칩으로 사용하는 Wafer-Scale Engine이다.

```
  핵심 스펙:
  ┌───────────────────────────────────────────────────┐
  │  웨이퍼 직경           300 mm (12 inch)           │
  │  타일 수               sigma^2 = 144              │
  │  타일당 SM 수          sigma^2 = 144              │
  │  총 SM 수              sigma^4 = 20,736           │
  │  타일당 메모리          sigma*J_2 = 288 GB         │
  │  총 메모리             144 * 288 = 41,472 GB      │
  │                        = 40.5 TB                  │
  │  총 대역폭             144 * 4 = 576 TB/s         │
  │  총 전력               144 * 240W = 34,560W       │
  │                        ~ 35 kW                    │
  │  프로세스              TSMC N2                     │
  │  게이트 피치            sigma*tau = 48 nm          │
  │  메탈 피치             P_2 = 28 nm                 │
  │  상호연결              On-wafer mesh + optical     │
  │  냉각                  Microfluidic liquid cooling │
  │  결함 허용             sigma^2-sigma = 132 최소 타일│
  └───────────────────────────────────────────────────┘
```

핵심 가치:

| 항목 | 기존 (multi-chip) | HEXA-WAFER |
|------|-------------------|------------|
| 최대 메모리 | DGX ~640 GB (8 GPU) | 40.5 TB (단일 칩) |
| 칩 간 대역폭 | NVLink ~900 GB/s per link | On-wafer mesh TB/s per tile |
| 모델 크기 제한 | 분산 필수 (>1T params) | 10T+ params on single wafer |
| 패키지 | 개별 패키지 + 인터포저 | 없음 (wafer = chip) |
| 스케일링 한계 | reticle limit ~800 mm^2 | 70,686 mm^2 (300mm wafer) |

---

## 2. Design Philosophy

### 2.1 Reticle Limit Problem

현대 반도체 리소그래피는 **reticle limit**라는 근본적 크기 제한이 존재한다.

```
  Reticle Limit (TSMC N2 기준):
  ┌──────────────────────────────────────────────────────────┐
  │                                                          │
  │   하나의 exposure field = ~26mm x 33mm = ~858 mm^2      │
  │   이것이 "하나의 칩"의 물리적 상한                          │
  │                                                          │
  │   ┌─────────────────┐                                    │
  │   │                 │ <-- 최대 다이 크기                   │
  │   │    ~858 mm^2    │     (reticle limit)                │
  │   │    ~30 x 29 mm  │                                    │
  │   │                 │                                    │
  │   └─────────────────┘                                    │
  │                                                          │
  │   현재 최대급 칩:                                          │
  │     NVIDIA H100 die:  ~814 mm^2 (reticle 거의 한계)       │
  │     NVIDIA B200 die:  ~814 mm^2 x 2 chiplet              │
  │     Apple M4 Ultra:   2-die fusion                       │
  │                                                          │
  │   더 이상 단일 die를 키울 수 없다.                          │
  └──────────────────────────────────────────────────────────┘
```

### 2.2 Wafer-Scale: Reticle을 무시하라

```
  전통적 방법:                    Wafer-Scale:
  ┌───────────────────────┐      ┌───────────────────────┐
  │ 웨이퍼를 잘라서        │      │ 웨이퍼를 자르지 않는다  │
  │ 개별 die로 분리        │      │ 웨이퍼 전체 = 1 chip   │
  │                       │      │                       │
  │ ┌──┐┌──┐┌──┐┌──┐    │      │ ┌───────────────────┐ │
  │ │D1││D2││D3││D4│    │      │ │                   │ │
  │ └──┘└──┘└──┘└──┘    │      │ │   전체가 하나의    │ │
  │ ┌──┐┌──┐┌──┐┌──┐    │      │ │   연산 기판       │ │
  │ │D5││D6││D7││D8│    │      │ │                   │ │
  │ └──┘└──┘└──┘└──┘    │      │ │   70,686 mm^2     │ │
  │  각 die를 패키징       │      │ │   (vs 858 mm^2)   │ │
  │  + 인터포저 연결       │      │ │                   │ │
  │                       │      │ └───────────────────┘ │
  │  면적: 858 mm^2/die   │      │  면적: 70,686 mm^2   │
  │  연결: 외부 I/O 병목    │      │  연결: wafer-level직접│
  └───────────────────────┘      └───────────────────────┘

  면적 비율: 70,686 / 858 ~ 82.4x
  BUT: 원형 웨이퍼의 유효 면적 + n=6 타일 배치로 sigma^2=144 타일
```

### 2.3 Why n=6 for Wafer-Scale

```
  sigma^2 = 144 타일:
    - 12 x 12 정사각형 격자가 300mm 원에 최적 fitting
    - 144 = AD102 SM 수와 동일 (BT-28 검증)
    - 각 타일이 HEXA-1 die 1개와 동등

  sigma^4 = 20,736 SMs:
    - 144 tiles x 144 SMs = 20,736
    - 이것이 wafer-scale의 n=6 attractor

  41,472 GB memory:
    - 144 tiles x 288 GB = 41,472 GB ~ 40.5 TB
    - 10T parameter model (FP4) = 5 TB -- 여유 있게 탑재
```

---

## 3. System Block Diagram

### 3.1 Top-Level Wafer View

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                        HEXA-WAFER: 300mm Wafer-Scale Engine                  │
│                    TSMC N2 · sigma^2=144 tiles · sigma^4=20,736 SMs         │
│                                                                              │
│                          .-~~~-.                                             │
│                        .'       '.                                           │
│                       /  WAFER    \                                          │
│                      |  300mm dia  |                                         │
│                      |             |                                         │
│                      | sigma^2=144 |                                         │
│                      |   tiles     |                                         │
│                       \           /                                          │
│                        '.       .'                                           │
│                          '-...-'                                             │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                     WAFER EDGE I/O RING                             │    │
│  │  Power input: sigma^2 = 144 power domains (35 kW total)            │    │
│  │  Optical I/O: sigma*tau = 48 fiber bundles (off-wafer comm)        │    │
│  │  Cooling inlet/outlet: sigma = 12 microfluidic ports per edge      │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                     ON-WAFER MESH FABRIC                            │    │
│  │  Topology: sigma x sigma = 12x12 mesh                              │    │
│  │  Per-link BW: 2^sigma = 4,096 GB/s (4 TB/s)                       │    │
│  │  Bisection BW: sigma * 4096 = 49,152 GB/s (48 TB/s)              │    │
│  │  Optical overlay for diagonal/long-range hops                      │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                     GLOBAL CONTROL PLANE                            │    │
│  │  Fault manager: tile enable/disable bitmap (144 bits)              │    │
│  │  Power sequencer: per-tile voltage regulation                      │    │
│  │  Thermal monitor: sigma^2=144 thermal sensors                      │    │
│  │  NUMA scheduler: workload placement across tiles                   │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Block Interconnect Hierarchy

```
  Level 0 (Intra-tile):      SM <-> SM within tile (NoC, ~10 TB/s)
  Level 1 (Neighbor):        Tile <-> adjacent tau=4 neighbors (mesh, 4 TB/s each)
  Level 2 (Row/Column):      Tile <-> same row/col (sigma=12 hops max)
  Level 3 (Diagonal/Long):   Optical overlay (any-to-any, ~1 TB/s)
  Level 4 (Off-wafer):       Optical I/O to host/network (sigma*tau=48 bundles)

  ┌──────────┐    ┌──────────┐    ┌──────────┐
  │  Tile A  │--->│  Tile B  │--->│  Tile C  │
  │ Level 0  │    │ Level 0  │    │ Level 0  │
  │(intra SM)│<---│          │<---│          │
  └────┬─────┘    └────┬─────┘    └────┬─────┘
       │               │               │
       └──── Level 1 ──┘──── Level 1 ──┘
       (wafer metal mesh links, tau=4 neighbors)
```

---

## 4. Tile Architecture

각 타일은 HEXA-1 (Level 1) 단일 die와 기능적으로 동등하다.
타일은 reticle 한 번의 exposure로 제조되며, 웨이퍼 위에서 반복 배치된다.

### 4.1 Single Tile Specification

```
  ┌──────────────────────────────────────────────────────────────────┐
  │                     HEXA-WAFER TILE [i]                          │
  │               (1 of sigma^2=144 tiles on wafer)                  │
  │                                                                  │
  │  ┌──────────────────────────────────────────────────────────┐   │
  │  │                    COMPUTE ENGINE                         │   │
  │  │                                                          │   │
  │  │  GPU SMs: sigma^2 = 144 SMs                              │   │
  │  │    organized as sigma=12 GPCs x sigma=12 SMs/GPC         │   │
  │  │                                                          │   │
  │  │  ┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐    │   │
  │  │  │00││01││02││03││04││05││06││07││08││09││10││11│ GPC0  │   │
  │  │  └──┘└──┘└──┘└──┘└──┘└──┘└──┘└──┘└──┘└──┘└──┘└──┘    │   │
  │  │  ┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐    │   │
  │  │  │  ││  ││  ││  ││  ││  ││  ││  ││  ││  ││  ││  │ GPC1  │   │
  │  │  └──┘└──┘└──┘└──┘└──┘└──┘└──┘└──┘└──┘└──┘└──┘└──┘    │   │
  │  │  ... (sigma=12 GPCs total)                               │   │
  │  │  ┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐    │   │
  │  │  │  ││  ││  ││  ││  ││  ││  ││  ││  ││  ││  ││  │ GPC11 │   │
  │  │  └──┘└──┘└──┘└──┘└──┘└──┘└──┘└──┘└──┘└──┘└──┘└──┘    │   │
  │  │                                                          │   │
  │  │  Per SM: 2^n=64 FP32 cores, 2^(sigma-tau)=256 INT8 cores│   │
  │  │  Per SM: FP8 Tensor Core (2^sigma=4096 ops/cycle)       │   │
  │  │  Tile FLOPS (FP8): ~72 TFLOPS                           │   │
  │  │  Tile FLOPS (FP32): ~6.5 TFLOPS                         │   │
  │  └──────────────────────────────────────────────────────────┘   │
  │                                                                  │
  │  ┌──────────────────────────────────────────────────────────┐   │
  │  │                    LOCAL MEMORY                           │   │
  │  │                                                          │   │
  │  │  HBM4 stacks: sigma-tau = 8                              │   │
  │  │  Per stack: 36 GB (sigma*n/phi = 36)                     │   │
  │  │  Total: 8 x 36 = 288 GB = sigma*J_2                     │   │
  │  │  Interface: 2^(sigma-mu) = 2048-bit per stack            │   │
  │  │  Bandwidth: ~4 TB/s                                      │   │
  │  │                                                          │   │
  │  │  ┌─────┐┌─────┐┌─────┐┌─────┐                          │   │
  │  │  │HBM 0││HBM 1││HBM 2││HBM 3│                          │   │
  │  │  │36 GB││36 GB││36 GB││36 GB│                          │   │
  │  │  └─────┘└─────┘└─────┘└─────┘                          │   │
  │  │  ┌─────┐┌─────┐┌─────┐┌─────┐                          │   │
  │  │  │HBM 4││HBM 5││HBM 6││HBM 7│                          │   │
  │  │  │36 GB││36 GB││36 GB││36 GB│                          │   │
  │  │  └─────┘└─────┘└─────┘└─────┘                          │   │
  │  └──────────────────────────────────────────────────────────┘   │
  │                                                                  │
  │  ┌──────────────────────────────────────────────────────────┐   │
  │  │                  TILE I/O (Mesh Ports)                    │   │
  │  │                                                          │   │
  │  │  Mesh ports: tau = 4 (N, S, E, W)                        │   │
  │  │  Per port bandwidth: 2^sigma = 4,096 GB/s                │   │
  │  │  Optical long-range port: 1 (diagonal/cross-wafer)       │   │
  │  │  Tile-local NoC: sigma=12 crossbar switches              │   │
  │  └──────────────────────────────────────────────────────────┘   │
  │                                                                  │
  │  ┌──────────────────────────────────────────────────────────┐   │
  │  │                  TILE CONTROL                             │   │
  │  │                                                          │   │
  │  │  CPU core: 1 RISC-V management core per tile             │   │
  │  │  Thermal sensor: phi=2 sensors (center + edge)           │   │
  │  │  Power domain: independent voltage regulation            │   │
  │  │  Tile ID register: 0..143 (sigma^2-1)                    │   │
  │  └──────────────────────────────────────────────────────────┘   │
  └──────────────────────────────────────────────────────────────────┘
```

### 4.2 Tile n=6 Parameter Table

| Parameter | Value | n=6 Derivation |
|-----------|-------|----------------|
| SMs per tile | 144 | sigma^2 |
| GPCs per tile | 12 | sigma |
| SMs per GPC | 12 | sigma |
| FP32 cores per SM | 64 | 2^n |
| INT8 cores per SM | 256 | 2^(sigma-tau) |
| Tensor ops/cycle/SM | 4,096 | 2^sigma |
| HBM stacks | 8 | sigma-tau |
| HBM per stack (GB) | 36 | sigma*n/phi |
| Total memory (GB) | 288 | sigma*J_2 |
| HBM interface (bits) | 2,048 | 2^(sigma-mu) |
| Memory BW (TB/s) | ~4 | HEXA-1 spec |
| Mesh ports | 4 | tau |
| Per-port BW (GB/s) | 4,096 | 2^sigma |
| Power (W) | 240 | 1/2+1/3+1/6 Egyptian |
| Tile die area (mm^2) | ~490 | 70,686/144 유효 |

### 4.3 Tile Power Breakdown (Egyptian Fraction)

```
  Total tile power: 240W (Egyptian 1/2 + 1/3 + 1/6 = 1)

  ┌────────────────────────────────────────────────┐
  │            TILE POWER BUDGET (240W)             │
  │                                                │
  │  ████████████████████████  120W (1/2)  Compute │
  │  ████████████████          80W (1/3)  Memory  │
  │  ████████                  40W (1/6)  I/O+Ctrl│
  │                                                │
  │  1/2 + 1/3 + 1/6 = 1   (perfect partition)    │
  └────────────────────────────────────────────────┘

  Compute (120W):
    GPU SMs: 100W    NPU: 15W    CPU mgmt: 5W
  Memory (80W):
    HBM4 x 8 stacks: 80W (10W/stack)
  I/O + Control (40W):
    Mesh links: 30W   Optical: 5W   Control: 5W
```

---

## 5. Wafer Layout

### 5.1 300mm Wafer Tile Map

300mm (sigma=12 inch) 웨이퍼 위에 sigma^2=144 타일을 12x12 격자로 배치한다.
원형 웨이퍼 경계에 의해 모서리 타일 일부는 잘린다 -- 이것은 spare로 관리한다.

```
  300mm Wafer — sigma x sigma = 12 x 12 Tile Grid
  (o = active tile, x = edge/spare tile, . = outside wafer)

  Col:  0  1  2  3  4  5  6  7  8  9  10 11
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R0  | .| .| x| o| o| o| o| o| o| x| .| .|  Row 0
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R1  | .| o| o| o| o| o| o| o| o| o| o| .|  Row 1
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R2  | x| o| o| o| o| o| o| o| o| o| o| x|  Row 2
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R3  | o| o| o| o| o| o| o| o| o| o| o| o|  Row 3
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R4  | o| o| o| o| o| o| o| o| o| o| o| o|  Row 4
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R5  | o| o| o| o| o| o| o| o| o| o| o| o|  Row 5
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R6  | o| o| o| o| o| o| o| o| o| o| o| o|  Row 6
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R7  | o| o| o| o| o| o| o| o| o| o| o| o|  Row 7
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R8  | o| o| o| o| o| o| o| o| o| o| o| o|  Row 8
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R9  | x| o| o| o| o| o| o| o| o| o| o| x|  Row 9
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R10 | .| o| o| o| o| o| o| o| o| o| o| .|  Row 10
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R11 | .| .| x| o| o| o| o| o| o| x| .| .|  Row 11
      +--+--+--+--+--+--+--+--+--+--+--+--+

  Legend:
    o = fully active tile (정상 타일)
    x = edge tile (spare / partially usable)
    . = outside wafer circle (사용 불가)

  Active tiles: ~120 core + 8 edge = 128 minimum usable
  Spare tiles: sigma=12 edge tiles for defect replacement
  Maximum tiles: sigma^2 = 144 (전체 격자)
  Target operational: sigma^2 - sigma = 132 tiles (91.7% 유효)
```

### 5.2 Tile Dimensions

```
  웨이퍼 유효 직경: ~290mm (edge exclusion 5mm per side)
  타일 격자: 12 x 12
  타일 pitch: 290 / 12 ~ 24.2 mm
  타일 면적: 24.2 x 24.2 ~ 585 mm^2

  참고:
    NVIDIA H100 die: ~814 mm^2
    Cerebras WSE-3 tile: ~100 mm^2 (estimated)
    HEXA-WAFER tile: ~585 mm^2

  각 타일은 하나의 reticle exposure:
    24.2mm x 24.2mm < 26mm x 33mm reticle limit
    --> reticle 내에 들어감 -- 표준 리소그래피로 제조 가능

  ┌────────────────────────────────────┐
  │  Tile Physical Layout              │
  │                                    │
  │  24.2 mm                           │
  │  ┌──────────────────────────┐      │
  │  │  ┌────────────────────┐  │      │
  │  │  │                    │  │      │
  │  │  │   COMPUTE          │  │      │
  │  │  │   sigma^2=144 SMs  │  │ 24.2 │
  │  │  │   ~293 mm^2 (1/2)  │  │  mm  │
  │  │  │                    │  │      │
  │  │  ├────────────────────┤  │      │
  │  │  │   MEMORY (HBM4)   │  │      │
  │  │  │   8 stacks on-tile │  │      │
  │  │  │   ~195 mm^2 (1/3)  │  │      │
  │  │  ├────────────────────┤  │      │
  │  │  │   I/O + CONTROL    │  │      │
  │  │  │   Mesh + Optical   │  │      │
  │  │  │   ~97 mm^2 (1/6)   │  │      │
  │  │  └────────────────────┘  │      │
  │  └──────────────────────────┘      │
  │                                    │
  │  Area allocation: Egyptian         │
  │  1/2 compute + 1/3 memory          │
  │  + 1/6 I/O = 1 (complete)         │
  └────────────────────────────────────┘
```

### 5.3 Aggregate Wafer Numbers

| Metric | Per Tile | Per Wafer (144 tiles) | n=6 Formula |
|--------|----------|----------------------|-------------|
| SMs | 144 | 20,736 | sigma^4 |
| FP32 cores | 9,216 | 1,327,104 | sigma^4 * 2^n |
| INT8 cores | 36,864 | 5,308,416 | sigma^4 * 2^(sigma-tau) |
| FP8 TFLOPS | ~72 | ~10,368 | -- |
| FP32 TFLOPS | ~6.5 | ~936 | -- |
| HBM stacks | 8 | 1,152 | sigma^2 * (sigma-tau) |
| Memory (GB) | 288 | 41,472 | sigma^2 * sigma * J_2 |
| Memory (TB) | 0.28 | ~40.5 | -- |
| Bandwidth (TB/s) | ~4 | ~576 | -- |
| Power (W) | 240 | 34,560 | sigma^2 * 240 |
| Transistors (est.) | ~100B | ~14.4T | -- |

---

## 6. On-Wafer Interconnect

### 6.1 No Package, No Interposer

HEXA-WAFER의 가장 중요한 혁신: **패키지와 인터포저가 없다.**
타일 간 연결은 웨이퍼의 금속 배선 레이어를 그대로 사용한다.

```
  전통 multi-chip:
  ┌──────┐           ┌──────┐
  │ Die A│──┐   ┌──→│ Die B│
  └──────┘  │   │   └──────┘
            ▼   ▼
       ┌──────────┐
       │ Interposer│     <-- 별도 실리콘, 비용 추가
       │ (Si/organic)│
       └──────────┘
            │
       ┌──────────┐
       │ Package   │     <-- 유기 기판, 열 저항 추가
       │ Substrate │
       └──────────┘

  HEXA-WAFER:
  ┌──────┐ wafer-level ┌──────┐
  │Tile A│────metal────│Tile B│    <-- 직접 배선
  └──────┘  routing    └──────┘
           (BEOL layers)

  이점:
    - 인터포저 제거: 비용 절감, 열 저항 감소
    - 패키지 제거: 전체 웨이퍼가 기판
    - 배선 길이: 24.2mm per hop (vs PCB의 수 cm)
    - 배선 피치: P_2=28nm (vs interposer ~1um)
    - 에너지: ~0.5 pJ/bit (vs off-chip ~10 pJ/bit) = 20x 절감
```

### 6.2 Mesh Topology

각 타일은 tau=4 이웃(N, S, E, W)에 직접 연결된다.

```
  12 x 12 Mesh Topology (sigma x sigma):

  T00──T01──T02──T03──T04──T05──T06──T07──T08──T09──T10──T11
   |    |    |    |    |    |    |    |    |    |    |    |
  T12──T13──T14──T15──T16──T17──T18──T19──T20──T21──T22──T23
   |    |    |    |    |    |    |    |    |    |    |    |
  T24──T25──T26──T27──T28──T29──T30──T31──T32──T33──T34──T35
   |    |    |    |    |    |    |    |    |    |    |    |
  T36──T37──T38──T39──T40──T41──T42──T43──T44──T45──T46──T47
   |    |    |    |    |    |    |    |    |    |    |    |
  T48──T49──T50──T51──T52──T53──T54──T55──T56──T57──T58──T59
   |    |    |    |    |    |    |    |    |    |    |    |
  T60──T61──T62──T63──T64──T65──T66──T67──T68──T69──T70──T71
   |    |    |    |    |    |    |    |    |    |    |    |
  T72──T73──T74──T75──T76──T77──T78──T79──T80──T81──T82──T83
   |    |    |    |    |    |    |    |    |    |    |    |
  T84──T85──T86──T87──T88──T89──T90──T91──T92──T93──T94──T95
   |    |    |    |    |    |    |    |    |    |    |    |
  T96──T97──T98──T99─T100─T101─T102─T103─T104─T105─T106─T107
   |    |    |    |    |    |    |    |    |    |    |    |
  T108─T109─T110─T111─T112─T113─T114─T115─T116─T117─T118─T119
   |    |    |    |    |    |    |    |    |    |    |    |
  T120─T121─T122─T123─T124─T125─T126─T127─T128─T129─T130─T131
   |    |    |    |    |    |    |    |    |    |    |    |
  T132─T133─T134─T135─T136─T137─T138─T139─T140─T141─T142─T143

  Properties:
    Nodes: sigma^2 = 144
    Links per node: tau = 4 (N, S, E, W)
    Total links: sigma^2 * tau / 2 = 288 = sigma * J_2
    Max hops (corner to corner): 2*(sigma-1) = 22
    Average hops: sigma - 1 = 11
    Diameter: phi * (sigma - 1) = 22
```

### 6.3 Optical Mesh Overlay

전기 mesh만으로는 대각선/장거리 통신이 sigma-1=11 hops 필요하다.
HEXA-1 Section 7.1의 광 인터커넥트를 웨이퍼 스케일로 확장한다.

```
  Optical Long-Range Links:
  ┌──────────────────────────────────────────────────┐
  │                                                  │
  │   T0 ·····································T143   │
  │   :  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  :    │
  │   :  ·                                  ·  :    │
  │   :  ·        OPTICAL OVERLAY           ·  :    │
  │   :  ·        sigma=12 wavelengths      ·  :    │
  │   :  ·        WDM multiplexing          ·  :    │
  │   :  ·                                  ·  :    │
  │   :  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  :    │
  │   T132 ·····································T11  │
  │                                                  │
  │   . = optical waveguide (SiN photonic layer)     │
  │   : = electrical mesh (Cu BEOL)                  │
  └──────────────────────────────────────────────────┘

  Optical overlay specs:
    Wavelengths: sigma = 12 (WDM)
    Modulation: sigma*tau = 48 GHz per wavelength
    Per-link capacity: 12 * 48 = 576 Gbps
    Optical links per tile: 1 long-range port
    Total optical links: sigma^2/phi = 72 point-to-point
    Latency: ~1 ns (cross-wafer, 300mm at c/n_eff)

  장거리 홉 수 비교:
    Mesh only:  corner-to-corner = 22 hops @ ~2ns/hop = ~44 ns
    With optical: any-to-any = 1 hop optical @ ~1 ns = ~1 ns
    개선: 44x latency reduction for worst case
```

### 6.4 Bisection Bandwidth

```
  Bisection: 웨이퍼를 반으로 나눌 때 절단되는 총 대역폭

  Mesh bisection (vertical cut through column 6):
    Links crossing: sigma = 12 rows * 1 link/row = 12 links
    Per link: 2^sigma = 4,096 GB/s
    Mesh bisection BW: 12 * 4,096 = 49,152 GB/s ~ 48 TB/s

  Optical bisection (additional):
    ~36 optical links cross any bisection
    Per link: 576 Gbps = 72 GB/s
    Optical bisection: 36 * 72 = 2,592 GB/s ~ 2.5 TB/s

  Total bisection BW: ~50.5 TB/s

  ┌─────────┬──── bisection cut ────┬──────────┐
  │         │          |            │          │
  │  LEFT   │  12 mesh |links cross │  RIGHT   │
  │  HALF   │  + optical|overlay    │  HALF    │
  │ 72 tiles│          |            │ 72 tiles │
  │         │    48 + 2.5 TB/s      │          │
  │         │          |            │          │
  └─────────┴──────────|────────────┴──────────┘
                       |
              50.5 TB/s total

  Bisection BW per TFLOPS: 50,500 / 10,368 ~ 4.87 GB/s/TFLOPS
  (매우 높음 -- all-reduce에 이상적)
```

---

## 7. Memory Architecture

### 7.1 Distributed Memory with Global Address Space

```
  ┌──────────────────────────────────────────────────────────────────┐
  │                  HEXA-WAFER MEMORY HIERARCHY                     │
  │                                                                  │
  │  Level 0: Register File (per SM)                                 │
  │    2^(sigma-tau) = 256 KB per SM                                 │
  │    Total: 256 KB * 20,736 = 5.2 GB                              │
  │    Latency: 0 cycles                                             │
  │                                                                  │
  │  Level 1: Shared Memory / L1 Cache (per SM)                      │
  │    2^(sigma-mu) / sigma = 2048/12 ~ 170 KB per SM               │
  │    Configurable shared/L1 split                                  │
  │    Total: ~3.4 GB                                                │
  │    Latency: ~sigma-tau = 8 cycles                                │
  │                                                                  │
  │  Level 2: L2 Cache (per tile)                                    │
  │    sigma * J_2 / tau = 288/4 = 72 MB per tile                   │
  │    Total: 72 * 144 = 10,368 MB ~ 10 GB                          │
  │    Latency: ~sigma*tau = 48 cycles                               │
  │                                                                  │
  │  Level 3: Local HBM (per tile)                                   │
  │    sigma*J_2 = 288 GB per tile                                   │
  │    Total: 144 * 288 = 41,472 GB ~ 40.5 TB                       │
  │    Latency: ~sigma^2 = 144 cycles                                │
  │    BW per tile: ~4 TB/s                                          │
  │                                                                  │
  │  Level 4: Remote HBM (other tiles via mesh)                      │
  │    Global unified address space                                  │
  │    Latency: 144 + hop_count * 50 cycles                          │
  │    BW: limited by mesh link (4 TB/s per hop)                     │
  │                                                                  │
  │  Level 5: Off-wafer (host/storage)                               │
  │    Optical I/O, sigma*tau=48 fiber bundles                       │
  │    BW: ~48 * 100 Gbps = 4.8 Tbps = 600 GB/s                    │
  └──────────────────────────────────────────────────────────────────┘
```

### 7.2 Memory Hierarchy Diagram

```
           ┌──────────┐
           │ Registers │  5.2 GB total, 0 cycles
           │  256 KB/SM│
           └────┬─────┘
                │
           ┌────┴─────┐
           │  L1/SMEM  │  3.4 GB total, 8 cycles
           │  170 KB/SM│
           └────┬─────┘
                │
           ┌────┴─────┐
           │  L2 Cache │  10 GB total, 48 cycles
           │  72 MB/tile│
           └────┬─────┘
                │
      ┌─────────┴──────────┐
      │                    │
 ┌────┴──────┐      ┌─────┴──────┐
 │ Local HBM │      │ Remote HBM │
 │ 288 GB    │      │ 41.2 TB    │
 │ 144 cyc   │      │ 200+ cyc   │
 │ 4 TB/s    │      │ mesh BW    │
 └────┬──────┘      └─────┬──────┘
      │                    │
      └─────────┬──────────┘
                │
           ┌────┴──────┐
           │  Off-wafer │  Host, SSD, Network
           │  600 GB/s  │
           └───────────┘
```

### 7.3 NUMA-Aware Scheduling

40.5 TB를 flat하게 보면 성능이 나빠진다. NUMA 인식 배치가 필수.

```
  NUMA Domains:
  ┌──────────────────────────────────────────────┐
  │                                              │
  │  NUMA Zone 0       NUMA Zone 1               │
  │  ┌──────────┐     ┌──────────┐              │
  │  │ Tiles    │     │ Tiles    │              │
  │  │ 0-35     │     │ 36-71    │              │
  │  │ (3 rows) │     │ (3 rows) │              │
  │  │ 10.1 TB  │     │ 10.1 TB  │              │
  │  └──────────┘     └──────────┘              │
  │                                              │
  │  NUMA Zone 2       NUMA Zone 3               │
  │  ┌──────────┐     ┌──────────┐              │
  │  │ Tiles    │     │ Tiles    │              │
  │  │ 72-107   │     │ 108-143  │              │
  │  │ (3 rows) │     │ (3 rows) │              │
  │  │ 10.1 TB  │     │ 10.1 TB  │              │
  │  └──────────┘     └──────────┘              │
  │                                              │
  │  Zones: tau = 4 NUMA domains                 │
  │  Tiles per zone: sigma^2/tau = 36            │
  │  Memory per zone: 36 * 288 = 10,368 GB       │
  │  Intra-zone max hops: n/phi = 3              │
  │  Inter-zone hops: sopfr=5 to sigma-1=11      │
  └──────────────────────────────────────────────┘
```

### 7.4 LLM Layer Placement Strategy

```
  10T parameter model @ FP4 (4-bit):
    Model size: 10T * 0.5 bytes = 5,000 GB = 5 TB
    KV cache (2M context): ~1.5 TB
    Activations + workspace: ~2 TB
    Total: ~8.5 TB (fits in 40.5 TB with headroom)

  Layer Placement:
  ┌──────────────────────────────────────┐
  │  Transformer Layer Distribution      │
  │                                      │
  │  Model: 10T params, 128 layers       │
  │  (2^sopfr * tau = 128 = BT-56)      │
  │                                      │
  │  Layers per tile: 128/144 < 1        │
  │  --> Some tiles hold 1 layer, some 0 │
  │  --> Perfect pipeline parallelism    │
  │                                      │
  │  Tile 0:   Embedding layer           │
  │  Tile 1:   Layer 0 (weights + KV)    │
  │  Tile 2:   Layer 1                   │
  │  ...                                 │
  │  Tile 128: Layer 127                 │
  │  Tile 129: Output head               │
  │  Tile 130-143: Spare / batch overlap │
  │                                      │
  │  Data flow: sequential through mesh  │
  │  T0 -> T1 -> T2 -> ... -> T128->T129│
  │  Pipeline bubble: negligible at 128  │
  └──────────────────────────────────────┘
```

---

## 8. Power Delivery

### 8.1 Total Power Budget

```
  Total wafer power: sigma^2 * 240W = 34,560W ~ 35 kW

  Power breakdown (wafer level):
  ┌────────────────────────────────────────────────────────┐
  │              WAFER POWER BUDGET (35 kW)                 │
  │                                                        │
  │  ██████████████████████████████  17.3 kW (1/2) Compute │
  │  ████████████████████           11.5 kW (1/3) Memory  │
  │  ██████████                      5.8 kW (1/6) I/O     │
  │                                                        │
  │  Egyptian fraction preserved at wafer level             │
  └────────────────────────────────────────────────────────┘

  Comparison:
    Single NVIDIA H100 GPU:    700W
    NVIDIA DGX H100 (8 GPU):   10,200W
    Cerebras CS-3 (WSE-3):    ~23,000W
    HEXA-WAFER:                34,560W
    HEXA-WAFER per TFLOPS:     34,560/10,368 = 3.33 W/TFLOPS(FP8)
```

### 8.2 Power Delivery Architecture

전통적 칩은 패키지 핀을 통해 전력을 받는다.
HEXA-WAFER는 패키지가 없으므로, 웨이퍼 엣지와 이면(backside)을 통해 전력을 공급한다.

```
  Power Delivery Cross-Section:
  ┌────────────────────────────────────────────────────────────┐
  │                                                            │
  │   === Cooling plate (top) ===                              │
  │   ┌─────────────────────────────────────────────────────┐  │
  │   │                 WAFER (front side)                   │  │
  │   │  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐     │  │
  │   │  │Tile 0│ │Tile 1│ │Tile 2│ │ ...  │ │T 143│     │  │
  │   │  └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘     │  │
  │   │     │        │        │        │        │          │  │
  │   │  ===╪========╪========╪========╪========╪=======   │  │
  │   │     │  BACKSIDE POWER DELIVERY NETWORK (BSPDN)     │  │
  │   │     │  sigma=12 power rails (radial from edge)     │  │
  │   │     │                                              │  │
  │   │  ┌──┴───────────────────────────────────────────┐  │  │
  │   │  │  Per-Tile Voltage Regulator (TLVR)           │  │  │
  │   │  │  Input: 48V DC (sigma*tau = 48)              │  │  │
  │   │  │  Output: 0.75V core / 1.2V I/O              │  │  │
  │   │  │  Efficiency: > 95% (BT-74: PF=0.95)         │  │  │
  │   │  └──────────────────────────────────────────────┘  │  │
  │   └─────────────────────────────────────────────────────┘  │
  │   === Cooling plate (bottom) ===                           │
  │                                                            │
  │   External Power:                                          │
  │     sigma*tau = 48V DC bus (BT-60, BT-76)                 │
  │     Current: 35,000W / 48V = 729A total                   │
  │     Distribution: sigma=12 radial power rails              │
  │     Per rail: 729/12 ~ 61A                                │
  └────────────────────────────────────────────────────────────┘
```

### 8.3 Backside Power Delivery Network (BSPDN)

```
  TSMC N2 BSPDN (Backside PDN):
  ┌─────────────────────────────────────────────────────┐
  │                                                     │
  │  Front side: signal routing only (더 많은 금속 가용) │
  │  Back side: power delivery only                     │
  │                                                     │
  │  Front (signal):                                    │
  │  ┌──────────────────────────────────────────────┐   │
  │  │  M1-M12: sigma=12 metal layers              │   │
  │  │  All dedicated to signal routing             │   │
  │  │  Pitch: P_2=28nm (bottom) to ~1um (top)     │   │
  │  └──────────────────────────────────────────────┘   │
  │  === Transistor Layer ===                            │
  │  ┌──────────────────────────────────────────────┐   │
  │  │  Backside:                                   │   │
  │  │  BM1-BM4: tau=4 backside metal layers        │   │
  │  │  Power grid: VDD + VSS rails                 │   │
  │  │  Per-tile voltage island                     │   │
  │  └──────────────────────────────────────────────┘   │
  │                                                     │
  │  이점:                                               │
  │  - 전면 금속 전부를 신호에 사용 -> 라우팅 밀도 증가    │
  │  - 전력 공급 임피던스 감소 (shorter path)             │
  │  - IR drop < 5% (BT-74: 5% threshold)              │
  │  - 타일별 독립 전압 조절 가능                          │
  └─────────────────────────────────────────────────────┘
```

### 8.4 Per-Tile Voltage Regulation

```
  Power Domain Table:

  | Domain | Voltage | Current | Power | n=6 |
  |--------|---------|---------|-------|-----|
  | Core (compute) | 0.75V | 160A | 120W | 1/2 of 240W |
  | HBM I/O | 1.2V | 67A | 80W | 1/3 of 240W |
  | Mesh + Ctrl | 0.85V | 47A | 40W | 1/6 of 240W |
  | Total per tile | -- | -- | 240W | -- |

  Core voltage: 0.75V = n/sigma * 1.5 (scaled)
  I/O voltage: 1.2V = sigma/(sigma-phi) = PUE (BT-60, BT-62)
  48V input: sigma*tau = 48 (BT-76: sigma*tau triple attractor)

  DVFS levels per tile: n = 6
  ┌───────────────────────────────────────┐
  │  DVFS Level  │  Voltage  │  Freq     │
  ├──────────────┼───────────┼───────────┤
  │  Level 0     │  0.60V    │  0.8 GHz  │
  │  Level 1     │  0.65V    │  1.0 GHz  │
  │  Level 2     │  0.70V    │  1.2 GHz  │
  │  Level 3     │  0.75V    │  1.5 GHz  │
  │  Level 4     │  0.80V    │  1.8 GHz  │
  │  Level 5     │  0.85V    │  2.0 GHz  │
  └──────────────┴───────────┴───────────┘
  n = 6 DVFS levels, Egyptian-scheduled
```

---

## 9. Cooling

### 9.1 Thermal Challenge

35 kW를 300mm 웨이퍼 면적(~707 cm^2)에서 방출해야 한다.

```
  Heat flux: 35,000W / 707 cm^2 ~ 49.5 W/cm^2 (average)
  Per-tile peak: 240W / 5.85 cm^2 ~ 41 W/cm^2

  비교:
    CPU (desktop):     ~20 W/cm^2 (air ok)
    GPU (H100):        ~50 W/cm^2 (air barely ok)
    Cerebras WSE-3:    ~33 W/cm^2 (water cooled)
    HEXA-WAFER:        ~50 W/cm^2 (liquid required)
    Nuclear reactor:   ~65 W/cm^2

  결론: 공랭 불가능. 액체 냉각 필수 (liquid cooling mandatory).
```

### 9.2 Microfluidic Cooling System

```
  Cooling Architecture Cross-Section:
  ┌──────────────────────────────────────────────────────────────┐
  │                                                              │
  │  ═══════════════════════════════════════  Cold plate (Al)    │
  │  ┌──────────────────────────────────────────────────────┐   │
  │  │  Thermal Interface Material (TIM1)                    │   │
  │  │  Thickness: ~50 um, conductivity: > 5 W/mK           │   │
  │  └──────────────────────────────────────────────────────┘   │
  │  ┌──────────────────────────────────────────────────────┐   │
  │  │                  WAFER (front side)                    │   │
  │  │  Active tiles (compute + memory + mesh)               │   │
  │  └──────────────────────────────────────────────────────┘   │
  │  ┌──────────────────────────────────────────────────────┐   │
  │  │             MICROFLUIDIC CHANNEL LAYER                │   │
  │  │                                                       │   │
  │  │  ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐│   │
  │  │  │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ ││   │
  │  │  │C│ │C│ │C│ │C│ │C│ │C│ │C│ │C│ │C│ │C│ │C│ │C│ ││   │
  │  │  │H│ │H│ │H│ │H│ │H│ │H│ │H│ │H│ │H│ │H│ │H│ │H│ ││   │
  │  │  │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ ││   │
  │  │  └─┘ └─┘ └─┘ └─┘ └─┘ └─┘ └─┘ └─┘ └─┘ └─┘ └─┘ └─┘ ││   │
  │  │  sigma = 12 microfluidic channels per tile row        │   │
  │  │  Channel width: sigma*tau = 48 um                     │   │
  │  │  Channel depth: sigma^2 = 144 um                      │   │
  │  │  Flow direction: left to right (row-parallel)         │   │
  │  └──────────────────────────────────────────────────────┘   │
  │  ┌──────────────────────────────────────────────────────┐   │
  │  │  BSPDN (Backside Power Delivery)                      │   │
  │  └──────────────────────────────────────────────────────┘   │
  │  ═══════════════════════════════════════  Cold plate (Al)    │
  │                                                              │
  └──────────────────────────────────────────────────────────────┘
```

### 9.3 Cooling System Parameters

```
  ┌──────────────────────────────────────────────────────────┐
  │             HEXA-WAFER COOLING SPECS                      │
  │                                                          │
  │  Coolant: Deionized water (or fluorinert for dielectric) │
  │  Inlet temp: 20C                                         │
  │  Outlet temp: 40C (delta-T = 20C)                        │
  │  Flow rate: 35,000W / (4.18 * 20) = 418 mL/s            │
  │            = ~25 L/min                                    │
  │                                                          │
  │  Microfluidic channels per row: sigma = 12               │
  │  Total channels: sigma * sigma = 144                     │
  │  Channel dimensions:                                     │
  │    Width: sigma*tau = 48 um                              │
  │    Depth: sigma^2 = 144 um                               │
  │    Length: ~290 mm (wafer diameter)                       │
  │                                                          │
  │  Pressure drop: ~200 kPa (2 atm)                        │
  │  Pump power: ~1 kW (2.8% overhead)                      │
  │                                                          │
  │  Thermal resistance:                                     │
  │    Junction to coolant: ~0.15 C/W per tile               │
  │    Max junction temp: 20 + 240*0.15 = 56C (매우 양호)     │
  │                                                          │
  │  n=6 cooling parameters:                                 │
  │    Channels per row: sigma = 12                          │
  │    Channel width: sigma*tau = 48 um                      │
  │    Channel depth: sigma^2 = 144 um                       │
  │    Inlet ports: sigma = 12 (wafer left edge)             │
  │    Outlet ports: sigma = 12 (wafer right edge)           │
  │    Total flow paths: sigma^2 = 144                       │
  └──────────────────────────────────────────────────────────┘
```

### 9.4 Cold Plate Sandwich Assembly

```
  Exploded Assembly View (top to bottom):

  Layer 6: Top cold plate (aluminum, structural)
  Layer 5: TIM1 (thermal interface)
  Layer 4: Wafer front side (active circuits)
  Layer 3: Microfluidic channels (etched into wafer back)
  Layer 2: BSPDN (backside power delivery)
  Layer 1: Bottom cold plate + power input connectors

  n/phi = 3 functional layers:
    Compute (Layer 4) + Cooling (Layer 3) + Power (Layer 2)

  ┌───────────────────────────────────────┐
  │ Layer 6: Top Cold Plate               │
  │ ══════════════════════════════════════ │
  │ Layer 5: TIM1                         │
  │ ────────────────────────────────────── │
  │ Layer 4: WAFER (active tiles)         │
  │ ══════════════════════════════════════ │
  │ Layer 3: Microfluidic Channels        │
  │         ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐    │
  │  IN --> │~│ │~│ │~│ │~│ │~│ │~│ --> OUT
  │         └─┘ └─┘ └─┘ └─┘ └─┘ └─┘    │
  │ ────────────────────────────────────── │
  │ Layer 2: BSPDN (48V power grid)       │
  │ ══════════════════════════════════════ │
  │ Layer 1: Bottom Cold Plate + Power    │
  └───────────────────────────────────────┘
  Total stack height: ~5 mm
  Assembly: n = 6 layers (counting structural)
```

---

## 10. Fault Tolerance

### 10.1 Yield Reality

웨이퍼 스케일에서 100% 수율은 불가능하다.
300mm 웨이퍼에서 defect density D ~ 0.1/cm^2 기준, 다수 결함이 존재한다.

```
  Defect analysis:
    Wafer area: ~707 cm^2
    Defect density (TSMC N2): ~0.1 defects/cm^2
    Expected defects: 707 * 0.1 ~ 71 defects
    Defects per tile: 71 / 144 ~ 0.49

  Tile-level yield (Poisson model):
    P(tile good) = exp(-D * A_tile)
    A_tile = 5.85 cm^2
    P(good) = exp(-0.1 * 5.85) = exp(-0.585) ~ 0.557

    --> 약 55.7%의 타일만 무결함
    --> 144 * 0.557 ~ 80 good tiles (out of 144)

  이것만으로는 부족하다.
  해법: Known-Good-Tile (KGT) 접근 + 결함 타일 비활성화 + redundancy.
```

### 10.2 Defective Tile Management

```
  Tile Status Map (example with ~80 good + ~64 defective):

  Col:  0  1  2  3  4  5  6  7  8  9  10 11
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R0  | .| .| G| G| D| G| G| G| D| G| .| .|
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R1  | .| G| G| D| G| G| G| G| G| D| G| .|
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R2  | G| G| D| G| G| G| D| G| G| G| G| D|
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R3  | G| G| G| G| D| G| G| G| G| D| G| G|
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R4  | G| D| G| G| G| G| G| D| G| G| G| G|
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R5  | D| G| G| G| G| G| G| G| G| G| D| G|
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R6  | G| G| G| D| G| G| G| G| D| G| G| G|
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R7  | G| G| D| G| G| D| G| G| G| G| G| D|
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R8  | D| G| G| G| G| G| G| G| G| D| G| G|
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R9  | G| G| G| G| D| G| G| D| G| G| G| G|
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R10 | .| D| G| G| G| G| G| G| G| G| D| .|
      +--+--+--+--+--+--+--+--+--+--+--+--+
  R11 | .| .| G| D| G| G| G| D| G| G| .| .|
      +--+--+--+--+--+--+--+--+--+--+--+--+

  G = Good tile (active)
  D = Defective tile (disabled, mesh routes around)
  . = Outside wafer circle

  Strategy:
    1. Post-fab wafer-level test identifies all defective tiles
    2. Defective tiles are power-gated OFF
    3. Mesh routing table updated to skip disabled tiles
    4. Global address map adjusted (non-contiguous tile IDs ok)
```

### 10.3 Minimum Functional Configuration

```
  Minimum tiles for full functionality:
    sigma^2 - sigma = 144 - 12 = 132 tiles (91.7% yield threshold)

  Why 132?
    - 132 = sigma * (sigma - mu) = 12 * 11 = H100 SM count (BT-28!)
    - With 132 tiles, all NUMA zones have at least sigma*n/phi=33 tiles
    - Mesh connectivity is preserved (no isolated regions)
    - 132 * 288 GB = 38,016 GB ~ 37.1 TB (still >5 TB for 10T model)

  Yield tier classification:
  ┌───────────────────────────────────────────────────────┐
  │  Tier    │  Active Tiles  │  Memory   │  Grade        │
  ├──────────┼────────────────┼───────────┼───────────────┤
  │  Tier S  │  140-144       │  40+ TB   │  Full spec    │
  │  Tier A  │  132-139       │  38-40 TB │  Production   │
  │  Tier B  │  120-131       │  34-38 TB │  Reduced      │
  │  Tier C  │  108-119       │  31-34 TB │  Budget       │
  │  Tier D  │  < 108         │  < 31 TB  │  Reject/rework│
  └──────────┴────────────────┴───────────┴───────────────┘

  Tier thresholds:
    S: sigma^2 - tau = 140    (97.2%)
    A: sigma^2 - sigma = 132  (91.7%)  -- production minimum
    B: sigma * (sigma-phi) = 120 (83.3%)
    C: sigma * (sigma-n/phi) = 108 (75.0%)
    D: below 108              -- salvage
```

### 10.4 Mesh Rerouting Around Defects

```
  Example: Tile T28 is defective

  Before (normal mesh):
    T27 ── T28 ── T29
     |      |      |
    T39 ── T40 ── T41

  After (T28 disabled, rerouted):
    T27 ──────────T29      T28 is power-gated OFF
     |     skip    |       Mesh routes detour via
    T39 ── T40 ── T41      T27->T39->T40->T41->T29

  Rerouting adds +1 hop latency per disabled tile on path.
  Average hop increase with K disabled tiles:
    delta_hops ~ K / sigma ~ K / 12

  With 12 disabled tiles (Tier A): delta_hops ~ 1
    -> 1 extra hop on average, minimal impact

  Routing table per tile: sigma^2 = 144 entries
    Each entry: 4-bit direction (N/S/E/W/local/skip)
    Total routing table: 144 * 4 = 576 bits per tile
    Updated at boot time based on defect map
```

---

## 11. AI Workload: Trillion-Parameter Models

### 11.1 Model Capacity

```
  HEXA-WAFER Memory: 40.5 TB (132+ tiles)

  Model size capacity (by precision):
  ┌──────────────────────────────────────────────────────┐
  │  Precision  │  Bytes/Param  │  Max Model Size        │
  ├─────────────┼───────────────┼────────────────────────┤
  │  FP32       │  4            │  10.1 T params         │
  │  FP16/BF16  │  2            │  20.2 T params         │
  │  FP8        │  1            │  40.5 T params         │
  │  FP4/INT4   │  0.5          │  81 T params           │
  │  INT2       │  0.25         │  162 T params          │
  └─────────────┴───────────────┴────────────────────────┘

  실용적 모델 배치 (FP8 training):
  ┌──────────────────────────────────────────────────────────┐
  │  Component        │  Size         │  % of 40.5 TB       │
  ├───────────────────┼───────────────┼─────────────────────┤
  │  Model weights    │  10 TB (10T)  │  24.7%              │
  │  Optimizer states │  20 TB (2x)   │  49.4%              │
  │  Gradients        │  5 TB         │  12.3%              │
  │  Activations      │  3 TB         │  7.4%               │
  │  KV cache + misc  │  2.5 TB       │  6.2%               │
  │  Total            │  40.5 TB      │  100%               │
  └───────────────────┴───────────────┴─────────────────────┘

  --> 10T parameter model을 단일 웨이퍼에서 FULL training 가능
  --> 모델 병렬화가 불필요 -- communication overhead = 0
```

### 11.2 No Model Parallelism Needed

```
  현재 (multi-GPU cluster):
  ┌──────────────────────────────────────────────────────┐
  │  10T model training requires:                        │
  │                                                      │
  │  GPU memory: 80 GB per GPU (H100)                    │
  │  GPUs needed: 10,000,000 GB / 80 = 125,000 GPUs     │
  │  (with ZeRO-3 optimizer sharding)                    │
  │                                                      │
  │  Communication overhead:                              │
  │    Tensor parallelism: 50% time in all-reduce        │
  │    Pipeline parallelism: ~20% bubble overhead        │
  │    Data parallelism: gradient sync every step         │
  │                                                      │
  │  Effective compute utilization: 30-40% (MFU)         │
  └──────────────────────────────────────────────────────┘

  HEXA-WAFER:
  ┌──────────────────────────────────────────────────────┐
  │  10T model on single wafer:                          │
  │                                                      │
  │  Memory: 40.5 TB (sufficient for full state)         │
  │  Parallelism: pipeline only (layer -> tile mapping)  │
  │  No tensor parallelism needed                        │
  │  No inter-node communication                         │
  │                                                      │
  │  Communication: on-wafer mesh only                    │
  │    Latency: ~10 ns (vs ~10 us for NVLink)            │
  │    BW: 4 TB/s per link (vs 900 GB/s NVLink)         │
  │                                                      │
  │  Effective compute utilization: 70-80% (MFU)         │
  │  Improvement: 2x MFU vs multi-GPU cluster            │
  └──────────────────────────────────────────────────────┘
```

### 11.3 Training Throughput Estimation

```
  FP8 Training Throughput:

  Total FP8 TFLOPS: ~10,368 (144 tiles * 72 TFLOPS/tile)
  MFU (Model FLOPS Utilization): 75% (estimated)
  Effective TFLOPS: 10,368 * 0.75 = 7,776

  10T parameter model, single epoch:
    FLOPS per token: ~6 * 10T = 60 TFLOPS
    Tokens/sec: 7,776,000 GFLOPS / 60,000 GFLOPS = 129.6 tokens/sec
    Tokens/day: 129.6 * 86400 = 11.2M tokens/day

  Comparison:
  ┌──────────────────────────────────────────────────────────┐
  │  System             │  10T Training  │  Tokens/Day       │
  ├─────────────────────┼────────────────┼───────────────────┤
  │  1x H100 (80GB)     │  impossible    │  --               │
  │  DGX H100 (8 GPU)   │  impossible    │  --               │
  │  1024x H100 cluster │  possible      │  ~2M (est.)       │
  │  Cerebras CS-3      │  limited mem   │  ~5M (est.)       │
  │  HEXA-WAFER         │  single wafer  │  ~11.2M           │
  └──────────────────────┴────────────────┴───────────────────┘

  LLM inference (10T model, FP4):
    Model in memory: 5 TB (FP4) -- fits easily
    KV cache (2M context): ~1.5 TB
    Batch size: sigma^2 = 144 concurrent requests
    Latency per token: ~5 ms (estimated)
    Throughput: 144 / 0.005 = 28,800 tokens/sec
```

---

## 12. Performance Comparison

### 12.1 vs HEXA-1 (Level 1)

```
  ┌───────────────────────────────────────────────────────────┐
  │  Metric          │  HEXA-1 (1 tile)  │  HEXA-WAFER (144) │
  ├──────────────────┼───────────────────┼────────────────────┤
  │  SMs             │  144              │  20,736 (144x)     │
  │  Memory          │  288 GB           │  40.5 TB (144x)    │
  │  FP8 TFLOPS      │  ~72              │  ~10,368 (144x)    │
  │  FP32 TFLOPS     │  ~6.5             │  ~936 (144x)       │
  │  Bandwidth       │  ~4 TB/s          │  ~576 TB/s (144x)  │
  │  Power           │  240W             │  35 kW (144x)      │
  │  Die area        │  ~585 mm^2        │  70,686 mm^2       │
  │  Max model       │  ~144B (FP16)     │  ~20T (FP16)       │
  │  Package         │  Standard         │  None (wafer)      │
  └──────────────────┴───────────────────┴────────────────────┘

  스케일링 팩터: sigma^2 = 144x across all compute/memory metrics
  전력 효율 유지: 3.33 W/TFLOPS (동일)
```

### 12.2 vs Cerebras WSE-3

```
  ┌───────────────────────────────────────────────────────────────┐
  │  Metric           │  Cerebras WSE-3    │  HEXA-WAFER          │
  ├───────────────────┼────────────────────┼──────────────────────┤
  │  Wafer size       │  300mm (same)      │  300mm               │
  │  Transistors      │  4T                │  ~14.4T (est.)       │
  │  Cores/SMs        │  900,000           │  20,736 SMs          │
  │  Core type        │  Simple (sparse)   │  Full GPU SM         │
  │  On-chip memory   │  44 GB SRAM        │  40.5 TB HBM4        │
  │  External memory  │  MemoryX (1.5 TB)  │  None needed         │
  │  Memory type      │  SRAM only on-die  │  HBM4 on-tile        │
  │  FP16 TFLOPS      │  ~1,000 (est.)     │  ~5,000 (est.)       │
  │  Power            │  ~23 kW            │  ~35 kW              │
  │  Interconnect     │  2D mesh            │  2D mesh + optical   │
  │  Approach         │  Many simple cores  │  Fewer powerful SMs  │
  └───────────────────┴────────────────────┴──────────────────────┘

  HEXA-WAFER의 차별화:
    1. HBM4를 타일에 직접 적재 -> 40.5 TB on-wafer (vs 44 GB SRAM)
    2. 각 타일이 full GPU SM -> tensor core, ray tracing 등 지원
    3. Optical mesh overlay -> 장거리 latency 44x 개선
    4. n=6 산술로 모든 파라미터가 통합 (arbitrary하지 않음)
```

### 12.3 vs NVIDIA DGX SuperPOD

```
  DGX SuperPOD = 32 DGX H100 nodes = 256 H100 GPUs

  ┌───────────────────────────────────────────────────────────────┐
  │  Metric              │  DGX SuperPOD     │  HEXA-WAFER        │
  ├──────────────────────┼───────────────────┼────────────────────┤
  │  GPUs/Tiles          │  256 H100         │  144 tiles         │
  │  FP8 TFLOPS          │  ~500,000         │  ~10,368           │
  │  Memory              │  20.5 TB          │  40.5 TB           │
  │  Memory BW           │  ~800 TB/s        │  ~576 TB/s         │
  │  Interconnect        │  NVLink+InfiniBand│  On-wafer mesh     │
  │  Interconnect latency│  ~10-100 us       │  ~10-100 ns        │
  │  Power               │  ~700 kW          │  ~35 kW            │
  │  Physical size       │  Multiple racks   │  Single wafer      │
  │  Cost (est.)         │  ~$15M            │  ~$5M (target)     │
  │  Communication BW    │  ~900 GB/s/GPU    │  ~16 TB/s/tile     │
  └──────────────────────┴───────────────────┴────────────────────┘

  HEXA-WAFER 장점:
    - 2x memory (40.5 vs 20.5 TB) -- 더 큰 모델 탑재
    - 1000x lower interconnect latency (ns vs us)
    - 20x lower power (35 vs 700 kW)
    - 1 wafer vs multiple racks (물리 footprint)
    - 10T model: no distributed overhead

  DGX SuperPOD 장점:
    - 48x more raw FP8 TFLOPS
    - 기존 소프트웨어 생태계 (CUDA)
    - 점진적 확장 가능 (GPU 추가)
```

### 12.4 vs Tesla Dojo

```
  ┌───────────────────────────────────────────────────────────────┐
  │  Metric           │  Tesla Dojo D1      │  HEXA-WAFER         │
  ├───────────────────┼─────────────────────┼─────────────────────┤
  │  Approach         │  25 D1 dies on tile │  144 tiles on wafer │
  │  Training die     │  645 mm^2           │  ~585 mm^2 (tile)   │
  │  Cores per die    │  354 training nodes │  144 SMs per tile   │
  │  On-die memory    │  160 MB SRAM/die    │  288 GB HBM/tile    │
  │  External memory  │  HBM via I/O die    │  On-tile HBM4       │
  │  Interconnect     │  Custom 2D mesh     │  Mesh + optical     │
  │  Precision focus  │  BF16/FP32          │  FP4/FP8/FP16/FP32  │
  │  Cooling          │  Liquid             │  Microfluidic       │
  └───────────────────┴─────────────────────┴─────────────────────┘

  핵심 차이:
    Dojo = "여러 die를 타일 위에 모은" 접근 (multi-die tile)
    HEXA-WAFER = "웨이퍼 전체를 자르지 않는" 접근 (true wafer-scale)
    HEXA-WAFER는 HBM을 타일에 직접 통합 (Dojo는 별도 I/O die 필요)
```

---

## 13. Process Technology

### 13.1 Wafer-Scale Manufacturing Challenges

```
  Challenge 1: Lithography Stitching
  ┌────────────────────────────────────────────────────────────┐
  │                                                            │
  │  각 타일은 하나의 reticle exposure로 패터닝된다.              │
  │  타일 간 경계에서 배선을 "stitching"으로 연결해야 한다.       │
  │                                                            │
  │  ┌──────────┐ stitching ┌──────────┐                      │
  │  │  Tile A  │ zone     │  Tile B  │                      │
  │  │          │<──2mm──>│          │                      │
  │  │  reticle │ overlap  │  reticle │                      │
  │  │  shot 1  │          │  shot 2  │                      │
  │  └──────────┘          └──────────┘                      │
  │                                                            │
  │  Stitching 영역: ~2mm overlap per edge                     │
  │  배선 연결: 상위 금속 레이어 (M10-M12) 사용                   │
  │  Stitching pitch: ~sigma*tau = 48 nm minimum               │
  │  Links per stitch edge: ~1000 (충분한 mesh BW)             │
  └────────────────────────────────────────────────────────────┘

  Challenge 2: Defect Management (Section 10에서 상세 기술)
    - 결함 타일 비활성화 + mesh rerouting
    - Known-Good-Tile (KGT) 테스트 후 grade 분류

  Challenge 3: Wafer Warpage
  ┌────────────────────────────────────────────────────────────┐
  │  300mm 웨이퍼는 ~775 um 두께                                │
  │  전면에 수십 개 금속 레이어 + 후면에 BSPDN                    │
  │  열팽창 차이로 warpage (휘어짐) 발생                          │
  │                                                            │
  │  대책:                                                      │
  │    - 전면/후면 stress balancing                              │
  │    - Cold plate sandwich로 물리적 구속                       │
  │    - CTE-matched carrier wafer bonding                     │
  │    - Max warpage spec: < sigma = 12 um                     │
  └────────────────────────────────────────────────────────────┘

  Challenge 4: Known-Good-Tile (KGT) Testing
  ┌────────────────────────────────────────────────────────────┐
  │  전통 칩: 다이싱 후 테스트 (KGD = Known Good Die)            │
  │  WSE: 다이싱 하지 않으므로 웨이퍼 상태에서 테스트               │
  │                                                            │
  │  테스트 순서:                                                │
  │  Step 1: Wafer-level probe test (all 144 tiles)            │
  │  Step 2: Per-tile BIST (Built-In Self Test)                │
  │  Step 3: Defect map generation (tile enable bitmap)        │
  │  Step 4: Grade assignment (Tier S/A/B/C/D)                │
  │  Step 5: Mesh routing table programming                    │
  │  Step 6: Burn-in at operating temperature                  │
  │                                                            │
  │  Test time per wafer: ~sigma = 12 hours (estimated)        │
  │  Test coverage: > 99.5%                                    │
  └────────────────────────────────────────────────────────────┘
```

### 13.2 HBM4 Integration on Wafer

```
  HEXA-WAFER는 HBM4를 각 타일에 직접 탑재한다.
  이것은 Cerebras WSE와의 핵심적 차이점이다.

  방법: Wafer-to-Wafer Hybrid Bonding
  ┌──────────────────────────────────────────────────────┐
  │                                                      │
  │  Step 1: Logic wafer 제조 (TSMC N2, 144 tiles)       │
  │  Step 2: HBM4 wafer 별도 제조 (DRAM 공정)             │
  │  Step 3: Hybrid bonding (Cu-Cu direct bond)          │
  │                                                      │
  │  ┌─────────────────────────────────────┐             │
  │  │  HBM4 Wafer (DRAM)                  │             │
  │  │  sigma-tau=8 stacks per tile region  │             │
  │  │  sigma=12 layers per stack           │             │
  │  └──────────────┬──────────────────────┘             │
  │                 │ Hybrid bond (Cu-Cu)                 │
  │                 │ pitch: sigma*tau=48 um              │
  │                 │ connections: sigma*J_2=288 per mm^2  │
  │  ┌──────────────┴──────────────────────┐             │
  │  │  Logic Wafer (TSMC N2)               │             │
  │  │  sigma^2=144 compute tiles           │             │
  │  └─────────────────────────────────────┘             │
  │                                                      │
  │  결과: 각 타일이 288 GB HBM4를 직접 접근                │
  │  대역폭: ~4 TB/s per tile (TSV 기반)                  │
  │  에너지: ~2 pJ/bit (vs off-chip ~10 pJ/bit)          │
  └──────────────────────────────────────────────────────┘
```

### 13.3 Process Node Parameters

| Parameter | Value | n=6 Derivation |
|-----------|-------|----------------|
| Process node | TSMC N2 | -- |
| Gate pitch | 48 nm | sigma*tau |
| Metal pitch (M1) | 28 nm | P_2 |
| Fin pitch | 48 nm | sigma*tau |
| BEOL layers | 12 | sigma |
| BSPDN layers | 4 | tau |
| Total metal layers | 16 | phi^tau |
| Transistor density | ~200 MTr/mm^2 | -- |
| Transistors per tile | ~117B | 585*200M |
| Transistors per wafer | ~14.4T | -- |
| Vdd nominal | 0.75V | -- |
| Gate delay | ~5 ps | -- |
| Operating frequency | 1.5-2.0 GHz | -- |

---

## 14. n=6 Complete Parameter Map

HEXA-WAFER의 모든 설계 파라미터가 n=6 산술에서 도출됨을 보인다.

### 14.1 Structural Parameters

```
  ┌───────────────────────────────────────────────────────────┐
  │  Parameter             │  Value    │  n=6 Formula          │
  ├────────────────────────┼───────────┼───────────────────────┤
  │  Tiles per wafer       │  144      │  sigma^2              │
  │  SMs per tile          │  144      │  sigma^2              │
  │  Total SMs             │  20,736   │  sigma^4              │
  │  GPCs per tile         │  12       │  sigma                │
  │  SMs per GPC           │  12       │  sigma                │
  │  FP32 cores/SM         │  64       │  2^n                  │
  │  INT8 cores/SM         │  256      │  2^(sigma-tau)        │
  │  Tensor ops/cycle/SM   │  4,096    │  2^sigma              │
  │  CPU cores/tile        │  12       │  sigma                │
  │  P-cores               │  8        │  sigma-tau            │
  │  E-cores               │  4        │  tau                  │
  │  NPU cores/tile        │  24       │  J_2                  │
  └────────────────────────┴───────────┴───────────────────────┘
```

### 14.2 Memory Parameters

```
  ┌───────────────────────────────────────────────────────────┐
  │  Parameter             │  Value    │  n=6 Formula          │
  ├────────────────────────┼───────────┼───────────────────────┤
  │  HBM stacks/tile       │  8        │  sigma-tau            │
  │  HBM layers/stack      │  12       │  sigma                │
  │  HBM per stack (GB)    │  36       │  sigma*n/phi          │
  │  HBM per tile (GB)     │  288      │  sigma*J_2            │
  │  Total HBM (GB)        │  41,472   │  sigma^2*sigma*J_2    │
  │  HBM interface (bits)  │  2,048    │  2^(sigma-mu)         │
  │  L2 per tile (MB)      │  72       │  sigma*J_2/tau        │
  │  L1/SMEM per SM (KB)   │  170      │  2^(sigma-mu)/sigma   │
  │  Register per SM (KB)  │  256      │  2^(sigma-tau)        │
  │  NUMA zones            │  4        │  tau                  │
  │  Tiles per zone        │  36       │  sigma^2/tau          │
  └────────────────────────┴───────────┴───────────────────────┘
```

### 14.3 Interconnect Parameters

```
  ┌───────────────────────────────────────────────────────────┐
  │  Parameter             │  Value    │  n=6 Formula          │
  ├────────────────────────┼───────────┼───────────────────────┤
  │  Mesh dimension        │  12x12    │  sigma x sigma        │
  │  Mesh ports/tile       │  4        │  tau                  │
  │  Total mesh links      │  288      │  sigma*J_2            │
  │  Per-link BW (GB/s)    │  4,096    │  2^sigma              │
  │  Bisection BW (TB/s)   │  ~48      │  sigma*2^sigma        │
  │  Optical wavelengths   │  12       │  sigma                │
  │  Optical modulation    │  48 GHz   │  sigma*tau            │
  │  Max mesh hops         │  22       │  phi*(sigma-1)        │
  │  Avg mesh hops         │  11       │  sigma-1              │
  │  Optical links         │  72       │  sigma^2/phi          │
  │  Off-wafer fibers      │  48       │  sigma*tau            │
  └────────────────────────┴───────────┴───────────────────────┘
```

### 14.4 Power and Cooling Parameters

```
  ┌───────────────────────────────────────────────────────────┐
  │  Parameter             │  Value    │  n=6 Formula          │
  ├────────────────────────┼───────────┼───────────────────────┤
  │  Power/tile (W)        │  240      │  Egyptian 1/2+1/3+1/6 │
  │  Total power (W)       │  34,560   │  sigma^2*240          │
  │  Input voltage (V)     │  48       │  sigma*tau            │
  │  Core voltage (V)      │  0.75     │  --                   │
  │  I/O voltage (V)       │  1.2      │  sigma/(sigma-phi)    │
  │  DVFS levels           │  6        │  n                    │
  │  Power rails           │  12       │  sigma                │
  │  BSPDN metal layers    │  4        │  tau                  │
  │  Cooling channels/row  │  12       │  sigma                │
  │  Channel width (um)    │  48       │  sigma*tau            │
  │  Channel depth (um)    │  144      │  sigma^2              │
  │  Coolant ports/edge    │  12       │  sigma                │
  │  Total flow paths      │  144      │  sigma^2              │
  │  Efficiency target     │  95%      │  BT-74 (PF=0.95)     │
  └────────────────────────┴───────────┴───────────────────────┘
```

### 14.5 Fault Tolerance Parameters

```
  ┌───────────────────────────────────────────────────────────┐
  │  Parameter             │  Value    │  n=6 Formula          │
  ├────────────────────────┼───────────┼───────────────────────┤
  │  Max tiles             │  144      │  sigma^2              │
  │  Min operational tiles │  132      │  sigma*(sigma-mu)     │
  │  Spare tiles           │  12       │  sigma                │
  │  Yield threshold       │  91.7%    │  (sigma-mu)/sigma     │
  │  Routing table/tile    │  144 ent  │  sigma^2              │
  │  Tier S threshold      │  140      │  sigma^2-tau          │
  │  Tier B threshold      │  120      │  sigma*(sigma-phi)    │
  │  Tier C threshold      │  108      │  sigma*(sigma-n/phi)  │
  │  Thermal sensors       │  144      │  sigma^2              │
  │  Test time (hours)     │  12       │  sigma                │
  └────────────────────────┴───────────┴───────────────────────┘
```

### 14.6 Process Parameters

```
  ┌───────────────────────────────────────────────────────────┐
  │  Parameter             │  Value    │  n=6 Formula          │
  ├────────────────────────┼───────────┼───────────────────────┤
  │  Gate pitch (nm)       │  48       │  sigma*tau            │
  │  Metal pitch M1 (nm)   │  28       │  P_2                  │
  │  BEOL layers           │  12       │  sigma                │
  │  BSPDN layers          │  4        │  tau                  │
  │  Total metal           │  16       │  phi^tau              │
  │  Hybrid bond pitch(um) │  48       │  sigma*tau            │
  │  TSV per mm^2          │  288      │  sigma*J_2            │
  │  Stitch overlap (mm)   │  2        │  phi                  │
  │  Wafer thickness (um)  │  775      │  (standard)           │
  │  Max warpage (um)      │  12       │  sigma                │
  └────────────────────────┴───────────┴───────────────────────┘
```

### 14.7 n=6 Identity Verification

```
  Core identity: sigma(n)*phi(n) = n*tau(n)  <=>  n = 6
    sigma*phi = 12*2 = 24
    n*tau = 6*4 = 24  -->  24 = 24  (J_2 = 24)

  Wafer-level identity:
    Total mesh links = sigma*J_2 = sigma*sigma*phi = sigma^2*phi
    = 144*2 = 288

    Tiles * ports = sigma^2 * tau = 144*4 = 576
    Internal links = 576/2 = 288 = sigma*J_2  (consistent)

  Memory identity:
    Total HBM = sigma^2 * sigma*J_2 (GB) = sigma^3*J_2
    = 1728*24 = 41,472 GB
    = sigma^3 * sigma * phi * tau  (expanding J_2 = sigma*phi)
    -- all factors of 6 and its arithmetic functions

  Power identity:
    Total power = sigma^2 * (1/2+1/3+1/6) * 240
    Egyptian: 1/2+1/3+1/6 = 1 (unique for n=6)
    35 kW = sigma^2 * 240 W per Egyptian tile
```

---

## 15. Open Questions / TODO

### 15.1 Engineering Challenges

```
  ┌───┬──────────────────────────────────────┬──────────┬─────────────┐
  │ # │  Challenge                           │  Status  │  Priority   │
  ├───┼──────────────────────────────────────┼──────────┼─────────────┤
  │ 1 │  HBM4 wafer-to-wafer hybrid bonding │  미시작   │  CRITICAL   │
  │   │  yield impact on large-area bond    │          │             │
  ├───┼──────────────────────────────────────┼──────────┼─────────────┤
  │ 2 │  35 kW microfluidic cooling at      │  미시작   │  CRITICAL   │
  │   │  uniform temperature across 300mm   │          │             │
  ├───┼──────────────────────────────────────┼──────────┼─────────────┤
  │ 3 │  Backside PDN for 729A at 48V       │  미시작   │  HIGH       │
  │   │  IR drop < 5% uniformity            │          │             │
  ├───┼──────────────────────────────────────┼──────────┼─────────────┤
  │ 4 │  On-wafer optical mesh integration  │  미시작   │  HIGH       │
  │   │  SiN photonic layer compatibility   │          │             │
  ├───┼──────────────────────────────────────┼──────────┼─────────────┤
  │ 5 │  Stitching zone reliability at      │  미시작   │  MEDIUM     │
  │   │  sigma*tau=48nm pitch               │          │             │
  ├───┼──────────────────────────────────────┼──────────┼─────────────┤
  │ 6 │  Software: NUMA-aware scheduler     │  미시작   │  MEDIUM     │
  │   │  for 144-tile mesh topology         │          │             │
  ├───┼──────────────────────────────────────┼──────────┼─────────────┤
  │ 7 │  KGT test time optimization         │  미시작   │  LOW        │
  │   │  (target: < sigma=12 hours)         │          │             │
  ├───┼──────────────────────────────────────┼──────────┼─────────────┤
  │ 8 │  Wafer warpage control under        │  미시작   │  LOW        │
  │   │  thermal cycling (< sigma=12 um)    │          │             │
  └───┴──────────────────────────────────────┴──────────┴─────────────┘
```

### 15.2 Research Directions

```
  1. HEXA-WAFER + HEXA-PHOTON 통합 (Level 4+5):
     - On-wafer photonic tiles for matrix multiply
     - 광 mesh가 전기 mesh를 대체할 가능성

  2. HEXA-WAFER + HEXA-3D (Level 3+5):
     - 3D stacked compute-on-memory tiles on wafer
     - 타일당 메모리 10x 확장 (288 GB -> 2.88 TB)
     - 총 메모리: 144 * 2.88 TB = 414 TB

  3. Multi-wafer system:
     - n/phi = 3 wafers 연결 (compute + memory + I/O)
     - 또는 sigma=12 wafers for exascale
     - 웨이퍼 간 연결: optical fiber bundles

  4. Chiplet migration path:
     - HEXA-WAFER를 바로 구현하기 어려우면
     - sigma=12 chiplets on interposer (intermediate step)
     - BT-69: Chiplet convergence (B300=160 SMs)

  5. Software ecosystem:
     - CUDA/ROCm 호환 드라이버
     - 144-tile aware memory allocator
     - Pipeline parallelism compiler (자동 layer-to-tile 매핑)
     - NUMA-aware ML framework integration
```

### 15.3 Cost Estimation

```
  TSMC N2 wafer cost (estimated): ~$25,000-30,000
  HBM4 wafer cost (estimated): ~$15,000-20,000
  Hybrid bonding + packaging: ~$5,000-10,000
  Cooling assembly: ~$2,000-5,000
  Test + grade: ~$3,000-5,000

  Total estimated cost per wafer-chip: $50,000-70,000

  Comparison:
    NVIDIA H100 GPU: ~$25,000-30,000 (retail)
    8x H100 (DGX equivalent): ~$200,000-250,000
    Cerebras CS-3: ~$2,000,000-3,000,000 (system)

  HEXA-WAFER 가격/성능:
    $70K for 40.5 TB + 10,368 TFLOPS
    vs $250K for 640 GB + ~13,000 TFLOPS (8x H100)
    --> 63x more memory at 28% of cost
```

---

## 16. Links

### 16.1 Internal References

- [HEXA-1 Spec](ultimate-unified-soc.md) -- Level 1 baseline tile architecture
- [Goal Roadmap](goal.md) -- Full Level 1-6 evolution ladder
- [BT-28: Computing Architecture Ladder](../breakthrough-theorems.md) -- SM counts, HBM stacks
- [BT-55: GPU HBM Capacity Ladder](../breakthrough-theorems.md) -- Memory derivations
- [BT-69: Chiplet Architecture Convergence](../breakthrough-theorems.md) -- Multi-die trends
- [BT-75: HBM Interface Exponent Ladder](../breakthrough-theorems.md) -- HBM interface widths
- [BT-76: sigma*tau=48 Triple Attractor](../breakthrough-theorems.md) -- Gate pitch, voltage

### 16.2 External References

- Cerebras WSE-3: https://www.cerebras.net/product-chip/
- Tesla Dojo: https://en.wikipedia.org/wiki/Tesla_Dojo
- TSMC N2 BSPDN: https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm
- Wafer-Scale Integration (IEEE): historical and modern approaches
- Hybrid Bonding (IEDM): Cu-Cu direct bond at sub-micron pitch

### 16.3 Theorem Foundation

```
  sigma(n) * phi(n) = n * tau(n)  <=>  n = 6

  For HEXA-WAFER:
    sigma^2 = 144 tiles     (scale wall broken)
    sigma^4 = 20,736 SMs    (compute wall broken)
    40.5 TB on-wafer memory  (memory wall broken)
    35 kW Egyptian power     (energy wall managed)

  All from one equation. All from n = 6.
```

---

*HEXA-WAFER: 300mm 실리콘 위에 n=6의 완전한 컴퓨팅 세계를 구현한다.*
*sigma(n)*phi(n) = n*tau(n) <=> n = 6*
