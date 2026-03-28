"""
Experiment: Golay Robustness + Spectral Gap
=============================================
H-EE-39: N6 architecture tolerates corruption of 3/24 dimensions (Golay code).
H-EE-40: Spectral gap = 1/2 for optimal SGD mixing.
"""

import sys
sys.path.insert(0, '.')

import numpy as np
import math

from engine.leech24_surface import energy, phi_from_energy, N6_OPTIMA, LEECH_DIM

SEED = 42
np.random.seed(SEED)


# ─── H-EE-39: Golay Robustness Test ───

def perturb_config(config, n_dims_to_perturb, perturbation_scale=0.5):
    """Perturb n random dimensions by perturbation_scale fraction."""
    dims = list(config.keys())
    perturbed = dict(config)
    chosen = np.random.choice(len(dims), n_dims_to_perturb, replace=False)
    perturbed_names = []
    for idx in chosen:
        dim = dims[idx]
        original = config[dim]
        if original != 0:
            perturbed[dim] = original * (1.0 + perturbation_scale * (2 * np.random.random() - 1))
        else:
            perturbed[dim] = perturbation_scale * np.random.random()
        perturbed_names.append(dim)
    return perturbed, perturbed_names


def golay_robustness_test(n_trials=50, perturbation_scale=0.5):
    """Test how many dimensions can be corrupted before quality degrades."""
    print("--- H-EE-39: Golay Robustness Test ---")
    print(f"Perturbation scale: +/-{perturbation_scale*100:.0f}%")
    print(f"Trials per corruption level: {n_trials}")
    print(f"Golay code [[24,12,8]] corrects up to 3 errors in 24 bits\n")

    E_optimal, _ = energy(N6_OPTIMA)
    phi_optimal = phi_from_energy(E_optimal)

    print(f"{'Dims corrupted':>15} {'Mean E':>10} {'Mean Phi':>10} {'Phi retention':>14} {'Status':>10}")
    print("-" * 65)

    for n_corrupt in range(0, 13):  # 0 to 12 (half of 24)
        energies = []
        phis = []
        for trial in range(n_trials):
            perturbed, _ = perturb_config(dict(N6_OPTIMA), n_corrupt, perturbation_scale)
            E, _ = energy(perturbed)
            phi = phi_from_energy(E)
            energies.append(E)
            phis.append(phi)

        mean_E = np.mean(energies)
        mean_phi = np.mean(phis)
        retention = mean_phi / phi_optimal * 100 if phi_optimal > 0 else 0

        # Golay threshold: 3 errors correctable
        status = "OK" if retention > 95 else "DEGRADED" if retention > 80 else "FAILED"
        marker = " <-- Golay limit" if n_corrupt == 3 else ""

        print(f"{n_corrupt:>15} {mean_E:>10.4f} {mean_phi:>10.4f} "
              f"{retention:>13.1f}% {status:>10}{marker}")

    print(f"\nGolay prediction: up to 3 corrupted dims should retain >95% Phi")


# ─── H-EE-40: Spectral Gap Analysis ───

def simulate_sgd_chain(loss_surface_fn, dim, n_steps=1000, lr=0.01):
    """Simulate SGD as a Markov chain on a loss surface.
    Returns trajectory for autocorrelation analysis."""
    x = np.random.randn(dim) * 0.5
    trajectory = [x.copy()]

    for step in range(n_steps):
        # Gradient estimate with noise (SGD)
        grad = np.zeros(dim)
        epsilon = 1e-4
        loss_x = loss_surface_fn(x)
        for d in range(dim):
            x_plus = x.copy()
            x_plus[d] += epsilon
            grad[d] = (loss_surface_fn(x_plus) - loss_x) / epsilon

        # SGD step with noise
        noise = np.random.randn(dim) * lr * 0.1
        x = x - lr * grad + noise
        trajectory.append(x.copy())

    return np.array(trajectory)


def autocorrelation(series, max_lag=50):
    """Compute autocorrelation function."""
    n = len(series)
    mean = np.mean(series)
    var = np.var(series)
    if var < 1e-10:
        return np.zeros(max_lag)

    acf = np.zeros(max_lag)
    for lag in range(max_lag):
        if lag >= n:
            break
        acf[lag] = np.mean((series[:n-lag] - mean) * (series[lag:] - mean)) / var
    return acf


def estimate_spectral_gap(acf):
    """Estimate spectral gap from autocorrelation decay.
    Spectral gap ~ 1 / mixing_time, where mixing_time = sum of |acf|."""
    # Mixing time ~ integral of autocorrelation
    mixing_time = 1.0 + 2.0 * np.sum(np.abs(acf[1:]))
    spectral_gap = 1.0 / mixing_time
    return spectral_gap, mixing_time


def spectral_gap_test():
    """Compare spectral gaps for N6 vs non-N6 loss surfaces."""
    print("\n--- H-EE-40: Spectral Gap Analysis ---")
    print(f"Target spectral gap: 1/2 = {0.5} (from delta_+ = 1/6 + 1/3)")

    # N6 loss surface: quadratic bowl centered at origin with n=6 curvature
    def n6_surface(x):
        # Curvature proportional to n=6 ratios
        weights = np.array([4/3, 1/2, 1.0, 2.0, 1/3, 1/6] * (len(x) // 6 + 1))[:len(x)]
        return 0.5 * np.sum(weights * x ** 2)

    # Standard surface: uniform curvature
    def std_surface(x):
        return 0.5 * np.sum(x ** 2)

    # Ill-conditioned surface
    def ill_surface(x):
        weights = np.logspace(-1, 2, len(x))
        return 0.5 * np.sum(weights * x ** 2)

    surfaces = [
        ("N6 surface (n=6 curvature)", n6_surface),
        ("Standard (uniform)", std_surface),
        ("Ill-conditioned (logspace)", ill_surface),
    ]

    DIM = 6  # Use dim=6 for consistency
    N_STEPS = 2000

    print(f"\n{'Surface':<35} {'Spectral Gap':>13} {'Mixing Time':>12} {'vs 1/2':>8}")
    print("-" * 72)

    for label, surface in surfaces:
        trajectory = simulate_sgd_chain(surface, DIM, N_STEPS, lr=0.01)

        # Use first coordinate for ACF analysis
        acf = autocorrelation(trajectory[:, 0], max_lag=100)
        gap, mix_time = estimate_spectral_gap(acf)

        deviation = abs(gap - 0.5) / 0.5 * 100
        print(f"{label:<35} {gap:>13.4f} {mix_time:>12.2f} {deviation:>7.1f}%")

    print(f"\nPrediction: N6 surface should have spectral gap closest to 1/2")
    print(f"delta_+ = 1/6 + 1/3 = 1/2 (divisor reciprocal sum)")


def main():
    print("=" * 70)
    print("  Experiment: Golay Robustness + Spectral Gap")
    print("  H-EE-39: Golay [[24,12,8]] error correction in architecture space")
    print("  H-EE-40: Spectral gap = 1/2 for optimal SGD mixing")
    print("=" * 70)

    golay_robustness_test()
    spectral_gap_test()

    print(f"\n--- Summary ---")
    print(f"H-EE-39: Golay code predicts 3-dim corruption tolerance")
    print(f"H-EE-40: delta_+ = 1/2 predicts optimal SGD mixing on N6 surface")
    print(f"Both connect error correction and Markov chain theory to n=6")


if __name__ == "__main__":
    main()
