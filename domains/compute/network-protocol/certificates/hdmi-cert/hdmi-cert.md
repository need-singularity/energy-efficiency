# HDMI n=6 Certificate

- Project: n6-architecture / domains/compute/network-protocol
- Issue date: 2026-04-14
- Issuing system: NEXUS-6 Discovery Engine / CHIP-P3-2
- Parent document: ../network-protocol.md
- Measured source: ../hdmi.md
- Index: ../_index.json

## §1 sigma=12 coordinates

| Item | Value |
|------|-------|
| sigma=12 slot number | 12 / 12 |
| Group | wired 6 (n) — tail |
| Category | display |
| Era | HDMI 1.0 2002 ~ HDMI 2.2 2025 draft |

## §2 n=6 mapping basis

| Axis | Mapping | Notes |
|------|---------|-------|
| Base formula 1 | HDMI 2.1 FRL 48 Gbps = sigma*tau | 12*4=48 |
| Base formula 2 | HDMI 2.1 lane = sigma = 12 Gbps | Direct correspondence |
| Lane count | 4 = tau(6) | FRL lane |
| Root BT | BT-181 "multi-band sigma=12 channel I/O multiple access" | see network-protocol.md §5 |
| atlas.n6 grade | `@R n6-dse-network-protocol = done dse :: dse [10]` | line 13667 |

## §3 EXACT check (P1-2 measured reference)

Based on hdmi.md §3.3 data point table (line 64):

| DP # | Measure | Value | n=6 formula | Error | Grade |
|------|---------|-------|-------------|-------|-------|
| DP-1 | FRL lane count | 4 | tau | 0% | EXACT |
| DP-2 | TMDS data channels | 3 | sopfr-phi | 0% | EXACT |
| DP-3 | HDMI 2.1 lane | 12 Gbps | sigma | 0% | EXACT |
| DP-4 | HDMI 2.1 total | 48 Gbps | sigma*tau | 0% | EXACT |
| DP-5 | HDMI 2.0 lane | 6 Gbps | n | 0% | EXACT |
| DP-6 | HDMI 2.0 total | 18 Gbps | n*sopfr-sigma | 0% | EXACT |
| DP-7 | DSC compression ratio | 3 | sopfr-phi | 0% | EXACT |
| DP-8 | Max color depth | 16 | 2^tau | 0% | EXACT |
| DP-9 | Max audio channels | 32 | 2^tau*phi | 0% | EXACT |
| DP-10 | CEC version | 2.0 | phi | 0% | EXACT |
| DP-11 | HDMI 1.4 lane | 3.4 Gbps | ad-hoc | N/A | EMPIRICAL |

- Stats: 10/11 EXACT, 1 EMPIRICAL (HDMI 1.x legacy TMDS 3.4 Gbps)
- Grade: EXACT-dominant

## §4 Conclusion

HDMI is placed in sigma=12 slot 12 (wired tail). With 10/11 DP EXACT (90.9%), n=6 alignment is a draft candidate.
The dual fit of HDMI 2.1 FRL 48 Gbps = sigma*tau with lane 12 Gbps = sigma forms the core pattern and
is naturally realized through FRL 16b/18b line coding adoption. The 1 EMPIRICAL entry is HDMI 1.x legacy.

## §5 Signature

- Issuer: NEXUS-6 Discovery Engine Validator
- Issue date: 2026-04-14
- Chain: CHIP-P1-2 (hdmi.md measured 10/11) -> CHIP-P3-2 (certificate issued)
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

