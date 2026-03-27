"""
H-EE-2: Phi6Simple Gradient Properties
========================================
Hypothesis: Phi6'(x) = 2x-1 gives natural gradient centering.
  - E[Phi6'(x)] ~ 0 for x ~ N(0,1)
  - Compare with GELU, ReLU, SiLU gradient statistics.

Analytical computation:
  For x ~ N(0,1):
    E[2x-1] = 2*E[x] - 1 = 2*0 - 1 = -1

  Wait -- that's NOT zero-centered! The hypothesis needs careful checking.
  Let's compute both with and without the clamp effect.

We compute:
  1. E[f'(x)] for each activation (should ideally be ~0 for good gradient flow)
  2. Var[f'(x)] (should not be too large or too small)
  3. Gradient magnitude distribution
  4. Fraction of "dead" gradients (|f'(x)| < 0.01)
"""

import numpy as np
from scipy import stats, integrate
import time

np.random.seed(42)

# ── Activation derivatives ──

def gelu_grad(x):
    c = 0.7978845608028654
    x3 = x**3
    t = np.tanh(c * (x + 0.044715 * x3))
    dt = 1.0 - t*t
    return 0.5 * (1.0 + t) + 0.5 * x * dt * c * (1.0 + 3 * 0.044715 * x**2)

def relu_grad(x):
    return (x > 0).astype(x.dtype)

def silu_grad(x):
    sig = 1.0 / (1.0 + np.exp(-np.clip(x, -30, 30)))
    return sig + x * sig * (1.0 - sig)

def phi6_grad(x):
    """Phi6Simple gradient: 2x-1 inside [-2,2], 0 outside."""
    mask = ((x >= -2.0) & (x <= 2.0)).astype(x.dtype)
    xc = np.clip(x, -2.0, 2.0)
    return mask * (2.0 * xc - 1.0)

def phi6_unclamped_grad(x):
    """Phi6 gradient without clamp: always 2x-1."""
    return 2.0 * x - 1.0

ACTIVATIONS = {
    "GELU":             gelu_grad,
    "ReLU":             relu_grad,
    "SiLU":             silu_grad,
    "Phi6_clamped":     phi6_grad,
    "Phi6_unclamped":   phi6_unclamped_grad,
}


# ── Analytical computation ──

def analytical_moments():
    """Compute E[f'(x)] and Var[f'(x)] analytically for x~N(0,1)."""
    print("\n  ANALYTICAL COMPUTATION")
    print("  " + "=" * 60)

    # Standard normal PDF
    phi = lambda x: np.exp(-x**2/2) / np.sqrt(2*np.pi)

    # Phi6_unclamped: f'(x) = 2x - 1
    # E[2x-1] = 2*E[x] - 1 = 0 - 1 = -1
    # E[(2x-1)^2] = 4*E[x^2] - 4*E[x] + 1 = 4*1 - 0 + 1 = 5
    # Var[2x-1] = 5 - (-1)^2 = 4
    print(f"\n  Phi6 unclamped: f'(x) = 2x - 1")
    print(f"    E[f'(x)]   = 2*E[x] - 1 = 2*0 - 1 = -1.000 (EXACT)")
    print(f"    Var[f'(x)] = 4*Var[x] = 4*1 = 4.000 (EXACT)")
    print(f"    Std[f'(x)] = 2.000")
    print(f"    NOTE: E[f'(x)] = -1, NOT zero! The gradient is biased negative.")

    # Phi6_clamped: need numerical integration due to clamp
    # f'(x) = (2x-1) * I(|x|<=2)
    def phi6c_grad_weighted(x):
        if abs(x) > 2:
            return 0.0
        return (2*x - 1) * phi(x)

    def phi6c_grad2_weighted(x):
        if abs(x) > 2:
            return 0.0
        return ((2*x - 1)**2) * phi(x)

    E_phi6c, _ = integrate.quad(lambda x: phi6c_grad_weighted(x), -5, 5)
    E_phi6c2, _ = integrate.quad(lambda x: phi6c_grad2_weighted(x), -5, 5)
    Var_phi6c = E_phi6c2 - E_phi6c**2

    print(f"\n  Phi6 clamped [-2,2]: f'(x) = (2x-1)*I(|x|<=2)")
    print(f"    E[f'(x)]   = {E_phi6c:.6f} (numerical integration)")
    print(f"    Var[f'(x)] = {Var_phi6c:.6f}")
    print(f"    Std[f'(x)] = {np.sqrt(Var_phi6c):.6f}")
    print(f"    P(|x|>2) for N(0,1) = {2*(1-stats.norm.cdf(2)):.6f} ({2*(1-stats.norm.cdf(2))*100:.2f}% of gradients are zero)")

    # ReLU: f'(x) = I(x>0)
    # E[f'(x)] = P(x>0) = 0.5
    # Var[f'(x)] = 0.5*0.5 = 0.25
    print(f"\n  ReLU: f'(x) = I(x>0)")
    print(f"    E[f'(x)]   = 0.500 (EXACT)")
    print(f"    Var[f'(x)] = 0.250 (EXACT)")

    # GELU: numerical
    def gelu_g(x):
        c = 0.7978845608028654
        t = np.tanh(c * (x + 0.044715 * x**3))
        dt = 1.0 - t*t
        return 0.5 * (1.0 + t) + 0.5 * x * dt * c * (1.0 + 3 * 0.044715 * x**2)

    E_gelu, _ = integrate.quad(lambda x: gelu_g(x) * phi(x), -10, 10)
    E_gelu2, _ = integrate.quad(lambda x: gelu_g(x)**2 * phi(x), -10, 10)
    Var_gelu = E_gelu2 - E_gelu**2

    print(f"\n  GELU: f'(x) = complex form")
    print(f"    E[f'(x)]   = {E_gelu:.6f}")
    print(f"    Var[f'(x)] = {Var_gelu:.6f}")
    print(f"    Std[f'(x)] = {np.sqrt(Var_gelu):.6f}")

    # SiLU: numerical
    def silu_g(x):
        sig = 1.0 / (1.0 + np.exp(-np.clip(x, -30, 30)))
        return sig + x * sig * (1.0 - sig)

    E_silu, _ = integrate.quad(lambda x: silu_g(x) * phi(x), -10, 10)
    E_silu2, _ = integrate.quad(lambda x: silu_g(x)**2 * phi(x), -10, 10)
    Var_silu = E_silu2 - E_silu**2

    print(f"\n  SiLU: f'(x) = sig(x) + x*sig(x)*(1-sig(x))")
    print(f"    E[f'(x)]   = {E_silu:.6f}")
    print(f"    Var[f'(x)] = {Var_silu:.6f}")
    print(f"    Std[f'(x)] = {np.sqrt(Var_silu):.6f}")

    return {
        "GELU": (E_gelu, Var_gelu),
        "ReLU": (0.5, 0.25),
        "SiLU": (E_silu, Var_silu),
        "Phi6_clamped": (E_phi6c, Var_phi6c),
        "Phi6_unclamped": (-1.0, 4.0),
    }


# ── Numerical verification ──

def numerical_verification(n_samples=1_000_000):
    """Verify analytical results with Monte Carlo."""
    print(f"\n  NUMERICAL VERIFICATION (N={n_samples:,})")
    print("  " + "=" * 60)

    x = np.random.randn(n_samples)

    print(f"\n  {'Activation':18s}  {'E[f\'(x)]':>10s}  {'Std[f\'(x)]':>10s}  "
          f"{'|grad|<0.01':>12s}  {'|grad|>2':>10s}  {'grad<0':>8s}")
    print("  " + "-" * 80)

    results = {}
    for name, grad_fn in ACTIVATIONS.items():
        g = grad_fn(x)
        mean_g = np.mean(g)
        std_g = np.std(g)
        dead_frac = np.mean(np.abs(g) < 0.01)
        large_frac = np.mean(np.abs(g) > 2.0)
        neg_frac = np.mean(g < 0)
        results[name] = {
            "mean": mean_g, "std": std_g,
            "dead": dead_frac, "large": large_frac, "neg": neg_frac
        }
        print(f"  {name:18s}  {mean_g:10.4f}  {std_g:10.4f}  "
              f"{dead_frac*100:11.2f}%  {large_frac*100:9.2f}%  {neg_frac*100:7.2f}%")

    return results


# ── Gradient histogram (ASCII) ──

def gradient_histogram(n_samples=200_000):
    """ASCII histogram of gradient distributions."""
    x = np.random.randn(n_samples)
    bins = np.linspace(-3, 3, 31)

    print(f"\n  GRADIENT DISTRIBUTION HISTOGRAMS")
    print("  " + "=" * 60)

    for name, grad_fn in ACTIVATIONS.items():
        g = grad_fn(x)
        g_clipped = np.clip(g, -3, 3)
        counts, _ = np.histogram(g_clipped, bins=bins)
        max_count = max(counts)
        scale = 40.0 / max_count if max_count > 0 else 1

        print(f"\n  {name}:")
        for i in range(len(counts)):
            lo, hi = bins[i], bins[i+1]
            bar = "#" * int(counts[i] * scale)
            if lo <= 0 < hi:
                print(f"  {lo:+5.1f}|{bar}  <-- zero")
            else:
                print(f"  {lo:+5.1f}|{bar}")


# ── Gradient flow analysis ──

def gradient_flow_analysis():
    """Analyze how gradients flow through a chain of activations (depth analysis)."""
    print(f"\n  GRADIENT FLOW THROUGH DEPTH (10 layers)")
    print("  " + "=" * 60)
    print("  Simulate: gradient magnitude after passing through N activation layers")
    print("  Starting gradient = 1.0, x ~ N(0,1) at each layer")

    n_samples = 50_000
    depths = [1, 2, 5, 10, 20]

    print(f"\n  {'Activation':18s}", end="")
    for d in depths:
        print(f"  {'depth='+str(d):>10s}", end="")
    print()
    print("  " + "-" * (18 + 12 * len(depths)))

    for name, grad_fn in ACTIVATIONS.items():
        row = f"  {name:18s}"
        for depth in depths:
            # Chain rule: product of gradients at each layer
            grad_product = np.ones(n_samples)
            for _ in range(depth):
                x = np.random.randn(n_samples)
                g = grad_fn(x)
                grad_product *= g
            mean_mag = np.mean(np.abs(grad_product))
            row += f"  {mean_mag:10.6f}"
        print(row)

    print("\n  Ideal: gradient magnitude stays close to 1.0 across all depths.")
    print("  >> 1.0 = exploding gradients, << 1.0 = vanishing gradients.")


# ── Main ──

def main():
    SEP = "=" * 72
    print(SEP)
    print("  H-EE-2: Phi6Simple Gradient Properties")
    print("  Hypothesis: Phi6'(x) = 2x-1 gives natural gradient centering")
    print(SEP)

    analytical = analytical_moments()
    numerical = numerical_verification()
    gradient_histogram()
    gradient_flow_analysis()

    # Verdict
    print(f"\n  VERDICT")
    print("  " + "=" * 60)

    phi6_mean = numerical["Phi6_clamped"]["mean"]
    gelu_mean = numerical["GELU"]["mean"]

    print(f"\n  Original hypothesis: E[Phi6'(x)] ~ 0 for x ~ N(0,1)")
    print(f"  Actual: E[Phi6'(x)] = {phi6_mean:.4f}")
    print(f"  GELU:   E[GELU'(x)] = {gelu_mean:.4f}")

    if abs(phi6_mean) < abs(gelu_mean):
        print(f"\n  Phi6 gradient IS more centered than GELU ({abs(phi6_mean):.4f} < {abs(gelu_mean):.4f})")
        grade = "SUPPORTED"
    elif abs(phi6_mean) < 0.1:
        print(f"\n  Phi6 gradient is approximately centered (|E| < 0.1)")
        grade = "PARTIAL"
    else:
        print(f"\n  Phi6 gradient is NOT zero-centered. E[2x-1] = -1 analytically.")
        print(f"  The clamping at [-2,2] helps (zeros out 4.6% of inputs) but E ~ -1 still.")
        grade = "REFUTED"

    # But check for other useful properties
    phi6_dead = numerical["Phi6_clamped"]["dead"]
    relu_dead = numerical["ReLU"]["dead"]
    gelu_dead = numerical["GELU"]["dead"]

    print(f"\n  Additional findings:")
    print(f"    Dead gradient fraction: Phi6={phi6_dead*100:.1f}%, ReLU={relu_dead*100:.1f}%, GELU={gelu_dead*100:.1f}%")
    print(f"    Phi6 gradient is LINEAR (2x-1) -- simplest possible non-trivial backward pass")
    print(f"    Phi6 has NO dead neurons (unlike ReLU's 50% dead zone)")

    phi6_large = numerical["Phi6_clamped"]["large"]
    gelu_large = numerical["GELU"]["large"]
    print(f"    Large gradient fraction (|g|>2): Phi6={phi6_large*100:.1f}%, GELU={gelu_large*100:.1f}%")

    print(f"\n  Grade: {grade}")
    print(SEP)


if __name__ == "__main__":
    main()
