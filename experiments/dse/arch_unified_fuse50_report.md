# DSE-P4-2 — arch_unified 4-mode fuse simulation (top 50 cells)

**Date**: 2026-04-14  
**Engine**: `engine/arch_unified.hexa` (INDUSTRIAL / QUANTUM / SELFORG / ADAPTIVE)  
**Source**: `cross_matrix_v3_full.json` — top 50 by fit (descending) out of 86,240 cells  
**seed**: 42  
**Rule**: pick 2 modes per fit band -> weighted-sum hybrid_score

## Mapping rules (fit -> mode pair)

Primary branching uses the fit band; sub-branching uses the deterministic hash `hash(tech|domain) % 3` to distribute mode_b across 3 lanes (preserving tie diversity).

| fit band | mode_a | mode_b candidates (sub=0/1/2) | Intent |
|---|---|---|---|
| > 0.9 | INDUSTRIAL (w=7) | QUANTUM / ADAPTIVE / SELFORG | Fixed main axis + diverse exploration |
| 0.8~0.9 | QUANTUM (w=4) | ADAPTIVE / SELFORG / INDUSTRIAL | Uncertainty evolution |
| 0.7~0.8 | SELFORG (w=5) | ADAPTIVE / INDUSTRIAL / QUANTUM | Static emergence reinforcement |
| <= 0.7 | SELFORG (w=5) | INDUSTRIAL / QUANTUM / ADAPTIVE | Low-confidence conservative blend |

## Mode pair distribution (top 50 cells)

| Mode pair | Count | Ratio |
|---|---|---|
| INDUSTRIAL+QUANTUM | 26 | 52% |
| INDUSTRIAL+ADAPTIVE | 24 | 48% |

## Top 10 hybrid_score

| Rank | cell_idx | tech | domain | fit | Mode pair | hybrid |
|---|---|---|---|---|---|---|
| 29 | 84 | `additive_attention` | compute | 1.0000 | INDUSTRIAL+ADAPTIVE | 869 |
| 43 | 120 | `additive_attention` | compute | 1.0000 | INDUSTRIAL+ADAPTIVE | 869 |
| 47 | 129 | `additive_attention` | compute | 1.0000 | INDUSTRIAL+ADAPTIVE | 869 |
| 34 | 94 | `additive_attention` | compute | 1.0000 | INDUSTRIAL+ADAPTIVE | 862 |
| 39 | 112 | `additive_attention` | compute | 1.0000 | INDUSTRIAL+ADAPTIVE | 862 |
| 44 | 121 | `additive_attention` | compute | 1.0000 | INDUSTRIAL+ADAPTIVE | 862 |
| 35 | 95 | `additive_attention` | compute | 1.0000 | INDUSTRIAL+ADAPTIVE | 855 |
| 37 | 104 | `additive_attention` | compute | 1.0000 | INDUSTRIAL+ADAPTIVE | 855 |
| 48 | 131 | `additive_attention` | compute | 1.0000 | INDUSTRIAL+ADAPTIVE | 855 |
| 30 | 87 | `additive_attention` | compute | 1.0000 | INDUSTRIAL+ADAPTIVE | 848 |

## Full table of 50 cells

| # | cell_idx | tech | domain | source | fit | alien | mode_a(wa) | mode_b(wb) | score_a | score_b | hybrid |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 4 | `additive_attention` | cognitive | `attention::engine` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 910 | 385 | 752 |
| 2 | 5 | `additive_attention` | cognitive | `attention::theory` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 900 | 370 | 741 |
| 3 | 7 | `additive_attention` | cognitive | `attention::reports` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 880 | 340 | 718 |
| 4 | 10 | `additive_attention` | cognitive | `attention::rules` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 850 | 295 | 683 |
| 5 | 12 | `additive_attention` | cognitive | `moe::papers` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 920 | 400 | 764 |
| 6 | 13 | `additive_attention` | cognitive | `moe::techniques` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 910 | 385 | 752 |
| 7 | 15 | `additive_attention` | cognitive | `moe::engine` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 890 | 355 | 729 |
| 8 | 17 | `additive_attention` | cognitive | `moe::domains` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 870 | 325 | 706 |
| 9 | 18 | `additive_attention` | cognitive | `moe::reports` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 860 | 310 | 695 |
| 10 | 19 | `additive_attention` | cognitive | `moe::bridge` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 850 | 295 | 683 |
| 11 | 23 | `additive_attention` | cognitive | `optim::papers` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 900 | 370 | 741 |
| 12 | 25 | `additive_attention` | cognitive | `optim::experiments` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 880 | 340 | 718 |
| 13 | 27 | `additive_attention` | cognitive | `optim::theory` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 860 | 310 | 695 |
| 14 | 29 | `additive_attention` | cognitive | `optim::reports` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 840 | 280 | 672 |
| 15 | 35 | `additive_attention` | cognitive | `sparse::techniques` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 870 | 325 | 706 |
| 16 | 37 | `additive_attention` | cognitive | `sparse::engine` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 850 | 295 | 683 |
| 17 | 38 | `additive_attention` | cognitive | `sparse::theory` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 840 | 280 | 672 |
| 18 | 40 | `additive_attention` | cognitive | `sparse::reports` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 910 | 385 | 752 |
| 19 | 43 | `additive_attention` | cognitive | `sparse::rules` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 880 | 340 | 718 |
| 20 | 44 | `additive_attention` | cognitive | `graph::atlas` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 870 | 325 | 706 |
| 21 | 47 | `additive_attention` | cognitive | `graph::experiments` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 840 | 280 | 672 |
| 22 | 55 | `additive_attention` | cognitive | `compress::atlas` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 850 | 295 | 683 |
| 23 | 56 | `additive_attention` | cognitive | `compress::papers` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 840 | 280 | 672 |
| 24 | 58 | `additive_attention` | cognitive | `compress::experiments` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 910 | 385 | 752 |
| 25 | 64 | `additive_attention` | cognitive | `compress::products` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 850 | 295 | 683 |
| 26 | 73 | `additive_attention` | cognitive | `arch::reports` | 1.0000 | 12 | INDUSTRIAL(7) | QUANTUM(3) | 850 | 295 | 683 |
| 27 | 81 | `additive_attention` | compute | `attention::engine` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 860 | 750 | 827 |
| 28 | 82 | `additive_attention` | compute | `attention::theory` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 850 | 750 | 820 |
| 29 | 84 | `additive_attention` | compute | `attention::reports` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 920 | 750 | 869 |
| 30 | 87 | `additive_attention` | compute | `attention::rules` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 890 | 750 | 848 |
| 31 | 89 | `additive_attention` | compute | `moe::papers` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 870 | 750 | 834 |
| 32 | 90 | `additive_attention` | compute | `moe::techniques` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 860 | 750 | 827 |
| 33 | 92 | `additive_attention` | compute | `moe::engine` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 840 | 700 | 798 |
| 34 | 94 | `additive_attention` | compute | `moe::domains` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 910 | 750 | 862 |
| 35 | 95 | `additive_attention` | compute | `moe::reports` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 900 | 750 | 855 |
| 36 | 96 | `additive_attention` | compute | `moe::bridge` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 890 | 750 | 848 |
| 37 | 104 | `additive_attention` | compute | `optim::theory` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 900 | 750 | 855 |
| 38 | 106 | `additive_attention` | compute | `optim::reports` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 880 | 750 | 841 |
| 39 | 112 | `additive_attention` | compute | `sparse::techniques` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 910 | 750 | 862 |
| 40 | 114 | `additive_attention` | compute | `sparse::engine` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 890 | 750 | 848 |
| 41 | 115 | `additive_attention` | compute | `sparse::theory` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 880 | 750 | 841 |
| 42 | 117 | `additive_attention` | compute | `sparse::reports` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 860 | 750 | 827 |
| 43 | 120 | `additive_attention` | compute | `sparse::rules` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 920 | 750 | 869 |
| 44 | 121 | `additive_attention` | compute | `graph::atlas` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 910 | 750 | 862 |
| 45 | 124 | `additive_attention` | compute | `graph::experiments` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 880 | 750 | 841 |
| 46 | 126 | `additive_attention` | compute | `graph::theory` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 860 | 750 | 827 |
| 47 | 129 | `additive_attention` | compute | `graph::bridge` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 920 | 750 | 869 |
| 48 | 131 | `additive_attention` | compute | `graph::rules` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 900 | 750 | 855 |
| 49 | 132 | `additive_attention` | compute | `compress::atlas` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 890 | 750 | 848 |
| 50 | 133 | `additive_attention` | compute | `compress::papers` | 1.0000 | 12 | INDUSTRIAL(7) | ADAPTIVE(3) | 880 | 750 | 841 |

## hybrid_score statistics

- min: 672
- max: 869
- mean: 774.1

## Verification notes

- The computation ports `run_pipeline`/`fuse_modes`/`mode_weight` from `arch_unified.hexa` 1:1 into Python (integer arithmetic only).
- No arbitrary values beyond the n=6 constants (sigma=12, tau=4, phi=2, sopfr=5).
- cross_matrix_v3_full.json source untouched (read-only).
- seed=42, stable sort -> reproducible.
