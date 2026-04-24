# n6-architecture submission format template — shared for the top 48 papers

| Field | Value |
|-------|-------|
| Roadmap | PAPER-P3-1 |
| Created | 2026-04-14 |
| Scope | the 48 papers registered in `_submission_top48.json` |
| Status | template_ready (skeleton only — do not regenerate the body) |
| DOI policy | simulated DOI `10.NEXUS6.n6-arch/2026-NNN` — not a real DOI |

This file provides a standard template for shaping the top 48 papers into a
journal / conference submission format. The source papers under
`papers/n6-*-paper.md` stay untouched; at submission time this template's
header / abstract / references blocks are overlaid on them. The
WHY / COMPARE / MAIN / VERIFICATION 4-stage structure is the common spine
used across every n6-architecture paper.

---

## 0. Header block (required)

```
---
doi_sim:         10.NEXUS6.n6-arch/2026-NNN
paper_id:        N6-XXX
rank:            <1..48>
target_venue:    <Nature Communications | Physical Review Letters | ICML | NeurIPS | JAIR | IEEE TVLSI>
format_status:   template_ready
submission_date: 2026-04-14
disclaimer:      simulated DOI — not registered with CrossRef/DataCite. Replace when citing externally.
---
```

- Copy `doi_sim` from `_submission_top48.json` as-is. Do not modify.
- Keep `paper_id` identical to the N6-NNN key in `_papers.json`.
- `target_venue` comes from the internal ranking; editors may swap it at
  submission time.

## 1. Authors and affiliation

```
Author: M. Park (n6-architecture owner), NEXUS-6 AI collaborators
Affiliation: n6-architecture project (AI-native Arithmetic Design Framework)
Contact: via the repository issue tracker
ORCID: (not assigned — mirrors the simulated DOI setup)
```

## 2. Abstract — 200~350 words

Template backbone:

1. **One sentence of motivation** — the limitation of existing theory in the
   target domain.
2. **Main claim** — project the n=6 identity (σ(n)·φ(n) = n·τ(n), holding
   only at n=6) onto the domain's measured quantities and identify the
   resulting closure pattern.
3. **Quantitative results** — one sentence with the three axes
   `exact_stat`, `closure_grade_pct`, `alien_index`.
4. **Reproducibility path** — atlas.n6 node paths + one line with the hexa
   verification STUB file name.
5. **Limitations and falsifier candidates** — at most two lines. Disclose
   honest MISS / unmapped entries.

## 3. WHY — motivation (1~2 pages)

- Present the domain's current SOTA numbers and a theoretical-limit table.
- One paragraph on how the n6 arithmetic coordinates (σ, τ, φ, sopfr) map to
  the domain variables.
- Intuitive explanation for why the closure condition that existing physics
  and engineering theory cannot predict is restricted to n=6.

## 4. COMPARE — ASCII chart versus baseline (required)

- Per CLAUDE.md's `feedback_ascii_report` rule, include at least one ASCII
  bar chart comparing the baseline (SOTA) to the HEXA result.
- At least three axes (accuracy / efficiency / scale).
- Units must be stated. The "ceiling" label is written in text only (no
  emoji).

```
Metric        baseline-SOTA   HEXA-n6
Accuracy [%]  ########           80
Accuracy [%]  ################   100   (ceiling)
Efficiency [J/op] ########       base
Efficiency [J/op] ##             0.25x (near ceiling)
```

## 5. MAIN — body (10~25 pages)

5.1 Arithmetic coordinate definition
- Map the domain's measurement variables x_i onto the four axes σ·τ·φ·sopfr.
- State the coordinate units and the atlas.n6 node whose data is cited.

5.2 Closure candidate and argument sketch
- The relation that holds only at n=6.
- Measured alignment rate in the domain (EXACT / NEAR / MISS classification).
- Argument path: start from pure mathematics and avoid post-hoc pattern
  matching onto n=6 (CLAUDE.md `feedback_proof_approach`).

5.3 Design / prediction output
- New design values or predictions derived from the n6 coordinates.
- Distance to the ceiling threshold.

5.4 Limitations and falsification conditions (required)
- Do not hide MISS cases. State source + measured value + error
  (CLAUDE.md `feedback_honest_verification`).

## 6. VERIFICATION — verification code block (required)

```hexa
// File: verify_<domain>_n6.hexa
// Check path: atlas.n6 node lookup → recompute measurement → EXACT/NEAR/MISS classification
import atlas.n6
measure <domain> {
  for node in atlas.lookup(domain) {
    expected = n6_coord(node.x, node.y, node.z, node.sopfr)
    measured = node.value
    classify(expected, measured)   // EXACT | NEAR | MISS
  }
}
```

- Either a `.hexa` STUB or a full script must be embedded in the body
  (HEXA-FIRST — no `.py`).
- The result statistic is recorded in the `exact_stat` field and appended to
  `experiments/_results.jsonl`.

## 7. References block

```
[1] n6-architecture internal reference: atlas.n6 node path + citation line.
[2] BT-NNN (BreakThrough registry `_registry.json` section id).
[3] External references — 3 to 10 per domain. Require a CrossRef DOI.
[4] Cross-citations between n6-architecture papers use the simulated DOI
    `10.NEXUS6.n6-arch/2026-NNN` and retain the "simulated" tag.
```

- Do not mix external references with internal simulated DOIs — keep them
  visually distinct.
- At real submission time, simulated DOIs remain only for internal tracking.

## 8. Supplementary materials

- The source paper body under `papers/n6-<domain>-paper.md` (do not edit).
- The relevant atlas.n6 section excerpt.
- The original verify_*.hexa.
- A link to any Monte-Carlo verification result, if available.

## 9. Post-submission state transitions

| format_status | Meaning |
|---------------|---------|
| template_ready | Only this template header / structure is attached (initial) |
| draft | Abstract + References filled in with real content |
| submitted_sim | Simulated-submission state — simulated DOI confirmed |
| published_sim | Simulated-publication state — not for external distribution |

- Actual journal submission is handled in a separate process. This template
  is n6-architecture's internal archival standard.

---

## Appendix A. How to apply to all 48 papers

1. In `papers/_submission_top48.json`, look up your rank row.
2. Copy this template into `papers/_submissions/N6-<id>_submission.md`
   (actual execution is out of scope for P3-1).
3. Fill only the three blocks: header, abstract, references; link the body
   to the original `n6-<domain>-paper.md`.
4. Promote `format_status` to `draft`.
5. If a falsification event triggers, recompute the ranking and update
   `experiments/paper_ranking_p3_top48.md`.

## Appendix B. Absolute rules

- English only. No emoji. Use the "ceiling" text marker.
- Mark every header clearly as "simulated DOI — not a real DOI".
- Do not edit the body of any of the 125 source papers (touch the registry,
  submission JSON, and this template only).
- No self-referential verification. Falsifier candidates must be disclosed.
