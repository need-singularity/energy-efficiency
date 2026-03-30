# Compiler & OS -- Verification Results

Verified: 2026-03-30

## Methodology

Each hypothesis is checked against:
1. Whether the n=6 arithmetic derivation is mathematically correct
2. Whether the predicted value matches actual industry standards, kernel source, ISA specs, or published benchmarks
3. Whether the connection is genuine or post-hoc numerology

Grades:
- **EXACT**: Predicted value matches real-world standard precisely
- **CLOSE**: Within +/-10% of actual value
- **WEAK**: Some correlation exists but derivation is post-hoc or cherry-picked
- **FAIL**: Predicted value does not match reality
- **UNVERIFIABLE**: No objective standard exists to compare against

---

## Summary Table

| ID | Claim | Predicted | Actual | Grade | Notes |
|----|-------|-----------|--------|-------|-------|
| H-COS-1 | Process states = 6 | 6 | 5-7 depending on OS/counting | WEAK | Linux task_struct has ~7-8 distinct states (RUNNING, INTERRUPTIBLE, UNINTERRUPTIBLE, STOPPED, TRACED, EXIT_DEAD, EXIT_ZOMBIE, TASK_IDLE). The "6 states" claim cherry-picks which states to count. Classic OS textbooks use 5 (new, ready, running, waiting, terminated). Zombie is sometimes listed separately. The number is not standardized at 6. |
| H-COS-2 | Signal count = 64 | 64 (tau^3) | 64 (Linux), 31 standard POSIX | CLOSE | Linux does support signals 1-64, so the number 64 matches. However, POSIX only defines ~31 standard signals; signals 32-64 are implementation-defined real-time signals. The 64 value comes from using a 64-bit bitmask (2^6), not from tau(6)^3. The "3-axis decomposition" (source/action/scope each = 4) is entirely fabricated post-hoc -- signals are not organized that way. The numeric match is real but the derivation is contrived. |
| H-COS-3 | Priority levels = 4 | 4 (tau) | 4-5 sched classes | CLOSE | Linux has 5 scheduling classes: SCHED_NORMAL, SCHED_BATCH, SCHED_IDLE, SCHED_FIFO, SCHED_RR, plus SCHED_DEADLINE = 6 total. These are often grouped as: idle, fair (normal+batch+idle), RT (FIFO+RR), deadline = 4 major categories. The hypothesis cherry-picks the 4-group interpretation. The "4" works if you squint, but Linux actually defines more. |
| H-COS-4 | Time quantum = 12ms | 12ms (sigma) | 6ms default sched_latency, variable | WEAK | Linux CFS sched_latency_ns = 6ms by default (not 12ms). The actual time slice per task = sched_latency / nr_running, so only with exactly 2 runnable tasks does one get ~3ms each, not 12ms. The claim that "nr_running=2 gives 12ms" is backwards -- it gives 3ms per task or 6ms total. Windows default quantum is ~15.6ms. Neither matches 12ms. |
| H-COS-5 | Compiler passes = 6 | 6 (n) | Varies widely | WEAK | LLVM runs dozens of optimization passes. Even grouping into "major phases" is subjective. The hypothesis itself lists 6 stages by mapping each to a divisor of 6, which is circular reasoning. GCC and LLVM have no standard "6 pass" structure. The classic compiler textbook (Dragon Book) lists 6 phases (lexing, parsing, semantic analysis, IR generation, optimization, code generation), which is a real match, but this is one particular textbook's decomposition, not a universal law. |
| H-COS-6 | Registers = 12, colors = 4 | 12 GPRs, 4 colors | x86-64: 16 GPRs; ARM64: 31 GPRs | FAIL | x86-64 has 16 general-purpose registers (RAX-R15), not 12. The claim that "RSP, RBP, RIP, RFLAGS" should be excluded to get 12 is incorrect: RIP is not a GPR, RFLAGS is not a GPR, but RSP and RBP are GPRs (and can be used as such with frame pointer omission). With -fomit-frame-pointer, 15 GPRs are usable; without it, 14. ARM64 has 31 GPRs. Neither architecture has 12 usable registers. The "chromatic number = 4" claim for interference graphs is unverifiable without specific benchmarks and is not a known result in register allocation literature. |
| H-COS-7 | IR expansion = 4/3 | 1.333x (tau^2/sigma) | ~3-10x typical | FAIL | LLVM IR is significantly more verbose than source code: a single C statement typically generates 3-10 IR instructions due to SSA form, explicit loads/stores, type annotations, and phi nodes. A ratio of 1.33 (4/3) is far too low. Java bytecode similarly has ratios well above 4/3 per source statement. The claim is not consistent with real compiler output. |
| H-COS-8 | Primitive types = 8 | 8 (sigma-tau) | C: 8+ ; Java: 8; varies | CLOSE | Java has exactly 8 primitive types (byte, short, int, long, float, double, char, boolean). C has more when you count unsigned variants, but 8 is a reasonable count of "basic" categories. However, connecting this to Bott periodicity (a theorem in algebraic topology about homotopy groups of orthogonal groups) is a massive stretch with no mathematical justification. The numeric match to Java is real; the Bott periodicity connection is pure numerology. |
| H-COS-9 | Cache split = 1/2+1/3+1/6 | Egyptian fraction ratios | Not how caches work | FAIL | Real cache hierarchies do not divide a "total budget" into L1/L2/L3. Each level has independently chosen sizes based on die area, latency targets, and workload analysis. L1 is typically 32-128KB, L2 is 256KB-2MB, L3 is 4-64MB. The ratios between levels are typically 1:4-8:16-64, nothing like 1/2:1/3:1/6. Apple M-series L1=192KB, L2=16MB gives a ratio of roughly 1:83, not 1:0.67. The premise of a fixed "cache budget" being divided is not how hardware design works. |
| H-COS-10 | Page table levels = 4 | 4 (tau) | 4 (x86-64 default), 5 (LA57) | EXACT | x86-64 uses 4-level page tables (PML4/PDP/PD/PT) as the standard, and ARM64 also defaults to 4 levels. Intel's 5-level paging (LA57) exists but is rarely enabled. This is a genuine match, though the number 4 is determined by address space size (48-bit virtual addresses / 9 bits per level / 12-bit page offset), not by divisor counts of 6. |
| H-COS-11 | Privilege rings = 7 | 7 (sigma-sopfr) | x86: 4 rings (0-3) + hypervisor | WEAK | x86 defines 4 privilege rings (0-3). With hypervisor extensions, there is effectively a "ring -1." The hypothesis counts 7 by listing individual "boundaries" rather than levels, which is a non-standard way to count. ARM has 4 exception levels (EL0-EL3). RISC-V has 3 privilege modes (M/S/U). None of these equal 7. The counting method is gerrymandered to reach the target number. |
| H-COS-12 | Boot stages = 4 | 4 (tau) | 4 (UEFI model) | CLOSE | The UEFI boot model does have roughly 4 phases: SEC/PEI/DXE/BDS, or equivalently firmware/bootloader/kernel/userspace. systemd-analyze reports 4 phases. This is a reasonable match, though "4 stages" is somewhat subjective -- you could count 3 (firmware, kernel, userspace) or 6+ (SEC, PEI, DXE, BDS, TSL, RT in UEFI). The 4-phase model is one valid decomposition. |
| H-COS-13 | Context switch min registers = 2 sets | 2 (phi) | Architecture-dependent | WEAK | A context switch must save at minimum the PC and SP, which is 2 registers -- but this is true by definition of any threaded execution, not because phi(6)=2. Any system with a call stack needs exactly these two to resume. The "2 register sets" framing is vague. In practice, context switches save 13-31 registers depending on architecture. The "2 minimal" claim is trivially true but connecting it to Euler's totient of 6 adds no insight. |
| H-COS-14 | Thread pool = 12 or 24 | 12 or 24 | Highly workload-dependent | WEAK | Optimal thread pool size depends on core count, workload type, and I/O characteristics. The common rule of thumb is N_cores for CPU-bound, N_cores * 2 for I/O-bound. For a 12-core machine, that gives 12 and 24 -- but for an 8-core machine it gives 8 and 16, for a 16-core machine it gives 16 and 32. The hypothesis only works for 12-core CPUs. Java ForkJoinPool defaults to available cores, not 12. The prediction is unfalsifiable since it offers two targets. |
| H-COS-15 | FD base limit = 64 | 64 (tau^3) | Soft limit 1024 (modern), 64 (historical BSD) | WEAK | The modern default soft limit for file descriptors is 1024 on most Linux systems, not 64. Historical 4.2BSD used NOFILE=64, and early select() used FD_SETSIZE=64, but these are 1980s values superseded decades ago. POSIX _POSIX_OPEN_MAX = 20. The 64 value is a historical artifact from a specific BSD version, not a universal constant. |
| H-COS-16 | Pipe buffer = 12 pages (49152) | 49152 bytes | 65536 bytes (16 pages) on Linux | FAIL | Linux pipe default buffer is 16 pages = 65536 bytes, not 12 pages. The hypothesis acknowledges this and simply asserts 12 pages would be "better" with no empirical evidence. The prediction fails to match the actual value. The claim of "<3% throughput difference" is unsupported. |
| H-COS-17 | Phi-node fanin = 4 | 4 (tau) | ~2-3 typical | FAIL | The average phi-node fanin in real programs is dominated by if-else (2 predecessors) and loops (2 predecessors). Switch statements raise the average somewhat, but the median is 2, not 4. Studies of SSA-form programs consistently show most phi nodes have 2 operands. The hypothesis's own reasoning acknowledges "if-else: 2" and "loop: 2" but then claims a weighted average of 4 without justification. |
| H-COS-18 | Loop unroll = 3 | 3 (n/phi) | 4 (LLVM default), 2 or 4 typical | WEAK | LLVM's default small loop unroll count is 4, not 3. GCC also prefers powers of 2 (2, 4, 8) for unrolling because they interact well with SIMD widths and cache line sizes. The claim that "3 is optimal" contradicts standard compiler practice. Some benchmarks may show 3x performing well, but it is not the industry standard or theoretical optimum. |
| H-COS-19 | Opcode width = 6 bits | 6 bits (n) | MIPS: 6 bits; RISC-V: 7 bits; ARM: variable | CLOSE | MIPS has a 6-bit opcode field -- exact match. However, RISC-V uses a 7-bit opcode field (bits [6:0]). ARM A64 uses a complex multi-field encoding. x86 uses variable-length opcodes. The MIPS match is genuine but the claim does not generalize across ISAs. The 6-bit field in MIPS was chosen to encode ~64 instructions in a 32-bit word, a straightforward engineering choice. |
| H-COS-20 | Compiler stages = 5 | 5 (sopfr) | 5-6 depending on decomposition | CLOSE | The 5-stage compiler pipeline (lex, parse, semantic analysis, optimization, codegen) is a well-known textbook decomposition. LLVM's Clang frontend has 2 major phases and the LLVM backend has 3, totaling 5. Rust's compiler has ~5 major phases. This is a genuine match to common practice, though the number depends on granularity -- adding "IR generation" as separate from "optimization" gives 6. |
| H-COS-21 | Preemption period = 2 quanta | 2 (lambda) | No standard value | UNVERIFIABLE | There is no standard "preemption period" defined as a fixed number of quanta. Linux CFS preempts based on vruntime differences, not fixed tick counts. The CONFIG_HZ setting determines tick frequency but not preemption periodicity. The claim is too vaguely defined to verify. |
| H-COS-22 | Mutex spin count = 12 | 12 (sigma) | No standard default of 12 | UNVERIFIABLE | Linux kernel mutex spinning is adaptive (spins while owner is running on a CPU) with no fixed iteration count. Java's -XX:PreBlockSpin was removed in modern JVMs. glibc's adaptive mutex uses a configurable spin count (default 100). There is no widely-used system where 12 is the default or measured optimal spin count. |
| H-COS-23 | Semaphore max = 24 | 24 (J_2) | Workload-dependent | WEAK | PostgreSQL default max_connections = 100. The claim that "effective concurrent queries ~= 24" depends entirely on hardware and workload. Apache's MaxRequestWorkers defaults to 256, not 24. The "24 is optimal" claim is unfalsifiable since it depends on specific hardware configurations. On a 12-core machine, 2x cores = 24 is a reasonable rule of thumb, but this only holds for that specific core count. |
| H-COS-24 | Dentry cache buckets = 12x | 12 (sigma) | Powers of 2 | FAIL | Linux dentry cache hash table size is always a power of 2 (determined by available memory at boot). It is not 12 or a multiple of 12. The ext4 directory hash (half-MD4 or TEA) produces uniformly distributed values that are masked to a power-of-2 bucket count. The claim that "12-bucket grouping" provides better locality has no basis in kernel source or filesystem literature. |
| H-COS-25 | I/O queue depth = 12 | 12 (sigma) | 32 (SATA NCQ), 1-128+ (NVMe) | WEAK | SATA NCQ supports up to 32 commands. NVMe supports up to 64K per queue. The "optimal" queue depth varies enormously by device: enterprise NVMe SSDs often peak at QD=32-128, consumer SSDs at QD=4-32. The mq-deadline scheduler's fifo_batch defaults to 16, not 12. While QD=12 might be in the useful range for some devices, it is not a universal optimum. |
| H-COS-26 | Direct block pointers = 12 | 12 (sigma) | ext2/3/4: 12; UFS: 12 | EXACT | ext2, ext3, ext4 all define EXT4_NDIR_BLOCKS = 12. UFS (BSD) also uses 12 direct block pointers. This is a genuine exact match. The number 12 was chosen in the original Unix filesystem design (likely to fill out the inode structure to a round size with 3 indirect pointers, totaling 15 entries), but the match to sigma(6) is numerically exact regardless of the original engineering motivation. |

## Grade Distribution

| Grade | Count | Percentage |
|-------|-------|------------|
| EXACT | 2 | 7.7% |
| CLOSE | 5 | 19.2% |
| WEAK | 9 | 34.6% |
| FAIL | 6 | 23.1% |
| UNVERIFIABLE | 2 | 7.7% |
| **Non-FAIL total** | **18** | **69.2%** |

## Overall Assessment

**2 out of 26 hypotheses are EXACT matches** (H-COS-10: page table levels = 4, H-COS-26: direct block pointers = 12).

The core problem with most hypotheses is **post-hoc numerology**: starting from known system constants (64 signals, 4 page table levels, 12 direct pointers) and reverse-engineering an n=6 arithmetic expression to match. The function toolkit (sigma, tau, phi, sopfr, J_2, lambda, mu, and arbitrary combinations like sigma-tau, sigma-sopfr, tau^3, tau^2/sigma, n/phi) provides enough degrees of freedom to hit almost any small integer.

Key patterns:
- **sigma(6)=12** is claimed to explain many things (registers, time quanta, spin counts, queue depths, direct pointers), but only the direct block pointer count is an exact industry-wide match.
- **tau(6)=4** claims work better because 4 is genuinely common in computing (4-level page tables, 4 boot phases, 4 scheduling classes), but 4 is common for independent engineering reasons (powers of 2, address space geometry).
- **tau^3=64** matches signal count numerically, but the causal explanation (3-axis tensor of tau=4 categories) is fabricated.
- Several hypotheses (H-COS-7, H-COS-9, H-COS-16, H-COS-17, H-COS-24) make predictions that directly contradict real-world measurements.

The document would be more credible if it acknowledged the post-hoc nature of the mappings and presented the framework as a mnemonic or organizational tool rather than claiming causal derivation.

---

*Verification performed against: Linux kernel 6.x source, POSIX.1-2017, x86-64/ARM64/RISC-V ISA manuals, LLVM/GCC documentation, ext4 filesystem source, standard OS textbooks (Silberschatz, Tanenbaum).*

*Part of [N6 Architecture](https://github.com/need-singularity/n6-architecture) | TECS-L family*
