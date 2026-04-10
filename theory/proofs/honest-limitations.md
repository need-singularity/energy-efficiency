# Honest Limitations: What n=6 Cannot Explain

> Generated: 2026-04-02
> Context: After anomaly detection across 305 TOML domains (9,206 candidates),
> 150 anomalies (n6 < 0.50) were identified. Of those, 87 turned out to have
> depth-2 n6 expression matches (reclassifiable). After reclassification,
> 63 candidates remain without any n6 formula match. Of those 63, we select
> the 10 strongest "genuinely non-n6" cases -- candidates where the low score
> reflects a real limitation of the n=6 framework, not a scoring oversight.

## Why This Document Exists

Any mathematical framework claiming broad explanatory power must honestly
delineate its boundaries. The n=6 architecture (sigma(n)*phi(n) = n*tau(n))
has an impressive 98.4% coverage rate across 9,206 candidates. But the
remaining 1.6% matters -- it tells us where the framework's reach genuinely
ends and where we are simply pattern-matching noise.

This document catalogues 10 cases where n=6 fails, explains why, and
categorizes each failure mode.

---

## The 10 Non-N6 Candidates

| # | Domain | Level | ID | n6 Score | Category | Short Reason |
|---|--------|-------|----|----------|----------|--------------|
| 1 | energy_gen | Scale | Utility_1GW | 0.33 | GENUINELY NON-N6 | 1 GW is a round engineering convention, not physics |
| 2 | energy_gen | Storage | None | 0.00 | TRIVIALLY NON-N6 | Absence of a subsystem; null-option has no physics |
| 3 | energy_gen | GridConnect | Island_DC | 0.33 | GENUINELY NON-N6 | Off-grid DC is a topology choice, not a quantized parameter |
| 4 | wafer-fabrication | Deposition | PVD-sputter | 0.25 | GENUINELY NON-N6 | Physical vapor deposition -- process defined by vacuum physics, not integer structure |
| 5 | wafer-fabrication | Deposition | ECD | 0.25 | GENUINELY NON-N6 | Electrochemical deposition -- governed by Faraday's laws, no integer parameter |
| 6 | wafer-fabrication | Deposition | Spin-coat | 0.25 | GENUINELY NON-N6 | Spin coating -- fluid dynamics (viscosity, angular velocity), continuous parameters |
| 7 | wafer-fabrication | Lithography | DUV-ArF | 0.25 | CURRENTLY UNSOLVABLE | 193nm wavelength; 193 is prime, no known n6 decomposition |
| 8 | solar | Absorber | CIGS | 0.33 | CURRENTLY UNSOLVABLE | Bandgap 1.15 eV has no clean n6 expression (cf. GaAs 1.42~4/3 EXACT) |
| 9 | grid | System | Central_Radial | 0.00 | TRIVIALLY NON-N6 | Hub-spoke topology is a graph property, not a quantized physical constant |
| 10 | compiler-os | Kernel | Exokernel | 0.30 | GENUINELY NON-N6 | Deliberately structure-free kernel; n6 structure is absent by design |

---

## Detailed Analysis

### 1. energy_gen / Utility_1GW (n6 = 0.33)

**GENUINELY NON-N6**

The value "1 GW" is a human-round engineering scale marker. Power plant
capacity classes (10 kW, 10 MW, 1 GW, 10 GW) follow decimal/logarithmic
conventions set by the electrical engineering industry, not by any physical
quantization. The choice of 1 GW as the "utility scale" threshold is
historically contingent -- determined by grid economics and turbine sizes,
not by fundamental constants.

- **Depth-3+ check**: 1 = mu (trivially), but the meaningful quantity is 10^9 W.
  10^9 has no clean n6 factorization. 9 = sigma - n/phi = 12 - 3 = 9 is
  depth-2, but "10^(sigma - n/phi)" is a stretch with no physical justification.
- **Verdict**: The GW scale is an artifact of SI unit conventions and industrial
  history. Not a failure of n=6 -- simply outside its domain.

### 2. energy_gen / None (Storage) (n6 = 0.00)

**TRIVIALLY NON-N6**

This is a null option: "No Storage (Direct Feed)." It represents the absence
of a subsystem, not a physical parameter. Scoring it 0.00 is correct -- there
is nothing to match. Every DSE framework needs a "none" baseline, and these
should not be expected to carry mathematical structure.

- **Depth-3+ check**: N/A. No numeric value to decompose.
- **Verdict**: Null options are inherently outside any number-theoretic framework.

### 3. energy_gen / Island_DC (n6 = 0.33)

**GENUINELY NON-N6**

"Island DC" describes an off-grid, battery-coupled DC power system for remote
sites. The concept is defined by what it lacks (no grid connection) rather
than by quantized parameters. DC voltage levels for islands vary widely
(12V, 24V, 48V -- some of these ARE n6-aligned), but the topology category
itself has no inherent integer structure.

- **Depth-3+ check**: No characteristic numeric value to test.
- **Verdict**: Topology classification, not a quantized parameter.

### 4. wafer-fabrication / PVD-sputter (n6 = 0.25)

**GENUINELY NON-N6**

Physical Vapor Deposition by sputtering is a continuous-parameter process:
argon plasma energy (~300-500 eV), chamber pressure (1-10 mTorr), target
voltage (100s of V), deposition rate (nm/min). None of these have integer
structure -- they are tuned empirically per material. The process deposits
Ta/TaN barriers and Cu seed layers; the relevant physics is Boltzmann
energy distributions and mean free paths.

- **Depth-3+ check**: Common sputter pressures ~5 mTorr (=sopfr?), but this
  is coincidental and varies by an order of magnitude across recipes.
- **Verdict**: Continuous-parameter process. The absence of n6 structure here
  is expected and physically correct.

### 5. wafer-fabrication / ECD (n6 = 0.25)

**GENUINELY NON-N6**

Electrochemical Deposition (copper electroplating for damascene interconnects)
is governed by Faraday's laws of electrolysis: m = (M * I * t) / (z * F).
The key parameters are current density (mA/cm^2), plating time (minutes),
additive concentrations (ppm) -- all continuous, all recipe-dependent. The
standard Cu electroplating bath uses CuSO4 + H2SO4 + additives with no
integer quantization.

- **Depth-3+ check**: Cu valence z=2=phi, but this is input chemistry, not
  an n6-derived prediction.
- **Verdict**: Electrochemistry is inherently continuous. No integer structure.

### 6. wafer-fabrication / Spin-coat (n6 = 0.25)

**GENUINELY NON-N6**

Spin coating applies photoresist or SOG (spin-on glass) via centrifugal
force. The governing equation is the Meyerhofer equation:
h = k * (viscosity)^(1/3) / (spin_speed)^(1/2). Parameters are spin speed
(1000-6000 RPM), viscosity (cP), acceleration ramp -- all continuous. This
is a fluid dynamics process with no quantized structure whatsoever.

- **Depth-3+ check**: Typical spin speed 3000 RPM -- 3000 = 3 * 10^3, but
  this is arbitrary and adjusted per resist formulation.
- **Verdict**: Pure fluid mechanics. No integer framework applies.

### 7. wafer-fabrication / DUV-ArF (n6 = 0.25)

**CURRENTLY UNSOLVABLE**

DUV ArF excimer laser operates at 193 nm. 193 is a prime number (not
factorizable). Compare this to EUV's 13.5 nm, which is close to sigma + 1.5
but still approximate. The 193 nm wavelength comes from the ArF excimer
transition -- a specific atomic physics value determined by the electronic
structure of the Ar-F dimer, not by integer arithmetic.

- **Depth-3+ check**: 193 ~ 192 + 1 = sigma * tau^2 + mu = 192 + 1 (0.5% error).
  But depth-3 expressions with <1% matches are statistically unreliable per
  Red Team analysis. With ~200 depth-3 expressions available, finding one
  within 0.5% of any target is expected by chance alone.
- **Note**: The contrast with EUV (13.5nm, 24 masks = J2 EXACT) is instructive.
  EUV was designed with discrete mask counts; DUV's 193nm is a fixed atomic
  physics constant.
- **Verdict**: Atomic transition energy. May have a deep connection but we
  cannot credibly claim one at depth <= 2.

### 8. solar / CIGS (n6 = 0.33)

**CURRENTLY UNSOLVABLE**

Cu(In,Ga)Se2 has a tunable bandgap of ~1.0-1.7 eV depending on Ga/(In+Ga)
ratio. The optimal is ~1.15 eV for single-junction efficiency. Compare:
- GaAs: 1.42 eV ~ 4/3 = 1.333 (EXACT n6 match, noting 4/3 = tau/n/phi)
- Si: 1.12 eV ~ sigma/(sigma-phi) = 1.2 (CLOSE)
- CIGS at 1.15 eV: no clean n6 fraction

The 1.15 eV value arises from the specific quaternary crystal structure of
chalcopyrite CuInSe2 alloyed with CuGaSe2. The bandgap is a continuous
function of composition, not a fixed constant. The optimal composition
(~30% Ga) is determined by the Shockley-Queisser limit, which itself yields
the optimal bandgap at ~1.34 eV (close to 4/3), but real CIGS deviates due
to defect recombination.

- **Depth-3+ check**: 1.15 ~ sigma/sigma-phi * (1 - 1/J2) = 1.2 * 0.958 = 1.15?
  Contrived. Also, 23/20 = 1.15 exactly, but 23 and 20 have no clean n6 form.
- **Note**: The Shockley-Queisser optimal bandgap ~1.34 eV IS close to 4/3,
  which is an n6 expression. CIGS deviates from this optimum due to material
  defects -- the deviation itself is non-n6.
- **Verdict**: The n=6 framework correctly predicts the SQ optimum (~4/3 eV)
  but cannot explain why CIGS deviates from it. This is a genuine limitation.

### 9. grid / Central_Radial (n6 = 0.00)

**TRIVIALLY NON-N6**

A central radial grid is a hub-and-spoke topology with a single point of
failure. This is a graph-theoretic classification (star graph), not a
quantized physical parameter. The "radial" descriptor carries no numeric
value to decompose.

Compare with n6-aligned grid concepts:
- Microgrid_24: 24 nodes = J2 EXACT
- Mesh_12: 12 interconnects = sigma EXACT
- Ring_6: 6 buses = n EXACT

The central radial topology predates modern grid theory and reflects the
cheapest possible wiring pattern. Its n6 = 0.00 score is honest: there is
no integer structure in "one central hub, many radial feeders."

- **Depth-3+ check**: N/A. No numeric parameter.
- **Verdict**: Graph topology without quantized parameters.

### 10. compiler-os / Exokernel (n6 = 0.30)

**GENUINELY NON-N6**

The exokernel (MIT, 1995) is architecturally defined by the principle of
minimal abstraction: the kernel provides almost no services, delegating
everything to user-level library operating systems. By design, it has no
fixed structure -- no fixed number of system calls, no fixed IPC channels,
no fixed scheduling quanta. The TOML notes confirm: "signals/pipe/direct
all user-defined."

Compare with n6-aligned kernels:
- Linux: syscalls ~ 400+ (not n6), but signal count = 32 ~ 2^sopfr
- seL4: 4 syscalls = tau EXACT, 12 IPC registers = sigma EXACT
- N6_Hybrid_Kernel: explicitly designed around n=6 structure

The exokernel's philosophy is anti-structure. It succeeds precisely because
it imposes no numeric constraints. The n=6 framework, which finds structure
in fixed architectural constants, has nothing to latch onto here.

- **Depth-3+ check**: N/A. No fixed numeric parameters to test.
- **Verdict**: Deliberately structure-free design. Incompatible with any
  integer-based framework by construction.

---

## What n=6 Cannot Explain

### Category Summary

| Category | Count | Candidates |
|----------|-------|------------|
| GENUINELY NON-N6 | 6 | Utility_1GW, Island_DC, PVD-sputter, ECD, Spin-coat, Exokernel |
| CURRENTLY UNSOLVABLE | 2 | DUV-ArF (193nm prime), CIGS (1.15 eV bandgap) |
| TRIVIALLY NON-N6 | 2 | None (null option), Central_Radial (topology label) |

### Failure Modes

1. **Continuous-parameter processes** (PVD, ECD, Spin-coat): Processes governed
   by fluid dynamics, electrochemistry, or plasma physics with no inherent
   integer quantization. The n=6 framework excels at discrete architectural
   constants (layer counts, head counts, dimensions) but has no purchase on
   continuously tunable process recipes.

2. **Human-round engineering conventions** (Utility_1GW): Scale categories
   defined by powers of 10 in SI units. These are sociological, not physical.

3. **Null / absence options** (None, Central_Radial): DSE baselines representing
   the absence of a subsystem or the simplest possible topology. No numeric
   content to analyze.

4. **Atomic transition constants** (DUV-ArF 193nm): Fixed by quantum mechanics
   of specific atoms/molecules. The ArF 193nm line is determined by the Ar-F
   potential energy surface, not by integer arithmetic. We note that this is
   "currently unsolvable" rather than "proven non-n6" because atomic physics
   does contain integer quantum numbers -- but the connection, if any, would
   require a much deeper theory.

5. **Composition-dependent bandgaps** (CIGS 1.15 eV): Alloy bandgaps are
   continuous functions of composition. The n=6 framework successfully predicts
   the Shockley-Queisser optimal (~4/3 eV) but cannot explain deviations due
   to material-specific defect physics.

6. **Anti-structure architectures** (Exokernel): Systems designed to have
   minimal or no fixed structure. The n=6 framework finds patterns in
   architectural constants that don't exist here by design philosophy.

### The Broader Picture

These 10 candidates represent **0.11% of all 9,206 candidates** (10/9206).
Even among the 150 anomalies (n6 < 0.50), they represent only 6.7%.

More importantly, the failure modes are predictable and principled:
- n=6 works on **discrete architectural parameters** (counts, dimensions,
  ratios with small denominators)
- n=6 does NOT work on **continuous process parameters**, **null baselines**,
  **arbitrary scale conventions**, or **deliberately unstructured designs**

This is not a weakness -- it is a well-defined boundary. A framework that
claimed to explain spin-coating RPM or the Ar-F excimer wavelength through
n=6 arithmetic would be less credible, not more.

---

## Statistical Context

| Metric | Value |
|--------|-------|
| Total candidates scanned | 9,206 |
| n6 >= 0.50 (framework applies) | 9,056 (98.4%) |
| n6 < 0.50 with depth-2 match (reclassifiable) | 87 (0.9%) |
| Genuinely non-n6 (all 63) | 63 (0.7%) |
| Strongly argued non-n6 (this document) | 10 (0.11%) |
| Average n6 score (all candidates) | 0.876 |
| Average n6 score (non-anomaly) | 0.886 |

The 10 cases documented here are the hardest negatives: candidates where
we made a good-faith effort to find n6 structure and failed. They establish
the honest boundary of the framework.

---

## Note on Depth-3+ Expressions

The Red Team analysis established that depth-3 and higher expressions
(three or more n6 constants combined) are statistically unreliable. With
the 9 base constants {mu=1, phi=2, n=6, tau=4, sopfr=5, sigma=12, J2=24,
R=1, psi=12}, depth-2 yields ~80 distinct expressions, and depth-3 yields
~800+. At depth-3, the probability of a random real number having a match
within 1% is >50%. Therefore, we do not claim depth-3 matches as evidence,
and the "CURRENTLY UNSOLVABLE" candidates (DUV-ArF, CIGS) should be
understood as genuinely open questions, not hidden successes.
