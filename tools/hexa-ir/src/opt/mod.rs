/// Optimization Pipeline — sigma=12 passes in n/phi=3 waves
///
/// Front (P1-P4): type resolution, ownership dedup, dead stores, redundant loads
/// Mid   (P5-P8): inlining, LICM, CSE, strength reduction
/// Back  (P9-P12): sinking, coalescing, final DCE, verification

pub mod front;
pub mod mid;
pub mod back;

use crate::ir::*;

/// Run the complete sigma=12 optimization pipeline
pub fn run_pipeline(func: &mut HexaFunction) -> Vec<PassResult> {
    let mut results = Vec::new();
    results.extend(front::run(func));
    results.extend(mid::run(func));
    results.extend(back::run(func));
    results
}
