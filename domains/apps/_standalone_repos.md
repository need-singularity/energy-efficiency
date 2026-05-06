# apps/ standalone repository pointers

Cross-reference index of `domains/apps/*` specs that have been extracted into standalone GitHub repositories. The spec files in this directory remain canonical (uchg-sealed after registration); standalone repos are the working implementations (Xcode project, Core ML weights, telemetry, F-gate measurement scripts).

## Active extractions

| Spec(s) | Standalone repo | Extracted | F-gates as issues | Notes |
|---|---|---|---|---|
| `camera-filter-app` ⊕ `hexa-main-character` | [need-singularity/lumiere](https://github.com/need-singularity/lumiere) | 2026-05-06 | #1–5 (F-CFA-MVP-1..5) · #6–10 (F-MC-MVP-1..5) | Camera (APPLIES) + Studio (DIRECTS) integrated under shared 16.67 ms real-time budget · 50 mJ/frame ceiling. Brand: **Lumière ✨** (lumi/Photon shot-noise + Lumière Brothers cinema). MIT license. |

## Convention

- Spec files in `domains/apps/<slug>/<slug>.md` are the canonical research-paper-style design — own#15 21-section template, uchg-sealed after registration.
- Standalone repos under `github.com/need-singularity/*` are the working implementations.
- F-gate falsifiers declared in spec §19.2 are mirrored as GitHub issues, with milestones tied to the spec's deadline (2026-08-30 / 2026-09-30 for the apps axis mk1 cohort).
- README in each standalone repo links back to the canonical spec via doc/ seed copies; this index links forward from canonical to standalone.

## Pending candidates

The remaining 3 apps-axis domains (`hexa-filter-algebra`, `hexa-parallel-self`, `hexa-vsco`) have no standalone repo yet. They share the same 16.67 ms real-time budget and may be extracted independently or bundled later.
