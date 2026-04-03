//! HEXA-IR Compiler Library — n=6 Native Compilation Stack
//!
//! σ(n)·φ(n) = n·τ(n) ⟺ n = 6
//! LLVM-independent compiler: J₂=24 opcodes, σ=12 passes, proof-preserving pipeline
//!
//! Module dependency (topological order):
//!   util → ir → diag → proof → alloc → lexer → parser → sema → lower → opt → codegen
#![allow(dead_code)]

// ═══ Foundation ═══
pub mod util;
pub mod ir;

// ═══ Support ═══
pub mod diag;
pub mod proof;
pub mod alloc;

// ═══ Pipeline (n=6 stages) ═══
pub mod lexer;    // Stage 1: Source → Tokens
pub mod parser;   // Stage 2: Tokens → AST
pub mod sema;     // Stage 3: AST → Typed AST
pub mod lower;    // Stage 4: AST → HEXA-IR
pub mod opt;      // Stage 5: IR → Optimized IR (σ=12 passes)
pub mod codegen;  // Stage 6: IR → Native Binary
