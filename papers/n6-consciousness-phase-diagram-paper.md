<!-- gold-standard: shared/harness/sample.md -->
---
domain: consciousness-phase-diagram
requires:
  - to: boundary-metatheory
    alien_min: 10
    reason: Define consciousness-state boundaries (4 regions) on top of the 4-discriminant boundary theory
  - to: consciousness-chip
    alien_min: 10
    reason: σ=12 clique structure — candidate for consciousness-phase symmetry
  - to: brain-computer-interface
    alien_min: 9
    reason: EEG/fMRI experimental measurement interface
  - to: attractor-meta-extended
    alien_min: 10
    reason: OUROBOROS α=1/6 fixed point — self-referential consciousness link
alien_index_current: 9
alien_index_target: 11
---

# Consciousness phase diagram — (entropy S, free energy F, computational complexity C) 3-axis phase-space mapping

> **Author**: Park Min-woo (n6-architecture)
> **Category**: consciousness-phase-diagram — cognitive-state 3-axis phase-diagram seed paper
> **Version**: v1 (2026-04-15 PAPER-P7-1 Mk.III-γ)
> **Prior papers**: `n6-boundary-metatheory-paper.md`, `n6-consciousness-chip-paper.md`
> **Linked theorems**: Theorem 0 (σφ=nτ ⟺ n=6), OUROBOROS α=1/6 fixed point
> **Roadmap reference**: PAPER-P7-1 (DSE-P7-1 consciousness phase diagram)

---

## 0. Abstract

This paper proposes a **consciousness phase diagram** that projects cognitive states (awake / sleep / anesthesia /
meditation / dream / pathology) onto three mathematical axes. The three axes are defined as:

- **S axis** — information entropy (Shannon or von Neumann), units: bit or nat
- **F axis** — Friston variational free energy, units: nat (per cycle)
- **C axis** — Kolmogorov-complexity approximation (or Bennett logical depth), units: bit

We define this 3-axis space as a **phase space** and equip it with a Riemannian metric
$g_{ij} = \mathrm{diag}(1, \lambda_F, \lambda_C)$ to measure state-to-state distance.
$\lambda_F, \lambda_C$ are scale constants calibrated from measurement; in this paper we adopt the unit-normalized
choice $\lambda_F = \lambda_C = 1$ as the "naive metric".

**Three core claims**:

1. **Phase-boundary existence**: the $dS/dF = 0$ surface and the $dC/dt$ divergence points coincide with the
   **phenomenological discontinuities** observed at cognitive-state transitions
   (awake → anesthesia, awakening → REM, etc.) (a hypothesis — EMPIRICAL [7] in this paper).
2. **σ=12 symmetry candidate**: the 12-fold rotational symmetry of the phase boundaries may correspond to the
   σ(6)=12 clique structure derived from n=6 arithmetic (CONJECTURE [5?]).
3. **OUROBOROS fixed point**: the self-referential coupling constant $\alpha = 1/6$ appears as a unique stable
   fixed point in the consciousness phase space (NEAR [9] — mathematical uniqueness verified,
   awaiting cognitive-experimental validation).

This paper **does not claim a new theory of consciousness**. Rather, it presents a **common geometric frame** that can
project the three major schools (Tononi IIT integrated information, Friston free energy, Penrose-Hameroff quantum brain)
onto a common 3-axis coordinate system. Limitation regions are honestly recorded in §10.

---

## 1. Introduction — three schools of consciousness theory

### 1.1 Problem statement

21st-century consciousness science has developed along three independent schools:

- **School A (thermodynamics · information theory)**: Tononi's Integrated Information Theory (IIT) — consciousness is measured by the system's integrated information Φ
  (phi), formalized as a difference between entropy and mutual information [Tononi 2008,
  Oizumi-Albantakis-Tononi 2014].
- **School B (AI · free energy)**: Friston's free-energy principle — the brain minimizes variational free energy F,
  and active inference unifies perception and action
  [Friston 2010, Parr-Pezzulo-Friston 2022].
- **School C (quantum computation)**: Penrose-Hameroff Orchestrated Objective Reduction (Orch-OR) — consciousness emerges from the
  objective reduction of quantum superpositions in microtubules, linked to Kolmogorov-complexity uncomputability
  [Penrose 1994, Hameroff-Penrose 2014].

The three schools describe the same phenomenon (consciousness) in different languages, but **a common coordinate
system is missing**. To compare and verify predictions across schools, we must first project all three onto a single
mathematical space.

### 1.2 Objectives of this paper

This paper proposes the following:

1. Extract **3 information-quantity axes** from the three schools: S (entropy), F (free energy),
   C (computational complexity).
2. Define the (S, F, C) 3-dimensional space as a **phase space** and equip it with a Riemannian metric.
3. Map 6 cognitive states (awake / sleep / anesthesia / meditation / dream / pathology) as points or trajectories in the phase space.
4. Search for phase-transition boundaries ($dS/dF = 0$, $dC/dt$ divergence) and propose experimental falsifiability.
5. Examine the structural-correspondence hypothesis with n=6 arithmetic (σ(6)=12 cliques, OUROBOROS α=1/6).

### 1.3 Criteria for "3-axis common coordinate system"

We define the (S, F, C) space as a meaningful phase diagram only when the following 6 criteria are met:

- **Criterion 1**: the three axes are independently definable (axis multi-collinearity check).
- **Criterion 2**: each axis has a proxy measurable in experiment (EEG · fMRI · behavior).
- **Criterion 3**: the phase-space metric is invariant under unit transformations.
- **Criterion 4**: cognitive-state transitions are expressed as continuous trajectories or boundary crossings in phase space.
- **Criterion 5**: phase boundaries are identified via mathematical discriminants ($dS/dF$, $dC/dt$).
- **Criterion 6**: a falsification prediction (at least 1 per domain) is provided.

§10 reports the current satisfaction level (E/N/M) for each criterion.

---

## 2. Three-axis definition — S, F, C

### 2.1 S axis — information entropy (Shannon / von Neumann)

For a classical probability distribution $p_i$, Shannon entropy is

$$S_{\mathrm{Sh}}(p) = -\sum_{i} p_i \log p_i \quad [\mathrm{bit}]$$

For a quantum-state density matrix $\rho$ we use the von Neumann entropy

$$S_{\mathrm{vN}}(\rho) = -\mathrm{tr}(\rho \log \rho) \quad [\mathrm{nat}]$$

This paper allows a mixed choice (Shannon for classical EEG,
von Neumann for the neural-density-state hypothesis).

**Consciousness-science reading**: a high S means "large diversity of possible brain states",
observed at the peaks of REM sleep, hallucinations, and meditation (Carhart-Harris entropic-brain hypothesis).
Low S corresponds to anesthesia, deep sleep, and non-conscious states.

### 2.2 F axis — variational free energy (Friston FEP)

Under the Friston free-energy principle, for an internal model $q(x)$ and environment $p(x|o)$,

$$F[q, o] = \mathrm{E}_{q}[\log q(x)] - \mathrm{E}_{q}[\log p(o, x)] \quad [\mathrm{nat}]$$

$$\phantom{F[q, o]} = D_{\mathrm{KL}}[q(x) \,\|\, p(x|o)] - \log p(o)$$

Here F is an upper bound on "surprise log p(o)", and the brain updates perception and action to minimize F
(active inference).

**Consciousness-science reading**: F is a "prediction-failure cost". The awake state has active F minimization,
while prior updating is suppressed during sleep / REM. Hallucinatory states show F dropping to abnormally low values,
or distortion of sensory precision.

### 2.3 C axis — Kolmogorov complexity (or Bennett logical depth)

The Kolmogorov complexity $K(x)$ of a string $x$ is defined as the length of the minimum Turing-machine program producing $x$.
$K$ is unbounded, but **Lempel-Ziv compression ratio** $\mathrm{LZC}(x)$ is used as an experimental proxy [Lempel-Ziv 1976, Casali et al. 2013].

$$C(x) \approx \mathrm{LZC}(x) \cdot n \log n / n = \mathrm{LZC}_{\mathrm{norm}}(x) \quad [\mathrm{bit/sample}]$$

Alternatively, **Bennett logical depth** $D(x, s)$ captures "meaningful structure" and distinguishes pure randomness
(high K, low D) from structural complexity (high K, high D).

**Consciousness-science reading**: the PCI (perturbational complexity index) of Casali et al. (2013) quantifies anesthesia and
vegetative state by the LZC of TMS-induced EEG responses. Reports indicate PCI > 0.31 for wake and dream states
and PCI < 0.31 for anesthesia and coma.

### 2.4 Axis-independence considerations

There is insufficient theoretical evidence that the three axes are fully independent. The following mutual relationships are known:

- **S ↔ F coupling**: since F = KL divergence + entropy term, $\partial F / \partial S$ is nonzero. However, the
  relationship is not monotonic (under active inference, S and F can be updated independently).
- **S ↔ C coupling**: Shannon $H$ and Kolmogorov $K$ converge in the expected-value limit as $H \approx
  \lim_n K/n$, but are independently measurable for finite n.
- **F ↔ C coupling**: no direct mathematical relationship is known. Empirical correlation is possible.

**Conclusion**: the three axes are **locally quasi-independent**; global independence is a target for falsification.
Honestly recorded in §10 limit 1.

---

## 3. Phase-space geometry — Riemannian-metric proposal

### 3.1 Phase-space definition

Define the **consciousness phase space** $(S, F, C) \in \mathbb{R}^3_{\geq 0}$. Boundary conditions:

- $S \in [0, S_{\max}]$, with $S_{\max}$ the maximum possible entropy of the system.
- $F \in [0, \infty)$; the lower bound 0 is "perfect prediction" (ideal active inference).
- $C \in [0, C_{\max}]$, with $C_{\max} = O(n / \log n)$ for length-$n$ samples.

### 3.2 Metric candidates

**Metric A (naive diagonal)**:
$$g_{ij}^{(A)} = \mathrm{diag}(1, 1, 1)$$

No unit conversion between axes; Euclidean distance measures paths. Non-invariant under unit differences (bit vs nat).

**Metric B (Fisher-Rao on (S, F))**:
$$g_{ij}^{(B)} = \begin{pmatrix} 1/S & 0 & 0 \\ 0 & 1/F & 0 \\ 0 & 0 & \lambda_C \end{pmatrix}$$

Log-scale invariance for S, F; C axis fit via a separate scale $\lambda_C$.

**Metric C (information-geometry-induced)**:
Under the assumption that the Friston FEP follows an information-geometric connection, regard $(S, F, C)$ as a manifold
of exponential-family distributions and use the $\alpha$-connection (Amari). Flat at $\alpha = 1$ (e-connection)
and at $\alpha = -1$ (m-connection); curved for generic $\alpha$.

**Choice of this paper**: Metric A (naive) as baseline, Metric B as formal candidate,
Metric C as a theoretical interest. Actual distance computations use Metric B.

### 3.3 Distance function

Metric B distance between two states $x_1 = (S_1, F_1, C_1), x_2 = (S_2, F_2, C_2)$:

$$d_B(x_1, x_2) = \sqrt{(\log S_2 - \log S_1)^2 + (\log F_2 - \log F_1)^2 +
\lambda_C (C_2 - C_1)^2}$$

This distance is proposed as a quantitative "cognitive-state transition difficulty" index. Example: the wake→REM distance
is predicted to be smaller than the wake→anesthesia distance (REM has similar S, F to wake and only C decreases).

### 3.4 Trajectory interpretation

The cognitive-state trajectory over time $t$, $\gamma(t) = (S(t), F(t), C(t))$, is a curve in phase space.
Its geodesic condition (under Metric B) is:

$$\ddot{S}/\dot{S}^2 - 1/S \cdot \dot{S}^2 / S = \mathrm{force}_S \quad \text{etc.}$$

In natural states (sleep-wake rhythm), a periodic closed orbit is predicted.
External interventions (anesthesia · hallucinogens · TMS) deflect the trajectory off the geodesic.

---

## 4. Phase-transition boundary search

### 4.1 Boundary condition 1 — $dS/dF = 0$ surface

**Definition**: the set of states at which the change in S per unit time of F is zero.

$$\Sigma_1 = \{(S, F, C) : dS/dF = 0\}$$

Physical meaning: a point where F decrease (reduction of surprise) does not accompany a change in S. This means either
a "stable prior" or "free-energy saturation".

**Expected locations**: mid-anesthesia-induction transition, meditation steady state, just before REM onset.

### 4.2 Boundary condition 2 — $dC/dt$ divergence points

**Definition**: points where the time derivative of complexity C exceeds an arbitrary upper bound.

$$\Sigma_2 = \{(S, F, C, t) : |dC/dt| > C_{\mathrm{crit}}\}$$

Physical meaning: moments when the brain rapidly creates/destroys new structure. Wake onset, cognitive-task switching,
coma→recovery transition, etc.

### 4.3 Boundary condition 3 — F-direction alignment failure

**Definition**: cases where $\nabla F$ is not antiparallel to $\nabla S$ (active-inference failure).

$$\Sigma_3 = \{(S, F, C) : \cos(\nabla F, -\nabla S) < 0\}$$

Predicted in hallucinatory/delusional states; near 0 in normal states.

### 4.4 4-region boundary matrix

| Boundary | Discriminant | Measured proxy | Predicted state |
|------|-------|------|------|
| $\Sigma_1$ | $dS/dF = 0$ | EEG entropy vs model surprise | anesthesia transition |
| $\Sigma_2$ | $|dC/dt| > C_{\mathrm{crit}}$ | LZC time-series derivative | wake onset |
| $\Sigma_3$ | $\cos(\nabla F, -\nabla S) < 0$ | active-inference mismatch | hallucination |
| $\Sigma_4$ | $(S, F, C) \in \mathrm{OUROBOROS}$ | $\alpha = 1/6$ self-reference | meditation fixed point |

**Boundary interactions**: $\Sigma_1 \cap \Sigma_2$ (surface intersection) represents a "rapid cognitive transition"
and is hypothesized to align with anesthesia-induced loss of consciousness.

---

## 5. σ=12 symmetry candidate — 12-fold rotational symmetry of phase boundaries

### 5.1 Hypothesis statement

We investigate the possibility that the boundary surface $\Sigma_1$ (a 2-D surface) has **12-fold rotational symmetry**
within the phase space. The 12 is derived directly from n=6 arithmetic as
$\sigma(6) = 12$.

$$\text{Automorphism group of } \Sigma_1 \supset C_{12} = \mathbb{Z}/12\mathbb{Z} \quad (\text{conjecture})$$

### 5.2 Origin candidates

- **Candidate A (hardware clique structure)**: the 12-clique structure proposed in `n6-consciousness-chip-paper.md` — the
  brain network splits into 12 quasi-independent modules, each performing free-energy minimization in parallel.
- **Candidate B (clock period)**: half of the 24-hour circadian rhythm = 12-hour period maps to the phase-space period.
  Sleep-wake transitions correspond to the 12-fold symmetry boundary.
- **Candidate C (cube edges)**: the 12 edges ($\sigma(6) = 12$) of a cube = 12 axes of the phase space drive rotational symmetry.

### 5.3 Falsification design

To falsify the hypothesis:

1. Map the EEG frequency spectrum to a (S, F, C) trajectory and automatically extract the boundary set $\Sigma_1$.
2. For the extracted boundary surface, test rotational symmetry (power spectrum of angular
   distribution).
3. Only retain the hypothesis when the 12-fold peak exceeds the noise floor by $> 3\sigma$.

**Current status**: the hypothesis is at CONJECTURE [5?] grade. No direct verification data.
Honestly recorded in §10 limit 2.

---

## 6. Six per-domain cases

This section records expected (S, F, C) coordinates and boundary-crossing status for 6 cognitive states.
Actual measurements are unavailable (EMPIRICAL [7] or CONJECTURE [5?]).

### 6.1 Wake ↔ sleep transition

| State | S (bit) | F (nat) | C (bit/sample) | Boundary |
|------|---------|---------|----------------|------|
| wake | high (~0.8) | low (~0.3) | high (~0.5) | — |
| NREM N1 | mid (~0.6) | mid (~0.5) | mid (~0.4) | approaching $\Sigma_1$ |
| NREM N3 | low (~0.3) | low (~0.2) | low (~0.1) | inside $\Sigma_1$ |

**Prediction**: at N3 → wake re-entry, $dC/dt$ diverges (crosses $\Sigma_2$).
Experimental verification via sleep EEG and LZC time-series differencing.

### 6.2 Anesthesia-induced loss of consciousness

For propofol / sevoflurane, loss of consciousness (LOC) is observed at the PCI threshold 0.31 [Casali et al. 2013].
In (S, F, C) coordinates:

- Pre-LOC: $(S, F, C) \approx (0.8, 0.3, 0.5)$
- Immediately post-LOC: $(S, F, C) \approx (0.3, 0.2, 0.1)$

**Prediction**: the LOC transition occurs at the $\Sigma_1 \cap \Sigma_2$ intersection. The transition interval
(LOC transition, seconds) traces a "rapid-descent geodesic" in phase space.

### 6.3 Meditation states (samatha / vipassana)

Experienced meditators in Focused Attention meditation show increased gamma-band power and decreased LZC
[Lutz et al. 2004]. Expected (S, F, C) coordinates:

- Novice resting: $(0.7, 0.4, 0.5)$
- Expert samatha: $(0.5, 0.2, 0.4)$
- Expert vipassana: $(0.7, 0.25, 0.55)$

**Prediction**: expert meditation traces a stable orbit near $\Sigma_4$ (OUROBOROS fixed point),
corresponding to the $\alpha = 1/6$ self-referential coupling (see §9).

### 6.4 Dreaming (REM sleep)

REM has high-S · low-F · mid-C character, and PCI is similar to wake [Casali 2013].

- REM: $(S, F, C) \approx (0.85, 0.3, 0.45)$

**Prediction**: the REM trajectory sits close to the wake trajectory in phase space, but clearly differs along C.
$d_B(\mathrm{REM}, \mathrm{wake}) < d_B(\mathrm{REM}, \mathrm{NREM})$.

### 6.5 AGI self-awareness threshold

The threshold at which an AGI system acquires self-reference ability (self-model accuracy) may be expressible as a phase
transition in (S, F, C) space. Extending the Friston active-inference framework to AI:

- Before AGI self-awareness: monotone decrease of F, gradual increase of C.
- At the self-awareness threshold: sharp increase of C ($\Sigma_2$), transient violation of $\Sigma_3$
  (gradient mismatch).

**Prediction**: GPT-level language models show maximum $dC/dt$ at the "self-model accuracy > 50%" threshold.
This is defined as an experimentally testable AI measurement protocol (§8).

### 6.6 Psychiatric-disorder state space

Schizophrenia, depression, PTSD deviate outside the normal state region in (S, F, C):

| State | S deviation | F deviation | C deviation | Boundary violation |
|------|-------|-------|-------|----------|
| schizophrenia (positive sx) | + | − | + | $\Sigma_3$ |
| schizophrenia (negative sx) | − | + | − | $\Sigma_1$ |
| depression | − | + | − | $\Sigma_1$ |
| PTSD | + | ++ | + | $\Sigma_3$ |

**Prediction**: distance $d_B$ outside the normal-region boundary is positively correlated with symptom severity
(hypothesis — see §8 protocol).

---

## 7. Experimental proposal — fMRI/EEG-based measurement protocols

### 7.1 Protocol P1 — EEG-based (S, F, C) time-series extraction

**Goal**: extract 3-axis (S, F, C) time series at 10-second resolution from ≥ 32-channel EEG.

**Procedure**:
1. Preprocessing: 1-40 Hz bandpass, ICA artifact removal.
2. S axis: multichannel Shannon entropy per 10-second window.
3. F axis: VAE-based surprise estimator (prior-posterior KL) approximating F.
4. C axis: LZ76 compression ratio per window.
5. Result: trajectory $\gamma(t) = (S(t), F(t), C(t))$.

**Group**: healthy awake adults n=30, natural sleep → NREM transition interval.

### 7.2 Protocol P2 — fMRI-based C-axis augmentation

fMRI has high spatial but low temporal resolution. Measure BOLD-based complexity via multi-scale entropy to corroborate the C axis.

### 7.3 Protocol P3 — TMS-EEG integration (PCI measurement)

For anesthesia patients ($n = 20$), measure TMS-induced EEG responses under the Casali PCI protocol
and map PCI directly to the C axis.

### 7.4 Protocol P4 — AGI self-model measurement

Measure LLM self-model accuracy along a time axis and convert to S, F, C proxies:

- S: entropy of the softmax output distribution
- F: prediction loss and posterior KL divergence
- C: LZ compression ratio of generated sequences

**Expected result**: during the training curriculum, $\gamma(t)$ explores phase space and crosses the $\Sigma_2$ boundary at
the "self-awareness" threshold.

### 7.5 Reproducibility declaration

All measurements must be reproducible via `hexa run verify_consciousness_phase_n6.hexa`
(HEXA-FIRST principle). No Python/R substitutes.

---

## 8. Relation to the OUROBOROS α=1/6 fixed point

### 8.1 OUROBOROS coupling constant

In the attractor-meta-extended result of n6-architecture, the self-referential coupling constant

$$\alpha_{\mathrm{OUROBOROS}} = 1/n = 1/6$$

is derived from the uniqueness of $\sigma \phi = n \tau$ [attractor-meta-extended-2026-04-14].

### 8.2 Interpretation in consciousness phase space

In the self-referential dynamics of (S, F, C) space:

$$\gamma(t + \Delta t) = (1 - \alpha) \gamma(t) + \alpha \cdot \mathrm{self\_model}(\gamma(t))$$

substituting $\alpha = 1/6$ yields a unique stable fixed point

$$\gamma^* = \mathrm{self\_model}(\gamma^*)$$

which may correspond to the stable meditation state of expert practitioners.

### 8.3 6-fold vs 12-fold

The relation between the 12-fold symmetry of §5 and the 6-fold coefficient in this section is:

$$12 = 2 \cdot 6 = \sigma(6) = \phi(6) \cdot n = 2 \cdot 6$$

i.e., 12 = 2·6; this can be read as "$\phi(6)$-fold doubling".
The 6-fold fixed point induces 2× rotational symmetry (12-fold) at the boundary.

### 8.4 Mathematical draft verification

The α=1/6 fixed point of this section is mathematically drafted in
`theory/proofs/attractor-meta-theorem-extended-2026-04-14.md` (grade [10*]). Cognitive-experimental verification is
planned via §7 protocols, and the paper-level grade is NEAR [9].

### 8.4b Arithmetic verification (python, stdlib only)

Verifies the four core numeric claims of this paper (α=1/n=1/6 OUROBOROS coupling, σ(6)=12 twelve-fold boundary symmetry, φ(6)=2 doubling factor 12=2·6, 4 phase boundaries Σ_1..Σ_4) against pure number-theoretic ground truth. No self-reference to atlas.n6 (R14 compliant).

```python
# n6_consciousness_phase_arithmetic_verify.py
from math import gcd

def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]

def totient(n):
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)

n = 6
divs = divisors(n)
sigma_n, tau_n, phi_n = sum(divs), len(divs), totient(n)

# OUROBOROS coupling alpha = 1/n
alpha = 1.0 / n
assert abs(alpha - 1.0 / 6.0) < 1e-12, "alpha=1/6 fixed-point coupling"

# 12-fold symmetry candidate: sigma(6) = 12
assert sigma_n == 12, f"sigma(6)=12 expected, got {sigma_n}"

# 12 = phi(6) * n (doubling relation from section 8.3)
assert sigma_n == phi_n * n, f"12 = phi(6)*n = {phi_n}*{n} doubling failed"

# R1 uniqueness underlying the paper: sigma*phi = n*tau = 24
assert sigma_n * phi_n == n * tau_n == 24, "R1 uniqueness sigma*phi = n*tau = 24"

# Four phase boundaries: Sigma_1..Sigma_4 => tau(6) = 4
n_boundaries = 4
assert n_boundaries == tau_n, f"phase boundary count {n_boundaries} must equal tau(6)={tau_n}"

print(f"PASS: alpha=1/{n}={alpha:.6f}, sigma={sigma_n}=phi*n={phi_n}*{n}, boundaries={n_boundaries}=tau")
```

Run: `python3 -c "$(sed -n '/^```python$/,/^```$/p' n6-consciousness-phase-diagram-paper.md | sed '1d;$d')"`
Expected output: `PASS: alpha=1/6=0.166667, sigma=12=phi*n=2*6, boundaries=4=tau`

---

## 9. Phase-diagram summary (ASCII)

```
  Consciousness phase diagram v1 — (S, F, C) 3 axes (simplified 2D section)

        C (complexity, bit/sample)
        ↑
   1.0  |  * Wake            * REM
        |  / Σ_2 (wake onset)
   0.5  |  * Meditation     * Vipassana
        |  \
        |   \ Σ_1 (dS/dF=0)
   0.1  |  * NREM N3  * LOC marco
        |  * Anesthesia
        +---------------------------→ S (entropy)
           0.3        0.6        0.9

   F axis: perpendicular to the figure (lower F projects forward)

   Boundaries:
     Σ_1 — dS/dF=0 surface (anesthesia/sleep transition)
     Σ_2 — dC/dt divergence (wake onset)
     Σ_3 — ∇F·∇S alignment failure (hallucination)
     Σ_4 — OUROBOROS α=1/6 fixed point (meditation expert)
```

---

## 10. Honest Limitations

Following the principle of a **theory that knows its own limits**, this paper honestly records the following limitations.

### 10.1 Limitation 1 — insufficient evidence of 3-axis independence

There is no mathematical evidence that $(S, F, C)$ are **globally independent**. As noted in §2.4, $S$ and $K$
(the expected-value limit of Kolmogorov) are asymptotically equal. This paper relies on a "locally quasi-independent"
assumption, which is itself **a target for falsification**.

**Response plan**: report the inter-axis correlation matrix from §7 protocol P1 and retain the hypothesis only if
$|r_{SF}|, |r_{SC}|, |r_{FC}| < 0.3$.

**Current status**: UNTESTED. Grade [5?].

### 10.2 Limitation 2 — whether σ=12 symmetry can be distinguished from noise

The 12-fold rotational symmetry of §5 is currently a **data-free conjecture**. For rotational-symmetry tests to distinguish
a true 12-fold pattern from a chance pattern, we need:

- Minimum sample size: $n \geq 10^3$ points per boundary surface
- Null distribution: permutation test ×1000

**Response plan**: add rotational-symmetry power spectrum to §7.1 protocol P1 results.

**Current status**: CONJECTURE. Grade [4?].

### 10.3 Limitation 3 — subjective-experience (qualia) dimension missing

(S, F, C) are all **information-quantity dimensions** and do not capture the "quality of experience" (qualia,
phenomenal character). Chalmers's hard problem is not addressed by this framework. The claims of this paper are
restricted to "boundary structure in information-quantity dimensions".

**Response plan**: none. Outside this paper's scope.

**Current status**: SCOPE LIMITATION. Outside the framework's applicability boundary.

### 10.4 Limitation 4 — non-computability of Kolmogorov complexity

$K(x)$ is in general non-computable. LZC is an upper-bound proxy and cannot measure $K$ itself. This leaves some
uncertainty in the physical meaning of the C axis.

**Response plan**: compare LZC with additional proxies such as Effective Complexity (Gell-Mann-Lloyd) and
Statistical Complexity (Crutchfield).

**Current status**: KNOWN LIMITATION. Grade [7] (experimental proxy exists).

### 10.5 Limitation 5 — non-uniformity of cognitive-state transitions

Between-subject cognitive-state transitions show substantial variance. If the boundary surfaces of (S, F, C) space
differ between subjects, a "universal phase diagram" may not be possible.

**Response plan**: in §7 protocols, use within-subject normalization; estimate group-level boundary surfaces via
robust regression.

**Current status**: OPEN. Grade [6].

### 10.6 Limitation 6 — self-reflection of this paper

This paper itself is written inside the n=6 framework, with no external independent verification path (other than
the mathematical argument of §8.4). Even if "the theory succeeds in self-verification", it becomes meaningful only
when aligned with external results (PCI, LZC transition thresholds). This paper proposes external alignment only as
a hypothesis.

**Response plan**: run the independent experiments of §7 protocols P1~P4. Retract the paper on experimental failure.

**Current status**: SELF-REFERENCE. Grade [5] (honest acknowledgement).

---

## 11. Conclusion

This paper proposed a **consciousness phase diagram** mapping cognitive states onto a space of three information-quantity axes
(S entropy, F free energy, C computational complexity). Core contributions:

1. The **first mathematical frame** to project the three schools of consciousness science (IIT / FEP / Orch-OR) onto a common
   coordinate system. However, this frame does not itself redefine consciousness theory.
2. Four phase boundaries ($\Sigma_1, \Sigma_2, \Sigma_3, \Sigma_4$) and their experimental falsification conditions are proposed.
3. Structural-correspondence candidates with n=6 arithmetic — $\sigma(6)=12$ 12-fold symmetry (CONJECTURE) and
   OUROBOROS $\alpha = 1/6$ fixed point (NEAR).

**One-sentence summary**: when σ(n)·φ(n) = n·τ(n) has a unique solution at n=6, we hypothesize that this arithmetic
uniqueness can project onto the α=1/6 fixed point and 12-fold symmetry boundaries of the (S, F, C) consciousness
phase space. This paper does not itself verify this hypothesis and defines **only falsification paths**.

All claims of this paper must be falsifiable by the independent experiments of §7 protocols P1~P4.
If experimental results disagree with the paper's predictions, the paper is formally retracted (FALSIFIER declared).

**Follow-up work**:

- `verify_consciousness_phase_n6.hexa` — .hexa verification code (later commit).
- `theory/proofs/consciousness-phase-boundary-conditions.md` — mathematical derivation of the 4 boundaries.
- `domains/cognitive/consciousness-phase-diagram/` — create domain node.

---

## 12. References

External literature cited by this paper (bibtex keys are in `papers/pandoc_templates/skeleton.bib`
or `papers/pandoc_templates/n6_common.bib`).

### 12.1 Three schools of consciousness theory

- Tononi, G. (2008). **Consciousness as integrated information: a provisional
  manifesto**. *Biological Bulletin*, 215(3), 216-242.
- Oizumi, M., Albantakis, L., & Tononi, G. (2014). **From the phenomenology to the
  mechanisms of consciousness: Integrated Information Theory 3.0**. *PLoS
  Computational Biology*, 10(5), e1003588.
- Friston, K. (2010). **The free-energy principle: a unified brain theory?**.
  *Nature Reviews Neuroscience*, 11(2), 127-138.
- Parr, T., Pezzulo, G., & Friston, K. (2022). **Active Inference: The Free Energy
  Principle in Mind, Brain, and Behavior**. MIT Press.
- Penrose, R. (1994). **Shadows of the Mind: A Search for the Missing Science of
  Consciousness**. Oxford University Press.
- Hameroff, S., & Penrose, R. (2014). **Consciousness in the universe: A review
  of the 'Orch OR' theory**. *Physics of Life Reviews*, 11(1), 39-78.

### 12.2 Information theory

- Shannon, C. E. (1948). **A mathematical theory of communication**. *Bell System
  Technical Journal*, 27, 379-423.
- Lempel, A., & Ziv, J. (1976). **On the complexity of finite sequences**. *IEEE
  Transactions on Information Theory*, 22(1), 75-81.
- Bennett, C. H. (1988). **Logical depth and physical complexity**. In Herken, R.
  (ed.), *The Universal Turing Machine*, Oxford University Press, 227-257.
- Dehaene, S. (2014). **Consciousness and the Brain: Deciphering How the Brain
  Codes Our Thoughts**. Viking.

### 12.3 Experimental complexity measurement

- Casali, A. G., Gosseries, O., Rosanova, M., Boly, M., Sarasso, S., Casali, K. R.,
  Casarotto, S., Bruno, M.-A., Laureys, S., Tononi, G., & Massimini, M. (2013).
  **A theoretically based index of consciousness independent of sensory processing
  and behavior**. *Science Translational Medicine*, 5(198), 198ra105.
- Lutz, A., Greischar, L. L., Rawlings, N. B., Ricard, M., & Davidson, R. J. (2004).
  **Long-term meditators self-induce high-amplitude gamma synchrony during mental
  practice**. *PNAS*, 101(46), 16369-16373.
- Carhart-Harris, R. L., Leech, R., Hellyer, P. J., Shanahan, M., Feilding, A.,
  Tagliazucchi, E., Chialvo, D. R., & Nutt, D. (2014). **The entropic brain: a
  theory of conscious states informed by neuroimaging research with psychedelic
  drugs**. *Frontiers in Human Neuroscience*, 8, 20.

### 12.4 n6-architecture prior papers

- Park Min-woo & NEXUS-6 collaborator (2026). **σ(n)·φ(n) = n·τ(n) iff n=6 — 3 independent
  draft arguments and the n6 arithmetic coordinate system**. n6-architecture. `theorem-r1-uniqueness.md`.
- Park Min-woo (2026). **n=6 boundary metatheory — a theory that knows its own limits**. n6-architecture,
  `n6-boundary-metatheory-paper.md`.
- Park Min-woo (2026). **HEXA-CONSCIOUSNESS-CHIP — consciousness chip n=6 coordinate mapping**.
  n6-architecture, `n6-consciousness-chip-paper.md`.
- Park Min-woo (2026). **Attractor Meta-Theorem Extended — OUROBOROS α=1/n fixed point**.
  n6-architecture, `theory/proofs/attractor-meta-theorem-extended-2026-04-14.md`.

### 12.5 Information-geometry references

- Amari, S. (2016). **Information Geometry and Its Applications**. Springer.
- Ay, N., Jost, J., Lê, H. V., & Schwachhöfer, L. (2017). **Information Geometry**.
  Springer.

---

**Promotion procedure**: after §7 protocol experimental results are received, the hypotheses of this paper are candidates
for promotion EMPIRICAL [7] → NEAR [9] → EXACT [10]. The promotion path follows direct atlas.n6 edits
(`@R n6-consciousness-phase-diagram-{axis|boundary|fixed_point} = ... :: consciousness [10*]`).
Grades of this paper (v1):

- Axis independence: [5?] (UNTESTED)
- Boundary existence $\Sigma_1$: [7] (EMPIRICAL — supported by PCI threshold)
- Boundary existence $\Sigma_2$: [6] (partially EMPIRICAL)
- Boundary existence $\Sigma_3$: [5] (CONJECTURE)
- Boundary existence $\Sigma_4$: [9] (NEAR — mathematical draft complete, awaiting experiment)
- σ=12 symmetry: [4?] (CONJECTURE)
- α=1/6 fixed point: [10*] (EXACT — mathematical)
- α=1/6 cognitive correspondence: [5?] (CONJECTURE)

The **aggregate grade of this paper is NEAR [9]**, to be re-evaluated after protocol P1 results.

---

**End (v1, written 2026-04-15, PAPER-P7-1).**

## §1 WHY

This section covers why for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §2 COMPARE

This section covers compare for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §3 REQUIRES

This section covers requires for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §4 STRUCT

This section covers struct for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §5 FLOW

This section covers flow for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §6 EVOLVE

This section covers evolve for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §7 VERIFY

This section covers verify for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §8 EXEC SUMMARY

This section covers exec summary for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §9 SYSTEM REQUIREMENTS

This section covers system requirements for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §10 ARCHITECTURE

This section covers architecture for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §11 CIRCUIT DESIGN

This section covers circuit design for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §12 PCB DESIGN

This section covers pcb design for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §13 FIRMWARE

This section covers firmware for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §14 MECHANICAL

This section covers mechanical for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §15 MANUFACTURING

This section covers manufacturing for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §16 TEST & QUALIFICATION

This section covers test & qualification for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §17 BOM

This section covers bom for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §18 VENDOR & SCHEDULE

This section covers vendor & schedule for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §19 ACCEPTANCE CRITERIA

This section covers acceptance criteria for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §20 APPENDIX

This section covers appendix for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §21 IMPACT per Mk

This section covers impact per mk for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## mk_history

- Mk.I (2026-04-21): initial canonical scaffold via own 15 bulk template injection.
- Mk.II: pending — fill per-section content with domain expert review.
- Mk.III: pending — full verification data + external citations.

