# N6 Robotics Hypotheses — Independent Verification

Verification of H-ROB-1 through H-ROB-28 against real-world data and mathematical validity.

**Grading scale:**
- **EXACT** — Predicted value matches real-world standard precisely
- **CLOSE** — Within ~20% or qualitatively correct but not exact
- **WEAK** — Loose connection; real-world data partially supports but the n=6 derivation is a stretch
- **FAIL** — Prediction contradicts real-world data or math is wrong
- **UNVERIFIABLE** — No accessible real-world benchmark to compare against

---

## H-ROB-1: Humanoid Major Joints = sigma(6) = 12

**Math check:** sigma(6) = 1+2+3+6 = 12. Correct.

**Real-world check:** Counting bilateral pairs of shoulder, elbow, wrist, hip, knee, ankle = 6 types x 2 = 12. This is a reasonable count of "major" joints. However, this is selective — the human body has more major joints than 12 if you include the spine (cervical, thoracic, lumbar), jaw, fingers, toes. Real humanoid robots vary: ASIMO has 34 DOF across many joints; Atlas (Boston Dynamics) has 28 joints. The "12 major joints" framing requires defining "major" to fit the number.

The divisor-to-grouping mapping ({1,2,3,6} = 1 skeleton, 2 chains, 3 upper + 3 lower, 6 types) is a post-hoc narrative overlay, not a derivation.

**Grade: CLOSE** — 12 is a defensible count of large bilateral limb joints, but the framing is cherry-picked.

---

## H-ROB-2: Quadruped Legs = tau(6) = 4, Each Leg = 6 DOF

**Math check:** tau(6) = 4. Correct (divisors: 1, 2, 3, 6).

**Real-world check:** 4 legs for quadrupeds — trivially true by definition, not a prediction. The claim that each leg has 6 DOF is **wrong** for commercial quadrupeds:
- Boston Dynamics Spot: **3 DOF per leg** (hip abduction, hip flexion, knee flexion) = 12 total
- Unitree B2/Go2: **3 DOF per leg** = 12 total
- ANYmal (ETH): **3 DOF per leg** = 12 total

No commercial quadruped uses 6 DOF per leg. 3 DOF/leg is the overwhelming industry standard. The claim that 6-DOF legs would give 35% better terrain adaptability is unverified and contradicted by the success of 3-DOF designs in extremely rough terrain.

**Grade: FAIL** — 4 legs is trivial (not a prediction), and 6 DOF/leg contradicts all major commercial quadrupeds (3 DOF/leg is standard).

---

## H-ROB-3: Hexapod = n = 6 Legs

**Math check:** n = 6. Trivially correct.

**Real-world check:** Hexapod robots exist (PhantomX, various research platforms) and do have excellent static stability. However, the hypothesis claims hexapods are the "mathematically optimal" walking form. In practice:
- Commercial legged robots are overwhelmingly **quadrupeds** (Spot, ANYmal, Unitree) or **bipeds** (Atlas, Digit)
- Hexapods are niche — used mainly in research and hobbyist contexts
- Insects have 6 legs, but the most agile terrestrial animals are quadrupeds and bipeds
- The tripod gait stability argument is valid but doesn't account for speed, agility, or energy efficiency where quadrupeds excel

**Grade: WEAK** — Hexapods exist and are stable, but calling 6 legs "optimal" is contradicted by the commercial dominance of quadrupeds and bipeds.

---

## H-ROB-4: Gripper = sopfr(6) = 5 Fingers, phi(6) = 2 Jaws

**Math check:** sopfr(6) = 2+3 = 5. phi(6) = 2. Both correct.

**Real-world check:**
- **2-jaw parallel gripper**: Yes, this is the dominant industrial gripper form. EXACT match.
- **5 fingers (human hand)**: The human hand does have 5 fingers. However, the human hand has approximately **27 DOF** (not 24 as J_2(6) would suggest — see H-ROB-5). Most dexterous robot hands also use 4 or 5 fingers (Shadow Hand: 5 fingers/24 DOF; Allegro Hand: 4 fingers/16 DOF). The claim that 4-finger is "suboptimal" is contradicted by Allegro Hand's wide research adoption.
- sopfr(6) = 5 matching human fingers is a neat coincidence but not a derivation — evolution determined finger count, not number theory.

**Grade: CLOSE** — 2-jaw gripper match is real. 5-finger match is a coincidence with human anatomy, not a validated design principle.

---

## H-ROB-5: Total Humanoid DOF = J_2(6) = 24

**Math check:** J_2(6) = 36 * (3/4) * (8/9) = 24. Correct.

**Real-world check:**
- **Human hand alone**: ~27 DOF (not counting the arm). The full human body has well over 200 DOF.
- **Real humanoid robots**: ASIMO: 34 DOF. Atlas: 28 DOF. Digit (Agility): 16+ DOF. HUBO: 41 DOF. NAO: 25 DOF (close to 24). Pepper: 20 DOF.
- 24 DOF is within the range of some humanoids but is not a clear standard. The proposed 24-DOF breakdown (6+2+4+6+2+4) omits the head, torso, and hands entirely.
- The human hand has **27 DOF** by standard anatomical counting (5 fingers x 4 DOF + 2 wrist + 5 MCP ab/ad), not 24. The hypothesis claims J_2(6) = 24 = total humanoid DOF, but this is too low for any humanoid that includes hands.

**Grade: WEAK** — 24 is in the range for limb-only DOF counts of simple humanoids, but does not match any clear real-world standard. Real humanoids vary widely (16-41+).

---

## H-ROB-6: 6-DOF Robot Arm = n

**Math check:** n = 6. The SE(3) dimension argument is valid: the group of rigid body motions in 3D has dimension 6 (3 translation + 3 rotation).

**Real-world check:** This is the strongest hypothesis in the document.
- **Universal Robots (UR3/5/10/20)**: 6 DOF. Industry standard.
- **FANUC**: 6-axis arms dominate their product line.
- **ABB**: 6-axis is standard.
- **KUKA**: 6-axis (plus 7-axis LBR iiwa for collaborative).
- 6-DOF is genuinely the overwhelming industry standard for industrial robot arms.

However, the reason is SE(3) kinematics, not "because 6 is a perfect number." The connection between SE(3) having dimension 6 and 6 being a perfect number is a coincidence — SE(3) would have dimension 6 regardless of number theory. The hypothesis conflates a kinematic fact with a number-theoretic property.

**Grade: EXACT** — 6-DOF is indeed the industry standard. The SE(3) reasoning is correct. The "perfect number" overlay is cosmetic but the prediction itself is spot-on.

---

## H-ROB-7: Gait Phases = tau(6) = 4

**Math check:** tau(6) = 4. Correct.

**Real-world check:** Quadruped gaits are typically classified as: walk, trot, pace, canter, gallop (and variants like bound, pronk). That is at least 5 distinct gaits, not 4. In CPG-based controllers, the number of phase offsets varies by gait. The walk-trot-canter-gallop mapping to 4 is selective (omits pace, bound, pronk).

For hexapod tripod gait having 2 phases (lambda(6)=2): this is correct — alternating tripod gait is indeed a 2-phase pattern.

**Grade: CLOSE** — Tripod 2-phase is correct. The quadruped 4-gait claim is an approximation that omits several real gaits.

---

## H-ROB-8: Sensor Fusion = Egyptian Fraction (1/2 + 1/3 + 1/6)

**Math check:** 1/2 + 1/3 + 1/6 = 1. Correct.

**Real-world check:** There is no established industry standard for sensor bandwidth allocation ratios. Different robots allocate bandwidth based on application:
- Autonomous vehicles: vision dominates (often >70%, not 50%)
- Manipulation robots: tactile/force may be higher priority than IMU
- The 50/33/17 split is plausible but completely unverified
- No published robotics paper establishes this as optimal

**Grade: UNVERIFIABLE** — The math is fine but there is no real-world standard to compare against. The allocation is plausible but arbitrary.

---

## H-ROB-9: PWM Resolution = sigma(6) = 12 Bits

**Math check:** sigma(6) = 12. Correct.

**Real-world check:**
- Hobby servos: typically 10-12 bit effective resolution
- Industrial servo drives: commonly 12-16 bit PWM
- Many modern motor controllers use 12-bit ADC/DAC (STM32 series have 12-bit ADC standard)
- 12-bit is indeed very common in practice

The reason is ADC/DAC silicon economics, not number theory. But the match is real.

**Grade: EXACT** — 12-bit PWM/ADC is a genuine industry-standard resolution for motor control.

---

## H-ROB-10: Kinematic Chain Depth = n = 6

**Math check:** dim(SE(3)) = 6. Correct.

**Real-world check:** This is essentially the same claim as H-ROB-6 (6-DOF arm). A standard robot arm has 6 links/joints. This is correct and matches industry practice.

Redundant — same as H-ROB-6.

**Grade: EXACT** — Same as H-ROB-6. 6-link kinematic chains are standard.

---

## H-ROB-11: Swarm Cluster Size = J_2(6) = 24

**Math check:** J_2(6) = 24. Correct.

**Real-world check:** There is no established optimal swarm size of 24 in multi-robot research. Swarm sizes in papers and demonstrations vary enormously:
- Kilobot swarms: 100-1000+
- Drone swarms: 10 to 3000+ (Intel drone shows)
- Warehouse robots (Kiva/Amazon): hundreds per facility
- Research typically tests a range of sizes; no magic number of 24

The 24 = 4 x 6 sub-squad structure is a post-hoc narrative. Swarm scalability is the whole point — optimal cluster size depends on communication range, task type, and environment.

**Grade: WEAK** — No real-world evidence for 24 as optimal swarm cluster size.

---

## H-ROB-12: Swarm Communication = 6-Regular Graph

**Math check:** n = 6. Trivially stated.

**Real-world check:** Swarm communication topologies are typically determined by physical proximity (range-limited broadcast), not fixed-degree graphs. In practice:
- Most swarm protocols use range-based neighbor discovery (variable degree)
- Mesh networks do not impose fixed connectivity
- There is no standard of 6-regular graphs in swarm robotics literature

**Grade: WEAK** — No real-world adoption of 6-regular communication graphs in swarm robotics.

---

## H-ROB-13: Energy Budget = Egyptian Fraction (50% actuation, 33% compute, 17% comms)

**Math check:** 1/2 + 1/3 + 1/6 = 1. Correct.

**Real-world check:**
- Mobile robots: actuation typically 50-80% of power budget (varies greatly by speed/terrain)
- Computation: 5-30% depending on onboard processing
- Communication: typically <5% for WiFi/Bluetooth, more for long-range
- The 50/33/17 split overstates communication and computation for most robots
- Boston Dynamics Spot: the vast majority of power goes to actuation
- A drone with an Nvidia Jetson might approach 33% compute, but that is not typical

**Grade: WEAK** — Actuation at 50% is in the right ballpark for some robots. Computation at 33% and comms at 17% are too high for most real systems.

---

## H-ROB-14: Battery = 3S (sigma/tau = 12/4 = 3)

**Math check:** sigma(6)/tau(6) = 12/4 = 3. Correct.

**Real-world check:**
- Hobby/small robots: 2S (7.4V) and 3S (11.1V) LiPo are both very common
- DJI drones: 3S, 4S, 6S depending on model
- Boston Dynamics Spot: 48V (approximately 13S)
- Unitree Go2: ~24V (approximately 6S-7S)
- TurtleBot: 12V (3S equivalent) — match
- Servo-based robots: often 2S (6V-7.4V)

3S is common for small/hobby robots but is NOT the standard for commercial/industrial robots, which use higher voltages. The claim that 3S is universally optimal is false.

**Grade: CLOSE** — 3S is common in hobby robotics but not dominant across all robot categories. Larger robots use significantly higher voltages.

---

## H-ROB-15: Control Loop Hierarchy = tau(6) = 4 Levels

**Math check:** tau(6) = 4. Correct.

**Real-world check:** Control hierarchies in robotics vary:
- Simple controllers: 2 levels (servo + planning)
- ROS-based systems: typically 3 levels (hardware, motion, behavior)
- Complex systems: 3-5 levels
- The proposed 4-level (servo/motion/planning/strategy) is reasonable but not uniquely standard

The frequency mapping (1kHz / 500Hz / 100Hz / 10Hz) is plausible but the ratios don't follow the divisor structure as claimed (1000:500:100:10 = 100:50:10:1, not {1,2,3,6}).

**Grade: CLOSE** — 4 levels is within the typical range but not a clear standard. The divisor-to-frequency mapping does not hold.

---

## H-ROB-16: PID Gain Ratio = {6:2:1}

**Math check:** Uses divisors {6, 2, 1}. Note: 3 is a divisor of 6 but is skipped.

**Real-world check:** Ziegler-Nichols classic tuning gives Kp:Ki:Kd ratios that vary by system. There is no universal "6:2:1" standard. PID gains are deeply system-dependent (mass, damping, inertia). The claim that this ratio replaces 80% of manual tuning is unverified and implausible — PID tuning depends entirely on plant dynamics.

Also, the divisors of 6 are {1, 2, 3, 6} but the hypothesis uses {6, 2, 1}, arbitrarily dropping 3.

**Grade: WEAK** — The ratio is arbitrary. PID gains are plant-specific and cannot be predetermined by number theory.

---

## H-ROB-17: SLAM Feature Dimensions = n = 6

**Math check:** dim(SE(3)) = 6. Correct.

**Real-world check:** SLAM feature descriptors (SIFT: 128D, ORB: 256-bit, SuperPoint: 256D) operate in high-dimensional spaces for a reason — discriminability. Reducing to 6D would catastrophically degrade matching performance. The state space being 6D does not mean features should be 6D; features represent visual appearance, not robot pose.

This conflates two different things: robot state dimension and feature descriptor dimension.

**Grade: FAIL** — Fundamentally flawed reasoning. Feature descriptor dimensionality and robot state dimensionality serve completely different purposes. 6D descriptors would fail for visual matching.

---

## H-ROB-18: Path Planning = Hex Grid (6-connectivity)

**Math check:** Hexagonal grids have 6-connectivity. Correct.

**Real-world check:** Hex grids are indeed mathematically superior to square grids for isotropic path planning — all neighbor distances are equal, eliminating the sqrt(2) diagonal problem. This is well-known in computational geometry.

However, in practice:
- Virtually all robotics path planning uses square grids (occupancy grids) or continuous representations (RRT, PRM)
- Hex grids are rarely used in real robotics due to sensor data alignment (cameras/LiDAR produce rectangular data)
- Game AI uses hex grids (Civilization series), but robotics does not

**Grade: CLOSE** — The mathematical advantage of hex grids is real, but real-world robotics overwhelmingly uses rectangular grids or sampling-based planners.

---

## H-ROB-19: Grasp Taxonomy = sigma(6) = 12 Categories

**Math check:** sigma(6) = 12. Correct.

**Real-world check:** The Feix/GRASP taxonomy identifies 33 human grasp types. The Cutkosky taxonomy has 16 categories. Reducing to 12 is one possible clustering, but 12 is not an established standard. The proposed 6+3+2+1 = 12 decomposition maps to divisors of 6 only by choosing category sizes to fit.

**Grade: WEAK** — 12 is a plausible but non-standard number of grasp categories. The decomposition into {6,3,2,1} is contrived to match divisors.

---

## H-ROB-20: Force/Position Bandwidth Ratio = phi(6)/n = 1/3

**Math check:** phi(6)/n = 2/6 = 1/3. Correct.

**Real-world check:** In impedance/hybrid force-position control, the force control loop is typically slower than position. Ratios of 1/3 to 1/10 are common depending on the application. The 1/3 ratio is within the reasonable range but is not a specific standard.

**Grade: CLOSE** — 1/3 is within the plausible range but not a validated optimum.

---

## H-ROB-21: RL Policy Network = N6 Architecture

**Math check:** This references the project's own techniques, not an independent mathematical derivation.

**Real-world check:** This is a self-referential hypothesis — it proposes using the project's own techniques for robot RL. No external validation exists. The claimed 2x sample efficiency improvement is unverified.

**Grade: UNVERIFIABLE** — Self-referential; no independent evidence.

---

## H-ROB-22: Sim-to-Real = R(6) = 1

**Math check:** R(6) = (12*2)/(6*4) = 1. Correct.

**Real-world check:** The claim that R=1 means "perfect reversibility" between sim and real is a metaphorical interpretation, not a physical or mathematical one. Sim-to-real transfer depends on physics fidelity, domain randomization design, and system identification — not on number-theoretic ratios. The claim that 12 physics parameters with 2x randomization range is optimal is unverified.

**Grade: WEAK** — The R(6)=1 identity is mathematically correct but the connection to sim-to-real transfer is purely metaphorical.

---

## H-ROB-23: Compliant Actuator Stiffness = Boltzmann (1/e)

**Math check:** 1/e ~ 0.368. The split of 37% stiff / 63% compliant. Mathematically stated correctly.

**Real-world check:** Variable stiffness actuators (VSAs) exist in research (DLR, IIT). The stiffness distribution depends on the task, not a universal constant. There is no published evidence that a 37/63 stiff/compliant split is optimal. Human muscles do modulate stiffness dynamically but not in a fixed 37/63 ratio.

**Grade: UNVERIFIABLE** — Interesting idea but no real-world data to verify against.

---

## H-ROB-24: Modular Robot = Cube (6 faces)

**Math check:** Cube has 6 faces. Correct.

**Real-world check:** This is genuinely the dominant form in modular self-reconfigurable robotics:
- M-TRAN: cube-based
- SMORES: cube-based
- Molecubes: cube-based
- Roombots: hybrid but cube-derived

The reason is practical (orthogonal connection axes, space-filling) rather than number-theoretic, but the match is real.

**Grade: EXACT** — Cubic modules are indeed the standard in modular robotics.

---

## H-ROB-25: Froude Number Transition = 1/n = 1/6 ~ 0.167

**Math check:** 1/6 = 0.1667. Correct.

**Real-world check:** This is the most interesting hypothesis. The walk-trot transition in quadrupeds does occur near Fr ~ 0.25-0.5 according to Alexander (1989) and other biomechanics literature. The often-cited transition is around Fr = 0.5 (walk-to-trot) and Fr = 2.5 (trot-to-gallop).

The hypothesis claims Fr = 0.16-0.17, citing "most mammals." However, the standard biomechanics reference (Alexander 1989, Heglund & Taylor 1988) places the walk-trot transition at **Fr ~ 0.5**, not 0.167.

**Grade: FAIL** — The walk-trot Froude number transition is approximately 0.5 in the biomechanics literature, not 1/6 ~ 0.167. The claimed match to "0.16-0.17" appears to be incorrect.

---

## H-ROB-26: Tactile Array = 12x12 = 144 taxels

**Math check:** sigma(6)^2 = 144. Correct.

**Real-world check:**
- BioTac sensor: ~19 taxels (much less than 144)
- DIGIT (Meta): continuous image (not discrete taxels)
- GelSight: camera-based, resolution varies
- Human fingertip: ~2500 mechanoreceptors (far more than 144)
- Research tactile arrays: vary from 4x4 to 32x32

There is no standard of 12x12. The claim that 12x12 matches human fingertip resolution (1-2mm spacing) requires specific sensor size assumptions.

**Grade: WEAK** — 12x12 is within a plausible range but not a standard. Real tactile sensors vary enormously.

---

## H-ROB-27: Multi-Robot Task Allocation = Egyptian Fraction

**Math check:** 1/2 + 1/3 + 1/6 = 1. Correct.

**Real-world check:** Task allocation in multi-robot systems uses auction-based, market-based, or optimization methods. The specific 50/33/17 split for primary/support/reserve is not an established paradigm. Military doctrine does use reserve forces (~1/3 in reserve is a common guideline, not 1/6), which contradicts the Egyptian fraction prediction.

**Grade: WEAK** — The allocation is one possible scheme but not a validated standard. Military reserve doctrine suggests ~1/3 reserve, not 1/6.

---

## H-ROB-28: Balance Control = mu(6) = 1

**Math check:** mu(6) = mu(2*3) = (-1)^2 = 1. Correct (6 is squarefree, has 2 prime factors).

**Real-world check:**
- A 6-axis IMU (3 accel + 3 gyro) is indeed the minimum sensor for full attitude estimation. This is correct.
- However, real humanoid balance relies on additional sensors: foot force/torque sensors, joint encoders, and sometimes vision. IMU alone is insufficient for robust balance (no contact force information).
- The "squarefree = no redundant sensors" metaphor is poetic but not rigorous.

**Grade: CLOSE** — 6-axis IMU as the minimal inertial sensor is correct, but the claim that IMU alone suffices for humanoid balance is wrong (force sensing is essential).

---

## Summary Scorecard

| ID | Hypothesis | Grade | Notes |
|----|-----------|-------|-------|
| H-ROB-1 | 12 major joints | CLOSE | Selective counting; real humanoids vary 16-41 DOF |
| H-ROB-2 | 4 legs, 6 DOF/leg | FAIL | Industry standard is 3 DOF/leg, not 6 |
| H-ROB-3 | Hexapod optimal | WEAK | Hexapods exist but quadrupeds dominate commercially |
| H-ROB-4 | 5 fingers / 2 jaws | CLOSE | 2-jaw is real; 5-finger is coincidence with human anatomy |
| H-ROB-5 | 24 total DOF | WEAK | Real humanoids range 16-41+; human hand alone is 27 DOF |
| H-ROB-6 | 6-DOF arm | EXACT | UR, FANUC, ABB, KUKA all standardize on 6 axes |
| H-ROB-7 | 4-phase gait | CLOSE | Tripod 2-phase correct; quadruped has 5+ gait types |
| H-ROB-8 | Egyptian sensor fusion | UNVERIFIABLE | No established bandwidth allocation standard |
| H-ROB-9 | 12-bit PWM | EXACT | 12-bit ADC/PWM is genuinely standard in motor control ICs |
| H-ROB-10 | 6-link chain | EXACT | Same as H-ROB-6; redundant hypothesis |
| H-ROB-11 | 24-robot swarm | WEAK | No evidence for 24 as optimal; swarms scale continuously |
| H-ROB-12 | 6-regular graph | WEAK | Not used in real swarm systems |
| H-ROB-13 | Egyptian energy split | WEAK | Actuation is usually 50-80%; comms is usually <5% |
| H-ROB-14 | 3S battery | CLOSE | Common in hobby robots; industrial robots use higher voltages |
| H-ROB-15 | 4-level control | CLOSE | Reasonable but not a unique standard |
| H-ROB-16 | PID {6:2:1} | WEAK | PID gains are entirely plant-specific |
| H-ROB-17 | 6D SLAM features | FAIL | Conflates robot state dim with feature descriptor dim |
| H-ROB-18 | Hex grid planning | CLOSE | Mathematically sound but not used in practice |
| H-ROB-19 | 12 grasp categories | WEAK | Non-standard number; standard taxonomies use 16 or 33 |
| H-ROB-20 | Force BW = 1/3 | CLOSE | Within plausible range but not a validated standard |
| H-ROB-21 | N6 RL policy | UNVERIFIABLE | Self-referential; no external evidence |
| H-ROB-22 | R(6)=1 sim-to-real | WEAK | Metaphorical connection only |
| H-ROB-23 | Boltzmann stiffness | UNVERIFIABLE | No experimental data available |
| H-ROB-24 | Cube module | EXACT | M-TRAN, SMORES, Molecubes all use cubic modules |
| H-ROB-25 | Froude = 1/6 | FAIL | Literature says walk-trot transition at Fr~0.5, not 0.167 |
| H-ROB-26 | 12x12 tactile | WEAK | No standard; real sensors vary 4x4 to camera-based |
| H-ROB-27 | Egyptian task alloc | WEAK | Not an established paradigm |
| H-ROB-28 | Squarefree balance | CLOSE | 6-axis IMU is minimal, but IMU alone is insufficient |

### Aggregate Statistics

| Grade | Count | Percentage |
|-------|-------|-----------|
| EXACT | 4 | 14% |
| CLOSE | 8 | 29% |
| WEAK | 10 | 36% |
| FAIL | 3 | 11% |
| UNVERIFIABLE | 3 | 11% |

### Key Findings

**Strongest hypotheses (EXACT):**
- H-ROB-6/10: 6-DOF robot arm. This is genuinely standard and the SE(3) reasoning is valid.
- H-ROB-9: 12-bit PWM. Real industry standard in motor control silicon.
- H-ROB-24: Cubic modular robots. Real standard in self-reconfigurable robotics.

**Clear failures:**
- H-ROB-2: 6 DOF per quadruped leg is wrong. Every major quadruped (Spot, ANYmal, Unitree) uses 3 DOF/leg.
- H-ROB-17: Reducing SLAM features to 6D confuses state space dimension with descriptor dimension.
- H-ROB-25: Froude number transition is ~0.5 in literature, not 1/6.

**Systemic pattern:** The strongest hypotheses are where n=6 coincides with a genuine physical or engineering constraint (SE(3) dimension, ADC bit depth, cubic geometry). The weakest are where arbitrary arithmetic functions (J_2, sopfr, Egyptian fractions) are mapped to design parameters without physical justification. The n=6 framework works best as a mnemonic device for values that are independently justified, not as a generative design principle.
