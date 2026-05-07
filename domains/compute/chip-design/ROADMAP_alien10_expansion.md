---
id: chip-design-alien10-expansion-roadmap
date: 2026-05-07
roadmap_task: §11.5 ALIEN-10-EXPANSION across all chip-design sister domains
grade: [10] EXACT closure target
status: 8/12 SISTERS LANDED (4 PENDING)
parent: domains/compute/chip-design/chip-design.md
license: CC-BY-SA-4.0
---

# Chip-Design §11.5 ALIEN-10-EXPANSION — Continuation Roadmap

> Cycle paused 2026-05-07 with 8 of 12 sister domains landed. This file
> tracks the remaining 4 (hexa-2-pim, hexa-3d-stack, hexa-wafer, hexa-topo-anyon)
> for future expansion. Each follows the same pattern landed in the 8 prior:
>
>   1. Add `## §11.5 ALIEN-10-EXPANSION (12 TP-<DOMAIN>-* candidates)` section
>      to the domain `.md` file, between §11 DEPENDENCIES and §12 TIMELINE
>   2. Create companion `verify_chip-<domain>_alien10.py` (stdlib-only)
>      with 12 auto-verifiable TPs
>   3. Smoke test → 12/12 PASS
>   4. Commit + push to origin/main
>   5. Update `README.md` §11.5 federation table (TPs total / alien=10 / EXACT)

---

## Landed (8/12) — 2026-05-07

| Order | Domain | Commit | TPs | alien=10 | EXACT | verify |
|------:|--------|--------|----:|---------:|------:|-------:|
| 1 | hexa-neuromorphic | `0c65155a` | 33 | 33 | 8 | 27/27 |
| 2 | hexa-quantum-hybrid | `ed08875b` | 12 | 11 | 4 | 12/12 |
| 3 | hexa-photonic | `8f414fd` | 12 | 11 | 3 | 12/12 |
| 4 | hexa-superconducting | `4d9e298` | 12 | 9 | 4 | 12/12 |
| 5 | hexa-photon-topo | `381f1f2` | 12 | 10 | **6** | 12/12 |
| 6 | hexa-dna-molecular | `9d6ad11` | 12 | 9 | 5 | 12/12 |
| 7 | hexa-field-effect | `30611b4` | 12 | 7 | 1 | 12/12 |
| 8 | hexa-1-digital | `528a502` | 12 | 8 | 3 | 12/12 |
| **Subtotal** | — | — | **117** | **98** | **34** | **108/116** |
| §11 AKIDA (existing baseline) | hexa-neuromorphic § | `db738f73` | 9 | 5 | 4 | 6/9 |
| **Total (incl. §11)** | — | — | **126** | **103** | **38** | **117/125** |

---

## Pending (4/12)

### C8: hexa-2-pim — Processing-in-Memory

**Alien-10 candidates (preview, 12 TPs)**:
- TP-PIM-A1 Memristor crossbar Ohm's law I = V·G — analog MAC primitive
- TP-PIM-A2 σ·J₂ = 288 ALU/bank EXACT — von Neumann bottleneck dismantle
- TP-PIM-A3 Crossbar I-V linearity range (universal analog floor)
- TP-PIM-A4 In-memory MAC energy ~10⁻¹⁵ J/op (sister of TP-NEURO-A1 Landauer)
- TP-PIM-A5 DRAM row buffer width = σ·J₂ = 288 EXACT
- TP-PIM-A6 Memristor switching threshold V_set ~ 1V (charge-trap floor)
- TP-PIM-A7 Crossbar parasitic IR drop limit
- TP-PIM-A8 Programming endurance ≥ 10⁹ cycles (NV memory floor)
- TP-PIM-A9 Read disturb floor (Read-Verify-Modify cycle)
- TP-PIM-A10 ADC quantization φ=2 bit per cell minimum
- TP-PIM-A11 In-place stochastic gradient — sister of STDP (TP-NEURO-D)
- TP-PIM-A12 Cross-domain: σ²=144 cells × τ=4 ADC bits = 576 effective resolution

### C9: hexa-3d-stack — 3D-Stacked Memory + Logic

**Alien-10 candidates (preview, 12 TPs)**:
- TP-3D-A1 TSV pitch ≥ φ = 2 μm — Cu/SiO₂ interfacial floor
- TP-3D-A2 Hybrid bond pitch ≥ 1 μm (Cu-Cu direct bonding floor)
- TP-3D-A3 Vertical interconnect density σ·J₂ = 288 lane/mm² EXACT
- TP-3D-A4 Thermal RC time constant τ_thermal = R_th × C_th
- TP-3D-A5 Stack height ≤ σ = 12 wafer layers (industrial limit)
- TP-3D-A6 Inter-layer coupling capacitance Cᵢⱼ = ε·A/d
- TP-3D-A7 Rent's rule p ≈ 0.6 holds across 3D (sister of TP-DIGITAL-A3)
- TP-3D-A8 Heat-flux density limit ~100 W/cm² (silicon thermal ceiling)
- TP-3D-A9 KGD (known-good-die) yield product Π_i Y_i
- TP-3D-A10 Vertical signaling delay ≈ d × √(LC) per layer
- TP-3D-A11 σ²=144 SM × τ=4 stack = 576 die total system
- TP-3D-A12 Memory hierarchy: DRAM/SRAM/Logic τ=4 stack tier EXACT

### C10: hexa-wafer — Wafer-Scale Integration

**Alien-10 candidates (preview, 12 TPs)**:
- TP-WAFER-A1 Murphy/Poisson yield Y(N) = exp(-D₀·A·N) (sister of TP-AKIDA-8)
- TP-WAFER-A2 σ²=144 tile + σ=12 spare row+col EXACT (Cerebras-class self-heal)
- TP-WAFER-A3 2D torus τ=4-hop diameter for σ²=144 grid EXACT
- TP-WAFER-A4 Wafer area 300mm Φ ≈ 70686 mm² (industry standard)
- TP-WAFER-A5 Defect density D₀ ≤ 0.1/cm² (foundry alien-10 ceiling)
- TP-WAFER-A6 Mesh routing congestion limit (Rent's rule cross)
- TP-WAFER-A7 SRAM density ≈ σ·τ = 48 GB at WSI scale EXACT
- TP-WAFER-A8 Cooling power density ≤ 1 kW/cm² (peak heat-flux limit)
- TP-WAFER-A9 Reticle stitching defect floor — wafer-scale interconnect
- TP-WAFER-A10 KGD redundancy = σ-φ = 10 % spare overhead
- TP-WAFER-A11 Wafer-test parallelism = σ·J₂ = 288 pin-parallel
- TP-WAFER-A12 Cross with TP-AKIDA-8: σ²=144 yield-curve peak universal

### C11: hexa-topo-anyon — Topological Anyon (separate from photon-topo)

**Alien-10 candidates (preview, 12 TPs)**:
- TP-ANYON-A1 Non-Abelian braiding σ_ij σ_jk σ_ij = σ_jk σ_ij σ_jk (Yang-Baxter EXACT)
- TP-ANYON-A2 Modular tensor category σ=12 fusion channels (sister of TP-TOPO-A11)
- TP-ANYON-A3 Anyon ground-state degeneracy = genus·integer
- TP-ANYON-A4 Topological gap protection — energy floor for braiding
- TP-ANYON-A5 Majorana zero-mode Z₂ parity (sister of TP-TOPO-A2)
- TP-ANYON-A6 Fibonacci anyons golden-ratio dimension d_F = φ_golden
- TP-ANYON-A7 Quantum dimension D² = Σ d_a² (universal modular invariant)
- TP-ANYON-A8 Topological entanglement entropy γ = log D
- TP-ANYON-A9 Levin-Wen string-net σ²=144 plaquette
- TP-ANYON-A10 Chern-Simons coupling integer k ∈ ℤ
- TP-ANYON-A11 Edge CFT central charge c (universal protocol invariant)
- TP-ANYON-A12 Topological quantum computation universal gate set (4 = τ basic gates)

---

## Final federation projection (when 4 pending complete)

| Status | TPs | alien=10 | EXACT | verify |
|---|---:|---:|---:|---:|
| Current (8 sisters + AKIDA) | 126 | 103 | 38 | 117/125 |
| + hexa-2-pim (~12 TPs, ~8 alien=10, ~3 EXACT) | 138 | 111 | 41 | 129/137 |
| + hexa-3d-stack (~12, ~8, ~3) | 150 | 119 | 44 | 141/149 |
| + hexa-wafer (~12, ~9, ~4) | 162 | 128 | 48 | 153/161 |
| + hexa-topo-anyon (~12, ~10, ~5) | **174** | **138** | **53** | **165/173** |

**Final**: 12 sister chip-design domains × 12 TPs = **144 TPs** (= σ² EXACT closure on the
expansion itself!) + 9 §11 AKIDA = **153 total TPs** registered across the alien-10 federation.

> Self-referential closure: the expansion size 12 = σ aligns with the n=6 framework
> it documents. 12 sisters × 12 TPs/sister = σ² = 144 — the expansion is itself
> n=6-EXACT.

---

## Resumption protocol

When the user says "continue alien-10 expansion" or "/loop keep going cycle" again:

1. Pick the next pending sister (C8 → C9 → C10 → C11 in order)
2. Apply the 5-step pattern (md insert / verify .py / smoke / commit-push / README update)
3. Update this roadmap with the new commit hash + verify count
4. Repeat until 144-TP closure achieved, then emit final completion banner.

## Cross-link

- `hive/spec/sovereign_cli_federation.spec.yaml` v1 — federation invariants
- `domains/compute/chip-design/hexa-neuromorphic/hexa-neuromorphic.md` §11.5 — pattern source
- `n6shared/GRADE_RUBRIC_1_TO_10PLUS.md` — closure-grade rubric

---

*Cycle paused 2026-05-07 by user "stop next roadmap add". Not abandoned — staged.*
