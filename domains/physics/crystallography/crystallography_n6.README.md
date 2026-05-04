# crystallography_n6

Pure integer enumeration of Fedorov 230 / 14 Bravais / 7 crystal systems / 32
point groups against n=6 closed forms.  Stdlib only (hexa).

**Origin**: extracted 2026-05-04 from `nexus/modules/crystallography_n6/`
(rank-1 candidate per `anima/docs/nexus_module_extraction_audit_2026_05_04.md`,
score 9). Co-located with `crystallography.md` research spec.

## Sample run

```
$ hexa run domains/physics/crystallography/crystallography_n6.hexa --system cubic
selected_system    = cubic
  cubic : bravais=3 space_groups=36 point_groups=5
total_bravais      = 3
total_space_groups = 36
total_point_groups = 5
falsifier_status   = PASS:n6-locked

$ hexa run domains/physics/crystallography/crystallography_n6.hexa --atlas
@F CRYSTAL-N6-01 fedorov-230-closure = sigma*J_2 - J_2*phi - (sigma-phi) = 230 :: crystallography [10]
@F CRYSTAL-N6-02 bravais-14 = phi*(sopfr+phi) = sigma+phi = 14 :: crystallography [10]
@F CRYSTAL-N6-03 systems-7 = sopfr+phi = 7 :: crystallography [10]
@F CRYSTAL-N6-04 octahedral-Oh-order = sigma*tau = 48 :: crystallography [10]
@F CRYSTAL-N6-05 point-groups-32 = J_2 + sigma - tau = 32 :: crystallography [10]
@F CRYSTAL-N6-06 max-rotation-axis = n = 6 :: crystallography [10]
```

## Self-test

```
$ hexa run domains/physics/crystallography/crystallography_n6.hexa --self-test
... __CRYSTALLOGRAPHY_N6__ PASS
```

5-case self-check: full enumerate, atlas_facts len==6, unknown-system rejection,
closed-form arithmetic identities, single-system query (cubic).

## Falsifiers (vs official IUCr counts)

- F1: Fedorov space-group count != 230 -> closure retracted
- F2: Bravais lattice count   != 14  -> phi-extension retracted
- F3: crystal-system count    != 7   -> sopfr+phi retracted
- F4: |O_h|                    != 48  -> sigma*tau retracted
- F5: 32 point groups          != 32 -> J_2+sigma-tau retracted
- F6: max crystallographic axis != 6 -> restriction theorem retracted

The `--atlas` output lists the 6 closed-form facts as DSL-ready
`@F CRYSTAL-N6-01..06 :: crystallography [10]` lines for human review.  This
module does NOT write to atlas.n6 or any shard.

## Reference

n=6 closure per `domains/physics/crystallography/crystallography.md` §X.5.
