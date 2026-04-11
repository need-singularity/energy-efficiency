use super::registry::{LensCategory, LensEntry};

/// Build metadata entries for 8 frontier discovery lenses.
///
/// These lenses cover previously uncovered scientific domains:
/// acoustics, fluid dynamics, game theory, linguistics,
/// irreversible thermodynamics, polymer physics, resonance, and convexity.
pub fn frontier_lens_entries() -> Vec<LensEntry> {
    vec![
        LensEntry {
            name: "acoustic".into(),
            category: LensCategory::Extended,
            description: "Detect sound-wave patterns: periodicity, harmonics, tonality (sigma=12 semitones)".into(),
            domain_affinity: vec!["audio".into(), "music".into(), "physics".into(), "signal".into(), "display".into()],
            complementary: vec!["wave".into(), "periodicity".into(), "resonance".into()],
        },
        LensEntry {
            name: "fluid_dynamics".into(),
            category: LensCategory::Extended,
            description: "Measure turbulence via Reynolds-like number and Kolmogorov 5/3 exponent (sopfr/n/phi)".into(),
            domain_affinity: vec!["physics".into(), "engineering".into(), "plasma".into(), "atmosphere".into()],
            complementary: vec!["chaos".into(), "multiscale".into(), "scale".into()],
        },
        LensEntry {
            name: "game_theory".into(),
            category: LensCategory::Extended,
            description: "Detect Nash equilibrium proximity, cooperation index, Egyptian allocation (1/2+1/3+1/6=1)".into(),
            domain_affinity: vec!["economics".into(), "social".into(), "ai".into(), "biology".into()],
            complementary: vec!["mirror".into(), "stability".into(), "network".into()],
        },
        LensEntry {
            name: "linguistic".into(),
            category: LensCategory::Extended,
            description: "Measure Zipf's law exponent and rank-frequency distribution (vocab ~ 2^n=6)".into(),
            domain_affinity: vec!["nlp".into(), "ai".into(), "social".into(), "information".into()],
            complementary: vec!["power_law".into(), "entropy".into(), "info".into()],
        },
        LensEntry {
            name: "entropy_production_rate".into(),
            category: LensCategory::Extended,
            description: "Quantify irreversibility via forward/backward transition asymmetry (R(6)=1 reversibility)".into(),
            domain_affinity: vec!["physics".into(), "chemistry".into(), "biology".into(), "thermo".into(), "environment".into()],
            complementary: vec!["thermo".into(), "causal".into(), "memory".into()],
        },
        LensEntry {
            name: "polymer".into(),
            category: LensCategory::Extended,
            description: "Chain statistics: Flory exponent, radius of gyration, persistence (Carbon Z=6 backbone)".into(),
            domain_affinity: vec!["chemistry".into(), "materials".into(), "biology".into(), "polymer".into(), "carbon-capture".into()],
            complementary: vec!["fractal".into(), "scale".into(), "hexagonal".into()],
        },
        LensEntry {
            name: "resonance".into(),
            category: LensCategory::Extended,
            description: "Detect cross-dimensional coupling at integer frequency ratios (divisors of 6: 1,2,3,6)".into(),
            domain_affinity: vec!["physics".into(), "engineering".into(), "music".into(), "signal".into()],
            complementary: vec!["wave".into(), "acoustic".into(), "correlation".into()],
        },
        LensEntry {
            name: "convexity_geometry".into(),
            category: LensCategory::Extended,
            description: "Measure data cloud convexity, curvature, and hull vertex count (hexagon=n=6 optimal)".into(),
            domain_affinity: vec!["mathematics".into(), "optimization".into(), "geometry".into(), "ai".into()],
            complementary: vec!["topology".into(), "boundary".into(), "hexagonal".into()],
        },
    ]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_frontier_lens_count() {
        let entries = frontier_lens_entries();
        assert_eq!(entries.len(), 8, "Must have exactly 8 frontier lenses");
    }

    #[test]
    fn test_frontier_lens_names_unique() {
        let entries = frontier_lens_entries();
        let mut names: Vec<&str> = entries.iter().map(|e| e.name.as_str()).collect();
        let total = names.len();
        names.sort();
        names.dedup();
        assert_eq!(names.len(), total, "All frontier lens names must be unique");
    }

    #[test]
    fn test_frontier_all_extended() {
        let entries = frontier_lens_entries();
        for entry in &entries {
            assert_eq!(
                entry.category,
                LensCategory::Extended,
                "Lens '{}' should be Extended category",
                entry.name
            );
        }
    }
}

/// Build metadata entries for 8 new-domain lenses (todo#16).
///
/// Domains: morphology, tonal harmony, ecological niche, macroeconomics,
/// immunogenetics, phonetics, food web, behavioral economics.
pub fn new_domain_lens_entries() -> Vec<LensEntry> {
    vec![
        LensEntry {
            name: "morphology".into(),
            category: LensCategory::Extended,
            description: "Detect morpheme distribution: 6 POS classes, tau=4 inflection, sigma=12 phoneme patterns (BT-112,BT-215)".into(),
            domain_affinity: vec!["linguistics".into(), "nlp".into(), "ai".into(), "social".into()],
            complementary: vec!["linguistic".into(), "entropy".into(), "clustering".into()],
        },
        LensEntry {
            name: "tonal_harmony".into(),
            category: LensCategory::Extended,
            description: "Measure hexatonic scale (6-note), triad tau=4 inversions, circle-of-fifths cycle 24 (BT-108,BT-135)".into(),
            domain_affinity: vec!["music".into(), "audio".into(), "signal".into(), "physics".into()],
            complementary: vec!["music_harmony".into(), "acoustic".into(), "resonance".into()],
        },
        LensEntry {
            name: "ecological_niche".into(),
            category: LensCategory::Extended,
            description: "Compute Simpson diversity and 6-tier trophic hierarchy alignment (BT-178,BT-201)".into(),
            domain_affinity: vec!["ecology".into(), "biology".into(), "environment".into(), "climate".into()],
            complementary: vec!["evolution".into(), "network".into(), "stability".into()],
        },
        LensEntry {
            name: "macroeconomics".into(),
            category: LensCategory::Extended,
            description: "Detect 6-phase business cycle, 4-quarter periodicity, sigma*phi=288 attractor (BT-143,BT-189)".into(),
            domain_affinity: vec!["economics".into(), "finance".into(), "social".into(), "energy".into()],
            complementary: vec!["game_theory".into(), "periodicity".into(), "phase_transition".into()],
        },
        LensEntry {
            name: "immunogenetics".into(),
            category: LensCategory::Extended,
            description: "Measure 6 Ig class diversity, HLA 6-locus polymorphism, MHC-II 6 subunit proximity (BT-155,BT-194,BT-220)".into(),
            domain_affinity: vec!["immunology".into(), "biology".into(), "medicine".into(), "genetics".into()],
            complementary: vec!["immune_response".into(), "genome_coding".into(), "evolution".into()],
        },
        LensEntry {
            name: "phonetics".into(),
            category: LensCategory::Extended,
            description: "Detect 6 articulation positions, F1/F2 formant ratios, sigma=12 vowel formant pairs (BT-112,BT-137)".into(),
            domain_affinity: vec!["linguistics".into(), "audio".into(), "nlp".into(), "signal".into()],
            complementary: vec!["morphology".into(), "acoustic".into(), "spectral".into()],
        },
        LensEntry {
            name: "food_web".into(),
            category: LensCategory::Extended,
            description: "Compute 6-tier biomass pyramid, sigma/tau=3 predator-prey ratio, energy transfer efficiency (BT-178,BT-201,BT-233)".into(),
            domain_affinity: vec!["ecology".into(), "biology".into(), "environment".into(), "ocean".into()],
            complementary: vec!["ecological_niche".into(), "network".into(), "graph".into()],
        },
        LensEntry {
            name: "behavioral_economics".into(),
            category: LensCategory::Extended,
            description: "Detect 6 cognitive bias clusters, phi=2 loss aversion, n=6 choice overload threshold (BT-143,BT-189,BT-212)".into(),
            domain_affinity: vec!["economics".into(), "psychology".into(), "social".into(), "ai".into()],
            complementary: vec!["macroeconomics".into(), "game_theory".into(), "decision".into()],
        },
    ]
}

/// 차원지각 렌즈 메타데이터 (BT-1108)
///
/// 도메인: VR/AR/XR, 완전광학, 4D 기하학, 인지과학, 끈이론, 디스플레이, 햅틱
pub fn dimensional_perception_lens_entries() -> Vec<LensEntry> {
    vec![
        LensEntry {
            name: "dimensional_perception".into(),
            category: LensCategory::Extended,
            description: "BT-1108 차원지각: 완전광학함수 6D=n, Tesseract C(4,2)=6=n, SO(4) 6 회전평면, OpenBCI 16ch=phi^tau, 알파밴드 8-12Hz, Calabi-Yau 6D".into(),
            domain_affinity: vec![
                "vr_ar_xr".into(),
                "plenoptic".into(),
                "4d_geometry".into(),
                "cognitive_science".into(),
                "string_theory".into(),
                "display".into(),
                "haptics".into(),
                "bci".into(),
            ],
            complementary: vec![
                "brain_neural".into(),
                "brain_map".into(),
                "dimensional_bridge".into(),
                "topology".into(),
                "quantum_circuit".into(),
                "hexagonal".into(),
            ],
        },
    ]
}

/// 신규 4종 렌즈 메타데이터 (마케팅/디지털트윈/발효/시계공학)
pub fn new_quad_lens_entries() -> Vec<LensEntry> {
    vec![
        LensEntry {
            name: "marketing".into(),
            category: LensCategory::Extended,
            description: "BT-548~557 마케팅 불변법칙 sigma=12, 4P tau=4, 이집트분수 1/2+1/3+1/6=1, NPS sigma-phi=10, 바이럴 R0=n=6".into(),
            domain_affinity: vec![
                "marketing".into(),
                "economics".into(),
                "social".into(),
                "psychology".into(),
                "media".into(),
            ],
            complementary: vec![
                "behavioral_economics".into(),
                "macroeconomics".into(),
                "game_theory".into(),
                "social_network".into(),
            ],
        },
        LensEntry {
            name: "digital_twin".into(),
            category: LensCategory::Extended,
            description: "디지털 트윈: IoT 6레이어=n, ISO 23247 tau=4 레이어, OPC UA sigma-tau=8 노드, 5G sopfr=5 슬라이스, J2=24시간 루프".into(),
            domain_affinity: vec![
                "digital_twin".into(),
                "iot".into(),
                "manufacturing".into(),
                "simulation".into(),
                "ai".into(),
            ],
            complementary: vec![
                "chip_architecture".into(),
                "networking_protocol".into(),
                "simulation".into(),
                "sensor".into(),
            ],
        },
        LensEntry {
            name: "fermentation".into(),
            category: LensCategory::Extended,
            description: "발효 생물화학: 포도당 C₆=n, 해당효소 n=6, ATP 순이득 phi=2, pH tau=4, 로지스틱 성장 S곡선, sigma=12 알코올내성".into(),
            domain_affinity: vec![
                "fermentation".into(),
                "biology".into(),
                "chemistry".into(),
                "food_science".into(),
                "biotechnology".into(),
            ],
            complementary: vec![
                "molecular_transform".into(),
                "evolution".into(),
                "polymer".into(),
                "food_chemistry".into(),
            ],
        },
        LensEntry {
            name: "horology".into(),
            category: LensCategory::Extended,
            description: "시계공학: 기어 n=6, 다이얼 sigma=12, J2=24시간, 탈진 tau=4Hz, 팰릿 phi=2, 3바늘 n/phi=3, 탈진 주기성 감지".into(),
            domain_affinity: vec![
                "horology".into(),
                "precision_mechanics".into(),
                "metrology".into(),
                "physics".into(),
                "manufacturing".into(),
            ],
            complementary: vec![
                "periodicity".into(),
                "tribology".into(),
                "materials_crystal".into(),
                "resonance".into(),
            ],
        },
    ]
}

/// 신규 56종 렌즈 메타데이터 (397→453 확장)
///
/// 카테고리: 도메인 간 브리지 (12), 시계열/인과/복잡계 (14),
///           불확실성/베이지안 (10), 머신러닝 고급 (20)
pub fn expansion_56_lens_entries() -> Vec<LensEntry> {
    vec![
        // ── 도메인 간 브리지 (12종) ──
        LensEntry {
            name: "cross_domain_bridge".into(),
            category: LensCategory::Extended,
            description: "이종 도메인 구조 공명: 브리지 연결=n=6, 동형 레이어=tau=4, 공명 주파수=sigma=12".into(),
            domain_affinity: vec!["multi_domain".into(), "integration".into(), "systems".into(), "ai".into()],
            complementary: vec!["isomorphism".into(), "topology".into(), "network".into()],
        },
        LensEntry {
            name: "agent_coordination".into(),
            category: LensCategory::Extended,
            description: "다중 에이전트 조율: 에이전트=n=6, 합의=tau=4, 메시지=sigma=12".into(),
            domain_affinity: vec!["ai".into(), "robotics".into(), "social".into(), "distributed".into()],
            complementary: vec!["faction_debate".into(), "consensus".into(), "game_theory".into()],
        },
        LensEntry {
            name: "knowledge_graph".into(),
            category: LensCategory::Extended,
            description: "지식 그래프: 관계=n=6, 엔티티=sigma=12, 임베딩=tau*sigma=48".into(),
            domain_affinity: vec!["nlp".into(), "ai".into(), "semantics".into(), "database".into()],
            complementary: vec!["graph".into(), "semantic".into(), "embedding".into()],
        },
        LensEntry {
            name: "distributed_consensus".into(),
            category: LensCategory::Extended,
            description: "분산 합의: 내결함성=n/phi=3, 노드=n=6, Paxos=phi=2".into(),
            domain_affinity: vec!["distributed".into(), "networking".into(), "blockchain".into()],
            complementary: vec!["consensus".into(), "network".into(), "fault_tolerance".into()],
        },
        LensEntry {
            name: "optimal_transport".into(),
            category: LensCategory::Extended,
            description: "최적 수송: Earth-mover 분할=n=6, Sinkhorn=sigma=12, dual=phi=2".into(),
            domain_affinity: vec!["mathematics".into(), "ai".into(), "economics".into(), "physics".into()],
            complementary: vec!["density".into(), "clustering".into(), "dimension_reduction".into()],
        },
        LensEntry {
            name: "structural_equation".into(),
            category: LensCategory::Extended,
            description: "구조 방정식 SEM: 잠재 변수=n=6, 경로=phi=2, 적합도=tau=4".into(),
            domain_affinity: vec!["statistics".into(), "social".into(), "psychology".into(), "biology".into()],
            complementary: vec!["causal_chain".into(), "bayesian_inference".into(), "network".into()],
        },
        LensEntry {
            name: "community_detection".into(),
            category: LensCategory::Extended,
            description: "커뮤니티 탐지: 커뮤니티=n=6, modularity=1-1/sigma, 해상도=phi=2".into(),
            domain_affinity: vec!["social".into(), "network".into(), "biology".into(), "marketing".into()],
            complementary: vec!["clustering".into(), "graph".into(), "faction_debate".into()],
        },
        LensEntry {
            name: "link_prediction".into(),
            category: LensCategory::Extended,
            description: "링크 예측: 경로=n=6, Katz beta=1/sigma, 공통 이웃=tau=4".into(),
            domain_affinity: vec!["social".into(), "network".into(), "recommendation".into()],
            complementary: vec!["graph".into(), "spectral_graph".into(), "network".into()],
        },
        LensEntry {
            name: "spectral_graph".into(),
            category: LensCategory::Extended,
            description: "스펙트럴 그래프: k=n=6 고유벡터, Fiedler=1/n, 스펙트럴 갭=phi=2".into(),
            domain_affinity: vec!["mathematics".into(), "network".into(), "image".into(), "physics".into()],
            complementary: vec!["spectral".into(), "graph".into(), "community_detection".into()],
        },
        LensEntry {
            name: "network_flow".into(),
            category: LensCategory::Extended,
            description: "네트워크 흐름: max-flow 컷=n=6, 채널=tau=4, 용량=sigma=12".into(),
            domain_affinity: vec!["logistics".into(), "network".into(), "engineering".into(), "economics".into()],
            complementary: vec!["graph".into(), "optimization".into(), "logistics_supply".into()],
        },
        LensEntry {
            name: "topological_sort".into(),
            category: LensCategory::Extended,
            description: "위상 정렬 DAG: 의존 깊이=n=6, 병렬 레벨=tau=4, 선행=phi=2".into(),
            domain_affinity: vec!["computer_science".into(), "build_systems".into(), "scheduling".into()],
            complementary: vec!["graph".into(), "recursion".into(), "causal_chain".into()],
        },
        LensEntry {
            name: "probabilistic_graphical".into(),
            category: LensCategory::Extended,
            description: "확률 그래프: 노드=n=6, 부모=phi=2, Markov blanket=tau=4".into(),
            domain_affinity: vec!["statistics".into(), "ai".into(), "biology".into(), "robotics".into()],
            complementary: vec!["bayesian_inference".into(), "markov_chain".into(), "causal".into()],
        },
        // ── 시계열/인과/복잡계 (14종) ──
        LensEntry {
            name: "causal_discovery".into(),
            category: LensCategory::Extended,
            description: "인과 발견 PC/FCI: 조건 집합=n=6, skeleton=sigma=12, v-구조=tau=4".into(),
            domain_affinity: vec!["statistics".into(), "ai".into(), "medicine".into(), "economics".into()],
            complementary: vec!["causal_chain".into(), "causal".into(), "bayesian_inference".into()],
        },
        LensEntry {
            name: "time_series_decomp".into(),
            category: LensCategory::Extended,
            description: "시계열 분해 STL: 계절성=n=6, 분해 레이어=tau=4, 레벨=sigma/phi=6".into(),
            domain_affinity: vec!["statistics".into(), "economics".into(), "signal".into(), "climate".into()],
            complementary: vec!["periodicity".into(), "fourier_analysis".into(), "stationarity".into()],
        },
        LensEntry {
            name: "markov_chain".into(),
            category: LensCategory::Extended,
            description: "마르코프 체인: 상태=n=6, 혼합=sigma=12, 재귀=n/phi=3".into(),
            domain_affinity: vec!["statistics".into(), "physics".into(), "economics".into(), "biology".into()],
            complementary: vec!["periodicity".into(), "stationarity".into(), "monte_carlo".into()],
        },
        LensEntry {
            name: "attractor_basin".into(),
            category: LensCategory::Extended,
            description: "어트랙터 분지: 카오스→질서=n=6, 주기 배가=tau=4, 분지=n/phi=3".into(),
            domain_affinity: vec!["physics".into(), "biology".into(), "neural".into(), "climate".into()],
            complementary: vec!["chaos".into(), "phase_transition".into(), "stability".into()],
        },
        LensEntry {
            name: "complexity_network".into(),
            category: LensCategory::Extended,
            description: "복잡 네트워크 스몰월드: 이웃=n=6, scale-free gamma=tau-1, 허브=sigma=12".into(),
            domain_affinity: vec!["network".into(), "biology".into(), "social".into(), "internet".into()],
            complementary: vec!["network".into(), "community_detection".into(), "emergence".into()],
        },
        LensEntry {
            name: "fourier_analysis".into(),
            category: LensCategory::Extended,
            description: "푸리에 분석: harmonics=n=6, FFT=phi^sigma=4096, 기본주파수=1/n".into(),
            domain_affinity: vec!["signal".into(), "physics".into(), "audio".into(), "communications".into()],
            complementary: vec!["spectral".into(), "wavelet_transform".into(), "periodicity".into()],
        },
        LensEntry {
            name: "wavelet_transform".into(),
            category: LensCategory::Extended,
            description: "웨이블릿 변환 다중 해상도: 레벨=n=6, Daubechies=tau*phi=8, 스케일=phi^n=64".into(),
            domain_affinity: vec!["signal".into(), "image".into(), "physics".into(), "finance".into()],
            complementary: vec!["fourier_analysis".into(), "multiscale".into(), "compression".into()],
        },
        LensEntry {
            name: "kalman_filter".into(),
            category: LensCategory::Extended,
            description: "칼만 필터 상태 추정: 상태=n=6, 관측=tau=4, innovation=1/n".into(),
            domain_affinity: vec!["robotics".into(), "navigation".into(), "signal".into(), "finance".into()],
            complementary: vec!["particle_filter".into(), "bayesian_inference".into(), "stability".into()],
        },
        LensEntry {
            name: "particle_filter".into(),
            category: LensCategory::Extended,
            description: "파티클 필터 비선형: 파티클=n*sigma=72, 재샘플=tau=4, 효과적=n=6".into(),
            domain_affinity: vec!["robotics".into(), "navigation".into(), "signal".into(), "biology".into()],
            complementary: vec!["kalman_filter".into(), "monte_carlo".into(), "bayesian_inference".into()],
        },
        LensEntry {
            name: "sampling_theory".into(),
            category: LensCategory::Extended,
            description: "샘플링 이론 Nyquist: 비율=phi=2, 오버샘플=sigma=12, aliasing=n=6".into(),
            domain_affinity: vec!["signal".into(), "audio".into(), "statistics".into(), "communications".into()],
            complementary: vec!["fourier_analysis".into(), "signal_reconstruction".into(), "periodicity".into()],
        },
        LensEntry {
            name: "signal_reconstruction".into(),
            category: LensCategory::Extended,
            description: "신호 재구성 compressed sensing: sparsity=n=6, RIP delta=1/n, measurement=sigma*tau=48".into(),
            domain_affinity: vec!["signal".into(), "image".into(), "communications".into(), "ai".into()],
            complementary: vec!["compression".into(), "sampling_theory".into(), "fourier_analysis".into()],
        },
        LensEntry {
            name: "sensitivity_analysis".into(),
            category: LensCategory::Extended,
            description: "민감도 분석 Sobol: 지수=n=6, 1차 효과=phi=2, 교호작용=tau=4".into(),
            domain_affinity: vec!["engineering".into(), "statistics".into(), "finance".into(), "ai".into()],
            complementary: vec!["uncertainty_quantification".into(), "simulation".into(), "gradient".into()],
        },
        LensEntry {
            name: "topological_data".into(),
            category: LensCategory::Extended,
            description: "위상 데이터 TDA: 필터링=n=6, 바코드=sigma=12, 호몰로지=tau=4".into(),
            domain_affinity: vec!["mathematics".into(), "biology".into(), "materials".into(), "ai".into()],
            complementary: vec!["persistence_homology".into(), "topology".into(), "manifold_learning".into()],
        },
        // ── 불확실성/베이지안 (10종) ──
        LensEntry {
            name: "bayesian_inference".into(),
            category: LensCategory::Extended,
            description: "베이지안 추론: beta=n=6, Bayes factor=tau-1=3, KL threshold=1/n".into(),
            domain_affinity: vec!["statistics".into(), "ai".into(), "medicine".into(), "physics".into()],
            complementary: vec!["probabilistic_graphical".into(), "variational_inference".into(), "monte_carlo".into()],
        },
        LensEntry {
            name: "uncertainty_quantification".into(),
            category: LensCategory::Extended,
            description: "불확실성 정량화: 6-sigma=n=6, UQ 분류=tau=4, coverage=5/6".into(),
            domain_affinity: vec!["engineering".into(), "statistics".into(), "ai".into(), "physics".into()],
            complementary: vec!["bayesian_inference".into(), "monte_carlo".into(), "sensitivity_analysis".into()],
        },
        LensEntry {
            name: "information_bottleneck".into(),
            category: LensCategory::Extended,
            description: "정보 병목 IB: beta=n=6, 클러스터=n=6, relevance 차원=tau=4".into(),
            domain_affinity: vec!["information_theory".into(), "ai".into(), "neuroscience".into()],
            complementary: vec!["entropy".into(), "dimension_reduction".into(), "compression".into()],
        },
        LensEntry {
            name: "renyi_entropy".into(),
            category: LensCategory::Extended,
            description: "레니 엔트로피 alpha 차수: Hartley=log(n=6), collision alpha=phi=2, min-entropy=1/sigma".into(),
            domain_affinity: vec!["information_theory".into(), "physics".into(), "cryptography".into()],
            complementary: vec!["entropy".into(), "information_bottleneck".into(), "bayesian_inference".into()],
        },
        LensEntry {
            name: "monte_carlo".into(),
            category: LensCategory::Extended,
            description: "몬테카를로 MCMC: chain=n=6, burn-in=sigma^phi=144, thin=tau=4".into(),
            domain_affinity: vec!["statistics".into(), "physics".into(), "finance".into(), "biology".into()],
            complementary: vec!["bayesian_inference".into(), "variational_inference".into(), "sampling_theory".into()],
        },
        LensEntry {
            name: "variational_inference".into(),
            category: LensCategory::Extended,
            description: "변분 추론 ELBO: 잠재=n=6, KL weight=1/n, 반복=sigma=12".into(),
            domain_affinity: vec!["ai".into(), "statistics".into(), "generative".into()],
            complementary: vec!["bayesian_inference".into(), "monte_carlo".into(), "dimensionality_bottleneck".into()],
        },
        LensEntry {
            name: "manifold_learning".into(),
            category: LensCategory::Extended,
            description: "다양체 학습 내재 차원: d_int=n=6, 이웃=sigma/phi=6, geodesic=n=6".into(),
            domain_affinity: vec!["ai".into(), "mathematics".into(), "image".into(), "neuroscience".into()],
            complementary: vec!["dimension_reduction".into(), "topology".into(), "topological_data".into()],
        },
        LensEntry {
            name: "persistence_homology".into(),
            category: LensCategory::Extended,
            description: "영속 호몰로지: Betti=n=6, persistence bar=sigma=12, death/birth=phi=2".into(),
            domain_affinity: vec!["mathematics".into(), "biology".into(), "materials".into(), "data_science".into()],
            complementary: vec!["topological_data".into(), "topology".into(), "manifold_learning".into()],
        },
        LensEntry {
            name: "cross_validation".into(),
            category: LensCategory::Extended,
            description: "교차 검증 k-fold: k=n=6, stratified=tau=4, nested=phi=2".into(),
            domain_affinity: vec!["ai".into(), "statistics".into(), "data_science".into()],
            complementary: vec!["hyperparameter_tuning".into(), "overfitting".into(), "model_selection".into()],
        },
        LensEntry {
            name: "hyperparameter_tuning".into(),
            category: LensCategory::Extended,
            description: "하이퍼파라미터 조정 BO: 탐색=n=6, acquisition=phi=2, budget=n*sigma=72".into(),
            domain_affinity: vec!["ai".into(), "optimization".into(), "data_science".into()],
            complementary: vec!["cross_validation".into(), "neural_architecture".into(), "active_learning".into()],
        },
        // ── 머신러닝 고급 (20종) ──
        LensEntry {
            name: "transfer_learning".into(),
            category: LensCategory::Extended,
            description: "전이 학습: 레이어=n=6, fine-tune=tau=4, 적응=1/phi=0.5".into(),
            domain_affinity: vec!["ai".into(), "nlp".into(), "vision".into(), "robotics".into()],
            complementary: vec!["meta_learning".into(), "continual_learning".into(), "neural_architecture".into()],
        },
        LensEntry {
            name: "contrastive_learning".into(),
            category: LensCategory::Extended,
            description: "대조 학습 SimCLR: negative=n=6, 온도=tau/sigma, augment=phi=2".into(),
            domain_affinity: vec!["ai".into(), "vision".into(), "nlp".into(), "representation".into()],
            complementary: vec!["self_supervised".into(), "transfer_learning".into(), "embedding".into()],
        },
        LensEntry {
            name: "self_supervised".into(),
            category: LensCategory::Extended,
            description: "자기지도 학습: 마스크=1/n=1/6, pretext=tau=4, 배치=sigma^phi=144".into(),
            domain_affinity: vec!["ai".into(), "nlp".into(), "vision".into(), "representation".into()],
            complementary: vec!["contrastive_learning".into(), "transfer_learning".into(), "mask_modeling".into()],
        },
        LensEntry {
            name: "meta_learning".into(),
            category: LensCategory::Extended,
            description: "메타 학습 MAML: shot=n=6, inner loop=phi=2, gradient=tau=4".into(),
            domain_affinity: vec!["ai".into(), "robotics".into(), "few_shot".into()],
            complementary: vec!["transfer_learning".into(), "active_learning".into(), "reinforcement_reward".into()],
        },
        LensEntry {
            name: "graph_neural".into(),
            category: LensCategory::Extended,
            description: "그래프 신경망 GNN: 집계 홉=n=6, 이웃=sigma=12, 레이어=tau=4".into(),
            domain_affinity: vec!["ai".into(), "chemistry".into(), "social".into(), "biology".into()],
            complementary: vec!["graph".into(), "spectral_graph".into(), "knowledge_graph".into()],
        },
        LensEntry {
            name: "attention_mechanism".into(),
            category: LensCategory::Extended,
            description: "어텐션 메커니즘 Transformer: 헤드=n=6, KV=sigma^phi=144, 온도=phi=2".into(),
            domain_affinity: vec!["ai".into(), "nlp".into(), "vision".into(), "speech".into()],
            complementary: vec!["transformer_anatomy".into(), "multi_task".into(), "neural_architecture".into()],
        },
        LensEntry {
            name: "reinforcement_reward".into(),
            category: LensCategory::Extended,
            description: "강화학습 정책 최적화: 행동=n=6, 할인=1-1/sigma, 에피소드=tau*sigma=48".into(),
            domain_affinity: vec!["ai".into(), "robotics".into(), "game".into(), "economics".into()],
            complementary: vec!["meta_learning".into(), "game_theory".into(), "multi_task".into()],
        },
        LensEntry {
            name: "multi_task".into(),
            category: LensCategory::Extended,
            description: "다중 과제 MTL: 과제=n=6, 공유=tau=4, MTL 손실=phi=2".into(),
            domain_affinity: vec!["ai".into(), "nlp".into(), "robotics".into(), "vision".into()],
            complementary: vec!["attention_mechanism".into(), "transfer_learning".into(), "neural_architecture".into()],
        },
        LensEntry {
            name: "adversarial_robustness".into(),
            category: LensCategory::Extended,
            description: "적대적 강건성 PGD: 단계=n=6, epsilon=1/sigma=1/12, L∞=1/n".into(),
            domain_affinity: vec!["ai".into(), "security".into(), "vision".into(), "nlp".into()],
            complementary: vec!["fairness_bias".into(), "explainability".into(), "neural_architecture".into()],
        },
        LensEntry {
            name: "continual_learning".into(),
            category: LensCategory::Extended,
            description: "연속 학습 EWC: 과제=n=6, lambda=1/n, replay=sigma*tau=48".into(),
            domain_affinity: vec!["ai".into(), "robotics".into(), "neuroscience".into()],
            complementary: vec!["transfer_learning".into(), "meta_learning".into(), "plasticity_consolidation".into()],
        },
        LensEntry {
            name: "federated_learning".into(),
            category: LensCategory::Extended,
            description: "연합 학습 FedAvg: 클라이언트=n=6, round=sigma=12, local=tau=4".into(),
            domain_affinity: vec!["ai".into(), "privacy".into(), "distributed".into(), "healthcare".into()],
            complementary: vec!["distributed_consensus".into(), "differential_privacy".into(), "multi_task".into()],
        },
        LensEntry {
            name: "neural_architecture".into(),
            category: LensCategory::Extended,
            description: "신경망 구조 NAS: depth=n=6, width=sigma^phi=144, bottleneck=tau=4".into(),
            domain_affinity: vec!["ai".into(), "hardware".into(), "optimization".into()],
            complementary: vec!["hyperparameter_tuning".into(), "transformer_anatomy".into(), "chip_architecture".into()],
        },
        LensEntry {
            name: "active_learning".into(),
            category: LensCategory::Extended,
            description: "능동 학습 쿼리: 배치=n=6, uncertainty=1/n, pool=sigma^phi=144".into(),
            domain_affinity: vec!["ai".into(), "annotation".into(), "data_science".into()],
            complementary: vec!["bayesian_inference".into(), "hyperparameter_tuning".into(), "cross_validation".into()],
        },
        LensEntry {
            name: "fairness_bias".into(),
            category: LensCategory::Extended,
            description: "공정성 편향 알고리즘: 집단=n=6, disparity=1/n, equalized odds=phi=2".into(),
            domain_affinity: vec!["ai".into(), "social".into(), "ethics".into(), "law".into()],
            complementary: vec!["adversarial_robustness".into(), "explainability".into(), "statistical_parity".into()],
        },
        LensEntry {
            name: "explainability".into(),
            category: LensCategory::Extended,
            description: "설명가능성 SHAP/LIME: 특성=n=6, 샘플=sigma^phi=144, 근사=1/n".into(),
            domain_affinity: vec!["ai".into(), "medicine".into(), "law".into(), "finance".into()],
            complementary: vec!["fairness_bias".into(), "attention_mechanism".into(), "gradient".into()],
        },
        LensEntry {
            name: "dimensionality_bottleneck".into(),
            category: LensCategory::Extended,
            description: "차원 병목 latent: 잠재=n=6, 인코더=tau=4, 재구성=1/n".into(),
            domain_affinity: vec!["ai".into(), "generative".into(), "signal".into()],
            complementary: vec!["variational_inference".into(), "information_bottleneck".into(), "compression".into()],
        },
        LensEntry {
            name: "spiking_neural".into(),
            category: LensCategory::Extended,
            description: "스파이킹 신경망 LIF: 불응기=tau=4ms, 시냅스=sigma=12, 발화=n=6Hz".into(),
            domain_affinity: vec!["neuroscience".into(), "ai".into(), "hardware".into(), "robotics".into()],
            complementary: vec!["hebbian_plasticity".into(), "plasticity_consolidation".into(), "bci_neurofeedback".into()],
        },
        LensEntry {
            name: "reservoir_computing".into(),
            category: LensCategory::Extended,
            description: "저수지 컴퓨팅 ESN: 노드=n*sigma=72, spectral=1-1/n, echo=tau=4".into(),
            domain_affinity: vec!["ai".into(), "signal".into(), "physics".into(), "neuroscience".into()],
            complementary: vec!["spiking_neural".into(), "markov_chain".into(), "time_series_decomp".into()],
        },
        LensEntry {
            name: "plasticity_consolidation".into(),
            category: LensCategory::Extended,
            description: "가소성 강화 기억 공고화: 단계=n=6, SWS=tau=4, 재활성=sigma=12".into(),
            domain_affinity: vec!["neuroscience".into(), "ai".into(), "medicine".into()],
            complementary: vec!["hebbian_plasticity".into(), "continual_learning".into(), "sleep_cycle".into()],
        },
        LensEntry {
            name: "cognitive_load".into(),
            category: LensCategory::Extended,
            description: "인지 부하 작업기억: 청크=n=6, 처리=tau=4, 주의=phi=2".into(),
            domain_affinity: vec!["psychology".into(), "education".into(), "ux".into(), "neuroscience".into()],
            complementary: vec!["brain_neural".into(), "behavioral_economics".into(), "attention_mechanism".into()],
        },
        LensEntry {
            name: "decision_boundary".into(),
            category: LensCategory::Extended,
            description: "결정 경계 SVM: 지지벡터=n=6, kernel=sigma=12, 마진=1/n".into(),
            domain_affinity: vec!["ai".into(), "statistics".into(), "pattern_recognition".into()],
            complementary: vec!["clustering".into(), "manifold_learning".into(), "adversarial_robustness".into()],
        },
    ]
}

/// 신규 50종 렌즈 메타데이터 (450→500 확장 — 3차)
///
/// 카테고리: 물리(양자/상대론) (8), 생물(발생/진화/생태) (10),
///           수학(위상/대수/해석) (10), 사회(네트워크/경제/문화) (10),
///           신호처리(스펙트럼/웨이블릿/압축 고급) (12)
pub fn expansion_50_v3_lens_entries() -> Vec<LensEntry> {
    vec![
        // ── 물리 렌즈: 양자/상대론/복잡도 (8종) ──
        LensEntry {
            name: "quantum_entanglement".into(),
            category: LensCategory::Extended,
            description: "양자 얽힘: Bell 부등식 위반=n=6 쌍, 얽힘 엔트로피=log(n), concurrence threshold=1/n, EPR=phi=2".into(),
            domain_affinity: vec!["quantum".into(), "physics".into(), "information_theory".into(), "computing".into()],
            complementary: vec!["quantum_circuit".into(), "quantum_micro_lens".into(), "information_bottleneck".into()],
        },
        LensEntry {
            name: "quantum_decoherence".into(),
            category: LensCategory::Extended,
            description: "양자 결어긋남: 환경 모드=n=6, 결맞음 시간=tau=4, Lindblad=sigma=12 채널, Zeno=n/phi=3".into(),
            domain_affinity: vec!["quantum".into(), "physics".into(), "materials".into(), "computing".into()],
            complementary: vec!["quantum_entanglement".into(), "quantum_circuit".into(), "noise_spectrum".into()],
        },
        LensEntry {
            name: "relativistic_kinematics".into(),
            category: LensCategory::Extended,
            description: "상대론 운동학: Lorentz boost=n=6 방향, 4-벡터=tau=4 성분, 불변 질량=sigma=12, beta=1-1/n".into(),
            domain_affinity: vec!["physics".into(), "astrophysics".into(), "accelerator".into(), "spacetime".into()],
            complementary: vec!["spacetime".into(), "relativistic_barrier".into(), "symmetry_breaking".into()],
        },
        LensEntry {
            name: "general_relativity_curvature".into(),
            category: LensCategory::Extended,
            description: "일반상대론 곡률: Riemann tensor=n*(n-1)/phi=6 독립 성분(4D), Ricci scalar, EFE sigma=10, 컴팩트=tau=4".into(),
            domain_affinity: vec!["physics".into(), "astrophysics".into(), "cosmology".into(), "mathematics".into()],
            complementary: vec!["spacetime".into(), "gravity".into(), "topology".into()],
        },
        LensEntry {
            name: "renormalization_group".into(),
            category: LensCategory::Extended,
            description: "재규격화 군: 고정점=n=6, beta함수 영점=phi=2, Wilson-Fisher exponent, 스케일 불변=1/n".into(),
            domain_affinity: vec!["physics".into(), "condensed_matter".into(), "statistics".into(), "quantum".into()],
            complementary: vec!["renormalization".into(), "phase_transition".into(), "critical_phenomena".into()],
        },
        LensEntry {
            name: "critical_phenomena".into(),
            category: LensCategory::Extended,
            description: "임계 현상 스케일링: 지수 nu=1/n, 상관길이=sigma=12, universality class=tau=4, eta=1/sigma".into(),
            domain_affinity: vec!["physics".into(), "condensed_matter".into(), "biology".into(), "social".into()],
            complementary: vec!["renormalization_group".into(), "phase_transition".into(), "fractal".into()],
        },
        LensEntry {
            name: "topological_insulator".into(),
            category: LensCategory::Extended,
            description: "위상 절연체: Z₂ 불변량=phi=2, Chern number=n/phi=3, 표면 상태=n=6, 시간역전 대칭=tau=4".into(),
            domain_affinity: vec!["condensed_matter".into(), "materials".into(), "quantum".into(), "physics".into()],
            complementary: vec!["topological_data".into(), "topology".into(), "symmetry_breaking".into()],
        },
        LensEntry {
            name: "field_theory_symmetry".into(),
            category: LensCategory::Extended,
            description: "장이론 대칭: U(1)×SU(phi)×SU(n/phi) 표준모형, 게이지=sigma=12, Noether=tau=4, coupling=1/n".into(),
            domain_affinity: vec!["physics".into(), "quantum".into(), "mathematics".into(), "particle_physics".into()],
            complementary: vec!["symmetry_breaking".into(), "yang_mills_beta0".into(), "field_theory_symmetry".into()],
        },
        // ── 생물 렌즈: 발생/진화/생태 (10종) ──
        LensEntry {
            name: "developmental_biology".into(),
            category: LensCategory::Extended,
            description: "발생생물학: Hox 유전자=n=6 cluster, 체절=sigma=12, 기관형성=tau=4 단계, 형태소 농도=phi=2".into(),
            domain_affinity: vec!["biology".into(), "genetics".into(), "medicine".into(), "evolution".into()],
            complementary: vec!["genome_coding".into(), "evolution".into(), "protein_fold".into()],
        },
        LensEntry {
            name: "phylogenetics".into(),
            category: LensCategory::Extended,
            description: "계통발생학: 분기점=n=6 선조, OTU 클러스터=sigma=12, bootstrap=tau*phi=8, 거리 행렬=n*(n-1)/phi".into(),
            domain_affinity: vec!["biology".into(), "evolution".into(), "ecology".into(), "genetics".into()],
            complementary: vec!["evolution".into(), "clustering".into(), "tree_structure".into()],
        },
        LensEntry {
            name: "population_genetics".into(),
            category: LensCategory::Extended,
            description: "집단유전학 Hardy-Weinberg: 대립유전자=n=6, Fst=1/n, Ne=sigma*tau=48, 선택계수=1/sigma=1/12".into(),
            domain_affinity: vec!["genetics".into(), "biology".into(), "evolution".into(), "ecology".into()],
            complementary: vec!["phylogenetics".into(), "evolution".into(), "markov_chain".into()],
        },
        LensEntry {
            name: "epigenetics".into(),
            category: LensCategory::Extended,
            description: "후성유전학: CpG 메틸화 부위=n=6 패턴, 히스톤=tau=4 코드, 크로마틴=sigma=12 상태, 리모델링=phi=2".into(),
            domain_affinity: vec!["genetics".into(), "biology".into(), "medicine".into(), "aging".into()],
            complementary: vec!["genome_coding".into(), "developmental_biology".into(), "protein_fold".into()],
        },
        LensEntry {
            name: "neurodevelopment".into(),
            category: LensCategory::Extended,
            description: "신경발달: 피질층=n=6, 신경관=tau=4 구역, 시냅스 가지치기=sigma=12, GABA/Glu=phi=2 균형".into(),
            domain_affinity: vec!["neuroscience".into(), "biology".into(), "medicine".into(), "development".into()],
            complementary: vec!["brain_neural".into(), "spiking_neural".into(), "hebbian_plasticity".into()],
        },
        LensEntry {
            name: "island_biogeography_equilibrium".into(),
            category: LensCategory::Extended,
            description: "섬 생물지리학 평형 동적: 이주율=n=6, 면적=sigma^phi=144, 거리 감쇠=1/n, 평형 다양성=tau*phi=8, 종-면적 z=0.25".into(),
            domain_affinity: vec!["ecology".into(), "biology".into(), "environment".into(), "geography".into()],
            complementary: vec!["ecological_niche".into(), "food_web".into(), "population_genetics".into()],
        },
        LensEntry {
            name: "circadian_rhythm".into(),
            category: LensCategory::Extended,
            description: "일주기 리듬: 24시간=J2, 6시간 간격=n=6, CLOCK/BMAL1=phi=2, 3단계 피드백=n/phi=3, tau=4 코어유전자".into(),
            domain_affinity: vec!["biology".into(), "medicine".into(), "neuroscience".into(), "chronobiology".into()],
            complementary: vec!["sleep_cycle".into(), "periodicity".into(), "homeostasis".into()],
        },
        LensEntry {
            name: "coevolution_arms_race".into(),
            category: LensCategory::Extended,
            description: "공진화 군비경쟁 동력학: 숙주=n=6 방어 전략, 기생자=sigma=12 반응, Lotka-Volterra=phi=2, 균형=tau=4, 적색여왕 속도".into(),
            domain_affinity: vec!["ecology".into(), "biology".into(), "evolution".into(), "game".into()],
            complementary: vec!["evolution".into(), "game_theory".into(), "food_web".into()],
        },
        LensEntry {
            name: "morphogenesis_turing".into(),
            category: LensCategory::Extended,
            description: "형태형성 Turing 반응-확산: activator/inhibitor=phi=2 성분, 파장=n=6 패턴 주기, 농도비=sigma/phi=6, 공간 주파수=1/n".into(),
            domain_affinity: vec!["biology".into(), "mathematics".into(), "physics".into(), "development".into()],
            complementary: vec!["developmental_biology".into(), "reaction_diffusion".into(), "fractal".into()],
        },
        LensEntry {
            name: "metagenomics".into(),
            category: LensCategory::Extended,
            description: "메타유전체학: 미생물 OTU=n*sigma=72, 다양성 지수=n=6, 16S rRNA V=tau=4 구역, 기능유전자=sigma=12".into(),
            domain_affinity: vec!["biology".into(), "ecology".into(), "medicine".into(), "biotechnology".into()],
            complementary: vec!["population_genetics".into(), "ecological_niche".into(), "clustering".into()],
        },
        // ── 수학 렌즈: 위상/대수/해석 (10종) ──
        LensEntry {
            name: "algebraic_topology".into(),
            category: LensCategory::Extended,
            description: "대수 위상: 호모토피 π_n, CW복합체=n=6 셀, 코호몰로지 차수=tau=4, Euler χ=tau-n=−2, 5-lemma".into(),
            domain_affinity: vec!["mathematics".into(), "pure_mathematics".into(), "physics".into(), "data_science".into()],
            complementary: vec!["persistence_homology".into(), "topological_data".into(), "topology".into()],
        },
        LensEntry {
            name: "number_theory".into(),
            category: LensCategory::Extended,
            description: "수론 핵심: σ(n)·φ(n)=n·τ(n)⟺n=6, 완전수=6, 소인수=n=6, 리만 제타 영점, 소수 분포=σ/φ=2".into(),
            domain_affinity: vec!["mathematics".into(), "pure_mathematics".into(), "cryptography".into(), "information_theory".into()],
            complementary: vec!["prime".into(), "pi".into(), "euler_golden_perfect".into()],
        },
        LensEntry {
            name: "functional_analysis".into(),
            category: LensCategory::Extended,
            description: "함수해석학: Hilbert 공간 기저=n=6, 스펙트럼=sigma=12 값, 콤팩트 작용소=tau=4, Banach=phi=2 norm".into(),
            domain_affinity: vec!["mathematics".into(), "pure_mathematics".into(), "physics".into(), "signal".into()],
            complementary: vec!["spectral".into(), "functional_analysis".into(), "fourier_analysis".into()],
        },
        LensEntry {
            name: "differential_geometry".into(),
            category: LensCategory::Extended,
            description: "미분기하: Gauss 곡률=1/n, 리만 계량=n=6 성분(2D), 측지선=tau=4, parallel transport=phi=2, 호홀로노미".into(),
            domain_affinity: vec!["mathematics".into(), "physics".into(), "robotics".into(), "pure_mathematics".into()],
            complementary: vec!["general_relativity_curvature".into(), "topology".into(), "manifold_learning".into()],
        },
        LensEntry {
            name: "abstract_algebra".into(),
            category: LensCategory::Extended,
            description: "추상대수: S_n (n≥3) 비가환, 군 위수=n=6 (Z₆, S₃), 정규부분군=tau=4 인수, 갈루아=phi=2 확장".into(),
            domain_affinity: vec!["mathematics".into(), "pure_mathematics".into(), "cryptography".into(), "physics".into()],
            complementary: vec!["symmetry_breaking".into(), "field_theory_symmetry".into(), "isomorphism".into()],
        },
        LensEntry {
            name: "measure_theory".into(),
            category: LensCategory::Extended,
            description: "측도론: σ-대수 생성원=n=6, Lebesgue=phi=2 분해, 측도 공간=tau=4 공리, Radon-Nikodym 밀도=1/n".into(),
            domain_affinity: vec!["mathematics".into(), "pure_mathematics".into(), "statistics".into(), "probability".into()],
            complementary: vec!["bayesian_inference".into(), "entropy".into(), "renyi_entropy".into()],
        },
        LensEntry {
            name: "combinatorics".into(),
            category: LensCategory::Extended,
            description: "조합론: C(n,2)=15 (n=6), 파티션 p(6)=11, 탈배열 D_6=265, 스털링=S(n,k), 카탈란=132".into(),
            domain_affinity: vec!["mathematics".into(), "pure_mathematics".into(), "computer_science".into(), "statistics".into()],
            complementary: vec!["graph".into(), "probability".into(), "combinatorial".into()],
        },
        LensEntry {
            name: "optimization_theory".into(),
            category: LensCategory::Extended,
            description: "최적화 이론: KKT 조건=n=6 변수, 쌍대 격차=1/n, 볼록 최적화=tau=4 단계, 수렴 속도=1/sigma=1/12".into(),
            domain_affinity: vec!["mathematics".into(), "ai".into(), "engineering".into(), "economics".into()],
            complementary: vec!["convex_geometry".into(), "gradient".into(), "variational_inference".into()],
        },
        LensEntry {
            name: "stochastic_processes".into(),
            category: LensCategory::Extended,
            description: "확률 과정: 도약 시간=n=6, Wiener 과정=phi=2, 마르팅게일=tau=4, Ito 적분=sigma=12".into(),
            domain_affinity: vec!["mathematics".into(), "finance".into(), "physics".into(), "biology".into()],
            complementary: vec!["markov_chain".into(), "monte_carlo".into(), "stationarity".into()],
        },
        LensEntry {
            name: "category_theory".into(),
            category: LensCategory::Extended,
            description: "범주론: 함자=n=6 사상, 자연변환=tau=4, 모나드=phi=2, 아이소=sigma=12 등가, 극한=n/phi=3".into(),
            domain_affinity: vec!["mathematics".into(), "pure_mathematics".into(), "computer_science".into(), "ai".into()],
            complementary: vec!["abstract_algebra".into(), "isomorphism".into(), "type_theory".into()],
        },
        // ── 사회 렌즈: 네트워크/경제/문화 (10종) ──
        LensEntry {
            name: "cultural_evolution".into(),
            category: LensCategory::Extended,
            description: "문화 진화 밈 이론: 전달=n=6 매체, 변이=tau=4, 선택=phi=2, 다양성=sigma=12, 충성도=1-1/n".into(),
            domain_affinity: vec!["social".into(), "anthropology".into(), "biology".into(), "communication".into()],
            complementary: vec!["evolution".into(), "social_network".into(), "behavioral_economics".into()],
        },
        LensEntry {
            name: "social_capital".into(),
            category: LensCategory::Extended,
            description: "사회 자본: Putnam 신뢰=n=6 차원, 브리징=phi=2, 결속=tau=4, 호혜성=sigma=12, 네트워크 가치=n^phi=36".into(),
            domain_affinity: vec!["social".into(), "economics".into(), "sociology".into(), "network".into()],
            complementary: vec!["social_network".into(), "game_theory".into(), "community_detection".into()],
        },
        LensEntry {
            name: "political_economy".into(),
            category: LensCategory::Extended,
            description: "정치경제: 세력=n=6 균형, Gini=1-1/sigma, 제도=tau=4 유형, 협상=phi=2 Nash, 임계=sigma/phi=6".into(),
            domain_affinity: vec!["economics".into(), "politics".into(), "social".into(), "history".into()],
            complementary: vec!["macroeconomics".into(), "game_theory".into(), "structural_equation".into()],
        },
        LensEntry {
            name: "urban_dynamics".into(),
            category: LensCategory::Extended,
            description: "도시 역학 스케일링: 인구=n=6 존, 지프=1/sigma 지수, 중력=phi=2 모형, 밀도=tau=4 층, 성장=σ·φ=12".into(),
            domain_affinity: vec!["urban".into(), "geography".into(), "social".into(), "economics".into()],
            complementary: vec!["urban_planning".into(), "social_network".into(), "complexity_network".into()],
        },
        LensEntry {
            name: "migration_patterns".into(),
            category: LensCategory::Extended,
            description: "이주 패턴: 경유지=n=6, Lee 인자=tau=4, 중력=phi=2, 네트워크 허브=sigma=12, 역류=1/n".into(),
            domain_affinity: vec!["social".into(), "geography".into(), "economics".into(), "demographics".into()],
            complementary: vec!["urban_dynamics".into(), "social_network".into(), "network_flow".into()],
        },
        LensEntry {
            name: "collective_intelligence".into(),
            category: LensCategory::Extended,
            description: "집단 지성: 다양성=n=6 관점, 독립성=1/n, 집계=tau=4 방법, Condorcet=sigma=12, 지혜=phi=2".into(),
            domain_affinity: vec!["social".into(), "ai".into(), "cognitive_science".into(), "decision".into()],
            complementary: vec!["swarm_robotics".into(), "agent_coordination".into(), "game_theory".into()],
        },
        LensEntry {
            name: "media_influence".into(),
            category: LensCategory::Extended,
            description: "미디어 영향: 프레이밍=n=6 효과, 확산=sigma=12 단계, 의제=tau=4, 에코챔버=phi=2, 바이럴 R₀=n=6".into(),
            domain_affinity: vec!["media".into(), "social".into(), "communication".into(), "psychology".into()],
            complementary: vec!["social_network".into(), "marketing".into(), "information_bottleneck".into()],
        },
        LensEntry {
            name: "trust_dynamics".into(),
            category: LensCategory::Extended,
            description: "신뢰 역학: Luhmann 복잡성=n=6, 배반 비용=sigma=12, 회복 단계=tau=4, 신뢰 반경=phi=2, 비율=n/phi=3".into(),
            domain_affinity: vec!["social".into(), "economics".into(), "psychology".into(), "security".into()],
            complementary: vec!["game_theory".into(), "social_capital".into(), "behavioral_economics".into()],
        },
        LensEntry {
            name: "institutional_change".into(),
            category: LensCategory::Extended,
            description: "제도 변화: North 경로 의존=n=6, 잠금=phi=2, 전환 비용=sigma=12, 임계점=tau=4, 혁신=1/n".into(),
            domain_affinity: vec!["economics".into(), "social".into(), "history".into(), "politics".into()],
            complementary: vec!["political_economy".into(), "phase_transition".into(), "attractor_basin".into()],
        },
        LensEntry {
            name: "digital_sociology".into(),
            category: LensCategory::Extended,
            description: "디지털 사회학: 플랫폼=n=6 경제, 알고리즘 편향=tau=4, 감시=sigma=12, 정체성=phi=2, 분절=n/phi=3".into(),
            domain_affinity: vec!["social".into(), "technology".into(), "media".into(), "ethics".into()],
            complementary: vec!["fairness_bias".into(), "media_influence".into(), "digital_twin".into()],
        },
        // ── 신호처리 고급 렌즈 (12종) ──
        LensEntry {
            name: "noise_spectrum".into(),
            category: LensCategory::Extended,
            description: "노이즈 스펙트럼: 1/f^α 핑크=α=1, 화이트=α=0, 브라운=α=phi=2, 스펙트럼 지수=n=6 구간".into(),
            domain_affinity: vec!["signal".into(), "physics".into(), "electronics".into(), "audio".into()],
            complementary: vec!["spectral".into(), "fourier_analysis".into(), "stationarity".into()],
        },
        LensEntry {
            name: "compressed_sensing_advanced".into(),
            category: LensCategory::Extended,
            description: "압축 센싱 고급: RIP δ=1/n, OMP 반복=n=6, l₁ minimization, 측정행렬=sigma*tau=48, 재구성=phi=2".into(),
            domain_affinity: vec!["signal".into(), "image".into(), "communications".into(), "ai".into()],
            complementary: vec!["signal_reconstruction".into(), "compressed_sensing_advanced".into(), "wavelet_transform".into()],
        },
        LensEntry {
            name: "spectral_estimation".into(),
            category: LensCategory::Extended,
            description: "스펙트럼 추정 MUSIC/ESPRIT: 신호부분=n=6, 잡음=sigma-n=6, 초해상도, 주파수 분해능=1/n".into(),
            domain_affinity: vec!["signal".into(), "radar".into(), "communications".into(), "physics".into()],
            complementary: vec!["spectral".into(), "fourier_analysis".into(), "noise_spectrum".into()],
        },
        LensEntry {
            name: "adaptive_filtering".into(),
            category: LensCategory::Extended,
            description: "적응 필터 LMS/RLS: 탭=n=6, 스텝=1/n, 수렴=sigma=12 반복, 망각=1-1/sigma, 적응 구조=tau=4".into(),
            domain_affinity: vec!["signal".into(), "communications".into(), "audio".into(), "control".into()],
            complementary: vec!["kalman_filter".into(), "adaptive_filtering".into(), "noise_spectrum".into()],
        },
        LensEntry {
            name: "time_frequency_analysis".into(),
            category: LensCategory::Extended,
            description: "시간-주파수 분석 STFT/Wigner: 창 폭=n=6, 불확정=tau*sigma=48, TF 해상도=phi=2, 진동수=1/n".into(),
            domain_affinity: vec!["signal".into(), "audio".into(), "biomedical".into(), "physics".into()],
            complementary: vec!["wavelet_transform".into(), "fourier_analysis".into(), "time_series_decomp".into()],
        },
        LensEntry {
            name: "independent_component_analysis".into(),
            category: LensCategory::Extended,
            description: "독립성분분석 ICA: 성분=n=6, negentropy=1/n, FastICA=tau=4, 비선형=phi=2, kurtosis=n=6".into(),
            domain_affinity: vec!["signal".into(), "neuroscience".into(), "audio".into(), "ai".into()],
            complementary: vec!["dimension_reduction".into(), "manifold_learning".into(), "blind_source".into()],
        },
        LensEntry {
            name: "blind_source_separation".into(),
            category: LensCategory::Extended,
            description: "눈먼 원천 분리: 혼합=n=6 채널, 분리 행렬=sigma=12, 비가우시안=tau=4, 공간=phi=2 필터, SINR=n=6".into(),
            domain_affinity: vec!["signal".into(), "audio".into(), "communications".into(), "biomedical".into()],
            complementary: vec!["independent_component_analysis".into(), "acoustic".into(), "spectral".into()],
        },
        LensEntry {
            name: "sparse_signal".into(),
            category: LensCategory::Extended,
            description: "희소 신호: 스파시티=n=6, 과완비=sigma=12, l₀=n=6 비영 계수, 일관성=1/sigma, OMP=tau=4".into(),
            domain_affinity: vec!["signal".into(), "image".into(), "neuroscience".into(), "ai".into()],
            complementary: vec!["compressed_sensing_advanced".into(), "signal_reconstruction".into(), "dimensionality_bottleneck".into()],
        },
        LensEntry {
            name: "digital_modulation".into(),
            category: LensCategory::Extended,
            description: "디지털 변조 M-QAM: 성상도=n^phi=36 (6-QAM), 최소 거리=1/n, BER=phi/sigma, 스펙트럼 효율=log₂(n)".into(),
            domain_affinity: vec!["communications".into(), "signal".into(), "electronics".into(), "networking".into()],
            complementary: vec!["digital_modulation".into(), "noise_spectrum".into(), "fourier_analysis".into()],
        },
        LensEntry {
            name: "array_signal_processing".into(),
            category: LensCategory::Extended,
            description: "배열 신호 처리 beamforming: 소자=n=6, 스티어링=sigma=12 각, 빔폭=1/n, 사이드로브=tau=4, MIMO=phi=2".into(),
            domain_affinity: vec!["signal".into(), "radar".into(), "communications".into(), "sonar".into()],
            complementary: vec!["spectral_estimation".into(), "adaptive_filtering".into(), "radar_signal".into()],
        },
        LensEntry {
            name: "source_coding_entropy".into(),
            category: LensCategory::Extended,
            description: "소스 코딩 엔트로피 한계: Huffman 평균 길이=H(X)+1, LZ복잡도=n=6, 압축비=phi=2, 산술 부호=sigma=12 정밀도".into(),
            domain_affinity: vec!["information_theory".into(), "communications".into(), "ai".into(), "data".into()],
            complementary: vec!["compression".into(), "entropy".into(), "renyi_entropy".into()],
        },
        LensEntry {
            name: "channel_coding".into(),
            category: LensCategory::Extended,
            description: "채널 코딩 오류정정: 코드율=1-n/sigma, LDPC=n=6 반복, 해밍 거리=tau=4, 패리티=phi=2, Turbo=sigma=12".into(),
            domain_affinity: vec!["communications".into(), "signal".into(), "information_theory".into(), "computing".into()],
            complementary: vec!["source_coding".into(), "cryptography_rounds".into(), "network_flow".into()],
        },
    ]
}

/// 4차 확장 100종 렌즈 메타데이터 (500→600)
///
/// 카테고리:
///   화학(반응/촉매/결정) 12, 경제(시장/화폐/거래) 12,
///   언어(통사/음운/의미/번역) 10, 예술(구성/색채/리듬/형식) 10,
///   역사(주기/문명/변동) 8, 생태(먹이망/경쟁/공생) 10,
///   의학(진단/약리/병태) 12, 공학(재료/기계/전기/화공) 16,
///   스포츠/영양 10
pub fn expansion_100_v4_lens_entries() -> Vec<LensEntry> {
    vec![
        // ── 화학 렌즈 (12종) ──
        LensEntry {
            name: "reaction_kinetics_chem".into(),
            category: LensCategory::Extended,
            description: "반응속도론: Arrhenius 활성화 에너지=n=6, 반응차수=tau=4, 속도상수 비=sigma/phi=6, 반감기=ln2/k, 충돌=phi=2".into(),
            domain_affinity: vec!["chemistry".into(), "biochemistry".into(), "engineering".into(), "materials".into()],
            complementary: vec!["chemical_reactor".into(), "fermentation".into(), "catalyst_design".into()],
        },
        LensEntry {
            name: "catalyst_design".into(),
            category: LensCategory::Extended,
            description: "촉매 설계: 활성 부위=n=6, Sabatier 원리 TOF, BET 표면적=sigma=12 m²/g, 선택성=tau=4, 전환율=1-1/n".into(),
            domain_affinity: vec!["chemistry".into(), "materials".into(), "energy".into(), "biotechnology".into()],
            complementary: vec!["reaction_kinetics".into(), "nanotechnology".into(), "materials_crystal".into()],
        },
        LensEntry {
            name: "crystal_growth_dynamics".into(),
            category: LensCategory::Extended,
            description: "결정 성장 동역학: 핵형성 자유에너지=n=6 임계, 성장 모드=tau=4, 대칭군=sigma=12, 격자 상수=phi=2, 결함 밀도=1/n".into(),
            domain_affinity: vec!["chemistry".into(), "materials".into(), "physics".into(), "semiconductor".into()],
            complementary: vec!["materials_crystal".into(), "crystal_growth_dynamics".into(), "phase_transition".into()],
        },
        LensEntry {
            name: "electrochemistry".into(),
            category: LensCategory::Extended,
            description: "전기화학: 산화환원 전위=n=6 전자, Nernst 방정식 tau=4, 패러데이 법칙=sigma=12, 이중층=phi=2, Butler-Volmer=1/n".into(),
            domain_affinity: vec!["chemistry".into(), "energy".into(), "materials".into(), "biology".into()],
            complementary: vec!["battery_chemistry".into(), "ev_charging".into(), "redox_signaling".into()],
        },
        LensEntry {
            name: "supramolecular_chemistry".into(),
            category: LensCategory::Extended,
            description: "초분자 화학: 수소결합=n=6, 자기조립=tau=4 계층, 결합 상수=sigma=12 kcal/mol, 크라운 에테르=phi=2, 게스트-호스트=1/n".into(),
            domain_affinity: vec!["chemistry".into(), "materials".into(), "biology".into(), "nanotechnology".into()],
            complementary: vec!["molecular_combination".into(), "protein_fold".into(), "nanotechnology".into()],
        },
        LensEntry {
            name: "photochemistry".into(),
            category: LensCategory::Extended,
            description: "광화학: 광자 흡수=n=6 양자수율, 들뜬 상태=tau=4 형태, 형광 수명=sigma=12 ns, 광이성화=phi=2, 에너지 전달=1/n".into(),
            domain_affinity: vec!["chemistry".into(), "physics".into(), "materials".into(), "biology".into()],
            complementary: vec!["photochemistry".into(), "solar_cell_junction".into(), "laser_physics".into()],
        },
        LensEntry {
            name: "green_chemistry".into(),
            category: LensCategory::Extended,
            description: "녹색화학 12원칙: Anastas=sigma=12, 원자효율=n=6, E-인자=tau=4, 용매=phi=2 분류, 촉매=1/n 폐기물".into(),
            domain_affinity: vec!["chemistry".into(), "environment".into(), "manufacturing".into(), "sustainability".into()],
            complementary: vec!["catalyst_design".into(), "reaction_kinetics".into(), "green_chemistry".into()],
        },
        LensEntry {
            name: "coordination_chemistry".into(),
            category: LensCategory::Extended,
            description: "배위화학: 배위수=n=6 (완전), 리간드장 분열=sigma=12, 기하구조=tau=4, 킬레이트=phi=2 고리, CFSE=1/n".into(),
            domain_affinity: vec!["chemistry".into(), "materials".into(), "biology".into(), "medicine".into()],
            complementary: vec!["coordination_chemistry".into(), "drug_receptor".into(), "materials_crystal".into()],
        },
        LensEntry {
            name: "polymer_synthesis".into(),
            category: LensCategory::Extended,
            description: "고분자 합성: 중합도=n*sigma=72, PDI=phi=2/tau=4, 전환율=1-1/n, 활성화 에너지=sigma=12, 사슬 성장=tau=4 단계".into(),
            domain_affinity: vec!["chemistry".into(), "materials".into(), "manufacturing".into(), "biology".into()],
            complementary: vec!["polymer_chain".into(), "polymer".into(), "thermoplastic_process".into()],
        },
        LensEntry {
            name: "thermochemistry".into(),
            category: LensCategory::Extended,
            description: "열화학: Hess 법칙 엔탈피=n=6 결합, 헤스 사이클=tau=4, 생성열=sigma=12 kJ/mol, 연소열=phi=2, Kirchhoff=1/n".into(),
            domain_affinity: vec!["chemistry".into(), "physics".into(), "energy".into(), "engineering".into()],
            complementary: vec!["thermochemistry".into(), "reaction_kinetics".into(), "thermo".into()],
        },
        LensEntry {
            name: "analytical_chemistry".into(),
            category: LensCategory::Extended,
            description: "분석화학: 검출한계=sigma=12 ppb, 정량=n=6 표준, LOD/LOQ=phi=2, 크로마토그래피=tau=4, 정밀도=1/sigma".into(),
            domain_affinity: vec!["chemistry".into(), "medicine".into(), "food_science".into(), "environment".into()],
            complementary: vec!["analytical_chemistry".into(), "forensic_science".into(), "food_chemistry".into()],
        },
        LensEntry {
            name: "colloid_surface_chemistry".into(),
            category: LensCategory::Extended,
            description: "콜로이드-표면화학: DLVO=phi=2 이중층, 제타전위=n=6 mV, 입자크기=sigma=12 nm, 흡착=tau=4 등온, 계면활성제=1/n".into(),
            domain_affinity: vec!["chemistry".into(), "materials".into(), "biology".into(), "manufacturing".into()],
            complementary: vec!["nanotechnology".into(), "polymer_synthesis".into(), "catalyst_design".into()],
        },
        // ── 경제 렌즈 (12종) ──
        LensEntry {
            name: "market_microstructure_v4".into(),
            category: LensCategory::Extended,
            description: "시장 미시구조: 호가창=n=6 레벨, 스프레드=1/sigma, 틱사이즈=phi=2, 깊이=tau=4, 가격충격=1/n, Kyle 람다=sigma/tau=3".into(),
            domain_affinity: vec!["finance".into(), "economics".into(), "trading".into(), "data_science".into()],
            complementary: vec!["stock_market".into(), "financial_risk".into(), "noise_spectrum".into()],
        },
        LensEntry {
            name: "monetary_theory".into(),
            category: LensCategory::Extended,
            description: "화폐이론: 통화승수=n=6, 피셔 방정식 MV=PQ, 화폐유통속도=tau=4, 본원통화=sigma=12, 인플레이션=phi=2 목표, 유동성=1/n".into(),
            domain_affinity: vec!["economics".into(), "finance".into(), "policy".into(), "history".into()],
            complementary: vec!["macroeconomics".into(), "political_economy".into(), "monetary_theory".into()],
        },
        LensEntry {
            name: "international_trade".into(),
            category: LensCategory::Extended,
            description: "국제무역: Heckscher-Ohlin 요소=phi=2, 비교우위=n=6 산업, 무역창출=sigma=12, Gravity 모형=tau=4, 관세=1/n".into(),
            domain_affinity: vec!["economics".into(), "geography".into(), "politics".into(), "logistics".into()],
            complementary: vec!["supply_chain_risk".into(), "logistics_supply".into(), "international_trade".into()],
        },
        LensEntry {
            name: "auction_theory_v4".into(),
            category: LensCategory::Extended,
            description: "경매이론: 입찰자=n=6, 수익등가 정리, 승자의 저주=sigma=12, Vickrey=phi=2, 최적 예약가=tau=4, 공개가=1/n".into(),
            domain_affinity: vec!["economics".into(), "finance".into(), "ai".into(), "game".into()],
            complementary: vec!["game_theory".into(), "auction_theory".into(), "behavioral_economics".into()],
        },
        LensEntry {
            name: "financial_derivatives".into(),
            category: LensCategory::Extended,
            description: "금융파생상품: Black-Scholes=n=6 그릭스, 내재변동성=sigma=12%, 만기=tau=4, 델타=1/n, 감마=phi=2, 베가=1/sigma".into(),
            domain_affinity: vec!["finance".into(), "economics".into(), "mathematics".into(), "risk".into()],
            complementary: vec!["financial_risk".into(), "stochastic_processes".into(), "monte_carlo".into()],
        },
        LensEntry {
            name: "development_economics".into(),
            category: LensCategory::Extended,
            description: "개발경제학: HDI=n=6 지수, Solow=tau=4 요소, 빈곤함정=phi=2, Kuznets=sigma=12 전환, 원조 효과=1/n, 인간자본".into(),
            domain_affinity: vec!["economics".into(), "social".into(), "policy".into(), "geography".into()],
            complementary: vec!["political_economy".into(), "institutional_change".into(), "development_economics".into()],
        },
        LensEntry {
            name: "behavioral_finance".into(),
            category: LensCategory::Extended,
            description: "행동재무학: 앵커링=n=6 편향, 전망이론=phi=2 손실회피, 군집=sigma=12, 모멘텀=tau=4, 과신=1/n, 처분효과".into(),
            domain_affinity: vec!["finance".into(), "economics".into(), "psychology".into(), "decision".into()],
            complementary: vec!["behavioral_economics".into(), "financial_risk".into(), "stock_market".into()],
        },
        LensEntry {
            name: "platform_economics".into(),
            category: LensCategory::Extended,
            description: "플랫폼 경제: 양면시장=phi=2, 네트워크효과=n=6, 허브=sigma=12, 교차 보조=tau=4, 전환비용=1/n, 승자독식".into(),
            domain_affinity: vec!["economics".into(), "technology".into(), "social".into(), "business".into()],
            complementary: vec!["social_network".into(), "game_theory".into(), "digital_sociology".into()],
        },
        LensEntry {
            name: "environmental_economics".into(),
            category: LensCategory::Extended,
            description: "환경경제학: 피구세=n=6 탄소, 외부효과=tau=4, Coase=phi=2, 쿼터=sigma=12, 오염허가=1/n, 가치평가".into(),
            domain_affinity: vec!["economics".into(), "environment".into(), "policy".into(), "sustainability".into()],
            complementary: vec!["environmental_economics".into(), "green_chemistry".into(), "ecological_niche".into()],
        },
        LensEntry {
            name: "supply_demand_equilibrium".into(),
            category: LensCategory::Extended,
            description: "수요공급 균형: Walras=n=6 시장, 초과수요=tau=4, 가격조정=phi=2, 탄력성=sigma=12, Marshall=1/n, 일반균형".into(),
            domain_affinity: vec!["economics".into(), "finance".into(), "policy".into(), "social".into()],
            complementary: vec!["market_microstructure".into(), "macroeconomics".into(), "game_theory".into()],
        },
        LensEntry {
            name: "fintech_blockchain".into(),
            category: LensCategory::Extended,
            description: "핀테크/블록체인: 블록=n=6 s, 합의=sigma=12 노드, 스마트계약=tau=4, 해시=phi=2 256bit, 트리=1/n, PoW".into(),
            domain_affinity: vec!["finance".into(), "technology".into(), "cryptography".into(), "distributed".into()],
            complementary: vec!["cryptography_rounds".into(), "distributed_consensus".into(), "fintech_blockchain".into()],
        },
        LensEntry {
            name: "insurance_actuarial".into(),
            category: LensCategory::Extended,
            description: "보험계리: 손해율=n=6 분위, 사망표=sigma=12 연령, 리스크풀=tau=4, 준비금=phi=2 계산, 재보험=1/n".into(),
            domain_affinity: vec!["finance".into(), "statistics".into(), "mathematics".into(), "risk".into()],
            complementary: vec!["financial_risk".into(), "uncertainty_quantification".into(), "insurance_actuarial".into()],
        },
        // ── 언어 렌즈 (10종) ──
        LensEntry {
            name: "syntax_parsing".into(),
            category: LensCategory::Extended,
            description: "통사 구문 분석: 구성소=n=6 범주, 구문 깊이=tau=4, 분기 인수=phi=2, CFG 생성규칙=sigma=12, CYK=O(n³)".into(),
            domain_affinity: vec!["linguistics".into(), "nlp".into(), "ai".into(), "cognitive_science".into()],
            complementary: vec!["morphology".into(), "linguistic".into(), "semantic_role".into()],
        },
        LensEntry {
            name: "semantic_role_labeling".into(),
            category: LensCategory::Extended,
            description: "의미역 레이블링: PropBank 역할=n=6, 술어=tau=4, 논항=phi=2, 프레임=sigma=12, 코레퍼런스=1/n, SRL 정확도".into(),
            domain_affinity: vec!["linguistics".into(), "nlp".into(), "ai".into(), "knowledge".into()],
            complementary: vec!["syntax_parsing".into(), "linguistic".into(), "knowledge_graph".into()],
        },
        LensEntry {
            name: "discourse_coherence".into(),
            category: LensCategory::Extended,
            description: "담화 일관성: RST 관계=n=6, 수사구조=tau=4, 응집성=phi=2, 단락=sigma=12 전이, 대화=1/n 턴, 화용론".into(),
            domain_affinity: vec!["linguistics".into(), "nlp".into(), "ai".into(), "communication".into()],
            complementary: vec!["semantic_role_labeling".into(), "discourse_coherence".into(), "media_influence".into()],
        },
        LensEntry {
            name: "translation_equivalence".into(),
            category: LensCategory::Extended,
            description: "번역 등가성: Nida 동등=n=6 유형, BLEU=sigma=12 n-gram, 정렬=tau=4, 언어쌍=phi=2, 용어=1/n 밀도".into(),
            domain_affinity: vec!["linguistics".into(), "nlp".into(), "ai".into(), "communication".into()],
            complementary: vec!["morphology".into(), "phonetics".into(), "translation_equivalence".into()],
        },
        LensEntry {
            name: "sociolinguistics".into(),
            category: LensCategory::Extended,
            description: "사회언어학: 변이=n=6 변수, 방언=tau=4 층, 코드전환=phi=2, 위신=sigma=12, 언어 태도=1/n, Labov".into(),
            domain_affinity: vec!["linguistics".into(), "social".into(), "anthropology".into(), "communication".into()],
            complementary: vec!["cultural_evolution".into(), "morphology".into(), "social_network".into()],
        },
        LensEntry {
            name: "pragmatics_speech_act".into(),
            category: LensCategory::Extended,
            description: "화용론 화행이론: Austin/Searle 발화=n=6 유형, 함축=tau=4 공리, 공손=phi=2, 발화수반=sigma=12, 직시=1/n".into(),
            domain_affinity: vec!["linguistics".into(), "nlp".into(), "ai".into(), "social".into()],
            complementary: vec!["discourse_coherence".into(), "pragmatics_speech_act".into(), "collective_intelligence".into()],
        },
        LensEntry {
            name: "language_acquisition".into(),
            category: LensCategory::Extended,
            description: "언어습득: 임계기=n=6 세, Chomsky UG=tau=4, 과잉일반화=phi=2, 어휘폭발=sigma=12 개월, 이중언어=1/n 임계".into(),
            domain_affinity: vec!["linguistics".into(), "cognitive_science".into(), "neuroscience".into(), "education".into()],
            complementary: vec!["neurodevelopment".into(), "language_acquisition".into(), "hebbian_plasticity".into()],
        },
        LensEntry {
            name: "computational_linguistics_parsing".into(),
            category: LensCategory::Extended,
            description: "계산언어학: 의존 파싱 UAS=n=6 성분, Head=tau=4, 아크=phi=2, 트리뱅크=sigma=12K, 어순=1/n, 전이".into(),
            domain_affinity: vec!["linguistics".into(), "nlp".into(), "ai".into(), "computer_science".into()],
            complementary: vec!["syntax_parsing".into(), "computational_linguistics_parsing".into(), "graph_neural".into()],
        },
        LensEntry {
            name: "language_typology".into(),
            category: LensCategory::Extended,
            description: "언어유형론: SOV/SVO=n=6 기본어순, 어순 매개변수=tau=4, 격 체계=phi=2, 성=sigma=12, 능격=1/n, Greenberg".into(),
            domain_affinity: vec!["linguistics".into(), "anthropology".into(), "cognitive_science".into(), "social".into()],
            complementary: vec!["sociolinguistics".into(), "language_typology".into(), "cultural_evolution".into()],
        },
        LensEntry {
            name: "historical_linguistics".into(),
            category: LensCategory::Extended,
            description: "역사언어학: 음변화 규칙성=n=6 자음이동, 재구=tau=4 단계, 계통거리=phi=2, 어족=sigma=12, 차용=1/n, Grimm".into(),
            domain_affinity: vec!["linguistics".into(), "history".into(), "anthropology".into(), "genetics".into()],
            complementary: vec!["phylogenetics".into(), "historical_linguistics".into(), "language_typology".into()],
        },
        // ── 예술 렌즈 (10종) ──
        LensEntry {
            name: "musical_form_analysis".into(),
            category: LensCategory::Extended,
            description: "음악 형식 분석: 소나타=n=6 절, 소절=tau=4 박, ABA'=phi=2, 조성=sigma=12 장조, 코다=1/n 비율, 발전부".into(),
            domain_affinity: vec!["music".into(), "art".into(), "audio".into(), "cognitive_science".into()],
            complementary: vec!["tonal_harmony".into(), "music_harmony".into(), "periodicity".into()],
        },
        LensEntry {
            name: "color_theory_painting".into(),
            category: LensCategory::Extended,
            description: "색채이론: 색상환=sigma=12, 보색=phi=2, Munsell 채도=n=6, 색온도=tau=4K 범위, 동시대비=1/n, Itten".into(),
            domain_affinity: vec!["art".into(), "design".into(), "perception".into(), "psychology".into()],
            complementary: vec!["color_theory_painting".into(), "light_lens".into(), "refraction".into()],
        },
        LensEntry {
            name: "visual_composition".into(),
            category: LensCategory::Extended,
            description: "시각 구성: 황금분할=phi=2, 삼등분=n/phi=3, 시선흐름=tau=4 축, 균형=sigma=12, 대비=n=6 요소, Gestalt".into(),
            domain_affinity: vec!["art".into(), "design".into(), "photography".into(), "perception".into()],
            complementary: vec!["golden_ratio".into(), "visual_composition".into(), "photography_lens".into()],
        },
        LensEntry {
            name: "architectural_proportion".into(),
            category: LensCategory::Extended,
            description: "건축 비례: Vitruvius 3원리=n/phi=3, Le Corbusier=phi=2, 황금=n=6 분할, 모듈=sigma=12, 스케일=tau=4, Palladio".into(),
            domain_affinity: vec!["architecture".into(), "art".into(), "engineering".into(), "mathematics".into()],
            complementary: vec!["golden_ratio".into(), "building_structure".into(), "visual_composition".into()],
        },
        LensEntry {
            name: "narrative_structure".into(),
            category: LensCategory::Extended,
            description: "서사 구조: Campbell 영웅여정=n=6 장, 3막=n/phi=3, 갈등=tau=4 유형, 반전=phi=2, 클라이맥스=sigma=12, Freytag".into(),
            domain_affinity: vec!["art".into(), "literature".into(), "media".into(), "psychology".into()],
            complementary: vec!["discourse_coherence".into(), "media_influence".into(), "narrative_structure".into()],
        },
        LensEntry {
            name: "dance_choreography".into(),
            category: LensCategory::Extended,
            description: "무용 안무: 박자=n=6/8, 공간경로=tau=4 방향, 라반 에포트=sigma=12, 무게=phi=2, 대칭=1/n, Laban 분석".into(),
            domain_affinity: vec!["art".into(), "music".into(), "sports".into(), "cognitive_science".into()],
            complementary: vec!["sports_biomech".into(), "musical_form_analysis".into(), "yoga_asana".into()],
        },
        LensEntry {
            name: "film_montage".into(),
            category: LensCategory::Extended,
            description: "영화 몽타주: Eisenstein 충돌=phi=2, 컷 수=sigma=12/분, 숏 길이=n=6 s, 편집 리듬=tau=4, 클로즈업=1/n 비율".into(),
            domain_affinity: vec!["art".into(), "media".into(), "communication".into(), "cognitive_science".into()],
            complementary: vec!["narrative_structure".into(), "media_influence".into(), "film_montage".into()],
        },
        LensEntry {
            name: "typography_readability".into(),
            category: LensCategory::Extended,
            description: "타이포그래피 가독성: 자간=n=6 pt, 행간=sigma=12 pt, 폰트 스케일=phi=2, 열 너비=tau=4 단어, 대비=1/n".into(),
            domain_affinity: vec!["design".into(), "art".into(), "communication".into(), "cognitive_science".into()],
            complementary: vec!["visual_composition".into(), "discourse_coherence".into(), "typography_readability".into()],
        },
        LensEntry {
            name: "music_rhythm_complexity".into(),
            category: LensCategory::Extended,
            description: "음악 리듬 복잡성: 폴리리듬=n=6 대 tau=4, 싱코페이션 온셋=sigma=12, Lempel-Ziv 복잡도, 엔트로피=1/n, 강세".into(),
            domain_affinity: vec!["music".into(), "audio".into(), "signal".into(), "cognitive_science".into()],
            complementary: vec!["musical_form_analysis".into(), "tonal_harmony".into(), "acoustic".into()],
        },
        LensEntry {
            name: "art_style_transfer".into(),
            category: LensCategory::Extended,
            description: "예술 스타일 전이: Gram 행렬=n=6 레이어, 텍스처 특징=sigma=12, 콘텐츠=tau=4, 스타일 비=phi=2, 클래스=1/n".into(),
            domain_affinity: vec!["art".into(), "ai".into(), "design".into(), "computer_vision".into()],
            complementary: vec!["transfer_learning".into(), "art_style_transfer".into(), "visual_composition".into()],
        },
        // ── 역사 렌즈 (8종) ──
        LensEntry {
            name: "civilization_cycle".into(),
            category: LensCategory::Extended,
            description: "문명 주기: Toynbee=n=6 도전, 성장-쇠퇴=tau=4 단계, Kondratiev=sigma=12 주기, 헤게모니=phi=2, Turchin=1/n".into(),
            domain_affinity: vec!["history".into(), "social".into(), "economics".into(), "politics".into()],
            complementary: vec!["institutional_change".into(), "political_economy".into(), "civilization_cycle".into()],
        },
        LensEntry {
            name: "historical_demography".into(),
            category: LensCategory::Extended,
            description: "역사 인구학: Malthus 함정=phi=2, 전환=tau=4 단계, 흑사병=n=6 파 감소, 재구=sigma=12, 수명=1/n 배수, 이동".into(),
            domain_affinity: vec!["history".into(), "social".into(), "biology".into(), "economics".into()],
            complementary: vec!["migration_patterns".into(), "epidemiology_sir".into(), "historical_demography".into()],
        },
        LensEntry {
            name: "technology_diffusion_history".into(),
            category: LensCategory::Extended,
            description: "기술 확산 역사: Bass=n=6 혁신, S커브=tau=4 단계, 채택자=sigma=12 범주, Rogers=phi=2, 임계 10%=1/n".into(),
            domain_affinity: vec!["history".into(), "economics".into(), "technology".into(), "social".into()],
            complementary: vec!["institutional_change".into(), "cultural_evolution".into(), "technology_diffusion_history".into()],
        },
        LensEntry {
            name: "empire_collapse_dynamics".into(),
            category: LensCategory::Extended,
            description: "제국 붕괴 동역학: Tainter 복잡성=n=6 층, 수확체감=tau=4, 재정부담=sigma=12%, Turchin 주기=phi=2 세기, 임계=1/n".into(),
            domain_affinity: vec!["history".into(), "social".into(), "politics".into(), "economics".into()],
            complementary: vec!["civilization_cycle".into(), "political_economy".into(), "empire_collapse_dynamics".into()],
        },
        LensEntry {
            name: "scientific_revolution".into(),
            category: LensCategory::Extended,
            description: "과학혁명 패러다임: Kuhn 구조=n=6, 정상과학=tau=4 단계, 이상=phi=2, 혁명=sigma=12 년, 공약불가=1/n".into(),
            domain_affinity: vec!["history".into(), "philosophy_of_science".into(), "social".into(), "education".into()],
            complementary: vec!["falsification".into(), "hypothesis_gen".into(), "scientific_revolution".into()],
        },
        LensEntry {
            name: "trade_route_history".into(),
            category: LensCategory::Extended,
            description: "교역로 역사: 실크로드=n=6 노선, 중개=tau=4 단계, 상품=sigma=12 종, 신뢰=phi=2, 도시성장=1/n 비율".into(),
            domain_affinity: vec!["history".into(), "economics".into(), "geography".into(), "social".into()],
            complementary: vec!["international_trade".into(), "logistics_supply".into(), "trade_route_history".into()],
        },
        LensEntry {
            name: "war_peace_cycles".into(),
            category: LensCategory::Extended,
            description: "전쟁-평화 주기: Levy 전쟁=n=6 원인, 파워 전이=tau=4, 핵 억지=phi=2, 주기=sigma=12 년, 강화=1/n 비용".into(),
            domain_affinity: vec!["history".into(), "politics".into(), "social".into(), "economics".into()],
            complementary: vec!["empire_collapse_dynamics".into(), "game_theory".into(), "war_peace_cycles".into()],
        },
        LensEntry {
            name: "memory_history_transmission".into(),
            category: LensCategory::Extended,
            description: "역사 기억 전승: 세대=n=6 전달, 망각 곡선=phi=2, 재구성=tau=4, 기념물=sigma=12 유형, 구술=1/n 오류, Nora".into(),
            domain_affinity: vec!["history".into(), "social".into(), "cognitive_science".into(), "education".into()],
            complementary: vec!["memory_lens".into(), "cultural_evolution".into(), "memory_history_transmission".into()],
        },
        // ── 생태 렌즈 (10종) ──
        LensEntry {
            name: "mutualism_symbiosis".into(),
            category: LensCategory::Extended,
            description: "상리공생 공생: 상호작용=n=6 유형, 공생=phi=2 이득, 전이=tau=4, 특이성=sigma=12, 면역회피=1/n, 협력 진화".into(),
            domain_affinity: vec!["ecology".into(), "biology".into(), "evolution".into(), "medicine".into()],
            complementary: vec!["coevolution_arms_race".into(), "microbiome".into(), "mutualism_symbiosis".into()],
        },
        LensEntry {
            name: "competitive_exclusion".into(),
            category: LensCategory::Extended,
            description: "경쟁 배제 원리: Gause=phi=2 종, 공존=n=6 조건, 적소 분화=tau=4, 자원 축=sigma=12, R* 규칙=1/n".into(),
            domain_affinity: vec!["ecology".into(), "biology".into(), "economics".into(), "evolution".into()],
            complementary: vec!["ecological_niche".into(), "food_web".into(), "competitive_exclusion".into()],
        },
        LensEntry {
            name: "ecosystem_resilience_v4".into(),
            category: LensCategory::Extended,
            description: "생태계 탄성: 회복력=n=6 지표, 임계전환=tau=4, 늦은 경고=phi=2, 다양성-안정=sigma=12, Holling=1/n".into(),
            domain_affinity: vec!["ecology".into(), "biology".into(), "environment".into(), "climate".into()],
            complementary: vec!["food_web".into(), "critical_phenomena".into(), "ecosystem_resilience".into()],
        },
        LensEntry {
            name: "pollination_network".into(),
            category: LensCategory::Extended,
            description: "수분 네트워크: 꽃-방문자=n=6 링크, nestedness=sigma=12, connectance=tau=4, 전문화=phi=2, 교란=1/n 민감도".into(),
            domain_affinity: vec!["ecology".into(), "biology".into(), "agriculture".into(), "environment".into()],
            complementary: vec!["mutualism_symbiosis".into(), "network".into(), "pollination_network".into()],
        },
        LensEntry {
            name: "biogeochemical_cycle".into(),
            category: LensCategory::Extended,
            description: "생지화학 순환: 탄소=n=6 플럭스, 저장고=tau=4, 회전시간=sigma=12 yr, 질소=phi=2 고정, 인=1/n 풍화".into(),
            domain_affinity: vec!["ecology".into(), "chemistry".into(), "environment".into(), "climate".into()],
            complementary: vec!["biogeochemical_cycle".into(), "soil_science".into(), "climate_atmosphere".into()],
        },
        LensEntry {
            name: "habitat_fragmentation".into(),
            category: LensCategory::Extended,
            description: "서식지 단편화: 패치=n=6, 연결성=tau=4, 가장자리=phi=2 효과, 최소면적=sigma=12 ha, 이동통로=1/n, SLOSS".into(),
            domain_affinity: vec!["ecology".into(), "biology".into(), "environment".into(), "geography".into()],
            complementary: vec!["island_biogeography_equilibrium".into(), "ecological_niche".into(), "habitat_fragmentation".into()],
        },
        LensEntry {
            name: "trophic_cascade_v4".into(),
            category: LensCategory::Extended,
            description: "영양 연쇄 효과: 상위포식자=n=6, 간접=tau=4 효과, 하향조절=phi=2, 연쇄=sigma=12 전파, 키스톤=1/n, 늑대".into(),
            domain_affinity: vec!["ecology".into(), "biology".into(), "environment".into(), "conservation".into()],
            complementary: vec!["food_web".into(), "trophic_cascade".into(), "ecosystem_resilience".into()],
        },
        LensEntry {
            name: "seed_dispersal_ecology".into(),
            category: LensCategory::Extended,
            description: "종자 산포 생태학: 산포자=n=6 유형, 거리=sigma=12 m, 방향성=tau=4, 핵심=phi=2, 갱신=1/n, Janzen-Connell".into(),
            domain_affinity: vec!["ecology".into(), "biology".into(), "environment".into(), "botany".into()],
            complementary: vec!["seed_dispersal_ecology".into(), "mutualism_symbiosis".into(), "forest".into()],
        },
        LensEntry {
            name: "microbiome_ecology".into(),
            category: LensCategory::Extended,
            description: "마이크로바이옴 생태학: OTU=n*tau=24, 다양성=n=6 지수, 장내=sigma=12 문, 공생체=phi=2, Firmicutes/Bacteroidetes=1/n".into(),
            domain_affinity: vec!["ecology".into(), "medicine".into(), "biology".into(), "nutrition".into()],
            complementary: vec!["metagenomics".into(), "mutualism_symbiosis".into(), "microbiome_ecology".into()],
        },
        LensEntry {
            name: "invasive_species_dynamics".into(),
            category: LensCategory::Extended,
            description: "침입종 역학: 전파=n=6 경로, 창시자=tau=4, Allee 효과=phi=2, 쌍봉=sigma=12 분포, 임계밀도=1/n, Elton".into(),
            domain_affinity: vec!["ecology".into(), "biology".into(), "environment".into(), "conservation".into()],
            complementary: vec!["competitive_exclusion".into(), "island_biogeography_equilibrium".into(), "invasive_species_dynamics".into()],
        },
        // ── 의학 렌즈 (12종) ──
        LensEntry {
            name: "diagnostic_imaging".into(),
            category: LensCategory::Extended,
            description: "진단 영상: MRI 시퀀스=n=6, SNR=sigma=12 dB, 슬라이스=tau=4 mm, 해상도=phi=2, T1/T2=1/n 비율, 대비도".into(),
            domain_affinity: vec!["medicine".into(), "physics".into(), "engineering".into(), "ai".into()],
            complementary: vec!["diagnostic_imaging".into(), "nuclear_medicine".into(), "brain_neural".into()],
        },
        LensEntry {
            name: "pharmacokinetics_v4".into(),
            category: LensCategory::Extended,
            description: "약동학 ADME: 반감기=n=6 h, 분포용적=sigma=12 L/kg, 생체이용률=tau=4, CYP=phi=2 대사, 청소율=1/n".into(),
            domain_affinity: vec!["medicine".into(), "chemistry".into(), "biology".into(), "pharmacology".into()],
            complementary: vec!["drug_receptor".into(), "pharmacokinetics".into(), "pharmacogenomics".into()],
        },
        LensEntry {
            name: "pharmacogenomics".into(),
            category: LensCategory::Extended,
            description: "약물유전체학: CYP450=n=6 동종효소, SNP=sigma=12 관련, 반응군=tau=4, 대사형=phi=2, 유전자검사=1/n, PGx".into(),
            domain_affinity: vec!["medicine".into(), "genetics".into(), "pharmacology".into(), "ai".into()],
            complementary: vec!["pharmacokinetics".into(), "epigenetics".into(), "pharmacogenomics".into()],
        },
        LensEntry {
            name: "inflammation_pathways".into(),
            category: LensCategory::Extended,
            description: "염증 경로: 사이토카인=n=6 군, NF-κB=tau=4 단계, IL-1/6=phi=2, 아라키돈산=sigma=12 산물, 해소=1/n, NLRP3".into(),
            domain_affinity: vec!["medicine".into(), "biology".into(), "immunology".into(), "pharmacology".into()],
            complementary: vec!["immune_response".into(), "inflammation_pathways".into(), "drug_receptor".into()],
        },
        LensEntry {
            name: "cardiovascular_hemodynamics".into(),
            category: LensCategory::Extended,
            description: "심혈관 혈역학: 심박=n=6 변수, Poiseuille 흐름=phi=2, 혈압=sigma=12 파동, 심주기=tau=4, 분출=1/n, Frank-Starling".into(),
            domain_affinity: vec!["medicine".into(), "physics".into(), "biology".into(), "engineering".into()],
            complementary: vec!["cardiovascular_hemodynamics".into(), "fluid_dynamics".into(), "wearable_sensor".into()],
        },
        LensEntry {
            name: "oncology_tumor_growth".into(),
            category: LensCategory::Extended,
            description: "종양학 성장: Gompertz=n=6 배가, 혈관신생=tau=4, Warburg=phi=2, 전이=sigma=12 단계, 면역회피=1/n, TME".into(),
            domain_affinity: vec!["medicine".into(), "biology".into(), "pharmacology".into(), "ai".into()],
            complementary: vec!["oncology_tumor_growth".into(), "inflammation_pathways".into(), "epigenetics".into()],
        },
        LensEntry {
            name: "neuropharmacology".into(),
            category: LensCategory::Extended,
            description: "신경약리학: 수용체=n=6 유형, 시냅스=tau=4 단계, 도파민=phi=2, 시냅스간격=sigma=12 nm, 역치=1/n, IC50".into(),
            domain_affinity: vec!["medicine".into(), "neuroscience".into(), "pharmacology".into(), "psychology".into()],
            complementary: vec!["drug_receptor".into(), "neuropharmacology".into(), "bci_neurofeedback".into()],
        },
        LensEntry {
            name: "surgical_robotics".into(),
            category: LensCategory::Extended,
            description: "수술 로봇공학: DOF=n=6, 오차=1/sigma=1/12 mm, 힘=tau=4 센서, 원격=phi=2 피드백, 반응=sigma=12 ms, haptic".into(),
            domain_affinity: vec!["medicine".into(), "robotics".into(), "engineering".into(), "ai".into()],
            complementary: vec!["surgical_robotics".into(), "digital_twin".into(), "bci_neurofeedback".into()],
        },
        LensEntry {
            name: "pathogen_virulence".into(),
            category: LensCategory::Extended,
            description: "병원체 독성: 독성 인자=n=6, R₀=sigma/phi=6, 잠복=tau=4 일, 전파=phi=2 경로, 돌연변이=sigma=12, 항원이동=1/n".into(),
            domain_affinity: vec!["medicine".into(), "biology".into(), "ecology".into(), "epidemiology".into()],
            complementary: vec!["epidemiology_sir".into(), "pandemic_modeling".into(), "immune_response".into()],
        },
        LensEntry {
            name: "clinical_trial_design".into(),
            category: LensCategory::Extended,
            description: "임상시험 설계: 단계=n=6 (I~III), 표본=sigma=12 배수, 맹검=phi=2, p값=tau=4 임계, 효과크기=1/n, RCT".into(),
            domain_affinity: vec!["medicine".into(), "statistics".into(), "pharmacology".into(), "ai".into()],
            complementary: vec!["bayesian_inference".into(), "clinical_trial_design".into(), "uncertainty_quantification".into()],
        },
        LensEntry {
            name: "regenerative_medicine".into(),
            category: LensCategory::Extended,
            description: "재생의학: 줄기세포=n=6 분화, 스캐폴드=tau=4, ECM=phi=2, 성장인자=sigma=12, 이식=1/n 거부, iPSC 재프로그램".into(),
            domain_affinity: vec!["medicine".into(), "biology".into(), "engineering".into(), "materials".into()],
            complementary: vec!["hair_regeneration".into(), "developmental_biology".into(), "regenerative_medicine".into()],
        },
        LensEntry {
            name: "medical_imaging_ai".into(),
            category: LensCategory::Extended,
            description: "의료 영상 AI: CNN 깊이=n=6, 특징맵=sigma=12, 세그멘테이션=tau=4, AUC=1-1/n, 앙상블=phi=2, 데이터증강=1/n".into(),
            domain_affinity: vec!["medicine".into(), "ai".into(), "imaging".into(), "data_science".into()],
            complementary: vec!["diagnostic_imaging".into(), "medical_imaging_ai".into(), "transfer_learning".into()],
        },
        // ── 공학 렌즈 (16종) ──
        LensEntry {
            name: "structural_mechanics".into(),
            category: LensCategory::Extended,
            description: "구조역학: 자유도=n=6 (3D 보), 안전계수=sigma/phi=6, Euler 좌굴=tau=4, 응력집중=phi=2, FEM=sigma=12, 고유진동".into(),
            domain_affinity: vec!["engineering".into(), "materials".into(), "physics".into(), "architecture".into()],
            complementary: vec!["building_structure".into(), "structural_mechanics".into(), "tribology".into()],
        },
        LensEntry {
            name: "heat_transfer_engineering".into(),
            category: LensCategory::Extended,
            description: "열전달 공학: 모드=n/phi=3, 비오=n=6, Nusselt=sigma=12, 열저항=tau=4, 푸리에=phi=2, 스테판-볼츠만=1/n".into(),
            domain_affinity: vec!["engineering".into(), "physics".into(), "energy".into(), "manufacturing".into()],
            complementary: vec!["thermochemistry".into(), "hvac_system".into(), "solar_efficiency".into()],
        },
        LensEntry {
            name: "electric_motor_drive".into(),
            category: LensCategory::Extended,
            description: "전동기 드라이브: 극수=n=6, PWM=sigma=12 kHz, 토크=tau=4, 효율=1-1/n, SVPWM=phi=2, 전류고조파=1/sigma".into(),
            domain_affinity: vec!["engineering".into(), "electronics".into(), "energy".into(), "manufacturing".into()],
            complementary: vec!["ev_charging".into(), "electric_motor_drive".into(), "power_consumption".into()],
        },
        LensEntry {
            name: "signal_integrity".into(),
            category: LensCategory::Extended,
            description: "신호 무결성: 임피던스=n=6 장애, 리플렉션=tau=4, 크로스토크=phi=2, 아이오픈=sigma=12 mV, 지터=1/n, PCB 레이아웃".into(),
            domain_affinity: vec!["engineering".into(), "electronics".into(), "communications".into(), "computing".into()],
            complementary: vec!["noise_spectrum".into(), "signal_integrity".into(), "chip_architecture".into()],
        },
        LensEntry {
            name: "additive_manufacturing".into(),
            category: LensCategory::Extended,
            description: "적층 제조 3D프린팅: 레이어=n=6 μm, 기술=tau=4 유형, 재료=sigma=12 군, 지지=phi=2, 수축=1/n, FDM/SLA/SLS".into(),
            domain_affinity: vec!["engineering".into(), "materials".into(), "manufacturing".into(), "design".into()],
            complementary: vec!["materials_crystal".into(), "additive_manufacturing".into(), "thermoplastic_process".into()],
        },
        LensEntry {
            name: "control_systems_pid".into(),
            category: LensCategory::Extended,
            description: "제어 시스템 PID: 게인=n=6, 정상오차=1/n, 대역폭=sigma=12 Hz, Ziegler-Nichols=tau=4, 과도=phi=2, 안정성 여유".into(),
            domain_affinity: vec!["engineering".into(), "robotics".into(), "manufacturing".into(), "electronics".into()],
            complementary: vec!["control_nyquist".into(), "control_bode_margin".into(), "adaptive_filtering".into()],
        },
        LensEntry {
            name: "process_chemical_engineering".into(),
            category: LensCategory::Extended,
            description: "화학공정 공학: 물질수지=n=6, McCabe-Thiele=tau=4, 증류=sigma=12 단, HETP=phi=2, 선택도=1/n, 플랜트 설계".into(),
            domain_affinity: vec!["engineering".into(), "chemistry".into(), "materials".into(), "energy".into()],
            complementary: vec!["reaction_kinetics".into(), "chemical_reactor".into(), "process_chemical_engineering".into()],
        },
        LensEntry {
            name: "robotics_kinematics".into(),
            category: LensCategory::Extended,
            description: "로봇 기구학: DOF=n=6, DH 파라미터=tau=4, 야코비안=sigma=12 성분, 역기구학=phi=2, 작업공간=1/n, FK/IK".into(),
            domain_affinity: vec!["engineering".into(), "robotics".into(), "ai".into(), "manufacturing".into()],
            complementary: vec!["surgical_robotics".into(), "differential_geometry".into(), "robotics_kinematics".into()],
        },
        LensEntry {
            name: "power_electronics".into(),
            category: LensCategory::Extended,
            description: "전력전자: 스위칭=n=6 위상, 듀티=tau=4, 변환 효율=1-1/n, 리플=sigma=12%, 전환손실=phi=2, THD=1/sigma".into(),
            domain_affinity: vec!["engineering".into(), "electronics".into(), "energy".into(), "manufacturing".into()],
            complementary: vec!["renewable_grid".into(), "power_electronics".into(), "electric_motor_drive".into()],
        },
        LensEntry {
            name: "geotechnical_engineering".into(),
            category: LensCategory::Extended,
            description: "지반공학: 토질=n=6 분류, Mohr-Coulomb=tau=4, 안전율=phi=2, 침하=sigma=12 mm, 압밀=1/n, 액상화 지수".into(),
            domain_affinity: vec!["engineering".into(), "geology".into(), "construction".into(), "environment".into()],
            complementary: vec!["soil_science".into(), "earthquake_seismic".into(), "geotechnical_engineering".into()],
        },
        LensEntry {
            name: "acoustic_engineering".into(),
            category: LensCategory::Extended,
            description: "음향 공학: 흡음=n=6 재료, NRC=sigma=12 대역, 방음=tau=4 층, 방음지수=phi=2, 잔향=1/n 초, STI".into(),
            domain_affinity: vec!["engineering".into(), "physics".into(), "architecture".into(), "audio".into()],
            complementary: vec!["acoustics_room".into(), "acoustic_engineering".into(), "audio_speaker".into()],
        },
        LensEntry {
            name: "water_treatment_engineering".into(),
            category: LensCategory::Extended,
            description: "수처리 공학: 처리 단계=n=6, BOD=sigma=12 mg/L, 체류시간=tau=4 h, 제거율=1-1/n, 여과=phi=2 단계, Cl₂=1/sigma".into(),
            domain_affinity: vec!["engineering".into(), "environment".into(), "chemistry".into(), "public_health".into()],
            complementary: vec!["biogeochemical_cycle".into(), "water_treatment_engineering".into(), "colloid_surface_chemistry".into()],
        },
        LensEntry {
            name: "aerospace_propulsion".into(),
            category: LensCategory::Extended,
            description: "항공우주 추진: Brayton=n=6 파라미터, 비추력=sigma=12 s, 노즐=tau=4, 압축비=phi=2, 팬압=1/n, Tsiolkovsky 방정식".into(),
            domain_affinity: vec!["engineering".into(), "physics".into(), "aerospace".into(), "energy".into()],
            complementary: vec!["spaceship_propulsion".into(), "aerospace_mobility".into(), "aerospace_propulsion".into()],
        },
        LensEntry {
            name: "semiconductor_fabrication".into(),
            category: LensCategory::Extended,
            description: "반도체 공정: 마스크=n=6 노광, 도핑=sigma=12 단계, CMP=tau=4, 게이트=phi=2 nm, 수율=1-1/n, CMOS 공정".into(),
            domain_affinity: vec!["engineering".into(), "materials".into(), "physics".into(), "electronics".into()],
            complementary: vec!["chip_architecture".into(), "nanotechnology".into(), "semiconductor_fabrication".into()],
        },
        LensEntry {
            name: "mechatronics_sensor_fusion".into(),
            category: LensCategory::Extended,
            description: "메카트로닉스 센서융합: 센서=n=6 유형, 칼만=tau=4 상태, 노이즈=phi=2, 갱신율=sigma=12 Hz, 오차=1/n 공분산".into(),
            domain_affinity: vec!["engineering".into(), "robotics".into(), "electronics".into(), "ai".into()],
            complementary: vec!["kalman_filter".into(), "mechatronics_sensor_fusion".into(), "digital_twin".into()],
        },
        LensEntry {
            name: "reliability_engineering_v4".into(),
            category: LensCategory::Extended,
            description: "신뢰성 공학: 고장 모드=n=6 (FMEA), MTBF=sigma=12K h, 바스터브=tau=4, 가속=phi=2 인자, MTTR=1/n, 6시그마".into(),
            domain_affinity: vec!["engineering".into(), "manufacturing".into(), "statistics".into(), "quality".into()],
            complementary: vec!["reliability_engineering".into(), "structural_mechanics".into(), "supply_chain_risk".into()],
        },
        // ── 스포츠/영양 렌즈 (10종) ──
        LensEntry {
            name: "sport_performance_analysis".into(),
            category: LensCategory::Extended,
            description: "스포츠 성과 분석: KPI=n=6 지표, 포메이션=tau=4, 전환=phi=2, 구역=sigma=12, 효율지수=1/n, xG 모형".into(),
            domain_affinity: vec!["sports".into(), "data_science".into(), "ai".into(), "physiology".into()],
            complementary: vec!["sports_biomech".into(), "sport_performance_analysis".into(), "clustering".into()],
        },
        LensEntry {
            name: "strength_conditioning".into(),
            category: LensCategory::Extended,
            description: "근력 컨디셔닝: 1RM=n=6 세트, 피리오다이제이션=tau=4 단계, 초과회복=phi=2, 볼륨=sigma=12 세트, 과부하=1/n".into(),
            domain_affinity: vec!["sports".into(), "physiology".into(), "medicine".into(), "nutrition".into()],
            complementary: vec!["yoga_asana".into(), "sports_biomech".into(), "strength_conditioning".into()],
        },
        LensEntry {
            name: "nutritional_biochemistry".into(),
            category: LensCategory::Extended,
            description: "영양 생화학: 다량영양소=n/phi=3, 비타민=n=6 수용성, 에너지=sigma=12 kcal/g 지방, 필수아미노산=tau=4 군, GI=1/n".into(),
            domain_affinity: vec!["nutrition".into(), "biology".into(), "medicine".into(), "sports".into()],
            complementary: vec!["microbiome_ecology".into(), "nutritional_biochemistry".into(), "food_chemistry".into()],
        },
        LensEntry {
            name: "sports_psychology".into(),
            category: LensCategory::Extended,
            description: "스포츠 심리학: 집중=n=6 상태, flow=tau=4 조건, 불안=phi=2 역U, 동기=sigma=12 유형, 자기효능=1/n, zone".into(),
            domain_affinity: vec!["sports".into(), "psychology".into(), "cognitive_science".into(), "medicine".into()],
            complementary: vec!["cognitive_load".into(), "sports_psychology".into(), "emotion_field".into()],
        },
        LensEntry {
            name: "hydration_electrolyte".into(),
            category: LensCategory::Extended,
            description: "수분-전해질: Na/K=phi=2 균형, 삼투압=sigma=12 mOsm, 수분=n=6 L, 탈수=tau=4 단계, 소변비중=1/n, 운동 손실".into(),
            domain_affinity: vec!["nutrition".into(), "medicine".into(), "sports".into(), "physiology".into()],
            complementary: vec!["homeostasis".into(), "hydration_electrolyte".into(), "cardiovascular_hemodynamics".into()],
        },
        LensEntry {
            name: "aerobic_energy_systems".into(),
            category: LensCategory::Extended,
            description: "유산소 에너지 시스템: ATP 경로=n/phi=3, VO₂max=n=6 L/min, 젖산역치=tau=4, 기질=phi=2, 미토콘드리아=sigma=12, RQ".into(),
            domain_affinity: vec!["sports".into(), "physiology".into(), "biology".into(), "medicine".into()],
            complementary: vec!["aerobic_energy_systems".into(), "nutritional_biochemistry".into(), "circadian_rhythm".into()],
        },
        LensEntry {
            name: "recovery_science".into(),
            category: LensCategory::Extended,
            description: "회복 과학: 수면=n=6 시간, 근피로=tau=4 단계, HRV=phi=2, 미세손상=sigma=12 h 회복, 글리코겐=1/n, 냉수침수".into(),
            domain_affinity: vec!["sports".into(), "medicine".into(), "physiology".into(), "nutrition".into()],
            complementary: vec!["sleep_cycle".into(), "recovery_science".into(), "strength_conditioning".into()],
        },
        LensEntry {
            name: "injury_prevention_biomechanics".into(),
            category: LensCategory::Extended,
            description: "부상 예방 생체역학: 위험요인=n=6, 접지 충격=sigma=12 BW, 무릎 외반=tau=4 각, 코어=phi=2, 피로=1/n 임계, FMS".into(),
            domain_affinity: vec!["sports".into(), "medicine".into(), "engineering".into(), "physiology".into()],
            complementary: vec!["sports_biomech".into(), "structural_mechanics".into(), "injury_prevention_biomechanics".into()],
        },
        LensEntry {
            name: "gut_microbiome_nutrition".into(),
            category: LensCategory::Extended,
            description: "장 마이크로바이옴 영양: 장내세균=n=6 문, 단쇄지방산=tau=4, 식이섬유=sigma=12 g, 프로바이오틱=phi=2, 투과성=1/n".into(),
            domain_affinity: vec!["nutrition".into(), "medicine".into(), "biology".into(), "ecology".into()],
            complementary: vec!["microbiome_ecology".into(), "gut_microbiome_nutrition".into(), "food_chemistry".into()],
        },
        LensEntry {
            name: "sports_tactics_game_model".into(),
            category: LensCategory::Extended,
            description: "스포츠 전술 게임 모델: 조직=n=6 원칙, 프레싱=tau=4, 포지션게임=phi=2, 전환=sigma=12 m/s, 깊이=1/n, 전술주기".into(),
            domain_affinity: vec!["sports".into(), "ai".into(), "data_science".into(), "cognitive_science".into()],
            complementary: vec!["game_theory".into(), "sport_performance_analysis".into(), "sports_tactics_game_model".into()],
        },
    ]
}

#[cfg(test)]
mod expansion_100_v4_tests {
    use super::*;

    #[test]
    fn test_expansion_100_v4_count() {
        let entries = expansion_100_v4_lens_entries();
        assert_eq!(entries.len(), 100, "4차 확장 렌즈는 정확히 100개여야 함");
    }

    #[test]
    fn test_expansion_100_v4_names_unique() {
        let entries = expansion_100_v4_lens_entries();
        let mut names: Vec<&str> = entries.iter().map(|e| e.name.as_str()).collect();
        let total = names.len();
        names.sort();
        names.dedup();
        assert_eq!(names.len(), total, "4차 확장 렌즈 이름은 모두 고유해야 함");
    }

    #[test]
    fn test_expansion_100_v4_all_extended() {
        for entry in expansion_100_v4_lens_entries() {
            assert_eq!(
                entry.category,
                LensCategory::Extended,
                "렌즈 '{}'는 Extended 카테고리여야 함",
                entry.name
            );
        }
    }

    #[test]
    fn test_expansion_100_v4_no_empty_fields() {
        for entry in expansion_100_v4_lens_entries() {
            assert!(!entry.name.is_empty(), "이름이 비어있음");
            assert!(!entry.description.is_empty(), "렌즈 '{}' description 없음", entry.name);
            assert!(!entry.domain_affinity.is_empty(), "렌즈 '{}' domain_affinity 없음", entry.name);
            assert!(!entry.complementary.is_empty(), "렌즈 '{}' complementary 없음", entry.name);
        }
    }
}

#[cfg(test)]
mod expansion_50_v3_tests {
    use super::*;

    #[test]
    fn test_expansion_50_v3_count() {
        let entries = expansion_50_v3_lens_entries();
        assert_eq!(entries.len(), 50, "3차 확장 렌즈는 정확히 50개여야 함");
    }

    #[test]
    fn test_expansion_50_v3_names_unique() {
        let entries = expansion_50_v3_lens_entries();
        let mut names: Vec<&str> = entries.iter().map(|e| e.name.as_str()).collect();
        let total = names.len();
        names.sort();
        names.dedup();
        assert_eq!(names.len(), total, "3차 확장 렌즈 이름은 모두 고유해야 함");
    }

    #[test]
    fn test_expansion_50_v3_all_extended() {
        for entry in expansion_50_v3_lens_entries() {
            assert_eq!(
                entry.category,
                LensCategory::Extended,
                "렌즈 '{}'는 Extended 카테고리여야 함",
                entry.name
            );
        }
    }

    #[test]
    fn test_expansion_50_v3_no_empty_fields() {
        for entry in expansion_50_v3_lens_entries() {
            assert!(!entry.name.is_empty(), "이름이 비어있음");
            assert!(!entry.description.is_empty(), "렌즈 '{}' description 없음", entry.name);
            assert!(!entry.domain_affinity.is_empty(), "렌즈 '{}' domain_affinity 없음", entry.name);
            assert!(!entry.complementary.is_empty(), "렌즈 '{}' complementary 없음", entry.name);
        }
    }
}

#[cfg(test)]
mod expansion_56_tests {
    use super::*;

    #[test]
    fn test_expansion_56_count() {
        let entries = expansion_56_lens_entries();
        assert_eq!(entries.len(), 56, "Must have exactly 56 expansion lenses");
    }

    #[test]
    fn test_expansion_56_names_unique() {
        let entries = expansion_56_lens_entries();
        let mut names: Vec<&str> = entries.iter().map(|e| e.name.as_str()).collect();
        let total = names.len();
        names.sort();
        names.dedup();
        assert_eq!(names.len(), total, "All expansion lens names must be unique");
    }

    #[test]
    fn test_expansion_56_all_extended() {
        for entry in expansion_56_lens_entries() {
            assert_eq!(
                entry.category,
                LensCategory::Extended,
                "Lens '{}' should be Extended category",
                entry.name
            );
        }
    }

    #[test]
    fn test_expansion_56_no_empty_fields() {
        for entry in expansion_56_lens_entries() {
            assert!(!entry.name.is_empty());
            assert!(!entry.description.is_empty(), "Lens '{}' needs description", entry.name);
            assert!(!entry.domain_affinity.is_empty(), "Lens '{}' needs domain affinity", entry.name);
            assert!(!entry.complementary.is_empty(), "Lens '{}' needs complementary", entry.name);
        }
    }
}

#[cfg(test)]
mod new_domain_tests {
    use super::*;

    #[test]
    fn test_new_domain_lens_count() {
        let entries = new_domain_lens_entries();
        assert_eq!(entries.len(), 8, "Must have exactly 8 new-domain lenses");
    }

    #[test]
    fn test_new_domain_lens_names_unique() {
        let entries = new_domain_lens_entries();
        let mut names: Vec<&str> = entries.iter().map(|e| e.name.as_str()).collect();
        let total = names.len();
        names.sort();
        names.dedup();
        assert_eq!(names.len(), total, "All new-domain lens names must be unique");
    }

    #[test]
    fn test_new_domain_all_extended() {
        for entry in new_domain_lens_entries() {
            assert_eq!(
                entry.category,
                LensCategory::Extended,
                "Lens '{}' should be Extended category",
                entry.name
            );
        }
    }

    #[test]
    fn test_new_domain_no_empty_fields() {
        for entry in new_domain_lens_entries() {
            assert!(!entry.name.is_empty());
            assert!(!entry.description.is_empty(), "Lens '{}' needs description", entry.name);
            assert!(!entry.domain_affinity.is_empty(), "Lens '{}' needs domain affinity", entry.name);
            assert!(!entry.complementary.is_empty(), "Lens '{}' needs complementary", entry.name);
        }
    }
}
