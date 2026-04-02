/// A pre-defined combination of lenses optimised for a specific analysis domain.
#[derive(Debug, Clone)]
pub struct DomainCombo {
    pub name: String,
    pub lenses: Vec<String>,
    pub target_domains: Vec<String>,
}

/// Return the 10 default domain combinations from the telescope specification.
///
/// Cross-verification rule (CLAUDE.md):
///   3+ lenses agree = Candidate, 7+ = HighConfidence, 12+ = Confirmed.
///
/// These combos are intentionally small (2-4 lenses each) so that multiple
/// combos can be stacked when broader coverage is needed.
pub fn default_combos() -> Vec<DomainCombo> {
    vec![
        DomainCombo {
            name: "default".into(),
            lenses: vec!["consciousness".into(), "topology".into(), "causal".into()],
            target_domains: vec!["general".into(), "exploration".into()],
        },
        DomainCombo {
            name: "stability".into(),
            lenses: vec!["stability".into(), "boundary".into(), "thermo".into()],
            target_domains: vec!["energy".into(), "plasma".into(), "control".into()],
        },
        DomainCombo {
            name: "structure".into(),
            lenses: vec!["network".into(), "topology".into(), "recursion".into()],
            target_domains: vec!["chip".into(), "biology".into(), "software".into()],
        },
        DomainCombo {
            name: "timeseries".into(),
            lenses: vec![
                "memory".into(),
                "wave".into(),
                "causal".into(),
                "multiscale".into(),
            ],
            target_domains: vec!["signal".into(), "finance".into(), "audio".into()],
        },
        DomainCombo {
            name: "scale_invariant".into(),
            lenses: vec!["multiscale".into(), "scale".into(), "recursion".into()],
            target_domains: vec!["cosmology".into(), "network".into(), "fractal".into()],
        },
        DomainCombo {
            name: "symmetry_invariant".into(),
            lenses: vec!["mirror".into(), "topology".into(), "quantum".into()],
            target_domains: vec!["physics".into(), "chemistry".into(), "materials".into()],
        },
        DomainCombo {
            name: "power_law".into(),
            lenses: vec!["scale".into(), "evolution".into(), "thermo".into()],
            target_domains: vec!["network".into(), "biology".into(), "economics".into()],
        },
        DomainCombo {
            name: "causal_relations".into(),
            lenses: vec!["causal".into(), "info".into(), "em".into()],
            target_domains: vec!["ai".into(), "neuroscience".into(), "economics".into()],
        },
        DomainCombo {
            name: "geometric".into(),
            lenses: vec!["ruler".into(), "triangle".into(), "compass".into()],
            target_domains: vec!["geometry".into(), "chip".into(), "robotics".into()],
        },
        DomainCombo {
            name: "quantum_deep".into(),
            lenses: vec![
                "quantum".into(),
                "quantum_microscope".into(),
                "em".into(),
            ],
            target_domains: vec!["quantum".into(), "materials".into(), "crypto".into()],
        },
    ]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_default_combo_count() {
        let combos = default_combos();
        assert_eq!(combos.len(), 10, "Must have exactly 10 domain combos");
    }

    #[test]
    fn test_default_combo_names_unique() {
        let combos = default_combos();
        let mut names: Vec<&str> = combos.iter().map(|c| c.name.as_str()).collect();
        names.sort();
        names.dedup();
        assert_eq!(names.len(), 10, "All 10 combo names must be unique");
    }
}
