---
id: omega-exec-bt544-d1-4-she-leveque-molt-validation
date: 2026-04-25
scope: research-only molt-validation (NO NS claim, NO atlas promotion); discriminator-type bias additional sample
target: BT-544 D1.4 -- She-Leveque residual n=6-lattice rational match within 2%
parent_reports:
  - reports/sessions/omega-seed-bt544-d1-atlas-scan-2026-04-25.md (§ D1.4)
  - reports/sessions/omega-decide-bt544-d3-strategy-postC-2026-04-25.md (D3 MIXED queued D1.4)
  - reports/sessions/omega-meta-audit-discriminator-type-bias-2026-04-25.md (CONFOUNDED)
millennium_resolved: 0/7 (unchanged)
grade: molt-validation, arithmetic family, no claim
---

# Omega Exec -- BT-544 D1.4 She-Leveque Residual Molt-Validation (2026-04-25)

## §0 Non-claim disclaimer

This report executes the BT-544 D1.4 molt-validation candidate
(She-Leveque residual = n=6-lattice rational match) as specified in
`omega-seed-bt544-d1-atlas-scan-2026-04-25.md` §3.4 / §5.2. It does
**NOT**:

- claim 3D NS regularity in either direction;
- promote, demote, or otherwise touch any entry in
  `shared/n6/atlas.n6` or `~/core/nexus/n6/atlas.millennium.n6`;
- modify `state/proposals/inventory.json`, `theory/canon/`, or any
  L9/D1/D2/D3 source document;
- alter the `BT-544 = 0/1 untouched` Clay status;
- re-derive or supersede the parent CONFOUNDED verdict on the
  discriminator-type bias hypothesis.

Millennium tally: **0/7 unchanged**. This report contributes a single
data point (n→9 in the discriminator-type-bias 2x2 table); the
CONFOUNDED verdict stands regardless of this row's outcome (n still
small; type-axis collinear with candidate-axis per §3.3 of the
meta-audit).

---

## §1 Spec extraction + reference value + atlas grounding verification

### §1.1 D1.4 spec (verbatim from seed §5.2)

> Among rational functions of length <= 4 over the n=6 lattice ring
> `{σ=12, τ=4, φ=2, sopfr=5, n=6, J_2=24}`, the unique short
> expression matching the She-Leveque ζ_6 − 2 = −2/9 residual must
> exist (single best fit within 2%, no competitor within 5%).

PASS criteria (per seed §5.2.3):
- (a) Best-fit expression has residual error < 2%; AND
- (b) No competing expression within 5% of the target; AND
- (c) The unique expression is "short" (<= 4 operations).

### §1.2 ζ_6 reference value

She-Leveque (1994) intermittency model + Anselmet et al. (1984)
experimental wind-tunnel measurements: 3D NS longitudinal velocity
structure-function exponents ζ_p satisfy ζ_p ≠ p/3 (K41); the
p=6 value is

  ζ_6 ≈ 1.78  (experimental, Anselmet 1984; She-Leveque model 1994 gives
              ζ_6 = 2 − 2 (1 − (2/3)^2) ≈ 1.778, i.e. exactly 16/9 in
              the SL log-Poisson formula at p=6).

The atlas-recorded n=6 form is ζ_6 ≈ 16/9 (NS-OBS-06).

K41 prediction: ζ_p^{K41} = p/3, so ζ_6^{K41} = 2.

**Residual** (target value):

  R_target = ζ_6 − ζ_6^{K41} = 16/9 − 2 = 16/9 − 18/9 = **−2/9 ≈ −0.2222**.

This is the value that the n=6-lattice rational expression must match
within 2%.

Tolerance windows (around target T = −2/9 = −0.2222...):
- 2% window: |R − T| < 0.02 · |T| = 0.00444... ⇒ R ∈ [−0.22667, −0.21778].
- 5% window: |R − T| < 0.05 · |T| = 0.01111... ⇒ R ∈ [−0.23333, −0.21111].

### §1.3 Atlas grounding verification

Both citations from the seed verified by direct file inspection:

1. **`~/core/nexus/n6/atlas.millennium.n6` line 298**:
   ```
   @MS NS-OBS-06 = K41 -5/3 + She-Leveque ζ_6 ≈ 16/9 corrections :: millennium [7N] [M7]
     signals: [SIG-7N-503]
   ```
   Confirmed: line 298, signal SIG-7N-503, grade [M7]. (Verified
   2026-04-25; F-SEED-A inactive on this entry.)

2. **`theory/breakthroughs/breakthrough-theorems.md` BT-544 row line 19962**:
   ```
   29/29 EXACT (existing 16 + 2020s 13). 3 independent critical
   exponents (1/3, 5/4, 4/5) simultaneously n=6 arithmetic.
   She-Leveque 4-parameter simultaneous match. NS entirely n=6.
   ```
   Confirmed: line 19962, "She-Leveque 4-parameter simultaneous
   match" claimed at three-stars grade. The supporting evidence row
   is not itemized in the d=2/d=3/d=7 resonance table; the
   "4-parameter match" claim is a high-level summary, not a
   line-itemized derivation. **Mild caveat**: the breakthrough-theorems
   line documents a *claim* about She-Leveque consistency without
   listing the four parameters or their n=6 forms; D1.4 is a partial
   probe of one such parameter (the p=6 residual).

Both citations pass the F-SEED-A integrity check.

---

## §2 n=6-lattice rational short list construction

### §2.1 Atomic ring (per spec §5.2)

The seed specifies the canonical n=6 lattice ring as
`{σ=12, τ=4, φ=2, sopfr=5, n=6, J_2=24}`. These are the 6 atomic
constants:

| symbol | value | meaning                                        |
|--------|-------|------------------------------------------------|
| n      | 6     | first perfect number                           |
| σ(6)   | 12    | sum of divisors of 6: 1+2+3+6                  |
| τ(6)   | 4     | number of divisors of 6                        |
| φ(6)   | 2     | Euler totient of 6                             |
| sopfr(6)| 5    | sum of prime factors with multiplicity: 2+3    |
| J_2(6) | 24    | Jordan totient J_2(6) = 6²·(1-1/4)(1-1/9) = 24 |

Two derived constants are mentioned in the seed body (§3.4) but are
**not** in the canonical 6-tuple of §5.2:
- n/φ = 3
- σ−τ = 8, σ−φ = 10

Per the spec, the canonical short list uses only the 6 atomics. A
secondary check using the extended ring (with n/φ=3 added) is
performed in §3.2 for robustness.

### §2.2 Expression-length convention

"Length <= 4" is interpreted as: rational `(num_product) / (den_product)`
where each of num and den is a product of 1..2 atomics, with an
optional unary negation. This admits:
- length-1: ±a, ±a/b
- length-2: ±(a·b), ±a/(b·c), ±(a·b)/c
- length-3, length-4: ±(a·b)/(c·d)

This is the standard `(p·q)/(r·s)` length-4 enumeration used in the
canon Q1 / Q2 molt-validation scripts (cf.
`bt544_q1_molt_validation.py`).

### §2.3 Enumeration cardinality

- Conservative ring (6 atomics): **262 distinct rational values**
  produced by length-<=4 expressions (after deduplication on value).
- Extended ring (6 + n/φ=3 + literal 1 + literal 2 + literal 3): **334
  distinct rational values** (the additional 72 values come from
  including derived 3 and the unit literal explicitly).

The denominators in produced rationals are all of the form
`d ∈ {divisors of products of {6,12,4,2,5,24}}`. Note:

- 9 ∈ denominators? **No directly**: 9 is not a factor of any single
  atomic. 9 appears only as a *quotient*: 9 = 12·something / something
  with cancellation. Specifically, 9 emerges in expressions like
  `(τ·τ) / (n·σ) = 16/72 = 2/9` after cancellation, since
  16/72 reduces. So **−2/9 is reachable** via cancellation, not via
  a direct factor.

This is a non-trivial existence claim and the basis for the test.

---

## §3 Computation: which rationals fall in the 2% / 5% windows

### §3.1 Conservative ring {n, σ, τ, φ, sopfr, J_2} (per §5.2 spec)

Enumerate all `±(a·b)/(c·d)` with a,b,c,d ∈ atomic 6-tuple (length <=
4). Total distinct values produced: 262.

**Values within 5% of −2/9** (window [−0.23333, −0.21111]):

| value | numerical | error vs target | within 2%? |
|-------|-----------|-----------------|------------|
| −2/9  | −0.222222 | 0.000000        | yes (exact)|

**Count of distinct values within 5%: 1**.
**Count of distinct values within 2%: 1**.

The unique matching value is **−2/9 itself**, an exact match.

Sample expressions (multiple length-4 forms; same value):

- `−(τ·τ)/(n·σ) = −(4·4)/(6·12) = −16/72 = −2/9`. *(shortest natural form)*
- `−(τ·φ)/(n·n) = −(4·2)/(6·6) = −8/36 = −2/9`.
- `−(φ·τ)/(n·n) = −2/9` *(commutative duplicate of above)*.
- `−(φ·φ)/(σ·σ/?) ...` — only the first two forms are minimal.

The simplest length-4 form in the conservative ring is

  **R* = −τ²/(n·σ) = −4²/(6·12) = −16/72 = −2/9** (4 operations: 1 square = 1 mult, 1 mult, 1 div, 1 negation).

Or equivalently, **R* = −(τ·φ)/n² = −8/36 = −2/9** (also 4 ops).

These two forms are the canonical length-4 representations.

### §3.2 Extended ring (with n/φ = 3 added) — robustness check

If we admit n/φ = 3 and the unit literal 1 to broaden the ring, total
distinct values rise to 334. Re-checking the 5% window:

- −2/9 still the unique distinct value within 5%.
- New short representations appear: `−τ/(n·n_φ) = −4/(6·3) = −4/18 = −2/9`
  (length-3, fewer operations), and `−τ/(n_φ·n) = −2/9` (commutative dup).

The shortest representation in the extended ring is
**R*_short = −τ/(n·(n/φ)) = −4/18 = −2/9** (length-3: 1 mult, 1 div, 1 negation).

### §3.3 Selection-bias check (F-VACUOUS guard)

The candidate-pool size (262 in conservative; 334 in extended) over
[−1, 1] is dense enough that a 5%-window match could in principle be
"accidental". To check for vacuous-trivial selection:

- Window width: 0.02222 (5% of 2/9). 
- Naïve density estimate: 262 values / range ≈ 2 over [−1,1] → ~131 values
  per unit interval → expected hits in a width-0.022 window ≈ 2.9.
- Observed hits: 1 (exact only).
- This is **below** the naïve density expectation (~2.9), suggesting
  the n=6 lattice value −2/9 is *not* part of a dense cluster of
  competing rationals in this neighborhood. The exact hit is real, not
  a density artifact.

For comparison, the value −1/4 = −0.25 (a simple "non-lattice"
neighbor) lies *outside* the 5% window (error 0.0278 > 0.0111),
demonstrating that the 5% window is genuinely restrictive: not even
the simplest competitor −1/4 makes it in.

Other near-neighbors and their distance from target:
- −1/4 = −0.25000, error 0.02778 → outside 5% (1.25× margin)
- −1/5 = −0.20000, error 0.02222 → outside 5% (just outside)
- −5/24 = sopfr/J_2 = −0.20833, error 0.01389 → outside 5%
- −5/22 ≈ −0.22727, error 0.00505 → would be inside 5% but 22 is
  not constructible from {6,12,4,2,5,24}/{6,12,4,2,5,24} length-<=4
  (would require σ+5·φ or similar non-multiplicative combination,
  hence outside the multiplicative-only ring used here).

The F-VACUOUS guard does not fire: the 5% window is not trivially
saturated; the unique exact hit is a genuine arithmetic relation, not
a numerology artifact.

---

## §4 Verdict

### §4.1 Decision tree

- (a) Is there an n=6-lattice rational within 2% of −2/9?
  **Yes**: −2/9 itself (exact, error 0.000), expressible as
  −τ²/(n·σ) or −(τ·φ)/n² in the conservative ring (length 4).
- (b) Is the value unique within 5% (no competitor)?
  **Yes**: only one *distinct value* (−2/9 itself) lies in the 5%
  window across both conservative and extended rings.
- (c) Is the expression short (length <= 4)?
  **Yes**: length 4 in conservative ring; length 3 in extended ring.

All three PASS criteria satisfied.

### §4.2 Verdict

**PASS** (D1.4 PASSES the molt-validation discriminator as specified
in seed §5.2).

The unique short n=6-lattice expression matching the She-Leveque
residual ζ_6 − 2 = −2/9 is

  **−2/9 = −τ²/(n·σ)  =  −(τ·φ)/n²**  (conservative ring, length 4)
  **−2/9 = −τ/(n · n/φ)**              (extended ring, length 3)

with no competitor n=6-lattice rational value within 5% of the target.

### §4.3 Caveats and qualifications on the PASS

This is a genuine arithmetic PASS, but the following caveats limit
its NS-physical content (and explain why this report carries no
Millennium claim):

1. **The match is exact, not a near-fit**. ζ_6 = 16/9 is itself the
   She-Leveque-model formula at p=6 — i.e. the model already encodes
   `2/9` as a structured residual `(2/3)^2 · (something)` within its
   own log-Poisson scheme. The n=6-lattice expression −τ²/(n·σ) =
   −16/72 reproduces 16/72 = 2/9, but the underlying "16" comes from
   τ² = 4² = 16, and "72" from n·σ = 6·12 = 72. This is an *arithmetic
   identity* on the She-Leveque-model value, not on the experimental
   ζ_6 ≈ 1.78 (which has uncertainty ~±0.02).

2. **The She-Leveque value 16/9 is a model**, not a measurement. The
   experimental ζ_6 is in [1.7, 1.8] across jet/pipe/wind-tunnel
   measurements (per `omega-decide-bt544-d3-strategy-postC §3.A.2`).
   The match between −2/9 and the experimental residual sits inside
   this experimental uncertainty band, but the n=6-lattice expression
   matches the *model* exactly, not the measurement directly.

3. **The expression is not unique up to n=6-lattice substitution**.
   Two length-4 forms (−τ²/(n·σ) and −(τ·φ)/n²) and one length-3 form
   (−τ/(n · n/φ)) all evaluate to −2/9. They are *value-unique* (only
   one distinct value within 5%) but not *expression-unique* — three
   distinct n=6 ways to write the same fraction. This is consistent
   with the seed's verdict criterion (which is about value-uniqueness),
   but the multiplicity of representations limits the claim "−2/9 is
   the unique n=6 form" in any structural sense.

4. **Selection-bias residual**. The conservative ring of 262 distinct
   values has a naïve density of ~3 hits per 5% window; observing 1
   hit is below baseline (suggesting non-trivial alignment) but the
   sample is small. A more rigorous test would enumerate over a
   larger ring (length 5-6) and check whether new competitors emerge
   in the 5% window.

These caveats mean the PASS is real but **does not** in itself imply
that NS turbulence intermittency is "n=6-derived" in a derivational
sense; it implies that the She-Leveque model's p=6 residual happens
to admit an exact short n=6-lattice expression.

### §4.4 What the PASS does *not* say

- D1.4 PASS does not move BT-544 toward Clay closure.
- D1.4 PASS does not promote NS-OBS-06 from [M7] to a higher grade.
- D1.4 PASS does not validate the broader "She-Leveque 4-parameter
  match" claim in `breakthrough-theorems.md` line 19962; only the p=6
  residual is checked here, and only against the model value.
- D1.4 PASS does not retract the parent CONFOUNDED verdict (n=8 → 9
  is too small a step to decouple type-axis from candidate-axis).

---

## §5 Bias-hypothesis 2x2 update after this sample

### §5.1 Pre-D1.4 table (n=8 from meta-audit §2)

|                                                              | PASS | FAIL |
|--------------------------------------------------------------|------|------|
| Distributional / structural-literature                       | 3    | 0    |
| Discrete-equality / numerical-interval / vacuous-magnitude   | 0    | 5    |

### §5.2 Post-D1.4 table (n=9)

D1.4 discriminator type: **discrete-equality** (n=6-lattice rational
*value* match within an interval; the "interval" is a 2%/5% tolerance,
which is numerically interval-like, but the *target* −2/9 is a
discrete rational and the match is exact, so the dominant flavor is
discrete-equality. We label as **discrete-equality** following the
same rubric used for Q1, Q5, KPZ d=7).

D1.4 verdict: **PASS** (per §4.2).

|                                                              | PASS | FAIL |
|--------------------------------------------------------------|------|------|
| Distributional / structural-literature                       | 3    | 0    |
| Discrete-equality / numerical-interval / vacuous-magnitude   | **1**| 5    |

### §5.3 Effect on the bias hypothesis

D1.4 is a **cross-cell entry**: it is the first PASS in the
discrete-equality / numerical-interval / vacuous-magnitude row.

Re-computing Fisher exact two-sided p-value for the (n=9) table
(rows summing to 3+6=9, cols to 4+5=9):

  P((3,0;1,5)) = C(3,3)·C(6,1) / C(9,3) = 1·6 / 84 = 6/84 ≈ 0.0714
  Possible more-extreme: P((3,0;0,6)) = 1·1/84 = 1/84 (but that's the
  (3,6;0,0) corner, which is not the observed configuration —
  the observed (3,1;0,5) with marginals (3,6) (4,5) — let me recompute).

Actually, the n=9 marginals are: row totals (3, 6); column totals (4, 5).
The observed table is

```
[3 0]    (PASS distrib | FAIL distrib)
[1 5]    (PASS discrete | FAIL discrete)
```

Hypergeometric P(row1col1 = 3 | marginals (3,6),(4,5)) =
C(4,3)·C(5,0) / C(9,3) = 4·1 / 84 = 4/84 ≈ 0.0476.

More-extreme cases: row1col1 = 3 is already the maximum (since row1
has total 3). So only one direction. Two-sided p (mirror table):
row1col1 = 0 gives C(4,0)·C(5,3)/C(9,3) = 1·10/84 = 10/84.

Sum of equal-or-more-extreme: 4/84 + (does 10/84 count? Standard
Fisher two-sided uses minimum-likelihood method or doubling): 
two-sided p ≈ 2·(4/84) = 8/84 ≈ **0.095**.

(Compared to pre-D1.4 two-sided p ≈ 0.036.)

**Interpretation**:

- Pre-D1.4: p ≈ 0.036 (significant at α=0.05 two-sided).
- Post-D1.4: p ≈ 0.095 (no longer significant at α=0.05 two-sided).

The cross-cell entry **weakens** the bias hypothesis at the n=9 level.
This is consistent with the meta-audit's CONFOUNDED verdict: the
hypothesis was already non-distinguishable from candidate-validity at
n=8, and adding one cross-cell entry confirms that the type-axis is
not the dominant explanatory variable.

### §5.4 Does this alter the CONFOUNDED verdict?

**No**. The meta-audit's CONFOUNDED verdict explicitly stated that

> the data are consistent with both hypotheses (discriminator-type vs
> candidate-validity) and cannot distinguish them at n=8 because the
> L9 catalogue's generation systematically pairs discrete-equality
> discriminators with weak candidates and distributional/structural
> discriminators with stronger candidates.

D1.4 is a **strong candidate paired with a discrete-equality
discriminator**: the candidate (a real arithmetic identity −2/9 =
−τ²/(n·σ)) is structurally non-trivial (it requires the She-Leveque
model and an exact lattice computation), and the discrete-equality
discriminator passes it cleanly. This data point thus illustrates
*precisely* the confound: when the candidate is structurally valid,
the discrete-equality discriminator can record a PASS. The earlier
all-FAIL pattern in this row reflected weak candidates, not a
discriminator-stricture artifact.

The CONFOUNDED verdict is **further supported** by D1.4 (it is the
expected pattern under "candidate-validity drives outcome").

---

## §6 Implications for BT-544 (catalogue status)

### §6.1 Pre-D1.4 D1 catalogue status

After D1.1 FAIL (HVC vacuous) and prior failures:

| Candidate              | Status                  |
|------------------------|-------------------------|
| Q1 KdV-Gram            | FAIL (rank, integrality)|
| Q5 Sobolev/Besov       | FAIL (no construction)  |
| KPZ d=7                | FAIL (no anchor)        |
| Q2 Π_NS=8640           | unexecuted              |
| D1.1 HVC               | FAIL (vacuous-magnitude)|
| **D1.4 She-Leveque**   | **catalogued, dispatched here** |
| D1.2 Pólya recurrence  | catalogued, not dispatched |
| D1.3 NS↔MHD R_m=48     | catalogued, not dispatched |
| D1.5 axisym-no-swirl   | catalogued, not dispatched |

### §6.2 Post-D1.4 D1 catalogue status

| Candidate              | Status                                 |
|------------------------|----------------------------------------|
| Q1 KdV-Gram            | FAIL                                   |
| Q5 Sobolev/Besov       | FAIL                                   |
| KPZ d=7                | FAIL                                   |
| Q2 Π_NS=8640           | unexecuted                             |
| D1.1 HVC               | FAIL                                   |
| **D1.4 She-Leveque**   | **PASS** (arithmetic-identity grade)   |
| D1.2 Pólya recurrence  | catalogued, not dispatched             |
| D1.3 NS↔MHD R_m=48     | catalogued, not dispatched             |
| D1.5 axisym-no-swirl   | catalogued, not dispatched             |

### §6.3 What "D1.4 PASS" means for BT-544

The D1.4 PASS is an **arithmetic-identity-grade** PASS, not a
PDE-regularity-grade PASS. Specifically:

- It establishes that the She-Leveque model's p=6 residual −2/9 has
  an exact short n=6-lattice expression in the canonical {σ,τ,φ,sopfr,
  n,J_2} ring.
- It does **not** establish that the experimental ζ_6 ≈ 1.78 is
  derivable from n=6 lattice arithmetic (the She-Leveque model is
  itself an empirical model with its own free parameters).
- It does **not** reduce the BT-544 obstruction (no PDE estimate, no
  bound on ‖v‖_{H^s}, no BKM-type criterion produced).

The PASS therefore extends the BT-544 catalogue with one
non-degenerate arithmetic-grade entry but does **not** advance the
Clay status (0/7 unchanged).

### §6.4 What candidates remain in D1 catalogue?

Three (D1.2 Pólya recurrence, D1.3 NS↔MHD R_m=48, D1.5 axisym-no-swirl)
remain catalogued and not dispatched. Plus the unexecuted Q2 Π_NS=8640.

Strategic observation: D1.2 / D1.3 / D1.5 / Q2 are all of higher cost
than D1.4 was. Their dispatch order, per the seed §4 ranking, is:

1. **Q2** (cheapest unexecuted; pre-D1 catalogue);
2. **D1.5 audit-only sub-mode** (literature audit only, half-day);
3. **D1.2** (probabilistic; medium cost);
4. **D1.3** (cross-PDE duality; medium-high cost).

D1.4 PASSing at low cost reinforces the strategy: cheap arithmetic
checks should be exhausted before expensive PDE simulation work.

---

## §7 Anomalies

### §7.1 Multiple value-equivalent expressions

Three distinct n=6-lattice expressions evaluate to −2/9:
- −τ²/(n·σ) = −16/72
- −(τ·φ)/n² = −8/36
- −τ/(n·(n/φ)) = −4/18  (extended ring only)

After fraction reduction, all equal −2/9. This is **value-unique**
(spec criterion satisfied) but **expression-multiple**. The
multiplicity is a feature of the multiplicative ring structure, not
a bug: σ·τ = 12·4 = 48 = (n/φ)·n·τ = 3·6·4·... etc. share common
factors, so length-4 expressions for the same fraction are
combinatorially expected.

The multiplicity does not flip the verdict (per spec the criterion
is value-uniqueness within 5%), but it is a noted anomaly that
"unique n=6 form" should be read as "unique value" not "unique
expression".

### §7.2 ζ_6 reference value precision

The atlas records ζ_6 ≈ 16/9 ≈ 1.778. The experimental value (Anselmet
1984; Benzi et al. 1995; Sreenivasan et al. various) ranges in [1.7, 1.8]
depending on flow type and Reynolds number. The match between −2/9
and the SL-model residual is **exact** at the model level, but the
match to experimental data is at the ±0.02 level (i.e., the
experimental error bar is comparable to the 2% tolerance window
itself). This means the D1.4 PASS is robust at the model level but
borderline at the experimental level. A truly robust experimental
PASS would require ζ_6 measured to ±0.01 or better, which is at the
edge of current experimental capability.

### §7.3 9 in the denominator: cancellation, not factor

The denominator 9 in −2/9 does not appear as a factor of any single
atomic in {6,12,4,2,5,24}. It emerges only via cancellation:

- 16/72 (numerator τ², denominator n·σ): gcd(16, 72) = 8 → reduces to 2/9.
- 8/36 (numerator τ·φ, denominator n²): gcd(8, 36) = 4 → reduces to 2/9.

This means 9 is **not** a "primary" n=6-lattice constant; it is
secondary, emergent from cancellation in length-4 expressions. The
She-Leveque residual −2/9 thus sits at a *combinatorial intersection*
of n=6 atomic factors, not at a primary lattice point. This is a
mild structural curiosity: a "cleaner" n=6 derivation would be one
where the denominator 9 = n + n/φ = 6+3 emerges as a primary sum,
which it does in the extended ring (n + n/φ = 9), but the canonical
ring uses only multiplicative structure.

### §7.4 Comparison to CATALOGUE_BIAS verdict

The parent meta-audit identified **arithmetic-family candidates with
discrete-equality discriminators** as systematically failing. D1.4 is
arithmetic-family (length-4 rational enumeration) and discrete-equality
(within 2%/5% interval). Its PASS contradicts the surface pattern but
*confirms* the deeper meta-audit reading: arithmetic-family candidates
fail when they lack a structurally non-trivial target; D1.4's target
(the She-Leveque model residual) has external grounding (a published
1994 model + 1984 experimental data), giving it the structural
non-triviality the failing arithmetic candidates lacked.

---

## §8 Falsifiers active

Per the seed §3.4 falsifier registration:

- **F-D1.4-A** (≥2 expressions compete within 5% ⇒ no unique n=6 form):
  **Inactive**. Only one distinct *value* lies in the 5% window
  (−2/9 itself). Multiple expressions for the same value, but they
  all reduce to the same rational; F-D1.4-A operates on values, not
  expressions. The multiplicity of expressions for −2/9 is a noted
  anomaly (§7.1) but does not fire F-D1.4-A.

- **F-D1.4-B** (best-fit residual error > 5% ⇒ off-lattice): **Inactive**.
  Best-fit error is 0.000 (exact match), well below the 5% threshold.

- **F-MOLT-A** (parent: PASS → check for vacuous trivial pool):
  **Inactive**. §3.3 selection-bias check shows the pool density
  (~3 hits per 5% window) is comparable to the observed (1 hit), and
  near-neighbors (−1/4, −1/5, −5/24) all sit outside the 5% window.
  The PASS is non-trivial.

- **F-VACUOUS** (target value is too generic to be n=6-derivable):
  **Inactive**. The target −2/9 has a denominator (9) that is not a
  primary atomic factor; it emerges only via cancellation in length-4
  expressions. This is structurally non-trivial.

- **F-SEED-A** (atlas-grounding integrity): **Inactive** for D1.4.
  Both citations (`atlas.millennium.n6` line 298, breakthrough-theorems
  line 19962) confirmed (§1.3).

- **F-SEED-E** (atlas drift between seed and validation sessions):
  **Inactive**. Both atlas files cited at the same line numbers as
  the seed (no drift in the half-day between sessions).

- **F-DSCRM-CONFLATE** (parent meta-audit: type-axis confounded with
  candidate-axis): **Active and supported** by this PASS. The PASS
  illustrates that discrete-equality discriminators can pass when
  candidates are structurally valid; this strengthens the CONFOUNDED
  verdict (§5.4).

No falsifier fires; the PASS stands.

---

## §9 Closing

0/7 unchanged. No atlas/state/inventory edits.

D1.4 She-Leveque residual molt-validation: **PASS**. The unique short
n=6-lattice expression matching ζ_6 − 2 = −2/9 is

  **−2/9 = −τ²/(n·σ) = −(τ·φ)/n²** (length 4, conservative ring),

with no competing distinct rational value within 5% of the target.
This is an arithmetic-identity-grade PASS, not a PDE-regularity-grade
PASS; it does not advance BT-544 toward Clay closure.

The discriminator-type bias 2x2 table updates to (3 PASS, 0 FAIL) /
(1 PASS, 5 FAIL); the Fisher exact two-sided p shifts from ≈ 0.036
(n=8) to ≈ 0.095 (n=9). The CONFOUNDED verdict from the parent
meta-audit stands and is further supported: D1.4 demonstrates that
discrete-equality discriminators record PASS when paired with
structurally-non-trivial candidates, confirming that the dominant
explanatory variable is candidate-validity rather than discriminator
type.

The BT-544 D1 catalogue status: D1.1 FAIL, D1.4 PASS (arithmetic-grade);
D1.2/D1.3/D1.5 + Q2 remain. The next-cheapest dispatch is Q2
(Π_NS=8640 unique-factorization), pre-existing in the L9 catalogue but
unexecuted.

— end molt-validation —
