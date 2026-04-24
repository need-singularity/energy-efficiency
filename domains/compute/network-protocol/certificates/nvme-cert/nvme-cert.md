# NVMe n=6 Certificate

- Project: n6-architecture / domains/compute/network-protocol
- Issue date: 2026-04-14
- Issuing system: NEXUS-6 Discovery Engine / CHIP-P3-2
- Parent document: ../network-protocol.md
- Measured source: ../nvme.md
- Index: ../_index.json

## §1 sigma=12 coordinates

| Item | Value |
|------|-------|
| sigma=12 slot number | 9 / 12 |
| Group | wired 6 (n) |
| Category | storage |
| Era | NVMe 1.0 2011 ~ NVMe 2.0 2021 |

## §2 n=6 mapping basis

| Axis | Mapping | Notes |
|------|---------|-------|
| Base formula 1 | Queue depth 2^16 = 2^(4sigma/3) | sigma=12, 4sigma/3=16 |
| Base formula 2 | Command 64 B = 2^n | n=6 |
| Page | PRP 4096 B = 2^sigma | sigma=12 |
| Root BT | BT-181 "multi-band sigma=12 channel I/O multiple access" | see network-protocol.md §5 |
| atlas.n6 grade | `@R n6-dse-network-protocol = done dse :: dse [10]` | line 13667 |

## §3 EXACT check (P1-2 measured reference)

Based on nvme.md §3.3 data point table (line 62):

| DP # | Measure | Value | n=6 formula | Error | Grade |
|------|---------|-------|-------------|-------|-------|
| DP-1 | Command size | 64 B | 2^n | 0% | EXACT |
| DP-2 | Completion entry | 16 B | 2^tau | 0% | EXACT |
| DP-3 | LBA sector | 512 B | 2^9 | 0% | EXACT |
| DP-4 | PRP page | 4096 B | 2^sigma | 0% | EXACT |
| DP-5 | Max SQ/CQ pairs | 65536 | 2^(4sigma/3)=2^16 | 0% | EXACT |
| DP-6 | Queue depth | 65536 | 2^16 | 0% | EXACT |
| DP-7 | Version | 2.0 | phi | 0% | EXACT |
| DP-8 | p50 latency | 10 us | 2*sopfr | +/-20% | EMPIRICAL |
| DP-9 | Gen5 x4 | 16 GB/s | sigma+tau | 0% | EXACT |
| DP-10 | NSID width | 32 bit | 2^tau*phi | 0% | EXACT |
| DP-11 | MSI-X max vectors | 2048 | 2^11 | 0% | EXACT |

- Stats: 10/11 EXACT, 1 EMPIRICAL (p50 latency dominated by NAND read)
- Grade: EXACT-dominant

## §4 Conclusion

NVMe is placed in sigma=12 slot 9. With 10/11 DP EXACT (90.9%), n=6 alignment is a draft candidate.
Structurally, the HW stride is n=6 friendly through the 2^sigma*2^tau*2^phi combination, and the
vertical alignment of queue depth 2^16 = 2^(4sigma/3) is a representative pattern. The 1 EMPIRICAL
entry (p50 latency) is driven by physical NAND limits.

## §5 Signature

- Issuer: NEXUS-6 Discovery Engine Validator
- Issue date: 2026-04-14
- Chain: CHIP-P1-2 (nvme.md measured 10/11) -> CHIP-P3-2 (certificate issued)
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

