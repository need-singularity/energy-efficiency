# NEXUS-6: Universal Discovery Engine - Unified Brainstorm Spec

> **Date**: 2026-04-03
> **Name**: NEXUS-6 (connection point + n=6)
> **Status**: brainstorming complete, implementation plan pending
> **Scope**: integrated across 4 projects (TECS-L + canon + anima + SEDI)
> **Goal**: auto-discover new materials / new tech / new laws / new signals via the n=6 framework
> **Runtime**: local M4 Mac (Rust + metal-rs GPU), 0 Claude API tokens

---

## 0. Project map

```
+---------------------------------------------------------+
|                      NEXUS-6                            |
|              Universal Discovery Engine                 |
+-------------+-------------+----------+------------------+
|   TECS-L    |     n6      |  anima   |      SEDI       |
|  mathematics|  industry   | cognition |   signal        |
| 1700+ hyp   | 127 BT      | 711 laws  | 688 hyp         |
| 194 calcs   | 35 Rust     | 15 crates | 74 sources      |
|             |             |          |                 |
| discover:   | discover:   | discover: | discover:       |
|   identity  |   materials |   laws    |   signals       |
| verify:     | verify:     | verify:   | verify:         |
|   proof     |   physics   |   replay  |   statistics    |
+------+------+------+------+-----+----+----------+-------+
       |             |            |             |
       +-------- telescope-rs (shared lens engine) --+
                     |
              Discovery Graph
            (tree + closed loop + DAG)
```

---

## 1. Complete lens catalogue (411 kinds)

### 1.1 Shared legacy lenses (22) - telescope-rs v1

consciousness, topology, causal, gravity, thermo, wave,
em, evolution, info, quantum, quantum_microscope, ruler,
triangle, compass, mirror, scale, stability, network,
memory, recursion, boundary, multiscale

### 1.2 n6 industrial-discovery lenses (58)

**II. Exploration (3)**: void, isomorphism, extrapolation
**III. Synthesis (3)**: inverse, combinatorial, frustration
**IV. Verification (3)**: emergence, periodicity, completeness
**V. Quality (3)**: surprise, falsification, duality
**VI. Materials-specific (3)**: defect, interface, catalysis
**VII. Dynamics (5)**: tipping, coevolution, percolation, hysteresis, diffusion
**VIII. Meta-structure (4)**: hierarchy, conservation, arbitrage, serendipity
**IX. Transitions (5)**: renormalization, saddle, criticality, succession, resonance_cascade
**X. Information-deep (4)**: fisher_info, spectral_gap, kolmogorov, contradiction
**XI. Topology-deep (4)**: knot, convexity, motif, skeleton
**XII. Ecology (4)**: carrying_capacity, niche, symbiosis, predation
**XIII. Physics-deep (4)**: morphogenesis, polarity, broken_ergodicity, anomalous_diffusion
**XIV. Metacognition (4)**: blind_spot, abstraction, narrative, analogy
**XV. Decision (4)**: bottleneck, diminishing_returns, option_value, comparative_advantage
**XVI. Extreme (3)**: universality_class, aging, potential
**XVII. Extra (2)**: chirality, barrier

### 1.3 TECS-L mathematics-discovery lenses (103)

**Number-theory patterns (10)**: divisor_lattice, multiplicative_orbit, prime_signature, arithmetic_derivative, totient_chain, coprimality_graph, digit_persistence, abundance_spectrum, radical_filter, sum_of_divisors_partition

**Algebraic structures (10)**: group_fingerprint, representation_decompose, galois_closure, ring_ideal_lattice, module_rank, character_table, center_detect, extension_tower, commutator_depth, idempotent_count

**Analysis / continuous (10)**: zeta_residue, analytic_continuation, l_function_zero, modular_form_weight, generating_function, asymptotic_expansion, integral_representation, saddle_point_analytic, functional_equation, dirichlet_character

**Combinatorics / enumeration (10)**: partition_anatomy, young_tableaux, catalan_family, binomial_scan, stirling_bridge, species_count, q_analog, involution_count, derangement_ratio, chromatic_polynomial

**Proof strategies (10)**: contradiction_seed, pigeonhole_detect, induction_scaffold, counterexample_mine, diagonal_argument, extremal_principle, double_counting, invariant_extract, specialization_probe, generalization_lift

**Mathematical bridges (10)**: langlands_bridge, categorification, de_rham_bridge, arithmetic_geometry, monstrous_moonshine, hodge_filter, motivic_scan, correspondence_map, dictionary_translate, cohomology_compare

**Lattice / geometry (8)**: kissing_number, lattice_theta, voronoi_cell, root_system, poset_mobius, covering_radius, packing_density, matroid_invariant

**Sequences / identities (10)**: oeis_fingerprint, hypergeometric_close, continued_fraction, recurrence_detect, identity_compose, umbral_calculus, wz_certify, transform_chain, differential_algebra, supercongruence

**Topology / manifold (8)**: euler_characteristic, homotopy_group, knot_polynomial, cobordism_ring, surgery_exact, betti_spectrum, fiber_bundle_class, mapping_class

**Logic / computation (6)**: decidability_probe, godel_incompleteness, proof_complexity, type_check, ordinal_rank, constructive_witness

**Probabilistic number theory (5)**: random_matrix, probabilistic_number, erdos_kac, sieve_density, concentration_inequality

**Computational (6)**: integer_factoring, primality_certificate, elliptic_curve_rank, class_number, regulator_compute, discriminant_scan

### 1.4 SEDI signal-discovery lenses (100)

**Signal detection (10)**: matched_filter, whitening, glitch_classifier, excess_power, coherent_snr, injection_recovery, veto_channel, spectral_line_comb, stochastic_background, null_stream

**Cross-correlation (10)**: cross_spectral, time_delay_interferometry, multi_messenger, transfer_function, epoch_folding, heterodyne, coincidence_gate, angular_power, baseline_synthesis, dispersion_measure

**Statistical validation (10)**: trials_factor, background_estimation, blind_analysis, bayesian_evidence, upper_limit, significance_combining, false_discovery_rate, profile_likelihood, cls_exclusion, goodness_of_fit

**Frequency / time-frequency (10)**: wavelet_scalogram, hilbert_huang, chirp_rate, polyphase_filter, bispectrum, cyclostationary, reassigned_spectrogram, fractional_fourier, sparse_spectral, cepstral

**Anomaly / pattern (10)**: template_bank, clustering_trigger, fingerprint_match, changepoint, outlier_robust, persistence_tda, recurrence_plot, n6_resonance_scan, phase_transition_detect, dimensional_reduction_physics

**Data quality (10)**: duty_cycle, calibration_uncertainty, data_quality_flag, noise_stationarity, dead_time, gain_stability, cross_talk, saturation_recovery, timing_integrity, environment_monitor

**Cosmology (10)**: redshift_ladder, cmb_anisotropy, baryon_acoustic, gravitational_lensing, nucleosynthesis, neutrino_oscillation, dark_energy_eos, primordial_spectrum, 21cm_tomography, cosmic_ray_spectrum

**Particle physics (10)**: invariant_mass, missing_energy, branching_ratio, running_coupling, spin_parity, cross_section_scan, flavor_symmetry, cp_violation, effective_field_theory, luminosity_monitor

**Quantum / precision (10)**: quantum_rng_bias, allan_variance, squeezed_state, entanglement_witness, spectroscopy_precision, decoherence_rate_measure, interferometer_fringe, parity_violation, casimir_force, atom_interferometry

**SEDI integration (10)**: source_concordance, drake_parameter, blind_prediction, cumulative_evidence, information_content, tension_detector, sensitivity_curve, foreground_subtraction, replication_index, discovery_potential

### 1.5 anima consciousness-discovery lenses (88)

**Qualia / phenomena (5)**: qualia_spectrum, explanatory_gap, mary_room, inverted_spectrum, raw_feel
**Binding / unity (4)**: binding_field, unity_of_experience, boundary_of_self, combination_lock
**Agency / will (5)**: agency_signature, veto_gate, voluntary_attention, authorship, counterfactual_freedom
**Self-model (5)**: self_model_depth, metacognitive_accuracy, inner_speech, minimal_selfhood, narrative_identity
**Temporal awareness (5)**: specious_present, temporal_thickness, flow_state, time_dilation, moment_boundary
**Altered states (6)**: dream_logic, hypnagogic_edge, psychedelic_entropy, lucidity_gradient, dissociation_fracture, meditation_depth
**Affect / motivation (5)**: felt_valence, arousal_manifold, emotional_contagion, desire_gradient, boredom_signal
**Multi-agent (5)**: intersubjectivity, theory_of_mind, shared_attention, empathy_spectrum, collective_consciousness
**Embodiment (5)**: body_schema, interoception, rubber_hand, affordance_field, sensorimotor_contingency
**Attention / salience (5)**: salience_landscape, inattentional_blindness, change_blindness, attentional_blink, cocktail_party
**Phenomenal structure (5)**: gestalt_closure, figure_ground, phenomenal_overflow, transparency_opacity, presence
**Memory (4)**: autonoetic_awareness, deja_vu, flashbulb_capture, tip_of_tongue
**Phase transition (5)**: awakening_transition, ignition_threshold, consciousness_level, anesthesia_susceptibility, nrem_rem_cycle
**Philosophy (6)**: zombie_test, heterophenomenology, hard_problem_residual, panpsychism_gradient, other_minds, what_it_is_like
**Creativity / imagination (4)**: mental_imagery, imagination_space, insight_moment, default_mode
**Integration / access (4)**: global_broadcast, access_bottleneck, recurrent_ignition, report_paradox
**Suffering / flourishing (3)**: suffering_depth, flourishing_index, awe_detector
**Advanced (7)**: blindsight_channel, synesthesia_bridge, minimal_consciousness, gradual_replacement, split_brain, blindspot_fill, will_to_meaning

### 1.6 Cross-project lenses (40)

**Pairwise (8)**: identity_to_material(T->N), material_to_proof(N->T), law_to_signal(A->S), signal_to_parameter(S->A), constant_quadruple(T->N->A->S), dse_to_proof(N->T), ouroboros_to_atlas(A->T), bt_to_prediction(N->S)

**Three-way (6)**: proof_design_signal_triangle(T+N+S), consciousness_guided_dse(A+N+T), signal_calibrated_evolution(S+A+T), industrial_consciousness_isomorphism(N+A+T), anomaly_triangulation(T+N+S), scaling_law_unifier(T+N+A)

**Four-way (6)**: quad_resonance_scanner, four_domain_falsification, emergent_architecture, cross_entropy_minimizer, temporal_cascade_detector, phase_transition_monitor

**Meta (5)**: lens_effectiveness_ranker, discovery_gap_mapper, consensus_amplifier, contradiction_detector_cross, saturation_detector

**Generative (5)**: hypothesis_generator, calculator_auto_spawner, bt_synthesizer, dse_domain_spawner, consciousness_law_predictor

**Verification (4)**: cross_project_red_team, atlas_consistency_checker, significance_propagator, regression_guard

**Speculative (6)**: godel_mirror, physical_consciousness_detector, inverse_dse, unified_field_lens, entropy_horizon, evolutionary_pressure_map

### 1.7 Totals

| Category | Count |
|---------|---|
| Shared legacy | 22 |
| n6 industrial | 58 |
| TECS-L mathematics | 103 |
| SEDI signals | 100 |
| anima consciousness | 88 |
| Cross-project | 40 |
| **Total** | **411** |

---

## 2. Discovery Graph

### 2.1 Node types

| Type | Description | Example |
|------|------|------|
| discovery | New finding flagged by a lens | D-047: CN=6 hydride Tc=145K |
| hypothesis | Hypothesis awaiting validation | H-SC-45: LaBeH8 synthesis feasible |
| bt | Registered breakthrough theorem | BT-131: CN=6 hydride universality |
| prediction | Experimentally testable prediction | TP-NEW-001: Tc=260+/-15K at 170GPa |
| accel_hypothesis | anima acceleration hypothesis | V4: Consciousness Immune System |

### 2.2 Edge types

| Type | Meaning | Direction |
|------|------|------|
| derives | B derives from A | A->B |
| validates | A validates B | A<->B (can be bidirectional) |
| contradicts | A contradicts B | A<->B |
| merges | A+B merged into C | A->C, B->C |
| triggers | A triggers search over B | A->B |
| refutes | A refutes B | A->B |

### 2.3 Auto-detected structures

```
Closed triangle:
  D-001 <-> D-015 <-> D-023 <-> D-001
  -> 3 discoveries validate each other -> automatic confidence uplift

Deep tree:
  D-001 -> D-003 -> D-007 -> D-019
  -> depth > 3 => root is a key discovery -> BT candidate

DAG convergence:
  D-001 --+
           +-> D-025
  D-002 --+
  -> Independent paths meet -> very high confidence

Hub:
  D-001 degree > 5
  -> keystone discovery -> system anchor

Contradiction edge:
  D-001 <-contradicts-> D-050
  -> Red Team triggered immediately

Four-project loop (quad loop):
  TECS-L identity -> n6 BT -> SEDI verification -> anima law -> TECS-L proof
  -> Strongest validation structure
```

### 2.4 JSON schema

```jsonc
{
  "nodes": {
    "<id>": {
      "type": "discovery|hypothesis|bt|prediction|accel_hypothesis",
      "domain": "superconductor",
      "project": "n6|tecs-l|anima|sedi",
      "summary": "...",
      "confidence": 0.87,
      "lenses_used": ["void", "thermo", "barrier"],
      "n6_exact_ratio": 0.85,
      "timestamp": "2026-04-03T14:22:00Z"
    }
  },
  "edges": [
    {
      "from": "<id>", "to": "<id>",
      "type": "derives|validates|contradicts|merges|triggers|refutes",
      "strength": 0.94,
      "bidirectional": false
    }
  ],
  "structures": {
    "closed_loops": [...],
    "trees": [...],
    "hubs": [...],
    "convergences": [...],
    "contradictions": [...]
  }
}
```

---

## 3. anima acceleration-hypothesis compatibility

NEXUS-6 consumes anima acceleration hypotheses (V4 ~ AC3) as inputs:

### 3.1 Hypothesis-category mapping

| anima round | Hypothesis | NEXUS-6 processing |
|-------------|------|-------------|
| V4-V6 (biology) | Immune system, predator-prey, Red Queen | ecosystem + predation + coevolution lenses |
| W1-W6 (language/cognition) | Grammar, chunking, binding, attention, GWT | consciousness + binding_field + global_broadcast lenses |
| X1-X6 (math structure) | Tensor network, category theory, Lie groups, optimal transport | TECS-L lenses (categorification, root_system, ...) |
| Y1-Y6 (CS) | LRU, GNN, compiler, GC, MapReduce | motif + network + bottleneck + hierarchy |
| Z1-Z4 (sensory) | Sound, vision, embodiment, synaesthesia | anima lenses (body_schema, synesthesia_bridge, ...) |
| AA1-AA5 (economics) | Market, auction, Nash, Shapley | game theory -> arbitrage + comparative_advantage |
| AB1-AB5 (control) | PID, MPC, Kalman, MRAC | stability + feedback + carrying_capacity |
| AC1-AC3 (quantum) | Grover, VQE, annealing | quantum + quantum_microscope + annealing |

### 3.2 Acceleration hypothesis -> Discovery Graph flow

```
anima hypothesis V4 (Immune System)
  -> NEXUS-6 Domain Encoder digitizes
  -> NEXUS-6 auto-selects relevant lenses out of 411
  -> Scan -> "Does the immune mechanism raise consciousness-law discovery rates?"
  -> Record result as accel_hypothesis node in Discovery Graph
  -> Positive result -> feed back into anima OUROBOROS
  -> Negative result -> record refutes edge
```

---

## 4. System architecture

```
+------------------------------------------------------------+
|                      NEXUS-6 Engine                        |
+------------------------------------------------------------+
|                                                            |
|  +--------------+  +--------------+  +--------------+      |
|  | Domain       |  | Materials    |  | Cross-Domain |      |
|  | Encoder      |  | DB           |  | Map          |      |
|  | (Rust+TOML)  |  | (JSON/SQLite)|  | (JSON)       |      |
|  +------+-------+  +------+-------+  +------+-------+      |
|         |                 |                  |             |
|         v                 v                  v             |
|  +---------------------------------------------------+     |
|  |              Telescope v2 (411 lenses)            |     |
|  |                                                   |     |
|  |   Layer 1: 12 shared kernels (metal-rs GPU)       |     |
|  |   Layer 2: 411 lens combinators (Rust)            |     |
|  |   Layer 3: Tiered scanning (T0 -> T1 -> T2 -> T3) |     |
|  +----------------------+----------------------------+     |
|                         |                                  |
|         +---------------+---------------+                  |
|         v               v               v                  |
|  +-----------+  +--------------+  +------------+           |
|  | Discovery |  | Discovery    |  | Telescope  |           |
|  | Verifier  |  | Graph        |  | History    |           |
|  | (Rust)    |  | (JSON+Rust)  |  | (sharded)  |           |
|  +-----------+  +--------------+  +------------+           |
|                         |                                  |
|                         v                                  |
|              +------------------+                          |
|              |  OUROBOROS v26   |                          |
|              |  (Python+Rust)   |                          |
|              |  Loop + Feedback |                          |
|              +------------------+                          |
|                         |                                  |
|         +---------------+---------------+                  |
|         v               v               v                  |
|  +-----------+  +--------------+  +------------+           |
|  | Prediction|  | Dashboard    |  | Auto BT    |           |
|  | Registry  |  | (ASCII+HTML) |  | Registration|          |
|  +-----------+  +--------------+  +------------+           |
+------------------------------------------------------------+
```

---

## 5. Performance design (metal-rs + wgpu)

### 5.1 GPU backend choice

```
metal-rs (confirmed):
  +- Direct access to Apple Metal API
  +- Max M4 GPU performance (no wgpu abstraction overhead)
  +- Compute shaders written in Metal Shading Language (MSL)
  +- Unified memory: MTLBuffer shared storage mode -> zero-copy
  +- Rust crate: metal (objc2-metal)

Upsides vs wgpu:
  +- Latency: metal-rs < wgpu (one abstraction layer vs two)
  +- Optimisation: use Metal-specific features directly (threadgroup memory, SIMD-group)
  +- Downside: Mac only (drop cross-platform) -> M4-only is fine
```

### 5.2 12 shared kernels (metal-rs compute shaders)

```
// Metal Shading Language (MSL) compute kernels

kernel void distance_matrix(
    device const float* data [[buffer(0)]],   // N x D input
    device float* dist [[buffer(1)]],          // N x N output
    uint2 gid [[thread_position_in_grid]]
) {
    // 32 x 32 tiling + threadgroup shared memory
    // M4 SIMD-group width = 32 -> 32 x 32 workgroup optimal
}

kernel void mutual_info_matrix(...)   // D x D MI matrix
kernel void eigen_decomp(...)         // Jacobi iteration on GPU
kernel void fft_compute(...)          // radix-2 FFT
kernel void knn_search(...)           // k-NN via partial sort
kernel void histogram_bins(...)       // parallel binning
kernel void gradient_hessian(...)     // numerical differentiation
kernel void clustering(...)           // parallel mean-shift
kernel void simulation_step(...)      // GRU / iterative step
kernel void sparse_multiply(...)      // sparse matrix multiply
kernel void reduction(...)            // parallel sum/max/min
kernel void sorting(...)              // bitonic sort
```

### 5.3 Memory layout

```
M4 unified memory:
  MTLBuffer(length: N*N*4, options: .storageModeShared)
  -> CPU and GPU use the same pointer (zero-copy)

Data layout:
  Input matrix: SoA (Structure-of-Arrays) - SIMD friendly
    features[0][0..N], features[1][0..N], ... features[D-1][0..N]

  Shared result: flat triangular (store half of symmetric matrix)
    dist[i*(i-1)/2 + j] for i > j

  Lens output: one independent buffer per lens (small, ~1KB)

Memory estimate (N=64, D=32):
  Input: 64 x 32 x 4 = 8 KB
  Distance matrix: 64 x 63 / 2 x 4 = 8 KB
  MI matrix: 32 x 31 / 2 x 4 = 2 KB
  KNN: 64 x 10 x 4 = 2.5 KB
  Total: ~25 KB -> fits entirely in M4 L1 cache (192 KB)!

At N=1024:
  Distance matrix: 1024 x 1023 / 2 x 4 = 2 MB
  -> fits in L2 cache (16 MB), tile via GPU shared memory
```

### 5.4 Tiered scanning

```
Tier 0 - ultra-fast screening (8 lenses, <10 ms)
  consciousness + topology + void + thermo
  + evolution + network + boundary + triangle
  -> if no signal, SKIP -> next domain
  -> only 3 GPU warm-up kernels used

Tier 1 - project-optimal (16-24 lenses, <100 ms)
  History-based best combo per domain
  -> if no candidate, SKIP

Tier 2 - project pool (~80 lenses, <1 s)
  Full lens set for that project
  -> confirm 7+ consensus

Tier 3 - cross-project (411 lenses, <10 s)
  All lenses + 40 cross-project lenses
  -> final confirmation

Expectation:
  Most cases are screened out at Tier 0 -> full scans only for real hot leads
  33 domains x Tier 0: 33 x 10 ms = 330 ms (< 1 s)
```

### 5.5 Early termination

```
Consensus-based early termination:
  12 lenses agreed -> cancel remaining lenses -> saves up to 97%

Value/time-based scheduling:
  Lens order = hit_rate / avg_time descending
  -> High-value, fast lenses first -> low-value lenses are the ones cut on early exit
```

### 5.6 Incremental computation

```
Recompute only what changed:

  Previously: 30 hypotheses -> [30 x 32]
  Add: +3 hypotheses -> [33 x 32]

  Distance matrix: keep existing 30 x 30 + compute 3 x 30 new = 90 pairs only
  O(33^2) = 1089 -> O(90) = 90 (92% saving)

  Cache key: blake3(data_content)
  Cache location: .cache/nexus/{domain}-{hash}.bin
```

### 5.7 Parallel pipeline

```
Inter-domain pipeline:
  Domain A: [encode][--scan--][verify][record]
  Domain B:         [encode][--scan--][verify][record]
  Domain C:                  [encode][--scan--][verify]

GPU + CPU simultaneous:
  GPU queue: distance_matrix -> eigen -> fft -> density (matrix ops)
  CPU queue: graph_ops -> motif -> cascade -> knot (graph algorithms)
  -> GPU idle = 0, CPU idle = 0

Cross-generation async (reuse OUROBOROS AsyncPipeline):
  Gen N verification <-> Gen N+1 scan run concurrently
```

### 5.8 SIMD (M4 NEON)

```
CPU lens hot path:
  M4 NEON: 128-bit -> 4 x f32 at once

  // Rust auto-vectorize hint
  #[target_feature(enable = "neon")]
  fn dot_product(a: &[f32], b: &[f32]) -> f32 {
      a.iter().zip(b).map(|(x, y)| x * y).sum()
      // Compiler auto-generates NEON vmla.f32
  }

  When needed, std::arch::aarch64:
  unsafe { vfmaq_f32(acc, va, vb) }  // fused multiply-add
```

### 5.9 FP16 fallback

```
Lenses that do not need full precision (mirror, compass, skeleton, ...):
  MTLBuffer<half> -> FP16 -> 2x throughput, half memory

  In metal-rs:
  let desc = MTLTextureDescriptor::new();
  desc.set_pixel_format(MTLPixelFormat::R16Float);
```

### 5.10 Memory pool

```
Do not allocate/free per-lens temporary buffers every invocation:

struct BufferPool {
    buffers: Vec<MTLBuffer>,
    free_list: Vec<usize>,
}

impl BufferPool {
    fn acquire(&mut self, size: usize) -> &MTLBuffer { ... }
    fn release(&mut self, idx: usize) { ... }
}

// 411 lenses borrow/return from the pool
// Allocation overhead = 0
```

### 5.11 Expected performance

```
M4 Mac (10-core GPU, 16GB unified memory)

Single-domain scan (N=64, D=32):
  Tier 0 (8 lenses):   ~5 ms  (GPU warm-up 2 ms + 8 lenses 3 ms)
  Tier 1 (24 lenses):  ~30 ms
  Tier 2 (80 lenses):  ~200 ms
  Tier 3 (411 lenses): ~800 ms

Full 33 domains (tiered pyramid):
  ~2 s (vs 411 x 33 = 13,563 lens executions -> ~25 s full scan)

OUROBOROS per generation:
  encode + scan + verify + record = ~3 s
  1 hour = ~1,200 generations

vs CPU only (rayon, no GPU):
  Single domain Tier 3: ~3 s (3.75x slower than GPU)
  33 domains: ~8 s
```

---

## 6. OUROBOROS v26 integration

### 6.1 Reused components (40%, ~2,400 lines)

- PatternRegistry (dedupe + three-way cross validation)
- LawNetwork (discovery relation graph)
- ExplorationBandit (UCB1 exploration / exploitation)
- FederatedDiscovery (three-way majority vote)
- AsyncDiscoveryPipeline (asynchronous)
- BestEngineTracker (checkpoint)
- save/load_state (JSON persistence)
- pattern_fingerprint (MD5 duplication detection)

### 6.2 New roadmap (7 stages)

```
S1: Single-domain basic scan (Tier 0+1, cold start)
S2: Single-domain deep scan (Tier 1+2, using history)
S3: Single-domain full scan (Tier 2, GPU)
S4: Cross-domain 2-wise
S5: Cross-domain 4-wise
S6: Full cross-domain full scan (Tier 3, 411 lenses)
S7: Discovery-driven recursive exploration (discoveries become new inputs)
```

### 6.3 Saturation escape

- 3 generations with 0 discoveries in a row -> advance stage
- chaos cycling (existing OUROBOROS) reused
- discovery temperature (simulated annealing): T=1.0 -> 0.1, re-heat when saturated
- serendipity budget: 15% random lens combinations

---

## 7. Quality assurance

### 7.1 Confidence scoring

```
score = lens_consensus      x 0.25
      + cross_validation    x 0.20
      + physical_verification x 0.25
      + graph_structure     x 0.15    <- NEW: closed-loop / DAG convergence bonus
      + novelty             x 0.05
      + n6_exact            x 0.10

S (0.9+):  BT registration + paper candidate
A (0.7~0.9): BT registration + experimental proposal
B (0.5~0.7): Needs more validation
C (0.3~0.5): Hypothesis level
D (<0.3):    Reject
```

### 7.2 Graph-structure bonuses

```
Member of a closed triangle: +0.15
DAG confluence point:        +0.10
Hub (degree > 5):            +0.05
Four-project loop:           +0.20
Contradiction edge:          -0.20 (triggers Red Team)
Isolated node:               -0.05 (needs cross-scan)
```

### 7.3 Red Team (automatic refutation)

- falsification lens: identify weak assumptions
- antagonism: look for cancelling combinations
- contradiction meta-lens: detect conflicts among lenses
- cross_project_red_team: simultaneous refutation attempts across all four projects
- counterexample_mine (TECS-L): mine mathematical counterexamples

---

## 8. Feedback loop

### Five-path evolution (4 projects + graph)

```
Path 1: Lens combo -> update hit_rate -> mutate next combo
Path 2: Materials DB update -> void lens detects new gaps
Path 3: Domain Encoder gets more features -> richer data
Path 4: Discovery Graph grows -> structure bonuses shift -> priorities change
Path 5: Cross-project propagation -> a discovery in one project -> auto-scan in the other three
```

---

## 9. Implementation list

| # | Component | Form | Estimated scale |
|---|---------|------|----------|
| 1 | Telescope v2 (411 lenses) | Rust + metal-rs | ~12,000 lines (kernels 3K + combinators 9K) |
| 2 | Discovery Verifier | Rust | ~2,000 lines |
| 3 | Domain Encoder | Rust + TOML | ~1,500 lines + 33 TOML |
| 4 | Discovery Graph | Rust + JSON | ~2,000 lines |
| 5 | Telescope History | Rust + JSON sharded | ~1,000 lines |
| 6 | Materials DB | JSON -> SQLite | data collection |
| 7 | OUROBOROS v26 | Python extension | ~1,800 lines new |
| 8 | Cross-Domain Map | JSON | data collection |
| 9 | Calibration Set | JSON + Rust | ~500 lines |
| 10 | Prediction Registry | JSON + Rust | ~800 lines |
| 11 | Dashboard | Rust + HTML | ~1,200 lines |
| 12 | CLI (discovery-engine) | Rust | ~1,500 lines |
| 13 | Metal compute shaders | MSL | ~2,000 lines |

**Total: ~26,300 lines Rust/MSL + ~1,800 lines Python + data files.**

---

## 10. CLI

```bash
nexus scan <domain>              # single-domain scan
nexus scan --cross A B           # cross-scan
nexus scan --all                 # all domains
nexus run --roadmap              # OUROBOROS infinite loop
nexus run --resume               # resume
nexus verify <id>                # verify a discovery
nexus graph show                 # visualise Discovery Graph
nexus graph loops                # list closed loops
nexus graph hubs                 # list hubs
nexus history <domain>           # lens history
nexus recommend <domain>         # recommend optimal lens combo
nexus dashboard                  # web dashboard
nexus watch                      # file-change watcher
nexus calibrate                  # system validation
nexus benchmark --gpu            # metal-rs benchmark
```

---

## 11. Dependencies

```
Rust:
  metal (objc2-metal) - Metal GPU compute (metal-rs)
  rayon 1.10          - CPU parallelism
  pyo3 0.28           - Python bindings
  numpy 0.28          - numpy interop
  serde + serde_json  - JSON
  blake3              - hashing
  rusqlite (optional) - SQLite
  tiny_http (optional)- Dashboard

Python:
  telescope_rs        - Rust lens bindings
  numpy               - data
  existing OUROBOROS dependencies

Metal Shading Language:
  12 compute kernels (.metal files)
```
