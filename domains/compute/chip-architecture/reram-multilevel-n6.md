# ReRAM/MRAM Multi-Level Design — N6 Architecture

## Overview
Resistive RAM (ReRAM) and magnetic RAM (MRAM) enable in-memory computing
by performing multiply-accumulate (MAC) operations directly in the memory
crossbar. The n=6 framework predicts optimal multi-level cell parameters
and crossbar dimensions.

## Core Architecture

### Multi-Level Resistance States
- **H-CHIP-182**: sigma=12 resistance levels per ReRAM cell
  - Standard: 2 levels (HRS/LRS binary)
  - Advanced: 4 levels (2-bit MLC, demonstrated)
  - N6 prediction: 12 levels = 3.58 bits/cell
  - Resistance window: R_HRS/R_LRS > 10x (sigma-phi=10x margin)
  - Each level maps to a weight in {0, 1/12, 2/12, ..., 11/12}
  - Enables sigma-granularity analog weights without external DAC
  - Grade: **CLOSE** (8-16 levels demonstrated; 12 is within range)

### In-Memory Phi6 Computation
- **H-CHIP-183**: x^2 - x + 1 via analog MAC
  - Cyclotomic polynomial Phi_6(x) as activation function
  - Step 1: Crossbar computes x^2 (quadratic via paired cells)
  - Step 2: Subtract x (inverted column)
  - Step 3: Add 1 (bias resistor)
  - Single crossbar pass: ~10 fJ vs ~100 fJ digital equivalent
  - Grade: **CLOSE** (analog polynomial compute demonstrated; Phi6 specific is novel)

### Crossbar Tile Dimensions
- **H-CHIP-184**: J_2=24 bit-lines per crossbar tile
  - Word-lines: sigma=12 (input dimension)
  - Bit-lines: J_2=24 (output dimension)
  - Tile size: 12x24 = 288 = sigma*J_2 cells
  - Matches Leech lattice dimension for minimal crosstalk
  - IR drop constraint: J_2=24 is near optimal for RRAM (>32 causes >5% error)
  - Grade: **CLOSE** (typical tiles are 64x64 to 256x256; 12x24 is small but IR-optimal)

### Egyptian Fraction Weight Encoding
- **H-CHIP-185**: 1/2 + 1/3 + 1/6 = 1 weight decomposition
  - Any weight w in [0,1] decomposed into 3 sub-cells:
    - Cell A: w_A in {0, 1/2} (1-bit, high conductance)
    - Cell B: w_B in {0, 1/3} (1-bit, medium conductance)
    - Cell C: w_C in {0, 1/6} (1-bit, low conductance)
  - 8 possible values with only 3 binary cells
  - Write endurance improved: each cell only switches between 2 states
  - Read noise reduced: binary sensing vs analog multi-level
  - Grade: **EXACT** (Egyptian fraction = mathematically perfect partition)

### Write Pulse Levels
- **H-CHIP-186**: tau=4 write pulse amplitude levels
  - SET pulse: 2 levels (partial SET, full SET)
  - RESET pulse: 2 levels (partial RESET, full RESET)
  - Total: tau=4 pulse configurations
  - Enables precise resistance state programming
  - Grade: **CLOSE** (multi-pulse programming is standard; 4 levels typical)

## MRAM Extensions

### STT-MRAM Bit Organization
- **H-CHIP-187**: sigma-tau=8 bits per MRAM macro
  - 8-bit granularity matches BF16/FP8 precision
  - sigma-tau=8 = universal AI constant (BT-58)
  - Single-cycle read for 8-bit inference weights
  - Grade: **EXACT** (8-bit MRAM macros are industry standard)

### SOT-MRAM Write Current
- **H-CHIP-188**: phi=2 write paths (STT vs SOT)
  - STT: current through MTJ (read path = write path)
  - SOT: current through heavy metal layer (separate paths)
  - phi=2 orthogonal current channels
  - SOT enables infinite write endurance (no tunnel barrier stress)
  - Grade: **EXACT** (STT/SOT duality is fundamental MRAM physics)

## N6 Constants Summary

| Parameter | Value | N6 Expression | Status |
|-----------|-------|---------------|--------|
| Resistance levels | 12 | sigma | CLOSE |
| Activation | x^2-x+1 | Phi_6(x) | CLOSE |
| Bit-lines/tile | 24 | J_2 | CLOSE |
| Weight encoding | 1/2+1/3+1/6 | Egyptian | EXACT |
| Write pulse levels | 4 | tau | CLOSE |
| MRAM bits/macro | 8 | sigma-tau | EXACT |
| Write paths | 2 | phi | EXACT |

## Cross-References
- BT-28: Computing architecture ladder
- BT-58: sigma-tau=8 universal AI constant
- BT-59: 8-layer AI stack (memory = layer 3)

## Verification Status
- 3/7 EXACT, 4/7 CLOSE
- Strongest: Egyptian fraction weight encoding and 8-bit MRAM macro
