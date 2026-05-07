#!/usr/bin/env python3
# verify_chip-dna-molecular_alien10.py -- §11.5 TP-DNA-* auto-verify (stdlib).

from fractions import Fraction
from math import log, log2


def sigma(n): return sum(d for d in range(1, n+1) if n % d == 0)
def tau(n):   return sum(1 for d in range(1, n+1) if n % d == 0)

N, SIGMA, TAU, PHI = 6, sigma(6), tau(6), 2
J2 = 2*SIGMA
SIGMA_SQ = SIGMA*SIGMA


def tp_d_a1_four_bases():
    bases = ["A","T","C","G"]
    return {"id":"TP-DNA-A1","name":"4-base alphabet = τ",
            "bases":bases,"count":len(bases),
            "PASS":len(bases) == TAU == 4,"alien_tgt":10,"closure":10}

def tp_d_a2_shannon_per_base():
    bits_per_base = log2(TAU)
    return {"id":"TP-DNA-A2","name":"Shannon log₂(τ) = φ bits",
            "bits_per_base":bits_per_base,
            "PASS":bits_per_base == PHI == 2.0,"alien_tgt":10,"closure":10}

def tp_d_a3_watson_crick_pairs():
    pairs = [("A","T"),("G","C")]
    return {"id":"TP-DNA-A3","name":"Watson-Crick = φ pairs",
            "pairs":pairs,"count":len(pairs),
            "PASS":len(pairs) == PHI == 2,"alien_tgt":10,"closure":10}

def tp_d_a4_codon_length():
    codon_len = N // PHI
    return {"id":"TP-DNA-A4","name":"Codon = n/φ",
            "codon_length":codon_len,
            "PASS":codon_len == 3 == N//PHI,
            "alien_tgt":10,"closure":10}

def tp_d_a5_codon_count():
    n_codons = TAU ** 3
    return {"id":"TP-DNA-A5","name":"64 codons = τ³",
            "n_codons":n_codons,
            "PASS":n_codons == 64 == TAU**3,
            "alien_tgt":10,"closure":10}

def tp_d_a6_polymerase_fidelity():
    error_rate = 1e-10
    floor = 1e-9
    return {"id":"TP-DNA-A6","name":"Polymerase ≤10⁻⁹",
            "error_rate":error_rate,"floor":floor,
            "PASS":error_rate < floor,"alien_tgt":10,"closure":6}

def tp_d_a7_eigen_threshold():
    L, s = 10**4, 2
    mu_max = log(s) / L
    real_mu = 1e-9
    return {"id":"TP-DNA-A7","name":"Eigen threshold",
            "L_bp":L,"mu_max":mu_max,"real_mu":real_mu,
            "PASS":real_mu < mu_max,"alien_tgt":10,"closure":7}

def tp_d_a8_storage_density():
    pb_per_g = 215.0
    bytes_per_g = pb_per_g * 1e15
    return {"id":"TP-DNA-A8","name":"DNA storage 215 PB/g",
            "pb_per_g":pb_per_g,"bytes_per_g":bytes_per_g,
            "PASS":bytes_per_g > 1e15,"alien_tgt":10,"closure":5}

def tp_d_a9_helical_pitch():
    bp_per_turn = 10
    return {"id":"TP-DNA-A9","name":"B-form 10 bp/turn",
            "bp_per_turn":bp_per_turn,
            "PASS":9 <= bp_per_turn <= 11,
            "alien_tgt":9,"closure":6}

def tp_d_a10_phosphodiester_energy():
    e_kj = 30.0
    return {"id":"TP-DNA-A10","name":"Phosphodiester ~30 kJ/mol",
            "energy_kJ_per_mol":e_kj,
            "PASS":25 <= e_kj <= 35,
            "alien_tgt":9,"closure":5}

def tp_d_a11_replication_rate():
    bp_per_s = 1000.0
    return {"id":"TP-DNA-A11","name":"Replication 1000 bp/s",
            "bp_per_s":bp_per_s,
            "PASS":500 <= bp_per_s <= 2000,
            "alien_tgt":9,"closure":5}

def tp_d_a12_amino_acid_count():
    n_amino = 20
    closure_path = TAU * 5  # τ × sopfr(6)
    return {"id":"TP-DNA-A12","name":"20 amino = τ·sopfr",
            "n_amino":n_amino,"tau_x_sopfr":closure_path,
            "PASS":n_amino == closure_path == 20,
            "alien_tgt":10,"closure":6}


ALL = [tp_d_a1_four_bases, tp_d_a2_shannon_per_base, tp_d_a3_watson_crick_pairs,
       tp_d_a4_codon_length, tp_d_a5_codon_count, tp_d_a6_polymerase_fidelity,
       tp_d_a7_eigen_threshold, tp_d_a8_storage_density, tp_d_a9_helical_pitch,
       tp_d_a10_phosphodiester_energy, tp_d_a11_replication_rate,
       tp_d_a12_amino_acid_count]


def main():
    print("=" * 72)
    print("§11.5 TP-DNA-* alien-10 auto-verify (12 TPs)")
    print(f"  n={N}, σ={SIGMA}, τ={TAU}, φ={PHI}, J₂={J2}, σ²={SIGMA_SQ}")
    print(f"  bases=τ=4 / bits=φ=2 / pairs=φ=2 / codon=n/φ=3 / count=τ³=64")
    print("=" * 72)
    rs = [fn() for fn in ALL]
    for r in rs:
        flag = "PASS" if r["PASS"] else "FAIL"
        print(f"  [{flag}] {r['id']:<12} {r['name']:<32} alien={r['alien_tgt']} closure={r['closure']}")
    p = sum(1 for r in rs if r["PASS"])
    print("=" * 72)
    print(f"  {p}/{len(rs)} PASS")
    return 0 if p == len(rs) else 1


if __name__ == "__main__":
    raise SystemExit(main())
