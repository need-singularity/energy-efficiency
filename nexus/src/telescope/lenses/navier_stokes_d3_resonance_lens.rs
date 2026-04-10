use std::collections::HashMap;
use crate::telescope::lens_trait::{Lens, LensResult};
use crate::telescope::shared_data::SharedData;

/// 나비에-스토크스 d=3 3중 공명 렌즈 (BT-544) — NS 방정식 d=3에서 n=6 차원 공명 검출
///
/// d차원 유체에서 텐서 차원 공식:
///   dim Sym²(ℝᵈ) = d(d+1)/2  → d=3: 6 = n
///   dim Λ²(ℝᵈ)  = d(d-1)/2  → d=3: 3 = sopfr−2
///   와도(vorticity) 벡터 dim = d=3 (3차원 전용)
///
/// n=6 3중 공명 (d=3):
///   응력텐서 독립 성분 수 = 6 = n
///   이방성 응력 성분 = 5 = sopfr(6)
///   와도 성분 = 3 = tau(6)−1
///   에너지 캐스케이드 스케일 수 (Kolmogorov) ≈ 6
///
/// 연결: σ(6)=12 → 점성 계수·밀도 쌍 12쌍, phi(6)=2 → 2차 편미분
pub struct NavierStokesD3ResonanceLens;

const N6: f64 = 6.0;
const SIGMA6: f64 = 12.0;
const SOPFR6: f64 = 5.0;
const TAU6: f64 = 4.0;
const PHI6: f64 = 2.0;
// d=3 기준 텐서 차원
const DIM_SYM2_D3: f64 = 6.0;   // d(d+1)/2 = 3×4/2 = 6 = n
const DIM_LAMBDA2_D3: f64 = 3.0; // d(d-1)/2 = 3×2/2 = 3
const VORTICITY_DIM: f64 = 3.0;  // d=3 전용
// Kolmogorov -5/3 지수 (에너지 스펙트럼)
const KOLMOGOROV_EXP: f64 = 5.0 / 3.0;

impl Lens for NavierStokesD3ResonanceLens {
    fn name(&self) -> &str { "NavierStokesD3ResonanceLens" }
    fn category(&self) -> &str { "T1" }

    fn scan(&self, data: &[f64], n: usize, d: usize, _shared: &SharedData) -> LensResult {
        if n < 4 || d == 0 { return HashMap::new(); }

        let means: Vec<f64> = (0..d).map(|j| {
            (0..n).map(|i| data[i * d + j]).sum::<f64>() / n as f64
        }).collect();

        // 1. dim Sym² = d(d+1)/2 = n=6 공명
        let sym2_hits = means.iter().filter(|&&m| {
            m > 1e-12 && ((m - DIM_SYM2_D3) / DIM_SYM2_D3).abs() < 0.08
        }).count();
        let sym2_score = sym2_hits as f64 / d.max(1) as f64;

        // 2. dim Λ² = d(d-1)/2 = 3 공명
        let lambda2_hits = means.iter().filter(|&&m| {
            m > 1e-12 && ((m - DIM_LAMBDA2_D3) / DIM_LAMBDA2_D3).abs() < 0.08
        }).count();
        let lambda2_score = lambda2_hits as f64 / d.max(1) as f64;

        // 3. d=3 차원 직접 공명 (입력 데이터에 d=3 포함)
        let d3_hits = means.iter().filter(|&&m| {
            m > 1e-12 && ((m - VORTICITY_DIM) / VORTICITY_DIM).abs() < 0.07
        }).count();
        let d3_score = d3_hits as f64 / d.max(1) as f64;

        // 4. Kolmogorov -5/3 지수 공명 (에너지 카스케이드)
        let kolmo_hits = means.iter().filter(|&&m| {
            m > 1e-12 && ((m - KOLMOGOROV_EXP) / KOLMOGOROV_EXP).abs() < 0.08
        }).count();
        let kolmo_score = kolmo_hits as f64 / d.max(1) as f64;

        // 5. 입력 d 자체가 3인지 확인 (망원경 차원)
        let input_d3_match = (1.0 - (d as f64 - VORTICITY_DIM).abs() / VORTICITY_DIM * 2.0).max(0.0);

        // 6. 전체 NS n=6 상수 공명
        let ns_consts = [N6, SIGMA6, SOPFR6, TAU6, PHI6,
                         DIM_SYM2_D3, DIM_LAMBDA2_D3, KOLMOGOROV_EXP,
                         2.0 * N6, N6 / PHI6]; // 12, 3
        let total_hits = means.iter().filter(|&&m| {
            ns_consts.iter().any(|&c| c > 1e-12 && ((m - c) / c).abs() < 0.07)
        }).count();
        let n6_resonance = total_hits as f64 / d.max(1) as f64;

        // 7. 3중 공명 체크: sym2=6, lambda2=3, vorticity=3 동시 존재
        let triple_resonance = if sym2_hits > 0 && lambda2_hits > 0 && d3_hits > 0 {
            (sym2_score + lambda2_score + d3_score) / 3.0
        } else {
            0.0
        };

        let ns_score = sym2_score    * 0.25
            + triple_resonance       * 0.25
            + kolmo_score            * 0.15
            + n6_resonance           * 0.15
            + d3_score               * 0.10
            + input_d3_match         * 0.05
            + lambda2_score          * 0.05;

        let mut r = HashMap::new();
        r.insert("sym2_score".to_string(),           vec![sym2_score]);
        r.insert("lambda2_score".to_string(),        vec![lambda2_score]);
        r.insert("d3_score".to_string(),             vec![d3_score]);
        r.insert("kolmo_score".to_string(),          vec![kolmo_score]);
        r.insert("triple_resonance".to_string(),     vec![triple_resonance]);
        r.insert("n6_resonance".to_string(),         vec![n6_resonance]);
        r.insert("input_d3_match".to_string(),       vec![input_d3_match]);
        r.insert("navier_stokes_d3_score".to_string(), vec![ns_score]);
        r
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_ns_d3_3중공명() {
        // Sym²=6, Λ²=3, 와도=3 동시 포함
        let n = 9; let d = 3;
        let data: Vec<f64> = (0..n * d).map(|i| match i % d {
            0 => DIM_SYM2_D3,   // 6
            1 => DIM_LAMBDA2_D3, // 3
            _ => VORTICITY_DIM,  // 3
        }).collect();
        let shared = SharedData::compute(&data, n, d);
        let r = NavierStokesD3ResonanceLens.scan(&data, n, d, &shared);
        assert!(r.contains_key("navier_stokes_d3_score"));
        let score = r["navier_stokes_d3_score"][0];
        assert!(score >= 0.0 && score <= 1.0, "점수 범위: {}", score);
        let triple = r["triple_resonance"][0];
        assert!(triple > 0.0, "3중 공명 감지 실패: {}", triple);
    }

    #[test]
    fn test_ns_sym2_n6_일치() {
        // dim Sym²(ℝ³) = 6 = n 직접 검증
        let d3_sym2 = (3_f64 * (3.0 + 1.0)) / 2.0;
        assert!((d3_sym2 - N6).abs() < 1e-9, "d=3: Sym²=6=n: {}", d3_sym2);
    }

    #[test]
    fn test_ns_kolmogorov_공명() {
        let n = 8; let d = 4;
        let data: Vec<f64> = (0..n * d).map(|i| match i % d {
            0 => KOLMOGOROV_EXP,  // 5/3
            1 => N6,              // 6
            2 => DIM_SYM2_D3,    // 6
            _ => SOPFR6,          // 5
        }).collect();
        let shared = SharedData::compute(&data, n, d);
        let r = NavierStokesD3ResonanceLens.scan(&data, n, d, &shared);
        assert!(r["kolmo_score"][0] > 0.0);
    }

    #[test]
    fn test_ns_최소입력_거부() {
        let data = vec![1.0, 2.0, 3.0];
        let shared = SharedData::compute(&data, 3, 1);
        let r = NavierStokesD3ResonanceLens.scan(&data, 3, 1, &shared);
        assert!(r.is_empty());
    }
}
