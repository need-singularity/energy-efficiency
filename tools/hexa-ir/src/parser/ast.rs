/// AST node types — the structured representation of HEXA-LANG programs
///
/// Node count follows n=6 arithmetic:
///   Decl:     tau=4 variants
///   Stmt:     n=6 variants
///   Expr:     sigma+phi=14 variants (Mk.I + ArrayLit + Match)
///   TypeExpr: n/phi=3 variants

use crate::lexer::Span;

/// Top-level program: a sequence of declarations
#[derive(Clone, Debug)]
pub struct Program {
    pub decls: Vec<Decl>,
}

// ── Declarations (tau=4) ──

#[derive(Clone, Debug)]
pub enum Decl {
    FnDecl(FnDecl),
    StructDecl(StructDecl),
    EnumDecl(EnumDecl),
    TypeAlias(TypeAliasDecl),
}

#[derive(Clone, Debug)]
pub struct FnDecl {
    pub name: String,
    pub params: Vec<(String, TypeExpr)>,
    pub ret_ty: Option<TypeExpr>,
    pub body: Block,
    pub span: Span,
}

#[derive(Clone, Debug)]
pub struct StructDecl {
    pub name: String,
    pub fields: Vec<(String, TypeExpr)>,
    pub span: Span,
}

#[derive(Clone, Debug)]
pub struct EnumDecl {
    pub name: String,
    pub variants: Vec<(String, Option<Vec<TypeExpr>>)>,
    pub span: Span,
}

#[derive(Clone, Debug)]
pub struct TypeAliasDecl {
    pub name: String,
    pub ty: TypeExpr,
    pub span: Span,
}

// ── Block ──

#[derive(Clone, Debug)]
pub struct Block {
    pub stmts: Vec<Stmt>,
    pub span: Span,
}

// ── Statements (n=6) ──

#[derive(Clone, Debug)]
pub enum Stmt {
    Let {
        name: String,
        mutable: bool,
        ty: Option<TypeExpr>,
        init: Option<Expr>,
        span: Span,
    },
    Assign {
        target: Expr,
        value: Expr,
        span: Span,
    },
    Return {
        value: Option<Expr>,
        span: Span,
    },
    If {
        cond: Expr,
        then_block: Block,
        else_block: Option<Block>,
        span: Span,
    },
    While {
        cond: Expr,
        body: Block,
        span: Span,
    },
    ExprStmt {
        expr: Expr,
        span: Span,
    },
}

// ── Expressions (sigma+phi=14) ──

#[derive(Clone, Debug)]
pub enum Expr {
    IntLit(i64, Span),
    FloatLit(f64, Span),
    BoolLit(bool, Span),
    StrLit(String, Span),
    Ident(String, Span),
    Binary {
        op: BinOp,
        lhs: Box<Expr>,
        rhs: Box<Expr>,
        span: Span,
    },
    Unary {
        op: UnOp,
        operand: Box<Expr>,
        span: Span,
    },
    Call {
        func: Box<Expr>,
        args: Vec<Expr>,
        span: Span,
    },
    Field {
        obj: Box<Expr>,
        name: String,
        span: Span,
    },
    Index {
        arr: Box<Expr>,
        idx: Box<Expr>,
        span: Span,
    },
    StructInit {
        name: String,
        fields: Vec<(String, Expr)>,
        span: Span,
    },
    /// Array literal: `[1, 2, 3]`
    ArrayLit {
        elements: Vec<Expr>,
        span: Span,
    },
    /// Match expression: `match expr { Pattern => body, ... }`
    Match {
        scrutinee: Box<Expr>,
        arms: Vec<MatchArm>,
        span: Span,
    },
    Block(Block),
}

/// A single arm of a match expression
#[derive(Clone, Debug)]
pub struct MatchArm {
    pub pattern: Pattern,
    pub body: Expr,
    pub span: Span,
}

/// Pattern for match arms
#[derive(Clone, Debug)]
pub enum Pattern {
    /// Wildcard: `_`
    Wildcard(Span),
    /// Integer literal: `42`
    Literal(i64, Span),
    /// Enum variant: `Color::Red` or `Color::RGB(r, g, b)`
    Variant {
        enum_name: String,
        variant_name: String,
        bindings: Vec<String>,
        span: Span,
    },
}

impl Expr {
    pub fn span(&self) -> Span {
        match self {
            Expr::IntLit(_, s) => *s,
            Expr::FloatLit(_, s) => *s,
            Expr::BoolLit(_, s) => *s,
            Expr::StrLit(_, s) => *s,
            Expr::Ident(_, s) => *s,
            Expr::Binary { span, .. } => *span,
            Expr::Unary { span, .. } => *span,
            Expr::Call { span, .. } => *span,
            Expr::Field { span, .. } => *span,
            Expr::Index { span, .. } => *span,
            Expr::StructInit { span, .. } => *span,
            Expr::ArrayLit { span, .. } => *span,
            Expr::Match { span, .. } => *span,
            Expr::Block(b) => b.span,
        }
    }
}

// ── Binary operators ──

#[derive(Clone, Debug, PartialEq)]
pub enum BinOp {
    // Arithmetic (n=6)
    Add, Sub, Mul, Div, Mod, Pow,
    // Comparison (n=6)
    Eq, Neq, Lt, Gt, Le, Ge,
    // Logic (n/phi=3 binary)
    And, Or, BitAnd, BitOr, BitXor,
    // Range
    Range,
}

// ── Unary operators ──

#[derive(Clone, Debug, PartialEq)]
pub enum UnOp {
    Neg,    // -
    Not,    // !
}

// ── Type expressions (n/phi=3) ──

#[derive(Clone, Debug)]
pub enum TypeExpr {
    /// Simple named type: `i64`, `bool`, `MyStruct`
    Named(String, Span),
    /// Array type: `[i64; 6]`
    Array(Box<TypeExpr>, usize, Span),
    /// Function type: `fn(i64, bool) -> f64`
    Fn(Vec<TypeExpr>, Box<TypeExpr>, Span),
}

impl TypeExpr {
    pub fn span(&self) -> Span {
        match self {
            TypeExpr::Named(_, s) => *s,
            TypeExpr::Array(_, _, s) => *s,
            TypeExpr::Fn(_, _, s) => *s,
        }
    }
}
