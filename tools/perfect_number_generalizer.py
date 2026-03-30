#!/usr/bin/env python3
"""Perfect Number Generalizer — Test if formulas holding at n=6 generalize to n=28, 496, 8128

Automates the Strong Law of Small Numbers check: most identities involving
perfect number 6 are coincidences that fail at n=28.

Usage:
  python3 calc/perfect_number_generalizer.py --formula "F(n) == sigma(n) - tau(n)"
  python3 calc/perfect_number_generalizer.py --formula "F(n) == phi(n)**3"
  python3 calc/perfect_number_generalizer.py --formula "sigma(n)/n == 2"
  python3 calc/perfect_number_generalizer.py --batch
  python3 calc/perfect_number_generalizer.py --scan
"""

import argparse
import math
import sys
from fractions import Fraction

# ═══════════════════════════════════════════════════════════════
# Perfect Number Data
# ═══════════════════════════════════════════════════════════════

PERFECT_NUMBERS = [
    {
        'n': 6,
        'sigma': 12,
        'tau': 4,
        'phi': 2,
        'divisors': [1, 2, 3, 6],
        'proper_divisors': [1, 2, 3],
        'prime_factors': [2, 3],
        'mersenne_prime': 3,
        'mersenne_exp': 2,
    },
    {
        'n': 28,
        'sigma': 56,
        'tau': 6,
        'phi': 12,
        'divisors': [1, 2, 4, 7, 14, 28],
        'proper_divisors': [1, 2, 4, 7, 14],
        'prime_factors': [2, 7],
        'mersenne_prime': 7,
        'mersenne_exp': 3,
    },
    {
        'n': 496,
        'sigma': 992,
        'tau': 10,
        'phi': 240,
        'divisors': [1, 2, 4, 8, 16, 31, 62, 124, 248, 496],
        'proper_divisors': [1, 2, 4, 8, 16, 31, 62, 124, 248],
        'prime_factors': [2, 31],
        'mersenne_prime': 31,
        'mersenne_exp': 5,
    },
    {
        'n': 8128,
        'sigma': 16256,
        'tau': 14,
        'phi': 3840,
        'divisors': [1, 2, 4, 8, 16, 32, 64, 127, 254, 508, 1016, 2032, 4064, 8128],
        'proper_divisors': [1, 2, 4, 8, 16, 32, 64, 127, 254, 508, 1016, 2032, 4064],
        'prime_factors': [2, 127],
        'mersenne_prime': 127,
        'mersenne_exp': 7,
    },
]

PN_LABELS = ['P\u2081', 'P\u2082', 'P\u2083', 'P\u2084']

# ═══════════════════════════════════════════════════════════════
# Mathematical Functions
# ═══════════════════════════════════════════════════════════════

_fib_cache = {0: 0, 1: 1}


def _fib(n):
    """Compute Fibonacci number F(n) iteratively with cache."""
    if n < 0:
        raise ValueError(f"Fibonacci not defined for negative n={n}")
    if n in _fib_cache:
        return _fib_cache[n]
    # fill cache up to n
    a, b = 0, 1
    start = 2
    # find highest cached
    for k in sorted(_fib_cache.keys(), reverse=True):
        if k < n:
            a = _fib_cache[k]
            b = _fib_cache.get(k + 1, None)
            if b is not None:
                start = k + 2
                break
            else:
                start = 2
                a, b = 0, 1
                break
    else:
        start = 2
        a, b = 0, 1
    # simple iterative
    if start == 2:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
            _fib_cache[i] = b
        return b
    for i in range(start, n + 1):
        a, b = b, a + b
        _fib_cache[i] = b
    return b


def _lucas(n):
    """Compute Lucas number L(n)."""
    if n == 0:
        return 2
    if n == 1:
        return 1
    a, b = 2, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# Partition function with memoization
_part_cache = {}


def _partition(n):
    """Compute partition number p(n) using bottom-up dynamic programming."""
    if n < 0:
        return 0
    if n in _part_cache:
        return _part_cache[n]
    # Build table bottom-up to avoid recursion depth issues
    max_cached = max((k for k in _part_cache if k <= n), default=-1)
    if max_cached < 1:
        _part_cache[0] = 1
        _part_cache[1] = 1
        max_cached = 1
    for m in range(max_cached + 1, n + 1):
        if m in _part_cache:
            continue
        result = 0
        k = 1
        while True:
            g1 = k * (3 * k - 1) // 2
            g2 = k * (3 * k + 1) // 2
            if g1 > m:
                break
            sign = (-1) ** (k + 1)
            result += sign * _part_cache[m - g1]
            if g2 <= m:
                result += sign * _part_cache[m - g2]
            k += 1
        _part_cache[m] = result
    return _part_cache[n]


def _sigma(n):
    """Sum of divisors of n."""
    if n <= 0:
        return 0
    s = 0
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
    return s


def _tau(n):
    """Number of divisors of n."""
    if n <= 0:
        return 0
    count = 0
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count


def _euler_phi(n):
    """Euler's totient function."""
    if n <= 0:
        return 0
    result = n
    p = 2
    temp = n
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result


# ═══════════════════════════════════════════════════════════════
# Formula Evaluation
# ═══════════════════════════════════════════════════════════════

def build_namespace(pn_data):
    """Build evaluation namespace for a given perfect number."""
    n = pn_data['n']
    return {
        # The perfect number itself
        'n': n,
        # Precomputed properties (for efficiency)
        'sigma_n': pn_data['sigma'],
        'tau_n': pn_data['tau'],
        'phi_n': pn_data['phi'],
        # Functions that can take arguments
        'F': _fib,
        'Fib': _fib,
        'Lucas': _lucas,
        'p': _partition,
        'partition': _partition,
        'sigma': lambda x=None: pn_data['sigma'] if x is None else _sigma(x),
        'tau': lambda x=None: pn_data['tau'] if x is None else _tau(x),
        'phi': lambda x=None: pn_data['phi'] if x is None else _euler_phi(x),
        # Math
        'sqrt': math.sqrt,
        'log': math.log,
        'log2': math.log2,
        'ln': math.log,
        'exp': math.exp,
        'floor': math.floor,
        'ceil': math.ceil,
        'abs': abs,
        'factorial': math.factorial,
        # Constants
        'pi': math.pi,
        'e': math.e,
    }


def eval_formula(formula_str, pn_data):
    """Evaluate a formula for a given perfect number.

    Returns (lhs_value, rhs_value, match: bool, error_msg or None).
    For '==' formulas, checks both sides.
    For expression formulas, just evaluates.
    """
    ns = build_namespace(pn_data)

    # Replace sigma(n), tau(n), phi(n) with precomputed values for clarity
    # but the namespace already handles function calls

    if '==' in formula_str:
        parts = formula_str.split('==', 1)
        lhs_str = parts[0].strip()
        rhs_str = parts[1].strip()
        try:
            lhs = eval(lhs_str, {"__builtins__": {}}, ns)
            rhs = eval(rhs_str, {"__builtins__": {}}, ns)
        except Exception as ex:
            return None, None, False, str(ex)

        # Check match: exact for integers, approximate for floats
        if isinstance(lhs, int) and isinstance(rhs, int):
            match = (lhs == rhs)
        else:
            lhs_f = float(lhs)
            rhs_f = float(rhs)
            if rhs_f == 0:
                match = abs(lhs_f) < 1e-10
            else:
                match = abs(lhs_f / rhs_f - 1) < 1e-10
        return lhs, rhs, match, None
    else:
        # Single expression — just evaluate
        try:
            val = eval(formula_str, {"__builtins__": {}}, ns)
            return val, None, True, None
        except Exception as ex:
            return None, None, False, str(ex)


# ═══════════════════════════════════════════════════════════════
# Test Runner
# ═══════════════════════════════════════════════════════════════

def test_formula(formula_str, verbose=True):
    """Test a formula against all 4 perfect numbers.

    Returns dict with results.
    """
    results = []
    pass_count = 0

    for i, pn in enumerate(PERFECT_NUMBERS):
        n = pn['n']
        lhs, rhs, match, err = eval_formula(formula_str, pn)
        results.append({
            'label': PN_LABELS[i],
            'n': n,
            'lhs': lhs,
            'rhs': rhs,
            'match': match,
            'error': err,
        })
        if match and err is None:
            pass_count += 1

    verdict = _verdict(pass_count)

    if verbose:
        _print_results(formula_str, results, pass_count, verdict)

    return {
        'formula': formula_str,
        'results': results,
        'pass_count': pass_count,
        'total': 4,
        'verdict': verdict,
    }


def _verdict(pass_count):
    """Generate verdict string."""
    if pass_count == 4:
        return 'UNIVERSAL'
    elif pass_count == 1:
        return 'P1-ONLY'
    elif pass_count == 0:
        return 'NONE'
    else:
        return f'PARTIAL ({pass_count}/4)'


def _format_number(x):
    """Format a number for display, truncating very large values."""
    if x is None:
        return 'N/A'
    if isinstance(x, int):
        s = str(x)
        if len(s) > 20:
            return f'{s[:6]}...({len(s)} digits)'
        return s
    if isinstance(x, float):
        if abs(x) > 1e15:
            return f'{x:.6e}'
        if x == int(x) and abs(x) < 1e15:
            return str(int(x))
        return f'{x:.6f}'
    return str(x)


def _print_results(formula_str, results, pass_count, verdict):
    """Pretty-print test results."""
    # Clean formula display
    display = formula_str.replace('==', ' = ')
    print(f'\nFormula: {display}')
    print()

    for r in results:
        n = r['n']
        label = r['label']
        if r['error']:
            print(f'  {label} = {n:>5}:  ERROR: {r["error"]}')
            continue

        lhs_s = _format_number(r['lhs'])
        if r['rhs'] is not None:
            rhs_s = _format_number(r['rhs'])
            if r['match']:
                print(f'  {label} = {n:>5}:  {lhs_s} = {rhs_s}  \u2705 MATCH')
            else:
                # compute ratio for context
                try:
                    lf = float(r['lhs'])
                    rf = float(r['rhs'])
                    if rf != 0:
                        ratio = lf / rf
                        print(f'  {label} = {n:>5}:  {lhs_s} vs {rhs_s}  \u274c FAIL (ratio: {ratio:.1f})')
                    else:
                        print(f'  {label} = {n:>5}:  {lhs_s} vs {rhs_s}  \u274c FAIL')
                except (OverflowError, ValueError):
                    print(f'  {label} = {n:>5}:  {lhs_s} vs {rhs_s}  \u274c FAIL')
        else:
            print(f'  {label} = {n:>5}:  {lhs_s}')

    print()
    if pass_count == 4:
        print(f'Verdict: UNIVERSAL (4/4 perfect numbers) \u2705')
        print('This property holds for all tested perfect numbers.')
    elif pass_count == 1:
        print(f'Verdict: P\u2081-ONLY (1/4 perfect numbers)')
        print('\u26a0\ufe0f  Strong Law of Small Numbers: works only for smallest perfect number.')
    elif pass_count == 0:
        print(f'Verdict: NONE (0/4 perfect numbers)')
        print('Formula does not hold for any perfect number.')
    else:
        matched = [r['label'] for r in results if r['match'] and r['error'] is None]
        print(f'Verdict: PARTIAL ({pass_count}/4 perfect numbers: {", ".join(matched)})')
    print()


# ═══════════════════════════════════════════════════════════════
# Built-in Formula Batch
# ═══════════════════════════════════════════════════════════════

BUILTIN_FORMULAS = [
    ('F(n) == sigma(n) - tau(n)',       'Fibonacci = sigma - tau'),
    ('F(n) == phi(n)**3',               'Fibonacci = phi^3'),
    ('F(sigma(n)) == sigma(n)**2',      'Fibonacci(sigma) = sigma^2'),
    ('Lucas(n) == sigma(n) + n',        'Lucas = sigma + n'),
    ('p(n) == sigma(n) - 1',            'Partition = sigma - 1'),
    ('sigma(n)*phi(n) == n*tau(n)',      'sigma*phi = n*tau (never universal)'),
    ('sigma(n)/n == 2',                 'sigma/n = 2 (defining property)'),
    ('n == sigma(n)/2',                 'n = sigma/2 (defining property)'),
    ('log2(64) == n',                   'log2(64) = n (trivially P1-only)'),
    ('F(n)/n == 4/3',                   'Fibonacci/n = 4/3'),
]


def run_batch():
    """Test all built-in formulas."""
    print('=' * 70)
    print('  Perfect Number Generalizer — Batch Test')
    print('  Testing all built-in formulas against P1..P4')
    print('=' * 70)

    summary = []
    for formula, description in BUILTIN_FORMULAS:
        print(f'\n--- {description} ---')
        result = test_formula(formula, verbose=True)
        summary.append((description, result['pass_count'], result['verdict']))

    # Summary table
    print('\n' + '=' * 70)
    print('  SUMMARY')
    print('=' * 70)
    print(f'  {"Formula":<45} {"Pass":>6}  {"Verdict":<20}')
    print(f'  {"-"*45} {"-"*6}  {"-"*20}')
    for desc, count, verdict in summary:
        icon = '\u2705' if count == 4 else '\u26a0\ufe0f ' if count == 1 else '\u2753'
        print(f'  {desc:<45} {count:>4}/4  {verdict:<20} {icon}')
    print()

    universal = sum(1 for _, c, _ in summary if c == 4)
    p1_only = sum(1 for _, c, _ in summary if c == 1)
    print(f'  Universal: {universal}/{len(summary)}')
    print(f'  P1-only:   {p1_only}/{len(summary)}')
    print(f'  Partial/None: {len(summary) - universal - p1_only}/{len(summary)}')
    print()


# ═══════════════════════════════════════════════════════════════
# Auto-scan Mode
# ═══════════════════════════════════════════════════════════════

def run_scan():
    """Auto-discover formulas that hold at P1=6 and test them at P2+.

    Generates candidate formulas from combinations of n=6 functions
    and checks which ones accidentally match, then tests generalization.
    """
    print('=' * 70)
    print('  Perfect Number Generalizer — Auto-Scan')
    print('  Discovering formulas that hold at P1=6, testing at P2+')
    print('=' * 70)

    pn1 = PERFECT_NUMBERS[0]  # n=6

    # Compute all relevant values at n=6
    vals = {
        'n': 6,
        'sigma(n)': pn1['sigma'],       # 12
        'tau(n)': pn1['tau'],            # 4
        'phi(n)': pn1['phi'],            # 2
        'F(n)': _fib(6),                 # 8
        'F(sigma(n))': _fib(12),         # 144
        'Lucas(n)': _lucas(6),           # 18
        'p(n)': _partition(6),           # 11
        'p(sigma(n))': _partition(12),   # 77
        'sigma(n)**2': pn1['sigma']**2,  # 144
        'phi(n)**2': pn1['phi']**2,      # 4
        'phi(n)**3': pn1['phi']**3,      # 8
        'tau(n)**2': pn1['tau']**2,      # 16
        'n**2': 36,
        'n**3': 216,
        'sigma(n)*phi(n)': pn1['sigma'] * pn1['phi'],  # 24
        'n*tau(n)': 6 * pn1['tau'],      # 24
        'sigma(n)+n': pn1['sigma'] + 6,  # 18
        'sigma(n)-n': pn1['sigma'] - 6,  # 6
        'sigma(n)-tau(n)': pn1['sigma'] - pn1['tau'],  # 8
        'sigma(n)+tau(n)': pn1['sigma'] + pn1['tau'],  # 16
        'sigma(n)-1': pn1['sigma'] - 1,  # 11
        'sigma(n)/n': Fraction(pn1['sigma'], 6),  # 2
        '2*n': 12,
        '3*n': 18,
        'n+2': 8,
        'n-2': 4,
        'n/2': 3,
        'n/3': 2,
    }

    # Find matching pairs at n=6
    keys = list(vals.keys())
    matches_found = []
    seen = set()

    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            k1, k2 = keys[i], keys[j]
            v1, v2 = vals[k1], vals[k2]
            try:
                if isinstance(v1, Fraction) or isinstance(v2, Fraction):
                    eq = (Fraction(v1) == Fraction(v2))
                elif isinstance(v1, float) or isinstance(v2, float):
                    eq = abs(float(v1) - float(v2)) < 1e-10
                else:
                    eq = (v1 == v2)
            except (ValueError, TypeError, ZeroDivisionError):
                continue

            if eq:
                pair = tuple(sorted([k1, k2]))
                if pair not in seen:
                    seen.add(pair)
                    matches_found.append((k1, k2, v1))

    print(f'\nFound {len(matches_found)} matching pairs at n=6:\n')

    universal_formulas = []
    p1_only_formulas = []
    partial_formulas = []

    for k1, k2, val_at_6 in matches_found:
        formula = f'{k1} == {k2}'
        print(f'  Testing: {k1} = {k2}  (value at n=6: {val_at_6})')

        pass_count = 0
        details = []
        for idx, pn in enumerate(PERFECT_NUMBERS):
            ns = build_namespace(pn)
            try:
                v1 = eval(k1, {"__builtins__": {}}, ns)
                v2 = eval(k2, {"__builtins__": {}}, ns)
                if isinstance(v1, Fraction) or isinstance(v2, Fraction):
                    match = (Fraction(v1) == Fraction(v2))
                elif isinstance(v1, float) or isinstance(v2, float):
                    f1, f2 = float(v1), float(v2)
                    match = abs(f1 - f2) < 1e-10 if f2 == 0 else abs(f1/f2 - 1) < 1e-10
                else:
                    match = (v1 == v2)
            except Exception:
                match = False
            if match:
                pass_count += 1
            details.append((PN_LABELS[idx], PERFECT_NUMBERS[idx]['n'], match))

        status_str = ' '.join(
            f'{lab}:\u2705' if m else f'{lab}:\u274c'
            for lab, _, m in details
        )
        verdict = _verdict(pass_count)
        print(f'    {status_str}  -> {verdict}')

        entry = (k1, k2, pass_count, verdict)
        if pass_count == 4:
            universal_formulas.append(entry)
        elif pass_count == 1:
            p1_only_formulas.append(entry)
        else:
            partial_formulas.append(entry)

    # Summary
    print('\n' + '=' * 70)
    print('  SCAN SUMMARY')
    print('=' * 70)

    if universal_formulas:
        print(f'\n  \u2705 UNIVERSAL ({len(universal_formulas)}):')
        for k1, k2, _, _ in universal_formulas:
            print(f'    {k1} = {k2}')

    if partial_formulas:
        print(f'\n  \u2753 PARTIAL ({len(partial_formulas)}):')
        for k1, k2, c, v in partial_formulas:
            print(f'    {k1} = {k2}  ({c}/4)')

    if p1_only_formulas:
        print(f'\n  \u26a0\ufe0f  P\u2081-ONLY ({len(p1_only_formulas)}):')
        for k1, k2, _, _ in p1_only_formulas:
            print(f'    {k1} = {k2}')

    total = len(matches_found)
    if total > 0:
        pct = len(p1_only_formulas) / total * 100
        print(f'\n  P\u2081-only rate: {len(p1_only_formulas)}/{total} ({pct:.0f}%)')
        print(f'  Universal rate: {len(universal_formulas)}/{total} ({100 - pct:.0f}%)')
    print()


# ═══════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description='Test if perfect-number formulas generalize beyond n=6',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  %(prog)s --formula "F(n) == sigma(n) - tau(n)"
  %(prog)s --formula "sigma(n)/n == 2"
  %(prog)s --batch
  %(prog)s --scan
""")
    parser.add_argument('--formula', type=str,
                        help='Formula to test (use == for equality, e.g. "F(n) == phi(n)**3")')
    parser.add_argument('--batch', action='store_true',
                        help='Test all built-in formulas')
    parser.add_argument('--scan', action='store_true',
                        help='Auto-discover formulas holding at P1=6 and test generalization')

    args = parser.parse_args()

    if not any([args.formula, args.batch, args.scan]):
        parser.print_help()
        sys.exit(1)

    if args.formula:
        test_formula(args.formula)

    if args.batch:
        run_batch()

    if args.scan:
        run_scan()


if __name__ == '__main__':
    main()
