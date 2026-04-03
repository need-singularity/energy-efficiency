/// Expression parser — Pratt parsing with sigma-tau=8 precedence levels
///
/// Precedence table (lowest to highest):
///   1: ||          (logic or)
///   2: &&          (logic and)
///   3: == != < > <= >=  (comparison)
///   4: | ^         (bitwise or/xor)
///   5: &           (bitwise and)
///   6: + -         (additive)
///   7: * / %       (multiplicative)
///   8: unary - !   (prefix)

use crate::lexer::{TokenKind, Span};
use super::ast::*;
use super::error::{Parser, ParseError};

/// Pratt parser entry point
pub fn parse_expr(p: &mut Parser) -> Result<Expr, ParseError> {
    parse_expr_bp(p, 0)
}

/// Pratt parser with minimum binding power
fn parse_expr_bp(p: &mut Parser, min_bp: u8) -> Result<Expr, ParseError> {
    let mut lhs = parse_prefix(p)?;

    loop {
        // Check for postfix operations: call, field, index
        lhs = match p.peek() {
            TokenKind::LParen => parse_call(p, lhs)?,
            TokenKind::Dot => parse_field_access(p, lhs)?,
            TokenKind::LBracket => parse_index(p, lhs)?,
            _ => lhs,
        };

        // Infix binary operators
        let (op, l_bp, r_bp) = match infix_binding_power(p.peek()) {
            Some(triple) => triple,
            None => break,
        };

        if l_bp < min_bp {
            break;
        }

        p.advance(); // consume operator token
        let rhs = parse_expr_bp(p, r_bp)?;
        let span = lhs.span().merge(rhs.span());
        lhs = Expr::Binary {
            op,
            lhs: Box::new(lhs),
            rhs: Box::new(rhs),
            span,
        };
    }

    Ok(lhs)
}

/// Parse prefix expressions (atoms + unary operators)
fn parse_prefix(p: &mut Parser) -> Result<Expr, ParseError> {
    let span = p.peek_span();

    match p.peek().clone() {
        TokenKind::IntLit(v) => {
            let v = v;
            p.advance();
            Ok(Expr::IntLit(v, span))
        }
        TokenKind::FloatLit(v) => {
            let v = v;
            p.advance();
            Ok(Expr::FloatLit(v, span))
        }
        TokenKind::True => {
            p.advance();
            Ok(Expr::BoolLit(true, span))
        }
        TokenKind::False => {
            p.advance();
            Ok(Expr::BoolLit(false, span))
        }
        TokenKind::StrLit(ref s) => {
            let s = s.clone();
            p.advance();
            Ok(Expr::StrLit(s, span))
        }
        TokenKind::Ident(ref name) => {
            let name = name.clone();
            p.advance();
            // Check for struct initialization: `Name { field: val }`
            if p.at(&TokenKind::LBrace) {
                parse_struct_init(p, name, span)
            } else {
                Ok(Expr::Ident(name, span))
            }
        }
        TokenKind::Minus => {
            p.advance();
            let operand = parse_expr_bp(p, prefix_bp())?;
            let full_span = span.merge(operand.span());
            Ok(Expr::Unary {
                op: UnOp::Neg,
                operand: Box::new(operand),
                span: full_span,
            })
        }
        TokenKind::Not => {
            p.advance();
            let operand = parse_expr_bp(p, prefix_bp())?;
            let full_span = span.merge(operand.span());
            Ok(Expr::Unary {
                op: UnOp::Not,
                operand: Box::new(operand),
                span: full_span,
            })
        }
        TokenKind::LParen => {
            p.advance(); // (
            let expr = parse_expr(p)?;
            p.expect(&TokenKind::RParen)?;
            Ok(expr)
        }
        other => Err(ParseError::new(
            span,
            format!("expected expression, found {:?}", other),
        )),
    }
}

/// Struct initialization: `Name { field1: expr1, field2: expr2 }`
fn parse_struct_init(p: &mut Parser, name: String, start_span: Span) -> Result<Expr, ParseError> {
    p.expect(&TokenKind::LBrace)?;
    let mut fields = Vec::new();

    while !p.at(&TokenKind::RBrace) && !p.is_eof() {
        let (field_name, _) = p.expect_ident()?;
        p.expect(&TokenKind::Colon)?;
        let value = parse_expr(p)?;
        fields.push((field_name, value));

        if !p.eat(&TokenKind::Comma) {
            break;
        }
    }

    let end_span = p.peek_span();
    p.expect(&TokenKind::RBrace)?;
    Ok(Expr::StructInit {
        name,
        fields,
        span: start_span.merge(end_span),
    })
}

/// Function call: `expr(arg1, arg2, ...)`
fn parse_call(p: &mut Parser, func: Expr) -> Result<Expr, ParseError> {
    p.expect(&TokenKind::LParen)?;
    let mut args = Vec::new();

    while !p.at(&TokenKind::RParen) && !p.is_eof() {
        args.push(parse_expr(p)?);
        if !p.eat(&TokenKind::Comma) {
            break;
        }
    }

    let end_span = p.peek_span();
    p.expect(&TokenKind::RParen)?;
    Ok(Expr::Call {
        span: func.span().merge(end_span),
        func: Box::new(func),
        args,
    })
}

/// Field access: `expr.field`
fn parse_field_access(p: &mut Parser, obj: Expr) -> Result<Expr, ParseError> {
    p.expect(&TokenKind::Dot)?;
    let (name, name_span) = p.expect_ident()?;
    Ok(Expr::Field {
        span: obj.span().merge(name_span),
        obj: Box::new(obj),
        name,
    })
}

/// Index access: `expr[index]`
fn parse_index(p: &mut Parser, arr: Expr) -> Result<Expr, ParseError> {
    p.expect(&TokenKind::LBracket)?;
    let idx = parse_expr(p)?;
    let end_span = p.peek_span();
    p.expect(&TokenKind::RBracket)?;
    Ok(Expr::Index {
        span: arr.span().merge(end_span),
        arr: Box::new(arr),
        idx: Box::new(idx),
    })
}

/// Binding power for prefix (unary) operators — level 8 (highest)
fn prefix_bp() -> u8 {
    15 // higher than any infix
}

/// Infix binding power: returns (BinOp, left_bp, right_bp)
/// sigma-tau=8 precedence levels, mapped to binding power pairs
fn infix_binding_power(kind: &TokenKind) -> Option<(BinOp, u8, u8)> {
    match kind {
        // Level 1: ||
        TokenKind::Or      => Some((BinOp::Or, 1, 2)),
        // Level 2: &&
        TokenKind::And     => Some((BinOp::And, 3, 4)),
        // Level 3: == != < > <= >=
        TokenKind::Eq      => Some((BinOp::Eq, 5, 6)),
        TokenKind::Neq     => Some((BinOp::Neq, 5, 6)),
        TokenKind::Lt      => Some((BinOp::Lt, 5, 6)),
        TokenKind::Gt      => Some((BinOp::Gt, 5, 6)),
        TokenKind::Le      => Some((BinOp::Le, 5, 6)),
        TokenKind::Ge      => Some((BinOp::Ge, 5, 6)),
        // Level 4: | ~
        TokenKind::BitOr   => Some((BinOp::BitOr, 7, 8)),
        TokenKind::BitXor  => Some((BinOp::BitXor, 7, 8)),
        // Level 5: &
        TokenKind::BitAnd  => Some((BinOp::BitAnd, 9, 10)),
        // Level 6: + -
        TokenKind::Plus    => Some((BinOp::Add, 11, 12)),
        TokenKind::Minus   => Some((BinOp::Sub, 11, 12)),
        // Level 7: * / %
        TokenKind::Star    => Some((BinOp::Mul, 13, 14)),
        TokenKind::Slash   => Some((BinOp::Div, 13, 14)),
        TokenKind::Percent => Some((BinOp::Mod, 13, 14)),
        // Level 8: ^ (right-associative)
        TokenKind::Caret   => Some((BinOp::Pow, 16, 15)),
        // Range
        TokenKind::DotDot  => Some((BinOp::Range, 0, 1)),
        _ => None,
    }
}
