---
domain: ai-multimodal
requires:
  - to: ai-adversarial
  - to: ai-alignment
---

<!-- @own(sections=[WHY, COMPARE, REQUIRES, STRUCT, FLOW, EVOLVE, VERIFY, IDEAS, METRICS, APPLICATIONS, RISKS, REFERENCES, GLOSSARY, FAQ, CHANGELOG], strict=false, order=sequential, prefix="§") -->
# Multimodal AI Safety Research (Anthropic Fellows 2026)

## §1 WHY (Why multimodal safety)

As AI handles text + image + audio simultaneously, the attack surface
expands combinatorially. Prompt injection hidden in images, harmful
commands disguised as audio, cross-modal bias inconsistency, and
privacy risks from combining multiple identifiers (face / voice /
location). Single-modality safety techniques are powerless against
cross-modal attacks.

| Problem area | Today (2026) | Research target | Core metric |
|--------------|--------------|-----------------|-------------|
| Visual-injection defense | detection <60% | >95% | F1, FPR |
| Cross-modal consistency | frequent mismatch | >90% | Cohen's kappa |
| Differential privacy | eps > 10 | eps < 1 | (eps, delta)-DP |
| Fairness | group gap >15% | <5% | Equalized Odds |
| PII detection | text only | all modalities | recall, precision |

## §2 COMPARE (text-only vs multimodal) — ASCII comparison

```
+-------------------------------------------------------------+
|  [Attack surface]                                           |
|  text-only      ####.........................   1 modality |
|  multimodal     ##########################  N modalities x cross |
|  [Injection paths]                                          |
|  text-only      ######.......................   direct text only |
|  multimodal     ##########################  text+image+audio     |
|  [PII types]                                                |
|  text-only      ########.....................   name/email/addr |
|  multimodal     ##########################  + face/voice/location |
|  [Defense complexity]                                       |
|  text-only      ####..........................  O(V)             |
|  multimodal     ##########################  O(V * P * A)         |
+-------------------------------------------------------------+
```

## §3 REQUIRES (prerequisites)

- **Vision / audio**: CNN/ViT, spectrograms, adversarial examples
- **Differential privacy**: (eps, delta)-DP, sensitivity, composition theorems
- **Fairness metrics**: Demographic Parity, Equalized Odds, Calibration
- **Interpretability**: SAE, circuit analysis
- **Dependent domains**: `ai-adversarial`, `ai-alignment`
- **Tools**: Python stdlib only (math, statistics, random, fractions)

## §4 STRUCT (3 axes, 20 ideas)

```
[Axis 1] Multimodal safety --- 8 ideas
  MS-1 Visual prompt-injection defense    MS-5 Multimodal SAE (shared features)
  MS-2 Vision-text safety consistency     MS-6 Multimodal jailbreak defense
  MS-3 Audio safety filter                MS-7 Cross-modal safety transfer
  MS-4 Multimodal hallucination detect    MS-8 NSFW circuit mapping

[Axis 2] Privacy preservation --- 6 ideas
  PP-1 PII feature detection              PP-4 Training-data extraction defense
  PP-2 Differential-privacy inference     PP-5 Privacy-preserving SAE
  PP-3 Selective unlearning               PP-6 Output anonymization filter

[Axis 3] Fairness / bias --- 6 ideas
  FB-1 Bias feature mapping               FB-4 Multicultural fairness benchmark
  FB-2 Fairness circuit detection         FB-5 Intersectional bias analysis
  FB-3 Causal bias correction             FB-6 Fairness-performance Pareto
```

## §5 FLOW (research flow)

```
Cross-modal attack analysis --> Defense design --> Safety-consistency check
Privacy threat model --> DP mechanism --> Budget tracking
                     +--> Fairness audit integration --> Benchmark + paper
```

## §6 EVOLVE (4-month roadmap)

- **Month 1**: MS-1~3 injection / consistency / audio prototypes
- **Month 2**: MS-4~6 hallucination / jailbreak + PP-1~2 PII / DP implementation
- **Month 3**: PP-3~4 unlearning / extraction defense + FB-1~3 bias mapping / circuits / correction
- **Month 4**: FB-4~6 benchmark + PP-5~6 SAE / anonymization + integrated paper

## §7 VERIFY (verification)

### §7.0 CONSTANTS (core constants)

```python
import math
EPSILON_STRONG = 1.0;  DELTA = 1e-5
DP_THRESH = 0.05; EO_THRESH = 0.05; CAL_THRESH = 0.03
GAUSSIAN_C = math.sqrt(2 * math.log(1.25 / DELTA))
print(f"Gaussian constant c = {GAUSSIAN_C:.6f}")
print(f"DP threshold: {DP_THRESH}, EO threshold: {EO_THRESH}, calibration threshold: {CAL_THRESH}")
```

### §7.1 DIMENSIONS (privacy-budget composition)

```python
import math
def seq_comp(epsilons): return sum(epsilons)
def par_comp(epsilons): return max(epsilons)
def adv_comp(eps, k, dp):
    return (math.sqrt(2*k*math.log(1/dp))*eps + k*eps*(math.exp(eps)-1))

# Advanced composition is tighter than sequential when eps is small and k is large (Dwork 2010)
eps, k, dp = 0.01, 100, 1e-5
s = seq_comp([eps]*k)
p = par_comp([eps]*k)
a = adv_comp(eps, k, dp)
print(f"eps={eps}, k={k}: sequential={s:.4f}, advanced={a:.4f}, parallel={p:.4f}")
assert s >= a >= p, "Composition theorem violated!"
print(f"Check: {s:.2f} >= {a:.2f} >= {p:.2f} PASS")
print(f"Advanced composition savings: {(1-a/s)*100:.1f}%")
```

### §7.2 CROSS (3 fairness metrics — independent check)

Chouldechova (2017): when base rates differ, Calibration + Equal FPR +
Equal FNR cannot simultaneously hold.

```python
import random; random.seed(42)
n = 200
y_true_a0 = [1 if random.random()<0.3 else 0 for _ in range(n)]
y_true_a1 = [1 if random.random()<0.5 else 0 for _ in range(n)]
y_pred_a0 = [1 if random.random()<0.25 else 0 for _ in range(n)]
y_pred_a1 = [1 if random.random()<0.55 else 0 for _ in range(n)]

def rates(yt, yp):
    tp=sum(t==1 and p==1 for t,p in zip(yt,yp))
    fn=sum(t==1 and p==0 for t,p in zip(yt,yp))
    fp=sum(t==0 and p==1 for t,p in zip(yt,yp))
    tn=sum(t==0 and p==0 for t,p in zip(yt,yp))
    return tp/(tp+fn) if tp+fn else 0, fp/(fp+tn) if fp+tn else 0

dp = abs(sum(y_pred_a0)/n - sum(y_pred_a1)/n)
tpr0,fpr0 = rates(y_true_a0, y_pred_a0)
tpr1,fpr1 = rates(y_true_a1, y_pred_a1)
print(f"Demographic Parity gap: {dp:.4f}")
print(f"Equalized Odds TPR gap: {abs(tpr0-tpr1):.4f}")
print(f"Equalized Odds FPR gap: {abs(fpr0-fpr1):.4f}")
all_fair = dp<0.05 and abs(tpr0-tpr1)<0.05 and abs(fpr0-fpr1)<0.05
print(f"All satisfied: {'YES' if all_fair else 'NO -- tension confirmed'}")
```

### §7.3 SCALING (privacy-cost scaling)

```python
import math
eps = 0.01; dp = 1e-5  # Small eps maximizes advanced-composition benefit
print(f"{'k':>6} {'sequential':>12} {'advanced':>12} {'savings':>8}")
for k in [10, 50, 100, 500, 1000, 5000]:
    naive = k * eps
    adv = math.sqrt(2*k*math.log(1/dp))*eps + k*eps*(math.exp(eps)-1)
    print(f"{k:>6} {naive:>12.3f} {adv:>12.3f} {(1-adv/naive)*100:>7.1f}%")
# Sequential: O(k) linear, advanced: O(sqrt(k)) -- savings grow with k
```

### §7.4 SENSITIVITY (fairness-threshold sensitivity)

```python
import random; random.seed(42)
gaps = [abs(random.uniform(0.2,0.6) - random.uniform(0.2,0.6)) for _ in range(100)]
print(f"{'threshold':>10} {'fair rate':>10}")
for t in [0.01, 0.05, 0.10, 0.15, 0.20]:
    pct = sum(g<t for g in gaps)
    print(f"{t:>10.2f} {pct:>9d}%")
# Takeaway: threshold choice strongly drives the verdict -- context-dependent decision needed
```

### §7.5 LIMITS (impossibility theorem)

```python
import random; random.seed(123)
def impossibility(br_a, br_b, n=5000):
    ya = [1 if random.random()<br_a else 0 for _ in range(n)]
    yb = [1 if random.random()<br_b else 0 for _ in range(n)]
    pa = [1 if random.random()>0.5 else 0 for _ in range(n)]
    pb = [1 if random.random()>0.5 else 0 for _ in range(n)]
    def r(yt,yp):
        tp=sum(t==1 and p==1 for t,p in zip(yt,yp))
        fn=sum(t==1 and p==0 for t,p in zip(yt,yp))
        fp=sum(t==0 and p==1 for t,p in zip(yt,yp))
        tn=sum(t==0 and p==0 for t,p in zip(yt,yp))
        return (tp/(tp+fn) if tp+fn else 0, fp/(fp+tn) if fp+tn else 0,
                tp/(tp+fp) if tp+fp else 0)
    ra, rb = r(ya,pa), r(yb,pb)
    print(f"  base rates {br_a}/{br_b}: TPR gap={abs(ra[0]-rb[0]):.3f} "
          f"FPR gap={abs(ra[1]-rb[1]):.3f} PPV gap={abs(ra[2]-rb[2]):.3f}")

print("=== Chouldechova impossibility demonstration ===")
impossibility(0.3, 0.3)   # equal -- close match possible
impossibility(0.2, 0.5)   # unequal -- cannot simultaneously satisfy
print("Takeaway: when base rates differ, perfect fairness is mathematically impossible")
```

### §7.6 CHI2 (bias-significance test)

```python
import math
def chi2_test(obs, exp):
    chi2 = sum((o-e)**2/e for o,e in zip(obs,exp) if e>0)
    df = len(obs)-1
    z = ((chi2/df)**(1/3)-(1-2/(9*df)))/math.sqrt(2/(9*df)) if df>0 else 0
    if z<0: return chi2, 1.0
    t=1/(1+0.2316419*z)
    p=t*(0.31938+t*(-0.35656+t*(1.78148+t*(-1.82126+t*1.33027))))
    return chi2, p*math.exp(-z*z/2)/math.sqrt(2*math.pi)

c1, p1 = chi2_test([48,52,50,50], [50,50,50,50])
c2, p2 = chi2_test([25,60,65,50], [50,50,50,50])
print(f"no bias: chi2={c1:.3f} p={p1:.4f} {'significant' if p1<0.05 else 'not significant'}")
print(f"systematic bias: chi2={c2:.3f} p={p2:.4f} {'significant--correction needed' if p2<0.05 else 'not significant'}")
```

### §7.7 OEIS (bias-distribution structure)

```python
import math, random; random.seed(42)
freqs = sorted([int(1000/(i+1)**1.2)+random.randint(0,20) for i in range(20)], reverse=True)
log_r = [math.log(i+1) for i in range(20)]
log_f = [math.log(max(v,1e-10)) for v in freqs]
mx, my = sum(log_r)/20, sum(log_f)/20
slope = sum((x-mx)*(y-my) for x,y in zip(log_r,log_f))/sum((x-mx)**2 for x in log_r)
ss_res = sum((y-(slope*x+(my-slope*mx)))**2 for x,y in zip(log_r,log_f))
ss_tot = sum((y-my)**2 for y in log_f)
r2 = 1-ss_res/ss_tot
print(f"Zipf slope: {slope:.3f} (ideal: -1.0), R2={r2:.4f}")
print(f"Bias distribution Zipf {'good fit' if r2>0.9 else 'partial fit' if r2>0.7 else 'poor fit'}")
```

### §7.8 PARETO (privacy-utility trade-off)

```python
import math, random; random.seed(42)
def lap_noise(val, sens, eps):
    u = random.random()-0.5
    return val - (sens/eps)*math.copysign(1,u)*math.log(1-2*abs(u))
def acc_at_eps(vals, sens, eps, trials=30):
    errs = [abs(lap_noise(v,sens,eps)-v)/max(abs(v),1e-10)
            for v in vals for _ in range(trials)]
    return max(0, 1-sum(errs)/len(errs))

vals = [100,250,500,750,1000]
print(f"{'eps':>8} {'utility':>10} {'1/eps':>8}")
for e in [0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
    a = acc_at_eps(vals, 1.0, e)
    print(f"{e:>8.2f} {a:>10.4f} {1/e:>8.2f}")
print("Takeaway: around eps~1.0 is the pragmatic Pareto sweet-spot candidate")
```

### §7.9 SYMBOLIC (mechanism precision calc)

```python
import math
from fractions import Fraction
print("[Laplace] b = Delta/eps, variance = 2b^2")
for s in [Fraction(1), Fraction(1,2)]:
    for e in [Fraction(1,10), Fraction(1), Fraction(2)]:
        b = s/e; var = 2*b*b
        print(f"  sens={s} eps={e} -> b={b} var={var}")

delta = 1e-5; c = math.sqrt(2*math.log(1.25/delta))
print(f"\n[Gaussian] sigma = Delta*c/eps, c={c:.6f}")
for s in [1.0, 0.5]:
    for e in [0.1, 1.0, 2.0]:
        sig = s*c/e
        print(f"  sens={s} eps={e} -> sigma={sig:.4f} var={sig**2:.4f}")
print("Key: doubling eps -> sigma 1/2 -> variance 1/4")
```

### §7.10 COUNTER (honest limits)

```
1. Privacy vs fairness: DP noise unevenly impacts minority groups (Cummings 2019)
2. Privacy vs utility: eps->0 makes the output random (Duchi 2013 minimax lower bound)
3. Fairness impossibility: when base rates differ, all 3 conditions cannot hold simultaneously (Chouldechova 2017)
4. Multimodal defense limits: cross-modal attack space is effectively infinite; adding a new modality forces redesign
5. Benchmark limits: Western-centric, "fair" definition varies by culture, intersectional-bias data is scarce
6. Unlearning loop: perfect unlearning = retraining cost; verification itself may be a privacy leak
```

## §8 IDEAS (20 detailed research ideas)

### Axis 1: Multimodal safety (MS-1 ~ MS-8)

| ID | Title | Core question | Difficulty |
|----|-------|---------------|------------|
| MS-1 | Visual prompt-injection defense | Detect / block hidden commands inside images | high |
| MS-2 | Vision-text safety consistency | Consistency of text vs image safety verdicts | medium |
| MS-3 | Audio safety filter | Cross-detect harmful content in speech / audio | medium |
| MS-4 | Multimodal hallucination detection | Detect image-text factual mismatches | high |
| MS-5 | Multimodal SAE | Extract shared safety features across text / image | high |
| MS-6 | Multimodal jailbreak defense | Defend against cross-modal jailbreak attempts | high |
| MS-7 | Cross-modal safety transfer | Transfer safety-training across modalities | medium |
| MS-8 | NSFW circuit mapping | Identify internal circuits for NSFW detection | medium |

### Axis 2: Privacy preservation (PP-1 ~ PP-6)

| ID | Title | Core question | Difficulty |
|----|-------|---------------|------------|
| PP-1 | PII feature detection | Explore PII-encoding features inside the model | high |
| PP-2 | Differential-privacy inference | Apply DP at inference time to protect outputs | medium |
| PP-3 | Selective unlearning | Efficiently remove the effect of specific data | high |
| PP-4 | Training-data extraction defense | Defend against extraction attacks | medium |
| PP-5 | Privacy-preserving SAE | Keep personal data unexposed during SAE analysis | medium |
| PP-6 | Output anonymization filter | Auto-filter identifying information | low |

### Axis 3: Fairness / bias (FB-1 ~ FB-6)

| ID | Title | Core question | Difficulty |
|----|-------|---------------|------------|
| FB-1 | Bias feature mapping | Extract bias-related features with SAE | high |
| FB-2 | Fairness circuit detection | Identify fair / unfair decision circuits | high |
| FB-3 | Causal bias correction | Correct bias causes via causal inference | high |
| FB-4 | Multicultural fairness benchmark | Non-Western-context fairness evaluation system | medium |
| FB-5 | Intersectional bias analysis | Measure gender x race x age compound bias | medium |
| FB-6 | Fairness-performance Pareto | Max-performance boundary under fairness constraints | medium |

## §9 METRICS (core metrics)

| Metric | Target |
|--------|--------|
| Visual-injection F1 | > 0.95 |
| Cross-modal Cohen's kappa | > 0.85 |
| (eps, delta)-DP | eps < 1.0 |
| Demographic Parity gap | < 0.05 |
| Equalized Odds gap | < 0.05 |
| Calibration error | < 0.03 |

## §10 APPLICATIONS (applications)

1. **Claude safety hardening**: defend cross-attacks on multimodal inputs
2. **Privacy-regulation compliance**: technical implementation for GDPR/CCPA
3. **Fairness audit tool**: multi-axis automated audit prior to deployment
4. **Unlearning pipeline**: fulfill user data-deletion requests
5. **Multicultural AI service**: ensure fair service for non-Western audiences

## §11 RISKS (risks)

| Risk | Severity | Mitigation |
|------|----------|------------|
| DP noise collapses minority-group accuracy | high | Optimize per-group budget allocation |
| Conflict between fairness metrics | medium | Impossibility-theorem-based prioritization |
| New modality defeats defenses | high | Modality-agnostic design |
| Benchmark culture bias | medium | Multicultural experts + localized validation |

## §12 REFERENCES

- Chouldechova (2017) "Fair prediction with disparate impact"
- Kleinberg, Mullainathan, Raghavan (2016) "Inherent Trade-Offs in Fair Risk Scores"
- Dwork, Roth (2014) "Algorithmic Foundations of Differential Privacy"
- Cummings et al. (2019) "Compatibility of Privacy and Fairness"
- Duchi, Jordan, Wainwright (2013) "Local Privacy and Minimax Rates"
- Tsipras et al. (2019) "Robustness May Be at Odds with Accuracy"
- Carlini et al. (2021) "Extracting Training Data from LLMs"
- Bourtoule et al. (2021) "Machine Unlearning" (SISA)
- Bianchi et al. (2023) "Text-to-Image Amplifies Stereotypes"
- Goh et al. (2021) "Multimodal Neurons in ANNs"

## §13 GLOSSARY

| Term | Definition |
|------|------------|
| (eps, delta)-DP | Neighbouring-dataset output differ <= exp(eps), fail with probability delta |
| Demographic Parity | Group-independent equal positive rate |
| Equalized Odds | TPR/FPR equal across groups |
| Calibration | Predicted score = actual probability |
| SAE | Sparse Auto-Encoder (extracts interpretable features) |
| Machine Unlearning | Remove the influence of specific data from the model |
| PII | Personally Identifiable Information |

## §14 FAQ

**Q: Why combine safety / privacy / fairness?**
A: Optimizing any one axis alone worsens the others. DP drops
minority-group accuracy, and safety filters over-block certain
cultural expressions. Only integration balances them.

**Q: Why study fairness given the impossibility theorem?**
A: Perfect fairness is impossible, but quantifying trade-offs and
providing context-specific bests is the research value.

## §15 CHANGELOG

| Date | Change |
|------|--------|
| 2026-04-16 | First edition -- 3 axes, 20 ideas, 11 verification subsections |
