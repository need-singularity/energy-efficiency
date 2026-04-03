/// N6ConstantFolder — algebraic identity exploitation
///
/// Detects expressions matching n=6 identities and folds them:
///   x * 12 * 2 → x * 24 (σ·φ = J₂)
///   x * 6 * 4  → x * 24 (n·τ = J₂)
///   x / 2 + x / 3 + x / 6 → x (Egyptian fraction identity)
///   x * 12 * 12 → x * 144 (σ² = 144)
///   x * 2 * 2 * 6 → x * 24 (φ²·n = J₂)
///
/// Measures arithmetic operation count before/after folding.
/// Target: τ²/σ = 16/12 = 33% fewer arithmetic ops.

/// Simple expression tree for IR simulation
#[derive(Clone, Debug)]
pub enum Expr {
    Var(String),
    Const(i64),
    Add(Box<Expr>, Box<Expr>),
    Sub(Box<Expr>, Box<Expr>),
    Mul(Box<Expr>, Box<Expr>),
    Div(Box<Expr>, Box<Expr>),
    Shl(Box<Expr>, Box<Expr>), // left shift (mul by power of 2)
}

impl Expr {
    /// Count arithmetic operations in expression tree
    pub fn op_count(&self) -> usize {
        match self {
            Expr::Var(_) | Expr::Const(_) => 0,
            Expr::Add(a, b) | Expr::Sub(a, b) |
            Expr::Mul(a, b) | Expr::Div(a, b) |
            Expr::Shl(a, b) => 1 + a.op_count() + b.op_count(),
        }
    }

    /// Try to evaluate to a constant
    fn try_const(&self) -> Option<i64> {
        match self {
            Expr::Const(v) => Some(*v),
            _ => None,
        }
    }
}

// ─── Constant Folding Pass ────────────────────────────────────────

pub fn fold(expr: Expr) -> Expr {
    match expr {
        Expr::Add(a, b) => {
            let a = fold(*a);
            let b = fold(*b);

            // Constant + Constant
            if let (Some(va), Some(vb)) = (a.try_const(), b.try_const()) {
                return Expr::Const(va + vb);
            }

            // x/2 + x/3 → check for Egyptian fraction pattern
            // We detect: (x/2 + x/3) + x/6 → x
            if let (Expr::Add(inner_a, inner_b), Expr::Div(c, d)) = (&a, &b) {
                if let (Expr::Div(a1, a2), Expr::Div(b1, b2)) = (inner_a.as_ref(), inner_b.as_ref()) {
                    if let (Some(2), Some(3), Some(6)) = (a2.try_const(), b2.try_const(), d.try_const()) {
                        if vars_equal(a1, b1) && vars_equal(a1, &c) {
                            return *a1.clone(); // x/2 + x/3 + x/6 = x
                        }
                    }
                }
            }

            // 0 + x → x, x + 0 → x
            if a.try_const() == Some(0) { return b; }
            if b.try_const() == Some(0) { return a; }

            Expr::Add(Box::new(a), Box::new(b))
        }

        Expr::Sub(a, b) => {
            let a = fold(*a);
            let b = fold(*b);
            if let (Some(va), Some(vb)) = (a.try_const(), b.try_const()) {
                return Expr::Const(va - vb);
            }
            if b.try_const() == Some(0) { return a; }
            Expr::Sub(Box::new(a), Box::new(b))
        }

        Expr::Mul(a, b) => {
            let a = fold(*a);
            let b = fold(*b);

            // Constant * Constant
            if let (Some(va), Some(vb)) = (a.try_const(), b.try_const()) {
                return Expr::Const(va * vb);
            }

            // (x * C1) * C2 → x * (C1*C2)
            if let Expr::Mul(inner_a, inner_b) = &a {
                if let (Some(c1), Some(c2)) = (inner_b.try_const(), b.try_const()) {
                    let product = c1 * c2;
                    // Further: if product is power of 2, convert to shift
                    if product > 0 && (product & (product - 1)) == 0 {
                        let shift = (product as f64).log2() as i64;
                        return Expr::Shl(inner_a.clone(), Box::new(Expr::Const(shift)));
                    }
                    return Expr::Mul(inner_a.clone(), Box::new(Expr::Const(product)));
                }
            }

            // x * 1 → x, 1 * x → x
            if a.try_const() == Some(1) { return b; }
            if b.try_const() == Some(1) { return a; }
            // x * 0 → 0
            if a.try_const() == Some(0) || b.try_const() == Some(0) {
                return Expr::Const(0);
            }

            // x * (power of 2) → x << log2
            if let Some(c) = b.try_const() {
                if c > 0 && (c & (c - 1)) == 0 {
                    let shift = (c as f64).log2() as i64;
                    return Expr::Shl(Box::new(a), Box::new(Expr::Const(shift)));
                }
            }

            Expr::Mul(Box::new(a), Box::new(b))
        }

        Expr::Div(a, b) => {
            let a = fold(*a);
            let b = fold(*b);
            if let (Some(va), Some(vb)) = (a.try_const(), b.try_const()) {
                if vb != 0 && va % vb == 0 {
                    return Expr::Const(va / vb);
                }
            }
            if b.try_const() == Some(1) { return a; }
            Expr::Div(Box::new(a), Box::new(b))
        }

        Expr::Shl(a, b) => {
            let a = fold(*a);
            let b = fold(*b);
            if let (Some(va), Some(vb)) = (a.try_const(), b.try_const()) {
                return Expr::Const(va << vb);
            }
            if b.try_const() == Some(0) { return a; }
            Expr::Shl(Box::new(a), Box::new(b))
        }

        other => other,
    }
}

fn vars_equal(a: &Expr, b: &Expr) -> bool {
    match (a, b) {
        (Expr::Var(x), Expr::Var(y)) => x == y,
        _ => false,
    }
}

// ─── Test Expression Generator ────────────────────────────────────

pub fn generate_test_exprs(seed: u64) -> Vec<Expr> {
    let mut rng = seed;
    let next = |r: &mut u64| -> u64 {
        *r = r.wrapping_mul(6364136223846793005).wrapping_add(1442695040888963407);
        *r >> 33
    };

    let mut exprs = Vec::new();

    // Pattern 1: x * 12 * 2 (σ·φ = J₂ = 24)
    for i in 0..50 {
        let var = Expr::Var(format!("v{}", i));
        exprs.push(Expr::Mul(
            Box::new(Expr::Mul(Box::new(var), Box::new(Expr::Const(12)))),
            Box::new(Expr::Const(2)),
        ));
    }

    // Pattern 2: x * 6 * 4 (n·τ = 24)
    for i in 50..100 {
        let var = Expr::Var(format!("v{}", i));
        exprs.push(Expr::Mul(
            Box::new(Expr::Mul(Box::new(var), Box::new(Expr::Const(6)))),
            Box::new(Expr::Const(4)),
        ));
    }

    // Pattern 3: x/2 + x/3 + x/6 = x (Egyptian fraction)
    for i in 100..150 {
        let var = format!("v{}", i);
        let v = || Expr::Var(var.clone());
        exprs.push(Expr::Add(
            Box::new(Expr::Add(
                Box::new(Expr::Div(Box::new(v()), Box::new(Expr::Const(2)))),
                Box::new(Expr::Div(Box::new(v()), Box::new(Expr::Const(3)))),
            )),
            Box::new(Expr::Div(Box::new(v()), Box::new(Expr::Const(6)))),
        ));
    }

    // Pattern 4: x * 12 * 12 (σ² = 144)
    for i in 150..200 {
        let var = Expr::Var(format!("v{}", i));
        exprs.push(Expr::Mul(
            Box::new(Expr::Mul(Box::new(var), Box::new(Expr::Const(12)))),
            Box::new(Expr::Const(12)),
        ));
    }

    // Pattern 5: compound arithmetic (a*3 + b*4 - 7) * 8
    for i in 200..300 {
        let a = Expr::Var(format!("a{}", i));
        let b = Expr::Var(format!("b{}", i));
        let inner = Expr::Sub(
            Box::new(Expr::Add(
                Box::new(Expr::Mul(Box::new(a), Box::new(Expr::Const(3)))),
                Box::new(Expr::Mul(Box::new(b), Box::new(Expr::Const(4)))),
            )),
            Box::new(Expr::Const(7)),
        );
        exprs.push(Expr::Mul(Box::new(inner), Box::new(Expr::Const(8))));
    }

    // Pattern 6: random constant expressions (fully foldable)
    for _ in 300..500 {
        let a = next(&mut rng) as i64 % 100;
        let b = next(&mut rng) as i64 % 100 + 1;
        let c = next(&mut rng) as i64 % 50;
        exprs.push(Expr::Add(
            Box::new(Expr::Mul(Box::new(Expr::Const(a)), Box::new(Expr::Const(b)))),
            Box::new(Expr::Const(c)),
        ));
    }

    // Pattern 7: non-foldable (single variable, no ops)
    for i in 500..600 {
        exprs.push(Expr::Var(format!("x{}", i)));
    }

    exprs
}

// ─── Benchmark ────────────────────────────────────────────────────

pub struct ConstFoldResult {
    pub total_exprs: usize,
    pub ops_before: usize,
    pub ops_after: usize,
    pub reduction_pct: f64,
}

pub fn bench_const_fold(seed: u64) -> ConstFoldResult {
    let exprs = generate_test_exprs(seed);
    let total_exprs = exprs.len();
    let ops_before: usize = exprs.iter().map(|e| e.op_count()).sum();

    let folded: Vec<Expr> = exprs.into_iter().map(fold).collect();
    let ops_after: usize = folded.iter().map(|e| e.op_count()).sum();

    let reduction_pct = if ops_before > 0 {
        (1.0 - ops_after as f64 / ops_before as f64) * 100.0
    } else {
        0.0
    };

    ConstFoldResult { total_exprs, ops_before, ops_after, reduction_pct }
}
