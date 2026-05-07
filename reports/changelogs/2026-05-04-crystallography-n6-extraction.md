# crystallography_n6 — extracted from nexus → canon

**Date**: 2026-05-04
**Source**: `nexus/modules/crystallography_n6/` (rank-1 candidate, score 9)
**Destination**: `domains/physics/crystallography/`
**Audit**: `anima/docs/nexus_module_extraction_audit_2026_05_04.md`

## What landed

| File | LoC | Note |
|------|----:|------|
| `domains/physics/crystallography/crystallography_n6.hexa` | 402 | Pure-hexa enumerator (Fedorov 230 / Bravais 14 / 7 systems / 32 pt-groups) |
| `domains/physics/crystallography/crystallography_n6.README.md` | ~50 | Usage + falsifiers |

Co-located with existing `crystallography.md` research spec.

## n=6 closed-form anchors

- F1: Fedorov-230  = sigma·J₂ - J₂·phi - (sigma-phi) = 12·24 - 24·2 - 10 = **230**
- F2: Bravais-14   = phi·(sopfr+phi) = sigma+phi = **14**
- F3: systems-7    = sopfr+phi = **7**
- F4: |O_h|=48     = sigma·tau = **48**
- F5: 32 pt groups = J₂ + sigma - tau = 24 + 12 - 4 = **32**
- F6: max axis-6   = n = **6**

All match IUCr canonical counts.

## Smoke test (run from this repo)

```
$ hexa run domains/physics/crystallography/crystallography_n6.hexa --self-test
=== crystallography_n6 --self-test ===
  case1 (full enumerate)   : systems=7 bravais=14 space=230 pt=32 status=PASS:n6-locked
  case2 (atlas_facts len)  : len=6
  case3 (unknown system)   : status=FAIL:unknown-system
  case4 (closed-form math) : sigma=12 tau=4 phi=2 sopfr=5 J_2=24 → identities=PASS
  case5 (cubic only)       : bravais=3 space=36 pt=5
  case1=PASS case2=PASS case3=PASS case4=PASS case5=PASS
__CRYSTALLOGRAPHY_N6__ PASS
```

## Consumer impact

Pre-extraction grep across nexus + anima + hive + canon: **0 functional
consumers** of `nexus/modules/crystallography_n6/` (only audit-doc references).
No nexus-side refactor needed beyond directory removal.

## Caveats (raw#10)

1. Scoring is subjective; activity-weighted ranking would re-shuffle.
2. Ranking depends on nexus monolith-vs-orchestrator direction.
3. Each new repo addition increases dual-mirror burden (GitHub already PUBLIC).
4. Audit may miss hidden coupling channels not surfaced by string grep.
