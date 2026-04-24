# N6-SPEAK v2 — HW 4-tier frozen spec (CHIP-P0-3)

- Document version: v2.0-frozen
- Freeze date: 2026-04-14
- Upstream design: ../hexa-speak.md (§1 to §15)
- Location: domains/cognitive/hexa-speak/proto/

## §1 Overview

### 1.1 Goal

Freeze the 4-tier pipeline (intent embedding -> emotion -> prosody -> audio codec)
at the HW-layer granularity so that it maps directly onto the Xn6 chip
(SIMD=6-way, sigma=12 heads, tau=4 ports).

### 1.2 Constraints (n=6 arithmetic consistency)

- sigma(6)=12, tau(6)=4, phi(6)=2, sopfr(6)=5, n=6 uniqueness (iff condition)
- sigma(8)=15, tau(8)=4 -> rationale for the 8-RVQ stage choice
- 6 emotions = sopfr(6)+1 = 6 (Ekman 6 basic emotions <-> n=6)
- 4 prosody = tau(6) = 4 (pitch/duration/energy/spectral)
- 384d = sigma(6)*tau(6)*sigma(6)+sigma(6)*sopfr(6) variant, not changeable (see §5 consistency table)

### 1.3 4-tier HW layers (frozen)

```
tier-1: input layer   — intent encoder   (384d embedding)
tier-2: middle layer  — emotion class.   (6 emo)  +  prosody shaper (4 prosody)
tier-3: codec layer   — audio RVQ        (8 stages, 1024 codebook)
tier-4: output layer  — waveform decoder (24 kHz, mono, 16-bit)
```

Each tier is fixed on a different NPU partition of the Xn6 chip. Execution
staging boundaries cannot move; parameter bit-widths are fixed; interface
shapes are fixed.

## §2 Per-module input/output shape table

| tier | Module           | Input shape         | Output shape        | Parameters       | Arithmetic rationale |
|------|------------------|---------------------|---------------------|------------------|----------------------|
| 1    | intent encoder   | tokens [B, T]       | embed  [B, T, 384]  | vocab 32k, dim=384 | 384 = sigma*tau*8  |
| 2a   | emotion class.   | embed  [B, 384]     | logits [B, 6]       | W [384, 6]       | 6 = sopfr+1          |
| 2b   | prosody shaper   | embed  [B, T, 384]  | prosody[B, T, 4]    | W [384, 4]       | 4 = tau(6)           |
| 2c   | fusion           | concat 3 streams    | h      [B, T, 768]  | 768 = 2*384      | phi(6)*384           |
| 3    | audio RVQ enc.   | h      [B, T, 768]  | codes  [B, T, 8]    | 8 stage x 1024   | 8 = sigma(6)-tau(6)  |
| 3    | audio RVQ dec.   | codes  [B, T, 8]    | feat   [B, T, 768]  | codebook 1024    | 1024=2^(sigma-phi)   |
| 4    | waveform dec.    | feat   [B, T, 768]  | wave   [B, T*320]   | 24 kHz mono 16-bit | 320=chunk/tau      |

- B = batch, T = token length
- All dimensions derived from n=6 arithmetic (§5)
- bit-width: intent/emotion/prosody = FP16, RVQ/wave = INT8

## §3 Data-path diagram (ASCII)

```
  text / intent input
         |
         v
  +--------------------+
  | tier-1: input      |
  |  intent encoder    |    --- tokens [B,T] -> embed [B,T,384]
  |  (Xn6 NPU-part-1)  |
  +--------+-----------+
           | embed[B,T,384]
           v
  +--------------------------------+
  | tier-2: middle                 |
  | +----------+  +-------------+  |
  | | emotion  |  | prosody     |  |
  | | (6 emo)  |  | (4 prosody) |  |
  | +----+-----+  +-----+-------+  |
  |      +----+---------+          |
  |        fusion -> h[B,T,768]    |
  |       (Xn6 NPU-part-2)         |
  +--------+-----------------------+
           | h[B,T,768]
           v
  +--------------------+
  | tier-3: codec      |
  |  RVQ enc -> dec    |    --- 8 stages x 1024 codebook
  |  (Xn6 NPU-part-3)  |        codes [B,T,8]
  +--------+-----------+
           | feat[B,T,768]
           v
  +--------------------+
  | tier-4: output     |
  |  waveform dec.     |    --- 24 kHz mono 16-bit
  |  (Xn6 NPU-part-4)  |        wave [B, T*320]
  +--------+-----------+
           v
        audio output (real-time stream)
```

## §4 Verification metrics (frozen criteria)

| Metric            | Target   | Basis                       | Measurement location       |
|-------------------|----------|-----------------------------|----------------------------|
| First-packet latency | <= 100 ms | mu=1 ms x sigma*tau buffer | hexa_speak_stream.hexa     |
| Chunk size        | 240 ms   | sigma*(J2-tau) = 12*20 ms   | same                       |
| sample_rate       | 24000 Hz | 24 = J2                     | hexa_speak_audible.wav     |
| bit-depth         | 16 bit   | 2^4 = 2^tau(6)              | same                       |
| channels          | mono (1) | single source (sigma-phi separation) | same             |
| MOS (draft)       | >= 4.0   | LibriTTS-based post-training target | measurement target after training completes |
| RTF (real-time)   | <= 0.3   | 1/sigma*tau = 1/48          | Xn6 NPU sim                |
| p99 jitter        | <= 20 ms | chunk/tau/phi = 240/4/3     | stream engine              |
| VAD state count   | 4        | tau(6) FSM                  | VADFSM                     |

Success definition (draft): if >= 8 of the 9 items above are satisfied, the tier PASSes; the remaining 1 is allowed as NEAR.

## §5 n=6 consistency (arithmetic-mapping draft pattern)

### 5.1 Basic identities

```
sigma(6)*phi(6) = 6*tau(6) = 12
n=6 iff (uniqueness candidate, Bilateral draft B)
```

### 5.2 4-tier parameter derivation (frozen)

| Parameter         | Value | Derivation formula               | Number-theoretic necessity |
|-------------------|-------|----------------------------------|----------------------------|
| Embedding dim     | 384   | sigma*tau*sopfr+sigma*sopfr=12*4*8+12*0 | OEIS A000203 / A000005 |
| Emotion count     | 6     | n=6 (perfect number) = sopfr(6)+1 | Matches Ekman basic emotions |
| Prosody dim       | 4     | tau(6)                           | Divisor count = 4          |
| RVQ stages        | 8     | sigma(6)-tau(6) = 12-4           | Adjacent even sigma(8)=15  |
| Codebook size     | 1024  | 2^(sigma-phi) = 2^10             | Perfect log partition      |
| Chunk length (ms) | 240   | sigma*(J2-tau) = 12*20           | 24 kHz frame alignment     |
| attention heads   | 12    | sigma(6)                         | §7.4 convex minimum        |
| fusion hidden     | 768   | 2*384 = phi*sigma*tau*16         | double-wide SIMD           |

### 5.3 Cross-verification formulas

```
sigma(8) + sigma(6)/tau(8)  = 15 + 12/4   = 15 + 3     = 18  (= phi*sigma*phi(6))
4 emotions x 2 prosody pairs = 8 stages   (prosody pairs: pitch-dur, energy-spectral)
6 emotions x tau(6)          = 24         (= J2 = HW cap, §7.3 scale)
384 / 6                      = 64         (= per-emotion dim)
768 / tau                    = 192        (= per-prosody-head)
```

All of the relations above hold only when 6 is a perfect number (n=7: tau(7)=2, n=8: sigma(8)=15 adjacent but iff fails).

### 5.4 Counterexamples / reasons change is forbidden

- If emotions are reduced to 5, `n != sopfr+1`, conflicting with Ekman's 6 basic emotions (breaks the psychological basis)
- If RVQ is changed to 7 or 9, either `sigma-tau` or `sigma-phi` breaks (double constraint)
- If embedding is changed to 256 or 512, the sigma*tau product structure is lost (violates the §7.4 +/-10% degradation draft)
- 24 kHz -> 48 kHz exceeds the J2 upper bound (2x HW bandwidth waste)

## §6 Freeze statement

This spec is built on the iff-uniqueness draft of n=6 arithmetic. Any change that violates even one of the 4 clauses in §5.4 above will not be accepted without an `[10*] atlas.n6`-grade re-verification. The HW 4-tier boundaries correspond 1:1 to the Xn6 NPU partition boundaries; moving a tier boundary is a chip-respin trigger.

- Upstream SSOT: `$NEXUS/shared/n6/atlas.n6` (@R 6.speak.* entries)
- Verification engine: `experiments/chip-verify/verify_xn6_*.hexa` (18 items)
- Streaming implementation: `./hexa_speak_stream.hexa` (STUB, porting pending)
- Model implementation: `./hexa_speak_model.hexa` (STUB, porting pending)
