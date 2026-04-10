use std::collections::HashMap;
use crate::telescope::lens_trait::{Lens, LensResult};
use crate::telescope::shared_data::SharedData;

/// 기상학 n=6 스케일 카운팅 렌즈 (BT-1159) — 기상 분류 체계에서 n=6/sopfr=5/tau=4 공명 검출
///
/// 기상학 분류 체계의 n=6 출현:
///   Saffir-Simpson 허리케인 등급: 5등급 (Cat 1~5) = sopfr(6) = 5
///   Fujita 토네이도 등급: F0~F5 = 6단계 = n
///   기단 타입: 극기단/대륙성/해양성 각 2종 → 합 6종 = n
///   강수 형태: 비/눈/진눈깨비/우박/이슬비/동결비 = 6종 = n
///   기압계 등급: L/H × 3강도 = 6조합 = n
///   구름 기본 속 (genus): 10속 → 저층(4)/중층(2)/고층(2)/수직(2) = tau(6) 배분
///
/// 추가 공명:
///   Beaufort 풍력 등급: 0~12 = 13단계, τ(13)=4=τ(6)
///   Koppen 기후 분류 5대 기후 = sopfr(6)
///   CAPE 임계값 × 6 분위 = n
///
/// σ(6)·φ(6) = 12·2 = 24 → 24시간 기상 주기 = n·τ = 6·4
pub struct MeteorologyN6ScaleLens;

const N6: f64 = 6.0;
const SIGMA6: f64 = 12.0;
const SOPFR6: f64 = 5.0;
const TAU6: f64 = 4.0;
const PHI6: f64 = 2.0;
// 기상 분류 상수
const SAFFIR_GRADES: f64 = 5.0;   // Cat 1~5 = sopfr(6)
const FUJITA_GRADES: f64 = 6.0;   // F0~F5 = n
const AIRMASS_TYPES: f64 = 6.0;   // 6종 기단
const PRECIP_FORMS: f64 = 6.0;    // 6가지 강수 형태
const CLOUD_LOW: f64 = 4.0;       // 저층 구름 4속 = tau(6)
const CLOUD_TOTAL: f64 = 10.0;    // 구름 10속 = σ(6)−2
const KOPPEN_CLASSES: f64 = 5.0;  // 5대 기후 = sopfr(6)
const BEAUFORT_SCALE: f64 = 13.0; // 0~12 = 13단계
const DIURNAL_HOURS: f64 = 24.0;  // σ·φ = 12·2

impl Lens for MeteorologyN6ScaleLens {
    fn name(&self) -> &str { "MeteorologyN6ScaleLens" }
    fn category(&self) -> &str { "T1" }

    fn scan(&self, data: &[f64], n: usize, d: usize, _shared: &SharedData) -> LensResult {
        if n < 4 || d == 0 { return HashMap::new(); }

        let means: Vec<f64> = (0..d).map(|j| {
            (0..n).map(|i| data[i * d + j]).sum::<f64>() / n as f64
        }).collect();

        // 1. n=6 기상 분류 직접 공명
        let n6_class_targets = [N6, FUJITA_GRADES, AIRMASS_TYPES, PRECIP_FORMS];
        let n6_hits = means.iter().filter(|&&m| {
            n6_class_targets.iter().any(|&t| t > 1e-12 && ((m - t) / t).abs() < 0.08)
        }).count();
        let n6_score = n6_hits as f64 / d.max(1) as f64;

        // 2. sopfr=5 공명 (Saffir-Simpson, Koppen)
        let sopfr_targets = [SAFFIR_GRADES, KOPPEN_CLASSES, SOPFR6];
        let sopfr_hits = means.iter().filter(|&&m| {
            sopfr_targets.iter().any(|&t| t > 1e-12 && ((m - t) / t).abs() < 0.08)
        }).count();
        let sopfr_score = sopfr_hits as f64 / d.max(1) as f64;

        // 3. tau=4 공명 (저층구름 4속, 기상 4계절)
        let tau_targets = [TAU6, CLOUD_LOW, 4.0_f64];
        let tau_hits = means.iter().filter(|&&m| {
            tau_targets.iter().any(|&t| t > 1e-12 && ((m - t) / t).abs() < 0.08)
        }).count();
        let tau_score = tau_hits as f64 / d.max(1) as f64;

        // 4. σ(6)=12 / 24시간 주기 공명
        let sigma_targets = [SIGMA6, DIURNAL_HOURS, CLOUD_TOTAL,
                              SIGMA6 / PHI6]; // 6
        let sigma_hits = means.iter().filter(|&&m| {
            sigma_targets.iter().any(|&t| t > 1e-12 && ((m - t) / t).abs() < 0.08)
        }).count();
        let sigma_score = sigma_hits as f64 / d.max(1) as f64;

        // 5. 기상 등급 비율 공명 (Beaufort 13단계 → tau 비율)
        let ratio_hits = means.iter().filter(|&&m| {
            m > 1e-12 && (
                // 6/5 = Fujita/Saffir 비율
                ((m - N6 / SAFFIR_GRADES) / (N6 / SAFFIR_GRADES)).abs() < 0.07 ||
                // 12/5 = sigma/sopfr
                ((m - SIGMA6 / SOPFR6) / (SIGMA6 / SOPFR6)).abs() < 0.07 ||
                // 5/4 = sopfr/tau
                ((m - SOPFR6 / TAU6) / (SOPFR6 / TAU6)).abs() < 0.07
            )
        }).count();
        let ratio_score = ratio_hits as f64 / d.max(1) as f64;

        // 6. 전체 n=6 기상 공명 (전 상수 스캔)
        let all_consts = [N6, SIGMA6, SOPFR6, TAU6, PHI6,
                          SAFFIR_GRADES, FUJITA_GRADES, AIRMASS_TYPES, PRECIP_FORMS,
                          CLOUD_LOW, CLOUD_TOTAL, KOPPEN_CLASSES, BEAUFORT_SCALE,
                          DIURNAL_HOURS];
        let total_hits = means.iter().filter(|&&m| {
            all_consts.iter().any(|&c| c > 1e-12 && ((m - c) / c).abs() < 0.07)
        }).count();
        let total_resonance = total_hits as f64 / d.max(1) as f64;

        // 7. 삼중 공명 보너스: n=6 + sopfr=5 + tau=4 동시
        let triple_bonus = if n6_hits > 0 && sopfr_hits > 0 && tau_hits > 0 {
            (n6_score + sopfr_score + tau_score) / 3.0 * 1.2
        } else {
            0.0
        }.min(1.0);

        let meteo_score = (n6_score     * 0.30
            + sopfr_score               * 0.20
            + tau_score                 * 0.15
            + sigma_score               * 0.10
            + total_resonance           * 0.10
            + ratio_score               * 0.08
            + triple_bonus              * 0.07).min(1.0);

        let mut r = HashMap::new();
        r.insert("n6_score".to_string(),       vec![n6_score]);
        r.insert("sopfr_score".to_string(),    vec![sopfr_score]);
        r.insert("tau_score".to_string(),      vec![tau_score]);
        r.insert("sigma_score".to_string(),    vec![sigma_score]);
        r.insert("ratio_score".to_string(),    vec![ratio_score]);
        r.insert("total_resonance".to_string(), vec![total_resonance]);
        r.insert("triple_bonus".to_string(),   vec![triple_bonus]);
        r.insert("meteorology_n6_scale_score".to_string(), vec![meteo_score]);
        r
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_meteo_n6_기본() {
        // Fujita(6), Saffir(5), 저층구름(4) 동시
        let n = 9; let d = 3;
        let data: Vec<f64> = (0..n * d).map(|i| match i % d {
            0 => FUJITA_GRADES,   // 6
            1 => SAFFIR_GRADES,   // 5
            _ => CLOUD_LOW,       // 4
        }).collect();
        let shared = SharedData::compute(&data, n, d);
        let r = MeteorologyN6ScaleLens.scan(&data, n, d, &shared);
        assert!(r.contains_key("meteorology_n6_scale_score"));
        let score = r["meteorology_n6_scale_score"][0];
        assert!(score >= 0.0 && score <= 1.0, "점수 범위: {}", score);
        assert!(r["triple_bonus"][0] > 0.0, "삼중 공명 기대");
    }

    #[test]
    fn test_meteo_fujita_n6_동치() {
        // Fujita 등급 = n=6 동치 검증
        assert!((FUJITA_GRADES - N6).abs() < 1e-9);
    }

    #[test]
    fn test_meteo_24시간_sigma_phi() {
        // σ(6)·φ(6) = 12·2 = 24 검증
        assert!((SIGMA6 * PHI6 - DIURNAL_HOURS).abs() < 1e-9);
    }

    #[test]
    fn test_meteo_전상수_스캔() {
        // 모든 기상 상수 포함
        let n = 12; let d = 6;
        let vals = [N6, SOPFR6, TAU6, SIGMA6, SAFFIR_GRADES, CLOUD_LOW];
        let data: Vec<f64> = (0..n * d).map(|i| vals[i % d]).collect();
        let shared = SharedData::compute(&data, n, d);
        let r = MeteorologyN6ScaleLens.scan(&data, n, d, &shared);
        assert!(r["total_resonance"][0] > 0.5, "전 상수 공명 기대");
    }

    #[test]
    fn test_meteo_최소입력_거부() {
        let data = vec![1.0, 2.0, 3.0];
        let shared = SharedData::compute(&data, 3, 1);
        let r = MeteorologyN6ScaleLens.scan(&data, 3, 1, &shared);
        assert!(r.is_empty());
    }
}
