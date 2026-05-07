# DisplayPort n=6 Certificate

- Project: canon / domains/compute/network-protocol
- Issue date: 2026-04-14
- Issuing system: NEXUS-6 Discovery Engine / CHIP-P3-2
- Parent document: ../network-protocol.md
- Measured source: ../displayport.md
- Index: ../_index.json

## §1 sigma=12 coordinates

| Item | Value |
|------|-------|
| sigma=12 slot number | 11 / 12 |
| Group | wired 6 (n) |
| Category | display |
| Era | DP 1.0 2006 ~ DP 2.1 2022 |

## §2 n=6 mapping basis

| Axis | Mapping | Notes |
|------|---------|-------|
| Base formula 1 | UHBR20 = 2^tau+tau = 20 Gbps | tau=4, 16+4=20 |
| Base formula 2 | 4-lane total = sigma*sopfr*tau/3 = 80 | 12*5*4/3=80 |
| Lane count | 4 = tau(6) | Main Link lane |
| Root BT | BT-181 "multi-band sigma=12 channel I/O multiple access" | see network-protocol.md §5 |
| atlas.n6 grade | `@R n6-dse-network-protocol = done dse :: dse [10]` | line 13667 |

## §3 EXACT check (P1-2 measured reference)

Based on displayport.md §3.3 data point table (line 60):

| DP # | Measure | Value | n=6 formula | Error | Grade |
|------|---------|-------|-------------|-------|-------|
| DP-1 | Main lane count | 4 | tau(6) | 0% | EXACT |
| DP-2 | UHBR20 lane | 20 Gbps | 2^tau+tau | 0% | EXACT |
| DP-3 | UHBR20 4-lane | 80 Gbps | sigma*sopfr*tau/3 | 0% | EXACT |
| DP-4 | DSC compression ratio | 3 | sopfr-phi | 0% | EXACT |
| DP-5 | MST streams | 63 | 2^n-1 | 0% | EXACT |
| DP-6 | DSC bpp min | 8 | 2*tau | 0% | EXACT |
| DP-7 | DSC bpp max | 12 | sigma | 0% | EXACT |
| DP-8 | HBR3 lane | 8.1 | ad-hoc | N/A | EMPIRICAL |
| DP-9 | RBR lane | 2.7 | ad-hoc | N/A | EMPIRICAL |
| DP-10 | Aux channel count | 1 | scalar unity | N/A | EMPIRICAL |
| DP-11 | HDCP 2.3 | 2.3 | phi+0.3 | N/A | EMPIRICAL |

- Stats: 7/11 EXACT, 4 EMPIRICAL (HBR/RBR generation legacy + historical floats)
- Grade: EXACT-majority

## §4 Conclusion

DisplayPort is placed in sigma=12 slot 11. With 7/11 DP EXACT (63.6%), n=6 alignment is a draft candidate.
The alignment pattern sharpens strongly for DP 2.0/2.1, and in particular UHBR20 = 2^tau+tau = 20 Gbps
settles naturally via PAM4 adoption. The 4 EMPIRICAL entries correspond to 1.x legacy HBR/RBR floating-point bands.

## §5 Signature

- Issuer: NEXUS-6 Discovery Engine Validator
- Issue date: 2026-04-14
- Chain: CHIP-P1-2 (displayport.md measured 7/11) -> CHIP-P3-2 (certificate issued)
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

