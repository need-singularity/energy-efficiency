# Red Team Analysis: Depth-4 N=6 Formulas

Date: 2026-04-02
Method: Combinatorial enumeration + statistical estimation + numerical verification

---

## Target Formulas Under Review

| Claim | Formula | Claimed precision |
|-------|---------|-------------------|
| G (Newton) | (sopfr^sopfr + n) * n / tau^J2 | "19 ppm" |
| m_top | (depth-4 expression) | 0.4 ppm |
| m_tau | (depth-4 expression) | 1.3 ppm |
| m_W | (depth-4 expression) | 0.8 ppm |

Constants used: {sigma=12, tau=4, phi=2, sopfr=5, J2=24, mu=1, n=6}

---

## 1. G Formula: Numerical Verification

```
G_formula = (5^5 + 6) * 6 / 4^24
         = 3131 * 6 / 281474976710656
         = 18786 / 281474976710656
         = 6.67412791696...e-11
```

### 1.1 Actual Deviation (Reference-Dependent)

| G Reference | Value | Deviation |
|-------------|-------|-----------|
| CODATA 2014 | 6.67408e-11 | **7.2 ppm** |
| Li et al. 2018 | 6.674184e-11 | **8.4 ppm** |
| CODATA 2018 | 6.67430e-11 | **25.8 ppm** |
| Quinn et al. 2013 | 6.67545e-11 | 198 ppm |
| Rosi et al. 2014 | 6.67191e-11 | 332 ppm |

**Finding: The claimed "19 ppm" does not match any standard G reference.**
- CODATA 2014 gives 7.2 ppm (favorable)
- CODATA 2018 gives 25.8 ppm (unfavorable)
- The "19 ppm" figure appears to use an intermediate or cherry-picked reference value

**G experimental uncertainty: 22 ppm (CODATA 2018).**
The formula is 1.17 sigma OUTSIDE the CODATA 2018 value. Against CODATA 2014, it is
0.33 sigma inside -- but CODATA 2014 is superseded.

### 1.2 Structural Decomposition

The formula uses tau^J2 = 4^24 = 2^48 as a large denominator to reach the 1e-11 scale.

```
G = numerator / 2^48    where numerator = 3131 * 6 = 18786
```

The question becomes: is 18786 special, or can many integers near 18786 be
expressed from the 7 constants?

Answer: **18786 = 2 * 3 * 31 * 101**. No n=6 significance.

The sub-expression 3131 = 5^5 + 6 = sopfr^sopfr + n.
- 3131 = 31 * 101. **Not prime, no known physical significance.**
- 5^5 = 3125 is just "a power of 5." Adding 6 is a fine-tuning adjustment.
- The ratio 3131/3125 = 1.00192 -- the "+6" contributes only 0.2% correction.
- Without the "+6": G_approx = 3125*6/4^24 = 6.6612e-11, which is 196 ppm off.
  The "+n" term is doing the heavy lifting for precision.

**Verdict: The "+n" acts as a fine-tuning knob.** Any formula of the form
(5^5 + small_integer) * 6 / 4^24 scans through G values as the small integer varies:

| small_int | G_approx | deviation from CODATA 2018 |
|-----------|----------|---------------------------|
| 0 | 6.6612e-11 | 196 ppm |
| 1 | 6.6634e-11 | 164 ppm |
| 2 | 6.6655e-11 | 131 ppm |
| 3 | 6.6677e-11 | 99 ppm |
| 4 | 6.6698e-11 | 67 ppm |
| 5 | 6.6720e-11 | 35 ppm |
| **6** | **6.6741e-11** | **25.8 ppm** |
| 7 | 6.6763e-11 | 29.9 ppm |
| 8 | 6.6784e-11 | 61.8 ppm |

**The "+n" term steps through G in ~32 ppm increments.** With 7 constants to try
as the additive term (1,2,4,5,6,12,24), the probability that one of them lands
within 26 ppm is approximately 7 * (2*26/32000) ~ 0.011 per template.
Since there are multiple base expressions and denominators to try, this is not surprising.

---

## 2. Search Space Estimation

### 2.1 Depth-2 Expressions

With 7 constants and 5 binary operations:
- Formal expressions: 7 * 7 * 5 = **245**
- Distinct numeric values (computed): **104**
- Including unary ops and a^b with large exponents: **~294**

### 2.2 Depth-4 Expressions

A depth-4 expression composes two depth-2 sub-expressions with a binary operation.

**By formula count:**
- Template (d2 op d2): 245^2 * 5 = **300,125**
- Template (c1^c2 op c3) * c4 / (c5^c6): 7^6 * 4 = **470,596**
- General 4-leaf trees (5 topologies * 7^4 leaves * 5^3 ops): **1,500,625**

**By distinct values:**
- From 104 distinct depth-2 values: 104^2 * 5 = **54,080** (upper bound)
- Accounting for degeneracy and non-finite results: **~20,000-50,000** effective distinct values

### 2.3 Values in the G Range [1e-12, 1e-10]

To produce values ~1e-11, you need large denominators. Available from a^b:

| Denominator | Value | Required numerator for G |
|-------------|-------|--------------------------|
| sopfr^sigma = 5^12 | 2.44e+08 | 0.016 |
| J2^n = 24^6 | 1.91e+08 | 0.013 |
| n^sigma = 6^12 | 2.18e+09 | 0.145 |
| sigma^sigma = 12^12 | 8.92e+12 | 595 |
| **tau^J2 = 4^24** | **2.81e+14** | **18786** |
| J2^sigma = 24^12 | 3.65e+16 | 2,437,478 |
| sopfr^J2 = 5^24 | 5.96e+16 | 3,978,193 |

For each of these ~10 large denominators, there are ~294 depth-2 numerator candidates.
Multiplying by a second depth-2 expression gives ~294^2 = 86,436 numerator candidates
per denominator.

**Estimated formulas producing values in [1e-12, 1e-10]: ~500-2000**

At 26 ppm tolerance: P(one match) = N_candidates * 2 * 26e-6

| Estimate | N_candidates | P(match at 26 ppm) |
|----------|-------------|---------------------|
| Conservative | 500 | 0.026 (2.6%) |
| Middle | 1000 | 0.052 (5.2%) |
| Generous | 2000 | 0.104 (10.4%) |

**These are per-target probabilities.** With ~30 physical constants to try
and ~3 unit conventions each (~90 targets total), the probability that
SOME depth-4 formula matches SOME constant at 26 ppm is virtually 100%.

---

## 3. Look-Elsewhere Effect

### 3.1 Target Selection Bias

The analyst can choose from ~30+ fundamental constants:
G, c, h, hbar, k_B, e, m_e, m_p, m_n, alpha, alpha_s, sin^2(theta_W),
G_F, Lambda_QCD, m_u, m_d, m_s, m_c, m_b, m_top, m_tau, m_mu, m_W, m_Z,
m_H, v_Higgs, f_pi, rho_Lambda, H_0, T_CMB, ...

Each can be expressed in multiple unit systems (SI, natural, eV, CGS).

**Effective number of targets: ~90**

### 3.2 Expected Random Matches Across All Targets

Using N_eff = 50,000 distinct depth-4 values (conservative):

| Tolerance | E[matches per target] | E[total across 90 targets] |
|-----------|----------------------|---------------------------|
| 1 ppm | 0.10 | 9 |
| 5 ppm | 0.50 | 45 |
| 19 ppm | 1.90 | 171 |
| 26 ppm | 2.60 | 234 |
| 50 ppm | 5.00 | 450 |
| 100 ppm | 10.00 | 900 |

**At 26 ppm tolerance with 90 targets: ~234 expected random matches.**

Finding ONE formula matching G at 26 ppm is entirely expected.

---

## 4. Particle Mass Claims

### 4.1 Precision vs Experimental Uncertainty

| Particle | Claimed precision | Experimental uncertainty | Ratio |
|----------|------------------|------------------------|-------|
| m_top | 0.4 ppm | 1,737 ppm (+-0.30 GeV) | 4,343x overclaim |
| m_tau | 1.3 ppm | 68 ppm (+-0.12 MeV) | 52x overclaim |
| m_W | 0.8 ppm | 149 ppm (+-12 MeV) | 186x overclaim |
| G | 25.8 ppm* | 22 ppm | 1.2x (comparable) |

*Using CODATA 2018; 7.2 ppm using CODATA 2014.

### 4.2 The Overclaim Problem

**m_top at 0.4 ppm**: The top quark mass is known experimentally to ~0.17%.
Claiming a formula matches it to 0.00004% means:
- The formula "predicts" a value 4,343x more precise than any measurement
- If the experimental value shifts by 0.1% (well within error bars), the
  "0.4 ppm match" becomes a "1000 ppm miss"
- **This match is UNFALSIFIABLE** -- you cannot verify 0.4 ppm precision
  on a quantity known only to 1,737 ppm

**m_W at 0.8 ppm**: Similar issue. The W mass has been contentious
(CDF II vs world average discrepancy). Claiming 0.8 ppm on a quantity
known to ~149 ppm is a 186x overclaim.

**m_tau at 1.3 ppm**: The tau lepton mass is among the better-known
particle masses, but still only to 68 ppm. A 1.3 ppm claim is 52x
beyond verification.

### 4.3 Statistical Expectation for Sub-ppm Matches

From ~50,000 depth-4 distinct values:
- E[matches at 0.4 ppm per target] = 50000 * 2 * 0.4e-6 = 0.04
- E[matches at 1.3 ppm per target] = 50000 * 2 * 1.3e-6 = 0.13
- E[matches at 0.8 ppm per target] = 50000 * 2 * 0.8e-6 = 0.08

Individually, these are low probability (~4%, 12%, 8% per target).
**But across 90 targets:**
- E[total sub-1-ppm matches] = 90 * 0.04 = 3.6
- E[total sub-2-ppm matches] = 90 * 0.13 = 11.7

**Finding 3-4 sub-ppm matches across all targets is expected by chance.**

---

## 5. Specific Structural Criticisms

### 5.1 tau^J2 = 4^24 = 2^48 is a "Universal Denominator"

2^48 = 2.815e+14. This is simply a large power of 2.

**Any** quantity of order 10^{-11} can be written as:
```
quantity = (integer near 18786) / 2^48
```
The 7 n=6 constants provide enough algebraic raw material to hit integers
near 18786 with ~32 ppm resolution (as shown by the stepping table in Section 1.2).

**This is not a derivation of G from number theory. It is a repackaging of
G as a rational number with denominator 2^48, then noting that the numerator
is expressible from small integers.**

### 5.2 sopfr^sopfr = 5^5 Lacks Structural Motivation

Why should the gravitational constant involve "the sum of prime factors of 6,
raised to the power of itself"? There is no physical argument connecting:
- The factorization 6 = 2 * 3 (which gives sopfr = 5)
- Self-exponentiation (5^5)
- Newton's gravitational constant

The operation a^a applied to small integers produces: 1, 4, 27, 256, 3125, 46656.
Of these, 3125 happens to be within 0.2% of the numerator needed for G / (6/4^24).
This is a coincidence, not a derivation.

### 5.3 The Formula Has No Predictive Power

A meaningful formula would:
1. Be derived from a physical theory
2. Predict G more precisely than experiment
3. Be falsifiable by future measurements

This formula fails all three:
1. No derivation -- it was found by search
2. Its precision (7-26 ppm depending on G reference) is comparable to, not better than,
   experimental uncertainty (22 ppm)
3. Different G reference values give 7-332 ppm -- the formula does not resolve the
   tension between G measurements

---

## 6. Depth-4 vs Simpler Formulas

### 6.1 No Depth-2 or Depth-3 Formula Matches G

Exhaustive search confirms: no depth-2 expression (c1 op c2) matches G within
1000 ppm. No depth-3 expression (unary applied to depth-2) matches within 100 ppm.

**This is expected**: G ~ 6.674e-11 requires a very large denominator,
which only appears at depth-2+ via exponentiation. The need for depth-4
does not make the match more impressive -- it simply reflects the scale
mismatch between G and small-integer arithmetic.

### 6.2 Suspicion Principle

If a formula only works at depth-4, it means:
- The search space is ~1.5M expressions
- More chances to find accidental matches
- The formula is harder to falsify or motivate physically

A genuine deep connection would more likely manifest at low depth
(like sigma(n)*phi(n) = n*tau(n), which is depth-2 and proved unique).

---

## 7. Summary Verdicts

### G = (sopfr^sopfr + n) * n / tau^J2

| Criterion | Assessment | Grade |
|-----------|------------|-------|
| Numerical accuracy | 7.2-25.8 ppm (reference-dependent) | WEAK |
| Statistical significance | E[random match] ~ 2-3 per target at this tolerance | **FAIL** |
| Look-elsewhere correction | ~234 random matches expected across 90 targets | **FAIL** |
| Structural motivation | sopfr^sopfr has no physical justification | **FAIL** |
| Fine-tuning | "+n" term steps through G in 32 ppm increments | **FAIL** |
| Predictive power | Does not resolve G measurement tensions | **FAIL** |
| Falsifiability | Within experimental uncertainty (barely) | NEUTRAL |

**OVERALL: NOT SIGNIFICANT.** Expected by chance from the search space.
The claimed "19 ppm" is reference-dependent (actually 7-26 ppm).

### Particle Masses (m_top, m_tau, m_W)

| Criterion | Assessment | Grade |
|-----------|------------|-------|
| Numerical accuracy | 0.4-1.3 ppm (claimed) | Unverifiable |
| Precision vs measurement | 52x to 4343x beyond experimental capability | **FAIL** |
| Statistical significance (individual) | 4-12% per target | WEAK |
| Look-elsewhere correction | ~12 sub-2-ppm matches expected across 90 targets | **FAIL** |
| Falsifiability | Cannot be tested at claimed precision | **FAIL** |

**OVERALL: OVERCLAIMS.** The formulas match central estimates of poorly-known
quantities to precision far beyond measurement capability. Finding ~4 such
matches across 90 targets is statistically expected.

### Combined Assessment

The depth-4 discoveries do not survive red-team analysis. The key failure modes:

1. **Search space is too large.** ~1.5M formal expressions, ~50K distinct values.
   At any reasonable tolerance, multiple random matches are expected per target.

2. **Look-elsewhere effect is devastating.** With ~90 candidate targets, hundreds
   of matches are expected at 20+ ppm tolerance.

3. **Precision claims are unverifiable.** Sub-ppm claims for quantities known to
   hundreds or thousands of ppm cannot be tested.

4. **No physical motivation.** The formulas are found by search, not derived.
   sopfr^sopfr, tau^J2, and the "+n" adjustment have no physical interpretation.

5. **Reference cherry-picking.** The G claim of "19 ppm" depends on which G
   measurement is used; against CODATA 2018 it is 25.8 ppm (outside 1-sigma).

**Recommendation: Classify all depth-4 physical constant matches as
NUMEROLOGICAL COINCIDENCES. Do not include in atlas-constants.md or
breakthrough theorems. The z-score methodology from red-team-formula-miner.md
already established this -- depth-4 simply amplifies the search space problem.**
