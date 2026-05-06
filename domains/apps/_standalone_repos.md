# apps/ standalone repository pointers

Cross-reference index of `domains/apps/*` specs that have been extracted into standalone GitHub repositories. The spec files in this directory remain canonical (uchg-sealed after registration); standalone repos are the working implementations (Xcode project, Core ML weights, telemetry, F-gate measurement scripts).

## Active extractions

| Spec(s) | Standalone repo | Extracted | F-gates as issues | Notes |
|---|---|---|---|---|
| `camera-filter-app` ⊕ `hexa-main-character` ⊕ `hexa-filter-algebra` ⊕ `hexa-parallel-self` ⊕ `hexa-vsco` | [need-singularity/lumiere](https://github.com/need-singularity/lumiere) | 2026-05-06 | #1–5 (F-CFA-MVP-1..5) · #6–10 (F-MC-MVP-1..5) · #11–15 (F-FA-MVP-1..5) · #16–20 (F-PSELF-MVP-1..5) · #21–25 (F-VSCO-MVP-1..5) | All 5 apps-axis domains absorbed into a single iOS app under the unifying 16.67 ms real-time budget. 5 verb-distinct surfaces — 📸 Camera (APPLIES) · 🎬 Studio (DIRECTS) · 🧮 Forge (AUTHORS) · 🪞 Mirror (GENERATES) · 🎨 Atelier (EDITS·LIBRARY·DISCOVER). Brand: **Lumière ✨**. MIT license. mk2-D (commit `239b9f8`) absorbed Forge / Mirror / Atelier; mk1 stages A–D shipped Camera + Studio scaffold. |

## Convention

- Spec files in `domains/apps/<slug>/<slug>.md` are the canonical research-paper-style design — own#15 21-section template, uchg-sealed after registration.
- Standalone repos under `github.com/need-singularity/*` are the working implementations.
- F-gate falsifiers declared in spec §19.2 are mirrored as GitHub issues, with milestones tied to the spec's deadline (2026-08-30 / 2026-09-30 for the apps axis mk1 cohort).
- A standalone repo MAY absorb multiple sibling specs if they share a runtime surface (single iOS app, shared NPU budget, common UX). Lumière demonstrates this for the entire apps axis.
- README in each standalone repo links back to the canonical specs via `docs/` seed copies; this index links forward from canonical to standalone.

## Status

All 5 apps-axis domains are absorbed into Lumière. No pending candidates in the apps axis. Future sibling axes (e.g. media-editor / fitness-coach / accessibility / productivity, when they register) follow the same pattern: single standalone repo per coherent runtime surface, multi-spec absorption when verb-distinction allows.
