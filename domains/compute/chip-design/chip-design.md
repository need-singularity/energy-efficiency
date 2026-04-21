<!-- gold-standard: shared/harness/sample.md -->
---
domain: chip-design
requires:
  - to: chip-architecture
---

<!-- @own(sections=[WHY, COMPARE, REQUIRES, STRUCT, FLOW, VERIFY, EVOLVE], strict=false, order=sequential, prefix="§") -->

# HEXA Chip Design — n=6 6-Stage Roadmap (canonical index)

This document is the canonical index for the HEXA chip-design catalog. Each row
in the table below is an independent sub-domain, restructured into its own
`hexa-<name>/hexa-<name>.md` directory (own 3: one-doc-per-domain). The
comparison material originally kept in `chip-roadmap-comparison.md` has been
merged here so that `chip-design/` contains a single canonical .md at the root.

## §1 WHY (why this catalog exists)

Today every stage of a chip — material, core, compute, memory, I/O — is
negotiated with an ad-hoc mix of pitches, voltages and headers. The n=6
arithmetic closure (σ(6)=12, τ(6)=4, φ=2, sopfr=5, J₂=2σ=24) collapses that
search space. A single master identity

    σ·φ = n·τ = J₂ = 24

binds the five number-theoretic functions (OEIS A000203 / A000005 / A000010 /
A001414) into one design surface. Every sub-domain in this catalog is one
concrete physical realization of that surface. The catalog is organized as a
6-stage roadmap (HEXA-1 .. HEXA-6) plus an exotic frontier branch.

## §2 COMPARE — 6-stage roadmap sub-domains

| Stage | Sub-domain | Tech focus | Alien index target | Directory |
|-------|------------|------------|--------------------|-----------|
| HEXA-1 | hexa-1-digital | Digital CMOS SoC, n=6 baseline | 🛸10 | `hexa-1-digital/` |
| HEXA-2 | hexa-2-pim | Processing-In-Memory, DRAM row-buffer compute | 🛸10 | `hexa-2-pim/` |
| HEXA-3 | hexa-3d-stack | TSV + hybrid bonding, σ=12 wafer stack | 🛸10 | `hexa-3d-stack/` |
| HEXA-4 | hexa-photonic | Silicon photonic compute, λ=12 WDM | 🛸10 | `hexa-photonic/` |
| HEXA-5 | hexa-wafer | Wafer-scale integration (Cerebras-class) | 🛸10 | `hexa-wafer/` |
| HEXA-6 | hexa-superconducting | Superconducting logic (SFQ / AQFP) | 🛸10 | `hexa-superconducting/` |

### Exotic / frontier branches

| Sub-domain | Tech focus | Directory |
|------------|------------|-----------|
| hexa-dna-molecular | DNA / molecular substrate compute | `hexa-dna-molecular/` |
| hexa-field-effect | Field-effect (HEXA-FET) novel device | `hexa-field-effect/` |
| hexa-neuromorphic | Spiking / neuromorphic (HEXA-NEURO) | `hexa-neuromorphic/` |
| hexa-photon-topo | Topological photonic (HEXA-PHTOPO) | `hexa-photon-topo/` |
| hexa-quantum-hybrid | Quantum / classical hybrid (HEXA-QH) | `hexa-quantum-hybrid/` |
| hexa-topo-anyon | Topological anyon (HEXA-TOPO) | `hexa-topo-anyon/` |

Total: 12 independent sub-domains (6 roadmap stages + 6 frontier).

## §3 REQUIRES — upstream domains

| Upstream | Current 🛸 | Needed 🛸 | Gap | Role | Link |
|----------|-----------|-----------|-----|------|------|
| chip-architecture | 🛸7 | 🛸10 | +3 | 6-stage roadmap spine | [`../chip-architecture/chip-architecture.md`](../chip-architecture/chip-architecture.md) |

Mk.III and beyond of any sub-domain requires chip-architecture 🛸10.
Today every entry is at Mk.I~II (component / prototype).

## §4 STRUCT — catalog-level system map

    +----------+  +----------+  +----------+  +----------+  +----------+
    |  L0 mat  |->|  L1 core |->| L2 compute|->| L3 memory|->| L4 IO/ctrl|
    |  C Z=6   |  | sigma^2  |  | tau=4 pipe|  | 4-tier   |  | sigma*J2 |
    |  phi=2nm |  |  =144 SM |  | phi=2 FMA |  | 1/2+1/3+ |  |  =288    |
    |  CN=6    |  | sopfr=5  |  | n=6 vec   |  | 1/6 Egy. |  | J2=24 PHY|
    +----------+  +----------+  +----------+  +----------+  +----------+

Each sub-domain maps the same 5-layer chain onto a different physical
substrate (CMOS, photonic, superconducting, DNA, ...). The catalog-level
n=6 parameter mapping (full L0..L4 table) is preserved inside each
sub-domain document; this index only lists the common backbone.

### BT anchors

| BT | Name | Catalog-level role |
|----|------|--------------------|
| BT-28 | Cache hierarchy Egyptian | 1/2+1/3+1/6 bandwidth split |
| BT-56 | GPU arithmetic σ²=144 SM | tensor core array |
| BT-85 | Carbon Z=6 universality | die base material |
| BT-86 | Crystal CN=6 law | lattice coordination |
| BT-90 | SM=φ×K₆ kissing number | on-board σ²=144 cores |
| BT-93 | Carbon Z=6 chip substrate | diamond substrate |
| BT-123 | SE(3) dim=n=6 | 6-DOF processing |
| BT-181 | Multi-band σ=12 channels | I/O multiple access |
| BT-328 | AD τ=4 subsystem | ASIL-D safety |
| BT-342 | Aerospace n=6 standard | boundary-constant formulas |

## §5 FLOW — catalog-level data / energy flow

    Power in  --> [sigma-tau=8 rails] --> [Egyptian 1/2+1/3+1/6] --> load
     48V/12V       8 power domains       1/2 compute + 1/3 mem + 1/6 IO

    Data in  --> [sigma*J2=288 lanes PHY] --> [tau=4 pipe] --> [sigma^2=144 SM] --> out
     J2=24 width   288 x 48 Gbps              4 stages         144 SM parallel

Five operational modes (IDLE / COMPUTE / AI_INFER / AI_TRAIN / HPC) are
defined per-sub-domain; the mode table and DSE pareto (K1..K5 = 6*5*4*5*4
= 2400, Pareto-Top-6 in Diamond / Systolic / HBM3 / UCIe / AI at n6% = 94%)
are repeated inside each sub-domain document where they differ.

## §6 EVOLVE — catalog-level Mk roadmap

- **Mk.V (2050+)**  full AI-native synthesis: "one sentence → RTL → wafer"
  in τ=4 months. Requires chip-architecture + compiler-os +
  programming-language all at 🛸10.
- **Mk.IV (2040~2050)** n=6 hard-wired silicon: σ²=144 SM, σ·J₂=288 MAC,
  Egyptian power split fully silicon-fabricated at σ-φ=10nm / High-NA EUV.
- **Mk.III (2035~2040)** RTL-integrated SoC: HEXA-1 digital core + σ=12
  channel I/O + τ=4 cache in a single 7nm SoC.
- **Mk.II (2030~2035)** FPGA prototype: n=6 boundary constants on FPGA,
  288 MAC simulation, σ-φ=10× efficiency vs baseline.
- **Mk.I (2026, current)** Samsung foundry status baseline: SF2 / SF3P +
  HBM3E + X-Cube + I-Cube. Silicon photonic / superconducting / wafer-scale
  are reference-only (Intel / Cerebras / IBM reference designs).

## §7 VERIFY — catalog-level honesty gates

The catalog-level verification (10-category honesty check, stdlib Python)
used to live in `chip-roadmap-comparison.md §7`. It has been **moved
verbatim** into each sub-domain's `verify_chip-*.hexa`. The 10 categories
are:

1. §7.0 CONSTANTS — derive σ/τ/φ/sopfr from number theory (no hardcoding)
2. §7.1 DIMENSIONS — SI (M, L, T, I) dimensional consistency
3. §7.2 CROSS — re-derive MAC=288 via 3 independent paths
4. §7.3 SCALING — log-log regression recovers B⁴ exponent = 4.0 ± 0.1
5. §7.4 SENSITIVITY — ±10% perturbation confirms convex optimum at n=6
6. §7.5 LIMITS — Carnot / Landauer / Shannon not exceeded
7. §7.6 CHI2 — H₀ "n=6 is coincidence" p-value > 0.05
8. §7.7 OEIS — [1,2,3,6,12,24,48] registered as A008586-variant
9. §7.8 PARETO — Monte Carlo 2400-combo ranking, n=6 in top 5%
10. §7.9 SYMBOLIC — Fraction(1,2)+Fraction(1,3)+Fraction(1,6) == Fraction(1,1)
11. §7.10 COUNTER — explicit counter-examples + falsifiers

Falsifiers (any one of these invalidates the catalog):

- measured MAC/cycle < 245 (= 288 × 85%) invalidates σ·J₂ formula
- SM array symmetry variance > 5% invalidates σ²=144
- Egyptian sum ≠ 1 (Fraction equality fails) invalidates power split
- χ² p-value < 0.01 invalidates the n=6 coincidence hypothesis

## Sub-domain verification coverage

| Sub-domain | Verify script |
|------------|---------------|
| hexa-1-digital | `hexa-1-digital/verify_chip-hexa1-digital.hexa` |
| hexa-2-pim | `hexa-2-pim/verify_chip-hexa2-pim.hexa` |
| hexa-3d-stack | `hexa-3d-stack/verify_chip-3d-stack.hexa` |
| hexa-dna-molecular | `hexa-dna-molecular/verify_chip-dna-molecular.hexa` |
| hexa-field-effect | *(no verify script — gap)* |
| hexa-neuromorphic | `hexa-neuromorphic/verify_chip-neuromorphic.hexa` |
| hexa-photon-topo | `hexa-photon-topo/verify_chip-photon-topo.hexa` |
| hexa-photonic | `hexa-photonic/verify_chip-photonic.hexa` |
| hexa-quantum-hybrid | `hexa-quantum-hybrid/verify_chip-quantum-hybrid.hexa` |
| hexa-superconducting | `hexa-superconducting/verify_chip-superconducting.hexa` |
| hexa-topo-anyon | `hexa-topo-anyon/verify_chip-topo-anyon.hexa` |
| hexa-wafer | `hexa-wafer/verify_chip-wafer.hexa` |

Coverage: 11/12. `hexa-field-effect` has no matching `verify_chip-*.hexa`
and needs one authored (see falsifier gate §7).

## Provenance

- 2026-04-21 — restructured from flat layout (13 loose .md + 11 loose
  verify scripts) into 12 sub-domain directories to comply with **own 3**
  (one-doc-per-domain). `chip-roadmap-comparison.md` merged into this
  canonical index and deleted.
- Previous canonical: `chip-roadmap-comparison` v2 (829 lines) — full §7
  verification code preserved inside each sub-domain's verify script.


## §8 IDEAS

This section covers ideas for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §9 METRICS

This section covers metrics for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §10 RISKS

This section covers risks for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §11 DEPENDENCIES

This section covers dependencies for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §12 TIMELINE

This section covers timeline for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §13 TOOLS

This section covers tools for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §14 TEAM

This section covers team for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §15 REFERENCES

This section covers references for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

