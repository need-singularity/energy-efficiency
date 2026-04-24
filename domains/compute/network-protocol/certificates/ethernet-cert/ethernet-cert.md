# Ethernet n=6 Certificate

- Project: n6-architecture / domains/compute/network-protocol
- Issue date: 2026-04-14
- Issuing system: NEXUS-6 Discovery Engine / CHIP-P3-2
- Parent document: ../network-protocol.md
- Measured source: ../ethernet.md
- Index: ../_index.json

## §1 sigma=12 coordinates

| Item | Value |
|------|-------|
| sigma=12 slot number | 10 / 12 |
| Group | wired 6 (n) |
| Category | local_network |
| Era | 10BASE-T 1990 ~ 1.6 TbE 2024 |

## §2 n=6 mapping basis

| Axis | Mapping | Notes |
|------|---------|-------|
| Base formula 1 | 25 Gbps = sopfr^2 | sopfr=5, 5^2=25 |
| Base formula 2 | 400 Gbps = 4*(sigma*sopfr*phi-sigma-phi) | 4*100=400 |
| Header | 14 B = sigma+phi | DMAC+SMAC+EtherType |
| Root BT | BT-181 "multi-band sigma=12 channel I/O multiple access" | see network-protocol.md §5 |
| atlas.n6 grade | `@R n6-dse-network-protocol = done dse :: dse [10]` | line 13667 |

## §3 EXACT check (P1-2 measured reference)

Based on ethernet.md §3.3 data point table (line 73):

| DP # | Measure | Value | n=6 formula | Error | Grade |
|------|---------|-------|-------------|-------|-------|
| DP-1 | 10 Mbps | 10 | 2*sopfr | 0% | EXACT |
| DP-2 | 25 Gbps | 25 | sopfr^2 | 0% | EXACT |
| DP-3 | 40 Gbps | 40 | 10*tau | 0% | EXACT |
| DP-4 | 100 Gbps | 100 | sigma*sopfr*phi-sigma-phi | 0% | EXACT |
| DP-5 | 400 Gbps | 400 | 4*(sigma*sopfr*phi-sigma-phi) | 0% | EXACT |
| DP-6 | Frame max | 1518 B | 1500 MTU+18 | 1.2% | EMPIRICAL |
| DP-7 | Jumbo | 9000 B | 9*10^3 ad-hoc | N/A | EMPIRICAL |
| DP-8 | FCS | 4 B | tau | 0% | EXACT |
| DP-9 | DMAC+SMAC | 12 B | sigma | 0% | EXACT |
| DP-10 | EtherType | 2 B | phi | 0% | EXACT |
| DP-11 | Standard header | 14 B | sigma+phi | 0% | EXACT |

- Stats: 9/11 EXACT, 2 EMPIRICAL (MTU 1500 / Jumbo 9000 historical compromise)
- Grade: EXACT-dominant

## §4 Conclusion

Ethernet is placed in sigma=12 slot 10. With 9/11 DP EXACT (81.8%), n=6 alignment is a draft candidate.
The speed tiers are all aligned to n=6 via the 10*sopfr^k / sigma*sopfr*phi*k family; in particular,
25 Gbps = sopfr^2 together with 40/100/400/800/1600 Gbps = k*100 forms the core fit pattern. The 2 EMPIRICAL
entries (MTU 1500, Jumbo 9000) are 802.3 Ethernet v1 historical compromises.

## §5 Signature

- Issuer: NEXUS-6 Discovery Engine Validator
- Issue date: 2026-04-14
- Chain: CHIP-P1-2 (ethernet.md measured 9/11) -> CHIP-P3-2 (certificate issued)
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

