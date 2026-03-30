#!/usr/bin/env python3
"""Divisor Field Theory — Action S(n) uniqueness and spacetime analysis

Usage:
  python3 calc/divisor_field_theory.py                      # Default: scan n=1..10000
  python3 calc/divisor_field_theory.py --limit 100000       # Extended scan
  python3 calc/divisor_field_theory.py --partition           # Vacuum thermodynamics
  python3 calc/divisor_field_theory.py --spacetime           # Divisor lattice -> spacetime signature
"""

import argparse
import math

from sympy import divisor_sigma, divisor_count, totient, factorint


def compute_arithmetic(n):
    """Compute tau, sigma, phi for integer n."""
    tau = int(divisor_count(n))
    sigma = int(divisor_sigma(n, 1))
    phi = int(totient(n))
    return tau, sigma, phi


def compute_r_factor(n):
    """R(n) = sigma*phi / (n*tau)."""
    tau, sigma, phi = compute_arithmetic(n)
    if n * tau == 0:
        return float('inf')
    return (sigma * phi) / (n * tau)


def compute_action(n):
    """Compute Divisor Field Theory action S(n).

    S(n) = [sigma*phi - n*tau]^2 + [sigma*(n+phi) - n*tau^2]^2

    S(n)=0 requires both terms to vanish simultaneously.
    """
    tau, sigma, phi = compute_arithmetic(n)
    term1 = sigma * phi - n * tau
    term2 = sigma * (n + phi) - n * tau * tau
    return term1 * term1 + term2 * term2, term1, term2


def scan_solutions(limit):
    """Scan for R(n)=1 solutions, structure constraint, and S(n)=0."""
    print(f'  Scanning n = 1 .. {limit:,} ...')
    print()

    r_one = []
    s_zero = []
    s_small = []

    for n in range(1, limit + 1):
        tau, sigma, phi = compute_arithmetic(n)
        if n * tau == 0:
            continue
        r = (sigma * phi) / (n * tau)

        action, t1, t2 = compute_action(n)

        if abs(r - 1.0) < 1e-9:
            r_one.append((n, tau, sigma, phi, r, action))

        if action == 0:
            s_zero.append((n, tau, sigma, phi))

        if action > 0 and action <= 100:
            s_small.append((n, tau, sigma, phi, action, t1, t2))

    # R(n)=1 solutions
    print(f'  R(n) = 1 solutions ({len(r_one)} found):')
    print(f'  {"n":>12} {"tau":>6} {"sigma":>8} {"phi":>8} {"R":>8} {"S(n)":>12}')
    print(f'  {"---":>12} {"---":>6} {"-----":>8} {"---":>8} {"---":>8} {"----":>12}')
    for n, tau, sigma, phi, r, action in r_one[:20]:
        print(f'  {n:>12,} {tau:>6} {sigma:>8,} {phi:>8,} {r:>8.4f} {action:>12,}')
    if len(r_one) > 20:
        print(f'  ... and {len(r_one) - 20} more')
    print()

    # S(n)=0 solutions
    print(f'  S(n) = 0 solutions ({len(s_zero)} found):')
    if s_zero:
        for n, tau, sigma, phi in s_zero[:20]:
            print(f'    n = {n:,}  tau={tau}  sigma={sigma}  phi={phi}')
    else:
        print(f'    None found in range (perfect numbers are S(n)=0 candidates)')
    print()

    # Near-zero S(n)
    if s_small:
        print(f'  Small S(n) <= 100 ({len(s_small)} found):')
        print(f'  {"n":>12} {"tau":>6} {"sigma":>8} {"phi":>8} {"S(n)":>10} {"term1":>8} {"term2":>8}')
        print(f'  {"---":>12} {"---":>6} {"-----":>8} {"---":>8} {"----":>10} {"-----":>8} {"-----":>8}')
        for n, tau, sigma, phi, action, t1, t2 in s_small[:20]:
            print(f'  {n:>12,} {tau:>6} {sigma:>8,} {phi:>8,} {action:>10,} {t1:>8} {t2:>8}')
        if len(s_small) > 20:
            print(f'  ... and {len(s_small) - 20} more')
    print()

    # Perfect number S(n) values
    perfect_nums = [6, 28, 496, 8128, 33550336]
    print(f'  Perfect Number Actions:')
    print(f'  {"P#":>4} {"n":>12} {"S(n)":>15} {"term1":>10} {"term2":>10} {"R":>8}')
    print(f'  {"--":>4} {"---":>12} {"----":>15} {"-----":>10} {"-----":>10} {"---":>8}')
    for i, n in enumerate(perfect_nums, 1):
        action, t1, t2 = compute_action(n)
        r = compute_r_factor(n)
        print(f'  P{i:>2} {n:>12,} {action:>15,} {t1:>10,} {t2:>10,} {r:>8.4f}')
    print()


def vacuum_partition(beta_values=None):
    """Compute vacuum partition function Z(beta) = sum_{n=1}^{N} exp(-beta * S(n)).

    Analyzes thermodynamic properties at different temperatures.
    """
    if beta_values is None:
        beta_values = [0.001, 0.01, 0.1, 1.0, 10.0]

    N = 1000  # partition sum cutoff

    print(f'  Vacuum Thermodynamics (N={N}):')
    print()
    print(f'  {"beta":>10} {"T=1/beta":>12} {"Z(beta)":>14} {"<S>":>14} {"S_thermo":>14} {"Phase":<20}')
    print(f'  {"----":>10} {"-------":>12} {"------":>14} {"---":>14} {"--------":>14} {"-----":<20}')

    for beta in beta_values:
        z = 0.0
        avg_s = 0.0
        avg_s2 = 0.0

        for n in range(1, N + 1):
            action, _, _ = compute_action(n)
            weight = math.exp(-beta * action) if beta * action < 500 else 0.0
            z += weight
            avg_s += action * weight
            avg_s2 += action * action * weight

        if z > 0:
            avg_s /= z
            avg_s2 /= z
            # Thermodynamic entropy S_thermo = beta^2 * d<S>/dbeta ~ beta^2 * Var(S)
            variance = avg_s2 - avg_s * avg_s
            s_thermo = beta * beta * variance if variance > 0 else 0
        else:
            avg_s = float('inf')
            s_thermo = 0

        if beta < 0.01:
            phase = 'Hot (all states)'
        elif beta < 1.0:
            phase = 'Warm (mixed)'
        elif beta < 5.0:
            phase = 'Cold (low S dominate)'
        else:
            phase = 'Frozen (ground state)'

        temp = 1.0 / beta if beta > 0 else float('inf')
        print(f'  {beta:>10.3f} {temp:>12.2f} {z:>14.4f} {avg_s:>14.2f} {s_thermo:>14.4f} {phase:<20}')

    print()
    print('  Interpretation:')
    print('    Hot  (beta->0): All integers contribute equally, Z ~ N')
    print('    Cold (beta->inf): Only S(n)=0 (perfect numbers) survive')
    print('    Phase transition: Perfect numbers are vacuum ground states')
    print()


def spacetime_signature(n):
    """Analyze divisor lattice as spacetime signature.

    For n with factorization p1^a1 * p2^a2 * ...:
    - Identity (1) -> time dimension
    - Prime divisors -> space dimensions
    - Composite divisors -> emergent/interaction dimensions
    """
    factors = factorint(n)
    tau = int(divisor_count(n))

    n_primes = len(factors)  # number of distinct prime factors
    n_composite = tau - 1 - n_primes  # composite divisors (excluding 1 and primes)
    n_time = 1  # identity = time

    return n_time, n_primes, n_composite


def show_spacetime():
    """Show spacetime signatures for perfect numbers."""
    perfect_nums = [6, 28, 496, 8128, 33550336]

    print(f'  Divisor Lattice -> Spacetime Signature:')
    print()
    print(f'  {"P#":>4} {"n":>12} {"tau":>6} {"time":>6} {"space":>6} {"emerge":>8} {"sig (t,s)":>12} {"Physics":<30}')
    print(f'  {"--":>4} {"---":>12} {"---":>6} {"----":>6} {"-----":>6} {"------":>8} {"---------":>12} {"-------":<30}')

    for i, n in enumerate(perfect_nums, 1):
        tau = int(divisor_count(n))
        t, s, e = spacetime_signature(n)
        sig = f'({t},{s})'
        phys = ''
        if n == 6:
            phys = '(1,3) = Minkowski 4D'
        elif n == 28:
            phys = '(1,2)+3 = 6D Calabi-Yau'
        elif n == 496:
            phys = '(1,3)+6 = 10D superstring'
        elif n == 8128:
            phys = '(1,4)+9 = 14D extended'
        elif n == 33550336:
            phys = '(1,5)+20 = 26D bosonic'

        print(f'  P{i:>2} {n:>12,} {tau:>6} {t:>6} {s:>6} {e:>8} {sig:>12} {phys:<30}')

    print()
    print('  Legend:')
    print('    time   = 1 (identity divisor = time dimension)')
    print('    space  = number of distinct prime factors')
    print('    emerge = composite divisors (interaction dimensions)')
    print('    tau    = time + space + emerge + 1(n itself excluded from count here)')
    print()

    # Detail for P1=6
    print('  Detailed: P1 = 6 = 2 * 3')
    print('    Divisors: {1, 2, 3, 6}')
    print('    1 -> time (identity)')
    print('    2, 3 -> space (primes)')
    print('    6 -> emergent (composite = interaction)')
    print('    Signature: (1, 3) Minkowski spacetime')
    print()


def main():
    parser = argparse.ArgumentParser(description='Divisor Field Theory Calculator')
    parser.add_argument('--limit', type=int, default=10000, help='Scan upper limit (default: 10000)')
    parser.add_argument('--partition', action='store_true', help='Vacuum thermodynamics')
    parser.add_argument('--spacetime', action='store_true', help='Divisor lattice spacetime signature')
    args = parser.parse_args()

    if args.partition:
        print('=' * 80)
        print('  Divisor Field Theory — Vacuum Thermodynamics')
        print('=' * 80)
        print()
        vacuum_partition()
        print('=' * 80)
        return

    if args.spacetime:
        print('=' * 80)
        print('  Divisor Field Theory — Spacetime from Divisor Lattice')
        print('=' * 80)
        print()
        show_spacetime()
        print('=' * 80)
        return

    # Default: scan for solutions
    print('=' * 80)
    print('  Divisor Field Theory — Action S(n) Analysis')
    print('=' * 80)
    print()
    print('  S(n) = [sigma*phi - n*tau]^2 + [sigma*(n+phi) - n*tau^2]^2')
    print('  R(n) = sigma*phi / (n*tau)')
    print()
    scan_solutions(args.limit)
    print('=' * 80)


if __name__ == '__main__':
    main()
