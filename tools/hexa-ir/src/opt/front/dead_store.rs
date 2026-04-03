/// P3: Dead Store Elimination — remove stores overwritten before read
///
/// If a Store to address A is followed by another Store to A with no
/// intervening Load from A, the first Store is dead and can be removed.

use crate::ir::*;

pub fn run(func: &mut HexaFunction) {
    for block in &mut func.blocks {
        let len = block.instrs.len();
        let mut dead_indices: Vec<bool> = vec![false; len];

        for i in 0..len {
            if block.instrs[i].op == HexaOp::Store {
                let store_addr = block.instrs[i].args.first().copied();
                // Look ahead for another store to same address with no intervening load
                for j in (i + 1)..len {
                    if block.instrs[j].op == HexaOp::Load {
                        if block.instrs[j].args.first().copied() == store_addr {
                            break; // address is read, can't eliminate
                        }
                    }
                    if block.instrs[j].op == HexaOp::Store {
                        if block.instrs[j].args.first().copied() == store_addr {
                            dead_indices[i] = true; // overwritten without read
                            break;
                        }
                    }
                }
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
