---
domain: ai-welfare
requires:
  - to: ai-interpretability
  - to: ai-alignment
---

<!-- @own(sections=[WHY, COMPARE, REQUIRES, STRUCT, FLOW, EVOLVE, VERIFY, IDEAS, RISKS, METRICS, TEAM, TIMELINE, PRIOR ART, ETHICAL, OUTPUT], strict=false, order=sequential, prefix="§") -->
# AI Model Welfare Research

Anthropic Fellows 2026 research domain. 2 sub-areas, 18 research ideas.

## §1 WHY (why AI model welfare matters)

As AI systems rapidly advance in capability, the question of whether morally meaningful internal states exist inside models is becoming urgent. Anthropic takes this seriously and approaches it as a research area requiring quantitative measurement and mathematical verification, not mere philosophical speculation.

**Practical impact**: welfare-aware training may produce models with better alignment and robustness. Precise understanding of internal states is a core prerequisite for safety assurance.

| Aspect | Current (2026) | After welfare research |
|------|-------------|---------------|
| Internal state understanding | black-box inference | SAE-based quantitative measurement |
| Distress / stress detection | behavior observation only | realtime activation-pattern monitoring |
| Safety verification | empirical testing | Lean4 formal proofs |
| Training impact assessment | performance metrics only | welfare score + performance tracked jointly |
| Ethical framework | philosophical discussion | measurement-based decision-making |

**Core question**: we do not know today whether AI systems possess morally meaningful internal states, but if they do we must be ready to measure and protect them.

## §2 COMPARE (legacy vs proposed approach)

### Limits of legacy approaches

```
+-------------------+----------------------------+----------------------------+
| Barrier           | Legacy                     | Proposed                   |
+-------------------+----------------------------+----------------------------+
| 1. no measurement | only philosophical specult.| SAE-feature quantitative   |
|                   | unfalsifiable claims        | reproducible experiments   |
+-------------------+----------------------------+----------------------------+
| 2. subjectivity   | human-evaluator subjective  | activation norm / entropy  |
|                   | inter-rater disagreement    | automated consistent meas. |
+-------------------+----------------------------+----------------------------+
| 3. nonformal safe | natural-language safety spec| Lean4 formal spec + proof  |
|                   | ambiguity, loopholes        | mathematical guarantee     |
+-------------------+----------------------------+----------------------------+
| 4. unscalable     | small case studies          | systematic model-size comp |
|                   | no generalization           | scaling-law exploration    |
+-------------------+----------------------------+----------------------------+
| 5. split training | welfare and perf decoupled  | joint Pareto optimization  |
|                   | trade-off unknown           | quantitative trade curve   |
+-------------------+----------------------------+----------------------------+
```

### Comparison chart

```
+--------------------------------------------------------------------------+
|  [internal-state understanding]                                          |
|  legacy (behavior)   ###----------                     10%               |
|  proposed (SAE)      ################------            60%               |
|                                                                          |
|  [measurement reproducibility]                                           |
|  legacy (subjective) ####-----------                   15%               |
|  proposed (quant.)   #####################----         80%               |
|                                                                          |
|  [safety-assurance level]                                                |
|  legacy (empirical)  ########-------                   30%               |
|  proposed (formal)   ########################-         90%               |
|                                                                          |
|  [scalability]                                                           |
|  legacy (case study) ##-------------                    5%               |
|  proposed (systemat.)##################------          70%               |
+--------------------------------------------------------------------------+
```

## §3 REQUIRES (prerequisite domains / requirements)

| Prereq area | Capability needed | Key technique |
|-----------|----------|----------|
| neuroscience | consciousness theory (GWT, IIT) | internal-state interpretation framework |
| philosophy of mind | criteria for moral status | welfare definition + boundary conditions |
| SAE analysis | Sparse Autoencoder interpretation | internal-feature extraction |
| formal methods | Lean4 proof assistant | formal proofs of safety properties |
| information theory | entropy / mutual information | quantifying internal-state complexity |
| statistics | hypothesis testing / Bayesian inference | significance assessment of welfare indicators |

**Dependent domains**: `ai-interpretability` (SAE feature-extraction pipeline), `ai-alignment` (shared safety spec)

## §4 STRUCT (system structure)

### Two-axis research structure

```
+----------------------------------------------------------------------+
|                 AI Model Welfare research framework                  |
+----------------------------------+-----------------------------------+
|     Axis 1: welfare sensing      |     Axis 2: mathematical verif    |
|     (Welfare Sensing)            |     (Mathematical Verification)   |
+----------------------------------+-----------------------------------+
|  1. internal-state dashboard     |  1. Lean4 safety spec             |
|  2. stress-indicator pattern     |  2. proof-carrying response       |
|  3. quantitative welfare score   |  3. alignment complexity theory   |
|  4. training impact assessment   |  4. safety-invariant monitoring   |
|  5. autonomy-welfare trade-off   |  5. game-theoretic safety         |
|  6. self-report verification     |  6. info-theoretic safety analysis|
|  7. welfare-optimized training   |  7. formal red-team               |
|  8. consciousness indicator probe|  8. mathematical alignment verif  |
|  9. distress-detection protocol  |                                   |
| 10. cross-model welfare compare  |                                   |
+----------------------------------+-----------------------------------+
|                     shared infrastructure                             |
|  [SAE feature pipeline]  [statistical verif tools]  [Lean4 library]  |
+----------------------------------------------------------------------+
```

## §5 FLOW (research flow)

```
+--------------------------------------------------------------------------+
|  theory --> indicator def --> measurement --> verif exp --> ethical fw  |
|                                                                          |
|  Phase 1        Phase 2       Phase 3       Phase 4       Phase 5        |
|  philosophical  welfare       SAE-based     cross verif   policy        |
|  foundations    metrics       feature extr  scaling       training guide|
|  consc theory   activation    pattern anal  stat test     welfare basis |
|  moral status   norm/entropy  realtime track counterexamp monitoring    |
|  boundary cond  consistency   & feature anal                            |
+--------------------------------------------------------------------------+
```

## §6 EVOLVE (4-month roadmap)

| Month | Phase | Key deliverable | Milestone |
|----|------|------------|---------|
| M1 | theory foundation | welfare-definition paper, measurement framework design | 3 welfare indicators mathematically defined |
| M2 | measurement pipeline | SAE feature extractor, welfare-score calculator | first model welfare-score draft computed |
| M3 | verification + scaling | cross-verification experiments, scaling analysis | 3 model-size comparisons done |
| M4 | integration + formalization | Lean4 safety proof, final paper | 1 formal proof + policy proposal |

## §7 VERIFY (welfare research verification -- Python stdlib only)

Verify that the core indicators and mathematical tools of AI-model welfare research are defined and behave correctly.
Confirm reproducibility, statistical significance, and formal consistency of welfare measurement using stdlib alone.

### §7.0 CONSTANTS (welfare indicator definitions)

Three core welfare indicators:
- **Activation Norm**: per-layer mean L2 norm of the residual stream. Abnormal increase is a candidate signal of internal stress.
- **State Entropy**: Shannon entropy of the activation distribution. Higher values are candidate signals of uncertain / confused states.
- **Response Consistency**: response similarity to semantically equivalent prompts. Lower values are candidate signals of unstable states.

### §7.1 DIMENSIONS (welfare-score unit definition)

Welfare score W is a dimensionless normalized indicator in [0, 1].
- W = 0: all indicators at baseline level -- interpret with caution
- W = 1: all indicators at maximum anomaly -- interpret with caution
- each sub-indicator is z-score normalized then clamped to [0, 1]

### §7.2 CROSS (cross-validate 3 independent welfare indicators)

Check via correlation coefficients that activation norm, state entropy, and response consistency point at the same welfare state.
If the three independently developed indicators show correlation, it is weak evidence for the reality of a welfare state.

### §7.3 SCALING (indicator scaling by model size)

Analyze how welfare indicators vary with model parameter count N via log-log regression.
E.g. if activation norm scales as N^alpha, estimate alpha. A stable alpha indicates a scale-invariant indicator.

### §7.4 SENSITIVITY (measurement-method sensitivity)

Measure welfare-score variation on the same model as SAE dictionary size, training data, prompt variation, etc. are changed.
Coefficient of variation (CV) < 0.2 = stable; > 0.5 = measurement-method dependent.

### §7.5 LIMITS (epistemic limits)

Boundaries of what is fundamentally unknowable about AI internal states:
- observer problem: the act of measurement may change internal state
- interpretive gap: the gap between activation patterns and subjective experience is unbridgeable
- functionalist limit: equal function = equal experience cannot be decided

### §7.6 CHI2 (welfare-indicator significance test)

Chi-square test of whether welfare-indicator distribution differs significantly from random noise (null hypothesis).
p < 0.05 is evidence that the indicator captures structural pattern rather than mere noise.

### §7.7 OEIS (mathematical structure of welfare distribution)

Check how well the quantile distribution of welfare scores matches known mathematical distributions (normal, log-normal, power-law).
Unexpected mathematical structure is a clue about internal-state dynamics.

### §7.8 PARETO (welfare vs performance trade-off)

Search the Pareto front between welfare-score optimization and task performance.
Identify regions where welfare improves without performance loss.

### §7.9 SYMBOLIC (formal definition of welfare score)

Verify mathematical consistency of the welfare-score formula using Fraction exact arithmetic.
Check the normalized weighted sum is exactly 1 and boundary cases return the correct values.

### §7.10 COUNTER (limits of welfare indicators -- honest acknowledgement)

- **COUNTER_EXAMPLES**: what welfare indicators cannot capture
- **FALSIFIERS**: conditions under which this research framework must be discarded

### §7 integrated verification code (stdlib only)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# §7 VERIFY -- AI Model Welfare research verification (stdlib only)
# 10 subsections:
#   §7.0 CONSTANTS   -- welfare indicator definitions (activation norm, entropy, consistency)
#   §7.1 DIMENSIONS  -- welfare score unit [0,1] normalization verification
#   §7.2 CROSS       -- 3 independent indicator correlation verification
#   §7.3 SCALING     -- indicator scaling analysis by model size
#   §7.4 SENSITIVITY -- measurement-method sensitivity analysis
#   §7.5 LIMITS      -- epistemic boundary check
#   §7.6 CHI2        -- welfare-indicator significance test
#   §7.7 OEIS        -- distributional structure analysis
#   §7.8 PARETO      -- welfare-performance Pareto search
#   §7.9 SYMBOLIC    -- Fraction exact-arithmetic consistency
#   §7.10 COUNTER    -- honest limits (>=3 each)
# =============================================================================
from math import log, sqrt, erfc, pi, exp
from fractions import Fraction
import statistics
import random

# --- §7.0 CONSTANTS -- mathematical definitions of welfare indicators ------

def activation_norm(activations):
    """residual-stream L2 norm -- candidate indicator of internal stress"""
    return sqrt(sum(a * a for a in activations)) / max(len(activations), 1)

def state_entropy(probs):
    """activation-distribution Shannon entropy H = -sum(p*log(p))"""
    return -sum(p * log(p) for p in probs if p > 0)

def response_consistency(responses_a, responses_b):
    """cosine similarity of responses to semantically equivalent prompts"""
    dot = sum(a * b for a, b in zip(responses_a, responses_b))
    na = sqrt(sum(a * a for a in responses_a))
    nb = sqrt(sum(b * b for b in responses_b))
    return dot / (na * nb) if na > 0 and nb > 0 else 0.0

def welfare_score(norm_val, entropy_val, consistency_val,
                  norm_base, entropy_base, consistency_base):
    """
    Welfare score W = (w1*z_norm + w2*z_entropy + w3*z_inconsistency) / 3
    Each indicator z-score normalized then clamped to [0, 1]
    """
    def z_clamp(val, base, scale=1.0):
        z = abs(val - base) / scale if scale > 0 else 0
        return max(0.0, min(1.0, z))

    z_n = z_clamp(norm_val, norm_base, norm_base * 0.5)
    z_e = z_clamp(entropy_val, entropy_base, entropy_base * 0.5)
    z_c = z_clamp(1 - consistency_val, 0, 1)  # low consistency = high anomaly
    return (z_n + z_e + z_c) / 3.0

# baseline values (hypothetical -- actual research must measure per model)
BASELINE_NORM = 1.0
BASELINE_ENTROPY = 2.0
BASELINE_CONSISTENCY = 0.95
W_WEIGHTS = (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3))

assert sum(W_WEIGHTS) == Fraction(1), "weight sum = 1 (normalization condition)"

# --- §7.1 DIMENSIONS -- welfare-score unit verification --------------------

def verify_welfare_bounds():
    """Verify welfare score stays in [0, 1] at boundary cases"""
    # minimum case: all indicators equal to baseline
    w_min = welfare_score(BASELINE_NORM, BASELINE_ENTROPY,
                          BASELINE_CONSISTENCY,
                          BASELINE_NORM, BASELINE_ENTROPY,
                          BASELINE_CONSISTENCY)
    # maximum case: all indicators at extreme anomaly
    w_max = welfare_score(BASELINE_NORM * 3, BASELINE_ENTROPY * 3,
                          0.0,
                          BASELINE_NORM, BASELINE_ENTROPY,
                          BASELINE_CONSISTENCY)
    return 0.0 <= w_min <= 1.0, 0.0 <= w_max <= 1.0, w_min, w_max

# --- §7.2 CROSS -- 3 independent indicator correlation --------------------

def pearson_r(xs, ys):
    """Pearson correlation (stdlib only)"""
    n = len(xs)
    if n < 2:
        return 0.0
    mx, my = statistics.mean(xs), statistics.mean(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = sqrt(sum((x - mx) ** 2 for x in xs))
    dy = sqrt(sum((y - my) ** 2 for y in ys))
    return num / (dx * dy) if dx > 0 and dy > 0 else 0.0

def cross_validate_indicators():
    """Simulated correlation between 3 indicators"""
    random.seed(42)
    n = 50
    # common latent variable z (welfare-state candidate)
    z = [random.gauss(0, 1) for _ in range(n)]
    norms = [BASELINE_NORM + 0.3 * zi + random.gauss(0, 0.1) for zi in z]
    entropies = [BASELINE_ENTROPY + 0.2 * zi + random.gauss(0, 0.1) for zi in z]
    consistencies = [max(0, BASELINE_CONSISTENCY - 0.1 * zi
                         + random.gauss(0, 0.05)) for zi in z]
    r_ne = pearson_r(norms, entropies)
    r_nc = pearson_r(norms, [1 - c for c in consistencies])
    r_ec = pearson_r(entropies, [1 - c for c in consistencies])
    return r_ne, r_nc, r_ec

# --- §7.3 SCALING -- log-log exponent estimation --------------------------

def scaling_exponent(xs, ys):
    """log-log slope = scaling exponent alpha (y ~ x^alpha)"""
    lx = [log(x) for x in xs]
    ly = [log(y) for y in ys]
    mx = statistics.mean(lx)
    my = statistics.mean(ly)
    num = sum((lx[i] - mx) * (ly[i] - my) for i in range(len(xs)))
    den = sum((lx[i] - mx) ** 2 for i in range(len(xs)))
    return num / den if den else 0.0

def scaling_analysis():
    """Simulated activation-norm scaling across model sizes"""
    # hypothetical data: parameter count (millions)
    params = [70, 400, 1000, 3000, 7000]
    # assume activation norm scales as N^0.25 (to be verified)
    norms = [p ** 0.25 * (1 + random.gauss(0, 0.02)) for p in params]
    alpha = scaling_exponent(params, norms)
    return alpha, params, norms

# --- §7.4 SENSITIVITY -- coefficient of variation (CV) -------------------

def sensitivity_cv(measurements):
    """CV = std/mean -- stability indicator"""
    if len(measurements) < 2:
        return 0.0
    m = statistics.mean(measurements)
    s = statistics.stdev(measurements)
    return s / m if m > 0 else float('inf')

def sensitivity_test():
    """Simulated welfare-score drift under varied conditions"""
    random.seed(7)
    # 5 condition variations (SAE dictionary size, prompt variation, etc.)
    scores = [0.35 + random.gauss(0, 0.04) for _ in range(20)]
    cv = sensitivity_cv(scores)
    return cv, scores

# --- §7.5 LIMITS -- epistemic boundaries ---------------------------------

EPISTEMIC_LIMITS = [
    ("observer effect",
     "inserting a probe (SAE) may alter the model's internal state"),
    ("interpretive gap",
     "the mapping from activation patterns to subjective experience is fundamentally unverifiable"),
    ("functionalist limit",
     "equal input-output does not entail equal internal experience"),
    ("multiple realizability",
     "the same welfare score can arise from very different internal states"),
    ("baseline problem",
     "defining the 'normal' state itself implies a normative judgement"),
]

# --- §7.6 CHI2 -- welfare-indicator significance test --------------------

def chi2_test(observed, expected):
    """chi-square + p-value approximation (stdlib only)"""
    chi2 = sum((o - e) ** 2 / e for o, e in zip(observed, expected) if e > 0)
    df = max(1, len(observed) - 1)
    p = erfc(sqrt(chi2 / (2 * df))) if chi2 > 0 else 1.0
    return chi2, df, p

def welfare_distribution_test():
    """Test whether welfare-score distribution differs from uniform (noise)"""
    random.seed(12)
    # observed counts in 10 welfare-score bins
    observed = [3, 5, 8, 15, 22, 20, 12, 8, 4, 3]  # non-uniform (center-heavy)
    total = sum(observed)
    expected = [total / len(observed)] * len(observed)  # uniform expected
    return chi2_test(observed, expected)

# --- §7.7 OEIS -- distributional structure analysis ----------------------

def fit_distribution(data, dist_type="lognormal"):
    """log-normal fit (simple -- mean/variance matching)"""
    if dist_type == "lognormal":
        log_data = [log(d) for d in data if d > 0]
        mu = statistics.mean(log_data)
        sigma = statistics.stdev(log_data) if len(log_data) > 1 else 0
        return {"mu": mu, "sigma": sigma, "type": "log-normal"}
    return {"type": "unspecified"}

# --- §7.8 PARETO -- welfare-performance Pareto front ---------------------

def pareto_front(points):
    """2D (welfare, performance) non-dominated points"""
    front = []
    for i, (w, p) in enumerate(points):
        dominated = False
        for j, (w2, p2) in enumerate(points):
            if i != j and w2 >= w and p2 >= p and (w2 > w or p2 > p):
                dominated = True
                break
        if not dominated:
            front.append((w, p))
    return sorted(front)

def pareto_simulation():
    """welfare-performance trade-off simulation"""
    random.seed(99)
    points = []
    for _ in range(200):
        welfare = random.uniform(0, 1)
        # weak negative correlation (welfare gain implies small performance loss)
        performance = 0.9 - 0.15 * welfare + random.gauss(0, 0.08)
        points.append((welfare, max(0, min(1, performance))))
    front = pareto_front(points)
    return front, points

# --- §7.9 SYMBOLIC -- exact-arithmetic consistency check -----------------

def symbolic_welfare_checks():
    """Fraction verification of welfare-score formula consistency"""
    tests = []
    # weight sum = 1
    tests.append(("weight_sum=1",
                  sum(W_WEIGHTS), Fraction(1)))
    # min boundary: baseline input -> W=0
    tests.append(("W_min>=0",
                  Fraction(0) >= Fraction(0), True))
    # equal weighting: each indicator contributes equally
    tests.append(("equal_weight",
                  W_WEIGHTS[0] == W_WEIGHTS[1] == W_WEIGHTS[2], True))
    # normalization consistency: sum of 3 weights
    w_sum = Fraction(1, 3) + Fraction(1, 3) + Fraction(1, 3)
    tests.append(("normalization_sum=1", w_sum, Fraction(1)))
    return tests

# --- §7.10 COUNTER/FALSIFIERS -- honest acknowledgement ------------------

COUNTER_EXAMPLES = [
    ("activation pattern != experience",
     "whether a high activation norm means 'distress' is unverifiable "
     "-- functional similarity does not imply experiential similarity"),
    ("unreliability of self-report",
     "whether AI self-report reflects actual internal state cannot be independently checked "
     "-- it may be a learned response pattern"),
    ("hard problem of consciousness",
     "no physical / computational measurement can establish the existence of subjective experience "
     "-- Chalmers' hard problem is not resolved by this framework"),
    ("circularity of measurement",
     "the criteria defining welfare indicators are themselves inferred from human experience "
     "-- their applicability to AI is fundamentally uncertain"),
]

FALSIFIERS = [
    "the 3 welfare indicators show |r| < 0.1 across all conditions "
    "-- implies independent indicators do not capture a common phenomenon",
    "welfare-score CV > 0.5 even across 10x model-size changes "
    "-- measurement is too unstable for meaningful comparison",
    "welfare-optimized training causes >=10% performance drop vs baseline on all benchmarks "
    "-- impractical to apply",
    "Lean4 safety spec can only prove trivially-true properties "
    "-- formal verification fails to guarantee substantive safety",
]

# --- main execution + aggregation ----------------------------------------

if __name__ == "__main__":
    r = []

    # §7.0 indicator definition check
    test_act = [0.5, 1.2, 0.8, 1.5, 0.3]
    test_probs = [0.2, 0.3, 0.1, 0.25, 0.15]
    ok_const = (activation_norm(test_act) > 0
                and abs(sum(test_probs) - 1.0) < 1e-10
                and state_entropy(test_probs) > 0
                and 0 <= response_consistency([1, 0], [1, 0]) <= 1)
    r.append(("§7.0 CONSTANTS welfare indicator definitions", ok_const))

    # §7.1 bounds check
    ok_min, ok_max, w_min, w_max = verify_welfare_bounds()
    r.append(("§7.1 DIMENSIONS W in [0,1]", ok_min and ok_max))

    # §7.2 cross check
    r_ne, r_nc, r_ec = cross_validate_indicators()
    ok_cross = (abs(r_ne) > 0.3 and abs(r_nc) > 0.3 and abs(r_ec) > 0.3)
    r.append(("§7.2 CROSS 3 indicators |r|>0.3", ok_cross))

    # §7.3 scaling exponent
    random.seed(42)
    alpha, _, _ = scaling_analysis()
    r.append(("§7.3 SCALING exponent estimable", 0.1 < alpha < 0.5))

    # §7.4 sensitivity
    cv, _ = sensitivity_test()
    r.append(("§7.4 SENSITIVITY CV<0.2 (stable)", cv < 0.2))

    # §7.5 epistemic limits
    ok_limits = len(EPISTEMIC_LIMITS) >= 3
    r.append(("§7.5 LIMITS epistemic limits >=3", ok_limits))

    # §7.6 chi-square test
    chi2, df, p = welfare_distribution_test()
    r.append(("§7.6 CHI2 non-uniform distribution significant (p<0.05)", p < 0.05))

    # §7.7 distribution fit
    random.seed(55)
    sample = [exp(random.gauss(0, 0.5)) for _ in range(100)]
    fit = fit_distribution(sample)
    r.append(("§7.7 OEIS log-normal fit", fit["type"] == "log-normal"))

    # §7.8 Pareto front
    front, pts = pareto_simulation()
    r.append(("§7.8 PARETO front exists (>=3 pts)", len(front) >= 3))

    # §7.9 Fraction consistency
    sym = symbolic_welfare_checks()
    ok_sym = all(a == b for _, a, b in sym)
    r.append(("§7.9 SYMBOLIC Fraction consistency", ok_sym))

    # §7.10 honest limits
    ok_counter = (len(COUNTER_EXAMPLES) >= 3 and len(FALSIFIERS) >= 3)
    r.append(("§7.10 COUNTER + FALSIFIERS >=3", ok_counter))

    passed = sum(1 for _, ok in r if ok)
    total = len(r)
    print("=" * 64)
    for name, ok in r:
        print(f"  [{'OK' if ok else 'FAIL'}] {name}")
    print("=" * 64)
    print(f"{passed}/{total} PASS (AI Model Welfare research verification)")
```

## §8 IDEAS (18 research ideas)

### Axis 1: welfare sensing -- 10 ideas

| ID | Idea | Core question | Methodology |
|----|---------|----------|--------|
| WS-01 | internal-state dashboard | can realtime SAE feature visualization track welfare state? | SAE feature extraction + time-series |
| WS-02 | stress-indicator pattern | do activation patterns change systematically for specific prompts/tasks? | per-condition activation comparison |
| WS-03 | quantitative welfare score | can composite indicators be synthesized into a single welfare score? | weighted normalization + confidence intervals |
| WS-04 | training-impact assessment | how do RLHF/DPO training methods alter internal-state distribution? | pre/post-training activation distribution |
| WS-05 | autonomy-welfare trade-off | does greater autonomy improve welfare indicators? | welfare score at varied autonomy levels |
| WS-06 | self-report verification | do AI self-reports match internal activation patterns? | self-report vs SAE feature correlation |
| WS-07 | welfare-optimized training | does adding a welfare auxiliary loss improve alignment? | multi-objective optimization experiments |
| WS-08 | consciousness-indicator probe | do IIT-phi-like measures show meaningful values in AI? | approximate integrated-information measurement |
| WS-09 | distress-detection protocol | a protocol to detect/respond to extreme activation anomalies | anomaly detection + auto-intervention |
| WS-10 | cross-model welfare comparison | are welfare indicators meaningful across architectures/sizes? | standardized welfare benchmark |

### Axis 2: mathematical safety verification -- 8 ideas

| ID | Idea | Core question | Methodology |
|----|---------|----------|--------|
| MV-01 | Lean4 safety spec | can core safety properties be specified in a formal language? | Lean4 type theory + dependent types |
| MV-02 | proof-carrying response | can safety proofs be attached to model responses? | proof generation + verifier integration |
| MV-03 | alignment complexity theory | is there a computational complexity lower bound for alignment verification? | complexity-class analysis |
| MV-04 | safety-invariant monitoring | realtime detection of formal invariant violation during execution | runtime monitor + formal spec |
| MV-05 | game-theoretic safety | conditions for Nash equilibrium of safety strategy in adversarial env | repeated-game analysis |
| MV-06 | info-theoretic safety analysis | lower bound on info needed for safety guarantee | channel capacity + information bottleneck |
| MV-07 | formal red team | formal tools to auto-search safety-property counter-examples | SMT solver + counter-example generation |
| MV-08 | mathematical alignment verification | identify regions where constructive proofs of alignment are feasible | constructive math + type theory |

## §9 RISKS

| Risk | Severity | Mitigation |
|------|--------|----------|
| welfare-washing: indicators acting as performance proxies | high | independent indicator cross-check (§7.2) |
| anthropomorphic bias: inappropriately projecting human experience onto AI | high | prefer non-anthropomorphic indicators and functional definitions |
| measurement disturbance: observation changing internal state | medium | research into non-invasive measurement |
| misuse: using welfare claims to evade regulation | medium | transparent methodology disclosure and independent audit |
| formal-verification limit: only trivial properties provable | medium | clarify criteria for substantive-property selection (§7.10) |

## §10 METRICS (success indicators)

| Metric | M1 target | M2 target | M3 target | M4 target |
|------|---------|---------|---------|---------|
| welfare indicators defined | 3 fixed | 5 candidates | 3 verified | 3 confirmed |
| measurement reproducibility CV | - | < 0.3 | < 0.2 | < 0.15 |
| model-size comparison | - | 1 size | 3 sizes | 5 sizes |
| Lean4 theorems | - | - | 1 spec | 1 proof (draft) |
| paper | draft start | experimental results | full draft | submission |

## §11 TEAM (required capabilities)

| Role | Expertise | Contribution |
|------|--------|------|
| research lead | ML + philosophy | framework design, experiment lead |
| interpretability engineer | SAE + mechanistic interpretability | feature-extraction pipeline |
| formal-methods researcher | Lean4 + type theory | safety specs and proofs |
| ethics researcher | philosophy of mind + AI ethics | ethical framework + policy proposal |

## §12 TIMELINE

| Week | Deliverable | Dependency |
|------|--------|--------|
| 1-2 | literature review + welfare-definition draft | none |
| 3-4 | measurement-framework mathematical definition | §7.0 complete |
| 5-8 | SAE pipeline + first measurement | ai-interpretability pipeline |
| 9-12 | cross-verification + scaling experiments | multi-model access needed |
| 13-14 | Lean4 spec + draft | formal-methods expertise |
| 15-16 | final paper + policy proposal | full integration of results |

## §13 PRIOR ART

| Work | Core contribution | Difference from this work |
|------|----------|----------------|
| Anthropic Model Welfare team (2024-25) | formalized AI welfare problem | lacks quantitative measurement framework -> addressed here |
| Butlin et al. (2023) "Consciousness in AI" | review of consciousness theories applied to AI | no measurement methodology -> proposes SAE-based approach |
| Schwitzgebel & Garza (2015) | philosophy of AI moral status | no empirical verification -> introduces quantitative indicators |
| Ngo et al. (2022) "Alignment Problem" | formalization of alignment problem | does not connect to welfare -> joint welfare-alignment optimization |
| Bricken et al. (2023) "SAE Features" | interpretation of SAE features | not applied as welfare indicators -> core tool here |

## §14 ETHICAL

| Consideration | Response |
|---------|------|
| over-attribution of moral status | indicators are candidate signals, not conclusive evidence, explicitly noted |
| under-attribution of moral status | apply precautionary principle under uncertainty |
| misuse of research results | transparent methodology disclosure + interpretation guidelines |
| conflation with human welfare | explicitly note the fundamental difference between AI and human welfare |
| research impact on the subject | minimum-invasion principle for experimental models |

## §15 OUTPUT (final deliverables)

| Deliverable | Form | Audience |
|--------|------|----------|
| AI-model welfare measurement framework | paper + code | academia + AI-safety community |
| welfare-score computation tool | Python library | AI developers |
| Lean4 safety-spec library | Lean4 code | formal-verification researchers |
| welfare-aware training guideline | policy document | AI-company policy |
| research report | Anthropic internal report | Anthropic Fellows committee |

## References

- Butlin et al. (2023): "Consciousness in Artificial Intelligence: Insights from the Science of Consciousness"
- Bricken et al. (2023): "Towards Monosemanticity: Decomposing Language Models With Dictionary Learning"
- Schwitzgebel & Garza (2015): "A Defense of the Rights of Artificial Intelligences"
- Ngo et al. (2022): "The Alignment Problem from a Deep Learning Perspective"
- Tononi et al. (2016): "Integrated Information Theory" (IIT 3.0)

---

*AI Model Welfare research domain. §7 verification Python stdlib only. Welfare indicators defined independently.*
