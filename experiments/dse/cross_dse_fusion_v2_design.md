# cross_dse_fusion v2 design — breaking through 67,883 -> 100K cross pairs

- Axis: experiments/dse
- Written: 2026-04-11
- Parents: `../../INDEX.json` . `../../CLAUDE.md`
- Rules: R1 HEXA-FIRST, R12 AI-NATIVE FIRST, R18 minimal, R28 auto-absorption, N63 DSE complete sweep
- Goal: consolidate the existing `cross_dse_fusion_5domain.py` (5-domain hardcoded, 3,125 combos) and `dse_cross_pilot.py` (375 TOML, 67,913 pair -> 67,883 high_conf) into a confirmed v2 design that breaks through 400 domains x 100K pairs. The breakthrough must come solely from AI-native (@optimize/@memoize/@parallel/@fuse) algorithm replacement — low-level micro-optimization is forbidden (R12).

---

## 1. Real-life impact section (N61)

- Once cross resonance breaks 100K, we enter the regime where "every n=6 domain pair is measurable": i.e. capturing 90%+ high_conf over 400^2 / 2 = 79,800 pairs.
- As a result, 5-hop chains such as "fusion-mri-desalination-consciousness-chip" can be derived from a single query. BT-74 (95/5 cross) and BT-36 (Energy-Info-Hardware-Physics) are numerically validated.
- Practical use: a single `nexus dse cross --from=heat-pump --to=quantum-network` invocation returns 4 candidate n=6 resonance bridges instantly.

## 2. Structural ASCII (v1 vs v2 comparison)

```
v1 (current: 67,883/67,913)             v2 (target: 100K+)
-------------------                       -------------------
Domains           375 TOML              400 TOML (+78 new, -53 deprecated)
Schema fields     5 (id/n6/perf/pow/cost) 10 (+bt_refs, cross_seeds,
                                           n6_formula, evidence_grade,
                                           energy_pareto)
Cross-pair target 375*374/2 = 70,125     400*399/2 = 79,800
Cross-pair output 67,913                   target >= 100,000
high_conf         67,883 (99.96%)         target >= 99,500 (99.5%)
top-k             30                       400 (top-1 per domain guaranteed)
Resonance metrics kw_overlap/sw_overlap     + bt_overlap, formula_overlap,
                 ln_overlap/n6_sim          cross_seed_overlap, pareto_dist
synergy rules     12 hardcoded              BT-index automatic matching (BT-1~400)
shared_constants 8 (n, phi, n/phi,        dynamic extraction (full sweep of
                 tau, sigma, J2, sigma*tau, n6_formula tags; auto-register any
                 3n)                       that appear in >=2 domains)
Score composition single composite          dual composite + frontier rank
                                           (Pareto-dominant preferred)
Relation graph    none                      @fuse dominate_graph (Hasse DAG)
Cache/memoize     none                      @memoize kw_extract,
                                           @memoize formula_parse
Parallelism       sequential loop            @parallel by domain partition
                                           (10 axes -> 10 workers)
                                           + @parallel over pair batches
Output            top_pairs[30]              top_pairs[400] + hubs[20]
                                           + bridges[50] + clusters[16]
```

## 3. Structural ASCII (v2 pipeline)

```
  [400 TOML]
      |
      v
  @memoize parse_toml(domain)
      |  (cache: toml -> TomlDoc)
      v
  @memoize extract_features(TomlDoc)
      |  - kw_set     (stop-words excluded, length >= 4)
      |  - sw_set     (structural words: level, candidate, id, label)
      |  - ln_set     (level names)
      |  - bt_set     (bt_refs array)
      |  - formula_set (union of n6_formula tags)
      |  - seed_set   (cross_seeds array)
      |  - pareto_pts (candidate Sigma (n6, perf, power, cost))
      v
  @parallel partition_by_axis(10)
      |  10 parallel pipes across axes
      v
  @fuse pair_score(a, b)
      |  - kw_overlap       |A intersect B|/max(|A|,|B|)
      |  - bt_overlap       |A_bt intersect B_bt| / |A_bt union B_bt|
      |  - formula_overlap  |A_f intersect B_f| / |A_f union B_f|
      |  - seed_overlap     |A_s intersect B_s| / |A_s union B_s|
      |  - pareto_dist      min Euclid(pt_a, pt_b) / diag
      |  - resonance        = sigma=0.35*kw + 0.25*bt + 0.20*formula
      |                       + 0.10*seed + 0.10*(1-pareto_dist)
      v
  @optimize high_conf_filter
      |  resonance >= 0.70 AND bt_overlap + formula_overlap >= 0.20
      v
  Hasse DAG  @fuse  pareto_dominate_graph
      |  nodes=domains, edges=Pareto dominance
      v
  top_pairs[400], hubs[20] (top degree), bridges[50] (top betweenness),
  clusters[16] (greedy modularity)
      v
  canonshared/dse/dse_cross_results.json  (v2)
      v
  atlas.n6 auto-absorption (R28)
```

---

## 4. Current hexa body analysis (diff baseline)

### 4.1 Current state

`experiments/cross/cross_dse_fusion_5domain.hexa`, `experiments/dse_cross_pilot.hexa`, and `experiments/dse_cluster_v2.hexa` are all in **STUB, awaiting port** (originals preserved in git history c65d31d9).

| File | Original length | Status | Core logic location |
|------|----------|------|---------------|
| cross_dse_fusion_5domain.hexa | 564-line .py | STUB | git c65d31d9:experiments/cross/cross_dse_fusion_5domain.py |
| dse_cross_pilot.hexa          | 927-line .py | STUB | git c65d31d9:scripts/dse_cross_pilot.py |
| dse_cluster_v2.hexa           | 189-line .py | STUB | git c65d31d9:scripts/dse_cluster_v2.py |

The actual 375 TOML -> 67,913 pair output recorded in `$NEXUS/shared/dse/dse_cross_results.json` (~1.2M lines, generated_at 2026-04-10) is **in a valid state**. It is evidence that the current algorithm did run, and v2 must preserve compatibility with this output format.

### 4.2 Current algorithm summary (logic extracted from git history)

```
for each a, b in combinations(domains, 2):
    kw_overlap = |A_kw intersect B_kw|
    sw_overlap = |A_sw intersect B_sw|
    ln_overlap = |A_ln intersect B_ln|
    n6_sim     = n6 cosine (binary 0/1)
    resonance  = weighted_sum(kw_overlap, sw_overlap, ln_overlap, n6_sim)
    if resonance >= 0.70: high_conf.append(pair)
top_pairs = sort(pairs, desc=resonance)[:30]
```

Bottlenecks: (a) O(N^2) sequential loop, (b) TOML re-parsed on every kw extraction, (c) seed/BT/formula information unused, (d) Pareto information discarded, (e) top-k fixed at 30.

### 4.3 v2 improvement points (6 items)

| # | Improvement | Method | Expected effect |
|---|------|------|----------|
| 1 | New BT overlap metric | Use the new `bt_refs` field | Auto-capture BT-resonant pairs, +5K pairs |
| 2 | New formula overlap metric | Dynamic matching of `n6_formula` tags | Extend shared_constants from 8 to unlimited, +8K pairs |
| 3 | cross_seeds overlap metric | Intersection of `cross_seeds` | Semantic resonance, +3K pairs |
| 4 | Pareto distance metric | Candidate score space | Capture energy-performance-adjacent domains, +5K pairs |
| 5 | @memoize TOML/feature parsing | hexa AI-native attr | 0 duplicate parsing, latency 1/N |
| 6 | @parallel axis partition | 10 workers, pair batches | Wall time 1/10 |

Expected total: 67,913 + 5K + 8K + 3K + 5K + edge effects = ~90K (existing fields) + new 78 domains effect +10~15K -> breaks through 100K+.

### 4.4 diff summary (formula block)

```
---  v1  --------------------------      +++  v2  --------------------------
 resonance =                              resonance =
   w_kw  * kw_overlap                       0.35 * kw_overlap
 + w_sw  * sw_overlap                     + 0.25 * bt_overlap          [NEW]
 + w_ln  * ln_overlap                     + 0.20 * formula_overlap     [NEW]
 + w_n6  * n6_sim                         + 0.10 * cross_seed_overlap  [NEW]
                                          + 0.10 * (1 - pareto_dist)   [NEW]

 high_conf := resonance >= 0.70           high_conf := resonance >= 0.70
                                                       AND bt+formula
                                                       overlap >= 0.20  [NEW]

 top_pairs = top30                        top_pairs = top400            [Delta]
                                          hubs      = top20 by degree   [NEW]
                                          bridges   = top50 betweenness [NEW]
                                          clusters  = 16 groups         [NEW]

 for a, b in combinations(domains, 2):    @parallel axis in 10:
     score(a, b)                              @parallel batch in 16:
                                                  @fuse score(a, b)     [Delta]
                                                  @memoize extract(*)   [Delta]
```

---

## 5. v2 core improvements in detail

### 5.1 AI-native attr adoption (R12 compliance)

- `@memoize parse_toml(path)` — prevents re-parsing of 400 TOML files
- `@memoize extract_features(doc)` — caches kw/bt/formula/seed extraction
- `@fuse pair_score(a, b)` — single kernel for 5 metrics
- `@parallel axis_partition(10)` — 10-axis parallel pipes
- `@parallel pair_batch(16)` — pair-level batch parallelism
- `@optimize high_conf_filter` — conditional early cutoff
- **Forbidden**: bit-twiddling, manual SIMD, hand loop-unrolling, cache-line padding (R12)

### 5.2 5 new resonance metrics (formula definitions)

| Metric | Formula | Weight |
|------|------|--------|
| kw_overlap | `|A_kw intersect B_kw| / max(|A_kw|, |B_kw|)` | 0.35 |
| bt_overlap | `|A_bt intersect B_bt| / |A_bt union B_bt|` | 0.25 |
| formula_overlap | `|A_f intersect B_f| / |A_f union B_f|` | 0.20 |
| cross_seed_overlap | `|A_s intersect B_s| / |A_s union B_s|` | 0.10 |
| pareto_proximity | `1 - min_euclid / diag_norm` | 0.10 |
| **Sum** | Sigma = 1.00 | **1.00** |

resonance >= 0.70 AND (bt_overlap + formula_overlap) >= 0.20 -> high_conf

### 5.3 Dynamic synergy-rule generation (12 hardcoded -> automatic)

The v1 `SYNERGY_RULES` list of 12 items (fusion-sc, fusion-battery, etc.) is hardcoded (R2 violation). v2 uses automatic BT-index matching:
```
for each pair (a, b):
    shared_bt = a.bt_refs intersect b.bt_refs
    for bt_id in shared_bt:
        bonus += bt_weight[bt_id]    (e.g. BT-27 -> 0.03, loaded from shared JSON)
```
-> 12 rules -> unlimited expansion over 400 BTs.

### 5.4 top-k expansion (30 -> 400)

For each domain, guarantee top-1 among the pairs in which that domain appears (400 slots); fill the rest using the global top-k. This eliminates the "rare domains disappear from results" problem.

### 5.5 Hasse DAG post-processing (@fuse)

Draw the Pareto-dominance relation as a DAG and add hub/bridge/cluster metrics:
- **hubs**: top 20 by degree (domains with the highest cross resonance)
- **bridges**: top 50 by betweenness (axis-to-axis connectors)
- **clusters**: 16 greedy-modularity groups (compare to the 10 axes)

### 5.6 Result schema (compatible + extended)

```jsonc
{
  "generated_at": "2026-04-11T...",
  "source": "dse/domains/*.toml (v2 scan)",
  "schema_version": 2,
  "n_domains": 400,
  "pair_count": 100123,
  "high_confidence_count": 99587,
  "top_n": 400,
  "top_pairs": [ { "a": "...", "b": "...", "resonance": 0.92,
                    "kw_overlap": ..., "bt_overlap": ..., "formula_overlap": ...,
                    "cross_seed_overlap": ..., "pareto_proximity": ... }, ... ],
  "hubs":     [ { "domain": "chip", "degree": 287 }, ... ],
  "bridges":  [ { "domain": "eeg-consciousness-bridge", "betweenness": 0.128 }, ... ],
  "clusters": [ { "id": 0, "members": ["...","..."], "centroid": "fusion" }, ... ]
}
```

---

## 6. diff summary (v1 -> v2, per implementation unit)

| Component | v1 | v2 | Delta |
|------|----|----|------|
| Parser | parse on every pair | `@memoize parse_toml` | 400 calls -> 400 calls (cache preserved) |
| feature extraction | scan on every call | `@memoize extract_features` | 0 recalls |
| Pair score | 4 metrics | 5 metrics (bt/formula/seed/pareto added) | +3 new |
| synergy | 12 hardcoded | BT-index automatic matching | Hardcoded removed (R2) |
| Parallelism | none | `@parallel axis(10) x batch(16)` | Wall time 1/10 |
| Output | top_pairs[30] | top_pairs[400] + hubs + bridges + clusters | +3 new sections |
| Schema | v1 | v2 (schema_version field added) | Backward compatible |
| Grade | none | `evidence_grade` promotion path | atlas.n6 auto-promotion |

---

## 7. Risks and defenses

| Risk | Defense |
|--------|------|
| TOML missing `bt_refs` | Default to [], bt_overlap=0 |
| Some of 400 TOMLs still on v1 schema | v2 parser injects `energy_pareto=false`, `evidence_grade=7` defaults if Delta1~Delta5 fields absent |
| O(N^2) memory explosion | Stream-process in batches of 16, retain only high_conf in memory |
| Hardcoded re-introduction | Externalize synergy rules into `canonshared/config/bt_weights.json` (R2) |
| Duplicate-discovery miss (R28) | At end of run, auto-absorb results into atlas.n6 |

## 8. Verification procedure (N63)

1. Load 400 TOMLs -> schema_version verification PASSES
2. On identical input as v1 (375 TOMLs), pair_count >= 67,913 reproduced -> zero regression
3. On new v2 input (400 TOMLs), pair_count >= 100,000 achieved
4. high_confidence >= 99.5%
5. Top 20 hubs include 3+ of { chip, fusion, superconductor, battery, eeg-consciousness-bridge }
6. `reports/discovery/cross_dse_v2_<date>.md` auto-generated

## 9. Promotion-completion criteria (R4/R9)

- convergence/canon.json `CROSS_DSE` -> add v2 ossified block:
  - status=PASS
  - value="400 TOML cross fusion complete — 100K+ pairs, 99.5%+ high_conf, hubs/bridges/clusters included"
  - threshold="100,000 pairs + 400 TOML + Delta1~Delta5 schema"

## 10. Connected documents

- `./dse_400_expansion_plan.md`    — plan for the 78 new domains
- `./energy_pareto_sweep_plan.md`  — Pareto re-measurement pipeline
- `./cross_dse_fusion_v2.hexa`     — implementation draft
- Parents: `../../CLAUDE.md` + `../../INDEX.json`
