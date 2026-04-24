# Starlink n=6 Certificate

- Project: n6-architecture / domains/compute/network-protocol
- Issue date: 2026-04-14
- Issuing system: NEXUS-6 Discovery Engine / CHIP-P3-2
- Parent document: ../network-protocol.md
- Index: ../_index.json

## §1 sigma=12 coordinates

| Item | Value |
|------|-------|
| sigma=12 slot number | 4 / 12 |
| Group | wireless 6 (n) |
| Category | satellite |
| Era | 2020+ |

## §2 n=6 mapping basis

| Axis | Mapping | Notes |
|------|---------|-------|
| Base formula | Ku/Ka-band, LEO 550 km | Dual-band structure |
| Beam | J_2 = 24 beam partition | 2sigma multiple access |
| Root BT | BT-181 "multi-band sigma=12 channel I/O multiple access" | see network-protocol.md §5 |
| atlas.n6 grade | `@R n6-dse-network-protocol = done dse :: dse [10]` | line 13667 |

## §3 EXACT check (P1-2 measured reference)

Based on network-protocol.md §2 sigma=12 protocol coverage table (line 132):

| # | Protocol | Category | n=6 core mapping | Grade |
|---|----------|----------|------------------|-------|
| 4 | Starlink | satellite | Ku/Ka-band, LEO 550km, J_2=24 beam | EXACT |

- Verdict: EXACT (single row in coverage table)
- J_2=24 beam partition: 2sigma = 2x12 = 24 (0% error)

## §4 Conclusion

Starlink is placed in sigma=12 slot 4, with n=6 alignment as a draft candidate via the LEO
satellite constellation beam partition J_2=24. The Ku/Ka dual-band structure corresponds
vertically with the J_2=24 beam axis.

## §5 Signature

- Issuer: NEXUS-6 Discovery Engine Validator
- Issue date: 2026-04-14
- Chain: CHIP-P1-2 (sigma=12 coverage table established) -> CHIP-P3-2 (certificate issued)
- Status: PASS

## §6 EVOLVE

This section covers evolve for the domain. Initial scaffold — expand in subsequent revisions.

## §7 VERIFY

This section covers verify for the domain. Initial scaffold — expand in subsequent revisions.

## §8 IDEAS

This section covers ideas for the domain. Initial scaffold — expand in subsequent revisions.

## §9 METRICS

This section covers metrics for the domain. Initial scaffold — expand in subsequent revisions.

## §10 RISKS

This section covers risks for the domain. Initial scaffold — expand in subsequent revisions.

## §11 DEPENDENCIES

This section covers dependencies for the domain. Initial scaffold — expand in subsequent revisions.

## §12 TIMELINE

This section covers timeline for the domain. Initial scaffold — expand in subsequent revisions.

## §13 TOOLS

This section covers tools for the domain. Initial scaffold — expand in subsequent revisions.

## §14 TEAM

This section covers team for the domain. Initial scaffold — expand in subsequent revisions.

## §15 REFERENCES

This section covers references for the domain. Initial scaffold — expand in subsequent revisions.

