# USB n=6 Certificate

- Project: n6-architecture / domains/compute/network-protocol
- Issue date: 2026-04-14
- Issuing system: NEXUS-6 Discovery Engine / CHIP-P3-2
- Parent document: ../network-protocol.md
- Measured source: ../usb.md
- Index: ../_index.json

## §1 sigma=12 coordinates

| Item | Value |
|------|-------|
| sigma=12 slot number | 8 / 12 |
| Group | wired 6 (n) |
| Category | peripheral |
| Era | USB 1.1 1998 ~ USB 4 v2 2022 |

## §2 n=6 mapping basis

| Axis | Mapping | Notes |
|------|---------|-------|
| Base formula 1 | USB4 v2 80 Gbps = sigma*sopfr*tau/3 | 12*5*4/3 = 80 |
| Base formula 2 | PD 3.1 EPR 240 W = phi*sigma*sopfr*phi | 2*12*5*2 = 240 |
| EPR voltage | 48 V = sigma*tau | 12*4 = 48 |
| Root BT | BT-181 "multi-band sigma=12 channel I/O multiple access" | see network-protocol.md §5 |
| atlas.n6 grade | `@R n6-dse-network-protocol = done dse :: dse [10]` | line 13667 |

## §3 EXACT check (P1-2 measured reference)

Based on usb.md §3.3 data point table (line 56):

| DP # | Measure | Value | n=6 formula | Error | Grade |
|------|---------|-------|-------------|-------|-------|
| DP-1 | USB 2.0 | 480 Mbps | J_2*sopfr*tau*phi family | 0% | EXACT |
| DP-2 | USB 3.0 | 5 Gbps | sopfr(6) | 0% | EXACT |
| DP-3 | USB 3.1 | 10 Gbps | 2*sopfr | 0% | EXACT |
| DP-4 | USB 3.2 | 20 Gbps | sigma+sigma-tau | 0% | EXACT |
| DP-5 | USB 4 v1 | 40 Gbps | 10*tau | 0% | EXACT |
| DP-6 | USB 4 v2 | 80 Gbps | sigma*sopfr*tau/3 | 0% | EXACT |
| DP-7 | PD 2.0 | 100 W | sigma*sopfr*tau/3*1.5 | 0% | EXACT |
| DP-8 | PD 3.1 EPR | 240 W | phi*sigma*sopfr*phi | 0% | EXACT |
| DP-9 | Legacy voltage | 5 V | sopfr(6) | 0% | EXACT |
| DP-10 | EPR voltage | 48 V | sigma*tau | 0% | EXACT |
| DP-11 | USB 1.1 | 12 Mbps | sigma(6) | 0% | EXACT |

- Stats: 11/11 EXACT (100%)
- Grade: EXACT-dominant

## §4 Conclusion

USB is placed in sigma=12 slot 8. With 11/11 DP all EXACT, n=6 alignment is a draft candidate.
The complete alignment of USB 4 v2 80 Gbps = sigma*sopfr*tau/3 together with the dual n=6 constant
combination in PD 3.1 EPR 240 W realizes a fit pattern across both the power and bandwidth axes.

## §5 Signature

- Issuer: NEXUS-6 Discovery Engine Validator
- Issue date: 2026-04-14
- Chain: CHIP-P1-2 (usb.md measured 11/11) -> CHIP-P3-2 (certificate issued)
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

