use serde::{Deserialize, Serialize};
use std::fs;
use std::io;
use std::path::Path;

use super::edge::Edge;
use super::node::Node;
use super::structure::{self, ClosedLoop, Convergence, Hub};

#[derive(Serialize, Deserialize, Debug, Clone, Default)]
pub struct DiscoveryGraph {
    pub nodes: Vec<Node>,
    pub edges: Vec<Edge>,
}

impl DiscoveryGraph {
    pub fn new() -> Self {
        Self {
            nodes: Vec::new(),
            edges: Vec::new(),
        }
    }

    pub fn add_node(&mut self, node: Node) {
        self.nodes.push(node);
    }

    pub fn add_edge(&mut self, edge: Edge) {
        self.edges.push(edge);
    }

    pub fn closed_loops(&self) -> Vec<ClosedLoop> {
        structure::find_closed_triangles(&self.nodes, &self.edges)
    }

    pub fn hubs(&self, min_degree: usize) -> Vec<Hub> {
        structure::find_hubs(&self.edges, min_degree)
    }

    pub fn convergences(&self) -> Vec<Convergence> {
        structure::find_convergences(&self.edges)
    }

    /// Atomic save: write to .tmp then rename to prevent corruption.
    pub fn save(&self, path: &str) -> io::Result<()> {
        let tmp_path = format!("{}.tmp", path);
        let json = serde_json::to_string_pretty(self)
            .map_err(|e| io::Error::new(io::ErrorKind::Other, e))?;
        fs::write(&tmp_path, &json)?;
        fs::rename(&tmp_path, path)?;
        Ok(())
    }

    /// Load from file, or return empty graph if file doesn't exist.
    pub fn load(path: &str) -> io::Result<Self> {
        if !Path::new(path).exists() {
            return Ok(Self::new());
        }
        let data = fs::read_to_string(path)?;
        let graph: DiscoveryGraph =
            serde_json::from_str(&data).map_err(|e| io::Error::new(io::ErrorKind::InvalidData, e))?;
        Ok(graph)
    }
}
