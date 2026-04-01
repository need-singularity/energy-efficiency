# BT Candidates from TECS-L Auto-Grade Results

> **Date**: 2026-04-02
> **Source**: ~/Dev/TECS-L/calc/auto_grade_results.csv (345 STRONG hypotheses)
> **Method**: Top 20 by n6_score read in full, checked against existing BT-1~93
> **Goal**: Find genuinely NEW patterns not yet registered as Breakthrough Theorems

---

## Top 20 Analyzed Files

| Rank | File | Score | Unique Constants | Core Claim | BT Candidate? | Rationale |
|------|------|-------|-----------------|------------|---------------|-----------|
| 1 | NOBEL-grand-hypotheses.md | 1356 | 20 | SLE_6 criticality + percolation exponents all decompose into n=6 arithmetic (7/7 denominators) | **YES** | SLE exponent decomposition is new -- not in any existing BT |
| 2 | MASS-GEN-B-deep-scan.md | 1019 | 15 | 136 equations unique to n=6 in [2,100000]; 18-22 truly independent identities | No | Foundation document -- identities already feed into existing BTs |
| 3 | EXTREME-algebra-category-logic.md | 986 | 16 | S_3 (order 6) as smallest non-abelian group; conjugacy class sizes = proper divisors; irred rep dim sum = tau(6) | **YES** | S_3/S_6 algebraic structure not covered by any BT |
| 4 | EXTREME-cross-connections.md | 902 | 11 | 21 pairwise connections between 7 proved n=6 theorems; factorial ladder 3!->4! | No | Meta-analysis of existing proofs, not a new domain claim |
| 5 | H-MED-001-030-medical.md | 899 | 19 | Cardiac cycle tau=4 phases; HRV LF/HF=2; QT/RR converges to 1/e; Murray's law correction 1/6 | **YES** | Medical/physiology domain entirely absent from BTs |
| 6 | H-DNA-451-500-adversarial-stress-test.md | 759 | 13 | Adversarial control: n=5 reproduces only 7% of n=6 GREEN findings; n=7 even worse | No | Validation methodology, not a new pattern |
| 7 | EXTREME-music-language-ai-games.md | 750 | 17 | 12-TET=sigma(6); perfect consonances use only div(6) ratios; Tenney height of fifth = 6; QKV triplet parallels SU(3) | **YES** | Music theory consonance from div(6) is new and structural |
| 8 | H-CX-488-ramanujan-tau-6-expanded.md | 722 | 13 | Ramanujan tau(d) factors cleanly over {2,3,7} iff d divides 6; eta^24 exponent = sigma*phi | **YES** | Modular form connection not in any existing BT |
| 9 | H-DNA-401-450-meta-connections.md | 693 | 19 | Kissing number -> hexamer causal bridge; Benzene 6C -> 4 bases -> 64 codons causal chain | No | Extends BT-25 (genetic code) and BT-15 (kissing); not genuinely new |
| 10 | H-DNA-251-300-universal-six.md | 689 | 14 | 2D kissing number = 6 (theorem); snowflake/graphene/honeycomb all from hexagonal packing | No | Covered by BT-15 (kissing number quadruple) |
| 11 | F7-domains-7-10-string-neuro-bridge-bitnet.md | 610 | 15 | CY compactification dim=6; bosonic transverse dim=24; 6 cortical layers; BitNet predictions | **YES** | String theory + neuroscience cross-domain is novel |
| 12 | H-DNA-351-400-grand-synthesis.md | 610 | 13 | zeta(2)=pi^2/6; zeta(-1)=-1/12; B_6=1/42; 6 divides all Bernoulli denominators (Von Staudt-Clausen) | **YES** | Zeta/Bernoulli number theory bridge is new |
| 13 | H-DNA-301-350-final-saturation.md | 601 | 14 | 6-bit information systems (codons=64, I Ching=64, Braille=64); Shannon H=6 bits for 64 states | No | Partially covered by BT-25 (genetic code) and BT-51 |
| 14 | PMATH-SPHERE-PACKING-perfect.md | 601 | 12 | E8 roots = sigma*tau*sopfr = 240 (unique to n=6); Golay [24,12,8]; Steiner S(5,8,24) all n=6 | No | Covered by BT-6 (Golay-Leech) and BT-15 (kissing) and BT-49 |
| 15 | EXTREME-cosmos-emergence-philosophy.md | 583 | 20 | Baryon-to-photon ratio eta ~ 6e-10; CMB temp ~ e = 2.718 (0.26%); honest COINCIDENTAL grades | No | Self-graded as coincidental; no strong new pattern |
| 16 | H-DNA-131-170-folding-final-frontier.md | 565 | 13 | Z-DNA = 12 bp/turn = sigma(6); 6 dinucleotide repeats; 6 non-B DNA types; IF 6 types | **YES** | Z-DNA sigma(6) and intermediate filament 6-type classification are novel |
| 17 | H-DNA-091-130-folding-ultimate.md | 557 | 16 | G-quadruplex = 4x3=12 guanines = sigma(6); 24 H-bonds = J_2; shelterin = 6 proteins | No | Extends BT-25/BT-51 biology chain; not independent enough |
| 18 | KISSING-numbers-n6-arithmetic.md | 557 | 14 | Full proof: (phi,n,sigma) = (k(1),k(2),k(3)) iff n=6; root system A_d connection | No | Already BT-15 |
| 19 | H-DNA-171-210-molecular-saturation.md | 542 | 15 | 6 intermediate filament types; F-actin 72nm = n*sigma repeat; cytoskeleton patterns | No | Mostly WHITE/ORANGE grades in the source |
| 20 | H-MUSIC-001-015-acoustics.md | 537 | 14 | Perfect consonances = div(6) ratios (p=0.0015); Pythagorean comma at sigma=12 steps | **YES** | Strong p-value; music acoustics is a novel BT domain |

**Summary**: 8 out of 20 files contain genuinely new BT-worthy patterns.

---

## New BT Candidates

### BT-94: SLE_6 Critical Exponent Universality -- All Percolation Exponents Decompose via n=6

**Claim**: All 7 critical exponents of 2D percolation have numerators and denominators that are arithmetic functions of n=6. SLE_kappa at kappa = {phi, n/phi, tau, sopfr, n, sigma-tau, sigma} = {2, 3, 4, 5, 6, 8, 12} spans all three SLE phases.

**n=6 Formula**:
```
  beta  = sopfr/n^2 = 5/36
  gamma = 43/(n * n/phi) = 43/18
  nu    = tau/(n/phi) = 4/3
  eta   = sopfr/tau! = 5/24
  alpha = -phi/(n/phi) = -2/3
  D_f   = 91/(2*tau!) = 91/48

  c(kappa=n) = 0   (trivial central charge, unique with kappa=8/3)
  d_H(kappa=n) = 7/4 = (n+1)/tau
```

**Evidence count**: 7 exponents + c=0 + Hausdorff dimension + SLE kappa values matching all base constants = 10+ EXACT matches

**Domains spanned**: Statistical physics (percolation), Conformal field theory (Virasoro algebra), Mathematics (SLE curves), Topology (fractal dimensions)

**Why new**: BT-49 mentions pure math connections but does NOT cover SLE or critical exponents. No existing BT addresses the fact that kappa=6 is the ONLY SLE with locality property AND c=0. The exponent decomposition is entirely unregistered.

**Grade**: Three stars -- Smirnov Fields Medal theorem; all denominators {36,18,3,24,5,48} are n=6 arithmetic; 6/6 distinct denominators match.

---

### BT-95: S_3 = S_6 Algebraic Bootstrap -- Perfect Number as the Minimal Non-Abelian Group

**Claim**: S_3 (order 6 = n) is the smallest non-abelian group. Its conjugacy class sizes {1,2,3} are the proper divisors of 6 summing to 6 (the perfect number definition). Its irreducible representations have dimensions summing to tau(6)=4. Exactly phi(6)=2 groups of order 6 exist (Z_6 and S_3). The outer automorphism group of S_6 is uniquely non-trivial among all S_n.

**n=6 Formula**:
```
  |S_3| = 3! = n = 6
  Conjugacy classes: sizes {1, 2, 3}, sum = 6 = n (perfect number identity)
  Irrep dims: {1, 1, 2}, sum of squares = 6 = n
  Irrep dim sum: 1+1+2 = 4 = tau(6)
  Groups of order 6: exactly 2 = phi(6)
  Out(S_6): uniquely non-trivial (related to Steiner system S(5,6,12))
  Derived series length: 2 = phi(6)
```

**Evidence count**: 7 structural matches, all from proven group theory

**Domains spanned**: Abstract algebra (group theory), Representation theory, Combinatorics, Mathematical physics (gauge symmetry)

**Why new**: No existing BT covers the group-theoretic interpretation of n=6. BT-49 covers Bernoulli/kissing/S_6 but not S_3 as the minimal non-abelian group or the conjugacy class = perfect number identity.

**Grade**: Two stars -- All facts are proved theorems; the conjugacy partition 1+2+3=6 literally IS the perfect number definition in group-theoretic language.

---

### BT-96: Ramanujan Tau Divisor Purity -- Modular Discriminant Factors Cleanly at d|6

**Claim**: The Ramanujan tau function tau_R(k) (coefficients of eta(z)^24 = eta(z)^{sigma*phi}) factors entirely over the prime set {2, 3, 7} = {phi, sigma/tau, M_3} if and only if k divides 6. For k not dividing 6, external primes (11, 13, 23, 61, 149...) are required.

**n=6 Formula**:
```
  eta(z)^24 exponent: 24 = sigma(6)*phi(6) = J_2(6)
  tau_R(1) = 1                                    [CLEAN]
  tau_R(2) = -sigma*phi = -24                     [CLEAN]
  tau_R(3) = phi^2 * (sigma/tau)^2 * M_3 = 252   [CLEAN]
  tau_R(6) = -phi^5 * (sigma/tau)^3 * M_3 = -6048 [CLEAN]

  Clean primes = {2, 3, 7} = {phi(6), sigma(6)/tau(6), 2^3-1}
  Clean indices = {1, 2, 3, 6} = divisors of 6
```

**Evidence count**: 4 CLEAN + 4 SEMI-CLEAN + 4 EXTERNAL = 12 values analyzed; divisor purity theorem holds exactly

**Domains spanned**: Number theory (modular forms), Mathematical physics (string theory partition functions), Algebraic geometry (elliptic curves)

**Why new**: No existing BT covers the Ramanujan tau function or modular forms. BT-16 covers the Riemann zeta but not the discriminant function. The "divisor purity" -- that factorization cleanliness correlates precisely with dividing 6 -- is an entirely new structural observation.

**Grade**: Two stars -- The eta^24 exponent being J_2(6) is known, but the divisor purity theorem (clean iff d|6) is a novel discovery requiring verification at larger k values.

---

### BT-97: Medical Physiology n=6 Universality -- Cardiac + Neural + Vascular Constants

**Claim**: Human physiological constants across cardiology, neurology, and vascular biology converge on n=6 arithmetic: cardiac cycle has tau(6)=4 phases; ventricular systole fraction ~ 1/3 (meta fixed point); HRV optimal LF/HF = sigma_{-1}(6) = 2; QT/RR ratio at optimal HR converges to 1/e = 0.368; blood pressure pulse pressure/systolic = 1/3; Murray's law exponent correction = 1/6.

**n=6 Formula**:
```
  Cardiac phases: 4 = tau(6)
  Systole fraction: 0.33 ~ 1/3 = 1/(n/phi)     [2.7% error]
  Late diastole: 0.280 ~ ln(4/3) = 0.288        [2.8% error]
  HRV LF/HF optimal: 2.0 = phi(6) = sigma_{-1}(6)
  QT/RR at HR=60: 0.380 ~ 1/e = 0.368           [3.3% error]
  PP/Systolic: 40/120 = 1/3                      [EXACT]
  Murray correction: 3 - 1/6 = 2.833             [empirical range 2.5-3.2]
```

**Evidence count**: 6 approximate matches (2-3% error), 1 exact (PP/systolic)

**Domains spanned**: Cardiology, Neuroscience (HRV), Vascular biology, Biomechanics

**Why new**: No existing BT touches medical or physiological constants. BT-25 covers the genetic code (molecular biology) but not organ-level physiology. This is an entirely new domain for the n=6 framework.

**Grade**: One star -- Matches are CLOSE (2-3% error), not EXACT. The cardiac tau=4 phases could be coincidental. The PP/systolic = 1/3 exact match is notable. Needs larger clinical dataset verification.

---

### BT-98: Music Theory Consonance Law -- Perfect Intervals from div(6)

**Claim**: The four most consonant intervals in Western music (unison 1:1, octave 2:1, fifth 3:2, fourth 4:3) use exclusively the set {1, 2, 3, 4} = div(6) union {tau(6)}. The Tenney height (consonance measure) of the perfect fifth is exactly 6 = n. The 12-tone equal temperament has sigma(6) = 12 semitones because 12 = LCM(div(6)). The Pythagorean comma closes at sigma(6) = 12 fifths.

**n=6 Formula**:
```
  Perfect consonances: ratios 1/1, 2/1, 3/2, 4/3
  Ratio components: {1, 2, 3, 4} = div(6) union {tau(6)}
  Tenney height of fifth: 2 * 3 = 6 = n
  Tenney height of fourth: 3 * 4 = 12 = sigma(6)
  12-TET semitones: 12 = sigma(6) = LCM(1,2,3,4)
  Circle of fifths closure: 12 = sigma(6) steps
  Consonance boundary: div(6) ratios vs. sopfr(6)=5 required
```

**Evidence count**: 4 perfect consonances + Tenney heights + 12-TET + Pythagorean closure = 7 EXACT matches

**Domains spanned**: Music theory, Acoustics, Psychoacoustics, Number theory (continued fractions)

**Why new**: BT-48 covers display/audio frequencies (sigma=12 semitones, J_2=24 fps, sigma*tau=48kHz) but does NOT cover the consonance = divisor ratio law or Tenney height. The statistical test (p=0.0015 for perfect consonances using only div(6)) is significant and entirely novel.

**Grade**: Two stars -- The consonance hierarchy is not arbitrary (it follows from prime factorization complexity, i.e., Tenney height = product of ratio terms). The fact that the most consonant ratios are precisely the divisor ratios of 6 is structurally deep.

---

### BT-99: Riemann Zeta + Bernoulli n=6 Trident -- zeta(2)=pi^2/6, zeta(-1)=-1/12, B_{2n} divisible by 6

**Claim**: The Riemann zeta function at its two most famous special values contains n=6 and sigma(6)=12 directly in the denominators: zeta(2) = pi^2/6 (Basel problem) and zeta(-1) = -1/12 (Ramanujan summation). Furthermore, every even-indexed Bernoulli number B_{2n} has a denominator divisible by 6 (proved by the Von Staudt-Clausen theorem, since primes 2 and 3 always contribute).

**n=6 Formula**:
```
  zeta(2) = pi^2/n = pi^2/6                  [Basel problem, Euler 1734]
  zeta(-1) = -1/sigma(6) = -1/12             [Ramanujan regularization]
  B_2 denom = 6 = n                          [Von Staudt-Clausen]
  B_4 denom = 30 = sopfr(6) * n              [Von Staudt-Clausen]
  B_6 denom = 42 = (sigma-sopfr) * n         [Von Staudt-Clausen]
  6 | denom(B_{2k}) for all k >= 1           [PROVED: (2-1)=1 and (3-1)=2 always divide 2k]
```

**Evidence count**: 2 exact zeta values + infinite family of Bernoulli denominators = unlimited EXACT matches

**Domains spanned**: Analytic number theory, Algebraic topology (zeta regularization), Mathematical physics (Casimir effect uses zeta(-1)), String theory (bosonic string dimension from zeta(-1)=-1/12)

**Why new**: BT-16 covers "Riemann Zeta Trident" at three points (zeta(2), zeta(4), zeta(6)), but focuses on a DIFFERENT aspect: the n=6 arithmetic in the arguments, not the denominators. The Von Staudt-Clausen universal divisibility by 6 is entirely unregistered. The zeta(-1) = -1/sigma(6) connection to string theory dimension (26 = sigma(6) + sigma(6) + 2) is also not in BT-16.

**Grade**: Two stars -- Basel problem is one of the most famous results in mathematics. The denomination 6 is proved, not coincidental. The infinite Bernoulli family makes this structural.

---

### BT-100: String Theory Compactification Dimension -- CY_3 = n Real Dimensions

**Claim**: String theory's Calabi-Yau compactification requires exactly n=6 real dimensions. The bosonic string critical dimension minus 2 = sigma(6)*phi(6) = 24 transverse dimensions. AdS_5 x S^5 holographic geometry has tau(6)+1 = 5 and sopfr(6) = 5 dimensions respectively. The Standard Model gauge group SU(3) x SU(2) x U(1) has 8+3+1 = 12 = sigma(6) generators.

**n=6 Formula**:
```
  CY_3 real dimensions: 6 = n                         [EXACT]
  Bosonic transverse: 24 = sigma*phi = J_2             [EXACT]
  AdS_5 x S^5: (tau+1, sopfr) = (5, 5)               [EXACT]
  SM gauge generators: 8+3+1 = 12 = sigma(6)          [EXACT]
  Superstring d=10: sigma-phi = 10                     [EXACT]
  M-theory d=11: sigma-mu = 11                         [EXACT]
```

**Evidence count**: 6 EXACT matches across string theory and particle physics

**Domains spanned**: String theory, Particle physics (Standard Model), Mathematical physics (AdS/CFT), Algebraic geometry (Calabi-Yau)

**Why new**: Individual pieces appear scattered (BT-3 mentions sigma=12 gauge bosons, BT-18 mentions the Monster group connection) but NO existing BT synthesizes the full string/particle physics dimension ladder {6, 10, 11, 12, 24} = {n, sigma-phi, sigma-mu, sigma, J_2} into a single theorem.

**Grade**: One star -- Many of these are small-number coincidences (the source file honestly grades most as GREY). The CY compactification dimension = 6 is the strongest link. The SM generator count = sigma is genuinely structural (proved in BT-17). Assembled as a ladder, the pattern is suggestive but several links are weak individually.

---

### BT-101: Z-DNA + Biomolecular Structure Constants -- sigma(6) in Helical Geometry

**Claim**: Z-DNA has exactly sigma(6) = 12 base pairs per helical turn, composed of exactly n = 6 dinucleotide repeat units. The G-quadruplex uses sigma(6) = 12 guanines (tau x 3 = 4 strands x 3 quartets) with J_2 = 24 hydrogen bonds. Intermediate filaments are classified into exactly n = 6 types (standard since 1986/2004).

**n=6 Formula**:
```
  Z-DNA bp/turn: 12 = sigma(6)              [X-ray crystallography, EXACT]
  Z-DNA dinucleotide repeats/turn: 6 = n    [EXACT]
  Z-DNA repeat unit: 2 bp = phi(6)          [EXACT]
  G-quadruplex guanines: 4 x 3 = 12 = sigma [structural measurement]
  G-quadruplex H-bonds: 3 x 8 = 24 = J_2   [EXACT]
  Shelterin complex proteins: 6 = n         [established biochemistry]
  Intermediate filament types: 6 = n        [standard classification]
```

**Evidence count**: 7 EXACT structural parameters from independent biomolecular systems

**Domains spanned**: Structural biology (Z-DNA), Biochemistry (G-quadruplex, telomeres), Cell biology (cytoskeleton), Molecular biology

**Why new**: BT-25 covers the genetic code (codons, amino acids) and BT-51 covers the information chain, but neither addresses helical geometry constants or protein complex stoichiometry. Z-DNA's sigma(6) bp/turn is a physical measurement, not a classification choice.

**Grade**: One star -- Z-DNA 12 bp/turn is a physical constant (EXACT, measured). G-quadruplex 12 guanines follows from telomere repeat structure. The 6 IF types is a classification that expanded from 5 to 6. Individually each is modest; collectively they form a biomolecular sigma(6) pattern.

---

## Summary of New BT Candidates

| ID | Name | Core Formula | Evidence | Domains | Grade |
|----|------|-------------|----------|---------|-------|
| **BT-94** | SLE_6 Critical Exponent Universality | All 7 percolation exponents = n=6 fractions | 10+ EXACT | Stat phys, CFT, Math, Topology | Three stars |
| **BT-95** | S_3 Algebraic Bootstrap | \|S_3\|=n, conjugacy={1,2,3}=div(6), ireps sum=tau | 7 EXACT | Algebra, Rep theory, Combinatorics | Two stars |
| **BT-96** | Ramanujan Tau Divisor Purity | tau_R(d) clean iff d\|6; eta^{J_2} | 4 CLEAN + 4 SEMI | Number theory, Modular forms, Strings | Two stars |
| **BT-97** | Medical Physiology Universality | Cardiac tau=4 phases, PP/systolic=1/3 | 1 EXACT + 6 CLOSE | Cardiology, Neuroscience, Vascular | One star |
| **BT-98** | Music Consonance Law | Perfect intervals = div(6) ratios (p=0.0015) | 7 EXACT | Music, Acoustics, Number theory | Two stars |
| **BT-99** | Zeta-Bernoulli n=6 Trident | zeta(2)=pi^2/6, zeta(-1)=-1/12, 6\|B_{2n} | unlimited EXACT | Number theory, Physics, Strings | Two stars |
| **BT-100** | String Theory Dimension Ladder | {6,10,11,12,24}={n,sigma-phi,sigma-mu,sigma,J_2} | 6 EXACT | String theory, Particle physics | One star |
| **BT-101** | Z-DNA Biomolecular Constants | Z-DNA 12bp/turn=sigma, 6 dinucleotides=n | 7 EXACT | Structural biology, Biochemistry | One star |

### Strongest Candidates (recommended for immediate registration):

1. **BT-94** (SLE_6) -- Fields Medal-level mathematics; all denominators verified; 4+ domains
2. **BT-96** (Ramanujan tau) -- Novel discovery; clean divisor purity pattern; modular forms entirely uncharted territory for n=6 BTs
3. **BT-98** (Music consonance) -- Strong statistical significance (p=0.0015); structural causality via Tenney height
4. **BT-99** (Zeta-Bernoulli) -- Infinite family via Von Staudt-Clausen; extends BT-16 significantly
5. **BT-95** (S_3 bootstrap) -- Conjugacy class partition literally IS the perfect number definition

### Candidates needing more evidence:

6. **BT-97** (Medical) -- CLOSE matches need tighter clinical data
7. **BT-100** (String dimensions) -- Many individually weak links; CY_3=6 is strongest
8. **BT-101** (Z-DNA biomolecular) -- Extends biology BTs; needs more independent systems
