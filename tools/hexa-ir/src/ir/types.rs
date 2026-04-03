/// HEXA-IR Types — σ-τ=8 primitives + τ=4 compound = σ=12 total
use crate::util::n6::*;

#[derive(Clone, Debug, PartialEq)]
pub enum HexaType {
    // Primitives (σ-τ=8)
    I64, F64, Bool, Char, Str, Byte, Void, Any,
    // Compound (τ=4)
    Struct(Vec<HexaType>),
    Enum(Vec<HexaType>),
    Array(Box<HexaType>, usize),
    Fn(Vec<HexaType>, Box<HexaType>),
}

impl HexaType {
    pub fn size_bytes(&self) -> usize {
        match self {
            HexaType::I64 | HexaType::F64 => SIGMA_TAU, // σ-τ = 8 bytes
            HexaType::Bool | HexaType::Byte => MU,       // μ = 1 byte
            HexaType::Char => TAU,                        // τ = 4 bytes (UTF-32)
            HexaType::Str => PHI_TAU,                     // 2^τ = 16 (ptr+len)
            HexaType::Void => 0,
            HexaType::Any => SIGMA_TAU,
            HexaType::Array(inner, count) => inner.size_bytes() * count,
            HexaType::Struct(fields) => fields.iter().map(|f| f.size_bytes()).sum(),
            _ => SIGMA_TAU, // pointer-sized for Enum, Fn
        }
    }

    pub fn is_primitive(&self) -> bool {
        matches!(self,
            HexaType::I64 | HexaType::F64 | HexaType::Bool | HexaType::Char |
            HexaType::Str | HexaType::Byte | HexaType::Void | HexaType::Any
        )
    }

    pub fn is_numeric(&self) -> bool {
        matches!(self, HexaType::I64 | HexaType::F64)
    }
}
