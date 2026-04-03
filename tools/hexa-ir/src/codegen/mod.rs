/// Code Generation — IR -> native machine code
///
/// Pipeline: regalloc -> instruction selection -> binary emission
/// Targets: x86-64 (Mk.I), ARM64 (Mk.II stub)
/// Output formats: ELF (Linux), Mach-O (macOS)

pub mod regalloc;
pub mod x86_64;
pub mod arm64;
pub mod elf;
pub mod macho;

use crate::ir::*;

/// Compilation target
#[derive(Clone, Debug, PartialEq)]
pub enum Target {
    X86_64Linux,
    X86_64MacOS,
    Arm64MacOS,
}

impl Target {
    /// Detect native target for current platform
    pub fn native() -> Self {
        if cfg!(target_os = "macos") {
            if cfg!(target_arch = "aarch64") { Target::Arm64MacOS }
            else { Target::X86_64MacOS }
        } else {
            Target::X86_64Linux
        }
    }
}

/// Compile multiple functions to a single binary
pub fn compile_to_binary(functions: &[HexaFunction], target: Target) -> Vec<u8> {
    let mut all_code = Vec::new();
    for func in functions {
        let code = generate(func, &target);
        all_code.extend_from_slice(&code);
    }
    all_code
}

/// Generate native binary from optimized IR
pub fn generate(func: &HexaFunction, target: &Target) -> Vec<u8> {
    // Step 1: Register allocation
    let alloc = regalloc::allocate(func);

    // Step 2: Instruction selection
    let machine_code = match target {
        Target::X86_64Linux | Target::X86_64MacOS => {
            x86_64::select_function(func, &alloc)
        }
        Target::Arm64MacOS => {
            arm64::select_function(func, &alloc)
        }
    };

    // Step 3: Binary emission
    match target {
        Target::X86_64Linux => {
            elf::write_elf(&machine_code, 0x401000)
        }
        Target::X86_64MacOS => {
            macho::write_macho(&machine_code, 0x100000000)
        }
        Target::Arm64MacOS => {
            macho::write_macho(&machine_code, 0x100000000)
        }
    }
}
