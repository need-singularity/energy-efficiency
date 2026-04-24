# DSE-P3-2 cross_matrix v3 Summary (112 × 10 × 77)

- Publication date: 2026-04-14
- Reproduction seed: 42
- Total cells: 86,240 / target 86,240
- Coverage: 100.0%
- Parent: experiments/dse/cross_matrix_112x10.json (P1 1,120 cells)
- Source definition: 7 technique sections × 11 source categories = 77 (frozen at P3)

## Dimensions
- tech: 112 (attention 14, moe 6, optim 37, sparse 5, graph 4, compress 9, arch 37)
- domain: 10 (cognitive, compute, culture, energy, infra, life, materials, physics, sf-ufo, space)
- source: 77 = 7 sections × 11 cats
  - sections: attention, moe, optim, sparse, graph, compress, arch
  - cats: atlas, papers, techniques, experiments, engine, theory, domains, reports, bridge, products, rules

## fit Distribution Histogram (10 bins)
```
[0.3~0.4)     14   0.02%  ································
[0.4~0.5)  2,351   2.73%  ███·····························
[0.5~0.6) 11,066  12.83%  ████████████████················
[0.6~0.7) 20,569  23.85%  █████████████████████████████···
[0.7~0.8) 22,583  26.19%  ████████████████████████████████
[0.8~0.9) 17,474  20.26%  █████████████████████████·······
[0.9~1.0) 12,183  14.13%  █████████████████···············
```

- Mean fit: 0.7434
- Median: 0.739
- Standard deviation: 0.1342
- Min/Max: 0.3714 / 1.0

## alien_idx Distribution
```
alien= 4       6  ································
alien= 5     790  █·······························
alien= 6   5,350  █████████·······················
alien= 7  12,396  █████████████████████···········
alien= 8  17,732  ██████████████████████████████··
alien= 9  18,683  ████████████████████████████████
alien=10  15,147  ██████████████████████████······
alien=11   9,541  ████████████████················
alien=12   6,495  ███████████·····················
alien=13     100  ································
```

## Domain Mean fit
```
   compute  0.8852  ████████████████████████████████
     infra  0.8128  █████████████████████████████···
   physics  0.7946  █████████████████████████████···
 cognitive  0.7826  ████████████████████████████····
      life  0.7388  ███████████████████████████·····
    energy  0.7382  ███████████████████████████·····
 materials  0.7289  ██████████████████████████······
     space  0.7273  ██████████████████████████······
    sf-ufo  0.6238  ███████████████████████·········
   culture  0.6016  ██████████████████████··········
```

## Top 10 (tech, domain, source) Pairs
| rank | tech | domain | source | fit | alien_idx |
|---:|---|---|---|---:|---:|
| 1 | adamw_quintuplet | infra | moe::techniques | 1.0 | 13 |
| 2 | adamw_quintuplet | infra | moe::engine | 1.0 | 13 |
| 3 | adamw_quintuplet | infra | moe::rules | 1.0 | 13 |
| 4 | adamw_quintuplet | infra | optim::rules | 1.0 | 13 |
| 5 | adamw_quintuplet | infra | arch::theory | 1.0 | 13 |
| 6 | adamw_quintuplet | infra | arch::reports | 1.0 | 13 |
| 7 | adamw_quintuplet | infra | arch::rules | 1.0 | 13 |
| 8 | bitnet | infra | graph::atlas | 1.0 | 13 |
| 9 | bitnet | infra | graph::engine | 1.0 | 13 |
| 10 | bitnet | infra | compress::theory | 1.0 | 13 |

## Top 10 Sources (by mean fit, descending)
| rank | source | avg_fit |
|---:|---|---:|
| 1 | arch::papers | 0.7624 |
| 2 | optim::products | 0.762 |
| 3 | compress::atlas | 0.7586 |
| 4 | attention::reports | 0.7585 |
| 5 | arch::experiments | 0.7581 |
| 6 | arch::domains | 0.7555 |
| 7 | arch::reports | 0.7549 |
| 8 | compress::bridge | 0.754 |
| 9 | moe::domains | 0.7527 |
| 10 | sparse::theory | 0.7518 |

## Publication
- Full tensor: experiments/dse/cross_matrix_v3_full.json (6.34 MB, 86,240 cells)
- Compressed copy: nexus/shared/dse/dse_cross_results_v3.json (16.2 KB)
- Summary: experiments/dse/cross_matrix_v3_summary.md (this document)

## Verification
- Cell count match: 86240 == 86,240 -> PASS
- tech count: 112 == 112 -> PASS
- domain count: 10 == 10 -> PASS
- source count: 77 == 77 -> PASS
- Coverage: 100.0% == 100% -> PASS
