#!/usr/bin/env python3
"""
Experiment: Harmonic Series Convergence
=======================================
Testing if H(sigma) = H(12) appears as a universal constant linking
disparate domains in the n=6 discovery system.

n=6 connection:
  - sigma(6) = 1+2+3+6 = 12, the divisor sum of the first perfect number
  - H(n) = sum(1/k, k=1..n) is the harmonic series
  - H(12) ~ 3.10321 emerges from standing wave analysis where m=12 gives Q=1.0
  - H(6) = 49/20 = 2.45, and 1/2 + 1/3 + 1/6 = 1 (Egyptian identity from 6's divisors)
  - Hypothesis: H(sigma) ~ 3.103 is a universal constant bridging domains

Algorithm:
  1. Compute H(n) for all n6-significant values: 1,2,3,4,5,6,12,24,48
  2. Check ratios H(sigma)/H(n) and differences H(sigma)-H(n) against n6 constants
  3. Egyptian fraction decomposition of H(sigma) using divisors of 6
  4. Cross-domain harmonic test: 10 domains with natural frequencies,
     check clustering of H values around H(12)
  5. Predict relationships between H(12), pi, phi, and other mathematical constants
"""

import math
import random
from fractions import Fraction

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
SIGMA_6 = 12          # sigma(6) = divisor sum of 6
PHI = (1 + math.sqrt(5)) / 2   # golden ratio ~ 1.618
N = 6

N6_CONSTANTS = {
    "n":           6,
    "sigma":       12,
    "J2":          48,
    "n*J2":        288,
    "phi":         PHI,
    "pi":          math.pi,
    "e":           math.e,
    "ln2":         math.log(2),
    "zeta2":       math.pi**2 / 6,   # pi^2/6 ~ 1.6449
    "euler_gamma": 0.5772156649,
    "1/6":         1/6,
    "1/3":         1/3,
    "1/2":         1/2,
    "2/3":         2/3,
    "sqrt6":       math.sqrt(6),
}

N6_SIGNIFICANT = [1, 2, 3, 4, 5, 6, 12, 24, 48]

DOMAINS = [
    "math",     # pure mathematics -- prime distribution
    "physics",  # quantum field harmonics
    "bio",      # circadian / neural oscillation
    "info",     # information channel capacity
    "mind",     # cognitive rhythm / attention
    "arch",     # architectural acoustics
    "ocean",    # tidal / wave period
    "music",    # harmonic series
    "chem",     # molecular vibration
    "astro",    # orbital resonance
]

EXACT_TOL = 0.01   # 1%
CLOSE_TOL = 0.05   # 5%

# ---------------------------------------------------------------------------
# Reproducible seed
# ---------------------------------------------------------------------------
random.seed(42)

# ---------------------------------------------------------------------------
# Harmonic number computation
# ---------------------------------------------------------------------------

def harmonic(n):
    """Compute H(n) = sum(1/k, k=1..n) using exact fractions."""
    h = Fraction(0)
    for k in range(1, n + 1):
        h += Fraction(1, k)
    return h


def harmonic_float(n):
    """Compute H(n) as a float."""
    return sum(1.0 / k for k in range(1, n + 1))


# ---------------------------------------------------------------------------
# Proximity check
# ---------------------------------------------------------------------------

def check_proximity(value, target, label=""):
    """Return (rel_error, grade) if value is close to target."""
    if abs(target) < 1e-15:
        return None
    rel_err = abs(value - target) / abs(target)
    if rel_err <= EXACT_TOL:
        return (rel_err, "EXACT", label)
    elif rel_err <= CLOSE_TOL:
        return (rel_err, "CLOSE", label)
    return None


# ---------------------------------------------------------------------------
# Egyptian fraction decomposition
# ---------------------------------------------------------------------------

def egyptian_fraction_greedy(frac):
    """Greedy algorithm for Egyptian fraction decomposition of a Fraction."""
    result = []
    remaining = Fraction(frac)
    max_iter = 50
    i = 0
    while remaining > 0 and i < max_iter:
        # Find smallest 1/k >= remaining
        k = math.ceil(1 / float(remaining))
        unit = Fraction(1, k)
        result.append(k)
        remaining -= unit
        i += 1
    return result


# ---------------------------------------------------------------------------
# Domain natural frequencies (from wave interference experiment)
# ---------------------------------------------------------------------------

def domain_base_freq(domain):
    """Return characteristic base frequency for each domain."""
    table = {
        "math":    6.0,
        "physics": 12.0,
        "bio":     4.0,
        "info":    3.0,
        "mind":    2.0,
        "arch":    24.0,
        "ocean":   1.0,
        "music":   18.0,
        "chem":    8.5,
        "astro":   7.7,
    }
    return table.get(domain, 5.0)


# ---------------------------------------------------------------------------
# Main experiment
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("  Experiment: Harmonic Series Convergence")
    print("  H(sigma) = H(12) as universal constant in n=6 system")
    print("=" * 70)

    # -----------------------------------------------------------------------
    # Phase 1: Compute H(n) for all n6-significant values
    # -----------------------------------------------------------------------
    print("\n[Phase 1] Harmonic numbers H(n) for n6-significant values")
    print("-" * 50)

    h_values = {}
    h_exact = {}
    for n in N6_SIGNIFICANT:
        h_exact[n] = harmonic(n)
        h_values[n] = float(h_exact[n])
        print("  H({:2d}) = {:<20s} = {:.6f}".format(
            n, str(h_exact[n]), h_values[n]))

    h_sigma = h_values[SIGMA_6]
    print("\n  ** H(sigma(6)) = H(12) = {:.6f}".format(h_sigma))
    print("  ** H(6)        = {}/{}  = {:.6f}".format(
        h_exact[6].numerator, h_exact[6].denominator, h_values[6]))

    # -----------------------------------------------------------------------
    # Phase 2: Check relationships between H values and n6 constants
    # -----------------------------------------------------------------------
    print("\n[Phase 2] H(sigma) ratio/difference scan against n6 constants")
    print("-" * 50)

    # 2a: Ratios H(sigma)/H(n)
    print("\n  [2a] Ratios H(12)/H(n):")
    ratio_hits = []
    for n in N6_SIGNIFICANT:
        if n == SIGMA_6:
            continue
        ratio = h_sigma / h_values[n]
        for cname, cval in N6_CONSTANTS.items():
            if abs(cval) < 1e-12:
                continue
            hit = check_proximity(ratio, cval, cname)
            if hit:
                ratio_hits.append((n, ratio, hit))
    for n, ratio, (rel_err, grade, cname) in sorted(ratio_hits, key=lambda x: x[2][0]):
        tag = "***" if grade == "EXACT" else "   "
        print("  {} H(12)/H({:2d}) = {:.6f}  ~ {}={:.6f}  err={:.4f}  [{}]".format(
            tag, n, ratio, cname, N6_CONSTANTS[cname], rel_err, grade))

    if not ratio_hits:
        print("    (no ratio matches found)")

    # 2b: Differences H(sigma) - H(n)
    print("\n  [2b] Differences H(12) - H(n):")
    diff_hits = []
    for n in N6_SIGNIFICANT:
        if n == SIGMA_6:
            continue
        diff = h_sigma - h_values[n]
        for cname, cval in N6_CONSTANTS.items():
            if abs(cval) < 1e-12:
                continue
            hit = check_proximity(diff, cval, cname)
            if hit:
                diff_hits.append((n, diff, hit))
    for n, diff, (rel_err, grade, cname) in sorted(diff_hits, key=lambda x: x[2][0]):
        tag = "***" if grade == "EXACT" else "   "
        print("  {} H(12)-H({:2d}) = {:.6f}  ~ {}={:.6f}  err={:.4f}  [{}]".format(
            tag, n, diff, cname, N6_CONSTANTS[cname], rel_err, grade))

    if not diff_hits:
        print("    (no difference matches found)")

    # 2c: H(6) = 49/20 = 2.45 check against n6 constants
    print("\n  [2c] H(6) = {:.6f} proximity check:".format(h_values[6]))
    h6_hits = []
    for cname, cval in N6_CONSTANTS.items():
        hit = check_proximity(h_values[6], cval, cname)
        if hit:
            h6_hits.append(hit)
    for rel_err, grade, cname in sorted(h6_hits, key=lambda x: x[0]):
        tag = "***" if grade == "EXACT" else "   "
        print("  {} H(6)={:.6f}  ~ {}={:.6f}  err={:.4f}  [{}]".format(
            tag, h_values[6], cname, N6_CONSTANTS[cname], rel_err, grade))
    # Also check H(6) against sqrt(6)
    print("    H(6)/sqrt(6) = {:.6f}".format(h_values[6] / math.sqrt(6)))

    if not h6_hits:
        print("    (no direct constant match)")

    # -----------------------------------------------------------------------
    # Phase 3: Egyptian fraction decomposition
    # -----------------------------------------------------------------------
    print("\n[Phase 3] Egyptian fraction analysis")
    print("-" * 50)

    # Egyptian identity from divisors of 6
    divs_6 = [1, 2, 3, 6]
    egyptian_sum = sum(Fraction(1, d) for d in divs_6)
    print("  Divisors of 6: {}".format(divs_6))
    print("  sum(1/d for d in divisors(6)) = {} = {:.6f}".format(
        egyptian_sum, float(egyptian_sum)))
    print("  Note: 1/2 + 1/3 + 1/6 = {} (Egyptian identity)".format(
        Fraction(1,2) + Fraction(1,3) + Fraction(1,6)))

    # Decompose H(12) as sum of 1/d contributions grouped by 6's structure
    print("\n  H(12) decomposition by divisor structure of 6:")
    # Group terms 1..12 by their relation to divisors of 6
    groups = {
        "divisors_of_6":   [1, 2, 3, 6],
        "multiples_of_6":  [6, 12],
        "coprime_to_6":    [1, 5, 7, 11],
        "even_non_div6":   [4, 8, 10],
        "odd_non_div6":    [9],
    }
    for gname, indices in groups.items():
        partial = sum(Fraction(1, k) for k in indices)
        print("    {:18s} {} = {} = {:.6f}".format(
            gname, indices, partial, float(partial)))

    # Greedy Egyptian fraction decomposition of H(12)
    print("\n  Egyptian fraction decomposition of H(12) = {}:".format(h_exact[12]))
    ef_denominators = egyptian_fraction_greedy(h_exact[12])
    ef_str = " + ".join("1/{}".format(d) for d in ef_denominators)
    ef_check = sum(Fraction(1, d) for d in ef_denominators)
    print("    H(12) = {}".format(ef_str))
    print("    Verification: sum = {} = {:.6f}".format(ef_check, float(ef_check)))
    print("    Denominator count: {}".format(len(ef_denominators)))
    # Check if any denominator is a multiple of 6
    div6_denoms = [d for d in ef_denominators if d % 6 == 0]
    print("    Denominators divisible by 6: {}".format(div6_denoms if div6_denoms else "none"))

    # -----------------------------------------------------------------------
    # Phase 4: Cross-domain harmonic test
    # -----------------------------------------------------------------------
    print("\n[Phase 4] Cross-domain harmonic clustering around H(12)")
    print("-" * 50)

    domain_h = {}
    for domain in DOMAINS:
        freq = domain_base_freq(domain)
        # Use floor of frequency as harmonic index (minimum 1)
        h_index = max(1, int(freq))
        h_val = harmonic_float(h_index)
        domain_h[domain] = (freq, h_index, h_val)
        # Check proximity to H(12)
        rel_err = abs(h_val - h_sigma) / h_sigma
        if rel_err <= EXACT_TOL:
            grade = "EXACT"
        elif rel_err <= CLOSE_TOL:
            grade = "CLOSE"
        else:
            grade = "---"
        tag = "***" if grade == "EXACT" else ("   " if grade == "CLOSE" else "   ")
        print("  {} {:8s}  freq={:5.1f}  H({:2d})={:.6f}  delta={:+.6f}  [{}]".format(
            tag, domain, freq, h_index, h_val, h_val - h_sigma, grade))

    # Clustering analysis: how many domains have H near H(12)?
    h_vals_list = [v[2] for v in domain_h.values()]
    mean_h = sum(h_vals_list) / len(h_vals_list)
    var_h = sum((v - mean_h)**2 for v in h_vals_list) / len(h_vals_list)
    std_h = math.sqrt(var_h)

    print("\n  Clustering statistics:")
    print("    Mean H across domains:  {:.6f}".format(mean_h))
    print("    Std dev:                {:.6f}".format(std_h))
    print("    H(12) target:           {:.6f}".format(h_sigma))
    print("    |mean - H(12)|:         {:.6f}".format(abs(mean_h - h_sigma)))

    # Count domains within 1 std of H(12)
    within_1std = sum(1 for v in h_vals_list if abs(v - h_sigma) <= std_h)
    print("    Domains within 1 std of H(12): {} / {}".format(
        within_1std, len(DOMAINS)))

    # Noise simulation: add jitter to frequencies and recheck
    print("\n  Monte Carlo stability (100 trials, freq jitter +/-10%):")
    cluster_counts = []
    for _ in range(100):
        trial_h = []
        for domain in DOMAINS:
            freq = domain_base_freq(domain)
            jittered = freq * (1 + 0.1 * (2 * random.random() - 1))
            h_idx = max(1, int(jittered))
            trial_h.append(harmonic_float(h_idx))
        count = sum(1 for v in trial_h if abs(v - h_sigma) / h_sigma <= CLOSE_TOL)
        cluster_counts.append(count)
    avg_cluster = sum(cluster_counts) / len(cluster_counts)
    max_cluster = max(cluster_counts)
    print("    Avg domains clustering at H(12): {:.2f}".format(avg_cluster))
    print("    Max cluster in any trial:        {}".format(max_cluster))

    # -----------------------------------------------------------------------
    # Phase 5: Mathematical constant relationships
    # -----------------------------------------------------------------------
    print("\n[Phase 5] H(12) relationships to mathematical constants")
    print("-" * 50)

    predictions = [
        ("H(12) * phi / n",       h_sigma * PHI / N),
        ("H(12) / pi",            h_sigma / math.pi),
        ("H(12) / e",             h_sigma / math.e),
        ("H(12) * ln(2)",         h_sigma * math.log(2)),
        ("H(12) - zeta(2)",       h_sigma - math.pi**2 / 6),
        ("H(12) / zeta(2)",       h_sigma / (math.pi**2 / 6)),
        ("H(12) * euler_gamma",   h_sigma * 0.5772156649),
        ("H(12)^2 / pi^2",       h_sigma**2 / math.pi**2),
        ("H(12) - ln(12)",        h_sigma - math.log(12)),
        ("H(12) - ln(12) - gamma", h_sigma - math.log(12) - 0.5772156649),
        ("6 * (H(12) - ln(12) - gamma)", 6 * (h_sigma - math.log(12) - 0.5772156649)),
    ]

    # Known constants to match against
    match_targets = {
        "1":           1.0,
        "1/2":         0.5,
        "1/3":         1/3,
        "1/6":         1/6,
        "2/3":         2/3,
        "phi":         PHI,
        "1/phi":       1/PHI,
        "pi/6":        math.pi/6,
        "sqrt(2)":     math.sqrt(2),
        "sqrt(3)":     math.sqrt(3),
        "sqrt(6)":     math.sqrt(6),
        "ln(2)":       math.log(2),
        "ln(6)":       math.log(6),
        "euler_gamma": 0.5772156649,
        "e":           math.e,
        "pi":          math.pi,
        "2":           2.0,
        "3":           3.0,
        "6":           6.0,
        "12":          12.0,
    }

    for label, value in predictions:
        best_match = None
        best_err = float('inf')
        for mname, mval in match_targets.items():
            if abs(mval) < 1e-15:
                continue
            rel_err = abs(value - mval) / abs(mval)
            if rel_err < best_err:
                best_err = rel_err
                best_match = mname
        grade = "EXACT" if best_err <= EXACT_TOL else ("CLOSE" if best_err <= CLOSE_TOL else "---")
        tag = "***" if grade == "EXACT" else ("  >" if grade == "CLOSE" else "   ")
        print("  {} {:35s} = {:.6f}  ~ {:12s} ({:.6f})  err={:.4f}  [{}]".format(
            tag, label, value, best_match, match_targets[best_match], best_err, grade))

    # Special: H(n) ~ ln(n) + gamma + 1/(2n)  (asymptotic)
    print("\n  Asymptotic check: H(n) ~ ln(n) + gamma + 1/(2n)")
    for n_val in N6_SIGNIFICANT:
        approx = math.log(n_val) + 0.5772156649 + 1.0 / (2 * n_val)
        actual = h_values[n_val]
        err = abs(approx - actual) / actual
        print("    H({:2d}): actual={:.6f}  approx={:.6f}  err={:.6f}".format(
            n_val, actual, approx, err))

    # -----------------------------------------------------------------------
    # Summary
    # -----------------------------------------------------------------------
    print("\n{}".format("=" * 70))
    print("  Summary")
    print("{}".format("=" * 70))

    total_ratio_hits = len(ratio_hits)
    total_diff_hits = len(diff_hits)
    total_h6_hits = len(h6_hits)
    exact_ratio = sum(1 for _, _, (_, g, _) in ratio_hits if g == "EXACT")
    exact_diff = sum(1 for _, _, (_, g, _) in diff_hits if g == "EXACT")
    phase5_exact = sum(1 for lbl, val in predictions
                       if any(abs(val - mv)/abs(mv) <= EXACT_TOL
                              for mv in match_targets.values() if abs(mv) > 1e-15))
    phase5_close = sum(1 for lbl, val in predictions
                       if any(EXACT_TOL < abs(val - mv)/abs(mv) <= CLOSE_TOL
                              for mv in match_targets.values() if abs(mv) > 1e-15))

    print("  H(sigma(6)) = H(12) = {:.6f}".format(h_sigma))
    print("  H(6)        = {:.6f}  (49/20)".format(h_values[6]))
    print()
    print("  Phase 2 -- Ratio/difference scan:")
    print("    Ratio hits:      {} (EXACT: {})".format(total_ratio_hits, exact_ratio))
    print("    Difference hits: {} (EXACT: {})".format(total_diff_hits, exact_diff))
    print("    H(6) matches:    {}".format(total_h6_hits))
    print()
    print("  Phase 3 -- Egyptian fractions:")
    print("    Decomposition terms: {}".format(len(ef_denominators)))
    print("    6-divisible denoms:  {}".format(len(div6_denoms)))
    print()
    print("  Phase 4 -- Cross-domain clustering:")
    print("    Domains at H(12):    {} / {} (within 5%)".format(
        sum(1 for v in h_vals_list if abs(v - h_sigma) / h_sigma <= CLOSE_TOL),
        len(DOMAINS)))
    print("    MC avg cluster:      {:.2f}".format(avg_cluster))
    print()
    print("  Phase 5 -- Constant relationships:")
    print("    EXACT matches:       {}".format(phase5_exact))
    print("    CLOSE matches:       {}".format(phase5_close))

    # Verdict
    total_exact = exact_ratio + exact_diff + phase5_exact
    total_close = total_ratio_hits + total_diff_hits + phase5_close - exact_ratio - exact_diff
    if total_exact >= 3:
        verdict = "STRONG -- H(sigma) = {:.4f} is a universal n=6 constant".format(h_sigma)
    elif total_exact >= 1 or total_close >= 3:
        verdict = "MODERATE -- H(sigma) shows significant n=6 linkage"
    else:
        verdict = "WEAK -- limited evidence for H(sigma) universality"
    print("\n  n=6 verdict: {}".format(verdict))
    print()


if __name__ == "__main__":
    main()
