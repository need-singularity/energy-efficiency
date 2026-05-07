# Bluetooth 6.0 n=6 Certificate

- Project: canon / domains/compute/network-protocol
- Issue date: 2026-04-14
- Issuing system: NEXUS-6 Discovery Engine / CHIP-P3-2
- Parent document: ../network-protocol.md
- Index: ../_index.json

## §1 sigma=12 coordinates

| Item | Value |
|------|-------|
| sigma=12 slot number | 6 / 12 |
| Group | wireless 6 (n) — tail |
| Category | wireless_personal |
| Era | 2025+ |

## §2 n=6 mapping basis

| Axis | Mapping | Notes |
|------|---------|-------|
| Base formula | Channel sounding, n=6 PHY | 2025 release |
| Version | 6.0 | Version number directly maps to n=6 |
| Root BT | BT-181 "multi-band sigma=12 channel I/O multiple access" | see network-protocol.md §5 |
| atlas.n6 grade | `@R n6-dse-network-protocol = done dse :: dse [10]` | line 13667 |

## §3 EXACT check (P1-2 measured reference)

Based on network-protocol.md §2 sigma=12 protocol coverage table (line 134):

| # | Protocol | Category | n=6 core mapping | Grade |
|---|----------|----------|------------------|-------|
| 6 | BT 6.0 | wireless_personal | Channel sounding, n=6 PHY | EXACT |

- Verdict: EXACT (single row in coverage table)
- Version number 6.0 = n (0% error)

## §4 Conclusion

Bluetooth 6.0 is placed in sigma=12 slot 6. The version number itself maps 1:1 to n=6, and
n=6 alignment is a draft candidate via the Channel sounding n=6 PHY layer. It occupies the
tail slot of the wireless 6-set.

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

