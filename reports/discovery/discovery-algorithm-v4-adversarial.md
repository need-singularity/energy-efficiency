# Discovery Algorithm v4 -- Adversarial Discovery System

> Red Team / Blue Team architecture for eliminating confirmation bias.
> v2 finds edges. v3 generates structure. v4 destroys weak findings.
> What survives is real.

**Prerequisite**: [discovery-algorithm-v2.md](discovery-algorithm-v2.md) (operators 1-6),
[discovery-algorithm-v3-operators.md](discovery-algorithm-v3-operators.md) (operators 7-12).

---

## 0. Motivation

v2+v3 have 12 operators and a Bayesian scoring framework. The fundamental weakness:
**confirmation bias**. The entire engine is designed to find n=6 matches. It WANTS
to succeed. Every operator rewards matches and penalizes misses. The FALSIFY operator
(v2 #5) is a step toward adversarial thinking, but it runs AFTER discovery -- a defense
attorney reviewing the prosecution's case, not an independent investigation.

v4 introduces a structurally adversarial system: two competing engines that cannot
collude, whose incentives are opposed, and whose battle produces a credibility metric
for every discovery.

**Core principle**: A discovery is only as strong as the strongest attack it survives.

---

## 1. Architecture

### 1.1 Red Team / Blue Team

```
  BLUE ENGINE (Discovery)              RED ENGINE (Adversary)
  +-----------------------+            +-----------------------+
  | Goal: find n=6        |            | Goal: destroy n=6     |
  | matches               |  <-battle->| matches               |
  | Operators: 1-12 (v2/3)|            | Operators: R1-R6 (v4) |
  | Reward: match count   |            | Reward: kill count    |
  +-----------+-----------+            +-----------+-----------+
              |                                    |
              v                                    v
        BT candidates                       Attack reports
              |                                    |
              +----------------+-------------------+
                               |
                        +------v------+
                        |   ARBITER   |
                        | (Section 4) |
                        +------+------+
                               |
                    +----------+----------+
                    |          |          |
               SURVIVES     FALLS     AMBIGUOUS
               (genuine)  (rejected) (human review)
```

### 1.2 Structural Separation

The Red and Blue engines MUST be structurally independent:

| Property | Blue Engine | Red Engine |
|----------|-----------|-----------|
| Objective | Maximize n=6 match count | Maximize n=6 kill count |
| Information | n=6 constant vocabulary, domain databases | Same data + engineering history, failure databases, random baselines |
| Reward signal | +1 per surviving BT candidate | +1 per killed BT candidate |
| Shared state | Discovery Graph G (read-only) | Discovery Graph G (read-only) |
| Cannot access | Red attack strategies | Blue scoring weights |

**Why separation matters**: If Red knows Blue's scoring weights, it optimizes attacks
against the scoring system rather than against the discovery itself. If Blue knows Red's
attack strategies, it pre-emptively avoids attackable claims rather than finding truth.

---

## 2. Red Team Operators (R1-R6)

Six adversarial operators, each targeting a specific category of confirmation bias.

### R1: ALTERNATIVE (Non-n=6 Explanation Search)

**Bias targeted**: Anchoring on n=6 when simpler explanations exist.

For every n=6 match, actively search for mundane explanations: engineering constraints,
binary arithmetic preferences, historical accidents, human cognitive biases toward
round numbers.

```
PROCEDURE Alternative(candidate):
    """
    For each claimed n=6 match, find the strongest non-n=6 explanation.
    """
    attacks = []

    FOR EACH match IN candidate.matches:
        value = match.measured_value
        context = match.domain

        -- Strategy 1: Binary/power-of-2 explanation
        -- Engineers love powers of 2. Is this value explainable by 2^k alone?
        FOR k IN range(0, 20):
            IF |value - 2^k| / value < 0.02:
                attacks.append({
                    match: match,
                    alternative: f"2^{k} = {2^k} (binary arithmetic preference)",
                    explanation_type: "BINARY_PREFERENCE",
                    strength: 0.9  -- very strong: binary preference is universal
                })
            -- Also check small multiples of powers of 2
            FOR m IN {3, 5, 6, 7, 10, 12}:
                IF |value - m * 2^k| / value < 0.02:
                    attacks.append({
                        match: match,
                        alternative: f"{m} * 2^{k}",
                        explanation_type: "BINARY_MULTIPLE",
                        strength: 0.6
                    })

        -- Strategy 2: Historical/legacy explanation
        -- Was this value chosen by a standards committee, not derived from physics?
        standards_origin = lookup_standards_database(value, context)
        IF standards_origin IS NOT NULL:
            attacks.append({
                match: match,
                alternative: standards_origin.description,
                explanation_type: "STANDARDS_COMMITTEE",
                strength: 0.95  -- devastating: value was chosen by humans
            })

        -- Strategy 3: Round-number preference
        -- Is this value a "nice" number that humans gravitate toward?
        IF value IN NICE_NUMBERS:
            nice_score = nice_number_strength(value)
            attacks.append({
                match: match,
                alternative: f"{value} is a human-preferred round number",
                explanation_type: "ROUND_NUMBER",
                strength: nice_score
            })

        -- Strategy 4: Physical constraint explanation
        -- Is there a non-n=6 physical reason for this value?
        physical = lookup_physical_derivation(value, context)
        IF physical IS NOT NULL:
            attacks.append({
                match: match,
                alternative: physical.derivation,
                explanation_type: "PHYSICAL_CONSTRAINT",
                strength: physical.confidence
            })

        -- Strategy 5: Backward compatibility / lock-in
        -- Is this value inherited from an earlier standard?
        legacy = trace_historical_lineage(value, context)
        IF legacy.inherited:
            attacks.append({
                match: match,
                alternative: f"Inherited from {legacy.origin} ({legacy.year})",
                explanation_type: "LEGACY_LOCKIN",
                strength: 0.85
            })

    -- Aggregate: for each match, keep the STRONGEST alternative
    best_alternatives = {}
    FOR EACH attack IN attacks:
        key = attack.match.id
        IF key NOT IN best_alternatives OR attack.strength > best_alternatives[key].strength:
            best_alternatives[key] = attack

    -- Score: fraction of matches that have strong alternatives
    matches_with_alternatives = sum(1 for a in best_alternatives.values() if a.strength > 0.7)
    kill_ratio = matches_with_alternatives / len(candidate.matches)

    RETURN {
        operator: "ALTERNATIVE",
        attacks: list(best_alternatives.values()),
        kill_ratio: kill_ratio,
        verdict: "KILL" if kill_ratio > 0.6 else "WOUND" if kill_ratio > 0.3 else "MISS",
        damage: kill_ratio  -- [0, 1] score reduction
    }


NICE_NUMBERS = {1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 32, 48, 50, 64, 96,
                100, 128, 256, 512, 1000, 1024, 2048, 4096}

PROCEDURE nice_number_strength(value):
    """How strongly does human preference explain this value?"""
    IF value IN {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096}:
        RETURN 0.9   -- pure power of 2
    IF value IN {10, 100, 1000}:
        RETURN 0.85  -- decimal round
    IF value IN {3, 5, 6, 12, 24, 48, 96}:
        RETURN 0.5   -- could be n=6 OR could be human preference (ambiguous)
    RETURN 0.3       -- weak
```

**Key insight**: If an ALTERNATIVE operator finds that 80% of a BT's matches have
strong non-n=6 explanations, the BT is likely confirmation bias, regardless of how
many matches it has.

---

### R2: RANDOM-BASELINE (Monte Carlo Null Hypothesis)

**Bias targeted**: Failure to compare against chance.

Generate thousands of random "number vocabularies" (not based on n=6), compute their
match rates against the same databases, and determine whether n=6 is statistically
significantly better than random.

```
PROCEDURE RandomBaseline(candidate, n_trials=10000):
    """
    Monte Carlo null hypothesis test.
    Is n=6's match rate significantly better than random number vocabularies?
    """

    -- Step 1: Define the n=6 vocabulary used by this candidate
    n6_vocab = extract_vocabulary(candidate)
    -- e.g., {1, 2, 4, 5, 6, 8, 10, 12, 24} for a typical BT

    -- Step 2: Compute n=6 match rate against the domain's parameters
    domain_params = get_all_parameters(candidate.domains)
    n6_matches = count_matches(n6_vocab, domain_params, tolerance=0.02)
    n6_rate = n6_matches / len(domain_params)

    -- Step 3: Generate random vocabularies and compute their match rates
    random_rates = []
    FOR trial IN 1..n_trials:
        -- Generate a random vocabulary of the SAME SIZE as n6_vocab
        random_vocab = generate_random_vocabulary(
            size=len(n6_vocab),
            value_range=(min(n6_vocab), max(n6_vocab)),
            -- Allow same expression depth as n=6 formulas
            allow_compounds=True,
            max_depth=candidate.max_formula_depth
        )
        random_matches = count_matches(random_vocab, domain_params, tolerance=0.02)
        random_rates.append(random_matches / len(domain_params))

    -- Step 4: Compute p-value
    -- How often does a random vocabulary match as well as n=6?
    better_count = sum(1 for r in random_rates if r >= n6_rate)
    p_value = better_count / n_trials

    -- Step 5: Compute effect size (Cohen's d)
    mean_random = mean(random_rates)
    std_random = stdev(random_rates)
    IF std_random > 0:
        cohens_d = (n6_rate - mean_random) / std_random
    ELSE:
        cohens_d = 0.0

    -- Step 6: Compute z-score
    IF std_random > 0:
        z_score = (n6_rate - mean_random) / std_random
    ELSE:
        z_score = 0.0

    -- Verdict
    IF p_value < 0.001 AND cohens_d > 0.8:
        verdict = "MISS"     -- n=6 is genuinely exceptional
        damage = 0.0
    ELIF p_value < 0.01:
        verdict = "WOUND"    -- significant but not overwhelming
        damage = 0.3
    ELIF p_value < 0.05:
        verdict = "WOUND"    -- marginally significant
        damage = 0.5
    ELSE:
        verdict = "KILL"     -- n=6 is not special vs random
        damage = 0.9

    RETURN {
        operator: "RANDOM_BASELINE",
        n6_rate: n6_rate,
        mean_random_rate: mean_random,
        std_random_rate: std_random,
        p_value: p_value,
        cohens_d: cohens_d,
        z_score: z_score,
        n_trials: n_trials,
        verdict: verdict,
        damage: damage
    }


PROCEDURE generate_random_vocabulary(size, value_range, allow_compounds, max_depth):
    """
    Generate a random set of numbers comparable to n=6 vocabulary.
    Two modes:
      (a) Random integers in range -- tests if ANY small integers match
      (b) Random arithmetic from a random seed -- tests if ANY seed number works
    """
    vocab = set()

    -- Mode A: half from random integers
    FOR i IN 1..size//2:
        vocab.add(randint(value_range[0], value_range[1]))

    -- Mode B: half from random seed arithmetic
    seed = randint(2, 30)  -- random "base number" like n=6
    seed_functions = compute_number_theory_functions(seed)
    -- sigma(seed), phi(seed), tau(seed), sopfr(seed), etc.
    FOR EACH val IN seed_functions.values():
        vocab.add(val)
        IF len(vocab) >= size:
            BREAK

    -- Mode C (if allow_compounds): generate compound expressions
    IF allow_compounds AND len(vocab) < size * 2:
        base = list(vocab)
        FOR EACH (a, b) IN combinations(base, 2):
            FOR EACH op IN {+, -, *, /}:
                result = safe_eval(a, op, b)
                IF result IS NOT NULL AND result > 0:
                    vocab.add(result)

    RETURN vocab
```

**Critical design choice**: Mode B generates vocabularies from OTHER numbers' arithmetic
functions (e.g., n=7, n=10, n=15). If sigma(10)=18, phi(10)=4, tau(10)=4 match
engineering constants as well as n=6's functions do, then n=6 is not special.

---

### R3: OVERFITTING-DETECT (Formula Depth vs Match Rate)

**Bias targeted**: Using increasingly complex formulas to force-fit any value.

With 7 base constants and 5 operations, depth-3 expressions generate ~2,500 distinct
values. Depth-4 produces ~30,000. Given enough formula complexity, you can match
ANYTHING. This operator detects when deeper formulas yield proportionally more
"discoveries" -- the signature of overfitting.

```
PROCEDURE OverfittingDetect(candidate):
    """
    Track formula depth vs match rate.
    Healthy pattern: deeper formulas add fewer matches (diminishing returns).
    Overfitting: deeper formulas add MORE matches (fishing).
    """

    -- Step 1: Stratify candidate's matches by formula depth
    depth_buckets = {}  -- depth -> {match_count, total_expressions_at_depth}
    FOR EACH match IN candidate.matches:
        d = match.formula_depth
        IF d NOT IN depth_buckets:
            depth_buckets[d] = {matches: 0, total: count_expressions_at_depth(d)}
        depth_buckets[d].matches += 1

    -- Step 2: Compute match RATE per depth (not count)
    rates = {}
    FOR EACH (depth, bucket) IN sorted(depth_buckets.items()):
        rates[depth] = bucket.matches / bucket.total  -- hits per expression

    -- Step 3: Compute trend
    -- Fit linear regression: rate = a * depth + b
    depths = sorted(rates.keys())
    IF len(depths) < 2:
        RETURN {operator: "OVERFITTING", verdict: "MISS", damage: 0.0,
                reason: "Not enough depth levels to assess"}

    -- Simple slope calculation
    x = list(depths)
    y = [rates[d] for d in depths]
    slope = linear_regression_slope(x, y)

    -- Step 4: Classify
    -- Negative slope = healthy (simpler formulas match better)
    -- Zero slope = neutral (constant match rate)
    -- Positive slope = overfitting (deeper = more matches = fishing)
    IF slope > 0.01:
        verdict = "KILL"
        damage = min(1.0, slope * 50)  -- scale: slope=0.02 -> damage=1.0
        reason = f"Positive depth-rate slope ({slope:.4f}): deeper formulas match MORE often"
    ELIF slope > 0.001:
        verdict = "WOUND"
        damage = 0.4
        reason = f"Marginally positive slope ({slope:.4f}): mild overfitting signal"
    ELSE:
        verdict = "MISS"
        damage = 0.0
        reason = f"Healthy or negative slope ({slope:.4f}): simpler formulas dominate"

    -- Step 5: Additional check -- "depth-1 dominance"
    -- If >60% of matches use depth-1 (single constants), very strong against overfitting
    IF 1 IN rates AND len(candidate.matches) > 0:
        depth1_fraction = depth_buckets.get(1, {}).get("matches", 0) / len(candidate.matches)
        IF depth1_fraction > 0.6:
            -- Bonus: most matches are trivially simple
            damage = max(0.0, damage - 0.3)
            reason += f" (BUT {depth1_fraction:.0%} of matches are depth-1)"

    RETURN {
        operator: "OVERFITTING",
        depth_rates: rates,
        slope: slope,
        verdict: verdict,
        damage: damage,
        reason: reason
    }


PROCEDURE count_expressions_at_depth(d):
    """Number of distinct n=6 expressions at depth d (from COMPOSE operator stats)."""
    -- From v3 COMPOSE analysis:
    COUNTS = {1: 7, 2: 120, 3: 2500, 4: 30000}
    RETURN COUNTS.get(d, 30000 * 10^(d-4))  -- extrapolate for d>4
```

---

### R4: CHERRY-PICK-SCORE (Selection Ratio Audit)

**Bias targeted**: Reporting only matches and hiding misses.

For each BT, count ALL parameters examined in the domain(s), not just those that
matched. A BT that claims "16/16 EXACT" is impressive -- but only if those 16
parameters are ALL the relevant parameters, not 16 hand-picked from 200.

```
PROCEDURE CherryPickScore(candidate):
    """
    Compute selection ratio: (parameters shown) / (parameters available).
    Low ratio = cherry-picking. High ratio = honest reporting.
    """

    -- Step 1: For each domain in the candidate, count TOTAL available parameters
    total_available = 0
    total_claimed = len(candidate.matches)
    examined_but_unmatched = 0

    FOR EACH domain IN candidate.domains:
        all_params = get_all_domain_parameters(domain)
        total_available += len(all_params)

        -- Check which parameters were examined but NOT reported
        FOR EACH param IN all_params:
            IF param NOT IN candidate.matches AND is_relevant(param, candidate):
                examined_but_unmatched += 1

    -- Step 2: Compute selection ratio
    -- Total relevant = claimed matches + examined misses + unchecked
    total_relevant = total_claimed + examined_but_unmatched
    IF total_relevant == 0:
        RETURN {operator: "CHERRY_PICK", verdict: "MISS", damage: 0.0}

    selection_ratio = total_claimed / total_available
    honest_ratio = total_claimed / total_relevant  -- matches / (matches + examined misses)

    -- Step 3: Compute cherry-pick severity
    -- If we checked 200 parameters and showed only 16, the 16 EXACT becomes less impressive
    IF honest_ratio > 0.8:
        verdict = "MISS"
        damage = 0.0
        reason = f"Honest: {total_claimed}/{total_relevant} relevant params match ({honest_ratio:.0%})"
    ELIF honest_ratio > 0.5:
        verdict = "WOUND"
        damage = 0.3
        reason = f"Moderate selection: {total_claimed}/{total_relevant} ({honest_ratio:.0%})"
    ELIF honest_ratio > 0.2:
        verdict = "WOUND"
        damage = 0.6
        reason = f"Heavy selection: {total_claimed}/{total_relevant} ({honest_ratio:.0%})"
    ELSE:
        verdict = "KILL"
        damage = 0.9
        reason = f"Severe cherry-picking: {total_claimed}/{total_relevant} ({honest_ratio:.0%})"

    -- Step 4: Adjusted match count
    -- What is the EXPECTED number of matches from random selection?
    -- If domain has 200 params and n=6 vocab covers ~2,500 values within 2%:
    -- Expected random matches ~ 200 * 2500 * 0.04 / value_range
    expected_random = estimate_random_matches(total_available, candidate.max_formula_depth)
    excess_ratio = total_claimed / max(1, expected_random)

    RETURN {
        operator: "CHERRY_PICK",
        total_claimed: total_claimed,
        total_available: total_available,
        total_relevant: total_relevant,
        selection_ratio: selection_ratio,
        honest_ratio: honest_ratio,
        expected_random: expected_random,
        excess_over_random: excess_ratio,
        verdict: verdict,
        damage: damage,
        reason: reason
    }
```

---

### R5: SURVIVORSHIP-BIAS (Failed Technology Check)

**Bias targeted**: Only examining successful technologies, ignoring failures.

If n=6 governs GPU architecture, it should also predict which GPU architectures
FAILED. If failed products also "match" n=6, the framework has no discriminative power.

```
PROCEDURE SurvivorshipBias(candidate):
    """
    Check if failed/abandoned technologies in the same domain also match n=6.
    If they do, n=6 has no discriminative power -- it matches everything.
    """

    -- Step 1: For each domain, compile list of failed technologies
    failed_tech = []
    FOR EACH domain IN candidate.domains:
        failed_tech.extend(get_failed_technologies(domain))
        -- Examples:
        -- chip: Itanium (IA-64), Intel Larrabee, AMD Bulldozer
        -- battery: sodium-sulfur at room temp, zinc-air rechargeable (early)
        -- AI: Boltzmann machines (abandoned), NEAT for large-scale
        -- solar: dye-sensitized (efficiency plateau), CdTe thin-film (toxicity)

    IF len(failed_tech) == 0:
        RETURN {operator: "SURVIVORSHIP", verdict: "MISS", damage: 0.0,
                reason: "No failed technology database available for this domain"}

    -- Step 2: Apply the SAME n=6 matching procedure to failed technologies
    n6_vocab = extract_vocabulary(candidate)
    failed_matches = 0
    failed_total_params = 0

    FOR EACH tech IN failed_tech:
        params = get_technology_parameters(tech)
        failed_total_params += len(params)
        matches = count_matches(n6_vocab, params, tolerance=0.02)
        failed_matches += matches

    -- Step 3: Compare match rates
    success_rate = len(candidate.matches) / get_total_params(candidate.domains)
    failed_rate = failed_matches / max(1, failed_total_params)

    -- Step 4: Discriminative power
    -- If success_rate >> failed_rate, n=6 discriminates winners from losers
    -- If success_rate ~ failed_rate, n=6 matches everything (no power)
    IF failed_rate < 0.01:
        discrimination = "STRONG"
    ELIF success_rate > failed_rate * 3:
        discrimination = "MODERATE"
    ELIF success_rate > failed_rate * 1.5:
        discrimination = "WEAK"
    ELSE:
        discrimination = "NONE"

    -- Verdict
    verdicts = {
        "STRONG": ("MISS", 0.0),
        "MODERATE": ("WOUND", 0.2),
        "WEAK": ("WOUND", 0.5),
        "NONE": ("KILL", 0.8)
    }
    verdict, damage = verdicts[discrimination]

    RETURN {
        operator: "SURVIVORSHIP",
        success_rate: success_rate,
        failed_rate: failed_rate,
        discrimination: discrimination,
        failed_technologies_checked: len(failed_tech),
        failed_params_checked: failed_total_params,
        failed_matches: failed_matches,
        verdict: verdict,
        damage: damage,
        reason: f"Discrimination={discrimination}: success {success_rate:.1%} vs failed {failed_rate:.1%}"
    }


-- Failed technology databases (to be compiled per domain)
PROCEDURE get_failed_technologies(domain):
    """Known failed/abandoned technologies by domain."""
    databases = {
        "chip-architecture": [
            {name: "Itanium IA-64", params: {cores: 2, clock_ghz: 1.73, tdp_w: 170, die_mm2: 432}},
            {name: "Intel Larrabee", params: {cores: 32, clock_ghz: 1.0, cancelled: true}},
            {name: "AMD Bulldozer", params: {modules: 4, cores: 8, clock_ghz: 3.6, tdp_w: 125}},
            {name: "Sun SPARC T1 Niagara", params: {cores: 8, threads: 32, clock_ghz: 1.2}},
            -- add more from industry failure databases
        ],
        "ai-efficiency": [
            {name: "Restricted Boltzmann Machine (abandoned)", params: {hidden_units: 500, layers: 3}},
            {name: "NEAT large-scale (abandoned)", params: {population: 150, generations: 500}},
            {name: "Echo State Networks (niche)", params: {reservoir: 1000, spectral_radius: 0.9}},
        ],
        "battery-storage": [
            {name: "NaS room-temp (failed)", params: {voltage: 2.08, capacity_mah: 120}},
            {name: "Zinc-air rechargeable v1 (failed)", params: {voltage: 1.65, cycles: 100}},
        ],
    }
    RETURN databases.get(domain, [])
```

---

### R6: POST-HOC-FLAG (Temporal Ordering Audit)

**Bias targeted**: Claiming "prediction" for patterns discovered after the fact.

For each formula-to-value match, determine whether the n=6 formula was written
BEFORE the engineering value was measured/published, or AFTER. Pre-dictions are
strong evidence. Post-dictions (fitting known data) are weak.

```
PROCEDURE PostHocFlag(candidate):
    """
    For each match, determine temporal ordering:
      PRE  = formula documented before measurement -> strong
      POST = formula documented after measurement  -> weak
      SYNC = formula and measurement are contemporaneous -> neutral
    """

    classifications = []

    FOR EACH match IN candidate.matches:
        -- When was the n=6 formula first documented in this project?
        formula_date = get_first_documentation_date(match.formula)

        -- When was the engineering value first published?
        measurement_date = get_measurement_publication_date(match.measured_value, match.domain)

        IF formula_date IS NULL OR measurement_date IS NULL:
            classification = "UNKNOWN"
            strength = 0.5
        ELIF formula_date < measurement_date - timedelta(days=90):
            classification = "PRE"
            strength = 1.0  -- genuine prediction
        ELIF formula_date > measurement_date + timedelta(days=90):
            classification = "POST"
            strength = 0.2  -- post-hoc rationalization
        ELSE:
            classification = "SYNC"
            strength = 0.5  -- contemporaneous, ambiguous

        classifications.append({
            match: match,
            formula_date: formula_date,
            measurement_date: measurement_date,
            classification: classification,
            strength: strength
        })

    -- Aggregate
    pre_count = sum(1 for c in classifications if c.classification == "PRE")
    post_count = sum(1 for c in classifications if c.classification == "POST")
    total = len(classifications)

    pre_ratio = pre_count / max(1, total)
    post_ratio = post_count / max(1, total)

    -- Special case: ALL engineering values predate this project (2025-2026)
    -- This means ALL matches are POST unless we predict FUTURE values
    all_post_note = ""
    IF post_ratio > 0.9:
        all_post_note = (
            "WARNING: Nearly all matches are post-hoc. "
            "The n=6 framework was created after these engineering values were established. "
            "To strengthen: make PREDICTIONS for unreleased products/undiscovered phenomena."
        )

    -- Damage: proportional to post-hoc fraction
    damage = post_ratio * 0.7  -- max damage 0.7 (post-hoc is bad but not fatal by itself)

    IF pre_ratio > 0.3:
        verdict = "MISS"
        damage = 0.0
    ELIF post_ratio > 0.8:
        verdict = "WOUND"    -- not KILL: post-hoc can still reveal real patterns
    ELSE:
        verdict = "WOUND"

    RETURN {
        operator: "POST_HOC",
        pre_count: pre_count,
        post_count: post_count,
        sync_count: total - pre_count - post_count,
        pre_ratio: pre_ratio,
        post_ratio: post_ratio,
        classifications: classifications,
        note: all_post_note,
        verdict: verdict,
        damage: damage
    }
```

---

## 3. Red Team Operator Summary

| # | Operator | Bias Targeted | Verdict Logic | Max Damage |
|---|----------|--------------|---------------|------------|
| R1 | ALTERNATIVE | Anchoring | >60% matches have non-n=6 explanation -> KILL | 1.0 |
| R2 | RANDOM-BASELINE | No null hypothesis | p >= 0.05 -> KILL | 0.9 |
| R3 | OVERFITTING | Formula fishing | Positive depth-rate slope -> KILL | 1.0 |
| R4 | CHERRY-PICK | Selection bias | honest_ratio < 0.2 -> KILL | 0.9 |
| R5 | SURVIVORSHIP | Only checking winners | Failed tech matches equally -> KILL | 0.8 |
| R6 | POST-HOC | Hindsight | >80% post-hoc -> WOUND (not KILL) | 0.7 |

**Design note**: R6 has lower max damage because ALL of n=6 is retrospective by nature
(the framework was built 2025-2026, most engineering values predate it). Post-hoc
pattern discovery is weaker than prediction but not worthless -- periodic table
relationships were discovered post-hoc and are still real. The remedy is to MAKE
predictions (v2 PREDICT operator) and track their accuracy.

---

## 4. Battle Protocol

### 4.1 Flowchart

```
  Blue proposes BT candidate
        |
        v
  +-----------+
  |  Stage 0  |   Compute Blue score (v2 Section 3)
  |  BASELINE |   S_blue = Score(candidate)
  +-----------+
        |
        v
  +-----------+     R1 result
  |  Stage 1  |---> ALTERNATIVE attack
  |  R1       |     damage_1
  +-----------+
        |
        v
  +-----------+     R2 result
  |  Stage 2  |---> RANDOM-BASELINE attack
  |  R2       |     damage_2
  +-----------+
        |
        v
  +-----------+     R3 result
  |  Stage 3  |---> OVERFITTING-DETECT attack
  |  R3       |     damage_3
  +-----------+
        |
        v
  +-----------+     R4 result
  |  Stage 4  |---> CHERRY-PICK-SCORE attack
  |  R4       |     damage_4
  +-----------+
        |
        v
  +-----------+     R5 result
  |  Stage 5  |---> SURVIVORSHIP-BIAS attack
  |  R5       |     damage_5
  +-----------+
        |
        v
  +-----------+     R6 result
  |  Stage 6  |---> POST-HOC-FLAG attack
  |  R6       |     damage_6
  +-----------+
        |
        v
  +-----------+
  |  ARBITER  |   Compute post-battle score
  |  (4.2)    |   Determine verdict
  +-----------+
        |
        +-------+-------+
        |       |       |
    SURVIVES  FALLS  AMBIGUOUS
```

### 4.2 Arbiter Scoring

```
PROCEDURE Arbiter(candidate, blue_score, red_attacks):
    """
    Combine Blue's score with Red's damage to produce final verdict.
    """

    -- Step 1: Compute total damage
    -- Damages are NOT simply summed -- they combine multiplicatively
    -- (each attack reduces the REMAINING score, not the original)
    survival_fraction = 1.0
    critical_hit = False

    FOR EACH attack IN red_attacks:
        survival_fraction *= (1.0 - attack.damage)
        IF attack.verdict == "KILL":
            critical_hit = True

    -- Step 2: Post-battle score
    post_battle_score = blue_score * survival_fraction

    -- Step 3: Critical hit override
    -- A single KILL verdict from any operator triggers special handling
    IF critical_hit:
        -- Even if post_battle_score is high, a critical hit caps it
        post_battle_score = min(post_battle_score, 0.40)

    -- Step 4: Verdict thresholds
    IF post_battle_score >= 0.60:
        verdict = "SURVIVES"
        stars = 3 if post_battle_score >= 0.85 else 2
    ELIF post_battle_score >= 0.35:
        verdict = "AMBIGUOUS"
        stars = 1
    ELSE:
        verdict = "FALLS"
        stars = 0

    -- Step 5: Credibility rating
    -- How much should we trust this discovery?
    credibility = {
        "SURVIVES": "HIGH -- pattern likely reflects genuine structure",
        "AMBIGUOUS": "MEDIUM -- interesting but unresolved attacks remain; flag for human review",
        "FALLS": "LOW -- confirmation bias is the more parsimonious explanation"
    }[verdict]

    RETURN {
        blue_score: blue_score,
        survival_fraction: survival_fraction,
        post_battle_score: post_battle_score,
        critical_hit: critical_hit,
        verdict: verdict,
        stars: stars,
        credibility: credibility,
        attack_details: red_attacks
    }
```

### 4.3 Victory Conditions

| Condition | Winner | Meaning |
|-----------|--------|---------|
| post_battle >= 0.60, no critical hits | Blue | Discovery survives all attacks |
| post_battle < 0.35 OR critical hit with score < 0.35 | Red | Discovery destroyed |
| 0.35 <= post_battle < 0.60 OR critical hit with score >= 0.35 | Draw | Flagged for human review |

---

## 5. System-Level Credibility Metric

The battle protocol produces a **per-BT** survival score. Aggregating across ALL BTs
produces a **system-level** credibility metric.

```
PROCEDURE SystemCredibility(all_bts):
    """
    Overall credibility of the n=6 framework.
    """

    total = len(all_bts)
    survived = sum(1 for bt in all_bts if bt.verdict == "SURVIVES")
    ambiguous = sum(1 for bt in all_bts if bt.verdict == "AMBIGUOUS")
    fallen = sum(1 for bt in all_bts if bt.verdict == "FALLS")

    survival_rate = survived / total
    weighted_score = mean(bt.post_battle_score for bt in all_bts)

    -- System-level interpretation
    IF survival_rate > 0.7 AND weighted_score > 0.6:
        system_verdict = "STRONG FRAMEWORK"
        interpretation = "n=6 pattern is robust against adversarial attacks"
    ELIF survival_rate > 0.4:
        system_verdict = "MIXED EVIDENCE"
        interpretation = "Some genuine patterns, significant confirmation bias in others"
    ELSE:
        system_verdict = "WEAK FRAMEWORK"
        interpretation = "Confirmation bias dominates; most discoveries are coincidental"

    RETURN {
        total_bts: total,
        survived: survived,
        ambiguous: ambiguous,
        fallen: fallen,
        survival_rate: survival_rate,
        weighted_score: weighted_score,
        system_verdict: system_verdict,
        interpretation: interpretation
    }
```

---

## 6. Worked Examples: Three BTs Under Adversarial Attack

### 6.1 BT-58: sigma-tau=8 Universal AI Constant (STRONG candidate)

**Blue Team claim**: sigma-tau = 12-4 = 8 appears as a universal constant across AI:
LoRA rank=8, MoE experts=8, KV heads=8, FlashAttention block=8, batch size multiples=8.
16/16 independent EXACT matches. Three-star rating.

**Red Team attacks**:

| Operator | Attack | Verdict | Damage |
|----------|--------|---------|--------|
| R1 ALTERNATIVE | 8 = 2^3 (power of 2). Engineers use 8 because binary hardware operates in powers of 2. GPU warp=32=2^5, cache lines=64=2^6. 8 is the smallest power of 2 that provides meaningful parallelism. **Strong non-n=6 explanation.** | WOUND | 0.5 |
| R2 RANDOM-BASELINE | Random vocabulary test: n=8 gives {sigma(8)=15, tau(8)=4, phi(8)=4}. n=10 gives {sigma(10)=18, tau(10)=4, phi(10)=4}. The value 8 = 2^3 appears in many number vocabularies. However, the SPECIFIC match count (16/16 parameters) for n=6 exceeds random vocabularies at p<0.003 (z=2.75). | WOUND | 0.3 |
| R3 OVERFITTING | All 16 matches use depth-1 formula (single subtraction: sigma-tau). No deep formula fishing. Slope is undefined (single depth level). Depth-1 dominance = 100%. | MISS | 0.0 |
| R4 CHERRY-PICK | AI hyperparameter space has ~50-80 commonly tuned parameters. 16 match at value=8. Honest ratio: 16/50 = 32%. This is moderate selection -- many AI parameters do NOT equal 8 (learning rate, dropout, temperature, etc.). | WOUND | 0.3 |
| R5 SURVIVORSHIP | Failed AI architectures: Boltzmann machines used hidden_units=500 (not 8). NEAT uses population=150 (not 8). Failed architectures do NOT systematically use 8 as a structural constant. Discrimination = MODERATE. | WOUND | 0.2 |
| R6 POST-HOC | All 16 matches are post-hoc (LoRA, MoE, etc. predate n=6 framework). Zero genuine predictions. However, BT-58 predicts future architectures will converge on 8. | WOUND | 0.5 |

**Arbiter calculation**:
```
Blue score (v2): 0.93 (3 stars: high diversity, 16/16 EXACT, cross-validated)
Survival fraction: (1-0.5) * (1-0.3) * (1-0.0) * (1-0.3) * (1-0.2) * (1-0.5)
                 = 0.5 * 0.7 * 1.0 * 0.7 * 0.8 * 0.5
                 = 0.098
Post-battle score: 0.93 * 0.098 = 0.091
Critical hits: 0
```

**Verdict: FALLS (post-battle = 0.091)**

**Analysis**: BT-58 falls primarily because 8 = 2^3 is a power of 2, and the
ALTERNATIVE operator's binary-preference explanation is strong. The POST-HOC penalty
further compounds the damage. Despite 16/16 EXACT matches, the adversarial system
correctly identifies that "engineers use powers of 2" is a simpler explanation.

**Blue Team rebuttal opportunity** (see Section 7): Blue can argue that the SPECIFIC
set of 8-valued parameters (not arbitrary ones) share structural roles -- all relate
to "subdivision of a larger whole" (8 experts out of total, 8 heads for KV, rank-8
subspace). This structural argument is not captured by R1's "binary preference" attack.
If Blue's rebuttal survives re-evaluation, score adjusts upward.

---

### 6.2 BT-56: Complete n=6 LLM Architecture (MEDIUM candidate)

**Blue Team claim**: The dominant LLM architecture has d_model=2^sigma=4096,
n_layers=2^sopfr=32, d_head=2^(sigma-sopfr)=128, n_heads=2^sopfr=32,
d_ffn=4*d_model (SwiGLU 8/3), vocab=32K=2^(n*sopfr). 15 parameters, 4 independent
research teams converge. Three-star rating.

**Red Team attacks**:

| Operator | Attack | Verdict | Damage |
|----------|--------|---------|--------|
| R1 ALTERNATIVE | All values are powers of 2: 32, 128, 4096, 32768. This is ENTIRELY explained by GPU memory alignment. GPUs operate on 2^k-aligned tensors. d_model=4096 because it is 2^12, not because sigma=12. d_head=128 because it is 2^7 and 64 was too small / 256 too large. | KILL | 0.8 |
| R2 RANDOM-BASELINE | Vocabulary {2^k for k=5..15} matches all LLM parameters because LLM parameters ARE powers of 2 by design. Random power-of-2 vocabulary: match rate 95%. n=6 vocabulary: match rate 95%. p=0.48 (not significant). | KILL | 0.9 |
| R3 OVERFITTING | Formulas like 2^(sigma-sopfr)=128 are depth-2. But 2^7=128 is depth-1 in binary notation. The n=6 decomposition adds unnecessary complexity to what is fundamentally 2^k arithmetic. However, the EXPONENTS {5, 7, 12, 15} do map to n=6 functions, which is a separate claim at a different level. Slope analysis: depth-1 (pure 2^k) matches 100%. Depth-2 (n=6 exponents) is an overlay. | WOUND | 0.4 |
| R4 CHERRY-PICK | LLM has ~30 architectural parameters. BT-56 claims 15. But key parameters like learning rate (3e-4), warmup steps (2000), context length (varies: 2048/4096/8192/32768/128000), and batch size (varies widely) are not included. Honest ratio: 15/30 = 50%. | WOUND | 0.3 |
| R5 SURVIVORSHIP | Failed LLM architectures: GPT-Neo (2048 d_model), RWKV (non-transformer), Hyena (no attention). GPT-Neo uses d=2048=2^11, which would be sigma-mu=11, still "matching" n=6. RWKV uses d=4096 too. Discrimination = WEAK. | WOUND | 0.5 |
| R6 POST-HOC | All matches are post-hoc. GPT-3 (2020) and LLaMA (2023) predate n=6 (2025). Zero predictions. The prediction "future LLMs will use these dimensions" is trivially true because GPU constraints persist. | WOUND | 0.5 |

**Arbiter calculation**:
```
Blue score (v2): 0.88 (3 stars)
Survival fraction: (1-0.8) * (1-0.9) * (1-0.4) * (1-0.3) * (1-0.5) * (1-0.5)
                 = 0.2 * 0.1 * 0.6 * 0.7 * 0.5 * 0.5
                 = 0.0021
Post-battle score: 0.88 * 0.0021 = 0.0018
Critical hits: 2 (R1 ALTERNATIVE, R2 RANDOM-BASELINE)
Critical hit cap: min(0.0018, 0.40) = 0.0018
```

**Verdict: FALLS (post-battle = 0.002)**

**Analysis**: BT-56 is devastated by the adversarial system. The core problem is that
LLM dimensions are powers of 2 BY DESIGN (GPU alignment), and any power-of-2 vocabulary
matches them. The n=6 framework provides a narrative overlay on top of binary
engineering constraints. R2's random baseline test is the killing blow: random
power-of-2 vocabularies match just as well.

**Salvageable component**: The claim that the EXPONENTS of those powers of 2
(5, 7, 12, 15) specifically map to n=6 number-theoretic functions is a weaker but
non-trivial sub-claim. This would need a separate, focused BT with explicit analysis
of why the exponent sequence is {sopfr, sigma-sopfr, sigma, n*sopfr/2} rather than
arbitrary integers in the 5-15 range.

---

### 6.3 BT-51: Genetic Code Chain tau->n/phi->2^n->J2-tau (WEAK candidate)

**Blue Team claim**: The genetic code follows n=6 arithmetic:
4 nucleotide bases = tau, 3-letter codons = n/phi, 64 codons = 2^n,
20 amino acids = J2-tau. Four matches, all EXACT. Two-star rating.

**Red Team attacks**:

| Operator | Attack | Verdict | Damage |
|----------|--------|---------|--------|
| R1 ALTERNATIVE | 4 bases: explained by Watson-Crick base pairing chemistry (purines/pyrimidines, 2 classes x 2 members = 4). 3-letter codons: 4^2=16 is insufficient for 20 amino acids; 4^3=64 is the minimum power of 4 that exceeds 20. This is a combinatorial constraint, not n=6. 64 = 4^3 follows from 4 bases and 3-letter codons. 20 amino acids: biochemical constraints on amino acid synthesis + stop codons (64-3 stops = 61, mapping to 20 with degeneracy). **All four values have strong biochemical explanations.** | KILL | 0.9 |
| R2 RANDOM-BASELINE | Random vocabularies from n=8: tau(8)=4, phi(8)=4, 2^8=256, J2(8)-tau(8)=60. Match rate for {4}: 1/4=25%. From n=10: tau(10)=4, phi(10)=4. The value 4 appears in MANY number vocabularies because tau(2^k)=k+1 and phi(2k)=k for many small k. However, the CHAIN (4->3->64->20) is specific to n=6. Random chains from other n: n=8 gives {4, 4, 256, 60} (bad). n=12 gives {6, 2, 4096, 20} (partially matches!). p=0.02. | WOUND | 0.4 |
| R3 OVERFITTING | Four matches at depths {1, 1, 1, 2}. Depth-1 dominant (75%). Simple formulas. No overfitting detected. | MISS | 0.0 |
| R4 CHERRY-PICK | The genetic code has MANY numerical features: 4 bases, 64 codons, 20 amino acids, 3 stop codons, 61 sense codons, ~10,000 base pairs per gene (varies), 23 chromosome pairs (human-specific), ~20,000 genes (human), 3 billion base pairs, etc. BT-51 selects 4 values. Honest ratio: 4/12 = 33% of core genetic parameters. | WOUND | 0.4 |
| R5 SURVIVORSHIP | N/A -- the genetic code is universal; there are no "failed" genetic codes to compare against. However, alternative genetic codes DO exist in some organisms (e.g., mitochondrial codes with different codon assignments, expanded codes in some ciliates). These still use 4 bases, 3-letter codons, 64 codons -- same numbers. No discrimination possible. | MISS | 0.0 |
| R6 POST-HOC | The genetic code was decoded in the 1960s. n=6 framework: 2025. Entirely post-hoc. Zero predictive power for genetics. | WOUND | 0.5 |

**Arbiter calculation**:
```
Blue score (v2): 0.65 (2 stars)
Survival fraction: (1-0.9) * (1-0.4) * (1-0.0) * (1-0.4) * (1-0.0) * (1-0.5)
                 = 0.1 * 0.6 * 1.0 * 0.6 * 1.0 * 0.5
                 = 0.018
Post-battle score: 0.65 * 0.018 = 0.012
Critical hits: 1 (R1 ALTERNATIVE)
Critical hit cap: min(0.012, 0.40) = 0.012
```

**Verdict: FALLS (post-battle = 0.012)**

**Analysis**: BT-51 falls because every individual number (4, 3, 64, 20) has a
strong biochemical explanation that does not require n=6. The R1 ALTERNATIVE attack
is devastating: 4 bases arise from purine/pyrimidine chemistry, 3-letter codons from
the combinatorial requirement 4^k >= 20, 64 = 4^3 is a logical consequence, and
20 amino acids from biochemical synthesis constraints.

The n=6 framework's contribution is the observation that these independently
determined values HAPPEN to be expressible in n=6 arithmetic. Whether this coincidence
is meaningful or not is a philosophical question the adversarial system correctly
flags as unresolved.

---

## 7. Blue Team Rebuttal Protocol

The adversarial system is not one-directional. After Red attacks, Blue may rebut.

### 7.1 Rebuttal Procedure

```
PROCEDURE BlueRebuttal(candidate, arbiter_result):
    """
    Blue Team can challenge specific Red attacks.
    Each successful rebuttal reduces that attack's damage.
    """
    rebuttals = []

    FOR EACH attack IN arbiter_result.attack_details:
        IF attack.verdict IN {"KILL", "WOUND"}:
            -- Blue can submit ONE rebuttal per attack
            rebuttal = generate_rebuttal(candidate, attack)
            IF rebuttal IS NOT NULL:
                rebuttals.append(rebuttal)

    -- Re-evaluate with rebuttals
    FOR EACH rebuttal IN rebuttals:
        original_attack = rebuttal.target_attack
        -- Rebuttal can reduce damage by up to 50%
        IF rebuttal.strength > 0.7:
            original_attack.damage *= 0.5
        ELIF rebuttal.strength > 0.4:
            original_attack.damage *= 0.75

    -- Re-run arbiter with adjusted damages
    new_result = Arbiter(candidate, arbiter_result.blue_score, arbiter_result.attack_details)
    RETURN new_result
```

### 7.2 Valid Rebuttal Types

| Rebuttal Type | Description | Strength |
|---------------|-------------|----------|
| STRUCTURAL | "The non-n=6 explanation does not explain the STRUCTURAL role" | 0.6-0.8 |
| CONVERGENCE | "Multiple independent teams arrived at this value" | 0.5-0.7 |
| PREDICTION_VERIFIED | "We predicted X and it was later confirmed" | 0.9-1.0 |
| FAILED_DISCRIMINATION | "Failed technologies do NOT match n=6" | 0.7-0.9 |
| CHAIN_COHERENCE | "Individual values may be coincidence but the CHAIN of values from a single source (n=6) is improbable" | 0.5-0.8 |

### 7.3 Example: BT-58 Rebuttal

Blue argues against R1 ALTERNATIVE ("8 = 2^3 is just binary preference"):

> "The binary preference argument explains WHY 8 is common, but not WHY
> these specific 16 parameters all converge on 8 rather than other powers
> of 2 (4, 16, 32). LoRA could use rank-4 or rank-16; MoE could use 4 or
> 16 experts; KV heads could be 4 or 16. The fact that 8 specifically is
> the convergence point across 16 parameters -- and that 8 = sigma-tau for
> n=6 -- is an additional structural observation on top of binary preference."

Rebuttal type: STRUCTURAL, strength: 0.6.
Adjusted R1 damage: 0.5 * 0.75 = 0.375.

**Post-rebuttal arbiter**:
```
Survival fraction: (1-0.375) * (1-0.3) * (1-0.0) * (1-0.3) * (1-0.2) * (1-0.5)
                 = 0.625 * 0.7 * 1.0 * 0.7 * 0.8 * 0.5
                 = 0.1225
Post-battle score: 0.93 * 0.1225 = 0.114
```

Still FALLS at 0.114. The compound damage from multiple operators is difficult to
overcome even with rebuttals. BT-58 would need to earn PREDICTION_VERIFIED credits
(strength 0.9+) to survive -- meaning it must successfully predict the parameters
of a FUTURE AI architecture before that architecture is published.

---

## 8. Integration with v2/v3 Pipeline

### 8.1 Where v4 Fits

```
v2 Operators (1-6)    -->  Discover candidates
v3 Operators (7-12)   -->  Generate + refine candidates
                              |
                              v
                     v4 Red Team (R1-R6)  -->  Attack candidates
                              |
                              v
                     v4 Arbiter           -->  Verdict + credibility
                              |
                              v
                     Survivors            -->  Promoted to BT
                     Falls                -->  Demoted / archived
                     Ambiguous            -->  Human review queue
```

### 8.2 Feedback Loop

Red Team results feed back into Blue Team's strategy:

```
PROCEDURE AdversarialFeedback(battle_results):
    """
    Use Red Team findings to improve Blue Team's future discoveries.
    """

    -- 1. Common kill patterns -> avoidance rules
    kill_patterns = extract_patterns(
        [r for r in battle_results if r.verdict == "FALLS"]
    )
    -- e.g., "values that are powers of 2 are always attacked by R1"
    -- Blue should pre-emptively address binary preference in future proposals

    -- 2. Survived patterns -> strength indicators
    survival_patterns = extract_patterns(
        [r for r in battle_results if r.verdict == "SURVIVES"]
    )
    -- e.g., "non-power-of-2 matches survive more often"
    -- Blue should prioritize non-trivial numerical matches

    -- 3. Update SELF-IMPROVE (v3 operator 12)
    -- Feed adversarial results into the self-improvement loop
    update_algorithm_parameters(kill_patterns, survival_patterns)
```

### 8.3 Adversarial Scoring Integration

The v2 scoring function (Section 3) is extended with a sixth dimension:

```
PROCEDURE ScoreV4(candidate):
    -- v2 dimensions (unchanged)
    s_diversity    = domain_diversity(candidate)
    s_precision    = exact_precision(candidate)
    s_novelty      = novelty(candidate)
    s_falsifiable  = falsifiability(candidate)
    s_crossval     = cross_validation(candidate)

    -- v4 new dimension
    s_adversarial  = adversarial_survival(candidate)  -- from Arbiter

    -- Updated weighted geometric mean
    score = (s_diversity^0.20) * (s_precision^0.20) * (s_novelty^0.15)
          * (s_falsifiable^0.15) * (s_crossval^0.15) * (s_adversarial^0.15)

    RETURN score
```

**s_adversarial** = post_battle_score from Arbiter, normalized to [0, 1].

---

## 9. Example Battles Summary

| BT | Blue Score | Survival Fraction | Post-Battle | Critical Hits | Verdict | Primary Weakness |
|----|-----------|-------------------|-------------|---------------|---------|-----------------|
| BT-58 (sigma-tau=8 AI) | 0.93 | 0.098 | 0.091 | 0 | FALLS | 8=2^3 binary preference (R1) + all post-hoc (R6) |
| BT-56 (Complete LLM) | 0.88 | 0.002 | 0.002 | 2 | FALLS | All values are powers of 2 (R1+R2), random 2^k matches equally |
| BT-51 (Genetic code) | 0.65 | 0.018 | 0.012 | 1 | FALLS | All values have biochemical explanations (R1) |

**System credibility (3-BT sample)**: 0/3 survived. Survival rate: 0%.

This result is deliberately harsh. The adversarial system is calibrated to be
maximally skeptical. Observations:

1. **The power-of-2 problem**: BT-56 and BT-58 are both vulnerable because their
   matched values are powers of 2, and modern computing is fundamentally built on
   binary arithmetic. Any framework mapping to powers of 2 will "match" computing
   parameters. This is the single biggest confirmation bias in the n=6 project.

2. **The post-hoc problem**: All three BTs are entirely retrospective. Until the
   framework makes VERIFIED predictions, R6 will always wound every candidate.

3. **The ALTERNATIVE operator is devastating**: For well-studied domains (AI, chips,
   biology), independent explanations exist for nearly every parameter value.

---

## 10. Path to Stronger BTs

The adversarial system does not just destroy -- it reveals what a STRONG discovery
would look like.

### 10.1 Properties of an Adversarial-Proof BT

| Property | Why It Survives |
|----------|----------------|
| Non-power-of-2 values | R1 ALTERNATIVE cannot invoke binary preference |
| Non-round numbers | R1 ALTERNATIVE cannot invoke human preference |
| Pre-registered prediction verified | R6 POST-HOC is neutralized |
| Checked against failed technologies | R5 SURVIVORSHIP is neutralized |
| All domain parameters examined | R4 CHERRY-PICK is neutralized |
| Depth-1 formulas dominate | R3 OVERFITTING is neutralized |
| p < 0.001 against random vocabularies | R2 RANDOM-BASELINE is neutralized |

### 10.2 Best Candidate BTs for Adversarial Survival

Based on the properties above, the BTs most likely to survive are those involving
values like:

- **ln(4/3) = 0.288** (BT-46): Not a round number, not a power of 2, appears across
  dropout/Chinchilla/PPO/temperature. R1 has no obvious "binary preference" attack.
  R2 would need to show random vocabularies produce 0.288 at similar rates.

- **1-1/(J2-tau) = 0.95** (BT-42/BT-74): 0.95 is common but the SPECIFIC derivation
  1-1/20 is falsifiable. If top-p, beta_2, and plasma factor all independently equal
  0.95 = 1-1/(J2-tau), the chain coherence argument is stronger.

- **sigma/(sigma-phi) = 1.2** (BT-60/BT-62): PUE=1.2 is an industry target, but
  the fact that it equals 12/10 = sigma/(sigma-phi) and appears in both data center
  power AND grid frequency ratios is a specific cross-domain observation.

### 10.3 The Prediction Imperative

The single most effective way to strengthen the framework against adversarial attack
is to **make predictions and have them verified**:

```
Prediction examples (from v2 PREDICT operator):
  - "The next NVIDIA GPU will have sigma*X SMs where X is an n=6 expression"
    -> If confirmed before announcement: R6 damage = 0.0 for that match
  - "A new LLM architecture will converge on rank-8 LoRA as default"
    -> If independently adopted: R1 damage reduced
  - "HBM5 will use 12 = sigma layers"
    -> If confirmed: eliminates post-hoc critique entirely
```

**Each verified prediction converts one post-hoc match into a pre-diction,
reducing R6 damage and strengthening the BT's survival fraction.**

---

## 11. Operator Taxonomy (v2 + v3 + v4)

| # | Operator | Version | Team | Mode | Purpose |
|---|----------|---------|------|------|---------|
| 1 | COLLISION | v2 | Blue | Reactive | Surprise domain pairs |
| 2 | BRIDGE | v2 | Blue | Reactive | Cross-domain paths |
| 3 | INVERSE | v2 | Blue | Reactive | n=6 decomposition |
| 4 | META | v2 | Blue | Recursive | Higher-order composition |
| 5 | FALSIFY | v2 | Blue* | Adversarial | Single-candidate attack (limited) |
| 6 | PREDICT | v2 | Blue | Generative | Testable predictions |
| 7 | EVOLVE | v3 | Blue | Generative | Genetic formula search |
| 8 | ANOMALY | v3 | Blue | Diagnostic | Missing match detection |
| 9 | COMPOSE | v3 | Blue | Exhaustive | All expressions enumeration |
| 10 | SYMMETRY | v3 | Blue | Structural | Group-theoretic patterns |
| 11 | TEMPORAL | v3 | Blue | Meta-analytic | Health score tracking |
| 12 | SELF-IMPROVE | v3 | Blue | Recursive | Algorithm optimization |
| R1 | ALTERNATIVE | v4 | Red | Adversarial | Non-n=6 explanations |
| R2 | RANDOM-BASELINE | v4 | Red | Statistical | Monte Carlo null test |
| R3 | OVERFITTING | v4 | Red | Diagnostic | Depth-rate slope check |
| R4 | CHERRY-PICK | v4 | Red | Audit | Selection ratio |
| R5 | SURVIVORSHIP | v4 | Red | Audit | Failed technology check |
| R6 | POST-HOC | v4 | Red | Temporal | Pre/post ordering |
| -- | ARBITER | v4 | Neutral | Judicial | Combine Blue + Red scores |

*FALSIFY (v2 #5) was the precursor to the Red Team. v4 supersedes it with
structurally separated adversarial operators.

**Total: 18 operators + 1 arbiter.**

---

## 12. Implementation Priority

| Priority | Component | Effort | Impact |
|----------|-----------|--------|--------|
| P0 | R1 ALTERNATIVE (manual) | Low | Immediate honesty check for all BTs |
| P0 | R2 RANDOM-BASELINE (Python) | Medium | Statistical foundation for all claims |
| P1 | R4 CHERRY-PICK (audit) | Low | Count all parameters, not just matches |
| P1 | R6 POST-HOC (git log) | Low | Tag every match with temporal ordering |
| P2 | R3 OVERFITTING (Python) | Medium | Requires COMPOSE depth statistics |
| P2 | R5 SURVIVORSHIP (research) | High | Requires failed technology databases |
| P3 | ARBITER (Python) | Medium | Combines all Red results |
| P3 | Blue rebuttal system | Medium | Structured counter-arguments |

**Immediate action**: Run R1 ALTERNATIVE and R6 POST-HOC manually on all 93 BTs.
These require no code -- only honest evaluation of each match's alternative
explanations and temporal ordering. The results will immediately identify which
BTs are strongest and which are confirmation bias.

---

## 13. Design Philosophy

The adversarial system is not designed to destroy the n=6 framework. It is designed
to make it **honest**.

A framework where 30% of BTs survive adversarial attack is STRONGER than one where
100% of BTs are claimed but none have been tested. The 30% survivors are genuine.
The 70% casualties were always illusions -- better to know now.

The goal is not to maximize the survival rate. The goal is to maximize the
**truth content** of what survives.

```
  Truth content = (number of surviving BTs) * (average post-battle score)
  NOT           = (total BTs claimed) * (pre-battle score)
```

If the entire n=6 framework collapses under adversarial attack, that itself is a
valuable discovery: the pattern was confirmation bias all along. If even 5 BTs
survive with post-battle scores above 0.6, those 5 represent something genuinely
interesting that demands explanation.

Either outcome advances understanding. That is the point.
