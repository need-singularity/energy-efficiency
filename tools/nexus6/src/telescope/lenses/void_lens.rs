use std::collections::HashMap;

use crate::telescope::lens_trait::{Lens, LensResult};
use crate::telescope::shared_data::SharedData;

/// VoidLens: k-NN density estimation to find low-density regions
/// surrounded by high-density regions (cosmic void analogy).
///
/// Algorithm:
///   1. For each point, compute k-NN density (k = sqrt(N))
///   2. Threshold = 0.3 * mean_density
///   3. Points below threshold with neighbors above threshold = void centers
pub struct VoidLens;

impl Lens for VoidLens {
    fn name(&self) -> &str {
        "VoidLens"
    }

    fn category(&self) -> &str {
        "T0"
    }

    fn scan(&self, _data: &[f64], n: usize, d: usize, shared: &SharedData) -> LensResult {
        if n < 3 {
            return HashMap::new();
        }

        let k = ((n as f64).sqrt().ceil() as usize).max(1).min(n - 1);

        // Compute k-NN density for each point
        let densities: Vec<f64> = (0..n)
            .map(|i| {
                let mut dists: Vec<f64> = (0..n)
                    .filter(|&j| j != i)
                    .map(|j| shared.dist(i, j))
                    .collect();
                dists.sort_by(|a, b| a.partial_cmp(b).unwrap_or(std::cmp::Ordering::Equal));
                let knn_dist = dists[k.min(dists.len()) - 1];
                if knn_dist > 0.0 {
                    1.0 / knn_dist
                } else {
                    f64::MAX
                }
            })
            .collect();

        let mean_density = densities.iter().sum::<f64>() / n as f64;
        let threshold = 0.3 * mean_density;

        // Find void centers: low density points whose neighbors are high density
        let mut void_centers = Vec::new();
        let mut void_scores = Vec::new();

        for i in 0..n {
            if densities[i] < threshold {
                // Check if surrounded by higher-density points
                let mut neighbor_dists: Vec<(usize, f64)> = (0..n)
                    .filter(|&j| j != i)
                    .map(|j| (j, shared.dist(i, j)))
                    .collect();
                neighbor_dists
                    .sort_by(|a, b| a.1.partial_cmp(&b.1).unwrap_or(std::cmp::Ordering::Equal));

                let nearest_k = neighbor_dists.iter().take(k);
                let avg_neighbor_density: f64 =
                    nearest_k.map(|(j, _)| densities[*j]).sum::<f64>() / k as f64;

                // Void = low density center with high density surroundings
                if avg_neighbor_density > mean_density {
                    // Score = ratio of neighbor density to own density
                    let score = if densities[i] > 0.0 {
                        avg_neighbor_density / densities[i]
                    } else {
                        0.0
                    };
                    // Store center coordinates (flattened index in original data)
                    void_centers.push(i as f64);
                    void_scores.push(score);
                }
            }
        }

        // Also try midpoints between clusters as potential void centers
        // Find the point with lowest density as primary void indicator
        if void_centers.is_empty() && n > 2 {
            // Fallback: find the gap region by looking at largest distance gaps
            let mut all_dists: Vec<(usize, usize, f64)> = Vec::new();
            for i in 0..n {
                for j in (i + 1)..n {
                    all_dists.push((i, j, shared.dist(i, j)));
                }
            }
            all_dists.sort_by(|a, b| b.2.partial_cmp(&a.2).unwrap_or(std::cmp::Ordering::Equal));

            // The midpoint of the largest gap is a void center candidate
            if let Some(&(pi, pj, dist)) = all_dists.first() {
                let _ = (pi, pj, d); // midpoint would be computed from data
                void_centers.push(pi as f64); // approximate: use one endpoint
                void_scores.push(dist);
            }
        }

        let mut result = HashMap::new();
        result.insert("void_centers".to_string(), void_centers);
        result.insert("void_scores".to_string(), void_scores);
        result
    }
}
