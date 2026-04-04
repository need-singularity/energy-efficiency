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

#[cfg(test)]
mod string_tests {
    use crate::lexer;
    use crate::parser;
    use crate::sema;
    use crate::lower;
    use crate::ir::HexaType;

    /// Helper: run full pipeline (lex → parse → sema → lower) and return IR functions
    fn compile_to_ir(source: &str) -> Vec<crate::ir::HexaFunction> {
        let tokens = lexer::lex(source).expect("lex failed");
        let program = parser::parse(tokens).expect("parse failed");
        sema::analyze(&program).expect("sema failed");
        lower::lower_program(&program)
    }

    #[test]
    fn test_string_literal_basic() {
        // Simple string literal assignment + return 0
        let source = r#"
fn main() -> i64 {
    let s = "hello";
    return 0;
}
"#;
        let funcs = compile_to_ir(source);
        assert_eq!(funcs.len(), 1);
        let main_fn = &funcs[0];
        assert_eq!(main_fn.name, "main");

        // String pool should contain "hello"
        assert_eq!(main_fn.string_pool.len(), 1);
        assert_eq!(main_fn.string_pool[0], "hello");
    }

    #[test]
    fn test_string_literal_escape_sequences() {
        let source = r#"
fn main() -> i64 {
    let s = "hello\nworld";
    return 0;
}
"#;
        let funcs = compile_to_ir(source);
        let main_fn = &funcs[0];
        assert_eq!(main_fn.string_pool.len(), 1);
        assert_eq!(main_fn.string_pool[0], "hello\nworld");
    }

    #[test]
    fn test_string_pool_dedup() {
        // Same string used twice should be interned once
        let source = r#"
fn main() -> i64 {
    let a = "hello";
    let b = "hello";
    return 0;
}
"#;
        let funcs = compile_to_ir(source);
        let main_fn = &funcs[0];
        assert_eq!(main_fn.string_pool.len(), 1);
        assert_eq!(main_fn.string_pool[0], "hello");
    }

    #[test]
    fn test_string_pool_multiple() {
        let source = r#"
fn main() -> i64 {
    let a = "hello";
    let b = "world";
    return 0;
}
"#;
        let funcs = compile_to_ir(source);
        let main_fn = &funcs[0];
        assert_eq!(main_fn.string_pool.len(), 2);
        assert_eq!(main_fn.string_pool[0], "hello");
        assert_eq!(main_fn.string_pool[1], "world");
    }

    #[test]
    fn test_string_type_checking() {
        // StrLit should type-check as Str
        let source = r#"
fn main() -> i64 {
    let s = "test";
    return 0;
}
"#;
        let tokens = lexer::lex(source).expect("lex failed");
        let program = parser::parse(tokens).expect("parse failed");
        // Should pass sema without errors
        sema::analyze(&program).expect("sema should accept string literal");
    }

    #[test]
    fn test_string_ir_alloc_has_pool_index() {
        let source = r#"
fn main() -> i64 {
    let s = "hello";
    return 0;
}
"#;
        let funcs = compile_to_ir(source);
        let main_fn = &funcs[0];

        // Find the Alloc instruction with Str type
        let str_alloc = main_fn.blocks.iter()
            .flat_map(|b| b.instrs.iter())
            .find(|i| matches!(i.ty, HexaType::Str) && i.label.is_some());

        assert!(str_alloc.is_some(), "should have a Str-typed Alloc instruction");
        let instr = str_alloc.unwrap();
        // args[0] = pool index (0), args[1] = string length (5)
        assert_eq!(instr.args.len(), 2);
        assert_eq!(instr.args[0], 0); // pool index
        assert_eq!(instr.args[1], 5); // "hello".len()
        assert_eq!(instr.label.as_deref(), Some("str_pool_0"));
    }
}

#[cfg(test)]
mod struct_tests {
    use crate::lexer;
    use crate::parser;
    use crate::sema;
    use crate::lower;
    use crate::ir::{HexaType, HexaOp};

    /// Helper: run full pipeline (lex -> parse -> sema -> lower) and return IR functions
    fn compile_to_ir(source: &str) -> Vec<crate::ir::HexaFunction> {
        let tokens = lexer::lex(source).expect("lex failed");
        let program = parser::parse(tokens).expect("parse failed");
        sema::analyze(&program).expect("sema failed");
        lower::lower_program(&program)
    }

    #[test]
    fn test_struct_basic_init() {
        let source = r#"
struct Point { x: i64, y: i64 }

fn main() -> i64 {
    let p = Point { x: 10, y: 20 };
    return 0;
}
"#;
        let funcs = compile_to_ir(source);
        assert_eq!(funcs.len(), 1);
        let main_fn = &funcs[0];
        assert_eq!(main_fn.name, "main");

        // Should have a Struct-typed Alloc instruction
        let struct_alloc = main_fn.blocks.iter()
            .flat_map(|b| b.instrs.iter())
            .find(|i| matches!(i.ty, HexaType::Struct(_)) && i.op == HexaOp::Alloc);
        assert!(struct_alloc.is_some(), "should have a Struct-typed Alloc instruction");
        let alloc_instr = struct_alloc.unwrap();
        // Total size should be 16 bytes (2 * i64 = 2 * 8)
        assert_eq!(alloc_instr.args[0], 16, "struct alloc size should be 16 bytes");
        assert_eq!(alloc_instr.label.as_deref(), Some("struct_Point"));
    }

    #[test]
    fn test_struct_field_access() {
        let source = r#"
struct Point { x: i64, y: i64 }

fn main() -> i64 {
    let p = Point { x: 10, y: 20 };
    return p.x + p.y;
}
"#;
        let funcs = compile_to_ir(source);
        assert_eq!(funcs.len(), 1);
        let main_fn = &funcs[0];

        // Should have field access Load instructions with field labels
        let field_loads: Vec<_> = main_fn.blocks.iter()
            .flat_map(|b| b.instrs.iter())
            .filter(|i| i.op == HexaOp::Load && i.label.is_some())
            .collect();

        // Should have at least 2 field loads (p.x and p.y)
        assert!(field_loads.len() >= 2,
            "should have at least 2 field Load instructions, found {}",
            field_loads.len());

        // First field load should be for "x" (offset 0, direct from base)
        let x_load = field_loads.iter().find(|i| i.label.as_deref() == Some("field_x"));
        assert!(x_load.is_some(), "should have a Load for field 'x'");

        // Second field load should be for "y"
        let y_load = field_loads.iter().find(|i| i.label.as_deref() == Some("field_y"));
        assert!(y_load.is_some(), "should have a Load for field 'y'");
    }

    #[test]
    fn test_struct_field_offset() {
        let source = r#"
struct Point { x: i64, y: i64 }

fn main() -> i64 {
    let p = Point { x: 10, y: 20 };
    return p.y;
}
"#;
        let funcs = compile_to_ir(source);
        let main_fn = &funcs[0];

        // For p.y (second field), there should be an Alloc with value 8 (byte offset)
        // followed by an Add (base + offset), then a Load
        let alloc_8 = main_fn.blocks.iter()
            .flat_map(|b| b.instrs.iter())
            .find(|i| i.op == HexaOp::Alloc
                && matches!(i.ty, HexaType::I64)
                && i.args.first() == Some(&8)
                && i.label.is_none());
        assert!(alloc_8.is_some(),
            "should have an Alloc with offset=8 for second field access");
    }

    #[test]
    fn test_struct_sema_field_type() {
        // Verify that sema correctly resolves struct field types
        let source = r#"
struct Point { x: i64, y: i64 }

fn main() -> i64 {
    let p = Point { x: 10, y: 20 };
    return p.x + p.y;
}
"#;
        let tokens = lexer::lex(source).expect("lex failed");
        let program = parser::parse(tokens).expect("parse failed");
        // Should pass sema without errors (field access types resolve correctly)
        sema::analyze(&program).expect("sema should accept struct field access");
    }

    #[test]
    fn test_struct_three_fields() {
        let source = r#"
struct Vec3 { x: i64, y: i64, z: i64 }

fn main() -> i64 {
    let v = Vec3 { x: 1, y: 2, z: 3 };
    return v.z;
}
"#;
        let funcs = compile_to_ir(source);
        let main_fn = &funcs[0];

        // Struct alloc should be 24 bytes (3 * 8)
        let struct_alloc = main_fn.blocks.iter()
            .flat_map(|b| b.instrs.iter())
            .find(|i| matches!(i.ty, HexaType::Struct(_)) && i.op == HexaOp::Alloc);
        assert!(struct_alloc.is_some());
        assert_eq!(struct_alloc.unwrap().args[0], 24, "Vec3 should be 24 bytes");

        // For v.z, offset should be 16 (2 * 8 bytes)
        let alloc_16 = main_fn.blocks.iter()
            .flat_map(|b| b.instrs.iter())
            .find(|i| i.op == HexaOp::Alloc
                && matches!(i.ty, HexaType::I64)
                && i.args.first() == Some(&16)
                && i.label.is_none());
        assert!(alloc_16.is_some(),
            "should have offset=16 for third field access");
    }

    #[test]
    fn test_struct_codegen_asm() {
        // Verify that ARM64 assembly generation handles structs without panicking
        let source = r#"
struct Point { x: i64, y: i64 }

fn main() -> i64 {
    let p = Point { x: 10, y: 20 };
    return p.x + p.y;
}
"#;
        let funcs = compile_to_ir(source);
        let asm = crate::codegen::arm64_asm::emit_program_asm(&funcs);
        assert!(asm.contains("_main:"), "ASM should contain _main label");
        // Should contain struct data allocation (add x9, sp, #offset)
        assert!(asm.contains("add x9, sp,"), "ASM should allocate struct on stack");
    }
}

#[cfg(test)]
mod enum_match_tests {
    use crate::lexer;
    use crate::parser;
    use crate::sema;
    use crate::lower;
    use crate::ir::{HexaType, HexaOp};

    /// Helper: run full pipeline (lex -> parse -> sema -> lower) and return IR functions
    fn compile_to_ir(source: &str) -> Vec<crate::ir::HexaFunction> {
        let tokens = lexer::lex(source).expect("lex failed");
        let program = parser::parse(tokens).expect("parse failed");
        sema::analyze(&program).expect("sema failed");
        lower::lower_program(&program)
    }

    #[test]
    fn test_enum_parse_and_lower() {
        let source = r#"
enum Color { Red, Green, Blue }

fn main() -> i64 {
    let c = Color::Green;
    return 0;
}
"#;
        let funcs = compile_to_ir(source);
        assert_eq!(funcs.len(), 1);
        let main_fn = &funcs[0];
        assert_eq!(main_fn.name, "main");

        // Color::Green should lower to an Alloc with tag=1 (second variant)
        let tag_alloc = main_fn.blocks.iter()
            .flat_map(|b| b.instrs.iter())
            .find(|i| i.op == HexaOp::Alloc
                && i.label.as_deref() == Some("enum_tag_Color::Green"));
        assert!(tag_alloc.is_some(), "should have an enum tag Alloc for Color::Green");
        assert_eq!(tag_alloc.unwrap().args[0], 1, "Green should have tag=1");
    }

    #[test]
    fn test_enum_variant_tags() {
        let source = r#"
enum Color { Red, Green, Blue }

fn main() -> i64 {
    let r = Color::Red;
    let g = Color::Green;
    let b = Color::Blue;
    return 0;
}
"#;
        let funcs = compile_to_ir(source);
        let main_fn = &funcs[0];

        let tags: Vec<_> = main_fn.blocks.iter()
            .flat_map(|b| b.instrs.iter())
            .filter(|i| i.op == HexaOp::Alloc
                && i.label.as_ref().map_or(false, |l| l.starts_with("enum_tag_")))
            .collect();

        assert_eq!(tags.len(), 3, "should have 3 enum tag Allocs");
        assert_eq!(tags[0].args[0], 0, "Red tag = 0");
        assert_eq!(tags[1].args[0], 1, "Green tag = 1");
        assert_eq!(tags[2].args[0], 2, "Blue tag = 2");
    }

    #[test]
    fn test_match_parse() {
        // Verify that match expression parses and sema-checks correctly
        let source = r#"
enum Color { Red, Green, Blue }

fn color_val(c: Color) -> i64 {
    return match c {
        Color::Red => 1,
        Color::Green => 2,
        Color::Blue => 3,
    };
}

fn main() -> i64 {
    let c = Color::Green;
    return color_val(c);
}
"#;
        let tokens = lexer::lex(source).expect("lex failed");
        let program = parser::parse(tokens).expect("parse failed");
        sema::analyze(&program).expect("sema should accept match expression");
    }

    #[test]
    fn test_match_lowering_creates_blocks() {
        let source = r#"
enum Color { Red, Green, Blue }

fn color_val(c: Color) -> i64 {
    return match c {
        Color::Red => 1,
        Color::Green => 2,
        Color::Blue => 3,
    };
}

fn main() -> i64 {
    return 0;
}
"#;
        let funcs = compile_to_ir(source);

        // Find color_val function
        let color_fn = funcs.iter().find(|f| f.name == "color_val")
            .expect("should have color_val function");

        // Match should create multiple blocks (entry + 3 arm blocks + check blocks + merge)
        assert!(color_fn.blocks.len() >= 4,
            "match should create multiple blocks, found {}",
            color_fn.blocks.len());

        // Should have Branch instructions (compare-and-branch for each arm)
        let branch_count = color_fn.blocks.iter()
            .flat_map(|b| b.instrs.iter())
            .filter(|i| i.op == HexaOp::Branch)
            .count();
        assert!(branch_count >= 2,
            "should have at least 2 Branch instructions for 3-arm match, found {}",
            branch_count);

        // Should have Jump instructions (arm -> merge)
        let jump_count = color_fn.blocks.iter()
            .flat_map(|b| b.instrs.iter())
            .filter(|i| i.op == HexaOp::Jump)
            .count();
        assert!(jump_count >= 3,
            "should have at least 3 Jump instructions (one per arm), found {}",
            jump_count);
    }

    #[test]
    fn test_match_with_wildcard() {
        let source = r#"
enum Color { Red, Green, Blue }

fn is_red(c: Color) -> i64 {
    return match c {
        Color::Red => 1,
        _ => 0,
    };
}

fn main() -> i64 {
    return 0;
}
"#;
        let funcs = compile_to_ir(source);
        let is_red_fn = funcs.iter().find(|f| f.name == "is_red")
            .expect("should have is_red function");

        // Should compile without errors and have multiple blocks
        assert!(is_red_fn.blocks.len() >= 3,
            "wildcard match should create multiple blocks, found {}",
            is_red_fn.blocks.len());
    }

    #[test]
    fn test_enum_sema_type_check() {
        // Verify enum type names are registered in sema
        let source = r#"
enum Direction { Up, Down, Left, Right }

fn main() -> i64 {
    let d = Direction::Up;
    return 0;
}
"#;
        let tokens = lexer::lex(source).expect("lex failed");
        let program = parser::parse(tokens).expect("parse failed");
        sema::analyze(&program).expect("sema should accept enum usage");
    }

    // ── Array tests ──

    #[test]
    fn test_array_literal_parse_and_sema() {
        let source = r#"
fn main() -> i64 {
    let arr: [i64; 3] = [10, 20, 30]
    return arr[1]
}
"#;
        let tokens = lexer::lex(source).expect("lex failed");
        let program = parser::parse(tokens).expect("parse failed");
        sema::analyze(&program).expect("sema should accept array literal");
    }

    #[test]
    fn test_array_ir_alloc_type() {
        let source = r#"
fn main() -> i64 {
    let arr: [i64; 3] = [10, 20, 30]
    return arr[0]
}
"#;
        let funcs = compile_to_ir(source);
        let main_fn = &funcs[0];
        // First instruction should be Array allocation
        let alloc = &main_fn.blocks[0].instrs[0];
        assert_eq!(alloc.op, crate::ir::HexaOp::Alloc);
        assert!(matches!(alloc.ty, HexaType::Array(_, 3)),
            "Array alloc should have Array(I64, 3) type, got {:?}", alloc.ty);
        // Total allocation = 3 * 8 = 24 bytes
        assert_eq!(alloc.args[0], 24, "Array alloc should request 24 bytes");
    }

    #[test]
    fn test_array_ir_stores_elements() {
        let source = r#"
fn main() -> i64 {
    let arr: [i64; 3] = [10, 20, 30]
    return arr[0]
}
"#;
        let funcs = compile_to_ir(source);
        let main_fn = &funcs[0];
        // Count Store instructions: should be 3 (one per element)
        let store_count = main_fn.blocks[0].instrs.iter()
            .filter(|i| i.op == crate::ir::HexaOp::Store)
            .count();
        assert_eq!(store_count, 3, "Should have 3 Store instructions for 3 array elements");
    }

    #[test]
    fn test_array_index_has_proof_assert() {
        let source = r#"
fn main() -> i64 {
    let arr: [i64; 3] = [10, 20, 30]
    return arr[1]
}
"#;
        let funcs = compile_to_ir(source);
        let main_fn = &funcs[0];
        // Should have a ProofAssert for bounds checking
        let has_proof = main_fn.blocks[0].instrs.iter()
            .any(|i| i.op == crate::ir::HexaOp::ProofAssert);
        assert!(has_proof, "Array index should emit ProofAssert for bounds checking");
    }

    #[test]
    fn test_array_index_element_size_scaling() {
        let source = r#"
fn main() -> i64 {
    let arr: [i64; 3] = [10, 20, 30]
    return arr[2]
}
"#;
        let funcs = compile_to_ir(source);
        let main_fn = &funcs[0];
        // Should have a Mul instruction for index * element_size
        let has_mul = main_fn.blocks[0].instrs.iter()
            .any(|i| i.op == crate::ir::HexaOp::Mul);
        assert!(has_mul, "Array index should emit Mul for element size scaling");
    }

    #[test]
    fn test_array_sema_element_type() {
        // Verify sema infers correct element type from array
        let source = r#"
fn main() -> i64 {
    let arr: [i64; 3] = [10, 20, 30]
    return arr[0]
}
"#;
        let tokens = lexer::lex(source).expect("lex failed");
        let program = parser::parse(tokens).expect("parse failed");
        // Should pass sema: arr[0] has type i64, matches return type
        sema::analyze(&program).expect("sema should accept array index as i64");
    }

    #[test]
    fn test_array_codegen_asm() {
        // Verify ARM64 assembly generation handles arrays without panicking
        let source = r#"
fn main() -> i64 {
    let arr: [i64; 3] = [10, 20, 30]
    return arr[1]
}
"#;
        let mut funcs = compile_to_ir(source);
        for func in &mut funcs {
            crate::opt::run_pipeline(func);
        }
        let asm = crate::codegen::arm64_asm::emit_program_asm(&funcs);
        // Assembly should contain array base address computation
        assert!(asm.contains("add x9, sp, #"), "Should compute array base from sp");
        // Assembly should contain pointer-based stores
        assert!(asm.contains("str x9, [x10]") || asm.contains("str x9, [x"),
            "Should have pointer-based stores for array elements");
    }
}

#[cfg(test)]
mod builtin_tests {
    use crate::lexer;
    use crate::parser;
    use crate::sema;
    use crate::lower;
    use crate::ir::{HexaType, HexaOp};

    /// Helper: full pipeline to IR
    fn compile_to_ir(source: &str) -> Vec<crate::ir::HexaFunction> {
        let tokens = lexer::lex(source).expect("lex failed");
        let program = parser::parse(tokens).expect("parse failed");
        sema::analyze(&program).expect("sema failed");
        lower::lower_program(&program)
    }

    #[test]
    fn test_print_sema_accepts() {
        let source = r#"
fn main() -> i64 {
    print("hello world\n");
    return 0;
}
"#;
        let tokens = lexer::lex(source).expect("lex failed");
        let program = parser::parse(tokens).expect("parse failed");
        sema::analyze(&program).expect("sema should accept print() built-in");
    }

    #[test]
    fn test_print_lowers_to_call() {
        let source = r#"
fn main() -> i64 {
    print("hello\n");
    return 0;
}
"#;
        let funcs = compile_to_ir(source);
        let main_fn = &funcs[0];

        let print_call = main_fn.blocks.iter()
            .flat_map(|b| b.instrs.iter())
            .find(|i| i.op == HexaOp::Call && i.label.as_deref() == Some("print"));
        assert!(print_call.is_some(), "should have a Call to 'print'");

        assert_eq!(main_fn.string_pool.len(), 1);
        assert_eq!(main_fn.string_pool[0], "hello\n");
    }

    #[test]
    fn test_print_codegen_emits_syscall() {
        let source = r#"
fn main() -> i64 {
    print("hello world\n");
    return 0;
}
"#;
        let funcs = compile_to_ir(source);
        let asm = crate::codegen::arm64_asm::emit_program_asm(&funcs);

        assert!(asm.contains("_str_main_0:"), "ASM should have string constant label");
        assert!(asm.contains("hello world"), "ASM should contain the string literal");
        assert!(asm.contains("mov x16, #4"), "ASM should have SYS_write syscall number");
        assert!(asm.contains("svc #0x80"), "ASM should have svc instruction");
        assert!(asm.contains("mov x0, #1"), "ASM should set fd=1 (stdout)");
        assert!(!asm.contains("bl _print"), "print should be inlined, not a bl call");
    }

    #[test]
    fn test_file_io_sema_accepts() {
        let source = r#"
fn main() -> i64 {
    let fd = file_open("test.txt");
    let n = file_close(fd);
    return 0;
}
"#;
        let tokens = lexer::lex(source).expect("lex failed");
        let program = parser::parse(tokens).expect("parse failed");
        sema::analyze(&program).expect("sema should accept file I/O built-ins");
    }

    #[test]
    fn test_file_io_lowers_to_calls() {
        let source = r#"
fn main() -> i64 {
    let fd = file_open("test.txt");
    let n = file_close(fd);
    return 0;
}
"#;
        let funcs = compile_to_ir(source);
        let main_fn = &funcs[0];

        let open_call = main_fn.blocks.iter()
            .flat_map(|b| b.instrs.iter())
            .find(|i| i.op == HexaOp::Call && i.label.as_deref() == Some("file_open"));
        assert!(open_call.is_some(), "should have Call to 'file_open'");

        let close_call = main_fn.blocks.iter()
            .flat_map(|b| b.instrs.iter())
            .find(|i| i.op == HexaOp::Call && i.label.as_deref() == Some("file_close"));
        assert!(close_call.is_some(), "should have Call to 'file_close'");
    }

    #[test]
    fn test_file_open_codegen_emits_syscall() {
        let source = r#"
fn main() -> i64 {
    let fd = file_open("test.txt");
    return 0;
}
"#;
        let funcs = compile_to_ir(source);
        let asm = crate::codegen::arm64_asm::emit_program_asm(&funcs);

        assert!(asm.contains("mov x16, #5"), "ASM should have SYS_open syscall number");
        assert!(!asm.contains("bl _file_open"), "file_open should be inlined");
    }

    #[test]
    fn test_heap_alloc_sema_accepts() {
        let source = r#"
fn main() -> i64 {
    let ptr = heap_alloc(4096);
    let r = heap_free(ptr, 4096);
    return 0;
}
"#;
        let tokens = lexer::lex(source).expect("lex failed");
        let program = parser::parse(tokens).expect("parse failed");
        sema::analyze(&program).expect("sema should accept heap built-ins");
    }

    #[test]
    fn test_heap_alloc_codegen_emits_mmap() {
        let source = r#"
fn main() -> i64 {
    let ptr = heap_alloc(4096);
    return 0;
}
"#;
        let funcs = compile_to_ir(source);
        let asm = crate::codegen::arm64_asm::emit_program_asm(&funcs);

        assert!(asm.contains("mov x16, #197"), "ASM should have SYS_mmap syscall number");
        assert!(asm.contains("mov x3, #0x1002"), "ASM should have MAP_ANON|MAP_PRIVATE flags");
        assert!(!asm.contains("bl _heap_alloc"), "heap_alloc should be inlined");
    }

    #[test]
    fn test_heap_free_codegen_emits_munmap() {
        let source = r#"
fn main() -> i64 {
    let ptr = heap_alloc(4096);
    let r = heap_free(ptr, 4096);
    return 0;
}
"#;
        let funcs = compile_to_ir(source);
        let asm = crate::codegen::arm64_asm::emit_program_asm(&funcs);

        assert!(asm.contains("mov x16, #73"), "ASM should have SYS_munmap syscall number");
    }

    #[test]
    fn test_all_builtins_coexist() {
        let source = r#"
fn main() -> i64 {
    print("start\n");
    let fd = file_open("data.txt");
    let n = file_close(fd);
    let ptr = heap_alloc(1024);
    let r = heap_free(ptr, 1024);
    print("done\n");
    return 0;
}
"#;
        let funcs = compile_to_ir(source);
        assert_eq!(funcs.len(), 1);
        let main_fn = &funcs[0];

        let call_count = main_fn.blocks.iter()
            .flat_map(|b| b.instrs.iter())
            .filter(|i| i.op == HexaOp::Call)
            .count();
        assert_eq!(call_count, 6, "should have 6 built-in calls");

        let asm = crate::codegen::arm64_asm::emit_program_asm(&funcs);
        assert!(!asm.contains("bl _print"), "print should be inlined");
        assert!(!asm.contains("bl _file_open"), "file_open should be inlined");
        assert!(!asm.contains("bl _file_close"), "file_close should be inlined");
        assert!(!asm.contains("bl _heap_alloc"), "heap_alloc should be inlined");
        assert!(!asm.contains("bl _heap_free"), "heap_free should be inlined");

        assert!(asm.contains("mov x16, #4"), "should have SYS_write");
        assert!(asm.contains("mov x16, #5"), "should have SYS_open");
        assert!(asm.contains("mov x16, #6"), "should have SYS_close");
        assert!(asm.contains("mov x16, #197"), "should have SYS_mmap");
        assert!(asm.contains("mov x16, #73"), "should have SYS_munmap");
    }
}
