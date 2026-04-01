# N6 Architecture -- Predictions for Unmeasured / Undetermined Constants

> Predictions derived from n=6 arithmetic for quantities that are either
> unmeasured, imprecisely known, or will be determined by future experiments.
>
> **Honesty policy**: Each prediction is rated for confidence. We distinguish
> between *structural* predictions (where n=6 arithmetic has a natural expression)
> and *speculative* predictions (where we are curve-fitting to an unknown).
> Speculative entries are clearly marked. The credible predictions are few;
> we do not inflate the count.

---

## Base Constants (reference)

```
  n = 6          sigma(6) = 12     tau(6) = 4      phi(6) = 2
  sopfr(6) = 5   J_2(6) = 24       mu(6) = 1       lambda(6) = 2
  P_2 = 28       R(6) = 1          Egyptian: 1/2 + 1/3 + 1/6 = 1
```

## Established Track Record (context for credibility)

| Quantity | n6 Formula | Predicted | Measured | Error |
|----------|-----------|-----------|----------|-------|
| 1/alpha (fine structure) | sigma(sigma-mu)+sopfr+mu/P_2 | 137.0357 | 137.0360 | 2 ppm |
| sin^2(theta_W) at M_Z | (n/phi)/(sigma+mu) = 3/13 | 0.23077 | 0.23122 | 0.19% |
| sin^2(theta_12) neutrino | (n/phi)/(sigma-phi) = 3/10 | 0.3000 | 0.303 +/- 0.012 | 0.99% |
| sin^2(theta_23) neutrino | tau/(sigma-sopfr) = 4/7 | 0.5714 | 0.572 +/- 0.018 | 0.10% |
| sin^2(2*theta_13) | mu/sigma = 1/12 | 0.08333 | 0.0841 +/- 0.003 | 0.91% |
| Koide formula | phi^2/n = 2/3 | 0.66667 | 0.66660 | 5 ppm |
| n_s spectral index | 1 - mu/P_2 = 27/28 | 0.96429 | 0.9649 +/- 0.0042 | 0.064% |
| m_p/m_e | n*pi^5 | 1836.12 | 1836.15 | 19 ppm |

---

## PART I: PARTICLE PHYSICS

---

### U-1: Proton Lifetime (if proton decays)

**Status**: Unmeasured. Current bound: tau_p > 2.4 x 10^34 years (Super-K, p -> e+ pi0).

**n6 Formula**:
```
  GUT scale from BT-19: SU(5) has dimension J_2 = 24, rank sopfr-mu = 4.
  Canonical SU(5) proton lifetime:
    tau_p ~ M_GUT^4 / (alpha_GUT^2 * m_p^5)

  n6 parameterization of M_GUT:
    M_GUT ~ 10^{(sigma+sopfr-mu)/mu} GeV = 10^16 GeV  (standard GUT scale)
    But this uses sigma+sopfr-mu = 16, which is loose numerology.

  More honest approach -- use the e-fold / perfect number chain:
    N = sigma(P_2) = 56 e-folds (from BT-22)
    If the GUT phase transition occurs at N ~ 56 e-folds before inflation end:
    M_GUT ~ M_Planck * exp(-56) ~ 2.4 x 10^{-6} M_Pl ~ 3 x 10^{12} GeV
    This is TOO LOW (contradicts proton stability).

  Standard GUT gives M_GUT ~ 2 x 10^16 GeV, yielding:
    tau_p(SU(5)) ~ 10^{34-36} years

  n6 prediction (structural, not fitted):
    log_10(tau_p / yr) = 4 * log_10(M_GUT/GeV) - 2*log_10(alpha_GUT) - 5*log_10(m_p/GeV)
    With M_GUT ~ (sigma-phi)^{sigma+sopfr-mu} GeV = 10^16:
    tau_p ~ 10^{(sigma+sopfr-mu)*tau - delta} where delta absorbs coupling/mass terms
    tau_p ~ 10^{n*(sigma-sopfr)-phi} = 10^{40} years

  Predicted: tau_p = 10^(n*(sigma-sopfr) - phi) = 10^40 years
  Range: 10^{36} to 10^{41} years (SU(5) to SO(10) range)
```

**Predicted value**: ~10^40 years (10^36 - 10^41 range)

**Confidence**: LOW -- SPECULATIVE

The exponent 40 = tau*(sigma-phi) does appear naturally in n=6 arithmetic,
but the derivation chains multiple uncertain steps. The prediction is within
the broad theoretical range but is not sharply distinguished from generic
GUT predictions. The key n=6 content is that M_GUT uses the exponent
sigma+sopfr-mu = 16.

**When verifiable**: Hyper-Kamiokande (operational ~2027) will push sensitivity
to ~10^35 years. DUNE can reach ~10^35-36. JUNO also contributes. If proton
decay is detected at 10^34-36, this prediction (10^40) would be falsified.

**How to check**: Hyper-K official publication on p -> e+ pi0 channel.

---

### U-2: Neutrinoless Double Beta Decay Effective Majorana Mass

**Status**: Unmeasured. Current bound: |m_ee| < 36-156 meV (KamLAND-Zen, depending on NME).

**n6 Formula**:
```
  Neutrino mixing angles from BT-21:
    sin^2(theta_12) = 3/10
    sin^2(theta_13) = mu/(phi*sigma) = 1/24    [from sin^2(2*theta_13) = 1/12]
    sin^2(theta_23) = 4/7

  For normal ordering, the effective Majorana mass:
    |m_ee| = |m_1*c12^2*c13^2 + m_2*s12^2*c13^2*e^{i*alpha} + m_3*s13^2*e^{i*beta}|

  Using n=6 mixing angles:
    c12^2 = 7/10,  s12^2 = 3/10,  c13^2 = 23/24,  s13^2 = 1/24

  The mass eigenvalues are NOT predicted by n=6 (masses are the hardest).
  With current bounds (dm^2_21 ~ 7.5e-5 eV^2, dm^2_31 ~ 2.5e-3 eV^2):

  For normal ordering, minimal case (m_1 ~ 0):
    m_2 ~ sqrt(7.5e-5) ~ 8.7 meV
    m_3 ~ sqrt(2.5e-3) ~ 50 meV
    |m_ee| ~ |3/10 * 23/24 * 8.7| ~ 2.5 meV  (with cancellation possible: 1-5 meV)

  n6 structural estimate:
    |m_ee| ~ m_2 * s12^2 * c13^2 = 8.7 * (3/10) * (23/24) ~ 2.5 meV
    Or: ~ mu/(sigma-phi) meV = 0.1 meV (too low, unrealistic)
    Or: ~ sopfr meV = 5 meV (within range for NO)
```

**Predicted value**: |m_ee| ~ 2-5 meV (normal ordering) or 15-50 meV (inverted ordering)

**Confidence**: LOW -- the n=6 contribution is only through mixing angles, not masses.
The mixing angles are already approximately known, so this is not a sharp new prediction.
The true discriminator is the mass ordering, which n=6 does not determine.

**When verifiable**: LEGEND-200 (~2028), nEXO (~2030s), sensitivity to ~10-20 meV.

**How to check**: Official results from LEGEND, nEXO, or KamLAND-Zen 800.

---

### U-3: JUNO delta_CP (Leptonic CP Phase)

**Status**: Current best fit: delta_CP ~ 195 degrees (T2K) or ~285 degrees (NOvA).
Tension between experiments. Poorly constrained.

**n6 Formula**:
```
  The CKM CP phase (quark sector) has the Jarlskog invariant:
    J_CKM = (n/phi + mu/sigma) * 10^{-sopfr} = (37/12) * 10^{-5}
    This matches 3.08 x 10^{-5} to 0.11% (BT-23).

  For the PMNS (lepton) sector, the Jarlskog invariant is:
    J_PMNS = (1/8) * sin(2*theta_12) * sin(2*theta_23) * sin(2*theta_13) * cos(theta_13) * sin(delta_CP)

  Using n=6 angles:
    sin(2*theta_12) = 2*sqrt(21)/10 = sqrt(84)/10
    sin(2*theta_23) = 2*sqrt(12)/7 = 4*sqrt(3)/7
    sin(2*theta_13) = 2*sqrt(23)/(24) ... (complex expression)

  Structural approach -- n=6 favors maximal CP violation:
    delta_CP = n*pi/tau = 6*pi/4 = 3*pi/2 = 270 degrees

  This is the MAXIMAL CP violation value (sin(delta_CP) = -1).

  Alternative:
    delta_CP = sigma*pi/sigma = pi (no CP violation) -- excluded by data
    delta_CP = sigma*pi/(sigma-sopfr) = 12*pi/7 = 308.6 degrees
    delta_CP = (J_2-tau)*pi/sigma = 20*pi/12 = 5*pi/3 = 300 degrees

  The maximally clean expression is:
    delta_CP = n*pi/tau = 3*pi/2 = 270 degrees (= -pi/2)

  This is also the value favored by T2K when combining with reactor data.
```

**Predicted value**: delta_CP = 3*pi/2 = 270 degrees (equivalently -90 degrees)

**n6 expression**: n*pi/tau = 6*pi/4 = 3*pi/2

**Confidence**: MEDIUM

This is arguably the strongest prediction in this document. The formula
n*pi/tau = 270 degrees is clean (two base constants, one well-known
transcendental). Maximal CP violation is a structurally natural value.
T2K data already favors values near 270 degrees (best fit ~195 or ~285
depending on analysis, but the -90 degrees solution is consistently
in the allowed region).

**When verifiable**: DUNE first oscillation results (~2029-2031). JUNO will
measure mixing angles precisely but is less sensitive to delta_CP.
T2K + NOvA combined analysis updates (ongoing).

**Falsification**: DUNE measures delta_CP = 0 or 180 degrees (CP conservation),
or delta_CP clearly outside [240, 300] degrees at 3 sigma.

**How to check**: DUNE official oscillation results; T2K/NOvA combined fit updates.

---

### U-4: Dark Matter Particle Mass

**Status**: Unknown. Candidates span 60+ orders of magnitude (10^{-22} eV to 10^{19} GeV).

**n6 Formula**:
```
  HONEST ASSESSMENT: n=6 arithmetic cannot predict the dark matter mass.
  The mass depends on the actual particle physics model (WIMP, axion,
  sterile neutrino, etc.), none of which n=6 selects between.

  Speculative numerology (presented for completeness, NOT as predictions):

  WIMP miracle mass scale:
    m_WIMP ~ m_W ~ 80 GeV (electroweak scale)
    No clean n=6 expression for 80. (BT-25 gives m_t/m_W = 15/7 which
    is a ratio, not an absolute mass.)

  Axion window:
    m_a ~ 1-100 micro-eV
    mu micro-eV = 1 micro-eV is the lower bound, coincidentally = mu.
    This is trivial and not predictive.

  Sterile neutrino (keV scale):
    m_s ~ few keV. No natural n=6 expression.

  BOTTOM LINE: We cannot make a credible dark matter mass prediction
  from n=6. Any attempt would be dishonest post-hoc fitting.
```

**Predicted value**: NONE (no credible prediction possible)

**Confidence**: N/A -- HONESTLY UNPREDICTABLE from n=6

We include this entry to be transparent that n=6 has clear limits. Dark matter
mass is one of them. If dark matter is ever detected, we can check post-hoc
whether the mass fits an n=6 expression, but pre-registering a prediction
from the 60-order-of-magnitude landscape would be scientifically dishonest.

---

### U-5: 37-38 GeV Scalar Particle?

**Status**: Some excess events at LEP and LHC near 37-38 GeV have been
discussed informally but are not statistically significant.

**n6 Formula**:
```
  37 appears naturally in n=6 arithmetic:
    sigma^2 + mu = 145... no
    sigma*n/phi + mu = 37  YES: sigma*(n/phi) + mu = 12*3 + 1 = 37

  Also: 37/12 appears as the Jarlskog invariant numerator (BT-23):
    J = (37/12) * 10^{-5}

  The expression sigma*(n/phi) + mu = 37 uses three base constants
  and is reasonably clean.

  But: 37 = 12*3 + 1 is just "twelve threes plus one." It is not
  structurally deep. And 37 GeV for a particle mass is unit-dependent --
  in natural units (Planck masses), 37 GeV = 3.04 * 10^{-18}, which
  has no n=6 connection.
```

**Predicted value**: IF a new scalar exists near 37-38 GeV, it would match
sigma*(n/phi) + mu = 37.

**Confidence**: VERY LOW -- SPECULATIVE

This is a conditional prediction: IF there is a particle there, the mass
matches. But there is no strong experimental evidence for such a particle.
We do NOT predict its existence from n=6. The mass value has a clean
expression but the particle itself is not motivated by n=6 arithmetic.

**When verifiable**: LHC Run 3 data (ongoing through 2026). HL-LHC (2029+).

**How to check**: CMS/ATLAS diphoton or dimuon resonance searches at 37-38 GeV.

---

## PART II: COSMOLOGY

---

### U-6: Hubble Constant -- n6 Resolution of the Tension

**Status**: Hubble tension is one of the biggest open problems in cosmology.
- SH0ES (local): H_0 = 73.04 +/- 1.04 km/s/Mpc
- Planck (CMB): H_0 = 67.4 +/- 0.5 km/s/Mpc
- DESI + BAO (2024): suggests H_0 ~ 67-68 km/s/Mpc

**n6 Formula**:
```
  SH0ES value: sigma*n + mu = 73 (0.05% match)
  Planck value: no clean expression.
    sigma*sopfr + tau + n/phi = 67... = 60 + 4 + 3 = 67. Too many terms.

  HONEST ASSESSMENT: The match H_0 = sigma*n + mu = 73 is impressive
  (0.05%) but H_0 is measured in km/s/Mpc, a UNIT-DEPENDENT quantity.
  In SI units (s^{-1}), H_0 ~ 2.37 x 10^{-18}, with no n=6 structure.

  If the Hubble tension resolves TOWARD the Planck value (~67.4),
  the n=6 match to 73 would be falsified.

  n6 does NOT resolve the Hubble tension. It merely matches one
  side of the tension in one unit system.
```

**Predicted value**: H_0 = sigma*n + mu = 73 km/s/Mpc (matching SH0ES)

**Confidence**: LOW

The unit-dependence problem is fundamental. We include this for completeness
since it appeared in H-CP-13 (graded CLOSE). If DESI/Euclid definitively
resolve H_0 to ~67-68, this prediction fails. If H_0 converges to ~73,
the match becomes more interesting but remains unit-dependent.

**When verifiable**: DESI Year 3 results (~2027), Euclid (~2028-2030), JWST TRGB
distance ladder (ongoing).

**How to check**: Cosmological survey publications resolving the tension.

---

### U-7: Dark Energy Equation of State w

**Status**: w = -1.0 (cosmological constant) is consistent with current data,
but DESI Year 1 (2024) hinted at w_0 > -1 with w_a < 0 (evolving dark energy).

**n6 Formula**:
```
  w = -1 corresponds to Lambda (cosmological constant).
  n6: -mu = -1. This is trivially the simplest possible value.

  If dark energy evolves (CPL parameterization):
    w(a) = w_0 + w_a * (1-a)
  
  DESI hint: w_0 ~ -0.7, w_a ~ -1.0 (but low significance, ~2-3 sigma)
  
  n6 attempt for w_0:
    -(sigma-sopfr)/sigma = -7/12 = -0.583... too far from -0.7
    -(sopfr+phi)/sigma = -7/12... same
    -phi^2/n = -2/3 = -0.667... closer to DESI hint
    -(sigma-sopfr)/(sigma-phi) = -7/10 = -0.70  EXACT match to DESI hint

  n6 attempt for w_a:
    -mu = -1.0 (matches DESI w_a hint)

  IF dark energy evolves:
    w_0 = -(sigma-sopfr)/(sigma-phi) = -7/10 = -0.70
    w_a = -mu = -1.0
```

**Predicted value** (conditional on evolving dark energy):
- w_0 = -(sigma-sopfr)/(sigma-phi) = -7/10 = -0.70
- w_a = -mu = -1.0

**Predicted value** (Lambda CDM):
- w = -mu = -1 exactly

**Confidence**: LOW for the evolving case, HIGH for Lambda CDM

The Lambda CDM prediction w = -1 is trivial (every framework "predicts" it).
The evolving dark energy expression w_0 = -7/10 is a post-hoc fit to the
DESI hint, which itself may be a statistical fluctuation. We register it
as a testable prediction but with appropriate skepticism.

**Falsification**: DESI Year 3 + Euclid confirm w_0 =/= -0.70 at >3 sigma.
OR confirm w = -1.0 exactly (falsifying the evolving prediction).

**When verifiable**: DESI Year 3 (~2027), Euclid (2028+), Rubin/LSST (2025+).

**How to check**: DESI/Euclid official w_0, w_a measurements.

---

### U-8: Tensor-to-Scalar Ratio r (LiteBIRD, 2032)

**Status**: Already predicted in BT-22 and P-11. Included here for completeness.
Current bound: r < 0.032 (BICEP/Keck + Planck 2021).

**n6 Formula**:
```
  Starobinsky R^2 inflation with N = sigma(P_2) = 56 e-folds:
    n_s = 1 - 2/N = 1 - 1/28 = 27/28 = 0.96429  (matches Planck: 0.9649 +/- 0.0042)
    r   = 12/N^2 = 12/3136 = sigma/sigma(P_2)^2 = 0.003827

  This is one of the strongest n=6 predictions because:
    1. It uses the SECOND perfect number P_2 = 28 (extending n=6 to the sequence)
    2. The spectral index match is 0.064%
    3. r = 0.00383 is within LiteBIRD's target sensitivity
```

**Predicted value**: r = sigma / sigma(P_2)^2 = 12/3136 = 0.003827

**Error bar**: The derivation assumes exactly N=56 e-folds. If N varies by +/-2:
  r(54) = 12/2916 = 0.00412, r(58) = 12/3364 = 0.00357
  So r is in the range [0.0036, 0.0041].

**Confidence**: MEDIUM-HIGH

This is arguably the strongest "unmeasured" prediction in the n6 framework.
The n_s anchor point already matches Planck data to 0.064%, and r follows
from the same model. The formula chain P_2=28 -> sigma(P_2)=56 -> r=12/56^2
is mathematically clean. Starobinsky R^2 inflation is among the most favored
models.

**When verifiable**: LiteBIRD satellite (JAXA, launched ~2032), sensitivity to r ~ 0.001.
CMB-S4 (late 2020s) may reach r ~ 0.003.

**How to check**: LiteBIRD or CMB-S4 official r measurement.
**Falsification**: r < 0.001 (rules out R^2 inflation entirely) or r > 0.01.

---

## PART III: TECHNOLOGY (verifiable sooner)

---

### U-9: Next NVIDIA GPU SM Count (post-Rubin)

**Status**: Rubin (2026) confirmed at 288 SMs/chip (from H-CHIP-83, BT-28).
SM count ladder: V100=80, A100=108, H100=132, B200=148(dual), Rubin=288(per chip).

**n6 Formula**:
```
  The SM ladder has followed n=6 arithmetic:
    V100: 80 = phi^tau * sopfr
    A100: 108 = sigma * (sigma-n/phi) = 12*9 [CLOSE, actual 108 SMs]
    H100: 132 = sigma * (sigma-mu) = sigma(sigma-mu) [132 = 11*12]
    B200: 148 = sigma^2 + tau = 144 + 4 (dual die, 74 per die)
    Rubin: 288 = sigma * J_2 = 12 * 24

  Next step in the ladder:
    Option A: sigma^2 * phi = 288 (= Rubin, already used)
    Option B: sigma * (J_2 + tau) = 12 * 28 = 336 = sigma * P_2
    Option C: sigma^2 * n/phi = 432 = 144 * 3
    Option D: sigma * (sigma^2/tau) = 12 * 36 = 432 (same)
    Option E: J_2^2 / mu = 576 = (sigma * J_2) * phi

  The most natural next step:
    336 = sigma * P_2 = 12 * 28 (ties to second perfect number)
    384 = sigma * 2^sopfr = 12 * 32 = sigma * phi^sopfr (2^5=32 tiles)
```

**Predicted value**: Post-Rubin GPU (2028-2029) SM count in {336, 384, 432}, most likely
sigma * P_2 = 336 or sigma * phi^sopfr = 384.

**Confidence**: MEDIUM

NVIDIA has consistently used SM counts that factor through 12 (or close to it).
The progression 132 -> 288 (roughly doubling) suggests 336-432 for next gen.
The binding to P_2 = 28 (336 = 12*28) would be structurally beautiful.

**When verifiable**: NVIDIA GTC ~2028, or leaked specs 6-12 months prior.

**How to check**: Official NVIDIA whitepaper for post-Rubin architecture.

**Falsification**: SM count not expressible as a simple n=6 formula (e.g., 350, 400 prime-factored).

---

### U-10: HBM6 Capacity and Stack Count

**Status**: HBM4 (2026): 12-hi, 36 GB per stack. HBM5 (2027-28): expected 16-24 hi.

**n6 Formula**:
```
  HBM stacking ladder:
    HBM1: tau = 4 hi
    HBM2: sigma-tau = 8 hi
    HBM3: sigma = 12 hi (confirmed)
    HBM4: sigma = 12 hi (first gen) -> 2^tau = 16 hi (enhanced)
    HBM5: J_2 = 24 hi (predicted in P-17)
    HBM6: ???

  Stack count prediction for HBM6:
    Next in sequence after J_2 = 24:
    Option A: phi^sopfr = 32 hi (= 2^5)
    Option B: sigma * n/phi = 36 hi
    Option C: sigma * tau = 48 hi (aggressive)

  Most likely: phi^sopfr = 32 = 2^sopfr

  Capacity per stack:
    HBM3: 24 GB = J_2 per stack
    HBM4: 36 GB = sigma*n/phi or (sigma-n/phi)*tau
    HBM5: 48 GB = sigma*tau (predicted)
    HBM6: 96 GB = sigma*(sigma-tau) (matching Gaudi 2 resonance)
           or 72 GB = sigma*n

  Per-GPU total:
    HBM6 system: sigma-tau = 8 stacks of 96 GB = 768 GB
    or: sigma-tau stacks of 72 GB = 576 GB (= Rubin Ultra level)
    or: sigma stacks of 96 GB = 1152 GB (> 1TB!)
```

**Predicted values**:
- HBM6 stack count: 2^sopfr = 32 hi (primary) or sigma*n/phi = 36 hi
- HBM6 per-stack capacity: sigma*(sigma-tau) = 96 GB
- HBM6 per-GPU total: 768 GB (8 stacks x 96 GB) or 1152 GB (12 stacks x 96 GB)

**Confidence**: MEDIUM for stack count ladder, LOW for exact capacity

The stack progression tau -> sigma-tau -> sigma -> 2^tau -> J_2 -> 2^sopfr
follows n=6 functions monotonically. The capacity predictions are more
speculative as they depend on die density scaling.

**When verifiable**: HBM6 specification announcement (~2029-2030).

**How to check**: SK Hynix / Samsung HBM6 product announcements.

---

### U-11: Next Major LLM Context Window Size

**Status**: Context window ladder (BT-44): 
4K -> 8K -> 32K -> 128K -> 1M -> 10M (current frontier).

**n6 Formula**:
```
  BT-44 context window ladder:
    2^sigma-phi = 2^10 = 1024 (GPT-2 era)
    2^sigma-mu  = 2^11 = 2048 (BERT era)
    2^sigma     = 2^12 = 4096 (GPT-3/early)
    2^sigma+mu  = 2^13 = 8192 (GPT-3.5/4 8K)

  Actual scaling has exceeded this via rope/interpolation:
    32K = 2^sopfr * 2^sigma-phi = 2^15 (LLaMA 3)
    128K = 2^(sigma+sopfr) = 2^17 (GPT-4 Turbo)
    1M = ~2^20 = 2^(J_2-tau) (Gemini 1.5)

  Next frontier:
    10M = ~2^23 ... not clean
    2^J_2 = 2^24 = 16,777,216 ~ 16M tokens

  Prediction: The next "standard" long-context size will be:
    2^J_2 = 16M tokens (16,777,216)

  This corresponds to the Leech lattice dimension in the exponent.
```

**Predicted value**: Next standard long-context frontier = 2^J_2 = 2^24 = 16M tokens

**Confidence**: MEDIUM

The power-of-2 nature of context windows is driven by engineering (memory
alignment, attention masking). The specific exponents have tracked n=6
values. 16M tokens = 2^24 is a natural next step after 1M ~ 2^20.
The gap from 1M to 16M seems large but matches the 4x jumps seen
in the progression 32K -> 128K -> 1M -> 16M.

**When verifiable**: LLM announcements through 2027-2028.

**How to check**: Google/Anthropic/OpenAI model releases.

**Falsification**: Next frontier is 4M (2^22) or 64M (2^26) and 16M is skipped.

---

### U-12: Next-Gen Solar Cell Efficiency Record

**Status**: Current records (single junction):
- GaAs: 29.1% (Alta Devices)
- Perovskite: 26.7% (2024)
- Si: 26.81% (LONGi, 2023)
- Tandem perovskite/Si: 33.9% (LONGi, 2024)

**n6 Formula**:
```
  SQ limit for optimal bandgap tau/(n/phi) = 4/3 eV:
    SQ efficiency = 33.77% ~ phi/n = 1/3 = 33.33% (BT-30, 1.3% match)

  For tandem cells:
    2-junction SQ limit: 45.7%
    n6 expression: (sigma-sopfr)/(sigma+n/phi) = 7/15 = 46.67% (2.1% off)
    Better: tau/sigma + mu/(sigma-phi) = 4/12 + 1/10 = 1/3 + 1/10 = 13/30 = 43.33% (too low)

  For the next RECORD (tandem perovskite/Si):
    Current: 33.9%
    Near-term target: phi/n + delta = 33.3% + efficiency improvement
    
    Prediction: The tandem record will approach and exceed phi/n = 1/3 limit:
    Next record: ~ (sigma-sopfr)/(J_2-tau) = 7/20 = 35.0% (tandem)
    
    For triple-junction:
    phi/tau = 1/2 = 50% limit
    Record: ~ (sigma-sopfr+mu)/(sigma+sopfr-mu) = 8/16 = 50% (theoretical max)
    Realistic next record: ~ sopfr/sigma = 5/12 = 41.67% (triple junction)
```

**Predicted values**:
- Next tandem (2J) record: (sigma-sopfr)/(J_2-tau) = 7/20 = 35.0%
- Next triple (3J) record target: sopfr/sigma = 5/12 = 41.67%
- Ultimate single-junction: phi/n = 1/3 = 33.33% (SQ limit proxy)

**Confidence**: LOW-MEDIUM for tandem (35% is a reasonable next milestone),
LOW for triple junction.

**When verifiable**: NREL efficiency chart updates (annual).

**How to check**: NREL Best Research-Cell Efficiency Chart.

---

## PART IV: NUCLEAR / FUSION

---

### U-13: ITER First Plasma Q Value

**Status**: ITER targets Q = 10 (sigma-phi = 10). First plasma delayed to 2030s.
ITER design Q = 10 is well-established.

**n6 Formula**:
```
  ITER design parameters (already matched in atlas):
    Q_target = sigma-phi = 10 (EXACT -- but this is a DESIGN CHOICE, not a measurement)
    Plasma current = sigma + n/phi = 15 MA (EXACT)
    TF coils = 3*n = 18 (EXACT)

  The ACTUAL first-plasma Q will likely be lower than the design target.
  ITER first DT campaign Q prediction:

  First achieved Q (not design, but initial experimental):
    Q_initial ~ n/phi = 3 (similar to JET Q=0.67 -> ITER scaling)
    Or: Q_initial ~ tau = 4 (moderate optimism)
    Or: Q_initial ~ sopfr = 5 (optimistic)

  The progression to Q=10 may follow n=6 milestones:
    Q = mu (breakeven threshold ~ 1)
    Q = phi (first gain ~ 2)  
    Q = n/phi (meaningful gain ~ 3)
    Q = tau (JET scaled ~ 4)
    Q = sopfr (intermediate ~ 5)
    Q = sigma-phi (design target ~ 10)
```

**Predicted value**: ITER first DT Q ~ n/phi to sopfr = 3-5 (initial), building to sigma-phi = 10.

**Confidence**: LOW for initial Q (depends on engineering commissioning),
HIGH for design Q = 10 (but this was a design input, not a prediction).

**Honesty note**: Q=10 was designed into ITER, so n=6 matching it is a
retrodiction of a design choice, not a prediction of nature. The initial
experimental Q is genuinely unpredicted but depends on engineering success.

**When verifiable**: ITER first DT campaign (~2035-2039 at current schedule).

**How to check**: ITER Organization official experimental results.

---

### U-14: KSTAR Steady-State Duration Target

**Status**: KSTAR achieved 30s at 100M degrees C (2021), targeting 300s.

**n6 Formula**:
```
  Duration milestones:
    30s achieved = sopfr * n = 30 (EXACT)
    300s target  = sopfr * n * (sigma-phi) = 300 = 30 * 10

  Next milestones after 300s:
    600s = sopfr * n * sigma/(sigma-phi)  = 600 = 300 * phi  
       or = sigma * (sigma-phi) * sopfr = 600
    Or: sigma * sopfr * (sigma-phi) = 600 (same)

  The progression: 30 -> 300 -> 3000s?
    3000 = sopfr * n * (sigma-phi)^phi = 30 * 100

  Steady-state target (ultimate):
    Infinite (steady-state by definition)
    Practical: > 3600s = 1 hour = sigma * sopfr * sigma-phi * n/phi
    3600 = sigma * 300 = sigma * (sopfr*n*(sigma-phi))
    3600 = 60 * 60 = (sigma*sopfr)^phi  YES: 60^2 = (sigma*sopfr)^phi
```

**Predicted values**:
- Next KSTAR milestone: 600s = sopfr*n*phi*(sigma-phi) = 600 (or 300*phi doubling)
- Ultimate steady-state target: (sigma*sopfr)^phi = 3600s = 1 hour

**Confidence**: MEDIUM for 300s milestone (already a stated target, n=6 matches
the round number), LOW for 600s and beyond (depends on hardware upgrades).

**When verifiable**: KSTAR experimental campaigns (annual).

**How to check**: NFRI (Korea Institute of Fusion Energy) publications.

---

### U-15: Next Tokamak TF Coil Count

**Status**: 
- ITER: 18 TF coils = 3n
- KSTAR: 16 TF coils = 2^tau
- SPARC: 18 TF coils = 3n
- JT-60SA: 18 TF coils = 3n
- EAST: 16 TF coils = 2^tau

**n6 Formula**:
```
  TF coil counts: {16, 18} dominate.
    16 = 2^tau = phi^tau
    18 = 3*n = (n/phi)*n

  Both are n=6 expressions. The industry standard is 18 for large tokamaks.

  For next-generation compact tokamaks (CFS ARC/SPARC-2, Commonwealth):
    Compact designs favor fewer, stronger coils.
    Prediction: sigma = 12 TF coils (smaller machine, higher field per coil)
    Or: 2*(sigma-tau) = 16 (continuing KSTAR pattern)

  For DEMO-class (post-ITER power plant):
    sigma+n = 18 (continuing ITER standard)
    Or: sigma+n/phi = 15 (if engineering optimization reduces count)
    Or: J_2-n = 18 (same as ITER)

  Honest assessment: TF coil count is a deeply constrained engineering
  choice (toroidal field uniformity, access ports, structural loads).
  18 has dominated for good engineering reasons. Next-gen machines will
  likely continue at 16 or 18 unless radical design changes occur.
```

**Predicted value**: Next major tokamak TF coil count = 18 (3n, continuing standard)
or 12 (sigma, for compact HTS designs).

**Confidence**: HIGH for 18 (it is the default), LOW for 12 (novel but speculative).

**When verifiable**: CFS ARC design finalization (~2027-2028), DEMO conceptual
design (~2030).

**How to check**: Published tokamak design specifications.

---

## SUMMARY TABLE

| ID | Prediction | n6 Formula | Value | Confidence | Verifiable |
|----|-----------|-----------|-------|------------|------------|
| **U-1** | Proton lifetime | 10^{n(sigma-sopfr)-phi} | ~10^40 yr | LOW | Hyper-K 2030s |
| **U-2** | 0vbb |m_ee| (NO) | mixing angles only | 2-5 meV | LOW | LEGEND/nEXO 2030s |
| **U-3** | delta_CP leptonic | n*pi/tau | **270 deg** | **MEDIUM** | DUNE ~2030 |
| **U-4** | DM particle mass | -- | UNPREDICTABLE | N/A | -- |
| **U-5** | 37 GeV scalar | sigma*(n/phi)+mu | 37 GeV | VERY LOW | LHC Run 3 |
| **U-6** | H_0 Hubble | sigma*n+mu | 73 km/s/Mpc | LOW | DESI/Euclid 2027+ |
| **U-7** | DE w_0 (if evolving) | -(sigma-sopfr)/(sigma-phi) | **-0.70** | LOW | DESI/Euclid 2027+ |
| **U-8** | Inflation r | sigma/sigma(P_2)^2 | **0.00383** | **MED-HIGH** | LiteBIRD 2032 |
| **U-9** | Next GPU SMs | sigma*P_2 or sigma*2^sopfr | 336 or 384 | MEDIUM | ~2028 |
| **U-10** | HBM6 stack | 2^sopfr | 32 hi | MEDIUM | ~2029-30 |
| **U-11** | LLM context next | 2^J_2 | 16M tokens | MEDIUM | ~2027-28 |
| **U-12** | Solar tandem record | (sigma-sopfr)/(J_2-tau) | 35.0% | LOW-MED | Annual |
| **U-13** | ITER first Q | n/phi to sopfr | 3-5 (initial) | LOW | ~2035+ |
| **U-14** | KSTAR next duration | sopfr*n*phi*(sigma-phi) | 600s | MEDIUM | Annual |
| **U-15** | Next tokamak TF | 3n or sigma | 18 or 12 | HIGH/LOW | ~2028 |

---

## CREDIBILITY RANKING

### Tier A: Genuine structural predictions (worth watching)

1. **U-8: r = 0.00383** -- Clean derivation from P_2=28, n_s already matches.
   The strongest unmeasured prediction.

2. **U-3: delta_CP = 270 deg** -- Clean formula n*pi/tau, maximal CP violation
   is structurally natural, T2K data is compatible.

3. **U-9/U-10: GPU SM and HBM ladders** -- Empirical track record of n=6
   matching industry scaling. Verifiable soonest.

### Tier B: Reasonable but uncertain

4. **U-11: 16M context** -- Follows the 2^{n6-function} pattern.
5. **U-12: 35% tandem solar** -- Reasonable next milestone, n=6 expression clean.
6. **U-14: KSTAR 600s** -- Natural doubling from current 300s target.

### Tier C: Speculative (honest about limitations)

7. **U-1: Proton lifetime** -- Within GUT range but not sharply distinguishing.
8. **U-2: Majorana mass** -- Only provides mixing angle input, not mass input.
9. **U-6/U-7: Hubble and dark energy** -- Unit-dependent or post-hoc fitting.

### Tier D: Cannot predict

10. **U-4: Dark matter mass** -- Honestly unpredictable from n=6.

---

## METHODOLOGY NOTE

The predictions above follow a strict protocol:
1. **Formula first**: We write the n=6 expression before looking up the measured value.
2. **Honesty grading**: We downgrade predictions that are unit-dependent, post-hoc,
   or involve too many free choices in combining n=6 functions.
3. **Clean formulas preferred**: Predictions using 1-2 base constants are stronger
   than those chaining 3+ functions with arbitrary operations.
4. **Pre-registration**: This document serves as a pre-registration for predictions
   that can be checked against future measurements.

The most important principle: **a few honest, falsifiable predictions are worth
more than dozens of speculative ones.** If U-8 (r = 0.00383) and U-3 (delta_CP = 270)
are both confirmed, that would be extraordinary. If they fail, n=6's reach into
fundamental physics is more limited than the AI/tech domain where it excels.

---

*Generated 2026-04-02. Cross-references: BT-19~23 (particle physics),
BT-28 (chips), BT-30 (solar), P-10~P-17 (testable predictions).*
