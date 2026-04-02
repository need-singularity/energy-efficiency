use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Debug, Clone, PartialEq)]
pub enum NodeType {
    Discovery,
    Hypothesis,
    Bt,
    Prediction,
    AccelHypothesis,
}

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct Node {
    pub id: String,
    pub node_type: NodeType,
    pub domain: String,
    pub project: String,
    pub summary: String,
    pub confidence: f64,
    pub lenses_used: Vec<String>,
    pub timestamp: String,
}
