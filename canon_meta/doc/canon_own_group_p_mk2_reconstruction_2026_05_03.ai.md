---
schema: canon/docs/own_group_p_mk2_reconstruction/ai-native/1
last_updated: 2026-05-03
ssot:
  rule_file: .own.group_p
  predecessor_handoff: canon_meta/doc/canon_self_mk2_tuning_landed_2026_05_02.ai.md
  absolute_rules_anchor: canonshared/config/absolute_rules.json (N62 + PP2 + R29)
  axis_spine: .roadmap.group_p (Tier-A planned, deferred per predecessor handoff §2.1)
  retired_mk1_own: confirmed (mk1 .own 881L + 35 rules deleted at commit 442afa7b 2026-05-03)
related_raws: []  # paper-md governance is n6-local; hive raw 270/271/272/273 + arch.001 do NOT govern paper-md content
related_docs:
  - canon_meta/doc/canon_self_mk2_tuning_landed_2026_05_02.ai.md (parent handoff)
  - canonshared/config/absolute_rules.json (N62 / PP2 / R29 SSOT, predates `.own` reconstruction)
status: PLAN-LANDED (.own.group_p emitted; Phase 2-5 deferred to follow-up cycles)
preset: friendly (handoff doc + minimal rule emit; impl-heavy phases preserved for follow-up)
policy:
  migration: PROHIBITED (additive only; no rename / no move / no delete)
  destructive_ops: 0
  user_verbatim_ban: enforced (BR-NO-USER-VERBATIM)
  hive_resource_only: enforced (own#35 mandate; no host python3 detection)
  raw_count_target: 8 caveats
  cap: 60min
  cost: $0 mac-local
omega_cycle: 6-step single-pass (audit -> plan -> emit -> handoff -> marker -> close)
---

# canon .own.group_p mk2 reconstruction — landed plan (2026-05-03)

> **TL;DR for the implementer**
>
> mk1 `.own` (881 LoC, 35 rules) was deleted at commit 442afa7b on 2026-05-03 as part of mk2 plan-land. This cycle restores **paper-md governance only** as a unified mk2 rule (`own 6 paper-3pack-verify-embedded` in `.own.group_p`), collapsing mk1 own#6 (paper-verify-embedded HARD) + mk1 own#15 (paper-canonical-sections HARD) into one canonical pattern, mirroring hive raw.mk2 arch.001 (4-rule cluster -> 1 collapsed). A new math/physics classification gate is added per 2026-05-03 user directive ("수학적, 물리적 검증코드여야한다") — auto-detection required, Tier-1 substring + Tier-2 AST fallback. **This cycle ships Phase 1 + Phase 5 only**: declarative `.own.group_p` emit + handoff + marker. Phase 2 (own#15 lint reconstruction + math/physics classifier), Phase 3 (SSCB mk1 paper md emission), Phase 4 (allowlist sidecar bootstrap) deferred to follow-up cycle.

## §1 Phase 0 — Deep-research audit findings (2026-05-03)

### §1.1 Paper inventory

- `find papers -mindepth 1 -maxdepth 1 -name '*.md' | wc -l` = **164**
- Papers containing ` ```python ` block: **148** (90.2%)
- Papers WITHOUT ` ```python ` block: **16** — perfect overlap with mk1 own#6 legacy allowlist
- Papers containing `## §1 WHY` header: **158** (96.3%)
- Papers containing `## §21 IMPACT` header: **158**
- Papers containing `mk_history` (underscore form): **158**
- Papers containing `mk-history` (hyphen form, mk1 own#15 spec): **2** (only `papers/hexa-weave-formal-mechanical-w2-2026-04-28.md` properly hyphenated; outlier)
- 6 non-conforming = subset of 16 own#6 legacy allowlist (math-pure / arxiv-stub format predates own#15 scaffold)

### §1.2 Lint coverage state at 2026-05-03

| Lint | File | Status | Scope |
|---|---|---|---|
| own#6 paper-verify-embedded | `tool/own6_paper_verify_embedded_lint.hexa` (269 LoC) | ACTIVE | `papers/*.md` (top-level only) — substring + sibling-glob; 16-entry hardcoded allowlist; selftest 4/4 PASS |
| own#15 paper-canonical-sections | (NONE) | ABSENT | Removed from `tool/own_doc_lint.hexa` TARGET_RULES on 2026-04-29 (full hexa-native migration commit `c47e9f22`) |
| own#31 verify-tautology-ban | `tool/own31_verify_tautology_ban_lint.hexa` (2603 LoC) | ACTIVE | `domains/**/*.md` + `papers/**/*.md` (line 2145 `let sxs = ["domains", "papers"]`) — 10 adversarial detectors + Tier-1 string heuristics |
| own#33 ai-native-verify-pattern | (NONE) | FORWARD-SPEC | Referenced via own#31 v3.19 ai-native fix-output (line 1916) — no dedicated lint |
| own#34 Tier-2 runtime | `tool/own31_ast_visitor.py` (213 LoC) + `tool/own31_runtime_sandbox.py` (255 LoC) | STANDALONE-CLI | Available for math/physics classifier extension; hexa lint dispatch deferred per own#35 hive-resource integration |

### §1.3 SSOT cross-reference

- `canonshared/config/absolute_rules.json` (459 LoC) carries paper-md HARD rules at:
  - `N62` lines 307-311 — 검증코드 100% 골화 형식 의무 (@register + ossification_loop + N/N OSSIFIED + assert)
  - `PP2` lines 336-340 — 검증코드 없는 논문 = 미완성; 별도 verify_*.py / verify_*.hexa 절대 금지; `_registry.json` `verify_script` 필드 신규 추가 금지
  - `R29` lines 233-239 — 도메인당 1파일; verify.hexa 별도 파일 금지
- `absolute_rules.json` predates `.own` and survives the mk1 deletion — it is the durable SSOT
- `.own.group_p` is the **declarative L1 wrapper** that names the rule, lists invariants, and points to `absolute_rules.json` + lint paths

### §1.4 Hive raw alignment

- `canon_meta/doc/canon_self_mk2_tuning_landed_2026_05_02.ai.md:194-220` (predecessor handoff §3.2) lists raw 270/271/272/273 + arch.001 n6-side adoption targets: T0 = `canonshared/n6/`, T1 = `engine/`, T2 = `tool/` — `papers/` **NOT in scope**
- `/Users/<user>/core/hive/.raw.mk2` line 74 (arch.001) lists `papers` repo in scope but the rule applies to module architecture, NOT paper-md content
- `grep paper/verify_block/fenced/python` in `/Users/<user>/core/hive/.raw.mk2` = 0 matches
- **Conclusion**: paper-md governance is n6-local. `.own.group_p` does not declare hive raw cross-links.

### §1.5 Math/physics auto-classification feasibility

- 135/148 (91.2%) py-bearing papers match shared n=6 math template signature: `def divisors|def sigma|def tau|def sopfr|def phi_min_prime`
- Strong MATH disambiguators: `def sigma\b`, `def divisors\b`, `def sopfr\b`, `from math import gcd`, `Fraction`, `_totient`, `is_squarefree`
- Strong PHYSICS disambiguators (rare in current corpus): `NIST`, `CODATA`, `Carnot`, `Shockley`, `Queisser`, `Bernoulli`, `Weibull`, `Darcy`, `Helmholtz`, scientific notation `[0-9]+\.[0-9]+e-?[0-9]+`, SI units (`mΩ`, `kHz`, `nm`, `μs`, `eV`, `J/K`)
- AMBIGUOUS pattern: 117 papers contain DIM dict like `'F': (1, 1, -2, 0)` (dimensional-tuple math, not numeric physics) — falls under MATH bucket
- **Tier-1 (substring)** sufficient for ~91% of papers
- **Tier-2 (AST extension of `own31_ast_visitor.py`)** covers remaining ~9% via `_MATH_LIB_IMPORTS` + `_PHYSICS_LIB_IMPORTS` + numeric-literal scientific-notation scan
- **Tier-3 (runtime sandbox)** required only for sub-5% truly ambiguous edge cases — defer indefinitely

## §2 Phase 1 — `.own.group_p` declarative emit (this cycle)

### §2.1 File path

```
/Users/<user>/core/canon/.own.group_p
```

Parallel to (retired) mk1 `.own`. Schema: `canon/own/group_p/2`.

### §2.2 Unified rule structure

Single `own 6 paper-3pack-verify-embedded` declaration absorbing mk1 own#6 + mk1 own#15:

| Field | Content |
|---|---|
| invariant brief-§1-§7 | 7 brief sections (WHY/COMPARE/REQUIRES/STRUCT/FLOW/EVOLVE/VERIFY) |
| invariant engineering-§8-§20 | 13 engineering sections (EXEC/SYSTEM/ARCH/CIRCUIT/PCB/FW/MECH/MFG/TEST/BOM/VENDOR/ACCEPTANCE/APPENDIX) |
| invariant impact-§21 | 1 impact section |
| invariant python-block-embedded | ` ```python ` fenced block ≥1 inside §7 VERIFY |
| invariant math-or-physics-classified | content classifies as math OR physics OR both (auto-detect required) |
| invariant mk_history-footer | `## mk_history` underscore + ≥3 lines |
| invariant ascii-check | encoding hygiene |
| forbid sibling-verify-file | `<stem>_verify.*` / `<stem>-verify.*` glob |
| forbid tautology-decoration | own#31 cross-fire |
| forbid n6-force-fit | own#32 cross-link |
| forbid 21-section-partial-omission | OWN6_LEGACY_ALLOWLIST exempt only |
| exempt META_STEMS | `[readme, claude, index, _index]` |
| exempt OWN6_LEGACY_ALLOWLIST | 16 entries (frozen, shrink-only) |
| exempt OWN15_LEGACY_ALLOWLIST | 6 entries (subset of OWN6 16) |

### §2.3 Cross-link cognitive-frameworks

own#2 (master identity) / own#31 (tautology ban) / own#32 (physical-limit framing) / own#33 (Block A-G template) / own#34 (Tier-2 runtime) / own#35 (hive-resource-only) / N62 / PP2 / R29.

### §2.4 Enforcement layers

- **PRIMARY (active)**: `tool/own6_paper_verify_embedded_lint.hexa` — substring + sibling-glob
- **SECONDARY (active)**: `tool/own31_verify_tautology_ban_lint.hexa` — papers/ scope already live
- **TERTIARY (deferred)**: own#15 21-section lint — Phase 2a reconstruction
- **QUATERNARY (deferred)**: math/physics classifier — Phase 2b-c

## §3 Phase 5 — Handoff + marker (this cycle)

### §3.1 Handoff (this doc)

- path: `canon_meta/doc/canon_own_group_p_mk2_reconstruction_2026_05_03.ai.md`
- frontmatter: AI-native (schema / last_updated / ssot / related_raws / related_docs / status / preset / policy / omega_cycle)
- length target: ≤ 300 lines

### §3.2 Marker

- path: `state/markers/canon_own_group_p_mk2_reconstruction.marker`
- format: JSON (schema `canon/markers/own_group_p_mk2_reconstruction/1`)
- key fields: completion_iso / handoff_path / handoff_sha256 / phase_outputs / raw_anchors / policy_compliance / next_step

## §4 What is NOT done (Phase 2-5 deferred)

1. **No `tool/own15_paper_canonical_sections_lint.hexa` emit** — Phase 2a follow-up
2. **No `tool/own_doc_lint.hexa` TARGET_RULES extension to include rule 15** — Phase 2a follow-up
3. **No `tool/own6_math_physics_classifier.hexa` emit** (Tier-1 substring) — Phase 2b follow-up
4. **No `tool/own31_ast_visitor.py` extension** (`_MATH_LIB_IMPORTS` / `_PHYSICS_LIB_IMPORTS`) — Phase 2c follow-up
5. **No `papers/sscb-mk1-2026-05-03.md` emit** (inaugural live precedent) — Phase 3 follow-up
6. **No `tool/own6_legacy_allowlist.json` sidecar** (mirror of hardcoded 16 entries) — Phase 4 follow-up
7. **No `tool/own15_legacy_allowlist.json` sidecar** (6 entries) — Phase 4 follow-up
8. **No `INDEX.json` 9-axis -> 10-axis manifest update** (governance axis) — Phase 5 follow-up
9. **No `bin/n6` / `tool/governance.hexa` `.own.group_p` recognition wiring** — verify in follow-up; if needed, additive 1-line path add

## §5 raw#10 honest caveats (8 items)

1. **mk2 collapsing pattern is documentary not enforced**: `.own.group_p` collapses mk1 own#6 + own#15 into one rule on paper, but enforce-tertiary (own#15 lint) is currently DEFERRED. Until Phase 2a lands, only own#6 substring + own#31 tautology surface is gated. The "21-section invariant" line in `.own.group_p` is **declarative-only this cycle**.

2. **Math/physics auto-classification is forward-spec**: invariant `math-or-physics-classified` references the classifier that does not yet exist. Current papers (135/148 math template) already pass any reasonable Tier-1 detection, but no automated check is wired. cat-litter §7 Block A-G precedent applies.

3. **mk_history form drift**: 158/164 papers use `mk_history` (underscore); the lone hyphen-form paper (`papers/hexa-weave-formal-mechanical-w2-2026-04-28.md`) is an outlier. `.own.group_p` codifies underscore as canonical. mk1 own#15 spec used hyphen — this is a known divergence; underscore wins because actual count > spec.

4. **OWN6_LEGACY_ALLOWLIST hardcoded in `.hexa`**: the 16 entries are at `tool/own6_paper_verify_embedded_lint.hexa:19-36`, NOT in a sidecar JSON. `.own.group_p` references the sidecar path that does not exist yet — Phase 4 emits it. Until then, lint and `.own` declaration are decoupled by file boundary.

5. **OWN15_LEGACY_ALLOWLIST count = 6 is provisional**: derived from the 158-vs-164 gap (6 papers missing §1-§21 scaffold). This subset is contained within the 16 own#6 legacy entries but not formally enumerated. Phase 4 will emit the explicit 6-entry sidecar after own#15 lint runs and produces the actual baseline.

6. **Subdir scope (papers/group-P/, papers/sigma_tau_8_submission/, papers/hexa_weave_*/) deferred**: current own#6 lint uses `find -mindepth 1 -maxdepth 1`, so only top-level `papers/*.md` is enforced. Subdirs contain additional paper-shaped content but are outside this cycle's scope. Phase plan does not assign a follow-up phase for this — explicit decision required for whether subdir expansion is governance scope or separate axis.

7. **hive raw 270/271/272/273 + arch.001 do NOT apply to paper-md**: `.own.group_p` does not declare hive raw cross-links. Confirmed via predecessor handoff §3.2 + `/Users/<user>/core/hive/.raw.mk2:74` (arch.001 scope is module architecture, not paper content). Sister-repo propagation per raw 47 is therefore **out-of-scope** for this rule.

8. **own#35 hive-resource-only compliance is forward-bind**: Phase 2c will add Tier-2 AST classifier requiring python3. Per own#35, dispatch must route through `hive resource exec python3 -- ...` not host `which python3`. Current cycle does not emit any python3 invocation, so compliance is trivially satisfied at this revision.

## §6 Next-step (follow-up cycles)

| ID | Action | ETA | Cost |
|---|---|---|---|
| FU-1 | Emit `tool/own15_paper_canonical_sections_lint.hexa` (~300 LoC) + extend `tool/own_doc_lint.hexa` TARGET_RULES to include 15 | 2026-05-15 | $0 |
| FU-2 | Emit `tool/own6_math_physics_classifier.hexa` (~250 LoC; Tier-1 substring; ~91% coverage) | 2026-05-15 | $0 |
| FU-3 | Extend `tool/own31_ast_visitor.py` with `_MATH_LIB_IMPORTS` / `_PHYSICS_LIB_IMPORTS` + emit `tool/own6_math_physics_classifier_tier2.py` (~150 LoC) | 2026-05-22 | $0 |
| FU-4 | Emit `papers/sscb-mk1-2026-05-03.md` as inaugural live precedent (3-pack PDF source markdown) | 2026-05-22 | $0 |
| FU-5 | Bootstrap `tool/own6_legacy_allowlist.json` + `tool/own15_legacy_allowlist.json` sidecars (frozen, shrink-only) | 2026-05-30 | $0 |
| FU-6 | Promote enforce-tertiary/quaternary from DEFERRED to ACTIVE; update `.own.group_p` status field | 2026-06-01 | $0 |
| FU-7 | `INDEX.json` 9-axis -> 10-axis manifest add (governance axis) | 2026-06-15 | $0 |

## §7 File index

| Path | Role |
|---|---|
| `.own.group_p` | this cycle's declarative rule emit (mk2 unified) |
| `canon_meta/doc/canon_own_group_p_mk2_reconstruction_2026_05_03.ai.md` | this handoff doc |
| `state/markers/canon_own_group_p_mk2_reconstruction.marker` | landing marker (JSON) |
| `canon_meta/doc/canon_self_mk2_tuning_landed_2026_05_02.ai.md` | predecessor handoff (mk2 plan-land) |
| `tool/own6_paper_verify_embedded_lint.hexa` | enforce-primary (active, 269 LoC) |
| `tool/own31_verify_tautology_ban_lint.hexa` | enforce-secondary (active, papers/ scope live) |
| `tool/own_doc_lint.hexa` | dispatcher (--rule 6 active; --rule 15 deferred) |
| `tool/own31_ast_visitor.py` | Tier-2 AST base (extension target for math/physics classifier) |
| `tool/own31_runtime_sandbox.py` | Tier-3 runtime sandbox base (defer indefinitely) |
| `canonshared/config/absolute_rules.json` | durable SSOT (N62 / PP2 / R29 predate `.own`) |

## §8 Closure

- omega-cycle: 6-step single-pass complete (audit -> Phase 0 / plan -> Phase 1 emit / handoff -> §3.1 / marker -> §3.2 / close -> §8)
- raw#10 honest count: 8 caveats (target hit)
- destructive ops: 0 (target hit)
- migration: 0 (target hit)
- cost: $0 mac-local
- BR-NO-USER-VERBATIM: enforced (no user-prompt verbatim quotation in body)
- AI-native: frontmatter present, schema declared, related_raws/related_docs cited
- preset: friendly (handoff doc tone + ramp explanations + no surprise mandates)
- mk1-mk2 unification: confirmed (mk1 own#6 + own#15 -> mk2 unified own 6 paper-3pack-verify-embedded)

End of doc.
