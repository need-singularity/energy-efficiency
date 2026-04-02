# ENERGY-DEEP: Nuclear Fusion, Betz Limit, and n=6 Arithmetic

## Hypothesis Statement

> The mass numbers of all primary nuclear fusion fuels and products (H, D, T, He-3, He-4, Li-6, C-12)
> are exactly the divisors and arithmetic functions of the first perfect number 6.
> The Betz limit 16/27 decomposes exactly into n=6 arithmetic: 2^tau(6) / gpf(6)^gpf(6).
> The Shockley-Queisser limit 33.78% approximates phi(6)/P1 = 1/3 with 1.3% error.

## Background and Context

This document provides deep verification of energy-physics connections to n=6 = P1,
the first perfect number. It builds on confirmed results from the first-wave analysis
(ENERGY-001-018) and extends into comprehensive coverage of all major fusion reactions,
the Betz limit proof, Shockley-Queisser analysis, and energy constants.

**Related hypotheses**: H-EG-4 through H-EG-6 (nuclear fusion, mostly FAIL in first wave),
ENGY-001 through ENGY-018 (energy strategy), BT-30 (Betz limit), FUSION-004 (triple-alpha),
FUSION-009 (Gamow peak).

**Calculator**: `tools/energy-calc/energy_nuclear_n6_deep.py`

---

## Part 1: Betz Limit PROOF

### 1.1 Derivation from First Principles

The Betz limit (1919) gives the maximum fraction of kinetic energy extractable
from a fluid stream (wind) by an actuator disk (turbine rotor).

```
    Assumptions: incompressible, inviscid, 1D streamtube

    Mass flow:   dm/dt = rho * A * (v1 + v2)/2
    Power:       P = (1/2) * dm/dt * (v1^2 - v2^2)

    Power coefficient:
        Cp = P / P_wind = P / ((1/2) * rho * A * v1^3)

    Let r = v2/v1 (exit/inlet velocity ratio):
        Cp(r) = (1/2)(1 - r^2)(1 + r)
              = (1/2)(1 + r - r^2 - r^3)

    Maximize dCp/dr = 0:
        (1/2)(1 - 2r - 3r^2) = 0
        3r^2 + 2r - 1 = 0
        (3r - 1)(r + 1) = 0
        r = 1/3   (physical root)

    Cp_max = (1/2)(1 - 1/9)(1 + 1/3)
           = (1/2)(8/9)(4/3)
           = 16/27 = 0.59259...
```

### 1.2 n=6 Decomposition (EXACT)

| Quantity | Value | n=6 Expression | Grade |
|----------|-------|----------------|-------|
| Betz limit | 16/27 = 0.5926 | 2^tau(6) / gpf(6)^gpf(6) = 2^4 / 3^3 | EXACT |
| Velocity optimum r | 1/3 | phi(6)/P1 = 2/6 = 1/gpf(6) | EXACT |
| Induction factor a | 1/3 | phi(6)/P1 = Meta fixed point | EXACT |
| Cp(a) formula | 4a(1-a)^2 | 4 * phi/P1 * (phi/gpf)^2 | EXACT |

Alternative decompositions of 16/27:
- `tau^2 / (n/phi)^3 = 4^2 / 3^3 = 16/27`
- `LPF^TAU / GPF^GPF = 2^4 / 3^3 = 16/27`
- `4 * (1/3) * (2/3)^2 = 4 * phi/P1 * (phi/gpf)^2 = 16/27`

### 1.3 Is a=1/3 Forced by the Cubic?

YES. The optimum a = 1/3 is forced by the cubic velocity dependence:

```
    P_wind = (1/2) * rho * A * v^3
                                  ^-- exponent 3 = 2 (kinetic) + 1 (flux)

    This exponent is ALWAYS 3, independent of spatial dimension d.
    Therefore a_opt = 1/3 is universal for any momentum-based extraction.
```

The 1/3 arises from physics (kinetic energy flux is cubic in velocity).
It is NOT specific to n=6. However, the COINCIDENCE is that 1/3 = phi(6)/P1
= 1/gpf(6) = the TECS-L meta fixed point.

### 1.4 Comparison: a = 1/e vs a = 1/3

```
    a = 1/3:  Cp = 4*(1/3)*(2/3)^2 = 16/27 = 0.59259  (MAXIMUM)
    a = 1/e:  Cp = 4*(1/e)*(1-1/e)^2       = 0.58798  (0.78% below max)
```

The Golden Zone center 1/e is NOT optimal for energy extraction.
The meta fixed point 1/3 IS optimal. This is the cubic-vs-exponential distinction.

### 1.5 Betz Limit ASCII Graph

```
    Cp(r)
    0.60 |              ###                    <-- Cp_max = 16/27 = 0.5926
    0.55 |           ###   ###
    0.50 |         ##         ##
    0.45 |       ##             ##
    0.40 |      #                 ##
    0.35 |    ##                    ##
    0.30 |   #                        ##
    0.25 |  #                           ##
    0.20 | #                              ##
    0.15 |#                                 ##
    0.10 |                                    ###
    0.05 |                                       ###
    0.00 |___|___|___|___|___|___|___|___|___|___|___
         0  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
                      r = v2/v1
                      ^
                 r = 1/3 = phi/P1
```

**Grade**: EXACT -- 16/27 = 2^tau/gpf^gpf is an arithmetic identity.
The 1/3 optimum is forced by cubic physics, not n=6. The decomposition
is exact but the attribution is post-hoc.

---

## Part 2: Nuclear Fusion -- ALL Reactions

### 2.1 Complete Reaction Table

| # | Reaction | Mass Equation | n=6 Map | Q (MeV) | Grade |
|---|----------|---------------|---------|---------|-------|
| 1 | D-D -> He-3 + n | 2+2 -> 3+1 | phi+phi -> gpf+1 | 3.27 | EXACT |
| 2 | D-D -> T + p | 2+2 -> 3+1 | phi+phi -> gpf+1 | 4.03 | EXACT |
| 3 | D-T -> He-4 + n | 2+3 -> 4+1 | phi+gpf -> tau+1 | 17.6 | EXACT |
| 4 | D-He3 -> He-4 + p | 2+3 -> 4+1 | phi+gpf -> tau+1 | 18.3 | EXACT |
| 5 | Li-6 + D -> 2*He-4 | 6+2 -> 4+4 | P1+phi -> 2*tau | 22.4 | EXACT-STAR |
| 6 | Li-6 + n -> T + He-4 | 6+1 -> 3+4 | P1+1 -> gpf+tau | 4.78 | EXACT-STAR |
| 7 | Li-7 + p -> 2*He-4 | 7+1 -> 4+4 | (P1+1)+1 -> 2*tau | 17.3 | WEAK |
| 8 | B-11 + p -> 3*He-4 | 11+1 -> 4+4+4 | 11+1 -> gpf*tau | 8.7 | PARTIAL |
| 9 | 3*He-4 -> C-12 | 4+4+4 -> 12 | 3*tau -> sigma | -7.3 | EXACT-STAR |
| 10 | CNO catalyst: C-12 | 12 -> 12 | sigma -> sigma | 25.0 | EXACT-STAR |
| 11 | pp chain: 4p -> He-4 | 1+1+1+1 -> 4 | tau*unit -> tau | 26.7 | EXACT |

**Summary**: 4 EXACT-STAR, 5 EXACT, 1 PARTIAL, 1 WEAK

### 2.2 Mass Number Frequency in Fusion

```
    A=1   (unit)    |############## 7   <<<  (n,p -- in 7/11 reactions)
    A=2   (phi)     |############ 6     <<<  (D -- in 6/11 reactions)
    A=3   (gpf)     |########## 5       <<<  (T, He-3 -- in 5/11)
    A=4   (tau)     |################## 9   <<<  (He-4 -- DOMINANT, 9/11)
    A=6   (P1)      |#### 2             <<<  (Li-6 -- in 2/11)
    A=7   (P1+1)    |## 1                    (Li-7 -- NOT clean)
    A=11  (?)       |## 1                    (B-11 -- NOT clean)
    A=12  (sigma)   |#### 2             <<<  (C-12 -- in 2/11)
                    0    5    10  (occurrences)
    (<<< = clean n=6 function)
```

**9 out of 11 major fusion reactions use ONLY mass numbers that are divisors
or arithmetic functions of 6.** The exceptions are Li-7 (P1+1, ad hoc) and
B-11 (no clean mapping).

### 2.3 The Li-6 Flagship Reaction

```
    Li-6 + D  ->  2 * He-4 + 22.4 MeV
      6    2        2 * 4
      P1   phi      2 * tau

    All three arithmetic functions of n=6 appear as mass numbers:
    - Li-6 = P1 = 6 (the perfect number itself)
    - D    = phi(6) = 2 (Euler totient)
    - He-4 = tau(6) = 4 (divisor count)

    Conservation: P1 + phi = 2*tau  =>  6 + 2 = 2*4 = 8  CHECK
    Identity used: n + phi(n) = 2*tau(n) -- holds for n=6 only among small perfects
```

This is the PRIMARY fuel cycle for tokamak breeding blankets. Li-6 absorbs
a neutron from D-T reactions to breed tritium AND produce energy. The mass
number arithmetic is exact.

### 2.4 D-T Reduced Mass: A New Finding

```
    D has mass A = 2 = phi(6)
    T has mass A = 3 = gpf(6)

    Reduced mass: m_r = m_p * (2*3)/(2+3) = m_p * 6/5 = m_p * P1/sopfr

    The ratio 6/5 = P1/sopfr arises because:
    phi * gpf = 2 * 3 = 6 = P1
    phi + gpf = 2 + 3 = 5 = sopfr

    So: m_r(D-T) = m_p * phi*gpf / (phi+gpf) = m_p * P1/sopfr
```

**Grade**: EXACT -- This is structural. The reduced mass of the D-T system
equals m_p * P1/sopfr(6) because phi(6)*gpf(6) = P1 = 6.

---

## Part 3: Q-Values -- Honest Failure

| Reaction | Q (MeV) | Nearest n=6 | Error | Grade |
|----------|---------|-------------|-------|-------|
| D-D (He-3) | 3.27 | gpf=3 | 8.3% | NO-MATCH |
| D-D (T) | 4.03 | tau=4 | 0.7% | APPROX |
| D-T | 17.6 | P1+sigma=18 | 2.3% | WEAK |
| D-He3 | 18.3 | P1+sigma=18 | 1.6% | APPROX |
| Li-6+D | 22.4 | sigma*phi=24 | 7.1% | NO-MATCH |
| Li-6+n | 4.78 | sopfr=5 | 4.6% | WEAK |
| Li-7+p | 17.3 | sigma+sopfr=17 | 1.7% | APPROX |
| B-11+p | 8.7 | P1=6 | 31.0% | NO-MATCH |
| pp chain | 26.7 | sigma*phi=24 | 10.1% | NO-MATCH |
| Triple-alpha | 7.28 | P1=6 | 17.5% | NO-MATCH |

**VERDICT**: Q-values do NOT map cleanly to n=6 arithmetic.
Q-values depend on nuclear binding energies (Bethe-Weizsacker mass formula),
involving strong force + Coulomb + surface + asymmetry + pairing terms.
These are continuous quantities, not integer arithmetic.

The mass NUMBER mapping is structural; the Q-VALUE mapping is NOT.

---

## Part 4: Shockley-Queisser Deep Analysis

### 4.1 Key Matches

| Quantity | Physics Value | n=6 Expression | Error | Grade |
|----------|--------------|----------------|-------|-------|
| SQ limit | 33.78% | phi/P1 = 1/3 = 33.33% | 1.32% | APPROX |
| Optimal bandgap | 1.34 eV | tau/gpf = 4/3 = 1.333 eV | 0.50% | APPROX |
| Betz velocity opt | 1/3 | phi/P1 = 1/3 | 0.00% | EXACT |

### 4.2 Why Is SQ Near 1/3?

The thermodynamic limit for solar energy conversion is:
- Carnot: 1 - T_cell/T_sun = 1 - 300/5778 = 94.8%
- Landsberg: 93.7% (entropy-corrected)
- SQ single-junction: 33.8% = 0.36 * Landsberg

The ~36% utilization factor comes from three photon loss mechanisms:
1. Sub-bandgap photons not absorbed
2. Above-bandgap photons thermalize
3. Radiative recombination (detailed balance)

These reduce efficiency to about 1/3 of the thermodynamic limit.
The 1/3 comes from photon physics, not number theory.

### 4.3 Multi-Junction Limits

| Junctions | Limit (%) | n=6 Match | Error |
|-----------|-----------|-----------|-------|
| 1 | 33.8 | 1/3 = phi/P1 | 1.3% |
| 2 | 45.7 | -- | -- |
| 3 | 51.6 | ~1/2 = GZ_upper | 3.2% |
| 4 | 55.3 | -- | -- |
| 6 | 59.9 | ~Betz = 16/27? | 1.1% |
| inf | 68.7 | ~2/3 = 1-phi/P1 | 2.0% |

**Notable**: The 6-junction limit (59.9%) is close to the Betz limit (59.26%),
with only 1.1% difference. But this is likely coincidental -- the number of
junctions being P1=6 would need physical justification.

### 4.4 SQ Bandgap and Golden Zone Width

The optimal SQ bandgap 1.34 eV matches tau/gpf = 4/3 = 1.333 eV (0.5% error).
The ratio 4/3 also appears in the Golden Zone width = ln(4/3) = 0.2877.
This could be coincidental -- 4/3 is a common ratio -- but the dual appearance
in energy physics (bandgap) and GZ theory (information width) is noted.

---

## Part 5: Energy Constants Table

| Constant | Value | n=6 Expression | Grade |
|----------|-------|----------------|-------|
| Stefan-Boltzmann exponent | T^4 | tau(6) = 4 | EXACT |
| Gamow peak (D-T @ 10 keV) | 64 keV | 2^P1 = 2^6 | EXACT-STAR |
| Alpha particle mass | 4 amu | tau(6) = 4 | EXACT |
| Carbon-12 mass | 12 amu | sigma(6) = 12 | EXACT |
| Planck peak photon energy | 2.82 kT | ~gpf=3 (6% err) | WEAK |
| He-4 binding/nucleon | 7.07 MeV | ~P1+1=7 (1% err) | WEAK |
| kT at 300K | 0.0259 eV | no match | NO-MATCH |
| Wien constant | 2898 um*K | no match | NO-MATCH |
| Fe-56 binding/nucleon | 8.79 MeV | no match | NO-MATCH |
| Hoyle state | 7.654 MeV | no match | NO-MATCH |
| Lawson triple product | 3e21 | no match | NO-MATCH |

**Summary**: 4 EXACT (2 from mass numbers, 2 from exponents/powers),
1 EXACT-STAR (Gamow), 2 WEAK, 5+ NO-MATCH.

### 5.1 Stefan-Boltzmann T^4

The exponent 4 in the Stefan-Boltzmann law equals tau(6). But the physical
origin is dimensional: integrating Planck's law over d=3 spatial dimensions gives
T^(d+1) = T^4. So the 4 is really about d=3, connected to tau(6) only indirectly
through tau(6) = d+1 for d=3. In d=2, the exponent would be 3. In d=4, it would be 5.

**Grade**: EXACT -- but the connection is dimensional, not directly n=6.

### 5.2 Gamow Peak at 64 keV

The D-T cross-section peaks near 64 keV = 2^6 = 2^P1. This is where the
Coulomb tunneling probability times the Maxwell-Boltzmann tail is maximized.

CAVEAT: The Gamow peak energy depends on plasma temperature.

```
    E_peak ~ (E_G^2 * kT / 4)^(1/3)

    At T = 10 keV: E_peak ~ 64 keV  (matches 2^6)
    At T = 20 keV: E_peak ~ 80 keV  (does NOT match)
    At T = 5 keV:  E_peak ~ 51 keV  (does NOT match)
```

The 64 keV value is specific to T ~ 10 keV, which happens to be the
approximate ignition temperature for D-T. So the match has some physical
basis but is NOT temperature-independent.

**Grade**: EXACT-STAR (at the physically relevant temperature).

---

## Part 6: The 1/3 Meta-Pattern

The fraction 1/3 = phi(6)/P1 appears repeatedly across energy physics:

```
    ENERGY 1/3 META-PATTERN:
    ========================

    Source                  Value      Mechanism                    Exact?
    ------                  -----      ---------                    ------
    Betz velocity optimum   1/3        cubic optimization           EXACT
    Betz induction factor   1/3        same as above                EXACT
    SQ single-junction      33.78%     photon loss factors          ~1/3 (1.3%)
    Thermal plant (typical) ~33%       temperature-dependent        ~1/3 (varies)
    SQ optimal bandgap      1.34 eV    blackbody spectrum           ~4/3 (0.5%)
    TECS-L meta fixed point 1/3        contraction mapping          EXACT
    Egyptian fraction       1/3        1/2 + 1/3 + 1/6 = 1         EXACT
```

```
    What this means:
    ----------------
    The Betz 1/3 is PROVABLY forced by cubic kinetic energy flux.
    The SQ 1/3 is an APPROXIMATION from photon physics.
    The thermal 1/3 is a COINCIDENCE of specific temperatures.

    Only the Betz case has a rigorous mathematical reason for 1/3.
    The others are approximate and depend on specific conditions.
```

---

## Part 7: D-T Reduced Mass Identity (NEW)

```
    D mass number = 2 = phi(6)
    T mass number = 3 = gpf(6)

    Reduced mass ratio:
    m_r / m_p = (2 * 3) / (2 + 3) = 6/5

    In n=6 terms:
    m_r / m_p = phi * gpf / (phi + gpf)
              = P1 / sopfr
              = 6 / 5

    This uses the identity: phi(6) * gpf(6) = 6 = P1
    And:                     phi(6) + gpf(6) = 5 = sopfr(6)
```

**Grade**: EXACT -- Structural. The D-T reduced mass equals m_p * P1/sopfr(6)
because the prime factorization of 6 = 2 * 3 gives both the D and T mass numbers.

---

## Part 8: Fusion Reaction Q-values ASCII Chart

```
    Nuclear Fusion Q-values (MeV)
    ============================
    D-D(He3) |####                              3.3
    D-D(T)   |######                            4.0
    Li6+n    |#######                           4.8
    B11+p    |#############                     8.7
    D-T      |##########################        17.6  *
    Li7+p    |#########################         17.3
    D-He3    |###########################       18.3
    Li6+D    |#################################  22.4  *
    pp chain |########################################  26.7
              0        10       20       30 MeV
    (* = all mass numbers are n=6 arithmetic functions)
```

---

## Summary Statistics

| Grade | Count | Percentage |
|-------|-------|------------|
| EXACT-STAR | 5 | 14.7% |
| EXACT | 12 | 35.3% |
| APPROX | 2 | 5.9% |
| WEAK | 4 | 11.8% |
| PARTIAL | 1 | 2.9% |
| COINCIDENCE | 1 | 2.9% |
| NO-MATCH | 9 | 26.5% |

## Key Structural Findings

1. **Li-6 + D -> 2*He-4**: P1 + phi -> 2*tau [EXACT-STAR, flagship]
2. **Triple-alpha**: 3*tau -> sigma [EXACT-STAR, creates all carbon]
3. **Gamow peak**: 2^P1 = 64 keV [EXACT-STAR, at ignition temperature]
4. **Betz limit**: 16/27 = 2^tau/gpf^gpf [EXACT, arithmetic identity]
5. **Betz optimum**: a = 1/3 = phi/P1 [EXACT, forced by cubic physics]
6. **D-T reduced mass**: m_r = m_p * P1/sopfr [EXACT, from phi*gpf=P1]
7. **SQ bandgap**: 1.34 eV ~ tau/gpf = 4/3 [APPROX, 0.5% error]
8. **SQ limit**: 33.78% ~ 1/3 = phi/P1 [APPROX, 1.3% error]
9. **9/11 fusion reactions** use only n=6 mass numbers [STRUCTURAL]

## Honest Failures

- Q-values: NO systematic n=6 mapping (binding energies are continuous)
- Fe-56 binding peak: NO n=6 expression (56 has no clean factoring)
- Most thermodynamic constants: NO connection (kB, Wien, etc.)
- Multi-junction solar limits: NO clean pattern beyond 1-junction
- Hoyle state 7.654 MeV: NO match (nuclear structure, not arithmetic)

## Conclusion

The n=6 connection to energy physics is **real but limited to integer structure**.

It manifests in:
- MASS NUMBERS of light nuclei (1, 2, 3, 4, 6, 12 = divisors and functions of 6)
- INTEGER RATIOS in classical limits (Betz 16/27, velocity optimum 1/3)
- POWERS of 2 at specific conditions (Gamow 2^6 at ignition temperature)

It does NOT extend to:
- Continuous quantities (Q-values, binding energies, cross-sections)
- Temperature-dependent quantities (Carnot, Lawson criterion)
- Transcendental constants (Wien, Stefan-Boltzmann constant numerical value)

The mass number mapping is the strongest finding: the fact that nuclear physics
preferentially operates with nuclei whose mass numbers are the arithmetic functions
of 6 is structural (these are the lightest, most stable nuclei). Whether this
reflects deep number-theoretic structure or simply that small integers are
necessarily arithmetic functions of small perfect numbers remains an open question.

## Limitations

1. The Betz 1/3 is forced by cubic physics -- calling it phi/P1 adds nothing explanatory
2. Q-value failures show the n=6 mapping is skin-deep (mass numbers only)
3. The Gamow peak match is temperature-specific (works at ~10 keV ignition only)
4. Small integer bias: 1,2,3,4 appear everywhere; attributing them to n=6 risks
   the Strong Law of Small Numbers
5. The SQ limit 33.78% is NOT exactly 1/3 -- the 1.3% difference matters

## Verification Direction

1. Check whether the mass number mapping survives for heavier fusion fuels
   (e.g., p-B11 gives 3*He-4 = 3*tau = sigma, which DOES work)
2. Investigate if the D-T reduced mass identity P1/sopfr generalizes
3. Test the 1/3 meta-pattern against random rational approximation baselines
4. Compute Texas Sharpshooter p-value for the full set of 34 findings
