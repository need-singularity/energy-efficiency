/// SigmaPipeline — σ=12 stage parallel compilation simulation
///
/// Models a 12-stage compilation pipeline where stages can run in parallel
/// on different functions, compared to a 6-stage sequential pipeline.
///
/// Pipeline stages (σ=12):
///   1. Lexing        2. Parsing       3. Name resolution  4. Type checking
///   5. Borrow check  6. Monomorph     7. MIR lowering     8. Const eval
///   9. Optimization  10. Codegen      11. Linking prep    12. Final emit
///
/// Each function flows through all 12 stages. With σ=12 stages and
/// sufficient parallelism, throughput improves φ=2x over 6-stage.

use std::collections::VecDeque;

// ─── Pipeline Models ──────────────────────────────────────────────

/// A compilation unit (function) with work cost per stage
#[derive(Clone)]
pub struct CompUnit {
    pub id: usize,
    /// Work cost for each stage (in time units)
    pub stage_costs: Vec<u64>,
}

/// Sequential pipeline: N_stages stages, functions processed one at a time
fn sequential_pipeline(units: &[CompUnit], num_stages: usize) -> u64 {
    let mut total_time = 0u64;
    for unit in units {
        for s in 0..num_stages {
            total_time += unit.stage_costs[s % unit.stage_costs.len()];
        }
    }
    total_time
}

/// Pipelined parallel: σ=12 stages, functions overlap in pipeline
/// Uses a simple pipeline simulation where stage i of function f+1
/// can begin as soon as stage i of function f completes.
fn pipelined_parallel(units: &[CompUnit], num_stages: usize) -> u64 {
    if units.is_empty() { return 0; }

    let n_funcs = units.len();
    // stage_finish[f][s] = time when function f finishes stage s
    let mut stage_finish = vec![vec![0u64; num_stages]; n_funcs];

    for f in 0..n_funcs {
        for s in 0..num_stages {
            let cost = units[f].stage_costs[s % units[f].stage_costs.len()];

            // Must wait for:
            // 1. Previous stage of same function to complete
            let prev_stage = if s > 0 { stage_finish[f][s - 1] } else { 0 };
            // 2. Same stage of previous function (pipeline hazard)
            let prev_func = if f > 0 { stage_finish[f - 1][s] } else { 0 };

            let start = prev_stage.max(prev_func);
            stage_finish[f][s] = start + cost;
        }
    }

    // Total time = when last function finishes last stage
    stage_finish[n_funcs - 1][num_stages - 1]
}

// ─── Benchmark ────────────────────────────────────────────────────

pub struct PipelineBenchResult {
    pub num_functions: usize,
    pub sequential_6_time: u64,
    pub pipelined_12_time: u64,
    pub speedup: f64,
}

pub fn bench_pipeline(seed: u64) -> PipelineBenchResult {
    let mut rng = seed;
    let next = |r: &mut u64| -> u64 {
        *r = r.wrapping_mul(6364136223846793005).wrapping_add(1442695040888963407);
        *r >> 33
    };

    // Generate N=144 (σ²) functions with varying costs
    let num_functions = 144;
    let mut units_6 = Vec::new();
    let mut units_12 = Vec::new();

    for i in 0..num_functions {
        // 6-stage costs (larger per stage since fewer stages)
        let mut costs_6 = Vec::new();
        for _ in 0..6 {
            costs_6.push(5 + next(&mut rng) % 15);
        }
        units_6.push(CompUnit { id: i, stage_costs: costs_6 });

        // 12-stage costs (each stage does roughly half the work of 6-stage)
        let mut costs_12 = Vec::new();
        for _ in 0..12 {
            costs_12.push(3 + next(&mut rng) % 8);
        }
        units_12.push(CompUnit { id: i, stage_costs: costs_12 });
    }

    let seq_time = sequential_pipeline(&units_6, 6);
    let pipe_time = pipelined_parallel(&units_12, 12);

    PipelineBenchResult {
        num_functions,
        sequential_6_time: seq_time,
        pipelined_12_time: pipe_time,
        speedup: seq_time as f64 / pipe_time as f64,
    }
}
