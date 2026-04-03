/// TopologicalDCE — n=6 homotopy-inspired dead code elimination
///
/// Builds a control flow graph, computes connected components and
/// Betti numbers (topological invariants) to find dead subgraphs.
///
/// Key insight: Betti_0 = number of connected components.
/// If a component has no path from entry AND Betti_1 (cycle count) > 0,
/// it's "topologically dead" — unreachable cyclic code that naive
/// reachability might partially miss when edges are conditional.

use std::collections::{HashSet, VecDeque, HashMap};

// ─── Control Flow Graph ───────────────────────────────────────────

#[derive(Clone)]
pub struct CFG {
    pub num_nodes: usize,
    pub edges: Vec<(usize, usize)>,
    pub entry: usize,
    /// Instructions per node (for measuring elimination)
    pub instructions: Vec<usize>,
    /// Edge conditions: Some edges are "conditional" (may not fire)
    pub conditional_edges: HashSet<(usize, usize)>,
}

impl CFG {
    pub fn total_instructions(&self) -> usize {
        self.instructions.iter().sum()
    }
}

// ─── Naive Reachability DCE ───────────────────────────────────────

pub fn naive_reachability_dce(cfg: &CFG) -> (HashSet<usize>, usize) {
    // Simple BFS from entry — marks reachable nodes
    // Does NOT consider conditional edges specially
    let mut adj: Vec<Vec<usize>> = vec![vec![]; cfg.num_nodes];
    for &(a, b) in &cfg.edges {
        adj[a].push(b);
    }

    let mut visited = HashSet::new();
    let mut queue = VecDeque::new();
    queue.push_back(cfg.entry);
    visited.insert(cfg.entry);

    while let Some(node) = queue.pop_front() {
        for &next in &adj[node] {
            if visited.insert(next) {
                queue.push_back(next);
            }
        }
    }

    let dead: HashSet<usize> = (0..cfg.num_nodes)
        .filter(|n| !visited.contains(n))
        .collect();
    let eliminated: usize = dead.iter().map(|&n| cfg.instructions[n]).sum();
    (dead, eliminated)
}

// ─── Topological DCE (Betti number analysis) ─────────────────────

pub fn topological_dce(cfg: &CFG) -> (HashSet<usize>, usize) {
    let n = cfg.num_nodes;

    // Build adjacency (ignoring conditional edges for strong reachability)
    let mut strong_adj: Vec<Vec<usize>> = vec![vec![]; n];
    let mut full_adj: Vec<Vec<usize>> = vec![vec![]; n];
    let mut undirected_adj: Vec<Vec<usize>> = vec![vec![]; n];

    for &(a, b) in &cfg.edges {
        full_adj[a].push(b);
        undirected_adj[a].push(b);
        undirected_adj[b].push(a);
        if !cfg.conditional_edges.contains(&(a, b)) {
            strong_adj[a].push(b);
        }
    }

    // Phase 1: Strong reachability (unconditional edges only)
    let mut strong_reachable = HashSet::new();
    {
        let mut queue = VecDeque::new();
        queue.push_back(cfg.entry);
        strong_reachable.insert(cfg.entry);
        while let Some(node) = queue.pop_front() {
            for &next in &strong_adj[node] {
                if strong_reachable.insert(next) {
                    queue.push_back(next);
                }
            }
        }
    }

    // Phase 2: Full reachability (all edges)
    let mut full_reachable = HashSet::new();
    {
        let mut queue = VecDeque::new();
        queue.push_back(cfg.entry);
        full_reachable.insert(cfg.entry);
        while let Some(node) = queue.pop_front() {
            for &next in &full_adj[node] {
                if full_reachable.insert(next) {
                    queue.push_back(next);
                }
            }
        }
    }

    // Phase 3: Compute connected components on undirected graph
    let mut component_id = vec![usize::MAX; n];
    let mut num_components = 0;
    for start in 0..n {
        if component_id[start] != usize::MAX { continue; }
        let mut queue = VecDeque::new();
        queue.push_back(start);
        component_id[start] = num_components;
        while let Some(node) = queue.pop_front() {
            for &next in &undirected_adj[node] {
                if component_id[next] == usize::MAX {
                    component_id[next] = num_components;
                    queue.push_back(next);
                }
            }
        }
        num_components += 1;
    }

    // Phase 4: Betti numbers per component
    // Betti_0 = 1 (each component is connected)
    // Betti_1 = E - V + 1 (cycle rank for connected component)
    let entry_component = component_id[cfg.entry];
    let mut component_nodes: HashMap<usize, Vec<usize>> = HashMap::new();
    for i in 0..n {
        component_nodes.entry(component_id[i]).or_default().push(i);
    }

    let mut dead_nodes = HashSet::new();

    for (&comp_id, nodes) in &component_nodes {
        // Skip the entry component
        if comp_id == entry_component { continue; }

        // Check if any node in this component is full-reachable
        let any_reachable = nodes.iter().any(|n| full_reachable.contains(n));

        if !any_reachable {
            // Completely unreachable component — dead
            for &node in nodes {
                dead_nodes.insert(node);
            }
            continue;
        }

        // Component is reachable only via conditional edges
        // Compute Betti_1 (cycle rank) for this component
        let v = nodes.len();
        let node_set: HashSet<usize> = nodes.iter().copied().collect();
        let e = cfg.edges.iter()
            .filter(|&&(a, b)| node_set.contains(&a) && node_set.contains(&b))
            .count();
        let betti_1 = if e >= v { e - v + 1 } else { 0 };

        // Topological insight: if component has cycles (Betti_1 > 0)
        // AND is only reachable via conditional edges,
        // it's likely dead code (unreachable loops/recursive structures)
        let only_conditional_entry = nodes.iter().all(|&node| {
            // Check if all incoming edges from outside component are conditional
            cfg.edges.iter()
                .filter(|&&(a, b)| b == node && !node_set.contains(&a))
                .all(|&(a, b)| cfg.conditional_edges.contains(&(a, b)))
        });

        if betti_1 > 0 && only_conditional_entry && !nodes.iter().any(|n| strong_reachable.contains(n)) {
            // Topologically dead: cyclic subgraph reachable only via conditional edges
            // that are never taken (no strong path)
            for &node in nodes {
                dead_nodes.insert(node);
            }
        }
    }

    // Also include all nodes that are not full-reachable (same as naive)
    for i in 0..n {
        if !full_reachable.contains(&i) {
            dead_nodes.insert(i);
        }
    }

    let eliminated: usize = dead_nodes.iter().map(|&n| cfg.instructions[n]).sum();
    (dead_nodes, eliminated)
}

// ─── Synthetic CFG Generator ─────────────────────────────────────

pub fn generate_test_cfg(seed: u64) -> CFG {
    let mut rng = seed;
    let next = |r: &mut u64| -> u64 {
        *r = r.wrapping_mul(6364136223846793005).wrapping_add(1442695040888963407);
        *r >> 33
    };

    let num_nodes = 120; // large enough for meaningful topology
    let entry = 0;
    let mut edges = Vec::new();
    let mut conditional_edges = HashSet::new();

    // Build main spine from entry (about 60% of nodes)
    let spine_len = 72; // σ·n = 72
    for i in 0..spine_len - 1 {
        edges.push((i, i + 1));
        // Add some branches
        if next(&mut rng) % 4 == 0 {
            let target = (next(&mut rng) as usize % spine_len).max(1);
            edges.push((i, target));
            if next(&mut rng) % 3 == 0 {
                conditional_edges.insert((i, target));
            }
        }
    }

    // Create isolated subgraphs (truly dead code)
    let isolated_start = spine_len;
    let isolated_nodes = 12; // σ=12 isolated nodes
    for i in isolated_start..isolated_start + isolated_nodes - 1 {
        edges.push((i, i + 1));
    }
    // Add a cycle in the isolated subgraph
    edges.push((isolated_start + isolated_nodes - 1, isolated_start));

    // Create conditionally-reachable cyclic subgraph
    // These nodes are reachable from spine ONLY via conditional edges
    let cond_start = isolated_start + isolated_nodes;
    let cond_nodes = 18; // n·n/φ = 18
    // Conditional edge from spine to this subgraph
    edges.push((spine_len / 2, cond_start));
    conditional_edges.insert((spine_len / 2, cond_start));
    for i in cond_start..cond_start + cond_nodes - 1 {
        edges.push((i, i + 1));
    }
    // Add cycles (high Betti_1)
    edges.push((cond_start + cond_nodes - 1, cond_start));
    edges.push((cond_start + 3, cond_start + cond_nodes - 2));
    edges.push((cond_start + 6, cond_start + 1));

    // Remaining nodes: loosely connected to spine via conditional edges
    let loose_start = cond_start + cond_nodes;
    for i in loose_start..num_nodes {
        let target_in_spine = next(&mut rng) as usize % spine_len;
        edges.push((target_in_spine, i));
        if next(&mut rng) % 2 == 0 {
            conditional_edges.insert((target_in_spine, i));
        }
        // Some edges back
        if next(&mut rng) % 4 == 0 && i + 1 < num_nodes {
            edges.push((i, i + 1));
        }
    }

    let mut instructions = Vec::with_capacity(num_nodes);
    for i in 0..num_nodes {
        instructions.push(3 + (next(&mut rng) as usize % 10));
    }

    CFG { num_nodes, edges, entry, instructions, conditional_edges }
}

// ─── Benchmark ────────────────────────────────────────────────────

pub struct DCEBenchResult {
    pub total_instructions: usize,
    pub naive_eliminated: usize,
    pub topo_eliminated: usize,
    pub naive_pct: f64,
    pub topo_pct: f64,
    pub improvement_pct: f64,
}

pub fn bench_dce(seed: u64) -> DCEBenchResult {
    // Average over multiple random CFGs
    let trials = 20;
    let mut total_instr = 0usize;
    let mut total_naive = 0usize;
    let mut total_topo = 0usize;

    for trial in 0..trials {
        let cfg = generate_test_cfg(seed.wrapping_add(trial * 7919));
        total_instr += cfg.total_instructions();
        let (_, naive_elim) = naive_reachability_dce(&cfg);
        let (_, topo_elim) = topological_dce(&cfg);
        total_naive += naive_elim;
        total_topo += topo_elim;
    }

    let naive_pct = total_naive as f64 / total_instr as f64 * 100.0;
    let topo_pct = total_topo as f64 / total_instr as f64 * 100.0;

    DCEBenchResult {
        total_instructions: total_instr,
        naive_eliminated: total_naive,
        topo_eliminated: total_topo,
        naive_pct,
        topo_pct,
        improvement_pct: topo_pct - naive_pct,
    }
}
