use crate::graph::persistence::DiscoveryGraph;
use crate::telescope::registry::{LensCategory, LensRegistry};
use crate::telescope::domain_combos;

/// Render an ASCII dashboard summarizing the NEXUS-6 engine state.
pub fn render_dashboard() -> String {
    let registry = LensRegistry::new();
    let combos = domain_combos::default_combos();
    let graph = DiscoveryGraph::new(); // fresh; in production would load from disk

    let core_count = registry.by_category(LensCategory::Core).len();
    let combo_count = combos.len();
    let ext_count = registry.by_category(LensCategory::Extended).len();
    let custom_count = registry.by_category(LensCategory::Custom).len();
    let total_lenses = registry.len();

    let node_count = graph.nodes.len();
    let edge_count = graph.edges.len();

    // Coverage: fraction of core lenses that are registered
    let target_core = 22;
    let coverage_pct = ((core_count as f64 / target_core as f64) * 100.0).min(100.0) as usize;
    let coverage_bar = progress_bar(coverage_pct, 10);

    let mut out = String::new();

    out.push_str("╔══════════════════════════════════════════════╗\n");
    out.push_str("║           NEXUS-6 Discovery Engine           ║\n");
    out.push_str("║           ════════════════════════            ║\n");
    out.push_str("╠══════════════════════════════════════════════╣\n");
    out.push_str(&format!(
        "║  Lenses: {:>2} core | {:>2} combos | {:>2} ext | {:>2} cust  ║\n",
        core_count, combo_count, ext_count, custom_count
    ));
    out.push_str(&format!(
        "║  Total:  {:>3} registered                       ║\n",
        total_lenses
    ));
    out.push_str(&format!(
        "║  Graph:  {:>4} nodes | {:>4} edges              ║\n",
        node_count, edge_count
    ));
    out.push_str(&format!(
        "║  Status: [{}] {:>3}% coverage        ║\n",
        coverage_bar, coverage_pct
    ));
    out.push_str("╠══════════════════════════════════════════════╣\n");
    out.push_str("║  n=6 Constants:                              ║\n");
    out.push_str("║    sigma=12  phi=2  tau=4  J2=24  sopfr=5    ║\n");
    out.push_str("║    sigma*phi=n*tau  <=>  n=6 (PROVED)        ║\n");
    out.push_str("╠══════════════════════════════════════════════╣\n");
    out.push_str("║  Domain Combos (10):                         ║\n");
    for combo in &combos {
        let lenses_str = combo.lenses.join("+");
        let line = format!("║    {:<14} {:<28} ║\n", combo.name, lenses_str);
        out.push_str(&line);
    }
    out.push_str("╠══════════════════════════════════════════════╣\n");
    out.push_str("║  Modules:                                    ║\n");
    out.push_str("║    telescope  graph     history   verifier   ║\n");
    out.push_str("║    encoder    gpu       materials ouroboros   ║\n");
    out.push_str("╚══════════════════════════════════════════════╝\n");

    out
}

/// Build an ASCII progress bar: e.g. "████████░░" for 80% with width=10.
fn progress_bar(pct: usize, width: usize) -> String {
    let filled = (pct * width / 100).min(width);
    let empty = width - filled;
    let mut bar = String::with_capacity(width * 3);
    for _ in 0..filled {
        bar.push('\u{2588}'); // █
    }
    for _ in 0..empty {
        bar.push('\u{2591}'); // ░
    }
    bar
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_progress_bar() {
        let bar = progress_bar(80, 10);
        assert_eq!(bar.chars().count(), 10);
        assert_eq!(bar.chars().filter(|&c| c == '\u{2588}').count(), 8);
    }

    #[test]
    fn test_render_dashboard_contains_header() {
        let out = render_dashboard();
        assert!(out.contains("NEXUS-6 Discovery Engine"));
        assert!(out.contains("sigma=12"));
    }
}
