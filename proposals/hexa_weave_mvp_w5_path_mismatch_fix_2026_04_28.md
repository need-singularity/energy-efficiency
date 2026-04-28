# HEXA-WEAVE MVP W5 — path mismatch fix (cycle 16)

**Date:** 2026-04-28
**Cycle:** 16 (path-mismatch closure)
**Owner:** tool/hexa_weave_w5_setup.hexa
**Parent missions:**
- proposals/hexa_weave_mvp_2026_04_28.md
- proposals/hexa_weave_mvp_w5_sandbox_cycle14_prep_2026_04_28.md (cycle 14 1-command runbook)
- design/kick/2026-04-28_w5-supporting-scripts-cycle15_omega_cycle.json (cycle 15 supporting scripts)

## 1. Mission

Cycle 14 authored `tool/hexa_weave_w5_setup.hexa` (305 LoC, 8-step
idempotent runbook) referencing `~/core/hexa-weave/scripts/...` for Step 6
(RCSB cluster-split download) and Step 8 (6L1U inference verdict).

Cycle 15 authored `scripts/rcsb_cluster_split_fetch.py` and
`scripts/w5_verdict.py` (+ `tool/hexa_weave_vram_ladder.hexa` and the
sister-repo README spec) — but in **n6-architecture** (this repo), not in
the sister `hexa-weave/` repo.

Net effect: Step 6 and Step 8 dispatch on the user's machine would emit
`FileNotFoundError`, breaking the 1-command claim.

Cycle 15's discovery_absorption row already disclosed this (raw 91 C3:
"agent did not edit cycle-14 .hexa to repoint Step 6/8 paths"). Cycle 16
closes that disclosure.

## 2. Path resolution decision (raw 91 C3 honest)

Three options were on the table:

| Option | Description | Trade-off |
|---|---|---|
| A | User runs `mkdir ~/core/hexa-weave/scripts/ && cp ...` before W5 dispatch | Two-source-of-truth; user has to remember to re-cp on each script update |
| B | Patch Step 6/8 to call `~/core/n6-architecture/scripts/...` directly via `HW_SCRIPTS_DIR` env override | Single-source-of-truth; cross-repo dependency made explicit |
| C | Auto-detect via relative-path resolver | Adds runtime probe complexity for marginal benefit |

**Selected: Option B** — minimal-scope, single-source-of-truth preserved,
raw 142 D2 (try-and-revert) friendly because the change is one
inline shell variable + a `test -f` guard, easily reverted via `git
checkout`.

## 3. Patch applied

### 3.1 Header (cycle annotation + version bump)

```diff
-# Cycle 14 / 2026-04-28
+# Cycle 14 / 2026-04-28 (initial 1.0.0)
+# Cycle 16 / 2026-04-28 (1.0.1: Step 6/8 path mismatch fix — HW_SCRIPTS_DIR from ~/core/n6-architecture/scripts/)
+# raw 47 cross-repo: n6-architecture (scripts) -> hexa-weave (data/weights/outputs)
-version: 1.0.0
+version: 1.0.1
```

### 3.2 Step 6 cmd (RCSB cluster-split download)

Before:

```yaml
python ~/core/hexa-weave/scripts/rcsb_cluster_split_fetch.py \
  --train 78 --val 13 --test 9 --seed 0xf927314f \
  --out ~/core/hexa-weave/data/ \
  2>&1 | tee ~/core/hexa-weave/logs/rcsb_split_$(date +%s).log
```

After:

```yaml
HW_SCRIPTS_DIR="${HW_SCRIPTS_DIR:-$HOME/core/n6-architecture/scripts}"
test -f "$HW_SCRIPTS_DIR/rcsb_cluster_split_fetch.py" || {
  echo "ERROR: rcsb_cluster_split_fetch.py not found at $HW_SCRIPTS_DIR" >&2
  echo "       set HW_SCRIPTS_DIR or run from /Users/ghost/core/n6-architecture/" >&2
  exit 127
}
python "$HW_SCRIPTS_DIR/rcsb_cluster_split_fetch.py" \
  --train 78 --val 13 --test 9 --seed 0xf927314f \
  --out ~/core/hexa-weave/data/ \
  --resume \
  2>&1 | tee ~/core/hexa-weave/logs/rcsb_split_$(date +%s).log
```

Two enhancements bundled:

1. `--resume` added: idempotent re-dispatch on partial failure (raw 65
   idempotent + raw 142 D2 single-retry friendly).
2. `test -f` guard with explicit error message: fail-fast with actionable
   "set HW_SCRIPTS_DIR or run from /Users/ghost/core/n6-architecture/"
   guidance (raw 66 ai-native trailer-friendly because exit 127 → step 6
   failed → trailer.suggested_fallback can prompt user to clone).

### 3.3 Step 8 cmd (Verifier verdict block)

Before:

```yaml
python ~/core/hexa-weave/scripts/w5_verdict.py \
  --pred ... --ref ... --vram-csv ... \
  --rmsd-max 5.0 --tm-min 0.4 --vram-max-mb 11000 \
  --out ...
```

After:

```yaml
HW_SCRIPTS_DIR="${HW_SCRIPTS_DIR:-$HOME/core/n6-architecture/scripts}"
test -f "$HW_SCRIPTS_DIR/w5_verdict.py" || {
  echo "ERROR: w5_verdict.py not found at $HW_SCRIPTS_DIR" >&2
  echo "       set HW_SCRIPTS_DIR or run from /Users/ghost/core/n6-architecture/" >&2
  exit 127
}
python "$HW_SCRIPTS_DIR/w5_verdict.py" \
  --pred ... --ref ... --vram-csv ... \
  --rmsd-max 5.0 --tm-min 0.4 --vram-max-mb 11000 \
  --out ...
```

Note: only the verifier verdict block uses `HW_SCRIPTS_DIR`; the
RCSB-fetched FASTA + ref PDB and OpenFold inference itself stay in
`hexa-weave/` (data/weights/outputs separation preserved).

### 3.4 Caveats section update

Cycle 14's caveat #2 ("scripts/* are referenced but NOT YET created")
was replaced with the cycle 16 path-resolution caveat:

> scripts/rcsb_cluster_split_fetch.py + scripts/w5_verdict.py LIVE in
> n6-architecture (this repo) per cycle 15; sister-repo hexa-weave/ is
> data + weights + outputs only. Step 6/8 use HW_SCRIPTS_DIR (default
> $HOME/core/n6-architecture/scripts) — cycle 16 path mismatch fix.

A new caveat #6 (raw 47 cross-repo edge declaration) was added:

> raw 47 cross-repo edge: HW_SCRIPTS_DIR sources n6-architecture/scripts;
> hexa-weave/ sister repo receives writes only (data/, weights/,
> outputs/, logs/). User MUST git clone n6-architecture before dispatch
> OR override HW_SCRIPTS_DIR.

## 4. Selftest evidence

### 4.1 Syntax check

```
$ python3 -c "import yaml; yaml.safe_load(open('tool/hexa_weave_w5_setup.hexa').read().split('\n',1)[1])"
schema: hexa/runbook/v1
version: 1.0.1
total_steps: 8
```

YAML PASS.

### 4.2 Bash semantic check

```
$ bash -n <<< (extracted Step 6 cmd block)
rc=0   # syntax PASS
```

### 4.3 Live probe

```
$ HW_SCRIPTS_DIR="${HW_SCRIPTS_DIR:-$HOME/core/n6-architecture/scripts}"
$ echo "Resolved HW_SCRIPTS_DIR=$HW_SCRIPTS_DIR"
Resolved HW_SCRIPTS_DIR=/Users/ghost/core/n6-architecture/scripts
$ test -f "$HW_SCRIPTS_DIR/rcsb_cluster_split_fetch.py" && echo PASS
PASS
$ test -f "$HW_SCRIPTS_DIR/w5_verdict.py" && echo PASS
PASS
$ python3 "$HW_SCRIPTS_DIR/rcsb_cluster_split_fetch.py" --help | head -1
usage: rcsb_cluster_split_fetch.py [-h] --out OUT [--train TRAIN] ...
$ python3 "$HW_SCRIPTS_DIR/w5_verdict.py" --help | head -1
usage: w5_verdict.py [-h] --pred PRED --ref REF ...
```

### 4.4 CLI flag conformance

| Step | flag | argparse-defined | result |
|---|---|---|---|
| 6 | `--out` | yes (`p.add_argument("--out", required=True)`) | PASS |
| 6 | `--train --val --test --seed` | yes | PASS |
| 6 | `--resume` | yes (`action="store_true"`) | PASS |
| 8 | `--pred --ref --vram-csv` | yes | PASS |
| 8 | `--rmsd-max --tm-min --vram-max-mb` | yes | PASS |
| 8 | `--out` | yes (verdict JSON path) | PASS |

All script-side argparse signatures match the Step 6/8 cmd invocations.

### 4.5 hexa parse caveat

`/Users/ghost/core/hexa-lang/hexa parse tool/hexa_weave_w5_setup.hexa`
emits 60+ parse errors — **but this is pre-existing**, identical to the
cycle-14 baseline. The .hexa-suffixed runbook files in this repo are
authored as YAML specs (per cycle-14 schema declaration `schema:
hexa/runbook/v1`); the actual hexa-lang interpreter parser is for
strand-typed hexa code, not YAML-spec runbooks. The runner that consumes
this .hexa is implied by the cycle-14 caveat #1 "the actual hexa runner
must implement step dispatch + probe + rollback + failure trailer per
main pseudocode." Cycle 16 inherits this caveat unchanged.

## 5. raw 142 D2 try-and-revert

If patch fails post-cycle smoke test, revert via:

```
git checkout HEAD -- tool/hexa_weave_w5_setup.hexa
```

This reverts to the cycle-14 1.0.0 path layout (still broken but
documented). User then falls back to **option A** (manual `cp` of scripts
into `~/core/hexa-weave/scripts/`).

## 6. raw 47 cross-repo

Explicit edge declaration:

```
n6-architecture/                   <-- THIS repo (source of truth)
├── tool/hexa_weave_w5_setup.hexa  <-- runbook
└── scripts/
    ├── rcsb_cluster_split_fetch.py  <-- Step 6 invokes
    └── w5_verdict.py                <-- Step 8 invokes

~/core/hexa-weave/                 <-- SISTER repo (data + weights + outputs)
├── data/                          <-- Step 6 writes (manifest + FASTAs)
├── weights/                       <-- Step 5 writes (AlphaFold params)
├── outputs/                       <-- Step 8 writes (predictions + verdict.json)
├── openfold/                      <-- Step 4 writes (shallow clone)
├── venv/                          <-- Step 2 writes
├── test_inputs/                   <-- Step 8 writes (6L1U.fasta + ref)
└── logs/                          <-- All steps write
```

## 7. raw 138 sentinel

Step 8 (the W5 PASS verdict) emits `__W5_SETUP_RESULT__ PASS|FAIL` per
the existing `pass_criteria` block. Cycle 16 patch does not modify the
sentinel emission — only the path to the verifier — so the sentinel
contract is preserved.

## 8. raw 91 C3 honest

- **Cycle 14 prep mistake acknowledged**: cycle 14 wrote the runbook
  before cycle 15 wrote the scripts; the implicit assumption was
  scripts would be authored under `hexa-weave/scripts/`. Cycle 15
  decided n6-architecture/scripts was the better single-source-of-truth
  location (Lean/atlas/proposals/scripts all colocate). Neither cycle
  was wrong individually; the mismatch is a cross-cycle handoff bug
  closed cycle 16.
- **Option B chosen** despite Option A being slightly less invasive
  because Option A creates a two-source-of-truth that drifts whenever
  a script is updated.
- **Sister-repo `hexa-weave/` is still required**: cycle 16 does NOT
  collapse repos. The sister repo holds large data (~3 GB weights, ~100
  PDB FASTAs, ~50 MB inference outputs) which is not appropriate for the
  n6-architecture source repo.
- **`hexa parse` parser noise is pre-existing** and not caused by the
  cycle 16 patch — see §4.5.
- **Option C deferred**: a full relative-path resolver would require
  introspecting the calling shell's PWD or PATH or git rev-parse, which
  adds runtime probe complexity for a single-step benefit. `HW_SCRIPTS_DIR`
  env override + sensible default covers 99% of dispatch scenarios.

## 9. Falsifiers preregistered

- **F-W5-PATH-1** (deadline 2026-04-30): User runs `hexa run --dry-run
  tool/hexa_weave_w5_setup.hexa --only 6,8` from `/Users/ghost/core/n6-architecture/`
  and Step 6/8 cmd echoes resolve `HW_SCRIPTS_DIR=/Users/ghost/core/n6-architecture/scripts`
  and pass the `test -f` probe. **Falsified if** `HW_SCRIPTS_DIR`
  resolves to wrong path or `test -f` fails.

- **F-W5-PATH-2** (deadline 2026-05-05): User dispatches full W5 1-command
  on ubu1 with HW_SCRIPTS_DIR=$HOME/core/n6-architecture/scripts, and
  Step 6 produces `~/core/hexa-weave/data/manifest.json` with 100 entries
  AND Step 8 produces `~/core/hexa-weave/outputs/verdict.json` with
  `__W5_SETUP_RESULT__ PASS`. **Falsified if** Step 6 or Step 8 emits
  exit 127 (path probe fail) or any other non-zero rc.

- **F-W5-PATH-3** (deadline 2026-04-29): Independent rerun of cycle 16
  selftest §4.3 reproduces all 4 PASS lines. **Falsified if** any of the
  4 lines fail on a clean shell.

- **F-W5-PATH-4** (deadline 2026-05-01): `git diff cycle-14-baseline
  HEAD -- tool/hexa_weave_w5_setup.hexa` shows ONLY 3 hunks (header,
  step 6 cmd, step 8 cmd, caveats) and no other steps were touched
  (raw 142 D2 minimal-scope). **Falsified if** unintended hunks appear.

- **F-W5-PATH-5** (deadline 2026-05-15): Sister-repo hexa-weave/
  README is updated by cycle 17+ to declare `HW_SCRIPTS_DIR` setup
  prerequisite ("clone n6-architecture before W5 dispatch"). **Falsified
  if** README still implies sister-repo-self-contained dispatch.

## 10. Next-cycle handoff

- **cycle 17+** (W5 actual dispatch): user runs the patched runbook on
  ubu1; cycle 17 writes the post-dispatch verdict + alien-grade bump.
- **cycle 17+** (sister-repo README spec absorption): cycle-15 README
  spec (`proposals/hexa_weave_sister_repo_README_spec_2026_04_28.md`)
  needs HW_SCRIPTS_DIR mention added, then user manually creates
  sister-repo .git + commits README.

## 11. Aggregate cost

- LoC delta: +20 / -3 (net +17 in tool/hexa_weave_w5_setup.hexa)
- Selftest wall: <2 sec
- Cycle wall: ~10 min (analysis + patch + selftest + this proposal +
  kick + registry)
- Disk: 0 (no new files written to ~/core/hexa-weave/)
- Network: 0
- Reversibility: 100% (single git checkout)

## 12. Sentinel

`__W5_PATH_FIX_RESULT__ PASS` (cycle 16 patch landed; selftest 4/4 PASS;
runbook 1.0.1 ready for user dispatch).
