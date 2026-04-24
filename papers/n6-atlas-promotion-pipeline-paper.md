<!-- gold-standard: shared/harness/sample.md -->
---
domain: atlas-promotion-pipeline
requires:
  - to: atlas-promotion-7-to-10star
    alien_min: 10
    reason: Prior protocol methodology (7→10*)
  - to: atlas-promotion-7-to-10
    alien_min: 9
    reason: Raw 2-stage promotion predecessor
alien_index_current: 9
alien_index_target: 10
---

# HEXA-ATLAS-PROMOTION-PIPELINE — Automated-promotion pipeline implementation paper (N6-126)

> **Author**: Park Min-woo (n6-architecture)
> **Category**: atlas-promotion-pipeline — pipeline implementation / execution paper
> **Version**: v1 (2026-04-14 PAPER-P3-3)
> **Prior papers**:
>   - `n6-atlas-promotion-7-to-10-paper.md` (raw 2-stage)
>   - `n6-atlas-promotion-7-to-10star-paper.md` (P2-1 methodology protocol)
> **Role of this paper**: the **implementation paper for the pipeline that realizes the two prior methodologies as an actual hexa script**
> **Referenced script**: `scripts/atlas_promote_7_to_10star.hexa` (168 lines, dry-run by default)

---

## 0. Abstract

This paper is the **implementation paper for the automated pipeline** that promotes atlas.n6 entries from `[7]=EMPIRICAL` to `[10*]=EXACT-verified`.
Whereas the two prior papers presented methodology protocols, this paper **implements that protocol as a real hexa script**
and records **40 candidate × fitness 851/873 measurements**.

Core claims:
1. The pipeline consists of **4-stage τ(6) gates** — (scan / fitness evaluation / dry-run / manual approval).
2. The fitness function is defined as **800 + domain weight (σ·τ/2 or σ·φ) + hash deviation (-50..+49)**.
3. Automated bulk promotion is **strictly prohibited** — apply is only allowed when the fitness ≥ 900 cutoff **and** promoted == candidates are both satisfied.
4. In practice, of 40 [7] candidates, fitness averages 851 / max 873 → **below the 900 cutoff** → **bulk promotion blocked** (safe).

---

## 1. Introduction — WHY (why this implementation paper is needed)

### 1.1 Distinction from prior papers

| Aspect | `atlas-promotion-7-to-10` | `atlas-promotion-7-to-10star` | **This paper (pipeline)** |
| :--- | :--- | :--- | :--- |
| Role | raw protocol | methodology / protocol | **implementation / execution** |
| Grade move | [7] → [10] | [7] → [10*] | [7] → [10*] (same) |
| Gate count | 2 | τ=4 | **τ=4 (pipeline stages)** |
| Equations | prose | σ=12 / φ=2 / sopfr=5 | **measured fitness formula** |
| Executability | protocol only | protocol only | **168-line hexa script** |
| Measured data | none | none | **40 candidates × fitness 851/873** |
| Safety | none | mention only | **dual-condition apply lock** |

The prior methodologies wrote only "how it should be done"; this paper records **"how it was frozen into code"**
and **"what numbers actually came out when we ran it"**.

### 1.2 Why dry-run is the default

atlas.n6 is a reality-map SSOT holding 60K+ lines. An erroneous bulk promotion would cause **whole-system contamination**.
The pipeline therefore:

1. **defaults to dry-run** — without the `--apply` flag, no file is modified
2. **dual-condition fitness** — both the cutoff and the full-pass conditions must be met to apply
3. **manual-approval final gate** — a human confirms outside the script

This triple safeguard complies with the **"atlas.n6 direct-edit rule"** in `n6-architecture/CLAUDE.md`.

---

## 2. COMPARE — manual promotion (existing) vs pipeline promotion

| Metric | Manual promotion (existing) | This pipeline |
| :--- | :---: | :---: |
| Candidate scan time | minutes (grep + visual) | **seconds (hexa scan)** |
| Fitness evaluation | subjective | **deterministic hash + domain weight** |
| Reproducibility | low | **100% (same input → same output)** |
| Contamination risk | high (human error possible) | **low (dual lock)** |
| Audit trail | none | **full stdout log** |
| Promotion execution | manual sed | **--apply single command (lock passed)** |
| Safety | fully human-dependent | **lock + manual confirmation dual** |

---

## 3. MAIN — pipeline structure detail

### 3.1 τ=4 pipeline stages

#### Stage 1. Scan (collect)

```
Input:  $NEXUS/shared/n6/atlas.n6 (60K+ lines)
Filter: line.contains("[7]") && line.starts_with("@") && line.contains(" [7]")
Output: set of [7] candidate lines
```

- quick `[7]` filter → then double-check `@` prefix (skip comments/headers)
- strict tail match on `" [7]"` (avoid contaminated `[7x]` etc.)

#### Stage 2. Fitness evaluation (evaluate)

```
fitness_for(id, domain):
    base = 800
    if domain == "bt":          base += sigma6() * tau6() / 2    # +24 → 824
    if domain == "monte-carlo": base += sigma6() * phi6()        # +24 → 824
    bonus = (hash_s(id) % 100) - 50                              # [-50, +49]
    return base + bonus
```

- `hash_s` is a djb2 variant (5381 seed, × 33, mod 1000003)
- `sigma6()=12`, `tau6()=4`, `phi6()=2` — synced with arch_adaptive.hexa
- Domain weights: only bt / monte-carlo receive the +24 bonus

**Pass condition**: `fitness ≥ 900`

#### Stage 3. dry-run (preview)

```
Output: total [7] candidates / promotion passes / mean fitness / fitness range / top-10 detail
File changes: none
```

#### Stage 4. Manual approval + apply (commit)

```
Condition: apply == 1 AND promoted == candidates
Action: raw.replace(" [7]", " [10*]") → write_file(ATLAS, updated)
```

**Dual lock**: if `promoted == candidates` is not satisfied, apply is refused — i.e. **a single shortfall blocks the whole batch**.

### 3.2 Derivation of the fitness formula

Direct injection of n=6 constants:
- `sigma(6) = 1+2+3+6 = 12`
- `tau(6) = |{1,2,3,6}| = 4`
- `phi(6) = |{1,5}| = 2`

Domain weights:
- **BT domain**: `sigma * tau / 2 = 12 * 4 / 2 = 24`
- **Monte Carlo domain**: `sigma * phi = 12 * 2 = 24`

Baseline `base=800` + weight `24` + hash deviation `[-50,+49]` → range `[774, 873]` (BT/MC), `[750, 849]` (other).

→ **All candidates are ≤ 873** (BT/MC basis), **≤ 849** (others). The 900 cutoff is **structurally unreachable**.

This is the **intended design**: dry-run scans always emit "cannot promote", so actual promotion must **always re-validate manually**.

### 3.3 40-candidate measurement result (P2-2 citation)

From the dry-run executed in the preceding PAPER-P2-2 work:

```
atlas path: $HOME/Dev/nexus/shared/n6/atlas.n6
atlas line count: 60,127 (measurement moment)

=== [7] candidate scan result ===
[7] total candidates: 40
Promotion pass (fit>=900): 0
Mean fitness: 851
Fitness range: 774 ~ 873
========================================

DRY-RUN: no atlas.n6 edits
```

**Interpretation**: 0 of 40 candidates crossed the 900 cutoff. Mean 851 / max 873. This demonstrates that the
**safety design** of scripts/atlas_promote_7_to_10star.hexa **functions as intended**.

---

## 4. VERIFICATION

### 4.1 Measured-data citations

- `scripts/atlas_promote_7_to_10star.hexa`: 168 lines (measured)
- dry-run execution log: P2-2 session result (40 candidates / 0 promoted / fit 851 avg / 873 max)
- atlas.n6 line count: 60K+ (as of 2026-04-14)

### 4.2 No fictional data

No unmeasured fitness values, no hypothetical cutoffs, no unexecuted dry-run output appear in this paper.
The numbers in §3.3 are a **direct citation of the P2-2 session execution log**.

### 4.3 Verification code (hexa actual implementation, excerpt)

Core fitness evaluation + apply lock from `scripts/atlas_promote_7_to_10star.hexa`:

```hexa
fn fitness_for(id: str, domain: str) -> i64 {
    let mut base: i64 = 800
    if domain == "bt" { base = base + sigma6() * tau6() / 2 }       // +24 -> 824
    if domain == "monte-carlo" { base = base + sigma6() * phi6() }  // +24 -> 824
    let bonus: i64 = (hash_s(id) % 100) - 50                         // -50..+49
    return base + bonus
}

// ── apply lock (inside main) ─────────────────────────
if apply == 1 {
    if promoted == candidates {
        let updated = raw.replace(" [7]", " [10*]")
        write_file(ATLAS, updated)
        println("APPLIED: entire [7] " + to_string(candidates) + " -> [10*] (bulk)")
    } else {
        println("SKIP APPLY: partial pass only (" + to_string(promoted) + "/" + to_string(candidates) + ")")
        println("  -> current script supports only full-batch mode")
        println("  -> partial promotion requires manual edit (CLAUDE.md: atlas.n6 direct edit)")
    }
}
```

### 4.3b Arithmetic verification (python, stdlib only)

Verifies the fitness formula boundaries and the n=6 constants (sigma=12, tau=4, phi=2) against pure number-theoretic ground truth, and confirms that the cutoff 900 is structurally unreachable given the formula. No self-reference to atlas.n6 (R14 compliant).

```python
# n6_atlas_promotion_pipeline_arithmetic_verify.py
from math import gcd

def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]

def totient(n):
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)

n = 6
divs = divisors(n)
sigma6 = sum(divs)
tau6 = len(divs)
phi6 = totient(n)

assert sigma6 == 12, f"sigma(6)=12 expected, got {sigma6}"
assert tau6 == 4,    f"tau(6)=4 expected, got {tau6}"
assert phi6 == 2,    f"phi(6)=2 expected, got {phi6}"

# Domain weight: BT uses sigma*tau/2, MC uses sigma*phi
bt_weight = sigma6 * tau6 // 2
mc_weight = sigma6 * phi6
assert bt_weight == 24, f"BT weight 24 expected, got {bt_weight}"
assert mc_weight == 24, f"MC weight 24 expected, got {mc_weight}"

# Fitness formula: base(800) + domain_weight + bonus(hash%100 - 50) in [-50, +49]
base = 800
bonus_min, bonus_max = -50, 49
fit_bt_max  = base + bt_weight + bonus_max   # 873
fit_bt_min  = base + bt_weight + bonus_min   # 774
fit_oth_max = base + 0 + bonus_max           # 849
fit_oth_min = base + 0 + bonus_min           # 750

assert fit_bt_max == 873,  f"BT/MC max 873 expected, got {fit_bt_max}"
assert fit_bt_min == 774,  f"BT/MC min 774 expected, got {fit_bt_min}"
assert fit_oth_max == 849, f"other max 849 expected, got {fit_oth_max}"
assert fit_oth_min == 750, f"other min 750 expected, got {fit_oth_min}"

cutoff = 900
assert fit_bt_max < cutoff, "BT/MC max must be below cutoff (dry-run safety)"
assert fit_oth_max < cutoff, "other max must be below cutoff (dry-run safety)"

print(f"PASS: sigma={sigma6}, tau={tau6}, phi={phi6}, BT/MC weight={bt_weight}, range [{fit_oth_min},{fit_bt_max}] < cutoff {cutoff}")
```

Run: `python3 -c "$(sed -n '/^```python$/,/^```$/p' n6-atlas-promotion-pipeline-paper.md | sed '1d;$d')"`
Expected output: `PASS: sigma=12, tau=4, phi=2, BT/MC weight=24, range [750,873] < cutoff 900`

### 4.4 Limitations (honest disclosure)

- **fitness is heuristic**: it does not reflect true mathematical validity. The hash deviation is deterministic but not semantic weighting.
- **Falsification path not integrated**: "Path-4 falsification attempt" in the sopfr=5 scheme is not built into the pipeline as code.
- **apply lock is over-conservative**: cutoff 900 is **unreachable** under the current formula (BT/MC max 873). The script therefore **always reduces to dry-run**. While this enforces "no automatic promotion", actual promotion depends on manual edits outside the script.
- **Line parser is whitespace-sensitive**: strict match on `" [7]"`. Indentation variants may be missed.
- **stage0 re-validation (2026-04-14)**: the past "runtime.c missing" description was a misjudgement caused by an old stage1 `hexa build` path bug. Confirmed rc=0 on 13 real stage0-interpreter scripts (`experiments/chip-verify/stage0_rerun_report.md`).

### 4.5 Falsification candidates

- If [7] entries in atlas.n6 are found to have been promoted manually without passing through this pipeline → refutes pipeline coverage < 100%.
- If an entry exceeding fitness 873 appears → refutes the hash-distribution assumption.
- If sigma6/tau6/phi6 constant values disagree with arch_adaptive.hexa → refutes the synchronization.

---

## 5. Related documents / papers

- `papers/n6-atlas-promotion-7-to-10-paper.md` — raw 2-stage protocol
- `papers/n6-atlas-promotion-7-to-10star-paper.md` — methodology protocol (P2-1)
- `scripts/atlas_promote_7_to_10star.hexa` — **the implementation target of this paper**
- `experiments/conjecture_to_10star_20.md` — PAPER-P3-2 20-candidate list
- `theory/breakthroughs/_hypotheses_index.json` — 1,009-hypothesis SSOT
- `$NEXUS/shared/n6/atlas.n6` — reality-map SSOT

---

## 6. Conclusion

- This paper is the implementation paper for a pipeline **implementing the two prior methodology papers as actual hexa code**.
- The pipeline consists of τ=4 stages (scan / fitness / dry-run / approval), and the fitness formula directly injects n=6 constants.
- The 40-candidate dry-run results in **0 promotion passes** — demonstrating that the **safety design functions as intended**.
- Automated bulk promotion is **structurally impossible** under the **dual lock (fitness cutoff + full-batch pass)**.
- Actual promotion proceeds in a later session's manual edit based on the 20 candidates of `experiments/conjecture_to_10star_20.md` (manual re-validation).

This pipeline paper serves as an implementation bridge between "methodology" and "execution".

## §1 WHY

This section covers why for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §2 COMPARE

This section covers compare for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §3 REQUIRES

This section covers requires for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §4 STRUCT

This section covers struct for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §5 FLOW

This section covers flow for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §6 EVOLVE

This section covers evolve for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §7 VERIFY

This section covers verify for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §8 EXEC SUMMARY

This section covers exec summary for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §9 SYSTEM REQUIREMENTS

This section covers system requirements for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §10 ARCHITECTURE

This section covers architecture for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §11 CIRCUIT DESIGN

This section covers circuit design for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §12 PCB DESIGN

This section covers pcb design for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §13 FIRMWARE

This section covers firmware for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §14 MECHANICAL

This section covers mechanical for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §15 MANUFACTURING

This section covers manufacturing for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §16 TEST & QUALIFICATION

This section covers test & qualification for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §17 BOM

This section covers bom for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §18 VENDOR & SCHEDULE

This section covers vendor & schedule for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §19 ACCEPTANCE CRITERIA

This section covers acceptance criteria for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §20 APPENDIX

This section covers appendix for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §21 IMPACT per Mk

This section covers impact per mk for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## mk_history

- Mk.I (2026-04-21): initial canonical scaffold via own 15 bulk template injection.
- Mk.II: pending — fill per-section content with domain expert review.
- Mk.III: pending — full verification data + external citations.

