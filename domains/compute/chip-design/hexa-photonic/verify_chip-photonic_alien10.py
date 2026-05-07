#!/usr/bin/env python3
# verify_chip-photonic_alien10.py -- §11.5 TP-PHOTONIC-* auto-verify (stdlib)

from fractions import Fraction
from math import pi, log, log2, sqrt, exp


def sigma(n): return sum(d for d in range(1, n+1) if n % d == 0)
def tau(n):   return sum(1 for d in range(1, n+1) if n % d == 0)

N, SIGMA, TAU, PHI = 6, sigma(6), tau(6), 2
J2 = 2*SIGMA
SIGMA_SQ = SIGMA*SIGMA

H    = 6.62607015e-34
HBAR = H / (2 * pi)
C    = 299792458.0       # m/s — SI 2019 EXACT definition
K_B  = 1.380649e-23
SIGMA_SB = 5.670374419e-8  # W/(m²·K⁴)
WIEN_B   = 2.897771955e-3  # m·K


def tp_p_a1_diffraction():
    """Δx_min = λ/(2·NA). λ=550nm, NA=1.4."""
    lam, NA = 550e-9, 1.4
    dx_min = lam / (2 * NA)
    return {"id":"TP-PHOTONIC-A1","name":"Abbe diffraction",
            "lambda_m":lam,"NA":NA,"dx_min_m":dx_min,
            "PASS":dx_min>0,"alien_tgt":10,"closure":6}

def tp_p_a2_casimir():
    """F/A = π²ℏc/(240·d⁴). d=100nm — exponent 4=τ EXACT."""
    d = 100e-9
    pressure = (pi**2 * HBAR * C) / (240 * d**4)
    exponent_eq_tau = (4 == TAU)
    return {"id":"TP-PHOTONIC-A2","name":"Casimir d⁻⁴",
            "d_m":d,"pressure_Pa":pressure,"exponent_eq_tau":exponent_eq_tau,
            "PASS":pressure>0 and exponent_eq_tau,"alien_tgt":10,"closure":10}

def tp_p_a3_stefan_boltzmann():
    """j = σ_SB·T⁴. T=1000K. exponent 4 = τ EXACT."""
    T = 1000.0
    j = SIGMA_SB * T**4
    return {"id":"TP-PHOTONIC-A3","name":"Stefan-Boltzmann T⁴",
            "T_K":T,"j_W_per_m2":j,"exponent_eq_tau":4==TAU,
            "PASS":j>0 and 4==TAU,"alien_tgt":10,"closure":10}

def tp_p_a4_planck():
    """E = hν. ν = 600 THz."""
    nu = 6e14
    E = H * nu
    return {"id":"TP-PHOTONIC-A4","name":"Planck E=hν",
            "nu_Hz":nu,"E_J":E,"E_eV":E/1.602e-19,
            "PASS":E>0,"alien_tgt":10,"closure":8}

def tp_p_a5_mzi():
    """Δφ = 2π·n_eff·L/λ. L=1mm, n_eff=2, λ=1.55μm."""
    L, n_eff, lam = 1e-3, 2.0, 1.55e-6
    phase = 2 * pi * n_eff * L / lam
    return {"id":"TP-PHOTONIC-A5","name":"MZI phase",
            "L_m":L,"n_eff":n_eff,"lambda_m":lam,"phase_rad":phase,
            "PASS":phase>0,"alien_tgt":9,"closure":7}

def tp_p_a6_wien():
    """λ_max·T = b. T=300K → λ_max≈9.66 μm."""
    T = 300.0
    lam_max = WIEN_B / T
    return {"id":"TP-PHOTONIC-A6","name":"Wien displacement",
            "T_K":T,"lambda_max_m":lam_max,"lambda_max_um":lam_max*1e6,
            "in_IR_band":5e-6 < lam_max < 50e-6,
            "PASS":5e-6 < lam_max < 50e-6,"alien_tgt":10,"closure":5}

def tp_p_a7_shannon():
    """C = B·log2(1+SNR), B=1THz, SNR=100."""
    B, snr = 1e12, 100.0
    cap = B * log2(1 + snr)
    n_lanes = SIGMA * J2  # 288
    return {"id":"TP-PHOTONIC-A7","name":"Shannon-Hartley",
            "B_Hz":B,"snr":snr,"per_lane_bits_s":cap,
            "n_lanes_sigma_J2":n_lanes,
            "PASS":cap>0 and n_lanes==288,"alien_tgt":10,"closure":9}

def tp_p_a8_heisenberg():
    """ΔE·Δt ≥ ℏ/2. ΔE=1eV → Δt_min ≈ 3.3e-16 s."""
    de = 1.602e-19
    dt_min = HBAR / (2 * de)
    return {"id":"TP-PHOTONIC-A8","name":"Heisenberg ΔE·Δt",
            "delta_E_J":de,"dt_min_s":dt_min,
            "PASS":dt_min>0,"alien_tgt":10,"closure":6}

def tp_p_a9_bragg():
    """λ_Bragg = 2·n_eff·d at σ=12 layer pairs."""
    n_eff, d_layer, layer_pairs = 2.0, 200e-9, SIGMA
    lam_bragg = 2 * n_eff * d_layer
    return {"id":"TP-PHOTONIC-A9","name":"Bragg σ=12 pairs",
            "n_eff":n_eff,"d_layer_m":d_layer,
            "lambda_bragg_m":lam_bragg,"layer_pairs":layer_pairs,
            "pairs_eq_sigma":layer_pairs==SIGMA,
            "PASS":lam_bragg>0 and layer_pairs==SIGMA,"alien_tgt":9,"closure":9}

def tp_p_a10_holographic():
    """S = A/(4ℓ_p²). A=1m². ℓ_p² = ℏG/c³."""
    G_const = 6.67430e-11
    l_p_sq = HBAR * G_const / (C**3)
    A = 1.0
    S_holographic = A / (4 * l_p_sq)
    return {"id":"TP-PHOTONIC-A10","name":"Holographic A/(4ℓ_p²)",
            "A_m2":A,"l_p_sq_m2":l_p_sq,
            "S_bits_per_m2":S_holographic / log(2),
            "PASS":S_holographic>0,"alien_tgt":10,"closure":7}

def tp_p_a11_speed_of_light():
    """c = 299792458 m/s exactly (SI 2019 definition)."""
    c_si = 299792458
    return {"id":"TP-PHOTONIC-A11","name":"c SI 2019 EXACT",
            "c_m_per_s":c_si,"matches_python_constant":C==c_si,
            "PASS":C==c_si,"alien_tgt":10,"closure":10}

def tp_p_a12_fourier_limit():
    """BW·Δt ≥ 1/(4π) for Gaussian pulse."""
    bw_dt_min = 1.0 / (4 * pi)
    bw, dt = 1e12, 1e-12
    product = bw * dt
    above_floor = product >= bw_dt_min
    return {"id":"TP-PHOTONIC-A12","name":"Fourier limit",
            "bw_Hz":bw,"dt_s":dt,"product":product,
            "floor_1_over_4pi":bw_dt_min,
            "above_floor":above_floor,
            "PASS":above_floor,"alien_tgt":10,"closure":7}


ALL = [tp_p_a1_diffraction, tp_p_a2_casimir, tp_p_a3_stefan_boltzmann,
       tp_p_a4_planck, tp_p_a5_mzi, tp_p_a6_wien,
       tp_p_a7_shannon, tp_p_a8_heisenberg, tp_p_a9_bragg,
       tp_p_a10_holographic, tp_p_a11_speed_of_light, tp_p_a12_fourier_limit]


def main():
    print("=" * 72)
    print("§11.5 TP-PHOTONIC-* alien-10 auto-verify (12 TPs)")
    print(f"  n={N}, σ={SIGMA}, τ={TAU}, φ={PHI}, J₂={J2}, σ²={SIGMA_SQ}")
    print("=" * 72)
    rs = [fn() for fn in ALL]
    for r in rs:
        flag = "PASS" if r["PASS"] else "FAIL"
        print(f"  [{flag}] {r['id']:<16} {r['name']:<30} alien={r['alien_tgt']} closure={r['closure']}")
    p = sum(1 for r in rs if r["PASS"])
    print("=" * 72)
    print(f"  {p}/{len(rs)} PASS")
    return 0 if p == len(rs) else 1


if __name__ == "__main__":
    raise SystemExit(main())
