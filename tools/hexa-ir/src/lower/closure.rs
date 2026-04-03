/// Closure capture lowering — Mk.II stub
///
/// When a closure captures variables from its enclosing scope,
/// we must allocate a capture struct and rewrite references.

use crate::ir::*;

/// Information about a captured variable
#[derive(Clone, Debug)]
pub struct CaptureInfo {
    /// Name of the captured variable
    pub name: String,
    /// SSA register in the enclosing scope
    pub outer_reg: usize,
    /// Offset within the capture struct
    pub capture_offset: usize,
    /// Whether captured by reference (true) or by value (false)
    pub by_ref: bool,
}

/// Closure representation in IR
#[derive(Clone, Debug)]
pub struct ClosureIR {
    /// The captures this closure needs
    pub captures: Vec<CaptureInfo>,
    /// Register holding the allocated capture struct
    pub env_reg: usize,
    /// The function that implements the closure body
    pub body_fn: String,
}

/// Lower a closure expression (Mk.II stub)
///
/// Full implementation will:
/// 1. Analyze free variables in the closure body
/// 2. Allocate a capture struct (Alloc with size = captures.len())
/// 3. Store each captured variable into the struct
/// 4. Create a function that takes the env struct as first arg
/// 5. Return a (fn_ptr, env_ptr) pair
pub fn lower_closure(
    _ctx: &mut super::LowerContext,
    _block: &mut HexaBlock,
    _captures: &[CaptureInfo],
) -> ClosureIR {
    // Mk.II: full closure conversion with lambda lifting
    ClosureIR {
        captures: Vec::new(),
        env_reg: 0,
        body_fn: String::new(),
    }
}
