---
schema: canon/docs/own21_drift_policy/ai-native/1
last_updated: 2026-05-04
ssot:
  proposal_only: true
  predecessor_handoff: canon_meta/doc/canon_own_readme_mk2_reconstruction_2026_05_04.ai.md
related_rules: [.own.readme own#21]
status: PROPOSAL (caller policy decision required)
policy:
  destructive_ops: 0
omega_cycle: investigation-only
---

# own#21 NEXUS tests count drift policy (2026-05-04)

## §1 Current values

- README L7 badge: `[![NEXUS](https://img.shields.io/badge/NEXUS-1116%20tests-green.svg)](tools/nexus/)`
- README L70 stats: ``  NEXUS tests:    1116``
- reports/n6_selftest.json fields:
  - `schema`: `canon/n6_selftest/1`
  - `ts`: `2026-04-24T12:36:19Z`
  - `total`: `51`
  - `pass`: `51`
  - `fail`: `0`
- Drift magnitude: 1116 / 51 ≈ 21.9× — almost certainly NOT the same metric.

## §2 History trace

### "1116" provenance

- **First introduced**: `60dc7eea` (2026-04-03 17:32:09 +0900) "Sync project list from TECS-L"
  - +1 README.md edit, no accompanying counter source. Badge format `NEXUS--6-1116%20tests`.
  - DSE was 323 at that point; STATS block created with `NEXUS-6 tests: 1116` literal.
- **Subsequent touches**: `04b17e8a` growth-cycle-1, `aec9faca`/`4b83e496`/`bdecf711` "Sync project list from TECS-L".
- **Last touched**: `2517fdec` (chore readme drift fix, BADGE/COMMON_LINKS reseal — kept 1116) and `e9c70049` (HEXA-WEAVE biology — kept 1116, only DSE bumped 323→324).
- **Likely meaning**: Static/legacy literal hard-coded into AUTO:STATS region at sync time from external TECS-L source. **No code in this repo has ever produced 1116.** The badge label still references `tools/nexus/` (a path that does not exist in the repo root), suggesting the count came from a sibling `nexus` repo's test inventory at sync time and has never been refreshed.

### "51" provenance

- **Most recent commit modifying selftest.json**: `e081a05e` "meta: regen selftest + blockers (post-push health verify)" — message states "Counts stable: selftest 51/51 pass, 0 fail".
- **Earlier same-day commits**: `4c583f89` and `fbb24a3e` (2026-04-24) "flip selftest stubs to full" — these are the commits that brought selftest_total from 19 (history/2026-04-23: total=19) up to 51.
- **Historical trajectory**:
  - 2026-04-22: total=16 (reports/history/2026-04-22/n6_selftest.json)
  - 2026-04-23: total=19 (reports/history/2026-04-23/n6_selftest.json)
  - 2026-04-24: total=51 (current reports/n6_selftest.json)
- **Tool maintaining it**: There is NO direct producer of `reports/n6_selftest.json` in `tool/`, `scripts/`, or `bin/`. The only references are:
  - `tool/own_nexus6_tests_drift.hexa` — READS the file (own#21 lint)
  - `tool/_n6_lib` — supporting library reference
- **Likely meaning**: count of registered scanner claims (one verdict entry per scanner). reports/n6_selftest.json verdicts list contains exactly 51 scanner names (`scan_blockers`, `scan_roi`, ..., `run_proof_obligations`).

## §3 Ground-truth counts

| Metric | Count | Source |
|---|---|---|
| Scanner claim files (`scanners/*.claim.json`) | **54** | `ls scanners/*.claim.json \| wc -l` |
| Selftest verdict entries (one per scanner) | **51** | `reports/n6_selftest.json#verdicts.length` |
| .hexa files under any path containing `test` | 25 | `find . -path '*/test*' -name '*.hexa'` |
| .hexa files w/ `fn test_*`/`fn _test_*`/`fn selftest*` defs | 25 (files), 36 (defs) | grep `^fn test_…` over .hexa, no worktrees |
| Files w/ `_selftest` or `--selftest` token | 25 | `grep -rln '_selftest\|--selftest' --include='*.hexa'` |
| `*test*.py` files | 0 | `find . -name '*test*.py'` (raw 9 hexa-only is in force) |
| Total .hexa files in repo (ex worktrees) | 946 | `find . -name '*.hexa' -not -path '*/worktrees/*'` |
| Schema reports/n6_selftest.json#total | **51** | reports/n6_selftest.json |
| README claim | **1116** | README.md L7+L70 |

**Third ground-truth read**: 51 (selftest) maps cleanly to 54 scanner claim files (verdicts list = 51, scanners dir = 54 → 3 scanners are declared as claim files but not yet wired to verdicts; consistent with the selftest harness covering only "live" scanners). 1116 maps to **nothing** measurable in this repo.

## §4 Policy options

### Option D1: Update README to match selftest.json (51) — RECOMMENDED

- **Pros**: README becomes accurate; own#21 drift lint goes green; matches the only auto-maintained source; matches three independent ground-truth probes (verdict list, scanner-dir count, history trajectory).
- **Cons**: Optical regression 1116 → 51 reads as ~95% loss to a casual visitor.
- **Risk**: If 1116 was ever accurate (in a sibling repo's test inventory), shrinking to 51 silently abandons that scope.
- **Mitigation**: Pair with Option D4 reframe (`NEXUS tests: 1116` → `n6 selftest scanners: 51`) to make the metric definition explicit.

### Option D2: Update reports/n6_selftest.json to match README (1116)

- **Pros**: README claim preserved; no optical regression.
- **Cons**: Requires 1065 new selftest verdict entries; selftest harness has no path to produce them; 1116 is not reproducible from any code path in this repo.
- **Risk**: Hand-edit of selftest.json would be a falsified report (raw#10 honest violation).
- **Verdict**: REJECT. Not feasible without inventing fixtures.

### Option D3: Re-baseline both to actual ground-truth count

- **Pros**: Forces explicit metric definition; both sources align with reality.
- **Cons**: There is no single canonical "test count" — candidates include scanner verdicts (51), scanner claim files (54), test_*.hexa files (25), test fn defs (36). Choice is arbitrary without policy.
- **Risk**: Future drift unless a tool emits the chosen value into both README and selftest.json on every regen.
- **Verdict**: VIABLE if paired with new harness emission logic.

### Option D4: Reframe the metric entirely

- README "NEXUS tests:" → "n6 selftest scanners:" (matches the 51 actually measured) OR "n6 scanner claims:" (matches the 54 declared).
- Document the metric definition in `.readme-rules.json` and `.own.readme own#21 scope`.
- **Pros**: Eliminates ambiguity; aligns label with what own#21 lint actually checks (the lint regex is `tests:\s+(\d+)` — relabeling to `scanners:` would also bypass the literal-match drift unless the regex is updated).
- **Cons**: Badge URL `NEXUS-1116%20tests-green` would also need relabeling (`NEXUS-51%20scanners`).
- **Verdict**: STRONGLY RECOMMEND combine with D1.

## §5 Recommendation

- **Primary**: **D1 + D4 combined** — update README to `51` AND relabel `NEXUS tests:` → `n6 selftest scanners:` (or similar accurate label). Keep README badge format `NEXUS-51%20scanners-green` to match.
- **Reasoning**:
  1. 1116 has no living source in this repo (raw#10 honest violation: the README claims a number nothing produces).
  2. 51 has a clear automated source (`reports/n6_selftest.json#total`, regen pattern visible across 04-22 → 04-23 → 04-24 history).
  3. Reframing the metric to "scanners" avoids the optical-regression read of 1116→51, since the new label conveys that this is a different (smaller, repo-internal) count, not a shrunk version of the old.
  4. own#21 lint (`tool/own_nexus6_tests_drift.hexa`) currently uses regex `tests:\s+(\d+)` — relabel requires either pattern update or compromise (keep `tests:` label).
- **Concrete next-step (caller-decision-pending)**:
  1. Caller approves D1+D4.
  2. New cycle: edit README L7 badge URL + L70 stats line; possibly update own#21 drift_pattern in `tool/own_nexus6_tests_drift.hexa` from `tests:\s+(\d+)` to a label-agnostic anchor.
  3. Update `.readme-rules.json` (and `.own.readme own#21 scope`) to record the canonical metric definition and source path.
  4. Verify by running `hexa tool/own_nexus6_tests_drift.hexa --verbose` → expect PASS with authoritative=51 matching README.
  5. Add reseal step (own#14) so README hash stays synchronized.

## §6 raw#10 honest caveats

1. **No producer for 1116 exists in this repo.** Searches across `tool/`, `scripts/`, `bin/`, `engine/`, `canonshared/`, `techniques/` find zero code that emits the integer 1116. This is a stale literal copied at TECS-L sync time on 2026-04-03 and never touched by an automated regen.
2. **51 ≠ 54** — there are 54 scanner claim files but only 51 verdicts. The 3-claim gap is unexplained and may itself be a separate drift (scanner declared but not registered in selftest harness). This is OUT OF SCOPE for own#21 but should be tracked.
3. **No selftest harness located.** The investigation could not find the tool that PRODUCES `reports/n6_selftest.json`. It must exist (the file is regenerated, per commit `e081a05e`), but it is not under `tool/n6_selftest*`. Possibly an external runner (engine/, hidden orchestrator, or shell-driven). This means the "tool that maintains it" claim in commit messages is unverified.
4. **own#21 regex literal-coupling**: the drift_pattern `tests:\s+(\d+)` couples lint to the literal label "tests:". A D4 relabel breaks the lint unless the pattern is updated in lockstep. Caller should decide whether to keep label "tests:" (compromise) or update the lint regex (strict).
5. **Predecessor reference is forward-dated**: the front-matter cites `canon_meta/doc/canon_own_readme_mk2_reconstruction_2026_05_04.ai.md` which was not directly verified in this investigation. If absent, the `predecessor_handoff` field should be revised before commit.
6. **No CI enforcement observed**: even after fixing drift, there is no mechanism preventing future TECS-L syncs from re-introducing a stale literal. Recommend adding own#21 to a pre-commit / pre-push hook gate.

## §7 Investigation provenance

- Files read: `README.md` (L1-80), `reports/n6_selftest.json` (full, 264 LoC), `tool/own_nexus6_tests_drift.hexa` (full, 257 LoC).
- Files listed: `scanners/` (54 files), `reports/history/2026-04-22/`, `reports/history/2026-04-23/`.
- Git probes: `log -S "1116"` (5 commits), `log -S '"total": 51'` (1 commit), per-commit show on `60dc7eea`, `2517fdec`, `e9c70049`, `fbb24a3e`, `e081a05e`.
- Counters: 4 independent ground-truth probes (scanner files 54; verdicts 51; .hexa test files 25; fn test_ defs 36).
- READ-ONLY: no modifications to README.md, reports/n6_selftest.json, scanners/, tool/own_nexus6_tests_drift.hexa, or any other source.
