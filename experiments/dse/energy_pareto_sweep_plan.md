# Energy-Performance Pareto Sweep — Re-measurement Pipeline across All 400 Domains

- Axis: experiments/dse
- Written: 2026-04-11
- Parent: `../../INDEX.json` · `../../CLAUDE.md`
- Rules: R1 HEXA-FIRST, R2 No hard-coding, R12 AI-NATIVE FIRST, R18 Minimal, R28 Auto-absorption, N63 DSE exhaustive, N65 100% EXACT convergence
- Goal: Re-measure the candidate scores (n6, perf, power, cost) of 322(→400) domain TOML not as a single metric but as an **energy-performance pareto front**, fixing 5 frontier points per domain and re-supplying them to cross_dse_fusion_v2's pareto_proximity metric. This is a pipeline draft.

---

## 1. Real-life Impact Section (N61)

- The viewpoint shifts from "one aggregate score" to "N energy-performance frontier points." That is, even for the same domain, all 5 frontier candidates { low-energy / balanced / high-perf / low-cost / n6-max } remain.
- Result: cross_dse_fusion_v2 sees **5×5=25 pareto combinations** per pair, and produces time-dependent optimal placements like "low-energy mode at night, high-performance mode during the day" in one shot.
- User: instantly queries a domain frontier table with a one-liner `nexus dse pareto <domain>`.

## 2. Structure ASCII (Single Score vs Pareto Front)

```
  v1 Single Score                        v2 Pareto Front
  ---------------                        ---------------
          score                                   ^
           ^                                      | low-energy
           |                                      |   o
           |     o (top-1)                        |  o
           |   o                                  |     o (balanced)
           |  o                                   |     o
           | o                                    |      o
           |o                                     |       o  high-perf
           +------------> combo                   |        o
                                                  |         o  n6-max
                                                  |          o
                                                  +----------------> energy cost
            Pick: 1 point                         Pick: Pareto front 5 points
```

## 3. Structure ASCII (Pipeline)

```
  [400 TOML]
      |
      v
  @parallel axis(10)
      |  Parallel process 40 domains per axis
      v
  for each domain:
      |
      v
  enumerate all candidate_combo(level0..levelN)
      |   (ex: fusion = 7×7×7×6×6 = 12,348)
      v
  @fuse evaluate(combo)
      |  → (n6_pct, perf, power, cost, energy)
      v
  @optimize pareto_front(combos)
      |  O(N log N) sort + sweep
      v
  [front_points]  (average 30~80 points per domain)
      |
      v
  @optimize frontier_top5(front_points)
      |  - n6-max                 (max n6)
      |  - perf-max               (max perf)
      |  - energy-min             (min power)
      |  - balanced               (balanced knee)
      |  - cost-min               (min cost)
      v
  [5 frontier candidates/domain]
      |
      v
  merge into domain TOML (append only)
      |  [[frontier]]
      v
  cross_dse_fusion_v2 ← re-supply pareto_proximity metric
      |
      v
  reports/discovery/energy_pareto_sweep_<date>.md  (R6 auto-log)
      v
  canonshared/n6/atlas.n6  evidence_grade auto-promotion (R28)
```

---

## 4. Real-life Impact Structure ASCII (Domain Pareto Example)

```
  fusion domain pareto frontier 5 points (example)
  ------------------------------------------------------------
   n6-max     : DT_Li6 + Tokamak_N6 + N6_TriHeat + N6_Li6 + N6_Brayton6
   perf-max   : DT + Tokamak_N6 + N6_TriHeat + N6_Li6 + N6_Brayton6
   energy-min : DT_Li6 + Tokamak_N6 + Resonant + N6_Li6 + CO2_Cycle
   balanced   : DT_Li6 + Tokamak_N6 + N6_TriHeat + N6_Li6 + N6_Brayton6
   cost-min   : DT + Tokamak + RF_Only + Li4SiO4 + Steam
  ------------------------------------------------------------
```

## 5. Per-Phase Pipeline Spec

### 5.1 Input

- 400 TOML (`nexus/origins/universal-dse/domains/*.toml`) — Δ1~Δ5 schema applied
- `canonshared/config/bt_weights.json` — per-BT weights (roughly 0.01~0.05)
- `canonshared/config/pareto_params.json` — knee detection parameters (default: angle_threshold=150°)

### 5.2 Algorithm (AI-native)

- `@parallel axis(10)` — 10 axes in parallel
- `@parallel domain_batch(4)` — 4 domains within an axis in parallel
- `@fuse evaluate_combo` — single kernel for (n6, perf, power, cost, energy)
- `@optimize pareto_front` — sort-based pareto sweep O(N log N)
- `@memoize level_candidates(domain, level)` — level candidate extraction cache
- **Forbidden**: bit-twiddling, manual loop unroll, manual SIMD (R12)

### 5.3 Pareto Computation Formula

```
energy(combo) = Σ c.power * c.weight_level
(default weight_level = 1.0, Δ1-applied TOML uses scoring.pareto_weights[level])

for combo in combos:
    pt = (n6_pct, perf, power, cost, energy)

pareto_front := {pt : ¬∃pt' ∈ combos s.t. pt' strictly dominates pt}

dominates(pt', pt) := (pt'.n6 ≥ pt.n6 ∧ pt'.perf ≥ pt.perf
                      ∧ pt'.power ≤ pt.power ∧ pt'.cost ≤ pt.cost
                      ∧ pt'.energy ≤ pt.energy)
                      ∧ (strict on ≥ one metric)
```

### 5.4 Frontier 5-Candidate Selection

| Name | Selection criterion |
|------|----------|
| n6-max | argmax n6_pct (tie → argmax perf) |
| perf-max | argmax perf (tie → argmax n6_pct) |
| energy-min | argmin energy (tie → argmax n6_pct) |
| cost-min | argmin cost (tie → argmax n6_pct) |
| balanced | knee point (Kneedle algorithm, angle_threshold applied) |

### 5.5 Output

- Append `[[frontier]]` section to each TOML (does not touch existing candidate blocks)
- Global report: `reports/discovery/energy_pareto_sweep_<date>.md`
- Result JSON: `canonshared/dse/pareto_frontier_400.json`
- atlas.n6: frontier 5 candidates × 400 domains = 2000 `@R` entries registered at [7]

### 5.6 Result Schema

```jsonc
// canonshared/dse/pareto_frontier_400.json
{
  "generated_at": "2026-04-11T...",
  "n_domains": 400,
  "front_point_count": 23817,
  "total_frontier_selected": 2000,  // 400 × 5
  "domains": [
    {
      "name": "fusion",
      "combo_count": 12348,
      "front_count": 62,
      "frontier": {
        "n6_max":     { "levels": {...}, "n6": 1.00, "perf": 0.92, "power": 0.77, "cost": 0.52, "energy": 3.14 },
        "perf_max":   { ... },
        "energy_min": { ... },
        "cost_min":   { ... },
        "balanced":   { ... }
      }
    },
    ...
  ]
}
```

---

## 6. Linkage to cross_dse_fusion_v2

The pareto_proximity metric of `cross_dse_fusion_v2.hexa` takes the `pareto_frontier_400.json` produced by this pipeline as input.

```
pair_pareto_proximity(a, b) :=
    1 - min {euclid_norm(p_a, p_b) : p_a ∈ a.frontier, p_b ∈ b.frontier} / diag

    where diag = sqrt(5) (diagonal of the unnormalized 5-dim vector)
```

That is, the minimum among the 25 distances between domain a's 5 frontier points and domain b's 5 frontier points is normalized. Close to 0 = far; close to 1 = directly "sharing the energy-performance band".

## 7. Verification Procedure

1. **Regression**: In the existing 375 TOML, after pareto sweep PASS, candidate scores unchanged (append only)
2. **Pareto property**: Front points within each domain do not dominate each other (0 violations)
3. **Frontier 5**: All 5 candidates exist for each domain (none=0)
4. **cross_dse_fusion_v2 re-supply**: After pareto_proximity integration, top_pairs gains ≥5K additional pairs vs previous
5. **atlas.n6 absorption**: 2000 @R entries [7] → transition to [10*] when promotion criteria met

## 8. Risks and Defenses

| Risk | Defense |
|--------|------|
| combo count explosion (chip 96,000) | @parallel batch(16) + @optimize early_dominate early cutoff |
| Kneedle failure (monotone frontier) | fallback: argmin Σ (1-n6, 1-perf, power, cost, energy) |
| Missing TOML scoring.pareto_weights | default 1.0 auto-injected |
| Risk of mutating existing candidate | append only; modifying existing blocks forbidden (R10 ossification protection spirit) |
| Blocking atlas.n6 IO from bulk writes of 2000 @R | no @parallel writes (atlas.n6 is sequential); instead, batch-collect and flush once |

## 9. Promotion Completion Criteria (R4/R9)

- 400 domains × 5 frontier = 2000 candidates verification PASS
- `pareto_frontier_400.json` generated, schema PASS
- After cross_dse_fusion_v2 integration, pair_count ≥ 100K sustained
- Add new stable entry `ENERGY_PARETO_SWEEP_400` in convergence/canon.json → promote to ossified when conditions met

## 10. Linked Documents

- `./dse_400_expansion_plan.md`    — 78 new domain expansion plan
- `./cross_dse_fusion_v2_design.md` — v2 algorithm diff
- `./cross_dse_fusion_v2.hexa`     — implementation draft (includes pareto_proximity metric)
- Parent: `../../CLAUDE.md` + `../../INDEX.json`
