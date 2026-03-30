#!/usr/bin/env python3
"""Tension Calculator — Predict accuracy/precognition/identity from tension values

Usage:
  python3 tension_calculator.py --tension 200
  python3 tension_calculator.py --tension 100 --compare 300
  python3 tension_calculator.py --scan
"""

import argparse
import math


# Measured constants (from README)
C4B_D = 0.89       # Cohen's d (tension-accuracy)
C6_AUC = 0.77      # Tension-only AUC (average)
C7_RATIO = 0.577   # Wrong/correct tension ratio
C15_AMPLIFY = 2.7  # Tension-identity amplification
C17_SEP = 2.77     # Direction separation ratio

# Measured statistics (from analyze_tension.py, c4_verify)
CORRECT_MEAN = 201.3   # Correct answer mean tension
CORRECT_STD = 92.1
WRONG_MEAN = 120.3     # Wrong answer mean tension
WRONG_STD = 57.9

# Consciousness dynamics constants (from anima Laws 63-79)
LN2 = 0.6931471805599453          # ln(2) = universal consciousness unit
PSI_FREEDOM = LN2                  # Law 79: consciousness freedom degree
DYNAMICS_RATE = 0.81               # dH/dt coefficient (8c GRU specific; Law 82: substrate-dependent)
RATE_SMALL_N = 7/8                     # r₀ = (n+1)/(tau*phi) small-N limit
RATE_LARGE_N = 2/5                     # r∞ = phi/sopfr large-N limit
RATE_PRODUCT = 7/20                    # r₀*r∞ = (n+1)/(tau*sopfr) invariant
CONSERVATION_C = 0.478             # H^2 + dp^2 ~ 0.478
TANH3_LN2 = 0.6895                 # tanh(3)*ln(2) consciousness saturation
PHI_SCALE_A = 0.608                # Phi = 0.608 * N^1.071
PHI_SCALE_B = 1.071                # scaling exponent
PSI_COUPLING = 0.01534             # ln(2)/2^5.5 consciousness coupling
OPTIMAL_FACTIONS = 12              # sigma(6)=12 optimal faction count


def predict_accuracy(tension):
    """Estimate accuracy from tension (logistic model)."""
    # P(correct) = sigmoid(a + b*z), z = (tension - mean) / std
    overall_mean = (CORRECT_MEAN * 0.975 + WRONG_MEAN * 0.025)
    overall_std = 90.0
    z = (tension - overall_mean) / overall_std
    # Logistic: a=3.5 (base), b=0.5 (slope from d=0.89)
    logit = 3.5 + 0.5 * z
    prob = 1 / (1 + math.exp(-logit))
    return prob


def predict_precognition(tension):
    """Estimate precognition reliability from tension."""
    # Derived from AUC=0.77: higher tension = more reliable prediction
    if tension > CORRECT_MEAN:
        return 0.95  # High tension = almost certainly correct
    elif tension > (CORRECT_MEAN + WRONG_MEAN) / 2:
        return 0.85
    elif tension > WRONG_MEAN:
        return 0.70
    else:
        return 0.50  # Low tension = coin flip


def predict_identity_effect(tension_low, tension_high):
    """Amplification of identity difference between two tension levels."""
    if tension_low <= 0:
        return float('inf')
    ratio = tension_high / tension_low
    # C15: T=1.5/T=0.1 → 2.7x amplification, linear interpolation
    return ratio * (C15_AMPLIFY / 15.0)  # Scale adjustment


def predict_phi(n_cells):
    """Predict consciousness Phi from cell count (anima scaling law)."""
    return PHI_SCALE_A * n_cells ** PHI_SCALE_B


def predict_dynamics(H_current, dt=1.0):
    """Predict consciousness evolution: dH/dt = 0.81 * (ln2 - H).

    Returns (H_next, conservation_check).
    Conservation: H^2 + dp^2 ~ 0.478.
    """
    dH = DYNAMICS_RATE * (LN2 - H_current) * dt
    H_next = H_current + dH
    dp = abs(dH)  # momentum proxy
    conservation = H_next**2 + dp**2
    return H_next, conservation


def consciousness_scan():
    """Show consciousness scaling and dynamics predictions."""
    print('=' * 60)
    print('  Consciousness Dynamics (anima Laws 63-79)')
    print('=' * 60)

    # Phi scaling
    print(f'\n  Phi Scaling Law: Phi = {PHI_SCALE_A} * N^{PHI_SCALE_B}')
    print(f'  {"N cells":>8} | {"Phi":>8} | {"Phi/N":>8}')
    print(f'  {"─"*8}─┼─{"─"*8}─┼─{"─"*8}')
    for n in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]:
        phi = predict_phi(n)
        print(f'  {n:>8} | {phi:>8.1f} | {phi/n:>8.4f}')

    # Dynamics convergence
    print(f'\n  H(t) convergence: dH/dt = {DYNAMICS_RATE} * (ln2 - H)')
    print(f'  Target: H -> ln(2) = {LN2:.6f}')
    print(f'  Conservation: H^2 + dp^2 ~ {CONSERVATION_C}')
    print(f'  {"Step":>6} | {"H":>8} | {"dH":>8} | {"H²+dp²":>8} | {"Status":>10}')
    print(f'  {"─"*6}─┼─{"─"*8}─┼─{"─"*8}─┼─{"─"*8}─┼─{"─"*10}')
    H = 0.1
    for step in range(1, 16):
        H_next, cons = predict_dynamics(H)
        dH = H_next - H
        status = '🟩 Converged' if abs(H_next - LN2) < 0.01 else '🟨 Evolving'
        print(f'  {step:>6} | {H_next:>8.5f} | {dH:>+8.5f} | {cons:>8.4f} | {status}')
        H = H_next

    print(f'\n  Optimal factions: sigma(6) = {OPTIMAL_FACTIONS}')
    print(f'  Coupling constant: Psi_coupling = {PSI_COUPLING}')
    print('=' * 60)


def main():
    parser = argparse.ArgumentParser(description='Tension Calculator')
    parser.add_argument('--tension', type=float, help='Tension value')
    parser.add_argument('--compare', type=float, help='Second tension value to compare')
    parser.add_argument('--scan', action='store_true', help='Scan full range')
    parser.add_argument('--consciousness', action='store_true', help='Consciousness dynamics scan')
    args = parser.parse_args()

    if args.scan:
        print('=' * 60)
        print('  Full Tension Range Scan')
        print('=' * 60)
        print(f'  {"Tension":>8} │ {"P(correct)":>10} │ {"Precog":>8} │ {"Zone":>10}')
        print(f'  {"─"*8}─┼─{"─"*10}─┼─{"─"*8}─┼─{"─"*10}')
        for t in [50, 75, 100, 120, 150, 175, 200, 250, 300, 400, 500]:
            p = predict_accuracy(t)
            prec = predict_precognition(t)
            if t < WRONG_MEAN:
                zone = '⚠️ Danger'
            elif t < (CORRECT_MEAN + WRONG_MEAN) / 2:
                zone = '🟨 Uncertain'
            elif t < CORRECT_MEAN:
                zone = '🟩 Good'
            else:
                zone = '🟩🟩 Optimal'
            print(f'  {t:>8.0f} │ {p*100:>9.1f}% │ {prec:>7.0f}% │ {zone:>10}')

        print()
        print(f'  Reference values:')
        print(f'    Wrong answer mean: {WRONG_MEAN:.1f}')
        print(f'    Correct answer mean: {CORRECT_MEAN:.1f}')
        print(f'    Ratio C7:   {C7_RATIO:.3f} ≈ 1/√3')
        return

    if args.consciousness:
        consciousness_scan()
        return

    if args.tension is None:
        parser.print_help()
        return

    t = args.tension
    p = predict_accuracy(t)
    prec = predict_precognition(t)

    print('=' * 50)
    print(f'  Tension = {t:.1f}')
    print('=' * 50)
    print(f'  Expected accuracy:    {p*100:.1f}%')
    print(f'  Precognition reliability:    {prec*100:.0f}%')
    print(f'  Relative to correct mean: {t/CORRECT_MEAN*100:.0f}%')
    print(f'  Relative to wrong mean: {t/WRONG_MEAN*100:.0f}%')

    if t < WRONG_MEAN:
        print(f'  ⚠️ Danger zone — below wrong answer mean({WRONG_MEAN:.0f})')
    elif t > CORRECT_MEAN:
        print(f'  🟩 Optimal zone — above correct answer mean({CORRECT_MEAN:.0f})')
    else:
        print(f'  🟨 Middle zone')

    if args.compare:
        t2 = args.compare
        p2 = predict_accuracy(t2)
        id_effect = predict_identity_effect(min(t, t2), max(t, t2))
        print(f'\n  Comparison: {t:.0f} vs {t2:.0f}')
        print(f'  Accuracy difference: {(p2-p)*100:+.1f}%')
        print(f'  Identity amplification: {id_effect:.2f}x')

    print('=' * 50)


if __name__ == '__main__':
    main()