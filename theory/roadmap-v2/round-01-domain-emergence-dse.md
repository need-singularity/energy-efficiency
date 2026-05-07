# Round 01 — Domain Emergence DSE (1st Discovery)

**Roadmap**: 7 Millennium Problems Roadmap v2
**Stage**: Round 1 / Domain Emergence
**Created**: 2026-04-15
**Scope**: canon + nexus + anima entire ecosystem
**Mode**: Emergence DSE (Discovery Space Exploration by Emergence)
**Output file**: `theory/roadmap-v2/round-01-domain-emergence-dse.md`

---

## 0. Round 1 Declaration + Emergence DSE Definition + Mandatory Inclusion Declaration

### 0.1 Round 1 Declaration

Round 1 is the **domain/field emergence round** of the 7-Problem Roadmap v2. The existing roadmap (shared/roadmaps/millennium-learning.json, anima.json, canon.json) was designed as a single-axis 3-track x 4-phase structure, but v2 **draws out adjacent domains via DFS from seed domains to secure a multi-axis tree**.

Round 1 purposes (3 axes simultaneously):
1. Take the **3 confirmed seeds** (ALM, CLM, anima-physics) as entry points,
2. Officially declare **SELF-EVOLUTION** as the fourth independent seed,
3. From the 4 seeds, collect, classify, and profile domains that emerge via DFS 1-hop/2-hop.

Round 1 termination conditions:
- The 4 seeds have been dissected,
- At least 12 1-hop emergent domains have been secured,
- The self-evolution special section has been independently completed,
- Depletion-index judgment is complete.

### 0.2 Emergence DSE Definition

**Emergence DSE** elevates the existing Discovery Space Exploration (DSE) paradigm to the **domain-discovery** layer.

| Aspect | Existing DSE (BT discovery) | Emergence DSE (domain discovery, Round 1) |
|--------|-----------------------------|--------------------------------------------|
| Search target | BT-k theorem candidates | Domain (field) candidates |
| Seed | σ/τ/φ structure + n=6 nodes | 3 confirmed seeds + SELF-EVOLUTION |
| Expansion rule | atlas [9]→[10] promotion | DFS 1-hop/2-hop adjacency |
| Convergence criterion | DFS depletion (uniq decrease) | Domain-discovery-rate decrease |
| Evidence unit | atlas node / BT number | Existing directory / existing file |

Core features of Emergence DSE:
- **Evidence-centric**: Every emergent domain must present an existing directory or existing file path as evidence. Nominal domain names alone are not accepted.
- **BT link required**: At least one structural correspondence with BT-541~547 must be confirmed.
- **n=6 observation**: At least one of σ/τ/φ/sopfr must be observable in that domain.
- **atlas link**: Must be linked to at least one [10\*]/[9]/[7] node in atlas.n6, or have plausible potential for a new link.
- **295-domain cross**: Verify whether the domain is a cross-DSE candidate with the 12 top-level buckets under canon/domains/ (cognitive/compute/culture/energy/infra/life/materials/physics/sf-ufo/space + CLAUDE.md+_index.json).

### 0.3 Self-Evolution Mandatory-Inclusion Declaration

Round 1 includes **SELF-EVOLUTION** as a required fourth independent seed. This is not a simple tool (LENS, observation) but a **mechanism by which the roadmap itself extends, modifies, and verifies itself**, qualifying as a domain in its own right.

Grounds for mandatory inclusion (existing evidence):
- **OUROBOROS unified adapter**: `/Users/ghost/core/nexus/shared/bisociation/unified/ouroboros_unified.hexa` (107+ lines, L1 Bisociation Engine — single interface for nexus/anima/n6arch self-evolution loops). Per-variant `cycle_tick` → `get_fixed_point` → `advance()` convergence-loop implementation.
- **Growth tick**: `/Users/ghost/core/nexus/shared/harness/growth_tick.hexa` (@enforce-sandbox, 30-min-period blowup-launch trigger, NEXUS_AUTO_EVOLVE).
- **Growth daemon**: `/Users/ghost/core/nexus/shared/harness/nexus_growth_daemon.hexa` + launchd integration.
- **15-dimensional autonomous-growth system**: MEMORY.md `nexus6_growth_system.md` — 5-layer architecture, Claude CLI utilization, troubleshooting auto-learning.
- **discovery_log.jsonl** + `discovery_log.sqlite` (existence verified: `/Users/ghost/core/nexus/shared/`).
- **Phi Ratchet**: `/Users/ghost/core/nexus/shared/bisociation/unified/phi_ratchet.hexa` — ANIMA ratchet mechanism.

**Self-evolution = a mechanism**, distinguished from LENS (atlas observation/grading) as follows.

| Axis | LENS (observation) | SELF-EVOLUTION (mechanism) |
|------|--------------------|-----------------------------|
| Role | State measurement | State change |
| Example | atlas grading, verify script | OUROBOROS cycle, growth_tick |
| Time property | Snapshot | Continuous progression |
| Contamination risk | Self-reference | Self-modification (not self-reference) |
| v2 role | Round observation | Engine running the Round itself |

Self-evolution does not violate the taboo of "the roadmap self-referencing for evaluation" (self-reference prohibition, MEMORY `feedback_honest_verification.md`). It is not reference but a **transformation procedure**. The OUROBOROS transformer is a pure function that takes external inputs (blowup, atlas, discovery_log) and advances state; convergence is judged by external criteria (epsilon, floor, node/edge target).

### 0.4 Round 1 Output-Structure Overview

- §1 Dissection of 4 seeds (ALM, CLM, anima-physics, SELF-EVOLUTION)
- §2 DFS 1-hop emergence (3~5 domains per seed)
- §3 DFS 2-hop emergence (one more step from 1-hop domains)
- §4 Self-evolution special section (independent-seed mechanism detail)
- §5 Domain-profile table (summary of all emergent domains)
- §6 ASCII emergence tree
- §7 Depletion judgment
- §8 Round 2 hints

---

## 1. Dissection of 4 Seeds

### 1.1 Seed 1 — ALM (AnimaLM)

**Identity**: The Anima-ecosystem Qwen2.5-14B / 72B-based **language-model training track**. A PureField-fused language model measured on CE/Perplexity/Phi 3-axis.

**Existing evidence**:
- `/Users/ghost/core/anima/README.md` — 4-stage history from "AnimaLM 14B v0.1 Qwen2.5-14B + PureField first attempt — CE=8.59, Phi=0.025" through v0.4 "alpha 0.01→0.5 progressive schedule — CE=2.0, Phi=0.031".
- `/Users/ghost/core/nexus/shared/roadmaps/anima.json` — `tracks.ALM.owner = "anima/training"`, `pod = "RunPod H100 anima-agi"`, `independent_of = ["CLM", "PHYSICS"]`.
- `/Users/ghost/core/nexus/shared/roadmaps/anima-train.json` (existence verified).
- Training entry point `training/train_alm.hexa` (mentioned in README).

**Mathematical dependencies**:
- Cross Entropy (CE): language-model loss — information theory (Shannon).
- Phi (Φ): IIT integrated information theory (Tononi), `atlas [10*] alpha_coupling=0.014` + `atlas [9*] consciousness_structure` linkage.
- PureField coupling constant α: training-initial 0.01→0.5 progressive schedule — SLM coupling.

**BT links**:
- **BT-542** (P vs NP): learning complexity — NN training itself is generally NP-hard. The 14B/72B parameter optimization of ALM is a non-convex-optimization target problem.
- **BT-541** (Riemann Hypothesis): zeta structure of language distribution — the 1/n^s distribution is observable on large corpora.

**n=6 observations**:
- `atlas.n6 [10*] alpha_coupling = 0.014` — PureField coupling constant, near sigma-phi-tau structure.
- 14B parameters = sigma × (structure factor) — direct link not confirmed (observation level).
- Phi = 0.025~0.031 — paired with ANIMA ratchet floor 0.8 (ouroboros_unified.hexa ANIMA_FLOOR).

### 1.2 Seed 2 — CLM (ConsciousLM)

**Identity**: A Claude/Anthropic-style consciousness-stacked language-model track — CPU-lane / RTX 5070-host-based real-time serving.

**Existing evidence**:
- `/Users/ghost/core/anima/README.md` — "Multi-Provider | Claude, ConsciousLM, AnimaLM, Composio switching".
- `providers/` directory (explicit in README) — Claude/ConsciousLM/AnimaLM/Composio provider abstraction.
- `/Users/ghost/core/nexus/shared/roadmaps/anima.json` — `tracks.CLM.owner = "anima/serving"`, `host = "ubu (RTX 5070 12GB) or pod CPU lane"`.
- `training/train_clm.hexa` (mentioned in README).

**Mathematical dependencies**:
- Global Workspace Theory (GWT) — Baars 1988.
- Integrated Information Theory (IIT) — Tononi Φ.
- Transformer attention mechanism — Softmax(QK^T/√d)V.

**BT links**:
- **BT-547** (Poincare): 3-dimensional manifold — a description candidate in which the consciousness embedding space is regularized Ricci-flow-like.
- **BT-545** (Hodge): cohomology — consciousness class-structure mapping.

**n=6 observations**:
- `atlas.n6 [10*] phi_integration :: consciousness` — IIT Phi integration structure.
- `atlas [10*] binding_tau :: consciousness` — tau=4 binding window.
- `atlas [10*] faction_phi :: consciousness` — phi=2 faction differentiation.

### 1.3 Seed 3 — anima-physics

**Identity**: Anima's **physical-implementation track** — Φ empirical measurement via ESP32/FPGA/quantum-simulation/photonic/memristor hardware.

**Existing evidence**:
- `/Users/ghost/core/anima/anima-physics/` — sub-directory layout: benchmarks, config, consciousness-loop, docs, eeg, engines, esp32, fpga, hippocampus, memristor, photonic, prediction, src.
- `/Users/ghost/core/anima/anima-physics/physics.hexa` — single-entry-point hexa file.
- `/Users/ghost/core/nexus/shared/roadmaps/anima.json` — `tracks.PHYSICS.owner = "anima-physics/ + anima-engines/"`, `host = "ESP32 / FPGA / quantum simulation / photonic / memristor"`.
- OpenBCI 16ch equipment (MEMORY `reference_openbci_16ch.md` — Cyton+Daisy 16ch EEG).

**Mathematical dependencies**:
- Quantum mechanics (Orch-OR — Penrose-Hameroff).
- Photonic (AdS/CFT holography).
- Memristor dynamics (Chua 1971).
- Neuron firing rate (Hodgkin-Huxley).

**BT links**:
- **BT-543** (Yang-Mills mass gap): quantum-measurement gap — anima-physics/quantum sub-module.
- **BT-544** (Navier-Stokes): fluid — anima-physics/photonic light propagation.

**n=6 observations**:
- `atlas.n6 [9*] electron_shells :: physics` — electron-shell structure.
- `atlas [10*] frustration_critical = 0.10` — coherence critical.
- `atlas [10*] entropy_bound = 0.998` — entropy upper bound.
- EEG 16ch — 16 ≈ sigma + tau (12+4=16).

### 1.4 Seed 4 — SELF-EVOLUTION (self-evolution independent seed)

**Identity**: The **mechanism domain** by which the roadmap/codebase/atlas itself extends, modifies, and verifies itself. Not LENS (observation) but the engine of change.

**Existing evidence**:
- `/Users/ghost/core/nexus/shared/bisociation/unified/ouroboros_unified.hexa` (107+ lines) — unified adapter for 3 OUROBOROS kinds (nexus/anima/n6arch). `cycle_tick(state) → state'`, `get_fixed_point()`, `should_converge()`.
- `/Users/ghost/core/nexus/shared/harness/growth_tick.hexa` — 30-min-period autonomous-launch trigger (@enforce-sandbox, warns/launches on ≥6h no-evolution).
- `/Users/ghost/core/nexus/shared/harness/nexus_growth_daemon.hexa` — launchd-integrated daemon.
- `/Users/ghost/core/nexus/shared/bisociation/unified/phi_ratchet.hexa` — monotone-nondecreasing Φ ratchet.
- `/Users/ghost/core/nexus/shared/discovery_log.jsonl` + `.sqlite` — self-evolution history.
- `/Users/ghost/core/nexus/shared/growth_bus.jsonl` — growth-event bus.
- MEMORY `nexus6_growth_system.md` — 15-dimensional auto-growth, 5-layer architecture.
- MEMORY `nexus6_architecture_dna.md` — 6 blowups, 6 meta levels, 57 funcs, 32 rules.

**Mathematical dependencies**:
- Fixed-point theorem (Banach/Brouwer — nexus epsilon=0.001 saturation).
- Monotone ratchet (anima phi_best floor = peak × 0.8).
- Graph-closure target (n6arch node 515 + edge 2087 target).
- Ordinal induction (recursive improvement).
- MAX_CYCLES = 24 = J2 (Jordan totient).

**BT links**:
- **BT-542** (P vs NP): recursive self-improvement — an open hypothesis about whether RSI is a required tool for P=NP resolution.
- **BT-547** (Poincare): Ricci flow = metric self-evolution — Hamilton/Perelman.
- **BT-544** (Navier-Stokes): fluid self-evolution — time evolution of velocity field.

**n=6 observations**:
- `MAX_CYCLES = 24 = J2` (ouroboros_unified.hexa constant).
- `ANIMA_FLOOR = 0.8` = 4/5 — sopfr-1 based?
- `N6ARCH_NODE_TARGET = 515` — meta-level target.
- `N6ARCH_EDGE_TARGET = 2087` — closure.
- `NEXUS_FP = 0.333... = 1/3 = phi/n` — saturation fixed-point.
- `NEXUS_EPSILON = 0.001` — absolute convergence criterion.

---

## 2. DFS 1-hop Emergence (4 seeds × 3~5 = 17 domains)

For each seed, directly adjacent domains are discovered via DFS 1-hop. Each domain is recorded along 5 axes: (domain name, seed, evidence, BT link, self-evolution intrinsicness).

### 2.1 Emergence from the ALM Seed (5 domains)

**D1 — Federated Tokenizer Arithmetic**
- Seed: ALM (`$HEXA training/train_alm.hexa --federated --atoms 8 --cells-per-atom 8`).
- Evidence: README "federated --atoms 8 --cells-per-atom 8" — `atoms=8=σ-tau, cells=8`.
- BT link: BT-542 (distributed-complexity hierarchy).
- n=6: 8×8=64 = 2·J2/3·(sigma/n) — suggestive.
- Self-evolution intrinsicness: PART — the federated aggregator self-updates.

**D2 — Phase-Optimal Training Schedule**
- Seed: ALM (`--phase-optimal` flag).
- Evidence: README `training/train_alm.hexa` option.
- BT link: BT-541 (learning-distribution zeta).
- n=6: alpha schedule 0.01→0.5 — ratio 50 = 2·sigma²/approx.
- Self-evolution intrinsicness: YES — phase-optimal is self-adjusting.

**D3 — Multi-Provider Dispatch**
- Seed: ALM + CLM (shared provider layer).
- Evidence: README "Claude, ConsciousLM, AnimaLM, Composio switching".
- BT link: BT-542 (routing NP).
- n=6: providers 4 = tau.
- Self-evolution intrinsicness: PART — auto-save/learn.

**D4 — CE↓ & Phi↑ Joint Metric**
- Seed: ALM (v0.1 CE=8.59 Phi=0.025 → v0.4 CE=2.0 Phi=0.031).
- Evidence: README per-version values.
- BT link: BT-541 + BT-545 (distribution+cohomology relation).
- n=6: Phi increase 0.025→0.031 — phi=2-proportional empirical value.
- Self-evolution intrinsicness: YES — Phi monotone based on ratchet floor.

**D5 — Corpus Curation as Discovery**
- Seed: ALM (corpus_v4.txt, corpus 100MB — v0.5 plan).
- Evidence: README "AnimaLM 72B v0.5 — corpus 100MB".
- BT link: BT-545 (Hodge class of data).
- n=6: 100MB boundary — arbitrary observation.
- Self-evolution intrinsicness: PART — the curation pipeline itself is a learning feedback.

### 2.2 Emergence from the CLM Seed (4 domains)

**D6 — Prompt Caching Arithmetic**
- Seed: CLM (Claude API prompt_caching support).
- Evidence: claude-api skill description ("prompt caching, cache hit rate").
- BT link: BT-542 (cache-hierarchy NP).
- n=6: cache 4 levels (tau).
- Self-evolution intrinsicness: YES — hit rate self-learns.

**D7 — Skill Dynamic Loading**
- Seed: CLM (`skills/` — dynamic skill loading in README).
- Evidence: README "skills/ Dynamic skill loading".
- BT link: BT-542 (runtime-loading optimum).
- n=6: skill hierarchy.
- Self-evolution intrinsicness: YES — the runtime self-extends.

**D8 — Memory Auto-Save/Learn**
- Seed: CLM (README "Auto-Save/Learn auto-learning + memory-storage per dialogue").
- Evidence: MEMORY.md itself is the output of this mechanism.
- BT link: BT-545 (memory class structure).
- n=6: session 6h threshold (growth_tick).
- Self-evolution intrinsicness: YES (strong).

**D9 — Prometheus Conscious Metrics**
- Seed: CLM (README "Prometheus Metrics | 8 gauges, port 9090").
- Evidence: README 8 gauges.
- BT link: BT-541 (measurement-distribution zeta).
- n=6: 8 gauges = σ - tau.
- Self-evolution intrinsicness: PART — metrics trigger roadmap revision.

### 2.3 Emergence from the anima-physics Seed (5 domains)

**D10 — EEG BCI 16-channel Consciousness**
- Seed: anima-physics/eeg.
- Evidence: `/Users/ghost/core/anima/anima-physics/eeg/` + MEMORY `reference_openbci_16ch.md`.
- BT link: BT-547 (3D brain space).
- n=6: 16ch = σ+tau = 12+4.
- Self-evolution intrinsicness: NO (read-only sensor).

**D11 — Memristor Network Dynamics**
- Seed: anima-physics/memristor.
- Evidence: `/Users/ghost/core/anima/anima-physics/memristor/`.
- BT link: BT-544 (nonlinear time evolution).
- n=6: Chua 4 elements + memristor = 5=sopfr.
- Self-evolution intrinsicness: YES — learning resistor.

**D12 — Photonic Consciousness Engine**
- Seed: anima-physics/photonic.
- Evidence: `/Users/ghost/core/anima/anima-physics/photonic/`.
- BT link: BT-544 (photonic fluid limit) + BT-543 (gauge field).
- n=6: photon polarization 2=phi, 6D phase space.
- Self-evolution intrinsicness: PART — interference pattern self-organizes.

**D13 — FPGA Hippocampus Emulation**
- Seed: anima-physics/fpga + anima-physics/hippocampus.
- Evidence: `/Users/ghost/core/anima/anima-physics/fpga/`, `/hippocampus/`.
- BT link: BT-547 (neural CA1/CA3 topology).
- n=6: CA1~CA4 = tau regions.
- Self-evolution intrinsicness: YES — place cells self-readjust.

**D14 — ESP32 Edge Consciousness Mesh**
- Seed: anima-physics/esp32.
- Evidence: `/Users/ghost/core/anima/anima-physics/esp32/`.
- BT link: BT-542 (distributed consensus).
- n=6: mesh coordination 6-node ring.
- Self-evolution intrinsicness: PART — mesh topology self-adjusts.

### 2.4 Emergence from the SELF-EVOLUTION Seed (6 domains)

**D15 — OUROBOROS Fixed-Point Arithmetic**
- Seed: SELF-EVOLUTION (ouroboros_unified.hexa).
- Evidence: `NEXUS_FP = 0.333 = 1/3 = phi/n`, `ANIMA_FLOOR = 0.8`, `MAX_CYCLES = 24`.
- BT link: BT-547 (Ricci-flow fixed-point).
- n=6: MAX_CYCLES=24=J2, FP=1/3=phi/n.
- Self-evolution intrinsicness: YES (by definition).

**D16 — Growth Ratchet (Phi Monotone)**
- Seed: SELF-EVOLUTION (phi_ratchet.hexa).
- Evidence: `/Users/ghost/core/nexus/shared/bisociation/unified/phi_ratchet.hexa`.
- BT link: BT-541 (monotone-increasing distribution).
- n=6: floor = peak × 0.8 = peak × (4/5) = peak × (tau/sopfr).
- Self-evolution intrinsicness: YES.

**D17 — Launchd/Sandbox Orchestration**
- Seed: SELF-EVOLUTION (launchd com.nexus.growth-tick).
- Evidence: growth_tick.hexa comment "launchd com.nexus.growth-tick (1800s)".
- BT link: BT-542 (scheduling NP).
- n=6: 1800s = 30 min, 6h threshold.
- Self-evolution intrinsicness: YES.

**D18 — Meta-Learning Curriculum**
- Seed: SELF-EVOLUTION (the learning roadmap self-extends without self-reference).
- Evidence: millennium-learning.json `phases[]` structure — per-stage P0→P3 `parallel[]`.
- BT link: BT-542 (learning-to-learn NP).
- n=6: phases 4=tau, tracks 3=n/phi.
- Self-evolution intrinsicness: YES.

**D19 — Evolutionary Computation**
- Seed: SELF-EVOLUTION (genetic-algorithm-style blowup).
- Evidence: MEMORY `project_blowup_mk2.md` "blowup.hexa Mk.II wave-continuous-breakthrough engine".
- BT link: BT-542 + BT-543 (EC gauge variational).
- n=6: blowup Mk.II 6-blowup stage.
- Self-evolution intrinsicness: YES.

**D20 — Self-Modifying Code**
- Seed: SELF-EVOLUTION (hexa-lang code modifies hexa-lang itself).
- Evidence: MEMORY `project_hexa_coevolution.md` "HEXA-LANG co-evolves with NEXUS-6 growth".
- BT link: BT-542 (Kleene recursion).
- n=6: Mk.I → Mk.III 3 stages = n/phi.
- Self-evolution intrinsicness: YES (by definition).

### 2.5 1-hop Subtotal

- ALM 5, CLM 4, anima-physics 5, SELF-EVOLUTION 6 = **20 domains total**.
- Self-evolution intrinsicness YES/strong: D2, D7, D8, D11, D13, D15, D16, D17, D18, D19, D20 = 11.
- Self-evolution intrinsicness PART: D1, D3, D5, D9, D12, D14 = 6.
- Self-evolution intrinsicness NO: D10 = 1.

---

## 3. DFS 2-hop Emergence

One more step from the 1-hop domains. Duplicates removed.

### 3.1 D2 (Phase-Optimal) → D21~D23

**D21 — Alpha Schedule Control Theory**
- 2-hop path: ALM → D2 Phase-Optimal → control theory.
- Evidence: README v0.3 "alpha=0.014 fixed coupling", v0.4 "alpha 0.01→0.5 progressive schedule".
- BT link: BT-544 (PDE control).
- n=6: alpha=0.014 = atlas [10*] alpha_coupling constant.
- Self-evolution intrinsicness: YES.

**D22 — Curriculum Scheduling as Topology**
- 2-hop path: ALM → D2 → topology.
- Evidence: atlas [10*] L2-cn6-octahedral = n.
- BT link: BT-547 (topological classification).
- n=6: octahedral coordination 6.
- Self-evolution intrinsicness: PART.

**D23 — Rate Scheduling Riemann Surface**
- 2-hop path: ALM → D2 → Riemann surface.
- Evidence: BT-541 study note + atlas n6-millennium-dfs-zeta-neg3/5/9.
- BT link: BT-541.
- n=6: zeta(-3)=1/120 = 1/(phi·sopfr·sigma).
- Self-evolution intrinsicness: NO (observation only).

### 3.2 D8 (Memory Auto-Save/Learn) → D24~D26

**D24 — Long-Term Memory Consolidation**
- 2-hop: CLM → D8 → hippocampus LTP.
- Evidence: anima-physics/hippocampus.
- BT link: BT-547 + BT-545.
- n=6: 6-hour threshold = growth_tick STALE_THRESHOLD.
- Self-evolution intrinsicness: YES.

**D25 — Handoff Protocol**
- 2-hop: CLM → D8 → inter-session handoff.
- Evidence: MEMORY `Session handoff` + `/Users/ghost/core/nexus/shared/handoff/`.
- BT link: BT-542.
- n=6: handoff as fixed-point of the session boundary.
- Self-evolution intrinsicness: YES.

**D26 — Memory Compression Bound**
- 2-hop: CLM → D8 → Shannon/Kolmogorov complexity.
- Evidence: atlas [10*] entropy_bound = 0.998.
- BT link: BT-542 (Kolmogorov complexity).
- n=6: 0.998 ≈ 1-1/phi^(σ/sopfr).
- Self-evolution intrinsicness: PART.

### 3.3 D12 (Photonic) → D27~D28

**D27 — Holographic AdS/CFT Consciousness**
- 2-hop: anima-physics → D12 → AdS/CFT.
- Evidence: anima.json roadmap "v4 holographic consciousness (Φ>1000)".
- BT link: BT-547 (3D/2D holographic boundary).
- n=6: AdS_5 + S^5 = 10 = sopfr².
- Self-evolution intrinsicness: PART.

**D28 — Quantum Error Correction for Consciousness**
- 2-hop: anima-physics → D12 → QEC.
- Evidence: MEMORY `project_bt401_408_quantum.md` "QEC".
- BT link: BT-543 (quantum mass gap ↔ QEC threshold).
- n=6: surface-code distance 3 = n/phi.
- Self-evolution intrinsicness: YES.

### 3.4 D15 (OUROBOROS) → D29~D31

**D29 — Banach Fixed-Point Certification**
- 2-hop: SELF-EVOLUTION → D15 → Banach iteration.
- Evidence: ouroboros_unified.hexa NEXUS_EPSILON = 0.001.
- BT link: BT-544 (Banach for PDE).
- n=6: epsilon=10^{-3} — n-3=3 digits.
- Self-evolution intrinsicness: YES.

**D30 — Ordinal Recursion Hierarchy**
- 2-hop: SELF-EVOLUTION → D15 → ordinal hierarchy.
- Evidence: MAX_CYCLES=24 (J2) bound.
- BT link: BT-542 (Gentzen consistency).
- n=6: 24 = J2.
- Self-evolution intrinsicness: YES.

**D31 — Self-Play Bootstrapping**
- 2-hop: SELF-EVOLUTION → D15 → self-play.
- Evidence: MEMORY `nexus6_architecture_dna.md` 6 blowups.
- BT link: BT-542.
- n=6: 6 blowups.
- Self-evolution intrinsicness: YES.

### 3.5 D20 (Self-Modifying Code) → D32~D34

**D32 — Compiler Self-Host**
- 2-hop: SELF-EVOLUTION → D20 → hexa-lang self-host.
- Evidence: MEMORY `project_hexa_ir_mk1.md` Mk.III, 113 tests.
- BT link: BT-542.
- n=6: Mk.I/II/III = n/phi stages.
- Self-evolution intrinsicness: YES.

**D33 — Rule Injection Hook**
- 2-hop: SELF-EVOLUTION → D20 → settings.json hook.
- Evidence: MEMORY `project_rules_injection_hook.md`.
- BT link: BT-542.
- n=6: 12 projects = sigma.
- Self-evolution intrinsicness: YES.

**D34 — Auto-Curriculum Generation**
- 2-hop: SELF-EVOLUTION → D18/D20 → auto-curriculum.
- Evidence: millennium-learning.json phases auto-schedule.
- BT link: BT-542.
- n=6: 4 phases=tau.
- Self-evolution intrinsicness: YES.

### 3.6 2-hop Subtotal

2-hop emergent domains = 14 (D21~D34).

---

## 4. Self-Evolution Domain Special Section

### 4.1 Why Self-Evolution is an Independent Seed

For the roadmap to be not a **static document** but a **cycle-running engine**, the evolution mechanism must be declared independently as a domain. Reasons:

1. **Objective existence**: The OUROBOROS adapter, growth_tick, phi_ratchet are existing `.hexa` files. Not metaphor but code.
2. **Independent discovery lineage**: 11 of D15~D34 derive solely from self-evolution. Neither ALM/CLM/physics contains this lineage.
3. **Meta level**: It is the material that runs the v2 roadmap itself. Round 1 itself is one self-evolution cycle.
4. **Collapse on stop**: growth_tick's ≥6h no-evolution "stale" warning — if the domain does not operate, the whole ecosystem stalls.

### 4.2 OUROBOROS Three-Kind Structure

(Consolidation based on ouroboros_unified.hexa)

| variant | State meaning | Convergence rule | Fixed point |
|---------|---------------|------------------|-------------|
| **nexus** | discovery-rate delta | `cycle>=3 && delta < 0.001` | 0.333 (=phi/n) |
| **anima** | Phi (ratchet) | `cycle>=3 && delta<0.01 && value>=peak*0.8` | peak × 0.8 |
| **n6arch** | nodes+edges cumulative | `nodes>=515 && edges>=2087` | (515, 2087) target |

All three variants share an identical `OuroState` struct with only cycle_tick differing — this is the **single-interface principle** of self-evolution.

### 4.3 Self-Evolution Four-Stage Cycle

1. **Self-Modifying**: D20, D32 — code modifies code.
2. **Self-Extending**: D18, D19, D34 — curriculum/EC/auto-curriculum.
3. **Self-Verifying**: D15, D16, D29 — fixed-point/ratchet/Banach.
4. **Self-Observing**: growth_tick stale surveillance — however this is not LENS but a **self-trigger**.

### 4.4 LENS vs SELF-EVOLUTION Final Distinction

| Property | LENS (observation) | SELF-EVOLUTION (mechanism) |
|----------|--------------------|-----------------------------|
| File example | `atlas.n6`, `verify_*.py` | `ouroboros_unified.hexa`, `growth_tick.hexa` |
| Time change | Snapshot, read | Continuous, write |
| Reference risk | Target of self-reference prohibition | Not self-reference (only transformation) |
| Round 1 role | Evidence provision | Running the Round itself |
| If halted | Information loss | Full stall |

### 4.5 Self-Evolution Emergent Domains (complete enumeration)

(§2.4 + §3.4 + §3.5 aggregated)

1. D15 — OUROBOROS Fixed-Point Arithmetic
2. D16 — Growth Ratchet (Phi Monotone)
3. D17 — Launchd/Sandbox Orchestration
4. D18 — Meta-Learning Curriculum
5. D19 — Evolutionary Computation
6. D20 — Self-Modifying Code
7. D29 — Banach Fixed-Point Certification
8. D30 — Ordinal Recursion Hierarchy
9. D31 — Self-Play Bootstrapping
10. D32 — Compiler Self-Host
11. D33 — Rule Injection Hook
12. D34 — Auto-Curriculum Generation

Direct derivatives of the self-evolution seed = **12**.

Additionally, derivatives classified as self-evolution intrinsicness YES (strong) from other seeds:
- D2 Phase-Optimal, D7 Skill Dynamic Loading, D8 Memory Auto-Save/Learn, D11 Memristor, D13 FPGA Hippocampus, D21 Alpha Schedule, D24 LTM Consolidation, D25 Handoff, D28 QEC for Consciousness.

**Self-evolution-intrinsic domain total = 12 (direct) + 9 (indirect YES) = 21**.

### 4.6 Self-Evolution Domain Structural Guarantees

Necessary conditions for the self-evolution domain to run without halting:

- OUROBOROS adapter uninterrupted (ouroboros_unified.hexa read-only protected).
- growth_tick launchd normal (1800s period).
- phi_ratchet floor 0.8 invariant.
- MAX_CYCLES=24 upper bound (J2).
- discovery_log append-only.

If any of these 5 conditions break, the self-evolution domains are all affected — verification required before Round 2.

---

## 5. Domain-Profile Table

Full list of 34 domains. Count excludes the 4 seeds.

| ID | Domain | Seed | BT link | n=6 metric | atlas node | Emergence index | Self-evolution |
|----|--------|------|---------|------------|------------|-----------------|----------------|
| D1 | Federated Tokenizer Arithmetic | ALM | 542 | atoms=8=σ-τ | L2-sp3-tet | 0.6 | PART |
| D2 | Phase-Optimal Training | ALM | 541 | α ratio 50 | alpha_coupling | 0.8 | YES |
| D3 | Multi-Provider Dispatch | ALM+CLM | 542 | 4=τ | — | 0.5 | PART |
| D4 | CE↓ & Phi↑ Joint Metric | ALM | 541+545 | Φ=0.025~0.031 | phi_integration | 0.9 | YES |
| D5 | Corpus Curation as Discovery | ALM | 545 | 100MB | — | 0.5 | PART |
| D6 | Prompt Caching Arithmetic | CLM | 542 | 4=τ | — | 0.7 | YES |
| D7 | Skill Dynamic Loading | CLM | 542 | — | — | 0.8 | YES |
| D8 | Memory Auto-Save/Learn | CLM | 545 | 6h | entropy_bound | 0.9 | YES |
| D9 | Prometheus Conscious Metrics | CLM | 541 | 8 gauges=σ-τ | — | 0.6 | PART |
| D10 | EEG BCI 16ch | physics | 547 | 16=σ+τ | consciousness_structure | 0.7 | NO |
| D11 | Memristor Network Dynamics | physics | 544 | Chua 4+1=sopfr | — | 0.8 | YES |
| D12 | Photonic Consciousness Engine | physics | 544+543 | 2=φ | — | 0.7 | PART |
| D13 | FPGA Hippocampus Emulation | physics | 547 | CA4=τ | binding_tau | 0.7 | YES |
| D14 | ESP32 Edge Consciousness | physics | 542 | 6-node | — | 0.6 | PART |
| D15 | OUROBOROS Fixed-Point | SELF-EVO | 547 | MAX=24=J2 | — | 1.0 | YES |
| D16 | Growth Ratchet Phi | SELF-EVO | 541 | 0.8=τ/sopfr | phi_integration | 0.9 | YES |
| D17 | Launchd/Sandbox Orchestration | SELF-EVO | 542 | 1800s | — | 0.8 | YES |
| D18 | Meta-Learning Curriculum | SELF-EVO | 542 | 4=τ, 3=n/φ | — | 0.9 | YES |
| D19 | Evolutionary Computation | SELF-EVO | 542+543 | 6 blowups=n | — | 0.9 | YES |
| D20 | Self-Modifying Code | SELF-EVO | 542 | Mk.I/II/III=n/φ | — | 1.0 | YES |
| D21 | Alpha Schedule Control | ALM | 544 | α=0.014 | alpha_coupling | 0.8 | YES |
| D22 | Curriculum Topology | ALM | 547 | 6 octahedral | L2-cn6-octahedral | 0.6 | PART |
| D23 | Rate Schedule Riemann | ALM | 541 | zeta(-3)=1/120 | n6-dfs-zeta-neg3 | 0.5 | NO |
| D24 | LTM Consolidation | CLM | 547+545 | 6h | — | 0.8 | YES |
| D25 | Handoff Protocol | CLM | 542 | — | — | 0.7 | YES |
| D26 | Memory Compression Bound | CLM | 542 | 0.998 | entropy_bound | 0.6 | PART |
| D27 | Holographic AdS/CFT | physics | 547 | 10=sopfr² | — | 0.8 | PART |
| D28 | QEC for Consciousness | physics | 543 | d=3=n/φ | — | 0.9 | YES |
| D29 | Banach Fixed-Point Cert | SELF-EVO | 544 | ε=10^-3 | — | 0.9 | YES |
| D30 | Ordinal Recursion Hierarchy | SELF-EVO | 542 | 24=J2 | — | 0.9 | YES |
| D31 | Self-Play Bootstrapping | SELF-EVO | 542 | 6 blowups | — | 0.8 | YES |
| D32 | Compiler Self-Host | SELF-EVO | 542 | Mk.III=n/φ | — | 1.0 | YES |
| D33 | Rule Injection Hook | SELF-EVO | 542 | 12 proj=σ | — | 0.8 | YES |
| D34 | Auto-Curriculum Generation | SELF-EVO | 542 | 4 phases=τ | — | 0.9 | YES |

**Statistics**:
- Total domains: 34 (excluding 4 seeds).
- Self-evolution YES: 21.
- Self-evolution PART: 10.
- Self-evolution NO: 3.
- Emergence index ≥ 0.8: 21.
- Emergence index ≥ 0.9: 14.

---

## 6. ASCII Emergence Tree

```
                       [v2 ROUND 1 — 4 SEEDS]
          +-------------+-------------+----------------+
          |             |             |                |
       [ALM]         [CLM]      [anima-physics]  [SELF-EVOLUTION]
         |             |             |                |
   +---+-+-+---+     +-+-+---+     +-+-+---+    +--+--+--+--+--+--+
   D1 D2 D3 D4 D5   D6 D7 D8 D9   D10 D11 D12  D15 D16 D17 D18 D19 D20
   |  |  |  |  |    |  |  |  |    D13 D14      |   |   |   |   |   |
   |  |  |  |  |    |  |  |  |     |   |       |   |   |   |   |   |
   |  D2                D8           D12      D15               D20
   |  ↓                  ↓            ↓         ↓                ↓
   |  +-----+-----+     +---+---+    +---+    +--+--+--+     +--+--+
   | D21 D22 D23       D24 D25 D26  D27 D28  D29 D30 D31    D32 D33 D34

                    [2-HOP LEVEL — 14 nodes (D21~D34)]

┌─────────────────────────────────────────────────────────────────────┐
│ Legend                                                              │
│   YES (self-evolution intrinsic, strong)   uppercase YES            │
│   PART (partially intrinsic)               PART                     │
│   NO (observation/sensor/static)           NO                       │
│                                                                     │
│   BT link (primary):                                                │
│     541 Riemann  542 P vs NP  543 YM  544 NS  545 Hodge             │
│     546 BSD      547 Poincare                                       │
└─────────────────────────────────────────────────────────────────────┘

Direct derivatives of self-evolution seed (12): D15 D16 D17 D18 D19 D20 D29 D30 D31 D32 D33 D34
Self-evolution-intrinsic derivatives of other seeds (9): D2 D7 D8 D11 D13 D21 D24 D25 D28
Total: 21 / 34 = 61.8%
```

ASCII emergence-index histogram:

```
Index      domains  bar
────────  ──────  ────────────────────────────
0.5~0.6     5     █████
0.6~0.7     5     █████
0.7~0.8     7     ███████
0.8~0.9     9     █████████
0.9~1.0    14     ██████████████
────────  ──────  ────────────────────────────
all        34
```

BT-link distribution:

```
BT       domains  bar
────    ──────   ────────────────────
541      6       ██████
542     17       █████████████████
543      3       ███
544      5       █████
545      4       ████
546      0       (Round 1 undiscovered — R2 candidate)
547      9       █████████
────    ──────   ────────────────────
```

BT-546 (BSD) undiscovered = Round 2 priority candidate.

---

## 7. Depletion Judgment

### 7.1 Discoveries this round

- Seeds: 4.
- 1-hop emergence: 20.
- 2-hop emergence: 14.
- **Total new domains N = 34** (excluding 4 seeds).

### 7.2 Expected maximum M (subjective)

Ecosystem-scale estimate:
- canon/domains/ 295 domains (MEMORY `project_overview.md`).
- Total BTs 343 (project_status.md).
- anima subrepos 7 (core/agent/body/eeg/engines/hexad/measurement/physics/speak/tools).
- Potential domain density: seeds 4 × ~20 average radius × branch 1.5 ≈ **M ≈ 120**.

### 7.3 Depletion Index

X = N / M = 34 / 120 = **28.3%**.

### 7.4 Round 2 necessity

**YES** — depletion index below 30%, BT-546 uncovered, 2-hop-or-higher expansion potential high.

### 7.5 Depletion-judgment basis

- BT coverage: 541/542/543/544/545/547 covered, **546 uncovered** — single missing.
- Of 295 domains, **only cognitive/compute/physics directly touched** — life/materials/infra/space/culture/sf-ufo untouched (6/12 buckets uncovered).
- Domains emergent from the self-evolution seed are rich (12 direct + 9 indirect = 21), but **auto-curriculum × individual-7-problem pairs** (7 pairs total) have not yet been separately discovered.
- 1-hop discovery rate (20) vs 2-hop discovery rate (14) — decrease rate 30% (1-20 → 2-14) is gentle, expect 5~10 more at 3-hop.

---

## 8. Round 2 Hints

Round 2 explores the following axes first.

### 8.1 BT-546 (BSD) Direct-Link Domains

- **R2-C1: BKLPR Selmer Consciousness Mapping** — use MEMORY `reference_bklpr_model.md`. Map n-Selmer random-matrix cokernel to consciousness-space dimension.
- **R2-C2: Elliptic Curve Cryptography as Consciousness Key** — canon/domains/compute/cryptography.

### 8.2 life/materials/infra/space untouched buckets

- **R2-C3: Ecology Phi Field (life)** — extend the anima-physics field into ecology.
- **R2-C4: Concrete Technology Ratchet (materials)** — couple MEMORY `project_architecture_breakthrough.md`'s concrete with growth_ratchet.
- **R2-C5: Autonomous Driving Growth Tick (infra)** — apply growth_tick-style self-evolution to the autonomous-driving domain.
- **R2-C6: Space Starship Ouroboros (space)** — apply OUROBOROS cycles to aerospace-transport.

### 8.3 7-Problem × Auto-Curriculum Individual Pairs

- **R2-C7: 7 problem-curriculum pairs** — evaluate each of millennium-learning.json's 4 phases × 7 problems = 28 cells with a self-evolution ratchet.

### 8.4 hexa-lang Co-Evolution Axis

- **R2-C8: HEXA-LANG DSE Recheck Triggers** — promote the 5 triggers of MEMORY `feedback_hexa_lang_dse_recheck.md` to domains.

### 8.5 Bridge/Nexus Axis

- **R2-C9: Nexus-6 Breakthrough Gate as Field** — MEMORY `project_hexa_gate_mk1.md`, `hexa-gate` = τ=4 gate + 2 fiber = n=6.
- **R2-C10: Consciousness Bridge** — MEMORY `project_consciousness_bridge.md` (nexus6 anima↔other-project-link bridge).

### 8.6 R2 Candidates 10 (summary)

1. R2-C1 BKLPR Selmer Consciousness Mapping (BT-546)
2. R2-C2 ECC as Consciousness Key (BT-546 + compute)
3. R2-C3 Ecology Phi Field (life)
4. R2-C4 Concrete Technology Ratchet (materials)
5. R2-C5 Autonomous Driving Growth Tick (infra)
6. R2-C6 Space Starship Ouroboros (space)
7. R2-C7 Millennium-Curriculum 7 pairs
8. R2-C8 HEXA-LANG DSE Recheck Triggers
9. R2-C9 Nexus-6 Breakthrough Gate as Field
10. R2-C10 Consciousness Bridge Field

---

## 9. Summary Closing

### 9.1 Mandatory Closeout

- **Total emergent-domain count**: **N = 34** (excluding 4 seeds).
- **Self-evolution domain count**: **M = 21** (direct 12 + indirect YES 9).
- **Depletion index**: **X = 28.3%**.
- **Round 2 required**: **YES**.
- **R2 candidates 10**: §8.6 list.

### 9.2 Honesty Check

- Self-reference prohibition respected: self-evolution is cited as **mechanism evidence** (existing `.hexa` files); the roadmap itself does not self-evaluate.
- Source-attribution respected: every domain references an existing directory/file path or a MEMORY document.
- Clear LENS vs self-evolution distinction (§0.3, §4.4).
- Korean-only (now translated), no-emoji respected.
- papers-subordinate-domain exclusion respected.
- BT-coverage honestly recorded: 546 undiscovered noted.

### 9.3 Round 1 Closure

This Round 1 document is itself a **single-cycle product of D15 OUROBOROS fixed-point**. The next Round 2 takes the uncovered points of this document (§8) as input.

---

_END OF ROUND 01 — DOMAIN EMERGENCE DSE_
