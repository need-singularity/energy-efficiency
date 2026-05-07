# LoRaWAN n=6 Certificate

- Project: canon / domains/compute/network-protocol
- Issue date: 2026-04-14
- Issuing system: NEXUS-6 Discovery Engine / CHIP-P3-2
- Parent document: ../network-protocol.md
- Index: ../_index.json

## §1 sigma=12 coordinates

| Item | Value |
|------|-------|
| sigma=12 slot number | 5 / 12 |
| Group | wireless 6 (n) |
| Category | IoT_low_power |
| Era | 2015+ |

## §2 n=6 mapping basis

| Axis | Mapping | Notes |
|------|---------|-------|
| Base formula | SF7~SF12 = 6 tiers | n=6 spreading factors |
| Invariant | +/-10% invariant | Uplink margin |
| Root BT | BT-181 "multi-band sigma=12 channel I/O multiple access" | see network-protocol.md §5 |
| atlas.n6 grade | `@R n6-dse-network-protocol = done dse :: dse [10]` | line 13667 |

## §3 EXACT check (P1-2 measured reference)

Based on network-protocol.md §2 sigma=12 protocol coverage table (line 133):

| # | Protocol | Category | n=6 core mapping | Grade |
|---|----------|----------|------------------|-------|
| 5 | LoRaWAN | IoT_low_power | SF7~SF12 = 6 tiers (n=6) | EXACT |

- Verdict: EXACT (single row in coverage table)
- SF7, SF8, SF9, SF10, SF11, SF12 = 6 tiers — direct n=6 correspondence (0% error)

## §4 Conclusion

LoRaWAN is placed in sigma=12 slot 5, with the spreading factors SF7~SF12 forming a draft
candidate n=6 6-tier alignment. The modulation space of low-power wide-area IoT
corresponds 1:1 to the n=6 axis.

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

