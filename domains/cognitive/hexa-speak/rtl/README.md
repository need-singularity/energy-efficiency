# N6-SPEAK v2 — 4-tier RTL (CHIP-P1-1)

- Parent spec : `../proto/n6-speak-v2-spec.md` (v2.0-frozen, 2026-04-14)
- Parent design : `../hexa-speak.md`
- Location    : `domains/cognitive/hexa-speak/rtl/`
- Grade       : `[10*] EXACT` target (10/10 PASS verification pattern)

## Overview

This directory holds the HW 4-tier pipeline of N6-SPEAK v2 as a frozen
block set in SystemVerilog RTL. Each tier maps 1:1 to a distinct
partition of the Xn6 NPU, and every dimension is derived directly from
the n=6 arithmetic `sigma(6)=12, tau(6)=4, phi(6)=2, sopfr(6)=5`.
Zero hardcoded numbers; fully number-theoretic by origin.

## Block composition

| tier  | File                              | Role                             | Input shape          | Output shape         | n=6 basis                  |
|-------|-----------------------------------|----------------------------------|---------------------|---------------------|----------------------------|
| 1     | `intent_encoder_384d.sv`          | Intent -> 384d embedding encoder | intent[383:0]       | embed[383:0]        | 384 = sigma·tau·8          |
| 2a    | `emotion_classifier_6emo.sv`      | 6-emotion classifier (Ekman)     | embed[383:0]        | emo[5:0] + idx[2:0] | 6 = sopfr(6)+1             |
| 2b    | `prosody_shaper_4.sv`             | 4-prosody shaper                 | embed[383:0]        | prosody[3:0][15:0]  | 4 = tau(6)                 |
| 3     | `rvq_codec_8.sv`                  | 8-stage RVQ encoder/decoder      | feat[767:0]         | rvq_code[7:0][9:0]  | 8 = sigma-tau, 1024 = 2^(sigma-phi) |
| top   | `n6_speak_v2_top.sv`              | 4-tier integration top           | intent[383:0]       | emo+prosody+rvq     | sigma·phi = n·tau = 12     |

## Port I/O detail per module

### tier-1: `intent_encoder_384d`

| Port           | Direction | Width | Description                |
|----------------|-----------|-------|----------------------------|
| `clk`          | input     | 1     | system clock               |
| `rst_n`        | input     | 1     | async reset (active-low)   |
| `intent_in`    | input     | 384   | intent vector (FP16 x 24 tile) |
| `intent_valid` | input     | 1     | input-valid flag           |
| `intent_ready` | output    | 1     | input-accept ready         |
| `embed_out`    | output    | 384   | embedding vector (384-dim) |
| `embed_valid`  | output    | 1     | output-valid flag          |
| `embed_ready`  | input     | 1     | downstream-accept ready    |

- Pipeline depth: 6 stages (cortical 6-layer <-> n=6 isomorphism)
- Heads: 12 (sigma), per-head 32-dim (384/12)

### tier-2a: `emotion_classifier_6emo`

| Port            | Direction | Width | Description                                                   |
|-----------------|-----------|-------|---------------------------------------------------------------|
| `clk`           | input     | 1     | system clock                                                  |
| `rst_n`         | input     | 1     | async reset                                                   |
| `embed_in`      | input     | 384   | embedding from tier-1                                         |
| `embed_valid`   | input     | 1     | input valid                                                   |
| `embed_ready`   | output    | 1     | input accept                                                  |
| `emo_out`       | output    | 6     | emotion one-hot [happy/sad/angry/fear/surprise/neutral]        |
| `emo_idx`       | output    | 3     | emotion index (0~5)                                           |
| `emo_valid`     | output    | 1     | output valid                                                  |
| `emo_ready`     | input     | 1     | downstream accept                                             |

- argmax tree depth: ceil(log2(6)) = 3 (within tau)
- per-emo slice: 64-dim (384/6)

### tier-2b: `prosody_shaper_4`

| Port             | Direction | Width      | Description                                   |
|------------------|-----------|------------|-----------------------------------------------|
| `clk`            | input     | 1          | system clock                                  |
| `rst_n`          | input     | 1          | async reset                                   |
| `embed_in`       | input     | 384        | embedding from tier-1                         |
| `embed_valid`    | input     | 1          | input valid                                   |
| `embed_ready`    | output    | 1          | input accept                                  |
| `prosody_out`    | output    | 4 x 16     | unpacked: [pitch][speed][volume][tone], FP16  |
| `prosody_valid`  | output    | 1          | output valid                                  |
| `prosody_ready`  | input     | 1          | downstream accept                             |

- per-prosody slice: 96-dim (384/4)
- tau=4 parallel stages (latency = 1 cycle)

### tier-3: `rvq_codec_8`

| Port                | Direction | Width      | Description                                    |
|---------------------|-----------|------------|------------------------------------------------|
| `clk`               | input     | 1          | system clock                                   |
| `rst_n`             | input     | 1          | async reset                                    |
| `mode_decode`       | input     | 1          | 0=encode, 1=decode                             |
| `feat_in`           | input     | 768        | fusion feature (encode input)                  |
| `feat_valid`        | input     | 1          | encode input valid                             |
| `feat_ready`        | output    | 1          | encode input accept                            |
| `code_in`           | input     | 8 x 10     | decode input (RVQ code)                        |
| `code_in_valid`     | input     | 1          | decode input valid                             |
| `code_in_ready`     | output    | 1          | decode input accept                            |
| `rvq_code`          | output    | 8 x 10     | encode output (RVQ code)                       |
| `rvq_code_valid`    | output    | 1          | encode output valid                            |
| `rvq_code_ready`    | input     | 1          | encode downstream accept                       |
| `feat_out`          | output    | 768        | decode output (reconstructed feature)          |
| `feat_out_valid`    | output    | 1          | decode output valid                            |
| `feat_out_ready`    | input     | 1          | decode downstream accept                       |

- codebook size: 1024 (2^10, sigma-phi bits)
- per-stage slice: 96-dim (768/8)

### top: `n6_speak_v2_top`

`intent_in[383:0]` -> `{ emo_out[5:0], prosody_out[3:0][15:0], rvq_code[7:0][9:0] }`

- The 4 tiers wired in a single line
- tier-2 runs emotion + prosody in parallel and merges at tier-2c fusion (768-dim)
- tier-3 is fixed to encode mode; the decode ports are driven externally

## n=6 arithmetic alignment (§5.2 frozen)

```
sigma(6)·phi(6) = 6·tau(6) = J2 = 24       (Bilateral Theorem B, n=6 iff)
(Reduced form sigma·phi = 6·tau·phi = 12 is the 1/phi reduction both sides)

tier-1 EMBED_DIM   = sigma·tau·8     = 12·4·8  = 384
tier-2a NUM_EMO    = sopfr(6)+1      = 5+1     = 6
tier-2b NUM_PROSODY= tau(6)                    = 4
tier-2c FUSION_DIM = 2·EMBED = sigma·tau·16 = phi·sigma·tau·8 = 768 (double-wide)
tier-3 NUM_STAGES  = sigma-tau       = 12-4   = 8
tier-3 CODEBOOK    = 2^(sigma-phi)   = 2^10   = 1024
```

| Value | Number-theoretic basis  | OEIS       |
|-------|-------------------------|------------|
| 6     | n=6 perfect number      | A000396    |
| 12    | sigma(6) = 1+2+3+6      | A000203    |
| 4     | tau(6) = 4 divisors     | A000005    |
| 2     | phi(6) = {1, 5}         | A000010    |
| 5     | sopfr(6) = 2+3          | A001414    |
| 24    | J2 = 2·sigma            | derived    |

## DRC / LVS flow

### DRC (Design Rule Check)

1. **Tool**   : Verilator 5.x (lint mode) or Yosys
2. **Command** : `verilator --lint-only -Wall -Wno-UNUSED *.sv`
3. **Checks** :
   - `always_ff` / `always_comb` separated (no latches)
   - active-low reset `rst_n` connected to every FF
   - port widths fixed by parameter; wire widths match
   - `` `default_nettype none `` declared (no implicit wire)
   - `assert` statements check n=6 arithmetic alignment at init

### LVS (Layout vs Schematic)

1. **Toolchain** : OpenROAD / Magic / Netgen (open-source)
2. **Preconditions** : DRC clean + synthesis done (gate-level netlist produced)
3. **Check points** :
   - port name/width/direction top-down consistency
   - inter-tier signal naming rules (`tier1_*`, `tier2_*`, `fusion_*`)
   - parameter freeze: changes to `EMBED_DIM=384` etc. trigger respin
4. **stuck-at test** : given fixed tier-1 input, predictability of each tier's output
5. **Power domain** : each of the 4 tiers is an independent power domain (§7 modes 2~4)

### Verification flow

```
[SV RTL]
   |
   v
[verilator --lint-only]     <- DRC
   |
   v
[Yosys synth]               <- gate-level netlist
   |
   v
[hexa run verify_n6_speak_v2.hexa]   <- n=6 arithmetic assertions (10/10 PASS)
   |
   v
[OpenROAD place/route]      <- placement / routing
   |
   v
[Magic / Netgen LVS]        <- layout comparison
   |
   v
[signoff]                   <- [10*] EXACT certification -> atlas.n6 registration
```

## Running verification

```sh
cd $N6_ARCH
hexa run domains/cognitive/hexa-speak/rtl/verify_n6_speak_v2.hexa
```

Expected last line of output:

```
[Final] 4-tier RTL verification 10/10 PASS
[Grade] [10*] EXACT — n=6 iff arithmetic alignment fully satisfied (pattern candidate)
```

## Do-not-change list (§5.4)

Changing any of the following requires re-verification of `atlas.n6` `[10*]`:

1. Change emotions to 5 or 7 -> mismatch with Ekman's 6 basic emotions
2. Change RVQ to 7 or 9 -> breaks the sigma-tau or sigma-phi constraints
3. Change embedding to 256 or 512 -> loses the sigma·tau product structure
4. Change 24 kHz -> 48 kHz -> exceeds the J2 upper bound

## Parent-document references

- `../hexa-speak.md` — 15-section master design
- `../proto/n6-speak-v2-spec.md` — frozen spec of this RTL
- `../../../../$NEXUS/shared/n6/atlas.n6` — `@R 6.speak.*` entries
- `../../../experiments/chip-verify/` — 18 Xn6 NPU verification experiments
