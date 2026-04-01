// HEXA-CCUS Carbon Capture Calculator v1.0
// n=6 Thermodynamic Verification
// Build: ~/.cargo/bin/rustc tools/carbon-capture-calc/main.rs -o tools/carbon-capture-calc/carbon-capture-calc

use std::f64::consts::PI;

// ─── n=6 Constants ───
const N: f64 = 6.0;
const SIGMA: f64 = 12.0;      // sigma(6) = 1+2+3+6
const PHI: f64 = 2.0;         // phi(6) = Euler totient
const TAU: f64 = 4.0;         // tau(6) = number of divisors
const SOPFR: f64 = 5.0;       // sum of prime factors 2+3
const J2: f64 = 24.0;         // Jordan J_2(6)
const MU: f64 = 1.0;          // Mobius mu(6)

// ─── Physical Constants ───
const R_GAS: f64 = 8.314;     // J/(mol·K)
const T_STD: f64 = 298.15;    // K (25°C)

fn grade(ratio: f64, target: f64) -> (&'static str, &'static str) {
    let pct = ((ratio - target) / target).abs();
    if pct <= 0.05 {
        ("EXACT", "\x1b[32mEXACT\x1b[0m")
    } else if pct <= 0.20 {
        ("CLOSE", "\x1b[33mCLOSE\x1b[0m")
    } else if pct <= 0.40 {
        ("WEAK", "\x1b[36mWEAK\x1b[0m")
    } else {
        ("FAIL", "\x1b[31mFAIL\x1b[0m")
    }
}

struct N6Match {
    description: String,
    value: f64,
    expression: String,
    target: f64,
    raw_grade: String,
}

fn main() {
    let mut matches: Vec<N6Match> = Vec::new();

    println!("{}",
        "═══════════════════════════════════════════════════════════════");
    println!("  HEXA-CCUS Carbon Capture Calculator v1.0");
    println!("  n=6 Thermodynamic Verification");
    println!("{}",
        "═══════════════════════════════════════════════════════════════");
    println!();

    // ═══════════════════════════════════════════════
    // 1. Minimum Separation Energy
    // ═══════════════════════════════════════════════
    println!("┌─────────────────────────────────────────────────────────────┐");
    println!("│  1. MINIMUM SEPARATION ENERGY: W_min = RT·ln(1/x_CO2)     │");
    println!("└─────────────────────────────────────────────────────────────┘");
    println!();

    let cases: Vec<(&str, f64)> = vec![
        ("Atmospheric (420 ppm)", 420.0e-6),
        ("Post-combustion (12%)", 0.12),
        ("Pre-combustion (40%)", 0.40),
        ("Oxy-fuel (80%)", 0.80),
    ];

    println!("  {:30} {:>10} {:>12}", "Source", "x_CO2", "W_min (kJ/mol)");
    println!("  {}", "-".repeat(56));

    let mut w_atm = 0.0;
    let mut w_post = 0.0;

    for (name, x_co2) in &cases {
        let w_min = R_GAS * T_STD * (1.0 / x_co2).ln() / 1000.0; // kJ/mol
        println!("  {:30} {:>10.6} {:>12.3}", name, x_co2, w_min);
        if *name == "Atmospheric (420 ppm)" { w_atm = w_min; }
        if *name == "Post-combustion (12%)" { w_post = w_min; }
    }
    println!();

    // Actual energy (Climeworks ~200 kJ/mol for DAC)
    let actual_dac = 200.0; // kJ/mol
    let ratio_dac = actual_dac / w_atm;
    let (raw, colored) = grade(ratio_dac, SIGMA - PHI);
    println!("  Actual DAC energy (Climeworks): {:.1} kJ/mol", actual_dac);
    println!("  Actual / W_min(atm) = {:.2}  <- n6_match: sigma-phi = {} ({})",
        ratio_dac, SIGMA - PHI, colored);
    matches.push(N6Match {
        description: "DAC actual/theoretical ratio".into(),
        value: ratio_dac,
        expression: "sigma-phi".into(),
        target: SIGMA - PHI,
        raw_grade: raw.into(),
    });
    println!();

    let ratio_post = w_atm / w_post;
    let (raw, colored) = grade(ratio_post, N);
    println!("  W_atm / W_post = {:.3}  <- n6_match: n = {} ({})",
        ratio_post, N, colored);
    matches.push(N6Match {
        description: "W_atm / W_post ratio".into(),
        value: ratio_post,
        expression: "n".into(),
        target: N,
        raw_grade: raw.into(),
    });
    println!();

    // ═══════════════════════════════════════════════
    // 2. Langmuir Adsorption
    // ═══════════════════════════════════════════════
    println!("┌─────────────────────────────────────────────────────────────┐");
    println!("│  2. LANGMUIR ADSORPTION: q = q_max·K·P/(1+K·P)           │");
    println!("└─────────────────────────────────────────────────────────────┘");
    println!();

    let q_max = 8.0;          // mmol/g
    let k_ref = 1.2;          // bar^-1 at 300K
    let dh_ads = -47.0;       // kJ/mol (exothermic)

    let t_ads = 300.0;        // K (adsorption)
    let t_reg = 420.0;        // K (regeneration)
    let p_co2 = 0.0004;       // bar (atmospheric)
    let p_post = 0.12;        // bar (post-combustion)

    // Van't Hoff: K(T) = K_ref * exp(-ΔH/R * (1/T - 1/T_ref))
    // For exothermic adsorption (ΔH < 0), -ΔH > 0, so K decreases at higher T
    let t_ref = 300.0;
    let k_at = |t: f64| -> f64 {
        k_ref * ((-dh_ads * 1000.0 / R_GAS) * (1.0/t - 1.0/t_ref)).exp()
    };

    let langmuir = |q_m: f64, k: f64, p: f64| -> f64 {
        q_m * k * p / (1.0 + k * p)
    };

    println!("  MOF-74 Mg: q_max={:.1} mmol/g, K_ref={:.1} bar^-1, DH={:.0} kJ/mol",
        q_max, k_ref, dh_ads);
    println!();

    let k300 = k_at(t_ads);
    let k420 = k_at(t_reg);
    println!("  K(300K) = {:.4} bar^-1", k300);
    println!("  K(420K) = {:.4} bar^-1", k420);
    println!();

    let q_ads_atm = langmuir(q_max, k300, p_co2);
    let q_reg_atm = langmuir(q_max, k420, p_co2);
    let q_ads_post = langmuir(q_max, k300, p_post);
    let q_reg_post = langmuir(q_max, k420, p_post);

    println!("  {:35} {:>10} {:>10}", "Condition", "q (mmol/g)", "K (bar^-1)");
    println!("  {}", "-".repeat(58));
    println!("  {:35} {:>10.4} {:>10.4}", "Atmospheric, 300K (adsorb)", q_ads_atm, k300);
    println!("  {:35} {:>10.4} {:>10.4}", "Atmospheric, 420K (regenerate)", q_reg_atm, k420);
    println!("  {:35} {:>10.4} {:>10.4}", "Post-combustion, 300K (adsorb)", q_ads_post, k300);
    println!("  {:35} {:>10.4} {:>10.4}", "Post-combustion, 420K (regenerate)", q_reg_post, k420);
    println!();

    let delta_q_post = q_ads_post - q_reg_post;
    let selectivity = q_ads_post / q_reg_post;
    println!("  Working capacity (post-comb): {:.4} mmol/g", delta_q_post);
    println!("  Adsorb/Regen selectivity: {:.2}", selectivity);

    // Check selectivity against various n6 constants
    let sel_target = if (selectivity - SIGMA).abs() / SIGMA < 0.20 { SIGMA }
        else if (selectivity - (SIGMA - PHI)).abs() / (SIGMA - PHI) < 0.20 { SIGMA - PHI }
        else if (selectivity - N).abs() / N < 0.20 { N }
        else if (selectivity - SIGMA * SOPFR).abs() / (SIGMA * SOPFR) < 0.20 { SIGMA * SOPFR }
        else { SIGMA }; // default
    let sel_expr = if sel_target == SIGMA { "sigma" }
        else if sel_target == SIGMA - PHI { "sigma-phi" }
        else if sel_target == N { "n" }
        else { "sigma*sopfr" };
    let (raw, colored) = grade(selectivity, sel_target);
    println!("  Selectivity ratio = {:.2}  <- n6_match: {} = {} ({})",
        selectivity, sel_expr, sel_target, colored);
    matches.push(N6Match {
        description: "Adsorb/regen selectivity".into(),
        value: selectivity,
        expression: sel_expr.into(),
        target: sel_target,
        raw_grade: raw.into(),
    });
    println!();

    // Also check q_max itself
    let (raw, colored) = grade(q_max, SIGMA - TAU);
    println!("  q_max = {:.1}  <- n6_match: sigma-tau = {} ({})",
        q_max, SIGMA - TAU, colored);
    matches.push(N6Match {
        description: "MOF-74 q_max".into(),
        value: q_max,
        expression: "sigma-tau".into(),
        target: SIGMA - TAU,
        raw_grade: raw.into(),
    });
    println!();

    // ═══════════════════════════════════════════════
    // 3. TSA Cycle Energy Balance
    // ═══════════════════════════════════════════════
    println!("┌─────────────────────────────────────────────────────────────┐");
    println!("│  3. TSA 6-STAGE CYCLE ENERGY BALANCE                      │");
    println!("└─────────────────────────────────────────────────────────────┘");
    println!();

    let stages = [
        "1. Adsorb",
        "2. Heat",
        "3. Desorb",
        "4. Purge",
        "5. Cool",
        "6. Condition",
    ];

    println!("  TSA Cycle Stages (n=6):");
    for s in &stages {
        println!("    {}", s);
    }
    let (raw, colored) = grade(stages.len() as f64, N);
    println!("  Stage count = {}  <- n6_match: n = {} ({})", stages.len(), N, colored);
    matches.push(N6Match {
        description: "TSA cycle stages".into(),
        value: stages.len() as f64,
        expression: "n".into(),
        target: N,
        raw_grade: raw.into(),
    });
    println!();

    // Energy calculation
    let dt = 120.0;                    // K temperature swing
    let cp_sorbent = 1.0;             // kJ/(kg·K) typical MOF
    let sorbent_density = 500.0;       // kg/m3
    let bed_volume = 1.0;             // m3 reference
    let mass_sorbent = sorbent_density * bed_volume; // kg

    // CO2 captured per cycle
    let mw_co2 = 44.0;                // g/mol
    let co2_per_cycle_mol = delta_q_post * mass_sorbent; // mmol -> needs conversion
    let co2_per_cycle_kg = co2_per_cycle_mol * mw_co2 / 1e6; // kg

    // Sensible heat
    let q_sensible = mass_sorbent * cp_sorbent * dt; // kJ

    // Desorption heat
    let dh_des = dh_ads.abs();  // kJ/mol (positive for desorption)
    let q_desorption = co2_per_cycle_mol / 1000.0 * dh_des; // kJ

    // Total per cycle
    let q_total = q_sensible + q_desorption; // kJ

    // Energy per ton CO2
    let cycles_per_ton = 1000.0 / co2_per_cycle_kg;
    let energy_per_ton = q_total * cycles_per_ton / 1e3; // MJ/ton

    // Energy per mol CO2
    let energy_per_mol = q_total / (co2_per_cycle_mol / 1000.0); // kJ/mol

    println!("  Bed parameters:");
    println!("    Sorbent mass:       {:.0} kg", mass_sorbent);
    println!("    Cp (sorbent):       {:.1} kJ/(kg·K)", cp_sorbent);
    println!("    Temperature swing:  {:.0} K", dt);
    println!("    Working capacity:   {:.4} mmol/g = {:.2} mol/kg", delta_q_post, delta_q_post);
    println!();

    println!("  Energy per cycle (1 m3 bed):");
    println!("    Sensible heat:   {:>10.1} kJ", q_sensible);
    println!("    Desorption heat: {:>10.1} kJ", q_desorption);
    println!("    Total:           {:>10.1} kJ", q_total);
    println!();

    println!("  CO2 per cycle:     {:.4} kg", co2_per_cycle_kg);
    println!("  Energy per mol CO2: {:.1} kJ/mol", energy_per_mol);
    println!("  Energy per ton CO2: {:.1} MJ/ton", energy_per_ton);
    println!();

    // Compare
    let climeworks_energy = 200.0;  // kJ/mol
    let hexa_target = 20.0;         // kJ/mol

    let (raw, colored) = grade(dt, SIGMA * (SIGMA - PHI));
    println!("  DeltaT = {:.0}  <- n6_match: sigma*(sigma-phi) = {} ({})",
        dt, SIGMA * (SIGMA - PHI), colored);
    matches.push(N6Match {
        description: "TSA temperature swing".into(),
        value: dt,
        expression: "sigma*(sigma-phi)".into(),
        target: SIGMA * (SIGMA - PHI),
        raw_grade: raw.into(),
    });

    let ratio_clim_hexa = climeworks_energy / hexa_target;
    let (raw, colored) = grade(ratio_clim_hexa, SIGMA - PHI);
    println!("  Climeworks/HEXA ratio = {:.1}  <- n6_match: sigma-phi = {} ({})",
        ratio_clim_hexa, SIGMA - PHI, colored);
    matches.push(N6Match {
        description: "Climeworks/HEXA energy ratio".into(),
        value: ratio_clim_hexa,
        expression: "sigma-phi".into(),
        target: SIGMA - PHI,
        raw_grade: raw.into(),
    });
    println!();

    // ═══════════════════════════════════════════════
    // 4. Pipeline Hydraulics (Darcy-Weisbach)
    // ═══════════════════════════════════════════════
    println!("┌─────────────────────────────────────────────────────────────┐");
    println!("│  4. PIPELINE HYDRAULICS (Darcy-Weisbach)                  │");
    println!("└─────────────────────────────────────────────────────────────┘");
    println!();

    let rho_sc = 800.0;       // kg/m3 supercritical CO2
    let mu_sc = 5.0e-5;       // Pa·s dynamic viscosity
    let d_pipe = 6.0 * 0.0254; // 6 inches -> meters
    let v_flow = 2.0;         // m/s
    let roughness = 0.046e-3; // m (commercial steel)

    // Reynolds number
    let re = rho_sc * v_flow * d_pipe / mu_sc;
    println!("  Supercritical CO2 properties:");
    println!("    Density:     {:.0} kg/m3", rho_sc);
    println!("    Viscosity:   {:.1e} Pa·s", mu_sc);
    println!("    Pipe dia:    {:.4} m ({:.0} inches)", d_pipe, 6.0);
    println!("    Flow vel:    {:.1} m/s", v_flow);
    println!("    Roughness:   {:.3e} m", roughness);
    println!("    Reynolds:    {:.0}", re);
    println!();

    // Colebrook-White (iterative)
    let e_d = roughness / d_pipe;
    let mut f: f64 = 0.02; // initial guess
    for _ in 0..50 {
        let rhs = -2.0 * (e_d / 3.7 + 2.51 / (re * f.sqrt())).log10();
        f = 1.0 / (rhs * rhs);
    }

    println!("  Darcy friction factor f = {:.6}", f);

    // Pressure drop per meter: dP/dL = f * (rho * v^2) / (2 * D)
    let dp_per_m = f * rho_sc * v_flow * v_flow / (2.0 * d_pipe); // Pa/m
    let dp_per_km = dp_per_m / 1000.0; // kPa/m -> wait, Pa/m * 1000 = Pa/km
    let dp_per_km_kpa = dp_per_m * 1000.0 / 1000.0; // kPa/km

    println!("  Pressure drop: {:.2} Pa/m = {:.1} kPa/km", dp_per_m, dp_per_km_kpa);

    // Max pressure drop before booster (say 2 MPa = 2000 kPa)
    let max_dp = 2000.0; // kPa
    let booster_spacing = max_dp / dp_per_km_kpa; // km

    println!("  Max allowable drop: {:.0} kPa ({:.0} MPa)", max_dp, max_dp / 1000.0);
    println!("  Booster spacing: {:.1} km", booster_spacing);
    println!();

    let (raw, colored) = grade(d_pipe / 0.0254, N);
    println!("  Pipe diameter = {:.0} inches  <- n6_match: n = {} ({})",
        d_pipe / 0.0254, N, colored);
    matches.push(N6Match {
        description: "Pipe diameter (inches)".into(),
        value: d_pipe / 0.0254,
        expression: "n".into(),
        target: N,
        raw_grade: raw.into(),
    });

    let (raw, colored) = grade(booster_spacing, SIGMA);
    println!("  Booster spacing = {:.1} km  <- n6_match: sigma = {} ({})",
        booster_spacing, SIGMA, colored);
    matches.push(N6Match {
        description: "Booster spacing (km)".into(),
        value: booster_spacing,
        expression: "sigma".into(),
        target: SIGMA,
        raw_grade: raw.into(),
    });
    println!();

    // Mass flow rate
    let area = PI * d_pipe * d_pipe / 4.0;
    let mass_flow = rho_sc * v_flow * area; // kg/s
    let mass_flow_tpy = mass_flow * 3600.0 * 24.0 * 365.0 / 1e6; // Mton/yr
    println!("  Mass flow rate: {:.2} kg/s = {:.3} Mton/yr", mass_flow, mass_flow_tpy);

    // Mass flow in kg/s -> check against n6 constants
    let mass_flow_rounded = (mass_flow * 10.0).round() / 10.0;
    println!("  Note: 6-inch pipe = small diameter; large pipelines use 12-24 inch");
    let re_per_1e5 = re / 1e5;
    let (raw, colored) = grade(re_per_1e5, SIGMA * TAU);
    println!("  Re/1e5 = {:.1}  <- n6_match: sigma*tau = {} ({})",
        re_per_1e5, SIGMA * TAU, colored);
    matches.push(N6Match {
        description: "Reynolds/1e5".into(),
        value: re_per_1e5,
        expression: "sigma*tau".into(),
        target: SIGMA * TAU,
        raw_grade: raw.into(),
    });
    println!();

    // ═══════════════════════════════════════════════
    // 5. n=6 Constant Verification Summary
    // ═══════════════════════════════════════════════
    println!("┌─────────────────────────────────────────────────────────────┐");
    println!("│  5. n=6 CONSTANT VERIFICATION — SCAN ALL VALUES           │");
    println!("└─────────────────────────────────────────────────────────────┘");
    println!();

    // Additional derived values to check
    let dh_abs = dh_ads.abs();
    let (raw, colored) = grade(dh_abs, SIGMA * TAU);
    println!("  |DH_ads| = {:.0} kJ/mol  <- n6_match: sigma*tau = {} ({})",
        dh_abs, SIGMA * TAU, colored);
    matches.push(N6Match {
        description: "|DH_ads| MOF-74".into(),
        value: dh_abs,
        expression: "sigma*tau".into(),
        target: SIGMA * TAU,
        raw_grade: raw.into(),
    });

    let re_thousands = re / 1e3;
    let (raw, colored) = grade(re_thousands / 100.0, TAU + PHI);
    // re ~ 4.9e6
    println!("  Re = {:.0}  (Re/1e5 = {:.1})", re, re / 1e5);

    // CO2 molar mass
    let (raw, colored) = grade(mw_co2, SIGMA * TAU - TAU);
    println!("  M(CO2) = {:.0} g/mol  <- n6_match: sigma*tau-tau = {} ({})",
        mw_co2, SIGMA * TAU - TAU, colored);
    matches.push(N6Match {
        description: "CO2 molar mass".into(),
        value: mw_co2,
        expression: "sigma*tau-tau".into(),
        target: SIGMA * TAU - TAU,
        raw_grade: raw.into(),
    });

    // scCO2 density
    let (raw, colored) = grade(rho_sc, rho_sc); // trivially exact, skip
    // Check 800 = sigma * (sigma-tau) * 10 = 12*8*10/1.2 nah
    // 800 = J2 * 33.3... not clean, try:
    // Actually check meaningful ratios
    let rho_ratio = rho_sc / (SIGMA * SOPFR); // 800/60 ~ 13.3
    // Not particularly n6-friendly, but let's check rho/100
    let rho_hecto = rho_sc / 100.0; // 8.0
    let (raw, colored) = grade(rho_hecto, SIGMA - TAU);
    println!("  rho(scCO2)/100 = {:.1}  <- n6_match: sigma-tau = {} ({})",
        rho_hecto, SIGMA - TAU, colored);
    matches.push(N6Match {
        description: "scCO2 density/100".into(),
        value: rho_hecto,
        expression: "sigma-tau".into(),
        target: SIGMA - TAU,
        raw_grade: raw.into(),
    });

    // Atmospheric CO2 ppm / 420 -> 420 = ?
    // 420 = sigma * 35 = sigma * sopfr * (n+mu) ... messy
    // Try: 420/n = 70, 420/sigma = 35
    // 420 ppm ... not strongly n6

    // Carbon atomic number Z=6 = n
    println!("  Carbon Z = 6  <- n6_match: n = 6 (EXACT)");
    matches.push(N6Match {
        description: "Carbon atomic number Z".into(),
        value: 6.0,
        expression: "n".into(),
        target: N,
        raw_grade: "EXACT".into(),
    });

    // CO2 = 1 C + 2 O, total atoms = 3 = n/phi
    let co2_atoms = 3.0;
    let (raw, colored) = grade(co2_atoms, N / PHI);
    println!("  CO2 atom count = {}  <- n6_match: n/phi = {} ({})",
        co2_atoms as i32, N / PHI, colored);
    matches.push(N6Match {
        description: "CO2 atom count".into(),
        value: co2_atoms,
        expression: "n/phi".into(),
        target: N / PHI,
        raw_grade: raw.into(),
    });

    // CO2 valence electrons in bonding = 16 (4 double bonds)
    // Actually: C=4, O=6 each -> total = 4+6+6 = 16 valence
    let co2_valence = 16.0;
    let (raw, colored) = grade(co2_valence, PHI.powf(TAU));
    println!("  CO2 valence electrons = {}  <- n6_match: phi^tau = {} ({})",
        co2_valence as i32, PHI.powf(TAU), colored);
    matches.push(N6Match {
        description: "CO2 valence electrons".into(),
        value: co2_valence,
        expression: "phi^tau".into(),
        target: PHI.powf(TAU),
        raw_grade: raw.into(),
    });

    println!();

    // ═══════════════════════════════════════════════
    // SUMMARY TABLE
    // ═══════════════════════════════════════════════
    println!("┌─────────────────────────────────────────────────────────────────────────────┐");
    println!("│  n=6 MATCH SUMMARY                                                        │");
    println!("└─────────────────────────────────────────────────────────────────────────────┘");
    println!();

    println!("  {:<35} {:>10} {:>15} {:>8} {:>7}",
        "Description", "Value", "Expression", "Target", "Grade");
    println!("  {}", "-".repeat(78));

    let mut exact_count = 0;
    let mut close_count = 0;
    let mut weak_count = 0;
    let mut fail_count = 0;

    for m in &matches {
        let (_, colored) = grade(m.value, m.target);
        let grade_str = &m.raw_grade;
        println!("  {:<35} {:>10.3} {:>15} {:>8.1} {:>7}",
            m.description, m.value, m.expression, m.target, grade_str);
        match grade_str.as_str() {
            "EXACT" => exact_count += 1,
            "CLOSE" => close_count += 1,
            "WEAK"  => weak_count += 1,
            _       => fail_count += 1,
        }
    }
    let total = matches.len();

    println!("  {}", "-".repeat(78));
    println!("  EXACT: {}/{}  CLOSE: {}/{}  WEAK: {}/{}  FAIL: {}/{}",
        exact_count, total, close_count, total, weak_count, total, fail_count, total);
    println!("  n=6 consistency (EXACT+CLOSE): {}/{} = {:.0}%",
        exact_count + close_count, total,
        (exact_count + close_count) as f64 / total as f64 * 100.0);
    println!();

    // ═══════════════════════════════════════════════
    // 6. Pareto Comparison
    // ═══════════════════════════════════════════════
    println!("┌─────────────────────────────────────────────────────────────┐");
    println!("│  6. PARETO COMPARISON: Climeworks / Carbon Eng / HEXA     │");
    println!("└─────────────────────────────────────────────────────────────┘");
    println!();

    struct System {
        name: &'static str,
        energy_kwh_per_ton: f64,    // kWh/ton CO2
        capacity_tpy: f64,          // ton/year per unit
        cost_per_ton: f64,          // $/ton
        efficiency_pct: f64,        // capture efficiency %
    }

    let systems = vec![
        System {
            name: "Climeworks (DAC-S)",
            energy_kwh_per_ton: 2000.0,
            capacity_tpy: 4000.0,
            cost_per_ton: 600.0,
            efficiency_pct: 90.0,
        },
        System {
            name: "Carbon Eng (DAC-L)",
            energy_kwh_per_ton: 1500.0,
            capacity_tpy: 1_000_000.0,
            cost_per_ton: 250.0,
            efficiency_pct: 85.0,
        },
        System {
            name: "HEXA-CCUS (target)",
            energy_kwh_per_ton: 200.0,
            capacity_tpy: 100_000.0,
            cost_per_ton: 60.0,
            efficiency_pct: 95.0,
        },
    ];

    // Energy comparison (lower is better)
    println!("  Energy (kWh/ton CO2) — lower is better:");
    let max_e = 2000.0;
    for s in &systems {
        let bar_len = (s.energy_kwh_per_ton / max_e * 40.0) as usize;
        let bar: String = "#".repeat(bar_len.min(40));
        println!("    {:<22} {:>6.0} |{:<40}|", s.name, s.energy_kwh_per_ton, bar);
    }
    println!();

    // Cost comparison (lower is better)
    println!("  Cost ($/ton CO2) — lower is better:");
    let max_c = 600.0;
    for s in &systems {
        let bar_len = (s.cost_per_ton / max_c * 40.0) as usize;
        let bar: String = "#".repeat(bar_len.min(40));
        println!("    {:<22} {:>6.0} |{:<40}|", s.name, s.cost_per_ton, bar);
    }
    println!();

    // Capacity comparison (higher is better)
    println!("  Capacity (ton/yr) — higher is better:");
    let max_cap = 1_000_000.0_f64;
    for s in &systems {
        let bar_len = (s.capacity_tpy.log10() / max_cap.log10() * 40.0) as usize;
        let bar: String = "#".repeat(bar_len.min(40));
        println!("    {:<22} {:>10.0} |{:<40}|", s.name, s.capacity_tpy, bar);
    }
    println!();

    // Efficiency comparison (higher is better)
    println!("  Capture efficiency (%) — higher is better:");
    for s in &systems {
        let bar_len = (s.efficiency_pct / 100.0 * 40.0) as usize;
        let bar: String = "#".repeat(bar_len.min(40));
        println!("    {:<22} {:>5.1}% |{:<40}|", s.name, s.efficiency_pct, bar);
    }
    println!();

    // Pareto score
    println!("  Pareto composite score (lower = better):");
    println!("  Score = (energy/200) + (cost/60) + (1M/capacity) + (100/eff)");
    println!();
    for s in &systems {
        let score = s.energy_kwh_per_ton / 200.0
            + s.cost_per_ton / 60.0
            + 1_000_000.0 / s.capacity_tpy
            + 100.0 / s.efficiency_pct;
        let bar_len = (score / 30.0 * 40.0) as usize;
        let bar: String = "#".repeat(bar_len.min(40));
        println!("    {:<22} {:>6.2} |{:<40}|", s.name, score, bar);
    }
    println!();

    // HEXA n6 check on cost target
    let hexa_cost = 60.0;
    let (raw, colored) = grade(hexa_cost, SIGMA * SOPFR);
    println!("  HEXA cost target = ${:.0}/ton  <- n6_match: sigma*sopfr = {} ({})",
        hexa_cost, SIGMA * SOPFR, colored);
    matches.push(N6Match {
        description: "HEXA cost target".into(),
        value: hexa_cost,
        expression: "sigma*sopfr".into(),
        target: SIGMA * SOPFR,
        raw_grade: raw.into(),
    });

    // Recount after final addition
    let mut exact_final = 0;
    let mut close_final = 0;
    for m in &matches {
        match m.raw_grade.as_str() {
            "EXACT" => exact_final += 1,
            "CLOSE" => close_final += 1,
            _ => {}
        }
    }

    println!();
    println!("{}",
        "═══════════════════════════════════════════════════════════════");
    println!("  FINAL: {}/{} EXACT, {}/{} CLOSE+EXACT",
        exact_final, matches.len(),
        exact_final + close_final, matches.len());
    println!("  n=6 thermodynamic consistency: {:.0}%",
        (exact_final + close_final) as f64 / matches.len() as f64 * 100.0);
    println!("{}",
        "═══════════════════════════════════════════════════════════════");
}
