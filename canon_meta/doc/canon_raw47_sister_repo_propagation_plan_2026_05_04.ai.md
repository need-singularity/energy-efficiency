---
schema: canon/docs/raw47_sister_repo_propagation/ai-native/1
last_updated: 2026-05-04
ssot:
  proposal_only: true
  predecessor_handoff: canon_meta/doc/canon_own_readme_mk2_reconstruction_2026_05_04.ai.md
related_raws: [raw 47, hive raw.mk2 arch.001]
status: PROPOSAL (read-only investigation; no impl this cycle)
policy:
  destructive_ops: 0
  user_verbatim_ban: enforced
omega_cycle: investigation-only (no emit beyond this doc)
---

# raw 47 sister-repo propagation plan (2026-05-04)

> Investigation-only doc. READ-ONLY scan of `~/core/{nexus,anima,hexa-lang,papers,airgenome,hive}/`
> mapped against canon mk2 governance items (own#6 / own#15 / own#29 / own#14 / own#17)
> + 4 FU-deferred lint emits from the 2026-05-04 own.readme cycle. Outcome: prioritized propagation
> matrix + own#17 hive-resource migration analysis + raw#10 caveats. NO impl this cycle.

## §1 Sister-repo survey

Direct `ls` probes (2026-05-04, all paths absolute home-relative):

| Repo | papers/ | README.md (LoC) | .own* | .readme-rules.json | tool/own*.hexa | Propagation candidate |
|---|---|---|---|---|---|---|
| nexus | N/A (5 .md/json files at root, not papers/) | YES (369) | absent | YES (independent: 8 sections + sealed) | 0 | own#14 sealed-active; own#29 ports |
| anima | absent (anima research host owns separate paper trail elsewhere) | YES (259) | YES (`.own` mk2 frontmatter) | YES (independent: 8 sections + sealed) | 0 | own#14 sealed-active; own#29 ports; own#15 N/A |
| hexa-lang | absent | YES (117 — small) | YES (`.own` self-host scope only) | NO | 5 (own_lint, own_runner, own_inherit_lint, own_self_host_lint, own_cli_install_lint) | own#17 host (cross-repo dep target — see §3) |
| papers (separate repo) | N/A (this IS the papers repo; subdirs anima/core/docs) | YES (251) | absent | NO | 0 (has tool/ for doi/keyword/growth) | own#15 papers-canonical-sections target; own#6 verify target |
| airgenome | absent | YES (214) | absent | NO | 0 | own#14 weak-only candidate (no governance grammar) |
| hive | absent | YES (251) | absent (hive uses `.raw.mk2` instead) | NO | 2 (own_lint, own_8_audit_log_lint) | own#14 candidate; cross-repo SSOT layer per arch.001 |
| **canon (source)** | YES (canonical_n6_invariants*, etc) | YES | YES (.own.readme, .own.group_p) | YES | 21 | (origin) |

Key finding: of 6 sister repos, **2 have papers content** (n6 itself; nexus has paper-shaped content but flat at root not in `papers/`). **`papers/` (separate repo) is the only true papers repo**. Three repos (nexus/anima/hexa-lang) have explicit per-repo governance grammar (`.own` or `.readme-rules.json`); three (papers/airgenome/hive) lack it. `hive` governs via `.raw.mk2` (different format — JSON-line rules with `id/mk/scope/decl/proof` keys per arch.001/ai-native.001/lint.001/resource.001-009 inspection of lines 70+).

## §2 mk2 governance items propagation matrix

| Item | n6 state | Direct propagation target | Indirect / inheritance | Impact |
|---|---|---|---|---|
| own#6 paper-3pack-verify-embedded | ACTIVE (tool/own6_paper_verify_embedded_lint.hexa 269L + tool/own6_math_physics_classifier.hexa 647L FU + tool/own31_ast_visitor.py 348L FU) | `papers/` (separate repo, has docs/+anima/+core/) | nexus root .md (if reclassified as papers) | Medium — papers repo is the natural home; verify-embedded only fires on python codeblocks |
| own#15 paper-canonical-sections (21-section + mk_history) | ACTIVE (tool/own15_paper_canonical_sections_lint.hexa 614L FU) | `papers/` (PA-01..PA-07 anima papers all use Korean section names — divergent) | none | Medium — schema divergence: papers/anima uses different section grammar |
| own#29 readme-friendly-toolkit-required (32 mandatory + 7-col toolkit) | ACTIVE (tool/own29_readme_friendly_toolkit_lint.hexa 362L + tool/own29_multi_section_lint.hexa 627L FU dispatcher) | nexus / anima (have `.readme-rules.json` infra ready) | hexa-lang / airgenome / hive / papers (no rules.json yet) | High — biggest immediate propagation surface |
| own#14 readme-sealed-required | ACTIVE (sealed.hash mechanism + tool/readme_sealed_check.hexa not yet ported) | nexus / anima already declare `require_sealed: true` | hexa-lang / airgenome / hive / papers need `.readme-rules.json` bootstrap | High — partial inheritance already declared |
| own#17 public-readme-english-only (cross-repo dep) | ACTIVE (`~/core/hexa-lang/tool/readme_english_audit.hexa` direct path) | own#35 cross-fire — see §3 | n/a (own#17 IS the cross-repo bridge) | Critical (own#35 grandfather expiry pending) |

Lint coverage delta per repo (sister tool/own*.hexa count vs n6's 21):
- nexus 0 / 21, anima 0 / 21, papers 0 / 21, airgenome 0 / 21, hive 2 / 21, hexa-lang 5 / 21 (but scoped to self-hosting only; not paper/readme governance).

## §3 own#17 cross-repo migration (FU-6 absorbed)

- **Current**: `.own.readme:50,82,93` declare `~/core/hexa-lang/tool/readme_english_audit.hexa` direct cross-repo path (8934 bytes 2026-04-22, ci.yml:143-170,253 wired with SOFT-skip).
- **own#35 (2026-05-02) bans path-based external-resource access** — own#17 grandfathered explicitly in `.own.readme:23` with caveat 4 in handoff doc.
- **hive resource CLI status: AVAILABLE.** `command -v hive` resolves to `$HOME/.hx/bin/hive`; `hive resource --help` lists 12 subcommands (list, status, add, remove, fix, oauth-status, oauth-reset, log, probe, sync, bootstrap, dispatch-check, patch). **Critical observation**: `hive resource` is a HOST-POOL operations CLI (ssh-direct fleet management), NOT a generic "exec foreign-repo tool" mechanism. It does NOT currently expose `hive resource exec <tool> -- <args>` semantics.
- **Migration plan (PROPOSED, not landed)**:
  - Option A — **add `hive resource exec` subcommand** to host-pool CLI: scope creep (exec is not host-pool-shaped); rejected.
  - Option B — **new `hive cross-repo` CLI namespace** for sister-repo tool dispatch: clean separation, but requires hive raw.mk2 new rule (cross-repo.001) + tool emit + FU cycle. Recommended.
  - Option C — **inline the english-audit tool into n6** (copy `readme_english_audit.hexa` to `~/core/canon/tool/`): violates raw 47 cross-repo SSOT spirit (English-audit logic is hexa-lang's domain); rejected.
  - Option D — **continue grandfather indefinitely**: own#35 enforcement asymmetry persists; not preferred but tolerable while Option B incubates.
- **Recommendation**: defer to Phase 3 (2026-06-01+); Option B requires hive-side rule registration first.

## §4 Per-rule propagation priority

### Priority 1: own#29 readme-friendly-toolkit (cross-repo READMEs benefit)

- Target repos: nexus (369L README, 8 sections declared), anima (259L README, 8 sections declared), hive (251L README, no rules.json).
- Required ports: `tool/own29_multi_section_lint.hexa` (627L FU dispatcher, generalized — already supports per-repo `.readme-rules.json` scopes).
- Dependencies: each target repo needs `.readme-rules.json` with toolkit-table-required scope + 7-col schema.
- Effort: **M** (lint is generalized; per-repo rules.json schema design is the load-bearing work).
- Caveat: nexus/anima sections are domain-specific (nexus 명령어/엔진/OUROBOROS, anima What is Anima/Quick Start/Core Architecture) — toolkit-table extension must layer additively, not replace.

### Priority 2: own#15 paper-canonical-sections

- Target repos: `papers/` (separate repo) — only true papers content host.
- Required ports: `tool/own15_paper_canonical_sections_lint.hexa` (614L FU) + 21-section spec + date-gate constants.
- Effort: **L**. Blocker: papers/anima/PA-0[1-7]*.md use Korean section names + different schema (consciousness research, not n6 invariants). Adoption requires either (a) papers-side schema reconciliation OR (b) own#15 with per-paper-class scope (n6-class vs anima-class section sets).
- Caveat: papers/.papers-cross-repo-lint-exempt already exists in n6 (per predecessor handoff §3.2.11) — n6-side governance must NOT collide with papers-side propagation.

### Priority 3: own#6 paper-3pack-verify-embedded + classifier

- Target repos: `papers/` (only repo with potential python codeblocks in markdown).
- Required ports: own#6 lint (269L) + classifier (647L) + AST visitor (348L). Total 1264 LoC payload.
- Effort: **L**. Depends on own#15 land (needs paper-canonical structure as prerequisite).
- Caveat: classifier + AST visitor are Tier-2 detection (math/physics keyword + Python AST tautology ban). Papers repo uses different domain vocabulary (consciousness/PA-04-phi-boosting); classifier keywords may need domain extension.

### Priority 4: own#14 readme-sealed-required

- Target repos: nexus + anima (BOTH already declare `require_sealed: true` in `.readme-rules.json` — partial inheritance live), hexa-lang + airgenome + hive + papers (no sealed mechanism).
- Required ports: `tool/readme_sealed_check.hexa` (not yet ported anywhere) + per-repo `.readme-rules.json` bootstrap (where missing) + `README.md.sealed.hash` initial hash bootstrap.
- Effort: **S** for nexus/anima (rules.json already declares); **M** for hexa-lang/airgenome/hive/papers (cold start).
- Caveat: nexus/anima `.readme-rules.json` declare `require_sealed: true` but no sealed-check tool exists in their tool/ trees → declaration is currently aspirational. Port priority should match toolkit-table priority (joint Phase 1+2).

## §5 Recommended phasing

- **Phase 1 (next cycle, 2026-05-05 to 2026-05-15)**: own#29 propagation to **nexus + anima** (both already have `.readme-rules.json` ports + sealed declarations). Concrete deliverables: (a) port `tool/own29_multi_section_lint.hexa` to nexus/anima/tool/; (b) extend each `.readme-rules.json` with toolkit-table scope additively; (c) verify with selftest. NO own#15 / own#6 / own#17 migration. Gates Phase 2.
- **Phase 2 (2026-05-15 to 2026-05-31)**: own#14 readme_sealed_check tool port (resolves nexus/anima aspirational-declaration drift) + own#15 land in `papers/` as **n6-class scope only** (PA-papers exempt initially; papers maintainer buy-in required for full coverage).
- **Phase 3 (2026-06-01+)**: hive `cross-repo.001` rule registration (Option B) + own#17 migration from direct path → `hive cross-repo exec readme_english_audit -- ...`; only then resolve own#35 grandfather. own#6 classifier+AST visitor port follows own#15 land in papers/.

## §6 raw#10 honest caveats

1. **Sister repos have divergent governance grammar**: hexa-lang `.own` is self-host scoped; anima `.own` is mk2 frontmatter-only with anima-specific own1-6 (FC+PC triad / σ/τ scalar / GPU dispatch); hive uses `.raw.mk2` JSON-line schema (NOT `.own` format); nexus has no `.own` at all. **n6's `.own` DSL does not literally portably propagate** — propagation means porting the LINT TOOL + per-repo grammar adaptation, not copying `.own.readme` text.
2. **hive `resource` CLI is host-pool ops, not generic exec dispatch**: own#17 migration to `hive resource exec` is NOT immediately viable; requires new hive cross-repo CLI namespace (Option B above) + raw.mk2 rule registration. Phase 3 minimum.
3. **Cross-repo propagation = synchronization burden**: governance spread across 6 repos requires either (a) hive-side dispatch (per arch.001 scope clause "all hive sister repos") OR (b) per-repo maintainer buy-in. arch.001 declares hive as the SSOT for module-architecture rules but does NOT extend coverage to README/paper governance — current raw 47 trawl observes propagation OPPORTUNITY, not propagation MANDATE.
4. **`papers/` (separate repo) divergence**: PA-01..PA-07 papers use Korean section names + consciousness research schema, not n6 invariants schema. own#15 propagation requires per-paper-class scope (multi-schema lint), not single-schema port.
5. **Sealed-hash declaration vs implementation drift**: nexus + anima both declare `require_sealed: true` but neither has `tool/readme_sealed_check.hexa`. Declaration without enforcement is a raw#10 honesty violation pre-existing in sister repos (not n6's drift, but n6 cannot in good conscience propagate without addressing).
6. **Investigation cap**: this doc emits no impl artifacts. Phase numbers are recommendations; user owns sequencing + sister-repo maintainer coordination.
7. **`airgenome/` `papers/` (subdir of papers repo) vs `~/core/papers/` (repo)**: terminology overload — "papers" appears in 3 distinct contexts (n6/papers/ subdir, papers repo root, anima subdir of papers repo). All references in this doc disambiguate explicitly.

## §7 Open questions for user

1. **Phase 1 priority**: agree own#29 → nexus + anima first (highest ready-to-port surface), OR prefer own#14 sealed-check tool port first (resolves aspirational-declaration drift in 2 repos)?
2. **hive cross-repo CLI bootstrap**: who owns adding `hive cross-repo` subcommand namespace + raw.mk2 cross-repo.001 rule? hive-side maintainer cycle, or n6-side proposal-then-handoff to hive?
3. **papers repo coordination**: own#15 + own#6 propagation to `~/core/papers/` requires maintainer buy-in for schema reconciliation (n6-class vs anima-class). Is papers-side coordination in scope this quarter, or defer to 2026-Q3?
4. **own#17 grandfather TTL**: indefinite Option D vs Phase 3 Option B migration — set hard expiry date for grandfather (e.g. 2026-07-01) to force resolution, or let it persist until hive cross-repo CLI lands organically?
5. **sister-repo lint runtime**: bin/hexa-local exists in n6; do nexus/anima/hexa-lang/papers/airgenome/hive each need their own bin/hexa-local for own#29 lint execution, or should hexa-runtime SSOT centralize via hexa-lang (sister #5 of own_lint family already uses tool/own_runner.hexa pattern)?
6. **arch.001 + raw 47 scope reconciliation**: arch.001 declares hive as SSOT for module-architecture rules across "all hive sister repos"; raw 47 says n6 rules CAN propagate. Is paper/README governance under hive arch SSOT (top-down propagation), or n6 SSOT with voluntary sister adoption (bottom-up)?
