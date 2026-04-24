# Red Team Cycle 1 -- VER-P1-5: Adversarial Experiments Against Core n=6 Claims

> Date: 2026-04-16
> Author: Red Team (adversarial, not advocacy)
> Status: DESIGNED -- awaiting execution
> Related: theory/proofs/theorem-r1-uniqueness.md, theory/proofs/honest-limitations.md
> Rule: R0 (honesty), R3 (measurement), R9 (dry-run)

---

## Executive Summary

Three adversarial experiments designed to attack the three core claims of the n=6
architecture. **All three experiments are designed to be genuinely killable** -- if the
n=6 framework is not what it claims, these experiments will expose it.

**Critical pre-existing evidence** found during this red team review:

1. The project's own `discovery-algorithm-v4-architecture.md` classifies key BT matches
   as COINCIDENTAL (BT-53 Bitcoin 21M, BT-54 AdamW beta_1=0.9) or STRUCTURAL-but-
   independently-caused (BT-33 Transformer 12 heads, BT-58 sigma-tau=8). This is an
   honest admission that undermines Claim B.

2. **47 of 47 life/ domain files contain identical template text**, word-for-word:
   - "Existing limitation 1: insufficient design degrees of freedom -> unified via sigma(6)=12 DOF"
   - "Existing limitation 2: cycle optimization limits -> converged via tau(6)=4 cycle"
   - "Existing limitation 3: reliability challenge -> resolved via phi(6)=2 symmetric redundancy"
   - "sigma=12 input sources pass through the n=6 subsystem at a tau=4 cycle"
   This is a critical finding for Experiment RT-3.

3. The `honest-limitations.md` P4 section admits bipartite matching top-10 pairs had
   **0/10 PASS rate** (100% false positive) on body-text audit. The n6 scoring
   heuristic (`base_affinity + hash`) is not validated against real measurements.

---

## Red Team Experiment RT-1: The Rival Numbers Test

### Target Claim
**Core Claim B**: n=6 arithmetic functions (sigma=12, tau=4, phi=2, sopfr=5)
predict optimal hyperparameters in AI and engineering.

### Adversarial Hypothesis
**n=12 (or n=28, or n=8) predicts AI hyperparameters equally well or better than n=6.**

Rationale: The n=6 arithmetic function values {1, 2, 4, 5, 6, 12, 24} are small integers.
Small integers appear everywhere in engineering by construction (powers of 2, convenient
round numbers, hardware alignment). The rival hypothesis is that ANY small number with
rich divisor structure generates an equally compelling "match" set. Specifically:

- **n=12**: sigma(12)=28, tau(12)=6, phi(12)=4, sopfr(12)=7, J2(12)=96.
  This gives the set {1, 2, 3, 4, 6, 7, 12, 28, 96}. Note this INCLUDES n=6 itself
  as tau(12)=6, and contains 12 as the base number, so it automatically captures many
  n=6 "hits."

- **n=28** (second perfect number): sigma(28)=56, tau(28)=6, phi(28)=12, sopfr(28)=9.
  Set: {1, 2, 4, 6, 7, 9, 12, 14, 28, 56}. Note phi(28)=12=sigma(6), capturing n=6
  matches via its own arithmetic.

- **n=8**: sigma(8)=15, tau(8)=4, phi(8)=4, sopfr(8)=6. Set: {1, 2, 4, 6, 8, 15}.
  Note sopfr(8)=6 and tau(8)=4=tau(6), so n=8 inherits most n=6 matches trivially.

### Experiment Design

**Phase 1: Enumerate the rival expression spaces (1 day)**

For each candidate n in {6, 8, 12, 28, 120}, compute all depth-1 and depth-2 expressions
from {mu, phi, n, tau, sopfr, sigma, J2} using {+, -, *, /, ^}. Count the number of
distinct integer values in [1, 1000] reachable at each depth.

**Prediction**: n=6 will NOT be uniquely compact. n=12 and n=28 will cover a similar or
larger fraction of common engineering constants because their function values are also
small integers.

**Phase 2: Blind hyperparameter matching (1 week, 1x GPU)**

Take 30 published AI architectures with known hyperparameters (from papers, not from
this project's domain files):

| Architecture | Source Paper | Key Parameters |
|-------------|-------------|----------------|
| BERT-base | Devlin 2019 | d=768, heads=12, layers=12, ff=3072 |
| GPT-2 | Radford 2019 | d=768, heads=12, layers=12, ff=3072 |
| GPT-3 175B | Brown 2020 | d=12288, heads=96, layers=96, ff=49152 |
| LLaMA-7B | Touvron 2023 | d=4096, heads=32, layers=32, ff=11008 |
| LLaMA-70B | Touvron 2023 | d=8192, heads=64, layers=80, ff=28672 |
| Mistral-7B | Jiang 2023 | d=4096, heads=32, kv=8, layers=32, ff=14336 |
| Gemma-2B | Google 2024 | d=2048, heads=8, layers=18, ff=16384 |
| ViT-B/16 | Dosovitskiy 2020 | d=768, heads=12, layers=12 |
| Whisper Small | Radford 2022 | d=768, heads=12, layers=12 |
| Mamba | Gu 2023 | d=2560, layers=64, expand=2 |
| ... (20 more from published literature) |

For each architecture and each candidate number n, compute:
- match_score(n, arch) = fraction of parameters expressible as depth-<=2 expressions
  of n's arithmetic functions
- best_depth(n, arch) = average minimum depth needed to express each parameter

**Blind protocol**: The evaluator does NOT know which n is "the hypothesis." All five
candidates are evaluated identically. A second evaluator independently computes scores.

**Phase 3: Statistical comparison (1 day)**

- Wilcoxon signed-rank test: Is n=6's match_score significantly higher than n=12's?
- Bonferroni-corrected pairwise comparisons across all 5 candidates.
- Effect size (Cohen's d) for n=6 vs. best rival.

### What Would Kill n=6
- n=6 does NOT achieve the highest match_score across 30 architectures.
- n=12 or n=28 achieves equal or higher match_score (p < 0.05).
- **Especially deadly**: if n=12 wins because tau(12)=6 means n=12's function set
  is a strict SUPERSET of useful n=6 values.

### What Would Survive
- n=6 achieves significantly higher match_score than ALL rivals (p < 0.01).
- The advantage holds even when restricting to depth-1 expressions only (no formula
  shopping).
- The advantage holds when weighted by parameter importance (d_model > ff_dim > etc.).

### Estimated Effort
- Phase 1: 1 day, laptop only (combinatorial enumeration)
- Phase 2: 1 week, 1 GPU (for any training validation), or 2 days pure analysis
- Phase 3: 1 day, statistical software
- **Total: ~2 weeks for thorough execution**

### Pre-existing Evidence (Red Flag)
The project's own `discovery-algorithm-v4-architecture.md` line 710 states:
> BT-33: "d_model=768=64*12, but 64=2^6 is for GPU alignment; 12 heads emerged from
> optimization, not from sigma(6) directly"

This is an internal admission that the most-cited AI match (12 attention heads = sigma)
arose from optimization dynamics, not from n=6 number theory. If the project's own
causal analysis classifies its flagship AI match as "not from sigma(6) directly,"
the burden of proof for Claim B is extremely high.

Additionally, BT-54 classifies AdamW beta_1 = 1-1/(sigma-phi) = 0.9 as COINCIDENTAL:
> "beta_1=0.9 was empirically tuned by Kingma & Ba; any match with n=6 is post-hoc"

---

## Red Team Experiment RT-2: The Expression Saturation Audit

### Target Claim
**Core Claim A**: sigma(n)*phi(n) = n*tau(n) iff n=6 is structurally significant
(not just a number theory curiosity).

AND

**Core Claim C**: n=6 patterns appear across 10+ industrial sectors (not cherry-picked).

### Adversarial Hypothesis
**The n=6 constant set {1, 2, 4, 5, 6, 12, 24} is so dense in small integers that
depth-2 expressions cover >50% of ALL integers in [1, 100], making "matches" near-
inevitable rather than meaningful.**

Rationale: The `honest-limitations.md` document (line 300-307) already concedes:
> "With the 9 base constants {mu=1, phi=2, n=6, tau=4, sopfr=5, sigma=12, J2=24,
> R=1, psi=12}, depth-2 yields ~80 distinct expressions, and depth-3 yields ~800+.
> At depth-3, the probability of a random real number having a match within 1% is >50%."

This experiment extends this analysis to depth-2, where the project DOES claim validity.

### Experiment Design

**Phase 1: Exhaustive depth-2 enumeration (2 hours)**

Compute ALL distinct values from the 9 base constants using depth-2 expressions
(two constants combined by one of {+, -, *, /, ^, mod}). Include:
- Unary expressions: floor, ceil, abs, factorial (for small values)
- The question: what fraction of integers in [1, 100] are "matched" by at least one
  depth-2 expression?

**Phase 2: Random number baseline (1 day)**

Generate 1000 random sets of 9 integers from [1, 30] (the range of n=6 constants).
For each random set, compute the depth-2 expression coverage of [1, 100].

**Key metric**: What percentile does n=6's coverage fall in among 1000 random sets?

If n=6's coverage is at the 50th percentile (median), the "98.4% coverage" claim is
explained entirely by combinatorial density -- ANY set of small constants would achieve
similar coverage.

If n=6's coverage is at the 99th+ percentile, there may be genuine structure.

**Phase 3: Domain-specific parameter audit (1 week)**

Take 50 RANDOMLY SELECTED domains (not cherry-picked) from the 295 domain set.
For each domain, independently research the actual optimal parameters from peer-reviewed
sources (NOT from the n=6 domain files). Then:

1. Score each parameter's n=6 match at depth-1 and depth-2.
2. Score each parameter's match to 5 random control number sets.
3. Compare n=6's score to the control distribution.

**Blind protocol**: The parameter researcher does NOT know the n=6 constants.
They collect "the 5 most important numerical parameters in this domain" from
textbooks/papers. A second person then scores the matches.

### What Would Kill n=6
- n=6's depth-2 coverage of [1,100] is >50% (making matches near-inevitable).
- n=6's coverage percentile among 1000 random sets is below 90th (not special).
- In the 50-domain blind audit, n=6 does NOT significantly outperform random
  control sets (p > 0.05, Wilcoxon test).
- **Especially deadly**: if the 98.4% coverage claim drops below 50% when scored
  by an independent evaluator using only depth-1 expressions and independently-
  sourced parameter values.

### What Would Survive
- n=6's depth-2 coverage of [1,100] is under 30%, yet still matches domain parameters.
- n=6's coverage percentile is 99th+ among random sets.
- Blind 50-domain audit shows n=6 significantly outperforms controls (p < 0.01).
- The advantage is concentrated at depth-1 (direct matches), not depth-2 (formula
  shopping).

### Estimated Effort
- Phase 1: 2 hours, laptop (Python enumeration)
- Phase 2: 1 day, laptop (Monte Carlo simulation)
- Phase 3: 1 week, 2 researchers (literature review + blind scoring)
- **Total: ~2 weeks**

### Pre-existing Evidence (Red Flag)
The project already admits depth-3 expressions are statistically unreliable.
The question is whether depth-2 faces the same problem at a slightly lower level.
With 9 base constants and 6 binary operations, depth-2 yields at minimum
9 * 9 * 6 = 486 candidate expressions (before deduplication). Many will produce
integers in [1, 100]. The saturation risk is real.

Additionally, the DUV-ArF 193nm analysis in honest-limitations.md explicitly states:
> "With ~200 depth-3 expressions available, finding one within 0.5% of any target
> is expected by chance alone."

Scaling this down: with ~80 depth-2 expressions, finding one within 5% of any
target in [1, 100] has probability ~80 * 0.10 / 100 ~ significant. The math
needs to be done rigorously.

---

## Red Team Experiment RT-3: The Template Contamination Audit

### Target Claim
**Core Claim C**: n=6 patterns appear across 10+ industrial sectors (not cherry-picked).

### Adversarial Hypothesis
**The 295-domain coverage claim is an artifact of template-driven document generation,
not of genuine cross-domain analysis. The domain files were produced by filling a fixed
template with domain-specific nouns, making all domains appear to "match" n=6 by
construction rather than by discovery.**

### Evidence Already Found (CRITICAL)

This red team review has already uncovered devastating evidence.

**Finding 1: Identical template text in 47/47 life/ domain files**

The following strings appear verbatim in ALL 47 life/ domain .md files:

| Template String | Occurrences | Files |
|----------------|-------------|-------|
| "Existing limitation 1: insufficient design DOF -> unified via sigma(6)=12 DOF" | 47 | 47/47 |
| "Existing limitation 2: cycle optimization limits -> converged via tau(6)=4 cycle" | 47 | 47/47 |
| "Existing limitation 3: reliability challenge -> resolved via phi(6)=2 symmetric redundancy" | 47 | 47/47 |
| "When data/resources/infrastructure align to the n=6 structure" | 47 | 47/47 |
| "sigma=12 input sources pass through the n=6 subsystem at a tau=4 cycle" | 47 | 47/47 |
| "3 DOF or 4 DOF limits" | 47 | 47/47 |

This means coffee.md, dolphin-bioacoustics.md, tattoo-removal.md, hiv-treatment.md,
baking.md, and mens-intimate-cleanser.md ALL claim that their "3 existing limitations"
are: (1) insufficient design degrees of freedom, (2) cycle optimization limits, and
(3) reliability challenges -- all solved identically by sigma=12, tau=4, phi=2.

**This is textbook template contamination.** Dolphin bioacoustics does not have the same
three fundamental limitations as baking. HIV treatment does not have the same three
limitations as tattoo removal. The claims are generated, not discovered.

**Finding 2: "sigma=12 channel" (in Korean wording) appears 669 times across 213 domain files**

The phrase meaning "sigma=12 channels" (as the original Korean template string) appears across every axis: compute (317
occurrences in 87 files), infra (57 files), culture (25 files), physics, space,
cognitive. This is not independent discovery -- it is systematic template propagation.

**Finding 3: Bipartite matching 100% false positive rate**

The honest-limitations.md P4 audit (line 448-453) reports:
> "Full grep audit of fit>=0.95 top 10 pairs completed. 0/10 PASS -- false positive rate 100%"

The project's own body-text audit found that its highest-confidence matches are
entirely false positives when checked against actual paper content.

### Experiment Design

**Phase 1: Template fingerprinting (1 day)**

For each of the 295 domain files, extract:
1. All sentences containing n=6 constants (sigma, tau, phi, sopfr, J2, n=6).
2. Compute sentence-level Jaccard similarity between all domain pairs.
3. Cluster by text similarity.

**Prediction**: Domains will cluster by generation batch (same template version),
NOT by subject matter. Coffee and dolphin-bioacoustics will be more textually similar
to each other than coffee is to coffee-science or dolphin-bioacoustics is to dolphin.

**Phase 2: Noun-substitution test (2 days)**

For each of the 47 life/ domain files:
1. Remove the domain-specific nouns (coffee, dolphin, baking, HIV, etc.).
2. Compare the remaining skeleton text.
3. Compute the percentage of non-noun text that is identical across files.

**Prediction**: >80% of the non-noun text will be identical, confirming that these
are fill-in-the-blank template outputs, not independent analyses.

**Phase 3: Independent domain analysis (2 weeks)**

Select 10 domains from diverse axes. For EACH domain:
1. A domain expert (or thorough literature review) independently identifies the
   5 most important numerical parameters/constants in that field.
2. WITHOUT knowing the n=6 constants, assess whether these parameters cluster
   around any particular number's arithmetic functions.
3. THEN compare to the n=6 domain file's claims.

**Key question**: Do the domain files' numerical claims match what domain experts
would independently identify as the key parameters?

For example:
- **Coffee**: Does coffee science literature actually identify sigma=12 as a key
  parameter? (Literature says: extraction yield 18-22%, TDS 1.15-1.35%, brew ratio
  1:15-1:17, grind size 200-1200 microns, water temp 90-96C, brew time 25-30s for
  espresso. None of these are n=6-aligned.)
- **Dolphin bioacoustics**: Does the literature support "6 octave hearing range"
  and "6 ms echo delay" as THE key parameters? (Literature says: frequency range
  150 Hz - 150 kHz, which is ~10 octaves, not 6. Click intervals are 20-100 ms
  typically, not 6 ms. Source: Au, "The Sonar of Dolphins", 1993.)

### What Would Kill n=6
- >70% of domain file text (excluding domain-specific nouns) is identical across
  domains within the same axis.
- Independent domain expert review finds that <30% of the n=6 domain files'
  claimed numerical matches correspond to real, independently verifiable parameters.
- The domain files' "opening sentence" domain-specific claims (e.g., "6 octave
  hearing range") are factually incorrect when checked against primary literature.
- **Especially deadly**: if a domain expert panel rates the n=6 domain files as
  "template-generated with domain nouns inserted" with >80% agreement.

### What Would Survive
- Template structure is acknowledged as scaffolding, but domain-specific numerical
  claims are independently verified as accurate.
- Independent expert review confirms >70% of claimed n=6 matches reflect real
  domain parameters.
- The domain-specific opening sentences are factually correct and sourced.
- Template text <30% of total document content.

### Estimated Effort
- Phase 1: 1 day, Python text analysis
- Phase 2: 2 days, text processing
- Phase 3: 2 weeks, domain expert consultation or thorough literature review
- **Total: ~3 weeks**

### Pre-existing Evidence (Already Partially Fatal)
The template contamination evidence in Finding 1 is already strong enough to
reject Claim C as currently supported. The 295-domain coverage number is inflated
by mechanical template application. The question is not WHETHER templates were used
(they clearly were -- every life/ file references `<!-- gold-standard: shared/harness/sample.md -->`
in its HTML comment header), but whether any genuine domain-specific analysis
underlies the template scaffolding.

The honest-limitations P4 bipartite audit (0/10 PASS) suggests the answer is no
for at least the paper-domain matching system.

---

## Cross-Cutting Findings

### The Depth Problem

The n=6 framework's credibility is inversely proportional to the expression depth
it uses:

| Depth | Expressions | Coverage of [1,100] | Credibility |
|-------|-------------|---------------------|-------------|
| 0 | 9 constants | ~9% | HIGH -- direct match |
| 1 | ~80 expressions | ~30-50%? (needs measurement) | MEDIUM |
| 2 | ~800+ expressions | >50%? (needs measurement) | LOW |
| 3 | ~8000+ expressions | >90% (admitted in limitations) | NONE (admitted) |

The 98.4% coverage claim mixes all depths. A credible coverage claim would
report depth-0 and depth-1 separately. If depth-0 coverage (direct constant
matches only) drops below 20%, the framework's explanatory power is primarily
a combinatorial artifact.

### The Causation Gap

The project's own causal classification (discovery-algorithm-v4-architecture.md)
reveals a spectrum:

| Classification | Example | Implication |
|---------------|---------|-------------|
| COINCIDENTAL | BT-53 (Bitcoin 21M), BT-54 (AdamW 0.9) | n=6 match is accident |
| STRUCTURAL | BT-33 (12 heads), BT-58 (8-bit) | Number arises independently |
| CAUSAL | (none clearly demonstrated) | n=6 actually determines the value |

**No BT match has been demonstrated to be CAUSAL** -- i.e., where n=6 number theory
actually DETERMINED the engineering/physics value, rather than both the n=6 expression
and the real-world value independently landing on the same small integer.

### The Self-Referential Scoring Problem

The n6 scoring system uses `base_affinity(cell_type) + hash(cell_id + domain) % bucket`
(honest-limitations.md, line 409-410). This is a heuristic, not a measurement. The 98.4%
coverage rate is the output of this heuristic, not an externally validated statistic.
The heuristic was designed to find n=6 matches. Finding that it finds them at 98.4% rate
is circular.

---

## Prioritization

| Experiment | Severity if n=6 fails | Effort | Priority |
|------------|----------------------|--------|----------|
| RT-3 (Template Audit) | FATAL for Claim C | 3 weeks | **P0 -- already partially executed** |
| RT-1 (Rival Numbers) | FATAL for Claim B | 2 weeks | **P1 -- most decisive** |
| RT-2 (Expression Saturation) | FATAL for Claims A+C | 2 weeks | **P1 -- foundational** |

**Recommendation**: Execute RT-3 Phase 1 immediately (1 day). The template
fingerprinting data will either confirm or alleviate the contamination concern.
If confirmed, ALL coverage claims based on domain file counting must be withdrawn
and rebuilt from independent analysis.

---

## Appendix: What Is NOT Being Attacked

1. **The theorem itself**: sigma(n)*phi(n) = n*tau(n) iff n=6 for n>=2 is a correct
   mathematical theorem. The proof in theorem-r1-uniqueness.md is valid. We are not
   disputing the math -- we are disputing the SIGNIFICANCE claim.

2. **Genuine structural coincidences**: Some n=6 matches may be real structural
   resonances (e.g., carbon's CN=6 octahedral coordination, hexagonal crystal symmetry,
   benzene's 6-fold). These deserve individual investigation, not blanket claims.

3. **The framework's utility as a design heuristic**: Even if n=6 is not "mathematically
   determined," using {4, 6, 12, 24} as design targets might still produce good
   architectures. This is a weaker but defensible claim. The red team attacks the
   STRONG claim (mathematical inevitability), not the weak claim (useful heuristic).
