/// Expression lowering — AST Expr -> SSA register
///
/// Each expression emits instructions into the current block
/// and returns the SSA register holding the result.

use crate::ir::*;
use crate::parser::ast::{Expr, BinOp, UnOp};
use super::LowerContext;

/// Lower an expression, returning the SSA register holding the result
pub fn lower_expr(ctx: &mut LowerContext, block: &mut HexaBlock, expr: &Expr) -> usize {
    match expr {
        Expr::IntLit(v, _) => {
            // Emit: %r = Alloc : I64  (conceptual "materialize constant")
            // In a real SSA, constants are implicit. We use Alloc+Store for addressable values,
            // but for pure integer literals we just emit a Copy from a virtual const register.
            // For Mk.I: allocate a register, the value is tracked by the register number.
            let dest = ctx.fresh_reg();
            block.instrs.push(HexaInstr {
                op: HexaOp::Alloc,
                dest: Some(dest),
                args: vec![*v as usize], // encode the constant value in args[0]
                ty: HexaType::I64,
            });
            dest
        }

        Expr::FloatLit(_v, _) => {
            let dest = ctx.fresh_reg();
            block.instrs.push(HexaInstr {
                op: HexaOp::Alloc,
                dest: Some(dest),
                args: vec![],
                ty: HexaType::F64,
            });
            dest
        }

        Expr::BoolLit(v, _) => {
            let dest = ctx.fresh_reg();
            block.instrs.push(HexaInstr {
                op: HexaOp::Alloc,
                dest: Some(dest),
                args: vec![if *v { 1 } else { 0 }],
                ty: HexaType::Bool,
            });
            dest
        }

        Expr::StrLit(_, _) => {
            let dest = ctx.fresh_reg();
            block.instrs.push(HexaInstr {
                op: HexaOp::Alloc,
                dest: Some(dest),
                args: vec![],
                ty: HexaType::Str,
            });
            dest
        }

        Expr::Ident(name, _) => {
            // Look up the variable's SSA register and emit a Load
            let src = ctx.lookup_var(name).unwrap_or(0);
            let dest = ctx.fresh_reg();
            block.instrs.push(HexaInstr {
                op: HexaOp::Load,
                dest: Some(dest),
                args: vec![src],
                ty: HexaType::Any, // type resolved by pass_type_inference
            });
            dest
        }

        Expr::Binary { op, lhs, rhs, .. } => {
            let l = lower_expr(ctx, block, lhs);
            let r = lower_expr(ctx, block, rhs);
            let dest = ctx.fresh_reg();
            let (hexa_op, ty) = lower_binop(op);
            block.instrs.push(HexaInstr {
                op: hexa_op,
                dest: Some(dest),
                args: vec![l, r],
                ty,
            });
            dest
        }

        Expr::Unary { op, operand, .. } => {
            let src = lower_expr(ctx, block, operand);
            let dest = ctx.fresh_reg();
            let hexa_op = match op {
                UnOp::Neg => HexaOp::Neg,
                UnOp::Not => HexaOp::Neg, // Mk.I: logical not as arithmetic neg
            };
            block.instrs.push(HexaInstr {
                op: hexa_op,
                dest: Some(dest),
                args: vec![src],
                ty: HexaType::Any,
            });
            dest
        }

        Expr::Call { func, args, .. } => {
            // Lower the callee expression
            let func_reg = lower_expr(ctx, block, func);
            // Lower each argument
            let mut arg_regs = vec![func_reg];
            for arg in args {
                let r = lower_expr(ctx, block, arg);
                arg_regs.push(r);
            }
            let dest = ctx.fresh_reg();
            block.instrs.push(HexaInstr {
                op: HexaOp::Call,
                dest: Some(dest),
                args: arg_regs,
                ty: HexaType::Any, // return type resolved later
            });
            dest
        }

        Expr::Field { obj, .. } => {
            // Mk.I: lower the object, field access becomes a Load
            let obj_reg = lower_expr(ctx, block, obj);
            let dest = ctx.fresh_reg();
            block.instrs.push(HexaInstr {
                op: HexaOp::Load,
                dest: Some(dest),
                args: vec![obj_reg],
                ty: HexaType::Any,
            });
            dest
        }

        Expr::Index { arr, idx, .. } => {
            let arr_reg = lower_expr(ctx, block, arr);
            let idx_reg = lower_expr(ctx, block, idx);
            // Compute address: base + index * element_size
            let addr = ctx.fresh_reg();
            block.instrs.push(HexaInstr {
                op: HexaOp::Add,
                dest: Some(addr),
                args: vec![arr_reg, idx_reg],
                ty: HexaType::I64,
            });
            let dest = ctx.fresh_reg();
            block.instrs.push(HexaInstr {
                op: HexaOp::Load,
                dest: Some(dest),
                args: vec![addr],
                ty: HexaType::Any,
            });
            dest
        }

        Expr::StructInit { fields, .. } => {
            // Allocate space for the struct, store each field
            let base = ctx.fresh_reg();
            block.instrs.push(HexaInstr {
                op: HexaOp::Alloc,
                dest: Some(base),
                args: vec![fields.len()],
                ty: HexaType::Any,
            });
            for (i, (_name, val_expr)) in fields.iter().enumerate() {
                let val_reg = lower_expr(ctx, block, val_expr);
                let field_addr = ctx.fresh_reg();
                block.instrs.push(HexaInstr {
                    op: HexaOp::Add,
                    dest: Some(field_addr),
                    args: vec![base, i], // offset by field index
                    ty: HexaType::I64,
                });
                block.instrs.push(HexaInstr {
                    op: HexaOp::Store,
                    dest: None,
                    args: vec![field_addr, val_reg],
                    ty: HexaType::Void,
                });
            }
            base
        }

        Expr::Block(blk) => {
            // Lower statements in the block; result is last expression if any
            let mut last_reg = ctx.fresh_reg();
            // Emit a void placeholder
            block.instrs.push(HexaInstr {
                op: HexaOp::Alloc,
                dest: Some(last_reg),
                args: vec![],
                ty: HexaType::Void,
            });
            for stmt in &blk.stmts {
                let r = super::stmt_lower::lower_stmt(ctx, block, stmt);
                last_reg = r;
            }
            last_reg
        }
    }
}

/// Map AST binary operator to HexaOp + result type
fn lower_binop(op: &BinOp) -> (HexaOp, HexaType) {
    match op {
        BinOp::Add => (HexaOp::Add, HexaType::I64),
        BinOp::Sub => (HexaOp::Sub, HexaType::I64),
        BinOp::Mul => (HexaOp::Mul, HexaType::I64),
        BinOp::Div => (HexaOp::Div, HexaType::I64),
        BinOp::Mod => (HexaOp::Mod, HexaType::I64),
        BinOp::Pow => (HexaOp::Mul, HexaType::I64), // Mk.I: pow approximated as mul
        // Comparison ops → produce Bool, use Sub as underlying op
        BinOp::Eq | BinOp::Neq | BinOp::Lt | BinOp::Gt |
        BinOp::Le | BinOp::Ge => (HexaOp::Sub, HexaType::Bool),
        // Logic/bitwise → integer arithmetic
        BinOp::And | BinOp::BitAnd => (HexaOp::Mul, HexaType::Bool),
        BinOp::Or | BinOp::BitOr => (HexaOp::Add, HexaType::Bool),
        BinOp::BitXor => (HexaOp::Sub, HexaType::I64),
        BinOp::Range => (HexaOp::Sub, HexaType::I64), // Mk.I: range as difference
    }
}
