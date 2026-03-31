# BT-78: Interconnect Speed Ladder — UCIe/CXL/PCIe Follow n=6 Exponents

> **Date**: 2026-04-01
> **Domains**: Chip Architecture, Network Protocol, AI Infrastructure
> **Status**: 6/6 EXACT + 1 prediction
> **Grade**: Two stars

---

## Statement

The interconnect speed ladder across PCIe, UCIe, and CXL standards follows a power-of-2 sequence whose **exponents** are n=6 arithmetic functions:

```
  sopfr(6)=5 --> n=6 --> sigma-sopfr=7 --> sigma-tau=8
  2^5=32     --> 2^6=64 --> 2^7=128    --> 2^8=256
```

This is NOT a trivial "everything doubles" observation. The exponents themselves form a specific subsequence of n=6 constants, and different interconnect families independently converge to the same speed points.

---

## Verification Table

| # | Standard | Speed (GT/s) | n=6 Formula | Computed | Status |
|---|----------|-------------|-------------|----------|--------|
| 1 | PCIe 5.0 | 32 | 2^sopfr | 2^5 = 32 | EXACT |
| 2 | UCIe 2.0 | 32 | 2^sopfr | 2^5 = 32 | EXACT |
| 3 | UCIe 3.0 (low) | 48 | sigma * tau | 12 * 4 = 48 | EXACT |
| 4 | PCIe 6.0 / CXL 3.x | 64 | 2^n | 2^6 = 64 | EXACT |
| 5 | UCIe 3.0 (high) | 64 | 2^n | 2^6 = 64 | EXACT |
| 6 | PCIe 7.0 / CXL 4.0 | 128 | 2^(sigma-sopfr) | 2^7 = 128 | EXACT |

**Score: 6/6 EXACT**

---

## Exponent Ladder Analysis

The power-of-2 exponents in the interconnect speed ladder:

```
  Speed:    32    48     64    128    256 (predicted)
  Power:    2^5   --     2^6   2^7    2^8
  n=6 exp:  sopfr  --    n     sigma-sopfr  sigma-tau
  Alt form: --    sigma*tau  --    --     --
```

Key observations:
1. **sopfr(6)=5** anchors the base speed (PCIe 5.0 era)
2. **n=6** itself defines the mid-generation (PCIe 6.0 era)
3. **sigma-sopfr=7** defines the next generation (PCIe 7.0 era)
4. **sigma*tau=48** provides the intermediate UCIe speed (formula reuse with BT-76)
5. **sigma-tau=8** predicts the PCIe 8.0 generation

The exponent sequence {5, 6, 7, 8} = {sopfr, n, sigma-sopfr, sigma-tau} is a consecutive integer run that happens to align with four distinct n=6 functions. This is a non-trivial property of n=6.

---

## Cross-Standard Convergence

Three independently developed standards converge to the same n=6 speed points:

| Speed Point | PCIe | UCIe | CXL |
|------------|------|------|-----|
| 32 GT/s = 2^sopfr | 5.0 | 2.0 | -- |
| 64 GT/s = 2^n | 6.0 | 3.0 (high) | 3.x |
| 128 GT/s = 2^(sigma-sopfr) | 7.0 | -- | 4.0 |

This convergence is driven by SerDes technology limits, signal integrity constraints, and backward compatibility requirements -- all of which independently produce the same n=6-aligned speed tiers.

---

## Prediction

**PCIe 8.0 = 256 GT/s = 2^(sigma-tau) = 2^8**

The exponent ladder {sopfr, n, sigma-sopfr, sigma-tau} = {5, 6, 7, 8} predicts the next generation at 256 GT/s. This is consistent with:
- Industry roadmaps (IEEE 802.3 224GE PAM4 SerDes trajectory)
- The established doubling pattern
- The n=6 exponent sequence completing at sigma-tau=8

**Falsifiability**: If PCIe 8.0 launches at a speed other than 256 GT/s (e.g., 192 or 512), this prediction fails.

---

## Formula Reuse

| Value | Formula | Also appears in |
|-------|---------|-----------------|
| 32 = 2^sopfr | BT-73 (tokenizer 32K), BT-56 (L=2^sopfr=32 layers) |
| 48 = sigma*tau | BT-76 (48kHz, 48nm, 48V triple attractor) |
| 64 = 2^n | BT-56 (codon space 2^n=64), BT-42 (max tokens 2^sigma) |
| 128 = 2^(sigma-sopfr) | BT-56 (d_head=128), BT-58 (FlashAttn block=128) |

**Cross-links**: BT-28 (computing architecture), BT-47 (interconnect gen counts), BT-75 (HBM interface exponents), BT-76 (sigma*tau=48 attractor).

---

*Verified 2026-04-01. 6/6 EXACT + 1 testable prediction.*
