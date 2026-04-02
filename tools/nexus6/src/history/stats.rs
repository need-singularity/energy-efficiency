use std::collections::HashMap;
use super::recorder::ScanRecord;

#[derive(Debug, Clone)]
pub struct LensStats {
    pub used: usize,
    pub contributed: usize,
    pub hit_rate: f64,
}

#[derive(Debug, Clone)]
pub struct DomainStats {
    pub total_scans: usize,
    pub total_discoveries: usize,
    pub lens_stats: HashMap<String, LensStats>,
}

/// Compute aggregate statistics for a set of scan records in one domain.
pub fn compute_domain_stats(records: &[ScanRecord]) -> DomainStats {
    let total_scans = records.len();
    let total_discoveries: usize = records.iter().map(|r| r.discoveries.len()).sum();

    let mut used_count: HashMap<String, usize> = HashMap::new();
    let mut contributed_count: HashMap<String, usize> = HashMap::new();

    for record in records {
        for lens in &record.lenses_used {
            *used_count.entry(lens.clone()).or_insert(0) += 1;
        }

        // A lens "contributed" if it was used in a scan that produced discoveries
        if !record.discoveries.is_empty() {
            for lens in &record.lenses_used {
                *contributed_count.entry(lens.clone()).or_insert(0) += 1;
            }
        }
    }

    let mut lens_stats = HashMap::new();
    for (lens, used) in &used_count {
        let contributed = contributed_count.get(lens).copied().unwrap_or(0);
        let hit_rate = if *used > 0 {
            contributed as f64 / *used as f64
        } else {
            0.0
        };
        lens_stats.insert(
            lens.clone(),
            LensStats {
                used: *used,
                contributed,
                hit_rate,
            },
        );
    }

    DomainStats {
        total_scans,
        total_discoveries,
        lens_stats,
    }
}

/// Compute lens affinity: for each pair of lenses, how often they co-occur
/// in scans that produce discoveries, normalized by total discovery-producing scans.
pub fn compute_lens_affinity(records: &[ScanRecord]) -> HashMap<(String, String), f64> {
    let discovery_records: Vec<&ScanRecord> = records
        .iter()
        .filter(|r| !r.discoveries.is_empty())
        .collect();

    let total = discovery_records.len();
    if total == 0 {
        return HashMap::new();
    }

    let mut pair_counts: HashMap<(String, String), usize> = HashMap::new();

    for record in &discovery_records {
        let lenses = &record.lenses_used;
        for i in 0..lenses.len() {
            for j in (i + 1)..lenses.len() {
                let (a, b) = if lenses[i] <= lenses[j] {
                    (lenses[i].clone(), lenses[j].clone())
                } else {
                    (lenses[j].clone(), lenses[i].clone())
                };
                *pair_counts.entry((a, b)).or_insert(0) += 1;
            }
        }
    }

    pair_counts
        .into_iter()
        .map(|(pair, count)| (pair, count as f64 / total as f64))
        .collect()
}
