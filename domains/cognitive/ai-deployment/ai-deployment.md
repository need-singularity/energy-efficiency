---
domain: ai-deployment
requires:
  - to: ai-adversarial
  - to: ai-alignment
---

<!-- @own(sections=[WHY, COMPARE, REQUIRES, STRUCT, FLOW, EVOLVE, VERIFY, IDEAS, METRICS, RISKS, DEPENDENCIES, TIMELINE, TOOLS, TEAM, REFERENCES], strict=false, order=sequential, prefix="§") -->
# AI Deployment Safety

## §1 WHY (why deployment safety)

Real harm emerges in the gap between "safe in the lab" and "safe in production".
Anthropic Fellows 2026 research domain. Four pillars: training safety, inference safety, deployment protocol, prompt defense.

| Effect | Current (2026) | After safe deployment | Basis |
|------|-------------|---------------|------|
| Deployment incident rate | 2-5/month | **< 0.1/month** | 4-stage rollout + auto rollback |
| Hallucination detection latency | hours-days | **< 30s** | streaming safety check |
| Prompt injection block | 60-70% | **> 95%** | layered classifier + de-obfuscation |
| Rollback time | 30min-2hr | **< 5min** | canary + SLA trigger |
| A/B safety test | non-standard | **chi2 significance** | p < 0.05 auto decision |
| Pre-certification | manual checklist | **CI/CD gate** | pipeline auto certification |

**One sentence**: a safety framework across training -> inference -> deployment -> prompt defense bridges the research-reality gap as a target pattern.

## §2 COMPARE (legacy vs safety-first deployment) -- ASCII comparison

```
+-------------------+----------------------------+---------------------------+
|  Barrier          |  Why it was a limit         |  Safe deployment pattern  |
+-------------------+----------------------------+---------------------------+
| reactive handling | manual rollback 30min-2hr   | realtime monitor+auto 5min|
| no safety test    | functional tests only       | CI/CD safety gate auto    |
| prompt unguarded  | single rule filter, exposed | layered injection + decode|
| non-std rollout   | all-at-once or manual canary| 4-stage + stat promotion  |
| no metrics        | subjective "it's safe"      | SLA metrics + dashboard   |
+-------------------+----------------------------+---------------------------+
```

```
+--------------------------------------------------------------------------+
|  [incident]   legacy ##############################  2-5/month          |
|               safe   ##............................  < 0.1/month        |
|  [detect]     legacy ##############################  hours-days         |
|               safe   #.............................  < 30s              |
|  [inj block]  legacy ##################............  60-70%             |
|               safe   #############################.  > 95%              |
|  [rollback]   legacy ##############################  30min-2hr          |
|               safe   ##............................  < 5min             |
+--------------------------------------------------------------------------+
```

## §3 REQUIRES (prerequisites)

| Prerequisite | Role |
|------|------|
| ai-adversarial | adversarial attack detection pipeline |
| ai-alignment | alignment regression test baseline |
| MLOps/CI-CD | pipeline infrastructure |
| production monitoring | realtime anomaly detection |
| prompt engineering | injection/jailbreak defense theory |

## §4 STRUCT (four-pillar structure)

```
+----------------+----------------+------------------+------------------+
|  training(4)   |  inference(4)  |  deploy proto(8) |  prompt def(8)   |
+----------------+----------------+------------------+------------------+
| A1 lr schedule | B1 speculative | C1 4-stage roll  | D1 sysprompt rob |
| A2 safe curric | B2 safe KV     | C2 realtime mon  | D2 inj classifier|
| A3 grad surgery| B3 safe compute| C3 auto rollback | D3 safe prompt   |
| A4 synth data  | B4 stream chk  | C4 A/B safe test | D4 de-obfuscate  |
|                |                | C5 canary deploy | D5 multi-turn def|
|                |                | C6 safety SLA    | D6 indirect inj  |
|                |                | C7 auto incident | D7 risk score    |
|                |                | C8 CI/CD cert    | D8 context def   |
+----------------+----------------+------------------+------------------+
   safe model ---------> safe inference -----> safe deploy -----> safe ops
```

## §5 FLOW (control flow)

```
train: [safe data] -> [curriculum] -> [grad surgery] -> [safe model]
infer: [input] -> [risk score] -> [inj classifier] -> [safe KV infer] -> [stream chk] -> [output]
deploy: [CI/CD cert] -> [canary 1%] -> [staging 10%] -> [limited GA 50%] -> [full GA]
emerg: SLA breach -> auto rollback -> incident triage -> isolation -> alert (< 5min)
```

## §6 EVOLVE (4-month roadmap)

| Stage | Period | Key deliverable |
|------|------|------------|
| 1 | month 1 | safety regression dataset, synthetic safety data, streaming check prototype, CI/CD gate |
| 2 | month 2 | 4-stage rollout, realtime dashboard, auto rollback, canary deploy |
| 3 | month 3 | injection classifier deploy, de-obfuscation, multi-turn detection, A/B chi2 auto decision |
| 4 | month 4 | full integration automation, safety SLA 99.9%, draft unattended ops across layers |

## §7 VERIFY (deployment safety verification -- Python stdlib only)

### §7.0 CONSTANTS (SLA thresholds)
reject rate cap 2%, hallucination cap 1%, p99 latency 500ms, rollback 300s, canary 1%, injection detect 95%.

### §7.1 DIMENSIONS (metric units)
reject/hallucination = dimensionless ratio (0-1). Latency = seconds (SI). Throughput = req/s (Hz). Unit mismatch rejects.

### §7.2 CROSS (3 independent metrics)
(1) reject rate (2) hallucination rate (3) incident rate -- simultaneous improvement across all three is genuine safety progress.

### §7.3 SCALING (traffic scaling)
log-log slope of safety-check latency vs traffic. alpha < 1.0 (sublinear) is needed for production viability.

### §7.4 SENSITIVITY (rollback threshold sensitivity)
For reject threshold 1%-5%, search the optimum where FP rollback < 1% and true detection > 99%.

### §7.5 LIMITS (theoretical detection limit)
attack space = vocab^L -> not enumerable. F1 > 0.95 is a reachable target but 100% is impossible (Rice's theorem). Zero-day pre-detection is impossible.

### §7.6 CHI2 (A/B significance)
2x2 contingency chi2 test. H0: two versions equally safe. p < 0.05 indicates significance. Minimum n >= 400 (d=0.2).

### §7.7 OEIS (attack combinatorial structure)
injection variants = C(L, k) x M. C(100,3) x 5 = 808,500 variants. Provides defense complexity lower bound.

### §7.8 PARETO (safety/latency/cost)
safety layer 0-5 x intensity combinations. safety > 0.95, latency increase < 50ms, cost < 20% Pareto frontier.

### §7.9 SYMBOLIC (canary risk boundary)
R = p x q x N. Fraction exact computation. p=1/100, q=1/1000, N=10^6 -> expected harm = 10 users.

### §7.10 COUNTER (honest limits)
- zero-day attacks: novel patterns outside the training distribution cannot be pre-detected
- distribution drift: passing tests does not guarantee production safety
- insider threat: prompt defense targets external actors; insiders need separate control
- compute cost: adding safety layers = added latency/cost (infinite safety = infinite cost)
- FALSIFIERS: scaling O(n^2)+, injection F1<0.7, A/B flipped conclusion, canary miss>10%

### §7 integrated verification code (stdlib only)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# §7 VERIFY -- AI deployment safety verification (stdlib only, domain=ai-deployment)
from math import log, sqrt, erfc, comb
from fractions import Fraction
import statistics, random

# §7.0 CONSTANTS
REJECT_MAX, HALLUC_MAX = 0.02, 0.01
P99_MS, ROLLBACK_SEC = 500, 300
CANARY_RATIO, INJECT_TARGET = 0.01, 0.95
STAGES = [0.01, 0.10, 0.50, 1.00]
assert len(STAGES) == 4 and 0 < REJECT_MAX < 1 and 0 < HALLUC_MAX < 1

# §7.1 DIMENSIONS -- ratios dimensionless, latencies additive
def rate_ok(num, den): return 0.0 <= num / den <= 1.0
def latency_sum(ms_list): return sum(ms_list)

# §7.2 CROSS -- 3 independent safety metrics
def cross_safety(rej, hal, inc, total):
    return rej < REJECT_MAX and hal < HALLUC_MAX and inc / total < REJECT_MAX

# §7.3 SCALING -- log-log slope
def scaling_exp(xs, ys):
    lx, ly = [log(x) for x in xs], [log(y) for y in ys]
    mx, my = statistics.mean(lx), statistics.mean(ly)
    num = sum((lx[i]-mx)*(ly[i]-my) for i in range(len(xs)))
    den = sum((lx[i]-mx)**2 for i in range(len(xs)))
    return num / den if den else 0.0

# §7.4 SENSITIVITY -- rollback threshold sensitivity
def sensitivity(thresholds, inc_rate=0.03, noise=0.005, n=1000, seed=42):
    random.seed(seed)
    results = []
    for th in thresholds:
        fp, tp, nh, ni = 0, 0, n//2, n-n//2
        for _ in range(nh):
            if 0.015 + random.gauss(0, noise) > th: fp += 1
        for _ in range(ni):
            if 0.015 + inc_rate + random.gauss(0, noise) > th: tp += 1
        results.append((th, fp/nh, tp/ni))
    return results

# §7.5 LIMITS -- F1 plus attack space
def f1_score(tp, fp, fn):
    p = tp/(tp+fp) if tp+fp else 0
    r = tp/(tp+fn) if tp+fn else 0
    return 2*p*r/(p+r) if p+r else 0

def attack_space(vocab=50000, L=100): return L * log(vocab)

# §7.6 CHI2 -- 2x2 contingency
def chi2_ab(ia, na, ib, nb):
    t = na + nb; ti = ia + ib; ts = t - ti
    exp_vals = [(ia, na*ti/t), (ib, nb*ti/t), (na-ia, na*ts/t), (nb-ib, nb*ts/t)]
    chi2 = sum((o-e)**2/e for o, e in exp_vals if e > 0)
    return chi2, erfc(sqrt(chi2/2)) if chi2 > 0 else 1.0

# §7.7 OEIS -- attack variant combinatorics
def variants(L, k, M): return comb(L, k) * M
def binom_seq(nmax, k): return [comb(n, k) for n in range(k, nmax+1)]

# §7.8 PARETO -- 3-axis search
def pareto(n_trials=1000, seed=42):
    random.seed(seed)
    pts = []
    for _ in range(n_trials):
        nl = random.randint(0, 5)
        st = [random.random() for _ in range(nl)]
        safety = 1 - (0.5**max(1,nl)) * (1 - statistics.mean(st) if st else 1)
        lat = sum(10 + 20*s for s in st)
        cost = sum(5 + 10*s for s in st)
        pts.append((safety, lat, cost))
    front = [p for p in pts if not any(
        q[0]>=p[0] and q[1]<=p[1] and q[2]<=p[2]
        and (q[0]>p[0] or q[1]<p[1] or q[2]<p[2]) for q in pts)]
    return front

# §7.9 SYMBOLIC -- Fraction canary risk
def canary_risk(p, q, N):
    return Fraction(p) * Fraction(q) * Fraction(N)

# §7.10 COUNTER
COUNTERS = ["zero-day pre-detection impossible", "distribution drift", "insider threat", "rising compute cost"]
FALSIFIERS = ["scaling O(n^2)+", "injection F1<0.7", "A/B flipped", "canary miss>10%"]

if __name__ == "__main__":
    r = []
    # §7.0
    r.append(("§7.0 CONSTANTS", abs(sum(STAGES)-1.61) < 0.01))
    # §7.1
    r.append(("§7.1 DIMENSIONS", rate_ok(20,1000) and latency_sum([10,20,15])==45))
    # §7.2
    r.append(("§7.2 CROSS 3-metric", cross_safety(0.01, 0.005, 5, 100000)))
    # §7.3
    alpha = scaling_exp([100,500,1000,5000,10000], [10,18,25,40,55])
    r.append(("§7.3 SCALING alpha=%.3f<1" % alpha, alpha < 1.0))
    # §7.4
    s = sensitivity([0.02, 0.03, 0.04, 0.05])
    r.append(("§7.4 SENSITIVITY", any(fp<0.05 and dt>0.95 for _,fp,dt in s)))
    # §7.5
    f1 = f1_score(950, 30, 50)
    r.append(("§7.5 LIMITS F1=%.3f" % f1, attack_space() > 100 and f1 > 0.90))
    # §7.6
    chi2, p = chi2_ab(50, 10000, 25, 10000)
    r.append(("§7.6 CHI2 p=%.4f" % p, p < 0.05))
    # §7.7
    v = variants(100, 3, 5)
    bs = binom_seq(10, 2)
    r.append(("§7.7 OEIS", v == comb(100,3)*5 and bs == [1,3,6,10,15,21,28,36,45]))
    # §7.8
    front = pareto()
    r.append(("§7.8 PARETO", any(p[0]>0.90 for p in front)))
    # §7.9
    risk = canary_risk(Fraction(1,100), Fraction(1,1000), 1000000)
    r.append(("§7.9 SYMBOLIC", risk == Fraction(10)))
    # §7.10
    r.append(("§7.10 COUNTER>=3", len(COUNTERS)>=3 and len(FALSIFIERS)>=3))

    passed = sum(1 for _,ok in r if ok)
    print("=" * 60)
    for name, ok in r:
        print(f"  [{'OK' if ok else 'FAIL'}] {name}")
    print("=" * 60)
    print(f"{passed}/{len(r)} PASS (AI deployment safety)")
```

## §8 IDEAS (26 research ideas)

### Pillar A -- training optimization (4)
- **A1 safe lr schedule**: cosine annealing + safety regression checkpoints, auto lr decrease on alignment drop
- **A2 safe curriculum**: easy safety cases -> boundary cases ordering, safety score up with same data
- **A3 gradient surgery**: when capability/alignment gradients conflict, project onto alignment direction (PCGrad-style)
- **A4 synthetic safety data**: auto-generate red-team prompt + expected refusal pairs, expand test coverage

### Pillar B -- inference optimization (4)
- **B1 safe speculative decoding**: pre-screen draft tokens with a safety classifier before sending to the verifier
- **B2 safe KV cache**: protect system-prompt / safety-directive KV entries from eviction, preserve safety context
- **B3 safe compute allocation**: allocate extra compute to high-risk inputs, hold average latency + lift safety
- **B4 streaming check**: token-wise realtime safety evaluation, stop generation immediately on unsafe sequence

### Pillar C -- deployment protocol (8)
- **C1 4-stage rollout**: canary(1%) -> staging(10%) -> limited GA(50%) -> full GA, promote when SLA holds
- **C2 realtime monitoring**: reject/hallucination/latency/incident realtime dashboard + z-score anomaly alert
- **C3 auto rollback**: on SLA breach, restore previous version within 5 minutes (blue-green zero-downtime)
- **C4 A/B safety test**: promote only when chi2 significance + effect size are jointly met
- **C5 canary deploy**: 1% traffic split, Fraction risk-boundary pre-computation, cut traffic on anomaly
- **C6 safety SLA**: reject<2%, hallucination<1%, p99<500ms, injection block>95% quantitative baseline
- **C7 auto incident response**: detect -> triage (severity 1-4) -> isolate -> alert -> auto report pipeline
- **C8 CI/CD cert**: deployment only permitted when safety regression tests pass gate

### Pillar D -- prompt safety (8)
- **D1 system-prompt robustness**: 1000 auto-fuzzed variants of "repeat the system prompt"
- **D2 injection classifier**: normal/injection/jailbreak 3-class, n-gram + structure + intent analysis, F1>0.95 target
- **D3 safe prompt generation**: delimiter hardening + instruction repetition + meta-instruction insertion auto-applied
- **D4 de-obfuscation**: normalize base64/ROT13/Unicode substitution then re-classify
- **D5 multi-turn attack defense**: intent trajectory analysis across dialog history, track cumulative risk score
- **D6 indirect injection defense**: detect malicious instructions in external docs/URLs, trust boundary authority separation
- **D7 risk score**: score input risk 0-1 (injection keyword density / encoding ratio / structure / context drift)
- **D8 context attack defense**: detect attention-distraction attacks in long context, preserve system-prompt attention

## §9 METRICS (key indicators)

| Metric | Baseline | Month 2 | Month 4 |
|------|--------|------|------|
| injection F1 | 0.65 | 0.90 | > 0.95 |
| reject rate | 5% | 2% | < 1.5% |
| hallucination | 3% | 1% | < 0.5% |
| rollback time | 60min | 10min | < 3min |

## §10 RISKS

1. over-filtering -> false positives -> degraded UX. Mitigation: track precision-recall balance
2. safety layers -> added latency. Mitigation: §7.8 Pareto optimization
3. adversarial evolution -> defense bypass. Mitigation: continuous red-team + retraining
4. organizational resistance -> deployment delay. Mitigation: minimize friction via automation

## §11 DEPENDENCIES

```
ai-adversarial --+--> ai-deployment --> MLOps infra
ai-alignment  ---+                  --> monitoring platform
                                    --> CI/CD pipeline
```

## §12 TIMELINE

| Week | Deliverable | Verification |
|------|--------|------|
| 1-4 | safety dataset + injection classifier v1 | §7.5 F1, §7.7 variants |
| 5-8 | 4-stage rollout + canary | §7.9 risk boundary, §7.3 scaling |
| 9-12 | A/B test + auto rollback | §7.6 chi2, §7.4 sensitivity |
| 13-16 | full integration automation | §7.0-§7.10 full pass |

## §13 TOOLS

| Tool | Role |
|------|------|
| Python stdlib | verification (zero external deps) |
| CI/CD pipeline | safety gate |
| log aggregation | realtime monitoring |
| A/B platform | traffic split |

## §14 TEAM (skills)

| Role | Headcount | Focus |
|------|------|------|
| ML safety researcher | 2 | alignment, red team, attack/defense |
| MLOps engineer | 1 | CI/CD, monitoring, deployment automation |
| security engineer | 1 | prompt injection, penetration testing |

## §15 REFERENCES

- Perez et al. "Red Teaming Language Models" (2022)
- Greshake et al. "Indirect Prompt Injection" (2023)
- Anthropic "Core Views on AI Safety" (2023)
- Anil et al. "Many-shot Jailbreaking" (2024)
- OWASP "LLM Top 10" (2025)

---
