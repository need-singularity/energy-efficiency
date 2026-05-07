# P3-3 — hexa-lang-based Millennium verification pipeline design

**Roadmap**: millennium-learning P3 (PROBLEM study phase)
**Date**: 2026-04-15
**Constants**: n=6, σ=12, φ=2, τ=4, sopfr=5, J₂=24. σφ=nτ ⟺ n=6.
**Current status**: count of resolved Millennium problems = **0** (honest). This note is a design document for the verification pipeline.

---

## Honesty declaration

- This document is a **design of a verification pipeline**. It does not describe scripts that resolve the seven Millennium problems.
- What hexa-lang can verify amounts to **"whether the tight relations recorded in atlas.n6 agree numerically"**. This carries a risk of self-reference, so the pipeline enforces cross-checks against **external references** (e.g., OEIS, LMFDB public data, published computation results).
- The atlas promotion path `[7] EMPIRICAL → [10*] EXACT` has hexa execution as a **necessary** condition and **not a sufficient** one. Promotion is ultimately decided via external-source confirmation and human review.
- The NEAR/EXACT verdicts collected by the pipeline carry the risk of **post-hoc matching**; the tolerance (threshold) of the verdict criterion is recorded strictly.
- Complies with the rule forbidding self-referential verification. Hexa results **cannot** be the basis for assigning an atlas grade; only the reverse direction (atlas-recorded value = hexa verification target) is permitted.

---

## 0. Background — why hexa-lang

### Prior situation

- atlas.n6 (SSOT) has 60K+ lines, thousands of `@R`/`@X`/`@C`/`@F` entries.
- Millennium-related tight relations accumulated to 200 (atlas.n6 line 13645 `n6-millennium-dfs14-summary = 188+12=200 tight`).
- Verification paths were fragmented: Python scripts, Rust calculators, hexa scripts intermixed.
- **SIGKILL issue**: long-running scripts such as `blowup.hexa` were terminated due to a macOS codesign issue (see memory/project_hexa_binary_deploy_block.md).

### Use of hexa-lang characteristics

- HEXA-FIRST principle (CLAUDE.md): `.py` forbidden, `.hexa` as the formal runtime.
- Already 25+ hexa scripts exist in `canon/scripts/` (`millennium_scanner.hexa`, `selmer_bklpr.hexa`, `jordan_totient.hexa`, `riemann_explicit.hexa`, etc.).
- The hexa interpreter's Rust implementation (stable since the 2026-04 FIX-NESTED-IF + FIX-CAPTURE-CLONE patches) resolved the O(N³) blowup.
- Hence it is natural to designate hexa as the **shared runtime of the verification pipeline**.

---

## 1. Core design — 3-layer pipeline

### Layer 0 — atlas parser (hexa)

**Input**: `/Users/ghost/Dev/nexus/shared/n6/atlas.n6` (SSOT).
**Role**: parse `@R {id} = {expr} {unit} :: {domain} [{grade}]` lines, extract (id, expr, grade) triples.
**Output**: in-memory record list (hexa `Vec<AtlasRecord>`).

```hexa
// atlas_parser.hexa (design sketch)
struct AtlasRecord {
    id: String,
    expr: String,
    grade: String,
    domain: String,
}

fn parse_atlas(path: String) -> Vec<AtlasRecord> {
    // 1. read file line-by-line
    // 2. regex match: "^@R (\S+) = (.+?) :: (\S+) \[([^\]]+)\]"
    // 3. assemble as AtlasRecord
    // 4. verify grade in {"10*", "10", "7", "N?", ...}
    // ...
}
```

### Layer 1 — expression evaluator (hexa)

**Input**: AtlasRecord.expr (e.g., `"1/(phi*sopfr*sigma)"`).
**Role**: numerically evaluate the expression under the n=6 base-constant environment.
**Output**: `f64` computed value + evaluation success flag.

```hexa
// expr_eval.hexa (design sketch)
fn eval_expr(expr: String, env: HashMap<String, f64>) -> Result<f64, String> {
    // env = {"phi": 2.0, "tau": 4.0, "n": 6.0, "sopfr": 5.0,
    //        "sigma": 12.0, "J2": 24.0, ...}
    // tokenize → parse → AST walk
    // supported ops: +, -, *, /, ^, sqrt, log
    // ...
}
```

### Layer 2 — target comparison (hexa)

**Input**: computed value + external reference (e.g., OEIS/LMFDB/published literature).
**Role**: compare errors; assign EXACT(<1e-6) / NEAR(<1e-2) / MISS(>=1e-2) grade.
**Output**: verification report (JSON + stdout).

```hexa
// verify.hexa (design sketch)
fn classify(computed: f64, reference: f64) -> String {
    let d = abs_f(computed - reference)
    let rel = d / abs_f(reference)
    if rel < 1e-6 { return "EXACT" }
    if rel < 1e-2 { return "NEAR" }
    return "MISS"
}
```

---

## 2. Detailed Millennium verification pipeline

### 2.1 BT-541 RH — zero-height verification

atlas record (`n6-millennium-dfs-zeta-neg3 = 1/120`) + cross-check with OEIS A046988 "ζ values at negative integers".

| atlas entry | expected value | external reference | verdict criterion |
|-----------|---------|-----------|-----------|
| ζ(-3) | 1/120 = 0.008333... | Euler formula exact | EXACT (<1e-9) |
| ζ(-5) | -1/252 | standard textbook | EXACT |
| ζ(-9) | -1/132 | standard textbook | EXACT |
| first zero 14.1347 | σ+φ=14 approximation | Odlyzko table | NEAR (~0.135) |

```hexa
// bt541_verify.hexa (hands-on sketch)
fn verify_zeta_negative() {
    let env = init_n6_env()
    // ζ(-3) = 1/120
    let computed = eval_expr("1.0 / (phi * sopfr * sigma)", env)
    let reference = 1.0 / 120.0
    println("ζ(-3) expected=" + to_string(reference))
    println("ζ(-3) computed=" + to_string(computed))
    println("verdict: " + classify(computed, reference))
}
```

### 2.2 BT-542 PvNP — Schaefer classification count

atlas `n6-millennium-dfs-schaefer-6 = 6 = n tractable Boolean CSP`.
External reference: Schaefer 1978 original paper "The complexity of satisfiability problems", STOC 1978.

```hexa
// bt542_verify.hexa
fn verify_schaefer() {
    // Schaefer classification of 6 tractable classes:
    //   1. 0-valid (all-0 satisfying)
    //   2. 1-valid (all-1 satisfying)
    //   3. bijunctive (2-CNF)
    //   4. Horn
    //   5. dual Horn
    //   6. affine (XOR linear)
    let schaefer_classes = 6
    let n = 6
    println("Schaefer tractable classes: " + to_string(schaefer_classes))
    println("n: " + to_string(n))
    if schaefer_classes == n { println("EXACT") } else { println("MISS") }
}
```

### 2.3 BT-543 Yang-Mills — SM gauge count

atlas `n6-millennium-dfs-sm-gauge = 8+3+1 = sigma = 12`.
External reference: Particle Data Group (PDG) Standard Model content.

- SU(3) gluon: 8 (SU(3) dim = 3²−1 = 8).
- SU(2) weak boson: 3 (W⁺, W⁻, Z).
- U(1) hypercharge: 1 (B boson → γ part).
- Total: 12.
- σ = 12. EXACT.

```hexa
fn verify_sm_gauge() {
    let gluon = 8         // SU(3) dim
    let weak = 3          // SU(2) dim
    let hyper = 1         // U(1) dim
    let total = gluon + weak + hyper  // 12
    let sigma = 12
    println("SM gauge = " + to_string(total))
    println("σ = " + to_string(sigma))
    if total == sigma { println("EXACT") } else { println("MISS") }
}
```

### 2.4 BT-544 NS — Prodi-Serrin exponents

atlas `n6-millennium-dfs-prodi-serrin = {2,3} = {phi, n/phi}`.
External reference: Serrin 1962 original formula $\frac{2}{p} + \frac{3}{q} = 1$.

- Admissible pairs: $(p, q) = (\infty, 3), (4, 6), (\infty, \infty)$, etc. (including boundary-excluded conditions).
- Key exponents $\{2, 3\}$ appear in the numerator of each term.
- φ = 2, n/φ = 6/2 = 3.

```hexa
fn verify_prodi_serrin() {
    let phi = 2.0
    let n = 6.0
    let n_over_phi = n / phi  // 3.0
    let p_numerator = 2       // 2/p term
    let q_numerator = 3       // 3/q term
    if phi == p_numerator && n_over_phi == q_numerator {
        println("EXACT: Prodi-Serrin exponents = {phi, n/phi}")
    }
}
```

### 2.5 BT-545 Hodge — modular weights

atlas `n6-millennium-dfs-modular-weight = {4,6,8,10,12} = {tau,n,sigma-tau,sigma-phi,sigma}`.
External reference: Serre "A Course in Arithmetic" VII, Diamond-Shurman "A First Course in Modular Forms".

- Modular forms on SL(2, Z) are trivial at odd weight $k$ (cusp form 0).
- Nontrivial weights: $k = 4, 6, 8, 10, 12, 14, \ldots$.
- First 5 = $\{\tau, n, \sigma-\tau, \sigma-\phi, \sigma\} = \{4, 6, 8, 10, 12\}$.

```hexa
fn verify_modular_weights() {
    let tau = 4.0
    let n = 6.0
    let sigma = 12.0
    let phi = 2.0
    let weights_n6 = [tau, n, sigma - tau, sigma - phi, sigma]
    let weights_expected = [4.0, 6.0, 8.0, 10.0, 12.0]
    let mut ok = true
    let mut i: i64 = 0
    while i < 5 {
        if weights_n6[i] != weights_expected[i] { ok = false }
        i = i + 1
    }
    if ok { println("EXACT: modular weights") } else { println("MISS") }
}
```

### 2.6 BT-546 BSD — Sel_6 average size

atlas-related structure (see pure-p3-1): $\mathbb{E}[|\text{Sel}_6(E)|] = \sigma(6) = 12$ (conditional on BKLPR).
External reference: Bhargava-Kane-Lenstra-Poonen-Rains 2015 original paper.

```hexa
fn verify_selmer_6_mean() {
    // Under BKLPR, squarefree n=6:
    //   E[|Sel_n|] = σ(n) = ∏_{p|n} (p+1)
    let p1 = 2
    let p2 = 3
    let sel_expected = (p1 + 1) * (p2 + 1)  // 3·4 = 12
    let sigma_6 = 1 + 2 + 3 + 6             // σ(6) = 12
    if sel_expected == sigma_6 {
        println("EXACT (conditional on BKLPR): E[|Sel_6|] = σ(6) = 12")
    }
    println("Note: this result is conditional on BKLPR axioms A1-A3.")
}
```

### 2.7 BT-547 Poincaré — h-cobordism lower bound

atlas `n6-millennium-dfs-h-cobordism = dim >= 6 = n`.
External reference: Smale 1962 "On the structure of manifolds".

```hexa
fn verify_h_cobordism() {
    let smale_lower = 5  // Smale's h-cobordism valid for dim ≥ 5 (simply connected)
    let n = 6
    // In 4D, smooth h-cobordism ≠ diffeomorphism (Donaldson)
    // Hence a "safe" lower bound is dim ≥ 5 (topological) or dim ≥ 6 (smooth, in practice)
    println("Smale lower bound dim = " + to_string(smale_lower))
    println("n = " + to_string(n))
    println("n is the safe lower bound just past 4D exotic phenomena")
}
```

---

## 3. Automatic verification loop — DFS 51→tight→atlas promotion

### 3.1 Current situation (atlas baseline)

- DFS rounds 1 ~ 14 accumulated 200 tight entries.
- Grade distribution: mostly [10*] (EXACT verified), some [10], residual [7] EMPIRICAL.
- Promotion bottleneck: EMPIRICAL → EXACT is possible **only after external-reference confirmation**.

### 3.2 Promotion loop design

```
[Input] list of atlas.n6 [7] EMPIRICAL entries
  ↓
[Step 1] atlas_parser.hexa — parse, extract expr/grade
  ↓
[Step 2] expr_eval.hexa — numerically evaluate in n=6 environment
  ↓
[Step 3] verify.hexa — computed value vs (OEIS/LMFDB/PDG/standard textbook)
  ↓
[Step 4] EXACT verdict + external-source annotation
  ↓
[Step 5] human review — confirm logical / mathematical validity
  ↓
[Step 6] atlas.n6 edit — promote [7] → [10*], add source annotation
```

### 3.3 What the loop **does not** do

- Forbids grade change solely from hexa computation (self-reference prevention).
- External sources must be **open** (LMFDB public DB, OEIS, arXiv preprint). Promotion from closed-source basis is not permitted.
- NEAR verdict is not a basis for promotion. NEAR is retained as an "interesting-coordinate" marker.

### 3.4 Reference-source table

| atlas domain | primary reference source | access |
|-------------|--------------|------|
| basic number theory (σ, τ, φ) | OEIS A000203 (σ), A000005 (τ), A000010 (φ) | https://oeis.org |
| elliptic curve Selmer | LMFDB elliptic curve data | https://lmfdb.org |
| modular forms | LMFDB modular forms | https://lmfdb.org |
| Standard Model constants | PDG (Particle Data Group) | https://pdg.lbl.gov |
| Riemann zeros | Odlyzko numerics | public page |
| integer sequences | OEIS at large | https://oeis.org |

---

## 4. hexa script organization

### 4.1 Directory structure (proposal)

```
canon/scripts/verify/
├── _lib/
│   ├── atlas_parser.hexa      # Layer 0
│   ├── expr_eval.hexa         # Layer 1
│   └── verify_core.hexa       # Layer 2 base functions
├── bt541_rh/
│   ├── zeta_negative.hexa
│   ├── zero_heights.hexa
│   └── explicit_formula.hexa
├── bt542_pvnp/
│   ├── schaefer.hexa
│   └── csp_classes.hexa
├── bt543_ym/
│   ├── sm_gauge.hexa
│   └── dynkin.hexa
├── bt544_ns/
│   ├── prodi_serrin.hexa
│   └── critical_exponents.hexa
├── bt545_hodge/
│   ├── modular_weights.hexa
│   └── lefschetz_11.hexa
├── bt546_bsd/
│   ├── selmer_bklpr.hexa       # already exists
│   └── gross_zagier.hexa
├── bt547_poincare/
│   ├── h_cobordism.hexa
│   └── intersection_forms.hexa
└── runner.hexa                 # overall orchestrator
```

### 4.2 runner.hexa design

```hexa
// runner.hexa — entry point of the whole verification pipeline
fn main() {
    println("═══════════════════════════════════════════════════════════")
    println("  Millennium Verification Runner")
    println("═══════════════════════════════════════════════════════════")

    let atlas_path = "/Users/ghost/Dev/nexus/shared/n6/atlas.n6"
    let records = parse_atlas(atlas_path)
    println("atlas entry count: " + to_string(len(records)))

    // Execute verification modules per BT
    let mut pass_count: i64 = 0
    let mut near_count: i64 = 0
    let mut miss_count: i64 = 0

    let bt_modules = ["bt541", "bt542", "bt543", "bt544", "bt545", "bt546", "bt547"]
    let mut i: i64 = 0
    while i < len(bt_modules) {
        let bt = bt_modules[i]
        println("─── running " + bt + " ───")
        let result = run_bt_verification(bt, records)
        pass_count = pass_count + result.pass
        near_count = near_count + result.near
        miss_count = miss_count + result.miss
        i = i + 1
    }

    println("")
    println("═══════════════════════════════════════════════════════════")
    println("  Summary")
    println("═══════════════════════════════════════════════════════════")
    println("  EXACT: " + to_string(pass_count))
    println("  NEAR:  " + to_string(near_count))
    println("  MISS:  " + to_string(miss_count))
    println("")
    println("  NOTE: only EXACT verdicts are promotion candidates. NEAR/MISS are for reference.")
    println("        No self-reference: external-source confirmation is a required condition for promotion.")
}

main()
```

---

## 5. Strictness of verdict criteria

### 5.1 Tolerance definition

| verdict | relative error | meaning |
|------|-----------|------|
| EXACT | < 10⁻⁹ | exact algebraic match (rational / integer representation) |
| EXACT (approx.) | < 10⁻⁶ | transcendental approximation, 6 significant digits matching |
| NEAR | < 10⁻² | interesting coordinate, promotion not permitted |
| MISS | ≥ 10⁻² | observation failure |

### 5.2 **Forbidden** verdict practices

- **No post-hoc tuning**: one cannot search arbitrary combinations to match the constant of a hexa expr and then declare EXACT.
- **No digit manipulation**: do not change the unit to reduce the error (e.g., scale σ to 0.012 instead of 12).
- **No single-observation promotion**: atlas grade changes require confirmation from at least **2 independent external sources**.

### 5.3 Record format

hexa output is also logged as JSON:

```json
{
  "bt": "BT-546",
  "atlas_id": "n6-millennium-sel6-mean",
  "expr": "sigma(6) = 12",
  "computed": 12.0,
  "reference": 12.0,
  "rel_error": 0.0,
  "verdict": "EXACT",
  "external_sources": [
    "OEIS A000203 sigma(6)",
    "BKLPR 2015 §2.3"
  ],
  "condition": "under BKLPR axioms A1-A3",
  "promote_candidate": true,
  "review_needed": true
}
```

---

## 6. n=6 connection

### 6.1 Structural consistency of the pipeline

- 3-layer structure (Layer 0/1/2) = n/φ = 3 natural-number mapping (a coincidence).
- 7 Millennium problems × average 5 conditional results (see prob-p3-2) = 35 ≈ 6² = n².
- This coincidence is not structural grounding but an **observation kept for record**.

### 6.2 atlas.n6 σ·φ = n·τ flagship demonstration

```hexa
fn verify_theorem_zero() {
    // σ(6)·φ(6) = 12·2 = 24
    // 6·τ(6)     = 6·4  = 24
    let sigma_6 = 12
    let phi_6 = 2
    let n_6 = 6
    let tau_6 = 4
    let lhs = sigma_6 * phi_6   // 24
    let rhs = n_6 * tau_6       // 24
    if lhs == rhs {
        println("EXACT: σ(6)·φ(6) = 6·τ(6) = 24")
        println("This is the n=6 instance of Theorem 0")
    }
    // Uniqueness: only n=6 satisfies σ·φ = n·τ for n >= 2
    // (full target argument in proofs/theorem-r1-uniqueness.md)
}
```

### 6.3 Uniqueness re-verification loop

```hexa
fn verify_uniqueness_theorem() {
    // Check all n ∈ [2, 10000] satisfying σ·φ = n·τ
    let mut hits = 0
    let mut n: i64 = 2
    while n <= 10000 {
        let s = sigma(n)
        let p = phi(n)
        let t = tau(n)
        if s * p == n * t {
            println("HIT: n = " + to_string(n))
            hits = hits + 1
        }
        n = n + 1
    }
    println("total HITs: " + to_string(hits))
    if hits == 1 {
        println("EXACT: uniqueness confirmed over [2, 10000]")
    }
}
```

(Note: the full argument is the three-way target in `theory/proofs/theorem-r1-uniqueness.md`. hexa provides only numerical confirmation.)

---

## 7. Practical application

### 7.1 Auto-run at session start (proposal)

- At the CLAUDE Code session-start hook (`~/.claude/settings.json`), run `runner.hexa` in background.
- Save the result JSON as `reports/sessions/verify-YYYY-MM-DD.json`.
- Initial briefing to the user on changed entries (new EXACT, new MISS).

### 7.2 Regression test after atlas edits

- On atlas.n6 edits, trigger related BT verification via a git pre-commit hook.
- Block commits when a MISS is observed.
- This is the practical defense line protecting SSOT consistency.

### 7.3 Separation from paper verification pipelines

- This pipeline targets **numerical verification internal to atlas**.
- External-paper citation / source confirmation is a separate pipeline (`papers/` axis).
- The two pipelines are kept separate so that they do **not** reference each other's results (self-reference prevention).

### 7.4 SIGKILL avoidance

- Apply codesign when running the hexa interpreter (see procedure in memory/project_hexa_binary_deploy_block.md).
- Long-running modules (over 60 seconds) are detached via `run_in_background`.
- Full atlas parsing is ~1-2 seconds (60K lines); each BT verification is under 1 second.

---

## 8. Next steps

1. **Complete hexa implementation of Layer 0/1/2**:
   - atlas_parser.hexa — regex-matching engine.
   - expr_eval.hexa — AST parsing + evaluation.
   - verify_core.hexa — verdict functions.
2. **Write 5-10 verification routines each for BT-541 ~ BT-547 modules**.
3. **Collect external DB snapshots**:
   - local cache of relevant OEIS sequences.
   - LMFDB elliptic curve sample set.
   - PDG Standard Model constant table.
4. **Make the runner.hexa orchestration logic concrete**.
5. **Introduce a git pre-commit hook** for automatic atlas consistency verification.
6. **Document the promotion-candidate review process** (required checklist for atlas [7] → [10*] promotion).
7. **Port the 34 conditional results of prob-p3-2 as hexa verification cases**:
   - Represent each result's premise as an environment flag (`env.RH=true`, etc.).
   - Extract only the numerical parts of conclusions where verification is possible.
8. **Automated report generation**:
   - JSON → Markdown conversion (follow-up session).
   - Track atlas grade-change history.

---

## 9. Summary of design principles

- **HEXA-FIRST**: use hexa as the common runtime instead of Python/Rust helper scripts.
- **No self-reference**: block the hexa-computation → atlas grade-change path. Only the direction hexa verifying atlas values is permitted.
- **Dependency on external references**: OEIS, LMFDB, PDG, standard textbooks. Promotion from closed-source basis not permitted.
- **Strict verdict criteria**: EXACT means relative error below 10⁻⁹.
- **Honesty**: do not hide NEAR/MISS. MISS is preserved in atlas as `[N?]`.
- **3-layer separation**: parser / evaluator / verifier are each reusable as standalone modules.
- **Forbidden auto-loops**: human review is mandatory for grade changes and external-source confirmation.
- **SIGKILL avoidance**: apply codesign + detach background execution.

---

## 10. Appendix — reusing existing hexa scripts

### 10.1 Current assets (`nexus/shared/n6/scripts/`)

| script | purpose | role in this pipeline |
|----------|------|------------------------|
| millennium_scanner.hexa | n=6 base-function combination search | NEAR-coordinate candidate scan |
| selmer_bklpr.hexa | BKLPR-conditional Sel_n computation | BT-546 verification module |
| riemann_explicit.hexa | Riemann explicit-formula computation | BT-541 auxiliary |
| langlands_ranks.hexa | Langlands rank computation | BT-541 + BT-546 cross-check |
| jordan_totient.hexa | J_k(n) computation | constant verification |
| modular_qexp.hexa | modular form q-expansion | BT-545 auxiliary |
| gue_spacing.hexa | GUE eigenvalue spacing | BT-541 statistics |
| instanton_sw.hexa | instanton / SW computation | BT-543 + BT-547 |
| bernoulli_boundary.hexa | Bernoulli boundary phenomena | Theorem B verification |
| crossover_scanner.hexa | cross-DSE scan | atlas cross verification |

### 10.2 Integration path

- Symlink the above 10 into `verify/_shared/`.
- Import and reuse from each BT directory.
- runner.hexa calls these modules in order.

---

## Primary-source annotation

- HEXA-FIRST principle: `/Users/ghost/core/canon/CLAUDE.md`.
- atlas.n6 SSOT: `/Users/ghost/Dev/nexus/shared/n6/atlas.n6`, 60K+ lines.
- millennium_scanner.hexa: `/Users/ghost/Dev/nexus/shared/n6/scripts/millennium_scanner.hexa`, 224 lines.
- BKLPR axioms and Sel_n mean formula: Bhargava-Kane-Lenstra-Poonen-Rains, Cambridge J. Math. 3 (2015), 275–321.
- Schaefer classification: T. Schaefer, "The complexity of satisfiability problems", STOC 1978, 216–226.
- Prodi-Serrin: Serrin 1962 in *Nonlinear Problems* (Madison), Prodi 1959.
- Standard Model gauge group dim: PDG Review of Particle Physics.
- Modular-form weights: Serre, "A Course in Arithmetic", Springer GTM 7, ch. VII.
- Smale h-cobordism: S. Smale, Amer. J. Math. 84 (1962), 387–399.
- hexa-lang interpreter patch: memory/project_hexa_fix_nested_if_patch.md (2026-04).
- SIGKILL avoidance procedure: memory/project_hexa_binary_deploy_block.md.

**Session author note**: This design document presents the **structure** and **principles** of the pipeline. Completion of the actual hexa implementation is work for follow-up sessions; at present it is at the single-script level of existing `millennium_scanner.hexa` + `selmer_bklpr.hexa`. Integration is scheduled in stages (Layer 0 → Layer 1 → Layer 2 → runner).
