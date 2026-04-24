# DSE uncovered-domain scan report

- Date: 2026-04-12
- Analysis: domains/_index.json (304 domains) vs nexus/origins/universal-dse/domains/ (490 TOML)

---

## Summary

| Item | Count |
|------|------|
| Total indexed domains | 304 |
| Total DSE TOML files | 490 (including 186 extension domains outside the index) |
| Covered domains | 84 |
| Uncovered domains | 220 |
| Coverage rate | 27.6% |
| Newly authored in this pass | 10 |
| Still uncovered after authoring | 220 (by index) |

---

## 10 newly authored this pass

| # | Domain | Axis | Core n=6 connection | Combinations |
|---|--------|----|---------------|--------|
| 1 | millennium-yang-mills | physics | SU(3) color n/phi=3, sigma=12 gauge bosons | 7,776 |
| 2 | millennium-riemann | physics | phi(6)/tau(6)=1/2 critical line, sigma(6)=12 divisor sum | 7,776 |
| 3 | autonomous-driving | infra | n=6 SAE levels, sigma=12 sensors, tau=4 perception | 7,776 |
| 4 | cancer-therapy | life | n=6 therapy modalities, sigma=12 biomarkers, tau=4 phases | 7,776 |
| 5 | fusion-powerplant | energy | sigma=12 TF coils, n=6 heating beamlines, phi=2 dual containment | 7,776 |
| 6 | mind-upload | cognitive | n=6 cortical layers, sigma=12 Brodmann areas, phi=2 bio/digital | 7,776 |
| 7 | aramid | materials | n=6 benzene rings, sigma=12 GPa strength, phi=2 core-shell | 7,776 |
| 8 | taekwondo | culture | n=6 basic kicks, sigma=12 poomsae, tau=4 rounds | 7,776 |
| 9 | cosmology | physics | n=6 BBN nuclides, z_reion=6, sigma=12 CMB frequency | 7,776 |
| 10 | baduk | culture | n=6 maximum liberties, sigma=12 joseki, phi=2 black/white | 7,776 |

---

## Per-axis uncovered status

| Axis | Uncovered | Main uncovered domains |
|----|--------|---------------------|
| infra | 43 | architecture, climate, geology, meteorology, transportation, ... |
| compute | 38 | chip-3d/hexa1/sc/wafer, dram, exynos, vnand, hexa-* series, ... |
| life | 31 | genetics, immunology, pharmacology, synbio, vaccine, ... |
| physics | 26 | millennium-bsd/hodge/ns/p-vs-np/poincare, electromagnetism, ... |
| culture | 18 | hangul-script, music, photography, writing-systems, yoga, ... |
| cognitive | 17 | anima-service/soc, dream-recorder, hexa-dream/mind/neuro, ... |
| materials | 16 | ceramics, epoxy, gemology, nylon, paper, swordsmithing, ... |
| sf-ufo | 16 | cloak, dragon, fantasy, hexa-cloak/grav/hover/sim/teleport, ... |
| energy | 9 | pemfc, smr-datacenter, superconductor, thermal-management, ... |
| space | 6 | astronomy, hexa-cosmic, hexa-starship, observational-astronomy, ... |

---

## Priority recommendations (next pass)

### Tier 1 (remaining 5 Millennium problems)
- millennium-bsd, millennium-hodge, millennium-navier-stokes, millennium-p-vs-np, millennium-poincare

### Tier 2 (industrial cores)
- genetics, immunology, superconductor, pemfc, chip-3d

### Tier 3 (Korean culture/heritage)
- hangul-script, music, photography, archaeology

### Tier 4 (hexa-* expansion)
- hexa-dream, hexa-mind, hexa-neuro, hexa-cosmic, hexa-starship

---

## TOML structure standard

Per-TOML standard:
- `[meta]`: name, desc, levels (5 levels), vision
- `[scoring]`: n6=0.35, perf=0.25, power=0.20, cost=0.20
- 5 `[[level]]` x 6 `[[candidate]]` = 30 candidates = 7,776 combinations
- Each candidate: level, id, label, n6, perf, power, cost, notes
- n=6 connection: n=6, sigma=12, tau=4, phi=2, n/phi=3, sigma-tau=8, etc.
- `[[rule]]`: type (require/exclude), if_level, if_id, then_level, then_ids

---

## Core-identity link

sigma(n) * phi(n) = n * tau(n) iff n = 6

- sigma(6) = 12 (divisor sum: 1+2+3+6)
- phi(6) = 2 (Euler totient: 1, 5)
- tau(6) = 4 (divisor count: 1, 2, 3, 6)
- n = 6 (unique solution)
- Check: 12 * 2 = 24 = 6 * 4

Every DSE TOML maps this constant set (n=6, sigma=12, tau=4, phi=2) onto its design-space parameters.
