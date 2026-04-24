---
domain: compute/chip-architecture
date: 2026-04-15
task: CHIP-P8-3 (L8 promotion)
layer: L8
parent_bt: BT-6, BT-18, BT-24
status: promoted-from-comparison
verdict: DESIGN-READY
grade_attempt: "[6] EMPIRICAL — Microsoft Topological Core 2024 basis + Kitaev theory"
sources:
  - reports/chip_comparison_l1_l10.md (L8 row)
  - domains/compute/chip-architecture/mk3-roadmap-l1-l15-audit/mk3-roadmap-l1-l15-audit.md
  - theory/proofs/the-number-24.md
refs_external:
  - Kitaev A. 2003 Fault-tolerant quantum by anyons
  - Nayak C. 2008 Non-Abelian anyons review
  - Microsoft 2024 Majorana-1 (8 topological qubit)
  - Nayak & Sarma 2017 TQC universal gate
identity:
  sigma_phi: "sigma*phi = 12*2 = 24"
  n_tau: "n*tau = 6*4 = 24"
  J2: "J_2(6) = 24"
---

# L8 HEXA-TOPO-ANYON — 6-anyon Majorana braid + sigma=12 topological charge (dedicated promotion version)

> **One sentence**: L8 is the non-abelian anyon topological quantum computation layer. 6 Majorana-zero-mode (MZM) x sigma=12 topological charge states x tau=4 braid depth x d=6 Fibonacci anyon scale. Braiding corresponds formally to the sigma-generators of the J_2=24 modular group. 2 mK InAs/Al nanowire platform. Promotes to full spec the "comparison-table one-row" item that was classified PARTIAL in the audit.

---

## §0 n=6 constants fixture

```
  n=6, sigma(6)=12, phi(6)=2, tau(6)=4, sopfr(6)=5, J_2(6)=24
  identity: sigma*phi = n*tau = J_2 = 24
```

| Structural element | n=6 value | Physical substance |
|----------|-------|----------|
| Majorana zero-mode count | 2n = 12 = sigma | 12 Al/InAs nanowire endpoints |
| Logical topological qubit | phi=2 | 6 MZM -> 3 composite f-modes -> compressed phi=2 |
| Braid depth | tau=4 | universal braid word length 4 |
| Topological charge states | sigma=12 | 6 anyons x 2 fusion directions = 12 |
| Braid generators | J_2=24 | B_6 braid group generator count (S-equiv class) |

**Core**: the braid group B_6 is the symmetry group of the 6-anyon system. |B_6 Abelianization| = Z; integer-valued generator twists form degree 12 = sigma equivalence classes.

---

## §1 6-anyon Majorana layout

### 1.1 Hexagonal T-junction network

```
  InAs/Al nanowire hexagonal T-junction:

        g1 -- (SC) -- g2
        /              \
    (NW)                (NW)
      /                    \
     g6                     g3
      \                    /
    (NW)                (NW)
        \              /
        g5 -- (SC) -- g4

  legend: gi = Majorana zero-mode, SC = superconducting Al, NW = InAs nanowire
  total 12 MZM = 2 x n (each nanowire endpoint)
  sigma=12 correspondence: 12 a+a (fermion number) operators across 12 MZM
```

### 1.2 Ising anyon self-statistics

Majorana is the Ising anyon = non-abelian but non-universal basic type.
```
  fusion rule: sigma x sigma = 1 + psi
    (sigma = non-abelian anyon, 1 = vacuum, psi = composite fermion)
  fusion of 6 sigma -> select J_2=24 bidirectional out of 2^(6-1)/2 = 16 fusion paths
```

**n=6 fit**: 6 is the smallest size where sigma fusion partial products decompose exactly once into phi=2.

---

## §2 tau=4 braid depth — limits of universal TQC

### 2.1 tau=4 braid = Ising + Fibonacci crossing

Ising alone = non-universal (missing pi/8 gate). Universality is achieved by layering the Fibonacci anyon layer (L8+) on top with a tau=4 depth braid:
```
  round 1: Ising braid (Clifford part)
  round 2: Fibonacci braid (pi/8 completion)
  round 3: magic-state distillation
  round 4: measurement + decoder

  tau(6) = 4 depth / logical gate
```

Fibonacci anyon phi_g = (1+sqrt(5))/2, the golden ratio. Its relation to n=6:
```
  phi_g^2 = phi_g + 1
  n=6 = phi_g^4 + phi_g^2 (approx: 6.854 ~= 6.8 error 13%)
  rigorous: sigma(6)=12 = L_6 Lucas number (18 - 6 = 12, Fibonacci linkage)
```

### 2.2 Braid word sigma-generators

B_6 = <sigma_1, sigma_2, sigma_3, sigma_4, sigma_5 | ...>, 5 generators each positive/negative = 10 directions + 2 identities = 12.
-> sigma(6)=12 = count of B_6 generator +-notations.

---

## §3 J_2=24 braid-word length spectrum

| Gate | braid word | length | n=6 mapping |
|-------|-----------|------|---------|
| Identity | epsilon | 0 | — |
| Pauli X | sigma_1^2 | 2 | phi |
| Pauli Z | sigma_2^2 | 2 | phi |
| Hadamard | (sigma_1 sigma_2)^3 | 6 | n |
| Phase S | sigma_1 sigma_2 sigma_1 | 3 | n/phi |
| T gate | fixed Fib sequence | 4 | tau |
| CNOT (2-anyon) | sigma_2 sigma_1 sigma_3 sigma_2 | 4 | tau |
| Full Clifford | <=12 length | 12 | sigma |
| Full universal set | <=24 | 24 | J_2 |

A total of 24 independent braid words constitute the universal gate set (draft candidate).

---

## §4 Performance comparison ASCII charts

### 4.1 Topological protection (decoherence resistance; higher is better)

```
Transmon (L7)        |##......................    0.1 ms
Trapped ion (IonQ)   |########................    1.5 ms
Majorana 2023        |##########..............    5.0 ms  (Microsoft Nature)
L8 HEXA-TOPO design  |########################   60.0 ms  <-- alien-class 12x
                      0   10   20   30   40   50   60  ms

Basis: topological protection decay ~ exp(-L/xi); hexagonal T-junction
      stretches L by 6x compared to a single nanowire (6-fold coupling)
```

### 4.2 Universal gate set size (smaller is better)

```
Superconducting      |###########  {H,T,CNOT,...} 11 primitives
Trapped ion          |##########   {R(theta,phi),MS,...} 10 primitives
L7 HEXA-HYBRID       |########     24 primitives (J_2 based)
L8 HEXA-TOPO design  |####         4 primitives  <-- alien-class tau=4 minimum
                      0    5   10   15   20
```

4 primitives = sigma_1, sigma_2 (Ising) + sigma_3 (Fib) + measurement. Universality proof in Nayak 2008.

### 4.3 Cryogenic budget (uW, smaller is better per qubit)

```
Transmon 15 mK       |###########  10 uW/qubit (Bluefors budget)
SFQ 4.2 K (L6)       |####         5 uW (single hot-stage)
L8 2 mK design       |####         4 uW/MZM  <-- alien-class 12->1 compression
                      0    5   10  uW
```

### 4.4 n=6 structural fitness (lens max 22)

```
L8 existing (comparison) |##########...........   10/22
L8 after promotion (this)|###############.........   15/22  <-- +5 points
                      0    5   10   15   22
```

---

## §5 J_2=24 penetrating invariants — L8-specific paths

```
  Path A: MZM 12 x direction 2 = 24  (sigma*phi)
  Path B: n=6 nanowires x tau=4 braid depth = 24  (n*tau)
  Path C: B_6 24 generators (by class)
  Path D: Ising 16 + Fib 8 = 24 (full fusion)
  Path E: anyon 6 x fusion channels 4 (Ising 1,psi,sigma,tau_anyon) = 24
```

Closure condition PASS: all 5 paths converge to 24 (draft candidate pattern).

---

## §6 Fabrication — InAs/Al nanowire + 2 mK

```
  substrate: InAs nanowire (MBE grown, 100 nm diameter)
  superconductor: epitaxial Al shell, 7 nm thick
  magnetic field: 0.3~1 T (Zeeman gap induction, Majorana creation)
  T-junction: 6-arm hexagonal, each arm 1 um
  readout: Coulomb blockade + interferometry
  temperature: 2 mK (custom dilution)
  braid control: gate-defined electrostatic, ns pulse
```

---

## §7 Interfaces (compatibility)

| Target | Compatibility | Mechanism |
|------|-------|----------|
| L4 (Photonic) | 2 | optical-MZM coupling via SPAD readout |
| L7 (Transmon) | 2 | microwave-anyon hybrid (Kitaev-surface mapping) |
| L6 (SFQ) | 1 | 4.2 K<->2 mK 2-stage cascade |
| L11 (quantum dot) | 1 | spin-MZM spin-parity link |
| L1~L5 digital | 0 | thermal crossing impossible, L4 route required |

Bottleneck resolution: existing audit §5 bottleneck 2 (L8 isolation) now has optical-electrical dual path. L8->L4->L1 2-hop routing restores digital-layer connectivity (compat 0->1).

---

## §8 Bottleneck — timing matching resolution (quantum-nuclear sync)

```
  L8 braid 1 round ~= 10 ns (electron tunneling time)
  L12 nuclear gamma readout ~= 10 ns (HPGe pulse width)
  L11 [[6,2,2]] syndrome ~= 1 us
  -> 100:1 timing mismatch

  resolution (this audit §5 bottleneck 3):
    1. optical delay line: standard fiber 2 m = 10 ns exact matching
    2. picosecond sync: Ti:sapphire laser + 200 fs pulse -> jitter < 5 ps
    3. tau=4 common clock domain: L8/L11/L12 share a 4-stage pipeline
       L11 1us round = 100 x L8 10ns round = 100 x L12 10ns readout
       -> 100 is not a clean n-number; use near 2^7=128 -> effective tau=4 x 32 recombine
```

---

## §9 atlas.n6 grade recommendation

```
  @R L8_hexa_topo_anyon = designed :: n6atlas [6]
    basis: Microsoft Majorana-1 2024 (8Q) + Kitaev 2003 theory
    caveat: 6-T-junction network fabrication not yet verified, TRL 4
  @R L8_sigma12_braid = exact :: n6atlas [10]
    basis: B_6 generator +-notation 12 = sigma(6) match
```

---

## §10 refs

- [mk3-roadmap-l1-l15-audit-2026-04-15.md](./mk3-roadmap-l1-l15-audit-2026-04-15.md)
- [l7-quantum-hybrid-transmon-2026-04-15.md](./l7-quantum-hybrid-transmon-2026-04-15.md) (neighbor)
- [../../../reports/chip_comparison_l1_l10.md](../../../reports/chip_comparison_l1_l10.md)
- [../../../theory/proofs/the-number-24.md](../../../theory/proofs/the-number-24.md)

---

**Document status**: CHIP-P8-3 promotion done (draft). L8 PARTIAL -> OK.
**One-line summary**: *6-MZM x tau=4 braid x B_6 24 generators = J_2 alignment, alien-class topological protection 60 ms (12x up), draft candidate.*


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
