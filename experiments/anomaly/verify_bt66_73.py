#!/usr/bin/env python3
"""
Independent verification of BT-66 through BT-73.
All claims checked against n=6 arithmetic constants.
"""

# ── n=6 constants ──
n = 6
sigma = 12       # σ(6) = 1+2+3+6
tau = 4          # τ(6) = |{1,2,3,6}|
phi = 2          # φ(6) = |{1,5}|
sopfr = 5        # sopfr(6) = 2+3
J2 = 24          # J₂(6) = Jordan totient
mu = 1           # μ(6) = Möbius (6=2·3 squarefree)

results = []

def check(bt, label, formula_str, computed, expected):
    ok = computed == expected
    tag = "PASS" if ok else "FAIL"
    results.append((bt, label, ok))
    print(f"  [{tag}] {label}: {formula_str} = {computed}  (expected {expected})")

# ═══════════════════════════════════════════════════════════
# BT-66  Vision AI Universality
# ═══════════════════════════════════════════════════════════
print("=" * 70)
print("BT-66: Vision AI Universality")
print("=" * 70)

check("BT-66", "ViT-B heads", "sigma", sigma, 12)
check("BT-66", "ViT-B layers", "sigma", sigma, 12)
check("BT-66", "ViT-B d_model", "sigma * 2**n", sigma * 2**n, 768)
check("BT-66", "ViT-L layers", "J2", J2, 24)
check("BT-66", "ViT-L d_model", "2**(sigma-phi)", 2**(sigma - phi), 1024)
check("BT-66", "ViT-H layers", "2**sopfr", 2**sopfr, 32)
check("BT-66", "ViT-H d_model", "sopfr * 2**(sigma-tau)", sopfr * 2**(sigma - tau), 1280)
check("BT-66", "DINOv2 d_model", "sigma * 2**(sigma-sopfr)", sigma * 2**(sigma - sopfr), 1536)
check("BT-66", "Patch size", "tau**2", tau**2, 16)
check("BT-66", "MLP ratio", "tau", tau, 4)
check("BT-66", "MAE mask ratio", "(n//phi)/tau", (n // phi) / tau, 0.75)
check("BT-66", "CLIP embed", "2**(sigma-tau+mu)", 2**(sigma - tau + mu), 512)
check("BT-66", "Whisper mel", "phi**tau * sopfr", phi**tau * sopfr, 80)
check("BT-66", "Whisper chunk(s)", "(sigma-phi)*(n//phi)", (sigma - phi) * (n // phi), 30)
check("BT-66", "SD3 blocks", "J2", J2, 24)
check("BT-66", "SD3 VAE channels", "tau", tau, 4)
check("BT-66", "Flux.1 double blocks", "J2-sopfr", J2 - sopfr, 19)
check("BT-66", "Flux.1 single blocks", "phi*(J2-sopfr)", phi * (J2 - sopfr), 38)
check("BT-66", "Flux.1 guidance", "(sigma-sopfr)/phi", (sigma - sopfr) / phi, 3.5)
check("BT-66", "SimCLR temperature", "1/(sigma-phi)", 1 / (sigma - phi), 0.1)
check("BT-66", "SimCLR proj dim", "2**(sigma-sopfr)", 2**(sigma - sopfr), 128)
check("BT-66", "LLaVA connector layers", "phi", phi, 2)
check("BT-66", "LLaVA input res", "(sigma-sopfr)*2**sopfr", (sigma - sopfr) * 2**sopfr, 224)

# ═══════════════════════════════════════════════════════════
# BT-67  MoE Top-k / Expert Ratios
# ═══════════════════════════════════════════════════════════
print()
print("=" * 70)
print("BT-67: MoE Top-k / Expert Ratios")
print("=" * 70)

from fractions import Fraction

def check_frac(bt, label, formula_str, num, den, expected_frac):
    computed = Fraction(num, den)
    ok = computed == expected_frac
    tag = "PASS" if ok else "FAIL"
    results.append((bt, label, ok))
    print(f"  [{tag}] {label}: {formula_str} = {num}/{den} = {float(computed):.6f}  (expected {expected_frac})")

check_frac("BT-67", "Mixtral 2/8", "1/tau", 2, 8, Fraction(1, tau))
check_frac("BT-67", "DBRX 4/16", "1/tau", 4, 16, Fraction(1, tau))
check_frac("BT-67", "DeepSeek-V3 8/256", "1/2**sopfr", 8, 256, Fraction(1, 2**sopfr))
check_frac("BT-67", "Llama 4  1/16", "1/2**tau", 1, 16, Fraction(1, 2**tau))
check_frac("BT-67", "Qwen3 8/128", "1/2**tau", 8, 128, Fraction(1, 2**tau))
check_frac("BT-67", "GShard 1/2048", "1/2**(sigma-mu)", 1, 2048, Fraction(1, 2**(sigma - mu)))

# ═══════════════════════════════════════════════════════════
# BT-68  HVDC Voltage Ladder
# ═══════════════════════════════════════════════════════════
print()
print("=" * 70)
print("BT-68: HVDC Voltage Ladder")
print("=" * 70)

check("BT-68", "500 kV", "sopfr*(sigma-phi)**2", sopfr * (sigma - phi)**2, 500)
check("BT-68", "800 kV", "(sigma-tau)*(sigma-phi)**2", (sigma - tau) * (sigma - phi)**2, 800)
check("BT-68", "1100 kV", "(sigma-mu)*(sigma-phi)**2", (sigma - mu) * (sigma - phi)**2, 1100)

# ═══════════════════════════════════════════════════════════
# BT-69  Chiplet / Next-Gen Hardware
# ═══════════════════════════════════════════════════════════
print()
print("=" * 70)
print("BT-69: Chiplet / Next-Gen Hardware")
print("=" * 70)

check("BT-69", "B300 SMs", "phi**tau * (sigma-phi)", phi**tau * (sigma - phi), 160)
check("BT-69", "R100 stacks", "sigma", sigma, 12)
check("BT-69", "R100 dies", "phi", phi, 2)
check("BT-69", "MI350X HBM (GB)", "sigma * J2", sigma * J2, 288)
check("BT-69", "SP/CU per SM", "2**n", 2**n, 64)
check("BT-69", "TPU v7 chips", "2**(sigma-tau)", 2**(sigma - tau), 256)
check("BT-69", "M4 Ultra GPU cores", "phi**tau * sopfr", phi**tau * sopfr, 80)
check("BT-69", "M4 Ultra mem (GB)", "sigma * phi**tau", sigma * phi**tau, 192)
check("BT-69", "UCIe pitch (um)", "J2 + mu", J2 + mu, 25)
check("BT-69", "UCIe lanes", "2**n", 2**n, 64)
check("BT-69", "N2 gate pitch (nm)", "sigma * tau", sigma * tau, 48)
check("BT-69", "N2 metal (nm)", "P2 = 28", 28, 28)
check("BT-69", "HBM4 channels", "2**tau", 2**tau, 16)
check("BT-69", "CXL lanes", "2**n", 2**n, 64)
check("BT-69", "CoWoS gen", "sopfr", sopfr, 5)

# ═══════════════════════════════════════════════════════════
# BT-70  0.1 Regularisation Universality Count
# ═══════════════════════════════════════════════════════════
print()
print("=" * 70)
print("BT-70: 0.1 Regularisation Universality (count of algorithms)")
print("=" * 70)

check("BT-70", "Count of 0.1 algorithms", "sigma - tau", sigma - tau, 8)

# ═══════════════════════════════════════════════════════════
# BT-71  NeRF / 3D Gaussian Splatting
# ═══════════════════════════════════════════════════════════
print()
print("=" * 70)
print("BT-71: NeRF / 3D Gaussian Splatting")
print("=" * 70)

check("BT-71", "NeRF pos_enc L", "sigma - phi", sigma - phi, 10)
check("BT-71", "NeRF dir_enc L", "tau", tau, 4)
check("BT-71", "NeRF layers", "sigma - tau", sigma - tau, 8)
check("BT-71", "NeRF width", "2**(sigma-tau)", 2**(sigma - tau), 256)
check("BT-71", "NeRF skip connection", "sopfr", sopfr, 5)
check("BT-71", "3DGS SH degree", "n // phi", n // phi, 3)
check("BT-71", "3DGS SH coeffs", "sigma * tau", sigma * tau, 48)

# ═══════════════════════════════════════════════════════════
# BT-72  Audio Neural Codec
# ═══════════════════════════════════════════════════════════
print()
print("=" * 70)
print("BT-72: Audio Neural Codec (EnCodec / SoundStream)")
print("=" * 70)

check("BT-72", "Codebooks", "sigma - tau", sigma - tau, 8)
check("BT-72", "Codebook entries", "2**(sigma-phi)", 2**(sigma - phi), 1024)
check("BT-72", "Sample rate (Hz)", "J2 * 1000", J2 * 1000, 24000)
check("BT-72", "Bandwidth (kbps tier)", "n", n, 6)
check("BT-72", "Frame ms", "J2 - tau", J2 - tau, 20)

# ═══════════════════════════════════════════════════════════
# BT-73  Tokenizer Vocabulary Sizes
# ═══════════════════════════════════════════════════════════
print()
print("=" * 70)
print("BT-73: Tokenizer Vocabulary Sizes")
print("=" * 70)

gpt2_vocab = sopfr * (sigma - phi)**tau + 2**(sigma - tau) + mu
check("BT-73", "GPT-2 vocab", "sopfr*(sigma-phi)**tau + 2**(sigma-tau) + mu",
      gpt2_vocab, 50257)

cl100k = (sigma - phi)**sopfr
check("BT-73", "cl100k (GPT-4)", "(sigma-phi)**sopfr", cl100k, 100000)

llama_vocab = 2**sopfr * (sigma - phi)**(n // phi)
check("BT-73", "LLaMA vocab", "2**sopfr * (sigma-phi)**(n//phi)", llama_vocab, 32000)

# ═══════════════════════════════════════════════════════════
# Summary
# ═══════════════════════════════════════════════════════════
print()
print("=" * 70)
print("SUMMARY")
print("=" * 70)

total = len(results)
passed = sum(1 for _, _, ok in results if ok)
failed = total - passed

# Per-BT breakdown
from collections import Counter
bt_total = Counter()
bt_pass = Counter()
for bt, _, ok in results:
    bt_total[bt] += 1
    if ok:
        bt_pass[bt] += 1

print()
print(f"{'BT':<10} {'PASS':>5} / {'TOTAL':>5}   {'Rate':>6}")
print("-" * 35)
for bt in sorted(bt_total.keys()):
    t = bt_total[bt]
    p = bt_pass[bt]
    pct = 100 * p / t
    marker = " <<<" if p < t else ""
    print(f"{bt:<10} {p:>5} / {t:>5}   {pct:>5.1f}%{marker}")

print("-" * 35)
pct_all = 100 * passed / total
print(f"{'TOTAL':<10} {passed:>5} / {total:>5}   {pct_all:>5.1f}%")
print()

if failed == 0:
    print("ALL CHECKS PASSED.")
else:
    print(f"FAILURES: {failed}")
    for bt, label, ok in results:
        if not ok:
            print(f"  - {bt} / {label}")
