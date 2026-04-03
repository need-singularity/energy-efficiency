/// ARM64 (AArch64) Code Generation — Mk.II stub
///
/// ARM64 uses 31 general-purpose registers (x0-x30) + sp.
/// AAPCS64 ABI: first sigma-tau=8 args in x0-x7.

use crate::ir::*;
use super::regalloc::RegAlloc;

/// ARM64 physical register
#[derive(Clone, Copy, Debug, PartialEq)]
pub enum Arm64Reg {
    X0, X1, X2, X3, X4, X5, X6, X7,
    X8, X9, X10, X11, X12, X13, X14, X15,
    X16, X17, X18, X19, X20, X21, X22, X23,
    X24, X25, X26, X27, X28, X29, X30,
    Sp,
}

/// Select ARM64 instructions for a function (Mk.II stub)
pub fn select_function(func: &HexaFunction, _alloc: &RegAlloc) -> Vec<u8> {
    let mut code = Vec::new();

    // Prologue: stp x29, x30, [sp, #-16]!; mov x29, sp
    code.extend_from_slice(&0xa9bf7bfdu32.to_le_bytes()); // stp x29, x30, [sp, #-16]!
    code.extend_from_slice(&0x910003fdu32.to_le_bytes()); // mov x29, sp

    // Mk.II: emit actual instructions per block
    // For now, emit a simple return sequence based on block count
    let total_instrs = func.count_instrs();
    if total_instrs == 0 {
        // mov x0, #0
        code.extend_from_slice(&0xd2800000u32.to_le_bytes());
    }

    // Epilogue: ldp x29, x30, [sp], #16; ret
    code.extend_from_slice(&0xa8c17bfdu32.to_le_bytes()); // ldp x29, x30, [sp], #16
    code.extend_from_slice(&0xd65f03c0u32.to_le_bytes()); // ret

    code
}
