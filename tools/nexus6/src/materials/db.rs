use serde::{Deserialize, Serialize};
use std::collections::HashMap;

/// A single material entry with numeric properties.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Material {
    pub name: String,
    pub properties: HashMap<String, f64>,
}

/// A domain (e.g., superconductor, chip-architecture) containing materials and an optional ceiling.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DomainData {
    pub materials: Vec<Material>,
    #[serde(default)]
    pub ceiling: HashMap<String, f64>,
}

/// Top-level materials database: domain name -> domain data.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MaterialsDB {
    pub domains: HashMap<String, DomainData>,
}

/// Load a MaterialsDB from a JSON file path.
pub fn load(path: &str) -> MaterialsDB {
    let content = std::fs::read_to_string(path)
        .unwrap_or_else(|e| panic!("Failed to read materials DB at {}: {}", path, e));
    serde_json::from_str(&content)
        .unwrap_or_else(|e| panic!("Failed to parse materials DB JSON: {}", e))
}

/// Convert a domain's materials into a flat f64 matrix for the given feature keys.
///
/// Returns (flat_data, n_rows, n_cols). Missing properties become f64::NAN.
pub fn materials_as_matrix(
    domain: &DomainData,
    feature_keys: &[&str],
) -> (Vec<f64>, usize, usize) {
    let n_rows = domain.materials.len();
    let n_cols = feature_keys.len();
    let mut data = Vec::with_capacity(n_rows * n_cols);

    for mat in &domain.materials {
        for &key in feature_keys {
            let val = mat.properties.get(key).copied().unwrap_or(f64::NAN);
            data.push(val);
        }
    }

    (data, n_rows, n_cols)
}
