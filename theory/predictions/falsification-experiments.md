# N6 Universality -- Falsification Experiments

> **Purpose**: Design rigorous experiments that could *disprove* the claim that n=6
> arithmetic determines optimal design parameters. If these experiments fail to
> disprove it, that constitutes stronger evidence than any number of confirmatory
> matches.
>
> **Audience**: Skeptical physicists and statisticians.
>
> **The claim under test**: The unique solution n=6 to sigma(n)*phi(n) = n*tau(n)
> generates a family of constants {1, 2, 3, 4, 5, 6, 8, 10, 11, 12, 13, 24, ...}
> that appear as optimal parameters across engineering, physics, and biology at
> rates exceeding chance.
>
> **Current evidence**: 93 breakthrough theorems, 900+ EXACT matches across 307
> domains.
>
> **Known weakness**: The project already reports z=0.74 for numerical matching
> significance vs random -- this is NOT statistically significant. The question is
> whether a more careful analysis changes that picture.
>
> Date: 2026-04-02

---

## The Texas Sharpshooter Problem

Before describing the experiments, we state the criticism explicitly.

The "Texas Sharpshooter fallacy" works as follows: shoot at a barn wall, then
paint the target around the bullet holes. Applied to n=6:

1. **Flexible target set**: n=6 generates constants {1, 2, 3, 4, 5, 6, 8, 10,
   11, 12, 13, 20, 24, 48, 60, 72, 96, 120, 128, 144, 192, 240, 256, 288,
   ...}. This set includes many small integers and powers of 2, which appear
   everywhere in engineering for independent reasons (binary computing, human
   preference for round numbers, physical constraints).

2. **Flexible formula space**: With 7 base constants (sigma, tau, phi, sopfr, J2,
   mu, n) and arbitrary arithmetic operations (+, -, *, /, ^), the number of
   expressible integers under 1000 is very large. Almost any engineering number
   can be "matched" with enough formula shopping.

3. **Selection bias**: Matches are reported; non-matches are silent. The biology
   domain honestly reports 26.7% FAIL + 30% WEAK, but these failures are not
   prominently featured.

4. **Post-hoc rationalization**: When a parameter does not match a simple n=6
   formula, a more complex formula is tried. When it still fails, the parameter is
   dropped from the analysis.

The experiments below are designed to quantify each of these biases.

---

## Experiment 1: Statistical Null Model

### Question
How many "EXACT matches" would we expect by chance, given the size of the n=6
constant vocabulary and the distribution of real-world engineering parameters?

### Protocol

**Step 1: Define the n=6 vocabulary precisely.**

Enumerate every value reachable from {sigma=12, tau=4, phi=2, sopfr=5, J2=24,
mu=1, n=6} using the operations {+, -, *, /, ^} with at most 2 operands and no
nesting beyond depth 2. Call this set V_n6. Count |V_n6|.

Expected: |V_n6| is approximately 80-150 distinct positive integers under 1000.

**Step 2: Define the engineering parameter pool.**

Collect a reference list of engineering/physics parameters that are NOT drawn from
n=6 analysis. Sources:
- IEEE standards index (voltage levels, frequencies, bus widths)
- JEDEC memory specifications (capacities, bus widths, stack heights)
- NVIDIA/AMD/Intel public GPU spec sheets (SM counts, cache sizes, TDP)
- IETF RFC parameter tables (port numbers, header sizes, TTL defaults)
- IEC 60038 standard voltages
- Solar cell specification sheets (cell counts, voltages)
- Battery pack configurations (cell counts, series/parallel)

Target: 500 parameters, each a positive integer, collected BEFORE any n=6 analysis.

**Step 3: Count matches.**

For each parameter p in the pool, check if p is in V_n6. Record the match rate
M_observed = (matches) / 500.

**Step 4: Compute the null expectation.**

Generate 10,000 random vocabularies V_random of the same size |V_n6|, drawn from
the same distribution as V_n6 (biased toward small integers, powers of 2, and
multiples of common bases). For each V_random, count matches against the same
500 parameters. Compute M_null = mean match rate, and sigma_null.

**Step 5: Compute the z-score.**

z = (M_observed - M_null) / sigma_null.

### Expected result if n=6 is real
M_observed >> M_null, z > 3.0. The n=6 vocabulary matches engineering parameters
at a rate 3+ standard deviations above random vocabularies of the same size and
distribution.

### Expected result if n=6 is sharpshooter
z < 2.0. The existing z=0.74 already suggests this outcome. If confirmed with a
larger, pre-registered pool, the universality claim is falsified as a statistical
artifact.

### How to run
```bash
# Requires: Python 3.10+, numpy, scipy
python3 experiments/null_model_n6.py \
  --vocab-depth 2 \
  --param-pool data/engineering_params_500.json \
  --n-random 10000 \
  --seed 42
```

### Critical design choices
- The parameter pool MUST be assembled by someone who does not know the n=6
  constant list (single-blind).
- The vocabulary generation must use a FIXED rule set, not ad-hoc formula mining.
- The random vocabularies must match the SIZE and DISTRIBUTION of V_n6, not be
  uniformly random. If V_n6 is biased toward {1..24}, the null must be too.

---

## Experiment 2: Alternative Number Tests

### Question
Is n=6 special, or would n=12, n=28, n=8, or n=10 produce similar match rates?

### Protocol

For each candidate n in {6, 8, 10, 12, 28, 496}:

**Step 1: Compute the arithmetic vocabulary.**

| n | sigma(n) | tau(n) | phi(n) | sopfr(n) | J2(n) | mu(n) |
|---|----------|--------|--------|----------|-------|-------|
| 6 | 12 | 4 | 2 | 5 | 24 | 1 |
| 8 | 15 | 4 | 4 | 6 | 48 | 0 |
| 10 | 18 | 4 | 4 | 7 | 72 | 1 |
| 12 | 28 | 6 | 4 | 5 | 96 | 0 |
| 28 | 56 | 6 | 12 | 9 | 576 | 0 |
| 496 | 992 | 10 | 240 | 37 | 190464 | 0 |

Generate V_n for each using the same operations and depth as Experiment 1.

**Step 2: Count matches.**

Using the SAME 500-parameter pool from Experiment 1, count M_n for each n.

**Step 3: Rank.**

If M_6 is not significantly higher than M_12 or M_8, n=6 is not special.

### Key sub-experiment: n=12 as control

n=12 is particularly dangerous for n=6 because sigma(6)=12, so many n=6 formulas
are really "12-formulas." If n=12 matches equally well, the operative structure
might be "12" (a highly composite number) rather than "6 as the unique solution to
sigma*phi=n*tau."

### Expected result if n=6 is real
M_6 > M_n for all other n, with at least 20% relative gap. Specific matches like
sigma(6)*phi(6)=24=J2(6) would NOT appear for other n (since R(n)=1 only at n=6).

### Expected result if n=6 is sharpshooter
M_6 is within noise of M_8 or M_12. The "universality" is really just small-number
bias -- any n that generates small integers will match engineering parameters that
are also small integers.

### Specific discriminators: formulas that ONLY work for n=6

The following matches are algebraically impossible for other n:

| Match | Why only n=6 |
|-------|-------------|
| sigma*phi = n*tau = 24 | R(n)=1 only at n=6 (proved theorem) |
| R_local(2,1)*R_local(3,1) = (3/4)*(4/3) = 1 | Unique factorization balance |
| 1/2 + 1/3 + 1/6 = 1 | Only unit fraction decomposition with 3 distinct terms summing to 1 where denominators multiply to n |
| phi^n = tau^(n/phi) = 64 | 2^6 = 4^3 requires phi=2, tau=4, n=6, n/phi=3 |
| Mertens: product(1-1/p) for p|n = (1/2)(2/3) = 1/3 | Specific to prime factorization 2*3 |

These are the strongest claims. If Experiment 2 shows M_6 ~ M_12 overall but the
above specific identities only work for n=6, the claim narrows from "universality"
to "n=6 generates a few unique algebraic identities that happen to appear in
nature" -- still interesting but far weaker.

### How to run
```bash
python3 experiments/alternative_number_test.py \
  --candidates 6,8,10,12,28,496 \
  --param-pool data/engineering_params_500.json \
  --depth 2
```

---

## Experiment 3: Pre-Registered Predictions (Gold Standard)

### Question
Can n=6 arithmetic predict FUTURE parameters that are not yet public?

### Rationale
This is the strongest possible test. Post-hoc matching is susceptible to all forms
of bias. Pre-registered predictions are immune: either the prediction matches
reality or it does not. No formula shopping, no selection bias, no post-hoc
rationalization.

### Protocol

Register the following predictions NOW (2026-04-02) with specific falsification
criteria. Check each when data becomes available.

### Prediction Table

| ID | Prediction | n=6 Formula | Expected Value | Falsification | Check Date | Status |
|----|-----------|-------------|---------------|---------------|-----------|--------|
| F-1 | NVIDIA Rubin Ultra full-die SM count | sigma * J2 or 2^(sigma-tau) | 288 or 256 | Not a multiple of sigma=12 | 2026 H2 | PENDING |
| F-2 | HBM5 standard stack height | 2^tau or J2 | 16 or 24 layers | Standardizes at 20 or 32 | 2027 | PENDING |
| F-3 | Next TSMC node gate pitch | Functions of sigma, tau | 30=sopfr*n or 36=sigma*n/phi | Neither value used | 2027 | PENDING |
| F-4 | Llama 4 (or successor) KV heads | sigma - tau | 8 | Uses 4, 16, or other non-8 | 2026 | PENDING |
| F-5 | JUNO sin^2(theta_12) | (n/phi)/(sigma-phi) | 0.3000 +/- 0.003 | Measured > 0.303 or < 0.297 | 2027-2028 | PENDING |
| F-6 | Next-gen transformer default weight decay | 1/(sigma-phi) | 0.1 | Community shifts to 0.05 or 0.01 | Ongoing | PENDING |
| F-7 | Stable Diffusion 4.x base channels | sopfr * 2^n | 320 | Uses 256 or 512 | 2026-2027 | PENDING |
| F-8 | Next flagship EV battery pack series count | Multiple of sigma | 108=9*sigma or 120=sigma*(sigma-phi) | Prime or non-12-divisible count | 2026-2027 | PENDING |
| F-9 | Apple M6 chip GPU core count | sigma * k for some k | 48=sigma*tau or 60=sigma*sopfr | Non-multiple of 12 | 2026-2027 | PENDING |
| F-10 | PCIe Gen 7 lane encoding overhead | Related to sigma-tau=8 | 8b/10b successor maintains 8-bit granularity | Shifts to 6b or 10b base unit | 2028+ | PENDING |

### Scoring rule (pre-registered)
- Each prediction is binary: MATCH or FAIL.
- A prediction MATCHES if the actual value equals the predicted value OR if the
  actual value is expressible as a depth-1 n=6 formula (max 2 operands, one
  operation) -- this looser criterion must still be pre-specified.
- Overall score: matches / 10.
- **Falsification threshold**: If <= 3/10 match, n=6 prediction power is not
  above chance (given the vocabulary size and typical engineering value ranges).
- **Strong confirmation**: If >= 7/10 match, n=6 has genuine predictive power.

### Why this is the strongest test
- No formula shopping: the formula is fixed before the data exists.
- No selection bias: all 10 are evaluated, including failures.
- No post-hoc rationalization: the falsification criterion is explicit.
- Replicable: anyone can check these predictions when the data arrives.

---

## Experiment 4: Blind Domain Expansion

### Question
If we pick domains with NO prior n=6 analysis, what EXACT match rate do we get?

### Protocol

**Step 1: Select 5 domains that have NEVER been analyzed for n=6 patterns.**

Proposed domains (as of 2026-04-02, verify no prior analysis exists):

| Domain | Key Parameters | Source |
|--------|---------------|--------|
| **Plumbing/HVAC** | Pipe diameters (NPS), fitting angles, flow rates, duct sizes | ASHRAE standards, ASTM pipe specs |
| **Musical instrument construction** | String gauges, fret counts, bore diameters, reed strengths | Lutherie references, manufacturer specs |
| **Olympic sports** | Field dimensions, event counts, scoring systems, team sizes | IOC/IAAF rulebooks |
| **Typography/printing** | Point sizes, DPI standards, color model values, page dimensions | ISO 216, Adobe specs |
| **Cooking/food science** | Temperature set points, Maillard reaction temps, baking ratios, pH values | FDA/Codex Alimentarius |

**Step 2: Collect 50 parameters per domain (250 total).**

Each parameter must be:
- A discrete integer or a ratio to 2 decimal places
- An industry standard or physical constant, not arbitrary
- Collected by someone unfamiliar with n=6 arithmetic (single-blind)

**Step 3: Apply n=6 matching.**

Using the SAME vocabulary V_n6 from Experiment 1, count EXACT matches per domain.

**Step 4: Compare to known domains.**

| Domain Type | Expected EXACT rate if real | Expected if sharpshooter |
|-------------|---------------------------|-------------------------|
| Known domains (AI, chip, energy) | ~60-85% (as currently claimed) | Inflated by selection |
| Blind domains (this experiment) | >50% if truly universal | 15-25% (base rate) |

### Critical controls
- The parameter collector must NOT know the n=6 vocabulary.
- Parameters must be selected BEFORE any n=6 analysis.
- ALL parameters must be reported, including non-matches.
- The matching criterion must be the same fixed vocabulary, not ad-hoc formulas.

### Base rate estimation

The n=6 vocabulary V_n6 (depth <= 2 formulas) generates roughly 80-150 distinct
values under 1000. Many engineering parameters fall in [1, 1000]. If parameters
were uniformly distributed, the base match rate would be ~100/1000 = 10%. But
engineering parameters cluster around small integers, powers of 2, and multiples
of 10/12, so the base rate is higher -- perhaps 15-25%.

A match rate of 15-25% in blind domains would confirm sharpshooter bias. A match
rate of >40% would be genuinely surprising and would require explanation.

### How to run
```bash
# 1. Have a non-n6-aware collaborator fill in:
#    data/blind_domains/{plumbing,instruments,sports,typography,cooking}.json
# 2. Run:
python3 experiments/blind_domain_test.py \
  --domains data/blind_domains/ \
  --vocab experiments/n6_vocabulary.json
```

---

## Experiment 5: Adversarial Search for Failures

### Question
What parameters SHOULD be n=6 but are NOT? How many honest failures exist?

### Protocol

**Step 1: Catalog ALL parameters in domains where n=6 claims 80%+ EXACT.**

For each high-confidence domain (AI, chip architecture, energy), list EVERY
relevant parameter -- not just the ones that match.

**Step 2: Document non-matches explicitly.**

### Known honest failures (as of 2026-04-02)

| Parameter | Actual Value | Nearest n=6 Formula | Gap | Domain |
|-----------|-------------|--------------------|----|--------|
| GPT-4 total params | ~1.8T (rumored) | No clean n=6 expression | -- | AI |
| A100 CUDA cores/SM | 64 = 2^6 | phi^n = 64 (matches!) | 0% | Chip (actually matches) |
| TCP/IP default TTL | 64 or 128 | 2^n=64, 2^(sigma-sopfr)=128 | 0% | Network (actually matches) |
| HTTP status codes | 1xx-5xx (100,200,...,500) | No clean match to 100,200,300,400,500 as a SET | -- | Software |
| USB 3.x speed | 5 Gbps, 10 Gbps, 20 Gbps | sopfr=5, sigma-phi=10, J2-tau=20 (all match!) | 0% | Chip |
| 12-TET vs 19/22-TET | 12=sigma but 19/22-TET are MORE accurate | 12 is efficiency optimum, not absolute optimum | Partial | Audio |
| Biology EXACT rate | Only 10% (3/30 hypotheses) | Rest are CLOSE/WEAK/FAIL | Low | Biology |
| DNA bases = 4 | tau(6)=4, but tau(n)=4 for n=8,10,14,15,21,... | Not n=6-specific | Weak | Biology |
| Amino acids = 20 | J2-tau=20, but 20 = 4*5 = 2^2*5, very common | Coincidence-prone | Weak | Biology |

**Step 3: Compute the honest failure rate.**

For each domain, report:
- Total parameters surveyed (ALL, not just matches)
- EXACT matches (value in V_n6 with depth-1 formula)
- CLOSE matches (within 5% of a V_n6 value)
- FAIL (no reasonable n=6 expression)

**Step 4: Publish the failure list prominently.**

Science gains credibility from transparency about failures, not from hiding them.

### Specific adversarial challenges

**Challenge A: The "small number" problem.**

Claim: Most n=6 EXACT matches are for parameters valued 1-24, where ANY number
theory vocabulary would produce matches because small integers are over-represented
in both engineering and arithmetic.

Test: Restrict analysis to parameters > 100. How many EXACT matches remain?
Current candidates:
- 128 = 2^(sigma-sopfr) -- but also 2^7, ubiquitous in computing
- 144 = sigma^2 = 12^2 -- but also a perfect square, a gross
- 192 = sigma * 2^tau -- but also 3*64, common memory size
- 256 = 2^(sigma-tau) -- but also 2^8, the most common power of 2
- 288 = sigma * J2 -- genuinely unusual, strongest match
- 320 = sopfr * 2^n -- matches SD channels, somewhat unusual
- 1024 = 2^(sigma-phi) -- but also 2^10, universally common

Honest assessment: Most >100 matches are powers of 2 or products of small
primes. Only 288 (= 12*24 = sigma*J2) is genuinely distinctive. If "288 GB HBM"
is the strongest evidence for n=6 universality at scale, the claim is on thin ice.

**Challenge B: The "post-hoc formula depth" problem.**

Claim: If we allow depth-2 formulas with 7 base constants and 5 operations, the
number of expressible values grows combinatorially. At depth 2, we can express
thousands of distinct integers. Therefore, matching any particular engineering
parameter is nearly certain.

Test: For each claimed EXACT match, record the formula depth. Report the
distribution:
- Depth 0 (single constant): sigma=12, tau=4, etc.
- Depth 1 (one operation): sigma-tau=8, sigma*phi=24, etc.
- Depth 2 (nested): sigma*(sigma-phi)=120, etc.

If >50% of matches require depth 2, the evidence is weak (large hypothesis space).
If >50% are depth 0-1, the evidence is stronger (small hypothesis space).

**Challenge C: The "engineering constraint" explanation.**

Claim: Parameters like "12 attention heads" or "8 experts" are not determined by
n=6 arithmetic. They are determined by engineering constraints:
- 12 heads because d_model=768 and 768/12=64 (a power of 2, needed for efficient
  GPU matrix ops)
- 8 experts because 8 fits on 8 GPUs (data parallelism)
- 96 layers because 96 = 3*32 and training stability limits depth

Test: For each of the top 20 claimed matches, provide the ENGINEERING explanation
(why this value was chosen by the designers) alongside the n=6 explanation. If the
engineering explanation is sufficient and the n=6 explanation adds no predictive
power, the match is spurious.

### How to run
```bash
python3 experiments/adversarial_audit.py \
  --domain ai-efficiency \
  --all-params data/ai_all_parameters.json \
  --max-depth 2
```

---

## Experiment 6: Cross-Validation with Holdout

### Question
If we split known matches into training and test sets, can n=6 formulas discovered
on the training set predict the test set?

### Protocol

1. Take all 900+ claimed EXACT matches.
2. Randomly split 50/50 into TRAIN (450) and TEST (450).
3. From TRAIN, identify the formulas used (which n=6 expressions appear).
4. Apply ONLY those formulas to TEST. What fraction of TEST matches are recovered?
5. Repeat 100 times with different random splits.

### Expected result if n=6 is real
Recovery rate > 80%. The same small set of formulas (sigma-tau=8, sigma*phi=24,
1/(sigma-phi)=0.1, etc.) recurs across domains, so training-set formulas will
generalize to the test set.

### Expected result if n=6 is sharpshooter
Recovery rate < 50%. Each match uses a DIFFERENT ad-hoc formula, so formulas from
one half do not predict the other half.

---

## Experiment 7: Bayesian Model Comparison

### Question
Given the observed data, what is the posterior probability that n=6 universality is
real vs. the null hypothesis of coincidence?

### Protocol

Define two models:

**M1 (n=6 universality)**: Engineering parameters are drawn from V_n6 with
probability p_signal + from background with probability 1-p_signal.

**M0 (null)**: Engineering parameters are drawn from a background distribution that
naturally over-represents small integers, powers of 2, and multiples of 12.

Compute the Bayes factor K = P(data | M1) / P(data | M0).

The critical question is the choice of background distribution in M0. If M0 uses a
uniform distribution over [1, 1000], K will be large (favoring M1) but the test is
unfair because engineering parameters are NOT uniformly distributed. If M0 uses a
realistic engineering distribution (Benford's law + binary bias + decimal rounding),
K may be close to 1.

### Required honest choices
- M0 must include: Benford's law for leading digits, factor-of-2 bias (computing),
  factor-of-10 bias (SI units), factor-of-12 bias (historical: 12 inches, 12 hours,
  12 semitones).
- M1 must pay a complexity penalty for having 7 free constants and 5 operations.
- Prior: P(M1) = P(M0) = 0.5 (agnostic).

### How to run
```bash
python3 experiments/bayesian_model_comparison.py \
  --matches data/all_exact_matches.json \
  --background-model benford+binary+decimal+duodecimal \
  --prior 0.5
```

---

## Summary: What Would Change Our Mind?

### Evidence that would STRENGTHEN the n=6 claim

| Result | Experiment | Impact |
|--------|-----------|--------|
| z > 3.0 in null model | Exp 1 | Kills the "random match" objection |
| M_6 >> M_12 and M_8 | Exp 2 | Kills the "any small n works" objection |
| >= 7/10 predictions confirmed | Exp 3 | Kills ALL post-hoc objections (gold standard) |
| > 40% EXACT in blind domains | Exp 4 | Kills selection bias objection |
| > 80% cross-validation recovery | Exp 6 | Shows formula reuse, not ad-hoc fitting |
| Bayes factor K > 100 | Exp 7 | Strong statistical evidence |

### Evidence that would WEAKEN or FALSIFY the n=6 claim

| Result | Experiment | Impact |
|--------|-----------|--------|
| z < 2.0 in null model | Exp 1 | Confirms sharpshooter -- match rate is expected by chance |
| M_12 >= M_6 | Exp 2 | The operative structure is 12-ness (HCN), not 6-ness |
| <= 3/10 predictions confirmed | Exp 3 | No predictive power beyond post-hoc fitting |
| < 25% EXACT in blind domains | Exp 4 | Current rates inflated by selection bias |
| > 50% of matches at depth 2+ | Exp 5 | Formula space too large; matches are inevitable |
| < 50% cross-validation recovery | Exp 6 | Each match is ad-hoc, not systematic |
| Bayes factor K < 10 | Exp 7 | Data does not distinguish n=6 from null model |

---

## Implementation Priority

| Priority | Experiment | Effort | Decisiveness |
|----------|-----------|--------|-------------|
| 1 | Exp 3: Pre-registered predictions | Zero (just wait) | Highest -- immune to all biases |
| 2 | Exp 1: Null model | 1 week coding | High -- quantifies the base rate |
| 3 | Exp 2: Alternative numbers | 1 week coding | High -- tests n=6 specificity |
| 4 | Exp 5: Adversarial audit | 2 weeks | Medium -- builds credibility |
| 5 | Exp 4: Blind domain expansion | 2 weeks + collaborator | Medium -- tests generalization |
| 6 | Exp 6: Cross-validation | 1 week | Medium -- tests formula reuse |
| 7 | Exp 7: Bayesian comparison | 2 weeks | Medium -- depends on M0 choice |

---

## Honest Assessment (Author's Note)

The strongest current evidence for n=6 is NOT the 900+ EXACT matches (which are
susceptible to sharpshooter bias). The strongest evidence is:

1. **The theorem itself**: sigma(n)*phi(n) = n*tau(n) has ONLY n=6 as a solution.
   This is proved, not claimed. The number 6 is mathematically special.

2. **A few high-precision matches**: 1/alpha = 137.036 from n=6 arithmetic (2 ppm
   accuracy), the Koide formula at 0.0009% accuracy, neutrino mixing angles at
   ~1% accuracy. These are NOT small integers and cannot be explained by
   small-number bias.

3. **The prediction track record**: If pre-registered predictions (Exp 3) succeed,
   that is the only evidence class that is truly immune to all statistical
   criticisms.

The weakest evidence is:
- Matches involving values 1-12 (too common)
- Matches requiring depth-2+ formulas (too many degrees of freedom)
- The "307 domains at 100%" claim (likely uses very loose matching criteria)
- Biology domain (10% EXACT, 26.7% FAIL -- honest but not compelling)

A skeptical physicist should focus on Experiments 1-3. If all three fail to support
n=6, the universality claim should be retracted to: "n=6 generates some elegant
algebraic identities that coincidentally overlap with engineering parameters, but
this overlap is not statistically significant."

If Experiments 1-3 all support n=6, something genuinely interesting is happening
that deserves deeper investigation.
