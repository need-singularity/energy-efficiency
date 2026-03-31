#!/usr/bin/env python3
"""HEXA-1 Unified SoC 아키텍처 수학 검증 — 전수 검사"""

import sys
import math

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
print("HEXA-1 UNIFIED SoC VERIFICATION")
print("=" * 70)

# === 1. CPU Cluster (Section 2) ===
print("\n--- 1. CPU Cluster (Section 2) ---\n")
s = passed
check("CPU", "Total cores", 12, "σ", sigma)
check("CPU", "P-cores", 8, "σ-τ", sigma-tau)
check("CPU", "E-cores", 4, "τ", tau)
check("CPU", "P-core ROB entries", 256, "2^(σ-τ)", 2**(sigma-tau))
check("CPU", "P-core decode width", 5, "sopfr", sopfr)
check("CPU", "E-core decode width", 3, "n/φ", n//phi)
check("CPU", "L1I per core (KB)", 64, "2^n", 2**n)
check("CPU", "L1D per core (KB)", 64, "2^n", 2**n)
check("CPU", "L2 per P-cluster (MB)", 48, "σ·τ", sigma*tau)
check("CPU", "L2 per E-cluster (MB)", 4, "τ", tau)
check("CPU", "SLC (MB)", 288, "σ·J₂", sigma*J2)
s1 = passed - s
print(f"\n  CPU Cluster: {s1}/11")

# === 2. GPU Array (Section 3) ===
print("\n--- 2. GPU Array (Section 3) ---\n")
s = passed
check("GPU", "Total SMs", 144, "σ²", sigma**2)
check("GPU", "GPCs", 12, "σ", sigma)
check("GPU", "SMs per GPC", 12, "σ", sigma)
check("GPU", "TPCs per GPC", 6, "n", n)
check("GPU", "SMs per TPC", 2, "φ", phi)
check("GPU", "CUDA cores per SM", 128, "2^(σ-sopfr)", 2**(sigma-sopfr))
check("GPU", "Tensor Cores per SM", 4, "τ", tau)
check("GPU", "Register file per SM (KB)", 576, "J₂²", J2**2)
check("GPU", "L1/Shared per SM (KB)", 256, "2^(σ-τ)", 2**(sigma-tau))
check("GPU", "Warp size", 32, "2^sopfr", 2**sopfr)
check("GPU", "Max warps per SM", 64, "2^n", 2**n)
check("GPU", "Total CUDA cores", 18432, "σ²·2^(σ-sopfr)", sigma**2 * 2**(sigma-sopfr))
check("GPU", "Total Tensor Cores", 576, "σ²·τ = J₂²", sigma**2 * tau)
s1 = passed - s
print(f"\n  GPU Array: {s1}/13")

# === 3. NPU Array (Section 4) ===
print("\n--- 3. NPU Array (Section 4) ---\n")
s = passed
check("NPU", "Neural cores", 24, "J₂", J2)
check("NPU", "MAC units per core", 256, "2^(σ-τ)", 2**(sigma-tau))
check("NPU", "Total MACs", 6144, "J₂·2^(σ-τ)", J2 * 2**(sigma-tau))
check("NPU", "Local SRAM per core (KB)", 64, "2^n", 2**n)
check("NPU", "Supported precisions", 4, "τ", tau)
check("NPU", "Banks", 5, "sopfr", sopfr)
s1 = passed - s
print(f"\n  NPU Array: {s1}/6")

# === 4. Unified Memory (Section 5) ===
print("\n--- 4. Unified Memory (Section 5) ---\n")
s = passed
check("MEM", "SLC (MB)", 288, "σ·J₂", sigma*J2)
check("MEM", "SLC banks", 12, "σ", sigma)
check("MEM", "SLC per bank (MB)", 24, "J₂", J2)
check("MEM", "Memory controllers", 8, "σ-τ", sigma-tau)
check("MEM", "HBM interface width (bits)", 2048, "2^(σ-μ)", 2**(sigma-mu))
check("MEM", "HBM stacks", 8, "σ-τ", sigma-tau)
check("MEM", "QoS priority levels", 4, "τ", tau)
s1 = passed - s
print(f"\n  Memory: {s1}/7")

# === 5. Media Engine (Section 6) ===
print("\n--- 5. Media Engine (Section 6) ---\n")
s = passed
check("Media", "Video encode engines", 6, "n", n)
check("Media", "Video decode engines", 6, "n", n)
check("Media", "Display outputs", 4, "τ", tau)
check("Media", "Max resolution (K)", 8, "σ-τ", sigma-tau)
check("Media", "ProRes engines", 2, "φ", phi)
check("Media", "Max framerate", 120, "σ·(σ-φ)", sigma*(sigma-phi))
check("Media", "Color depth (bits)", 12, "σ", sigma)
check("Media", "Audio sample rate (kHz)", 48, "σ·τ", sigma*tau)
check("Media", "Audio channels", 24, "J₂", J2)
s1 = passed - s
print(f"\n  Media Engine: {s1}/9")

# === 6. I/O Hub (Section 7) ===
print("\n--- 6. I/O Hub (Section 7) ---\n")
s = passed
check("IO", "Thunderbolt ports", 4, "τ", tau)
check("IO", "TB speed (Gbps)", 48, "σ·τ", sigma*tau)
check("IO", "PCIe lanes", 16, "φ^τ", phi**tau)
check("IO", "PCIe GT/s", 128, "2^(σ-sopfr)", 2**(sigma-sopfr))
check("IO", "USB4 ports", 6, "n", n)
check("IO", "WiFi band (GHz)", 6, "n", n)
check("IO", "WiFi speed (Gbps)", 24, "σ·φ", sigma*phi)
check("IO", "Ethernet (Gbps)", 120, "σ·(σ-φ)", sigma*(sigma-phi))
check("IO", "UCIe speed (GT/s)", 48, "σ·τ", sigma*tau)
check("IO", "UCIe lanes", 64, "2^n", 2**n)
check("IO", "Total controllers", 8, "σ-τ", sigma-tau)
s1 = passed - s
print(f"\n  I/O Hub: {s1}/11")

# === 7. Optical Interconnect (Section 7.1) ===
print("\n--- 7. Optical Interconnect (Section 7.1) ---\n")
s = passed
check("Optic", "WDM wavelengths", 12, "σ", sigma)
check("Optic", "Waveguides per D2D link", 4, "τ", tau)
check("Optic", "D2D optical channels", 48, "σ·τ", sigma*tau)
check("Optic", "D2D modulators", 48, "σ·τ", sigma*tau)
check("Optic", "C2C modulators", 96, "σ·(σ-τ)", sigma*(sigma-tau))
check("Optic", "Lasers", 12, "σ", sigma)
check("Optic", "C2C fiber pairs per link", 12, "σ", sigma)
check("Optic", "C2C bidirectional links", 8, "σ-τ", sigma-tau)
check("Optic", "Per wavelength Gbps", 32, "2^sopfr", 2**sopfr)
check("Optic", "Switch ports", 144, "σ²", sigma**2)
check("Optic", "Pod chip count", 72, "σ·n", sigma*n)
check("Optic", "Pod max latency (ns)", 24, "J₂", J2)
s1 = passed - s
print(f"\n  Optical Interconnect: {s1}/12")

# === 8. Power Architecture (Section 8) ===
print("\n--- 8. Power Architecture (Section 8) ---\n")
s = passed
check("PWR", "TDP (W)", 240, "J₂·(σ-φ)", J2*(sigma-phi))
check("PWR", "GPU power (W)", 120, "σ·(σ-φ)", sigma*(sigma-phi))
check("PWR", "CPU power (W)", 80, "φ^τ·sopfr", phi**tau * sopfr)
check("PWR", "NPU+IO power (W)", 40, "τ·(σ-φ)", tau*(sigma-phi))
check("PWR", "VRM phases", 24, "J₂", J2)
check("PWR", "Power states (S)", 5, "sopfr", sopfr)
check("PWR", "Thermal zones", 12, "σ", sigma)
check("PWR", "Max Tj (°C)", 120, "σ·(σ-φ)", sigma*(sigma-phi))
s1 = passed - s
print(f"\n  Power: {s1}/8")

# === 9. Process Technology (Section 9) ===
print("\n--- 9. Process Technology (Section 9) ---\n")
s = passed
check("Proc", "Gate pitch (nm)", 48, "σ·τ", sigma*tau)
check("Proc", "Metal pitch (nm)", 28, "P₂", P2)
check("Proc", "Metal layers", 12, "σ", sigma)
check("Proc", "Transistor count (B)", 144, "σ²", sigma**2)
check("Proc", "Interposer tiles", 5, "sopfr", sopfr)
s1 = passed - s
print(f"\n  Process: {s1}/5")

# === 10. Clock Architecture (Section 14.1) ===
print("\n--- 10. Clock & DVFS (Section 14.1) ---\n")
s = passed
check("CLK", "Clock domains", 12, "σ", sigma)
check("CLK", "PLLs", 6, "n", n)
check("CLK", "CPU P-core boost (GHz)", 3, "n/φ", n//phi)
check("CLK", "CPU E-core max (GHz)", 2, "φ", phi)
check("CLK", "GPU core clock (GHz)", 2, "φ", phi)
check("CLK", "NPU clock (GHz)", 2, "φ", phi)
check("CLK", "Fabric/NoC boost (GHz)", 3, "n/φ", n//phi)
check("CLK", "Media base (GHz)", 1, "R(6)", R)
check("CLK", "SerDes (GHz/lane)", 10, "sopfr·φ", sopfr*phi)
check("CLK", "DVFS operating points", 10, "σ-φ", sigma-phi)
check("CLK", "S-states", 5, "sopfr", sopfr)
check("CLK", "C-states", 4, "τ", tau)
check("CLK", "Idle entry delay (μs)", 4, "τ", tau)
check("CLK", "Wakeup delay (μs)", 2, "φ", phi)
s1 = passed - s
print(f"\n  Clock & DVFS: {s1}/14")

# === 11. Boot Sequence (Section 14.2) ===
print("\n--- 11. Boot Sequence (Section 14.2) ---\n")
s = passed
check("Boot", "Boot phases", 6, "n", n)
check("Boot", "Total boot time (ms)", 64, "2^n", 2**n)
check("Boot", "Phase 0 time (ms)", 4, "τ", tau)
check("Boot", "Phase 1 time (ms)", 12, "σ", sigma)
check("Boot", "Phase 2 time (ms)", 24, "J₂", J2)
check("Boot", "Phase 3 time (ms)", 10, "σ-φ", sigma-phi)
check("Boot", "Phase 4 time (ms)", 8, "σ-τ", sigma-tau)
check("Boot", "Phase 5 time (ms)", 6, "n", n)
check("Boot", "Secure ROM (KB)", 8, "σ-τ", sigma-tau)
check("Boot", "SPI initial clock (MHz)", 12, "σ", sigma)
check("Boot", "SPI fast clock (MHz)", 48, "σ·τ", sigma*tau)
check("Boot", "Firmware size (KB)", 4096, "2^σ", 2**sigma)
check("Boot", "Training pattern (bits)", 64, "2^n", 2**n)
s1 = passed - s
print(f"\n  Boot: {s1}/13")

# === 12. DMA & Data Movement (Section 14.3) ===
print("\n--- 12. DMA & Data Movement (Section 14.3) ---\n")
s = passed
check("DMA", "DMA channels", 8, "σ-τ", sigma-tau)
check("DMA", "Descriptor ring entries", 64, "2^n", 2**n)
check("DMA", "Descriptor size (bytes)", 28, "P₂", P2)
s1 = passed - s
print(f"\n  DMA: {s1}/3")

# === 13. Debug & RAS (Section 14.4) ===
print("\n--- 13. Debug & RAS (Section 14.4) ---\n")
s = passed
check("DBG", "HW perf counters", 144, "σ²", sigma**2)
check("DBG", "CPU pipeline counters", 24, "J₂", J2)
check("DBG", "GPU SM counters", 48, "σ·τ", sigma*tau)
check("DBG", "NPU counters", 24, "J₂", J2)
check("DBG", "Memory/Fabric counters", 24, "J₂", J2)
check("DBG", "I/O counters", 24, "J₂", J2)
check("DBG", "Counter width (bits)", 48, "σ·τ", sigma*tau)
check("DBG", "Simultaneous events", 8, "σ-τ", sigma-tau)
check("DBG", "ETM per CPU core", 12, "σ", sigma)
check("DBG", "GPU trace per GPC", 12, "σ", sigma)
check("DBG", "Trace port width (bits)", 20, "sopfr·τ", sopfr*tau)
check("DBG", "Trace buffer per cluster (MB)", 24, "J₂", J2)
check("DBG", "Total trace SRAM (MB)", 96, "σ·(σ-τ)", sigma*(sigma-tau))
check("DBG", "Thermal sensors", 12, "σ", sigma)
check("DBG", "Thermal sampling (ms)", 6, "n", n)
check("DBG", "Throttle threshold (°C)", 120, "σ·(σ-φ)", sigma*(sigma-phi))
check("DBG", "Shutdown threshold (°C)", 144, "σ²", sigma**2)
check("DBG", "CPU watchdogs", 12, "σ", sigma)
check("DBG", "GPU watchdogs", 12, "σ", sigma)
check("DBG", "Error inject registers", 8, "σ-τ", sigma-tau)
check("DBG", "Debug modules", 12, "σ", sigma)
check("DBG", "JTAG clock (MHz)", 12, "σ", sigma)
s1 = passed - s
print(f"\n  Debug & RAS: {s1}/22")

# === 14. Security Engine (Section 15) ===
print("\n--- 14. Security Engine (Section 15) ---\n")
s = passed
check("SEC", "AES key (bits)", 256, "2^(σ-τ)", 2**(sigma-tau))
check("SEC", "SHA hash (bits)", 384, "σ·2^sopfr", sigma * 2**sopfr)
check("SEC", "ECC curve P-384", 384, "σ·2^sopfr", sigma * 2**sopfr)
check("SEC", "RSA key (bits)", 4096, "2^σ", 2**sigma)
check("SEC", "Secure Boot ROM (bytes)", 4096, "2^σ", 2**sigma)
check("SEC", "Secure SRAM (KB)", 256, "2^(σ-τ)", 2**(sigma-tau))
check("SEC", "Key slots", 6, "n", n)
check("SEC", "HRNG entropy sources", 6, "n", n)
check("SEC", "Tamper detect sensors", 12, "σ", sigma)
check("SEC", "Mailbox priorities", 4, "τ", tau)
check("SEC", "Secure memory partitions", 6, "n", n)
check("SEC", "Secure IRQ channels", 8, "σ-τ", sigma-tau)
check("SEC", "AES block (bits)", 128, "2^(σ-sopfr)", 2**(sigma-sopfr))
check("SEC", "SHA-384 block (bits)", 1024, "2^(σ-φ)", 2**(sigma-phi))
check("SEC", "SHA-384 word (bits)", 64, "2^n", 2**n)
check("SEC", "SHA-384 rounds", 80, "φ^τ·sopfr", phi**tau * sopfr)
check("SEC", "ECC security strength (bits)", 192, "σ·φ^τ", sigma * phi**tau)
check("SEC", "RSA security strength (bits)", 144, "σ²", sigma**2)
check("SEC", "Boot chain stages", 4, "τ", tau)
s1 = passed - s
print(f"\n  Security: {s1}/19")

# === 15. Cache Coherency (Section 17) ===
print("\n--- 15. Cache Coherency (Section 17) ---\n")
s = passed
check("COH", "Coherency states", 6, "n", n)
check("COH", "Cache line (bytes)", 64, "2^n", 2**n)
check("COH", "Directory banks", 12, "σ", sigma)
check("COH", "Coarse bitmap width (bits)", 12, "σ", sigma)
check("COH", "Owner ID bits", 8, "σ-τ", sigma-tau)
check("COH", "State encoding bits", 3, "ceil(log₂(n))", math.ceil(math.log2(n)))
check("COH", "Snoop filter sets", 4096, "2^σ", 2**sigma)
check("COH", "Max agents", 180, "σ+σ²+J₂", sigma + sigma**2 + J2)
check("COH", "Coherency domains", 2, "φ", phi)
check("COH", "QoS levels", 4, "τ", tau)
s1 = passed - s
print(f"\n  Coherency: {s1}/10")

# === 16. Virtual Memory & TLB (Section 18) ===
print("\n--- 16. Virtual Memory & TLB (Section 18) ---\n")
s = passed
check("VM", "VA width (bits)", 48, "σ·τ", sigma*tau)
check("VM", "PA width (bits)", 48, "σ·τ", sigma*tau)
check("VM", "Base page (KB)", 4, "2^σ / 1024", 2**sigma // 1024)
check("VM", "Page table levels", 4, "τ", tau)
check("VM", "Page offset bits", 12, "σ", sigma)
check("VM", "PTE permission bits", 6, "n", n)
check("VM", "L1 ITLB entries", 256, "2^(σ-τ)", 2**(sigma-tau))
check("VM", "L1 DTLB entries", 256, "2^(σ-τ)", 2**(sigma-tau))
check("VM", "L2 TLB entries", 4096, "2^σ", 2**sigma)
check("VM", "Huge TLB entries", 64, "2^n", 2**n)
check("VM", "GPU L1 TLB entries", 256, "2^(σ-τ)", 2**(sigma-tau))
check("VM", "GPU L2 TLB entries", 4096, "2^σ", 2**sigma)
check("VM", "IOMMU TLB entries", 4096, "2^σ", 2**sigma)
check("VM", "IOMMU stream IDs", 256, "2^(σ-τ)", 2**(sigma-tau))
check("VM", "TLB associativity", 8, "σ-τ", sigma-tau)
s1 = passed - s
print(f"\n  VM & TLB: {s1}/15")

# === 17. Multi-Chip Scaling (Section 16) ===
print("\n--- 17. Multi-Chip Scaling (Section 16) ---\n")
s = passed
check("SCALE", "Duo chips", 2, "φ", phi)
check("SCALE", "Quad chips", 4, "τ = φ²", tau)
check("SCALE", "Pod chips", 72, "σ·n", sigma*n)
check("SCALE", "Rack chips", 144, "σ²", sigma**2)
check("SCALE", "Pod rows", 12, "σ", sigma)
check("SCALE", "Pod columns", 6, "n", n)
check("SCALE", "C2C links per chip", 8, "σ-τ", sigma-tau)
check("SCALE", "Quad mesh links used", 3, "n/φ", n//phi)
check("SCALE", "D2D optical channels", 48, "σ·τ", sigma*tau)
check("SCALE", "Rack total SMs", 20736, "σ⁴", sigma**4)
s1 = passed - s
print(f"\n  Multi-Chip: {s1}/10")

# === 18. SKU Variants (Section 10) ===
print("\n--- 18. SKU Variants (Section 10) ---\n")
s = passed
# Ultra
check("SKU", "Ultra GPU SMs", 144, "σ²", sigma**2)
check("SKU", "Ultra NPU", 24, "J₂", J2)
check("SKU", "Ultra Memory (GB)", 288, "σ·J₂", sigma*J2)
check("SKU", "Ultra TDP (W)", 240, "J₂·(σ-φ)", J2*(sigma-phi))
# Max
check("SKU", "Max GPU SMs", 72, "σ²/φ", sigma**2 // phi)
check("SKU", "Max NPU", 12, "σ", sigma)
# Pro
check("SKU", "Pro GPU SMs", 48, "σ·τ", sigma*tau)
check("SKU", "Pro NPU", 8, "σ-τ", sigma-tau)
# Base
check("SKU", "Base GPU SMs", 24, "J₂", J2)
check("SKU", "Base NPU", 6, "n", n)
check("SKU", "Base TDP (W)", 40, "τ·(σ-φ)", tau*(sigma-phi))
# Air
check("SKU", "Air GPU SMs", 12, "σ", sigma)
check("SKU", "Air NPU", 4, "τ", tau)
# Mobile
check("SKU", "Mobile GPU SMs", 6, "n", n)
check("SKU", "Mobile Memory (GB)", 12, "σ", sigma)
# Phone
check("SKU", "Phone CPU cores", 4, "τ", tau)
check("SKU", "Phone GPU SMs", 4, "τ", tau)
check("SKU", "Phone NPU", 3, "n/φ", n//phi)
check("SKU", "Phone Memory (GB)", 8, "σ-τ", sigma-tau)
check("SKU", "Phone TDP (W)", 5, "sopfr", sopfr)
# Watch
check("SKU", "Watch CPU cores", 2, "φ", phi)
check("SKU", "Watch GPU SMs", 2, "φ", phi)
check("SKU", "Watch NPU", 1, "μ", mu)
check("SKU", "Watch Memory (GB)", 4, "τ", tau)
check("SKU", "Watch TDP (W)", 1, "μ", mu)
# IoT
check("SKU", "IoT CPU cores", 1, "μ", mu)
check("SKU", "IoT GPU SMs", 1, "μ", mu)
check("SKU", "IoT NPU", 1, "μ", mu)
check("SKU", "IoT Memory (GB)", 2, "φ", phi)
s1 = passed - s
print(f"\n  SKU Variants: {s1}/28")

# === 19. Software Stack (Section 11) ===
print("\n--- 19. Software Stack (Section 11) ---\n")
s = passed
check("SW", "SIMD width", 8, "σ-τ", sigma-tau)
check("SW", "QoS priority levels", 4, "τ", tau)
check("SW", "Thermal zones managed", 12, "σ", sigma)
check("SW", "Page size (bytes)", 4096, "2^σ", 2**sigma)
s1 = passed - s
print(f"\n  Software: {s1}/4")

# === Summary ===
print("\n" + "=" * 70)
print("HEXA-1 UNIFIED SoC VERIFICATION SUMMARY")
print("=" * 70)

sections = [
    ("CPU Cluster", 11), ("GPU Array", 13), ("NPU Array", 6),
    ("Memory", 7), ("Media Engine", 9), ("I/O Hub", 11),
    ("Optical Interconnect", 12), ("Power", 8), ("Process", 5),
    ("Clock & DVFS", 14), ("Boot Sequence", 13), ("DMA", 3),
    ("Debug & RAS", 22), ("Security Engine", 19),
    ("Cache Coherency", 10), ("VM & TLB", 15),
    ("Multi-Chip Scaling", 10), ("SKU Variants", 28),
    ("Software Stack", 4),
]

# Recount from above — we just print global totals
print(f"  TOTAL:  {passed}/{total}")
print(f"  PASS RATE: {passed/total*100:.1f}%")
print("=" * 70)

if failed > 0:
    print(f"\n  ⚠️  {failed} FAILURES detected!")
    sys.exit(1)
else:
    print(f"\n  ✅ ALL {passed} PARAMETERS VERIFIED — 100% EXACT")
    sys.exit(0)
