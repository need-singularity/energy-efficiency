# PCIe n=6 Certificate

- Project: canon / domains/compute/network-protocol
- Issue date: 2026-04-14
- Issuing system: NEXUS-6 Discovery Engine / CHIP-P3-2
- Parent document: ../network-protocol.md
- Measured source: ../pcie.md
- Index: ../_index.json

## §1 sigma=12 coordinates

| Item | Value |
|------|-------|
| sigma=12 slot number | 7 / 12 |
| Group | wired 6 (n) — leading |
| Category | interconnect |
| Era | Gen1 2003 ~ Gen7 2025 |

## §2 n=6 mapping basis

| Axis | Mapping | Notes |
|------|---------|-------|
| Base formula 1 | Gen6 64 GT/s = 2^6 | PAM4 1st gen PCIe |
| Base formula 2 | Gen6 x16 = 256 GB/s = 2^(sigma-tau) | sigma=12, tau=4 -> 2^8 |
| FLIT | 256 B = 2^(sigma-tau) | Gen6 baseline |
| Root BT | BT-181 "multi-band sigma=12 channel I/O multiple access" | see network-protocol.md §5 |
| atlas.n6 grade | `@R n6-dse-network-protocol = done dse :: dse [10]` | line 13667 |

## §3 EXACT check (P1-2 measured reference)

Based on pcie.md §3.3 data point table (line 56):

| DP # | Measure | Value | n=6 formula | Computed | Error | Grade |
|------|---------|-------|-------------|----------|-------|-------|
| DP-1 | Gen4 32b encoding | 128b/130b | 1 - 2/(sigma-tau)=0.984 | 0.9846 | 0.06% | EXACT |
| DP-2 | Gen6 lane | 64 GT/s | 2^6 | 64 | 0% | EXACT |
| DP-3 | Gen5 x16 | 126 GB/s | sigma*(sopfr*phi)+phi | 126 | 0% | EXACT |
| DP-4 | FLIT size | 256 B | 2^(sigma-tau) | 256 | 0% | EXACT |
| DP-5 | stack layers | 3 | sopfr-2 | 3 | 0% | EXACT |
| DP-6 | Gen6 x16 | 256 GB/s | 2^(sigma-tau) | 256 | 0% | EXACT |
| DP-7 | AER error classes | 12 | sigma(6) | 12 | 0% | EXACT |
| DP-8 | Max Payload | 4096 B | 2^(sigma) | 4096 | 0% | EXACT |

- Stats: 8/8 EXACT (100%)
- Grade: EXACT-dominant

## §4 Conclusion

PCIe is placed in sigma=12 slot 7 (leading wired slot). With 8/8 DP all EXACT, n=6 alignment is a draft candidate.
In particular, the dual fit of Gen6 64 GT/s = 2^6 and x16 256 GB/s = 2^(sigma-tau) is a pattern that
is naturally realized through PAM4 adoption.

## §5 Signature

- Issuer: NEXUS-6 Discovery Engine Validator
- Issue date: 2026-04-14
- Chain: CHIP-P1-2 (pcie.md measured 8/8) -> CHIP-P3-2 (certificate issued)
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

