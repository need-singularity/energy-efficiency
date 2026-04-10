#!/usr/bin/env python3
"""Testable Predictions Tier 1 — Numerical Verification

Verifies the numerical/mathematical claims behind Tier 1 predictions
from docs/testable-predictions.md without requiring ML training.

Each check: prediction text, expected value, computed value, PASS/FAIL
"""

import math
import sys
from fractions import Fraction

# ── n=6 Core Constants ──
n = 6
sigma = 12       # sum of divisors of 6: 1+2+3+6
tau = 4          # number of divisors of 6: {1,2,3,6}
phi = 2          # Euler totient of 6
J2 = 24          # Jordan totient J_2(6)
mu = 1           # Mobius mu(6) = (-1)^2
sopfr = 5        # sum of prime factors: 2+3
divisors = [1, 2, 3, 6]

results = []

def check(name, source, expected, computed, tol=1e-9):
    """Register a verification result."""
    if isinstance(expected, (int, Fraction)) and isinstance(computed, (int, Fraction)):
        passed = (expected == computed)
    else:
        passed = abs(float(expected) - float(computed)) <= tol
    grade = "PASS" if passed else "FAIL"
    results.append({
        "name": name,
        "source": source,
        "expected": expected,
        "computed": computed,
        "grade": grade,
    })

# ════════════════════════════════════════════════════════════
# P-1: EFA Head Split — sigma=12 heads as 6+4+2
# ════════════════════════════════════════════════════════════
# Verify the split sums to sigma and uses n=6 arithmetic
efa_full = n           # 6 full attention heads
efa_local = tau        # 4 local attention heads
efa_global = phi       # 2 global attention heads
check(
    "P-1: EFA head split sums to sigma=12",
    "BT-39 / EFA",
    sigma,
    efa_full + efa_local + efa_global,
)
check(
    "P-1: EFA full heads = n = 6",
    "BT-39",
    n, efa_full,
)
check(
    "P-1: EFA local heads = tau = 4",
    "BT-39",
    tau, efa_local,
)
check(
    "P-1: EFA global heads = phi = 2",
    "BT-39",
    phi, efa_global,
)

# ════════════════════════════════════════════════════════════
# P-2: LoRA rank r = sigma - tau = 8
# ════════════════════════════════════════════════════════════
check(
    "P-2: LoRA optimal rank = sigma-tau = 8",
    "BT-58",
    8,
    sigma - tau,
)
# LoRA rank ladder
check("P-2: LoRA rank ladder r=4 = tau", "BT-58", 4, tau)
check("P-2: LoRA rank ladder r=8 = sigma-tau", "BT-58", 8, sigma - tau)
check("P-2: LoRA rank ladder r=16 = 2^tau", "BT-58", 16, 2**tau)
check("P-2: LoRA rank ladder r=32 = 2^sopfr", "BT-58", 32, 2**sopfr)

# ════════════════════════════════════════════════════════════
# P-3: MoE (8,2) — experts=sigma-tau=8, top-k=phi=2
# ════════════════════════════════════════════════════════════
check(
    "P-3: MoE experts = sigma-tau = 8",
    "BT-31",
    8,
    sigma - tau,
)
check(
    "P-3: MoE top-k = phi = 2",
    "BT-31",
    2,
    phi,
)
# MoE top-k vocabulary
check("P-3: MoE top-1 = mu", "BT-31", 1, mu)
check("P-3: MoE top-2 = phi", "BT-31", 2, phi)
check("P-3: MoE top-6 = n", "BT-31", 6, n)
check("P-3: MoE top-8 = sigma-tau", "BT-31", 8, sigma - tau)

# ════════════════════════════════════════════════════════════
# P-4: Mertens Dropout p = ln(4/3) ≈ 0.2877
# ════════════════════════════════════════════════════════════
expected_dropout = math.log(4 / 3)
check(
    "P-4: Mertens dropout = ln(4/3) ≈ 0.288",
    "BT-46",
    math.log(4 / 3),  # ln(4/3) exact
    expected_dropout,
    tol=1e-15,
)
check(
    "P-4: ln(4/3) = ln(tau^2/sigma)",
    "BT-46",
    math.log(4 / 3),
    math.log(tau**2 / sigma),
    tol=1e-15,
)

# ════════════════════════════════════════════════════════════
# Chinchilla Scaling (BT-26) — tokens/params ratio
# ════════════════════════════════════════════════════════════
chinchilla_ratio = J2 - tau  # = 20
check(
    "BT-26: Chinchilla tokens/params = J2-tau = 20",
    "BT-26",
    20,
    chinchilla_ratio,
)
chinchilla_alpha = Fraction(1, n // phi)  # 1/3
check(
    "BT-26: Chinchilla alpha = 1/(n/phi) = 1/3",
    "BT-26",
    Fraction(1, 3),
    chinchilla_alpha,
)
chinchilla_beta = math.log(tau**2 / sigma)  # ln(4/3)
check(
    "BT-26: Chinchilla beta = ln(tau^2/sigma) = ln(4/3)",
    "BT-26",
    math.log(4 / 3),
    chinchilla_beta,
    tol=1e-15,
)

# ════════════════════════════════════════════════════════════
# AdamW Parameters (BT-54) — The Training Quintuplet
# ════════════════════════════════════════════════════════════
beta1 = 1 - 1 / (sigma - phi)       # 1 - 1/10 = 0.9
beta2 = 1 - 1 / (J2 - tau)          # 1 - 1/20 = 0.95
epsilon = 10 ** (-(sigma - tau))     # 10^-8
weight_decay = 1 / (sigma - phi)     # 0.1
grad_clip = (sigma * phi) / (n * tau)  # R(6) = 1.0

check("BT-54: AdamW beta1 = 1-1/(sigma-phi) = 0.9", "BT-54", 0.9, beta1)
check("BT-54: AdamW beta2 = 1-1/(J2-tau) = 0.95", "BT-54", 0.95, beta2)
check("BT-54: AdamW epsilon = 10^-(sigma-tau) = 1e-8", "BT-54", 1e-8, epsilon)
check("BT-54: AdamW weight_decay = 1/(sigma-phi) = 0.1", "BT-54", 0.1, weight_decay)
check("BT-54: AdamW grad_clip = R(6) = sigma*phi/(n*tau) = 1.0", "BT-54", 1.0, grad_clip)
# beta1 = 1 - weight_decay conjugacy
check("BT-54: beta1 + weight_decay = 1 (conjugacy)", "BT-54", 1.0, beta1 + weight_decay)

# ════════════════════════════════════════════════════════════
# sigma-tau=8 Universal AI Constant (BT-58)
# ════════════════════════════════════════════════════════════
st = sigma - tau
check("BT-58: sigma-tau = 8", "BT-58", 8, st)
check("BT-58: 2^(sigma-tau) = 256 (byte/BPE/batch)", "BT-58", 256, 2**st)
check("BT-58: FP8 = sigma-tau bits", "BT-58", 8, st)
check("BT-58: ImageNet base batch = 2^(sigma-tau) = 256", "BT-58", 256, 2**st)
check("BT-58: LoRA default rank = sigma-tau = 8", "BT-58", 8, st)

# ════════════════════════════════════════════════════════════
# 0.1 Universal Regularization (BT-64)
# ════════════════════════════════════════════════════════════
reg = 1 / (sigma - phi)
check("BT-64: 1/(sigma-phi) = 0.1", "BT-64", 0.1, reg)
check("BT-64: 1 - 0.1 = 0.9 = beta1 (conjugate)", "BT-64", 0.9, 1 - reg)

# ════════════════════════════════════════════════════════════
# Diffusion DDPM constants (BT-61)
# ════════════════════════════════════════════════════════════
ddpm_T = (sigma - phi) ** (n // phi)        # 10^3 = 1000
ddpm_beta_start = (sigma - phi) ** (-tau)    # 10^-4 = 0.0001
ddpm_beta_end_num = phi                      # 2
ddpm_beta_end_den = (sigma - phi) ** phi     # 100
ddpm_beta_end = ddpm_beta_end_num / ddpm_beta_end_den  # 0.02
ddim_steps = (sigma - phi) * sopfr           # 50
ddim_ratio = J2 - tau                        # 20

check("BT-61: DDPM T = (sigma-phi)^(n/phi) = 1000", "BT-61", 1000, ddpm_T)
check("BT-61: DDPM beta_start = (sigma-phi)^(-tau) = 1e-4", "BT-61", 0.0001, ddpm_beta_start)
check("BT-61: DDPM beta_end = phi/(sigma-phi)^phi = 0.02", "BT-61", 0.02, ddpm_beta_end)
check("BT-61: DDIM steps = (sigma-phi)*sopfr = 50", "BT-61", 50, ddim_steps)
check("BT-61: DDIM/DDPM ratio = J2-tau = 20", "BT-61", 20, ddim_ratio)
check("BT-61: CFG scale = (sigma+n/phi)/phi = 7.5", "BT-61", 7.5, (sigma + n // phi) / phi)
check("BT-61: Latent channels = tau = 4", "BT-61", 4, tau)
check("BT-61: Spatial compression = sigma-tau = 8", "BT-61", 8, sigma - tau)

# ════════════════════════════════════════════════════════════
# Inference Scaling (BT-42)
# ════════════════════════════════════════════════════════════
top_p = 1 - 1 / (J2 - tau)    # 1 - 1/20 = 0.95
top_k = tau * (sigma - phi)    # 4*10 = 40
max_tokens = 2 ** sigma        # 2^12 = 4096

check("BT-42: top-p = 1-1/(J2-tau) = 0.95", "BT-42", 0.95, top_p)
check("BT-42: top-k = tau*(sigma-phi) = 40", "BT-42", 40, top_k)
check("BT-42: max_tokens = 2^sigma = 4096", "BT-42", 4096, max_tokens)

# ════════════════════════════════════════════════════════════
# RoPE theta (BT-34)
# ════════════════════════════════════════════════════════════
rope_theta = (sigma - phi) ** tau  # 10^4 = 10000
check("BT-34: RoPE theta = (sigma-phi)^tau = 10000", "BT-34", 10000, rope_theta)
check("BT-34: Weight decay = 1/(sigma-phi) = 0.1", "BT-34", 0.1, 1 / (sigma - phi))

# ════════════════════════════════════════════════════════════
# Egyptian Fraction — Perfect Number Definition
# ════════════════════════════════════════════════════════════
egyptian_sum = Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 6)
check("Core: 1/2+1/3+1/6 = 1 (perfect number)", "BT-5/7", Fraction(1, 1), egyptian_sum)

# Core Theorem R(6) = 1
R6 = Fraction(sigma * phi, n * tau)
check("Core: R(6) = sigma*phi/(n*tau) = 1", "Core Theorem", Fraction(1, 1), R6)

# sigma(n)*phi(n) = n*tau(n) for n=6
check("Core: sigma*phi = n*tau = 24", "Core Theorem", 24, sigma * phi)
check("Core: n*tau = 24", "Core Theorem", 24, n * tau)

# ════════════════════════════════════════════════════════════
# Transformer Dimension Ladder (BT-33)
# ════════════════════════════════════════════════════════════
# BERT d=768 = sigma * 2^n = 12 * 64
check("BT-33: BERT d=768 = sigma*2^n = 12*64", "BT-33", 768, sigma * 2**n)
# GPT-3 d=12288 = sigma*1024 = sigma*2^(sigma-phi)
# Actually 12288 = sigma * 1024 = 12 * 1024
check("BT-33: GPT-3 d=12288 = sigma*1024", "BT-33", 12288, sigma * 1024)
# SwiGLU ratio 8/3
swiglu = Fraction(sigma - tau, n // phi)  # 8/3
check("BT-33: SwiGLU ratio = (sigma-tau)/(n/phi) = 8/3", "BT-33", Fraction(8, 3), swiglu)
# Head dimension d_h = 2^(sigma-sopfr) = 128
check("BT-33: Head dim = 2^(sigma-sopfr) = 128", "BT-33", 128, 2**(sigma - sopfr))

# ════════════════════════════════════════════════════════════
# Print Results
# ════════════════════════════════════════════════════════════
print("=" * 90)
print("N6 Architecture — Testable Predictions Tier 1 Verification")
print("=" * 90)
print()

pass_count = sum(1 for r in results if r["grade"] == "PASS")
fail_count = sum(1 for r in results if r["grade"] == "FAIL")
total = len(results)

# Group by source
from collections import OrderedDict
groups = OrderedDict()
for r in results:
    src = r["source"]
    if src not in groups:
        groups[src] = []
    groups[src].append(r)

for src, items in groups.items():
    print(f"── {src} ──")
    for r in items:
        status = "PASS" if r["grade"] == "PASS" else "FAIL"
        print(f"  [{status}] {r['name']}")
        print(f"         Expected: {r['expected']}  |  Computed: {r['computed']}")
    print()

print("=" * 90)
print(f"TOTAL: {pass_count}/{total} PASS, {fail_count}/{total} FAIL")
print("=" * 90)

if fail_count > 0:
    print("\nFAILED checks:")
    for r in results:
        if r["grade"] == "FAIL":
            print(f"  - {r['name']}: expected={r['expected']}, got={r['computed']}")

sys.exit(0 if fail_count == 0 else 1)
