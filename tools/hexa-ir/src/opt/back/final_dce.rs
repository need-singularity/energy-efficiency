/// P11: Final Dead Code Elimination — global use-set analysis
///
/// Removes instructions whose dest registers are never used as operands
/// anywhere in the function, EXCEPT for side-effectful operations.
/// Uses HexaOp::has_side_effect() to preserve stores, calls, branches, proofs.

use crate::ir::*;
use std::collections::HashSet;

pub fn run(func: &mut HexaFunction) {
    // Collect all registers used as operands across all blocks
    let mut used_regs: HashSet<usize> = HashSet::new();
    for block in &func.blocks {
        for instr in &block.instrs {
            for &arg in &instr.args {
                used_regs.insert(arg);
            }
        }
    }

    // Remove instructions whose dest is never used (except side-effectful ops)
    for block in &mut func.blocks {
        block.instrs.retain(|instr| {
            if let Some(dest) = instr.dest {
                if !used_regs.contains(&dest) && !instr.op.has_side_effect() {
                    return false; // dead instruction
                }
            }
            true
        });
    }
}
