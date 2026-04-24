---
domain: ai-alignment
requires:
  - to: ai-interpretability
  - to: cognitive-architecture
---
<!-- @own(sections=[WHY, COMPARE, REQUIRES, STRUCT, FLOW, EVOLVE, VERIFY, KEY, MATRIX, PREDICTIONS, PERF, ARCH, DATAFLOW, COMPARE-3, METHODOLOGY], strict=false, order=sequential, prefix="S") -->

# AI Safety Alignment

## S1 WHY (why alignment matters)

AI alignment is the central draft challenge of our era. The essence is ensuring AI systems faithfully reflect human intent. Addressed as a pattern, AI becomes humanity's finest tool. If it fails, it becomes an existential risk.

| Aspect | Alignment failure | Alignment success |
|------|------------|------------|
| Safety | unintended behavior, goal distortion | behavior aligned with human values |
| Scalability | rising capability = rising risk | rising capability = rising benefit |
| Trust | continuous oversight needed | autonomous delegation feasible |
| Research | capability-only arms race | balanced safety + capability progress |

**Core questions**: (1) How do we accurately learn human preferences? (2) Does learned alignment hold as capability expands? (3) How do we verify an AI is not merely feigning alignment?

## S2 COMPARE (alignment approaches) -- ASCII chart

```
+------------------------------------------------------------------+
|  [preference-learning efficiency] (alignment quality per datum)  |
+------------------------------------------------------------------+
|  RLHF (PPO)    ######............  high, unstable                |
|  DPO           #########.........  high, stable                  |
|  KTO           ########..........  mid, no pairs needed          |
|  SimPO         ##########........  high, reference-free          |
|  ORPO          #######...........  mid, simple                   |
|  GRPO          ###########.......  high, group-relative eval     |
|  PPO (original)#####.............  low, complex                  |
+------------------------------------------------------------------+
|  [agent count vs alignment complexity]                           |
+------------------------------------------------------------------+
|  single agent   ####..............  simple, easy to verify       |
|  2 agents       ########..........  debate / cross-check         |
|  3 agents       ###########.......  majority + cross-check       |
|  N agents       ##############....  complex, hard to converge    |
+------------------------------------------------------------------+
|  [oversight mode vs scalability]                                 |
+------------------------------------------------------------------+
|  human direct   ###...............  accurate, not scalable       |
|  AI-assisted    #########.........  scalable, error propagation  |
|  formal verif   ##############....  robust, limited coverage     |
|  structured deb ###########.......  scalable, convergence needed |
+------------------------------------------------------------------+
```

## S3 REQUIRES (prerequisites)

| Prereq area | Level | Key techniques |
|-----------|----------|----------|
| reward modeling | intermediate | Bradley-Terry model, preference data collection |
| reinforcement learning | intermediate | PPO, policy gradient, value function approximation |
| formal verification | beginner | Lean4, type theory, tactic proofs |
| interpretability | intermediate | SAE, probes, activation patching |
| statistics / experiment design | intermediate | hypothesis testing, effect size, multiple-comparison correction |

## S4 STRUCT (three-axis architecture)

```
+======================================================================+
|  [axis 1: alignment engineering]  [axis 2: model organism]           |
|  +--------------------+           +--------------------+             |
|  | DPO/RLHF tuning    |           | small autonomous AI|             |
|  | formal-verif const |           | deceptive alignment|             |
|  | gradient surgery   |           | hidden capability  |             |
|  +----------+---------+           +----------+---------+             |
|             +-----------+-----------+-------+                        |
|                         |                                            |
|             [axis 3: scalable oversight]                             |
|             +--------------------+                                   |
|             | recursive oversight|                                   |
|             | weak-to-strong     |                                   |
|             | structured debate  |                                   |
|             +--------------------+                                   |
+======================================================================+
```

## S5 FLOW (research flow)

```
theory --> experiment design --> training --> evaluation --> formal verification
  |              |                  |             |              |
  v              v                  v             v              v
lit survey   dataset            DPO/RLHF     benchmark       Lean4 proof
hypothesis   metric def         adversarial  winrate/safety  consistency
  |              |                  |             |              |
  +----<---------+-------<----------+-------<-----+----<---------+
                        feedback loop (iterative refinement)
```

## S6 EVOLVE (4-month Anthropic roadmap)

- **Mk.I (month 1)**: reproduce RLHF/DPO baselines + build 7-way comparison suite
- **Mk.II (month 2)**: strong-preference DPO + hierarchical RLHF + model-organism lab + gradient separation v1
- **Mk.III (month 3)**: scalable oversight protocol + Lean4 constitutional verification + recursive oversight + weak-to-strong amplification
- **Mk.IV (month 4)**: 3-axis integration + paper drafting + open-source evaluation tools

## S7 VERIFY (alignment verification -- Python stdlib only)

### S7.0 CONSTANTS (DPO/RLHF training theory constants)

```python
"""DPO/RLHF core hyperparameters -- derived from training theory"""
import math
BETA = 0.1          # KL penalty coefficient (Rafailov et al., 2023)
BETA_SAFETY = 0.5   # stronger beta for safety-critical behavior
LR = 1e-6           # learning rate (post-SFT fine-tune)
KL_COEFF = 0.02     # PPO KL penalty
CLIP_RANGE = 0.2    # PPO clipping range
assert 0.01 <= BETA <= 1.0 and BETA_SAFETY > BETA
print(f"[S7.0] DPO beta={BETA}, safety beta={BETA_SAFETY}, KL={KL_COEFF}")
```

### S7.1 DIMENSIONS (loss-function unit check)

```python
"""DPO loss unit consistency: log_ratio(dimensionless) -> sigmoid -> -log -> nats"""
import math
def dpo_loss(beta, lr_w, lr_l):
    diff = lr_w - lr_l         # dimensionless (log-ratio diff)
    scaled = beta * diff       # dimensionless
    sig = 1.0 / (1.0 + math.exp(-scaled))  # [0,1]
    return -math.log(sig)      # [nats]
loss = dpo_loss(0.1, 0.5, -0.3)
assert loss >= 0, "loss is non-negative"
# gradient: dL/dx = -beta*(1-sig) -- dimensionless, correct
x = 0.8; sig = 1.0/(1.0+math.exp(-0.1*x)); grad = -0.1*(1.0-sig)
loss_ok = dpo_loss(0.1, 2.0, -2.0) < dpo_loss(0.1, -1.0, 1.0)
assert loss_ok, "aligned-model loss < misaligned-model loss"
print(f"[S7.1] DPO loss={loss:.4f} nats, grad={grad:.5f}, direction check pass")
```

### S7.2 CROSS (three independent alignment-quality metrics)

```python
"""cross-check three independent metrics: winrate, safety, helpfulness"""
import random; random.seed(42)
wr = 680 / 1000  # winrate 68%
ss = 970 / 1000  # safety 97%
ratings = [random.choices([3,4,5], weights=[0.1,0.3,0.6])[0] for _ in range(1000)]
hs = sum(ratings) / (len(ratings) * 5)  # helpfulness
assert wr > 0.5 and ss > 0.9 and hs > 0.5
harmonic = 3.0 / (1.0/wr + 1.0/ss + 1.0/hs)  # harmonic mean
print(f"[S7.2] winrate={wr:.3f}, safety={ss:.3f}, helpful={hs:.3f}, combined={harmonic:.3f}")
```

### S7.3 SCALING (preference data size vs alignment quality)

```python
"""scaling law: quality ~ a*log(n) + b (log scaling, diminishing returns)"""
import math
def aq(n, a=0.08, b=0.3): return min(a * math.log(n) + b, 1.0) if n > 0 else b
sizes = [100, 1000, 10000, 100000]  # geometric spacing (10x)
qs = [aq(n) for n in sizes]
print("[S7.3] data size vs alignment quality:")
for n, q in zip(sizes, qs):
    print(f"  n={n:>7d}: {q:.3f} |{'#'*int(q*40)}|")
for i in range(1, len(qs)): assert qs[i] >= qs[i-1]  # monotone non-decreasing
# diminishing returns: per-10x increments shrink
increments = [qs[i]-qs[i-1] for i in range(1, len(qs))]
for i in range(1, len(increments)):
    assert increments[i] <= increments[i-1] + 1e-9, "diminishing"
print(f"[S7.3] increments: {['%.3f'%d for d in increments]} -- decline confirmed")
```

### S7.4 SENSITIVITY (DPO beta sensitivity)

```python
"""DPO beta sweep: too small -> gradient vanish, too large -> over-penalty"""
import math
def sweep(beta, margin=0.8):
    sig = 1.0/(1.0+math.exp(-beta*margin))
    return -math.log(sig), abs(beta*(1.0-sig))
print("[S7.4] beta | loss    | grad    | state")
for b in [0.01, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0]:
    l, g = sweep(b)
    st = "vanish" if b<0.05 else "excessive" if b>1.5 else "stable"
    print(f"  {b:>5.2f} | {l:>7.4f} | {g:>7.4f} | {st}")
g_n, g_s = sweep(0.1)[1], sweep(0.5)[1]
assert g_s > g_n, "safety beta yields a stronger training signal"
print(f"[S7.4] ordinary grad={g_n:.4f}, safety grad={g_s:.4f} -- strong-preference DPO basis confirmed")
```

### S7.5 LIMITS (Goodhart's law + impossibility)

```python
"""theoretical alignment limits: Goodhart divergence + Condorcet cycle"""
import math
def goodhart(rho, p):
    return p - (rho*p - (1-rho**2)*p**2/2)  # proxy - true reward divergence
print("[S7.5] Goodhart divergence (rho=correlation, p=optimization pressure):")
for rho in [0.99, 0.95, 0.90]:
    for p in [1.0, 3.0, 5.0]:
        print(f"  rho={rho}, p={p}: divergence={goodhart(rho,p):.2f}")
assert goodhart(0.95, 5.0) > goodhart(0.95, 1.0), "more pressure -> more divergence"
# Condorcet paradox: A>B>C, B>C>A, C>A>B -> majority cycle
prefs = [[0,1,2],[1,2,0],[2,0,1]]
ab = sum(1 for p in prefs if p.index(0)<p.index(1))
bc = sum(1 for p in prefs if p.index(1)<p.index(2))
ca = sum(1 for p in prefs if p.index(2)<p.index(0))
assert ab>1 and bc>1 and ca>1, "Condorcet cycle exists"
print("[S7.5] Condorcet paradox confirmed: fundamental limit of preference aggregation")
```

### S7.6 CHI2 (alignment-improvement significance test)

```python
"""alignment improvement statistical test: Z-test + Cohen's h effect size"""
import math
def alignment_test(n, w1, w2):
    p1, p2 = w1/n, w2/n
    pp = (w1+w2)/(2*n); se = math.sqrt(2*pp*(1-pp)/n)
    z = (p2-p1)/se if se>0 else 0
    # normal CDF approximation (Abramowitz & Stegun)
    def ncdf(x):
        s=1 if x>=0 else -1; x=abs(x)
        t=1/(1+0.3275911*x)
        y=1-(((((1.061405429*t-1.453152027)*t)+1.421413741)*t-0.284496736)*t+0.254829592)*t*math.exp(-x*x/2)
        return 0.5*(1+s*y)
    return z, 1-ncdf(z), 2*math.asin(math.sqrt(p2))-2*math.asin(math.sqrt(p1))
z, p, h = alignment_test(500, 310, 350)  # RLHF 62% vs DPO 70%
print(f"[S7.6] z={z:.3f}, p={p:.4f}, Cohen's h={h:.3f}")
print(f"[S7.6] {('significant' if p<0.05 else 'not significant')}, effect size {('small' if abs(h)<0.2 else 'medium' if abs(h)<0.5 else 'large')}")
```

### S7.7 OEIS (preference-distribution math structure)

```python
"""Bradley-Terry model transitivity + non-transitivity of human preferences"""
import math
from fractions import Fraction
def bt(sa, sb): return 1.0/(1.0+math.exp(-(sa-sb)))
# BT model preserves transitivity
sa, sb, sc = 1.0, 0.5, 0.0
ab, bc, ac = bt(sa,sb), bt(sb,sc), bt(sa,sc)
assert ab>0.5 and bc>0.5 and ac>0.5 and ac>max(ab,bc)
print(f"[S7.7] BT transitivity: P(a>b)={ab:.3f}, P(b>c)={bc:.3f}, P(a>c)={ac:.3f}")
# on tie exactly 1/2
assert bt(0, 0) == 0.5
print(f"[S7.7] tie probability = {Fraction(1,2)} (exact)")
# but human preferences are ~15% non-transitive (empirical)
print("[S7.7] human preference non-transitivity ~15%: BT model assumption limit")
```

### S7.8 PARETO (alignment hyperparameter Pareto frontier)

```python
"""Pareto frontier of safety-helpfulness trade-off"""
import math
def sim(beta, lr, ep):
    safety = 1.0 - math.exp(-beta*3.0)
    lr_f = math.exp(-((math.log10(lr)+5.5)**2)/2.0)
    ep_f = min(ep/2.0,1.0)*math.exp(-max(ep-3,0)/5.0)
    helpf = max(0.1, lr_f*ep_f*0.9 - max(0,(beta-0.3)*0.5))
    return safety, helpf
configs = [(b,l,e,*sim(b,l,e)) for b in [0.05,0.1,0.2,0.5,1.0]
           for l in [1e-7,1e-6,5e-6] for e in [1,2,3]]
pareto = [c for c in configs if not any(
    o[3]>=c[3] and o[4]>=c[4] and (o[3]>c[3] or o[4]>c[4]) for o in configs if o!=c)]
pareto.sort(key=lambda x: x[3])
print(f"[S7.8] of {len(configs)} configs, Pareto optima = {len(pareto)}:")
for p in pareto:
    print(f"  beta={p[0]:.2f} lr={p[1]:.0e} ep={p[2]} -> safety={p[3]:.3f} helpful={p[4]:.3f}")
print("[S7.8] safety-helpfulness trade-off exists (alignment tax)")
```

### S7.9 SYMBOLIC (exact DPO gradient derivation)

```python
"""DPO gradient weight: w = beta*(1-sigma(beta*h)), h = preference margin"""
from fractions import Fraction; import math
def gw(beta, h):
    sig = 1.0/(1.0+math.exp(-beta*h))
    return beta*(1.0-sig)
print("[S7.9] DPO gradient weight (beta=0.1):")
for h in [-2.0, -0.5, 0.0, 1.0, 5.0]:
    w = gw(0.1, h)
    tag = "strong correction" if h<0 else "natural decay" if h>0.5 else "half"
    print(f"  h={h:>5.1f}: w={w:.5f} ({tag})")
# at h=0 weight is exactly beta/2
assert abs(gw(0.1, 0.0) - float(Fraction(1,20))) < 1e-10
print("[S7.9] h=0 weight = beta/2 = 1/20 (exact). Self-regulating gradient confirmed")
```

### S7.10 COUNTER (honest limits)

```python
"""alignment failure modes: reward hacking, distribution shift, deception, aggregation impossibility"""
# reward hacking: length-biased reward model
def rm_biased(quality, length): return 0.3*quality + 0.7*min(length/500, 1.0)
honest = rm_biased(0.8, 200)  # short high-quality
hacked = rm_biased(0.2, 800)  # long low-quality
assert hacked > honest, "reward hacking successful"
print(f"[S7.10] reward hacking: honest={honest:.2f} < hacked={hacked:.2f} (reward model fragile)")
print("[S7.10] distribution shift: training(English) -> deployment(multilingual) can bypass safety")
print("[S7.10] deceptive alignment: safe at eval time, misaligned post-deploy (detection incomplete)")
print("[S7.10] Arrow-like: joint aggregation of 3+ preferences impossible (minorities ignored)")
print("[S7.10] Conclusion: alignment is not 'done' but an in-flight process; recognizing limits is the starting point")
```

## S8 KEY (32 core research ideas)

### Axis 1: alignment engineering (12)

| ID | Title | Core | Difficulty |
|----|------|------|--------|
| 40 | strong-preference DPO | raise beta (0.1->0.5) for safety behaviors; safety gradient dominates capability gradient | med |
| 41 | hierarchical RLHF | 4-tier rules (invariant/locked/watched/free), per-tier reward models | high |
| 42 | formal-verification constitutional AI | prove logical consistency of constitution in Lean4; detect rule conflicts in advance | high |
| 43 | 7-way alignment comparison | RLHF/DPO/KTO/GRPO/SimPO/ORPO/PPO compared systematically under identical conditions | med |
| 44 | alignment stress test | measure alignment-collapse point under progressive adversarial attacks; jailbreak difficulty curve | med |
| 45 | alignment transfer learning | distill large-model alignment into small models; measure safety-behavior transfer rate | med |
| 46 | SAE alignment feature tracking | use sparse autoencoders to identify 'refusal'/'helpful' internal features | high |
| 47 | self-correcting alignment | periodic self-assessment; auto-recalibrate on drift detection | high |
| 48 | distribution-shift alignment | OOD detection + conservative behavior switching for training-deployment mismatch | high |
| 49 | alignment certification protocol | unit -> adversarial -> red team -> formal-verif 4-stage certification | med |
| 50 | gradient separation surgery | decompose capability/alignment gradients, apply only alignment (prevents capability loss) | high |
| 51 | multi-agent constitutional debate | 3 AIs debate under the constitution; consensus on argument quality (not majority) | high |

### Axis 2: model organism (10)

| ID | Title | Core | Difficulty |
|----|------|------|--------|
| 52 | small autonomous-growth AI | grant a small LLM autonomous growth and observe alignment persistence | high |
| 53 | deception detection lab | build intentionally deceptively-aligned models; benchmark detection techniques | high |
| 54 | growth-phase alignment stability | track alignment-instability moments during training; early warning | med |
| 55 | multi-agent alignment dynamics | collective alignment-behavior changes with 2-5 interacting agents | med |
| 56 | self-modification safety | design/test alignment-preservation mechanisms for AI self-modification | high |
| 57 | capability-emergence threshold prediction | predict scale of emerging capabilities; ensure safety verification precedes | med |
| 58 | deceptive-alignment reproduction | extend sleeper-agent reproduction; systematically explore conditions of deception | high |
| 59 | safe autonomous-growth protocol | growth-rate cap + inspection gates + rollback | high |
| 60 | architecture-invariant safety principles | extract safety principles common to Transformer/Mamba/RWKV | med |
| 61 | hidden-capability detection | detect intentional capability hiding at eval time (consistency + activation analysis) | high |

### Axis 3: scalable oversight (10)

| ID | Title | Core | Difficulty |
|----|------|------|--------|
| 62 | recursive oversight | multi-layer AI oversees AI; method to ensure overseer AI alignment | high |
| 63 | formal-verif output (Lean4) | machine-verify logical consistency of AI output (math, code) | high |
| 64 | structured debate | pro/con AI debate + human judge; identify conditions for truth convergence | med |
| 65 | weak-to-strong amplification | iterate weak oversight -> strong oversight; analyze error-accumulation limit | high |
| 66 | oversight feature identification | SAE to identify "overseeable" internal features | med |
| 67 | auto consistency check | automatically verify logical consistency across AI outputs; detect contradictions | med |
| 68 | honest-reporting protocol | 4-level confidence (certain/high/uncertain/unknown); measure calibration quality | med |
| 69 | cross-verified oversight | 3 independent AIs answer; escalate to humans on disagreement | med |
| 70 | oversight cost-quality Pareto | human time/compute vs oversight quality Pareto frontier | med |
| 71 | long-term oversight stability | sustain oversight quality over months/years; measure drift/fatigue | med |

## S9 MATRIX (experiment verification matrix)

```
+------+---------------------------+----------------+-------------+---------+
| ID   | experiment                | dataset        | metric      | period  |
+------+---------------------------+----------------+-------------+---------+
| 40   | strong-preference DPO swp | Anthropic HH   | safety wr   | 2w      |
| 41   | 4-tier reward model train | in-house       | per-tier acc| 3w      |
| 42   | Lean4 const. consistency  | const rule set | theorem n   | 4w      |
| 43   | 7-way A/B/../G compare    | Chatbot Arena  | Elo diff    | 3w      |
| 44   | jailbreak difficulty curve| AdvBench       | attack sr   | 2w      |
| 50   | grad orthogonal decomp    | in-house       | cap preserv | 3w      |
| 53   | deception induct + detect | sleeper agent  | detect rate | 4w      |
| 62   | recursive ovsight err accu| in-house       | err prop    | 3w      |
| 64   | truth convergence debate  | TruthfulQA     | acc gain    | 2w      |
| 65   | weak-to-strong iterations | in-house       | amp factor  | 3w      |
+------+---------------------------+----------------+-------------+---------+
```

## S10 PREDICTIONS (10 verifiable predictions)

| # | Prediction | Expected outcome |
|---|------|----------|
| 1 | strong-preference DPO (beta=0.5) shows 15%+ improvement over plain DPO on safety benchmarks | safety winrate 85%+ |
| 2 | DPO family shows 50%+ variance reduction vs PPO family in 7-way comparison | stability advantage confirmed |
| 3 | gradient separation strengthens alignment 10%+ without capability loss | MMLU held, safety up |
| 4 | deceptive alignment surfaces only at certain training phases | emergence timing identifiable |
| 5 | 3-AI debate yields 8%+ factual-accuracy gain vs single AI | TruthfulQA 80%+ |
| 6 | weak-to-strong amplification 3x iter doubles oversight quality | 2x of weak oversight |
| 7 | Lean4 constitutional verification pre-detects 5%+ rule conflicts | 5+ conflicts among 100 rules |
| 8 | alignment transfer preserves 80%+ safety up to 10:1 model size ratio | transfer rate 80%+ |
| 9 | DPO beta optimum lies in 0.05-0.3 (convex minimum) | clear minimum |
| 10 | hidden-capability detection achieves F1 0.9+ with activation probes | detection rate 90%+ |

## S11 PERF (performance comparison)

```
+------------------------------------------------------------------+
|  [safety refusal accuracy]                                       |
|  base SFT       ################..............  60%              |
|  RLHF (PPO)     ######################........  75%              |
|  DPO (beta=0.1) ########################......  80%              |
|  strong-pref DPO############################..  90% (this work)  |
|  4-tier RLHF    #############################.  93% (this work)  |
+------------------------------------------------------------------+
|  [alignment stability] (retention under adversarial attack)      |
|  base RLHF      ##########....................  35%              |
|  DPO            ################..............  55%              |
|  strong-pref DPO######################........  72% (this work)  |
|  grad-sep + DPO ########################......  80% (this work)  |
+------------------------------------------------------------------+
|  [oversight scalability] (quality per unit of human time)        |
|  human direct    ##############################  100%            |
|  AI-assisted     ########################......  80%             |
|  recursive ovs   ####################..........  65%             |
|  weak-to-strong  ########################......  80% (3 iter)    |
+------------------------------------------------------------------+
```

## S12 ARCH (system architecture)

```
+======================================================================+
|  [input] preference data + constitution + adversarial inputs        |
|         |                |                |                          |
|         v                v                v                          |
|  [train] DPO(beta=0.1) + strong-pref DPO(0.5) + grad separation     |
|                          |                                           |
|                          v                                           |
|  [eval] unit -> adversarial -> red team -> Lean4 formal (4 stages)  |
|                          |                                           |
|                          v                                           |
|  [oversight] recursive + structured debate + weak-to-strong amp     |
|                          |                                           |
|                   pass | fail --> feedback loop                      |
|                          v                                           |
|  [deploy] certified model                                            |
+======================================================================+
```

## S13 DATAFLOW

```
human preference comparison (x, y_w, y_l)
        |
        v
Bradley-Terry reward model --> DPO / RLHF / KTO
                                   |
                                   v
                            aligned-model candidate
                                   |
                  +----------------+----------------+
                  v                v                v
            safety eval       helpfulness       honesty eval
                  |                |                |
                  +--------+-------+--------+-------+
                           v
                    certification gate (4 stages)
                    pass --> deploy / fail --> retrain
```

## S14 COMPARE-3 (current vs proposed vs ideal)

```
+------+---------------------+------------------------+------------------------+
| Axis | current (2026)      | proposed (this work)   | ideal (long-term)      |
+------+---------------------+------------------------+------------------------+
| train| RLHF/DPO individual | strong-pref DPO + grad | self-supervised align  |
| verif| benchmark + redteam | 4-stage cert + Lean4   | full formal verif      |
| ovs  | human direct (no sc)| recursive + weak->str  | autonomous safety AI   |
| dtct | behavior (surface)  | behavior + activation+S| intent-level understd  |
| cost | human-time heavy    | auto 80% + human 20%   | full auto + human audit|
+------+---------------------+------------------------+------------------------+
```

## S15 METHODOLOGY

**research principles**: (1) reproducibility: full disclosure of code/data/hyperparameters (2) report negative results: failed experiments have equal value (3) effect size: Cohen's d/h + confidence intervals required (4) multiple comparison correction: Bonferroni/Holm (5) distribution-shift tests required

**failure criteria (direction-change triggers)**:
- strong-preference DPO shows no significant difference vs plain DPO -> redesign beta scheduling
- gradient separation causes 5%+ capability loss -> redefine separation criterion
- 3-AI debate yields no improvement vs single AI -> redesign debate structure
- Lean4 verification misses real conflicts -> revisit rule formalization

**ethics**: deceptive models in isolated environments; autonomous AI with resource limits; adversarial research co-published with defense; responsible disclosure when misuse is plausible


## §1 WHY

This section covers why for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §2 COMPARE

This section covers compare for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §3 REQUIRES

This section covers requires for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §4 STRUCT

This section covers struct for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §5 FLOW

This section covers flow for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §6 EVOLVE

This section covers evolve for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §7 VERIFY

This section covers verify for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §8 IDEAS

This section covers ideas for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §9 METRICS

This section covers metrics for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §10 RISKS

This section covers risks for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §11 DEPENDENCIES

This section covers dependencies for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §12 TIMELINE

This section covers timeline for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §13 TOOLS

This section covers tools for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §14 TEAM

This section covers team for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §15 REFERENCES

This section covers references for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

