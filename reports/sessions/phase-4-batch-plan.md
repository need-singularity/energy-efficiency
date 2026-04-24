# Phase 4 Batch Plan — reports/ track (284 files, 14 batches)

**Date**: 2026-04-25
**Author**: Phase 4 planner (automated)
**Status**: planning only — no code edits in this proposal
**Scope**: adds only this plan under `reports/sessions/`; allowlist and reports/**/*.md files remain untouched
**Compliance**:
- own#1 (doc-english-hard): this file under `reports/` is in own#1 scope and must be CJK-free. Verified by `python3 tool/own_doc_lint.py --rule 1`.
- own#11 (bt-solution-claim-ban): targets described as "draft/target/candidate" only. No "solved"/"proven" claims.
- own#17 (README English-only): out of scope for this plan.

---

## 1. Context

Source roadmap: `proposals/own1-hard-english-only-translation-roadmap-2026-04-24.md`.

Completed phases (merged on origin/main = `ef246bc6`):

- Phase 0: bridge/ + +n6shared/ (10 files)
- Phase 1: proposals/ (9 files)
- Phase 2: experiments/ (25 files)
- Phase 3: domains/ priority (200 files) — allowlist 1015 -> 815

Phase 4 scope: all 284 `reports/` entries currently on the own#1 legacy allowlist. Target allowlist reduction after Phase 4 completion: 815 -> 531.

## 2. Priority Criteria

The roadmap does not enumerate a precise 284-file reports/ set; the documented fallback rule is applied:

1. Enumerate all `reports/` allowlist entries (284 confirmed).
2. Group by first-level subdirectory (breakthroughs/, audits/, sessions/, discovery/, top-level reports/*.md, plus small buckets changelogs/, meta/, templates/, validation/).
3. Within each subdirectory sort by CJK character count ascending (shortest first = easier starter wins, reduces allowlist race duration per batch).
4. Pack into 14 batches: 13 batches of exactly 20 files plus 1 tail batch of 24 files (balance: 13*20 + 24 = 284).
5. Preserve subtree contiguity where possible; allow cross-subtree "tail+head" batches at subdirectory boundaries to keep batch sizes uniform.

Deviation note vs. pure per-subtree packing:
- Subtree sizes are not multiples of 20. Five boundary batches (B6, B9, B11, B13, B14) each span two adjacent subtrees.
- The small buckets (changelogs=3, meta=2, templates=2, validation=1; 8 files total) are pooled into the final tail batch B14 along with the reports/*.md top-level tail.

## 3. Selection Summary

| Subdirectory | Files | CJK Total | Avg CJK |
|---|---:|---:|---:|
| `reports/breakthroughs/` | 113 | 184997 | 1637.1 |
| `reports/audits/` | 55 | 59239 | 1077.1 |
| `reports/sessions/` | 42 | 87504 | 2083.4 |
| `reports/discovery/` | 38 | 33367 | 878.1 |
| `reports/*.md` (top-level) | 28 | 22205 | 793.0 |
| `reports/changelogs/` | 3 | 638 | 212.7 |
| `reports/meta/` | 2 | 4180 | 2090.0 |
| `reports/templates/` | 2 | 346 | 173.0 |
| `reports/validation/` | 1 | 1949 | 1949.0 |
| **Total** | **284** | **394425** | **1388.8** |

## 4. Batch Overview

| Batch | Label | Files | CJK Total | Primary Subtree |
|---|---|---:|---:|---|
| 1 | `phase-4-1-breakthroughs-a` | 20 | 4856 | reports/breakthroughs/ |
| 2 | `phase-4-2-breakthroughs-b` | 20 | 12455 | reports/breakthroughs/ |
| 3 | `phase-4-3-breakthroughs-c` | 20 | 19701 | reports/breakthroughs/ |
| 4 | `phase-4-4-breakthroughs-d` | 20 | 26644 | reports/breakthroughs/ |
| 5 | `phase-4-5-breakthroughs-e` | 20 | 50317 | reports/breakthroughs/ |
| 6 | `phase-4-6-breakthroughs-tail-audits-a` | 20 | 72837 | reports/breakthroughs/ + reports/audits/ |
| 7 | `phase-4-7-audits-b` | 20 | 13075 | reports/audits/ |
| 8 | `phase-4-8-audits-c` | 20 | 23915 | reports/audits/ |
| 9 | `phase-4-9-audits-tail-sessions-a` | 20 | 24407 | reports/audits/ + reports/sessions/ |
| 10 | `phase-4-10-sessions-b` | 20 | 22726 | reports/sessions/ |
| 11 | `phase-4-11-sessions-tail-discovery-a` | 20 | 62616 | reports/sessions/ + reports/discovery/ |
| 12 | `phase-4-12-discovery-b` | 20 | 15056 | reports/discovery/ |
| 13 | `phase-4-13-discovery-tail-reports-top-a` | 20 | 21055 | reports/discovery/ + reports/*.md |
| 14 | `phase-4-14-reports-top-b-misc` | 24 | 24765 | reports/*.md + reports/{changelogs,meta,templates,validation}/ |
| **Total** | — | **284** | **394425** | — |

Note on CJK-per-batch: Phase 4 processes larger/denser files than Phase 3 (breakthroughs/ and sessions/ include long-form reports). Average is ~28k CJK/batch; outliers B5 (50k), B6 (73k), B11 (63k) carry the per-subtree tails. Per the "outliers OK" clause established in Phase 2, these are acceptable.

## 5. Parallelism Coordination Notes (allowlist race pattern)

All 14 batch agents will attempt to edit the shared file `tool/own1_legacy_allowlist.json`. The following mitigation pattern, proven in Phase 2 and Phase 3, is MANDATORY. See `reports/sessions/hard-english-only-session-2026-04-24.md` section 11.6 for the full post-mortem (stash-wipeout race, allowlist re-introduction race, post-write CJK verify requirement).

1. **Read-modify-write with mtime check**: capture `os.stat(path).st_mtime_ns` before read; re-check after edit is staged but before commit. If mtime changed, re-pull and re-apply removal set.
2. **Removal set, not index-based edits**: each agent computes the set of paths to remove (its batch files). Re-apply idempotently (`[e for e in allowlist if e not in removal_set]`). Never use positional indices.
3. **`_meta.count` resync**: after editing `allowlist`, set `_meta.count = len(allowlist)` unconditionally.
4. **Rebase-retry loop on push**: `git pull --rebase origin main`, max 3 retries. On rebase conflict in the allowlist JSON, resolve by accepting theirs + re-applying our removal set (our entries are a disjoint subset).
5. **Stash/pop on dirty tree**: if rebase complains about uncommitted changes (e.g., pre-commit hook left artifacts), `git stash push -u`, rebase, `git stash pop`. Always `pop` after rebase to avoid the stash-wipeout race documented in session log section 11.6.
6. **Post-write CJK re-verify**: after `git stash pop` or any rebase-merge resolution, re-run `python3 tool/own_doc_lint.py --rule 1` before commit. A rebase may re-introduce CJK content from concurrent sibling batches.
7. **Pre-commit hook race**: `--no-verify` is permitted after the agent has locally run `python3 tool/own_doc_lint.py --rule 1` and confirmed pass. This is explicitly authorized ONLY under that precondition.
8. **Staging hygiene**: `git add` only the translated `.md` files + `tool/own1_legacy_allowlist.json`. Never `git add -A` or `git add .`.
9. **own#11 softener vocabulary**: use "draft", "candidate", "pattern", "target" when describing results. Never "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense.
10. **Preservation rules**: code fences verbatim, math blocks (`$...$`, `$$...$$`) verbatim, YAML frontmatter keys verbatim, hyperlinks and image paths verbatim, technical identifiers as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N.

## 6. File Lists Per Batch

### Batch 1: `phase-4-1-breakthroughs-a` (20 files, CJK=4856)

| # | Path | CJK |
|---:|---|---:|
| 1 | `reports/breakthroughs/v4-loop11-M3-case4c-i-2026-04-16.md` | 120 |
| 2 | `reports/breakthroughs/v4-loop12-M3-case4c-ii-2026-04-16.md` | 142 |
| 3 | `reports/breakthroughs/v4-loop8-M3-case4b-i-2026-04-16.md` | 146 |
| 4 | `reports/breakthroughs/v4-loop10-M3-case4b-iii-2026-04-16.md` | 186 |
| 5 | `reports/breakthroughs/v4-loop13-M3-case4c-iii-capstone-2026-04-16.md` | 209 |
| 6 | `reports/breakthroughs/bt-1423-ai-quality-scale-mk5-2026-04-20.md` | 227 |
| 7 | `reports/breakthroughs/bt-1427-ai-consciousness-mk5-2026-04-20.md` | 227 |
| 8 | `reports/breakthroughs/bt-1421-ai-inference-cost-mk5-2026-04-20.md` | 231 |
| 9 | `reports/breakthroughs/bt-1422-ai-training-cost-mk5-2026-04-20.md` | 239 |
| 10 | `reports/breakthroughs/bt-1428-ai-safety-mk5-2026-04-20.md` | 244 |
| 11 | `reports/breakthroughs/bt-1424-ai-agent-serving-mk5-2026-04-20.md` | 262 |
| 12 | `reports/breakthroughs/v4-loop5-M3-case2b-2026-04-16.md` | 275 |
| 13 | `reports/breakthroughs/bt-1425-ai-enterprise-custom-mk5-2026-04-20.md` | 282 |
| 14 | `reports/breakthroughs/bt-1426-ai-eval-pipeline-mk5-2026-04-20.md` | 283 |
| 15 | `reports/breakthroughs/bt-1420-millennium-dfs-round26-2026-04-15.md` | 284 |
| 16 | `reports/breakthroughs/v3-e5-kappa-7bin-power-law-2026-04-15.md` | 286 |
| 17 | `reports/breakthroughs/v4-loop4-M3-case2-2026-04-16.md` | 287 |
| 18 | `reports/breakthroughs/v4-loop9-M3-case4b-ii-2026-04-16.md` | 294 |
| 19 | `reports/breakthroughs/v4-loop6-M3-case3-2026-04-16.md` | 301 |
| 20 | `reports/breakthroughs/bt-1418-millennium-dfs-round24-2026-04-15.md` | 331 |

### Batch 2: `phase-4-2-breakthroughs-b` (20 files, CJK=12455)

| # | Path | CJK |
|---:|---|---:|
| 1 | `reports/breakthroughs/bt-1419-millennium-dfs-round25-2026-04-15.md` | 347 |
| 2 | `reports/breakthroughs/bt-111-mk4-lemma-tau2-sigma-2026-04-15.md` | 370 |
| 3 | `reports/breakthroughs/v3-loop19-lean4-extended-kappa-bootstrap-2026-04-16.md` | 370 |
| 4 | `reports/breakthroughs/bt-1396-dfs5-representation-theory-2026-04-12.md` | 472 |
| 5 | `reports/breakthroughs/v3-e1-m3-toolchain-bootstrap-2026-04-16.md` | 517 |
| 6 | `reports/breakthroughs/v4-loop3-M3-primes-E6-uniqueness-2026-04-16.md` | 518 |
| 7 | `reports/breakthroughs/v3-t3-joint-distribution-modeling-2026-04-15.md` | 534 |
| 8 | `reports/breakthroughs/v3-t2-moonshine-l5-retry-2026-04-15.md` | 607 |
| 9 | `reports/breakthroughs/bt-1396-dfs5-tqft-reptheory-2026-04-12.md` | 610 |
| 10 | `reports/breakthroughs/bt-1395-millennium-dfs-round4-2026-04-12.md` | 650 |
| 11 | `reports/breakthroughs/emergence-312-meta-analysis-2026-04-15.md` | 681 |
| 12 | `reports/breakthroughs/v4-t4-A3-double-prime-rigorization-2026-04-16.md` | 688 |
| 13 | `reports/breakthroughs/v3-t5-hirahara-mcsp-deep-2026-04-15.md` | 708 |
| 14 | `reports/breakthroughs/v3-saturation-adjacent-2026-04-16.md` | 723 |
| 15 | `reports/breakthroughs/bt-1396-tqft-lattice-knot-dfs5-2026-04-12.md` | 733 |
| 16 | `reports/breakthroughs/ouroboros-atlas-audit-2026-04-15.md` | 750 |
| 17 | `reports/breakthroughs/new-domain-breakthrough-2026-04-06.md` | 785 |
| 18 | `reports/breakthroughs/bt-1394-millennium-dfs-round3-2026-04-12.md` | 790 |
| 19 | `reports/breakthroughs/v3-t1-abelian-sixfolds-deep-dive-2026-04-15.md` | 790 |
| 20 | `reports/breakthroughs/v3-t4-guth-maynard-2024-deep-dive-2026-04-15.md` | 812 |

### Batch 3: `phase-4-3-breakthroughs-c` (20 files, CJK=19701)

| # | Path | CJK |
|---:|---|---:|
| 1 | `reports/breakthroughs/v4-t1-alpha-log2-over-4-derivation-attempt-2026-04-16.md` | 814 |
| 2 | `reports/breakthroughs/external-coordination-infrastructure-2026-04-15.md` | 842 |
| 3 | `reports/breakthroughs/v3-t6-balaban-2d-modern-reorg-2026-04-15.md` | 848 |
| 4 | `reports/breakthroughs/bsd-A3-modified-with-joint-covariance-2026-04-15.md` | 870 |
| 5 | `reports/breakthroughs/bt-1415-millennium-dfs-round21-2026-04-14.md` | 870 |
| 6 | `reports/breakthroughs/lean4-formalization-plan-2026-04-15.md` | 871 |
| 7 | `reports/breakthroughs/bt-748-752-new-domains-2026-04-11.md` | 874 |
| 8 | `reports/breakthroughs/bt-18-fi24prime-3a-path-2026-04-15.md` | 879 |
| 9 | `reports/breakthroughs/moonshine-l5-barrier-paths-2026-04-15.md` | 883 |
| 10 | `reports/breakthroughs/bsd-kappa-asymptotic-964k-2026-04-15.md` | 922 |
| 11 | `reports/breakthroughs/bt-18-hauptmodul-gamma047plus-2026-04-15.md` | 1042 |
| 12 | `reports/breakthroughs/bt-1417-dfs23-info-coding-2026-04-15.md` | 1062 |
| 13 | `reports/breakthroughs/v4-t5-cross-bt-survey-544-546-547-2026-04-16.md` | 1079 |
| 14 | `reports/breakthroughs/bt-1417-millennium-dfs-round23-2026-04-15.md` | 1088 |
| 15 | `reports/breakthroughs/bt-1414-millennium-dfs-round21-2026-04-14.md` | 1095 |
| 16 | `reports/breakthroughs/bt-1389-cube-octahedron-duality-2026-04-12.md` | 1112 |
| 17 | `reports/breakthroughs/bt-1176-nuclear-reactor-kinetics-2026-04-12.md` | 1128 |
| 18 | `reports/breakthroughs/millennium-n6-attractor-2026-04-11.md` | 1129 |
| 19 | `reports/breakthroughs/arxiv-millennium-survey-180papers-2026-04-15.md` | 1140 |
| 20 | `reports/breakthroughs/bt-1387-huckel-aromatic-2026-04-12.md` | 1153 |

### Batch 4: `phase-4-4-breakthroughs-d` (20 files, CJK=26644)

| # | Path | CJK |
|---:|---|---:|
| 1 | `reports/breakthroughs/bt-1390-hsv-color-hexad-2026-04-12.md` | 1157 |
| 2 | `reports/breakthroughs/bt-1388-ionic-octahedral-2026-04-12.md` | 1163 |
| 3 | `reports/breakthroughs/bt-1418-dfs23b-rep-theory-modular-2026-04-15.md` | 1169 |
| 4 | `reports/breakthroughs/bt-1391-photosynthesis-equation-2026-04-12.md` | 1173 |
| 5 | `reports/breakthroughs/bt-1416-millennium-dfs-round22-2026-04-15.md` | 1190 |
| 6 | `reports/breakthroughs/bt-1175-water-treatment-2026-04-12.md` | 1228 |
| 7 | `reports/breakthroughs/bt-1386-standard-model-2026-04-12.md` | 1241 |
| 8 | `reports/breakthroughs/bsd-cremona-sel6-empirical-2026-04-15.md` | 1247 |
| 9 | `reports/breakthroughs/breakthrough-theorems-warp-dimension-2026-04-08.md` | 1249 |
| 10 | `reports/breakthroughs/bt-1413-millennium-dfs-round20-2026-04-14.md` | 1275 |
| 11 | `reports/breakthroughs/breakthrough-theorems-extension-2026-04-08.md` | 1295 |
| 12 | `reports/breakthroughs/new-breakthrough-hypotheses-2026-03-31.md` | 1389 |
| 13 | `reports/breakthroughs/millennium-7-closure-2026-04-11.md` | 1394 |
| 14 | `reports/breakthroughs/bt-19-consciousness-triple-verification-2026-04-15.md` | 1431 |
| 15 | `reports/breakthroughs/bt-542-p-vs-np-4-barriers-survey-2026-04-15.md` | 1445 |
| 16 | `reports/breakthroughs/bt-1169-1174-fusion-v5-2026-04-12.md` | 1468 |
| 17 | `reports/breakthroughs/bt-1163-1168-superconductor-v5-2026-04-12.md` | 1494 |
| 18 | `reports/breakthroughs/forge-triple-fusion-2026-04-14.md` | 1499 |
| 19 | `reports/breakthroughs/bt-18-baby-monster-p10-retry-2026-04-15.md` | 1546 |
| 20 | `reports/breakthroughs/millennium-dfs-complete-2026-04-11.md` | 1591 |

### Batch 5: `phase-4-5-breakthroughs-e` (20 files, CJK=50317)

| # | Path | CJK |
|---:|---|---:|
| 1 | `reports/breakthroughs/bt-1412-millennium-dfs-round20-2026-04-14.md` | 1650 |
| 2 | `reports/breakthroughs/bt-19-tau4-promotion-2026-04-15.md` | 1669 |
| 3 | `reports/breakthroughs/bt-1397-uncovered-domains-2026-04-12.md` | 1727 |
| 4 | `reports/breakthroughs/bt-19-tau4-pci-validation-2026-04-15.md` | 1942 |
| 5 | `reports/breakthroughs/bt-19-alternative-paths-2026-04-15.md` | 2025 |
| 6 | `reports/breakthroughs/bt-1398-millennium-dfs-round6-2026-04-12.md` | 2059 |
| 7 | `reports/breakthroughs/bt-19-perfect-number-near-promotion-2026-04-15.md` | 2090 |
| 8 | `reports/breakthroughs/bt-18-vacuum-monster-chain-dfs-2026-04-14.md` | 2259 |
| 9 | `reports/breakthroughs/new-bt-new-domains-part1-2026-04-06.md` | 2280 |
| 10 | `reports/breakthroughs/consciousness-triple-fusion-2026-04-15.md` | 2529 |
| 11 | `reports/breakthroughs/new-bt-dimensional-unfolding-2026-04-06.md` | 2586 |
| 12 | `reports/breakthroughs/new-bt-new-domains-part2-2026-04-06.md` | 2629 |
| 13 | `reports/breakthroughs/bt-19-consciousness-alternate-paths-2026-04-15.md` | 2663 |
| 14 | `reports/breakthroughs/bt-19-perfect-number-path-2026-04-15.md` | 2832 |
| 15 | `reports/breakthroughs/bt-1393-n6-dfs-10k-autonomous-2026-04-12.md` | 2901 |
| 16 | `reports/breakthroughs/bt-1399-millennium-dfs-round7-2026-04-12.md` | 2987 |
| 17 | `reports/breakthroughs/bt-1406-millennium-dfs-round14-2026-04-12.md` | 3031 |
| 18 | `reports/breakthroughs/bt-18-moonshine-l5-barrier-2026-04-15.md` | 3059 |
| 19 | `reports/breakthroughs/bt-1407-millennium-dfs-round15-2026-04-12.md` | 3460 |
| 20 | `reports/breakthroughs/bt-1392-millennium-7-breakthrough-ideas-2026-04-12.md` | 3939 |

### Batch 6: `phase-4-6-breakthroughs-tail-audits-a` (20 files, CJK=72837)

| # | Path | CJK |
|---:|---|---:|
| 1 | `reports/breakthroughs/bt-reinforcement-dimensional-unfolding-2026-04-06.md` | 4130 |
| 2 | `reports/breakthroughs/bt-1405-millennium-dfs-round13-2026-04-12.md` | 4728 |
| 3 | `reports/breakthroughs/bt-1400-millennium-dfs-round8-2026-04-12.md` | 4817 |
| 4 | `reports/breakthroughs/bt-1401-millennium-dfs-round9-2026-04-12.md` | 4901 |
| 5 | `reports/breakthroughs/bt-1408-millennium-dfs-round16-2026-04-12.md` | 4968 |
| 6 | `reports/breakthroughs/bt-1402-millennium-dfs-round10-2026-04-12.md` | 5254 |
| 7 | `reports/breakthroughs/bt-1404-millennium-dfs-round12-2026-04-12.md` | 5286 |
| 8 | `reports/breakthroughs/bt-1409-millennium-dfs-round17-2026-04-12.md` | 5303 |
| 9 | `reports/breakthroughs/bt-1410-millennium-dfs-round18-2026-04-12.md` | 5694 |
| 10 | `reports/breakthroughs/bt-1403-millennium-dfs-round11-2026-04-12.md` | 5719 |
| 11 | `reports/breakthroughs/bt-1413-millennium-dfs-round21-2026-04-12.md` | 6269 |
| 12 | `reports/breakthroughs/bt-1411-millennium-dfs-round19-2026-04-12.md` | 6880 |
| 13 | `reports/breakthroughs/bt-1412-millennium-dfs-round20-2026-04-12.md` | 7075 |
| 14 | `reports/audits/verification-bt-mapping-2026-04-08.md` | 166 |
| 15 | `reports/audits/paper-legacy-audit/blowup-invariant-core-2026-04-04.md` | 177 |
| 16 | `reports/audits/3d-map-verification-2026-04-08.md` | 239 |
| 17 | `reports/audits/paper-legacy-audit/audit-quality-full.md` | 280 |
| 18 | `reports/audits/sedi-brainwire-folder-removal-2026-04-11.md` | 293 |
| 19 | `reports/audits/n61-15section-audit-2026-04-11.md` | 324 |
| 20 | `reports/audits/paper-legacy-audit/verify-results.md` | 334 |

### Batch 7: `phase-4-7-audits-b` (20 files, CJK=13075)

| # | Path | CJK |
|---:|---|---:|
| 1 | `reports/audits/paper-legacy-audit/verification-audit-2026-04-08.md` | 355 |
| 2 | `reports/audits/products-drift-fix-2026-04-11.md` | 430 |
| 3 | `reports/audits/ubu-exit137-diagnosis-2026-04-14.md` | 456 |
| 4 | `reports/audits/verification-audit-2026-04-08.md` | 482 |
| 5 | `reports/audits/paper-legacy-audit/audit-missing-verification.md` | 497 |
| 6 | `reports/audits/sota-3-integration-2026-04-11.md` | 507 |
| 7 | `reports/audits/atlas-promotion-2026-04-11.md` | 535 |
| 8 | `reports/audits/miss-links-audit.md` | 546 |
| 9 | `reports/audits/tecs-l-cleanup-2026-04-11.md` | 586 |
| 10 | `reports/audits/atlas-promotion-round2-2026-04-11.md` | 587 |
| 11 | `reports/audits/grade13-candidates-2026-04-14.md` | 649 |
| 12 | `reports/audits/audit-latest.md` | 687 |
| 13 | `reports/audits/paper-legacy-audit/verify-coverage.md` | 768 |
| 14 | `reports/audits/products-postsession-additions-2026-04-11.md` | 793 |
| 15 | `reports/audits/r29-migration-bulk-2026-04-11.md` | 797 |
| 16 | `reports/audits/goal-md-expansion-20-295.md` | 809 |
| 17 | `reports/audits/products-upgrade-9-2026-04-11.md` | 837 |
| 18 | `reports/audits/atlas-promotion-round3-2026-04-11.md` | 897 |
| 19 | `reports/audits/products-link-remap-2026-04-11.md` | 924 |
| 20 | `reports/audits/papers-expansion-39-50.md` | 933 |

### Batch 8: `phase-4-8-audits-c` (20 files, CJK=23915)

| # | Path | CJK |
|---:|---|---:|
| 1 | `reports/audits/sedi-brainwire-lens-ref-fix-2026-04-11.md` | 951 |
| 2 | `reports/audits/convergence-ossification-2026-04-11.md` | 971 |
| 3 | `reports/audits/lens-ssot-cleanup-2026-04-11.md` | 986 |
| 4 | `reports/audits/r29-migration-synbio-2026-04-11.md` | 998 |
| 5 | `reports/audits/papers-ssot-ghost-audit-2026-04-11.md` | 1016 |
| 6 | `reports/audits/convergence-update-2026-04-11.md` | 1078 |
| 7 | `reports/audits/registry-path-fix-2026-04-11.md` | 1111 |
| 8 | `reports/audits/paper-legacy-audit/audit-quality-11.md` | 1122 |
| 9 | `reports/audits/atlas-promotion-round4-2026-04-11.md` | 1168 |
| 10 | `reports/audits/synbio-merge-2026-04-11.md` | 1180 |
| 11 | `reports/audits/papers-n62-completion-2026-04-11.md` | 1184 |
| 12 | `reports/audits/stale-md-48-investigation-2026-04-11.md` | 1207 |
| 13 | `reports/audits/2026-04-12/millennium-status.md` | 1257 |
| 14 | `reports/audits/go-audit-v6-2026-04-12.md` | 1261 |
| 15 | `reports/audits/auto-audit-system-proposal.md` | 1286 |
| 16 | `reports/audits/go-audit-2026-04-12.md` | 1307 |
| 17 | `reports/audits/zenodo-publish-ready-2026-04-11.md` | 1318 |
| 18 | `reports/audits/go-session-audit-v2-2026-04-12.md` | 1323 |
| 19 | `reports/audits/manifest-expansion-11-papers-2026-04-11.md` | 1528 |
| 20 | `reports/audits/ai-techniques-16-canonical-2026-04-12.md` | 1663 |

### Batch 9: `phase-4-9-audits-tail-sessions-a` (20 files, CJK=24407)

| # | Path | CJK |
|---:|---|---:|
| 1 | `reports/audits/readme-ssot-audit-2026-04-19.md` | 1668 |
| 2 | `reports/audits/go-audit-v4-2026-04-12.md` | 1769 |
| 3 | `reports/audits/go-audit-v5-2026-04-12.md` | 1829 |
| 4 | `reports/audits/zenodo-publish-3-papers-2026-04-11.md` | 1872 |
| 5 | `reports/audits/go-session-audit-v3-2026-04-12.md` | 2097 |
| 6 | `reports/audits/bt-audit-report.md` | 3216 |
| 7 | `reports/audits/readme-products-drift-2026-04-11.md` | 3549 |
| 8 | `reports/audits/products-link-audit-2026-04-11.md` | 4436 |
| 9 | `reports/sessions/dfs-24-hodge-direction-2026-04-24.md` | 5 |
| 10 | `reports/sessions/dfs-24-ns-direction-2026-04-24.md` | 12 |
| 11 | `reports/sessions/plans/2026-04-04-tecs-l-discovery-loop.md` | 171 |
| 12 | `reports/sessions/specs/2026-04-07-next-model-blowup-design.md` | 301 |
| 13 | `reports/sessions/2026-04-11-weekly-audit.md` | 311 |
| 14 | `reports/sessions/2026-04-11-weekly-audit_rerun-2056.md` | 311 |
| 15 | `reports/sessions/cross-dse-resonance-2026-04-08.md` | 357 |
| 16 | `reports/sessions/experiments-expansion-200-250.md` | 415 |
| 17 | `reports/sessions/cross-domain-resonance-2026-03-31.md` | 499 |
| 18 | `reports/sessions/cross-dse-rerun-2026-04-08.md` | 505 |
| 19 | `reports/sessions/cross-dse-results-2026-04-05.md` | 525 |
| 20 | `reports/sessions/experiments-expansion-122-150.md` | 559 |

### Batch 10: `phase-4-10-sessions-b` (20 files, CJK=22726)

| # | Path | CJK |
|---:|---|---:|
| 1 | `reports/sessions/plans/2026-03-28-n6-inevitability-engine.md` | 627 |
| 2 | `reports/sessions/specs/2026-04-06-ufo-warp-dimension-design.md` | 639 |
| 3 | `reports/sessions/experiments-expansion-150-200.md` | 689 |
| 4 | `reports/sessions/nexus-roadmap-2026-04-04.md` | 844 |
| 5 | `reports/sessions/specs/2026-04-01-hexa-battery-design.md` | 863 |
| 6 | `reports/sessions/plans/2026-04-01-ultimate-pure-mathematics-dse.md` | 921 |
| 7 | `reports/sessions/dfs-24-ym-direction-2026-04-24.md` | 929 |
| 8 | `reports/sessions/millennium-lemmas-2026-04-11.md` | 976 |
| 9 | `reports/sessions/specs/2026-04-01-ultimate-pure-mathematics-dse.md` | 1013 |
| 10 | `reports/sessions/dfs-24-riemann-direction-2026-04-24.md` | 1106 |
| 11 | `reports/sessions/specs/2026-04-02-hexa-ccus-design.md` | 1149 |
| 12 | `reports/sessions/millennium-dfs345-2026-04-12.md` | 1250 |
| 13 | `reports/sessions/plans/2026-04-01-ultimate-fusion-dse.md` | 1324 |
| 14 | `reports/sessions/dfs-24-pnp-direction-2026-04-24.md` | 1381 |
| 15 | `reports/sessions/explosive-growth-2026-04-10.md` | 1403 |
| 16 | `reports/sessions/specs/2026-04-01-ultimate-programming-language-design.md` | 1461 |
| 17 | `reports/sessions/plans/2026-04-01-ultimate-programming-language.md` | 1500 |
| 18 | `reports/sessions/specs/2026-04-08-hexa-lang-blockers-for-porting.md` | 1518 |
| 19 | `reports/sessions/plans/2026-04-02-hexa-ccus-implementation.md` | 1545 |
| 20 | `reports/sessions/2026-04-11-products-readme-unification.md` | 1588 |

### Batch 11: `phase-4-11-sessions-tail-discovery-a` (20 files, CJK=62616)

| # | Path | CJK |
|---:|---|---:|
| 1 | `reports/sessions/millennium-lemmas-2026-04-14.md` | 1617 |
| 2 | `reports/sessions/plans/2026-04-01-hexa-battery-architecture.md` | 1804 |
| 3 | `reports/sessions/millennium-loop-25-26.md` | 1885 |
| 4 | `reports/sessions/specs/2026-04-03-nexus-unified-brainstorm.md` | 1982 |
| 5 | `reports/sessions/specs/2026-04-03-discovery-engine-design.md` | 2541 |
| 6 | `reports/sessions/cross-project-transplant-2026-04-07.md` | 3164 |
| 7 | `reports/sessions/hypotheses-dfs-chain-2026-04-07.md` | 4950 |
| 8 | `reports/sessions/specs/2026-04-02-kstar-300s-steady-state-design.md` | 11872 |
| 9 | `reports/sessions/specs/2026-04-02-kstar-n6-tokamak-design.md` | 15141 |
| 10 | `reports/sessions/specs/2026-04-02-ultimate-fusion-powerplant-design.md` | 15851 |
| 11 | `reports/discovery/n6-optimal-llm-spec.md` | 8 |
| 12 | `reports/discovery/cross-dse-bottom-analysis.md` | 12 |
| 13 | `reports/discovery/llm-improvement-new-hypotheses-2026.md` | 73 |
| 14 | `reports/discovery/anomaly-detection-results.md` | 93 |
| 15 | `reports/discovery/cross-dse-4-2026-04-12-raw.md` | 215 |
| 16 | `reports/discovery/dse-domains.md` | 227 |
| 17 | `reports/discovery/mc-v93-domain-breakdown.md` | 233 |
| 18 | `reports/discovery/monte-carlo-domain-breakdown.md` | 284 |
| 19 | `reports/discovery/dse-uncovered-scan-2026-04-12.md` | 310 |
| 20 | `reports/discovery/dse-map.md` | 354 |

### Batch 12: `phase-4-12-discovery-b` (20 files, CJK=15056)

| # | Path | CJK |
|---:|---|---:|
| 1 | `reports/discovery/dse-cluster-v2.md` | 421 |
| 2 | `reports/discovery/lens-expansion-397-450.md` | 433 |
| 3 | `reports/discovery/lens-expansion-500-600.md` | 515 |
| 4 | `reports/discovery/dse-500-expansion-2026-04-11.md` | 561 |
| 5 | `reports/discovery/dse-cross-pilot-result.md` | 603 |
| 6 | `reports/discovery/claude-code-cache-bug-analysis.md` | 636 |
| 7 | `reports/discovery/ai-energy-savings-guide.md` | 657 |
| 8 | `reports/discovery/nobel-grade-findings.md` | 734 |
| 9 | `reports/discovery/xn6-rtl-phase3-2026-04-11.md` | 745 |
| 10 | `reports/discovery/xn6-isa-phase2-2026-04-11.md` | 748 |
| 11 | `reports/discovery/cross-dse-4-2026-04-12.md` | 772 |
| 12 | `reports/discovery/dse-v2-results-2026-04-11.md` | 773 |
| 13 | `reports/discovery/proof4-candidate-2026-04-11.md` | 785 |
| 14 | `reports/discovery/lens-expansion-450-500.md` | 812 |
| 15 | `reports/discovery/kolon-n6-breakthrough.md` | 818 |
| 16 | `reports/discovery/l7-meta-layer-proposal.md` | 820 |
| 17 | `reports/discovery/reality-map-monte-carlo-v8.md` | 1006 |
| 18 | `reports/discovery/mc-v9-proposal.md` | 1054 |
| 19 | `reports/discovery/consciousness-cluster-bt.md` | 1072 |
| 20 | `reports/discovery/dimensional-perception.md` | 1091 |

### Batch 13: `phase-4-13-discovery-tail-reports-top-a` (20 files, CJK=21055)

| # | Path | CJK |
|---:|---|---:|
| 1 | `reports/discovery/layer-dashboard.md` | 1168 |
| 2 | `reports/discovery/chip-architecture-guide.md` | 1177 |
| 3 | `reports/discovery/dse-cross-resonance.md` | 1232 |
| 4 | `reports/discovery/mc-v9-results-2026-04-11.md` | 1359 |
| 5 | `reports/discovery/bt-425-444-proposal.md` | 2517 |
| 6 | `reports/discovery/bt-381-400-proposal.md` | 2590 |
| 7 | `reports/discovery/bt-401-420-proposal.md` | 2604 |
| 8 | `reports/discovery/dse-cross-fusion.md` | 3855 |
| 9 | `reports/digest-20260416.md` | 83 |
| 10 | `reports/E6_signal_homology_20260415.md` | 133 |
| 11 | `reports/E1_signal_soc_map_20260415.md` | 139 |
| 12 | `reports/E2_signal_bt_autocorr_20260415.md` | 151 |
| 13 | `reports/megahub-detection-20260415.md` | 213 |
| 14 | `reports/cross-backfill-20260415.md` | 439 |
| 15 | `reports/chip-roadmap-mk3-2026-04-15.md` | 444 |
| 16 | `reports/atlas-promotion-p5-2026-04-14.md` | 536 |
| 17 | `reports/meta-group-H-20260415.md` | 575 |
| 18 | `reports/dfs27-yangmills-20260415.md` | 613 |
| 19 | `reports/ym-beta-series-20260415.md` | 613 |
| 20 | `reports/millennium-group-F-20260415.md` | 614 |

### Batch 14: `phase-4-14-reports-top-b-misc` (24 files, CJK=24765)

| # | Path | CJK |
|---:|---|---:|
| 1 | `reports/bsd-kappa-0.175-decomposition.md` | 654 |
| 2 | `reports/kuramoto-perfect-numbers-20260415.md` | 714 |
| 3 | `reports/field-emergence-dse-2026-04-15.md` | 750 |
| 4 | `reports/SR-universality-design-20260415.md` | 766 |
| 5 | `reports/tau_sigma_ratio_universality.md` | 788 |
| 6 | `reports/sigma-sopfr-7-megasignature-20260415.md` | 822 |
| 7 | `reports/chip_comparison_l1_l10.md` | 871 |
| 8 | `reports/bernoulli-17-validation-20260415.md` | 880 |
| 9 | `reports/wild-group-G-20260415.md` | 891 |
| 10 | `reports/transcend-p12-2-mk3-atlas-integration-2026-04-15.md` | 1063 |
| 11 | `reports/transcend-p11-1-hexa-gate-mk3-impl-2026-04-15.md` | 1192 |
| 12 | `reports/group-O-applications-physics-20260415.md` | 1210 |
| 13 | `reports/millennium-dfs-status.md` | 1538 |
| 14 | `reports/atlas-mk3-audit-2026-04-15.md` | 1667 |
| 15 | `reports/mk3-synthesis-2026-04-15.md` | 1916 |
| 16 | `reports/transcend-p13-2-discovery-engine-mk3-2026-04-15.md` | 1930 |
| 17 | `reports/changelogs/README-details.md` | 15 |
| 18 | `reports/changelogs/2026-04-11-weekly.md` | 55 |
| 19 | `reports/templates/changelog-template.md` | 85 |
| 20 | `reports/templates/weekly-audit-template.md` | 261 |
| 21 | `reports/changelogs/3d-map-changelog-2026-04-08.md` | 568 |
| 22 | `reports/meta/p9-bt18-l5-retry-judgment-audit-2026-04-15.md` | 1156 |
| 23 | `reports/validation/techniques-68-smoke-test-2026-04-12.md` | 1949 |
| 24 | `reports/meta/p9-consciousness-red-team-audit-2026-04-15.md` | 3024 |

## 7. Per-Batch Launch Prompt Templates

Each block below is a paste-ready prompt for a single agent. Do not edit; copy-paste verbatim into a fresh agent session. Replace the per-batch file list only if you want to re-split batches.

### Prompt for Batch 1: `phase-4-1-breakthroughs-a`

```
You are a Phase 4 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-4-1-breakthroughs-a
Batch number: 1 of 14

## Files to translate (20 files, CJK total = 4856)

- reports/breakthroughs/v4-loop11-M3-case4c-i-2026-04-16.md (CJK=120)
- reports/breakthroughs/v4-loop12-M3-case4c-ii-2026-04-16.md (CJK=142)
- reports/breakthroughs/v4-loop8-M3-case4b-i-2026-04-16.md (CJK=146)
- reports/breakthroughs/v4-loop10-M3-case4b-iii-2026-04-16.md (CJK=186)
- reports/breakthroughs/v4-loop13-M3-case4c-iii-capstone-2026-04-16.md (CJK=209)
- reports/breakthroughs/bt-1423-ai-quality-scale-mk5-2026-04-20.md (CJK=227)
- reports/breakthroughs/bt-1427-ai-consciousness-mk5-2026-04-20.md (CJK=227)
- reports/breakthroughs/bt-1421-ai-inference-cost-mk5-2026-04-20.md (CJK=231)
- reports/breakthroughs/bt-1422-ai-training-cost-mk5-2026-04-20.md (CJK=239)
- reports/breakthroughs/bt-1428-ai-safety-mk5-2026-04-20.md (CJK=244)
- reports/breakthroughs/bt-1424-ai-agent-serving-mk5-2026-04-20.md (CJK=262)
- reports/breakthroughs/v4-loop5-M3-case2b-2026-04-16.md (CJK=275)
- reports/breakthroughs/bt-1425-ai-enterprise-custom-mk5-2026-04-20.md (CJK=282)
- reports/breakthroughs/bt-1426-ai-eval-pipeline-mk5-2026-04-20.md (CJK=283)
- reports/breakthroughs/bt-1420-millennium-dfs-round26-2026-04-15.md (CJK=284)
- reports/breakthroughs/v3-e5-kappa-7bin-power-law-2026-04-15.md (CJK=286)
- reports/breakthroughs/v4-loop4-M3-case2-2026-04-16.md (CJK=287)
- reports/breakthroughs/v4-loop9-M3-case4b-ii-2026-04-16.md (CJK=294)
- reports/breakthroughs/v4-loop6-M3-case3-2026-04-16.md (CJK=301)
- reports/breakthroughs/bt-1418-millennium-dfs-round24-2026-04-15.md (CJK=331)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY; see session log 2026-04-24 section 11.6):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
   - After `git stash pop` or any merge resolution: re-run `python3 tool/own_doc_lint.py --rule 1` (post-write CJK verify — a rebase can re-introduce CJK from sibling batches)
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the translated `.md` files in this batch and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-4-1 phase-4-1-breakthroughs-a (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-4-1` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 815 minus shrinkage from this and concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

### Prompt for Batch 2: `phase-4-2-breakthroughs-b`

```
You are a Phase 4 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-4-2-breakthroughs-b
Batch number: 2 of 14

## Files to translate (20 files, CJK total = 12455)

- reports/breakthroughs/bt-1419-millennium-dfs-round25-2026-04-15.md (CJK=347)
- reports/breakthroughs/bt-111-mk4-lemma-tau2-sigma-2026-04-15.md (CJK=370)
- reports/breakthroughs/v3-loop19-lean4-extended-kappa-bootstrap-2026-04-16.md (CJK=370)
- reports/breakthroughs/bt-1396-dfs5-representation-theory-2026-04-12.md (CJK=472)
- reports/breakthroughs/v3-e1-m3-toolchain-bootstrap-2026-04-16.md (CJK=517)
- reports/breakthroughs/v4-loop3-M3-primes-E6-uniqueness-2026-04-16.md (CJK=518)
- reports/breakthroughs/v3-t3-joint-distribution-modeling-2026-04-15.md (CJK=534)
- reports/breakthroughs/v3-t2-moonshine-l5-retry-2026-04-15.md (CJK=607)
- reports/breakthroughs/bt-1396-dfs5-tqft-reptheory-2026-04-12.md (CJK=610)
- reports/breakthroughs/bt-1395-millennium-dfs-round4-2026-04-12.md (CJK=650)
- reports/breakthroughs/emergence-312-meta-analysis-2026-04-15.md (CJK=681)
- reports/breakthroughs/v4-t4-A3-double-prime-rigorization-2026-04-16.md (CJK=688)
- reports/breakthroughs/v3-t5-hirahara-mcsp-deep-2026-04-15.md (CJK=708)
- reports/breakthroughs/v3-saturation-adjacent-2026-04-16.md (CJK=723)
- reports/breakthroughs/bt-1396-tqft-lattice-knot-dfs5-2026-04-12.md (CJK=733)
- reports/breakthroughs/ouroboros-atlas-audit-2026-04-15.md (CJK=750)
- reports/breakthroughs/new-domain-breakthrough-2026-04-06.md (CJK=785)
- reports/breakthroughs/bt-1394-millennium-dfs-round3-2026-04-12.md (CJK=790)
- reports/breakthroughs/v3-t1-abelian-sixfolds-deep-dive-2026-04-15.md (CJK=790)
- reports/breakthroughs/v3-t4-guth-maynard-2024-deep-dive-2026-04-15.md (CJK=812)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY; see session log 2026-04-24 section 11.6):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
   - After `git stash pop` or any merge resolution: re-run `python3 tool/own_doc_lint.py --rule 1` (post-write CJK verify — a rebase can re-introduce CJK from sibling batches)
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the translated `.md` files in this batch and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-4-2 phase-4-2-breakthroughs-b (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-4-2` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 815 minus shrinkage from this and concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

### Prompt for Batch 3: `phase-4-3-breakthroughs-c`

```
You are a Phase 4 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-4-3-breakthroughs-c
Batch number: 3 of 14

## Files to translate (20 files, CJK total = 19701)

- reports/breakthroughs/v4-t1-alpha-log2-over-4-derivation-attempt-2026-04-16.md (CJK=814)
- reports/breakthroughs/external-coordination-infrastructure-2026-04-15.md (CJK=842)
- reports/breakthroughs/v3-t6-balaban-2d-modern-reorg-2026-04-15.md (CJK=848)
- reports/breakthroughs/bsd-A3-modified-with-joint-covariance-2026-04-15.md (CJK=870)
- reports/breakthroughs/bt-1415-millennium-dfs-round21-2026-04-14.md (CJK=870)
- reports/breakthroughs/lean4-formalization-plan-2026-04-15.md (CJK=871)
- reports/breakthroughs/bt-748-752-new-domains-2026-04-11.md (CJK=874)
- reports/breakthroughs/bt-18-fi24prime-3a-path-2026-04-15.md (CJK=879)
- reports/breakthroughs/moonshine-l5-barrier-paths-2026-04-15.md (CJK=883)
- reports/breakthroughs/bsd-kappa-asymptotic-964k-2026-04-15.md (CJK=922)
- reports/breakthroughs/bt-18-hauptmodul-gamma047plus-2026-04-15.md (CJK=1042)
- reports/breakthroughs/bt-1417-dfs23-info-coding-2026-04-15.md (CJK=1062)
- reports/breakthroughs/v4-t5-cross-bt-survey-544-546-547-2026-04-16.md (CJK=1079)
- reports/breakthroughs/bt-1417-millennium-dfs-round23-2026-04-15.md (CJK=1088)
- reports/breakthroughs/bt-1414-millennium-dfs-round21-2026-04-14.md (CJK=1095)
- reports/breakthroughs/bt-1389-cube-octahedron-duality-2026-04-12.md (CJK=1112)
- reports/breakthroughs/bt-1176-nuclear-reactor-kinetics-2026-04-12.md (CJK=1128)
- reports/breakthroughs/millennium-n6-attractor-2026-04-11.md (CJK=1129)
- reports/breakthroughs/arxiv-millennium-survey-180papers-2026-04-15.md (CJK=1140)
- reports/breakthroughs/bt-1387-huckel-aromatic-2026-04-12.md (CJK=1153)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY; see session log 2026-04-24 section 11.6):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
   - After `git stash pop` or any merge resolution: re-run `python3 tool/own_doc_lint.py --rule 1` (post-write CJK verify — a rebase can re-introduce CJK from sibling batches)
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the translated `.md` files in this batch and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-4-3 phase-4-3-breakthroughs-c (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-4-3` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 815 minus shrinkage from this and concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

### Prompt for Batch 4: `phase-4-4-breakthroughs-d`

```
You are a Phase 4 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-4-4-breakthroughs-d
Batch number: 4 of 14

## Files to translate (20 files, CJK total = 26644)

- reports/breakthroughs/bt-1390-hsv-color-hexad-2026-04-12.md (CJK=1157)
- reports/breakthroughs/bt-1388-ionic-octahedral-2026-04-12.md (CJK=1163)
- reports/breakthroughs/bt-1418-dfs23b-rep-theory-modular-2026-04-15.md (CJK=1169)
- reports/breakthroughs/bt-1391-photosynthesis-equation-2026-04-12.md (CJK=1173)
- reports/breakthroughs/bt-1416-millennium-dfs-round22-2026-04-15.md (CJK=1190)
- reports/breakthroughs/bt-1175-water-treatment-2026-04-12.md (CJK=1228)
- reports/breakthroughs/bt-1386-standard-model-2026-04-12.md (CJK=1241)
- reports/breakthroughs/bsd-cremona-sel6-empirical-2026-04-15.md (CJK=1247)
- reports/breakthroughs/breakthrough-theorems-warp-dimension-2026-04-08.md (CJK=1249)
- reports/breakthroughs/bt-1413-millennium-dfs-round20-2026-04-14.md (CJK=1275)
- reports/breakthroughs/breakthrough-theorems-extension-2026-04-08.md (CJK=1295)
- reports/breakthroughs/new-breakthrough-hypotheses-2026-03-31.md (CJK=1389)
- reports/breakthroughs/millennium-7-closure-2026-04-11.md (CJK=1394)
- reports/breakthroughs/bt-19-consciousness-triple-verification-2026-04-15.md (CJK=1431)
- reports/breakthroughs/bt-542-p-vs-np-4-barriers-survey-2026-04-15.md (CJK=1445)
- reports/breakthroughs/bt-1169-1174-fusion-v5-2026-04-12.md (CJK=1468)
- reports/breakthroughs/bt-1163-1168-superconductor-v5-2026-04-12.md (CJK=1494)
- reports/breakthroughs/forge-triple-fusion-2026-04-14.md (CJK=1499)
- reports/breakthroughs/bt-18-baby-monster-p10-retry-2026-04-15.md (CJK=1546)
- reports/breakthroughs/millennium-dfs-complete-2026-04-11.md (CJK=1591)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY; see session log 2026-04-24 section 11.6):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
   - After `git stash pop` or any merge resolution: re-run `python3 tool/own_doc_lint.py --rule 1` (post-write CJK verify — a rebase can re-introduce CJK from sibling batches)
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the translated `.md` files in this batch and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-4-4 phase-4-4-breakthroughs-d (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-4-4` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 815 minus shrinkage from this and concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

### Prompt for Batch 5: `phase-4-5-breakthroughs-e`

```
You are a Phase 4 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-4-5-breakthroughs-e
Batch number: 5 of 14

## Files to translate (20 files, CJK total = 50317)

- reports/breakthroughs/bt-1412-millennium-dfs-round20-2026-04-14.md (CJK=1650)
- reports/breakthroughs/bt-19-tau4-promotion-2026-04-15.md (CJK=1669)
- reports/breakthroughs/bt-1397-uncovered-domains-2026-04-12.md (CJK=1727)
- reports/breakthroughs/bt-19-tau4-pci-validation-2026-04-15.md (CJK=1942)
- reports/breakthroughs/bt-19-alternative-paths-2026-04-15.md (CJK=2025)
- reports/breakthroughs/bt-1398-millennium-dfs-round6-2026-04-12.md (CJK=2059)
- reports/breakthroughs/bt-19-perfect-number-near-promotion-2026-04-15.md (CJK=2090)
- reports/breakthroughs/bt-18-vacuum-monster-chain-dfs-2026-04-14.md (CJK=2259)
- reports/breakthroughs/new-bt-new-domains-part1-2026-04-06.md (CJK=2280)
- reports/breakthroughs/consciousness-triple-fusion-2026-04-15.md (CJK=2529)
- reports/breakthroughs/new-bt-dimensional-unfolding-2026-04-06.md (CJK=2586)
- reports/breakthroughs/new-bt-new-domains-part2-2026-04-06.md (CJK=2629)
- reports/breakthroughs/bt-19-consciousness-alternate-paths-2026-04-15.md (CJK=2663)
- reports/breakthroughs/bt-19-perfect-number-path-2026-04-15.md (CJK=2832)
- reports/breakthroughs/bt-1393-n6-dfs-10k-autonomous-2026-04-12.md (CJK=2901)
- reports/breakthroughs/bt-1399-millennium-dfs-round7-2026-04-12.md (CJK=2987)
- reports/breakthroughs/bt-1406-millennium-dfs-round14-2026-04-12.md (CJK=3031)
- reports/breakthroughs/bt-18-moonshine-l5-barrier-2026-04-15.md (CJK=3059)
- reports/breakthroughs/bt-1407-millennium-dfs-round15-2026-04-12.md (CJK=3460)
- reports/breakthroughs/bt-1392-millennium-7-breakthrough-ideas-2026-04-12.md (CJK=3939)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY; see session log 2026-04-24 section 11.6):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
   - After `git stash pop` or any merge resolution: re-run `python3 tool/own_doc_lint.py --rule 1` (post-write CJK verify — a rebase can re-introduce CJK from sibling batches)
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the translated `.md` files in this batch and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-4-5 phase-4-5-breakthroughs-e (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-4-5` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 815 minus shrinkage from this and concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

### Prompt for Batch 6: `phase-4-6-breakthroughs-tail-audits-a`

```
You are a Phase 4 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-4-6-breakthroughs-tail-audits-a
Batch number: 6 of 14

## Files to translate (20 files, CJK total = 72837)

- reports/breakthroughs/bt-reinforcement-dimensional-unfolding-2026-04-06.md (CJK=4130)
- reports/breakthroughs/bt-1405-millennium-dfs-round13-2026-04-12.md (CJK=4728)
- reports/breakthroughs/bt-1400-millennium-dfs-round8-2026-04-12.md (CJK=4817)
- reports/breakthroughs/bt-1401-millennium-dfs-round9-2026-04-12.md (CJK=4901)
- reports/breakthroughs/bt-1408-millennium-dfs-round16-2026-04-12.md (CJK=4968)
- reports/breakthroughs/bt-1402-millennium-dfs-round10-2026-04-12.md (CJK=5254)
- reports/breakthroughs/bt-1404-millennium-dfs-round12-2026-04-12.md (CJK=5286)
- reports/breakthroughs/bt-1409-millennium-dfs-round17-2026-04-12.md (CJK=5303)
- reports/breakthroughs/bt-1410-millennium-dfs-round18-2026-04-12.md (CJK=5694)
- reports/breakthroughs/bt-1403-millennium-dfs-round11-2026-04-12.md (CJK=5719)
- reports/breakthroughs/bt-1413-millennium-dfs-round21-2026-04-12.md (CJK=6269)
- reports/breakthroughs/bt-1411-millennium-dfs-round19-2026-04-12.md (CJK=6880)
- reports/breakthroughs/bt-1412-millennium-dfs-round20-2026-04-12.md (CJK=7075)
- reports/audits/verification-bt-mapping-2026-04-08.md (CJK=166)
- reports/audits/paper-legacy-audit/blowup-invariant-core-2026-04-04.md (CJK=177)
- reports/audits/3d-map-verification-2026-04-08.md (CJK=239)
- reports/audits/paper-legacy-audit/audit-quality-full.md (CJK=280)
- reports/audits/sedi-brainwire-folder-removal-2026-04-11.md (CJK=293)
- reports/audits/n61-15section-audit-2026-04-11.md (CJK=324)
- reports/audits/paper-legacy-audit/verify-results.md (CJK=334)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY; see session log 2026-04-24 section 11.6):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
   - After `git stash pop` or any merge resolution: re-run `python3 tool/own_doc_lint.py --rule 1` (post-write CJK verify — a rebase can re-introduce CJK from sibling batches)
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the translated `.md` files in this batch and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-4-6 phase-4-6-breakthroughs-tail-audits-a (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-4-6` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 815 minus shrinkage from this and concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

### Prompt for Batch 7: `phase-4-7-audits-b`

```
You are a Phase 4 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-4-7-audits-b
Batch number: 7 of 14

## Files to translate (20 files, CJK total = 13075)

- reports/audits/paper-legacy-audit/verification-audit-2026-04-08.md (CJK=355)
- reports/audits/products-drift-fix-2026-04-11.md (CJK=430)
- reports/audits/ubu-exit137-diagnosis-2026-04-14.md (CJK=456)
- reports/audits/verification-audit-2026-04-08.md (CJK=482)
- reports/audits/paper-legacy-audit/audit-missing-verification.md (CJK=497)
- reports/audits/sota-3-integration-2026-04-11.md (CJK=507)
- reports/audits/atlas-promotion-2026-04-11.md (CJK=535)
- reports/audits/miss-links-audit.md (CJK=546)
- reports/audits/tecs-l-cleanup-2026-04-11.md (CJK=586)
- reports/audits/atlas-promotion-round2-2026-04-11.md (CJK=587)
- reports/audits/grade13-candidates-2026-04-14.md (CJK=649)
- reports/audits/audit-latest.md (CJK=687)
- reports/audits/paper-legacy-audit/verify-coverage.md (CJK=768)
- reports/audits/products-postsession-additions-2026-04-11.md (CJK=793)
- reports/audits/r29-migration-bulk-2026-04-11.md (CJK=797)
- reports/audits/goal-md-expansion-20-295.md (CJK=809)
- reports/audits/products-upgrade-9-2026-04-11.md (CJK=837)
- reports/audits/atlas-promotion-round3-2026-04-11.md (CJK=897)
- reports/audits/products-link-remap-2026-04-11.md (CJK=924)
- reports/audits/papers-expansion-39-50.md (CJK=933)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY; see session log 2026-04-24 section 11.6):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
   - After `git stash pop` or any merge resolution: re-run `python3 tool/own_doc_lint.py --rule 1` (post-write CJK verify — a rebase can re-introduce CJK from sibling batches)
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the translated `.md` files in this batch and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-4-7 phase-4-7-audits-b (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-4-7` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 815 minus shrinkage from this and concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

### Prompt for Batch 8: `phase-4-8-audits-c`

```
You are a Phase 4 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-4-8-audits-c
Batch number: 8 of 14

## Files to translate (20 files, CJK total = 23915)

- reports/audits/sedi-brainwire-lens-ref-fix-2026-04-11.md (CJK=951)
- reports/audits/convergence-ossification-2026-04-11.md (CJK=971)
- reports/audits/lens-ssot-cleanup-2026-04-11.md (CJK=986)
- reports/audits/r29-migration-synbio-2026-04-11.md (CJK=998)
- reports/audits/papers-ssot-ghost-audit-2026-04-11.md (CJK=1016)
- reports/audits/convergence-update-2026-04-11.md (CJK=1078)
- reports/audits/registry-path-fix-2026-04-11.md (CJK=1111)
- reports/audits/paper-legacy-audit/audit-quality-11.md (CJK=1122)
- reports/audits/atlas-promotion-round4-2026-04-11.md (CJK=1168)
- reports/audits/synbio-merge-2026-04-11.md (CJK=1180)
- reports/audits/papers-n62-completion-2026-04-11.md (CJK=1184)
- reports/audits/stale-md-48-investigation-2026-04-11.md (CJK=1207)
- reports/audits/2026-04-12/millennium-status.md (CJK=1257)
- reports/audits/go-audit-v6-2026-04-12.md (CJK=1261)
- reports/audits/auto-audit-system-proposal.md (CJK=1286)
- reports/audits/go-audit-2026-04-12.md (CJK=1307)
- reports/audits/zenodo-publish-ready-2026-04-11.md (CJK=1318)
- reports/audits/go-session-audit-v2-2026-04-12.md (CJK=1323)
- reports/audits/manifest-expansion-11-papers-2026-04-11.md (CJK=1528)
- reports/audits/ai-techniques-16-canonical-2026-04-12.md (CJK=1663)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY; see session log 2026-04-24 section 11.6):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
   - After `git stash pop` or any merge resolution: re-run `python3 tool/own_doc_lint.py --rule 1` (post-write CJK verify — a rebase can re-introduce CJK from sibling batches)
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the translated `.md` files in this batch and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-4-8 phase-4-8-audits-c (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-4-8` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 815 minus shrinkage from this and concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

### Prompt for Batch 9: `phase-4-9-audits-tail-sessions-a`

```
You are a Phase 4 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-4-9-audits-tail-sessions-a
Batch number: 9 of 14

## Files to translate (20 files, CJK total = 24407)

- reports/audits/readme-ssot-audit-2026-04-19.md (CJK=1668)
- reports/audits/go-audit-v4-2026-04-12.md (CJK=1769)
- reports/audits/go-audit-v5-2026-04-12.md (CJK=1829)
- reports/audits/zenodo-publish-3-papers-2026-04-11.md (CJK=1872)
- reports/audits/go-session-audit-v3-2026-04-12.md (CJK=2097)
- reports/audits/bt-audit-report.md (CJK=3216)
- reports/audits/readme-products-drift-2026-04-11.md (CJK=3549)
- reports/audits/products-link-audit-2026-04-11.md (CJK=4436)
- reports/sessions/dfs-24-hodge-direction-2026-04-24.md (CJK=5)
- reports/sessions/dfs-24-ns-direction-2026-04-24.md (CJK=12)
- reports/sessions/plans/2026-04-04-tecs-l-discovery-loop.md (CJK=171)
- reports/sessions/specs/2026-04-07-next-model-blowup-design.md (CJK=301)
- reports/sessions/2026-04-11-weekly-audit.md (CJK=311)
- reports/sessions/2026-04-11-weekly-audit_rerun-2056.md (CJK=311)
- reports/sessions/cross-dse-resonance-2026-04-08.md (CJK=357)
- reports/sessions/experiments-expansion-200-250.md (CJK=415)
- reports/sessions/cross-domain-resonance-2026-03-31.md (CJK=499)
- reports/sessions/cross-dse-rerun-2026-04-08.md (CJK=505)
- reports/sessions/cross-dse-results-2026-04-05.md (CJK=525)
- reports/sessions/experiments-expansion-122-150.md (CJK=559)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY; see session log 2026-04-24 section 11.6):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
   - After `git stash pop` or any merge resolution: re-run `python3 tool/own_doc_lint.py --rule 1` (post-write CJK verify — a rebase can re-introduce CJK from sibling batches)
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the translated `.md` files in this batch and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-4-9 phase-4-9-audits-tail-sessions-a (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-4-9` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 815 minus shrinkage from this and concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

### Prompt for Batch 10: `phase-4-10-sessions-b`

```
You are a Phase 4 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-4-10-sessions-b
Batch number: 10 of 14

## Files to translate (20 files, CJK total = 22726)

- reports/sessions/plans/2026-03-28-n6-inevitability-engine.md (CJK=627)
- reports/sessions/specs/2026-04-06-ufo-warp-dimension-design.md (CJK=639)
- reports/sessions/experiments-expansion-150-200.md (CJK=689)
- reports/sessions/nexus-roadmap-2026-04-04.md (CJK=844)
- reports/sessions/specs/2026-04-01-hexa-battery-design.md (CJK=863)
- reports/sessions/plans/2026-04-01-ultimate-pure-mathematics-dse.md (CJK=921)
- reports/sessions/dfs-24-ym-direction-2026-04-24.md (CJK=929)
- reports/sessions/millennium-lemmas-2026-04-11.md (CJK=976)
- reports/sessions/specs/2026-04-01-ultimate-pure-mathematics-dse.md (CJK=1013)
- reports/sessions/dfs-24-riemann-direction-2026-04-24.md (CJK=1106)
- reports/sessions/specs/2026-04-02-hexa-ccus-design.md (CJK=1149)
- reports/sessions/millennium-dfs345-2026-04-12.md (CJK=1250)
- reports/sessions/plans/2026-04-01-ultimate-fusion-dse.md (CJK=1324)
- reports/sessions/dfs-24-pnp-direction-2026-04-24.md (CJK=1381)
- reports/sessions/explosive-growth-2026-04-10.md (CJK=1403)
- reports/sessions/specs/2026-04-01-ultimate-programming-language-design.md (CJK=1461)
- reports/sessions/plans/2026-04-01-ultimate-programming-language.md (CJK=1500)
- reports/sessions/specs/2026-04-08-hexa-lang-blockers-for-porting.md (CJK=1518)
- reports/sessions/plans/2026-04-02-hexa-ccus-implementation.md (CJK=1545)
- reports/sessions/2026-04-11-products-readme-unification.md (CJK=1588)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY; see session log 2026-04-24 section 11.6):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
   - After `git stash pop` or any merge resolution: re-run `python3 tool/own_doc_lint.py --rule 1` (post-write CJK verify — a rebase can re-introduce CJK from sibling batches)
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the translated `.md` files in this batch and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-4-10 phase-4-10-sessions-b (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-4-10` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 815 minus shrinkage from this and concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

### Prompt for Batch 11: `phase-4-11-sessions-tail-discovery-a`

```
You are a Phase 4 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-4-11-sessions-tail-discovery-a
Batch number: 11 of 14

## Files to translate (20 files, CJK total = 62616)

- reports/sessions/millennium-lemmas-2026-04-14.md (CJK=1617)
- reports/sessions/plans/2026-04-01-hexa-battery-architecture.md (CJK=1804)
- reports/sessions/millennium-loop-25-26.md (CJK=1885)
- reports/sessions/specs/2026-04-03-nexus-unified-brainstorm.md (CJK=1982)
- reports/sessions/specs/2026-04-03-discovery-engine-design.md (CJK=2541)
- reports/sessions/cross-project-transplant-2026-04-07.md (CJK=3164)
- reports/sessions/hypotheses-dfs-chain-2026-04-07.md (CJK=4950)
- reports/sessions/specs/2026-04-02-kstar-300s-steady-state-design.md (CJK=11872)
- reports/sessions/specs/2026-04-02-kstar-n6-tokamak-design.md (CJK=15141)
- reports/sessions/specs/2026-04-02-ultimate-fusion-powerplant-design.md (CJK=15851)
- reports/discovery/n6-optimal-llm-spec.md (CJK=8)
- reports/discovery/cross-dse-bottom-analysis.md (CJK=12)
- reports/discovery/llm-improvement-new-hypotheses-2026.md (CJK=73)
- reports/discovery/anomaly-detection-results.md (CJK=93)
- reports/discovery/cross-dse-4-2026-04-12-raw.md (CJK=215)
- reports/discovery/dse-domains.md (CJK=227)
- reports/discovery/mc-v93-domain-breakdown.md (CJK=233)
- reports/discovery/monte-carlo-domain-breakdown.md (CJK=284)
- reports/discovery/dse-uncovered-scan-2026-04-12.md (CJK=310)
- reports/discovery/dse-map.md (CJK=354)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY; see session log 2026-04-24 section 11.6):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
   - After `git stash pop` or any merge resolution: re-run `python3 tool/own_doc_lint.py --rule 1` (post-write CJK verify — a rebase can re-introduce CJK from sibling batches)
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the translated `.md` files in this batch and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-4-11 phase-4-11-sessions-tail-discovery-a (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-4-11` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 815 minus shrinkage from this and concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

### Prompt for Batch 12: `phase-4-12-discovery-b`

```
You are a Phase 4 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-4-12-discovery-b
Batch number: 12 of 14

## Files to translate (20 files, CJK total = 15056)

- reports/discovery/dse-cluster-v2.md (CJK=421)
- reports/discovery/lens-expansion-397-450.md (CJK=433)
- reports/discovery/lens-expansion-500-600.md (CJK=515)
- reports/discovery/dse-500-expansion-2026-04-11.md (CJK=561)
- reports/discovery/dse-cross-pilot-result.md (CJK=603)
- reports/discovery/claude-code-cache-bug-analysis.md (CJK=636)
- reports/discovery/ai-energy-savings-guide.md (CJK=657)
- reports/discovery/nobel-grade-findings.md (CJK=734)
- reports/discovery/xn6-rtl-phase3-2026-04-11.md (CJK=745)
- reports/discovery/xn6-isa-phase2-2026-04-11.md (CJK=748)
- reports/discovery/cross-dse-4-2026-04-12.md (CJK=772)
- reports/discovery/dse-v2-results-2026-04-11.md (CJK=773)
- reports/discovery/proof4-candidate-2026-04-11.md (CJK=785)
- reports/discovery/lens-expansion-450-500.md (CJK=812)
- reports/discovery/kolon-n6-breakthrough.md (CJK=818)
- reports/discovery/l7-meta-layer-proposal.md (CJK=820)
- reports/discovery/reality-map-monte-carlo-v8.md (CJK=1006)
- reports/discovery/mc-v9-proposal.md (CJK=1054)
- reports/discovery/consciousness-cluster-bt.md (CJK=1072)
- reports/discovery/dimensional-perception.md (CJK=1091)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY; see session log 2026-04-24 section 11.6):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
   - After `git stash pop` or any merge resolution: re-run `python3 tool/own_doc_lint.py --rule 1` (post-write CJK verify — a rebase can re-introduce CJK from sibling batches)
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the translated `.md` files in this batch and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-4-12 phase-4-12-discovery-b (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-4-12` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 815 minus shrinkage from this and concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

### Prompt for Batch 13: `phase-4-13-discovery-tail-reports-top-a`

```
You are a Phase 4 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-4-13-discovery-tail-reports-top-a
Batch number: 13 of 14

## Files to translate (20 files, CJK total = 21055)

- reports/discovery/layer-dashboard.md (CJK=1168)
- reports/discovery/chip-architecture-guide.md (CJK=1177)
- reports/discovery/dse-cross-resonance.md (CJK=1232)
- reports/discovery/mc-v9-results-2026-04-11.md (CJK=1359)
- reports/discovery/bt-425-444-proposal.md (CJK=2517)
- reports/discovery/bt-381-400-proposal.md (CJK=2590)
- reports/discovery/bt-401-420-proposal.md (CJK=2604)
- reports/discovery/dse-cross-fusion.md (CJK=3855)
- reports/digest-20260416.md (CJK=83)
- reports/E6_signal_homology_20260415.md (CJK=133)
- reports/E1_signal_soc_map_20260415.md (CJK=139)
- reports/E2_signal_bt_autocorr_20260415.md (CJK=151)
- reports/megahub-detection-20260415.md (CJK=213)
- reports/cross-backfill-20260415.md (CJK=439)
- reports/chip-roadmap-mk3-2026-04-15.md (CJK=444)
- reports/atlas-promotion-p5-2026-04-14.md (CJK=536)
- reports/meta-group-H-20260415.md (CJK=575)
- reports/dfs27-yangmills-20260415.md (CJK=613)
- reports/ym-beta-series-20260415.md (CJK=613)
- reports/millennium-group-F-20260415.md (CJK=614)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY; see session log 2026-04-24 section 11.6):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
   - After `git stash pop` or any merge resolution: re-run `python3 tool/own_doc_lint.py --rule 1` (post-write CJK verify — a rebase can re-introduce CJK from sibling batches)
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the translated `.md` files in this batch and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-4-13 phase-4-13-discovery-tail-reports-top-a (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-4-13` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 815 minus shrinkage from this and concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

### Prompt for Batch 14: `phase-4-14-reports-top-b-misc`

```
You are a Phase 4 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-4-14-reports-top-b-misc
Batch number: 14 of 14

## Files to translate (24 files, CJK total = 24765)

- reports/bsd-kappa-0.175-decomposition.md (CJK=654)
- reports/kuramoto-perfect-numbers-20260415.md (CJK=714)
- reports/field-emergence-dse-2026-04-15.md (CJK=750)
- reports/SR-universality-design-20260415.md (CJK=766)
- reports/tau_sigma_ratio_universality.md (CJK=788)
- reports/sigma-sopfr-7-megasignature-20260415.md (CJK=822)
- reports/chip_comparison_l1_l10.md (CJK=871)
- reports/bernoulli-17-validation-20260415.md (CJK=880)
- reports/wild-group-G-20260415.md (CJK=891)
- reports/transcend-p12-2-mk3-atlas-integration-2026-04-15.md (CJK=1063)
- reports/transcend-p11-1-hexa-gate-mk3-impl-2026-04-15.md (CJK=1192)
- reports/group-O-applications-physics-20260415.md (CJK=1210)
- reports/millennium-dfs-status.md (CJK=1538)
- reports/atlas-mk3-audit-2026-04-15.md (CJK=1667)
- reports/mk3-synthesis-2026-04-15.md (CJK=1916)
- reports/transcend-p13-2-discovery-engine-mk3-2026-04-15.md (CJK=1930)
- reports/changelogs/README-details.md (CJK=15)
- reports/changelogs/2026-04-11-weekly.md (CJK=55)
- reports/templates/changelog-template.md (CJK=85)
- reports/templates/weekly-audit-template.md (CJK=261)
- reports/changelogs/3d-map-changelog-2026-04-08.md (CJK=568)
- reports/meta/p9-bt18-l5-retry-judgment-audit-2026-04-15.md (CJK=1156)
- reports/validation/techniques-68-smoke-test-2026-04-12.md (CJK=1949)
- reports/meta/p9-consciousness-red-team-audit-2026-04-15.md (CJK=3024)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY; see session log 2026-04-24 section 11.6):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
   - After `git stash pop` or any merge resolution: re-run `python3 tool/own_doc_lint.py --rule 1` (post-write CJK verify — a rebase can re-introduce CJK from sibling batches)
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the translated `.md` files in this batch and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-4-14 phase-4-14-reports-top-b-misc (24 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-4-14` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 815 minus shrinkage from this and concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

## 8. Post-Phase-4 Target State

- Allowlist count: 815 -> 531 (all 284 reports/ entries removed)
- Remaining subtrees on allowlist (approximate, pending Phase 4 execution):
  - domains/ residual (~217 files, non-priority longer-form documents)
  - Other subtrees as enumerated in the roadmap
- Next wave: Phase 5 (domains/ residual + remaining sub-trees per roadmap).

## 9. References

- Roadmap: `proposals/own1-hard-english-only-translation-roadmap-2026-04-24.md`
- Phase 3 plan (template source): `reports/sessions/phase-3-batch-plan.md`
- Session log with race-pattern post-mortem: `reports/sessions/hard-english-only-session-2026-04-24.md` (section 11.6)
- Current allowlist: `tool/own1_legacy_allowlist.json` (815 entries at planning time)

