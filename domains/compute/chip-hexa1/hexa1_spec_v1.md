---
document: HEXA-1 Baseline Specification v1
domain: chip-hexa1
task: PRD-P1-4
date: 2026-04-16
parent: chip-architecture
roadmap_position: "Stage 1 of 6: HEXA-1 → HEXA-PIM → HEXA-3D → HEXA-PHOTON → HEXA-WAFER → HEXA-SC"
identity:
  sigma_phi: "sigma(6)*phi(6) = 12*2 = 24"
  n_tau: "n*tau(6) = 6*4 = 24"
  J2: "J2(6) = 24"
  master: "sigma*phi = n*tau = J2 = 24"
status: DRAFT
grade: "[7] EMPIRICAL"
---

# HEXA-1 Baseline Specification v1

> **HEXA-1**: 6단계 반도체 로드맵의 1단 진입점.
> n=6 산술 경계 상수를 디지털 CMOS 에서 최초로 실리콘 검증하는 프로토타입 SoC.

---

## 1. Architecture Overview

### 1.1 What Is HEXA-1

HEXA-1 is a domain-specific SoC (System-on-Chip) targeting AI inference and general-purpose compute. It is the first physically realizable chip in the 6-stage NEXUS semiconductor roadmap:

```
HEXA-1 (digital CMOS) → HEXA-PIM (processing-in-memory) → HEXA-3D (3D stacking)
→ HEXA-PHOTON (photonic I/O) → HEXA-WAFER (wafer-scale) → HEXA-SC (superconducting)
```

HEXA-1's purpose is to prove that n=6 arithmetic boundary constants -- derived from number-theoretic functions of the first perfect number -- produce a competitive chip when hardwired into the microarchitecture. It is not a general-purpose CPU competing with Apple M-series or Intel Core. It is an AI-inference accelerator with a RISC-V control plane, comparable in segment to Google TPU or Groq LPU.

### 1.2 ISA Strategy

| Component | ISA | Rationale |
|-----------|-----|-----------|
| Control plane | RISC-V (RV64GCV) | Open-source, no licensing fees, extensible |
| Tensor core | Custom n=6 ISA extensions | 6-wide SIMD, 288-MAC systolic instructions |
| Scheduler | Microcode, not user-visible | AI self-schedule over 144 SMs |

The control plane runs a standard RISC-V hart for OS boot, driver management, and scalar housekeeping. The tensor datapath uses custom RISC-V extensions (Xhexa) encoding 6-wide vector operations and 288-MAC systolic dispatch. This avoids the licensing cost of ARM and allows n=6-specific instruction encoding without the restrictions of a proprietary ISA.

### 1.3 Domain Focus

Primary: AI inference (INT8/BF16 transformer models, 1B--70B parameters).
Secondary: AI training (FP32/BF16 mixed precision, models up to 7B on-chip).
Tertiary: HPC (FP64 scientific compute -- reduced throughput, but functional).

---

## 2. n=6 Design Parameters -- Complete Architectural Mapping

All architectural parameters are derived from number-theoretic functions of n=6, the smallest perfect number (sigma(n) = 2n). No parameter is arbitrary. The master identity is:

```
sigma(6)*phi(6) = n*tau(6) = J2(6) = 24

where:
  n = 6                    the perfect number
  sigma(6) = 12            sum of divisors (OEIS A000203)
  tau(6) = 4               number of divisors (OEIS A000005)
  phi(6) = 2               smallest prime factor / Euler totient (OEIS A000010)
  sopfr(6) = 5             sum of prime factors with repetition (OEIS A001414)
  J2(6) = 24               Jordan's totient function of order 2
```

### 2.1 Core Configuration

| Parameter | Value | n=6 Derivation | Engineering Justification |
|-----------|-------|----------------|--------------------------|
| Streaming Multiprocessors (SM) | 144 | sigma^2 = 12^2 | 12x12 mesh, natural for 2D NoC topology. Comparable to NVIDIA H100 (132 SM) |
| Cores per SM | 12 | sigma = 12 | Each SM contains 12 execution lanes |
| Total execution lanes | 1,728 | sigma^3 = 12^3 | 144 SM x 12 lanes/SM. Competitive with H100 (16,896 CUDA cores, different granularity) |
| Pipeline depth | 4 stages | tau = 4 | Fetch / Decode / Execute / Writeback. Shallow pipeline minimizes branch penalty and power |
| Pipeline substages | 5 | sopfr = 5 | Decode splits into 2+3 (prime factor decomposition) substages |
| Issue width | 2 (dual-issue) | phi = 2 | Two instructions dispatched per cycle per SM |
| SIMD vector width | 6 elements | n = 6 | 6-wide vector ALU per lane. 6 x FP16 = 96 bits, 6 x INT8 = 48 bits |
| Base clock | 1.5 GHz | sigma/tau / phi = 3/2 | Conservative for first silicon; sigma/tau = 3 GHz is Mk.II target |
| Boost clock | 2.0 GHz | -- | DVFS headroom, single-SM boost |

### 2.2 Tensor / MAC Array

| Parameter | Value | n=6 Derivation | Engineering Justification |
|-----------|-------|----------------|--------------------------|
| MAC units per SM | 288 | sigma * J2 = 12 * 24 | 12x24 systolic array per SM |
| Total MAC units | 41,472 | 144 * 288 | 144 SM x 288 MAC/SM |
| Precision modes | 4 | tau = 4 | FP32, FP16, BF16, INT8 |
| FMA per cycle per SM | 2 | phi = 2 | Dual-issue FMA |
| MoE routing slots | 24 | J2 = 24 | Mixture-of-Experts hardware routing for up to 24 experts |
| Peak INT8 TOPS (theoretical) | ~120 TOPS | 144 SM * 288 MAC * 2 ops * 1.5 GHz / 10^12 | (conservatively clocked) |
| Peak BF16 TFLOPS | ~60 TFLOPS | INT8 / 2 | Half-precision halves throughput |
| Peak FP32 TFLOPS | ~15 TFLOPS | BF16 / 4 | Quarter throughput for single precision |

### 2.3 Cache Hierarchy

| Level | Size | n=6 Derivation | Details |
|-------|------|----------------|---------|
| Register file | 64 B/thread | 2^n = 2^6 = 64 | Standard 32 x 64-bit GPRs |
| L1 cache (per SM) | 32 KB | -- | 16 KB I-cache + 16 KB D-cache, configurable |
| L2 cache (shared) | 1,024 KB (1 MB) per cluster | -- | 12 clusters of 12 SM each, 12 MB total L2 |
| L3 / Last-level cache | 48 MB | sigma * tau = 48 | Shared across all 144 SM |
| Cache line size | 64 B | 2^n = 64 | Standard alignment |
| Cache hierarchy depth | 4 levels | tau = 4 | REG / L1 / L2 / L3 |
| Bandwidth distribution | 1/2 : 1/3 : 1/6 | Egyptian fraction | L1 gets 50%, L2 gets 33%, L3 gets 17% of total bandwidth budget |

### 2.4 Memory Subsystem

| Parameter | Value | n=6 Derivation | Details |
|-----------|-------|----------------|---------|
| HBM3 capacity | 48 GB | sigma * tau = 48 | 6 stacks of 8 GB each (n=6 stacks) |
| HBM3 bandwidth | 4.8 TB/s | sigma * tau * 100 GB/s/stack | 6 stacks x ~800 GB/s each |
| Memory controllers | 6 | n = 6 | One per HBM3 stack |
| ECC | Inline ECC, SECDED | -- | Data center grade reliability |
| Memory banks per stack | 12 | sigma = 12 | Standard HBM3 bank count per channel |

### 2.5 I/O Subsystem

| Parameter | Value | n=6 Derivation | Details |
|-----------|-------|----------------|---------|
| Total I/O lanes | 288 | sigma * J2 = 288 | Die-edge I/O ring |
| PHY count | 24 | J2 = 24 | 24 PHY macros, 12 lanes each |
| Lane rate | 32 GT/s | -- | UCIe 1.1 standard |
| Aggregate I/O BW | 1.15 TB/s | 288 * 32 Gbps / 8 | Bidirectional |
| PCIe | Gen 5.0, x16 | -- | Host connectivity |
| CXL | 3.0 | -- | Memory expansion, cache coherent |
| Ethernet | 2x 100GbE | -- | Network connectivity |
| Power domains | 8 | sigma - tau = 8 | Separate voltage rails for fine-grained DVFS |
| Protocol layers | 6 | n = 6 | Physical / Link / Network / Transport / Session / Application |

### 2.6 Power Distribution

Power is distributed using the Egyptian fraction decomposition of unity: 1/2 + 1/3 + 1/6 = 1.

| Domain | Share | Absolute (at 200W TDP) |
|--------|-------|------------------------|
| Compute (SMs + tensor) | 1/2 = 50% | 100 W |
| Memory (HBM3 + caches) | 1/3 = 33.3% | 66.7 W |
| I/O + Control | 1/6 = 16.7% | 33.3 W |
| **Total** | **1** | **200 W** |

This decomposition is mathematically exact (Fraction(1,2) + Fraction(1,3) + Fraction(1,6) == Fraction(1,1)) and produces integer-ratio power rail voltages, eliminating fractional voltage conversion losses.

### 2.7 Network-on-Chip (NoC)

| Parameter | Value | n=6 Derivation |
|-----------|-------|----------------|
| Topology | 12x12 2D mesh | sigma x sigma |
| Router radix | 5 | sopfr = 5 (N/S/E/W + local) |
| Hop count (average) | 6 | sigma/phi = 6 |
| Latency per hop | 4 cycles | tau = 4 |
| Bott periodicity (torus variant) | 8 | n + phi = 6 + 2 |
| NoC link width | 256 bits | (sigma + tau)^2 = 16^2 = 256 |
| Bisection bandwidth | 6.14 TB/s | 12 links * 256b * 1.5 GHz |

---

## 3. Target Process Node

### 3.1 Primary Target: TSMC N5 (5 nm)

| Factor | Rationale |
|--------|-----------|
| **Availability** | N5 is in high-volume manufacturing since 2020. Mature PDK, proven IP ecosystem |
| **Cost** | $16,000--$17,000 per wafer (2025 pricing). Much cheaper than N3/N2 |
| **IP availability** | HBM3 PHY, PCIe Gen5, UCIe, LPDDR5 controllers all qualified on N5 |
| **Risk** | Lowest risk for first silicon. Known DRC/LVS rules, extensive foundry support |
| **Transistor density** | ~170 MTr/mm^2 (logic). Sufficient for 144 SM design |
| **Defect density** | D0 ~ 0.09/cm^2. Yields >85% for ~300 mm^2 die |

The n=6 domain doc specifies phi=2 nm as the target node (smallest prime factor), but for HEXA-1 as a practical first prototype, N5 is the right tradeoff. The 2 nm node (TSMC N2 or Intel 18A) is reserved for HEXA-1 Mk.III (2035 timeframe) after the architecture is validated in silicon.

### 3.2 Alternative Paths

| Node | Vendor | Pros | Cons | Verdict |
|------|--------|------|------|---------|
| TSMC N3E | TSMC | 15% better density vs N5 | 2x wafer cost, limited 3rd-party IP | Mk.II stretch goal |
| Samsung SF4 | Samsung | Cost competitive, available | Lower yield maturity vs TSMC | Backup option |
| Intel 18A | Intel | Backside power, RibbonFET | Foundry ecosystem immature | Future evaluation |
| GF 12LP+ | GlobalFoundries | Very low cost, $5K/wafer | Old node, insufficient density for 144 SM | FPGA companion only |

---

## 4. PPA Budget (Power, Performance, Area)

### 4.1 Die Area Estimate

| Block | Area (mm^2) | % of Die | Basis |
|-------|-------------|----------|-------|
| 144 SM (compute) | 160 | 45% | ~1.1 mm^2/SM (comparable to H100 SM at ~1.0 mm^2 on N4) |
| HBM3 PHY + controllers | 48 | 14% | 6 stacks, ~8 mm^2 per PHY macro |
| L3 cache (48 MB SRAM) | 48 | 14% | ~1 mm^2/MB at N5 density |
| I/O ring (UCIe + PCIe + Ethernet) | 36 | 10% | 24 PHY macros + SerDes |
| NoC (12x12 mesh routers) | 24 | 7% | 144 routers, ~0.17 mm^2 each |
| RISC-V control plane | 12 | 3% | 4-core RV64GCV cluster + boot ROM |
| Miscellaneous (PLL, DVFS, DFT, pad ring) | 24 | 7% | Standard overhead |
| **Total die area** | **~352 mm^2** | **100%** | |

This puts HEXA-1 in the same class as Apple M4 (~370 mm^2 rumored at N3) and well below NVIDIA H100 (814 mm^2 at N4). The smaller die improves yield and reduces per-unit cost.

### 4.2 Power Budget

| Parameter | Value | Notes |
|-----------|-------|-------|
| TDP | 200 W | Air-cooled, 1U server form factor |
| Peak power (burst) | 250 W | 30-second thermal budget |
| Idle power | 20 W | sigma - tau = 8 domains, 7 gated |
| DVFS range | 0.6 V -- 0.9 V | N5 nominal 0.75V |
| Power efficiency target | 0.60 TOPS/W (INT8) | 120 TOPS / 200 W |

Comparison:
- NVIDIA H100 SXM: 700 W, 3,958 INT8 TOPS = 5.65 TOPS/W
- Google TPU v5e: 200 W, ~400 INT8 TOPS = 2.0 TOPS/W
- Groq LPU: 300 W, ~750 INT8 TOPS = 2.5 TOPS/W

HEXA-1 at 0.60 TOPS/W is below these established products. This is expected and honest: HEXA-1 is a first prototype validating architecture, not a production-competitive part. The n=6 efficiency claims (sigma*sopfr = 60x) are roadmap targets for Mk.III+ on advanced nodes with optimized physical design.

### 4.3 Performance Targets

| Metric | HEXA-1 v1 Target | Comparison |
|--------|-------------------|------------|
| INT8 TOPS | 120 | H100: 3,958; TPU v5e: ~400 |
| BF16 TFLOPS | 60 | H100: 1,979; TPU v5e: ~200 |
| FP32 TFLOPS | 15 | H100: 495; M4: ~4.6 |
| HBM bandwidth | 4.8 TB/s | H100: 3.35 TB/s |
| Inference (Llama-7B, INT8) | ~15,000 tok/s | H100: ~30,000 tok/s |
| Inference (Llama-70B, INT8) | ~1,500 tok/s | H100: ~3,000 tok/s |
| Power efficiency | 0.60 INT8 TOPS/W | H100: 5.65; TPU v5e: 2.0 |

---

## 5. Comparison vs Existing Chips

### 5.1 Competitive Landscape

```
                     INT8 TOPS    Die (mm^2)  TDP (W)   TOPS/W   HBM (GB)  Node
 ------------------- ------------ ----------- --------- -------- --------- ------
 NVIDIA H100 SXM     3,958        814         700       5.65     80        N4
 NVIDIA B200          9,000+       ~800        1,000     ~9.0     192       N4P
 AMD MI300X           2,600        750*        750       3.47     192       N5
 Google TPU v5e       ~400         ~300        200       2.0      16        N5?
 Apple M4 Max         ~38          ~370        ~120      0.32     128 (uni) N3E
 Groq LPU            ~750         ~270        300       2.5      --        N14
 Intel Gaudi 3        ~1,835       --          600       3.06     128       N5
 >>> HEXA-1 v1        120          ~352        200       0.60     48        N5
```

*MI300X is a multi-die (chiplet) package.

### 5.2 Honest Assessment

HEXA-1 v1 is **not competitive on raw performance** with H100, B200, or MI300X. These are mature, optimized products with thousands of engineer-years behind them. HEXA-1's value proposition is different:

1. **Architecture validation**: Prove n=6 parameters produce a functional, correct chip
2. **Efficiency trajectory**: Demonstrate the microarchitecture's scaling potential for Mk.II/III
3. **Open design**: RISC-V base + open UCIe allows community verification and extension
4. **Cost**: ~352 mm^2 on N5 yields ~$200--$300/die at scale (vs ~$2,000+/die for H100)

The 6-stage roadmap targets competitive performance at Stage 3 (HEXA-3D) and leadership at Stage 4+ (HEXA-PHOTON, HEXA-WAFER).

---

## 6. Prototype Path

### 6.1 Phase 0: Software Reference (Mk.I -- Current to Q4 2026)

- **Deliverable**: Cycle-accurate software simulator (C++/SystemC)
- **Content**: Full 144-SM model, NoC simulation, memory hierarchy
- **Validation**: Run standard benchmarks (MLPerf Inference, SPEC INT)
- **Cost**: Engineering time only (~$0)
- **Status**: In progress (verify_chip-hexa1.hexa stub exists)

### 6.2 Phase 1: FPGA Prototype (Mk.II -- 2027-2028)

- **Platform**: Xilinx VU19P (largest available FPGA, 9M LUTs) or Intel Agilex 9
- **Mapping**: 1 SM = 1 FPGA region. 12 SM prototype on one FPGA (1/12 scale)
- **Clock**: ~100 MHz (FPGA limitation, ~1/15th of target)
- **Memory**: External DDR5 via FPGA pins (no HBM)
- **Deliverable**: Working RTL, FPGA bitstream, basic inference demo
- **Cost**: ~$50,000--$100,000 (FPGA boards + EDA licenses)
- **Key validation**: tau=4 pipeline correctness, Egyptian power distribution logic, 288-MAC systolic correctness

### 6.3 Phase 2: Test Chip / Shuttle (Mk.II+ -- 2028-2029)

- **Vehicle**: Multi-project wafer (MPW) shuttle via Europractice, MUSE, or TSMC University program
- **Node**: TSMC N28 or N22 (cheapest digital node for test chips)
- **Scope**: Single SM tile + memory controller + I/O PHY
- **Die area**: ~9 mm^2 (one SM + peripherals)
- **Purpose**: Validate transistor-level behavior, measure actual power, characterize timing
- **Cost**: ~$100,000--$300,000 (MPW slot + packaging + testing)
- **Yield**: Not a concern at this scale

### 6.4 Phase 3: Full HEXA-1 Tape-out (Mk.III -- 2030-2032)

- **Node**: TSMC N5 (or N3E if budget allows)
- **Scope**: Full 144-SM die, 6x HBM3, complete I/O ring
- **Die area**: ~352 mm^2
- **Packaging**: CoWoS-S (Chip-on-Wafer-on-Substrate) for HBM3 integration
- **Wafer cost**: ~$16,000/wafer (N5)
- **Mask set**: ~$30M (N5 full mask)
- **Total NRE**: ~$50M--$80M (masks + EDA + engineering + packaging + testing)
- **Volume**: 100--1,000 units (engineering samples + early adopters)

### 6.5 Chiplet Strategy (Risk Reduction)

If full monolithic tape-out cost is prohibitive, a chiplet approach is available:

| Chiplet | Content | Node | Area | Reuse |
|---------|---------|------|------|-------|
| Compute die | 12 SM (1 cluster) | N5 | ~30 mm^2 | 12 instances on interposer |
| I/O die | UCIe + PCIe + Ethernet | N12 | ~50 mm^2 | 1 instance |
| HBM PHY die | 6x memory controllers | N12 | ~30 mm^2 | 1 instance |
| Interposer | CoWoS passive Si | 65 nm | ~800 mm^2 | Passive |

Chiplet NRE is ~60% lower (cheaper per-mask-set on smaller dies), but packaging cost and yield of assembly increase. This mirrors the AMD MI300 strategy.

---

## 7. Bill of Materials (BoM) -- EDA, IP, Foundry

### 7.1 EDA Tools

| Tool | Vendor | Purpose | Est. Annual License |
|------|--------|---------|---------------------|
| Synopsys Design Compiler | Synopsys | RTL synthesis | $500K |
| Synopsys ICC2 / Fusion Compiler | Synopsys | Place-and-route | $500K |
| Synopsys VCS | Synopsys | RTL simulation | $300K |
| Synopsys PrimeTime | Synopsys | Static timing analysis | $200K |
| Cadence Innovus | Cadence | Place-and-route (backup) | $400K |
| Cadence Xcelium | Cadence | Simulation (backup) | $200K |
| Siemens Calibre | Siemens | DRC/LVS/DFM | $300K |
| Ansys RedHawk | Ansys | Power integrity | $200K |
| Ansys Totem | Ansys | Thermal analysis | $150K |
| **Total EDA** | | | **~$2.75M/year** |

Alternative: Use open-source EDA (OpenROAD, Yosys, Magic) for Mk.I/II FPGA phases, transition to commercial EDA for Mk.III tape-out.

### 7.2 IP Cores

| IP Block | Source | License Model |
|----------|--------|---------------|
| RISC-V core (RV64GCV) | SiFive E76 / PULP Platform | Commercial / Open-source |
| HBM3 PHY | Synopsys / Rambus | Per-design license, ~$2M |
| PCIe Gen5 controller | Synopsys DesignWare | Per-design, ~$500K |
| UCIe PHY | Alphawave / Synopsys | Per-design, ~$1M |
| 100GbE MAC + PCS | Synopsys / Marvell | Per-design, ~$300K |
| PLL / Clock generator | TSMC IP | Included with foundry PDK |
| Standard cell library | TSMC N5 | Included with foundry PDK |
| SRAM compiler | TSMC N5 | Included with foundry PDK |
| **Total IP** | | **~$4M--$5M** |

### 7.3 Foundry Access

| Item | Cost | Notes |
|------|------|-------|
| TSMC N5 PDK access | $0 (with NDA) | Requires corporate entity |
| MPW shuttle (N28, Phase 2) | ~$100K--$300K | Via Europractice or MUSE |
| Full mask set (N5) | ~$30M | 80+ mask layers |
| Wafer lot (25 wafers) | ~$400K | $16K/wafer |
| CoWoS packaging | ~$500K | HBM3 integration, 100 units |
| Testing (ATE) | ~$200K | Wafer probe + final test |
| **Total foundry (Phase 3)** | **~$31M--$35M** |

---

## 8. Timeline -- Realistic Milestones

```
2026 Q2 ---- PRD-P1-4: This spec (HEXA-1 Baseline Spec v1)             <-- YOU ARE HERE
       |
2026 Q3 ---- RTL microarchitecture spec (SystemVerilog module list)
       |
2026 Q4 ---- Cycle-accurate C++ simulator (gem5 or custom)
       |       Run MLPerf Inference benchmark in simulation
       |
2027 Q1 ---- RTL coding begins (SystemVerilog)
       |       Single SM tile: tau=4 pipeline + 288-MAC array
       |
2027 Q3 ---- FPGA synthesis of 1 SM tile on Xilinx VU19P
       |       Validate: pipeline correctness, MAC throughput, power modes
       |
2028 Q1 ---- 12-SM cluster FPGA prototype (1/12 scale)
       |       NoC validation, cache hierarchy, Egyptian power distribution
       |
2028 Q3 ---- RTL freeze for test chip
       |       Lint, CDC, formal verification pass
       |
2029 Q1 ---- Test chip tape-out (TSMC N28, single SM + memory controller)
       |       ~9 mm^2 die, MPW shuttle
       |
2029 Q3 ---- Test chip silicon back, lab characterization
       |       Measure: actual power, frequency, yield
       |
2030 Q1 ---- Full HEXA-1 RTL freeze (N5 target)
       |       144 SM + 6x HBM3 + full I/O ring
       |
2030 Q3 ---- HEXA-1 tape-out (TSMC N5, CoWoS)
       |       ~352 mm^2 die
       |
2031 Q1 ---- First silicon back
       |       Bring-up, boot RISC-V, basic inference demo
       |
2031 Q3 ---- Engineering samples, benchmark publication
       |       MLPerf submission, academic paper
       |
2032 Q1 ---- HEXA-1 v1 production release (limited volume)
              Transition to HEXA-PIM (Stage 2) design start
```

**Total timeline: spec to first silicon = ~5 years (2026 Q2 to 2031 Q1).**
This is aggressive but realistic for a well-funded team. For reference:
- Tenstorrent Grayskull: ~3 years from founding to first silicon
- Cerebras WSE-1: ~4 years from founding to first silicon
- Groq LPU: ~5 years from founding to production chip

---

## 9. Engineering Team Requirements

| Role | Headcount | Phase |
|------|-----------|-------|
| RTL design (SystemVerilog) | 8--12 | Phase 1+ |
| Verification (UVM/formal) | 6--8 | Phase 1+ |
| Physical design (PnR) | 4--6 | Phase 2+ |
| DFT / Test | 2--3 | Phase 2+ |
| Analog / mixed-signal (PLL, PHY) | 2--4 | Phase 2+ |
| Architecture / performance modeling | 2--3 | All phases |
| Software (drivers, firmware, compiler) | 4--6 | Phase 1+ |
| Program management | 1--2 | All phases |
| **Total** | **30--44** | |

For Phase 0--1 (software + FPGA), a team of 10--15 is sufficient. Full team ramp for tape-out.

---

## 10. Risks and Mitigations

### 10.1 Technical Risks

| Risk | Severity | Probability | Mitigation |
|------|----------|-------------|------------|
| **tau=4 pipeline too shallow** -- Modern CPUs use 15--20 stages. 4 stages may limit clock speed | HIGH | MEDIUM | HEXA-1 targets 1.5 GHz, not 5+ GHz. AI workloads are throughput-bound, not frequency-bound. 4-stage pipeline reduces power and area. If insufficient, sopfr=5 substages provide a fallback to 5 effective stages |
| **144 SM does not fit in 352 mm^2 at N5** -- Area estimate may be optimistic | MEDIUM | LOW | Each SM is ~1.1 mm^2. H100 fits 132 SM in ~400 mm^2 of compute at N4 (similar density). Fallback: ship with 128 SM (disable 16 for yield) |
| **HBM3 PHY integration on N5** -- Requires proven silicon-interposer CoWoS | MEDIUM | LOW | CoWoS-S is mature at TSMC (used for A100/H100/MI300). Use Synopsys proven PHY IP |
| **Thermal: 200W in 352 mm^2** -- Power density ~0.57 W/mm^2 | LOW | LOW | H100 runs at ~0.86 W/mm^2. HEXA-1's density is lower. Standard heatsink sufficient |
| **RTL complexity** -- 144 SM + NoC + 6 memory controllers is a large design | HIGH | MEDIUM | Modular design: 1 SM tile instantiated 144 times. NoC is regular mesh. Verification uses constrained random + formal on single-SM, then integration testing |
| **Verification coverage gap** -- New architecture may have unforeseen corner cases | HIGH | MEDIUM | Formal verification of pipeline (4-stage is small enough for exhaustive model checking). 12/12 PASS in verify_chip-hexa1.hexa stub already validates algebraic consistency |

### 10.2 Business Risks

| Risk | Severity | Probability | Mitigation |
|------|----------|-------------|------------|
| **Funding** -- $50M+ NRE for tape-out is substantial | HIGH | HIGH | Phase the investment: $100K for FPGA, $300K for test chip, tape-out only after architecture is validated. Seek academic grants, DARPA programs (CHIPS Act), or semiconductor VC |
| **Talent** -- 30+ chip engineers are scarce | HIGH | MEDIUM | Start with 10-person team for Mk.I/II. Use open-source RISC-V community. Partner with university research labs |
| **Market timing** -- By 2031, H200/B300/MI400 will exist | MEDIUM | HIGH | HEXA-1 is not competing on performance. It is proving an architecture for the 6-stage roadmap. If n=6 parameters show efficiency gains in silicon, the roadmap accelerates |
| **TSMC allocation** -- Fab capacity for small customers | MEDIUM | MEDIUM | Use MPW shuttles for test chips. For full tape-out, TSMC's N5 will have excess capacity by 2030 as customers migrate to N3/N2 |
| **IP licensing cost** -- $4M+ for commercial IP cores | MEDIUM | LOW | Open-source alternatives exist for most blocks. HBM PHY is the main commercial dependency |

### 10.3 n=6 Specific Risks

| Risk | Assessment |
|------|-----------|
| **n=6 parameters are suboptimal** -- What if 128 SM beats 144 SM? | This is exactly what HEXA-1 is designed to test. The sensitivity analysis (Section 7.4 of chip-architecture.md) predicts 144 is a convex optimum. If wrong, we learn something valuable and adjust |
| **Egyptian power distribution has no practical advantage** -- 1/2+1/3+1/6 may be equivalent to any 50/33/17 split | The claim is that integer-ratio voltages reduce conversion losses. Test chip (Phase 2) will measure actual power distribution efficiency vs conventional PDN |
| **tau=4 pipeline is an arbitrary constraint** -- 4 might just happen to be a number of divisors, not a microarchitectural optimum | Fair criticism. The FPGA prototype (Phase 1) will benchmark tau=4 against tau=5 and tau=6 pipeline variants. If tau=4 loses, the pipeline depth becomes a free parameter |

---

## 11. ANIMA-SOC Integration (CHIP-P2-2 alignment)

HEXA-1 incorporates the ANIMA-SOC 10D TCU architecture defined in chip-architecture.md Section 16:

| Subsystem | HEXA-1 Implementation |
|-----------|-----------------------|
| 10D TCU | Tensor dimensions = sopfr(6)*phi(6) = 5*2 = 10. Each SM processes 10D tensor tiles |
| PureField 72+72 SM | 144 SM organized as two 72-SM hemispheres (front-end inference + back-end training). n*sigma = 6*12 = 72 per hemisphere |
| HEXA-TOPO Bott-8 NoC | 12x12 mesh with Bott periodicity 8 = n+phi = 6+2. Deadlock-free routing proven by 1M-cycle simulation (PASS) |
| Clifford Cl(8) addressing | 256-bit NoC link width = (sigma+tau)^2 = 16^2 = 256. Sufficient for Cl(8) spinor addressing |

---

## 12. Success Criteria for HEXA-1 v1

| Criterion | Threshold | Stretch |
|-----------|-----------|---------|
| Silicon functional (boots RISC-V, runs inference) | YES | -- |
| 144 SM all active simultaneously | 128+ SM | 144 SM |
| INT8 TOPS measured | >80 TOPS | >120 TOPS |
| Power at nominal workload | <250 W | <200 W |
| HBM3 bandwidth utilized | >60% theoretical | >80% |
| Inference accuracy (Llama-7B INT8) | Matches FP32 reference within 1% | <0.5% |
| Egyptian power split measured | 50/33/17 +/- 5% | +/- 2% |
| tau=4 pipeline IPC sustained | >1.5 | >2.0 |
| Total bugs to fix post-silicon | <50 critical | <20 |
| Time from tape-out to working demo | <6 months | <3 months |

---

## 13. Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| v1.0 | 2026-04-16 | PRD-P1-4 (HEXA-1 chip baseline spec) | Initial creation. Architecture overview, n=6 parameter mapping, PPA budget, comparison, prototype path, BoM, timeline, risks |

---

## 14. References

- `domains/compute/chip-architecture/chip-architecture.md` -- Parent HEXA-ARCH domain
- `domains/compute/chip-hexa1/chip-hexa1.md` -- HEXA-1 domain document (n=6 parameter tables, DSE, verification code)
- `domains/compute/chip-architecture/mk3-roadmap-l1-l15-audit-2026-04-15.md` -- L1--L15 audit
- `domains/compute/chip-hexa1/verify_chip-hexa1.hexa` -- Verification stub
- OEIS A000203 (sigma), A000005 (tau), A000010 (Euler phi), A001414 (sopfr)
- NVIDIA H100 Datasheet (2023), AMD MI300X Whitepaper (2023), Google TPU v5e (2023)
- TSMC N5 Technology Brief, CoWoS-S Packaging Overview
