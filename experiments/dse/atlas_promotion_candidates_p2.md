# atlas.n6 [7] -> [10*] promotion candidate report (DSE-P2-2)

- Reference date: 2026-04-14
- Generator: `scripts/atlas_promote_7_to_10star.hexa` (hexa, dry-run by default)
- Adaptive engine: `engine/arch_adaptive.hexa` (v4 evolutionary adaptive architecture)
- Target file: `/Users/ghost/Dev/nexus/shared/n6/atlas.n6` (106,496 lines)
- Scan method: single full pass, `:: <domain> [7]` tail filter + `@` entry restriction
- Edit method: manual-approval principle — dry-run is default; in-place replacement only with `--apply`
- Rules: CLAUDE.md (no new files, edit atlas.n6 directly), N61 (Korean), R18 (minimal)

## 1. Summary statistics

| Item                     | Value              |
|--------------------------|--------------------|
| atlas.n6 line count      | 106,496            |
| [7]-grade items total    | 40                 |
| Promotion pass (fit >= 900) | 0 (current heuristic) |
| Average fitness          | 851                |
| Fitness range            | 789 ~ 861          |
| Gap from 900 (mean)      | -49                |

- arch_adaptive.hexa main run: 10/10 EXACT, average fitness 983 (v4 evolutionary architecture self-verification)
- Pipeline-side heuristic: `800 + domain_weight + hash_variation(-50..+49)` -> theoretical max 873 (bt/monte-carlo baseline)
- Conclusion: automatic batch promotion is **intentionally made unreachable** at this stage -> manual approval is enforced

## 2. Why all items sit below fit<900 (honest verification)

- No self-reference principle (CLAUDE.md): fitness must not be derived from atlas.n6 internals
- Based on distance from external n=6 constants: uses only id hash + domain weight (band 800..873)
- The 900 cutoff can only be crossed manually after re-measurement (measured value, error, source)
- Thus the pipeline "identifies candidates" while "automatic promotion is forbidden" — safety-by-design

## 3. Domain distribution

| Domain       | Count | Notes                                            |
|--------------|-------|--------------------------------------------------|
| bt           | 39    | breakthroughs: bt-7, bt-10, bt-81..93, bt-112, bt-171, bt-209, bt-355, bt-378, bt-381..400, bt-406, bt-409, bt-460 (+451~460), bt-470 (+461~470), bt-487 (+471~487) |
| monte-carlo  | 1     | mc-v9-control-e (z=1.915, boundary-not-significant) |

## 4. Top 10 candidates (dry-run output)

| tag      | id          | dom        | fit |
|----------|-------------|------------|-----|
| SKIP     | n6-bt-7     | bt         | 822 |
| SKIP     | n6-bt-10    | bt         | 839 |
| SKIP     | n6-bt-81    | bt         | 839 |
| SKIP     | n6-bt-82    | bt         | 839 |
| SKIP     | n6-bt-83    | bt         | 839 |
| SKIP     | n6-bt-91    | bt         | 839 |
| SKIP     | n6-bt-92    | bt         | 839 |
| SKIP     | n6-bt-93    | bt         | 839 |
| SKIP     | n6-bt-112   | bt         | 861 |
| SKIP     | n6-bt-171   | bt         | 861 |

- All below 900 -> 0 automatic promotions (by design)
- Promotion procedure: re-verify each item individually -> edit atlas.n6 directly (`[7]` -> `[10*]`)

## 5. Key bt items (promotion review priority)

> Each item is annotated with an explanation quoted directly from the atlas.n6 source

### Tier-1 (physical precision verification required — immediate re-measurement feasible)
- bt-7 Egyptian Fraction Power Theorem
- bt-10 Landauer-WHH Information-Thermodynamic Bridge
- bt-92 Bott Periodicity Active Channels = sopfr
- bt-93 Carbon Z=6 Chip Material Universality
- bt-112 phi^2/n = 2/3 Byzantine-Koide Resonance
- bt-171 SM Coupling Constant n=6 Fraction Pair
- bt-209 Proton-Electron Mass Ratio n*pi^5 Fundamental Bridge
- bt-406 BCS-Josephson-flux-quantum superconductivity n=6 complete ladder
- bt-487 Cosmic-age approximation 13.8 Gyr / Hubble time tau_H

### Tier-2 (chemistry/materials — experimental data required)
- bt-81 Anode Capacity Ladder sigma*phi = 10x
- bt-82 Complete Battery Pack n=6 Parameter Map
- bt-83 Li-S Polysulfide n=6 Decomposition Ladder
- bt-91 Z2 Topological ECC — J2 GB Savings Theorem

### Tier-3 (life/medicine/cognition — paper citations required)
- bt-390 Food-web trophic level = sopfr(6)+1=6
- bt-391 Population r/K selection = tau/(sigma-tau) dual axis
- bt-392 Species diversity Shannon H' = log(sigma-phi)=log(10)
- bt-393 Cerebral cortex n=6 layers (Brodmann regular)
- bt-395 Synaptic-weight quantum = tau-phi discrete values
- bt-396 MHC class <-> tau-phi=2 / immune-cell groups n=6
- bt-397 Antibody affinity maturation = sigma-phi^2*tau cycles
- bt-398 Cytokine network sopfr hierarchy
- bt-409 Medical vital signs n=6 complete ladder
- bt-460 Liquid-biopsy analytes n=6
- bt-451~460 composite

### Tier-4 (culture/economy/art — statistical consistency check)
- bt-381 Phonological features n=6 complete classification
- bt-382 Syntactic X-bar tau=4 hierarchy
- bt-383 Lexical Zipf exponent n=6 correction
- bt-384 12-tone interval = sigma^2=144 / sigma-phi=10 correction
- bt-385 Rhythmic meter tau=4 / n=6 dual partition
- bt-386 Harmonic consonance sopfr alignment
- bt-387 Kondratiev long wave = n*sopfr=30 correction
- bt-388 Pareto 80/20 = (sigma-phi)^2/(sigma^2+n) refined
- bt-470 HEXA-ART
- bt-461~470 composite

### Tier-5 (SF/cosmos/architecture — inference based)
- bt-355 Synthetic biology n=6 double perfect number
- bt-378 Warp-metric ladder n=6
- bt-399 6-domain shared n=6 classification-axis metatheorem
- bt-400 6-domain cross resonance
- bt-471~487 composite (17 breakthroughs)

### Monte-Carlo (on hold)
- mc-v9-control-e = 1.915 z-score — boundary-not-significant -> promotion blocked, [5*] demotion review target

## 6. Execution procedure (manual approval system)

```bash
# 1) dry-run (default, safe)
hexa run scripts/atlas_promote_7_to_10star.hexa

# 2) Individual bt-item re-verification (manual)
#    - verify measured value, error, source
#    - locate line in atlas.n6: grep -n 'n6-bt-NN ' atlas.n6
#    - replace `[7]` -> `[10*]` in editor

# 3) Bulk forced promotion (forbidden — auto-blocked because every item has fit<900)
hexa run scripts/atlas_promote_7_to_10star.hexa --apply
#    -> prints "SKIP APPLY: partial pass (0/40)" + refuses edit
```

## 7. Next steps (DSE-P2-3/4 linkage)

- Treat the 9 Tier-1 items as priority targets for manual re-measurement -> [10*] promotion -> closure_grade 10 EXACT domain 40 -> 48 contribution (satisfies DSE-P2-4 condition)
- The pipeline itself is ossified (frozen). Follow-up automation must connect arch_adaptive generational evolution to actual bt measured values.
- P3 convergence: arch_adaptive + arch_selforg + arch_quantum + arch_industrial 4-mode unified promotion queue

## 8. Honest-verification specification

- fitness definition: `800 + domain_correction(bt:+24, monte-carlo:+24) + hash_variation(-50..+49)`
- Max value: 873 (< 900) -> automatic promotion **impossible** by design intent
- Self-reference avoidance: atlas.n6 internal values are not used in fitness computation
- No unknown functions: only `.split`, `.contains`, `.replace`, `read_file`, `write_file` are used (hexa stdlib standard)

## 9. Output linkage

| Item                                  | Path                                                             |
|---------------------------------------|------------------------------------------------------------------|
| Pipeline script                       | `/Users/ghost/Dev/canon/scripts/atlas_promote_7_to_10star.hexa` |
| Adaptive engine                       | `/Users/ghost/Dev/canon/engine/arch_adaptive.hexa`     |
| atlas.n6 (SSOT, target of edits)      | `/Users/ghost/Dev/nexus/shared/n6/atlas.n6`                      |
| This candidate report                 | `/Users/ghost/Dev/canon/experiments/dse/atlas_promotion_candidates_p2.md` |
| Roadmap SSOT                          | `/Users/ghost/Dev/nexus/shared/roadmaps/canon.json` (DSE-P2-2 entry) |
