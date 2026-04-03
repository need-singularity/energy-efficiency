/// P7: Common Subexpression Elimination — merge duplicate computations
///
/// Two instructions with the same opcode + same args produce the same result.
/// The second can be replaced with a Copy from the first's dest register.
/// Also merges consecutive identical proof instructions (proof fusion).

use crate::ir::*;
use std::collections::HashMap;

pub fn run(func: &mut HexaFunction) {
    for block in &mut func.blocks {
        // Phase 1: CSE for pure arithmetic/logic ops
        // Key: (op_discriminant, args) -> first dest register
        let mut expr_cache: HashMap<(u8, Vec<usize>), usize> = HashMap::new();

        for instr in &mut block.instrs {
            // Only CSE pure ops (no side effects)
            if instr.op.has_side_effect() {
                // Side-effectful ops invalidate the cache for their written addresses
                if instr.op == HexaOp::Store {
                    // Conservatively clear cache (a Store could alias any expression)
                    expr_cache.clear();
                }
                continue;
            }

            if let Some(dest) = instr.dest {
                let key = (op_discriminant(&instr.op), instr.args.clone());
                if let Some(&prev_dest) = expr_cache.get(&key) {
                    // Replace with Copy from the previous computation
                    instr.op = HexaOp::Copy;
                    instr.args = vec![prev_dest];
                } else {
                    expr_cache.insert(key, dest);
                }
            }
        }

        // Phase 2: Proof fusion — merge consecutive identical proof instructions
        let len = block.instrs.len();
        let mut dead_indices: Vec<bool> = vec![false; len];

        for i in 1..len {
            let prev = &block.instrs[i - 1];
            let curr = &block.instrs[i];
            let prev_is_proof = matches!(prev.op,
                HexaOp::ProofAssert | HexaOp::ProofInvariant | HexaOp::ProofWitness);
            let curr_is_proof = matches!(curr.op,
                HexaOp::ProofAssert | HexaOp::ProofInvariant | HexaOp::ProofWitness);

            if prev_is_proof && curr_is_proof
                && prev.op == curr.op
                && prev.args == curr.args
            {
                dead_indices[i - 1] = true; // keep the later one
            }
        }

        let mut idx = 0;
        block.instrs.retain(|_| {
            let keep = !dead_indices[idx];
            idx += 1;
            keep
        });
    }
}

/// Map HexaOp to a u8 discriminant for hashing
fn op_discriminant(op: &HexaOp) -> u8 {
    match op {
        HexaOp::Add => 0, HexaOp::Sub => 1, HexaOp::Mul => 2,
        HexaOp::Div => 3, HexaOp::Mod => 4, HexaOp::Neg => 5,
        HexaOp::Load => 6, HexaOp::Store => 7, HexaOp::Alloc => 8,
        HexaOp::Free => 9, HexaOp::Copy => 10, HexaOp::Move => 11,
        HexaOp::Jump => 12, HexaOp::Branch => 13, HexaOp::Call => 14,
        HexaOp::Return => 15, HexaOp::Phi => 16, HexaOp::Switch => 17,
        HexaOp::ProofAssert => 18, HexaOp::ProofInvariant => 19,
        HexaOp::ProofWitness => 20, HexaOp::OwnershipTransfer => 21,
        HexaOp::BorrowCheck => 22, HexaOp::LifetimeEnd => 23,
    }
}
