#!/usr/bin/env python3
"""Egyptian Fraction Calculator — Solutions of 1 = 1/a1 + ... + 1/aK

Searches for Egyptian fraction representations summing to 1,
checks perfect number connections (H-CX-482/489).

Usage:
  python3 calc/egyptian_fraction.py --solve 3 --perfect
  python3 calc/egyptian_fraction.py --divisors 28
  python3 calc/egyptian_fraction.py --kmin 496
  python3 calc/egyptian_fraction.py --verify
"""
import sys, os, argparse, math
from fractions import Fraction
from itertools import combinations
from functools import reduce

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ---------------------------------------------------------------------------
# Utility
# ---------------------------------------------------------------------------

def lcm(a, b):
    return a * b // math.gcd(a, b)


def lcm_list(lst):
    return reduce(lcm, lst)


def is_perfect(n):
    """Check if n is a perfect number (sum of proper divisors = n)."""
    if n < 2:
        return False
    s = 1
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
    return s == n


def proper_divisors(n):
    """Return sorted list of proper divisors of n (including 1, excluding n)."""
    divs = [1]
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
    divs.sort()
    return divs


def all_divisors(n):
    """Return sorted list of all divisors of n (including n)."""
    return proper_divisors(n) + [n]


KNOWN_PERFECTS = [6, 28, 496, 8128, 33550336]


# ---------------------------------------------------------------------------
# Core: solve 1 = 1/a1 + ... + 1/aK  (a1 <= a2 <= ... <= aK)
# ---------------------------------------------------------------------------

def solve_egyptian(K, max_denom=200):
    """Find all solutions of 1 = sum of K unit fractions with denoms <= max_denom.

    Uses recursive backtracking with pruning.
    Returns list of tuples (a1, ..., aK).
    """
    solutions = []

    def backtrack(remaining, k_left, min_a, current):
        """remaining: Fraction left to reach; k_left: slots left; min_a: minimum denom."""
        if k_left == 0:
            if remaining == 0:
                solutions.append(tuple(current))
            return

        # Pruning: remaining must be achievable
        # Best case: all remaining slots use 1/min_a
        if Fraction(k_left, min_a) < remaining:
            return
        # Worst case: remaining > 1/min_a means min_a too small (only if k_left slots)
        # Lower bound for next denom: ceil(1/remaining) but at least min_a
        if remaining <= 0:
            return
        lo = max(min_a, int(math.ceil(remaining.denominator / remaining.numerator)))
        # Upper bound: remaining >= k_left / hi  =>  hi >= k_left / remaining
        # Also hi <= max_denom
        hi = min(max_denom, int(k_left * remaining.denominator / remaining.numerator))

        for a in range(lo, hi + 1):
            f = Fraction(1, a)
            if f > remaining:
                continue
            backtrack(remaining - f, k_left - 1, a, current + [a])

    backtrack(Fraction(1, 1), K, 2, [])
    return solutions


# ---------------------------------------------------------------------------
# Divisor subsets: find subsets of divisors of P with reciprocal sum = 1
# ---------------------------------------------------------------------------

def divisor_subsets_sum1(P):
    """Find all subsets of divisors of P (excluding 1) whose reciprocals sum to 1.

    Excludes divisor 1 since 1/1 = 1 is trivial.
    """
    divs = [d for d in all_divisors(P) if d > 1]
    results = []
    # Check subsets of increasing size
    for size in range(1, len(divs) + 1):
        for combo in combinations(divs, size):
            s = sum(Fraction(1, d) for d in combo)
            if s == 1:
                results.append(tuple(sorted(combo)))
    # Deduplicate
    return sorted(set(results), key=lambda t: (len(t), t))


# ---------------------------------------------------------------------------
# kmin: minimum K where 1 = sum of K unit fractions with each denom | P
# ---------------------------------------------------------------------------

def find_kmin(P):
    """Find minimum number of unit fractions (with denoms dividing P, >1) summing to 1."""
    divs = [d for d in all_divisors(P) if d > 1]
    # BFS by subset size
    for size in range(1, len(divs) + 1):
        for combo in combinations(divs, size):
            s = sum(Fraction(1, d) for d in combo)
            if s == 1:
                return size, tuple(sorted(combo))
    return None, None


# ---------------------------------------------------------------------------
# Verify k_min = 2p - 1 formula for first three perfect numbers
# ---------------------------------------------------------------------------

def verify_kmin_formula():
    """Verify whether k_min(P_n) = 2p_n - 1 for P_n = 2^(p-1)(2^p - 1)."""
    print("=" * 65)
    print("  Verify k_min = 2p - 1 formula for perfect numbers")
    print("=" * 65)
    print()

    # Perfect numbers: P = 2^(p-1) * (2^p - 1) for Mersenne prime 2^p - 1
    perfect_data = [
        (2, 6),
        (3, 28),
        (5, 496),
    ]

    results = []
    for p, P in perfect_data:
        predicted_kmin = 2 * p - 1
        print(f"  P = {P}  (p = {p})")
        print(f"    Predicted k_min = 2*{p} - 1 = {predicted_kmin}")

        kmin, example = find_kmin(P)
        if kmin is not None:
            print(f"    Actual k_min    = {kmin}")
            print(f"    Example subset  = {example}")
            match = (kmin == predicted_kmin)
            print(f"    Match: {'YES' if match else 'NO'}")
            results.append((P, p, predicted_kmin, kmin, match))
        else:
            print(f"    No solution found among divisors of {P}")
            results.append((P, p, predicted_kmin, None, False))
        print()

    # Summary table
    print("-" * 65)
    print(f"  {'P':>8}  {'p':>3}  {'2p-1':>5}  {'k_min':>5}  {'Match':>6}")
    print("-" * 65)
    for P, p, pred, actual, match in results:
        act_str = str(actual) if actual is not None else "N/A"
        print(f"  {P:>8}  {p:>3}  {pred:>5}  {act_str:>5}  {'YES' if match else 'NO':>6}")
    print("-" * 65)

    all_match = all(m for _, _, _, _, m in results)
    print(f"\n  All match: {'YES' if all_match else 'NO'}")
    return all_match


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------

def display_solutions(solutions, show_perfect_only=False):
    """Display solutions with lcm and perfect number marking."""
    K = len(solutions[0]) if solutions else 0
    print(f"\n  Found {len(solutions)} solutions for K = {K}")
    print()

    perfect_count = 0
    displayed = 0

    for sol in solutions:
        L = lcm_list(sol)
        perf = is_perfect(L)
        if perf:
            perfect_count += 1
        if show_perfect_only and not perf:
            continue

        fracs = " + ".join(f"1/{a}" for a in sol)
        mark = " *** PERFECT ***" if perf else ""
        print(f"    1 = {fracs}   lcm = {L}{mark}")
        displayed += 1

    print()
    print(f"  Total solutions: {len(solutions)}")
    print(f"  With perfect lcm: {perfect_count}")
    if show_perfect_only:
        print(f"  (Showing perfect-lcm solutions only)")


def display_divisor_subsets(P, subsets):
    """Display divisor subsets summing to 1."""
    print(f"\n  Divisor subsets of {P} with reciprocal sum = 1")
    print(f"  Divisors of {P}: {all_divisors(P)}")
    print(f"  Found {len(subsets)} subsets")
    print()

    for sub in subsets:
        fracs = " + ".join(f"1/{d}" for d in sub)
        print(f"    K={len(sub):2d}: 1 = {fracs}")

    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Egyptian Fraction Calculator (H-CX-482/489)")
    parser.add_argument("--solve", type=int, metavar="K",
                        help="Find all solutions of 1 = 1/a1 + ... + 1/aK")
    parser.add_argument("--perfect", action="store_true",
                        help="Filter: show only solutions where lcm is perfect")
    parser.add_argument("--divisors", type=int, metavar="P",
                        help="Find all subsets of divisors of P with reciprocal sum = 1")
    parser.add_argument("--kmin", type=int, metavar="P",
                        help="Find minimum K for divisor-reciprocal sum = 1")
    parser.add_argument("--max-denom", type=int, default=200,
                        help="Maximum denominator for --solve (default 200)")
    parser.add_argument("--verify", action="store_true",
                        help="Verify k_min = 2p-1 formula for P1, P2, P3")

    args = parser.parse_args()

    if not any([args.solve, args.divisors, args.kmin, args.verify]):
        parser.print_help()
        return

    if args.solve:
        K = args.solve
        max_d = args.max_denom
        print("=" * 65)
        print(f"  Egyptian Fraction: 1 = sum of {K} unit fractions")
        print(f"  Max denominator: {max_d}")
        print("=" * 65)
        solutions = solve_egyptian(K, max_denom=max_d)
        if solutions:
            display_solutions(solutions, show_perfect_only=args.perfect)
        else:
            print(f"\n  No solutions found for K={K}, max_denom={max_d}")

    if args.divisors is not None:
        P = args.divisors
        print("=" * 65)
        print(f"  Divisor subsets of {P} with reciprocal sum = 1")
        print("=" * 65)
        subsets = divisor_subsets_sum1(P)
        if subsets:
            display_divisor_subsets(P, subsets)
        else:
            print(f"\n  No subsets found for P={P}")

    if args.kmin is not None:
        P = args.kmin
        print("=" * 65)
        print(f"  Minimum K for divisor-reciprocal sum = 1 (P = {P})")
        print("=" * 65)
        kmin, example = find_kmin(P)
        if kmin is not None:
            print(f"\n  k_min({P}) = {kmin}")
            fracs = " + ".join(f"1/{d}" for d in example)
            print(f"  Example: 1 = {fracs}")
        else:
            print(f"\n  No solution found among divisors of {P}")

    if args.verify:
        verify_kmin_formula()


if __name__ == "__main__":
    main()
