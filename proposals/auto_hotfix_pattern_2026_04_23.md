# AUTO: Hotfix pattern audit — 2026-04-23

**source**: Phase 8 propose_from_gaps (hotfix_commit_count_30d=8 ≥ 5)

The last 30 days include 8 commits whose subject matches one of
`workaround | hotfix | emergency | regression | revert`. Review whether
these cluster around a single module/file; if they do, promote the
underlying cause to a ROI item.

## Action checklist

- [x] `git log --since='30 days ago' --grep='workaround\|hotfix\|emergency\|regression\|revert' --name-only` — inspected.
- [x] Identify the top-3 hottest paths (real code/docs, excluding auto-regenerated reports):
  1. **README.md** — 5 hits
  2. **tool/_n6_lib** — 4 hits
  3. **docs/*/goal.md** — 2 hits each (~20 files, Revert of en-translation series)
- [x] If one module shows ≥3 hits: open a root-cause ROI item.
- [x] Otherwise mark this audit closed.

## Resolution

**Verdict: CLOSED — no pathological clustering.**

Both ≥3-hit paths have natural explanations:

- **README.md (5)** — touched by every `loop(n6)` meta-summary commit and
  several `feat(meta): Phase N` additions. Not hotfix pattern; it's the
  standard docs-touch that accompanies ROI sweeps and phase landings.
- **tool/_n6_lib (4)** — this is the meta-engine bootstrap period
  (Phases 7–14 were added in this ~12h window). Each phase legitimately
  edits the file. The commits are additive feat() commits that happen to
  match the regex via words like "regression alarm" (P7), not
  regressions themselves.

**The docs/*/goal.md cluster** is a one-time series of reverts of an
English-translation experiment — not ongoing churn.

**No root-cause ROI item opened.** The `hotfix_commit_count_30d ≥ 5`
trigger is firing on legitimate additive work; the keyword filter is
too loose (matches "regression alarm" and "Revert" equally). Consider
tightening the regex in a future P1x to exclude `feat(meta):.*regression`
and `Revert "..."` without a follow-up `Reapply`.

## Meta

- Generated automatically. Delete or fill in manually.
- Re-running `bin/n6_meta propose` on a different day creates a new
  audit file; same-day runs are idempotent.
