# HEXA-WEAVE MVP — W5 Sandbox Attempt Report

**Date**: 2026-04-28
**Cycle**: 8 / fan-out 4/5
**Companion doc**: `hexa_weave_mvp_w5_user_approval_request_2026_04_28.md`
**Witness**: `design/kick/2026-04-28_hexa-weave-mvp-w5-sandbox-plan_omega_cycle.json`
**Implementation status**: **plan + dry-run verification only** — no destructive ops executed; awaiting user approval

---

## 1. TL;DR

- 6 dry-run read-only checks completed: 3 PASS, 3 expected GAP (Mac dev box has no CUDA/no python3.10/no nvidia-smi; redirects GPU work to ubu1 per W3 spec).
- OpenFold v2.2.0 tag SHA `e938c184a291bf053af3b14c1e3e8bb29aee57e2` confirmed (matches W3 spec pin character-for-character).
- RCSB FASTA endpoint live (HTTP/2 200, `text/x-fasta`); 6L1U fetch is trivial CPU-only step.
- 8-item user approval checklist drafted with per-item reversibility + estimated cost.
- 4 alternative GPU-free paths identified (none require items 3, 5, 6, 8).
- F-TP5-b 90d gate now at ~35% (spec-side); awaiting user approval to advance to ~45% (one forward pass verified).

---

## 2. Dry-run verification (6 items, read-only)

| # | check | result | classification |
|---|-------|--------|----------------|
| D1 | `ls ~/core/hexa-weave/` | `No such file or directory` | PASS — clean slate |
| D2 | `python3.10 --version` | `command not found` (system has 3.14.4) | GAP — install needed |
| D3 | `python3 -c "import torch; print(torch.cuda.is_available())"` | `torch 2.10.0`, `cuda_available=False` | GAP — Mac has no CUDA (expected) |
| D4 | `git ls-remote ... v2.2.0` | `e938c184a291bf053af3b14c1e3e8bb29aee57e2` | PASS — SHA matches W3 spec |
| D5 | `curl -sI https://www.rcsb.org/fasta/entry/6L1U` | HTTP/2 200, `text/x-fasta; charset=utf-8` | PASS — endpoint live |
| D6 | `nvidia-smi` | `command not found` | GAP — Mac has no NVIDIA GPU (expected) |

PASS: 3/6 (D1, D4, D5). GAP: 3/6 (D2, D3, D6 — all environmental, redirected to ubu1).

The 3 GAPs are not blockers — they confirm the W3 spec's host topology assumption: **Mac is the spec/dev box; ubu1 is the GPU execution host.**

---

## 3. User approval gate (8 items)

Full per-item detail in `hexa_weave_mvp_w5_user_approval_request_2026_04_28.md`. Summary:

| # | item | host | disk | wall | GPU-week | reversible |
|---|------|------|------|------|----------|------------|
| 1 | `~/core/hexa-weave/` 8-subdir mkdir | Mac | 0 | 1 min | 0 | yes |
| 2 | python3.10 install + venv | Mac | ~80 MB | 5 min | 0 | yes |
| 3 | PyTorch 2.5.1+cu124 install | ubu1 | ~5 GB | 10 min | 0 | yes |
| 4 | OpenFold v2.2.0 shallow clone | ubu1 | ~120 MB | 2 min | 0 | yes |
| 5 | OpenFold weights (~3 GB) download | ubu1 | ~3 GB | 5-15 min | 0 | yes |
| 6 | sm_120 deepspeed source compile | ubu1 | ~500 MB | 10 min | 0 | yes |
| 7 | PDB 6L1U FASTA fetch | either | <10 KB | <1 sec | 0 | yes |
| 8 | ubu1 GPU forward pass dry-run | ubu1 GPU | ~50 MB | 30 min | ~0.001 | yes |

**Aggregate**: ~8.6 GB remote disk, ~8 GB bandwidth, ~0.001 GPU-week, ~60-90 min wall (sequential).

User reply expected as `approve: <list>; defer: <list>`. Four approval modes (A full, B1/B2/B3 partial, C deferral, D alternate) defined in companion doc.

---

## 4. Alternative GPU-free paths (executable WITHOUT user approval, or with minimal approval)

These paths advance F-TP5-b without burning GPU or downloading weights.

### Alt-1 — spec-only external review

- **What**: package W3 (35.5 KB) + W4 (34.3 KB) + W5 (this) specs and request external reviewer evaluation
- **Cost**: $0, ~1 hour author time to assemble package
- **Approval needed**: none (read-only spec sharing)
- **Yield**: independent spec validation; surfaces design flaws before any GPU burn
- **F-TP5-b gate move**: +5% (spec-quality validation)

### Alt-2 — GPU-free dataset prep

- **What**: items 1, 2, 4, 7 only (mkdir + py3.10 venv + OpenFold source clone + 6L1U FASTA). No torch install, no weights, no GPU.
- **Cost**: ~10 min wall, ~150 MB disk
- **Approval needed**: items 1, 2, 4, 7 (lightweight subset)
- **Yield**: env skeleton + reference codebase + test sequence ready; can read source code, write integration scaffolds, plan test harness
- **F-TP5-b gate move**: +5% (env-readiness validation)

### Alt-3 — mock-up architecture validation (no torch, no weights)

- **What**: write Python stubs that mimic OpenFold's I/O signatures (input: FASTA / MSA / template; output: coords + pLDDT) using random tensors. Validate the HEXA-WEAVE write-side wrapper around these stubs without any real model.
- **Cost**: ~2-4 hours author time, $0 compute
- **Approval needed**: items 1, 2 only (just dirs + py3.10 venv); torch CPU-only is enough
- **Yield**: full integration scaffold (data loader, MSA builder, output parser, eval harness) tested against mocks; when real weights land, only the model call swaps in
- **F-TP5-b gate move**: +10% (architecture validated end-to-end with mock model)
- **Risk**: mock signatures may diverge from real OpenFold's at integration time — real-model swap-in surfaces gaps; mitigation = re-read OpenFold source signatures during stub writing

### Alt-4 — Lean4 axiom continuation (decoupled from GPU)

- **What**: extend ax1/ax2 (per W2/W3 lean4 audits already in proposals/) with mk-bridge formal proofs (W5 ax2/mkbridge integration spec already exists)
- **Cost**: ~2-6 hours author time, $0 compute
- **Approval needed**: none (file edits only, no installs)
- **Yield**: formal verification track advances independently of GPU track; provides correctness floor before any forward pass
- **F-TP5-b gate move**: +5% (proof-side validation)
- **Note**: this path runs in parallel with the GPU track; does not block or unblock it

### Recommended sequencing

If user wants to make progress without yet approving GPU/weight downloads:
1. **Alt-2 first** (10 min, items 1+2+4+7) — establishes skeleton.
2. **Alt-3 second** (2-4 hr) — validates wrapper architecture against mock model.
3. **Alt-4 in parallel** — formal proof track.
4. **Then** approve items 3, 5, 6, 8 (the GPU-burning items) once Alt-2/3/4 give confidence the wrapper is correct.

This sequencing reduces risk of burning GPU on a misdesigned wrapper.

---

## 5. F-TP5-b 90d MVP gate progress

| W milestone | gate share | status |
|-------------|-----------|--------|
| W1 architecture decision | 5% | DONE (cycle 5) |
| W2 base model integration spec | 5% | DONE (cycle 5) |
| W3 clone+VRAM spec | 10% | DONE (cycle 6) |
| W4 8-subdir+dryrun spec | 10% | DONE (cycle 7) |
| W5 plan + dry-run + approval doc | 5% | DONE (cycle 8 — this) |
| W5 actual exec (8 items) | 10% | AWAITING APPROVAL |
| W6 training | 25% | future |
| W7 ax2/mkbridge integration | 15% | future |
| W8 downstream eval | 15% | future |

Current: **35% spec-complete**. Post-approval execution: **45%**.

---

## 6. raw 91 C3 honest disclosures

1. **No code has been run.** This cycle produced two markdown documents and ran 6 read-only shell commands. Nothing is installed, nothing is downloaded, no GPU has been touched.
2. **Local Mac is the wrong host for items 3, 5, 6, 8.** Per D3+D6 dry-run, Mac has no CUDA. The W3 spec already designates ubu1 as the GPU host; this is consistent.
3. **python3.10 pin is brittle.** D2 shows local Mac has only 3.14. ubu1 likely needs `apt install python3.10` (additional sudo step not in current checklist). Recommendation: flag in companion doc Section 8 (already flagged).
4. **sm_120 deepspeed is bleeding-edge.** W4 spec fallback row exists; user should approve Item 6 *with* fallback authorization, not bare.
5. **GPU-week 0.001 estimate** is optimistic — assumes one clean 30-min inference. OOM-driven retries (per W4 5-row fallback) could double or triple this. Real range: 0.001 - 0.004 GPU-week for Item 8 alone.
6. **Cost-attribution coverage is incomplete.** raw 86 demands per-resource cost; this doc estimates compute and storage but does not quantify (a) author/reviewer human-hours, (b) external validation cost if Alt-1 is taken, (c) opportunity cost vs other 90d-gate work.

---

## 7. Falsifiers (raw 71, TRANSCEND-tier, 5 items)

1. **F-W5-1** — Within 7 days, user approves all 8 items but Item 8 forward pass fails with non-OOM error (e.g. SHA mismatch on weights, OpenFold API breakage, deepspeed/torch version conflict). Detection: error log from ubu1. Trip action: revert to W4 5-row fallback; if fallback also fails, halt and re-spec.
2. **F-W5-2** — Within 14 days, sm_120 deepspeed source build fails irrecoverably on ubu1 (Item 6). Detection: build log error. Trip action: switch to sm_90 prebuilt deepspeed (W4 fallback); accept reduced perf.
3. **F-W5-3** — Within 30 days, RCSB removes 6L1U or changes FASTA endpoint format (D5 endpoint changes). Detection: D5 re-run returns non-200 or non-FASTA. Trip action: switch to PDB FTP mirror or local cache; update W3/W4 spec.
4. **F-W5-4** — Within 7 days, OpenFold v2.2.0 tag is force-pushed (SHA `e938c184` no longer resolves). Detection: D4 re-run returns different SHA. Trip action: pin to commit SHA explicitly in clone command (`--branch e938c184` or post-clone `git checkout e938c184`).
5. **F-W5-5** — Within 14 days, user reports the 8-item checklist is too coarse (e.g. wants to split Item 5 into "weight-fetch" + "weight-verify" + "weight-load") OR too fine (e.g. wants to bundle 1+2+4+7 as one approval). Detection: user feedback. Trip action: re-issue companion doc with revised granularity; honor user's preferred chunking.

---

## 8. Deliverables

- This file: `proposals/hexa_weave_mvp_w5_sandbox_attempt_2026_04_28.md`
- Companion approval request: `proposals/hexa_weave_mvp_w5_user_approval_request_2026_04_28.md`
- Witness JSON: `design/kick/2026-04-28_hexa-weave-mvp-w5-sandbox-plan_omega_cycle.json`
- Dry-run results: §2 above (6 commands, 3 PASS, 3 GAP)
- Alternative GPU-free paths: §4 (4 alternatives)
- F-TP5-b 90d gate progress: §5 (35% → 45% post-approval)
