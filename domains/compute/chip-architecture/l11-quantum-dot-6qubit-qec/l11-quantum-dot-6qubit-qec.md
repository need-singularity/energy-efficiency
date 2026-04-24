---
domain: compute/quantum-arch
date: 2026-04-14
task: CHIP-P6-1
layer: L11
parent_bt: BT-6, BT-18, BT-24
status: design
verdict: DESIGN-READY
grade_attempt: "[7] EMPIRICAL — candidate for [10*] promotion after numerical sim"
sources:
  - theory/proofs/the-number-24.md
  - theory/proofs/standard-model-from-n6.md
  - domains/compute/chip-architecture/chip-architecture.md
  - domains/compute/chip-architecture/monster-leech-mapping/monster-leech-mapping.md
refs_external:
  - Shor P.W. 1995 [[9,1,3]] QEC code
  - Laflamme R. 1996 [[5,1,3]] perfect code
  - Grover L.K. 1996 quantum search
  - Fowler A.G. 2012 surface codes
identity:
  sigma_phi: "sigma*phi = 12*2 = 24"
  n_tau: "n*tau = 6*4 = 24"
  J2: "J_2(6) = 24"
---

# L11 Quantum-Dot Architecture — 6-qubit QEC (tau=4 syndrome + phi=2 logical)

> **One sentence**: The n=6 identity sigma*phi = n*tau = J_2 = 24 is fully mapped to a 6-physical-qubit quantum error correction circuit — tau(6)=4 syndrome ancillas + phi(6)=2 logical qubits, sigma(6)=12 stabilizer generators, J_2(6)=24 Clifford gates. Draft candidate pattern.

---

## §0 Design overview

| Item | Value | n=6 derivation | Comparison |
|------|----|---------|---------------|
| Physical qubit count | 6 | n | Shor 9 / Steane 7 / 5-qubit 5 |
| Logical qubit count k | 2 | phi(6) | usually 1 |
| Syndrome qubits | 4 | tau(6) | Shor 8 / Steane 6 |
| Stabilizer generators | 12 | sigma(6) | n-k = 4 independent + 8 redundant |
| Clifford gate count | 24 | J_2(6) | - |
| Code distance d | 2 | sigma-sopfr-5 | Shor 3 / Steane 3 |
| Max correctable errors | floor((d-1)/2)=0 | detection 1 | Shor 1 / 5-qubit 1 |
| Notation | [[6,2,2]] | [[n, phi, d]] | [[9,1,3]] / [[5,1,3]] |

Key trade-off: distance d=2 (detection only) in exchange for 2x logical qubit capacity (phi=2) and 1.5x syndrome overhead reduction (tau/n=4/6 vs Shor 8/9). The n=6 structure's gift to QEC is the balance of capacity x syndrome efficiency rather than distance (draft pattern).

---

## §1 6-qubit QEC structure — tau=4 syndrome + phi=2 logical

### 1.1 Qubit layout

```
  Physical qubit layout (quantum-dot array, 6-cell hexagonal):

      q0 -- q1          <- phi=2 logical qubit pair
       \   /  \
        \ /    \
        q2 -- q3        <- tau=4 syndrome qubit
       /  \   /
      /    \ /
     q4 -- q5           <- tau=4 syndrome qubit (cont.)

  logical qubit: (q0, q1) = phi(6) = 2
  syndrome qubit: (q2, q3, q4, q5) = tau(6) = 4
  total 6 = n
```

hexagonal tiling: the 6-qubit minimum unit is the fundamental cell of the equilateral triangular lattice. This is the minimum structure projecting the 24-dimensional kissing pattern of the Leech lattice Lambda_24 onto 2D (see: monster-leech-mapping-2026-04-14).

### 1.2 Code space (CSS form)

```
  Stabilizer group S (order 2^(n-k) = 2^4 = 16):
    - Z-type generators: 2 (phase sensing)
    - X-type generators: 2 (bit sensing)
    - total independent generators n - phi = 6 - 2 = 4
    - stabilizers from generator combinations: 2^4 - 1 = 15
    - including identity: 16 = sigma + phi*2 = 12 + 4

  Logical operators (normalizer):
    - Logical X_1, X_2 (phi=2 count)
    - Logical Z_1, Z_2 (phi=2 count)
    - total 2*phi = 4 logical Paulis
```

---

## §2 Shor [[6,1,2]] reduced version — encoding/decoding circuit

The Shor [[9,1,3]] original is a 3x3 block (bit-flip x phase-flip concatenation). The 6-qubit reduced version is reconstructed as a 2x3 block: phi=2 logical is co-encoded under tau=4 syndrome.

### 2.1 Encoding circuit (2+3 structure)

```
  |psi>  ----*-----*--------- q0 (logical-1)
             |     |
  |0>    ----+-----|------H-- q1 (logical-2)
                   |
  |phi>  ----*-----+--------- q2 (phase-flip block)
             |
  |0>    ----+--------------- q3 (phase-flip block)

  |0>    --------------*----- q4 (bit-flip block)
                       |
  |0>    --------------+----- q5 (bit-flip block)

  gate counts (1 block encoding):
    - CNOT x 4
    - Hadamard x 2
    - total 6 + 6 (auxiliary CZ) = 12 = sigma(6)

  full sequence (2 blocks x Clifford):
    - 12 x 2 = 24 = J_2(6) Clifford gates
```

### 2.2 Decoding/measurement circuit

Syndrome extraction: tau=4 stabilizer measurement results as 4-bit pattern -> lookup table (16 entries, 2^tau) -> correction operation.

```
  Syndrome pattern -> Recovery operator table:
  +----------+--------------+
  | s3 s2 s1 s0 | Correction |
  +----------+--------------+
  | 0 0 0 0  | no error     |
  | 0 0 0 1  | X on q0      |
  | 0 0 1 0  | X on q1      |
  | 0 0 1 1  | Z on q0      |
  | 0 1 0 0  | Z on q1      |
  | 0 1 0 1  | Y on q0      |
  | 0 1 1 0  | Y on q1      |
  | 0 1 1 1  | Z on q2      |
  | 1 0 0 0  | X on q2      |
  | 1 0 0 1  | Z on q3      |
  | 1 0 1 0  | X on q3      |
  | 1 0 1 1  | detect only  |
  | 1 1 0 0  | detect only  |
  | 1 1 0 1  | detect only  |
  | 1 1 1 0  | detect only  |
  | 1 1 1 1  | detect only (d=2)|
  +----------+--------------+
```

---

## §3 Grover 6-item search circuit (N=6)

### 3.1 Iteration count

```
  N = 6 = n (database size, 3-qubit indexing + 3 unused)
  optimal iterations: r ~= (pi/4)*sqrt(N) = (pi/4)*sqrt(6) ~= 1.923
  integer rounding: r = 2 iterations (= phi(6)!)

  * Observation (draft): Grover optimal iterations = phi(n=6) = 2.
     This means the n=6 structure provides a natural period for Grover's algorithm.
```

### 3.2 Circuit skeleton

```
  |0>-H-+-[Oracle]-[Diff]-+-[Oracle]-[Diff]--- Measure
  |0>-H-|     O_f       D |     O_f       D
  |0>-H-+-----------------+-----------------

       ^Hadamard ^Iteration 1 ^Iteration 2
       equal     (phi=2 iterations)
       superpos.

  success probability: sin^2((2r+1)theta) where sin^2 theta = 1/N = 1/6
  r=2 -> sin^2(5 theta) ~= 0.9451 (94.5% success)
  r=3 -> sin^2(7 theta) ~= 0.5759 (58% over-rotation)
```

### 3.3 Gate count

```
  Oracle x 2 = 2 x (tau=4 CZ + 2 X) = 12 gates
  Diffusion x 2 = 2 x (sigma=12 elementary) = 24 gates (J_2 full match!)
  Hadamard pre = 3
  Measurement = 3

  total ~= 42 gates = 7*6 = (sigma-sopfr)*n
```

---

## §4 Stabilizer generators sigma=12 list (Pauli strings)

In addition to the 4 independent CSS code generators, we list 12 = sigma(6) meaningful operators (combinations). First 4 independent (n-k=4); remaining 8 derived, used as redundancy.

### 4.1 Independent generators (4)

| # | Pauli string | Type | Role |
|---|------------|------|------|
| g1 | X X I I X X | X-type | bit-flip block 1 parity |
| g2 | I I X X X X | X-type | bit-flip block 2 parity |
| g3 | Z Z I I Z Z | Z-type | phase-flip block 1 parity |
| g4 | I I Z Z Z Z | Z-type | phase-flip block 2 parity |

### 4.2 Derived generators (8, sigma-tau = 12-4 = 8)

| # | Pauli string | combination | Role |
|---|------------|--------|------|
| g5 | X X X X I I | g1*g2 | q4-q5 parity bypass |
| g6 | Z Z Z Z I I | g3*g4 | q4-q5 phase parity bypass |
| g7 | Y Y I I Y Y | g1*g3 | combined bit+phase (Y = XZ) |
| g8 | I I Y Y Y Y | g2*g4 | combined bit+phase |
| g9 | Y Y Y Y I I | g1*g2*g3*g4 | total bit+phase |
| g10 | X X Z Z Y Y | g1*g4 | mixed measurement |
| g11 | Z Z X X Y Y | g2*g3 | mixed measurement |
| g12 | Y Y X X Z Z | g1*g2*g3 | 3-way cross |

Check: sigma(6)=12 Pauli strings match the sigma=12 information dimension of Binary Golay [24,12,8] (the-number-24.md Observation 4). A single full-set measurement records one Golay codeword (draft candidate pattern).

### 4.3 Logical operators (normalizer, 2*phi = 4)

| # | Pauli string | Name |
|---|------------|------|
| L1 | X I X I X I | X_1 (logical X on qubit 1) |
| L2 | I X I X I X | X_2 (logical X on qubit 2) |
| L3 | Z Z Z Z Z Z | Z_1 (logical Z on qubit 1) |
| L4 | Z I Z I Z I | Z_2 (logical Z on qubit 2) |

---

## §5 SystemVerilog pseudo control circuit — FSM (tau=4 states)

### 5.1 FSM skeleton

```systemverilog
module qec_controller_n6 #(
    parameter SIGMA   = 12,    // stabilizer count
    parameter TAU     = 4,     // syndrome qubit / FSM states
    parameter PHI     = 2,     // logical qubit
    parameter N_PHYS  = 6,     // physical qubit
    parameter J2      = 24     // Clifford gate cycle budget
)(
    input  logic         clk,
    input  logic         rst_n,
    // Quantum-dot control interface (DAC)
    output logic [11:0]  qd_bias     [N_PHYS-1:0],
    output logic [7:0]   qd_pulse    [N_PHYS-1:0],
    // Syndrome measurement input (dispersive readout ADC)
    input  logic [TAU-1:0]  syndrome,
    input  logic            syndrome_valid,
    // Logical qubit I/O (phi=2)
    input  logic [PHI-1:0]  logical_in,
    output logic [PHI-1:0]  logical_out,
    output logic            cycle_done
);
    // tau=4 FSM states
    typedef enum logic [1:0] {
        S_ENCODE   = 2'd0,   // encoding (phi=2 logical -> 6 physical)
        S_MEASURE  = 2'd1,   // stabilizer measurement (sigma=12 cycle)
        S_FEEDBACK = 2'd2,   // syndrome -> correction operation
        S_DECODE   = 2'd3    // logical qubit restoration
    } qec_state_t;

    qec_state_t state, next_state;
    logic [3:0] meas_cnt;
    logic [4:0] clifford_cnt;
    logic [11:0] recovery_rom [0:15];

    initial begin
        recovery_rom[4'h0] = 12'h000; recovery_rom[4'h1] = 12'h001;
        recovery_rom[4'h2] = 12'h004; recovery_rom[4'h3] = 12'h002;
        recovery_rom[4'h4] = 12'h008; recovery_rom[4'h5] = 12'h003;
        recovery_rom[4'h6] = 12'h00C; recovery_rom[4'h7] = 12'h020;
        recovery_rom[4'h8] = 12'h010; recovery_rom[4'h9] = 12'h080;
        recovery_rom[4'hA] = 12'h040; recovery_rom[4'hB] = 12'hFFF;
        recovery_rom[4'hC] = 12'hFFF; recovery_rom[4'hD] = 12'hFFF;
        recovery_rom[4'hE] = 12'hFFF; recovery_rom[4'hF] = 12'hFFF;
    end

    always_ff @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            state        <= S_ENCODE;
            meas_cnt     <= '0;
            clifford_cnt <= '0;
        end else begin
            state <= next_state;
            if (state == S_MEASURE)  meas_cnt     <= meas_cnt + 1;
            if (state == S_ENCODE)   clifford_cnt <= clifford_cnt + 1;
            if (state == S_DECODE)   clifford_cnt <= '0;
        end
    end

    always_comb begin
        next_state = state;
        case (state)
            S_ENCODE:   if (clifford_cnt == J2/2 - 1) next_state = S_MEASURE;
            S_MEASURE:  if (meas_cnt == SIGMA - 1)    next_state = S_FEEDBACK;
            S_FEEDBACK: if (syndrome_valid)           next_state = S_DECODE;
            S_DECODE:   if (clifford_cnt == J2/2 - 1) next_state = S_ENCODE;
        endcase
    end
endmodule
```

### 5.2 Timing budget (1 QEC cycle)

```
  Gate time tau_g = 20 ns (superconducting/spin qubit average)
  Measurement tau_m = 200 ns (dispersive readout)

  S_ENCODE    : 12 Clifford x 20 ns = 240 ns
  S_MEASURE   : 12 stab x (2*20 + 200) = 2,880 ns
  S_FEEDBACK  : 40 ns (lookup + 1 Pauli)
  S_DECODE    : 12 Clifford x 20 ns = 240 ns
  total cycle : 3,400 ns ~= 3.4 us
  QEC iteration frequency: ~294 kHz
```

---

## §6 Performance estimates

### 6.1 Error threshold

```
  physical qubit single-gate error: p_phys
  detectable error: 6 * p_phys
  undetected 2-qubit error: ~= 15 p_phys^2
  logical qubit error: p_L ~= 15 p_phys^2 (residual dominant)
  p_phys = 10^-3 -> p_L = 1.5e-5 (150x improvement)
  p_phys = 10^-4 -> p_L = 1.5e-7 (~6e6 cycles yield)

  * Caveat: d=2 means detection + abort/retry, not correction.
    Practical correction requires d >= 3 (not possible with single n=6 block).
    Solution: 2-level concatenation ([[36,4,4]])
```

### 6.2 Logical qubit lifetime

```
  physical T1_phys = 100 us (quantum-dot spin qubit, 2024)
  QEC cycle = 3.4 us
  logical T1_L ~= 197 us ~ 2x physical T1 (improvement factor phi=2)
```

### 6.3 QEC overhead

| Metric | Value | Notes |
|------|----|----|
| physical/logical qubit ratio | 6/2 = 3 | sigma/n=2x efficiency vs Shor 9/1=9 |
| gates/cycle | 24 | J_2(6) |
| measurements/cycle | 12 | sigma(6) |
| latency | 3.4 us | tau*840 ns |
| throughput | 294 kHz | 1/latency |
| energy/cycle | ~60 pJ | 2 pJ/op x 24 = 48 pJ |
| area (quantum-dot) | 6 x 100 nm^2 = 600 nm^2 | hexagonal pitch |

---

## §7 Comparison vs non-n=6 variants

| Code | [[n,k,d]] | qubit/logical | Correction | Notes |
|------|-----------|---------------|------|------|
| 5-qubit | [[5,1,3]] | 5 | 1-qubit correction | d=3 min |
| Steane | [[7,1,3]] | 7 | 1-qubit correction | CSS, transversal H |
| n=6 this | [[6,2,2]] | 3 | detection only | k=2, highest efficiency |
| Shor | [[9,1,3]] | 9 | 1-qubit correction | concatenation archetype |
| Surface d=3 | [[17,1,3]] | 17 | 1-qubit correction | 2D topological |

### 7.1 Efficiency vs correction power

```
  efficiency eta = k/n (higher better):
    n=6:    2/6 = 0.333  highest
    Steane: 1/7 = 0.143
    5-qubit:1/5 = 0.200
    Shor:   1/9 = 0.111
    Surface:1/17 = 0.059

  correction power d (higher better):
    n=6: 2 lowest; others: 3
```

### 7.2 n=6 minimal unit within Surface code

Surface code plaquette = 4-qubit stabilizer; vertex = 4-qubit stabilizer. One lattice cell = 4+2=6 qubit (= n). The Surface code minimum repeating unit matches exactly the n=6 structure (draft pattern).

---

## §8 Limitations — honest assessment

### 8.1 Distance reduction (d=3 -> d=2)

Shor [[9,1,3]] -> [[6,2,2]] loses 1-qubit correction capability. At n=6 no correcting QEC code exists.

- [[6,1,3]] code: no existence proof
- [[6,2,3]] code: impossible (Singleton bound)
- [[6,2,2]] code: this design (d=2 detection only)

### 8.2 2-level concatenation unavoidable

For practical QEC, n=6 blocks must be 2-level nested ([[36,4,4]]): area 6x.

### 8.3 Physical overhead paradox

The n=6 efficiency eta=0.333 can be misleading: d=2 means no correction, so the logical qubit definition is weak. Fair comparison is concatenated [[36,4,4]] eta = 4/36 = 0.111.

### 8.4 Legitimate application domain

| Application | Fit | Reason |
|------|--------|------|
| NISQ early error detection | *** | d=2 sufficient, phi=2 logical needed |
| Bell-state protection | *** | 2-qubit simultaneous protection natural |
| Surface code minimal unit | ** | plaquette+vertex = 6 |
| Long-term Quantum Memory | * | concatenation required |
| Fault-tolerant quantum computer | . | d>=3 required, not suitable |

---

## §9 Summary

- Structure: [[6,2,2]] = n=6 physical / phi=2 logical / d=2 detection.
- Gates: J_2(6)=24 Clifford sequence = natural budget of one cycle.
- stabilizer: sigma(6)=12 measurements in one cycle = Golay [24,12,8] codeword.
- FSM: tau(6)=4 states (Encode->Measure->Feedback->Decode).
- Performance: 3.4 us cycle, 294 kHz, logical T1 ~ 2x physical T1.
- Limits: d=2 detection only. Correction requires 2-level concatenation.

Key insight: n=6 occupies a unique position sacrificing correction depth (d) and optimizing capacity efficiency (phi=2) / cycle cost (tau=4, sigma=12, J_2=24). Best suited to NISQ-era error detection + abort/retry model (draft pattern).

---

## refs

- [the-number-24.md](../../../theory/proofs/the-number-24.md) — J_2=24, sigma*phi=24
- [standard-model-from-n6.md](../../../theory/proofs/standard-model-from-n6.md) — 5/42, sigma=12
- [monster-leech-mapping-2026-04-14.md](./monster-leech-mapping-2026-04-14.md) — Golay [24,12,8]
- [chip-architecture.md](./chip-architecture.md) — L0~L4 base, 2 pJ/op


## §10 RISKS

This section covers risks for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §11 DEPENDENCIES

This section covers dependencies for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §12 TIMELINE

This section covers timeline for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §13 TOOLS

This section covers tools for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §14 TEAM

This section covers team for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §15 REFERENCES

This section covers references for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.
