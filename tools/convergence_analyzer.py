#!/usr/bin/env python3
"""
Convergence Analyzer -- Depth-1 Reachability Across 8 Mathematical Domains

Based on H-CX-474 convergence engine findings. Answers:
  "Given a target constant, which domains can reach it at depth 1
   using only their own constants?"

Depth 1 = one binary op on two constants from the same domain,
          or one unary op on a single constant.

Usage:
  python3 calc/convergence_analyzer.py --target 1.41421356
  python3 calc/convergence_analyzer.py --target-name sqrt2
  python3 calc/convergence_analyzer.py --all
  python3 calc/convergence_analyzer.py --all --texas
  python3 calc/convergence_analyzer.py --domain Q
  python3 calc/convergence_analyzer.py --domain Q --threshold 0.01
"""

import argparse
import math
import os
import random
import sys
import warnings
from collections import defaultdict
from itertools import combinations

import numpy as np

try:
    import tecsrs
    _HAS_TECSRS = True
except ImportError:
    _HAS_TECSRS = False

warnings.filterwarnings("ignore", category=RuntimeWarning)

# Import DOMAINS from convergence_engine.py
_engine_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _engine_dir)
from convergence_engine import DOMAINS

# ═════════════════════════════════════════════════════════════════
# STANDARD TARGETS
# ═════════════════════════════════════════════════════════════════

STANDARD_TARGETS = {
    "sqrt(2)":      np.sqrt(2),
    "sqrt(3)":      np.sqrt(3),
    "sqrt(5)":      np.sqrt(5),
    "e":            np.e,
    "pi":           np.pi,
    "phi":          (1 + np.sqrt(5)) / 2,
    "gamma_EM":     0.5772156649015329,
    "zeta(3)":      1.2020569031595942,
    "ln(2)":        np.log(2),
    "ln(3)":        np.log(3),
    "ln(4/3)":      np.log(4/3),
    "1/e":          1 / np.e,
    "e^2":          np.e ** 2,
    "pi/2":         np.pi / 2,
    "pi/3":         np.pi / 3,
    "pi/4":         np.pi / 4,
    "pi/6":         np.pi / 6,
    "pi^2/6":       np.pi ** 2 / 6,
    "Catalan":      0.9159655941772190,
    "Khinchin":     2.6854520011,
    "Feigenbaum_d": 4.66920160910299,
    # Consciousness constants (from anima Laws 63-79)
    "Psi_steps":    3.0 / np.log(2),       # 4.328 consciousness evolution number
    "Psi_coupling": np.log(2) / 2**5.5,    # 0.01534 consciousness coupling
    "conservation": 0.478,                  # H^2 + dp^2 conservation
    "dynamics":     0.81,                   # dH/dt coefficient
    "tanh3_ln2":    np.tanh(3)*np.log(2),  # 0.6895 consciousness saturation
}

# Alias map for --target-name convenience
TARGET_ALIASES = {
    "sqrt2":       "sqrt(2)",
    "sqrt3":       "sqrt(3)",
    "sqrt5":       "sqrt(5)",
    "euler":       "e",
    "golden":      "phi",
    "golden_ratio": "phi",
    "phi_gold":    "phi",
    "gamma":       "gamma_EM",
    "apery":       "zeta(3)",
    "catalan":     "Catalan",
    "khinchin":    "Khinchin",
    "feigenbaum":  "Feigenbaum_d",
    "ln2":         "ln(2)",
    "ln3":         "ln(3)",
}


# ═════════════════════════════════════════════════════════════════
# DEPTH-1 EXPRESSION GENERATOR
# ═════════════════════════════════════════════════════════════════

def _safe_add(results, val, expr):
    """Append (val, expr) if val is finite and in reasonable range."""
    if isinstance(val, (int, float, np.floating)) and np.isfinite(val) and 1e-15 < abs(val) < 1e12:
        results.append((float(val), expr))


def unary_ops(name, val):
    """Unary operations on a single constant. Returns [(value, expr), ...]"""
    results = []
    _safe_add(results, val, name)  # identity
    if val > 0:
        _safe_add(results, np.log(val), f"ln({name})")
        _safe_add(results, np.sqrt(val), f"sqrt({name})")
    if val != 0:
        _safe_add(results, 1.0 / val, f"1/{name}")
    if abs(val) < 20:
        try:
            _safe_add(results, np.exp(val), f"exp({name})")
        except OverflowError:
            pass
    return results


def binary_ops(na, va, nb, vb):
    """Binary operations on two values. Returns [(value, expr), ...]"""
    results = []

    _safe_add(results, va + vb, f"({na}+{nb})")
    _safe_add(results, va - vb, f"({na}-{nb})")
    _safe_add(results, vb - va, f"({nb}-{na})")
    _safe_add(results, va * vb, f"({na}*{nb})")

    if vb != 0:
        _safe_add(results, va / vb, f"({na}/{nb})")
    if va != 0:
        _safe_add(results, vb / va, f"({nb}/{na})")

    # Powers
    if va > 0 and abs(vb) < 20:
        try:
            _safe_add(results, va ** vb, f"({na}^{nb})")
        except (OverflowError, ValueError):
            pass
    if vb > 0 and abs(va) < 20:
        try:
            _safe_add(results, vb ** va, f"({nb}^{na})")
        except (OverflowError, ValueError):
            pass

    # Logarithms
    if va > 0 and va != 1 and vb > 0:
        try:
            _safe_add(results, np.log(vb) / np.log(va), f"log_{na}({nb})")
        except (ValueError, ZeroDivisionError):
            pass
    if vb > 0 and vb != 1 and va > 0:
        try:
            _safe_add(results, np.log(va) / np.log(vb), f"log_{nb}({na})")
        except (ValueError, ZeroDivisionError):
            pass

    # sqrt(a*b)
    if va * vb > 0:
        _safe_add(results, np.sqrt(va * vb), f"sqrt({na}*{nb})")

    return results


def generate_depth1(domain_id, threshold=0.001):
    """
    Generate all depth-1 reachable values from a domain.
    Returns dict: {value_bucket: [(value, expr, domain_id), ...]}
    where value_bucket = round(value, 8) for grouping.
    """
    domain = DOMAINS[domain_id]
    consts = domain["constants"]
    names = list(consts.keys())
    values = [consts[n] for n in names]

    all_results = []

    # Unary on each constant
    for i, (n, v) in enumerate(zip(names, values)):
        for val, expr in unary_ops(n, v):
            all_results.append((val, expr))

    # Binary on each pair
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            for val, expr in binary_ops(names[i], values[i], names[j], values[j]):
                all_results.append((val, expr))

    return all_results


# ═════════════════════════════════════════════════════════════════
# REACHABILITY CHECK
# ═════════════════════════════════════════════════════════════════

def check_reachability(target_val, threshold=0.001):
    """
    Check which domains can reach target_val at depth 1.
    Returns list of (domain_id, domain_name, best_expr, rel_error).
    """
    results = []
    for did in sorted(DOMAINS.keys()):
        exprs = generate_depth1(did, threshold)
        best_err = float("inf")
        best_expr = None
        for val, expr in exprs:
            if target_val == 0:
                err = abs(val)
            else:
                err = abs(val - target_val) / abs(target_val)
            if err < best_err:
                best_err = err
                best_expr = expr
        if best_err <= threshold:
            results.append((did, DOMAINS[did]["name"], best_expr, best_err))
    return results


def domain_reachable_targets(domain_id, threshold=0.001):
    """
    Show all standard targets reachable from a specific domain at depth 1.
    Returns list of (target_name, target_val, best_expr, rel_error).
    """
    exprs = generate_depth1(domain_id, threshold)
    results = []
    for tname, tval in sorted(STANDARD_TARGETS.items(), key=lambda x: x[1]):
        best_err = float("inf")
        best_expr = None
        for val, expr in exprs:
            if tval == 0:
                err = abs(val)
            else:
                err = abs(val - tval) / abs(tval)
            if err < best_err:
                best_err = err
                best_expr = expr
        if best_err <= threshold:
            results.append((tname, tval, best_expr, best_err))
    return results


# ═════════════════════════════════════════════════════════════════
# TEXAS SHARPSHOOTER TEST
# ═════════════════════════════════════════════════════════════════

def texas_sharpshooter(reach_counts, n_targets, n_domains=8, n_trials=10000, seed=42):
    """
    Monte Carlo test: if each domain produced random values, how often
    would we see the observed total reach count?
    Uses tecsrs Rust acceleration when available.

    reach_counts: list of (target_name, observed_reach_count)
    """
    observed_total = sum(c for _, c in reach_counts)
    target_vals = [v for _, v in sorted(STANDARD_TARGETS.items(), key=lambda x: x[1])]

    if _HAS_TECSRS:
        tolerances = [0.001] * len(target_vals)
        result = tecsrs.texas_sharpshooter(
            real_hits=observed_total,
            targets=target_vals,
            tolerances=tolerances,
            n_constants=sum(len(generate_depth1(did)) for did in DOMAINS),
            n_trials=n_trials,
            seed=seed,
        )
        return {
            "observed": observed_total,
            "null_mean": result.random_mean,
            "null_std": result.random_std,
            "p_value": result.p_value,
            "z_score": result.z_score,
        }

    # Python fallback
    rng = np.random.default_rng(seed)

    domain_sizes = {}
    for did in DOMAINS:
        exprs = generate_depth1(did)
        domain_sizes[did] = len(exprs)

    null_totals = []
    for _ in range(n_trials):
        total = 0
        for did in DOMAINS:
            n_expr = domain_sizes[did]
            rand_vals = rng.uniform(0, 10, size=n_expr)
            for tv in target_vals:
                diffs = np.abs(rand_vals - tv) / max(abs(tv), 1e-15)
                if np.any(diffs < 0.001):
                    total += 1
        null_totals.append(total)

    null_totals = np.array(null_totals)
    p_value = np.mean(null_totals >= observed_total)
    null_mean = np.mean(null_totals)
    null_std = np.std(null_totals)

    return {
        "observed": observed_total,
        "null_mean": null_mean,
        "null_std": null_std,
        "p_value": p_value,
        "z_score": (observed_total - null_mean) / max(null_std, 1e-15),
    }


# ═════════════════════════════════════════════════════════════════
# OUTPUT FORMATTING
# ═════════════════════════════════════════════════════════════════

def print_target_results(target_name, target_val, results, threshold):
    """Print reachability results for a single target."""
    print(f"\n{'='*70}")
    print(f"  Target: {target_name} = {target_val:.10f}")
    print(f"  Threshold: {threshold*100:.2f}%")
    print(f"  Domains reached: {len(results)}/{len(DOMAINS)}")
    print(f"{'='*70}")

    if not results:
        print("  No domain reaches this target at depth 1.")
        return

    print(f"  {'Domain':<4} {'Name':<22} {'Expression':<35} {'RelErr':>10}")
    print(f"  {'-'*4} {'-'*22} {'-'*35} {'-'*10}")
    for did, dname, expr, err in results:
        if err < 1e-12:
            err_str = "EXACT"
        else:
            err_str = f"{err:.2e}"
        print(f"  {did:<4} {dname:<22} {expr:<35} {err_str:>10}")


def print_all_scan(all_results, threshold, do_texas=False):
    """Print full scan table: all targets x all domains."""
    print(f"\n{'='*70}")
    print(f"  DEPTH-1 REACHABILITY SCAN -- {len(STANDARD_TARGETS)} targets x {len(DOMAINS)} domains")
    print(f"  Threshold: {threshold*100:.2f}%")
    print(f"{'='*70}\n")

    domain_ids = sorted(DOMAINS.keys())
    header = f"  {'Target':<14} {'Value':>12}  " + "  ".join(f"{d:>2}" for d in domain_ids) + f"  {'Reach':>5}"
    print(header)
    print(f"  {'-'*14} {'-'*12}  " + "  ".join("--" for _ in domain_ids) + f"  {'-'*5}")

    reach_counts = []
    domain_hit_counts = defaultdict(int)
    sorted_targets = sorted(all_results.keys(), key=lambda t: all_results[t]["value"])

    for tname in sorted_targets:
        info = all_results[tname]
        tval = info["value"]
        hits = info["hits"]  # dict: domain_id -> (expr, err)
        reach = len(hits)
        reach_counts.append((tname, reach))

        markers = []
        for did in domain_ids:
            if did in hits:
                markers.append(" *")
                domain_hit_counts[did] += 1
            else:
                markers.append("  ")

        val_str = f"{tval:>12.6f}" if abs(tval) < 1e6 else f"{tval:>12.4e}"
        print(f"  {tname:<14} {val_str}  " + "  ".join(markers) + f"  {reach:>5}")

    # Summary row
    print(f"  {'-'*14} {'-'*12}  " + "  ".join("--" for _ in domain_ids) + f"  {'-'*5}")
    totals = [domain_hit_counts.get(d, 0) for d in domain_ids]
    print(f"  {'TOTAL':<14} {'':>12}  " + "  ".join(f"{t:>2}" for t in totals) + f"  {sum(t for _, t in reach_counts):>5}")

    # Domain ranking
    print(f"\n  Domain Ranking (by targets reached):")
    print(f"  {'Rank':>4}  {'ID':<4} {'Name':<24} {'Targets':>7} {'Coverage':>8}")
    print(f"  {'-'*4}  {'-'*4} {'-'*24} {'-'*7} {'-'*8}")
    ranked = sorted(domain_hit_counts.items(), key=lambda x: -x[1])
    for rank, (did, count) in enumerate(ranked, 1):
        pct = count / len(STANDARD_TARGETS) * 100
        print(f"  {rank:>4}  {did:<4} {DOMAINS[did]['name']:<24} {count:>7} {pct:>7.1f}%")

    # Non-reaching domains
    for did in domain_ids:
        if did not in domain_hit_counts:
            print(f"     -  {did:<4} {DOMAINS[did]['name']:<24}       0    0.0%")

    # Target difficulty ranking
    print(f"\n  Target Difficulty (hardest to reach):")
    print(f"  {'Target':<14} {'Reach':>5}  Domains")
    print(f"  {'-'*14} {'-'*5}  {'-'*40}")
    for tname, reach in sorted(reach_counts, key=lambda x: x[0]):
        hits = all_results[tname]["hits"]
        dom_list = ", ".join(sorted(hits.keys())) if hits else "(none)"
        print(f"  {tname:<14} {reach:>5}  {dom_list}")

    # Texas Sharpshooter
    if do_texas:
        print(f"\n{'='*70}")
        print(f"  TEXAS SHARPSHOOTER TEST")
        print(f"{'='*70}")
        print(f"  Running {10000} Monte Carlo trials...")
        ts = texas_sharpshooter(reach_counts, len(STANDARD_TARGETS))
        print(f"  Observed total hits:  {ts['observed']}")
        print(f"  Null mean +/- std:    {ts['null_mean']:.1f} +/- {ts['null_std']:.1f}")
        print(f"  Z-score:              {ts['z_score']:.2f}")
        print(f"  p-value:              {ts['p_value']:.6f}")
        if ts['p_value'] < 0.001:
            print(f"  Verdict:              *** HIGHLY SIGNIFICANT (p < 0.001)")
        elif ts['p_value'] < 0.01:
            print(f"  Verdict:              ** SIGNIFICANT (p < 0.01)")
        elif ts['p_value'] < 0.05:
            print(f"  Verdict:              * MARGINALLY SIGNIFICANT (p < 0.05)")
        else:
            print(f"  Verdict:              NOT SIGNIFICANT (p >= 0.05)")


def print_domain_targets(domain_id, results, threshold):
    """Print all targets reachable from a specific domain."""
    dname = DOMAINS[domain_id]["name"]
    n_consts = len(DOMAINS[domain_id]["constants"])
    print(f"\n{'='*70}")
    print(f"  Domain: {domain_id} -- {dname}")
    print(f"  Constants: {n_consts}")
    print(f"  Threshold: {threshold*100:.2f}%")
    print(f"  Targets reached: {len(results)}/{len(STANDARD_TARGETS)}")
    print(f"{'='*70}\n")

    if not results:
        print("  No standard targets reachable at depth 1.")
        return

    print(f"  {'Target':<14} {'Value':>12} {'Expression':<35} {'RelErr':>10}")
    print(f"  {'-'*14} {'-'*12} {'-'*35} {'-'*10}")
    for tname, tval, expr, err in results:
        if err < 1e-12:
            err_str = "EXACT"
        else:
            err_str = f"{err:.2e}"
        val_str = f"{tval:>12.6f}" if abs(tval) < 1e6 else f"{tval:>12.4e}"
        print(f"  {tname:<14} {val_str} {expr:<35} {err_str:>10}")

    # Show constants used
    print(f"\n  Domain constants:")
    for cname, cval in sorted(DOMAINS[domain_id]["constants"].items(), key=lambda x: x[1]):
        print(f"    {cname:<20} = {cval}")


# ═════════════════════════════════════════════════════════════════
# MAIN
# ═════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Depth-1 convergence reachability analyzer across 8 mathematical domains",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 calc/convergence_analyzer.py --target 1.41421356
  python3 calc/convergence_analyzer.py --target-name sqrt2
  python3 calc/convergence_analyzer.py --all
  python3 calc/convergence_analyzer.py --all --texas
  python3 calc/convergence_analyzer.py --domain Q
        """,
    )
    parser.add_argument("--target", type=float, help="Numeric target value to check")
    parser.add_argument("--target-name", type=str, help="Named target (e.g., pi, sqrt2, ln2)")
    parser.add_argument("--all", action="store_true", help="Scan all standard targets")
    parser.add_argument("--domain", type=str, help="Show all targets reachable from a domain (N/A/G/T/C/Q/I/S)")
    parser.add_argument("--threshold", type=float, default=0.001, help="Relative error threshold (default: 0.001 = 0.1%%)")
    parser.add_argument("--texas", action="store_true", help="Run Texas Sharpshooter test on results")

    args = parser.parse_args()

    # Validate at least one mode selected
    if not any([args.target is not None, args.target_name, args.all, args.domain]):
        parser.print_help()
        sys.exit(1)

    print(f"  Convergence Analyzer -- Depth-1 Reachability")
    print(f"  Domains: {len(DOMAINS)} | Targets: {len(STANDARD_TARGETS)} | Threshold: {args.threshold*100:.2f}%")

    # Mode: --target VALUE
    if args.target is not None:
        results = check_reachability(args.target, args.threshold)
        print_target_results(f"(numeric)", args.target, results, args.threshold)

    # Mode: --target-name NAME
    if args.target_name:
        name = args.target_name
        # Resolve alias
        if name in TARGET_ALIASES:
            name = TARGET_ALIASES[name]
        if name not in STANDARD_TARGETS:
            print(f"\n  ERROR: Unknown target name '{args.target_name}'")
            print(f"  Available targets: {', '.join(sorted(STANDARD_TARGETS.keys()))}")
            print(f"  Aliases: {', '.join(sorted(TARGET_ALIASES.keys()))}")
            sys.exit(1)
        tval = STANDARD_TARGETS[name]
        results = check_reachability(tval, args.threshold)
        print_target_results(name, tval, results, args.threshold)

    # Mode: --all
    if args.all:
        all_results = {}
        for tname, tval in STANDARD_TARGETS.items():
            hits = {}
            for did in sorted(DOMAINS.keys()):
                exprs = generate_depth1(did, args.threshold)
                best_err = float("inf")
                best_expr = None
                for val, expr in exprs:
                    if tval == 0:
                        err = abs(val)
                    else:
                        err = abs(val - tval) / abs(tval)
                    if err < best_err:
                        best_err = err
                        best_expr = expr
                if best_err <= args.threshold:
                    hits[did] = (best_expr, best_err)
            all_results[tname] = {"value": tval, "hits": hits}
        print_all_scan(all_results, args.threshold, do_texas=args.texas)

    # Mode: --domain DOMAIN_ID
    if args.domain:
        did = args.domain.upper()
        if did not in DOMAINS:
            print(f"\n  ERROR: Unknown domain '{args.domain}'")
            print(f"  Available: {', '.join(sorted(DOMAINS.keys()))}")
            sys.exit(1)
        results = domain_reachable_targets(did, args.threshold)
        print_domain_targets(did, results, args.threshold)

    print()


if __name__ == "__main__":
    main()
