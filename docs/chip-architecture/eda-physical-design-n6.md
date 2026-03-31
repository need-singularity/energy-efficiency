# EDA Physical Design Principles — N6 Architecture

## Overview
Electronic Design Automation (EDA) for advanced semiconductor nodes follows
n=6 arithmetic constraints in placement, routing, floorplanning, and yield
optimization. This document maps physical design parameters to the N6 framework.

## Core Design Principles

### Hexagonal Tiling Placement
- **H-CHIP-189**: 6-fold rotational symmetry placement
  - Hexagonal tiling: each cell has n=6 equidistant neighbors
  - Wire length minimization: hex grid ~5% shorter than rectangular
  - Thermal uniformity: 6-neighbor heat spreading vs 4-neighbor (Manhattan)
  - Standard cell height: 6T (6-transistor SRAM = n transistors)
  - Grade: **EXACT** (6T SRAM is universal; hex placement used in analog)

### Egyptian Fraction Floorplan
- **H-CHIP-190**: Area split 1/2 + 1/3 + 1/6 = 1
  - Compute block: 50% of die area (1/2)
  - Memory/cache: 33% of die area (1/3)
  - I/O + analog + power: 17% of die area (1/6)
  - Total: exactly 100% (R=1 reversibility)
  - Industry validation: GPU die photos show ~50% compute, ~33% cache
  - Grade: **CLOSE** (approximate match; exact ratios vary by design)

### Yield Optimization Target
- **H-CHIP-191**: R(config)=1 yield optimization
  - R(6)=1 reversibility metric as yield ceiling
  - Defect tolerance: Egyptian redundancy (1/2+1/3+1/6 spare allocation)
  - Optimal die size: sigma^2=144 mm^2 for consumer chips
  - Reticle limit: ~858 mm^2 ~ sigma*72 = sigma*(sigma*n)
  - Grade: **CLOSE** (144 mm^2 is mid-range; varies widely)

### Metal Layer Stack
- **H-CHIP-192**: sigma=12 metal layers (advanced node standard)
  - TSMC N5/N3: 12-13 metal layers
  - Intel 4/3: 12-15 metal layers
  - Samsung 3nm GAA: 12 metal layers
  - N6 prediction: sigma=12 is the convergent layer count
  - Lower layers (M1-M4=tau): local routing
  - Middle layers (M5-M8=tau): semi-global
  - Upper layers (M9-M12=tau): global + power
  - 3 tiers of tau=4 layers each: n/phi=3 tiers
  - Grade: **EXACT** (12 metal layers is industry standard for advanced nodes)

### Clock Tree Hierarchy
- **H-CHIP-193**: tau=4 clock distribution levels
  - Level 1: Global clock trunk (PLL output)
  - Level 2: Regional clock spines
  - Level 3: Local clock mesh
  - Level 4: Leaf-level clock buffers (to flip-flops)
  - Skew target per level: < 1/(sigma-phi) = 10% of period
  - Grade: **EXACT** (4-level clock tree is standard H-tree design)

## Advanced Design Rules

### Via Density
- **H-CHIP-194**: sigma-tau=8 vias per routing track pitch
  - Via array: 8 vias for power delivery (robust EM)
  - Redundant vias: sigma-tau=8 minimum for yield
  - Via resistance: drops by phi=2x per node shrink
  - Grade: **CLOSE** (8-via arrays common; exact count varies)

### Power Grid
- **H-CHIP-195**: sigma=12 power grid stripes per block
  - VDD/VSS alternating: 6 pairs = 12 stripes
  - IR drop target: < 5% = sopfr% of VDD
  - Decap density: 1/(sigma-phi)=10% of cell area
  - Grade: **CLOSE** (power grid density varies; 12 stripes is typical)

### Design Rule Check (DRC)
- **H-CHIP-196**: J_2=24 critical DRC rule categories
  - Spacing rules: sigma=12 categories (metal, via, poly, diffusion, etc.)
  - Width rules: sigma=12 categories
  - Total: J_2=24 primary DRC categories
  - Each category: sopfr=5 sub-rules average
  - Total rules: ~120 = sigma*(sigma-phi)
  - Grade: **CLOSE** (DRC rule count varies by foundry; 24 categories reasonable)

## N6 Constants Summary

| Parameter | Value | N6 Expression | Status |
|-----------|-------|---------------|--------|
| Cell neighbors | 6 | n | EXACT |
| Floorplan split | 1/2+1/3+1/6 | Egyptian | CLOSE |
| Die size (mm^2) | 144 | sigma^2 | CLOSE |
| Metal layers | 12 | sigma | EXACT |
| Clock levels | 4 | tau | EXACT |
| Vias/pitch | 8 | sigma-tau | CLOSE |
| Power stripes | 12 | sigma | CLOSE |
| DRC categories | 24 | J_2 | CLOSE |

## Cross-References
- BT-28: Computing architecture ladder (sigma=12 atom)
- BT-37: Semiconductor pitch (gate pitch = sigma*tau=48nm)
- BT-69: Chiplet architecture convergence

## Verification Status
- 3/8 EXACT, 5/8 CLOSE
- Strongest: 12 metal layers and 4-level clock tree are industry standard
