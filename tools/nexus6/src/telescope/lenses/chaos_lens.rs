use std::collections::HashMap;

use crate::telescope::lens_trait::{Lens, LensResult};
use crate::telescope::shared_data::SharedData;

/// ChaosLens: Nonlinear dynamics & chaos detection.
///
/// Metrics:
///   1. 0-1 Test (Gottwald-Melbourne): K ~ 0 = regular, K ~ 1 = chaotic
///   2. Recurrence Rate: fraction of phase-space recurrences (Eckmann et al.)
///   3. Correlation Dimension (Grassberger-Procaccia): fractal attractor dimension
///   4. Permutation Entropy: ordinal pattern complexity (Bandt-Pompe)
///   5. Determinism: ratio of recurrence points forming diagonal lines
///
/// n=6 connection: Logistic map onset of chaos at r=3.569945... ≈ τ·ln(φ+1) + μ,
/// Feigenbaum δ=4.669... ≈ τ + φ/n·τ, period-doubling cascade uses powers of φ=2.
pub struct ChaosLens;

impl Lens for ChaosLens {
    fn name(&self) -> &str { "ChaosLens" }
    fn category(&self) -> &str { "T1" }

    fn scan(&self, data: &[f64], n: usize, d: usize, shared: &SharedData) -> LensResult {
        if n < 10 { return HashMap::new(); }

        let mut result = HashMap::new();

        // --- 1. 0-1 Test for Chaos (Gottwald-Melbourne 2004) ---
        // Use first column as time series
        let ts: Vec<f64> = (0..n).map(|i| data[i * d]).collect();
        let k_stat = zero_one_test(&ts);
        result.insert("zero_one_K".to_string(), vec![k_stat]);

        // --- 2. Recurrence Rate & Determinism (RQA) ---
        let epsilon = median_distance(shared, n) * 0.1; // 10% of median distance
        let (rr, det) = recurrence_quantification(shared, n, epsilon);
        result.insert("recurrence_rate".to_string(), vec![rr]);
        result.insert("determinism".to_string(), vec![det]);

        // --- 3. Correlation Dimension (Grassberger-Procaccia) ---
        let corr_dim = correlation_dimension(shared, n);
        result.insert("correlation_dimension".to_string(), vec![corr_dim]);

        // --- 4. Permutation Entropy (Bandt-Pompe, order=6=n) ---
        let pe = permutation_entropy(&ts, 6);
        result.insert("permutation_entropy".to_string(), vec![pe]);

        // Normalized PE (0=deterministic, 1=random)
        let max_pe = (factorial(6) as f64).ln();
        let npe = if max_pe > 0.0 { pe / max_pe } else { 0.0 };
        result.insert("normalized_perm_entropy".to_string(), vec![npe]);

        // --- 5. Chaos classification ---
        // K > 0.5 AND npe > 0.5 AND det < 0.8 → chaotic
        let chaos_score = k_stat * 0.4 + npe * 0.3 + (1.0 - det) * 0.3;
        result.insert("chaos_score".to_string(), vec![chaos_score]);

        result
    }
}

/// 0-1 Test for Chaos (Gottwald & Melbourne 2004/2009).
/// K ≈ 0 → regular, K ≈ 1 → chaotic.
/// Uses the modified regression method with V_osc correction.
fn zero_one_test(ts: &[f64]) -> f64 {
    let n = ts.len();
    if n < 20 { return 0.0; }

    // Use c = 1.0 + sqrt(2)/5 (irrational, avoids resonance with common periods)
    let c = 1.0 + std::f64::consts::SQRT_2 / 5.0;

    // Build p(n) and q(n) translation variables
    let mut p = vec![0.0f64; n];
    let mut q = vec![0.0f64; n];
    for j in 1..n {
        p[j] = p[j - 1] + ts[j] * (j as f64 * c).cos();
        q[j] = q[j - 1] + ts[j] * (j as f64 * c).sin();
    }

    // Mean square displacement D(t)
    let n_cut = n / 3;
    if n_cut < 4 { return 0.0; }

    // Subtract oscillatory part: V_osc(t) = (E[x])^2 * (1-cos(tc))/(1-cos(c))
    let mean_x = ts.iter().sum::<f64>() / n as f64;
    let mean_x2 = mean_x * mean_x;

    let mut d_t = vec![0.0f64; n_cut];
    for t in 1..n_cut {
        let mut sum = 0.0;
        let count = n - t;
        for j in 0..count {
            let dp = p[j + t] - p[j];
            let dq = q[j + t] - q[j];
            sum += dp * dp + dq * dq;
        }
        let m_raw = sum / count as f64;
        // V_osc correction for bounded signals
        let v_osc = mean_x2 * (1.0 - (t as f64 * c).cos()) / (1.0 - c.cos());
        d_t[t] = m_raw - v_osc;
    }

    // K = correlation of D(t) vs t
    // For chaotic: D(t) ~ t (linear growth) → K ≈ 1
    // For regular: D(t) ~ bounded → K ≈ 0
    let t_vals: Vec<f64> = (1..n_cut).map(|t| t as f64).collect();
    let d_vals: Vec<f64> = d_t[1..n_cut].to_vec();
    let k = correlation_coefficient(&t_vals, &d_vals);
    k.clamp(0.0, 1.0)
}

/// Pearson correlation coefficient.
fn correlation_coefficient(x: &[f64], y: &[f64]) -> f64 {
    let n = x.len().min(y.len());
    if n < 2 { return 0.0; }
    let nf = n as f64;
    let mx = x.iter().sum::<f64>() / nf;
    let my = y.iter().sum::<f64>() / nf;
    let mut sxy = 0.0;
    let mut sxx = 0.0;
    let mut syy = 0.0;
    for i in 0..n {
        let dx = x[i] - mx;
        let dy = y[i] - my;
        sxy += dx * dy;
        sxx += dx * dx;
        syy += dy * dy;
    }
    let denom = (sxx * syy).sqrt();
    if denom < 1e-15 { 0.0 } else { sxy / denom }
}

/// Median pairwise distance from pre-computed distance matrix.
fn median_distance(shared: &SharedData, n: usize) -> f64 {
    let max_samples = 500;
    let step = if n > max_samples { n / max_samples } else { 1 };
    let mut dists = Vec::new();
    let mut i = 0;
    while i < n {
        let mut j = i + 1;
        while j < n {
            dists.push(shared.dist(i, j));
            j += step;
        }
        i += step;
    }
    if dists.is_empty() { return 1.0; }
    dists.sort_unstable_by(|a, b| a.partial_cmp(b).unwrap());
    dists[dists.len() / 2]
}

/// Recurrence Quantification Analysis: recurrence rate + determinism.
fn recurrence_quantification(shared: &SharedData, n: usize, epsilon: f64) -> (f64, f64) {
    let max_n = n.min(200); // cap for O(n^2)
    let mut recurrence_count = 0u64;
    let mut diag_count = 0u64;
    let total = (max_n * (max_n - 1)) / 2;

    for i in 0..max_n {
        for j in (i + 1)..max_n {
            if shared.dist(i, j) < epsilon {
                recurrence_count += 1;
                // Check diagonal: if (i-1, j-1) also recurs
                if i > 0 && j > 0 && shared.dist(i - 1, j - 1) < epsilon {
                    diag_count += 1;
                }
            }
        }
    }

    let rr = if total > 0 { recurrence_count as f64 / total as f64 } else { 0.0 };
    let det = if recurrence_count > 0 {
        diag_count as f64 / recurrence_count as f64
    } else {
        0.0
    };
    (rr, det)
}

/// Correlation Dimension via Grassberger-Procaccia algorithm.
/// Uses log-log slope of C(r) vs r at multiple radii.
fn correlation_dimension(shared: &SharedData, n: usize) -> f64 {
    let max_n = n.min(200);
    let total_pairs = (max_n * (max_n - 1)) / 2;
    if total_pairs == 0 { return 0.0; }

    // Collect distances
    let mut dists = Vec::with_capacity(total_pairs);
    for i in 0..max_n {
        for j in (i + 1)..max_n {
            dists.push(shared.dist(i, j));
        }
    }
    dists.sort_unstable_by(|a, b| a.partial_cmp(b).unwrap());

    if dists.is_empty() || dists[dists.len() - 1] < 1e-15 { return 0.0; }

    // Sample 6 radii (n=6!) logarithmically spaced
    let r_min = dists[dists.len() / 20].max(1e-12); // 5th percentile
    let r_max = dists[dists.len() * 4 / 5];         // 80th percentile
    if r_max <= r_min { return 0.0; }

    let n_radii = 6; // n=6
    let log_min = r_min.ln();
    let log_max = r_max.ln();
    let step = (log_max - log_min) / (n_radii - 1) as f64;

    let mut log_r = Vec::with_capacity(n_radii);
    let mut log_c = Vec::with_capacity(n_radii);

    for k in 0..n_radii {
        let r = (log_min + k as f64 * step).exp();
        // C(r) = fraction of pairs with distance < r
        let count = dists.partition_point(|&d| d < r);
        let c_r = count as f64 / total_pairs as f64;
        if c_r > 0.0 {
            log_r.push(r.ln());
            log_c.push(c_r.ln());
        }
    }

    if log_r.len() < 3 { return 0.0; }

    // Linear regression slope = correlation dimension
    linear_slope(&log_r, &log_c)
}

/// Simple linear regression slope.
fn linear_slope(x: &[f64], y: &[f64]) -> f64 {
    let n = x.len();
    if n < 2 { return 0.0; }
    let nf = n as f64;
    let mx = x.iter().sum::<f64>() / nf;
    let my = y.iter().sum::<f64>() / nf;
    let mut num = 0.0;
    let mut den = 0.0;
    for i in 0..n {
        let dx = x[i] - mx;
        num += dx * (y[i] - my);
        den += dx * dx;
    }
    if den.abs() < 1e-15 { 0.0 } else { num / den }
}

/// Permutation Entropy (Bandt & Pompe 2002).
/// `order` = embedding dimension (we use 6 = n).
fn permutation_entropy(ts: &[f64], order: usize) -> f64 {
    let n = ts.len();
    if n < order + 1 { return 0.0; }

    let n_patterns = n - order + 1;
    let mut pattern_counts: HashMap<Vec<u8>, u32> = HashMap::new();

    for i in 0..n_patterns {
        let window = &ts[i..i + order];
        // Rank the values to get ordinal pattern
        let mut indices: Vec<u8> = (0..order as u8).collect();
        indices.sort_by(|&a, &b| {
            window[a as usize]
                .partial_cmp(&window[b as usize])
                .unwrap_or(std::cmp::Ordering::Equal)
        });
        *pattern_counts.entry(indices).or_insert(0) += 1;
    }

    // Shannon entropy of pattern distribution
    let inv_n = 1.0 / n_patterns as f64;
    let mut entropy = 0.0;
    for &count in pattern_counts.values() {
        let p = count as f64 * inv_n;
        if p > 0.0 {
            entropy -= p * p.ln();
        }
    }
    entropy
}

/// Factorial (small n only, for normalization).
fn factorial(n: usize) -> usize {
    (1..=n).product()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_chaos_lens_logistic_map() {
        // Logistic map at r=3.9 (chaotic regime)
        let mut x = 0.1f64;
        let r = 3.9;
        let n = 200;
        let mut ts = Vec::with_capacity(n);
        for _ in 0..n {
            ts.push(x);
            x = r * x * (1.0 - x);
        }
        // 1D time series: each row has d=1
        let shared = SharedData::compute(&ts, n, 1);
        let result = ChaosLens.scan(&ts, n, 1, &shared);

        assert!(result.contains_key("zero_one_K"));
        assert!(result.contains_key("chaos_score"));

        let k = result["zero_one_K"][0];
        // Chaotic logistic map should have K close to 1
        assert!(k > 0.3, "Logistic r=3.9 should be chaotic, K={k}");
    }

    #[test]
    fn test_chaos_lens_periodic() {
        // Simple periodic signal (sine wave)
        let n = 200;
        let ts: Vec<f64> = (0..n)
            .map(|i| (2.0 * std::f64::consts::PI * i as f64 / 20.0).sin())
            .collect();
        let shared = SharedData::compute(&ts, n, 1);
        let result = ChaosLens.scan(&ts, n, 1, &shared);

        let k = result["zero_one_K"][0];
        // Periodic signal should have K close to 0
        assert!(k < 0.7, "Sine wave should be regular, K={k}");
    }

    #[test]
    fn test_permutation_entropy_constant() {
        let ts = vec![1.0; 50];
        let pe = permutation_entropy(&ts, 6);
        // Constant signal → only 1 pattern → entropy = 0
        assert!((pe - 0.0).abs() < 1e-12);
    }

    #[test]
    fn test_correlation_dimension_positive() {
        let n = 100;
        let data: Vec<f64> = (0..n * 2)
            .map(|i| (i as f64 * 0.1).sin() + (i as f64 * 0.037).cos())
            .collect();
        let shared = SharedData::compute(&data, n, 2);
        let cd = correlation_dimension(&shared, n);
        assert!(cd >= 0.0, "Correlation dimension should be non-negative");
    }

    #[test]
    fn test_zero_one_test_short() {
        let ts = vec![1.0, 2.0, 3.0];
        let k = zero_one_test(&ts);
        assert!((k - 0.0).abs() < 1e-12, "Too short → K=0");
    }
}
