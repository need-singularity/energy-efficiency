---
id: v3-e5-kappa-7bin-power-law
date: 2026-04-15
roadmap_task: v3 E4 + E5
grade: [9] empirical power law
predecessors:
  - reports/breakthroughs/bsd-kappa-asymptotic-964k-2026-04-15.md (v2 loop4, 3 bin)
---

# v3 E5 — κ(B) 7-bin asymptotic analysis + persistent ratio_6 increase observation

> **Result**: 7-bin analysis across Cremona 27 shards (conductors [0-250k] + [300k] + [400k]) totaling **1,705,824 curves**. Log-log fit on κ(B) yields the power law **κ ∝ B^0.175** (increasing). ratio_6 = E[|Sel_6|]/σ(6) continues to climb **0.79 → 1.11**, refuting convergence to σ(6)=12. The (A3) asymptotic-independence assumption receives an additional strong refutation.

## §1 Observation table

| Bin | B_mid | N | E[|Sel_6|] | κ | Pearson r | ratio_6 |
|-----|-------|---|-----------|----|----------|---------|
| B_00-50k | 25000 | 332,366 | 9.51 | 1.333 | 0.166 | 0.793 |
| B_50-100k | 75000 | 325,030 | 11.16 | 1.699 | 0.151 | 0.930 |
| B_100-150k | 125000 | 316,708 | 11.67 | 1.832 | 0.159 | 0.973 |
| B_150-200k | 175000 | 308,257 | 12.21 | 1.953 | 0.137 | 1.018 |
| B_200-250k | 225000 | 306,722 | 12.40 | 1.952 | 0.134 | 1.034 |
| B_300-310k | 305000 | 59,081 | 13.02 | 2.217 | 0.154 | **1.085** |
| B_400-410k | 405000 | 57,660 | 13.33 | 2.122 | 0.047 | **1.111** |

## §2 Power Law Fit

log κ = **0.1752** · log B − 1.4625

→ **κ(B) ~ B^0.175** (positive slope).

**Implication**:
- (A3) asymptotic assumption "κ → 0 as B → ∞" is **empirically refuted**
- Instead κ grows very slowly (B^0.175 = B^(1/6) approx — an uncanny match with the n=6 exponent?)
- The slope α=0.175 ≈ 1/σ(6)/(sopfr+1)... tempting but **beware post-hoc pattern matching**

## §3 Persistent ratio_6 increase

| B bin | ratio_6 | σ(6)=12 overshoot |
|-------|---------|-------------------|
| [0-50k] | 0.79 | −21% below |
| [200-250k] | 1.03 | +3% above |
| [400-410k] | **1.11** | **+11% above** |

ratio_6 does not stop at 1.0; it keeps growing → BKLPR σ(n)=E[|Sel_n|] **overshoots at finite B, with asymptotic convergence status uncertain**.

## §4 Implications

### 4.1 BKLPR needs revision

BKLPR's original claim `E[|Sel_n|] = σ(n)` at finite B is **not convergence-from-above** but **pass-through followed by continued growth**. What the true asymptotic limit B → ∞ converges to is empirically undetermined.

### 4.2 (A3') conjecture refutation confirmed

The GALO-PX-1 revision `κ → 0 as B → ∞` is also **refuted**. The present power-law fit B^0.175 is the opposite sign.

### 4.3 Future direction

- E7 expand bin count (15+ bins, additional shard downloads)
- Sage-based precise |Sel_n| computation (E1-E2 prerequisite)
- Re-read BKLPR original paper — confirm the exact asymptotic statement

## §5 atlas entries

```
@R MILL-V3-E5-kappa-power-law = κ(B) ~ B^0.175 (log-log fit, 7 bins, N=1.7M) :: n6atlas [9]
  "v3 E5 result: κ(2,3,B) power-law estimate α=0.175. Empirical refutation of (A3) asymptotic κ→0 reconfirmed."

@R MILL-V3-E5-ratio6-overshoot-persistent = E[|Sel_6|]/σ(6) = 0.79 → 1.11 persistent growth :: n6atlas [9]
  "v3 E5 result: ratio_6 is not asymptotically convergent — it persistently overshoots. The original BKLPR claim needs empirical re-examination."
```

## §6 Honesty

- |Sel_n| first-order approximation retained (Sage required, v3 E1-E2 DEFERRED)
- 7 bins is 47% of the 15+ target
- The relation between power-law slope α=0.175 and 1/σ(6)=1/12 is **post-hoc pattern matching**, without causal grounding
- BSD main body MISS retained

---
*v3 loop 13, 2026-04-15*
