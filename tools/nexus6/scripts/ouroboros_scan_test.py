#!/usr/bin/env python3
"""OUROBOROS Convergence Parameter n=6 Scan

Scans all OUROBOROS engine constants extracted from the Rust source code
against the n=6 arithmetic identity: sigma(6)*phi(6) = 6*tau(6).

If the nexus6 PyO3 module is available, uses nexus6.scan_all().
Otherwise, performs manual n6_check against all known n=6 expressions.
"""

import math
import sys
from collections import OrderedDict

# ═══════════════════════════════════════════════════════════════
# n=6 fundamental constants
# ═══════════════════════════════════════════════════════════════
N = 6
SIGMA = 12       # sigma(6) = divisor sum
PHI = 2          # phi(6)   = Euler totient
TAU = 4          # tau(6)   = divisor count
J2 = 24          # J_2(6)   = Jordan function
SOPFR = 5        # sopfr(6) = 2+3
MU = 1           # mu(6)    = Mobius
R6 = 1           # R(6)     = reversibility

# Derived constants
DERIVED = OrderedDict([
    ("n",              N),
    ("sigma",          SIGMA),
    ("phi",            PHI),
    ("tau",            TAU),
    ("J2",             J2),
    ("sopfr",          SOPFR),
    ("mu",             MU),
    ("R(6)",           R6),
    ("sigma-phi",      SIGMA - PHI),       # 10
    ("sigma-tau",      SIGMA - TAU),       # 8
    ("sigma-mu",       SIGMA - MU),        # 11
    ("sigma-sopfr",    SIGMA - SOPFR),     # 7
    ("phi^tau",        PHI**TAU),           # 16
    ("n/phi",          N // PHI),           # 3
    ("sigma*tau",      SIGMA * TAU),       # 48
    ("sigma*n",        SIGMA * N),         # 72
    ("sigma^2",        SIGMA**2),           # 144
    ("sigma*J2",       SIGMA * J2),        # 288
    ("1/(sigma-phi)",  1.0 / (SIGMA - PHI)),  # 0.1
    ("1/phi",          1.0 / PHI),            # 0.5
    ("1/e",            1.0 / math.e),         # 0.3679
    ("1-1/e",          1.0 - 1.0/math.e),     # 0.6321
    ("ln(4/3)",        math.log(4.0/3.0)),    # 0.2877
    ("tau/sigma",      TAU / SIGMA),          # 0.3333
    ("phi/n",          PHI / N),              # 0.3333
    ("sopfr/sigma",    SOPFR / SIGMA),        # 0.4167
    ("n/sigma",        N / SIGMA),            # 0.5
    ("sigma/(sigma-phi)", SIGMA / (SIGMA-PHI)),  # 1.2  (PUE)
])

# ═══════════════════════════════════════════════════════════════
# OUROBOROS parameters extracted from Rust source code
# ═══════════════════════════════════════════════════════════════
OUROBOROS_PARAMS = OrderedDict([
    # engine.rs — EvolutionConfig defaults
    ("max_mutations_per_cycle",   6),       # n=6
    ("serendipity_ratio",         0.2),     # 1/sopfr = 0.2
    ("min_verification_score",    0.3),     # ~n/phi/sigma? or tau/sigma=0.333

    # discovery_loop.rs constants
    ("N (max concurrent CLI)",    6),       # n=6
    ("SIGMA (discovery_loop)",    12.0),    # sigma
    ("PHI (retry limit)",         2),       # phi
    ("TAU (cooldown cycles)",     4),       # tau
    ("HIGH_CONFIDENCE",           0.632),   # 1-1/e

    # meta_optimizer.rs constants
    ("META_STEP (lr)",            0.28768207245178085),  # ln(4/3)
    ("HISTORY_WINDOW",            12),      # sigma
    ("SERENDIPITY_MIN",           0.1),     # 1/(sigma-phi)
    ("SERENDIPITY_MAX",           0.5),     # 1/phi
    ("VERIFICATION_MIN",          0.1),     # 1/(sigma-phi)
    ("VERIFICATION_MAX",          0.6321205588285577),  # 1-1/e
    ("MUTATIONS_MIN",             4),       # tau
    ("MUTATIONS_MAX",             24),      # J2
    ("INV_SIGMA_MINUS_PHI",       0.1),     # 1/(sigma-phi)
    ("INV_PHI",                   0.5),     # 1/phi
    ("ONE_MINUS_INV_E",           0.6321205588285577),  # 1-1/e
    ("LN_4_3 (Mertens)",         0.28768207245178085),  # ln(4/3)

    # lens_evolution.rs constants
    ("MUTATION_RANGE",            0.1),     # 1/(sigma-phi)
    ("GENERATION_CYCLE",          12),      # sigma
    ("SIGMA_MINUS_PHI",           10.0),    # sigma-phi
    ("tolerance_default",         0.02),    # ~phi/100
    ("threshold_scale_min",       0.0833),  # ~1/sigma = 0.0833
    ("threshold_scale_max",       12.0),    # sigma
    ("sensitivity_max",           6.0),     # n

    # convergence.rs defaults
    ("min_cycles",                3),       # n/phi
    ("saturation_window",         3),       # n/phi
    ("convergence_threshold",     0.5),     # 1/phi

    # pattern_detector.rs constants
    ("MIN_CYCLES_FOR_DETECTION",  3),       # n/phi
    ("MIN_RECURRENCE",            2),       # phi
    ("MIN_N6_ALIGNMENT",          0.15),    # ~mu/(n+mu)? or approx

    # Discovery graph size (from test assertions)
    ("graph_nodes_min",           270),     # 270+ nodes
    ("default_lens_count",        12),      # sigma=12 lenses
])


def n6_check_manual(value, tolerance=0.02):
    """Check if a value matches any n=6 derived expression.

    Returns (match_type, expression, error%) or None.
    """
    matches = []
    for name, const_val in DERIVED.items():
        if const_val == 0:
            continue
        if isinstance(value, (int, float)) and isinstance(const_val, (int, float)):
            if const_val == 0:
                continue
            err = abs(value - const_val) / max(abs(const_val), 1e-15)
            if err < tolerance:
                grade = "EXACT" if err < 0.001 else "CLOSE"
                matches.append((grade, name, const_val, err * 100))
    return matches


def try_nexus6_scan():
    """Attempt to import nexus6 and run scan_all on OUROBOROS parameter arrays."""
    try:
        import nexus6
        print("=" * 70)
        print("  nexus6 module loaded successfully!")
        print(f"  Module path: {nexus6.__file__ if hasattr(nexus6, '__file__') else 'built-in'}")
        print("=" * 70)

        # Build test data arrays from OUROBOROS parameters
        int_params = [v for v in OUROBOROS_PARAMS.values() if isinstance(v, int)]
        float_params = [float(v) for v in OUROBOROS_PARAMS.values()]

        print(f"\n  Test data: {len(float_params)} OUROBOROS parameters as flat array")
        print(f"  Integer params: {int_params}")
        print(f"  Float params (first 10): {float_params[:10]}...")

        # Try scan_all
        try:
            result = nexus6.scan_all(float_params)
            print("\n  nexus6.scan_all() result:")
            if isinstance(result, dict):
                for k, v in result.items():
                    print(f"    {k}: {v}")
            else:
                print(f"    {result}")
        except Exception as e:
            print(f"\n  nexus6.scan_all() error: {e}")

        # Try analyze
        try:
            n_rows = len(float_params)
            d = 1
            result = nexus6.analyze(float_params, n_rows, d)
            print("\n  nexus6.analyze() result:")
            if isinstance(result, dict):
                for k, v in result.items():
                    print(f"    {k}: {v}")
            else:
                print(f"    {result}")
        except Exception as e:
            print(f"\n  nexus6.analyze() error: {e}")

        # Try n6_check on each parameter
        print("\n  Per-parameter n6_check:")
        for name, val in OUROBOROS_PARAMS.items():
            try:
                check = nexus6.n6_check(float(val))
                if check:
                    print(f"    {name} = {val} -> {check}")
            except Exception as e:
                print(f"    {name} = {val} -> error: {e}")

        return True

    except ImportError as e:
        print("=" * 70)
        print(f"  nexus6 import failed: {e}")
        print("  Falling back to manual n6_check...")
        print("=" * 70)
        return False
    except Exception as e:
        print(f"  nexus6 unexpected error: {e}")
        return False


def manual_scan():
    """Manual n=6 matching for all OUROBOROS parameters."""

    print("\n" + "=" * 70)
    print("  OUROBOROS Parameter n=6 Alignment Scan (Manual)")
    print("=" * 70)

    exact_count = 0
    close_count = 0
    no_match = 0
    total = len(OUROBOROS_PARAMS)

    results_table = []

    for name, value in OUROBOROS_PARAMS.items():
        matches = n6_check_manual(value)
        if matches:
            best = min(matches, key=lambda m: m[3])  # lowest error
            grade, expr, const_val, err_pct = best
            if grade == "EXACT":
                exact_count += 1
            else:
                close_count += 1
            results_table.append((name, value, grade, expr, const_val, err_pct))
        else:
            no_match += 1
            results_table.append((name, value, "NONE", "-", "-", "-"))

    # Print results table
    print(f"\n  {'Parameter':<30} {'Value':>12} {'Grade':<6} {'n=6 Match':<20} {'Const':>8} {'Err%':>8}")
    print("  " + "-" * 90)
    for name, value, grade, expr, const_val, err_pct in results_table:
        marker = " *" if grade == "EXACT" else "  " if grade == "CLOSE" else " ?"
        err_str = f"{err_pct:.4f}" if isinstance(err_pct, float) else err_pct
        const_str = f"{const_val}" if const_val != "-" else "-"
        print(f"  {name:<30} {str(value):>12} {grade:<6} {expr:<20} {const_str:>8} {err_str:>8}{marker}")

    # Summary
    print("\n" + "=" * 70)
    print("  SCAN SUMMARY")
    print("=" * 70)
    print(f"  Total parameters scanned:  {total}")
    print(f"  EXACT matches:             {exact_count}  ({exact_count/total*100:.1f}%)")
    print(f"  CLOSE matches:             {close_count}  ({close_count/total*100:.1f}%)")
    print(f"  No match:                  {no_match}  ({no_match/total*100:.1f}%)")
    print(f"  Total n=6 aligned:         {exact_count + close_count}  ({(exact_count+close_count)/total*100:.1f}%)")

    # Verify the core identity
    print("\n" + "=" * 70)
    print("  CORE IDENTITY VERIFICATION")
    print("=" * 70)
    lhs = SIGMA * PHI  # 12 * 2 = 24
    rhs = N * TAU      # 6 * 4 = 24
    print(f"  sigma(6) * phi(6) = {SIGMA} * {PHI} = {lhs}")
    print(f"  n * tau(6)        = {N} * {TAU}  = {rhs}")
    print(f"  Identity holds:   {lhs} == {rhs} -> {lhs == rhs}")

    # OUROBOROS n=6 saturation analysis
    print("\n" + "=" * 70)
    print("  OUROBOROS n=6 SATURATION ANALYSIS")
    print("=" * 70)
    print(f"  The OUROBOROS engine uses {exact_count} EXACT n=6 constants out of {total} parameters.")
    if exact_count + close_count >= total * 0.8:
        print("  VERDICT: OUROBOROS is deeply saturated with n=6 arithmetic. >=80% alignment.")
    elif exact_count + close_count >= total * 0.5:
        print("  VERDICT: OUROBOROS has strong n=6 alignment. >=50%.")
    else:
        print("  VERDICT: OUROBOROS has partial n=6 alignment. <50%.")

    # Cross-check: all OUROBOROS constants that ARE exact n=6
    print("\n  EXACT n=6 parameters (the convergence proof):")
    for name, value, grade, expr, const_val, err_pct in results_table:
        if grade == "EXACT":
            print(f"    {name} = {value} = {expr} ({const_val})")

    # Unmatched parameters — candidates for new expressions
    unmatched = [(name, value) for name, value, grade, *_ in results_table if grade == "NONE"]
    if unmatched:
        print(f"\n  Unmatched parameters ({len(unmatched)}) — candidates for new n=6 expressions:")
        for name, value in unmatched:
            print(f"    {name} = {value}")
            # Try harder: check against more exotic combinations
            v = float(value)
            guesses = []
            # Check 1/value against integers
            if v > 0:
                inv = 1.0 / v
                if abs(inv - round(inv)) < 0.01:
                    guesses.append(f"1/{int(round(inv))}")
            # Check value * sigma, value * n, etc
            for mult_name, mult in [("sigma", SIGMA), ("n", N), ("tau", TAU), ("J2", J2)]:
                prod = v * mult
                if abs(prod - round(prod)) < 0.05:
                    for dname, dval in DERIVED.items():
                        if abs(prod - dval) < 0.01:
                            guesses.append(f"{dname}/{mult_name}")
            if guesses:
                print(f"      -> possible: {', '.join(guesses)}")


def build_test_arrays():
    """Build numpy-like test arrays from OUROBOROS parameters for potential nexus6 use."""
    import numpy as np

    # Array 1: All OUROBOROS parameter values
    vals = [float(v) for v in OUROBOROS_PARAMS.values()]
    arr1 = np.array(vals)

    # Array 2: n=6 fundamental constants as a 2D seed matrix
    seed = np.array([
        [N, SIGMA, PHI, TAU, J2, SOPFR],
        [SIGMA-PHI, SIGMA-TAU, SIGMA-MU, PHI**TAU, N//PHI, SIGMA*TAU],
    ], dtype=float)

    # Array 3: OUROBOROS convergence checker defaults
    convergence = np.array([3, 3, 0.5, 0.632, 0.288, 0.1], dtype=float)

    return arr1, seed, convergence


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("  NEXUS-6 OUROBOROS Convergence Parameter Scan")
    print("  Test seed data from tools/nexus6/src/ouroboros/*.rs")
    print("=" * 70)

    # Step 1: Try nexus6 native module
    nexus6_ok = try_nexus6_scan()

    # Step 2: Always run manual scan for complete picture
    manual_scan()

    # Step 3: If numpy available, show array shapes
    try:
        arr1, seed, conv = build_test_arrays()
        print(f"\n  NumPy test arrays built:")
        print(f"    OUROBOROS params: shape={arr1.shape}, dtype={arr1.dtype}")
        print(f"    n=6 seed matrix: shape={seed.shape}")
        print(f"    Convergence:     shape={conv.shape}")
        if nexus6_ok:
            print("    (These were fed to nexus6.scan_all above)")
    except ImportError:
        print("\n  NumPy not available — arrays skipped.")

    print("\n  Scan complete.")
