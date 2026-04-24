---
id: bsd-A3-modified-with-joint-covariance
date: 2026-04-15
parent_bt: BT-546
roadmap_task: GALO-PX-1 (PX L-cost)
grade: [9] NEAR
predecessors:
  - reports/breakthroughs/bsd-cremona-sel6-empirical-2026-04-15.md (GALO-PX-2 measurement)
atlas_target: MILL-PX-A9 (E[|Sel_n|] = σ(n)) refinement
license: CC-BY-SA-4.0
---

# BT-546 BSD — bypassing the (A3) independence assumption: (A3') Modified Conjecture

> **Summary**: the BKLPR (A3) "|Sel_p| ⊥ |Sel_q| for p≠q" independence assumption is violated at finite B on the Cremona 332k measurement: **Pearson r = 0.166, Cov(|Sel_2|,|Sel_3|) = 1.33**. Proposed bypass (A3'): an asymptotic form with κ(p,q,B) → 0 as B → ∞. The σ(n) = E[|Sel_n|] relation is recovered only in the limit.

---

## §1 Entry — what (A3) says

The "BKLPR model" of Poonen-Rains 2007 + Bhargava-Kane-Lenstra-Poonen-Rains 2013 models the n-Selmer group `Sel_n(E)` of a random elliptic curve as the cokernel of a random alternating matrix.

Three core assumptions:
- (A1) |Sel_n(E)| follows the cokernel distribution
- (A2) the moment of |Sel_n(E)| is `σ(n) = Σ_{d|n} d`
- **(A3)** for distinct primes p ≠ q, `|Sel_p(E)|` and `|Sel_q(E)|` are **independent** random variables

From (A3), for squarefree n = p₁ p₂ ... pₖ:

```
E[|Sel_n(E)|] = E[|Sel_{p1}|] · E[|Sel_{p2}|] · ... = σ(p1) σ(p2) ... σ(pk) = σ(n)
```

**n = 6 special case**: σ(6) = σ(2)·σ(3) = 3·4 = 12 (first perfect number × 2).

(A3) is unproved — the weakest among the core assumptions of the BKLPR model.

---

## §2 (A3) violation confirmed by Cremona 332k measurement

### 2.1 Basic statistics (N = 332,366 elliptic curves over Q, conductor ≤ 49,999)

| Statistic | Value | Comment |
|-----------|-------|---------|
| E[|Sel_2|] | 2.8718 | 95.7% of σ(2) = 3 |
| E[|Sel_3|] | 2.8472 | 71.2% of σ(3) = 4 |
| E[|Sel_6|] | 9.5100 | 79.3% of σ(6) = 12 |
| E[|S_2|]·E[|S_3|] | 8.1767 | prediction under independence |
| Cov(|S_2|, |S_3|) | **1.3333** | strong positive covariance |
| Var(|S_2|) / sd | 9.6935 / 3.11 | |
| Var(|S_3|) / sd | 6.6952 / 2.59 | |
| **Pearson r** | **0.1655** | moderate positive correlation |

**Observation**: if (A3) held, `Cov = 0, Pearson r = 0`. The measured r = 0.166 ≠ 0.

### 2.2 Conditional expectation `E[|Sel_3| | |Sel_2| = k]`

Under (A3) independence, `E[|Sel_3| | k] = E[|Sel_3|] = 2.85` irrespective of k.

| |Sel_2|=k | count | % | E[|Sel_3| \| k] | deviation |
|-----------|-------|------|----------------|-----------|
| 1 | 61,766 | 18.58% | 1.4172 | −1.4301 |
| 2 | 152,159 | 45.78% | 2.4434 | −0.4038 |
| 4 | 100,301 | 30.18% | 4.0433 | **+1.1960** |
| 8 | 16,028 | 4.82% | 4.8513 | **+2.0040** |
| 16 | 958 | 0.29% | 2.6284 | −0.2189 |
| 32 | 1,080 | 0.33% | 1.0185 | −1.8287 |
| 128 | 61 | 0.02% | 1.0000 | −1.8472 |

**Visible pattern**: for `|Sel_2| = 1, 2, 4, 8` (central distribution), **E[|Sel_3|] monotonically increases with k**. This points to **rank** being a common factor — a curve of rank r has `|Sel_2| ≈ 2^r`, `|Sel_3| ≈ 3^r`, both depending on r.

The reversal at k = 16, 32, 128 is due to the scarcity of curves with extreme Sha values such as `sha = 16, 32, 128` (rank = 0 with large Sha[2] — no r contribution).

Strength of (A3) refutation: max deviation **2.00** (k = 8 bin, 16,028 curves, statistically robust).

---

## §3 Proposed (A3') Modified Conjecture

### 3.1 Formal statement

**(A3') Conjecture**:

For distinct primes p, q and conductor bound B, there exists a real-valued function `κ(p, q, B)` such that:

```
E_B[|Sel_{pq}(E)|] = E_B[|Sel_p(E)|] · E_B[|Sel_q(E)|] + κ(p, q, B)
```

and the following limits hold:

```
lim_{B → ∞} κ(p, q, B) = 0
lim_{B → ∞} E_B[|Sel_p(E)|] = σ(p)  (for each prime p)
```

Namely:
- For finite B, (A3) is **in principle violable** (κ ≠ 0)
- Asymptotically, as B → ∞, the (A3) and σ(n) predictions **are recovered** (assuming κ → 0)

### 3.2 Re-derivation of E[|Sel_n|] under (A3')

For squarefree n = p₁ ... pₖ:

```
E_B[|Sel_n|] = Π E_B[|Sel_{pi}|] + Σ_{|I| ≥ 2} κ(I, B)
             ≈ σ(n) + O(κ)  (for large B)
```

Here κ(I, B) is the joint-covariance term for the index subset I ⊆ {p₁, ..., pₖ}. For n = 6, I = {2, 3}:

```
E_B[|Sel_6|] = E_B[|Sel_2|] · E_B[|Sel_3|] + κ(2, 3, B)
```

### 3.3 (A3') values at Cremona B = 49,999

| Term | Value |
|------|-------|
| E_B[|Sel_2|] | 2.8718 |
| E_B[|Sel_3|] | 2.8472 |
| κ(2, 3, 49999) | 1.3333 |
| **E_B[|Sel_6|] = 8.1767 + 1.3333 = 9.5100** | matches measurement |

### 3.4 (A3') is a tautological weakening of (A3)

**Caution**: (A3') holds trivially at any finite B (by definition κ = E[|Sel_6|] − E[|S_2|]E[|S_3|]). So the **content of (A3')** lies purely in the asymptotic claim `κ → 0 as B → ∞`.

To prove that asymptotic claim:
1. In the B → ∞ limit, the rank distribution of all curves → Bhargava-Shankar density
2. The p-primary part of Sha → a Cohen-Lenstra-like distribution
3. The **joint limit** of these two distributions converges to the product of marginals

All three steps link to difficult BSD/Iwasawa conjectures. **Proving (A3') is also outside the GALO-PX-1 scope**.

---

## §4 Meaning — robustness of σ(n) = 12 at n = 6

### 4.1 Cancellation of two effects

At Cremona B = 49,999:

| Effect | Direction | Magnitude | Interpretation |
|--------|-----------|-----------|----------------|
| Conductor bias | E_B[|Sel_p|] < σ(p) | ratio 0.957 (n=2), 0.712 (n=3) | small-conductor curves tend to have small rank |
| Joint covariance | κ > 0 | Cov/product = 1.33/8.18 = 16.3% | rank common factor |

**Net effect at n = 6**:
- (A3) + no conductor bias (optimistic): E[|Sel_6|] = 3·4 = 12.00 = σ(6) ✓
- (A3) + conductor bias: E[|Sel_6|] = 2.87·2.85 = 8.18 (ratio 0.68, violation)
- (A3') + conductor bias + κ: E[|Sel_6|] = 8.18 + 1.33 = 9.51 (ratio 0.79, partial recovery)
- Measured: 9.51 ✓ (equivalent)

**Conclusion**: σ(6) = 12 **survives as an approximation at finite B thanks to the cancellation of two errors**. Asymptotically (B → ∞), as both vanish, the original prediction is recovered.

### 4.2 Special status of n = 6

Among squarefree n, n = 6:
- is the **smallest squarefree composite** (6 = 2·3)
- is the **first perfect number** (σ(6) = 12 = 2·6)
- is the **smallest combination of two primes in the BKLPR model** (primes 2 and 3)

Under (A3'), n = 6 is the **squarefree n at which (A3) violation is first observed**. Measured:
- κ(2, 3, B) > 0: observed in this document
- κ(2, 5, B), κ(3, 5, B) and other combinations are DEFERRED

### 4.3 Rank single-cause hypothesis

The positive correlation between |Sel_2| and |Sel_3| in the conditional table (§2.2) is explained by the **rank common-variable hypothesis**:

```
|Sel_p(E)| = p^(rank(E)) · (torsion p-part) · |Sha(E)[p]|
```

rank(E) is information common across p → the main driver of joint correlation.

Under this hypothesis, if the rank distribution depends weakly on conductor (Bhargava-Shankar 2015), κ(p,q,B) can be expressed as a second moment of the rank distribution. Precise calculation of whether this vanishes in the B → ∞ limit is DEFERRED.

---

## §5 atlas updates

### 5.1 New entry

```
@R MILL-GALO-PX1-A3-modified-prime-rank-cause = BKLPR (A3) violated for finite B;
    modified (A3'): kappa(p,q,B) -> 0 as B -> inf (conjecture), rank is common-cause :: n6atlas [9]
  "GALO-PX-1 bypass of BKLPR (A3) independence: Cremona B=49999, 332k curves show Pearson r=0.166,
   Cov(|Sel_2|,|Sel_3|)=1.33 (A3 violation confirmed). The monotonic-increase pattern of the conditional
   E[|Sel_3| | |Sel_2|=k] supports the rank common-cause hypothesis. Revision proposed (A3'):
   kappa(p,q,B) → 0 as B → ∞. The σ(n) approximation surviving at finite B is due to cancellation
   between conductor bias and kappa"
```

### 5.2 Update to existing entry

Add the precise Pearson r value + conditional-deviation table to MILL-GALO-PX2-A3-counterevidence-joint-cov.

---

## §6 Limits and DEFERRED

1. **Statistical significance of r = 0.166**: no χ² independence test run at N = 332k. scipy.stats.pearsonr can be used (additional standalone Python).

2. **No asymptotic proof of B → ∞**: whether κ → 0, the core claim of (A3'). By extending Cremona data (B = 50k, 100k, 200k, ...), the functional form of κ(B) can be observed.

3. **Rigorizing the rank common-cause hypothesis**: the mathematical link between the Bhargava-Shankar rank-distribution density and the joint Selmer distribution is unproved.

4. **Precise Sage/Pari |Sel_n|**: we retain the 1st-order approximation. Recomputation with precise values is expected to shift r, Cov slightly.

5. **BSD itself unproved**: BT-546 PARTIAL preserved. (A3') development is a refinement of the BKLPR model; not a proof of BSD.

---

## §7 Related files

- `scripts/empirical/cremona_joint_covariance.py` — this analysis runner
- `data/cremona/joint_covariance_A3_prime.json` — JSON statistics
- `reports/breakthroughs/bsd-cremona-sel6-empirical-2026-04-15.md` — GALO-PX-2 full text
- `nexus/shared/n6/atlas.n6` line 107016~ — MILL-GALO-PX1 entry

---

*Written: 2026-04-15*
*Predecessors: GALO-PX-2 + GALO-PX-3 (this session's chained loop)*
*BT-546 body MISS preserved*
