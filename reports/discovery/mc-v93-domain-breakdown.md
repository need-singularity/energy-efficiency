# Monte Carlo v9.3 - per-domain breakdown report

- Basis: `scripts/monte_carlo_v93.py` + `scripts/mc_v93_by_domain.py`
- Data: `$NEXUS/shared/reality_map.json`
- Number of domains: **15**
- Per-domain simulation: 2000 runs (seed=42)
- Average z-score: **10.22**
- Strongest domain: **particle physics (Standard Model)** (z=23.26)
- Weakest domain: **molecular chemistry** (z=4.90)

## Per-domain strength ranking

| Rank | Domain | Sample N | n=6 hits | Hit rate | Random mean | Random sigma | z-score | p-value | Strength |
|---:|---|---:|---:|---:|---:|---:|---:|---:|:---:|
| 1 | Particle physics (Standard Model) | 41 | 31 | 75.6% | 1.1 | 1.28 | 23.26 | 0.0000 | strong |
| 2 | HIV | 10 | 10 | 100.0% | 0.4 | 0.49 | 19.44 | 0.0000 | strong |
| 3 | Materials | 157 | 109 | 69.4% | 5.0 | 5.68 | 18.32 | 0.0000 | strong |
| 4 | Biology | 34 | 25 | 73.5% | 1.5 | 1.84 | 12.75 | 0.0000 | strong |
| 5 | Humanities/Social (L6) | 97 | 80 | 82.5% | 4.7 | 6.20 | 12.13 | 0.0000 | strong |
| 6 | Atomic physics | 40 | 37 | 92.5% | 2.8 | 3.57 | 9.57 | 0.0000 | strong |
| 7 | Earth science (L6) | 72 | 52 | 72.2% | 4.3 | 5.46 | 8.74 | 0.0000 | strong |
| 8 | Chemical bonding | 94 | 65 | 69.1% | 7.0 | 7.41 | 7.83 | 0.0000 | strong |
| 9 | Engineering/Physics (L6) | 39 | 28 | 71.8% | 3.1 | 3.64 | 6.84 | 0.0000 | strong |
| 10 | Life sciences (L6) | 51 | 45 | 88.2% | 4.8 | 5.91 | 6.80 | 0.0000 | strong |
| 11 | Chemistry (L6) | 9 | 7 | 77.8% | 0.8 | 0.98 | 6.31 | 0.0000 | strong |
| 12 | Cancer therapy | 18 | 12 | 66.7% | 1.4 | 1.87 | 5.69 | 0.0000 | strong |
| 13 | Particle physics (quarks) | 15 | 15 | 100.0% | 1.7 | 2.34 | 5.69 | 0.0000 | strong |
| 14 | Genetics / molecular biology | 15 | 14 | 93.3% | 2.2 | 2.36 | 4.98 | 0.0000 | medium |
| 15 | Molecular chemistry | 39 | 34 | 87.2% | 4.4 | 6.04 | 4.90 | 0.0000 | medium |

## Weak domains (z < 3)

None - every domain passes z >= 3.

## Interpretation

- Per-domain independent Monte Carlo enables comparison across regions with different node counts.
- z >= 5: n=6 specificity confirmed (extremely significant)
- 3 <= z < 5: statistically significant
- z < 3: either too small a sample, or insufficient n=6 alignment within the domain, so reinforcement candidate.
