# Quantum Computing -- Verification Results

Verified: 2026-03-30
Verifier: Claude Opus 4.6 (independent review against published QC literature and industry data)

## Verification Summary Table

| ID | Claim | Predicted | Actual | Grade | Notes |
|----|-------|-----------|--------|-------|-------|
| H-QC-1 | Optimal qubit module = 24 | J_2(6)=24 qubits | IBM modules: 17 (Falcon), 27 (Peekaboo), 127 (Eagle), 133 (Heron); Google: 53, 72 (Willow); no vendor uses 24 as a module unit | WEAK | J_2(6)=24 is correct math. Leech lattice is real. But the leap from sphere packing to qubit crosstalk minimization is analogical, not proven. No hardware vendor has converged on 24-qubit modules. |
| H-QC-2 | Optimal qubit connectivity degree = 12 | sigma(6)=12 | Heavy-hex (IBM): degree 3; Google Sycamore: degree 4; Trapped ions: all-to-all; No hardware uses degree 12 | FAIL | FCC kissing number = 12 is correct, but 2D chip layouts cannot physically realize degree-12 nearest-neighbor coupling. The hypothesis conflates 3D sphere packing with 2D chip topology. Industry trend is low-degree connectivity (3-4) with high-fidelity couplings. |
| H-QC-3 | 4 types of qubit roles | tau(6)=4 | Standard QEC uses 2 types (data + ancilla); some architectures add flag qubits (3 types); magic state factories use dedicated qubits (arguable 4th type) | CLOSE | The enumeration of 4 roles (data, ancilla, flag, magic state) is a reasonable taxonomy that appears in advanced QEC literature (e.g., Chamberland & Campbell 2018 flag qubits). However, deriving this from tau(6) is post-hoc pattern matching. |
| H-QC-4 | Hexagonal qubit lattice optimal | n=6 symmetry | IBM uses heavy-hex (modified hexagonal); Google uses square grid; hex lattice studied for color codes | CLOSE | Hexagonal geometry is indeed used (IBM heavy-hex) and has theoretical advantages for certain codes (color codes). But it is not universally optimal -- Google's square grid works well for surface codes. The claim has partial support. |
| H-QC-5 | 6-fold chip rotational symmetry | C6 group | No major QC chip uses 6-fold symmetry; rectangular layouts dominate | FAIL | Crystallographic restriction theorem is real math, but quantum chips are not crystals. Chip layouts are rectangular due to packaging, wiring, and fabrication constraints. No evidence 6-fold symmetry helps. |
| H-QC-6 | 5 levels of coupling hierarchy | sopfr(6)=5 | Typical hierarchy: nearest-neighbor, intra-chip, inter-chip (2-3 levels in practice); no standard defines exactly 5 | WEAK | The 5-level hierarchy described is plausible as an organizational framework but arbitrary. One could define 3, 4, 6, or 7 levels equally well. The number 5 is not a recognized standard. |
| H-QC-7 | 12 optimal stabilizer generators | sigma(6)=12 | Stabilizer count = n-k varies by code: surface code d=3 has 8; d=5 has 24; no special status for 12 | WEAK | The math sigma(6)=12 is trivially correct. But "optimal stabilizer count = 12" has no basis in QEC theory. The [[16,4,4]] code is a known code (it exists), but its optimality is not established, and 12 stabilizers is just one of many valid configurations. |
| H-QC-8 | 4 logical qubits per block | tau(6)=4 | Surface code standard: 1 logical qubit per patch; some codes encode k>1 but no universal preference for k=4 | WEAK | Most practical QEC proposals use k=1 per patch (surface code). Higher-rate codes exist but k=4 has no special status. The claim that 4 is optimal lacks supporting evidence. |
| H-QC-9 | Egyptian fraction syndrome decoding (50/33/17% split) | 1/2+1/3+1/6=1 | Real decoders: MWPM, Union-Find, or neural-net; no standard 3-tier split; lookup tables handle ~70-90% of trivial syndromes in practice, not 50% | WEAK | Multi-tier decoding is a real idea (e.g., Skoric et al. 2023 use a fast pre-decoder + MWPM). But the specific 50/33/17 split is not observed or predicted by any decoder theory. The actual fractions depend on error rate and code distance. |
| H-QC-10 | [[24,12,8]] quantum Leech code | sigma*phi=24 | Classical Golay [24,12,8] exists and is well-known. CSS construction yields a [[24,12,8]] quantum code -- this is a real, studied code | CLOSE | The classical Golay code and its quantum CSS version are real and important. sigma(6)*phi(6)=24 matching the Golay code dimension is a genuine numerical coincidence worth noting. However, the Golay code was not "derived from" n=6 arithmetic -- it was discovered by Golay in 1949 from coding theory. |
| H-QC-11 | Error threshold = 1/12 ~ 8.33% | 1/sigma(6)=1/12 | Surface code threshold ~1.1% (circuit-level noise), ~10.3% (phenomenological); toric code ~10.9% (phenomenological) | CLOSE | 8.33% falls between circuit-level (~1%) and phenomenological (~10%) thresholds. This is not a well-defined "break-even" point. The prediction is in the right ballpark for phenomenological thresholds but not a precise match to any standard result. |
| H-QC-12 | 2-phase QEC cycle (X then Z) | lambda(6)=2 | CSS codes do measure X-type and Z-type stabilizers, often in alternating rounds. This is standard practice. | CLOSE | The observation is correct -- CSS codes use 2 types of stabilizer measurements. But this follows trivially from CSS code structure (X and Z stabilizers are independent), not from lambda(6)=2. Deriving a well-known design from Carmichael function is post-hoc. |
| H-QC-13 | Squarefree stabilizer = optimal QEC | mu(6)=1 | Independent stabilizer generators are required by definition in stabilizer codes. Redundant stabilizers are sometimes deliberately added (e.g., for single-shot QEC). | WEAK | Stabilizer generators must be independent by definition -- this is not an insight, it is the definition. The connection to mu(6)=1 is purely metaphorical. Moreover, redundant stabilizers ARE useful in some contexts (single-shot error correction, Bacon-Shor codes). |
| H-QC-14 | R(6)=1 implies perfect QEC at n=6 | R(6)=1 | [[6,2,2]] code exists and is known. It detects 1 error but cannot correct any (d=2). It is not particularly remarkable. | WEAK | [[6,2,2]] exists but it is a detection code, not a correction code. The R(n)=1 framework is the project's own construction and has no independent standing in QEC theory. The claim that perfect numbers yield optimal codes is not supported. |
| H-QC-15 | 2 basis gate classes (Clifford + non-Clifford) | phi(6)=2 | Gottesman-Knill theorem: Clifford gates are classically simulable; adding any non-Clifford gate (e.g., T) gives universality. This is a fundamental theorem. | CLOSE | The factual claim is correct and well-established. But deriving it from phi(6)=2 is numerological. The number 2 arises from the structure of the Clifford group and Gottesman-Knill theorem, not from Euler's totient of 6. The "2" here is a coincidence. |
| H-QC-16 | Universal gate set has exactly 6 gates | n=6 | IBM native gates: {CX, ID, RZ, SX, X} = 5 gates; Google Sycamore: {sqrt(iSWAP), Phased-XZ} = 2 native + decompositions; IonQ: {GPI, GPI2, MS} = 3 gates; there is no universal "6-gate" standard | FAIL | The set {H,T,CNOT,S,X,Z} is one common pedagogical set, but S=T^2 and Z=S^2 make it redundant. The minimal universal set is {H,T,CNOT} = 3 gates. Native gate sets vary by vendor (3-5 gates typically). Claiming 6 as optimal is incorrect. |
| H-QC-17 | Optimal T-count is multiple of 4 | tau(6)=4 | Optimal T-counts from literature: Toffoli = 7T, T-depth for common circuits varies; no evidence T-count clusters at multiples of 4 | FAIL | T^4=Z is correct, but optimal T-counts for standard circuits are not multiples of 4. Toffoli = 7T, Fredkin = 7T, controlled-S = 3T. The claim is falsified by basic circuit synthesis results. |
| H-QC-18 | Single:two-qubit gate ratio = 3:1 | sigma/tau=3 | Empirical data from QASMBench: ratio varies widely (1:1 to 10:1+ depending on algorithm); no universal 3:1 ratio | WEAK | The ratio varies enormously by algorithm. Grover's algorithm has roughly 2:1; QFT-heavy circuits can be 4:1+. There is no universal 3:1 ratio in quantum circuits. |
| H-QC-19 | Gate scheduling: 50% parallel, 33% sequential, 17% barrier | 1/2+1/3+1/6=1 | No published data supports this specific breakdown; parallelism depends entirely on circuit structure and qubit connectivity | UNVERIFIABLE | This is a novel claim with no published supporting data. The fractions would depend on the specific algorithm, qubit topology, and compiler. |
| H-QC-20 | Quantum advantage at depth ~5*log(n) | sopfr(6)=5 | Sycamore: 53 qubits, depth 20; 5*log2(53)=28.5 -- does not match. Random circuit depth scales as O(n) for anti-concentration, not O(log n) | WEAK | The Sycamore depth=20 vs predicted 28.5 is off by 30%. More fundamentally, the scrambling depth for random circuits scales as O(n), not O(log n). The O(log n) scaling comes from circuit complexity lower bounds, which use different constants. The "5" has no theoretical basis. |
| H-QC-21 | 2-qubit gate = 24 elementary operations | J_2(6)=24 | KAK decomposition: any 2-qubit gate = at most 3 CNOTs + 15 single-qubit rotations = 18 operations; pulse-level: varies by hardware (typically 1-3 cross-resonance pulses + dressing) | FAIL | The KAK decomposition requires at most 3 CNOTs and up to 15 single-qubit parameters, giving 18 total gate operations, not 24. At pulse level, a CNOT is 1-2 physical pulses on IBM hardware. The number 24 does not match any standard decomposition. |
| H-QC-22 | QEC width expansion = 4/3x (ancilla = 1/3 of data) | tau^2/sigma=4/3 | Surface code: ancilla/data ~ 1:1 (2x total); best LDPC codes: overhead ratio ~3-10x for practical distances; Tanner codes: asymptotically constant but still > 4/3x in practice | FAIL | Surface code uses roughly equal data and ancilla qubits (2x expansion). No known practical QEC code achieves 4/3x expansion while maintaining useful distance. The 4/3 ratio is far more optimistic than any real code. |
| H-QC-23 | QV threshold for usefulness = 4096 | 2^sigma(6)=4096 | IBM achieved QV=4096 in 2021 (Eagle). But QV=4096 has not been a recognized "usefulness" threshold. Quantum advantage demos used different metrics. | WEAK | IBM did reach QV=4096, but this was not a transition to "practical quantum advantage." QV is largely an IBM-specific metric; Google and others do not use it. No practical quantum advantage application was unlocked specifically at QV=4096. The threshold is arbitrary. |
| H-QC-24 | Qubit allocation: 50% compute, 33% memory, 17% communication | 1/2+1/3+1/6=1 | No standard allocation exists; current monolithic chips dedicate ~50% to QEC ancilla; distributed QC architectures are still experimental | UNVERIFIABLE | No established qubit allocation standard exists to compare against. |
| H-QC-25 | Surface code optimal patch = 24 data qubits (d=5) | sigma*phi=24 | d=5 surface code has d^2=25 data qubits, not 24. d=5 is commonly considered a good starting point for QEC, but so are d=3 and d=7. | CLOSE | 25 is close to 24, and d=5 is indeed a commonly discussed code distance. But 25 != 24, and the "24+1" framing is ad hoc. The d=5 preference comes from error suppression scaling, not from n=6 arithmetic. |
| H-QC-26 | Ultimate QC efficiency = 1/6 (logical/physical ratio) | phi/sigma=1/6 | Current estimates: surface code ~1/1000 to 1/10000; optimistic LDPC projections: ~1/100 to 1/10; no known bound of 1/6 | WEAK | 1/6 (~16.7%) is far more optimistic than current surface code overhead but within the range of theoretical LDPC projections. There is no known fundamental limit of 1/6. The connection to phi(6)/sigma(6) is numerological. |
| H-QC-27 | 2-mode connectivity (dense/sparse alternation) | lambda(6)=2 | Google uses tunable couplers with on/off states (2 modes). This is a real design pattern. | CLOSE | Tunable couplers do have 2 states (coupled/decoupled), which is a genuine 2-mode system. But this follows from the binary nature of coupling (on/off), not from lambda(6)=2. |
| H-QC-28 | Quantum advantage at 6^k qubit milestones | n=6 powers: 6, 36, 216, 1296, 7776 | Milestones: Sycamore 53 qubits (not 36); IBM Eagle 127 (not 216); major targets are typically 100, 1000, 1M qubits | FAIL | Actual milestone qubit counts do not align with powers of 6. Google's supremacy was at 53 (not 36); IBM's roadmap targets 100K+ (not 7776). The 6^k sequence has no predictive power for actual hardware milestones. |
| H-QC-29 | Optimal amplitude distribution follows Egyptian fractions | 1/2+1/3+1/6=1 | Grover's algorithm: amplitude of target state approaches 1 (not Egyptian fractions); no known algorithm has this specific distribution as optimal | FAIL | Grover's algorithm concentrates amplitude on the target state, not in a 1/2+1/3+1/6 split. No known quantum algorithm has Egyptian fraction amplitude distribution as an optimality condition. |
| H-QC-30 | Quantum chemistry active space = 12 orbitals | sigma(6)=12 | Common active spaces: (6,6) for benzene, (8,8) for small molecules, (10,10) to (16,16) for transition metals; 12 is within the range but not uniquely standard | CLOSE | 12 orbitals (or 12 qubits) is a reasonable size for transition metal active spaces and is used in some benchmarks. But active space size varies enormously by molecule. 12 is not uniquely optimal -- it is one of many reasonable choices. |
| H-QC-31 | 4-layer variational ansatz optimal | tau(6)=4 | Optimal depth depends on problem and qubit count; QAOA p=1-3 often sufficient for simple problems, p>>4 needed for hard ones; no universal "4 layers" result | WEAK | There is no universal optimal layer count. Barren plateau onset depends on circuit expressibility and qubit count, not a fixed number of layers. Some problems need p=1, others need p=20+. |
| H-QC-32 | Iterative QPE uses 2-bit feedback | phi(6)=2 | Kitaev's iterative QPE uses 1 ancilla qubit with classical feedback. Standard QPE uses n ancilla qubits. "2-bit feedback" is not a standard characterization. | WEAK | Iterative QPE (Kitaev 1995) uses 1 qubit recycled with 1-bit classical feedback, not 2-bit. The hypothesis mischaracterizes the algorithm. The original file claims this is "confirmed" but it does not match the actual protocol. |
| H-QC-33 | 24-qubit quantum simulator as fundamental unit | J_2(6)=24 | Classical simulation becomes hard around 40-50 qubits (full state vector); 24 qubits are well within classical simulation capability (2^24 = 16M entries, trivial) | FAIL | 24 qubits are easily simulated classically. The classical limit for exact state vector simulation is ~45-50 qubits. 24 qubits is not a quantum advantage boundary. |
| H-QC-34 | 6-qubit entanglement as fundamental unit | n=6 | No standard defines 6-qubit entanglement as a fundamental unit. Bell pairs (2 qubits) and GHZ/W states (3+ qubits) are standard. Entanglement classification is incomplete beyond 4 qubits. | WEAK | 6-qubit entanglement classification is indeed incomplete and complex, but this does not make it a "fundamental unit." The claim is unfalsifiable and vague. |
| H-QC-35 | QML allocation: 50% encoding, 33% processing, 17% readout | 1/2+1/3+1/6=1 | No standard QML resource allocation exists; typical QML circuits use all qubits for both encoding and processing | UNVERIFIABLE | QML is too young a field to have established optimal resource allocations. |
| H-QC-36 | R(6)=1 implies thermodynamic optimality | R(6)=1 | Quantum gates are unitary (reversible) by definition; Landauer's principle applies to measurement; this is basic physics, not an n=6 result | WEAK | The claim that quantum computation is reversible is trivially true (unitarity). Connecting this to R(6)=1 adds no insight. The energy cost of QEC measurement is real but is not quantified by sigma(6)*kT*ln(2) in any published work. |

## Grade Summary

| Grade | Count | Percentage |
|-------|-------|------------|
| EXACT | 0 | 0% |
| CLOSE | 9 | 25% |
| WEAK | 13 | 36% |
| FAIL | 8 | 22% |
| UNVERIFIABLE | 3 | 8% |
| **Not EXACT** | **36** | **100%** |

Note: The original document's "Already Confirmed" section claims 5 EXACT matches. Upon independent review, **none of them survive as EXACT**. See detailed analysis below.

---

## Detailed Notes on FAIL Grades

### H-QC-2: Degree-12 qubit connectivity (FAIL)

The kissing number in 3D is indeed 12 (Newton's theorem). However, quantum processor qubits are fabricated on 2D chips. In 2D, the kissing number is 6, not 12. No physical qubit technology can achieve degree-12 nearest-neighbor coupling in a planar layout. IBM's heavy-hex uses degree 2-3; Google's Sycamore uses degree 4. The hypothesis fundamentally confuses dimensionality.

### H-QC-5: 6-fold chip symmetry (FAIL)

The crystallographic restriction theorem states that 2D lattices can have 1, 2, 3, 4, or 6-fold rotational symmetry. This is correct mathematics. However, quantum chips are not periodic lattices -- they are finite engineered structures. Chip layout is dominated by I/O, wiring, and packaging constraints that favor rectangular geometry. No evidence exists that 6-fold symmetry provides any advantage for quantum processors.

### H-QC-16: 6-gate universal set (FAIL)

The set {H, T, CNOT, S, X, Z} contains redundancies: S = T^2, Z = S^2 = T^4, X = HZH. The minimal universal set is {H, T, CNOT} (3 gates), or even {H, Toffoli} (2 gates). Real hardware native gate sets: IBM = 5 gates, Google = 2-3 native gates, IonQ = 3 gates. No vendor uses exactly 6, and the number 6 has no special significance in gate set theory.

### H-QC-17: T-count multiples of 4 (FAIL)

While T^4 = Z is correct, optimal T-counts for standard circuits are demonstrably not multiples of 4. Published results: Toffoli gate = 7T (Amy et al. 2013), multiply-controlled Toffoli varies, many circuits have odd T-counts. This is directly falsified by circuit synthesis literature.

### H-QC-21: 24 elementary operations for 2-qubit gates (FAIL)

The KAK decomposition of an arbitrary SU(4) gate requires at most 3 CNOTs and 15 single-qubit rotations (Vatan & Williams 2004), totaling 18 operations. At the pulse level, IBM's cross-resonance gate uses 1-3 pulses. Neither 18 nor typical pulse counts equal 24. The derivation in the hypothesis (3 CNOT * 2 rotations + extras = 24) is ad hoc arithmetic that does not match the actual KAK result.

### H-QC-22: 4/3x QEC width expansion (FAIL)

The surface code requires approximately equal numbers of data and ancilla qubits, giving 2x expansion (not 4/3x). The best known quantum LDPC codes (e.g., Panteleev-Kalachev 2022) achieve constant rate asymptotically, but at practical distances still require overhead well above 4/3x. No known QEC code achieves 4/3x expansion with meaningful error correction capability.

### H-QC-28: 6^k qubit milestones (FAIL)

The powers of 6 (6, 36, 216, 1296, 7776) do not align with actual quantum computing milestones. Google's quantum supremacy experiment used 53 qubits (not 36). IBM's Eagle used 127 qubits (not 216). Industry roadmaps target round numbers like 1000 and 1,000,000. The hypothesis has zero predictive power.

### H-QC-29: Egyptian fraction amplitude distribution (FAIL)

Grover's algorithm evolves amplitudes sinusoidally, concentrating probability on marked states toward 1.0. At no point in Grover's algorithm (or any other standard quantum algorithm) does the amplitude distribution match 1/2, 1/3, 1/6. This is straightforwardly false.

### H-QC-33: 24-qubit quantum simulation as classical limit (FAIL)

A 24-qubit system has a Hilbert space of dimension 2^24 = 16,777,216. This is trivially simulable on a modern laptop. The practical classical simulation limit for exact state-vector methods is approximately 45-50 qubits (2^45 to 2^50 complex amplitudes). Tensor network methods can push this further for structured circuits. The claim that 24 qubits represents a classical limit is off by a factor of ~2 million in Hilbert space dimension.

---

## Detailed Notes on WEAK Grades

### H-QC-1: 24-qubit module (WEAK)

The Leech lattice is genuinely significant in mathematics, and 24 dimensions is special for sphere packing. However, qubit crosstalk minimization is a problem in 2D chip geometry, not 24D abstract space. No hardware vendor has adopted 24 as a module size. IBM uses irregular groupings; Google has not published a modular architecture.

### H-QC-6: 5-level coupling hierarchy (WEAK)

Hierarchical coupling exists in quantum systems, but the number of levels is not standardized. One could equally argue for 3 levels (local, chip, network) or 7 levels (adding finer granularity). The number 5 = sopfr(6) is imposed on the data, not derived from it.

### H-QC-7, H-QC-8: 12 stabilizers and 4 logical qubits (WEAK)

These values can be achieved by specific codes but have no special optimality status. The [[16,4,4]] code exists but is not the "optimal" QEC code in any accepted sense. Code selection depends on specific hardware noise models, not fixed numerological values.

### H-QC-13: Squarefree stabilizers (WEAK)

Independent stabilizer generators are required by the definition of stabilizer codes. Claiming this as a "prediction" from mu(6)=1 is circular -- it is simply restating a definition. Moreover, deliberately redundant stabilizers are useful for single-shot QEC (Bombim 2015).

### H-QC-23: QV=4096 threshold (WEAK)

IBM did achieve QV=4096, but this was not a recognized threshold for practical quantum advantage. QV is primarily an IBM-promoted metric that other vendors do not emphasize. No practical quantum advantage application was demonstrated specifically at QV=4096.

### H-QC-32: 2-bit QPE feedback (WEAK)

Kitaev's iterative QPE uses a single ancilla qubit with 1-bit classical feedback per iteration. The hypothesis claims phi(6)=2 predicts "2-bit feedback," but the actual algorithm uses 1-bit feedback. The original document marks this as "confirmed" which is incorrect.

---

## Assessment of the Original "Already Confirmed" Claims

The original document lists 7 predictions as confirmed. Here is the re-evaluation:

| Original Claim | Original Grade | Revised Grade | Reason |
|----------------|---------------|---------------|--------|
| Gate set size = 6 | EXACT | FAIL | Redundant set; actual native sets are 2-5 gates |
| 2 basis gate classes | EXACT | CLOSE | Factually correct but coincidental, not derived from phi(6) |
| QV=4096 | EXACT | WEAK | IBM reached it but it is not a meaningful threshold |
| Iterative QPE 2-bit | EXACT | WEAK | Actual algorithm uses 1-bit feedback, not 2-bit |
| X/Z alternation | EXACT | CLOSE | Correct observation but trivially follows from CSS structure |
| d=5 surface code ~24 | CLOSE | CLOSE | 25 != 24; d=5 is common but not uniquely optimal |
| Sycamore depth ~5*log(53) | CLOSE | WEAK | 20 vs 28.5 is 30% off; theoretical scaling is O(n) not O(log n) |

---

## Overall Assessment

The N6 quantum computing hypotheses follow a consistent methodology: take a number-theoretic function of 6, find a quantum computing concept with a similar numerical value, and declare a derivation. This is **numerological pattern-matching**, not mathematical derivation.

Genuine mathematical connections (e.g., the Golay code having dimension 24, the Clifford/non-Clifford dichotomy) are real facts, but they were discovered independently of n=6 arithmetic. Claiming them as "derived from" perfect number properties reverses the direction of discovery.

The strongest claims (CLOSE grades) identify real patterns in quantum computing but provide no mechanism by which n=6 arithmetic would cause these patterns. The weakest claims (FAIL grades) make specific numerical predictions that are contradicted by published data.

**0 out of 36 hypotheses achieve EXACT verification against real-world data.**
