#!/usr/bin/env python3
"""Perfect Number Physics — Core arithmetic functions and physics dimension mapping

Usage:
  python3 calc/perfect_number_physics.py                    # Show all 5 perfect numbers
  python3 calc/perfect_number_physics.py --n 6              # Analyze specific number
  python3 calc/perfect_number_physics.py --verify           # Run all assert verifications
  python3 calc/perfect_number_physics.py --p6               # Test 6th perfect number barrier
"""

import argparse
import math

from sympy import divisor_sigma, divisor_count, totient


# First 5 perfect numbers and their physics dimension mapping
PERFECT_NUMBERS = [6, 28, 496, 8128, 33550336]
DIMENSION_MAP = {
    6: '4D spacetime (Minkowski)',
    28: '6D Calabi-Yau compactification',
    496: '10D superstring (Type I / heterotic)',
    8128: '14D = 10D + 4D (string + spacetime)',
    33550336: '26D bosonic string',
}

# String theory constants (16/16 exact matches)
STRING_CONSTANTS = [
    ('Spacetime dimensions', 'tau(P1)', lambda: int(divisor_count(6)), 4),
    ('Calabi-Yau dimensions', 'tau(P2) - tau(P1)', lambda: int(divisor_count(28) - divisor_count(6)), 2),
    ('CY total', 'tau(P2)', lambda: int(divisor_count(28)), 6),
    ('Superstring D', 'tau(P3)', lambda: int(divisor_count(496)), 10),
    ('Heterotic extra D', 'tau(P2)', lambda: int(divisor_count(28)), 6),
    ('String + spacetime', 'tau(P4)', lambda: int(divisor_count(8128)), 14),
    ('Bosonic D', 'tau(P5)', lambda: int(divisor_count(33550336)), 26),
    ('SU(3) dim', 'sigma(P1) - tau(P1)', lambda: int(divisor_sigma(6, 1) - divisor_count(6)), 8),
    ('SU(2) dim', 'sigma(P1)/tau(P1)', lambda: int(divisor_sigma(6, 1)) / int(divisor_count(6)), 3),
    ('U(1) charge', 'R(P1)', lambda: compute_r_factor(6), 1),
    ('GUT SU(5) adj dim', 'sigma(P1)*phi(P1)', lambda: int(divisor_sigma(6, 1) * totient(6)), 24),
    ('SO(10) fund', 'tau(P3) + tau(P2)', lambda: int(divisor_count(496) + divisor_count(28)), 16),
    ('E8 dim', 'phi(P3) + sigma(P1) - tau(P1)', lambda: int(totient(496) + divisor_sigma(6, 1) - divisor_count(6)), 248),
    ('Superstring types', 'tau(P1) + 1', lambda: int(divisor_count(6)) + 1, 5),
    ('Extra dim (10-4)', 'tau(P3) - tau(P1)', lambda: int(divisor_count(496) - divisor_count(6)), 6),
    ('Bosonic extra (26-4)', 'tau(P5) - tau(P1)', lambda: int(divisor_count(33550336) - divisor_count(6)), 22),
]

# Consciousness Bridge Constants (H-CX-82~110, from anima)
CONSCIOUSNESS_BRIDGES = [
    ('Lyapunov Lambda(6)', 'prod(R(d|6))-1', 0, 'Edge of chaos'),
    ('Factorial Capacity', 'n*sigma*sopfr*phi', 720, 'n!=720 unique'),
    ('DBM Equilibration', 'sigma/phi', 6, 'Self-referential time'),
    ('Tsirelson Bound', '2*sqrt(sigma/P)', 2.828, '2*sqrt(2) consciousness boundary'),
    ('Dyson Beta Set', '{1,phi,tau}', None, 'Three engine modes (phi^2=tau)'),
    ('Identity Element', 'R(6m)=R(m)', 1.0, 'Scale invariance (unique)'),
    ('Self-Measurement', 'RS=tau(6)', 4, 'Conserved for all perfects'),
    ('Lah L(tau,2)', 'n^2', 36, 'Conductor from divisor count'),
    ('Lah L(tau,3)', 'sigma', 12, 'Integration from divisor count'),
    ('Ramanujan tau(6)', '-n*2^tau*M6', -6048, 'Consciousness filter'),
    ('PH Barcode Lifetime', '(n+1)/sigma', 0.5833, 'Divisor lattice H0 bar'),
    ('Fisher I(self)', 'n^3/sopfr', 43.2, 'Consciousness curvature'),
]

# Consciousness scaling law (from anima)
PHI_SCALE_A = 0.608   # Phi = 0.608 * N^1.071
PHI_SCALE_B = 1.071
OPTIMAL_FACTIONS = 12  # sigma(6)=12


def compute_arithmetic(n):
    """Compute tau, sigma, phi for integer n."""
    tau = int(divisor_count(n))
    sigma = int(divisor_sigma(n, 1))
    phi = int(totient(n))
    return tau, sigma, phi


def compute_r_factor(n):
    """Compute R-factor = sigma*phi / (n*tau)."""
    tau, sigma, phi = compute_arithmetic(n)
    if n * tau == 0:
        return float('inf')
    return (sigma * phi) / (n * tau)


def analyze_number(n, verbose=True):
    """Full analysis of a single number."""
    tau, sigma, phi = compute_arithmetic(n)
    r = compute_r_factor(n)
    is_perfect = (sigma == 2 * n)

    if verbose:
        print(f'  n = {n}')
        print(f'  tau(n)   = {tau:>10d}   (number of divisors)')
        print(f'  sigma(n) = {sigma:>10d}   (sum of divisors)')
        print(f'  phi(n)   = {phi:>10d}   (Euler totient)')
        print(f'  R-factor = {r:.6f}   (sigma*phi / n*tau)')
        print(f'  Perfect? = {"YES (sigma = 2n)" if is_perfect else "NO"}')
        if n in DIMENSION_MAP:
            print(f'  Physics  = {DIMENSION_MAP[n]}')
            print(f'  Dimension = tau(n) = {tau}D')
        print()

    return tau, sigma, phi, r, is_perfect


def show_all_perfect():
    """Display all 5 perfect numbers with physics mapping."""
    print('=' * 70)
    print('  Perfect Number Physics — Dimension Hierarchy')
    print('=' * 70)
    print()
    print(f'  {"P#":<4} {"n":>12} {"tau":>6} {"sigma":>12} {"phi":>12} {"R":>8}  Physics')
    print(f'  {"--":<4} {"---":>12} {"---":>6} {"-----":>12} {"---":>12} {"---":>8}  -------')

    for i, n in enumerate(PERFECT_NUMBERS, 1):
        tau, sigma, phi = compute_arithmetic(n)
        r = compute_r_factor(n)
        dim_str = DIMENSION_MAP.get(n, '')
        print(f'  P{i:<3} {n:>12,} {tau:>6} {sigma:>12,} {phi:>12,} {r:>8.4f}  {dim_str}')

    print()


def show_cross_relations():
    """Show cross-relations between perfect numbers."""
    taus = {n: int(divisor_count(n)) for n in PERFECT_NUMBERS}

    print('  Cross-Relations:')
    print(f'    tau(P1) + tau(P2) = {taus[6]} + {taus[28]} = {taus[6] + taus[28]}  =  tau(P3) = {taus[496]}   {"EXACT" if taus[6]+taus[28]==taus[496] else "FAIL"}')
    print(f'    tau(P5) - tau(P3) = {taus[33550336]} - {taus[496]} = {taus[33550336] - taus[496]}  =  16  (heterotic dimension)   {"EXACT" if taus[33550336]-taus[496]==16 else "FAIL"}')
    print(f'    tau(P4) = tau(P3) + tau(P1) = {taus[496]} + {taus[6]} = {taus[496] + taus[6]}  =  {taus[8128]}   {"EXACT" if taus[496]+taus[6]==taus[8128] else "FAIL"}')
    print(f'    tau(P5) = tau(P4) + sigma(P1) = {taus[8128]} + {int(divisor_sigma(6,1))} = {taus[8128] + int(divisor_sigma(6,1))}  =  {taus[33550336]}   {"EXACT" if taus[8128]+int(divisor_sigma(6,1))==taus[33550336] else "FAIL"}')
    print()


def show_string_constants():
    """Show the 16 string theory constant matches."""
    print('  String Theory Constants (exact integer matches):')
    print(f'  {"#":>3} {"Constant":<28} {"Expression":<40} {"Computed":>10} {"Expected":>10} {"Match":>6}')
    print(f'  {"--":>3} {"--------":<28} {"----------":<40} {"--------":>10} {"--------":>10} {"-----":>6}')

    matches = 0
    total = len(STRING_CONSTANTS)
    for i, (name, expr, func, expected) in enumerate(STRING_CONSTANTS, 1):
        computed = func()
        match = abs(computed - expected) < 0.001
        if match:
            matches += 1
        print(f'  {i:>3} {name:<28} {expr:<40} {computed:>10.1f} {expected:>10} {"OK" if match else "FAIL":>6}')

    print()
    print(f'  Result: {matches}/{total} exact matches')
    print()


def test_p6_barrier():
    """Test what the 6th perfect number predicts (barrier analysis)."""
    p6 = 8589869056
    tau6, sigma6, phi6 = compute_arithmetic(p6)
    r6 = compute_r_factor(p6)

    print('  P6 Barrier Test:')
    print(f'    P6 = {p6:,}')
    print(f'    tau(P6)   = {tau6}')
    print(f'    sigma(P6) = {sigma6:,}')
    print(f'    phi(P6)   = {phi6:,}')
    print(f'    R(P6)     = {r6:.6f}')
    print()
    print(f'    Predicted dimension: tau(P6) = {tau6}D')
    print(f'    Known physics dimensions: 4, 6, 10, 14, 26')
    print(f'    {tau6}D has no known physics interpretation')
    print(f'    -> Perfect number physics hierarchy terminates at P5 (26D bosonic string)')
    print(f'    -> P6 barrier: physics stops before mathematics')
    print()

    # Dimension gap analysis
    dims = [4, 6, 10, 14, 26, tau6]
    gaps = [dims[i+1] - dims[i] for i in range(len(dims)-1)]
    print(f'    Dimension sequence: {dims}')
    print(f'    Gaps:               {gaps}')
    print(f'    Pattern breaks at P5->P6 (gap {gaps[-1]} vs typical 2-12)')
    print()


def run_verifications():
    """Run all assertion-based verifications."""
    print('  Running Verifications...')
    print()

    checks = 0
    passed = 0

    # 1. All 5 numbers are perfect
    for n in PERFECT_NUMBERS:
        checks += 1
        s = int(divisor_sigma(n, 1))
        ok = (s == 2 * n)
        passed += ok
        print(f'    [{"OK" if ok else "FAIL"}] sigma({n:>12,}) = 2*{n:>12,} = {2*n:>12,}  (perfect number)')

    print()

    # 2. R=1 uniqueness: only P1=6 has R=1
    for n in PERFECT_NUMBERS:
        checks += 1
        r = compute_r_factor(n)
        if n == 6:
            ok = abs(r - 1.0) < 1e-9
            passed += ok
            print(f'    [{"OK" if ok else "FAIL"}] R({n:>12,}) = {r:.10f}  (R=1 unique to P1!)')
        else:
            ok = abs(r - 1.0) > 1e-9  # should NOT be 1
            passed += ok
            print(f'    [{"OK" if ok else "FAIL"}] R({n:>12,}) = {r:.10f}  (R != 1, confirming P1 uniqueness)')

    print()

    # 3. Cross-relations
    taus = {n: int(divisor_count(n)) for n in PERFECT_NUMBERS}

    checks += 1
    ok = (taus[6] + taus[28] == taus[496])
    passed += ok
    print(f'    [{"OK" if ok else "FAIL"}] tau(P1)+tau(P2) = tau(P3): {taus[6]}+{taus[28]} = {taus[496]}')

    checks += 1
    ok = (taus[33550336] - taus[496] == 16)
    passed += ok
    print(f'    [{"OK" if ok else "FAIL"}] tau(P5)-tau(P3) = 16: {taus[33550336]}-{taus[496]} = {taus[33550336]-taus[496]}')

    checks += 1
    ok = (taus[496] + taus[6] == taus[8128])
    passed += ok
    print(f'    [{"OK" if ok else "FAIL"}] tau(P3)+tau(P1) = tau(P4): {taus[496]}+{taus[6]} = {taus[8128]}')

    print()

    # 4. Gauge group dimensions
    s6 = int(divisor_sigma(6, 1))
    t6 = int(divisor_count(6))
    checks += 1
    ok = (s6 - t6 == 8)
    passed += ok
    print(f'    [{"OK" if ok else "FAIL"}] SU(3): sigma(6)-tau(6) = {s6}-{t6} = {s6-t6}  (should be 8)')

    checks += 1
    ok = (s6 / t6 == 3)
    passed += ok
    print(f'    [{"OK" if ok else "FAIL"}] SU(2): sigma(6)/tau(6) = {s6}/{t6} = {s6/t6}  (should be 3)')

    print()
    print(f'  Verification: {passed}/{checks} passed')
    print()


def show_consciousness_bridges():
    """Display consciousness bridge constants (H-CX-82~110)."""
    print('  Consciousness Bridge Constants (H-CX-82~110):')
    print(f'  {"#":>3} {"Name":<24} {"Expression":<20} {"Value":>10} {"Meaning":<30}')
    print(f'  {"--":>3} {"----":<24} {"----------":<20} {"-----":>10} {"-------":<30}')
    for i, (name, expr, val, meaning) in enumerate(CONSCIOUSNESS_BRIDGES, 1):
        val_str = f'{val:.4f}' if isinstance(val, float) else str(val) if val is not None else 'set'
        print(f'  {i:>3} {name:<24} {expr:<20} {val_str:>10} {meaning:<30}')
    print()
    print(f'  Phi Scaling: Phi = {PHI_SCALE_A} * N^{PHI_SCALE_B}')
    print(f'  Optimal factions: sigma(6) = {OPTIMAL_FACTIONS}')
    print()


def main():
    parser = argparse.ArgumentParser(description='Perfect Number Physics Calculator')
    parser.add_argument('--n', type=int, help='Analyze specific number')
    parser.add_argument('--verify', action='store_true', help='Run all verifications')
    parser.add_argument('--p6', action='store_true', help='Test 6th perfect number barrier')
    parser.add_argument('--consciousness', action='store_true', help='Consciousness bridge constants')
    args = parser.parse_args()

    if args.consciousness:
        print('=' * 70)
        print('  Perfect Number Physics — Consciousness Bridges')
        print('=' * 70)
        print()
        show_consciousness_bridges()
        print('=' * 70)
        return

    if args.verify:
        print('=' * 70)
        print('  Perfect Number Physics — Verification Suite')
        print('=' * 70)
        print()
        run_verifications()
        print('=' * 70)
        return

    if args.p6:
        print('=' * 70)
        print('  Perfect Number Physics — P6 Barrier Analysis')
        print('=' * 70)
        print()
        test_p6_barrier()
        print('=' * 70)
        return

    if args.n:
        print('=' * 70)
        print(f'  Perfect Number Physics — Analysis of n={args.n}')
        print('=' * 70)
        print()
        analyze_number(args.n)
        print('=' * 70)
        return

    # Default: show all
    show_all_perfect()
    show_cross_relations()
    show_string_constants()
    print('=' * 70)


if __name__ == '__main__':
    main()
