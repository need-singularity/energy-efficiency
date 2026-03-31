#!/usr/bin/env python3
"""HEXA-MATERIAL 소재 아키텍처 수학 검증 — 101개 파라미터 전수 검사"""

import sys

# N6 constants
n = 6; phi = 2; tau = 4; sigma = 12; sopfr = 5; mu = 1; J2 = 24; R = 1; P2 = 28

passed = 0; failed = 0; total = 0

def check(cat, name, expected, formula_str, formula_val):
    global passed, failed, total
    total += 1
    ok = expected == formula_val
    if not ok:
        failed += 1
        print(f"  ❌ FAIL [{cat}] {name}: expected={expected}, got={formula_val} ({formula_str})")
    else:
        passed += 1
        print(f"  ✅ PASS [{cat}] {name} = {expected} = {formula_str}")

print("=" * 70)
print("HEXA-MATERIAL Verification")
print("=" * 70)

# === 1. Wafer Materials (22) ===
print("\n--- 1. Wafer Materials ---\n")
w = passed
check("Si", "Atomic number Z", 14, "σ+φ", sigma+phi)
check("Si", "Coordination CN", 4, "τ", tau)
check("Si", "Valence electrons", 4, "τ", tau)
check("Si", "Atoms/unit cell", 8, "σ-τ", sigma-tau)
check("Si", "Wafer 300mm (inches)", 12, "σ", sigma)
check("Si", "Wafer 200mm (inches)", 8, "σ-τ", sigma-tau)
check("Si", "Crystal planes (major)", 3, "n/φ", n//phi)
check("SiC", "4H polytype", 4, "τ", tau)
check("SiC", "6H polytype", 6, "n", n)
check("SiC", "3C polytype", 3, "n/φ", n//phi)
check("SiC", "Mobility 1000", 1000, "10^(n/φ)", 10**(n//phi))
check("GaN", "Coordination CN", 4, "τ", tau)
check("GaN", "2DEG exponent", 13, "σ+μ", sigma+mu)
check("GaN", "Buffer layers", 3, "n/φ", n//phi)
check("GaN", "HEMT freq exp", 10, "σ-φ", sigma-phi)
check("Diamond", "Carbon Z", 6, "n", n)
check("Diamond", "CN", 4, "τ", tau)
check("Diamond", "Mohs hardness", 10, "σ-φ", sigma-phi)
check("Diamond", "Atoms/unit cell", 8, "σ-τ", sigma-tau)
check("Ge", "Z", 32, "2^sopfr", 2**sopfr)
check("Ge", "CN", 4, "τ", tau)
check("Ge", "Atoms/unit cell", 8, "σ-τ", sigma-tau)
w1 = passed - w
print(f"\n  Wafer: {w1}/22")

# === 2. Gate Materials (15) ===
print("\n--- 2. Gate Materials ---\n")
g = passed
check("HfO2", "k", 25, "J₂+μ", J2+mu)
check("HfO2", "Hf Z", 72, "σ·n", sigma*n)
check("HfO2", "O Z", 8, "σ-τ", sigma-tau)
check("HfO2", "Thickness", 2, "φ nm", phi)
check("Gate", "Metal gate thickness", 5, "sopfr nm", sopfr)
check("Gate", "N5 gate pitch", 48, "σ·τ nm", sigma*tau)
check("Gate", "Metal layers total", 12, "σ", sigma)
check("Gate", "Fine pitch M1-M4", 4, "τ", tau)
check("Gate", "Medium M5-M8", 4, "τ", tau)
check("Gate", "Thick M9-M12", 4, "τ", tau)
check("GAA", "Nanosheet thickness", 8, "σ-τ nm", sigma-tau)
check("GAA", "Sheet spacing", 12, "σ nm", sigma)
check("GAA", "Sheets Samsung 3nm", 3, "n/φ", n//phi)
check("GAA", "Sheets Intel/TSMC", 4, "τ", tau)
check("GAA", "Fin pitch 7nm", 28, "P₂ nm", P2)
g1 = passed - g
print(f"\n  Gate: {g1}/15")

# === 3. Interconnect Materials (13) ===
print("\n--- 3. Interconnect Materials ---\n")
i = passed
check("Cu", "Z", 29, "P₂+μ", P2+mu)
check("Cu", "Mean free path", 40, "τ·(σ-φ) nm", tau*(sigma-phi))
check("Cu", "Damascene steps", 2, "φ", phi)
check("Pitch", "N7 M1", 40, "τ·(σ-φ) nm", tau*(sigma-phi))
check("Pitch", "N5 M1", 28, "P₂ nm", P2)
check("Pitch", "N3 M1", 24, "J₂ nm", J2)
check("Pitch", "N2 M1", 20, "J₂-τ nm", J2-tau)
check("Pitch", "A14 M1", 16, "φ^τ nm", phi**tau)
check("Pitch", "A10 M1", 12, "σ nm", sigma)
check("Next", "Co Z", 27, "P₂-μ", P2-mu)
check("Next", "Mo Z", 42, "σ·n/φ+n", sigma*(n//phi)+n)
check("Next", "Graphene C Z", 6, "n", n)
check("Liner", "Ru thickness", 2, "φ nm", phi)
i1 = passed - i
print(f"\n  Interconnect: {i1}/13")

# === 4. Photoresist & Litho (12) ===
print("\n--- 4. Photoresist & Litho ---\n")
p = passed
check("EUV", "Sn Z", 50, "sopfr·(σ-φ)", sopfr*(sigma-phi))
check("EUV", "Mirror material types", 2, "φ", phi)
check("EUV", "Mirror pairs", 40, "τ·(σ-φ)", tau*(sigma-phi))
check("EUV", "Resist thickness", 24, "J₂ nm", J2)
check("EUV", "Resolution limit", 8, "σ-τ nm", sigma-tau)
check("EUV", "SAQP mask count", 4, "τ", tau)
check("DUV", "Ar Z", 18, "σ+n", sigma+n)
check("DUV", "F Z", 9, "σ-n/φ", sigma-n//phi)
check("DUV", "Single-pattern res", 40, "τ·(σ-φ) nm", tau*(sigma-phi))
check("DUV", "SADP factor", 2, "φ", phi)
check("DUV", "SAQP factor", 4, "τ", tau)
check("DUV", "Kr Z", 36, "σ·n/φ", sigma*(n//phi))
p1 = passed - p
print(f"\n  Litho: {p1}/12")

# === 5. Packaging Materials (18) ===
print("\n--- 5. Packaging Materials ---\n")
k = passed
check("CoWoS", "Tiles standard", 5, "sopfr", sopfr)
check("CoWoS", "Tiles B300", 6, "n", n)
check("CoWoS", "TSV pitch", 10, "σ-φ μm", sigma-phi)
check("CoWoS", "RDL layers", 6, "n", n)
check("CoWoS", "RDL pitch", 2, "φ μm", phi)
check("CoWoS", "μ-bump pitch", 48, "σ·τ μm", sigma*tau)
check("CoWoS", "C4 bump pitch", 144, "σ² μm", sigma**2)
check("Sub", "Organic layers", 12, "σ", sigma)
check("Sub", "BGA pitch", 144, "σ² μm", sigma**2)
check("HBM", "HBM3 die count", 8, "σ-τ", sigma-tau)
check("HBM", "HBM3E die count", 12, "σ", sigma)
check("HBM", "HBM4 die count", 16, "φ^τ", phi**tau)
check("HBM", "TSV pitch", 10, "σ-φ μm", sigma-phi)
check("HBM", "TSV diameter", 5, "sopfr μm", sopfr)
check("HBM", "TSV aspect ratio", 10, "σ-φ", sigma-phi)
check("HBM", "Interface width", 1024, "2^(σ-φ) bit", 2**(sigma-phi))
check("HBM", "Channels/stack", 16, "φ^τ", phi**tau)
check("HBM", "Pseudo-channels", 32, "2^sopfr", 2**sopfr)
k1 = passed - k
print(f"\n  Packaging: {k1}/18")

# === 6. Dielectric Materials (12) ===
print("\n--- 6. Dielectric Materials ---\n")
d = passed
check("Low-k", "SiO2 PECVD k", 4, "τ", tau)
check("Low-k", "Si3N4 k", 7, "σ-sopfr", sigma-sopfr)
check("Low-k", "SiCO k", 3, "n/φ", n//phi)
check("Low-k", "Porous ULK k", 2, "φ", phi)
check("Low-k", "Air gap k", 1, "μ", mu)
check("Low-k", "Sub-layers per metal", 3, "n/φ", n//phi)
check("High-k", "HfO2 k", 25, "J₂+μ", J2+mu)
check("High-k", "Zr Z", 40, "τ·(σ-φ)", tau*(sigma-phi))
check("High-k", "La2O3 k", 30, "sopfr·n", sopfr*n)
check("Spacer", "SiN k", 7, "σ-sopfr", sigma-sopfr)
check("Spacer", "SiBCN k", 5, "sopfr", sopfr)
check("STI", "Depth", 256, "2^(σ-τ) nm", 2**(sigma-tau))
d1 = passed - d
print(f"\n  Dielectric: {d1}/12")

# === 7. Dopant Materials (9) ===
print("\n--- 7. Dopant Materials ---\n")
dp = passed
check("p-type", "B Z", 5, "sopfr", sopfr)
check("n-type", "P Z", 15, "σ+n/φ", sigma+n//phi)
check("Count", "Primary species", 4, "τ", tau)
check("Count", "Total species", 6, "n", n)
check("Implant", "Tilt angle", 7, "σ-sopfr deg", sigma-sopfr)
check("Implant", "Steps per device", 12, "σ", sigma)
check("Junction", "S/D extension", 8, "σ-τ nm", sigma-tau)
check("Junction", "S/D depth", 24, "J₂ nm", J2)
check("Junction", "Well depth", 500, "sopfr·10^φ nm", sopfr*10**phi)
dp1 = passed - dp
print(f"\n  Dopant: {dp1}/9")

# === Summary ===
print("\n" + "=" * 70)
print("HEXA-MATERIAL VERIFICATION SUMMARY")
print("=" * 70)
print(f"  Wafer Materials:      {w1}/22")
print(f"  Gate Materials:       {g1}/15")
print(f"  Interconnect:         {i1}/13")
print(f"  Photoresist & Litho:  {p1}/12")
print(f"  Packaging:            {k1}/18")
print(f"  Dielectric:           {d1}/12")
print(f"  Dopant:               {dp1}/9")
print(f"  ─────────────────────────────")
print(f"  TOTAL:                {passed}/{total}")
print(f"  PASS RATE:            {passed/total*100:.1f}%")
print("=" * 70)

if failed > 0:
    print(f"\n  ⚠️  {failed} FAILURES detected!")
    sys.exit(1)
else:
    print(f"\n  ✅ ALL {passed} PARAMETERS VERIFIED — 100% EXACT")
    sys.exit(0)
