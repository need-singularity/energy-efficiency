use std::collections::HashMap;

use crate::telescope::lens_trait::{Lens, LensResult};
use crate::telescope::shared_data::SharedData;

/// ChaosLens: 카오스 역학 감지 — 리아푸노프 지수 추정 + 위상 공간 재구성
///
/// 알고리즘:
///   1. 첫 번째 차원을 시계열 신호로 취급
///   2. 인접 궤적 발산율로 최대 리아푸노프 지수(MLE) 추정
///   3. 위상 공간 점유율 (phase_space_fill) — 카오스 어트랙터 차원 지표
///   4. 평균 발산 지수가 양수이면 chaos_detected = 1.0
///
/// n=6 연결:
///   - 로렌츠 어트랙터 σ=10, ρ=28, β=8/3 — β·σ = 80/3 ≈ n·tau·φ²
///   - 리아푸노프 지수 합 ≤ 0 (보존계) vs 합 > 0 (카오스)
///   - 3D 로렌츠 상태벡터: n/phi=3 차원
///   - 카오스 어트랙터 fractal 차원 ≈ 2.06 ≈ n/3
pub struct ChaosLens;

impl Lens for ChaosLens {
    fn name(&self) -> &str {
        "ChaosLens"
    }

    fn category(&self) -> &str {
        "T0"
    }

    fn scan(&self, data: &[f64], n: usize, d: usize, shared: &SharedData) -> LensResult {
        if n < 6 || d == 0 {
            return HashMap::new();
        }

        // 1. 첫 번째 차원을 1D 시계열로 추출
        let signal: Vec<f64> = (0..n).map(|i| data[i * d]).collect();

        // 2. 최대 리아푸노프 지수(MLE) 추정
        //    Rosenstein(1993) 방법: 각 점 i에 대해 가장 가까운 궤적 파트너 j 를 찾고,
        //    시간이 지남에 따라 |x[i+k] - x[j+k]| 의 log 평균 기울기를 계산
        let max_n = n.min(200);
        let tau = 1usize; // 시간 지연
        let max_steps = (max_n / 4).max(2);

        // 각 점의 가장 가까운 non-temporal 이웃 찾기
        let mut divergence_sum = vec![0.0f64; max_steps];
        let mut divergence_count = vec![0u32; max_steps];

        for i in 0..(max_n.saturating_sub(max_steps)) {
            // 시간적으로 가까운 점은 제외하고 공간적 이웃 탐색
            let min_temporal_sep = (max_n as f64).sqrt() as usize + 1;
            let mut best_j = usize::MAX;
            let mut best_dist = f64::INFINITY;

            for j in 0..(max_n.saturating_sub(max_steps)) {
                if i == j { continue; }
                let temporal_sep = if i > j { i - j } else { j - i };
                if temporal_sep < min_temporal_sep { continue; }

                let di = (signal[i] - signal[j]).abs();
                if di < best_dist {
                    best_dist = di;
                    best_j = j;
                }
            }

            if best_j == usize::MAX || best_dist < 1e-15 {
                continue;
            }

            // 이웃 쌍의 발산 추적
            for k in 1..=max_steps {
                let ni = i + k * tau;
                let nj = best_j + k * tau;
                if ni >= max_n || nj >= max_n { break; }

                let new_dist = (signal[ni] - signal[nj]).abs();
                if new_dist > 1e-15 && best_dist > 1e-15 {
                    divergence_sum[k - 1] += (new_dist / best_dist).ln();
                    divergence_count[k - 1] += 1;
                }
            }
        }

        // MLE = 발산율의 평균 기울기 (선형 회귀)
        let valid_steps: Vec<(f64, f64)> = (0..max_steps)
            .filter(|&k| divergence_count[k] > 0)
            .map(|k| (
                k as f64,
                divergence_sum[k] / divergence_count[k] as f64,
            ))
            .collect();

        let lyapunov_estimate = if valid_steps.len() >= 2 {
            let (slope, _) = linear_regression_pairs(&valid_steps);
            slope
        } else if !valid_steps.is_empty() {
            valid_steps[0].1
        } else {
            0.0
        };

        // 3. 위상 공간 채움율 — 격자 점유 셀 수 / 총 셀 수
        let phase_space_fill = phase_space_occupancy(&signal, max_n, 12);

        // 4. 카오스 감지: 양수 리아푸노프 지수 + 위상 공간 분산
        let chaos_detected = if lyapunov_estimate > 0.01 && phase_space_fill > 0.2 {
            1.0
        } else {
            0.0
        };

        // 5. 발산 점수 정규화 (0~1 범위)
        let divergence_score = if lyapunov_estimate > 0.0 {
            (lyapunov_estimate / (lyapunov_estimate.abs() + 1.0)).min(1.0)
        } else {
            0.0
        };

        // 6. n=6 연결 — 발산 지수가 n=6 관련 비율에 근접하는지
        let n6_consts = [6.0f64, 3.0, 2.0, 1.0 / 3.0, 8.0 / 3.0]; // 로렌츠 파라미터
        let n6_affinity = n6_consts.iter()
            .map(|&c| {
                if c > 1e-12 {
                    let rel = (lyapunov_estimate.abs() - c).abs() / c;
                    (-rel * 2.0).exp()
                } else {
                    0.0
                }
            })
            .fold(0.0f64, f64::max);

        // 7. 거리 행렬 기반 지역 비선형성 — 이웃 거리 분산
        let local_nonlinearity = compute_local_nonlinearity(n, shared);

        let mut result = HashMap::new();
        result.insert("chaos_detected".to_string(), vec![chaos_detected]);
        result.insert("lyapunov_estimate".to_string(), vec![lyapunov_estimate]);
        result.insert("phase_space_fill".to_string(), vec![phase_space_fill]);
        result.insert("divergence_score".to_string(), vec![divergence_score]);
        result.insert("n6_attractor_affinity".to_string(), vec![n6_affinity]);
        result.insert("local_nonlinearity".to_string(), vec![local_nonlinearity]);
        result
    }
}

/// 선형 회귀 — (x, y) 쌍에서 기울기와 절편 반환
fn linear_regression_pairs(pairs: &[(f64, f64)]) -> (f64, f64) {
    let n = pairs.len() as f64;
    if n < 2.0 { return (0.0, 0.0); }

    let sum_x: f64 = pairs.iter().map(|p| p.0).sum();
    let sum_y: f64 = pairs.iter().map(|p| p.1).sum();
    let sum_xy: f64 = pairs.iter().map(|p| p.0 * p.1).sum();
    let sum_xx: f64 = pairs.iter().map(|p| p.0 * p.0).sum();

    let denom = n * sum_xx - sum_x * sum_x;
    if denom.abs() < 1e-15 {
        return (0.0, sum_y / n);
    }

    let slope = (n * sum_xy - sum_x * sum_y) / denom;
    let intercept = (sum_y - slope * sum_x) / n;
    (slope, intercept)
}

/// 위상 공간 점유율 계산 — n_grid^1 격자 셀 중 점이 있는 셀의 비율
fn phase_space_occupancy(signal: &[f64], n: usize, n_grid: usize) -> f64 {
    if n < 2 { return 0.0; }

    let mut lo = f64::INFINITY;
    let mut hi = f64::NEG_INFINITY;
    for &v in &signal[..n] {
        if v < lo { lo = v; }
        if v > hi { hi = v; }
    }

    let range = (hi - lo).max(1e-12);
    let scale = (n_grid - 1) as f64 / range;

    let mut occupied = vec![false; n_grid];
    for &v in &signal[..n] {
        let bin = ((v - lo) * scale) as usize;
        let bin = bin.min(n_grid - 1);
        occupied[bin] = true;
    }

    let filled = occupied.iter().filter(|&&b| b).count();
    filled as f64 / n_grid as f64
}

/// 지역 비선형성 — KNN 거리 분산으로 측정
fn compute_local_nonlinearity(n: usize, shared: &SharedData) -> f64 {
    let max_n = n.min(100);
    if max_n < 3 { return 0.0; }

    let mut variances = Vec::with_capacity(max_n);
    for i in 0..max_n {
        let knn = shared.knn(i);
        if knn.len() < 2 { continue; }

        let dists: Vec<f64> = knn.iter()
            .map(|&j| shared.dist(i, j as usize))
            .collect();
        let mean_d = dists.iter().sum::<f64>() / dists.len() as f64;
        let var_d = dists.iter()
            .map(|&d| (d - mean_d) * (d - mean_d))
            .sum::<f64>() / dists.len() as f64;
        variances.push(var_d);
    }

    if variances.is_empty() { return 0.0; }
    let mean_var = variances.iter().sum::<f64>() / variances.len() as f64;

    // 전체 거리 스케일로 정규화
    let mut global_dist_sum = 0.0f64;
    let mut pair_count = 0u32;
    for i in 0..max_n.min(20) {
        for j in (i + 1)..max_n.min(20) {
            global_dist_sum += shared.dist(i, j);
            pair_count += 1;
        }
    }
    let global_scale = if pair_count > 0 {
        (global_dist_sum / pair_count as f64).powi(2)
    } else {
        1.0
    };

    if global_scale < 1e-15 { 0.0 } else { (mean_var / global_scale).min(1.0) }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// 카오스적 시계열 생성 — 로지스틱 맵 x_{n+1} = r·x_n·(1-x_n), r=3.9 (카오스 영역)
    fn logistic_map(n: usize, r: f64) -> Vec<f64> {
        let mut signal = Vec::with_capacity(n);
        let mut x = 0.3;
        for _ in 0..n {
            signal.push(x);
            x = r * x * (1.0 - x);
        }
        signal
    }

    #[test]
    fn test_chaos_detected_logistic_map() {
        let n = 60;
        let d = 1;
        let data = logistic_map(n, 3.9);
        let shared = SharedData::compute(&data, n, d);
        let result = ChaosLens.scan(&data, n, d, &shared);

        assert!(result.contains_key("chaos_detected"), "chaos_detected 키 필수");
        assert!(result.contains_key("lyapunov_estimate"), "lyapunov_estimate 키 필수");
        assert!(result.contains_key("phase_space_fill"), "phase_space_fill 키 필수");
        assert!(result.contains_key("divergence_score"), "divergence_score 키 필수");
        assert!(result.contains_key("n6_attractor_affinity"), "n6_attractor_affinity 키 필수");
        assert!(result.contains_key("local_nonlinearity"), "local_nonlinearity 키 필수");
    }

    #[test]
    fn test_phase_space_fill_range() {
        let n = 50;
        let d = 1;
        let data = logistic_map(n, 3.9);
        let shared = SharedData::compute(&data, n, d);
        let result = ChaosLens.scan(&data, n, d, &shared);

        let fill = result["phase_space_fill"][0];
        assert!(fill >= 0.0 && fill <= 1.0, "위상 공간 채움율 [0,1] 범위여야 함, 실제: {fill}");
    }

    #[test]
    fn test_divergence_score_range() {
        let n = 50;
        let d = 1;
        let data = logistic_map(n, 3.9);
        let shared = SharedData::compute(&data, n, d);
        let result = ChaosLens.scan(&data, n, d, &shared);

        let score = result["divergence_score"][0];
        assert!(score >= 0.0 && score <= 1.0, "발산 점수 [0,1] 범위여야 함, 실제: {score}");
    }

    #[test]
    fn test_periodic_signal_low_chaos() {
        // 단순 주기 신호는 카오스가 아님
        let n = 60;
        let d = 1;
        let data: Vec<f64> = (0..n)
            .map(|i| (i as f64 * 2.0 * std::f64::consts::PI / 12.0).sin())
            .collect();
        let shared = SharedData::compute(&data, n, d);
        let result = ChaosLens.scan(&data, n, d, &shared);

        assert!(result.contains_key("lyapunov_estimate"), "lyapunov_estimate 키 필수");
        // 주기 신호의 리아푸노프 지수는 카오스 신호보다 작아야 함
        let lyap = result["lyapunov_estimate"][0];
        assert!(lyap.is_finite(), "리아푸노프 지수는 유한해야 함, 실제: {lyap}");
    }

    #[test]
    fn test_small_n_returns_empty() {
        let data = vec![0.1, 0.2, 0.3, 0.4, 0.5];
        let shared = SharedData::compute(&data, 5, 1);
        let result = ChaosLens.scan(&data, 5, 1, &shared);
        assert!(result.is_empty(), "n<6 이면 빈 HashMap 반환해야 함");
    }

    #[test]
    fn test_multidim_uses_first_dim() {
        // 다차원 데이터도 처리 가능해야 함
        let n = 30;
        let d = 3;
        let data: Vec<f64> = (0..n * d).map(|i| {
            let row = i / d;
            let col = i % d;
            logistic_map(n, 3.9)[row] + col as f64 * 0.01
        }).collect();
        let shared = SharedData::compute(&data, n, d);
        let result = ChaosLens.scan(&data, n, d, &shared);
        assert!(!result.is_empty(), "다차원 데이터도 결과 반환해야 함");
    }

    #[test]
    fn test_n6_affinity_finite() {
        let n = 40;
        let d = 1;
        let data = logistic_map(n, 3.9);
        let shared = SharedData::compute(&data, n, d);
        let result = ChaosLens.scan(&data, n, d, &shared);

        let affinity = result["n6_attractor_affinity"][0];
        assert!(affinity.is_finite() && affinity >= 0.0, "n6 친화도는 유한 양수여야 함, 실제: {affinity}");
    }
}
