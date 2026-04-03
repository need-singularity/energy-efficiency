/// P6: Loop Invariant Code Motion (LICM) — hoist invariant loads out of loops
///
/// A Load is loop-invariant iff its address is NOT written by any Store in the loop body.
/// Loop blocks are identified by back-edges: successor ID < block ID.

use crate::ir::*;
use std::collections::HashSet;

pub fn run(func: &mut HexaFunction) {
    let mut hoisted = Vec::new();

    for block in &mut func.blocks {
        // Detect loop blocks by back-edge heuristic
        let has_back_edge = block.successors.iter().any(|&s| s < block.id);
        if !has_back_edge {
            continue;
        }

        // Collect all addresses written by Store in this loop block
        let mut stored_addrs: HashSet<usize> = HashSet::new();
        for instr in &block.instrs {
            if instr.op == HexaOp::Store {
                if let Some(&addr) = instr.args.first() {
                    stored_addrs.insert(addr);
                }
            }
        }

        // Only hoist Loads whose address is NOT in the stored set (truly invariant)
        let mut kept = Vec::new();
        for instr in block.instrs.drain(..) {
            if instr.op == HexaOp::Load {
                let addr = instr.args.first().copied().unwrap_or(usize::MAX);
                if !stored_addrs.contains(&addr) {
                    hoisted.push(instr); // safe to hoist
                } else {
                    kept.push(instr); // address written in loop -- must stay
                }
            } else {
                kept.push(instr);
            }
        }
        block.instrs = kept;
    }

    // Prepend hoisted instructions to entry block
    if !hoisted.is_empty() && !func.blocks.is_empty() {
        let mut new_instrs = hoisted;
        new_instrs.append(&mut func.blocks[0].instrs);
        func.blocks[0].instrs = new_instrs;
    }
}
