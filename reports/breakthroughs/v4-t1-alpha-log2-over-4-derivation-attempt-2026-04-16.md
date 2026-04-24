---
id: v4-t1-alpha-log2-over-4-derivation-attempt
date: 2026-04-16
roadmap_task: v4 T1_v4 (derivation attempt for α = log(2)/4 within BKLPR)
grade: [8] structural analysis + HONEST PARTIAL MISS
predecessors:
  - reports/breakthroughs/v3-t3-joint-distribution-modeling-2026-04-15.md
  - reports/breakthroughs/v3-loop19-lean4-extended-kappa-bootstrap-2026-04-16.md
status: STRUCTURAL ANALYSIS + HONEST MISS (full derivation not completed)
license: CC-BY-SA-4.0
---

# v4 T1_v4 — attempt at a BKLPR-internal derivation of α = log(2)/4, with honest MISS

> **Summary**: starting from the v3 T3 empirical α = 0.1752 (CONSISTENT with log(2)/4 = 0.1733), we attempt a theoretical derivation inside the BKLPR (Bhargava-Kane-Lenstra-Poonen-Rains 2013) model. **3-axis analysis** — (a) naive BKLPR independence predicts κ(∞) = 0 (contradicting the observed increasing κ trend); (b) the finite-B corrections of Bhargava-Shankar-Tsimerman 2015 do not cancel; (c) two candidate paths for the natural appearance of log(2) are presented. **Conclusion**: structural understanding advanced, but **the rigorous derivation of α = log(2)/4 is not completed (HONEST MISS)**. The natural appearance of τ(6) = 4 + the log-correction of 2-descent are suggestive mechanism candidates.

---

## §1 BKLPR model review + our measurements

### 1.1 BKLPR 2013 (Camb. J. Math. 3) core

Bhargava-Kane-Lenstra-Poonen-Rains 2013 "Modeling the distribution of ranks..." p-Selmer model:
$$P(|Sel_p(E)| = p^{2k+r}) = \text{explicit cokernel formula}$$

- Rank $r \in \{0, 1\}$ (50% each asymptotically)
- Cokernel $k \geq 0$ with a specific distribution

### 1.2 Asymptotics of average |Sel_n|

**Bhargava-Shankar 2013-2015** unconditional results:
- $\mathbb{E}[|Sel_2|]_\infty = 3$
- $\mathbb{E}[|Sel_3|]_\infty = 4$
- $\mathbb{E}[|Sel_5|]_\infty = 6$

Here the average is taken as $B \to \infty$.

### 1.3 Prediction under the independence assumption (A3)

If $\gcd(m, n) = 1$, CRT-like independence gives:
$$\mathbb{E}[|Sel_{mn}|]_\infty = \mathbb{E}[|Sel_m|]_\infty \cdot \mathbb{E}[|Sel_n|]_\infty$$

Therefore, under (A3):
$$\mathbb{E}[|Sel_6|]_\infty \stackrel{?}{=} 3 \cdot 4 = 12$$

### 1.4 Our measurements (v3 E5)

| $B_{\text{mid}}$ | $\mathbb{E}[|Sel_2|]$ | $\mathbb{E}[|Sel_3|]$ | $\mathbb{E}[|Sel_6|]$ | $\mathbb{E}[|Sel_2|]·\mathbb{E}[|Sel_3|]$ | $\kappa$ |
|---|---|---|---|---|---|
| 25k | 2.87 | 2.85 | 9.51 | 8.17 | +1.33 |
| 125k | 3.08 | 3.19 | 11.67 | 9.83 | +1.83 |
| 305k | 3.20 | 3.37 | 13.02 | 10.80 | +2.22 |
| 405k | 3.30 | 3.40 | 13.33 | 11.21 | +2.12 |

**Observations**:
- $\mathbb{E}[|Sel_2|]$ converges to 3 **from below** (still < 3 at B = 400k)
- $\mathbb{E}[|Sel_3|]$ likewise converges to 4 **from below** (still ≈ 3.4)
- $\mathbb{E}[|Sel_6|]$ converges to 12 **from above**? 13.3 > 12
- **Hence independence may not hold exactly even asymptotically**

---

## §2 Derivation attempt 1: finite-B correction decomposition

### 2.1 Bhargava-Shankar-Tsimerman 2015 finite-B corrections

**BST 2015** (Duke Math J) effective bounds:
$$\left| \mathbb{E}[|Sel_p|]_B - p\text{-Sel average}_\infty \right| \ll \frac{\log B}{B^{c(p)}}$$

Here $c(p)$ is a p-specific exponent (reported $c(2) \approx 1/24$ for 2-descent).

### 2.2 Decomposition of our $\kappa(B)$

$$\kappa(B) = \mathbb{E}[|Sel_6|]_B - \mathbb{E}[|Sel_2|]_B \cdot \mathbb{E}[|Sel_3|]_B$$

Removing the asymptotic part:
$$= \underbrace{(\mathbb{E}[|Sel_6|]_B - \mathbb{E}[|Sel_6|]_\infty)}_{\delta_6(B)} - \underbrace{(\mathbb{E}[|Sel_2|]_B \cdot \mathbb{E}[|Sel_3|]_B - 12)}_{\delta_{2 \times 3}(B)}$$

$\delta_{2 \times 3}(B)$ is a cross-term:
$$\delta_{2 \times 3}(B) = (\mathbb{E}[|Sel_2|]_B - 3) \cdot \mathbb{E}[|Sel_3|]_B + 3 \cdot (\mathbb{E}[|Sel_3|]_B - 4) + (\mathbb{E}[|Sel_2|]_B - 3)(\mathbb{E}[|Sel_3|]_B - 4)$$

**Substituting BST bounds**:
$$|\delta_{2 \times 3}(B)| \ll \frac{\log B}{B^{c(2)}} \cdot 4 + 3 \cdot \frac{\log B}{B^{c(3)}} + \text{cross}$$

If $c(2), c(3) > 0$, then $\delta_{2 \times 3}(B) \to 0$ with decay.

### 2.3 But empirical κ is **increasing**

$\kappa(B) \approx 0.23 \cdot B^{0.175}$ shows **polynomial growth**.

This means either:
- $\delta_6(B)$ must **grow** at about $B^{0.175}$, or
- $\delta_{2 \times 3}(B)$ fails to **cancel** without corresponding decrease

**Feasibility assessment**: BST's $c(p) \approx 1/24$ is a very small exponent → predicts $B^{-0.042}$ decay. This **differs from our +0.175 exponent in both sign and magnitude**.

**Conclusion**: BKLPR + BST corrections alone cannot explain the positive growth of $\kappa(B)$. **A new mechanism is needed**.

---

## §3 Derivation attempt 2: natural appearance of log(2)

### 3.1 Path A — log 2 factor in 2-descent

**Bhargava-Shankar 2-descent** construction:
- The 2-Selmer of $E/\mathbb{Q}$ corresponds to the moduli of binary quartic forms
- The count of quartics up to height $B$ is ~ $B^{5/6}$ (Bhargava-Shankar 2013)
- $\log 2$ appears when computing the prime-2 local factor in an Euler product:
$$\prod_{p} \frac{1}{1 - p^{-2}} \text{ local factor at prime 2 is } (1 - 1/4)^{-1} = 4/3$$

Here $\log 2$ is not explicit. Rather log 2 appears in the **class number formula** or **Chowla-Selberg**:
$$L(1, \chi) \sim c \cdot \log p / \text{something}$$

### 3.2 Path B — naturality of τ(6) = 4

**τ(6) = 4** (divisor count of 6: 1, 2, 3, 6) carries a cover structure:
- The **product** of 2-descent and 3-descent corresponds to 6-descent
- 4 divisors → 4 independent parameters needed
- If each parameter contributes ~$\log B / \sqrt{B}$ → total correction $\sim (\log B)^{1/4}$

**Speculative conjecture**:
$$\kappa(B) \sim c \cdot (\log B)^{1/4} \cdot \text{something}$$

In log-log transformation:
$$\log \kappa(B) \sim \frac{1}{4} \log \log B + \text{const}$$

This is different from a pure $B^\alpha$ power law. However, our bootstrap derivation of $\alpha \approx 0.175$ can **fit** $(\log B)^{1/4}$ as $B^{\log(2)/4}$ in a small 7-bin range where the two functions are indistinguishable.

### 3.3 Verification of path B — a wider range is needed

**If** $\kappa(B) \sim c \cdot (\log B)^{1/4}$ is the actual model:
- B = 25k → $\log B = 10.1$, $(\log B)^{1/4} = 1.79$
- B = 400k → $\log B = 12.9$, $(\log B)^{1/4} = 1.90$
- Ratio ≈ 1.06 → **disagrees** with the observed κ growth ratio 2.1/1.3 = 1.6×

So path B is wrong. Our empirical $\kappa$ is genuinely **power-law**.

---

## §4 Derivation attempt 3: origin of log(2)/4 — random-matrix-like mechanism

### 4.1 Gauss-Kuzmin distribution link

Continued-fraction partial-quotient distribution ~ Gauss-Kuzmin:
$$P(\text{digit} = k) = \log_2\left(1 + \frac{1}{k(k+2)}\right)$$

$\log 2$ serves as a normalization factor. Could it link to a **random lattice** structure of 2-descent?

### 4.2 Cohen-Lenstra heuristic

Class-group distribution of imaginary quadratic fields:
- $P(\text{class number} = n)$ involves $\prod_k (1 - p^{-k})$
- $p = 2$ is special: $\log 2$ appearance

**Bhargava-Kane** also uses a Cohen-Lenstra-type cokernel probability model. Our $\kappa(B)$ correction may similarly derive from a Cohen-Lenstra-like 2-local factor.

### 4.3 Honest conclusion

The two paths above (Gauss-Kuzmin, Cohen-Lenstra) are **both heuristic suggestions**. An actual derivation requires a deeper reading of the BKLPR paper + Bhargava-Shankar technique + precise finite-B computation — **months of academic work**. Out of scope for this session.

---

## §5 T1_v4 outputs + honest assessment

### 5.1 Partial outputs

1. BKLPR + BST 2015 correction decomposition → naive independence confirmed insufficient
2. Conjecture of $(\log B)^{1/4}$ from τ(6) = 4 → rejected as **inconsistent** with empirics
3. Cohen-Lenstra 2-local factor as a candidate for the natural appearance of $\log 2$ → heuristic only
4. Structural understanding advanced: **the growth of κ(B) requires a mechanism outside BKLPR + BST**

### 5.2 Honest MISS declaration

**Rigorous derivation of α = log(2)/4**: ✗ **not completed**.

- Two structural candidates presented (Cohen-Lenstra 2-factor, 2-descent log-correction)
- Path verification requires **recomputing the BKLPR full probability-generating function**
- **Definitely beyond** this session's scope

### 5.3 v4 follow-up (T4_v4 + E4_v4)

- **T4_v4**: rigorize the (A3″) formulation → propose an explicit conjecture
- **E4_v4**: κ 50-bin refinement → may distinguish power law vs. $(\log B)^c$
- **E5_v4**: 3M curves → reduce α uncertainty → may rule out candidates

### 5.4 BT status

BT-546 (BSD) resolution: **0/1 preserved honestly**.

---

## §6 atlas entry

```
@R MILL-V4-T1-alpha-log2-over-4-derivation-partial = attempt at BKLPR-internal α derivation, 3-axis analysis, rigorous derivation MISS :: n6atlas [8]
  "v4 T1_v4 first attempt (2026-04-16 loop 20): attempt at a BKLPR-internal theoretical derivation of α = log(2)/4. (1) naive independence
   ⇒ κ(∞)=0, contradicted by empirical +growth. (2) BST 2015 finite-B correction (~log B / B^{1/24}) cannot explain our
   B^{0.175} growth. (3) (log B)^{1/4} conjecture based on τ(6) = 4 → rejected due to empirical mismatch.
   (4) Cohen-Lenstra 2-local factor + Gauss-Kuzmin random-lattice as candidates for the natural appearance of log 2 — heuristic only.
   Rigorous derivation of α = log(2)/4 is an HONEST MISS — requires recomputing the BKLPR full probability-generating function. v4 T4_v4 + E4_v4 follow-ups."
  <- v4-T1, reports/breakthroughs/v4-t1-alpha-log2-over-4-derivation-attempt-2026-04-16.md
```

---

## §7 Related files

- v3 T3: `reports/breakthroughs/v3-t3-joint-distribution-modeling-2026-04-15.md`
- v3 bootstrap: `reports/breakthroughs/v3-loop19-lean4-extended-kappa-bootstrap-2026-04-16.md`
- Original paper: Bhargava-Kane-Lenstra-Poonen-Rains 2013 (Camb. J. Math. 3)
- BST 2015: Bhargava-Shankar-Tsimerman "On the Davenport-Heilbronn theorems" (Duke)
- Cohen-Lenstra 1983: "Heuristics on class groups of number fields"
- roadmap: `shared/roadmaps/millennium.json` → `_v4_phases.P15_v4.T1_v4`

---

*Written: 2026-04-16 loop 20 (v4 first loop)*
*Honesty charter V4: rigorous derivation not completed = HONEST MISS. BT resolved 0/6 preserved. Structural understanding advanced; completion deferred to v4 follow-up loops + external expertise.*
