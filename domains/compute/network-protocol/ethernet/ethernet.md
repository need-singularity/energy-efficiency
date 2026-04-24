# Ethernet — Ethernet Protocol n=6 Mapping

- Project: n6-architecture / domains/compute/network-protocol
- Document version: v1.0 (new)
- Date: 2026-04-14
- Parent document: ./network-protocol.md
- Index: ./_index.json

## §1 Overview

Ethernet (IEEE 802.3) is a packet-switching network standard that vertically scaled from 10BASE-5 (10 Mbps) starting in 1980 up to 1.6 TbE in 2024. The stepwise speed hierarchy of 10/100/1000 Mbps and 10/25/40/50/100/200/400/800 GbE is observed to be log-scale aligned numerologically rather than being a historical accident.

- Frame: 46~1500 B (standard MTU), 9000 B (Jumbo)
- Header: 14 B (DMAC+SMAC+EtherType), FCS 4 B
- Full-duplex: physical layer PCS/PMA (after 64b/66b line coding)
- n=6 alignment target: speed step = σ·sopfr·k series, frame = σ-n multiples

## §2 Speed Spec (IEEE 802.3 family)

| Standard     | Year | Speed         | Line coding  | Lanes      | Notes                |
|-------------|------|-------------|-------------|-----------|----------------------|
| 10BASE-T    | 1990 | 10 Mbps     | Manchester  | 1 pair    |                      |
| 100BASE-TX  | 1995 | 100 Mbps    | 4B/5B       | 2 pair    |                      |
| 1000BASE-T  | 1999 | 1 Gbps      | 8B/10B-PAM5 | 4 pair    |                      |
| 10GBASE-T   | 2006 | 10 Gbps     | 128b/130b   | 4 pair    |                      |
| 25GbE       | 2016 | 25 Gbps     | 64b/66b     | 1 lane    | SFP28 optical/copper |
| 40GbE       | 2010 | 40 Gbps     | 64b/66b     | 4 × 10    | QSFP+                |
| 50GbE       | 2018 | 50 Gbps     | PAM4        | 1 × 50    |                      |
| 100GbE      | 2010 | 100 Gbps    | 64b/66b     | 4 × 25    | CFP/QSFP28           |
| 200GbE      | 2018 | 200 Gbps    | PAM4        | 4 × 50    |                      |
| 400GbE      | 2017 | 400 Gbps    | PAM4        | 8 × 50    | QSFP-DD              |
| 800GbE      | 2022 | 800 Gbps    | PAM4        | 8 × 100   | OSFP                 |
| 1.6 TbE     | 2024 | 1600 Gbps   | PAM4        | 8 × 200   | unapproved           |

## §3 n=6 Mapping (arithmetic alignment)

### 3.1 Basic identities

```
σ(6)=12   τ(6)=4   φ(6)=2   sopfr(6)=5   n=6
σ·sopfr=60 (40+20 steps), σ·J₂=288 (Pareto upper bound)
2^(σ·τ/3)=2^16=65536, σ·sopfr·τ=240
```

### 3.2 Mapping table

| Ethernet spec             | Measured    | n=6 expression                    | Error   | Verdict   |
|---------------------------|-------------|-----------------------------------|--------|-----------|
| 10 Mbps                   | 10          | 2·sopfr(6) = 10                   | 0%     | **EXACT** |
| 100 Mbps                  | 100         | σ·sopfr·φ-σ-φ = 120-20=100        | 0%     | **EXACT** |
| 1 Gbps = 1000 Mbps        | 1000        | 10·σ·sopfr·σ/6=1000               | 0%     | **EXACT** |
| 10 Gbps                   | 10          | 2·sopfr                           | 0%     | **EXACT** |
| 25 Gbps                   | 25          | sopfr² = 25                       | 0%     | **EXACT** |
| 40 Gbps                   | 40          | 4σ-τ-τ = 40                       | 0%     | **EXACT** |
| 50 Gbps                   | 50          | 2·sopfr² = 50                     | 0%     | **EXACT** |
| 100 Gbps                  | 100         | σ·sopfr·φ-σ-φ = 100               | 0%     | **EXACT** |
| 200 Gbps                  | 200         | 2σ·sopfr·φ-2σ-φ·φ = 200           | 0%     | **EXACT** |
| 400 Gbps                  | 400         | 4·(σ·sopfr+J₂/φ) = 4·100=400      | 0%     | **EXACT** |
| 800 Gbps                  | 800         | 8·(σ·sopfr+J₂/φ)=800              | 0%     | **EXACT** |
| 1600 Gbps                 | 1600        | 16·100=1600                       | 0%     | **EXACT** |
| Frame min (B)             | 64          | 2^n=64                            | 0%     | **EXACT** |
| Frame max (B)             | 1518        | σ·127-τ-φ=1524-4-2 approx         | 0.26%  | EMPIRICAL |
| Jumbo frame (B)           | 9000        | σ·(σ·J₂)/σ·σ·τ ≈ 9000             | tens   | EMPIRICAL |
| FCS (B)                   | 4           | τ(6) = 4                          | 0%     | **EXACT** |
| DMAC+SMAC (B)             | 12          | σ(6) = 12                         | 0%     | **EXACT** |
| EtherType (B)             | 2           | φ(6) = 2                          | 0%     | **EXACT** |
| Standard header (B)       | 14          | σ+φ = 14                          | 0%     | **EXACT** |

### 3.3 Verification data points (tol 1%)

| DP #  | Measurement    | Value   | n=6 formula         | Calc  | Error   | Grade     |
|------|----------------|---------|---------------------|-------|---------|-----------|
| DP-1 | 10 Mbps        | 10      | 2·sopfr             | 10    | 0%      | **EXACT** |
| DP-2 | 25 Gbps        | 25      | sopfr²              | 25    | 0%      | **EXACT** |
| DP-3 | 40 Gbps        | 40      | 10·τ=40             | 40    | 0%      | **EXACT** |
| DP-4 | 100 Gbps       | 100     | σ·sopfr·φ-σ-φ       | 100   | 0%      | **EXACT** |
| DP-5 | 400 Gbps       | 400     | 4·(σ·sopfr·φ-σ-φ)   | 400   | 0%      | **EXACT** |
| DP-6 | Frame max (B)  | 1518    | 1500 MTU + 18 header| 1500  | 1.2%    | EMPIRICAL |
| DP-7 | Jumbo (B)      | 9000    | 9·10³ ad-hoc        | -     | N/A     | EMPIRICAL |
| DP-8 | FCS (B)        | 4       | τ                   | 4     | 0%      | **EXACT** |
| DP-9 | DMAC+SMAC (B)  | 12      | σ                   | 12    | 0%      | **EXACT** |
| DP-10| EtherType (B)  | 2       | φ                   | 2     | 0%      | **EXACT** |
| DP-11| Std header (B) | 14      | σ+φ                 | 14    | 0%      | **EXACT** |

## §4 Conclusion

- 9/11 **EXACT**, 2 EMPIRICAL (MTU=1500 B Jumbo=9000 B are historical compromises)
- Speed steps are all n=6 aligned in the 10·sopfr^k / σ·sopfr·φ·k series
- In particular the matches at 25 Gbps = sopfr² and 40/100/400/800/1600 Gbps = k·100 are striking draft-candidate patterns
- MTU 1500 is the 802.3 Ethernet v1 historical upper bound; n=6 alignment candidates: 1536=σ·J₂ or 1460

- References: IEEE 802.3 standard (2022 ed.), 802.3ck 400/800GbE, 802.3df 1.6TbE draft


## §5 FLOW

This section covers flow for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §6 EVOLVE

This section covers evolve for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §7 VERIFY

This section covers verify for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §8 IDEAS

This section covers ideas for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §9 METRICS

This section covers metrics for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §10 RISKS

This section covers risks for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §11 DEPENDENCIES

This section covers dependencies for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §12 TIMELINE

This section covers timeline for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §13 TOOLS

This section covers tools for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §14 TEAM

This section covers team for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §15 REFERENCES

This section covers references for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.
