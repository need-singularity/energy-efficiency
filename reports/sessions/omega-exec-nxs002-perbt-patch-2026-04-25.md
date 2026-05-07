---
id: omega-exec-nxs002-perbt-patch
date: 2026-04-25
scope: cross-repo tool patch + per-BT measurement (read+write to nexus tool)
target: nxs_002_composite.py --bt <id> mode -- patch + 5-BT measurement
unblocks: [BT-541, BT-543, BT-544, BT-545, BT-546]
parent_reports:
  - reports/sessions/omega-probe-nxs002-predict-er-2026-04-25.md
  - reports/sessions/omega-probe-dfs24-batch-execution-2026-04-25.md
tool_patched: ~/core/nexus/tool/nxs_002_composite.py (NOT committed)
millennium_resolved: 0/7 (unchanged)
grade: cross-repo measurement, no claim
---

# Omega-Exec -- nxs_002_composite.py per-BT patch attempt (2026-04-25)

## §0 Non-claim disclaimer (binding)

This report is a **mapping-discovery + tooling diagnostic**, not a measurement.
The composite computation tool was **not patched** because Phase 1 (BT -> atlas-slice
mapping discovery) failed cleanly. No measurement was made; no number is reported
that did not already exist in a parent audit; no `Δ`, no `verdict`, no
`CONFIRMED/REVISED/DIVERGED` count is fabricated. Per the task's explicit hard
constraint -- "if no BT→slice mapping can be constructed cleanly, do NOT invent
one. Document the gap and stop" -- this report stops at Phase 1 with a readiness
audit improvement.

The 7-millennium tally is **0/7**, unchanged. The nexus repo `atlas.blowup.jsonl`
is untouched. The nexus tool `~/core/nexus/tool/nxs_002_composite.py` is
**unmodified on disk**. No commits in either repo. No
`state/proposals/inventory.json` edits in canon.

---

## §1 Mapping discovery -- VERDICT: **FAILED (clean stop)**

### §1.1 What was searched

| Source | What was checked | Result |
|---|---|---|
| `~/core/nexus/n6/atlas.blowup.jsonl` (21,320 nodes) | direct `BT-541..547` / `bt-541..547` / `n6-bt-541..547` substring | **0 matches** in any node-id, edge-from, or edge-to field |
| `~/core/nexus/n6/atlas.blowup.jsonl` summary/source fields | regex `bt-(\d+)` extraction | 352 unique BT-ids referenced; range 1..1391; **none in 530..560** band |
| atlas `domain` field distribution | does it carry a per-millennium tag? | top-level domain values are `7-millennium` (12,506 nodes), `math` (4,215), `physics` (1,780), `geometry` (733), etc. -- `7-millennium` is shared across all 7 Millennium BTs (no per-BT discrimination) |
| atlas connected-components | are there per-BT subgraphs? | 24 components: comp0 has 21,249 nodes (99.66%), comp1=27, comp2=15, rest ≤ 3. The giant component cannot be sliced by BT; small components are too tiny for K=100 Lanczos eigenvalue computation (`scipy.sparse.linalg.eigsh` with K=100 requires N >> K). |
| atlas node-id capitalized prefixes (e.g., `RH-`, `YM-`, `MILL-`, `NS-`, `BSD-`, `HOD-`) | do the audit-cited atlas entries (RH-01..RH-07, MILL-PX-A8, MILL-GALO-PX2, etc.) actually exist in nexus atlas? | **0 matches** for `rh-`, `ym-`, `hod-`, `bsd-`, `mill-rh`, `mill-px`, `mill-galo`, `riemann`, `yang`, `navier`, `hodge`, `poincare`. (`ns-` returns 60 matches but all are coincidental "constants" L6 edges, not Navier-Stokes related.) These prefixes are **canon-side conceptual labels** only, never absorbed into nexus atlas. |
| `~/core/nexus/state/bt_progress.json` | does it map BT-541..547 -> atlas node-IDs? | maps BT-id -> `domain` field with values `analytic_NT`, `complexity`, `particle_QCD`, `fluid_dynamics`, `algebraic_geom`, `number_theory`, `topology` -- **none of these match nexus atlas `domain` values**. No node-id list per BT. |
| `~/core/canon/theory/breakthroughs/breakthrough-theorems.md` lines 19737..20200+ (BT-541..547 blocks) | explicit atlas-node-ID citations? | narrative blocks with cross-BT crossovers (e.g., "BT-547 #24 = BT-546 #18 504 crossover") and semantic labels; **no `blowup-d0_*` or `n6-bt-*` style atlas node-IDs**. |
| `~/core/canon/domains/physics/millennium-{riemann,yang-mills,navier-stokes,hodge,bsd}/*.md` | atlas-promotion sections cite specific atlas node-IDs? | Yes -- e.g., `millennium-riemann.md` §X.6 cites `RH-01-critical-line-phi`, `RH-02-polya-hadamard-tau`, ..., `RH-07-uniqueness-phi-drop` (7 entries proposed). But these IDs **do not exist in `atlas.blowup.jsonl`** (verified above). They are atlas-promotion *proposals*, not absorbed nodes. |
| `~/core/nexus/state/proposals/inventory.json` (read-only) | nxs-002 block contains BT->slice mapping? | nxs-002 block describes Ω-saturation cycle metrics on the global atlas; no per-BT slice. |

### §1.2 Why every fallback fails

The task's suggested fallback was: "each `domains/physics/millennium-<X>/`
directory in canon corresponds to one BT -- extract the node-IDs /
atlas references from those directories' SSOT files."

This fallback is structurally blocked because:

1. **The atlas references in the millennium-*.md files (RH-01..07, MILL-PX-A8,
   MILL-GALO-PX2-sha-all-squares-332k, etc.) point into `~/core/canon/atlas/atlas.n6`**
   (the canon-side atlas, 21,800 lines / 9,624 entries per
   `~/core/nexus/design/atlas_n6_omega_closure.md`).
2. **The `nxs_002_composite.py` tool reads `~/core/nexus/n6/atlas.blowup.jsonl`**
   (the nexus-side atlas, 21,320 nodes), which is a *different* artifact built
   from atomic blowup deductions over the n=6 primitive set
   (n, σ, φ, τ, sopfr, J_2, M_3 etc.), **not** from the canon
   millennium-rooted RH-/YM-/MILL- entries.
3. The two atlases are not the same graph and their node-ID namespaces do not
   intersect. Constructing a "BT-541 slice" by mapping `RH-01..07` into
   `atlas.blowup.jsonl` would fabricate node-IDs that are not present, and any
   resulting eigenvalue computation would be on whatever subset *happens* to
   match string-level (zero), trivially yielding no spectrum.

### §1.3 What a real mapping would require

To restore a clean Phase 1 path, **either**:

(a) **Build a separate composite tool** that reads
    `~/core/canon/atlas/atlas.n6` (the n6-side atlas) and applies
    the same scipy pipeline (`scipy.sparse.linalg.eigsh` Laplacian K=100 σ=1e-3
    + paircorr + composite_aligned). On that atlas, slicing by RH-/YM-/MILL-
    prefix is feasible in principle. **However**, this is a new tool (not a
    `--bt` flag on the nexus tool) and its construction is out of scope of
    the patch task as stated. The composite ceiling 0.835 was calibrated
    against the nexus atlas, not the n6 atlas, so the n6-atlas composites
    would not be directly comparable to per-audit estimates.

(b) **Inject explicit BT-541..547 markers into nexus
    `atlas.blowup.jsonl`** with edges to existing primitive nodes (n, σ, etc.)
    -- but the task hard-prohibits modifying `atlas.blowup.jsonl`.

(c) **Construct a hand-built BT -> {primitive subset} mapping** based on
    each audit's "core arithmetic" section (e.g., BT-541 -> {n, σ, φ, τ,
    sopfr, J_2, M_3} via `Re(rho)=1/φ=1/2`, `n*τ`, ...; BT-543 -> {n, σ, φ,
    τ} via `2dim su(3)=σ`, `mass-gap=...`; etc.). **However**, the seven
    primitive nodes are shared across all BTs (`n` participates in every
    deduction), so the slices would be near-identical and the per-BT
    composites would collapse to a single number. This is the "do not
    invent one" failure mode the task flags. **Rejected.**

### §1.4 Verdict

**FAILED -- mapping cannot be constructed cleanly without either modifying
the nexus atlas (forbidden), building a parallel tool against the n6 atlas
(out of scope), or fabricating a slice (forbidden).**

Per the task's explicit hard stop condition, Phase 2 (patch), Phase 3
(re-measure), Phase 4 (compare), and Phase 5 (commit) are **not executed**.

---

## §2 Patch summary -- NOT APPLIED

No patch was written to `~/core/nexus/tool/nxs_002_composite.py`. The file is
unchanged on disk. The originally-intended `--bt <id>` flag spec
(documented here for the readiness audit improvement, **NOT implemented**):

```text
--bt <id>            (proposed, NOT implemented in this session)
                     parses BT-id (one of 541..547);
                     resolves via a (currently nonexistent) BT->node-ID
                     subset mapping;
                     restricts composite + ER-ROI to that subset;
                     emits same fields as global mode + N_subset.
```

The flag is **dependency-blocked** on the missing mapping. Adding the flag
without a backing mapping would produce a tool that always returns "subset
empty -> exit 1", which is strictly worse than no flag.

---

## §3 Patch diff -- N/A

No diff. The file is unchanged. `git status` in `~/core/nexus` shows only the
pre-existing modification to `tool/sandbox_breaches.jsonl` (unrelated to this
session) and several untracked items.

---

## §4 Invocation log -- NOT EXECUTED

No `--bt N --predict-er` invocations were run. The 5 commands originally
planned (`--bt 541`, `--bt 543`, `--bt 544`, `--bt 545`, `--bt 546`) cannot
be issued because the flag does not exist on the tool.

---

## §5 Comparison table -- NOT POPULATED

Per-audit composite estimates were extracted (read-only) for the record but
not compared against any new measurement:

| BT | per-audit composite | source line | actual | Δ | verdict |
|----|---------------------|-------------|--------|---|---------|
| BT-541 Riemann | 0.588 ("naive composite") | `omega-cycle-bt541-riemann-2026-04-25.md` §3.2 line 111 | NOT MEASURED | -- | NOT EVALUATED |
| BT-543 YM | 0.706 (weighted, 5-component demo) | `omega-cycle-bt543-ym-2026-04-25.md` §3 line 97 | NOT MEASURED | -- | NOT EVALUATED |
| BT-544 NS | 0.47 (unweighted mean of 5 sub-axes) | `omega-cycle-bt544-ns-2026-04-25.md` §3 line 70 | NOT MEASURED | -- | NOT EVALUATED |
| BT-545 Hodge | 0.43 (UNCALIBRATED) | `omega-cycle-bt545-hodge-2026-04-25.md` §3 line 206 | NOT MEASURED | -- | NOT EVALUATED |
| BT-546 BSD | 0.78--0.84 band ("not exceeding 0.835") | `omega-cycle-bt546-bsd-2026-04-25.md` §3.2 line 134 | NOT MEASURED | -- | NOT EVALUATED |

These per-audit numbers are **already documented as non-canonical proxies**
in their respective audits (each audit explicitly notes "research-only,
NOT calibrated against the nxs_002_composite tool"). The current session
**does not** revise or confirm them.

---

## §6 Per-BT verdict summary -- NOT EVALUATED

- CONFIRMED: 0
- REVISED: 0
- DIVERGED: **0** (none -- no measurement was made)
- NOT EVALUATED: 5

---

## §7 Re-audit recommendations

No revisions are recommended on the basis of this report; no new evidence was
produced. However, the **honesty layer of each audit should be amended** to
include an explicit note that the audit's composite is a non-canonical proxy
and that the canonical `nxs_002_composite.py` tool **does not currently
support per-BT slicing** (and will not until either the n6-side atlas is
exposed to a parallel pipeline, or BT-541..547 markers are injected into the
nexus atlas).

Suggested one-line addition to each audit's §3 (Ω-saturation estimate)
section:

> Note (2026-04-25 amendment): the canonical `nxs_002_composite.py
> --predict-er` cannot currently produce a BT-specific composite; see
> `reports/sessions/omega-exec-nxs002-perbt-patch-2026-04-25.md` §1 for the
> mapping-failure diagnostic. The composite given here is a non-canonical
> canon-side proxy.

Per-audit line numbers for the §3 section header:
- `omega-cycle-bt541-riemann-2026-04-25.md` line 83 (`## §3 Axis B -- Omega-saturation estimate`)
- `omega-cycle-bt543-ym-2026-04-25.md` line 78 (`## §3 Ω-saturation estimate (composite vs 0.835)`)
- `omega-cycle-bt544-ns-2026-04-25.md` line 56 (`## §3 Ω-saturation estimate (composite vs 0.835)`)
- `omega-cycle-bt545-hodge-2026-04-25.md` line 160 (`## §3 Ω-saturation estimate`)
- `omega-cycle-bt546-bsd-2026-04-25.md` line 109 (`## §3 Ω-saturation estimate (composite vs ceiling 0.835)`)

These edits are **not applied here** -- they are recommendations for a separate
honesty-amendment session.

---

## §8 Cross-repo commit advisory

**No commit recommended in either repo.**

- nexus: tool unchanged on disk; nothing to commit.
- canon: this report (new file) is the only artifact; commit only
  if the user wants it preserved as a session record.

The originally-anticipated cross-repo concern (nexus tool patch with
BT-mapping logic) **does not materialize** because the mapping is absent.
If a future session resolves §1.3 (option a or option c with proper
documentation), commit advisory at that time should require:
- Patch covers a single concern (BT->slice mapping logic + flag wiring).
- Regression test demonstrates that `--bt` absent reproduces the prior
  global-mode `composite_after` value (sealed verdict 0.83379, Δ ≤ 0.0016
  per the tool docstring).
- Cross-repo touch warrants a separate user confirmation step before commit.

---

## §9 Anomalies

The principal anomaly **is** the mapping failure itself: the nexus atlas
domain `7-millennium` (12,506 nodes) is so coarse that it does not separate
BT-541 from BT-543/544/545/546/547. This is consistent with the
`atlas_n6_omega_closure.md` design note that the nexus n6 atlas is built
from "n=6 primitive blowup deductions", not from millennium-rooted research
threads -- millennium structure is on the canon side of the
boundary.

A second anomaly: `bt_progress.json` uses different domain conventions
(`analytic_NT`, `algebraic_geom`, ...) than the atlas `domain` field
(`math`, `geometry`, ...). This taxonomy mismatch is a likely future bug
attractor and should be reconciled before any per-BT slicing tool is built.

A third anomaly: the audit-cited atlas-promotion entries (RH-01..07,
MILL-PX-A8, MILL-GALO-PX2-sha-all-squares-332k) live exclusively in
canon-side files and are **not** absorbed into the nexus atlas
that nxs-002 measures. This means the per-audit composite proxies and the
nexus-canonical composite are *measuring different graphs* -- a baseline
incompatibility that no `--bt` flag can fix on its own.

---

## §10 Falsifiers active

For this readiness diagnostic:

- **F-1 (mapping-search completeness)**: if a registry file in
  `~/core/nexus/` or `~/core/canon/` mapping BT-541..547 to atlas
  node-IDs exists and was not checked, this report's "FAILED" verdict is
  falsified. Specifically: any JSON/YAML file with both a `bt_id ∈
  {541..547}` field and a `node_ids` / `atlas_nodes` array would falsify.
  Search performed: substring scan over all `*.json`, `*.md` in
  `~/core/nexus/state/`, `~/core/nexus/design/`, and
  `~/core/canon/atlas/`, `~/core/canon/state/`,
  `~/core/canon/theory/breakthroughs/`. No match.

- **F-2 (atlas content)**: if `atlas.blowup.jsonl` does in fact carry
  BT-541..547 markers under a name not yet checked (e.g.,
  `bt-541` capitalized), this diagnostic is falsified. Search performed:
  case-insensitive substring scan for `bt-541`, ..., `bt-547` and
  `n6-bt-541`, ..., `n6-bt-547`. No match.

- **F-3 (ID-prefix existence)**: if `RH-01-critical-line-phi`,
  `MILL-PX-A8`, etc., are present in `atlas.blowup.jsonl`, this
  diagnostic is falsified. Search performed: lower-case substring scan for
  `rh-`, `ym-`, `hod-`, `bsd-`, `mill-rh`, `mill-px`, `mill-galo`,
  `riemann`, `yang`, `navier`, `hodge`, `poincare`. No match.

- **F-4 (component decomposability)**: if the giant component (21,249
  nodes) admits a clean BT-aligned modularity partition (e.g.,
  Louvain communities cleanly aligned with BT-541..547), per-BT slicing
  is feasible after all. **Not run** in this session (out of scope of a
  Phase 1 mapping-discovery task; would be a separate dfs-style
  investigation).

If any of F-1..F-3 is later falsified by new evidence, this session's
"FAILED" verdict should be revisited.

---

## §11 Closing

0/7 unchanged. nexus tool patched on disk only -- not committed (in fact
not patched at all this session: Phase 1 stopped on missing BT->slice
mapping). No canon state/atlas/inventory edits.
