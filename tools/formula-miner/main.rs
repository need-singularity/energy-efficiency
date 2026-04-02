// EVOLVE v2 — Genetic Formula Miner for n=6 Architecture
// Depth-3 exhaustive + GA(5000,500) + expanded targets + ppm output + surprisal
// Build: ~/.cargo/bin/rustc main.rs -o formula-miner

use std::fmt;
use std::collections::HashSet;
use std::collections::HashMap;

// ── N=6 Base Constants ──────────────────────────────────────────────
const N: f64 = 6.0;
const PHI: f64 = 2.0;    // phi(6) = 2
const TAU: f64 = 4.0;    // tau(6) = 4  (number of divisors)
const SIGMA: f64 = 12.0; // sigma(6) = 12
const J2: f64 = 24.0;    // Jordan J_2(6) = 24
const SOPFR: f64 = 5.0;  // sopfr(6) = 2+3 = 5
const MU: f64 = 1.0;     // mu(6) = 1 (Mobius)

const NC: usize = 7; // number of constants
const CONST_NAMES: [&str; NC] = ["n", "phi", "tau", "sigma", "J2", "sopfr", "mu"];
const CONST_VALS: [f64; NC] = [N, PHI, TAU, SIGMA, J2, SOPFR, MU];

// ── Operations ──────────────────────────────────────────────────────
const NUM_OPS: usize = 5;

#[derive(Clone, Copy, PartialEq)]
enum Op { Add, Sub, Mul, Div, Pow }

impl Op {
    #[inline]
    fn eval(self, a: f64, b: f64) -> Option<f64> {
        let r = match self {
            Op::Add => a + b,
            Op::Sub => a - b,
            Op::Mul => a * b,
            Op::Div => { if b.abs() < 1e-15 { return None; } a / b },
            Op::Pow => {
                if a.abs() < 1e-15 && b < 0.0 { return None; }
                if a.abs() > 1e6 || b.abs() > 50.0 { return None; }
                a.powf(b)
            }
        };
        if r.is_finite() && r.abs() < 1e30 { Some(r) } else { None }
    }
    fn sym(self) -> &'static str {
        match self { Op::Add=>"+", Op::Sub=>"-", Op::Mul=>"*", Op::Div=>"/", Op::Pow=>"^" }
    }
    #[inline]
    fn from_idx(i: usize) -> Op {
        match i % 5 { 0=>Op::Add, 1=>Op::Sub, 2=>Op::Mul, 3=>Op::Div, _=>Op::Pow }
    }
}

// ── Expression Tree ─────────────────────────────────────────────────
#[derive(Clone)]
enum Expr {
    Leaf(usize),                       // index into CONST_VALS
    BinOp(Op, Box<Expr>, Box<Expr>),
}

impl Expr {
    fn eval(&self) -> Option<f64> {
        match self {
            Expr::Leaf(i) => Some(CONST_VALS[*i]),
            Expr::BinOp(op, l, r) => {
                let lv = l.eval()?;
                let rv = r.eval()?;
                op.eval(lv, rv)
            }
        }
    }

    fn depth(&self) -> usize {
        match self {
            Expr::Leaf(_) => 0,
            Expr::BinOp(_, l, r) => 1 + l.depth().max(r.depth()),
        }
    }

    fn node_count(&self) -> usize {
        match self {
            Expr::Leaf(_) => 1,
            Expr::BinOp(_, l, r) => 1 + l.node_count() + r.node_count(),
        }
    }
}

impl fmt::Display for Expr {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            Expr::Leaf(i) => write!(f, "{}", CONST_NAMES[*i]),
            Expr::BinOp(op, l, r) => {
                let need_parens_l = matches!(l.as_ref(), Expr::BinOp(..));
                let need_parens_r = matches!(r.as_ref(), Expr::BinOp(..));
                if need_parens_l { write!(f, "(")?; }
                write!(f, "{}", l)?;
                if need_parens_l { write!(f, ")")?; }
                write!(f, " {} ", op.sym())?;
                if need_parens_r { write!(f, "(")?; }
                write!(f, "{}", r)?;
                if need_parens_r { write!(f, ")")?; }
                Ok(())
            }
        }
    }
}

// ── Simple RNG (xorshift64) ────────────────────────────────────────
struct Rng(u64);

impl Rng {
    fn new(seed: u64) -> Self { Rng(seed ^ 0xdeadbeef12345678) }
    #[inline]
    fn next(&mut self) -> u64 {
        self.0 ^= self.0 << 13;
        self.0 ^= self.0 >> 7;
        self.0 ^= self.0 << 17;
        self.0
    }
    #[inline]
    fn usize(&mut self, max: usize) -> usize { (self.next() % max as u64) as usize }
    #[inline]
    fn f64(&mut self) -> f64 { (self.next() & 0xFFFFFFFF) as f64 / 4294967296.0 }
}

// ── Random Tree Generation ──────────────────────────────────────────
fn random_tree(rng: &mut Rng, max_depth: usize) -> Expr {
    if max_depth == 0 || rng.f64() < 0.35 {
        Expr::Leaf(rng.usize(NC))
    } else {
        let op = Op::from_idx(rng.usize(NUM_OPS));
        let l = random_tree(rng, max_depth - 1);
        let r = random_tree(rng, max_depth - 1);
        Expr::BinOp(op, Box::new(l), Box::new(r))
    }
}

// ── Mutation ────────────────────────────────────────────────────────
fn mutate(expr: &Expr, rng: &mut Rng) -> Expr {
    let choice = rng.f64();
    match expr {
        Expr::Leaf(_) => {
            if choice < 0.7 {
                Expr::Leaf(rng.usize(NC))
            } else {
                let op = Op::from_idx(rng.usize(NUM_OPS));
                let other = Expr::Leaf(rng.usize(NC));
                if rng.f64() < 0.5 {
                    Expr::BinOp(op, Box::new(expr.clone()), Box::new(other))
                } else {
                    Expr::BinOp(op, Box::new(other), Box::new(expr.clone()))
                }
            }
        }
        Expr::BinOp(op, l, r) => {
            if choice < 0.12 {
                random_tree(rng, 3)
            } else if choice < 0.24 {
                let new_op = Op::from_idx(rng.usize(NUM_OPS));
                Expr::BinOp(new_op, l.clone(), r.clone())
            } else if choice < 0.36 {
                if rng.f64() < 0.5 { *l.clone() } else { *r.clone() }
            } else if choice < 0.60 {
                Expr::BinOp(*op, Box::new(mutate(l, rng)), r.clone())
            } else {
                Expr::BinOp(*op, l.clone(), Box::new(mutate(r, rng)))
            }
        }
    }
}

// ── Crossover ───────────────────────────────────────────────────────
fn random_subtree<'a>(expr: &'a Expr, rng: &mut Rng) -> &'a Expr {
    match expr {
        Expr::Leaf(_) => expr,
        Expr::BinOp(_, l, r) => {
            let choice = rng.f64();
            if choice < 0.33 { expr }
            else if choice < 0.66 { random_subtree(l, rng) }
            else { random_subtree(r, rng) }
        }
    }
}

fn replace_random_subtree(expr: &Expr, replacement: &Expr, rng: &mut Rng) -> Expr {
    match expr {
        Expr::Leaf(_) => {
            if rng.f64() < 0.5 { replacement.clone() } else { expr.clone() }
        }
        Expr::BinOp(op, l, r) => {
            let choice = rng.f64();
            if choice < 0.25 {
                replacement.clone()
            } else if choice < 0.60 {
                Expr::BinOp(*op, Box::new(replace_random_subtree(l, replacement, rng)), r.clone())
            } else {
                Expr::BinOp(*op, l.clone(), Box::new(replace_random_subtree(r, replacement, rng)))
            }
        }
    }
}

fn crossover(a: &Expr, b: &Expr, rng: &mut Rng) -> Expr {
    let sub = random_subtree(b, rng).clone();
    let child = replace_random_subtree(a, &sub, rng);
    if child.depth() > 4 { a.clone() } else { child }
}

// ── Target Constants ────────────────────────────────────────────────
struct Target {
    name: &'static str,
    value: f64,
    category: &'static str,
}

fn targets() -> Vec<Target> {
    vec![
        // Fundamental physics
        Target { name: "c (speed of light)", value: 299792458.0, category: "physics" },
        Target { name: "h (Planck)", value: 6.626e-34, category: "physics" },
        Target { name: "k_B (Boltzmann)", value: 1.381e-23, category: "physics" },
        Target { name: "N_A (Avogadro)", value: 6.022e23, category: "physics" },
        Target { name: "G (gravitational)", value: 6.674e-11, category: "physics" },
        // Particle masses in MeV — original
        Target { name: "m_p (proton MeV)", value: 938.272, category: "particle" },
        Target { name: "m_e (electron MeV)", value: 0.511, category: "particle" },
        Target { name: "m_W (W boson GeV)", value: 80.377, category: "particle" },
        Target { name: "m_Z (Z boson GeV)", value: 91.188, category: "particle" },
        Target { name: "m_H (Higgs GeV)", value: 125.25, category: "particle" },
        // NEW particle masses
        Target { name: "m_muon (MeV)", value: 105.658, category: "particle" },
        Target { name: "m_tau (MeV)", value: 1776.86, category: "particle" },
        Target { name: "m_top (GeV)", value: 172.69, category: "particle" },
        Target { name: "m_bottom (GeV)", value: 4.18, category: "particle" },
        Target { name: "m_charm (GeV)", value: 1.27, category: "particle" },
        Target { name: "m_strange (MeV)", value: 93.4, category: "particle" },
        Target { name: "m_up (MeV)", value: 2.16, category: "particle" },
        Target { name: "m_down (MeV)", value: 4.67, category: "particle" },
        Target { name: "m_n (neutron MeV)", value: 939.565, category: "particle" },
        Target { name: "m_p-m_n diff (MeV)", value: 1.293, category: "particle" },
        Target { name: "Lambda_QCD (MeV)", value: 200.0, category: "particle" },
        // Mathematical constants
        Target { name: "pi", value: std::f64::consts::PI, category: "math" },
        Target { name: "e", value: std::f64::consts::E, category: "math" },
        Target { name: "golden ratio", value: 1.6180339887, category: "math" },
        Target { name: "sqrt(2)", value: std::f64::consts::SQRT_2, category: "math" },
        Target { name: "sqrt(3)", value: 1.7320508075688772, category: "math" },
        Target { name: "ln(2)", value: 2.0_f64.ln(), category: "math" },
        Target { name: "ln(4/3)", value: (4.0/3.0_f64).ln(), category: "n6-known" },
        Target { name: "1/e (Boltzmann gate)", value: 1.0/std::f64::consts::E, category: "n6-known" },
        Target { name: "zeta(2)=pi^2/6", value: std::f64::consts::PI*std::f64::consts::PI/6.0, category: "math" },
        // Semiconductor / chip
        Target { name: "28nm (TSMC N5 pitch)", value: 28.0, category: "chip" },
        Target { name: "48nm (N3 gate)", value: 48.0, category: "chip" },
        Target { name: "132 (H100 SMs)", value: 132.0, category: "chip" },
        Target { name: "144 (AD102 SMs)", value: 144.0, category: "chip" },
        Target { name: "256 (typical width)", value: 256.0, category: "chip" },
        Target { name: "1024 (codebook size)", value: 1024.0, category: "chip" },
        // AI hyperparameters
        Target { name: "0.1 (universal reg)", value: 0.1, category: "ai" },
        Target { name: "0.95 (top-p/beta2)", value: 0.95, category: "ai" },
        Target { name: "0.9 (beta1)", value: 0.9, category: "ai" },
        Target { name: "128 (d_head)", value: 128.0, category: "ai" },
        Target { name: "8 (sigma-tau)", value: 8.0, category: "ai" },
        Target { name: "20 (Chinchilla ratio)", value: 20.0, category: "ai" },
        Target { name: "64 (codons)", value: 64.0, category: "bio" },
        Target { name: "96 (Tesla S / layers)", value: 96.0, category: "energy" },
        // Energy
        Target { name: "120 (H2 LHV)", value: 120.0, category: "energy" },
        Target { name: "60 (Hz / panel cells)", value: 60.0, category: "energy" },
        Target { name: "1.2 (PUE)", value: 1.2, category: "energy" },
        // Fine structure constant
        Target { name: "alpha (~1/137)", value: 1.0/137.036, category: "physics" },
        Target { name: "137 (1/alpha)", value: 137.036, category: "physics" },
        // Weinberg angle
        Target { name: "sin^2(theta_W)", value: 0.2312, category: "physics" },
        // Cosmology
        Target { name: "Omega_Lambda", value: 0.685, category: "cosmo" },
        Target { name: "Omega_matter", value: 0.315, category: "cosmo" },
        Target { name: "H0 (km/s/Mpc)", value: 67.4, category: "cosmo" },
        // NEW: Cosmological constant (dimensionless proxy: exponent)
        Target { name: "CC exponent (-52)", value: 52.0, category: "cosmo" },
    ]
}

// ── Surprisal scoring ──────────────────────────────────────────────
// Larger, non-round numbers are more surprising to match
fn surprisal(value: f64) -> f64 {
    let v = value.abs();
    if v < 1e-30 { return 0.0; }
    // Base: log of absolute value (bigger = more surprising)
    let mag = v.log10().abs();
    // Penalty for round numbers (integers, powers of 10)
    let frac = v - v.floor();
    let roundness_penalty = if frac.abs() < 1e-9 {
        // Integer — less surprising
        0.5
    } else if (frac - 0.5).abs() < 1e-9 {
        0.7
    } else {
        1.0 // Non-round = more surprising
    };
    // Penalty for small integers
    let small_penalty = if v < 30.0 && frac.abs() < 1e-9 { 0.3 } else { 1.0 };
    mag * roundness_penalty * small_penalty
}

// ── Fitness ─────────────────────────────────────────────────────────
#[derive(Clone)]
struct Match {
    target_idx: usize,
    rel_error: f64,
}

fn evaluate(expr: &Expr, tgts: &[Target]) -> (f64, Vec<Match>) {
    let val = match expr.eval() {
        Some(v) if v.is_finite() && v != 0.0 => v,
        _ => return (0.0, vec![]),
    };

    let mut score = 0.0;
    let mut matches = Vec::new();

    for (i, t) in tgts.iter().enumerate() {
        let rel_err = ((val - t.value) / t.value).abs();
        if rel_err < 0.05 {
            let s = -rel_err.max(1e-15).log10();
            score += s;
            matches.push(Match { target_idx: i, rel_error: rel_err });
        }
    }

    let complexity_penalty = expr.node_count() as f64 * 0.05;
    let simplicity_bonus = if !matches.is_empty() {
        3.0 / (expr.node_count() as f64)
    } else {
        0.0
    };

    (score - complexity_penalty + simplicity_bonus, matches)
}

// fast evaluation for pre-computed depth-2 value
fn evaluate_val(val: f64, tgts: &[Target], node_count: usize) -> (f64, Vec<Match>) {
    if !val.is_finite() || val == 0.0 { return (0.0, vec![]); }
    let mut score = 0.0;
    let mut matches = Vec::new();
    for (i, t) in tgts.iter().enumerate() {
        let rel_err = ((val - t.value) / t.value).abs();
        if rel_err < 0.05 {
            let s = -rel_err.max(1e-15).log10();
            score += s;
            matches.push(Match { target_idx: i, rel_error: rel_err });
        }
    }
    let complexity_penalty = node_count as f64 * 0.05;
    let simplicity_bonus = if !matches.is_empty() {
        3.0 / (node_count as f64)
    } else { 0.0 };
    (score - complexity_penalty + simplicity_bonus, matches)
}

// ── Value deduplication ─────────────────────────────────────────────
fn val_key(v: f64) -> i64 {
    if v.abs() < 1e-30 { return 0; }
    let exp = v.abs().log10().floor();
    let mantissa = v / 10.0_f64.powf(exp);
    (mantissa * 1e8).round() as i64
}

// ── Pre-compute depth-2 expression table ────────────────────────────
struct D2Entry {
    val: f64,
    expr: Expr,
    node_count: usize,
}

fn build_depth2_table() -> Vec<D2Entry> {
    let mut table: Vec<D2Entry> = Vec::with_capacity(20000);
    let mut seen_vals: HashSet<i64> = HashSet::new();

    // Depth 0: leaves
    for i in 0..NC {
        let v = CONST_VALS[i];
        let k = val_key(v);
        if seen_vals.insert(k) {
            table.push(D2Entry { val: v, expr: Expr::Leaf(i), node_count: 1 });
        }
    }

    // Depth 1: op(leaf, leaf)
    for op_i in 0..NUM_OPS {
        let op = Op::from_idx(op_i);
        for i in 0..NC {
            for j in 0..NC {
                if let Some(v) = op.eval(CONST_VALS[i], CONST_VALS[j]) {
                    let k = val_key(v);
                    if seen_vals.insert(k) {
                        let e = Expr::BinOp(op, Box::new(Expr::Leaf(i)), Box::new(Expr::Leaf(j)));
                        table.push(D2Entry { val: v, expr: e, node_count: 3 });
                    }
                }
            }
        }
    }

    // Depth 2: op(op(leaf,leaf), leaf) and op(leaf, op(leaf,leaf))
    for op1_i in 0..NUM_OPS {
        let op1 = Op::from_idx(op1_i);
        for op2_i in 0..NUM_OPS {
            let op2 = Op::from_idx(op2_i);
            for i in 0..NC {
                for j in 0..NC {
                    let inner_val = match op2.eval(CONST_VALS[i], CONST_VALS[j]) {
                        Some(v) => v,
                        None => continue,
                    };
                    for k in 0..NC {
                        // op1(op2(i,j), k)
                        if let Some(v) = op1.eval(inner_val, CONST_VALS[k]) {
                            let kk = val_key(v);
                            if seen_vals.insert(kk) {
                                let e = Expr::BinOp(op1,
                                    Box::new(Expr::BinOp(op2, Box::new(Expr::Leaf(i)), Box::new(Expr::Leaf(j)))),
                                    Box::new(Expr::Leaf(k)));
                                table.push(D2Entry { val: v, expr: e, node_count: 5 });
                            }
                        }
                        // op1(k, op2(i,j))
                        if let Some(v) = op1.eval(CONST_VALS[k], inner_val) {
                            let kk = val_key(v);
                            if seen_vals.insert(kk) {
                                let e = Expr::BinOp(op1,
                                    Box::new(Expr::Leaf(k)),
                                    Box::new(Expr::BinOp(op2, Box::new(Expr::Leaf(i)), Box::new(Expr::Leaf(j)))));
                                table.push(D2Entry { val: v, expr: e, node_count: 5 });
                            }
                        }
                    }
                }
            }
        }
    }

    table
}

// ── Build depth-3 by composing depth-2 entries with one more op ─────
fn build_depth3_table(d2: &[D2Entry]) -> Vec<D2Entry> {
    let mut table: Vec<D2Entry> = Vec::with_capacity(100000);
    let mut seen_vals: HashSet<i64> = HashSet::new();

    // Collect existing keys to avoid duplicating depth-2
    for entry in d2 {
        seen_vals.insert(val_key(entry.val));
    }

    let d2_len = d2.len();
    // depth-3 type A: op(d2_expr, leaf)
    for op_i in 0..NUM_OPS {
        let op = Op::from_idx(op_i);
        for entry in d2.iter() {
            if entry.node_count < 3 { continue; } // skip trivial leaves for depth-3
            for k in 0..NC {
                if let Some(v) = op.eval(entry.val, CONST_VALS[k]) {
                    let kk = val_key(v);
                    if seen_vals.insert(kk) {
                        let e = Expr::BinOp(op,
                            Box::new(entry.expr.clone()),
                            Box::new(Expr::Leaf(k)));
                        table.push(D2Entry { val: v, expr: e, node_count: entry.node_count + 2 });
                    }
                }
                // op(leaf, d2_expr)
                if let Some(v) = op.eval(CONST_VALS[k], entry.val) {
                    let kk = val_key(v);
                    if seen_vals.insert(kk) {
                        let e = Expr::BinOp(op,
                            Box::new(Expr::Leaf(k)),
                            Box::new(entry.expr.clone()));
                        table.push(D2Entry { val: v, expr: e, node_count: entry.node_count + 2 });
                    }
                }
            }
        }
    }

    // depth-3 type B: op(d2_expr_a, d2_expr_b) — sample to avoid explosion
    // Only use depth-1 entries (node_count==3) composed with depth-1 entries
    let d1_entries: Vec<usize> = (0..d2_len).filter(|&i| d2[i].node_count == 3).collect();
    for op_i in 0..NUM_OPS {
        let op = Op::from_idx(op_i);
        for &ai in &d1_entries {
            for &bi in &d1_entries {
                if let Some(v) = op.eval(d2[ai].val, d2[bi].val) {
                    let kk = val_key(v);
                    if seen_vals.insert(kk) {
                        let e = Expr::BinOp(op,
                            Box::new(d2[ai].expr.clone()),
                            Box::new(d2[bi].expr.clone()));
                        table.push(D2Entry { val: v, expr: e, node_count: 7 });
                    }
                }
            }
        }
    }

    table
}

// ── Tournament selection ────────────────────────────────────────────
fn tournament_select(scored: &[(f64, usize)], rng: &mut Rng, size: usize) -> usize {
    let mut best_idx = 0;
    let mut best_score = f64::NEG_INFINITY;
    for _ in 0..size {
        let idx = rng.usize(scored.len());
        if scored[idx].0 > best_score {
            best_score = scored[idx].0;
            best_idx = scored[idx].1;
        }
    }
    best_idx
}

// ── Main ────────────────────────────────────────────────────────────
fn main() {
    let tgts = targets();
    let pop_size = 5000;
    let generations = 500;
    let elite_frac = 0.10;
    let elite_count = (pop_size as f64 * elite_frac) as usize;
    let tournament_size = 5;
    let mut rng = Rng::new(42);

    println!("=== EVOLVE v2: n=6 Genetic Formula Miner ===");
    println!("Population: {}, Generations: {}, Elitism: top {}%", pop_size, generations, (elite_frac*100.0) as u32);
    println!("Tournament selection (size {})", tournament_size);
    println!("Base constants: n=6, phi=2, tau=4, sigma=12, J2=24, sopfr=5, mu=1");
    println!("Targets: {} values across physics/math/chip/AI/energy/particle/cosmo", tgts.len());
    println!();

    // ── Phase 1: Exhaustive depth-2 scan (pre-computed) ─────────────
    println!("Phase 1: Building depth-2 expression table...");
    let d2_table = build_depth2_table();
    println!("  Depth <=2: {} unique values", d2_table.len());

    // ── Phase 2: Depth-3 exhaustive scan ────────────────────────────
    println!("Phase 2: Building depth-3 expression table...");
    let d3_table = build_depth3_table(&d2_table);
    println!("  Depth-3 (new): {} unique values", d3_table.len());
    println!("  Total exhaustive: {} unique expressions", d2_table.len() + d3_table.len());

    // Evaluate all exhaustive expressions
    println!("Phase 3: Evaluating exhaustive expressions against {} targets...", tgts.len());
    let mut all_discoveries: Vec<(f64, Expr, Vec<Match>)> = Vec::new();
    let mut seen: HashSet<(i64, usize)> = HashSet::new();

    for entry in d2_table.iter().chain(d3_table.iter()) {
        let (s, m) = evaluate_val(entry.val, &tgts, entry.node_count);
        if s > 1.0 && !m.is_empty() {
            let key = val_key(entry.val);
            for mi in &m {
                if seen.insert((key, mi.target_idx)) {
                    all_discoveries.push((s, entry.expr.clone(), vec![mi.clone()]));
                }
            }
        }
    }
    println!("  Exhaustive hits: {}", all_discoveries.len());

    // ── Phase 4: GA for depth-3/4 exploration ───────────────────────
    println!("\nPhase 4: Genetic Algorithm ({} pop x {} gen)...", pop_size, generations);

    let mut population: Vec<Expr> = (0..pop_size)
        .map(|_| random_tree(&mut rng, 4))
        .collect();

    // Seed known good formulas
    let seeds = vec![
        Expr::BinOp(Op::Mul, Box::new(Expr::BinOp(Op::Mul,
            Box::new(Expr::Leaf(3)), Box::new(Expr::Leaf(0)))),
            Box::new(Expr::Leaf(1))),
        Expr::BinOp(Op::Mul, Box::new(Expr::Leaf(3)),
            Box::new(Expr::BinOp(Op::Sub, Box::new(Expr::Leaf(3)), Box::new(Expr::Leaf(6))))),
        Expr::BinOp(Op::Sub, Box::new(Expr::Leaf(4)), Box::new(Expr::Leaf(2))),
        Expr::BinOp(Op::Sub, Box::new(Expr::Leaf(3)), Box::new(Expr::Leaf(2))),
        Expr::BinOp(Op::Mul, Box::new(Expr::Leaf(3)), Box::new(Expr::Leaf(5))),
        Expr::BinOp(Op::Pow, Box::new(Expr::Leaf(1)), Box::new(Expr::Leaf(2))),
        Expr::BinOp(Op::Mul, Box::new(Expr::Leaf(3)),
            Box::new(Expr::BinOp(Op::Sub, Box::new(Expr::Leaf(3)), Box::new(Expr::Leaf(1))))),
        Expr::BinOp(Op::Div, Box::new(Expr::Leaf(3)),
            Box::new(Expr::BinOp(Op::Sub, Box::new(Expr::Leaf(3)), Box::new(Expr::Leaf(1))))),
        Expr::BinOp(Op::Div, Box::new(Expr::Leaf(6)),
            Box::new(Expr::BinOp(Op::Sub, Box::new(Expr::Leaf(3)), Box::new(Expr::Leaf(1))))),
        Expr::BinOp(Op::Pow, Box::new(Expr::Leaf(1)), Box::new(Expr::Leaf(3))),
        Expr::BinOp(Op::Pow, Box::new(Expr::Leaf(0)), Box::new(Expr::Leaf(5))),
    ];
    for (i, s) in seeds.into_iter().enumerate() {
        if i < pop_size { population[i] = s; }
    }

    // Also seed with some depth-2 exhaustive hits
    let mut seed_idx = 20;
    for entry in d2_table.iter().take(200) {
        if seed_idx < pop_size {
            population[seed_idx] = entry.expr.clone();
            seed_idx += 1;
        }
    }

    let mut best_score = 0.0_f64;
    let mut best_gen = 0;

    for gen in 0..generations {
        // Evaluate population
        let mut scored: Vec<(f64, usize)> = population.iter()
            .enumerate()
            .map(|(i, e)| {
                let (s, _) = evaluate(e, &tgts);
                (s, i)
            })
            .collect();
        scored.sort_by(|a, b| b.0.partial_cmp(&a.0).unwrap());

        let gen_best = scored[0].0;
        if gen_best > best_score {
            best_score = gen_best;
            best_gen = gen;
        }

        // Collect good matches
        for &(sc, idx) in scored.iter().take(100) {
            if sc > 1.0 {
                let (_, matches) = evaluate(&population[idx], &tgts);
                if !matches.is_empty() {
                    if let Some(v) = population[idx].eval() {
                        let key = val_key(v);
                        for mi in &matches {
                            if seen.insert((key, mi.target_idx)) {
                                all_discoveries.push((sc, population[idx].clone(), vec![mi.clone()]));
                            }
                        }
                    }
                }
            }
        }

        if gen % 50 == 0 {
            let best_expr = &population[scored[0].1];
            println!("  Gen {:3}: best_score={:.2}, expr={}, val={:.6}",
                gen, gen_best, best_expr,
                best_expr.eval().unwrap_or(f64::NAN));
        }

        // ── Selection + reproduction (tournament) ───────────────────
        let mut next_pop: Vec<Expr> = Vec::with_capacity(pop_size);

        // Elitism: top 10%
        for i in 0..elite_count.min(scored.len()) {
            next_pop.push(population[scored[i].1].clone());
        }

        // Fill rest with tournament selection + crossover + mutation
        while next_pop.len() < pop_size {
            let p1_idx = tournament_select(&scored, &mut rng, tournament_size);
            let p2_idx = tournament_select(&scored, &mut rng, tournament_size);

            let mut child = if rng.f64() < 0.7 {
                crossover(&population[p1_idx], &population[p2_idx], &mut rng)
            } else {
                population[p1_idx].clone()
            };

            if rng.f64() < 0.4 {
                child = mutate(&child, &mut rng);
            }

            if child.depth() <= 4 {
                next_pop.push(child);
            } else {
                next_pop.push(random_tree(&mut rng, 4));
            }
        }

        // Inject fresh blood
        let inject_count = pop_size / 20; // 5%
        for i in (pop_size - inject_count)..pop_size {
            next_pop[i] = random_tree(&mut rng, 4);
        }

        population = next_pop;
    }

    println!("\nGA complete. Best score {:.2} at generation {}", best_score, best_gen);

    // ── Deduplicate all discoveries ─────────────────────────────────
    all_discoveries.sort_by(|a, b| b.0.partial_cmp(&a.0).unwrap());

    // Group by target, keep best per (value, target)
    let mut unique: Vec<(f64, Expr, Match)> = Vec::new();
    let mut final_seen: HashSet<(i64, usize)> = HashSet::new();

    for (sc, expr, matches) in &all_discoveries {
        if let Some(v) = expr.eval() {
            let key = val_key(v);
            for m in matches {
                if final_seen.insert((key, m.target_idx)) {
                    unique.push((*sc, expr.clone(), m.clone()));
                }
            }
        }
    }

    // Sort by target, then by error
    unique.sort_by(|a, b| {
        a.2.target_idx.cmp(&b.2.target_idx)
            .then(a.2.rel_error.partial_cmp(&b.2.rel_error).unwrap())
    });

    // ── Print Results ───────────────────────────────────────────────
    println!("\n{}", "=".repeat(120));
    println!("  TOP FORMULA DISCOVERIES (n=6 -> physical/engineering constants)");
    println!("  Depth-3 exhaustive + GA(5000x500) | {} targets | {} unique formulas",
        tgts.len(), unique.len());
    println!("{}\n", "=".repeat(120));

    // Group results by target
    let mut by_target: HashMap<usize, Vec<(f64, Expr, Match)>> = HashMap::new();
    for (sc, expr, m) in &unique {
        by_target.entry(m.target_idx).or_insert_with(Vec::new)
            .push((*sc, expr.clone(), m.clone()));
    }

    // Sort each target's results by error
    for entries in by_target.values_mut() {
        entries.sort_by(|a, b| a.2.rel_error.partial_cmp(&b.2.rel_error).unwrap());
    }

    // Print per-target, sorted by surprisal
    let mut target_order: Vec<(usize, f64, f64)> = Vec::new(); // (idx, best_error, surprisal)
    for (&tidx, entries) in &by_target {
        let best_err = entries[0].2.rel_error;
        let surp = surprisal(tgts[tidx].value);
        target_order.push((tidx, best_err, surp));
    }
    // Sort: EXACT first, then by surprisal descending
    target_order.sort_by(|a, b| {
        let a_exact = a.1 < 1e-10;
        let b_exact = b.1 < 1e-10;
        if a_exact != b_exact { return b_exact.cmp(&a_exact); }
        b.2.partial_cmp(&a.2).unwrap()
    });

    let mut exact_count = 0;
    let mut close_count = 0; // < 1%

    for (tidx, _best_err, surp) in &target_order {
        let t = &tgts[*tidx];
        let entries = &by_target[tidx];
        let best = &entries[0];

        let err_str = if best.2.rel_error < 1e-10 {
            exact_count += 1;
            "EXACT".to_string()
        } else if best.2.rel_error < 0.0001 {
            close_count += 1;
            let ppm = best.2.rel_error * 1e6;
            format!("{:.1} ppm", ppm)
        } else if best.2.rel_error < 0.001 {
            close_count += 1;
            format!("{:.4}%", best.2.rel_error * 100.0)
        } else {
            format!("{:.2}%", best.2.rel_error * 100.0)
        };

        let surp_stars = if *surp > 3.0 { "***" }
            else if *surp > 2.0 { "**" }
            else if *surp > 1.0 { "*" }
            else { "" };

        println!("  {:<30} = {:<45} -> {:>14.6}  [{:>10}] {}",
            t.name,
            format!("{}", best.1),
            best.1.eval().unwrap_or(f64::NAN),
            err_str,
            surp_stars);

        // Show up to 2 more alternatives
        for alt in entries.iter().skip(1).take(2) {
            let alt_err = if alt.2.rel_error < 1e-10 {
                "EXACT".to_string()
            } else if alt.2.rel_error < 0.0001 {
                format!("{:.1} ppm", alt.2.rel_error * 1e6)
            } else if alt.2.rel_error < 0.001 {
                format!("{:.4}%", alt.2.rel_error * 100.0)
            } else {
                format!("{:.2}%", alt.2.rel_error * 100.0)
            };
            println!("  {:<30}   {:<45} -> {:>14.6}  [{:>10}]",
                "",
                format!("{}", alt.1),
                alt.1.eval().unwrap_or(f64::NAN),
                alt_err);
        }
    }

    // ── Summary ─────────────────────────────────────────────────────
    println!("\n{}", "=".repeat(120));
    println!("  SUMMARY");
    println!("{}", "=".repeat(120));
    println!("  Total targets:          {}", tgts.len());
    println!("  Targets with matches:   {} / {}", by_target.len(), tgts.len());
    println!("  EXACT matches:          {}", exact_count);
    println!("  Close matches (<1%):    {}", close_count);
    println!("  Unique formulas:        {}", unique.len());
    println!("  Exhaustive depth <=2:   {} unique values", d2_table.len());
    println!("  Exhaustive depth-3:     {} unique values", d3_table.len());

    // ── Category breakdown ──────────────────────────────────────────
    println!("\n  By category:");
    let categories = ["physics", "particle", "math", "n6-known", "chip", "ai", "bio", "energy", "cosmo"];
    for cat in &categories {
        let total_in_cat = tgts.iter().filter(|t| t.category == *cat).count();
        let matched_in_cat = target_order.iter()
            .filter(|(tidx, _, _)| tgts[*tidx].category == *cat)
            .count();
        let exact_in_cat = target_order.iter()
            .filter(|(tidx, err, _)| tgts[*tidx].category == *cat && *err < 1e-10)
            .count();
        if total_in_cat > 0 {
            println!("    {:<12} {:>2}/{:>2} matched, {:>2} EXACT",
                cat.to_uppercase(), matched_in_cat, total_in_cat, exact_in_cat);
        }
    }

    // ── New discoveries (depth-3 only) ──────────────────────────────
    println!("\n  === NEW DEPTH-3 DISCOVERIES (not reachable at depth-2) ===");
    let mut new_count = 0;
    for (tidx, best_err, _surp) in &target_order {
        let entries = &by_target[tidx];
        let best = &entries[0];
        // Check if this formula has depth > 2
        if best.1.depth() > 2 && *best_err < 0.01 {
            let t = &tgts[*tidx];
            let err_str = if *best_err < 1e-10 { "EXACT".to_string() }
                else { format!("{:.1} ppm", best_err * 1e6) };
            println!("    {} = {}  [{}]", t.name, best.1, err_str);
            new_count += 1;
        }
    }
    if new_count == 0 {
        println!("    (all best matches were already depth <=2)");
    }

    println!("\n{}", "=".repeat(120));
}
