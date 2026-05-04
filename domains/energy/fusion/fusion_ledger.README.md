# fusion_ledger

ITER + n=6 fusion design-constants verifier. Verifies 27 measured constants
against closed-form n=6 expressions (sigma, tau, phi, sopfr, J2, n, mu)
within per-entry tolerance. Stdlib only (hexa).

**Origin**: extracted 2026-05-04 from `nexus/modules/fusion_ledger/`
(rank-1 Phase-2 candidate per
`anima/state/nexus_module_extraction_audit_phase2_2026_05_04/`,
ZERO_COLLISION). Co-located with `fusion.md` research spec +
`verify_fusion.hexa` predecessor.

Source SHA: nexus@bcadbf6d (modules/fusion_ledger/).

## Anchors

`sigma=12, tau=4, phi=2, sopfr=5, J2=24, n=6, mu(6)=1`. Master identity:
`σ·φ = n·τ = J₂ = 24`. Fuel mass numbers encode directly:
`D = phi (A=2)`, `T = n/phi (A=3)`, `alpha = tau (A=4)`.

## CLI

```sh
hexa run domains/energy/fusion/fusion_ledger.hexa --self-test
hexa run domains/energy/fusion/fusion_ledger.hexa --verify
```

## Self-test

```
$ hexa run domains/energy/fusion/fusion_ledger.hexa --self-test
... __FUSION_LEDGER__ PASS total=27 matched=26 falsified=1 pct=96.2963
```

5-check self-test: master identity, total==27, match >=80%,
lawson_triple in falsified list (HONESTY guard), exact 26/27 (no inflation).

## Falsifier list

1. **Per-constant match** within `tolerance` (relative; `tol=0.0` requires
   sub-ULP equality). Mismatches go into `falsified`.
2. **Master identity** `sigma*phi == n*tau == J2` asserted in `_self_test`.
3. **Threshold**: `_self_test` requires `n6_match_pct >= 80%` to PASS.
4. **HONESTY guard**: `lawson_triple_keV_s_per_m3` MUST remain in falsified
   list (one-decade gap preserved; measured 5.6e21 vs n=6 closed-form 5.6e20).
5. **Match-count drift**: matched MUST equal exactly 26 (not 27 — no
   silent inflation).

## Honesty / source-vs-impl gap

The `lawson_triple` entry is falsified by one decade and intentionally
preserved as such to honor the source-as-found principle. The packaged
ledger encodes 27 verifiable constants drawn from `fusion.md` §4/§7/§8
+ `verify_fusion.hexa` (11 EXACT items). Honest 26/27 = 96.3% match.

## Data

The .hexa source uses an inline 27-entry table for runtime — fully
self-contained, no external file load. A canonical JSON mirror
(`iter_constants.json`, 250 LoC) lives at `nexus/modules/fusion_ledger/data/`
for external review (n6-arch `.gitignore` excludes `data/` by default;
the JSON is preserved at the nexus side and may be re-added under a
non-`data/` path in a follow-up if external overrides become needed).

## Reference

n=6 closure per `domains/energy/fusion/fusion.md` §4/§7/§8 + 11-EXACT items
in `verify_fusion.hexa`.
