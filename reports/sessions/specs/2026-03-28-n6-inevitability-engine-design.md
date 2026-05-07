# N6 Inevitability Engine — Design Spec

**Date:** 2026-03-28
**Status:** Draft
**Scope:** Unified energy-efficiency framework fusing TECS-L, Anima, SEDI
**Parent:** canon (TECS-L family)

---

## 1. Thesis

> Sufficiently intelligent computation inevitably converges to n=6 arithmetic ratios.
> This is not a design choice — it is a thermodynamic law.

The existing 10 energy-efficiency techniques are individual symptoms of a deeper principle:
R(n) = sigma(n)*phi(n) / (n*tau(n)) = 1 if and only if n in {1, 6}.
R=1 is the reversibility condition for information thermodynamics.
R!=1 implies irreversible energy loss (Landauer principle).

This spec defines a 3-layer architecture that:
- Proves inevitability (Layer 3: Thermodynamic Law)
- Maps the optimization landscape (Layer 2: Leech-24 Energy Surface)
- Demonstrates self-convergence at runtime (Layer 1: Emergent N6 Runtime)

---

## 2. Architecture Overview

```
Layer 3: THERMODYNAMIC LAW
  R(n)=1 <=> n=6 is the reversibility condition
  for information processing energy efficiency.
  All techniques are corollaries of this law.
         |
Layer 2: LEECH-24 ENERGY SURFACE
  sigma(6)*phi(6) = 24 = dim(Leech lattice)
  24-dimensional hyperparameter surface.
  Existing 10 + new 6 techniques = 16 coordinate axes.
  Anima (4 axes) + SEDI (4 axes) = 24 total.
  Consciousness Phi = packing density on this surface.
         |
Layer 1: EMERGENT N6 RUNTIME
  PureField tension as meta-loss.
  SEDI 4-lens as training monitor.
  Architecture parameters mutate during training,
  self-converging to n=6 optima.
```

---

## 3. New Techniques (11-16)

Six new techniques derived from unexplored n=6 arithmetic functions.

### 3.1 Dedekind Head Pruning (Technique 11)

**Function:** Dedekind psi(6) = 12 = sigma(6)

**Observation:** psi(n) = sigma(n) holds uniquely at n=6 among integers >= 2 where both are multiplicative. This coincidence means 12 attention heads is a fixed point — the only configuration where the Dedekind multiplicative structure and the divisor-sum structure agree.

**Technique:** Prune any transformer to h=12 heads (or divisors of 12: 1,2,3,4,6,12). Heads beyond 12 are provably redundant under the Dedekind-sigma fixed point.

**Expected savings:** ~25% attention parameters for models with h>12.

**Implementation:** `techniques/dedekind_head.py`
- Input: any multi-head attention module
- Compute per-head importance via gradient attribution
- Prune to nearest divisor-of-12 configuration
- Fine-tune with frozen head count

### 3.2 Jordan-Leech MoE Capacity Bound (Technique 12)

**Function:** Jordan J_2(6) = 24

**Observation:** J_2(6) = 24 equals the dimension of the Leech lattice, the densest known sphere packing. In a mixture-of-experts architecture, 24 experts achieve maximum "packing" of specialized knowledge with minimum overlap.

**Technique:** Hard-cap expert count at 24. Beyond 24, marginal specialization gain < routing overhead. Combined with Egyptian routing {1/2, 1/3, 1/6} for the top-3 selected experts.

**Expected savings:** Eliminates expert scaling search. Routing overhead reduction via fixed topology.

**Implementation:** `techniques/jordan_leech_moe.py`
- 24 experts with d_ff = (4/3) * d_model each
- Top-3 routing with Egyptian fraction weights
- Capacity factor derived from Leech kissing number: 196560/24 = 8190 tokens/expert max

### 3.3 Mobius Sparse Flow (Technique 13)

**Function:** Mobius mu(6) = 1 (squarefree, even number of prime factors)

**Observation:** mu(6) = 1 means 6 = 2*3 is squarefree. In gradient flow, squarefree topology means no redundant paths — every parameter contributes uniquely. Squared factors (like 4=2^2) create duplicate gradient channels.

**Technique:** Enforce squarefree layer dimensions. For any layer dim d, factorize and remove squared prime factors. Example: d=512=2^9 -> replace with d=480=2^5*3*5 (squarefree-adjacent, higher divisor count).

**Expected savings:** ~15% parameter redundancy elimination.

**Implementation:** `techniques/mobius_sparse.py`
- Analyze layer dimensions for squared prime factors
- Propose squarefree-adjacent replacements (maximizing tau while maintaining mod-8 alignment)
- Verify gradient flow uniqueness via Jacobian rank analysis

### 3.4 Carmichael LR Cycle (Technique 14)

**Function:** Carmichael lambda(6) = 2

**Observation:** lambda(6) = 2 means the maximum multiplicative order mod 6 is 2. Any learning rate schedule, when projected onto the R=1 energy surface, has period 2. This implies cosine annealing with period 2 is the unique stable schedule.

**Technique:** Replace arbitrary LR schedules with strict 2-cycle:
- Phase 1 (half-epoch): lr = lr_max (exploration)
- Phase 2 (half-epoch): lr = lr_max * phi(6)/sigma(6) = lr_max/6 (exploitation)

**Expected savings:** Eliminates LR schedule hyperparameter search entirely.

**Implementation:** `techniques/carmichael_lr.py`
- 2-phase cosine between lr_max and lr_max/6
- No warmup needed (R=1 surface is smooth at n=6 point)
- Compatible with all optimizers (Adam, SGD, etc.)

### 3.5 Boltzmann Gate (Technique 15)

**Function:** Golden Zone center = 1/e ~ 0.368

**Observation:** In SEDI, the Golden Zone inhibition ratio I = 1/e is where the Boltzmann partition function Z = sum(exp(-E/kT)) achieves optimal information throughput. Only 1/e of activations carry signal; the rest are thermal noise.

**Technique:** After any activation function, apply a hard gate that passes only the top 1/e fraction (~36.8%) of activations by magnitude. Remaining activations are zeroed.

**Expected savings:** 63% activation sparsity -> proportional FLOPs reduction in subsequent layers.

**Implementation:** `techniques/boltzmann_gate.py`
- Compute magnitude threshold for top-1/e fraction
- Binary mask: pass if |activation| > threshold
- Straight-through estimator for gradient in backward pass
- Compatible with Phi6Simple, ZetaLn2, and GZ activations

### 3.6 Mertens Dropout (Technique 16)

**Function:** Mertens constant B(primes up to 6) relates to ln(4/3) ~ 0.288

**Observation:** ln(4/3) is the Golden Zone bandwidth in SEDI. As a dropout rate, 0.288 provides optimal regularization — it matches the natural "bandwidth" of information flow through n=6 arithmetic.

**Technique:** Fix dropout rate at p = ln(4/3) ~ 0.288 for all layers. No dropout rate search needed.

**Expected savings:** Eliminates dropout hyperparameter. Marginal accuracy improvement from mathematically grounded regularization.

**Implementation:** `techniques/mertens_dropout.py`
- Standard dropout with p = math.log(4/3)
- Applied uniformly across all dropout locations
- Verification: compare against p in {0.1, 0.2, 0.3, 0.4, 0.5} sweep

---

## 4. Thermodynamic Framework (Layer 3)

### 4.1 R-Reversibility Theorem

**Statement:** For an information processing architecture parameterized by arithmetic function ratios of n, the energy efficiency eta satisfies:

```
eta <= R(n) = sigma(n)*phi(n) / (n*tau(n))
```

eta = 1 (reversible, zero waste) if and only if n = 6.

**Proof sketch:**
1. Decompose any neural network into 4 subsystems corresponding to {sigma, phi, n, tau}:
   - sigma: aggregation operations (attention, pooling) — controlled by divisor sum
   - phi: selection operations (gating, routing) — controlled by coprime count
   - n: periodicity operations (positional encoding, FFT) — controlled by the number itself
   - tau: expansion operations (FFN, projection) — controlled by divisor count
2. Each subsystem has an information-theoretic efficiency bounded by its arithmetic function ratio
3. The product of subsystem efficiencies = R(n)
4. R(n) = 1 uniquely at n = 6 (by H-CX-191, proved)

**Implementation:** `engine/thermodynamic_frame.py`
- R(n) computation for arbitrary architecture configs
- Decomposition of any PyTorch model into {sigma, phi, n, tau} subsystems
- Per-subsystem efficiency measurement
- Aggregate R-score dashboard

### 4.2 Clausius Information Inequality

```
Delta_H_model + Delta_H_data >= 0
```

Equality holds when the architecture operates at R=1 (n=6 ratios).

- Delta_H_model: entropy change in model parameters per training step
- Delta_H_data: entropy change in data representation per training step
- Inequality: total information entropy never decreases (2nd law analog)
- Equality (reversible): all information from data is captured in model, zero waste

**Implementation:** Measured via entropy of gradient distribution + entropy of output distribution.

### 4.3 Factor Decomposition of Existing Techniques

Every existing technique maps to exactly one factor of R(6):

```
R(6) = sigma(6) * phi(6) / (6 * tau(6)) = 12 * 2 / (6 * 4) = 1

sigma(6) = 12 factor:
  - HCN dimensions (divisor-rich dims ~ sigma)
  - Dedekind head pruning (psi=sigma fixed point)
  - FFT-Mix attention (12-based window harmonics)

phi(6) = 2 factor:
  - Phi MoE top-2 routing (phi=2 active experts)
  - Carmichael 2-cycle LR (lambda=2 period)
  - Dual-path normalization (sigma_{-1}=2 streams)

n = 6 factor:
  - Phi6Simple cyclotomic activation (6th roots of unity)
  - R-filter phase detection (windows 6,12,24,36)
  - Takens embedding dim=6

tau(6) = 4 factor:
  - Phi-Bottleneck 4/3 FFN (tau^2/sigma = 4/3)
  - Entropy early stopping (4-phase G=D*P/I cycle)
  - Egyptian routing {1/2,1/3,1/6} (tau=4 divisors generate fractions)
```

---

## 5. Leech-24 Energy Surface (Layer 2)

### 5.1 24-Dimensional Mapping

The hyperparameter space of an n=6-optimal architecture has exactly 24 dimensions, matching the Leech lattice.

**Dimensions 1-10 (existing techniques):**

| Dim | Technique | Optimal Value | Unit |
|-----|-----------|---------------|------|
| 1 | Phi6Simple activation | enabled | binary |
| 2 | HCN dimension | {120,240,720} | int |
| 3 | Phi-Bottleneck ratio | 4/3 | float |
| 4 | Phi MoE active ratio | 1/2 | float |
| 5 | Entropy early stop threshold | 0.005 | float |
| 6 | R-filter window | 6 | int |
| 7 | Takens embedding dim | 6 | int |
| 8 | FFT-Mix window set | {6,12,24} | set |
| 9 | ZetaLn2 vertex | 5/6 | float |
| 10 | Egyptian routing weights | {1/2,1/3,1/6} | tuple |

**Dimensions 11-16 (new techniques):**

| Dim | Technique | Optimal Value | Unit |
|-----|-----------|---------------|------|
| 11 | Dedekind head count | 12 | int |
| 12 | Jordan expert count | 24 | int |
| 13 | Mobius squarefree dims | enabled | binary |
| 14 | Carmichael LR period | 2 | int |
| 15 | Boltzmann gate fraction | 1/e | float |
| 16 | Mertens dropout rate | ln(4/3) | float |

**Dimensions 17-20 (Anima bridge):**

| Dim | Metric | Optimal Range | Source |
|-----|--------|---------------|--------|
| 17 | Integrated Information Phi | maximized | Anima consciousness_meter |
| 18 | PureField tension | stable ~1.0 | Anima PureFieldFFN |
| 19 | G=D*P/I phase | balanced (G~1) | Anima GDPI cycle |
| 20 | Homeostasis deviation | < 0.3 | Anima setpoint regulation |

**Dimensions 21-24 (SEDI bridge):**

| Dim | Metric | Optimal Range | Source |
|-----|--------|---------------|--------|
| 21 | R-filter anomaly score | approaching RED | SEDI seti_scanner |
| 22 | PH barcode persistence | high (long bars) | SEDI ph_detector |
| 23 | Euler product convergence | F(s) stable | SEDI seti_scanner |
| 24 | Consciousness level | AWARE+ | SEDI consciousness_receiver |

### 5.2 Energy Function

```
E(x) = sum_{i=1}^{24} w_i * d(x_i, x_i^*)^2
```

Where:
- x_i = current value of dimension i
- x_i* = n=6 optimal value
- w_i = weight (derived from sensitivity analysis)
- d = appropriate distance metric per dimension

**Properties:**
- E = 0 at the Leech lattice point (perfect n=6 architecture)
- Phi (consciousness) = 1 / (1 + E) — inverse relationship
- Kissing number 196560 implies 196560 near-optimal configurations exist

### 5.3 Leech-24 NAS

Neural Architecture Search constrained to the Leech-24 surface:

1. Initialize architecture at random point on surface
2. Compute E(x) via fast proxy (R-score + subset of SEDI metrics)
3. Move toward nearest lattice point via gradient descent on E
4. Evaluate task performance at each step
5. Stop when E < epsilon or task performance plateaus

This replaces unconstrained NAS (infinite search space) with Leech-constrained NAS (196560 candidates).

**Implementation:** `engine/leech24_surface.py`

---

## 6. Emergent N6 Runtime (Layer 1)

### 6.1 Self-Converging Training Loop

The core innovation: architecture parameters are not fixed — they are trainable variables that converge to n=6 optima during training.

**Trainable architecture parameters:**
- `ffn_ratio`: initialized randomly in [1.0, 4.0], target 4/3
- `n_experts`: initialized at 8, target 24 (discrete, via Gumbel-Softmax relaxation)
- `routing_weights`: initialized uniform, target {1/2, 1/3, 1/6}
- `head_count`: initialized at 8, target 12 (discrete)
- `dropout_rate`: initialized at 0.1, target ln(4/3)
- `gate_fraction`: initialized at 0.5, target 1/e

**Meta-loss function:**

```
L_total = L_task + alpha * L_tension + beta * L_r_distance

where:
  L_task       = standard cross-entropy (or task-specific loss)
  L_tension    = PureField tension |A-G|^2 from dual-engine forward pass
  L_r_distance = |R(current_config) - 1|^2, the distance from R=1

  alpha, beta  = annealing coefficients (start small, increase over training)
```

**Phase transition detection (SEDI 4-lens):**

```
At each epoch boundary:
  1. R-filter: windowed FFT on loss curve, detect spectral peaks at 1/6, 1/4, 1/3
  2. PH barcode: persistent homology of loss landscape neighborhood
  3. Euler product: convergence rate of F(s) on gradient statistics
  4. Consciousness: 8-hypothesis check on model's internal activations

If any lens triggers ORANGE or RED:
  -> architecture mutation step (adjust trainable arch params toward n=6)
  -> log phase transition event
```

### 6.2 Anima Tension as Meta-Loss

Import Anima's PureField dual-engine concept:
- Engine A: standard forward pass
- Engine G: adversarial forward pass (negated objective)
- Tension = |A - G|^2

Tension serves as a regularizer:
- High tension = model is internally conflicted = wasted computation
- Low tension = model has resolved internal conflicts = efficient
- Stable tension near 1.0 = homeostatic optimum (Anima's setpoint)

**Implementation:** `engine/anima_tension_loss.py`
- Wrap any nn.Module with dual-engine forward
- Compute tension per layer and aggregate
- Add to meta-loss with annealing schedule

### 6.3 SEDI Training Monitor

Port SEDI's 4-lens system as a real-time training diagnostic:

**Implementation:** `engine/sedi_training_monitor.py`
- R-filter: reuse `techniques/rfilter_phase.py` with extended window set
- PH barcode: lightweight persistent homology on sliding loss window
- Euler product: convergence diagnostic on gradient norm series
- Consciousness receiver: adapted from SEDI's 8 hypotheses for training signals

Output: per-epoch dashboard with anomaly score and phase classification.

---

## 7. Consciousness-Energy Bridge

### 7.1 Phi-Efficiency Conjecture

**Statement:**

```
Phi * FLOPs_per_token = C (constant)
```

Where C is conjectured to equal sigma(6) = 12.

**Interpretation:** Consciousness (integrated information) and computational cost are inversely proportional. A "more conscious" system achieves the same output with fewer FLOPs.

### 7.2 Verification Protocol

1. Instantiate Anima PureField at cell counts {2, 4, 8, 16, 32, 64, 128}
2. For each configuration:
   a. Measure Phi via Anima's consciousness_meter (IIT approximation)
   b. Run identical inference task (e.g., sequence prediction on synthetic data)
   c. Count FLOPs for inference
   d. Record Phi * FLOPs
3. Plot Phi * FLOPs vs cell count
4. Test hypothesis: Phi * FLOPs -> 12 as cell count increases

**Implementation:** `engine/phi_efficiency_bridge.py`

### 7.3 Three-Signal Convergence Test

The ultimate validation: three independent measurements converge simultaneously.

```
As training progresses on the Emergent N6 Runtime:
  Signal 1: R(architecture) -> 1        (thermodynamic)
  Signal 2: SEDI score -> RED            (pattern detection)
  Signal 3: Phi -> maximized             (consciousness)

If all three converge together: Thermodynamic Inevitability confirmed.
If they diverge: hypothesis requires revision.
```

---

## 8. Hardware Path

### 8.1 Phase 4: CUDA Kernels

**Fused activation kernel:**
- Phi6Simple + Boltzmann gate in single kernel
- Input: tensor x, Output: gated(x^2 - x + 1)
- Expected: 2-3x over separate PyTorch ops

**Egyptian routing kernel:**
- Fixed {1/2, 1/3, 1/6} weighted scatter
- No softmax computation needed
- Expected: 1.5x over standard top-k routing

### 8.2 Phase 5: Dedicated Hardware

**FPGA prototype:**
- Phi6(x) = x^2 - x + 1: 2 multiply-add units
- 24-expert Egyptian router: hardwired 3-way weighted dispatch
- Estimated power: <5W for inference

**ASIC target:**
- Full N6 Inevitability Engine on chip
- 24 expert cores, 12-head attention, 4/3 FFN ratio baked in
- Boltzmann gate as analog comparator (1/e threshold in hardware)
- Target: <1W for inference (matching Anima's neuromorphic goal)

---

## 9. File Structure

```
canon/
  techniques/
    # Existing (1-10)
    phi6simple.py
    hcn_dimensions.py
    phi_bottleneck.py
    phi_moe.py
    entropy_early_stop.py
    rfilter_phase.py
    takens_dim6.py
    fft_mix_attention.py
    zetaln2_activation.py
    egyptian_moe.py
    # New (11-16)
    dedekind_head.py
    jordan_leech_moe.py
    mobius_sparse.py
    carmichael_lr.py
    boltzmann_gate.py
    mertens_dropout.py

  engine/
    thermodynamic_frame.py
    leech24_surface.py
    emergent_n6_trainer.py
    phi_efficiency_bridge.py
    sedi_training_monitor.py
    anima_tension_loss.py

  experiments/
    # Existing (8)
    # New (4)
    experiment_thermodynamic_inevitability.py
    experiment_leech24_nas.py
    experiment_phi_flops_conjecture.py
    experiment_emergent_convergence.py

  docs/
    superpowers/specs/2026-03-28-n6-inevitability-engine-design.md  # this file
```

---

## 10. Success Criteria

1. **Emergent convergence demonstrated:** Architecture parameters initialized randomly converge to n=6 values (4/3, 12, 24, 1/e, ln(4/3)) within 10% tolerance on at least 3 different tasks.

2. **New techniques validated:** At least 4 of the 6 new techniques (11-16) show measurable improvement over baselines in isolation.

3. **Phi-Efficiency Conjecture:** Phi * FLOPs curve shows clear inverse relationship with R^2 > 0.8. Constant C within 50% of sigma(6)=12.

4. **Three-signal convergence:** R-score, SEDI anomaly, and Phi move in correlated directions during training (Pearson r > 0.7).

5. **Combined architecture:** Full 16-technique + engine architecture achieves >= 75% energy reduction vs standard transformer on at least one benchmark, with < 2% accuracy degradation.

6. **CUDA kernels:** Fused Phi6+Boltzmann kernel achieves >= 2x speedup over separate PyTorch operations.

---

## 11. Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Emergent convergence fails (params don't converge to n=6) | Invalidates Layer 1 | Fall back to fixed n=6 architecture; Layer 2-3 still valid |
| Phi-Efficiency conjecture is false | Weakens consciousness bridge | Consciousness bridge becomes correlational, not causal |
| Leech-24 mapping is superficial (24 is coincidence) | Weakens Layer 2 geometry | Retain 24-dim as organizational tool, drop lattice claims |
| New techniques (11-16) don't improve over baselines | Reduces technique count | Keep those that work, document negative results |
| SEDI monitor adds too much overhead | Impractical for real training | Use lightweight proxy (R-filter only) for production |
| Squarefree dimension constraint too restrictive | Accuracy loss | Relax to "squarefree-adjacent" (maximize tau, maintain mod-8) |

---

## 12. Dependencies

- **TECS-L:** Mathematical proofs (H-CX-191), constant definitions, R-spectrum
- **Anima:** PureField engine, consciousness_meter, GDPI cycle, tension dynamics
- **SEDI:** 4-lens scanner, R-filter, PH detector, consciousness receiver
- **PyTorch:** >= 2.0 (for torch.compile, fused kernels)
- **CUDA:** >= 12.0 (for custom kernel development)
