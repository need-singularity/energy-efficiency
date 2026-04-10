#!/usr/bin/env python3
"""
N6 PPA (Performance, Power, Area) 모델
SM 단위부터 적산하여 "240W에 144 SM이 진짜 들어가나?" 검증
"""

# ============================================================
# 공정 파라미터 (TSMC N2 기준)
# ============================================================
PROCESS = "TSMC_N2"
CLOCK_GHZ = 2.0          # GPU 클럭 (보수적)
CPU_CLOCK_GHZ = 3.5      # CPU 클럭

# N2 공정 단위 비용 (공개 데이터 + 추정)
# Power per unit (mW)
PW_FP32_UNIT  = 5.0      # mW per FP32 ALU
PW_TC_UNIT    = 150.0    # mW per Tensor Core
PW_RF_PER_KB  = 1.0      # mW per KB register file
PW_SRAM_PER_KB = 0.8     # mW per KB SRAM (L1/Shared)
PW_L2_PER_MB  = 200.0    # mW per MB L2
PW_HBM_STACK  = 5000.0   # mW per HBM stack (PHY + controller)
PW_CPU_PCORE  = 3000.0   # mW per P-core
PW_CPU_ECORE  = 800.0    # mW per E-core
PW_NPU_CORE   = 500.0    # mW per NPU core
PW_IO_FIXED   = 15000.0  # mW I/O + misc fixed
PW_MEDIA      = 5000.0   # mW media engine

# Area per unit (mm²)
AR_FP32_UNIT  = 0.008    # mm² per FP32 ALU
AR_TC_UNIT    = 0.25     # mm² per Tensor Core
AR_RF_PER_KB  = 0.001    # mm² per KB register file
AR_SRAM_PER_KB = 0.0005  # mm² per KB SRAM
AR_L2_PER_MB  = 0.8      # mm² per MB L2
AR_HBM_PHY    = 5.0      # mm² per HBM PHY (on logic die)
AR_CPU_PCORE  = 3.0       # mm² per P-core
AR_CPU_ECORE  = 1.0       # mm² per E-core
AR_NPU_CORE   = 1.5       # mm² per NPU core
AR_IO_FIXED   = 50.0      # mm² I/O + misc
AR_MEDIA      = 10.0      # mm² media engine

print("=" * 70)
print("N6 PPA MODEL — SM부터 적산")
print("=" * 70)

# ============================================================
# Part 1: GPU SM (1개)
# ============================================================
print("\n--- GPU SM (1개) ---\n")

SM_FP32 = 128
SM_FP64 = 64
SM_TC = 4
SM_RF_KB = 576      # J₂² KB
SM_SRAM_KB = 256    # 2^(σ-τ) KB

sm_perf_fp32 = SM_FP32 * CLOCK_GHZ * 2  # FMA = 2 ops
sm_perf_fp16_tc = SM_TC * (8*8*8) * CLOCK_GHZ * 2

sm_power = (
    SM_FP32 * PW_FP32_UNIT +
    SM_TC * PW_TC_UNIT +
    SM_RF_KB * PW_RF_PER_KB +
    SM_SRAM_KB * PW_SRAM_PER_KB
)

sm_area = (
    SM_FP32 * AR_FP32_UNIT +
    SM_TC * AR_TC_UNIT +
    SM_RF_KB * AR_RF_PER_KB +
    SM_SRAM_KB * AR_SRAM_PER_KB
)

print(f"  Performance:")
print(f"    FP32:    {SM_FP32} × {CLOCK_GHZ} GHz × 2 = {sm_perf_fp32:.0f} GFLOPS")
print(f"    FP16 TC: {SM_TC} × 8×8×8 × {CLOCK_GHZ} GHz × 2 = {sm_perf_fp16_tc:.0f} GFLOPS")
print(f"  Power:     {sm_power:.0f} mW = {sm_power/1000:.2f} W")
print(f"  Area:      {sm_area:.2f} mm²")

# ============================================================
# Part 2: GPU 전체 (144 SM)
# ============================================================
print("\n--- GPU Array (σ²=144 SMs) ---\n")

NUM_SM = 144

gpu_perf_fp32 = sm_perf_fp32 * NUM_SM
gpu_perf_fp16_tc = sm_perf_fp16_tc * NUM_SM
gpu_power = sm_power * NUM_SM
gpu_area = sm_area * NUM_SM

print(f"  Performance:")
print(f"    FP32:    {gpu_perf_fp32:.0f} GFLOPS = {gpu_perf_fp32/1000:.1f} TFLOPS")
print(f"    FP16 TC: {gpu_perf_fp16_tc:.0f} GFLOPS = {gpu_perf_fp16_tc/1000:.1f} TFLOPS")
print(f"  Power:     {gpu_power:.0f} mW = {gpu_power/1000:.1f} W")
print(f"  Area:      {gpu_area:.1f} mm²")

# ============================================================
# Part 3: CPU Cluster (8P + 4E)
# ============================================================
print("\n--- CPU Cluster (σ-τ=8 P + τ=4 E) ---\n")

P_CORES = 8
E_CORES = 4
L2_P_MB = 48    # σ·τ MB
L2_E_MB = 4     # τ MB

cpu_power = (
    P_CORES * PW_CPU_PCORE +
    E_CORES * PW_CPU_ECORE +
    L2_P_MB * PW_L2_PER_MB +
    L2_E_MB * PW_L2_PER_MB
)
cpu_area = (
    P_CORES * AR_CPU_PCORE +
    E_CORES * AR_CPU_ECORE +
    L2_P_MB * AR_L2_PER_MB +
    L2_E_MB * AR_L2_PER_MB
)

print(f"  P-cores: {P_CORES} × {PW_CPU_PCORE/1000:.1f}W = {P_CORES*PW_CPU_PCORE/1000:.1f}W")
print(f"  E-cores: {E_CORES} × {PW_CPU_ECORE/1000:.1f}W = {E_CORES*PW_CPU_ECORE/1000:.1f}W")
print(f"  L2 P:    {L2_P_MB}MB × {PW_L2_PER_MB/1000:.1f}W/MB = {L2_P_MB*PW_L2_PER_MB/1000:.1f}W")
print(f"  L2 E:    {L2_E_MB}MB × {PW_L2_PER_MB/1000:.1f}W/MB = {L2_E_MB*PW_L2_PER_MB/1000:.1f}W")
print(f"  Power:   {cpu_power/1000:.1f} W")
print(f"  Area:    {cpu_area:.1f} mm²")

# ============================================================
# Part 4: NPU (24 cores)
# ============================================================
print("\n--- NPU Array (J₂=24 cores) ---\n")

NPU_CORES = 24
npu_power = NPU_CORES * PW_NPU_CORE
npu_area = NPU_CORES * AR_NPU_CORE

print(f"  Power: {NPU_CORES} × {PW_NPU_CORE/1000:.1f}W = {npu_power/1000:.1f} W")
print(f"  Area:  {NPU_CORES} × {AR_NPU_CORE}mm² = {npu_area:.1f} mm²")

# ============================================================
# Part 5: Memory (HBM + SLC)
# ============================================================
print("\n--- Memory (σ-τ=8 HBM + σ·J₂=288MB SLC) ---\n")

HBM_STACKS = 8
SLC_MB = 288

mem_power = (
    HBM_STACKS * PW_HBM_STACK +
    SLC_MB * PW_SRAM_PER_KB * 1024 / 1000  # convert KB rate to MB
)
# SLC power correction: SRAM at 288MB is huge
slc_power = SLC_MB * 0.8 * 1000  # ~0.8 W/MB for large SRAM
mem_power = HBM_STACKS * PW_HBM_STACK + slc_power

mem_area = (
    HBM_STACKS * AR_HBM_PHY +
    SLC_MB * AR_SRAM_PER_KB * 1024  # convert KB rate to MB
)
slc_area = SLC_MB * 0.5  # ~0.5 mm²/MB for large SRAM
mem_area = HBM_STACKS * AR_HBM_PHY + slc_area

print(f"  HBM:   {HBM_STACKS} stacks × {PW_HBM_STACK/1000:.1f}W = {HBM_STACKS*PW_HBM_STACK/1000:.1f}W")
print(f"  SLC:   {SLC_MB}MB × ~0.8W/MB = {slc_power/1000:.1f}W")
print(f"  Power: {mem_power/1000:.1f} W")
print(f"  Area:  HBM PHY {HBM_STACKS*AR_HBM_PHY:.0f}mm² + SLC {slc_area:.0f}mm² = {mem_area:.0f} mm²")

# ============================================================
# Part 6: I/O + Media
# ============================================================
print("\n--- I/O + Media ---\n")

io_power = PW_IO_FIXED + PW_MEDIA
io_area = AR_IO_FIXED + AR_MEDIA

print(f"  I/O:    {PW_IO_FIXED/1000:.0f}W")
print(f"  Media:  {PW_MEDIA/1000:.0f}W")
print(f"  Power:  {io_power/1000:.0f} W")
print(f"  Area:   {io_area:.0f} mm²")

# ============================================================
# TOTAL
# ============================================================
print("\n" + "=" * 70)
print("TOTAL SoC PPA")
print("=" * 70)

total_power = gpu_power + cpu_power + npu_power + mem_power + io_power
total_area = gpu_area + cpu_area + npu_area + mem_area + io_area

print(f"\n  ┌──────────────┬──────────┬──────────┐")
print(f"  │   Component  │  Power   │   Area   │")
print(f"  ├──────────────┼──────────┼──────────┤")
print(f"  │ GPU (144 SM) │ {gpu_power/1000:>6.1f} W │ {gpu_area:>6.1f} mm²│")
print(f"  │ CPU (8P+4E)  │ {cpu_power/1000:>6.1f} W │ {cpu_area:>6.1f} mm²│")
print(f"  │ NPU (24)     │ {npu_power/1000:>6.1f} W │ {npu_area:>6.1f} mm²│")
print(f"  │ Memory/SLC   │ {mem_power/1000:>6.1f} W │ {mem_area:>6.0f} mm²│")
print(f"  │ I/O + Media  │ {io_power/1000:>6.1f} W │ {io_area:>6.0f} mm²│")
print(f"  ├──────────────┼──────────┼──────────┤")
print(f"  │ TOTAL        │ {total_power/1000:>6.1f} W │ {total_area:>6.0f} mm²│")
print(f"  └──────────────┴──────────┴──────────┘")

print(f"\n  Target TDP:    240W (J₂·(σ-φ))")
print(f"  Actual Power:  {total_power/1000:.1f}W")
print(f"  Delta:         {total_power/1000 - 240:+.1f}W")

print(f"\n  Target Area:   ~800 mm² (reticle limit)")
print(f"  Actual Area:   {total_area:.0f} mm²")
print(f"  Delta:         {total_area - 800:+.0f} mm²")

# Feasibility
print(f"\n  ┌────────────────────────────────────────────┐")
power_ok = total_power/1000 <= 300  # 25% margin
area_ok = total_area <= 850
if power_ok and area_ok:
    print(f"  │  ✅ FEASIBLE — 전력/면적 모두 범위 내      │")
elif power_ok:
    print(f"  │  ⚠️  면적 초과 — SM 수 줄이거나 다이 확장  │")
elif area_ok:
    print(f"  │  ⚠️  전력 초과 — 클럭/SM 수 조정 필요      │")
else:
    print(f"  │  ❌ INFEASIBLE — 전력+면적 모두 초과        │")
print(f"  └────────────────────────────────────────────┘")

# Performance summary
print(f"\n  Performance Summary:")
print(f"    FP32:        {gpu_perf_fp32/1000:.1f} TFLOPS")
print(f"    FP16 (TC):   {gpu_perf_fp16_tc/1000:.1f} TFLOPS")
print(f"    NPU INT8:    ~{NPU_CORES * 256 * CLOCK_GHZ * 2 / 1000:.0f} TOPS")
print(f"    HBM:         {HBM_STACKS * 36} GB, ~{HBM_STACKS * 500} GB/s")
print(f"    Perf/W FP32: {gpu_perf_fp32/1000/(total_power/1000):.2f} TFLOPS/W")
print(f"    Perf/W FP16: {gpu_perf_fp16_tc/1000/(total_power/1000):.2f} TFLOPS/W")

# vs H100
print(f"\n  vs NVIDIA H100:")
print(f"    {'':>20} {'HEXA-1':>10} {'H100':>10} {'비교':>10}")
print(f"    {'FP32 TFLOPS':>20} {gpu_perf_fp32/1000:>10.1f} {66.9:>10.1f} {'':>10}")
print(f"    {'FP16 TC TFLOPS':>20} {gpu_perf_fp16_tc/1000:>10.1f} {989.5:>10.1f} {'':>10}")
print(f"    {'TDP (W)':>20} {total_power/1000:>10.1f} {700.0:>10.1f} {'':>10}")
print(f"    {'HBM (GB)':>20} {HBM_STACKS*36:>10} {80:>10} {'':>10}")
print(f"    {'BW (GB/s)':>20} {HBM_STACKS*500:>10} {3350:>10} {'':>10}")
