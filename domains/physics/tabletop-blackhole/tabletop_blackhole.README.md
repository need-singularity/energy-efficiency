# tabletop_blackhole

BEC analog Hawking-temperature simulator (Steinhauer 2014). Verifies n=6
closure of B_trap=48T, L_h=10μm, c_s=48 mm/s, T_H=0.5 nK against
sigma·tau=48, sigma−phi=10, sigma/(tau·n)=0.5 closed forms. Stdlib only
(hexa).

**Origin**: extracted 2026-05-04 from `nexus/modules/tabletop_blackhole/`
(rank-2 Phase-2 candidate per
`anima/state/nexus_module_extraction_audit_phase2_2026_05_04/`,
ZERO_COLLISION). Co-located with `tabletop-blackhole.md` research spec
(TBHL-01..08).

Source SHA: nexus@bcadbf6d (modules/tabletop_blackhole/).

## Anchors (n=6 locked)

- `B_trap = sigma·tau = 48 T` (superconducting magnetic trap)
- `L_h    = sigma−phi = 10 μm` (sonic event horizon length)
- `c_s    = sigma·tau = 48 mm/s` (BEC sound speed)
- `T_H    = sigma/(tau·n) = 0.5 nK` (Hawking analog temperature)

## CLI

```sh
hexa run domains/physics/tabletop-blackhole/tabletop_blackhole.hexa --self-test
hexa run domains/physics/tabletop-blackhole/tabletop_blackhole.hexa --json
hexa run domains/physics/tabletop-blackhole/tabletop_blackhole.hexa --anchors
```

## Self-test

```
$ hexa run domains/physics/tabletop-blackhole/tabletop_blackhole.hexa --self-test
... __TABLETOP_BLACKHOLE__ PASS
```

3-case self-check: locked (n=6 anchors), off-lock (B=1T → OFFLOCK
diagnostic), edge input (N<0 → FAIL:input).

## Falsifiers

- `B_trap != sigma·tau` (48 T) → OFFLOCK flagged
- `L_horizon != sigma−phi` (10 μm) → OFFLOCK flagged
- `c_sound != sigma·tau` (48 mm/s) → OFFLOCK flagged
- `T_H != sigma/(tau·n)` (0.5 nK) → OFFLOCK flagged
- `N_atoms <= 0` or `L_horizon <= 0` → input rejection
- `lifetime_consistent` flips False if `T_H · n_modes` contradicts `tau_BH`

## Reference

n=6 closure per `domains/physics/tabletop-blackhole/tabletop-blackhole.md`
TBHL-01..08. Empirical anchor: Steinhauer 2014 (BEC analog Hawking
phonon observation).
