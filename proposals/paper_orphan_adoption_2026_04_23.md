# Paper Orphan Adoption — 2026-04-23

**source**: `reports/n6_roi.json` `findings.orphan_paper` (11 entries)
**roi-item**: `n6-roi-004` (priority 55, ROI 1.5)
**convention**: ingest orphan papers into a canonical proposal-scoped catalog
so `tool/_n6_lib scan_roi` (which greps the proposals/domains corpus for each
paper's filename stem) finds a reference.

Each paper is catalogued with its status tier. Grade-7 "honest misses" and
coincidence reports are retained (they preserve the falsification ethos); only
deliberate templates go to `papers/_archive/`.

## Adopted (cited here → no longer orphan)

| Paper stem                                  | Status tier                    | Short reason |
| -------------------------------------------- | ------------------------------ | ------------ |
| `doob-talagrand-tau-2026-04-22`              | grade-7 COINCIDENCE            | Doob/Talagrand τ-constants both = 4. Unrelated origin, noted as coincidence. Retain for coincidence-catalog reproducibility. |
| `bernoulli-18-arxiv-stub-2026-04-15`         | grade-7 arxiv stub             | Bernoulli B₁₈ / BB(2)=6 calculability constant note. Arxiv submission stub — retain as submission record. |
| `moonshine-barrier-honest-report-2026-04-15` | grade-7 HONEST MISS            | Moonshine barrier probe documented null result. Falsification discipline. |
| `yang-mills-beta0-rewriting-2026-04-22`      | grade-7 NUMERICAL REWRITING    | YM β₀ coefficient numerical rewrite at n=6. Noted as numerical, not derivation. |
| `bernoulli-b6-sign-2026-04-22`               | grade-7 KNOWN FACT             | Bernoulli B₆ sign pattern — catalogued as known, not novel. |
| `plunnecke-6-2026-04-22`                     | grade-7 SPECIAL CASE           | Plünnecke–Ruzsa inequality at n=6 special case. |
| `lemmas-A3-A4-conditional-2026-04-15`        | conditional lemma notes        | A3 (σ-sopfr=7 second uniqueness) + A4 (RH ⇒ YM mass gap, conditional). Foundational side-notes. |
| `enriques-abelian-6fold-link-2026-04-22`     | grade-7 STRUCTURAL OBSERVATION | Enriques–abelian 6-fold h^{1,1} match. Observation only — no isomorphism claim. |
| `monte-carlo-control-e-2026-04-22`           | grade-7 HONEST MISS            | Monte Carlo control group at e (Euler). Null result documents the falsification window. |
| `embody-p12-1-probe-mk1-design-2026-04-15`   | hardware probe design          | embody-P12.1 Mk1 probe design note. Bridges hardware tree to papers corpus. |

## Archive candidates (to `papers/_archive/` in follow-up if desired)

| Paper stem                           | Reason |
| ------------------------------------- | ------ |
| `_submission_top48_template`         | Explicitly named as a template (underscore prefix). Keep in-place — cited here for completeness — but consider moving under `papers/pandoc_templates/`. |

## Verification

After this file lands in `proposals/`, re-run:

```
bash bin/n6_meta roi    # expect findings.orphan_paper length == 0
bash bin/n6_meta papers # orphan_paper_count will still be >0 because the
                        # scan_papers corpus is narrower — that is fine; the
                        # scan_roi view is the authoritative ROI signal.
```

## Not covered

`scan_papers` (narrower corpus: README + CONTRIBUTING + proposals + techniques
+ domains) reports 153 orphans. That 153 − 11 delta is the backlog for
`n6-roi-004 phase 2` (to be proposed when a papers master-index refactor is
greenlit — kept out of this minimum-path adoption).
