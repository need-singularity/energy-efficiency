/// Trait resolution — Mk.II placeholder
///
/// In Mk.I, traits are not yet supported. This module provides the
/// structural scaffolding so that Mk.II can implement:
///   - Trait definition and method lookup
///   - impl block resolution
///   - Trait bounds on generics
///
/// For now, resolve_trait always succeeds (no-op pass).

use crate::parser::ast::Program;
use super::error::SemaError;

/// Trait resolver state (Mk.II: will hold trait definitions + impl tables)
pub struct TraitResolver {
    // Mk.II: trait_defs: HashMap<String, TraitDef>
    // Mk.II: impl_table: HashMap<(String, String), ImplBlock>
    _placeholder: (),
}

impl TraitResolver {
    pub fn new() -> Self {
        TraitResolver { _placeholder: () }
    }

    /// Resolve all trait implementations in the program.
    /// Mk.I: no-op, always returns Ok.
    pub fn resolve_traits(&mut self, _program: &Program) -> Result<(), Vec<SemaError>> {
        // Mk.II will:
        //   1. Collect all trait definitions
        //   2. Collect all impl blocks
        //   3. Verify each impl satisfies the trait's required methods
        //   4. Build a dispatch table for dynamic dispatch
        Ok(())
    }
}
