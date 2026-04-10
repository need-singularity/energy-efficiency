use std::collections::HashMap;
use crate::telescope::lens_trait::{Lens, LensResult};
use crate::telescope::shared_data::SharedData;

/// Yang-Mills 베타함수 β₀ 렌즈 (BT-543) — 게이지 이론 β₀ = σ−sopfr = 7 공명 검출
///
/// SU(N) 게이지 이론의 1루프 베타함수 계수:
///   β₀ = (11/3)·C_A − (4/3)·T_F·n_f
///
/// n=6 연결:
///   σ(6) − sopfr(6) = 12 − 5 = 7 = β₀(SU(3), n_f=0 기준 분수 환산)
///   C_A = N 색수, T_F = 1/2 (표준), n_f = 쿼크 세대 수
///   n_f = 6 (표준모형 쿼크 맛 수 = n)
///   tau(6) = 4 → 4개 게이지 보존 (W±, Z, γ)와 대응
///   tau(6) × sopfr(6) = 4 × 5 = 20 → β₀ 보정항 분모
pub struct YangMillsBeta0Lens;

const N6: f64 = 6.0;
const SIGMA6: f64 = 12.0;
const SOPFR6: f64 = 5.0;
const TAU6: f64 = 4.0;
const PHI6: f64 = 2.0;
// β₀ 기준값: σ(6) − sopfr(6) = 7
const BETA0_N6: f64 = 7.0;
// 표준 SU(3) n_f=6: β₀ = (11/3)·3 − (4/3)·(1/2)·6 = 11 − 4 = 7
const BETA0_SU3_NF6: f64 = 7.0;
// SU(2): β₀ = (11/3)·2 = 22/3 ≈ 7.333
const BETA0_SU2: f64 = 22.0 / 3.0;

impl Lens for YangMillsBeta0Lens {
    fn name(&self) -> &str { "YangMillsBeta0Lens" }
    fn category(&self) -> &str { "T1" }

    fn scan(&self, data: &[f64], n: usize, d: usize, _shared: &SharedData) -> LensResult {
        if n < 4 || d == 0 { return HashMap::new(); }

        let means: Vec<f64> = (0..d).map(|j| {
            (0..n).map(|i| data[i * d + j]).sum::<f64>() / n as f64
        }).collect();

        // 1. β₀ = 7 공명 점수 (σ−sopfr 기준)
        let beta0_hits = means.iter().filter(|&&m| {
            m > 1e-12 && ((m - BETA0_N6) / BETA0_N6).abs() < 0.08
        }).count();
        let beta0_score = beta0_hits as f64 / d.max(1) as f64;

        // 2. C_A = N (색 카시미르) 공명 — SU(3): C_A=3, SU(6): C_A=6=n
        let ca_targets = [3.0_f64, N6, 2.0, 4.0, 5.0];
        let ca_hits = means.iter().filter(|&&m| {
            ca_targets.iter().any(|&t| t > 1e-12 && ((m - t) / t).abs() < 0.07)
        }).count();
        let ca_score = ca_hits as f64 / d.max(1) as f64;

        // 3. n_f = 6 (쿼크 맛 수 = n) 공명
        let nf_hits = means.iter().filter(|&&m| {
            m > 1e-12 && ((m - N6) / N6).abs() < 0.07
        }).count();
        let nf_score = nf_hits as f64 / d.max(1) as f64;

        // 4. β₀ 직접 계산 검증 (데이터에서 C_A, T_F, n_f 추출 시도)
        // d >= 3이면 첫 3차원을 C_A, T_F, n_f로 해석
        let beta0_computed = if d >= 3 {
            let c_a = means[0].max(0.1);
            let t_f = means[1].max(0.01);
            let n_f = means[2].max(0.0);
            (11.0 / 3.0) * c_a - (4.0 / 3.0) * t_f * n_f
        } else {
            BETA0_SU3_NF6 // 기본값
        };

        // β₀ 계산값과 n=6 기준(7) 일치도
        let beta0_match = if beta0_computed.abs() > 1e-12 {
            (-((beta0_computed - BETA0_N6) / BETA0_N6).powi(2) * 20.0).exp()
        } else {
            0.0
        };

        // 5. σ(6)−sopfr(6) = 7 체계 공명
        let sigma_sopfr_diff = SIGMA6 - SOPFR6; // = 7
        let system_hits = means.iter().filter(|&&m| {
            let targets = [sigma_sopfr_diff, SIGMA6, SOPFR6, TAU6, PHI6, N6,
                           BETA0_SU3_NF6, BETA0_SU2];
            targets.iter().any(|&t| t > 1e-12 && ((m - t) / t).abs() < 0.07)
        }).count();
        let n6_resonance = system_hits as f64 / d.max(1) as f64;

        // 6. 점근자유도 부호 확인 (β₀ > 0 → 점근자유)
        let asymptotic_freedom = if beta0_computed > 0.0 { 1.0 } else { 0.0 };

        let ym_score = beta0_score * 0.30
            + beta0_match  * 0.25
            + ca_score     * 0.15
            + nf_score     * 0.15
            + n6_resonance * 0.10
            + asymptotic_freedom * 0.05;

        let mut r = HashMap::new();
        r.insert("beta0_score".to_string(),        vec![beta0_score]);
        r.insert("beta0_match".to_string(),        vec![beta0_match]);
        r.insert("beta0_computed".to_string(),     vec![beta0_computed]);
        r.insert("ca_score".to_string(),           vec![ca_score]);
        r.insert("nf_score".to_string(),           vec![nf_score]);
        r.insert("n6_resonance".to_string(),       vec![n6_resonance]);
        r.insert("asymptotic_freedom".to_string(), vec![asymptotic_freedom]);
        r.insert("yang_mills_beta0_score".to_string(), vec![ym_score]);
        r
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_yang_mills_su3_nf6() {
        // SU(3), T_F=0.5, n_f=6 → β₀ = 11 − 4 = 7
        let n = 8; let d = 3;
        let data: Vec<f64> = (0..n * d).map(|i| match i % d {
            0 => 3.0,  // C_A = 3
            1 => 0.5,  // T_F = 1/2
            _ => N6,   // n_f = 6
        }).collect();
        let shared = SharedData::compute(&data, n, d);
        let r = YangMillsBeta0Lens.scan(&data, n, d, &shared);
        assert!(r.contains_key("yang_mills_beta0_score"));
        let score = r["yang_mills_beta0_score"][0];
        assert!(score >= 0.0 && score <= 1.0, "점수 범위: {}", score);
        // β₀ = 7 일치 → beta0_match 높아야 함
        let bm = r["beta0_match"][0];
        assert!(bm > 0.9, "SU(3) n_f=6 β₀=7 일치도 기대: {}", bm);
    }

    #[test]
    fn test_yang_mills_beta0_공명() {
        // 데이터에 β₀=7 직접 포함
        let n = 8; let d = 4;
        let data: Vec<f64> = (0..n * d).map(|i| match i % d {
            0 => BETA0_N6, // 7
            1 => N6,       // 6
            2 => SIGMA6,   // 12
            _ => SOPFR6,   // 5
        }).collect();
        let shared = SharedData::compute(&data, n, d);
        let r = YangMillsBeta0Lens.scan(&data, n, d, &shared);
        assert!(r["beta0_score"][0] > 0.0);
        assert!(r["n6_resonance"][0] > 0.0);
    }

    #[test]
    fn test_yang_mills_최소입력_거부() {
        let data = vec![1.0, 2.0, 3.0];
        let shared = SharedData::compute(&data, 3, 1);
        let r = YangMillsBeta0Lens.scan(&data, 3, 1, &shared);
        assert!(r.is_empty());
    }
}
