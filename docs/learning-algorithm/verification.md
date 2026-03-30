# N6 Learning Algorithm Hypotheses -- Verification Against Real-World Data

## Methodology

Each hypothesis (H-LA-1 through H-LA-28) is evaluated on three axes:

1. **Math check**: Does the claimed n=6 derivation hold arithmetically?
2. **Real-world check**: Does the predicted value match actual industry standards or published research?
3. **Grade**: EXACT / CLOSE / WEAK / FAIL / UNVERIFIABLE

Grading rubric:
- **EXACT**: The n=6-derived value matches a well-known standard within 5%.
- **CLOSE**: The value is in a reasonable range but not a recognized standard (within 20%).
- **WEAK**: The derivation is mathematically correct but the connection to practice is speculative or the value is outside typical ranges.
- **FAIL**: The predicted value contradicts well-established practice or published results.
- **UNVERIFIABLE**: No widely accepted standard exists for comparison; claim is domain/task-dependent.

---

## Tier 1: Reinforcement Learning

### H-LA-1: Sigma Discount Factor -- gamma = 12/13 ~ 0.923

**Math check**: sigma(6) = 12 is correct. 12/(12+1) = 12/13 ~ 0.923. Arithmetic holds.

**Real-world check**: FAIL. Standard RL discount factors are:
- Atari (DeepMind DQN): gamma = 0.99
- MuJoCo continuous control (PPO, SAC): gamma = 0.99 or 0.995
- Robotics (short-horizon): gamma = 0.95 to 0.99
- Very short-horizon tasks: gamma = 0.9 is sometimes used

gamma = 0.923 gives an effective horizon of only 13 steps. At 50 Hz control this is 0.26 seconds -- far too short for most locomotion or manipulation tasks. The claim that this is better than 0.99 for general RL contradicts decades of practice. Lower gamma can help in specific short-horizon settings, but 0.923 is not a recognized optimum.

**Grade: FAIL**

---

### H-LA-2: Tau-Divisor TD(lambda) -- lambda = 0.5

**Math check**: phi(6)/tau(6) = 2/4 = 0.5. Arithmetic holds.

**Real-world check**: WEAK. Standard TD(lambda) values in practice:
- GAE (Schulman et al.): lambda = 0.95 or 0.97 is standard for PPO
- TD(lambda) in tabular settings: lambda = 0.9 is common
- lambda = 0.5 is not a recognized optimum; it is lower than most recommended values

lambda = 0.5 overweights short-horizon bootstrapping. While it reduces variance, the bias increase typically hurts performance compared to lambda = 0.9-0.97. The claim that 0.5 is a "golden division point" has no empirical support in the RL literature.

**Grade: FAIL**

---

### H-LA-3: Egyptian Fraction Reward Decomposition -- 1/2 + 1/3 + 1/6

**Math check**: 1/2 + 1/3 + 1/6 = 1. Correct, and these are the reciprocals of proper divisors of 6.

**Real-world check**: WEAK. Multi-objective reward weighting is entirely task-dependent. There is no universal "best" weighting. The 50/33/17 split is a plausible heuristic for "primary/secondary/auxiliary" decomposition, and the constraint that weights sum to 1 is reasonable. However:
- Reward weights in practice are found via hyperparameter search or domain knowledge
- No published benchmark uses 1/2 + 1/3 + 1/6 as a standard
- The claim of "no tuning needed" is too strong

The structure (dominant + moderate + minor = 1) is a sensible design pattern, but it is not uniquely optimal.

**Grade: WEAK**

---

## Tier 2: Sim-to-Real Transfer

### H-LA-4: Tau-Domain Randomization -- 4 domains

**Math check**: tau(6) = 4. Correct.

**Real-world check**: CLOSE. The four proposed randomization domains (dynamics, visual, sensor, actuator) are a reasonable taxonomy. In practice:
- OpenAI (Dactyl, 2019): used ~50+ individual randomization parameters, but they cluster into roughly these categories
- NVIDIA Isaac Gym: typically randomizes across dynamics, visual appearance, and sensor noise
- The idea of 4 high-level categories is a reasonable organizational framework

The claim that ">4 domains" hurts is too strong -- more fine-grained randomization categories have been used successfully. But 4 as a high-level grouping is defensible.

**Grade: CLOSE**

---

### H-LA-5: Sigma-Step Domain Adaptation -- 12 steps

**Math check**: sigma(6) = 12. Correct.

**Real-world check**: UNVERIFIABLE. Curriculum-based domain adaptation exists in the literature, but:
- There is no standard number of adaptation steps
- AutoDR (Akkaya et al., OpenAI) uses continuous adaptation, not fixed stages
- 12 stages is neither standard nor contradicted -- it is one design choice among many
- The claim about "performance jumps at divisor checkpoints" is unfalsifiable without experiments

**Grade: UNVERIFIABLE**

---

## Tier 3: Imitation Learning

### H-LA-6: Egyptian Data Mix -- 1/2 demo + 1/3 self-play + 1/6 correction

**Math check**: 1/2 + 1/3 + 1/6 = 1. Correct.

**Real-world check**: WEAK. Data mixing ratios in imitation learning are task-dependent:
- DAgger (Ross et al.): uses a schedule that shifts from demo to online data
- IWR (Mandlekar et al.): weighted replay, ratios tuned per task
- The specific 50/33/17 split is not a recognized standard
- Having a majority of expert demonstrations with smaller portions of self-play and corrections is a reasonable heuristic, but the claim of 40% efficiency improvement over pure demonstration is unsubstantiated

The structure is plausible as a starting point but not uniquely derived from n=6.

**Grade: WEAK**

---

### H-LA-7: Sopfr BC Depth -- 5 layers

**Math check**: sopfr(6) = 2 + 3 = 5. Correct.

**Real-world check**: CLOSE. For behavioral cloning in robotics:
- ACT (Zhao et al., 2023): uses transformer-based architectures, not simple MLPs
- Diffusion Policy: uses U-Net style architectures with many more layers
- Simple MLP policies: 2-4 hidden layers is common (e.g., robomimic uses 2-layer MLPs)
- 5 layers is in a reasonable range for MLP-based BC, though slightly deeper than the most common 2-3 layer configurations

The "2 encoder + 3 decoder" decomposition aligned with prime factors is a creative interpretation, but 5-layer MLPs are not a recognized optimum. Still, it is within the plausible range.

**Grade: CLOSE**

---

## Tier 4: Reward Shaping

### H-LA-8: R(n)=1 Reward Normalization

**Math check**: R(6) = sigma(6)*phi(6)/(6*tau(6)) = 12*2/(6*4) = 24/24 = 1. Correct.

**Real-world check**: WEAK. The practical implementation described (using running statistics to normalize mean*variance/(scale*count) = 1) is essentially a form of adaptive reward normalization. Existing approaches:
- PopArt (van Hasselt et al.): normalizes value targets adaptively -- well-established
- Reward standardization (z-score): common in PPO implementations
- The n=6 formula adds a layer of interpretation but the actual normalization is standard practice repackaged

The "R(6) = 1" identity is mathematically elegant but the practical implementation reduces to standard normalization. The claimed equivalence to PopArt suggests this is not novel.

**Grade: WEAK**

---

### H-LA-9: Divisor-Structured Potential Shaping -- {1, 2, 3, 6} hierarchy

**Math check**: The divisor lattice of 6 is {1, 2, 3, 6}. Egyptian fraction weights 1/d sum correctly. The PBRS theorem (Ng et al., 1999) does guarantee policy invariance for any potential function, so a weighted sum of sub-goal potentials is valid.

**Real-world check**: WEAK. Potential-based reward shaping is a well-studied technique, and hierarchical sub-goals are common. However:
- The specific choice of 4 sub-goals weighted by 1, 1/2, 1/3, 1/6 is arbitrary
- In practice, potential functions are designed based on domain knowledge, not number theory
- The claim of 2-3x learning speedup is plausible for PBRS in general, not specific to this weighting

The mathematical framework is valid (PBRS preserves optimal policies by theorem), but the n=6 connection is ornamental.

**Grade: WEAK**

---

## Tier 5: Curriculum Learning

### H-LA-10: Sigma-12 Difficulty Curriculum -- 12 stages

**Math check**: sigma(6) = 12. Correct.

**Real-world check**: UNVERIFIABLE. Curriculum learning stages vary widely:
- Bengio et al. (2009): no fixed number of stages
- ALP-GMM (Portelas et al.): continuous, no fixed stages
- OpenAI Rubik's Cube: used automatic domain randomization, not fixed stages
- 12 stages is neither standard nor obviously wrong -- it is a design choice

The claim about "performance jumps at divisor checkpoints" is testable but unverified.

**Grade: UNVERIFIABLE**

---

### H-LA-11: Tau-Phase Training -- 4 phases (Imitation/RL/Adaptation/Deployment)

**Math check**: tau(6) = 4. Correct.

**Real-world check**: CLOSE. Modern physical AI pipelines often do follow a multi-phase approach:
- Tesla FSD: pretrain + RL + sim adaptation + deployment optimization
- Google RT-2: pretrain (foundation model) + finetune + evaluation + deployment
- The 4-phase structure (imitation -> RL -> adaptation -> deployment) is a reasonable abstraction

However, the claim that 50% of effort goes to deployment (based on divisor ratio 6/12) contradicts practice where the majority of compute is in training phases 1-2. The phase structure is sensible; the time allocation is not.

**Grade: CLOSE** (for the 4-phase structure; time allocation ratios are WEAK)

---

## Tier 6: Policy Network Architecture

### H-LA-12: Phi-Bottleneck Actor-Critic -- 4/3x expansion

**Math check**: tau(6)^2/sigma(6) = 16/12 = 4/3. Correct.

**Real-world check**: FAIL. Standard FFN expansion ratios:
- Transformer FFN: 4x expansion is the standard (Vaswani et al., 2017)
- MLP policies in RL: typically use hidden layers of 256 or 512 (not a ratio-based expansion)
- 4/3x expansion is aggressively small and would significantly limit network capacity
- The claim of "67% parameter reduction with <2% performance loss" would require experimental evidence

A 4/3x ratio is far below what is standard. While smaller networks can work for simple tasks, claiming this as universally optimal contradicts common practice.

**Grade: WEAK**

---

### H-LA-13: Phi6 Activation -- x^2 - x + 1

**Math check**: The 6th cyclotomic polynomial is indeed x^2 - x + 1. Correct.

**Real-world check**: UNVERIFIABLE. Custom activation functions are an active research area:
- GELU and SiLU are current standards
- x^2 - x + 1 is a simple polynomial that could work as an activation function
- The 71% FLOPs claim vs GELU is plausible since GELU uses exp/erf operations
- However, no published benchmark validates Phi6 activation in RL policy networks
- Polynomial activations risk unbounded outputs and training instability

The computational simplicity is real, but the performance claim requires experimental validation.

**Grade: UNVERIFIABLE**

---

### H-LA-14: Dedekind Head Attention -- 12 heads with pruning

**Math check**: psi(6) = 12, sigma(6) = 12. Both correct. psi(n) = sigma(n) for n=6 is a valid identity.

**Real-world check**: CLOSE. Attention head counts in practice:
- BERT-base: 12 heads (this is a match!)
- GPT-2 small: 12 heads
- Decision Transformer (Chen et al., 2021): follows standard transformer configs
- 12 heads is a genuinely common choice in transformer architectures

Dynamic head pruning is also an active research area (Michel et al., 2019 found many heads can be pruned). The 25% pruning claim is within published ranges.

The match with BERT/GPT-2 head count is notable. However, 12 heads became standard for independent engineering reasons (it divides common hidden dimensions like 768).

**Grade: CLOSE**

---

## Tier 7: Exploration

### H-LA-15: Boltzmann Exploration -- epsilon = 1/e ~ 0.368

**Math check**: 1/e ~ 0.3679. The connection to Boltzmann distribution at E=kT is correct.

**Real-world check**: FAIL. Standard exploration rates:
- DQN: epsilon starts at 1.0, decays to 0.01 or 0.1
- Typical fixed epsilon: 0.1 to 0.2 for epsilon-greedy
- SAC: uses entropy regularization, not fixed epsilon
- epsilon = 0.368 is extremely high for most tasks -- the agent would act randomly 37% of the time

An epsilon of 0.368 would severely degrade performance in most environments. Exploration rates this high are only used at the very beginning of training as part of a decay schedule.

**Grade: FAIL**

---

### H-LA-16: Mertens Dropout Policy Noise -- p = ln(4/3) ~ 0.288

**Math check**: ln(4/3) ~ 0.2877. tau(6)^2/sigma(6) = 4/3. Correct.

**Real-world check**: CLOSE. Standard dropout rates:
- Original dropout paper (Srivastava et al., 2014): p = 0.5 for hidden layers
- Modern practice: p = 0.1 to 0.3 for most networks
- RL policy networks: dropout is rarely used, but when used, p = 0.1 to 0.2 is typical
- p = 0.288 is within the plausible range, though on the high side for RL

The claim that dropout alone can replace explicit exploration noise (OU, Gaussian) is interesting but not well-established. The dropout rate itself is in a reasonable range.

**Grade: CLOSE**

---

### H-LA-17: Squarefree Exploration Graph -- mu(6) = 1

**Math check**: 6 = 2 * 3, which is squarefree. mu(6) = (-1)^2 = 1. Correct.

**Real-world check**: UNVERIFIABLE. The idea of using Mobius inversion to prune redundant state visits is mathematically interesting but:
- No published algorithm implements "squarefree exploration" as described
- Count-based exploration (Bellemare et al., 2016) and RND (Burda et al., 2019) are standard
- The connection between mu(6)=1 and exploration graph structure is metaphorical
- The 30-50% coverage improvement claim is unsubstantiated

**Grade: UNVERIFIABLE**

---

## Tier 8: Multi-Agent

### H-LA-18: J2(6) = 24 Agent Swarm

**Math check**: J_2(6) = 6^2 * product_{p|6}(1 - 1/p^2) = 36 * (1 - 1/4) * (1 - 1/9) = 36 * 3/4 * 8/9 = 24. Correct.

**Real-world check**: WEAK. Multi-agent swarm sizes in practice:
- StarCraft MARL: varies (5 to 27 agents depending on scenario)
- Swarm robotics: team sizes from 3 to 1000+ depending on application
- OpenAI Five (Dota 2): 5 agents
- There is no universal "optimal swarm size" -- it depends entirely on the task
- The connection to Leech lattice dimension is numerologically interesting but not physically meaningful for agent counts

**Grade: WEAK**

---

### H-LA-19: Egyptian Role Allocation -- 12:8:4

**Math check**: 24 * (1/2, 1/3, 1/6) = (12, 8, 4). Correct.

**Real-world check**: WEAK. Role allocation in multi-agent systems:
- The claim about insect colonies is partially true -- honeybees do have age-dependent role specialization, but not in 50/33/17 ratios
- In MARL, role allocation is typically learned, not fixed
- The explorer/executor/supervisor taxonomy is a reasonable design pattern
- The specific ratios are not supported by either biology or MARL literature

**Grade: WEAK**

---

### H-LA-20: Carmichael Communication Cycle -- every 2 steps

**Math check**: lambda(6) = lcm(lambda(2), lambda(3)) = lcm(1, 2) = 2. Correct.

**Real-world check**: CLOSE. Communication frequency in multi-agent systems:
- CommNet, TarMAC: communicate every step (cycle = 1)
- Some works use periodic communication to reduce overhead
- 2-step communication is a simple and reasonable design choice
- The 50% bandwidth reduction claim is trivially true (communicate half as often)
- The claim that 95% of performance is retained with 50% less communication is plausible for many cooperative tasks, supported by work on communication-efficient MARL

**Grade: CLOSE**

---

## Tier 9: Model Predictive Control

### H-LA-21: Tau-Horizon MPC -- H = 4

**Math check**: tau(6) = 4. Correct.

**Real-world check**: WEAK. MPC horizon in practice:
- Legged locomotion (MIT Cheetah, ANYmal): H = 10 to 30 at 50-100 Hz
- Autonomous driving: H = 20 to 50
- Drone control: H = 10 to 20
- H = 4 is extremely short for most MPC applications
- At 50 Hz, H=4 means planning only 80ms ahead -- insufficient for locomotion or manipulation

The claim that H=4 is universally optimal contradicts standard MPC practice where longer horizons are needed for stability guarantees.

**Grade: FAIL**

---

### H-LA-22: Sigma-12 Planning Steps -- 12-step rollout

**Math check**: sigma(6) = 12. Correct.

**Real-world check**: CLOSE. Model-based RL imagination rollout lengths:
- Dreamer v1 (Hafner et al., 2020): imagination horizon = 15
- Dreamer v2: 15 steps
- Dreamer v3: 15 steps
- MBPO (Janner et al., 2019): 1 to 25 steps depending on model quality
- 12 steps is within the typical range (5-50), though slightly below Dreamer's default of 15

The claim that model error becomes dominant beyond 12 steps is reasonable but the exact crossover depends on model quality and environment complexity.

**Grade: CLOSE**

---

### H-LA-23: Egyptian Control Allocation -- 1/2 FF + 1/3 FB + 1/6 Adaptation

**Math check**: 1/2 + 1/3 + 1/6 = 1. Correct.

**Real-world check**: WEAK. Control allocation in practice:
- Classical control: feedforward + feedback is standard, but ratios depend on system dynamics
- Adaptive control: adaptation is typically a correction term, not a fixed fraction
- The 50/33/17 split has no basis in control theory
- In practice, feedback dominance varies: stable systems need less feedback, unstable systems more
- The allocation cannot be fixed -- it must adapt to operating conditions

**Grade: WEAK**

---

## Tier 10: Chip-in-the-Loop

### H-LA-24: Egyptian Latency Budget -- 1/2 sense + 1/3 decide + 1/6 act

**Math check**: 1/2 + 1/3 + 1/6 = 1. Correct.

**Real-world check**: CLOSE. Real-time pipeline budgets:
- Autonomous driving (NVIDIA): perception ~60%, planning ~30%, actuation ~10%
- This roughly matches 1/2 + 1/3 + 1/6 (50% + 33% + 17%)!
- The observation that sensing is the most expensive stage is well-established
- Actuation being the lightest stage is also standard

This is one of the stronger matches. The industry trend of allocating roughly half the compute budget to perception is well-documented.

**Grade: CLOSE**

---

### H-LA-25: Tau-Stage Inference Pipeline -- 4 stages

**Math check**: tau(6) = 4. Correct.

**Real-world check**: CLOSE. Pipeline stage counts:
- Classic RISC: 5-stage pipeline (IF, ID, EX, MEM, WB)
- Modern GPUs: much deeper pipelines (10-20+ stages)
- ML accelerator inference: 3-5 stages is typical for simple designs
- The 4-stage decomposition (encode, extract, infer, decode) is reasonable for an inference accelerator

4 stages is within the normal range but not uniquely optimal. The RISC 5-stage pipeline is a closer "natural" number.

**Grade: CLOSE**

---

### H-LA-26: Boltzmann Thermal Throttling -- threshold at 1/e ~ 63.2%

**Math check**: 1 - 1/e ~ 0.632. The Boltzmann connection is valid.

**Real-world check**: CLOSE. Thermal throttling thresholds:
- Intel CPUs: begin throttling around 80-100C (roughly 80-90% of T_junction max)
- NVIDIA GPUs: throttle at ~83C typically (varies by SKU)
- ARM mobile SoCs: thermal governors activate at configurable thresholds, often 70-80%
- Starting throttling at 63.2% of thermal budget is more conservative than industry practice (which typically starts at 75-85%)

The threshold is on the conservative side but not unreasonable. The Boltzmann physics motivation is elegant. Actual practice uses higher thresholds to maximize performance.

**Grade: WEAK**

---

### H-LA-27: Sigma-Core Distribution -- 12 cores for inference

**Math check**: sigma(6) = 12. J_2(6) = 24. 12 = 24/2. Correct.

**Real-world check**: WEAK. Core counts for ML inference:
- Google TPU v4: 2 tensor cores per chip
- NVIDIA A100: 108 SMs, thousands of CUDA cores
- Apple Neural Engine: 16 cores (A15+)
- Intel Gaudi: depends on configuration
- 12 cores is a design choice, not a universal optimum
- The "1 core per attention head" mapping is a valid architectural concept but not standard practice (modern hardware uses parallelism within matrix operations, not head-level parallelism)

**Grade: WEAK**

---

### H-LA-28: Lambda-2 Compute-Refresh Cycle -- double buffering

**Math check**: lambda(6) = 2. Correct.

**Real-world check**: EXACT. Double buffering is one of the most fundamental techniques in computer science:
- GPU rendering: standard double (or triple) buffering
- Network packet processing: ping-pong buffers
- ML inference: weight double-buffering is standard on accelerators
- The minimum useful buffer count is indeed 2

While lambda(6) = 2 gives the right answer, double buffering was invented for completely independent engineering reasons. The n=6 derivation is coincidental, but the value is genuinely correct.

**Grade: EXACT**

---

## Summary Table

| ID | Hypothesis | n=6 Math | Real-World Match | Grade |
|----|-----------|----------|-----------------|-------|
| H-LA-1 | Sigma Discount gamma=0.923 | OK | Standard is 0.99; 0.923 is too low | **FAIL** |
| H-LA-2 | TD(lambda=0.5) | OK | Standard is 0.9-0.97; 0.5 is too low | **FAIL** |
| H-LA-3 | Egyptian Reward 1/2+1/3+1/6 | OK | Task-dependent; no universal standard | **WEAK** |
| H-LA-4 | 4-Domain Randomization | OK | Reasonable taxonomy, roughly matches practice | **CLOSE** |
| H-LA-5 | 12-Step Domain Adaptation | OK | No standard exists | **UNVERIFIABLE** |
| H-LA-6 | Egyptian Data Mix | OK | Task-dependent; no universal ratio | **WEAK** |
| H-LA-7 | 5-Layer BC Network | OK | Plausible range for MLP policies | **CLOSE** |
| H-LA-8 | R(n)=1 Normalization | OK | Reduces to standard normalization | **WEAK** |
| H-LA-9 | Divisor Potential Shaping | OK | Valid PBRS; weighting is arbitrary | **WEAK** |
| H-LA-10 | 12-Stage Curriculum | OK | No standard exists | **UNVERIFIABLE** |
| H-LA-11 | 4-Phase Training | OK | Reasonable pipeline structure | **CLOSE** |
| H-LA-12 | 4/3x Actor-Critic | OK | Too narrow vs standard 4x expansion | **WEAK** |
| H-LA-13 | Phi6 Activation | OK | Untested in RL | **UNVERIFIABLE** |
| H-LA-14 | 12-Head Attention | OK | Matches BERT/GPT-2 head count | **CLOSE** |
| H-LA-15 | Boltzmann epsilon=0.368 | OK | Way too high; standard is 0.01-0.1 | **FAIL** |
| H-LA-16 | Mertens Dropout p=0.288 | OK | Within plausible range (0.1-0.3) | **CLOSE** |
| H-LA-17 | Squarefree Exploration | OK | No published algorithm | **UNVERIFIABLE** |
| H-LA-18 | 24-Agent Swarm | OK | Task-dependent; no universal optimum | **WEAK** |
| H-LA-19 | Egyptian Role 12:8:4 | OK | Not supported by biology or MARL | **WEAK** |
| H-LA-20 | 2-Step Communication | OK | Reasonable bandwidth/performance tradeoff | **CLOSE** |
| H-LA-21 | MPC Horizon H=4 | OK | Too short; standard is 10-30 | **FAIL** |
| H-LA-22 | 12-Step Rollout | OK | Close to Dreamer's 15; reasonable | **CLOSE** |
| H-LA-23 | Egyptian Control Split | OK | No fixed split in control theory | **WEAK** |
| H-LA-24 | Egyptian Latency Budget | OK | Roughly matches AV industry practice | **CLOSE** |
| H-LA-25 | 4-Stage Pipeline | OK | Reasonable for inference accelerator | **CLOSE** |
| H-LA-26 | 1/e Thermal Throttle | OK | Too conservative vs industry 75-85% | **WEAK** |
| H-LA-27 | 12-Core Distribution | OK | Core counts are design-specific | **WEAK** |
| H-LA-28 | Double Buffering (lambda=2) | OK | Matches universal CS practice | **EXACT** |

## Grade Distribution

| Grade | Count | Percentage |
|-------|-------|------------|
| EXACT | 1 | 3.6% |
| CLOSE | 10 | 35.7% |
| WEAK | 10 | 35.7% |
| FAIL | 4 | 14.3% |
| UNVERIFIABLE | 3 | 10.7% |

## Overall Assessment

**All 28 n=6 derivations are arithmetically correct.** The number theory is sound throughout.

**The connection to real-world practice is mixed:**

**Strongest matches (EXACT/CLOSE):**
- H-LA-28 (double buffering = 2) is genuinely a universal standard, though independently motivated.
- H-LA-14 (12 attention heads) matches BERT/GPT-2, though for independent reasons.
- H-LA-24 (latency budget ~50/33/17) roughly matches autonomous vehicle pipeline allocation.
- H-LA-22 (12-step rollout) is close to Dreamer's default of 15.

**Clear failures:**
- H-LA-1 (gamma=0.923): Industry standard is 0.99. The effective horizon of 13 steps is too short.
- H-LA-2 (TD lambda=0.5): GAE standard is 0.95-0.97.
- H-LA-15 (epsilon=0.368): Exploration rate is 3-30x higher than practice.
- H-LA-21 (MPC H=4): Standard horizons are 10-30 steps.

**Fundamental pattern:** The n=6 framework generates values that are mathematically elegant but systematically biased toward small numbers (2, 4, 5, 12, 13, 24). When a domain happens to use values in that range (attention heads, pipeline stages, buffer counts), the match is reasonable. When a domain uses larger values (discount factors near 1, long MPC horizons, high lambda), the n=6 derivation fails.

The Egyptian fraction 1/2 + 1/3 + 1/6 = 1 decomposition is the most broadly applicable pattern -- not because n=6 is special, but because "half + third + sixth" is a reasonable importance hierarchy for any three-way split. This is a useful heuristic, not a deep law.
