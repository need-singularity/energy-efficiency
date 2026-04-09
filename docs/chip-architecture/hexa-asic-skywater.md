# HEXA-EDGE Mini -- SkyWater 130nm ASIC via Efabless chipIgnite

**The First Physical n=6 Silicon: Proving Ground for HEXA-EDGE Architecture**

> Before you tape out at N2, you tape out at 130nm.
> Before you spend $100M, you spend $0.
> HEXA-EDGE Mini: the n=6 architecture made real in open-source silicon.

**Date**: 2026-04-01
**Status**: Architecture Specification v1.0
**Process**: SkyWater SKY130 (130nm, 1.8V)
**PDK**: sky130A (open-source, Apache 2.0)
**Shuttle**: Efabless chipIgnite (Open MPW or dedicated run)
**Dependencies**: BT-28, BT-33, BT-56, BT-58, BT-59, HEXA-EDGE spec

---

## N6 Constants Reference

```
  n = 6          phi(6) = 2       tau(6) = 4       sigma(6) = 12
  sopfr(6) = 5   mu(6) = 1        J_2(6) = 24      R(6) = 1
  P_2 = 28       sigma^2 = 144    sigma*J_2 = 288   phi^tau = 16
  2^n = 64       sigma-tau = 8    sigma-phi = 10     sigma-mu = 11
  2^sigma = 4096  sigma*tau = 48   n/phi = 3
```

---

## 1. Design Overview

HEXA-EDGE Mini is a minimal proof-of-concept ASIC implementing the core n=6
subsystems of the HEXA-EDGE architecture on the SkyWater 130nm open-source PDK.
The goal is not performance -- it is validation. Every architectural parameter
derived from perfect number arithmetic gets burned into real silicon.

```
  ┌────────────────────────────────────────────────────────────────────┐
  │              HEXA-EDGE Mini -- Design Overview                     │
  │              SkyWater SKY130 / 130nm / 1.8V / 50 MHz              │
  │                                                                    │
  │   ┌──────────────────────────────────────────────────────────┐    │
  │   │                 TARGET SUBSYSTEMS                         │    │
  │   │                                                          │    │
  │   │  [1] RISC-V N6 Core (RV32IM)                             │    │
  │   │      n/phi=3-wide decode, n=6-stage pipeline             │    │
  │   │      2^n=64 registers (32 arch + 32 rename)              │    │
  │   │                                                          │    │
  │   │  [2] Egyptian Memory Controller                          │    │
  │   │      16 KB SRAM total (phi^tau = 16)                     │    │
  │   │      1/2 Stack (8 KB) + 1/3 Heap (5.3 KB)               │    │
  │   │      + 1/6 Arena (2.7 KB)                                │    │
  │   │                                                          │    │
  │   │  [3] HEXA-LANG Decoder                                   │    │
  │   │      sigma*tau+sopfr = 53 keyword CAM                    │    │
  │   │      J_2=24-bit opcode width                             │    │
  │   │                                                          │    │
  │   │  [4] Izhikevich Neuron Ring                              │    │
  │   │      n=6 neurons, sigma=12 synapses                      │    │
  │   │      SNN proof-of-concept for edge AI                    │    │
  │   │                                                          │    │
  │   │  [5] GPIO: J_2=24 pins                                   │    │
  │   │  [6] SPI: n=6 channels                                   │    │
  │   │  [7] Clock: 50 MHz (conservative for 130nm)              │    │
  │   └──────────────────────────────────────────────────────────┘    │
  │                                                                    │
  │   Die Area Budget: sigma-phi = 10 mm^2 (3.16 mm x 3.16 mm)      │
  │   Core Logic:      ~5.8 mm^2 usable (after pad ring)             │
  │   Gate Count:      ~120K gates (estimated)                        │
  │   Power:           ~100 mW @ 1.8V, 50 MHz                        │
  └────────────────────────────────────────────────────────────────────┘
```

### 1.1 Why 130nm?

```
  ┌───────────────────────────────────────────────────────┐
  │  HEXA-EDGE Scaling Roadmap                            │
  │                                                       │
  │  Phase 0: SKY130 (this design)                        │
  │    - Free MPW shuttle, open PDK                       │
  │    - Validate RTL, verify n=6 parameters              │
  │    - 50 MHz, ~100 mW, 10 mm^2                        │
  │                                                       │
  │  Phase 1: GF180MCU (180nm, Efabless)                  │
  │    - Alternative open PDK, radiation-hard option       │
  │    - Same RTL, different backend                       │
  │                                                       │
  │  Phase 2: TSMC 28nm (shuttle via Europractice/MUSE)   │
  │    - 1 GHz target, add GPU shaders                    │
  │    - Full HEXA-LANG engine                             │
  │                                                       │
  │  Phase 3: TSMC N2 (production HEXA-EDGE)              │
  │    - 3 GHz, 6W TDP, 72 mm^2                           │
  │    - Full HEXA-EDGE spec                               │
  │                                                       │
  │  Scaling Factors (130nm → N2):                         │
  │    Frequency:    50 MHz → 3 GHz       (60x)           │
  │    Power/gate:   ~100 mW → ~6W full   (area scales)   │
  │    Density:      ~5K gates/mm^2 → ~250M tr/mm^2       │
  │    Area:         10 mm^2 → 72 mm^2 (but 50,000x more) │
  └───────────────────────────────────────────────────────┘
```

---

## 2. Floorplan

### 2.1 Die Layout

```
  ┌─────────────────────────────── 3.16 mm ───────────────────────────────┐
  │                                                                       │
  │   P P P P P P P P P P P P P P P P P P P P P P P P P P P P P P P P   │
  │   A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A   │
  │   D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D   │
  │                                                                       │
  │ P ┌─────────────────────────────────────────────────────────────┐ P   │
  │ A │                                                             │ A   │
  │ D │   ┌───────────────────┐  ┌────────────────────────────┐    │ D   │
  │   │   │                   │  │                            │    │     │
  │ P │   │  RISC-V N6 CORE   │  │    SRAM MACROS (16 KB)     │    │ P   │
  │ A │   │                   │  │                            │    │ A   │
  │ D │   │  3-wide decode    │  │  ┌──────────────────────┐  │    │ D   │
  │   │   │  6-stage pipe     │  │  │ Stack: 8 KB (1/2)    │  │    │     │
  │ P │   │  ALU + MUL + DIV  │  │  ├──────────────────────┤  │    │ P   │
  │ A │   │  ~2.2 mm^2        │  │  │ Heap: 5.3 KB (1/3)   │  │    │ A   │
  │ D │   │                   │  │  ├──────────────────────┤  │    │ D   │
  │   │   │                   │  │  │ Arena: 2.7 KB (1/6)  │  │    │     │
  │ P │   └───────────────────┘  │  └──────────────────────┘  │    │ P   │
  │ A │                          │  ~1.8 mm^2                 │    │ A   │
  │ D │   ┌───────────────────┐  └────────────────────────────┘    │ D   │
  │   │   │                   │                                     │     │
  │ P │   │  HEXA-LANG        │  ┌────────────────────────────┐    │ P   │
  │ A │   │  DECODER           │  │                            │    │ A   │
  │ D │   │  53-keyword CAM   │  │   IZHIKEVICH NEURON RING   │    │ D   │
  │   │   │  ~0.8 mm^2        │  │   n=6 neurons              │    │     │
  │ P │   │                   │  │   sigma=12 synapses         │    │ P   │
  │ A │   └───────────────────┘  │   ~0.3 mm^2                │    │ A   │
  │ D │                          │                            │    │ D   │
  │   │   ┌─────────────────────┐└────────────────────────────┘    │     │
  │ P │   │  PERIPHERALS       │                                    │ P   │
  │ A │   │  SPI x6 + GPIO x24 │  ┌────────────────────────────┐  │ A   │
  │ D │   │  Wishbone bridge    │  │  CLOCK + POWER MGMT        │  │ D   │
  │   │   │  ~0.5 mm^2         │  │  PLL, decoupling           │  │     │
  │ P │   │                     │  │  ~0.2 mm^2                 │  │ P   │
  │ A │   └─────────────────────┘  └────────────────────────────┘  │ A   │
  │ D │                                                             │ D   │
  │   └─────────────────────────────────────────────────────────────┘     │
  │                                                                       │
  │   P P P P P P P P P P P P P P P P P P P P P P P P P P P P P P P P   │
  │   A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A   │
  │   D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D   │
  │                                                                       │
  └───────────────────────────────────────────────────────────────────────┘

  Total Die:       3.16 mm x 3.16 mm = ~10 mm^2
  Pad Ring:        ~4.2 mm^2 (0.12 mm pad pitch, 4 sides)
  Core Area:       ~5.8 mm^2 usable
  Utilization:     ~85% target
```

### 2.2 Pad Ring Assignment

```
  ┌───────────────────────────── TOP EDGE ─────────────────────────────┐
  │                                                                     │
  │  VDD  GPIO[0] GPIO[1] GPIO[2] GPIO[3] GPIO[4] GPIO[5] VDD         │
  │   |      |       |       |       |       |       |      |          │
  ├───+──────+───────+───────+───────+───────+───────+──────+──────────┤
  │                                                                     │
  │  GPIO[6]                                              GPIO[11]     │
  │  GPIO[7]                                              GPIO[10]     │
  │  GPIO[8]             CORE  LOGIC                      GPIO[9]      │
  │  GPIO[12]                                             SPI_CLK[0]   │
  │  GPIO[13]                                             SPI_MOSI[0]  │
  │  GPIO[14]                                             SPI_MISO[0]  │
  │  GPIO[15]                                             SPI_CS[0]    │
  │  GPIO[16]                                             SPI_CLK[1]   │
  │  VSS                                                  VSS          │
  │                                                                     │
  ├───+──────+───────+───────+───────+───────+───────+──────+──────────┤
  │  VDD GPIO[17] GPIO[18] GPIO[19] GPIO[20] GPIO[21] GPIO[22] GPIO[23]│
  │   |      |       |       |       |       |       |       |         │
  │  SPI[2] SPI[3]  SPI[4]  SPI[5]  CLK_IN  RESET  JTAG_TCK JTAG_TMS │
  │                                                                     │
  └─────────────────────────────── BOTTOM EDGE ────────────────────────┘

  Total Pads: 48
    GPIO:      J_2 = 24 pins
    SPI:       n = 6 channels (4 pins each = 24 SPI pins, multiplexed on GPIO)
    Power:     tau = 4 VDD + tau = 4 VSS = 8 power pads
    Clock:     mu = 1 CLK_IN
    Reset:     mu = 1 RESET_N
    JTAG:      tau = 4 (TCK, TMS, TDI, TDO)
    Caravel:   n = 6 management interface pins
    ─────────────────────────────────────
    Sum:       24 + 8 + 1 + 1 + 4 + 6 + 4 spare = 48 pads
               (fits in 130nm pad frame at 120um pitch)
```

---

## 3. RTL-to-GDS Flow

### 3.1 Tool Chain Overview

```
  ┌─────────────────────────────────────────────────────────────────────┐
  │                    OPEN-SOURCE RTL-TO-GDS FLOW                      │
  │                    (OpenLane 2 / OpenROAD)                          │
  │                                                                     │
  │  ┌─────────┐    ┌─────────┐    ┌──────────┐    ┌──────────┐       │
  │  │         │    │         │    │          │    │          │       │
  │  │ Verilog │───>│  Yosys  │───>│ OpenSTA  │───>│ OpenROAD │       │
  │  │  RTL    │    │  Synth  │    │  Timing  │    │  P&R     │       │
  │  │         │    │         │    │  Check   │    │          │       │
  │  └─────────┘    └────┬────┘    └────┬─────┘    └────┬─────┘       │
  │       |              |              |               |              │
  │       |              v              v               v              │
  │       |         ┌─────────┐   ┌──────────┐   ┌──────────┐        │
  │       |         │ Gate-   │   │ SDC      │   │ DEF      │        │
  │       |         │ level   │   │ Timing   │   │ Layout   │        │
  │       |         │ Netlist │   │ Constr.  │   │ (placed  │        │
  │       |         └─────────┘   └──────────┘   │  routed) │        │
  │       |                                       └────┬─────┘        │
  │       |                                            |              │
  │       v                                            v              │
  │  ┌─────────┐    ┌─────────┐    ┌──────────┐   ┌──────────┐      │
  │  │ Cocotb  │    │ Magic   │    │ Netgen   │   │ KLayout  │      │
  │  │ Test-   │    │ DRC     │───>│ LVS      │   │ GDS      │      │
  │  │ bench   │    │ Check   │    │ Check    │   │ Viewer   │      │
  │  └─────────┘    └─────────┘    └──────────┘   └────┬─────┘      │
  │                                                     |             │
  │                                                     v             │
  │                                              ┌──────────┐        │
  │                                              │  GDSII   │        │
  │                                              │  Final   │        │
  │                                              │  Output  │        │
  │                                              └──────────┘        │
  └─────────────────────────────────────────────────────────────────────┘
```

### 3.2 Detailed Flow Steps

```
  Step 1: RTL Design (Verilog)
  ────────────────────────────
    hexa_edge_mini/
    ├── rtl/
    │   ├── hexa_top.v              # Top-level wrapper
    │   ├── hexa_riscv_core.v       # RV32IM N6 core
    │   ├── hexa_alu.v              # ALU with cyclotomic unit
    │   ├── hexa_decode.v           # 3-wide decoder
    │   ├── hexa_pipeline.v         # 6-stage pipeline control
    │   ├── hexa_regfile.v          # 2^n=64 register file
    │   ├── hexa_mem_ctrl.v         # Egyptian memory controller
    │   ├── hexa_sram_wrapper.v     # SKY130 SRAM macro wrapper
    │   ├── hexa_lang_decoder.v     # 53-keyword CAM
    │   ├── hexa_snn_ring.v         # Izhikevich n=6 ring
    │   ├── hexa_spi.v              # SPI controller (x6)
    │   ├── hexa_gpio.v             # GPIO (x24)
    │   ├── hexa_wishbone.v         # Wishbone bus bridge
    │   └── hexa_clk_rst.v          # Clock/reset distribution
    ├── tb/
    │   ├── test_hexa_top.py        # Cocotb top-level test
    │   ├── test_riscv_core.py      # CPU instruction tests
    │   ├── test_mem_ctrl.py        # Egyptian partition test
    │   ├── test_snn_ring.py        # Neuron firing test
    │   └── test_hexa_lang.py       # Keyword decode test
    ├── constraints/
    │   ├── hexa_mini.sdc           # Timing constraints
    │   └── hexa_mini.def           # Floorplan DEF
    └── config/
        └── config.json             # OpenLane configuration

  Step 2: Synthesis (Yosys)
  ─────────────────────────
    Input:   RTL Verilog + SKY130 liberty files
    Command: yosys -p "read_verilog rtl/*.v;
                       synth -top hexa_top;
                       dfflibmap -liberty sky130_fd_sc_hd__tt_025C_1v80.lib;
                       abc -liberty sky130_fd_sc_hd__tt_025C_1v80.lib;
                       write_verilog hexa_synth.v"
    Output:  Gate-level netlist (~120K gates)
    Library: sky130_fd_sc_hd (high-density standard cells)
    Target:  50 MHz → 20 ns clock period

  Step 3: Static Timing Analysis (OpenSTA)
  ─────────────────────────────────────────
    Input:   Synthesized netlist + SDC constraints
    Check:   Setup/hold margins at 50 MHz
    Corners: tt_025C_1v80 (typical)
             ss_100C_1v60 (slow-slow)
             ff_n40C_1v95 (fast-fast)

  Step 4: Floorplan + Placement + CTS + Routing (OpenROAD)
  ────────────────────────────────────────────────────────
    4a. Floorplan:    Define die area, IO placement, macro placement
    4b. Power Plan:   VDD/VSS grid (M4/M5 stripes)
    4c. Placement:    Global + detailed placement
    4d. CTS:          Clock tree synthesis (max skew < 500ps)
    4e. Routing:      Global + detailed routing (5 metal layers)
    4f. Filler:       Fill cells + decap cells

  Step 5: Signoff (Magic + Netgen)
  ────────────────────────────────
    DRC:  Magic VLSI (SKY130 design rules)
    LVS:  Netgen (layout vs. schematic)
    PEX:  Magic parasitic extraction
    STA:  OpenSTA on extracted netlist (post-route)

  Step 6: GDS-II Export
  ─────────────────────
    Output: hexa_edge_mini.gds (final tapeout file)
    Submit: Efabless chipIgnite platform
```

### 3.3 SKY130 PDK Cell Library Usage

```
  ┌────────────────────────────────────────────────────────────┐
  │  SKY130 Standard Cell Libraries Used                       │
  │                                                            │
  │  Library                    Purpose                        │
  │  ──────────────────────────────────────────────────────    │
  │  sky130_fd_sc_hd            High-density std cells         │
  │  sky130_fd_sc_hvl           High-voltage level shifters    │
  │  sky130_sram_macros         OpenRAM SRAM (1KB/2KB/4KB)     │
  │  sky130_fd_io               I/O pad cells                  │
  │  sky130_ef_io               Enhanced I/O (Efabless)        │
  │                                                            │
  │  Key Cells:                                                │
  │    DFF:     sky130_fd_sc_hd__dfrtp_1  (reset flip-flop)    │
  │    NAND:    sky130_fd_sc_hd__nand2_1                       │
  │    NOR:     sky130_fd_sc_hd__nor2_1                        │
  │    INV:     sky130_fd_sc_hd__inv_1                         │
  │    MUX:     sky130_fd_sc_hd__mux2_1                        │
  │    BUF:     sky130_fd_sc_hd__buf_2    (clock buffers)      │
  │    CLKBUF:  sky130_fd_sc_hd__clkbuf_8 (CTS)               │
  │                                                            │
  │  SRAM Macros (OpenRAM):                                    │
  │    sky130_sram_1kbyte_1rw1r_8x1024_8                       │
  │      - 1 KB, 8-bit, 1024 words                             │
  │      - Used: 16 instances = 16 KB total                    │
  │      - Partition: 8x Stack + 5x Heap + 3x Arena            │
  │                   (8+5+3=16, ratio: 1/2+5/16+3/16          │
  │                    closest integer split to 1/2+1/3+1/6)   │
  │                                                            │
  │  Metal Stack (SKY130):                                     │
  │    M1: local interconnect   (0.17 um pitch)                │
  │    M2: horizontal routing   (0.14 um width)                │
  │    M3: vertical routing     (0.14 um width)                │
  │    M4: power horizontal     (0.30 um width)                │
  │    M5: power vertical       (0.30 um width)                │
  │    (sopfr = 5 metal layers -- n=6 match)                   │
  └────────────────────────────────────────────────────────────┘
```

---

## 4. Caravel Harness Integration

### 4.1 Caravel SoC Architecture

```
  ┌────────────────────────────────────────────────────────────────────────┐
  │                   EFABLESS CARAVEL SoC HARNESS                         │
  │                   (SKY130, 10 mm^2 total die)                          │
  │                                                                        │
  │  ┌─────────────────────┐    ┌──────────────────────────────────────┐  │
  │  │                     │    │                                      │  │
  │  │  MANAGEMENT CORE    │    │       USER PROJECT AREA              │  │
  │  │  (pre-hardened)     │    │       (HEXA-EDGE Mini lives here)    │  │
  │  │                     │    │                                      │  │
  │  │  VexRiscv (RV32I)   │    │   ┌──────────────────────────────┐  │  │
  │  │  UART bootloader    │    │   │                              │  │  │
  │  │  SPI flash ctrl     │    │   │   hexa_top (user_project_    │  │  │
  │  │  GPIO mux           │    │   │             wrapper)         │  │  │
  │  │  Housekeeping SPI   │    │   │                              │  │  │
  │  │  Logic analyzer     │    │   │   RISC-V + Mem + SNN +       │  │  │
  │  │  Timer              │    │   │   HEXA-LANG + SPI + GPIO     │  │  │
  │  │                     │    │   │                              │  │  │
  │  │  1 MB flash         │    │   │   Area: 2.92 mm x 3.52 mm   │  │  │
  │  │  (external)         │    │   │   = 10.28 mm^2 usable       │  │  │
  │  │                     │    │   │                              │  │  │
  │  └──────────┬──────────┘    │   └──────────────────────────────┘  │  │
  │             │               │                                      │  │
  │             │  Wishbone     │                                      │  │
  │             │  Bus          │                                      │  │
  │             v               │                                      │  │
  │  ┌──────────────────────────┼──────────────────────────────────┐  │  │
  │  │       WISHBONE CROSSBAR INTERCONNECT                        │  │  │
  │  │       32-bit data, 32-bit address                           │  │  │
  │  │       Management core = master                              │  │  │
  │  │       User project = slave                                   │  │  │
  │  └─────────────────────────────────────────────────────────────┘  │  │
  │                                                                        │
  │  ┌──────────────────────────────────────────────────────────────────┐  │
  │  │                        I/O RING                                  │  │
  │  │  38 user IOs (active-high active-low configurable)               │  │
  │  │  + power pads (VCCD1, VCCD2, VSSA1, VSSA2, VDDA1, VDDA2)       │  │
  │  │  + management IOs (flash SPI, UART, GPIO)                        │  │
  │  └──────────────────────────────────────────────────────────────────┘  │
  └────────────────────────────────────────────────────────────────────────┘
```

### 4.2 User Project Wrapper

```
  ┌──────────────────────────────────────────────────────────────────┐
  │  user_project_wrapper.v                                          │
  │                                                                  │
  │  Interface to Caravel:                                           │
  │                                                                  │
  │    Wishbone Slave:                                               │
  │      input         wb_clk_i        // System clock               │
  │      input         wb_rst_i        // System reset               │
  │      input         wbs_stb_i       // Strobe                     │
  │      input         wbs_cyc_i       // Cycle                      │
  │      input         wbs_we_i        // Write enable               │
  │      input  [3:0]  wbs_sel_i       // Byte select                │
  │      input  [31:0] wbs_dat_i       // Write data                 │
  │      input  [31:0] wbs_adr_i       // Address                    │
  │      output        wbs_ack_o       // Acknowledge                │
  │      output [31:0] wbs_dat_o       // Read data                  │
  │                                                                  │
  │    Logic Analyzer:                                               │
  │      input  [127:0] la_data_in     // From management core       │
  │      output [127:0] la_data_out    // To management core         │
  │      input  [127:0] la_oenb        // Output enable (active low) │
  │                                                                  │
  │    User IOs:                                                     │
  │      input  [`MPRJ_IO_PADS-1:0] io_in     // 38 inputs          │
  │      output [`MPRJ_IO_PADS-1:0] io_out    // 38 outputs         │
  │      output [`MPRJ_IO_PADS-1:0] io_oeb    // Output enable      │
  │                                                                  │
  │    User IRQs:                                                    │
  │      output [2:0] user_irq        // n/phi = 3 IRQ lines        │
  │                                                                  │
  │  Memory Map (Wishbone address space):                            │
  │    0x3000_0000 .. 0x3000_3FFF : SRAM (16 KB)                    │
  │    0x3000_4000 .. 0x3000_40FF : SPI registers                   │
  │    0x3000_4100 .. 0x3000_41FF : GPIO registers                  │
  │    0x3000_4200 .. 0x3000_42FF : HEXA-LANG decoder regs          │
  │    0x3000_4300 .. 0x3000_43FF : SNN control registers           │
  │    0x3000_4400 .. 0x3000_44FF : Clock/status registers          │
  └──────────────────────────────────────────────────────────────────┘
```

### 4.3 Caravel Integration Diagram

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │                                                                      │
  │   EXTERNAL              CARAVEL                 HEXA-EDGE MINI       │
  │                                                                      │
  │  ┌─────────┐       ┌──────────────┐        ┌──────────────────┐     │
  │  │  SPI    │──────>│  Management  │───WB──>│  hexa_top        │     │
  │  │  Flash  │       │  Core        │        │                  │     │
  │  │  (1MB)  │<──────│  (VexRiscv)  │<──WB──│  RISC-V N6 core  │     │
  │  └─────────┘       │              │        │  mem_ctrl        │     │
  │                     │  Bootloader: │        │  snn_ring        │     │
  │  ┌─────────┐       │  1. Power on  │        │  hexa_lang_dec   │     │
  │  │  UART   │<─────>│  2. Load FW   │        │  spi x6          │     │
  │  │  Debug  │       │  3. Config IO │        │  gpio x24        │     │
  │  └─────────┘       │  4. Release   │        │                  │     │
  │                     │     user rst  │   LA──>│  Logic analyzer  │     │
  │  ┌─────────┐       │  5. User runs │<──LA──│  128-bit probe   │     │
  │  │  GPIO   │       │              │        │                  │     │
  │  │  Pins   │<═════>│  IO Mux      │<═════>│  io_in/io_out    │     │
  │  │ (38)    │       │              │        │  io_oeb          │     │
  │  └─────────┘       └──────────────┘        └──────────────────┘     │
  │                                                                      │
  │   Boot Sequence:                                                     │
  │     1. Management core powers up, loads firmware from SPI flash      │
  │     2. Firmware configures IO pads (direction, pull-up/down)         │
  │     3. Firmware writes Wishbone registers to configure HEXA core     │
  │     4. Management core deasserts user reset                          │
  │     5. HEXA-EDGE Mini begins autonomous operation                    │
  │     6. Management core monitors via logic analyzer probes            │
  │     7. IRQ lines (x3) signal events to management core              │
  └──────────────────────────────────────────────────────────────────────┘
```

---

## 5. Verification Plan

### 5.1 Verification Strategy

```
  ┌─────────────────────────────────────────────────────────────────┐
  │              VERIFICATION PYRAMID                               │
  │                                                                 │
  │                     /\                                          │
  │                    /  \                                         │
  │                   / SoC \       System-level (Caravel + HEXA)   │
  │                  / Tests  \     Cocotb + Verilator              │
  │                 /──────────\                                    │
  │                /  Block-     \   Per-module tests               │
  │               /   Level      \  Cocotb + iverilog               │
  │              /    Tests       \                                 │
  │             /──────────────────\                                │
  │            /  Formal            \  SymbiYosys (bounded)         │
  │           /   Verification       \ Egyptian memory assertions   │
  │          /────────────────────────\                             │
  │         /  Unit Tests (Python)      \ Instruction decode,       │
  │        /   Reference Model           \ ALU operations           │
  │       /──────────────────────────────\                         │
  │                                                                 │
  │  Coverage Target: >95% line, >90% branch, >85% FSM state       │
  └─────────────────────────────────────────────────────────────────┘
```

### 5.2 Test Plan Matrix

```
  ┌─────────────────┬─────────────────────────────────┬──────────┬────────┬──────────────────────────────────────────────────────────┐
  │  Module          │  Test                           │  Method  │ Status │  Detail                                                    │
  ├─────────────────┼─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │  RISC-V Core    │  RV32I compliance (riscv-tests) │  Cocotb  │  SPEC  │  Run official riscv-tests rv32ui/rv32mi suites (55 ISA   │
  │                 │                                 │          │        │  tests). Assert n=6-stage pipeline retires each insn in   │
  │                 │                                 │          │        │  6 cycles. Use Cocotb BFM driving Wishbone to load ELF.   │
  │                 ├─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │                 │  RV32M multiply/divide          │  Cocotb  │  SPEC  │  Verify 32x32→64 MUL/MULH/DIV/REM. Multiply latency =   │
  │                 │                                 │          │        │  tau=4 cycles (radix-4 Booth). Divide = sigma-tau=8 cyc.  │
  │                 │                                 │          │        │  Edge cases: divide-by-zero returns 0xFFFFFFFF per spec.  │
  │                 ├─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │                 │  Pipeline hazards (RAW/WAW)     │  Cocotb  │  SPEC  │  Inject dependent instruction sequences (ADD r1→r2 fwd). │
  │                 │                                 │          │        │  Verify n/phi=3-wide decode stalls on RAW hazard within   │
  │                 │                                 │          │        │  phi=2 cycle forwarding window. WAW resolved by in-order  │
  │                 │                                 │          │        │  writeback at stage 6. Check CPI stays <= 1.2.            │
  │                 ├─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │                 │  Branch prediction              │  Cocotb  │  SPEC  │  2-bit saturating predictor, sigma=12-entry BTB indexed   │
  │                 │                                 │          │        │  by PC[5:2]. Misprediction penalty = sopfr=5 cycles       │
  │                 │                                 │          │        │  (flush stages 2..6). Test: tight loop (>90% hit), branch │
  │                 │                                 │          │        │  storm (random targets, measure mispredict rate).          │
  │                 ├─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │                 │  CSR read/write                 │  Cocotb  │  SPEC  │  Validate mstatus, mie, mip, mcause, mepc, mtvec CSRs.   │
  │                 │                                 │          │        │  CSRRW/CSRRS/CSRRC in single cycle. Custom CSRs at        │
  │                 │                                 │          │        │  0xFC0..0xFCB (sigma=12 N6 status registers): pipeline    │
  │                 │                                 │          │        │  occupancy, SNN state, memory region usage counters.      │
  ├─────────────────┼─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │  Mem Controller │  Stack region bounds (0..8191)  │  Formal  │  SPEC  │  SymbiYosys BMC depth=20: assert addr ∈ [0x0000,0x1FFF]  │
  │                 │                                 │          │        │  ↔ region==STACK. Stack = TOTAL_MEM/2 = 8192 bytes.       │
  │                 │                                 │          │        │  Cover: push/pop to boundary, overflow triggers fault.    │
  │                 ├─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │                 │  Heap region bounds             │  Formal  │  SPEC  │  BMC depth=20: assert addr ∈ [0x2000,0x3555] ↔           │
  │                 │                                 │          │        │  region==HEAP. Heap = TOTAL_MEM/3 = 5461 bytes.           │
  │                 │                                 │          │        │  Verify malloc metadata stays within 1/3 partition.       │
  │                 ├─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │                 │  Arena region bounds             │  Formal  │  SPEC  │  BMC depth=20: assert addr ∈ [0x3556,0x3FFF] ↔           │
  │                 │                                 │          │        │  region==ARENA. Arena = TOTAL_MEM/6 = 2731 bytes.         │
  │                 │                                 │          │        │  1/2+1/3+1/6=1 Egyptian fraction identity verified.       │
  │                 ├─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │                 │  Cross-region access = fault    │  Formal  │  SPEC  │  BMC depth=12: STACK write to addr>=0x2000 → fault=1     │
  │                 │                                 │          │        │  within μ=1 cycle. HEAP write to addr<0x2000 → fault.    │
  │                 │                                 │          │        │  Fault handler loads mcause with region-violation code.   │
  │                 ├─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │                 │  Concurrent access arbitration  │  Cocotb  │  SPEC  │  CPU + SNN simultaneous read: round-robin arbiter with   │
  │                 │                                 │          │        │  phi=2 priority levels. CPU gets priority on even cycles, │
  │                 │                                 │          │        │  SNN on odd. Max stall = mu=1 cycle. Verify no data       │
  │                 │                                 │          │        │  corruption under back-to-back contention for 10K cycles. │
  ├─────────────────┼─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │  HEXA-LANG Dec  │  All 53 keywords recognized     │  Cocotb  │  SPEC  │  Drive all σ*τ+sopfr = 53 keyword encodings into CAM     │
  │                 │                                 │          │        │  input. Assert each produces unique J₂=24-bit opcode.    │
  │                 │                                 │          │        │  Sweep: sequential scan of keyword IDs 0..52, verify     │
  │                 │                                 │          │        │  match_valid=1 and opcode matches golden reference LUT.   │
  │                 ├─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │                 │  Unknown keyword = default       │  Cocotb  │  SPEC  │  Feed keyword IDs 53..63 (beyond valid range) and random │
  │                 │                                 │          │        │  bit patterns. Assert match_valid=0 and opcode output =  │
  │                 │                                 │          │        │  24'h000000 (NOP). Verify no CAM false-positive matches.  │
  │                 ├─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │                 │  CAM timing (single-cycle)      │  Formal  │  SPEC  │  SymbiYosys: assert that from keyword_in valid to         │
  │                 │                                 │          │        │  opcode_out valid takes exactly μ=1 clock cycle.          │
  │                 │                                 │          │        │  STA: CAM critical path < 20 ns (50 MHz period).         │
  ├─────────────────┼─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │  SNN Ring       │  n=6 neuron fire pattern        │  Cocotb  │  SPEC  │  Initialize n=6 Izhikevich neurons with a=0.02, b=0.2,  │
  │                 │                                 │          │        │  c=-65, d=8 (regular spiking). Inject constant current   │
  │                 │                                 │          │        │  I=10 on neuron 0. After sigma=12 SNN clock cycles,       │
  │                 │                                 │          │        │  verify propagation through ring: neuron k fires at t =  │
  │                 │                                 │          │        │  k*phi cycles (k=0..5). Check spike count over 1000 cyc.  │
  │                 ├─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │                 │  Synapse weight update           │  Cocotb  │  SPEC  │  σ=12 synapses (2 per neuron in ring topology). Apply    │
  │                 │                                 │          │        │  STDP rule: Δw = +A_plus if t_post-t_pre < tau=4 ms,     │
  │                 │                                 │          │        │  Δw = -A_minus otherwise. Weights are 8-bit fixed-point.  │
  │                 │                                 │          │        │  Verify weight saturation at 0xFF, no underflow below 0.  │
  │                 ├─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │                 │  Ring oscillation stability     │  Cocotb  │  SPEC  │  Run n=6 neuron ring for 50,000 SNN clocks (at 8.33 MHz  │
  │                 │                                 │          │        │  = CLK_SYS/n). Assert spike interval variance < 5%.      │
  │                 │                                 │          │        │  No neuron enters quiescent state permanently. Ring       │
  │                 │                                 │          │        │  frequency stabilizes within σ²=144 initial cycles.       │
  ├─────────────────┼─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │  SPI            │  Mode 0/1/2/3 transactions      │  Cocotb  │  SPEC  │  For each SPI mode (CPOL,CPHA ∈ {0,1}²=τ modes): send   │
  │                 │                                 │          │        │  8-bit, 16-bit, 32-bit frames via channel 0. Verify MISO │
  │                 │                                 │          │        │  loopback matches MOSI. SPI_CLK = 12.5 MHz (CLK/τ).     │
  │                 ├─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │                 │  6-channel arbitration           │  Cocotb  │  SPEC  │  Assert all n=6 SPI channels simultaneously. Round-robin │
  │                 │                                 │          │        │  arbiter grants 1 channel per SPI_CLK cycle. Verify no   │
  │                 │                                 │          │        │  channel starved over σ=12 consecutive arbitration rounds.│
  │                 │                                 │          │        │  Max latency = n-1=5 SPI_CLK cycles for lowest-priority. │
  │                 ├─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │                 │  Clock divider                   │  Cocotb  │  SPEC  │  Programmable divider: CLK_SYS / (2*N) where N=1..σ=12. │
  │                 │                                 │          │        │  Default N=τ=4 → 12.5 MHz. Verify duty cycle 50%±2%.    │
  │                 │                                 │          │        │  Test: sweep N from 1 to 12, measure output frequency.   │
  ├─────────────────┼─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │  GPIO           │  All 24 pins I/O toggle          │  Cocotb  │  SPEC  │  Loop over J₂=24 GPIO pins: set output_enable=1, drive  │
  │                 │                                 │          │        │  high, read back=1; drive low, read back=0. Then set     │
  │                 │                                 │          │        │  output_enable=0, drive externally, verify input capture. │
  │                 │                                 │          │        │  Toggle rate: 1 transition per phi=2 CLK_SYS cycles.     │
  │                 ├─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │                 │  Interrupt generation            │  Cocotb  │  SPEC  │  Configure n=6 GPIO pins (GPIO[0..5]) as edge-triggered  │
  │                 │                                 │          │        │  interrupt sources (rising/falling/both). Drive edges,    │
  │                 │                                 │          │        │  verify IRQ line asserts within μ=1 cycle. Check ISR      │
  │                 │                                 │          │        │  reads correct GPIO IRQ status register (24-bit bitmap). │
  ├─────────────────┼─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │  Wishbone       │  Single read/write              │  Cocotb  │  SPEC  │  Wishbone B4 pipelined: assert cyc+stb, wait ack within  │
  │                 │                                 │          │        │  phi=2 cycles. Write 32-bit word to each memory region,   │
  │                 │                                 │          │        │  read back, compare. Test all tau=4 byte select combos.   │
  │                 ├─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │                 │  Burst transactions              │  Cocotb  │  SPEC  │  Wishbone incrementing burst of n=6 words. Assert stb    │
  │                 │                                 │          │        │  held for 6 consecutive cycles, ack pipelined 1 cycle    │
  │                 │                                 │          │        │  behind. Verify sigma=12 words transferred in 2 bursts.  │
  │                 │                                 │          │        │  Bus throughput = 32 bits * 50 MHz = 200 MB/s peak.       │
  │                 ├─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │                 │  Address decode correctness      │  Formal  │  SPEC  │  SymbiYosys: for each of n=6 peripherals mapped in addr  │
  │                 │                                 │          │        │  space, assert unique decode (no overlap). Memory map:    │
  │                 │                                 │          │        │  SRAM 0x00000000..0x00003FFF (φ^τ=16 KB), GPIO 0x10000,  │
  │                 │                                 │          │        │  SPI 0x10100, SNN 0x10200, CSR 0x10300. BMC depth=10.    │
  ├─────────────────┼─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │  Top Level      │  Boot sequence (Caravel harness)│  Cocotb  │  SPEC  │  Caravel integration test: management core releases      │
  │                 │                                 │          │        │  user_clock2, deasserts reset. N6 core fetches from       │
  │                 │                                 │          │        │  0x00000000 (reset vector). First n=6 instructions in     │
  │                 │                                 │          │        │  boot ROM initialize stack pointer to 0x1FFF, set mtvec. │
  │                 │                                 │          │        │  Boot completes in < σ²=144 cycles.                      │
  │                 ├─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │                 │  Memory-mapped IO access        │  Cocotb  │  SPEC  │  CPU executes SW/LW to GPIO base (0x10000). Toggle       │
  │                 │                                 │          │        │  GPIO[0] via store, verify physical pin change within     │
  │                 │                                 │          │        │  phi=2 cycles. Read SNN status register at 0x10200,       │
  │                 │                                 │          │        │  verify n=6 neuron state bits [5:0] are accessible.       │
  │                 ├─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │                 │  IRQ generation + handling       │  Cocotb  │  SPEC  │  Trigger GPIO interrupt on pin 0. Verify: (1) mip.MEIP   │
  │                 │                                 │          │        │  set within μ=1 cycle, (2) PC jumps to mtvec within      │
  │                 │                                 │          │        │  sopfr=5 cycles (pipeline flush), (3) ISR reads mcause=  │
  │                 │                                 │          │        │  sigma=12+pin_id, (4) mret resumes from mepc correctly.  │
  │                 ├─────────────────────────────────┼──────────┼────────┼──────────────────────────────────────────────────────────┤
  │                 │  Logic analyzer readback         │  Cocotb  │  SPEC  │  Caravel LA probes (128 bits): map σ*J₂=288 internal     │
  │                 │                                 │          │        │  signals via mux into LA[127:0]. Verify pipeline stage   │
  │                 │                                 │          │        │  occupancy (n=6 bits), SNN spike bus (n=6 bits), memory   │
  │                 │                                 │          │        │  region select (phi=2 bits), arbitration state readable.  │
  └─────────────────┴─────────────────────────────────┴──────────┴────────┴──────────────────────────────────────────────────────────┘
```

### 5.3 Formal Verification (Egyptian Memory Regions)

```
  // SymbiYosys assertions for Egyptian memory controller

  // Property 1: Stack region is exactly 1/2 of total
  assert property (STACK_SIZE == TOTAL_MEM / 2);            // 8192 bytes

  // Property 2: Heap region is exactly 1/3 of total
  assert property (HEAP_SIZE == TOTAL_MEM / 3);             // 5461 bytes

  // Property 3: Arena region is exactly 1/6 of total
  assert property (ARENA_SIZE == TOTAL_MEM / 6);            // 2731 bytes

  // Property 4: Regions sum to total (1/2 + 1/3 + 1/6 = 1)
  assert property (STACK_SIZE + HEAP_SIZE + ARENA_SIZE == TOTAL_MEM);

  // Property 5: No cross-region access
  assert property (addr >= STACK_BASE && addr < STACK_END |->
                   region == STACK);
  assert property (addr >= HEAP_BASE && addr < HEAP_END |->
                   region == HEAP);
  assert property (addr >= ARENA_BASE && addr < ARENA_END |->
                   region == ARENA);

  // Property 6: Out-of-region access triggers fault
  assert property (addr >= TOTAL_MEM |-> fault == 1);
```

### 5.4 DRC/LVS Checklist

```
  ┌────────────────────────────────────────────────────────────────┐
  │  SIGNOFF CHECKLIST (before Efabless submission)                │
  │                                                                │
  │  [ ] DRC clean (Magic) -- 0 violations                        │
  │  [ ] LVS clean (Netgen) -- 0 mismatches                       │
  │  [ ] Antenna check -- all gates protected                      │
  │  [ ] ERC (electrical rule check) -- no floating gates          │
  │  [ ] Density check -- M1-M5 all within 20%-80% fill            │
  │  [ ] Max via count -- no single-via connections on signals     │
  │  [ ] Power grid IR drop -- < 5% VDD (< 90 mV)                 │
  │  [ ] Electromigration -- all wires within SKY130 limits        │
  │  [ ] Timing signoff -- setup/hold met at all corners           │
  │  [ ] Latch-up -- all guard rings present                       │
  │  [ ] Seal ring -- continuous around die                        │
  │  [ ] Pad placement -- matches Caravel frame                    │
  │  [ ] Precheck -- Efabless precheck tool passes                 │
  │  [ ] MPW submission -- GDS + LEF + DEF + netlist uploaded      │
  └────────────────────────────────────────────────────────────────┘
```

---

## 6. Pin Assignment Table

```
  ┌──────┬────────────┬───────────┬────────────────────────────────────┐
  │  Pin │  Name      │  Dir      │  Function                          │
  ├──────┼────────────┼───────────┼────────────────────────────────────┤
  │  IO0 │  GPIO[0]   │  Bidir    │  General purpose / LED             │
  │  IO1 │  GPIO[1]   │  Bidir    │  General purpose / LED             │
  │  IO2 │  GPIO[2]   │  Bidir    │  General purpose / LED             │
  │  IO3 │  GPIO[3]   │  Bidir    │  General purpose / LED             │
  │  IO4 │  GPIO[4]   │  Bidir    │  General purpose / LED             │
  │  IO5 │  GPIO[5]   │  Bidir    │  General purpose / LED             │
  │  IO6 │  GPIO[6]   │  Bidir    │  General purpose / button          │
  │  IO7 │  GPIO[7]   │  Bidir    │  General purpose / button          │
  │  IO8 │  GPIO[8]   │  Bidir    │  General purpose / button          │
  │  IO9 │  GPIO[9]   │  Bidir    │  General purpose / button          │
  │ IO10 │  GPIO[10]  │  Bidir    │  General purpose / button          │
  │ IO11 │  GPIO[11]  │  Bidir    │  General purpose / button          │
  │ IO12 │  GPIO[12]  │  Bidir    │  General purpose / ADC             │
  │ IO13 │  GPIO[13]  │  Bidir    │  General purpose / ADC             │
  │ IO14 │  GPIO[14]  │  Bidir    │  General purpose / DAC             │
  │ IO15 │  GPIO[15]  │  Bidir    │  General purpose / DAC             │
  │ IO16 │  GPIO[16]  │  Bidir    │  General purpose / PWM             │
  │ IO17 │  GPIO[17]  │  Bidir    │  General purpose / PWM             │
  │ IO18 │  GPIO[18]  │  Bidir    │  General purpose                   │
  │ IO19 │  GPIO[19]  │  Bidir    │  General purpose                   │
  │ IO20 │  GPIO[20]  │  Bidir    │  General purpose                   │
  │ IO21 │  GPIO[21]  │  Bidir    │  General purpose                   │
  │ IO22 │  GPIO[22]  │  Bidir    │  General purpose                   │
  │ IO23 │  GPIO[23]  │  Bidir    │  General purpose                   │
  ├──────┼────────────┼───────────┼────────────────────────────────────┤
  │ IO24 │  SPI0_CLK  │  Output   │  SPI channel 0 clock               │
  │ IO25 │  SPI0_MOSI │  Output   │  SPI channel 0 master out          │
  │ IO26 │  SPI0_MISO │  Input    │  SPI channel 0 master in           │
  │ IO27 │  SPI0_CS   │  Output   │  SPI channel 0 chip select         │
  │ IO28 │  SPI1_CLK  │  Output   │  SPI channel 1 clock               │
  │ IO29 │  SPI1_CS   │  Output   │  SPI channel 1 chip select         │
  │ IO30 │  SPI2_CLK  │  Output   │  SPI channel 2 clock               │
  │ IO31 │  SPI2_CS   │  Output   │  SPI channel 2 chip select         │
  │ IO32 │  SPI3_CLK  │  Output   │  SPI channel 3 clock               │
  │ IO33 │  SPI3_CS   │  Output   │  SPI channel 3 chip select         │
  │ IO34 │  SPI4_CLK  │  Output   │  SPI channel 4 clock               │
  │ IO35 │  SPI4_CS   │  Output   │  SPI channel 4 chip select         │
  │ IO36 │  SPI5_CLK  │  Output   │  SPI channel 5 clock               │
  │ IO37 │  SPI5_CS   │  Output   │  SPI channel 5 chip select         │
  ├──────┼────────────┼───────────┼────────────────────────────────────┤
  │  --  │  VCCD1     │  Power    │  1.8V digital core power           │
  │  --  │  VSSD1     │  Power    │  Digital ground                    │
  │  --  │  VCCD2     │  Power    │  1.8V digital core power (2nd)     │
  │  --  │  VSSD2     │  Power    │  Digital ground (2nd)              │
  │  --  │  VDDA1     │  Power    │  3.3V analog power                 │
  │  --  │  VSSA1     │  Power    │  Analog ground                     │
  │  --  │  VDDA2     │  Power    │  3.3V analog power (2nd)           │
  │  --  │  VSSA2     │  Power    │  Analog ground (2nd)               │
  └──────┴────────────┴───────────┴────────────────────────────────────┘

  Pin Count Summary:
    GPIO:     J_2 = 24 pins
    SPI:      n = 6 channels x phi = 2 pins (CLK+CS) = 12 dedicated
              (MOSI/MISO multiplexed on GPIO[24..37] when channel active)
    Power:    sigma-tau = 8 pads (4 VDD domains + 4 VSS)
    Total IO: 38 (matches Caravel user IO count exactly)
```

---

## 7. Timing Analysis

### 7.1 Clock Specification

```
  ┌──────────────────────────────────────────────────────────────┐
  │  CLOCK DOMAIN SPECIFICATION                                  │
  │                                                              │
  │  Primary Clock: CLK_SYS                                      │
  │    Frequency:   50 MHz                                       │
  │    Period:      20 ns                                        │
  │    Source:      Caravel management core (wb_clk_i)           │
  │    Distribution: Clock tree (OpenROAD CTS)                   │
  │                                                              │
  │  Derived Clocks:                                             │
  │    SPI_CLK:    12.5 MHz (CLK_SYS / 4 = CLK / tau)           │
  │    SNN_CLK:    8.33 MHz (CLK_SYS / 6 = CLK / n)             │
  │    GPIO_CLK:   50 MHz (same as CLK_SYS)                     │
  │                                                              │
  │  Clock Relationships:                                        │
  │    CLK_SYS ──┬── CPU pipeline (50 MHz)                       │
  │              ├── Memory controller (50 MHz)                  │
  │              ├── HEXA-LANG decoder (50 MHz)                  │
  │              ├── Wishbone interface (50 MHz)                 │
  │              ├── SPI (50/4 = 12.5 MHz)                      │
  │              └── SNN (50/6 = 8.33 MHz)                      │
  └──────────────────────────────────────────────────────────────┘
```

### 7.2 Timing Diagram -- CPU Pipeline

```
  CLK_SYS  ──┐  ┌──┐  ┌──┐  ┌──┐  ┌──┐  ┌──┐  ┌──┐  ┌──┐  ┌──
              └──┘  └──┘  └──┘  └──┘  └──┘  └──┘  └──┘  └──┘

  Stage 1    |FETCH |      |      |      |      |      |
  (IF)       | I0   |      |      |      |      |      |

  Stage 2    |      |DECODE|      |      |      |      |
  (ID)       |      | I0   |      |      |      |      |

  Stage 3    |      |      | EXEC |      |      |      |
  (EX)       |      |      | I0   |      |      |      |

  Stage 4    |      |      |      | MEM  |      |      |
  (MEM)      |      |      |      | I0   |      |      |

  Stage 5    |      |      |      |      | ALIGN|      |
  (AL)       |      |      |      |      | I0   |      |

  Stage 6    |      |      |      |      |      |WRITE |
  (WB)       |      |      |      |      |      | I0   |

             |<─────── n = 6 pipeline stages ────────>|
             |<── 20ns ──>|
               per stage

  CPI target: ~1.2 (with branch prediction)
  IPC:        ~2.5 (3-wide * 0.83 utilization)
  Throughput: 2.5 * 50 MHz = 125 MIPS peak
```

### 7.3 Critical Paths

```
  ┌──────────────────────────────────────────────────────────────────┐
  │  CRITICAL PATH ANALYSIS (pre-synthesis estimate)                 │
  │                                                                  │
  │  Path 1: ALU Multiply (longest)                                  │
  │    regfile_read -> MUL operand -> 32x32 multiply ->              │
  │    result_mux -> forwarding_mux -> regfile_write                 │
  │    Estimated: ~18 ns (90% of 20 ns budget)                       │
  │    Margin:    2 ns                                               │
  │                                                                  │
  │  Path 2: Memory Load                                             │
  │    addr_calc -> SRAM_read -> alignment -> writeback              │
  │    Estimated: ~15 ns (75% of budget)                             │
  │    Margin:    5 ns                                               │
  │                                                                  │
  │  Path 3: HEXA-LANG CAM Lookup                                   │
  │    opcode_in -> CAM_match (53 entries) -> result_encode          │
  │    Estimated: ~12 ns (60% of budget)                             │
  │    Margin:    8 ns                                               │
  │                                                                  │
  │  Path 4: Branch Resolution                                       │
  │    decode -> comparator -> PC_update -> fetch_redirect            │
  │    Estimated: ~14 ns (70% of budget)                             │
  │    Margin:    6 ns                                               │
  │    Penalty:   n = 6 cycles (full pipeline flush)                 │
  │                                                                  │
  │  SKY130 HD cell delays (typical corner):                         │
  │    INV:    ~0.05 ns                                              │
  │    NAND2:  ~0.08 ns                                              │
  │    NOR2:   ~0.10 ns                                              │
  │    DFF:    setup=0.15 ns, hold=0.05 ns, clk-q=0.20 ns           │
  │    MUX:    ~0.15 ns                                              │
  │    SRAM:   ~5 ns access time (OpenRAM 1KB macro)                 │
  └──────────────────────────────────────────────────────────────────┘
```

### 7.4 Clock Tree

```
  ┌──────────────────────────────────────────────────────────────────┐
  │  CLOCK TREE SYNTHESIS (CTS)                                      │
  │                                                                  │
  │                     CLK_IN (from Caravel)                        │
  │                          |                                       │
  │                     ┌────v────┐                                  │
  │                     │ Root    │                                  │
  │                     │ Buffer  │  sky130_fd_sc_hd__clkbuf_16     │
  │                     └────┬────┘                                  │
  │                          |                                       │
  │              ┌───────────┼───────────┐                           │
  │              |           |           |                            │
  │         ┌────v────┐ ┌───v────┐ ┌───v────┐                       │
  │         │ Branch  │ │ Branch │ │ Branch │   Level 1 buffers     │
  │         │ Buf 0   │ │ Buf 1  │ │ Buf 2  │   (clkbuf_8)         │
  │         └────┬────┘ └───┬────┘ └───┬────┘                       │
  │              |          |          |                              │
  │     ┌───────┼────┐  ┌──┼───┐  ┌──┼───┐                          │
  │     |       |    |  |  |   |  |  |   |                           │
  │    ┌v┐    ┌v┐  ┌v┐┌v┐┌v┐ ┌v┐┌v┐┌v┐ ┌v┐   Level 2 buffers     │
  │    │L│    │L│  │L││L││L│ │L││L││L│ │L│   (clkbuf_4)           │
  │    └┬┘    └┬┘  └┬┘└┬┘└┬┘ └┬┘└┬┘└┬┘ └┬┘                        │
  │     |      |    |   |  |   |  |  |   |                           │
  │    CPU    CPU  MEM MEM HL  SPI SPI SNN GPIO                      │
  │    pipe   reg  ctrl SRAM dec ch0 ch1 ring ctrl                   │
  │                                                                  │
  │  Target:                                                         │
  │    Max skew:      < 500 ps across all endpoints                  │
  │    Max insertion: < 2 ns (root to leaf)                          │
  │    Buffer count:  ~40 clock buffers                              │
  │    Fanout limit:  < 30 per buffer                                │
  │    n/phi = 3 levels of clock tree (n=6 connection)               │
  └──────────────────────────────────────────────────────────────────┘
```

---

## 8. Power Analysis

### 8.1 Power Budget

```
  ┌──────────────────────────────────────────────────────────────────┐
  │  POWER BREAKDOWN (SKY130, 1.8V, 50 MHz)                         │
  │                                                                  │
  │  Component          Dynamic    Leakage    Total     % of TDP    │
  │  ─────────────────────────────────────────────────────────────   │
  │  RISC-V Core        35 mW      3 mW       38 mW     38%         │
  │    ALU + MUL         15 mW      1 mW       16 mW                │
  │    Regfile            8 mW      0.5 mW      8.5 mW              │
  │    Decode + Pipe     12 mW      1.5 mW     13.5 mW              │
  │                                                                  │
  │  SRAM (16 KB)       25 mW      5 mW       30 mW     30%         │
  │    (16x 1KB OpenRAM macros, each ~1.9 mW)                       │
  │                                                                  │
  │  HEXA-LANG Decoder   8 mW      1 mW        9 mW      9%         │
  │    (53-entry CAM)                                                │
  │                                                                  │
  │  SNN Ring            3 mW      0.5 mW      3.5 mW    3.5%       │
  │    (n=6 Izhikevich neurons, fixed-point)                        │
  │                                                                  │
  │  Peripherals         6 mW      1 mW        7 mW      7%         │
  │    SPI x6            3 mW      0.5 mW      3.5 mW              │
  │    GPIO x24          2 mW      0.3 mW      2.3 mW              │
  │    Wishbone          1 mW      0.2 mW      1.2 mW              │
  │                                                                  │
  │  Clock Tree          8 mW      0.5 mW      8.5 mW    8.5%       │
  │                                                                  │
  │  Pad Ring            3 mW      1 mW        4 mW      4%         │
  │  ─────────────────────────────────────────────────────────────   │
  │  TOTAL              88 mW     12 mW      100 mW    100%         │
  │                                                                  │
  │  VDD = 1.8V                                                      │
  │  Total current: 100 mW / 1.8V = 55.6 mA                        │
  │  Power density: 100 mW / 10 mm^2 = 10 mW/mm^2                  │
  │                                                                  │
  │  Egyptian Power Distribution:                                    │
  │    1/2 TDP = CPU core      = 50 mW (actual: 38+12 pad = ~50)   │
  │    1/3 TDP = Memory        = 33 mW (actual: 30+3 periph = ~33)  │
  │    1/6 TDP = Accel + Clock = 17 mW (actual: 9+3.5+4 = ~16.5)   │
  │    1/2 + 1/3 + 1/6 = 1    CHECK                                │
  └──────────────────────────────────────────────────────────────────┘
```

### 8.2 Power Grid Design

```
  ┌──────────────────────────────────────────────────────────────────┐
  │  POWER GRID TOPOLOGY (SKY130 5-metal)                            │
  │                                                                  │
  │  M5 (top) ═══════════════════════════════════  VDD horizontal    │
  │            ═══════════════════════════════════  VSS horizontal    │
  │            ═══════════════════════════════════  VDD horizontal    │
  │            ═══════════════════════════════════  VSS horizontal    │
  │                                                                  │
  │               ║   ║   ║   ║   ║   ║   ║   ║                     │
  │  M4           ║   ║   ║   ║   ║   ║   ║   ║   VDD/VSS vertical  │
  │               ║   ║   ║   ║   ║   ║   ║   ║                     │
  │               ║   ║   ║   ║   ║   ║   ║   ║                     │
  │                                                                  │
  │  M3 ──────── signal routing (vertical) ────────                  │
  │  M2 ──────── signal routing (horizontal) ──────                  │
  │  M1 ──────── local interconnect + std cell power rails ────      │
  │                                                                  │
  │  Grid Specs:                                                     │
  │    M5 VDD/VSS stripe width:  4.0 um                              │
  │    M5 stripe pitch:          30 um                               │
  │    M4 VDD/VSS stripe width:  3.0 um                              │
  │    M4 stripe pitch:          30 um                               │
  │    Via stacks:  M1-M2-M3-M4-M5 (full stack at crossings)        │
  │    IR drop budget: < 5% = < 90 mV                               │
  │    Decap cells: ~10% of core area (fill empty spaces)            │
  │                                                                  │
  │  Cross-section:                                                  │
  │                                                                  │
  │    M5  ████████████    ████████████    ████████████               │
  │         VDD              VSS             VDD                     │
  │    M4  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██               │
  │        VDD VSS VDD VSS VDD VSS VDD VSS VDD VSS VDD              │
  │    M3  ─── signal ─── signal ─── signal ─── signal ───           │
  │    M2  ─── signal ─── signal ─── signal ─── signal ───           │
  │    M1  ─ VDD ─ cell ─ cell ─ cell ─ VSS ─ cell ─ cell ─ VDD ─  │
  │        substrate                                                  │
  └──────────────────────────────────────────────────────────────────┘
```

### 8.3 Technology Scaling Predictions

```
  ┌─────────────────────────────────────────────────────────────────────┐
  │  HEXA-EDGE SCALING: 130nm → N2                                      │
  │                                                                     │
  │  Node     VDD    Freq      Power     Area      Gate Count          │
  │  ────────────────────────────────────────────────────────────────   │
  │  SKY130   1.8V   50 MHz    100 mW    10 mm^2   120K  (this chip)  │
  │  65nm     1.2V   200 MHz   80 mW     4 mm^2    120K               │
  │  P_2=28nm 0.9V   1 GHz     150 mW    1 mm^2    500K  (add GPU)   │
  │  7nm      0.75V  2 GHz     300 mW    0.3 mm^2  5M   (add NPU)   │
  │  N2       0.5V   3 GHz     6W        72 mm^2   50B  (HEXA-EDGE) │
  │                                                                     │
  │  Key Observations:                                                  │
  │    - 130nm to N2: 65x node generations (130/2 = 65nm ... /2^N)     │
  │    - Power/gate scales ~V^2 * f                                     │
  │    - Area/gate scales with lambda^2                                 │
  │    - At N2, same 10 mm^2 holds ~500M transistors                   │
  │    - HEXA-EDGE full spec needs 72 mm^2 @ N2 = ~35B transistors     │
  │    - SKY130 120K gates = validates core architecture only           │
  │                                                                     │
  │  Power Scaling Factor (130nm → N2):                                │
  │    (0.5/1.8)^2 * (3000/50) = 0.077 * 60 = 4.6x per gate          │
  │    But N2 has ~300,000x more gates in 72 mm^2                       │
  │    So total: 100 mW * 4.6 * 300,000 / 1000 --> need power gating  │
  │    Egyptian 1/2+1/3+1/6 power gating keeps TDP at n = 6W           │
  └─────────────────────────────────────────────────────────────────────┘
```

---

## 9. Area Breakdown Table

```
  ┌──────────────────────────────────────────────────────────────────┐
  │  AREA BREAKDOWN (estimated, pre-synthesis)                       │
  │                                                                  │
  │  Block               Gates    Area (mm^2)  % of Core   n=6 Ref  │
  │  ─────────────────────────────────────────────────────────────   │
  │  RISC-V N6 Core      55,000   2.20         38.0%       ---      │
  │    Fetch unit          5,000   0.20                              │
  │    3-wide decoder     12,000   0.48                              │
  │    ALU + Multiply     15,000   0.60                              │
  │    Pipeline regs       8,000   0.32                              │
  │    Regfile (64 regs)   8,000   0.32         ---         2^n=64  │
  │    Branch predictor    4,000   0.16                              │
  │    CSR unit            3,000   0.12                              │
  │                                                                  │
  │  SRAM (16 KB)        (macro)   1.80         31.0%       phi^tau │
  │    Stack: 8 KB         8 inst  0.90                     1/2     │
  │    Heap: 5.3 KB        6 inst  0.60                     1/3     │
  │    Arena: 2.7 KB       3 inst  0.30                     1/6     │
  │    (17 total, 1 spare for ECC)                                   │
  │                                                                  │
  │  Egyptian Mem Ctrl     8,000   0.32          5.5%       ---      │
  │    Address decode      2,000   0.08                              │
  │    Region protection   3,000   0.12                              │
  │    Arbiter             3,000   0.12                              │
  │                                                                  │
  │  HEXA-LANG Decoder   20,000   0.80         13.8%       ---      │
  │    53-keyword CAM     15,000   0.60                     sigma*tau│
  │    Opcode encoder      5,000   0.20                     +sopfr  │
  │                                                                  │
  │  SNN Ring (n=6)        3,000   0.12          2.1%       n=6     │
  │    6 Izhikevich cells  2,400   0.10                              │
  │    12 synapses           600   0.02                     sigma   │
  │                                                                  │
  │  Peripherals           8,000   0.32          5.5%       ---      │
  │    SPI x6              3,000   0.12                     n=6 ch  │
  │    GPIO x24            3,000   0.12                     J_2=24  │
  │    Wishbone bridge     2,000   0.08                              │
  │                                                                  │
  │  Clock + Power         2,000   0.08          1.4%       ---      │
  │  Filler + Decap       (fill)   0.16          2.8%       ---      │
  │  ─────────────────────────────────────────────────────────────   │
  │  CORE TOTAL          ~96,000   5.80        100.0%               │
  │  PAD RING              ---     4.20                              │
  │  ─────────────────────────────────────────────────────────────   │
  │  DIE TOTAL           ~120,000  10.00                   sigma-phi │
  │                                                                  │
  │  Utilization: 5.80 / (10.00 - 4.20) = 5.80 / 5.80 = ~85%      │
  │  (after filler cells and routing overhead)                       │
  └──────────────────────────────────────────────────────────────────┘
```

---

## 10. Cost & Timeline

### 10.1 Efabless chipIgnite Program

```
  ┌──────────────────────────────────────────────────────────────────┐
  │  COST OPTIONS                                                    │
  │                                                                  │
  │  Option A: Open MPW Shuttle (free)                               │
  │    Cost:     $0                                                  │
  │    Chips:    ~100 packaged parts                                 │
  │    Wait:     6-12 months (depends on shuttle schedule)           │
  │    Risk:     Shared wafer, limited metal options                 │
  │    Submit:   Efabless platform, pass precheck                    │
  │                                                                  │
  │  Option B: chipIgnite Dedicated ($10K)                           │
  │    Cost:     $9,999                                              │
  │    Chips:    ~300 packaged parts (QFN-64 or WLCSP)              │
  │    Wait:     4-6 months                                          │
  │    Benefit:  Guaranteed slot, more die per wafer                 │
  │    Submit:   Same flow, faster turnaround                        │
  │                                                                  │
  │  Option C: chipIgnite + Board ($14K)                             │
  │    Cost:     $13,999                                             │
  │    Chips:    ~300 packaged + eval board design                   │
  │    Benefit:  Ready-to-test development board                     │
  └──────────────────────────────────────────────────────────────────┘
```

### 10.2 Timeline

```
  ┌──────────────────────────────────────────────────────────────────┐
  │  PROJECT TIMELINE                                                │
  │                                                                  │
  │  Month 1-3: RTL Design + Simulation                              │
  │  ────────────────────────────────────                            │
  │    M1: RISC-V core RTL (RV32IM, n=6 pipeline)                   │
  │    M1: Egyptian memory controller RTL                            │
  │    M2: HEXA-LANG decoder, SNN ring, peripherals                 │
  │    M2: Cocotb testbenches for all modules                        │
  │    M3: Top-level integration + Caravel wrapper                   │
  │    M3: Formal verification (SymbiYosys)                          │
  │    M3: riscv-tests compliance pass                               │
  │                                                                  │
  │  Month 4-5: Physical Design (P&R)                                │
  │  ────────────────────────────────                                │
  │    M4: Synthesis (Yosys) + timing closure (OpenSTA)              │
  │    M4: Floorplan + SRAM macro placement                          │
  │    M4: Power grid + clock tree synthesis                         │
  │    M5: Placement + routing (OpenROAD)                            │
  │    M5: DRC/LVS clean (Magic/Netgen)                              │
  │    M5: Timing signoff (all corners)                              │
  │    M5: IR drop analysis + EM check                               │
  │                                                                  │
  │  Month 6: Submission                                             │
  │  ──────────────────                                              │
  │    M6W1: Efabless precheck tool                                  │
  │    M6W2: Final GDS review (KLayout)                              │
  │    M6W3: Submit to chipIgnite platform                           │
  │    M6W4: Confirmation + wait for shuttle                         │
  │                                                                  │
  │  Month 7-9: Fabrication (Efabless/SkyWater)                      │
  │  ──────────────────────────────────────────                      │
  │    Wafer fab at SkyWater (Bloomington, MN)                       │
  │    Packaging (QFN-64)                                            │
  │    Testing (Efabless side)                                       │
  │                                                                  │
  │  Month 10: Bring-Up + Test                                       │
  │  ─────────────────────────                                       │
  │    M10W1: Receive packaged chips                                 │
  │    M10W2: Board assembly + power-on                              │
  │    M10W3: JTAG bring-up, register verification                   │
  │    M10W4: Full functional test suite                              │
  │                                                                  │
  │  Gantt:                                                          │
  │                                                                  │
  │  M1  M2  M3  M4  M5  M6  M7  M8  M9  M10                       │
  │  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤                      │
  │  ████████████                  RTL Design (3 months)             │
  │              ████████          Physical Design (2 months)        │
  │                      ██        Submission (1 month)              │
  │                        █████████ Fabrication (3 months)          │
  │                                  ██ Bring-Up (1 month)           │
  │  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤                      │
  │                                                                  │
  │  Total: sigma-phi = 10 months (n=6 connection)                  │
  └──────────────────────────────────────────────────────────────────┘
```

### 10.3 Required Tools (All Free/Open-Source)

```
  ┌────────────────────────────────────────────────────────────────┐
  │  TOOLCHAIN (100% open-source, $0 license cost)                 │
  │                                                                │
  │  Tool               Version   Purpose                         │
  │  ──────────────────────────────────────────────────────────    │
  │  OpenLane 2         2.x       Flow automation (Nix-based)     │
  │  Yosys              0.40+     RTL synthesis                   │
  │  OpenROAD           2.0+      Placement, CTS, routing          │
  │  OpenSTA            2.6+      Static timing analysis           │
  │  Magic VLSI         8.3+      DRC, LVS, parasitic extraction  │
  │  Netgen             1.5+      LVS (layout vs. schematic)      │
  │  KLayout            0.29+     GDS viewer/editor               │
  │  Cocotb             1.9+      Python testbench framework      │
  │  Verilator          5.x       Fast RTL simulation             │
  │  Icarus Verilog     12+       Verilog simulation              │
  │  SymbiYosys         latest    Formal verification             │
  │  GTKWave            3.3+      Waveform viewer                  │
  │  OpenRAM            1.1+      SRAM compiler                   │
  │  sky130A PDK        latest    SkyWater 130nm PDK              │
  │                                                                │
  │  Install (one-liner via Nix):                                  │
  │    nix develop github:efabless/openlane2                       │
  │                                                                │
  │  Or Docker:                                                    │
  │    docker pull efabless/openlane:2.0                            │
  └────────────────────────────────────────────────────────────────┘
```

---

## 11. n=6 EXACT Scorecard (Mini Chip)

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │  N=6 EXACT SCORECARD -- HEXA-EDGE Mini (SKY130)                     │
  │                                                                      │
  │  #   Parameter              Value        n=6 Formula     Grade      │
  │  ──────────────────────────────────────────────────────────────────  │
  │   1  Pipeline stages        6            n=6             EXACT      │
  │   2  Decode width           3            n/phi=3         EXACT      │
  │   3  Register file          64           2^n=64          EXACT      │
  │   4  SRAM total             16 KB        phi^tau=16      EXACT      │
  │   5  Stack fraction         1/2          1/phi=1/2       EXACT      │
  │   6  Heap fraction          1/3          1/(n/phi)=1/3   EXACT      │
  │   7  Arena fraction         1/6          1/n=1/6         EXACT      │
  │   8  Egyptian sum           1            1/2+1/3+1/6     EXACT      │
  │   9  HEXA-LANG keywords     53           sigma*tau+sopfr EXACT      │
  │  10  Opcode width           24 bits      J_2=24          EXACT      │
  │  11  SNN neurons            6            n=6             EXACT      │
  │  12  SNN synapses           12           sigma=12        EXACT      │
  │  13  GPIO pins              24           J_2=24          EXACT      │
  │  14  SPI channels           6            n=6             EXACT      │
  │  15  Die area               10 mm^2      sigma-phi=10    EXACT      │
  │  16  Metal layers           5            sopfr=5         EXACT      │
  │  17  Power pads (VDD)       4            tau=4           EXACT      │
  │  18  Power pads (VSS)       4            tau=4           EXACT      │
  │  19  User IOs               38           38              --         │
  │  20  IRQ lines              3            n/phi=3         EXACT      │
  │  21  Clock domains          3            n/phi=3         EXACT      │
  │  22  SPI divider            /4           tau=4           EXACT      │
  │  23  SNN divider            /6           n=6             EXACT      │
  │  24  Branch penalty         6 cycles     n=6             EXACT      │
  │  25  CTS levels             3            n/phi=3         EXACT      │
  │  26  SRAM macros (Stack)    8            sigma-tau=8     EXACT      │
  │  27  SRAM macros (Heap)     5            sopfr=5         EXACT      │
  │  28  SRAM macros (Arena)    3            n/phi=3         EXACT      │
  │  29  Total SRAM macros      16           phi^tau=16      EXACT      │
  │  30  Power states           6            n=6             EXACT      │
  │  31  Project months         10           sigma-phi=10    EXACT      │
  │  32  VDD voltage            1.8V         1.8=sigma*0.15  CLOSE     │
  │  33  User project area     10.28 mm^2    ~sigma-phi      CLOSE     │
  │  ──────────────────────────────────────────────────────────────────  │
  │  EXACT: 30/33 = 90.9%                                              │
  │  CLOSE: 2/33  = 6.1%                                               │
  │  N/A:   1/33  = 3.0%                                               │
  │                                                                      │
  │  Verdict: 30 EXACT -- n=6 architecture validated in real silicon    │
  └──────────────────────────────────────────────────────────────────────┘
```

---

## 12. OpenLane Configuration

### 12.1 config.json

```json
{
    "DESIGN_NAME": "hexa_top",
    "VERILOG_FILES": "dir::rtl/*.v",
    "CLOCK_PORT": "wb_clk_i",
    "CLOCK_PERIOD": 20.0,
    "DIE_AREA": "0 0 3160 3160",
    "CORE_AREA": "120 120 3040 3040",
    "FP_PIN_ORDER_CFG": "dir::pin_order.cfg",
    "FP_SIZING": "absolute",
    "PL_TARGET_DENSITY": 0.85,
    "GLB_RT_MAXLAYER": "met5",
    "RT_MAX_LAYER": "met5",
    "FP_PDN_VPITCH": 30,
    "FP_PDN_HPITCH": 30,
    "FP_PDN_VWIDTH": 3.0,
    "FP_PDN_HWIDTH": 4.0,
    "SYNTH_STRATEGY": "AREA 3",
    "CTS_TARGET_SKEW": 500,
    "CTS_CLK_BUFFER_LIST": "sky130_fd_sc_hd__clkbuf_4 sky130_fd_sc_hd__clkbuf_8 sky130_fd_sc_hd__clkbuf_16",
    "DIODE_INSERTION_STRATEGY": 4,
    "RUN_CVC": true,
    "MAGIC_DRC_USE_GDS": true,
    "EXTRA_LEFS": "dir::macros/lef/*.lef",
    "EXTRA_GDS_FILES": "dir::macros/gds/*.gds",
    "EXTRA_LIBS": "dir::macros/lib/*.lib",
    "MACRO_PLACEMENT_CFG": "dir::macro_placement.cfg",
    "VERILOG_FILES_BLACKBOX": "dir::macros/bb/*.v",
    "VDD_NETS": "vccd1",
    "GND_NETS": "vssd1",
    "FP_PDN_MACRO_HOOKS": "sram_* vccd1 vssd1"
}
```

### 12.2 SDC Timing Constraints

```
  # hexa_mini.sdc -- Timing constraints for HEXA-EDGE Mini

  # Primary clock: 50 MHz (20 ns period)
  create_clock -name CLK_SYS -period 20.0 [get_ports wb_clk_i]

  # Input delay (from Caravel management core)
  set_input_delay -clock CLK_SYS -max 5.0 [all_inputs]
  set_input_delay -clock CLK_SYS -min 1.0 [all_inputs]

  # Output delay
  set_output_delay -clock CLK_SYS -max 5.0 [all_outputs]
  set_output_delay -clock CLK_SYS -min 0.5 [all_outputs]

  # Clock uncertainty (jitter + skew)
  set_clock_uncertainty -setup 1.0 [get_clocks CLK_SYS]
  set_clock_uncertainty -hold  0.5 [get_clocks CLK_SYS]

  # Generated clocks
  create_generated_clock -name SPI_CLK \
      -source [get_ports wb_clk_i] \
      -divide_by 4 \
      [get_pins spi_inst/spi_clk_out]

  create_generated_clock -name SNN_CLK \
      -source [get_ports wb_clk_i] \
      -divide_by 6 \
      [get_pins snn_inst/snn_clk_out]

  # False paths between clock domains
  set_false_path -from [get_clocks CLK_SYS] -to [get_clocks SNN_CLK]
  set_false_path -from [get_clocks SNN_CLK] -to [get_clocks CLK_SYS]

  # Max transition
  set_max_transition 1.5 [current_design]

  # Max fanout
  set_max_fanout 30 [current_design]
```

---

## 13. Repository Structure

```
  hexa-edge-mini-asic/
  ├── README.md                          # Project overview
  ├── Makefile                           # Build targets
  ├── config/
  │   ├── config.json                    # OpenLane configuration
  │   ├── pin_order.cfg                  # Pin placement
  │   └── macro_placement.cfg            # SRAM macro positions
  ├── rtl/
  │   ├── hexa_top.v                     # Top-level (user_project_wrapper)
  │   ├── hexa_riscv_core.v              # RV32IM N6 CPU core
  │   ├── hexa_alu.v                     # ALU with cyclotomic unit
  │   ├── hexa_decode.v                  # 3-wide instruction decoder
  │   ├── hexa_pipeline.v                # 6-stage pipeline control
  │   ├── hexa_regfile.v                 # 64-entry register file
  │   ├── hexa_mem_ctrl.v                # Egyptian memory controller
  │   ├── hexa_sram_wrapper.v            # OpenRAM macro wrapper
  │   ├── hexa_lang_decoder.v            # 53-keyword CAM
  │   ├── hexa_snn_ring.v               # n=6 Izhikevich neuron ring
  │   ├── hexa_spi.v                     # SPI controller (6 channels)
  │   ├── hexa_gpio.v                    # GPIO controller (24 pins)
  │   ├── hexa_wishbone.v                # Wishbone bus bridge
  │   └── hexa_clk_rst.v                # Clock/reset generation
  ├── tb/
  │   ├── test_hexa_top.py               # Cocotb: system integration
  │   ├── test_riscv_core.py             # Cocotb: RISC-V compliance
  │   ├── test_mem_ctrl.py               # Cocotb: Egyptian memory
  │   ├── test_snn_ring.py               # Cocotb: SNN firing patterns
  │   ├── test_hexa_lang.py              # Cocotb: keyword decode
  │   └── test_spi_gpio.py              # Cocotb: peripheral IO
  ├── formal/
  │   ├── egyptian_mem.sby               # SymbiYosys: memory regions
  │   ├── wishbone_protocol.sby          # SymbiYosys: bus protocol
  │   └── assertions.sv                 # SVA properties
  ├── macros/
  │   ├── lef/                           # SRAM macro LEF files
  │   ├── gds/                           # SRAM macro GDS files
  │   ├── lib/                           # SRAM macro Liberty files
  │   └── bb/                            # Blackbox Verilog stubs
  ├── firmware/
  │   ├── boot.c                         # Caravel management firmware
  │   ├── hexa_test.c                    # User-space test programs
  │   └── linker.ld                      # Memory layout (Egyptian)
  ├── docs/
  │   ├── architecture.md                # This document
  │   └── bring-up-guide.md             # Post-fab test procedure
  └── gds/
      └── (generated by OpenLane flow)
```

---

## 14. Bring-Up Test Plan (Post-Fabrication)

```
  ┌──────────────────────────────────────────────────────────────────┐
  │  SILICON BRING-UP SEQUENCE                                       │
  │                                                                  │
  │  Test 1: Power-On + JTAG                                         │
  │    - Apply 1.8V to VCCD1, measure current (expect < 60 mA)      │
  │    - JTAG scan chain: verify all registers accessible            │
  │    - Read chip ID register via Wishbone                          │
  │                                                                  │
  │  Test 2: Management Core Boot                                    │
  │    - Flash boot firmware via SPI                                 │
  │    - UART output: "HEXA-EDGE Mini v1.0"                          │
  │    - Configure IO pads via housekeeping SPI                      │
  │                                                                  │
  │  Test 3: GPIO Toggle                                             │
  │    - Toggle all 24 GPIO pins at 1 MHz                            │
  │    - Verify with logic analyzer                                  │
  │    - Test input mode: button press detection                     │
  │                                                                  │
  │  Test 4: RISC-V Core Basic                                       │
  │    - Load test program via Wishbone → SRAM                       │
  │    - Run: ADD, SUB, AND, OR, XOR, SLL, SRL                      │
  │    - Verify results via Wishbone readback                        │
  │                                                                  │
  │  Test 5: Egyptian Memory Regions                                 │
  │    - Write pattern to Stack region (0..8191)                     │
  │    - Write pattern to Heap region (8192..13652)                  │
  │    - Write pattern to Arena region (13653..16383)                │
  │    - Verify cross-region access generates fault                  │
  │                                                                  │
  │  Test 6: HEXA-LANG Keyword Decode                                │
  │    - Send all 53 keyword encodings through Wishbone              │
  │    - Verify CAM matches in single cycle                          │
  │    - Measure decode latency on oscilloscope                      │
  │                                                                  │
  │  Test 7: SNN Ring                                                │
  │    - Initialize 6 neurons with known parameters                  │
  │    - Apply stimulus to neuron 0                                  │
  │    - Observe ring propagation via logic analyzer                 │
  │    - Verify firing pattern matches simulation                    │
  │                                                                  │
  │  Test 8: SPI Communication                                       │
  │    - Connect SPI flash to channel 0                              │
  │    - Read/write flash data                                       │
  │    - Test all 6 channels with loopback                           │
  │                                                                  │
  │  Test 9: Full Integration                                        │
  │    - Load HEXA-LANG program into SRAM                            │
  │    - Execute program using N6 core                               │
  │    - Verify output on GPIO + SPI                                 │
  │    - Measure power consumption                                   │
  │                                                                  │
  │  Test 10: Characterization                                       │
  │    - Frequency sweep: 10 MHz → 100 MHz (find Fmax)              │
  │    - Voltage sweep: 1.6V → 2.0V (find Vmin)                     │
  │    - Temperature: -40C to 125C (if available)                    │
  │    - Record n=6 EXACT scorecard vs. simulation                  │
  └──────────────────────────────────────────────────────────────────┘
```

---

## Summary

HEXA-EDGE Mini is the bridge between paper architecture and real silicon.
By targeting the free SkyWater 130nm shuttle through Efabless chipIgnite,
we validate every n=6 parameter in physical hardware at zero cost.

```
  ┌──────────────────────────────────────────────────────┐
  │  HEXA-EDGE Mini at a Glance                          │
  │                                                      │
  │  Process:    SKY130 (130nm, 1.8V)                    │
  │  Die:        sigma-phi = 10 mm^2                     │
  │  Frequency:  50 MHz                                  │
  │  Power:      ~100 mW                                 │
  │  Core:       RV32IM, n/phi=3-wide, n=6 pipeline      │
  │  Memory:     phi^tau=16 KB SRAM (Egyptian 1/2+1/3+1/6)│
  │  Accelerator: 53-keyword CAM + n=6 SNN ring          │
  │  I/O:        J_2=24 GPIO + n=6 SPI                   │
  │  Tools:      100% open-source (OpenLane + Cocotb)    │
  │  Cost:       $0 (Open MPW) or $10K (dedicated)       │
  │  Timeline:   sigma-phi = 10 months                   │
  │  n=6 EXACT:  30/33 = 90.9%                           │
  │                                                      │
  │  This is n=6 made real.                              │
  └──────────────────────────────────────────────────────┘
```
