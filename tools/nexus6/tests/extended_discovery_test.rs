use nexus6::graph::*;
use nexus6::graph::bt_nodes::populate_bt_graph;
use nexus6::graph::discovery_nodes::populate_all_discoveries;
use nexus6::graph::expanded_nodes::populate_expanded_graph;
use nexus6::graph::extended_discovery_nodes::*;

fn full_graph() -> DiscoveryGraph {
    let mut g = DiscoveryGraph::new();
    populate_bt_graph(&mut g);
    populate_expanded_graph(&mut g);
    populate_all_discoveries(&mut g);
    g
}

// ── Full integration: base + extended ──

#[test]
fn test_full_graph_with_extended_nodes() {
    let mut g = full_graph();
    let (nodes, edges) = populate_all_extended(&mut g);

    assert_eq!(nodes, 32, "32 extended nodes");
    assert!(edges > 100, "should add 100+ edges, got {}", edges);

    // Total: 127 BT + 79 expanded + 39 discovery + 32 extended = 277
    assert!(
        g.nodes.len() >= 270,
        "total graph should have 270+ nodes, got {}",
        g.nodes.len()
    );
}

#[test]
fn test_extended_entry_count() {
    assert_eq!(extended_entry_count(), 32);
}

// ── Validates edge chains ──

#[test]
fn test_validates_chain_env_ghg() {
    let mut g = full_graph();
    populate_env_ghg_extended(&mut g);

    // XDISC-ENV-01 validates DISC-ENV-01 (Kyoto GHG completeness)
    // XDISC-ENV-02 validates DISC-ENV-01 too (CH4 sub-finding)
    let val_count = g.edges.iter()
        .filter(|e| e.to == "DISC-ENV-01" && e.edge_type == EdgeType::Validates)
        .count();
    assert!(val_count >= 2, "DISC-ENV-01 should receive 2+ Validates edges, got {}", val_count);
}

#[test]
fn test_validates_chain_robo_se3() {
    let mut g = full_graph();
    populate_robo_kinematics_extended(&mut g);

    // Multiple kinematic discoveries validate DISC-ROBO-01 (SE(3) universality)
    let val_count = g.edges.iter()
        .filter(|e| e.to == "DISC-ROBO-01" && e.edge_type == EdgeType::Validates)
        .count();
    assert!(val_count >= 2, "DISC-ROBO-01 should receive 2+ Validates edges, got {}", val_count);
}

// ── Cross-domain connectivity ──

#[test]
fn test_cross_nodes_bridge_env_and_robo() {
    let mut g = full_graph();
    populate_all_extended(&mut g);

    // XDISC-CROSS-01 should exist and span Environment + Robotics
    let cross01 = g.nodes.iter().find(|n| n.id == "XDISC-CROSS-01").unwrap();
    assert!(cross01.domain.contains("Environment"));
    assert!(cross01.domain.contains("Robotics"));
    assert!(cross01.domain.contains("Material"));
}

#[test]
fn test_cross_nodes_bridge_sw_and_robo() {
    let mut g = full_graph();
    populate_all_extended(&mut g);

    // XDISC-CROSS-05 spans Software + Environment + Robotics
    let cross05 = g.nodes.iter().find(|n| n.id == "XDISC-CROSS-05").unwrap();
    assert!(cross05.domain.contains("Software"));
    assert!(cross05.domain.contains("Robotics"));
}

#[test]
fn test_extended_merges_with_existing_discoveries() {
    let mut g = full_graph();
    populate_all_extended(&mut g);

    // At least some XDISC nodes should Merge with existing DISC nodes
    let ext_to_existing_merges = g.edges.iter().filter(|e| {
        e.edge_type == EdgeType::Merges
            && (e.from.starts_with("XDISC-") || e.from.starts_with("XHYP-"))
            && (e.to.starts_with("DISC-") || e.to.starts_with("HYP-"))
    }).count();
    assert!(
        ext_to_existing_merges > 20,
        "Extended nodes should merge with 20+ existing nodes, got {}",
        ext_to_existing_merges
    );
}

// ── Hub analysis ──

#[test]
fn test_extended_graph_has_hubs() {
    let mut g = full_graph();
    populate_all_extended(&mut g);

    let hubs = g.hubs(10);
    assert!(!hubs.is_empty(), "Extended graph should have hubs with degree >= 10");
}

// ── Experiment nodes ──

#[test]
fn test_experiment_node_types() {
    let mut g = full_graph();
    populate_all_extended(&mut g);

    let experiments: Vec<_> = g.nodes.iter()
        .filter(|n| n.id.starts_with("XEXP-"))
        .collect();
    assert_eq!(experiments.len(), 2);
    for exp in &experiments {
        assert_eq!(exp.node_type, NodeType::Experiment);
    }
}

// ── Convergence detection ──

#[test]
fn test_convergence_on_validated_nodes() {
    let mut g = full_graph();
    populate_all_extended(&mut g);

    let convs = g.convergences();
    // DISC-ROBO-01 should be a convergence target (validated by XDISC-ROBO-06 and XDISC-ROBO-07)
    let robo01_conv = convs.iter().find(|c| c.target == "DISC-ROBO-01");
    assert!(
        robo01_conv.is_some(),
        "DISC-ROBO-01 should be a convergence target"
    );
    assert!(
        robo01_conv.unwrap().sources.len() >= 2,
        "DISC-ROBO-01 should have 2+ incoming sources"
    );
}

// ── Persistence roundtrip ──

#[test]
fn test_extended_graph_save_load() {
    let mut g = full_graph();
    populate_all_extended(&mut g);

    let tmp = "/tmp/nexus6_extended_graph_test.json";
    g.save(tmp).expect("save failed");
    let loaded = DiscoveryGraph::load(tmp).expect("load failed");

    assert_eq!(loaded.nodes.len(), g.nodes.len());
    assert_eq!(loaded.edges.len(), g.edges.len());

    // Verify an extended node survived roundtrip
    assert!(loaded.nodes.iter().any(|n| n.id == "XDISC-CROSS-01"));
    assert!(loaded.nodes.iter().any(|n| n.id == "XEXP-ROBO-01"));

    std::fs::remove_file(tmp).ok();
}
