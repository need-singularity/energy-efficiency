# Discovery Engine Design Spec

**Date**: 2026-04-03
**Status**: Draft
**Goal**: auto-discovery engine that uses the n=6 framework to predict new materials / new technologies

---

## 1. Background

11 domains have reached level 10, confirming the physical ceiling (Mk.V).
Transition from "proof mode" (n=6 is here too) to "discovery mode" (use n=6 to predict things that do not yet exist).

Existing infrastructure:
- telescope-rs: 22 lenses (Rust, 6,045 lines, 58/58 tests passing)
- OUROBOROS: infinite discovery loop (Python, 5,996 lines, v25)
- universal-dse: 322 TOML domains, 5.9M+ combinations
- 35 Rust calculators

---

## 2. System overview

```
┌──────────────────────────────────────────────────────────┐
│          Discovery Engine (OUROBOROS v26)                 │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  Domain Encoder ──→ Telescope v2 (80 lenses) ──→        │
│       (Rust+TOML)      (Rust+wgpu)                      │
│                              │                           │
│                              ▼                           │
│  Materials DB ──→ Discovery Verifier ──→ Recorder       │
│     (JSON/SQLite)    (Rust)              │               │
│                                          ▼               │
│  Telescope History ←── OUROBOROS Loop ──→ Predictions   │
│     (JSON sharded)     (Python+Rust)     (JSON+MD)      │
│                              │                           │
│                              ▼                           │
│                      Cross-Domain Map                    │
│                         (JSON)                           │
└──────────────────────────────────────────────────────────┘
```

---

## 3. Component details

### 3.1 Telescope v2 — 80 lenses

**Structure**: 12 shared kernels + 80 combinator layers

#### 3.1.1 Shared kernels (GPU/CPU)

| # | Kernel | Lens count | Execution |
|---|------|------------|----------|
| 1 | distance_matrix (N×N pairwise) | ~20 | GPU |
| 2 | eigen_decomp (Jacobi/power iteration) | ~10 | GPU |
| 3 | mi_matrix (D×D mutual information) | ~15 | GPU |
| 4 | fft (DFT) | ~5 | GPU |
| 5 | knn_indices (k-nearest neighbors) | ~12 | GPU |
| 6 | gradient_hessian (numerical differentiation) | ~8 | GPU |
| 7 | histogram (binned counting) | ~15 | CPU |
| 8 | graph_ops (BFS/community) | ~12 | CPU |
| 9 | simulation_step (iterative) | ~6 | GPU |
| 10 | clustering (mean-shift/DBSCAN) | ~6 | CPU |
| 11 | regression (log-log/logistic) | ~8 | CPU |
| 12 | interpolation (interp/extrap) | ~4 | CPU |

#### 3.1.2 80 lenses (8 categories)

**I. Analysis (22, existing)** — see what is there
consciousness, topology, causal, gravity, thermo, wave,
em, evolution, info, quantum, quantum_microscope, ruler,
triangle, compass, mirror, scale, stability, network,
memory, recursion, boundary, multiscale

**II. Exploration (3)** — find what is missing
- void: k-NN density → low-density regions surrounded by high density → empty center + expected spec
- isomorphism: domain A/B graph → VF2 subgraph isomorphism → mapping + transfer candidates
- extrapolation: polynomial/exponential/power-law fit (AIC) → Mk.V extrapolation + confidence interval

**III. Synthesis (3)** — how to fill
- inverse: target spec → KNN inverse search + Jacobian back-track → required inputs + sensitivity
- combinatorial: existing combo DB → full-space complement → untried combos + promise score
- frustration: spin-glass energy → pairs of constraints that cannot be simultaneously satisfied → Pareto compromise

**IV. Verification (3)** — is this really new
- emergence: Shapley interaction → detect non-additive synergy
- periodicity: integer lattice fitting → empty slot prediction (periodic-table style)
- completeness: Voronoi partition → cell size distribution → unexplored ratio + location

**V. Quality (3)** — how valuable
- surprise: KL divergence → novelty score vs existing
- falsification: per-assumption sensitivity → weakest link
- duality: Fourier/Legendre transform → hidden equivalence

**VI. Materials-specific (3)**
- defect: controlled perturbation → points where a defect improves performance
- interface: boundary of two datasets → emergent properties at the junction
- catalysis: transition-state energy barrier → catalyst tech that breaks a bottleneck

**VII. Dynamics (5)**
- tipping: bifurcation analysis → small change → big-jump point
- coevolution: time-lagged mutual MI → paired technology identification
- percolation: connection threshold → critical point where global connectivity suddenly emerges
- hysteresis: path dependence → discoveries where order matters
- diffusion: diffusion equation → predict ripple effects

**VIII. Meta-structure (4)**
- hierarchy: recursive clustering → nested tech structure
- conservation: Noether-style symmetry → conserved-quantity mapping
- arbitrage: value difference across domains → rare transfer opportunity
- serendipity: controlled random walk + outliers → unintended discoveries

**IX. Transitions (5)**
- renormalization: RG flow → scale dependence of effective parameters
- saddle: Hessian sign → transition-state coordinates
- criticality: avalanche distribution → self-organized criticality decision
- succession: automatic qualitative-stage partition of a time series
- resonance_cascade: trace resonance propagation in subsystems

**X. Deep information (4)**
- fisher_info: Fisher information matrix → parameter identifiability
- spectral_gap: eigenvalue gap of the transition matrix → convergence rate
- kolmogorov: BWT+RLE complexity → minimum description complexity
- contradiction: detect disagreement across lenses → meta-lens

**XI. Deep topology (4)**
- knot: Jones polynomial → entanglement/twist classification
- convexity: Hessian positive-definite → optimization-difficulty map
- motif: 3-5 node subgraph frequency → repeated micro-patterns
- skeleton: minimum spanning tree → core backbone

**XII. Ecology (4)**
- carrying_capacity: logistic fit → system saturation point
- niche: resource-space occupied/empty → why it is empty
- symbiosis: mutually beneficial pairs → gains when combined
- predation: growth of one = decrease of another → competing techs

**XIII. Deep physics (4)**
- morphogenesis: Turing reaction-diffusion → spontaneous pattern formation conditions
- polarity: directional asymmetry → gradient direction
- broken_ergodicity: inaccessible regions of phase space
- anomalous_diffusion: MSD ∝ t^α detection → anomalous diffusion

**XIV. Metacognition (4)** — lens-of-lenses
- blind_spot: complement of total lens output → system blind spots
- abstraction: search for optimal abstraction level
- narrative: serialize causal chain → full story
- analogy: functional role matching (structure-agnostic)

**XV. Decision (4)**
- bottleneck: minimum-capacity link along a causal/flow chain
- diminishing_returns: marginal utility curves per parameter
- option_value: value of decision deferral
- comparative_advantage: relative-strength matrix per domain

**XVI. Limits (3)**
- universality_class: critical exponents → universality-class classification
- aging: non-Markov memory kernel → system-age effects
- potential: unrealized energy / performance residual

#### 3.1.3 Tiered scanning

```
Tier 0: screening (8, <0.1s)
  consciousness + topology + void + thermo
  + evolution + network + boundary + triangle
  → SKIP if no signal

Tier 1: refined (24, <2s)
  existing 22 + void + isomorphism
  → SKIP if no candidate

Tier 2: full scan (80, <10s)
  all lenses → final confirmation

Expected: ~85% compute reduction vs full every time
```

#### 3.1.4 Consensus system

```
Weighted consensus:
  score = Σ(lens_hit_rate[domain] × found)
  
Grade:
  3+ lens agreement → candidate (weight 2)
  7+ lens agreement → high (weight 3)
  12+ lens agreement → confirmed (weight 4)

Early termination: 12-lens agreement reached → skip remaining lenses
```

### 3.2 Discovery Verifier — physics verifier

```
tools/discovery-verifier/
├── main.rs          — CLI
├── thermo.rs        — ΔG, ΔH, ΔS, phase-equilibrium checks
├── crystal.rs       — CN, lattice energy, tolerance factor
├── n6_check.rs      — n=6 constant match (EXACT/CLOSE/WEAK)
├── scaling.rs       — whether physical limits are exceeded
├── bt_compat.rs     — consistency with 127 BTs
└── feasibility.rs   — overall score + pass/candidate/fail grade
```

**Input**: telescope discovery candidates (JSON)
**Output**: verification report (pass/fail + reason + EXACT% + grade)

**Confidence score**:
```
score = lens_consensus × 0.3
      + cross_validation × 0.2
      + physical_verification × 0.3
      + novelty × 0.1
      + n6_exact × 0.1

S (0.9+): BT registration + paper candidate
A (0.7~0.9): BT registration + experiment proposal
B (0.5~0.7): further verification needed
C (0.3~0.5): hypothesis level
D (<0.3): rejected
```

### 3.3 Domain Encoder — domain data → numeric matrix

```
tools/domain-encoder/
├── main.rs          — CLI
├── schema.rs        — TOML schema
├── parser.rs        — hypotheses.md / goal.md parser
├── vectorize.rs     — text → float vectors
└── domains/         — per-domain encoding rules
    ├── superconductor.toml
    ├── chip-architecture.toml
    └── ... (33 files)
```

**Input**: docs/{domain}/hypotheses.md + goal.md + verification.md
**Output**: float64 matrix [N_hypotheses × N_features]

**Caching**: blake3(file contents) → .cache/domain-vectors/{domain}-{hash}.bin

### 3.4 Telescope History — lens learning system

```
telescope-history/          — sharded history
├── index.json              — overall stats + domain list
├── superconductor.jsonl    — per-domain scan log (append-only)
├── chip-architecture.jsonl
├── ...
├── affinity.json           — lens affinity (global)
├── discoveries.json        — confirmed discovery list
└── compact/                — quarterly compressed archive
```

**Automatic learning loop**:
```
scan → record results → confirm discovery → update outcome
→ recompute hit_rate → update affinity → update optimal_combo
→ next scan: recommendation engine picks the combo
```

**Recommendation strategy**:
- promotion_threshold: hit_rate > 30% → add to combo
- demotion_threshold: hit_rate < 5% → remove from combo
- serendipity_ratio: 15% → random lens allocation (exploration)
- cold_start: transfer combo from similar domain, or default 8

### 3.5 Materials DB — existing materials/technology DB

**Initial**: JSON (materials-db.json)
**At scale**: SQLite (materials.db) — migrate when materials exceed 1000

```jsonc
{
  "superconductor": {
    "known_materials": [
      {"name": "MgB2", "Tc": 39, "CN": 6, "type": "conventional", "year": 2001},
      ...
    ],
    "ceiling": {"Tc": 300, "CN": 6, "Jc": 1e8}
  }
}
```

### 3.6 OUROBOROS v26 — orchestrator

Existing OUROBOROS (~2,400 lines reused) + Discovery Mode extension.

**Reused components**:
- PatternRegistry (dedup + 3-way cross-check)
- LawNetwork (discovery-relation graph)
- ExplorationBandit (UCB1 exploration/exploitation)
- FederatedDiscovery (3-vote majority)
- AsyncDiscoveryPipeline (async)
- BestEngineTracker (checkpoints)
- save/load_state (JSON persistence)

**New roadmap (7 stages)**:
```
S1: single-domain basic scan (Tier 0+1, 8 lenses, cold start)
S2: single-domain deep (Tier 1+2, history-aware)
S3: single-domain full scan (80 lenses, GPU)
S4: cross-domain 2-way
S5: cross-domain 4-way
S6: all-11-domain cross full scan
S7: discovery-driven recursive exploration (discoveries are new inputs)
```

**Saturation escape**:
- 3 generations with 0 discoveries → advance stage
- chaos cycling (existing OUROBOROS) reused
- discovery "temperature" (SA): T=1.0→0.1, reheat on saturation

### 3.7 Cross-Domain Map

```jsonc
{
  "mappings": [
    {
      "concept": "coordination_number",
      "domains": {
        "superconductor": "CN (crystal)",
        "chip": "interconnect_count",
        "battery": "CN (cathode)",
        "biology": "codon_triplet"
      },
      "n6_value": 6,
      "bt_refs": ["BT-43", "BT-113", "BT-51"]
    }
  ]
}
```

### 3.8 Calibration Set

Validate the system with known discoveries.
- Historical discoveries (high-Tc superconductivity 1987, graphene 2004)
- Synthetic tests (inject known patterns)
- LK-99 failure → check that the verifier filters it

### 3.9 Prediction Registry

```jsonc
{
  "id": "TP-NEW-001",
  "domain": "superconductor",
  "prediction": "LaH10 at 170GPa exhibits Tc=260±15K",
  "basis": {
    "discovering_lenses": ["void", "extrapolation", "thermo"],
    "consensus_level": 7,
    "bt_connections": ["BT-43", "BT-80"],
    "n6_exact_ratio": 0.85
  },
  "falsification": {
    "method": "Diamond anvil cell + 4-probe resistivity",
    "cost_estimate": "$50K-200K",
    "timeline": "3-6 months"
  },
  "outcome": null
}
```

### 3.10 Dashboard

ASCII CLI baseline + HTML option.
- Void Map
- Tension Heatmap (cross-domain)
- Discovery Timeline
- Lens Performance chart
- GPU/CPU/MEM live status

---

## 4. Performance design

### 4.1 GPU usage (M4 Metal)

- Backend: wgpu (Rust-native, Metal support)
- Unified memory: 0-cost CPU↔GPU copy
- FP16 fallback: lenses not needing precision use half precision (2x throughput)
- Tiling: 32×32 tiles → shared-memory caching

### 4.2 Shared-kernel warmup

```
At scan start:
  distance_matrix → computed once, ~20 lenses share
  mi_matrix → computed once, ~15 lenses share
  knn_indices → computed once, ~12 lenses share
  fft_result → computed once, ~5 lenses share

Without warmup: 80 × 5ms = 400ms
With warmup:    12 × 3ms + 80 × 1ms = 116ms (71% reduction)
```

### 4.3 Memory layout

- SoA (Structure-of-Arrays): features stored column-wise → SIMD friendly
- Arc<[f64]>: 80 lenses share-reference the input data (0 copies)
- Memory pool: per-lens temp buffers reused

### 4.4 SIMD (M4 NEON)

- 128-bit NEON → 4×f32 at a time
- Hot paths: distance, dot product, histogram bin count
- Rust auto-vectorize + std::arch::aarch64 intrinsics as needed

### 4.5 Pipeline parallelism

- Across domains: encode B while scanning A (pipeline)
- Intra-lens: GPU queue (matrix ops) + CPU queue (graphs) concurrently
- Across generations: OUROBOROS AsyncPipeline (scan gen N+1 while verifying gen N)

### 4.6 Caching

- Result cache: blake3(data+lens_set) → avoid rescanning identical data
- Incremental scan: recompute distance/MI only on the added delta (O(N²)→O(N·ΔN))
- Domain-encoder cache: reuse vectors when files are unchanged

### 4.7 Adaptive resolution

```
N < 32:   full precision
N < 256:  standard
N < 1024: sampled (subset + estimate)
N > 1024: hierarchical (cluster representatives → zoom in)
```

### 4.8 Early termination

- 12/80 consensus reached → skip remaining 68 lenses (up to 85% savings)
- Lens execution order = descending hit_rate (run high value/time first)

### 4.9 Expected performance

```
Data size: 64×32 (typical domain)

Full scan (80):
  Warmup: 12 kernels × 3ms = 36ms
  GPU lenses (40): 40 × 2ms = 80ms (parallel ~20ms)
  CPU lenses (40): 40 × 3ms = 120ms (rayon parallel ~30ms)
  Consensus: 1ms
  Total: ~90ms (GPU) / ~240ms (CPU only)

Tier 0 (8): ~12ms
Tier 1 (24): ~50ms
Tier 2 (80): ~90ms

Full scan of all 33 domains (Tier pyramid):
  ~50s (vs ~330s if full scan every time, 85% reduction)
```

---

## 5. Quality assurance

### 5.1 Cross-validation
- OUROBOROS pattern: 3 occurrences required (existing, reused)
- FederatedDiscovery 3-way majority (existing, reused)

### 5.2 Red Team (automatic falsification)
- falsification lens: identify weak assumptions
- antagonism: search for cancelling combinations
- contradiction meta-lens: verify lens-to-lens conflicts
- broken_ergodicity: confirm unreachable regions

### 5.3 Discovery chain lineage
- Record parent/child relations
- Track which discovery spawned the most follow-ons

### 5.4 False-positive tracking
- Record per-lens FP rate
- FP rate > 30% → automatically tighten verification criterion

### 5.5 Calibration
- Recall on known discoveries
- Precision on known failures
- Regression test each release

---

## 6. Automation

### 6.1 BT auto-registration
score ≥ S (0.9) + Red Team pass + cross-validation → BT-XXX auto-created

### 6.2 Auto-update of domain files
discovery → auto-update novel-predictions.md / verification.md / hypotheses.md

### 6.3 Auto-generate experiment proposal
A-grade or higher discovery → auto-propose experimental method / equipment / cost / timeline

### 6.4 Watch mode
File-change watcher → auto-rescan affected domain

---

## 7. Feedback loops

### 3-path evolution:

1. **Lens-combo evolution**: discovery → update hit_rate → change next combo
2. **Data evolution**: discovery → add to Materials DB → void detects new gaps
3. **Feature evolution**: discovery → "this property matters" → Encoder feature added

### Meta-discovery (every 100 generations):
- completeness does a self-scan → coverage map
- blind_spot detects system blind spots
- Results feed OUROBOROS self-modification

---

## 8. Durability

- Lens isolation: panic::catch_unwind per lens → 1 failure leaves 79 running
- GPU fallback: Metal error → auto-switch to CPU rayon
- Checkpoint: save every 10 lenses complete → resume on interruption
- Data integrity: tmp → fsync → atomic rename

---

## 9. CLI design

```bash
discovery-engine scan <domain>           # single-domain scan
discovery-engine scan --cross A B        # cross scan
discovery-engine run --roadmap           # OUROBOROS loop
discovery-engine run --resume            # resume
discovery-engine verify <id>             # verify a discovery
discovery-engine status                  # current status
discovery-engine history <domain>        # history
discovery-engine recommend <domain>      # recommend lenses
discovery-engine dashboard               # dashboard
discovery-engine watch                   # file-watch mode
discovery-engine calibrate               # system calibration
discovery-engine benchmark               # performance benchmark
```

---

## 10. Implementation list

| # | Component | Form | Location | Est. size |
|---|---------|------|------|----------|
| 1 | Telescope v2 | Rust+wgpu | telescope-rs/ (extension) | ~7,000 lines (kernels 3K + combos 4K) |
| 2 | Discovery Verifier | Rust | tools/discovery-verifier/ | ~2,000 lines |
| 3 | Domain Encoder | Rust+TOML | tools/domain-encoder/ | ~1,500 lines + 33 TOML |
| 4 | Telescope History | Rust | tools/telescope-history/ | ~1,000 lines |
| 5 | Materials DB | JSON→SQLite | docs/materials-db.json | data collection |
| 6 | OUROBOROS v26 | Python extension | infinite_evolution.py | ~1,800 new lines |
| 7 | Cross-Domain Map | JSON | docs/cross-domain-map.json | data collection |
| 8 | Calibration Set | JSON | tools/telescope-calibration/ | ~500 lines |
| 9 | Prediction Registry | JSON+Rust | tools/prediction-registry/ | ~800 lines |
| 10 | Dashboard | Rust+HTML | tools/discovery-dashboard/ | ~1,200 lines |
| 11 | CLI Orchestrator | Rust | tools/discovery-engine/ | ~1,500 lines |

**Total: ~17,300 lines Rust + ~1,800 lines Python + data files**

---

## 11. Dependencies

```
Rust:
  wgpu 23.x          — Metal GPU compute
  rayon 1.10          — CPU parallelism
  pyo3 0.28           — Python bindings
  numpy 0.28          — numpy integration
  serde + serde_json  — JSON serialization
  blake3              — hashing (cache key)
  rusqlite (optional) — SQLite (when Materials DB grows)
  tiny_http (optional)— Dashboard HTTP

Python:
  telescope_rs        — Rust lens bindings
  numpy               — data processing
  (existing OUROBOROS dependencies)
```

---

## 12. Constraints and future work

**Current constraints**:
- M4 single machine (no distribution)
- All 80 lenses implemented incrementally (by priority)
- External DB (Materials Project, AFLOW) integration is future work

**Future extensions**:
- WASM lens plugins (dynamic load, no recompilation)
- Distributed execution (multiple machines)
- Auto-pull from external DBs
- S-grade discovery → auto-generated arXiv paper draft
