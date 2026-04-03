/// HEXA-LANG Semantic Analysis — n=6 files
///
/// Three analysis layers:
///   Layer 1: Name resolution + type checking (Hindley-Milner Mk.I)
///   Layer 2: Ownership analysis (single-owner, no use-after-move)
///   Layer 3: Trait resolution (Mk.II placeholder)
///
/// File count = n = 6: mod.rs, resolve.rs, typecheck.rs, ownership.rs, trait_impl.rs, error.rs

pub mod resolve;
pub mod typecheck;
pub mod ownership;
pub mod trait_impl;
pub mod error;

pub use error::SemaError;

use crate::parser::ast::Program;
use typecheck::TypeChecker;
use ownership::OwnershipChecker;
use trait_impl::TraitResolver;

/// Run all semantic analysis passes on a parsed program.
/// Returns Ok(()) if the program is semantically valid,
/// or Err(errors) with all detected issues.
pub fn analyze(program: &Program) -> Result<(), Vec<SemaError>> {
    let mut all_errors = Vec::new();

    // Layer 1: Type checking (includes name resolution)
    let mut tc = TypeChecker::new();
    if let Err(mut errs) = tc.check_program(program) {
        all_errors.append(&mut errs);
    }

    // Layer 2: Ownership analysis per function
    for decl in &program.decls {
        if let crate::parser::ast::Decl::FnDecl(f) = decl {
            let mut oc = OwnershipChecker::new();
            // Register parameters as owned
            for (pname, _) in &f.params {
                oc.define(pname, f.span);
            }
            let mut errs = oc.check_block(&f.body);
            all_errors.append(&mut errs);
        }
    }

    // Layer 3: Trait resolution (Mk.II — currently no-op)
    let mut tr = TraitResolver::new();
    if let Err(mut errs) = tr.resolve_traits(program) {
        all_errors.append(&mut errs);
    }

    if all_errors.is_empty() {
        Ok(())
    } else {
        Err(all_errors)
    }
}
