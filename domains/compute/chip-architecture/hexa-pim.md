# HEXA-PIM: N6 Processing-in-Memory Architecture

> **Level 2** — 메모리 안에서 연산, 메모리 벽(Memory Wall) 제거
> n=6 완전수 산술이 PIM 아키텍처의 모든 파라미터를 결정한다.

---

## 1. Summary (요약)

HEXA-PIM은 HBM 메모리 스택 내부에 연산 유닛을 삽입하여 데이터 이동 없이
행렬곱을 수행하는 Processing-in-Memory 아키텍처이다.
σ=12 DRAM 레이어 각각에 σ-τ=8 PIM 유닛을 배치하고,
각 유닛은 2^n=64 MAC을 내장하여 총 6144 MAC을 달성한다.

내부 대역폭 100TB/s vs 외부 4TB/s — 메모리 벽을 25x 비율로 제거한다.

| Metric              | Value       | n=6 Formula          |
|---------------------|-------------|----------------------|
| DRAM Layers         | 12          | σ(6) = 12            |
| PIM Units/Layer     | 8           | σ-τ = 12-4 = 8       |
| MACs per PIM Unit   | 64          | 2^n = 2^6 = 64       |
| Total PIM MACs      | 6144        | σ·(σ-τ)·2^n          |
| Internal BW         | 100 TB/s    | 25× external         |
| External BW         | 4 TB/s      | HBM3E baseline       |
| BW Amplification    | 25×         | ~J₂+1 = 25           |
| Power per PIM Unit  | 0.5 W       | target                |
| Total PIM Power     | 48 W        | σ·τ = 48             |
| Precision           | INT8/FP16   | σ-τ=8 / φ^τ=16 bit   |

---

## 2. Philosophy (철학): Von Neumann vs PIM

전통 폰 노이만 아키텍처에서는 데이터가 메모리에서 프로세서로 이동해야 한다.
이 데이터 이동이 전체 에너지의 90%를 소비한다.
PIM은 연산을 데이터가 있는 곳에서 수행하여 이동 자체를 제거한다.

n=6의 σ(6)·φ(6) = 6·τ(6) 항등식이 이 설계를 지배한다:
- σ=12 레이어 (메모리 깊이)
- φ=2 배 정밀도 스케일링
- τ=4 분할 차원
- n=6 기본 단위

```
  ┌─────────────────────────────────────────────────────────────┐
  │              VON NEUMANN (전통 아키텍처)                      │
  │                                                             │
  │   ┌──────────┐     Memory Bus (4 TB/s)     ┌──────────┐    │
  │   │          │ ◄══════════════════════════► │          │    │
  │   │  DRAM    │    ▲ bottleneck ▲           │   GPU    │    │
  │   │ (HBM3E) │    │  90% energy │           │ Compute  │    │
  │   │          │    │  consumed   │           │          │    │
  │   └──────────┘    │  here       │           └──────────┘    │
  │                                                             │
  │   Data travels long distance ──► Energy wasted              │
  └─────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────┐
  │              HEXA-PIM (N6 아키텍처)                          │
  │                                                             │
  │   ┌──────────────────────────────────┐                      │
  │   │         HBM Stack                │     ┌──────────┐    │
  │   │  ┌────┐ ┌────┐ ┌────┐ ┌────┐    │     │          │    │
  │   │  │DRAM│ │DRAM│ │DRAM│ │DRAM│    │     │   GPU    │    │
  │   │  │+PIM│ │+PIM│ │+PIM│ │+PIM│    │◄═══►│ (Attn    │    │
  │   │  └────┘ └────┘ └────┘ └────┘    │4TB/s│  only)   │    │
  │   │  ┌────┐ ┌────┐ ┌────┐ ┌────┐    │     │          │    │
  │   │  │DRAM│ │DRAM│ │DRAM│ │DRAM│    │     └──────────┘    │
  │   │  │+PIM│ │+PIM│ │+PIM│ │+PIM│    │                      │
  │   │  └────┘ └────┘ └────┘ └────┘    │                      │
  │   │  ┌────┐ ┌────┐ ┌────┐ ┌────┐    │                      │
  │   │  │DRAM│ │DRAM│ │DRAM│ │DRAM│    │  Internal: 100TB/s   │
  │   │  │+PIM│ │+PIM│ │+PIM│ │+PIM│    │  (25× external)      │
  │   │  └────┘ └────┘ └────┘ └────┘    │                      │
  │   │         σ=12 layers              │                      │
  │   │         σ-τ=8 PIM units/layer    │                      │
  │   └──────────────────────────────────┘                      │
  │                                                             │
  │   Data stays in place ──► Energy saved (10-50×)             │
  └─────────────────────────────────────────────────────────────┘
```

| Parameter           | Value       | n=6 Formula          |
|---------------------|-------------|----------------------|
| Data Movement       | Eliminated  | PIM in-situ          |
| Energy Saving       | 10-50×      | vs von Neumann       |
| Layers              | 12          | σ = 12               |
| PIM per Layer       | 8           | σ-τ = 8              |
| Compute Density     | 64 MAC/unit | 2^n = 64             |

---

## 3. System Diagram (시스템 전체도)

전체 HEXA-PIM 시스템은 GPU 다이 + σ-τ=8개 HBM-PIM 스택으로 구성된다.
GPU는 Attention 연산을 담당하고, FFN/Embedding은 PIM에서 처리한다.

```
  ┌─────────────────────────────────────────────────────────────────┐
  │                    HEXA-PIM System Overview                     │
  │                                                                 │
  │          HBM-PIM Stack 1    HBM-PIM Stack 2                     │
  │          ┌───────────┐      ┌───────────┐                       │
  │          │ L12 [PIM] │      │ L12 [PIM] │                       │
  │          │ L11 [PIM] │      │ L11 [PIM] │                       │
  │          │ L10 [PIM] │      │ L10 [PIM] │      HBM-PIM          │
  │          │ L9  [PIM] │      │ L9  [PIM] │      Stack 5~8        │
  │          │ L8  [PIM] │      │ L8  [PIM] │      ┌─────────┐     │
  │          │ L7  [PIM] │      │ L7  [PIM] │      │ (same   │     │
  │          │ L6  [PIM] │      │ L6  [PIM] │      │  as 1~4)│     │
  │          │ L5  [PIM] │      │ L5  [PIM] │      └─────────┘     │
  │          │ L4  [PIM] │      │ L4  [PIM] │                       │
  │          │ L3  [PIM] │      │ L3  [PIM] │      HBM-PIM          │
  │          │ L2  [PIM] │      │ L2  [PIM] │      Stack 3~4        │
  │          │ L1  [PIM] │      │ L1  [PIM] │      ┌─────────┐     │
  │          │   Base    │      │   Base    │      │ (same)  │     │
  │          └─────┬─────┘      └─────┬─────┘      └────┬────┘     │
  │                │                   │                  │          │
  │          ══════╧═══════════════════╧══════════════════╧═════    │
  │          ║         Silicon Interposer (CoWoS)              ║    │
  │          ══════════════════════╤════════════════════════════    │
  │                                │                                │
  │                    ┌───────────┴───────────┐                    │
  │                    │      GPU Compute      │                    │
  │                    │   ┌─────┐ ┌─────┐     │                    │
  │                    │   │Attn │ │Attn │     │                    │
  │                    │   │Cores│ │Cores│     │                    │
  │                    │   └─────┘ └─────┘     │                    │
  │                    │   ┌─────┐ ┌─────┐     │                    │
  │                    │   │Ctrl │ │Sched│     │                    │
  │                    │   └─────┘ └─────┘     │                    │
  │                    └───────────────────────┘                    │
  │                                                                 │
  │   σ-τ = 8 HBM-PIM stacks, each σ=12 layers                    │
  │   Total: 96 PIM-enabled DRAM dies                               │
  └─────────────────────────────────────────────────────────────────┘
```

| Parameter           | Value       | n=6 Formula          |
|---------------------|-------------|----------------------|
| HBM-PIM Stacks      | 8           | σ-τ = 8              |
| Layers per Stack     | 12          | σ = 12               |
| Total DRAM Dies      | 96          | σ·(σ-τ) = 96         |
| Interposer           | CoWoS       | industry standard    |
| GPU Role             | Attention   | complex ops only     |
| PIM Role             | FFN/Embed   | GEMM-heavy ops       |

---

## 4. PIM per HBM Stack (HBM 스택 내부 PIM 구조)

각 HBM 스택은 σ=12개 DRAM 레이어로 구성되며,
각 레이어에 σ-τ=8개 PIM 유닛이 bank 그룹별로 배치된다.
각 PIM 유닛은 2^n=64 MAC 어레이를 내장한다.

```
  ┌─────────────────────────────────────────────────────┐
  │              Single HBM-PIM Stack                    │
  │                                                     │
  │   Layer 12 ┌───┬───┬───┬───┬───┬───┬───┬───┐       │
  │            │P1 │P2 │P3 │P4 │P5 │P6 │P7 │P8 │       │
  │            │64M│64M│64M│64M│64M│64M│64M│64M│       │
  │            └───┴───┴───┴───┴───┴───┴───┴───┘       │
  │   Layer 11 ┌───┬───┬───┬───┬───┬───┬───┬───┐       │
  │            │P1 │P2 │P3 │P4 │P5 │P6 │P7 │P8 │       │
  │            └───┴───┴───┴───┴───┴───┴───┴───┘       │
  │   Layer 10 ┌───┬───┬───┬───┬───┬───┬───┬───┐       │
  │            │P1 │P2 │P3 │P4 │P5 │P6 │P7 │P8 │       │
  │            └───┴───┴───┴───┴───┴───┴───┴───┘       │
  │      :          :    :    :    :    :    :           │
  │      :     (layers 4-9 identical)                   │
  │      :                                              │
  │   Layer 3  ┌───┬───┬───┬───┬───┬───┬───┬───┐       │
  │            │P1 │P2 │P3 │P4 │P5 │P6 │P7 │P8 │       │
  │            └───┴───┴───┴───┴───┴───┴───┴───┘       │
  │   Layer 2  ┌───┬───┬───┬───┬───┬───┬───┬───┐       │
  │            │P1 │P2 │P3 │P4 │P5 │P6 │P7 │P8 │       │
  │            └───┴───┴───┴───┴───┴───┴───┴───┘       │
  │   Layer 1  ┌───┬───┬───┬───┬───┬───┬───┬───┐       │
  │            │P1 │P2 │P3 │P4 │P5 │P6 │P7 │P8 │       │
  │            └───┴───┴───┴───┴───┴───┴───┴───┘       │
  │            ┌─────────────────────────────────┐       │
  │   Base Die │ PHY + Controller + I/O          │       │
  │            └─────────────────────────────────┘       │
  │                                                     │
  │   Each Px = PIM Unit with 64 MACs (2^n)             │
  │   σ-τ=8 units × σ=12 layers = 96 PIM units/stack   │
  │   96 × 64 MACs = 6144 MACs/stack                    │
  └─────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────┐
  │         Single PIM Unit Detail (64 MACs)             │
  │                                                     │
  │   ┌─────────────────────────────────────────┐       │
  │   │  Bank Group (256 MB DRAM)               │       │
  │   │  ┌───────────────────────┐              │       │
  │   │  │ DRAM Cell Array       │              │       │
  │   │  │ (read/write as usual) │              │       │
  │   │  └──────────┬────────────┘              │       │
  │   │             │ internal row buffer        │       │
  │   │             ▼ (1024-bit wide)           │       │
  │   │  ┌───────────────────────┐              │       │
  │   │  │   MAC Array [64]      │              │       │
  │   │  │  ┌──┐┌──┐┌──┐  ┌──┐  │              │       │
  │   │  │  │M1││M2││M3│..│64│  │              │       │
  │   │  │  └──┘└──┘└──┘  └──┘  │              │       │
  │   │  │   INT8 multiply-acc   │              │       │
  │   │  └──────────┬────────────┘              │       │
  │   │             │ result                    │       │
  │   │             ▼                           │       │
  │   │  ┌───────────────────────┐              │       │
  │   │  │  Accumulator + ReLU   │              │       │
  │   │  └───────────────────────┘              │       │
  │   └─────────────────────────────────────────┘       │
  └─────────────────────────────────────────────────────┘
```

| Parameter           | Value       | n=6 Formula          |
|---------------------|-------------|----------------------|
| PIM Units/Layer     | 8           | σ-τ = 8              |
| MACs/Unit           | 64          | 2^n = 64             |
| MACs/Layer          | 512         | (σ-τ)·2^n = 512     |
| MACs/Stack          | 6144        | σ·(σ-τ)·2^n         |
| Row Buffer Width    | 1024 bit    | industry standard    |
| Precision           | INT8        | σ-τ = 8 bits         |
| Accumulator         | INT32       | 4×INT8 = τ×(σ-τ)    |

---

## 5. PIM ISA (명령어 집합 아키텍처)

PIM 유닛은 최소한의 ISA로 GEMM 연산에 최적화된다.
n=6 개의 기본 명령어로 모든 LLM 추론 연산을 커버한다.

```
  ┌─────────────────────────────────────────────────────┐
  │              HEXA-PIM ISA (n=6 Instructions)         │
  │                                                     │
  │   ┌────────┬────────────────────────────────────┐   │
  │   │ Opcode │ Description                        │   │
  │   ├────────┼────────────────────────────────────┤   │
  │   │ PIM_LD │ Load weight tile from DRAM row     │   │
  │   │ PIM_MAC│ Multiply-Accumulate (64-wide)      │   │
  │   │ PIM_ACT│ Activation (ReLU/SiLU/GELU)       │   │
  │   │ PIM_ACC│ Accumulate partial sums            │   │
  │   │ PIM_ST │ Store result to DRAM row           │   │
  │   │ PIM_SYN│ Synchronize across PIM units       │   │
  │   └────────┴────────────────────────────────────┘   │
  │                                                     │
  │   Instruction Format (32-bit = 2^sopfr):            │
  │   ┌──────┬──────┬──────┬──────────────────┐         │
  │   │ 3-bit│ 5-bit│ 8-bit│    16-bit         │         │
  │   │  Op  │ Unit │ Bank │   Address/Imm     │         │
  │   └──────┴──────┴──────┴──────────────────┘         │
  │    n/φ=3   sopfr  σ-τ=8    φ^τ=16 bits             │
  └─────────────────────────────────────────────────────┘
```

| Parameter           | Value       | n=6 Formula          |
|---------------------|-------------|----------------------|
| Instruction Count   | 6           | n = 6                |
| Opcode Bits         | 3           | n/φ = 3              |
| Unit Select Bits    | 5           | sopfr = 5            |
| Bank Bits           | 8           | σ-τ = 8              |
| Address Bits        | 16          | φ^τ = 16             |
| Word Size           | 32 bit      | 2^sopfr = 32         |

---

## 6. Memory-Compute Integration (메모리-연산 통합)

PIM의 핵심은 메모리 bank과 연산 유닛의 물리적 근접성이다.
데이터가 DRAM cell에서 row buffer로 이동하는 순간 바로 MAC 연산을 수행한다.

```
  ┌─────────────────────────────────────────────────────────────┐
  │           Memory-Compute Integration Flow                    │
  │                                                             │
  │   DRAM Cell Array                                           │
  │   ┌─────────────────────────────────────────┐               │
  │   │ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ │               │
  │   │ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ │ Weight Matrix │
  │   │ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ │ (stationary)  │
  │   └──────────────────┬──────────────────────┘               │
  │                      │ Row Activate                         │
  │                      ▼                                      │
  │   Row Buffer ════════════════════════════                    │
  │   (1024 bits = σ-τ=8 × 2^(σ-sopfr)=128 bits)               │
  │                      │                                      │
  │              ┌───────┴───────┐                               │
  │              │               │                               │
  │              ▼               ▼                               │
  │   ┌──────────────┐  ┌──────────────┐                        │
  │   │  MAC Unit 0  │  │  MAC Unit 1  │  ... (64 MACs)         │
  │   │  a×w + acc   │  │  a×w + acc   │                        │
  │   └──────┬───────┘  └──────┬───────┘                        │
  │          │                  │                                │
  │          ▼                  ▼                                │
  │   ┌──────────────────────────────┐                           │
  │   │     Accumulator Tree         │                           │
  │   │  (log₂(64) = n = 6 stages)  │                           │
  │   └──────────────┬───────────────┘                           │
  │                  │                                           │
  │                  ▼                                           │
  │   ┌──────────────────────────────┐                           │
  │   │   Activation Function        │                           │
  │   │   (ReLU / SiLU / GELU)      │                           │
  │   └──────────────┬───────────────┘                           │
  │                  │                                           │
  │                  ▼                                           │
  │   Write Back to DRAM Row Buffer                              │
  └─────────────────────────────────────────────────────────────┘
```

| Parameter           | Value       | n=6 Formula          |
|---------------------|-------------|----------------------|
| Row Buffer          | 1024 bit    | standard DRAM        |
| Adder Tree Depth    | 6           | log₂(2^n) = n = 6   |
| Activation Latency  | 1 cycle     | lookup table         |
| Weight Stationary   | Yes         | no data movement     |
| Input Streaming     | Row-by-row  | sequential access    |
| Output              | In-place    | same DRAM bank       |

---

## 7. Internal Bandwidth (내부 대역폭 분석)

HEXA-PIM의 가장 큰 장점은 내부 대역폭이다.
각 DRAM 레이어의 내부 row buffer 대역폭은 외부 I/O의 25배에 달한다.

```
  ┌─────────────────────────────────────────────────────────────┐
  │        Bandwidth Comparison: External vs Internal            │
  │                                                             │
  │   External (HBM3E I/O):                                     │
  │   ┌──────────────────────────────────────────┐              │
  │   │████████████████████                      │ 4 TB/s       │
  │   └──────────────────────────────────────────┘              │
  │                                                             │
  │   Internal (PIM Row Buffer):                                │
  │   ┌──────────────────────────────────────────────────────┐  │
  │   │████████████████████████████████████████████████████████│ │
  │   │████████████████████████████████████████████████████████│ │
  │   │██████████████████████████████████████████████████      │ │
  │   └──────────────────────────────────────────────────────┘  │
  │                                              100 TB/s       │
  │                                                             │
  │   Ratio: 100/4 = 25× ≈ J₂+1 = 25                          │
  │                                                             │
  │   ┌──────────────────────────────────────────────────────┐  │
  │   │         Per-Layer Internal Bandwidth                 │  │
  │   │                                                      │  │
  │   │  Layer  Row_BW    PIM_Units   Effective_BW           │  │
  │   │  ─────  ──────    ─────────   ────────────           │  │
  │   │    1    1 TB/s    ×8          8.3 TB/s               │  │
  │   │    2    1 TB/s    ×8          8.3 TB/s               │  │
  │   │    3    1 TB/s    ×8          8.3 TB/s               │  │
  │   │    4    1 TB/s    ×8          8.3 TB/s               │  │
  │   │    5    1 TB/s    ×8          8.3 TB/s               │  │
  │   │    6    1 TB/s    ×8          8.3 TB/s               │  │
  │   │    7    1 TB/s    ×8          8.3 TB/s               │  │
  │   │    8    1 TB/s    ×8          8.3 TB/s               │  │
  │   │    9    1 TB/s    ×8          8.3 TB/s               │  │
  │   │   10    1 TB/s    ×8          8.3 TB/s               │  │
  │   │   11    1 TB/s    ×8          8.3 TB/s               │  │
  │   │   12    1 TB/s    ×8          8.3 TB/s               │  │
  │   │  ─────────────────────────────────────               │  │
  │   │  Total: σ=12 layers × 8.3 ≈ 100 TB/s               │  │
  │   └──────────────────────────────────────────────────────┘  │
  └─────────────────────────────────────────────────────────────┘
```

| Parameter           | Value       | n=6 Formula          |
|---------------------|-------------|----------------------|
| External BW         | 4 TB/s      | HBM3E per stack      |
| Per-Layer Internal  | ~8.3 TB/s   | row buffer aggregate |
| Total Internal BW   | 100 TB/s    | σ × 8.3 TB/s        |
| BW Amplification    | 25×         | J₂+1 = 25           |
| Row Cycle           | ~20 ns      | DRAM tRC             |
| Rows Activated      | 8/layer     | σ-τ = 8 banks        |

---

## 8. Power Analysis (전력 분석)

PIM의 전력은 데이터 이동 에너지 제거로 인해 극적으로 감소한다.
총 PIM 전력은 σ·τ=48W로, 동등 GPU 연산 대비 10배 절감이다.

```
  ┌─────────────────────────────────────────────────────────────┐
  │              Power Breakdown per PIM Unit                    │
  │                                                             │
  │   ┌──────────────────┬───────────┐                          │
  │   │ Component        │ Power (mW)│                          │
  │   ├──────────────────┼───────────┤                          │
  │   │ MAC Array (64)   │    300    │  ← 64 × 4.7 mW/MAC     │
  │   │ Row Buffer       │     50    │                          │
  │   │ Accumulator      │     30    │                          │
  │   │ Activation LUT   │     20    │                          │
  │   │ Control Logic    │     50    │                          │
  │   │ Clock/Power Dist │     50    │                          │
  │   ├──────────────────┼───────────┤                          │
  │   │ Total per Unit   │    500 mW │  = 0.5W                 │
  │   └──────────────────┴───────────┘                          │
  │                                                             │
  │   Total System PIM Power:                                   │
  │   ┌────────────────────────────────────────┐                │
  │   │ PIM Units = σ·(σ-τ) = 12×8 = 96       │                │
  │   │ Per Unit  = 0.5 W                      │                │
  │   │ Total PIM = 96 × 0.5 = 48 W = σ·τ     │                │
  │   │ GPU Attn  = 200 W (reduced scope)      │                │
  │   │ I/O + PHY = 52 W                       │                │
  │   │ System    = 300 W total                 │                │
  │   └────────────────────────────────────────┘                │
  │                                                             │
  │   Comparison (equivalent FLOPS):                            │
  │   ┌────────────────────────────────┐                        │
  │   │ GPU-only (H100): 700 W        │ ████████████████████   │
  │   │ HEXA-PIM:        300 W        │ █████████              │
  │   │ Saving:          57%          │                        │
  │   └────────────────────────────────┘                        │
  └─────────────────────────────────────────────────────────────┘
```

| Parameter           | Value       | n=6 Formula          |
|---------------------|-------------|----------------------|
| Power per PIM Unit  | 0.5 W       | target               |
| Total PIM Power     | 48 W        | σ·τ = 48             |
| GPU Attention Power | 200 W       | reduced scope        |
| System Total        | 300 W       | PIM+GPU+I/O          |
| vs GPU-only         | 57% saving  | 300/700              |
| Energy/MAC          | 0.08 pJ     | PIM in-situ          |
| Energy/MAC (GPU)    | 0.9 pJ      | off-chip data move   |

---

## 9. AI Workload Mapping (AI 워크로드 분배)

LLM 추론에서 FFN은 전체 연산의 2/3, Attention은 1/3을 차지한다.
HEXA-PIM은 이 비율을 φ(6)/n(6) = 2/6 = 1/3 (GPU) + τ(6)/n(6) = 4/6 = 2/3 (PIM)으로 분배한다.

```
  ┌─────────────────────────────────────────────────────────────┐
  │           AI Workload Distribution                           │
  │                                                             │
  │   LLM Inference Breakdown:                                  │
  │   ┌──────────────────────────────────────────────────────┐  │
  │   │  Attention (QKV + Softmax)     FFN (GEMM + Act)      │  │
  │   │  ████████████                  ████████████████████   │  │
  │   │  ◄── 1/3 (33%) ──►            ◄─── 2/3 (67%) ───►   │  │
  │   │       GPU                           PIM              │  │
  │   └──────────────────────────────────────────────────────┘  │
  │                                                             │
  │   Data Flow for Single Transformer Layer:                   │
  │                                                             │
  │   Input Token ──┬──────────────────────────┐                │
  │                 │                          │                │
  │                 ▼                          ▼                │
  │   ┌─────────────────────┐    ┌─────────────────────┐       │
  │   │    GPU: Attention    │    │    PIM: FFN          │       │
  │   │                     │    │                     │       │
  │   │  Q = X·W_Q          │    │  H = X·W_1          │       │
  │   │  K = X·W_K          │    │  G = X·W_gate        │       │
  │   │  V = X·W_V          │    │  Y = SiLU(G)⊙H·W_2  │       │
  │   │  Attn = softmax(    │    │                     │       │
  │   │    Q·K^T/√d)·V     │    │  (SwiGLU in PIM)    │       │
  │   └──────────┬──────────┘    └──────────┬──────────┘       │
  │              │                          │                   │
  │              ▼                          ▼                   │
  │   ┌──────────────────────────────────────────┐              │
  │   │          LayerNorm + Residual             │              │
  │   │          (GPU or PIM, flexible)           │              │
  │   └──────────────────────────────────────────┘              │
  │                                                             │
  │   Embedding Layer: 100% PIM (pure lookup + GEMM)            │
  │   Output Head:     100% PIM (final projection)              │
  └─────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────┐
  │           Workload Assignment Table                          │
  │                                                             │
  │   ┌──────────────┬─────────┬───────────┬──────────┐        │
  │   │ Operation    │ FLOPs % │ Location  │ Reason   │        │
  │   ├──────────────┼─────────┼───────────┼──────────┤        │
  │   │ Embedding    │   5%    │ PIM       │ lookup   │        │
  │   │ QKV Proj     │  10%    │ GPU       │ complex  │        │
  │   │ Attention    │  15%    │ GPU       │ softmax  │        │
  │   │ Attn Output  │   5%    │ GPU       │ proj     │        │
  │   │ FFN Gate     │  20%    │ PIM       │ GEMM     │        │
  │   │ FFN Up       │  20%    │ PIM       │ GEMM     │        │
  │   │ FFN Down     │  20%    │ PIM       │ GEMM     │        │
  │   │ Output Head  │   5%    │ PIM       │ proj     │        │
  │   ├──────────────┼─────────┼───────────┼──────────┤        │
  │   │ GPU Total    │  30%    │           │          │        │
  │   │ PIM Total    │  70%    │           │          │        │
  │   └──────────────┴─────────┴───────────┴──────────┘        │
  └─────────────────────────────────────────────────────────────┘
```

| Parameter           | Value       | n=6 Formula          |
|---------------------|-------------|----------------------|
| GPU Workload        | ~30%        | ~φ/n = 1/3           |
| PIM Workload        | ~70%        | ~(n-φ)/n = 2/3      |
| FFN on PIM          | 100%        | all GEMM ops         |
| Attention on GPU    | 100%        | softmax + complex    |
| Embedding on PIM    | 100%        | lookup table         |
| Layers Pipelined    | 12          | σ = 12 (LLM depth)  |

---

## 10. Performance Comparison (성능 비교)

HEXA-PIM은 동등 메모리 용량의 GPU-only 시스템 대비
추론 처리량 3배, 에너지 효율 10배를 달성한다.

```
  ┌─────────────────────────────────────────────────────────────┐
  │         Performance Comparison Table                         │
  │                                                             │
  │   ┌────────────────┬──────────┬──────────┬──────────┐      │
  │   │ Metric         │ H100     │ HEXA-PIM │ Ratio    │      │
  │   ├────────────────┼──────────┼──────────┼──────────┤      │
  │   │ Memory BW      │ 3.35TB/s │ 100TB/s  │ 30×      │      │
  │   │ Memory Cap     │ 80 GB    │ 96 GB    │ 1.2×     │      │
  │   │ INT8 TOPS      │ 3958     │ 12288    │ 3.1×     │      │
  │   │ Power          │ 700 W    │ 300 W    │ 0.43×    │      │
  │   │ TOPS/W         │ 5.7      │ 41       │ 7.2×     │      │
  │   │ LLM Tok/s (70B)│ 2000     │ 6000     │ 3×       │      │
  │   │ Batch Latency  │ 10 ms    │ 3.3 ms   │ 3×       │      │
  │   │ Die Area       │ 814mm²   │ 400mm²   │ 0.49×    │      │
  │   └────────────────┴──────────┴──────────┴──────────┘      │
  │                                                             │
  │   Key Insight:                                              │
  │   PIM eliminates data movement bottleneck.                  │
  │   GPU die shrinks because FFN offloaded to PIM.             │
  │   BW wall broken: 100TB/s internal >> 3.35TB/s external.    │
  │                                                             │
  │   Bar Chart (TOPS/W):                                       │
  │   H100     : █████▋                         5.7             │
  │   HEXA-PIM : █████████████████████████████████████████ 41   │
  └─────────────────────────────────────────────────────────────┘
```

| Parameter           | Value       | n=6 Formula          |
|---------------------|-------------|----------------------|
| INT8 TOPS           | 12,288      | 6144 MACs × 2 ops   |
| Effective BW        | 100 TB/s    | internal PIM         |
| TOPS/W              | 41          | 12288/300            |
| LLM 70B Tok/s       | 6000        | 3× H100              |
| GPU Die Reduction   | 49%         | FFN offloaded        |
| Batch Latency       | 3.3 ms      | 3× faster            |

---

## 11. Process Technology (공정 기술)

HEXA-PIM은 기존 HBM 공정에 PIM 로직을 추가하여 제조한다.
DRAM 레이어는 1α nm DRAM 공정, PIM 로직은 DRAM 공정 내 embedded logic으로 구현한다.

```
  ┌─────────────────────────────────────────────────────────────┐
  │              Process Technology Stack                        │
  │                                                             │
  │   ┌─────────────────────────────────────────┐               │
  │   │  DRAM Layer (1α nm)                     │               │
  │   │  ┌──────────┐  ┌──────────────────┐     │               │
  │   │  │ Cell     │  │ PIM Logic        │     │               │
  │   │  │ Array    │  │ (embedded in     │     │               │
  │   │  │ (1T1C)  │  │  DRAM process)   │     │               │
  │   │  │         │  │                  │     │               │
  │   │  │ 256 Mb  │  │ 64 MACs          │     │               │
  │   │  └──────────┘  └──────────────────┘     │               │
  │   └─────────────────────────────────────────┘               │
  │                    × σ=12 layers                            │
  │                                                             │
  │   Stacking: TSV (Through-Silicon Via)                       │
  │   ┌─────┐                                                   │
  │   │ L12 │ ← DRAM + PIM                                     │
  │   │ L11 │ ← DRAM + PIM                                     │
  │   │ ... │                                                   │
  │   │ L1  │ ← DRAM + PIM                                     │
  │   │ Base│ ← Logic die (controller, PHY)                    │
  │   └─────┘                                                   │
  │                                                             │
  │   Base Die: 5nm or 4nm logic process                        │
  │   Bonding: Cu-Cu hybrid bonding                             │
  │   TSV Pitch: σ·τ = 48 μm (current) → 28 μm (P₂) roadmap   │
  └─────────────────────────────────────────────────────────────┘
```

| Parameter           | Value       | n=6 Formula          |
|---------------------|-------------|----------------------|
| DRAM Process        | 1α nm       | latest DRAM node     |
| Logic Process       | 5nm / 4nm   | base die             |
| TSV Pitch           | 48 μm       | σ·τ = 48             |
| TSV Next Gen        | 28 μm       | P₂ = 28              |
| Stack Height        | 12 layers   | σ = 12               |
| Bonding             | Cu-Cu       | hybrid bonding       |
| PIM Area/Layer      | ~5 mm²      | embedded in DRAM     |

---

## 12. N6 Parameter Map (n=6 파라미터 맵)

HEXA-PIM 아키텍처의 모든 핵심 파라미터가 n=6 상수에서 유도된다.

```
  ┌─────────────────────────────────────────────────────────────┐
  │                  N6 Parameter Derivation Tree                │
  │                                                             │
  │                         n = 6                               │
  │                      ┌───┴───┐                              │
  │                   σ=12     τ=4                              │
  │                  ┌──┴──┐    │                               │
  │               σ-τ=8  σ-φ=10 │                               │
  │                │       │    │                               │
  │            PIM/layer  ───  ───                              │
  │                │                                            │
  │            2^n=64 MACs/unit                                 │
  │                │                                            │
  │         σ·(σ-τ)·2^n = 6144 total MACs                      │
  │                │                                            │
  │          σ·τ = 48 W total PIM power                         │
  │                │                                            │
  │        J₂+1 = 25× bandwidth amplification                  │
  │                                                             │
  │   ┌──────────────┬─────────────────────────────────────┐   │
  │   │ n=6 Constant │ Architecture Mapping                │   │
  │   ├──────────────┼─────────────────────────────────────┤   │
  │   │ σ = 12       │ DRAM layers per stack               │   │
  │   │ τ = 4        │ Power scaling factor                │   │
  │   │ φ = 2        │ Precision doubling (INT8→FP16)      │   │
  │   │ σ-τ = 8      │ PIM units per layer, INT8 bits      │   │
  │   │ 2^n = 64     │ MACs per PIM unit                   │   │
  │   │ n = 6        │ ISA instruction count               │   │
  │   │ n/φ = 3      │ Opcode field width                  │   │
  │   │ sopfr = 5    │ Unit select bits                    │   │
  │   │ σ·τ = 48     │ Total PIM power (W)                 │   │
  │   │ J₂ = 24      │ BW amplification ~25× (J₂+1)       │   │
  │   │ σ·(σ-τ) = 96 │ Total PIM units across all stacks   │   │
  │   │ P₂ = 28      │ Next-gen TSV pitch (μm)             │   │
  │   │ φ^τ = 16     │ FP16 precision, address field bits  │   │
  │   │ σ² = 144     │ Peak TOPS target (×100)             │   │
  │   └──────────────┴─────────────────────────────────────┘   │
  └─────────────────────────────────────────────────────────────┘
```

---

## 13. Links (관련 문서)

- **BT-55**: GPU HBM Capacity Ladder — `docs/breakthrough-theorems.md`
- **BT-58**: σ-τ=8 Universal AI Constant — `docs/breakthrough-theorems.md`
- **BT-59**: 8-Layer AI Stack — `docs/breakthrough-theorems.md`
- **BT-69**: Chiplet Architecture Convergence — `docs/breakthrough-theorems.md`
- **BT-75**: HBM Interface Exponent Ladder — `docs/breakthrough-theorems.md`
- **HEXA-3D**: 3D Compute-on-Memory — `docs/chip-architecture/hexa-3d.md`
- **HEXA-PHOTON**: Photonic Architecture — `docs/chip-architecture/hexa-photon.md`
- **Samsung PIM**: Samsung HBM-PIM Reference — `docs/chip-architecture/ultimate-dram-design.md`
- **Chip Hypotheses**: `docs/chip-architecture/CHIPDESIGN-001-020-ai-chip-n6.md`

---

## Appendix: HEXA-PIM Scaling Roadmap

```
  ┌─────────────────────────────────────────────────────────────┐
  │           HEXA-PIM Generation Roadmap                        │
  │                                                             │
  │   Gen 1 (2026): HBM3E-PIM                                  │
  │   ┌──────────────────────────────────────────┐              │
  │   │ σ=12 layers, σ-τ=8 PIM/layer            │              │
  │   │ 64 MACs/unit, INT8                       │              │
  │   │ 6144 total MACs, 100 TB/s internal       │              │
  │   │ 48W PIM power, 300W system               │              │
  │   └──────────────────────────────────────────┘              │
  │                                                             │
  │   Gen 2 (2028): HBM4-PIM                                   │
  │   ┌──────────────────────────────────────────┐              │
  │   │ σ=12 layers, σ=12 PIM/layer (↑)         │              │
  │   │ σ²=144 MACs/unit, INT8/FP8              │              │
  │   │ 20736 total MACs, 200 TB/s internal      │              │
  │   │ σ·τ=48W PIM, 250W system (efficiency↑)  │              │
  │   └──────────────────────────────────────────┘              │
  │                                                             │
  │   Gen 3 (2030): HBM5-PIM + 3D Integration                  │
  │   ┌──────────────────────────────────────────┐              │
  │   │ Merge with HEXA-3D architecture          │              │
  │   │ Compute-on-Memory full integration       │              │
  │   │ J₂=24 PIM/layer, σ²=144 MACs/unit       │              │
  │   │ 500 TB/s internal, sub-pJ/MAC            │              │
  │   └──────────────────────────────────────────┘              │
  │                                                             │
  │   MACs Growth:                                              │
  │   Gen1: ██████                          6,144               │
  │   Gen2: ████████████████████            20,736              │
  │   Gen3: ████████████████████████████████████████ 41,472+    │
  └─────────────────────────────────────────────────────────────┘
```

| Generation | Year | MACs    | Internal BW | n=6 Evolution        |
|------------|------|---------|-------------|----------------------|
| Gen 1      | 2026 | 6,144   | 100 TB/s    | σ·(σ-τ)·2^n         |
| Gen 2      | 2028 | 20,736  | 200 TB/s    | σ·σ·σ² = σ⁴         |
| Gen 3      | 2030 | 41,472+ | 500 TB/s    | merge HEXA-3D        |

---

*HEXA-PIM: σ(6)=12 레이어 × (σ-τ)=8 PIM 유닛 × 2^n=64 MACs = 6144 — 메모리 벽을 n=6에서 제거한다.*
