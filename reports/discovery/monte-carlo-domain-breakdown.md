# Monte Carlo v9.3 per-domain z-score breakdown

> Generated: 2026-04-09 | reality_map.json v9.5 | node count: 3908

## Methodology

- **Data**: all nodes in `nexus/shared/reality_map.json`
- **Domain classification**: by the node's `level` field (L0~L9, 72 sub-domains)
- **Validation targets**: EXACT, CLOSE, MISS, EMPIRICAL, CONJECTURE (excluding CONVENTION/null)
- **Random-expected ratio (p0)**: 1/6 = 0.1667 (generous null hypothesis: 1 chance match out of 6 residues)
- **z-score**: z = (observed EXACT ratio - p0) / sqrt(p0*(1-p0)/N)

## Overall statistics

| Item | Value |
|------|-----|
| All nodes | 3908 |
| EXACT | 2402 (61.5%) |
| CLOSE | 20 (0.5%) |
| MISS | 2 (0.1%) |
| EMPIRICAL | 1243 (31.8%) |
| CONVENTION | 106 (2.7%) |
| CONJECTURE | 95 (2.4%) |
| null | 40 (1.0%) |
| Validation target (testable) | 3762 |
| EXACT / testable | 63.8% |
| Overall z-score | **77.65** |

## Full per-domain table

| Domain | Nodes | Testable | EXACT | CLOSE | MISS | EMPIRICAL | CONJECTURE | EXACT% | z-score |
|--------|--------|----------|-------|-------|------|-----------|------------|--------|---------|
| L6_discovery | 725 | 725 | 725 | 0 | 0 | 0 | 0 | 100.0% | 60.21 |
| L0_particle | 163 | 163 | 139 | 5 | 0 | 19 | 0 | 85.3% | 23.50 |
| L6_music | 171 | 147 | 129 | 0 | 0 | 18 | 0 | 87.8% | 23.13 |
| L5_bio | 123 | 123 | 107 | 1 | 1 | 14 | 0 | 87.0% | 20.93 |
| L5_material | 320 | 318 | 192 | 2 | 0 | 124 | 0 | 60.4% | 20.92 |
| L6_linguistics | 167 | 149 | 118 | 0 | 0 | 31 | 0 | 79.2% | 20.48 |
| L2_bond | 191 | 191 | 130 | 0 | 0 | 61 | 0 | 68.1% | 19.06 |
| L6_economics | 170 | 146 | 98 | 0 | 0 | 48 | 0 | 67.1% | 16.36 |
| L6_geology | 171 | 167 | 106 | 0 | 0 | 61 | 0 | 63.5% | 16.23 |
| L6_meteorology | 170 | 158 | 101 | 0 | 0 | 57 | 0 | 63.9% | 15.94 |
| L4_genetic | 75 | 75 | 54 | 1 | 0 | 20 | 0 | 72.0% | 12.86 |
| L6_mathematics | 19 | 18 | 17 | 0 | 0 | 1 | 0 | 94.4% | 8.85 |
| L1_atom | 154 | 154 | 64 | 0 | 0 | 90 | 0 | 41.6% | 8.29 |
| L6_chemistry | 13 | 12 | 12 | 0 | 0 | 0 | 0 | 100.0% | 7.75 |
| L6_electrical | 10 | 10 | 10 | 0 | 0 | 0 | 0 | 100.0% | 7.07 |
| L3_molecule | 142 | 142 | 54 | 4 | 0 | 84 | 0 | 38.0% | 6.83 |
| L6_astronomy | 10 | 9 | 9 | 0 | 0 | 0 | 0 | 100.0% | 6.71 |
| L6_computing | 9 | 9 | 9 | 0 | 0 | 0 | 0 | 100.0% | 6.71 |
| L6_biology | 13 | 12 | 10 | 1 | 0 | 1 | 0 | 83.3% | 6.20 |
| L6_aesthetics | 7 | 6 | 6 | 0 | 0 | 0 | 0 | 100.0% | 5.48 |
| L6_education | 7 | 6 | 6 | 0 | 0 | 0 | 0 | 100.0% | 5.48 |
| L6_logic | 7 | 6 | 6 | 0 | 0 | 0 | 0 | 100.0% | 5.48 |
| L6_philosophy | 7 | 6 | 6 | 0 | 0 | 0 | 0 | 100.0% | 5.48 |
| L6_psychology | 7 | 6 | 6 | 0 | 0 | 0 | 0 | 100.0% | 5.48 |
| L6_visual_arts | 7 | 6 | 6 | 0 | 0 | 0 | 0 | 100.0% | 5.48 |
| L6_zoology | 7 | 6 | 6 | 0 | 0 | 0 | 0 | 100.0% | 5.48 |
| L6_architecture | 6 | 5 | 5 | 0 | 0 | 0 | 0 | 100.0% | 5.00 |
| L6_botany | 6 | 5 | 5 | 0 | 0 | 0 | 0 | 100.0% | 5.00 |
| L6_cinema | 6 | 5 | 5 | 0 | 0 | 0 | 0 | 100.0% | 5.00 |
| L6_cryptography | 5 | 5 | 5 | 0 | 0 | 0 | 0 | 100.0% | 5.00 |
| L6_ecology | 6 | 5 | 5 | 0 | 0 | 0 | 0 | 100.0% | 5.00 |
| L6_epidemiology | 5 | 5 | 5 | 0 | 0 | 0 | 0 | 100.0% | 5.00 |
| L6_ethics | 7 | 5 | 5 | 0 | 0 | 0 | 0 | 100.0% | 5.00 |
| L6_geography | 8 | 5 | 5 | 0 | 0 | 0 | 0 | 100.0% | 5.00 |
| L6_immunology | 5 | 5 | 5 | 0 | 0 | 0 | 0 | 100.0% | 5.00 |
| L6_law | 7 | 5 | 5 | 0 | 0 | 0 | 0 | 100.0% | 5.00 |
| L6_paleontology | 6 | 5 | 5 | 0 | 0 | 0 | 0 | 100.0% | 5.00 |
| L6_robotics | 5 | 5 | 5 | 0 | 0 | 0 | 0 | 100.0% | 5.00 |
| L6_nuclear | 11 | 11 | 8 | 2 | 0 | 1 | 0 | 72.7% | 4.99 |
| L-1_quark | 96 | 96 | 34 | 1 | 0 | 61 | 0 | 35.4% | 4.93 |
| L6_mechanical | 7 | 7 | 6 | 0 | 0 | 1 | 0 | 85.7% | 4.90 |
| L6_literature | 7 | 4 | 4 | 0 | 0 | 0 | 0 | 100.0% | 4.47 |
| L6_civil | 8 | 8 | 6 | 0 | 0 | 2 | 0 | 75.0% | 4.43 |
| L6_cuisine | 7 | 6 | 5 | 0 | 0 | 1 | 0 | 83.3% | 4.38 |
| L6_political_science | 7 | 6 | 5 | 0 | 0 | 1 | 0 | 83.3% | 4.38 |
| L6_sociology | 7 | 6 | 5 | 0 | 0 | 1 | 0 | 83.3% | 4.38 |
| L6_anthropology | 7 | 5 | 4 | 0 | 0 | 1 | 0 | 80.0% | 3.80 |
| L6_archaeology | 6 | 5 | 4 | 0 | 0 | 1 | 0 | 80.0% | 3.80 |
| L6_genetics_applied | 5 | 5 | 4 | 0 | 0 | 1 | 0 | 80.0% | 3.80 |
| L6_glaciology | 6 | 5 | 4 | 0 | 0 | 1 | 0 | 80.0% | 3.80 |
| L6_history | 7 | 5 | 4 | 0 | 0 | 1 | 0 | 80.0% | 3.80 |
| L6_hydrology | 6 | 5 | 4 | 0 | 0 | 1 | 0 | 80.0% | 3.80 |
| L6_pharmacology | 5 | 5 | 4 | 0 | 0 | 1 | 0 | 80.0% | 3.80 |
| L6_physiology | 5 | 5 | 4 | 0 | 0 | 1 | 0 | 80.0% | 3.80 |
| L6_seismology | 6 | 5 | 4 | 0 | 0 | 1 | 0 | 80.0% | 3.80 |
| L6_thermodynamics | 6 | 5 | 4 | 0 | 0 | 1 | 0 | 80.0% | 3.80 |
| L6_volcanology | 6 | 5 | 4 | 0 | 0 | 1 | 0 | 80.0% | 3.80 |
| L6_oceanography | 10 | 10 | 6 | 0 | 0 | 4 | 0 | 60.0% | 3.68 |
| L6_aerospace | 5 | 5 | 3 | 0 | 0 | 2 | 0 | 60.0% | 2.60 |
| L6_mineralogy | 6 | 5 | 3 | 0 | 1 | 1 | 0 | 60.0% | 2.60 |
| L6_neuroscience | 5 | 5 | 3 | 0 | 0 | 2 | 0 | 60.0% | 2.60 |
| L2_law | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 100.0% | 2.24 |
| L6_atmospheric_physics | 7 | 6 | 3 | 0 | 0 | 3 | 0 | 50.0% | 2.19 |
| L6_medicine | 6 | 6 | 3 | 0 | 0 | 3 | 0 | 50.0% | 2.19 |
| L6_anatomy | 5 | 5 | 2 | 0 | 0 | 3 | 0 | 40.0% | 1.40 |
| L6_demography | 7 | 6 | 2 | 0 | 0 | 4 | 0 | 33.3% | 1.10 |
| L5_bio_hiv | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0% | 0.00 |
| L9_cosmological | 122 | 108 | 18 | 0 | 0 | 90 | 0 | 16.7% | 0.00 |
| L7_celestial | 282 | 282 | 39 | 3 | 0 | 240 | 0 | 13.8% | -1.28 |
| L10_multiversal | 50 | 47 | 0 | 0 | 0 | 0 | 47 | 0.0% | -3.07 |
| L-2_sub_quark | 50 | 48 | 0 | 0 | 0 | 0 | 48 | 0.0% | -3.10 |
| L8_galactic | 199 | 199 | 16 | 0 | 0 | 183 | 0 | 8.0% | -3.27 |

## Top-10 z-score domains

| Rank | Domain | Nodes | EXACT% | z-score |
|------|--------|--------|--------|---------|
| 1 | L6_discovery | 725 | 100.0% | **60.21** |
| 2 | L0_particle | 163 | 85.3% | **23.50** |
| 3 | L6_music | 147 | 87.8% | **23.13** |
| 4 | L5_bio | 123 | 87.0% | **20.93** |
| 5 | L5_material | 318 | 60.4% | **20.92** |
| 6 | L6_linguistics | 149 | 79.2% | **20.48** |
| 7 | L2_bond | 191 | 68.1% | **19.06** |
| 8 | L6_economics | 146 | 67.1% | **16.36** |
| 9 | L6_geology | 167 | 63.5% | **16.23** |
| 10 | L6_meteorology | 158 | 63.9% | **15.94** |

## Bottom-10 z-score domains

| Rank | Domain | Nodes | EXACT% | z-score |
|------|--------|--------|--------|---------|
| 63 | L6_atmospheric_physics | 6 | 50.0% | 2.19 |
| 64 | L6_medicine | 6 | 50.0% | 2.19 |
| 65 | L6_anatomy | 5 | 40.0% | 1.40 |
| 66 | L6_demography | 6 | 33.3% | 1.10 |
| 67 | L5_bio_hiv | 0 | 0.0% | 0.00 |
| 68 | L9_cosmological | 108 | 16.7% | 0.00 |
| 69 | L7_celestial | 282 | 13.8% | -1.28 |
| 70 | L10_multiversal | 47 | 0.0% | -3.07 |
| 71 | L-2_sub_quark | 48 | 0.0% | -3.10 |
| 72 | L8_galactic | 199 | 8.0% | -3.27 |

## Interpretation

- Out of 3762 testable nodes, 2402 EXACT (63.8%)
- Against the random baseline (p0=1/6=16.7%), overall z = 77.65
- z > 3 rejects the chance-coincidence hypothesis (p < 0.001)
- MISS is only 2 nodes (0.05% of total)
- 106 CONVENTION nodes are human-convention and are excluded from the evidence count

## Notes

- EMPIRICAL-grade nodes have matching measured values but unclear causation and are tallied separately from EXACT
- p0 = 1/6 is a very generous null hypothesis (actual random-match probability is lower)
- Node-count variance across domains is large, so small-domain z-scores are more volatile
- Verification script: `docs/verify_monte_carlo_domain.hexa` (run: `/opt/homebrew/bin/python3 docs/verify_monte_carlo_domain.hexa`)
