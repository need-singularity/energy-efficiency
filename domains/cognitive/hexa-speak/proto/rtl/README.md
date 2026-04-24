# N6-SPEAK v2 — RTL 4-tier block (CHIP-P1-1)

- Version: v2.0-frozen (2026-04-14)
- Upstream spec: `../n6-speak-v2-spec.md` (158-line frozen spec)
- Upstream design: `../../hexa-speak.md` (§1 to §15)
- Roadmap: `CHIP-P1-1` (n6-architecture.json)

## Overview

A collection of `.hexa` blocks describing the 4 tiers of the N6-SPEAK v2 hardware pipeline at pseudo-RTL level. Before actual Verilog synthesis, the n=6 arithmetic consistency and port-I/F consistency are pre-verified via `hexa parse` + `hexa run`. Each block maps 1:1 to the 4 partitions of the Xn6 NPU, and the top-level `top.hexa` joins the 4 blocks + fusion interposer into a single data path.

## File structure

| File                      | tier  | Role                                      | Lines | Tests |
|---------------------------|-------|-------------------------------------------|-------|-------|
| `intent_encoder.hexa`     | 1     | tokens -> 384d embedding                  | 147   | 5/5   |
| `emotion_classifier.hexa` | 2a    | embedding -> 6 emotion logits (Ekman set) | 157   | 5/5   |
| `prosody_shaper.hexa`     | 2b    | embedding -> 4 prosody (pitch/dur/ene/spec) | 170 | 5/5   |
| `rvq_codec.hexa`          | 3     | 8-stage RVQ (codebook 1024, 2^10)         | 203   | 5/5   |
| `top.hexa`                | 1~3   | 4 blocks + fusion interposer top-level wrapper | 340 | 7/7 |

Total 5 files. All `.hexa` blocks round-trip PASS on `hexa parse` + `hexa run`.

## 4-tier data path

```
                          intent_in[384]
                                |
                                v
                    +-----------------------+
                    | tier-1 intent_encoder |  Xn6 NPU-part-1
                    |  384d = sigma*tau*8   |
                    +---------+-------------+
                              | embed_sum
                  +-----------+------------+
                  v                        v
          +---------------+        +---------------+
          | tier-2a       |        | tier-2b       |  Xn6 NPU-part-2
          | emotion_cls   |        | prosody_shape |
          | 6 = sopfr+1   |        | 4 = tau(6)    |
          +-------+-------+        +-------+-------+
                  | emo_id                 | pros_sum
                  +------------+-----------+
                               v
                    +----------------------+
                    | tier-2c fusion (top) |
                    | h = phi*embed +      |
                    |     emo*sigma +      |
                    |     pros*tau         |
                    | 768 = 2*384          |
                    +----------+-----------+
                               | h_sum
                               v
                    +----------------------+
                    | tier-3 rvq_codec     |  Xn6 NPU-part-3
                    | 8 stages x 1024 cb   |
                    +----------+-----------+
                               |
                               v
                         audio_out[8]
```

Top-level port: `{intent_in[384], audio_out[8]}` — `top.hexa::top_forward(intent_in, t) -> audio_out`.

## Per-block port I/F

### tier-1 intent_encoder.hexa

```
fn forward(token_id: i64, pos: i64, batch_idx: i64) -> i64   // embed_sum
fn forward_sequence(seq_len: i64) -> i64                      // T-timestep sum
```

- Input shape: `tokens[B,T]`  (sim: scalar token_id + pos)
- Output shape: `embed[B,T,384]`  (sim: i64 checksum)
- Parameters: vocab=32768=2^15, dim=384=sigma*tau*8
- FP16 bias: `+sigma(6)*dim = +12*384`
- Pseudo-HW: BRAM row lookup + adder tree

### tier-2a emotion_classifier.hexa

```
fn logit_for_emo(embed_sum: i64, emo: i64) -> i64
fn forward(embed_sum: i64) -> i64                             // argmax 0~5
fn emo_name(idx: i64) -> i64                                  // console label
```

- Input shape: `embed[B,384]`
- Output shape: `logits[B,6]` -> argmax scalar
- Emotion indices: `0=neutral 1=joy 2=anger 3=sadness 4=fear 5=surprise`
- Arithmetic rationale: `emo_cnt = sopfr(6)+1 = 5+1 = 6`
- Pseudo-HW: 6-way parallel MAC + argmax tree

### tier-2b prosody_shaper.hexa

```
fn prosody_channel(embed_sum: i64, p: i64, t: i64) -> i64
fn forward(embed_sum: i64, t: i64) -> i64                     // sum of 4 channels
fn forward_sequence(embed_sum_base: i64, seq_len: i64) -> i64
```

- Input shape: `embed[B,T,384]`
- Output shape: `prosody[B,T,4]`
- Channels: `0=pitch 1=duration 2=energy 3=spectral`
- Arithmetic rationale: `prosody_cnt = tau(6) = 4`, per-head = `768/tau = 192`
- Pseudo-HW: tau=4 FFN expansion + sigmoid scale [0,1000]

### tier-3 rvq_codec.hexa

```
fn quantize_one_stage(residual: i64, stage: i64, codebook_sz: i64) -> i64
fn decode_code(code_idx: i64, stage: i64, codebook_sz: i64) -> i64
fn encode(feat_sum: i64) -> i64                               // sum of 8 codes
fn decode(codes_sum: i64, stages: i64) -> i64                 // feat reconstruction
fn forward(feat_sum: i64) -> i64                              // loopback check
fn compression_ratio() -> i64                                 // = 153
```

- Input shape: `h[B,T,768]`
- Output shape: `codes[B,T,8]` -> reconstruct `feat[B,T,768]`
- stages: `sigma(6)-tau(6) = 12-4 = 8`
- codebook size: `2^(sigma-phi) = 2^10 = 1024`
- Compression ratio: `768*2 / (8*10/8) = 1536/10 = 153x`
- Pseudo-HW: BRAM codebook x 8 + residual subtractor

### tier-2c fusion interposer (embedded in top.hexa)

```
fn fusion_forward(embed_sum: i64, emo_id: i64, pros_sum: i64) -> i64
```

- Inputs: 3 streams (embed 384 + emo 1 + prosody 4)
- Output: `h[B,T,768]`  (sim checksum)
- Arithmetic: `h = phi(6)*embed + emo*sigma(6)*256 + pros*tau(6)`
- Consistency: `768 = 2*384 = phi*sigma*tau*16` (spec §5.2)

## Port / clock domain consistency

| Item                 | Basis                               | Status |
|----------------------|-------------------------------------|--------|
| Inter-block bus signal | checksum `i64` (embed/h/codes)     | consistent |
| Timestep meaning     | `t` = token index / pos synonym     | consistent |
| Batch axis           | B (omitted, single-stream assumed)  | consistent |
| Clock domain         | single (pipe depth tau=4)           | consistent |
| bit-width            | FP16 (tier 1/2) / INT8 (tier 3/4)   | conforms to spec §2 |

`top.hexa` acts as an interposer between tiers and reproduces the `forward`-corresponding logic of the 4 blocks via namespace prefixes (`intent_` / `emo_` / `pros_` / `rvq_`). Because the hexa language does not provide module import, this is a single-file full-stack configuration. Each original block file remains standalone `hexa run`-capable.

## Synthesizability check

| File                      | `hexa parse` | `hexa run` | Notes                   |
|---------------------------|--------------|-----------|-------------------------|
| intent_encoder.hexa       | OK           | exit=0    | 5/5 tests PASS          |
| emotion_classifier.hexa   | OK           | exit=0    | 5/5 tests PASS          |
| prosody_shaper.hexa       | OK           | exit=0    | 5/5 tests PASS          |
| rvq_codec.hexa            | OK           | exit=0    | 5/5 tests PASS          |
| top.hexa                  | OK           | exit=0    | 7/7 tests PASS          |

Total 27/27 embedded tests PASS. lint/parse/run round-trip all pass. However, Verilog RTL translation and actual standard-cell synthesis (Synopsys DC / Cadence Genus) are deferred to the follow-on stage CHIP-P2-1 (SoC integration + DRC/LVS).

## Top-level run example

```bash
cd /Users/ghost/Dev/n6-architecture/domains/cognitive/hexa-speak/proto
hexa parse rtl/top.hexa   # OK: rtl/top.hexa parses cleanly
hexa run   rtl/top.hexa   # exit 0 -> 7/7 PASS
```

`top.hexa::top_run_sequence(24)` runs the whole pipeline for T=24=J2 timesteps, traversing the 4 blocks + fusion + RVQ in a single pipe.

## n=6 consistency summary

```
sigma(6) = 12   tau(6) = 4   phi(6) = 2   sopfr(6) = 5
sigma*phi = n*tau = 12   (Bilateral draft B, n=6 uniqueness candidate)

intent dim    = sigma*tau*8     = 384
emo count     = sopfr+1         = 6      (Ekman)
prosody count = tau             = 4
fusion dim    = 2*384           = 768
RVQ stages    = sigma-tau       = 8
codebook sz   = 2^(sigma-phi)   = 1024
pipe depth    = tau             = 4
```

The 4 blocks + fusion interposer + top.hexa are all fixed on a single arithmetic-consistency axis (n=6 perfect number).

## Follow-on work

- CHIP-P1-2: 12-protocol expansion
- CHIP-P2-1: N6-SPEAK v2 SoC integration (DRC/LVS PASS) — trigger for Verilog conversion of these RTL blocks
- CHIP-P3-x: Xn6 NPU 4-partition realization + benchmark
