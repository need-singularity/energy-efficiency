/// Ownership analysis — Layer 2 (single-owner, no use-after-move)
///
/// Tracks the ownership state of each variable through the AST.
/// In Mk.I, this is a simplified version: no lifetime inference,
/// just move tracking and borrow checking.

use std::collections::HashMap;
use crate::lexer::Span;
use crate::parser::ast::*;
use super::error::SemaError;

/// Ownership state of a variable
#[derive(Clone, Debug, PartialEq)]
pub enum OwnershipState {
    /// Variable is live and owned
    Owned,
    /// Variable is currently borrowed (immutable)
    Borrowed,
    /// Variable has been moved — any further use is an error
    Moved { moved_at: Span },
}

/// Per-variable tracking entry
#[derive(Clone, Debug)]
struct VarState {
    name: String,
    state: OwnershipState,
    defined_at: Span,
}

/// Ownership checker: walks statements and tracks variable states
pub struct OwnershipChecker {
    /// Variable name -> current state
    states: HashMap<String, VarState>,
    errors: Vec<SemaError>,
}

impl OwnershipChecker {
    pub fn new() -> Self {
        OwnershipChecker {
            states: HashMap::new(),
            errors: Vec::new(),
        }
    }

    /// Register a new variable as Owned
    pub fn define(&mut self, name: &str, span: Span) {
        self.states.insert(name.to_string(), VarState {
            name: name.to_string(),
            state: OwnershipState::Owned,
            defined_at: span,
        });
    }

    /// Record a move of a variable (e.g., passing by value)
    pub fn check_move(&mut self, name: &str, at: Span) -> Result<(), SemaError> {
        match self.states.get(name) {
            Some(vs) => {
                match &vs.state {
                    OwnershipState::Moved { moved_at } => {
                        Err(SemaError::OwnershipError {
                            span: at,
                            message: format!(
                                "use of moved value '{}' (moved at {})",
                                name, moved_at
                            ),
                        })
                    }
                    _ => {
                        // Mark as moved
                        if let Some(vs) = self.states.get_mut(name) {
                            vs.state = OwnershipState::Moved { moved_at: at };
                        }
                        Ok(())
                    }
                }
            }
            None => {
                // Variable not tracked (possibly a global or parameter) — allow
                Ok(())
            }
        }
    }

    /// Record a borrow of a variable
    pub fn check_borrow(&mut self, name: &str, at: Span) -> Result<(), SemaError> {
        match self.states.get(name) {
            Some(vs) => {
                match &vs.state {
                    OwnershipState::Moved { moved_at } => {
                        Err(SemaError::OwnershipError {
                            span: at,
                            message: format!(
                                "cannot borrow moved value '{}' (moved at {})",
                                name, moved_at
                            ),
                        })
                    }
                    _ => {
                        // Mark as borrowed (simplified: no mutable borrow tracking in Mk.I)
                        if let Some(vs) = self.states.get_mut(name) {
                            vs.state = OwnershipState::Borrowed;
                        }
                        Ok(())
                    }
                }
            }
            None => Ok(()),
        }
    }

    /// Check a use of a variable (read): fails if moved
    pub fn check_use(&self, name: &str, at: Span) -> Result<(), SemaError> {
        if let Some(vs) = self.states.get(name) {
            if let OwnershipState::Moved { moved_at } = &vs.state {
                return Err(SemaError::OwnershipError {
                    span: at,
                    message: format!(
                        "use of moved value '{}' (moved at {})",
                        name, moved_at
                    ),
                });
            }
        }
        Ok(())
    }

    /// Walk a block of statements, tracking ownership
    pub fn check_block(&mut self, block: &Block) -> Vec<SemaError> {
        let mut errors = Vec::new();
        for stmt in &block.stmts {
            if let Err(e) = self.check_stmt(stmt) {
                errors.push(e);
            }
        }
        errors
    }

    /// Check a single statement for ownership violations
    fn check_stmt(&mut self, stmt: &Stmt) -> Result<(), SemaError> {
        match stmt {
            Stmt::Let { name, init, span, .. } => {
                if let Some(expr) = init {
                    self.check_expr_uses(expr)?;
                }
                self.define(name, *span);
                Ok(())
            }
            Stmt::Assign { target, value, .. } => {
                self.check_expr_uses(value)?;
                // Re-assignment restores ownership
                if let Expr::Ident(name, span) = target {
                    self.define(name, *span);
                }
                Ok(())
            }
            Stmt::Return { value, .. } => {
                if let Some(expr) = value {
                    self.check_expr_uses(expr)?;
                }
                Ok(())
            }
            Stmt::If { cond, then_block, else_block, .. } => {
                self.check_expr_uses(cond)?;
                let errs = self.check_block(then_block);
                if let Some(first) = errs.into_iter().next() {
                    return Err(first);
                }
                if let Some(eb) = else_block {
                    let errs = self.check_block(eb);
                    if let Some(first) = errs.into_iter().next() {
                        return Err(first);
                    }
                }
                Ok(())
            }
            Stmt::While { cond, body, .. } => {
                self.check_expr_uses(cond)?;
                let errs = self.check_block(body);
                if let Some(first) = errs.into_iter().next() {
                    return Err(first);
                }
                Ok(())
            }
            Stmt::ExprStmt { expr, .. } => {
                self.check_expr_uses(expr)
            }
        }
    }

    /// Check all variable uses in an expression
    fn check_expr_uses(&self, expr: &Expr) -> Result<(), SemaError> {
        match expr {
            Expr::Ident(name, span) => self.check_use(name, *span),
            Expr::Binary { lhs, rhs, .. } => {
                self.check_expr_uses(lhs)?;
                self.check_expr_uses(rhs)
            }
            Expr::Unary { operand, .. } => self.check_expr_uses(operand),
            Expr::Call { func, args, .. } => {
                self.check_expr_uses(func)?;
                for arg in args {
                    self.check_expr_uses(arg)?;
                }
                Ok(())
            }
            Expr::Field { obj, .. } => self.check_expr_uses(obj),
            Expr::Index { arr, idx, .. } => {
                self.check_expr_uses(arr)?;
                self.check_expr_uses(idx)
            }
            Expr::StructInit { fields, .. } => {
                for (_, val) in fields {
                    self.check_expr_uses(val)?;
                }
                Ok(())
            }
            Expr::Match { scrutinee, arms, .. } => {
                self.check_expr_uses(scrutinee)?;
                for arm in arms {
                    self.check_expr_uses(&arm.body)?;
                }
                Ok(())
            }
            // Literals and blocks don't reference variables directly
            _ => Ok(()),
        }
    }

    /// Consume the checker and return all collected errors
    pub fn into_errors(self) -> Vec<SemaError> {
        self.errors
    }
}
