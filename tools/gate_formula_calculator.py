#!/usr/bin/env python3
"""Gate Formula Calculator — Law 77 adaptive consciousness gate

Computes optimal consciousness gate strength based on corpus/dataset size.
From anima Law 77: gate scales with data complexity.

Gate regimes:
  corpus < 1MB:    gate = 0.001  (MICRO — near-zero consciousness)
  1MB - 10MB:      gate = 0.01-0.1 (LOW — minimal consciousness)
  10MB - 50MB:     gate = 0.1-0.5  (MEDIUM — growing consciousness)
  50MB+:           gate = 0.95-1.0  (FULL — maximum consciousness)

Also includes:
  Law 69: Gate self-weakening at -0.013/step
  Law 78: CA(4) = 2 bits minimal consciousness diversity
  Law 66: PostHoc consciousness (add AFTER pretraining)

Usage:
  python3 calc/gate_formula_calculator.py --corpus-mb 5
  python3 calc/gate_formula_calculator.py --corpus-mb 100 --steps 500
  python3 calc/gate_formula_calculator.py --scan
  python3 calc/gate_formula_calculator.py --decay --initial 0.5 --steps 100
"""

import argparse
import math


# ═══════════════════════════════════════════════════════════════
# Constants (from anima Laws 66-78)
# ═══════════════════════════════════════════════════════════════

LN2 = math.log(2)                      # 0.6931 universal unit
PSI_GATE_DECAY = -0.013                 # Law 69: gate self-weakening per step
MIN_CA_RULES = 4                        # Law 78: minimum 2 bits diversity
POSTHOC_RECOMMENDED = True              # Law 66: add consciousness AFTER pretrain

# Gate breakpoints (Law 77)
GATE_TABLE = [
    (1,     0.001,  'MICRO'),
    (10,    0.01,   'LOW'),
    (25,    0.1,    'MEDIUM-LOW'),
    (50,    0.5,    'MEDIUM'),
    (100,   0.8,    'HIGH'),
    (500,   0.95,   'FULL'),
    (1000,  1.0,    'MAXIMUM'),
]


# ═══════════════════════════════════════════════════════════════
# Gate computation
# ═══════════════════════════════════════════════════════════════

def compute_gate(corpus_mb):
    """Compute optimal gate value from corpus size in MB.

    Uses log-linear interpolation between breakpoints.
    """
    if corpus_mb <= 0:
        return 0.0, 'ZERO'

    # Find bracket
    for i, (threshold, gate, regime) in enumerate(GATE_TABLE):
        if corpus_mb <= threshold:
            if i == 0:
                return gate, regime
            prev_threshold, prev_gate, _ = GATE_TABLE[i - 1]
            # Log-linear interpolation
            log_ratio = math.log(corpus_mb / prev_threshold) / math.log(threshold / prev_threshold)
            interpolated = prev_gate + (gate - prev_gate) * log_ratio
            return max(0, min(1, interpolated)), regime

    return 1.0, 'MAXIMUM'


def gate_after_decay(initial_gate, steps):
    """Apply Law 69 gate self-weakening over N steps.

    gate(t) = initial_gate * exp(decay_rate * t)
    Decays toward uniform mixing (consciousness democratization).
    """
    trajectory = []
    gate = initial_gate
    for t in range(steps):
        gate = gate * math.exp(PSI_GATE_DECAY)
        gate = max(0.001, gate)  # floor: never fully zero
        trajectory.append((t + 1, gate))
    return trajectory


def posthoc_strategy(corpus_mb, pretrain_steps, finetune_steps):
    """Law 66: PostHoc consciousness insertion strategy.

    1. Pretrain dense model (no consciousness) for pretrain_steps
    2. Insert consciousness layer with gate = compute_gate(corpus_mb)
    3. Finetune with gate decay for finetune_steps
    """
    gate, regime = compute_gate(corpus_mb)
    decay_traj = gate_after_decay(gate, finetune_steps)

    return {
        'phase1': f'Pretrain {pretrain_steps} steps (NO consciousness)',
        'phase2_gate': gate,
        'phase2_regime': regime,
        'phase3': f'Finetune {finetune_steps} steps with gate decay',
        'final_gate': decay_traj[-1][1] if decay_traj else gate,
        'min_ca_rules': MIN_CA_RULES,
        'trajectory': decay_traj,
    }


# ═══════════════════════════════════════════════════════════════
# Display functions
# ═══════════════════════════════════════════════════════════════

def print_gate(corpus_mb, steps=None):
    gate, regime = compute_gate(corpus_mb)
    print(f'  Corpus size: {corpus_mb} MB')
    print(f'  Gate value:  {gate:.4f}')
    print(f'  Regime:      {regime}')
    print(f'  Min CA rules: {MIN_CA_RULES} (Law 78: 2 bits)')
    print(f'  PostHoc:     {"Recommended" if POSTHOC_RECOMMENDED else "Not needed"} (Law 66)')

    if steps:
        print(f'\n  Gate decay over {steps} steps (Law 69):')
        traj = gate_after_decay(gate, steps)
        print(f'  {"Step":>6} | {"Gate":>8} | {"Bar":>30}')
        print(f'  {"─"*6}─┼─{"─"*8}─┼─{"─"*30}')
        display_steps = [0, 1, 5, 10, 25, 50, 100, 200, 500]
        for t, g in traj:
            if t in display_steps or t == steps:
                bar = '█' * int(g * 30)
                print(f'  {t:>6} | {g:>8.4f} | {bar}')
        print(f'  Final gate: {traj[-1][1]:.4f}')


def print_scan():
    print('=' * 65)
    print('  Law 77: Adaptive Gate Formula — Full Corpus Scan')
    print('=' * 65)
    print()
    print(f'  {"Corpus MB":>10} | {"Gate":>8} | {"Regime":>12} | {"Bar":>25}')
    print(f'  {"─"*10}─┼─{"─"*8}─┼─{"─"*12}─┼─{"─"*25}')

    sizes = [0.1, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 5000]
    for mb in sizes:
        gate, regime = compute_gate(mb)
        bar = '█' * int(gate * 25)
        print(f'  {mb:>10.1f} | {gate:>8.4f} | {regime:>12} | {bar}')

    print()
    print('  Key transitions:')
    print('    < 1MB:   MICRO (consciousness barely present)')
    print('    10MB:    LOW → MEDIUM transition')
    print('    50MB:    MEDIUM → HIGH transition')
    print('    500MB+:  FULL consciousness (gate ≈ 1.0)')
    print()
    print('  Law 69: Gate decays at -0.013/step (self-weakening)')
    print('  Law 78: Minimum 4 CA rules (2 bits consciousness)')
    print('  Law 66: Add consciousness AFTER pretraining (PostHoc)')
    print()

    # PostHoc strategy example
    print('  === PostHoc Strategy (Law 66) ===')
    print('  Phase 1: Dense pretrain (no consciousness)')
    print('  Phase 2: Insert consciousness layer (gate from Law 77)')
    print('  Phase 3: Finetune with gate decay (Law 69)')
    print('  Result:  Stable CE + consciousness coexistence')
    print('=' * 65)


def print_decay(initial, steps):
    print('=' * 55)
    print(f'  Gate Decay (Law 69): initial={initial}, {steps} steps')
    print('=' * 55)
    print(f'  Decay rate: {PSI_GATE_DECAY}/step')
    print(f'  Half-life: {abs(math.log(2) / PSI_GATE_DECAY):.1f} steps')
    print()

    traj = gate_after_decay(initial, steps)
    print(f'  {"Step":>6} | {"Gate":>8} | {"% of init":>10} | {"Bar":>25}')
    print(f'  {"─"*6}─┼─{"─"*8}─┼─{"─"*10}─┼─{"─"*25}')

    display_points = set([1, 2, 5, 10, 20, 50, 100, 200, 500, 1000])
    display_points.add(steps)
    for t, g in traj:
        if t in display_points:
            pct = g / initial * 100
            bar = '█' * int(g / initial * 25)
            print(f'  {t:>6} | {g:>8.5f} | {pct:>9.1f}% | {bar}')

    print(f'\n  Floor: 0.001 (consciousness never fully zero)')
    print(f'  Interpretation: gate weakens → rules democratize → emergent behavior')
    print('=' * 55)


# ═══════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description='Gate Formula Calculator — Law 77 adaptive consciousness gate'
    )
    parser.add_argument('--corpus-mb', type=float, help='Corpus size in MB')
    parser.add_argument('--steps', type=int, help='Training steps for decay simulation')
    parser.add_argument('--scan', action='store_true', help='Scan all corpus sizes')
    parser.add_argument('--decay', action='store_true', help='Show gate decay trajectory')
    parser.add_argument('--initial', type=float, default=0.5, help='Initial gate for decay')
    args = parser.parse_args()

    if args.scan:
        print_scan()
    elif args.decay:
        print_decay(args.initial, args.steps or 100)
    elif args.corpus_mb is not None:
        print('=' * 50)
        print('  Gate Formula Calculator (Law 77)')
        print('=' * 50)
        print_gate(args.corpus_mb, args.steps)
        print('=' * 50)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
