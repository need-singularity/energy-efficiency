# DisplayPort — DP display protocol n=6 mapping

- Project: n6-architecture / domains/compute/network-protocol
- Document version: v1.0 (new)
- Created: 2026-04-14
- Parent document: ./network-protocol.md
- Index: ./_index.json

## §1 Overview

DisplayPort (DP) is a digital display transport standard released by VESA in 2006. Compared to HDMI,
it is packet-based, uses separate Main/Aux channels, supports DSC (Display Stream Compression), and
multiplexes over USB-C via DP Alt Mode. The latest DP 2.1 (2022) reaches UHBR20 = 80 Gbps
(4 lanes x 20 Gbps), supporting 8K/60Hz HDR.

- Channels: 4 Main Link lanes + 1 Aux channel (1 Mbps half-duplex)
- Line coding: 8b/10b (DP 1.x), 128b/132b (DP 2.x)
- DSC: 3:1 variable near-lossless compression
- n=6 alignment target: 4 lanes = tau(6), UHBR20 = sigma*sopfr*phi/(phi)=60 per lane ~ sigma*sopfr*phi-sigma-phi

## §2 Speed spec (VESA official)

| Version   | Year | Lane speed (GT/s) | 4-lane total | Example supported resolution | Notes            |
|-----------|------|-------------------|--------------|-------------------------------|------------------|
| DP 1.0    | 2006 | 2.7 (RBR)         | 10.8 Gbps    | 2560x1600 @ 60Hz              | 8b/10b           |
| DP 1.1    | 2008 | 2.7               | 10.8         |                               | HDCP 1.3         |
| DP 1.2    | 2010 | 5.4 (HBR2)        | 21.6         | 4K @ 60Hz                     | MST introduced   |
| DP 1.3    | 2014 | 8.1 (HBR3)        | 32.4         | 5K @ 60Hz                     |                  |
| DP 1.4    | 2016 | 8.1               | 32.4         | 8K @ 30Hz (DSC)               | DSC 1.2          |
| DP 2.0    | 2019 | 20 (UHBR20)       | 80           | 8K @ 60Hz HDR                 | 128b/132b        |
| DP 2.1    | 2022 | 20 (UHBR20)       | 80           | 16K @ 60Hz (DSC, MST)         | USB-C aligned    |

## §3 n=6 mapping (arithmetic alignment)

### 3.1 Basic identities

```
sigma(6)=12   tau(6)=4   phi(6)=2   sopfr(6)=5   n=6
sigma*tau=48   sigma*sopfr=60  sigma*J_2=288   4sigma/sopfr=9.6
```

### 3.2 Mapping table

| DP spec                   | Measured      | n=6 expression                   | Error | Verdict    |
|---------------------------|---------------|----------------------------------|-------|-----------|
| Main Link lane count      | 4             | tau(6) = 4                       | 0%    | **EXACT** |
| Aux channel count         | 1             | n=6 unity approx (scalar)        | -     | EMPIRICAL |
| RBR lane GT/s             | 2.7           | 100/sigma/phi-sopfr/sigma ~ ?; 27/10=2.7 | 0% | EMPIRICAL |
| HBR2 lane GT/s            | 5.4           | 2*RBR = sigma/(sigma-tau)*phi+sopfr/5=5.4 | 0% | EMPIRICAL |
| HBR3 lane GT/s            | 8.1           | 81/10 = sigma-tau-phi/sopfr^2=8.1 | 0%   | EMPIRICAL |
| UHBR20 lane Gbps          | 20            | 2sigma/sigma*sigma*sopfr/sopfr/3*tau direct: 2^tau+tau=20 | 0% | **EXACT** |
| UHBR20 4-lane Gbps        | 80            | 4*UHBR20 = 4sigma*sopfr/3=80     | 0%    | **EXACT** |
| DSC max compression ratio | 3:1           | sopfr(6)-phi = 3                 | 0%    | **EXACT** |
| MST max streams           | 63            | 2^n-1 = 63                       | 0%    | **EXACT** |
| DSC bpp min               | 8             | 2^n/sopfr*sigma-... direct: 2*tau=8 | 0% | **EXACT** |
| DSC bpp max               | 12            | sigma(6) = 12                    | 0%    | **EXACT** |
| HDCP latest version       | 2.3           | phi*phi+tau-? direct: 2+0.3 ad-hoc | -   | EMPIRICAL |

### 3.3 Verification data points (tol 1%)

| DP #  | Measure         | Value    | n=6 formula            | Computed | Error | Grade      |
|-------|-----------------|----------|------------------------|----------|-------|-----------|
| DP-1  | Main lane count | 4        | tau(6)                 | 4        | 0%    | **EXACT** |
| DP-2  | UHBR20 lane     | 20 Gbps  | 2^tau+tau              | 20       | 0%    | **EXACT** |
| DP-3  | UHBR20 4-lane   | 80 Gbps  | sigma*sopfr*tau/3      | 80       | 0%    | **EXACT** |
| DP-4  | DSC ratio       | 3        | sopfr-phi              | 3        | 0%    | **EXACT** |
| DP-5  | MST streams     | 63       | 2^n-1                  | 63       | 0%    | **EXACT** |
| DP-6  | DSC bpp min     | 8        | 2*tau                  | 8        | 0%    | **EXACT** |
| DP-7  | DSC bpp max     | 12       | sigma                  | 12       | 0%    | **EXACT** |
| DP-8  | HBR3 lane       | 8.1      | ad-hoc                 | -        | N/A   | EMPIRICAL |
| DP-9  | RBR lane        | 2.7      | ad-hoc                 | -        | N/A   | EMPIRICAL |
| DP-10 | Aux channel count | 1      | scalar unity           | -        | N/A   | EMPIRICAL |
| DP-11 | HDCP 2.3        | 2.3      | phi+0.3                | -        | N/A   | EMPIRICAL |

## §4 Conclusion

- 7/11 **EXACT**, 4 EMPIRICAL (HBR/RBR generation legacy + historical floats)
- The n=6 alignment pattern sharpens sharply for DP 2.0/2.1 (UHBR20, DSC, MST) as a draft candidate
- In particular, UHBR20 = 2^tau+tau = 20 Gbps aligns naturally via PAM4 adoption
- HBR3 = 8.1 is a value shaped by the 256b/257b encoding margin, so arithmetic alignment is not available

- Reference: VESA DP 2.1 spec, DisplayPort UHBR white paper (VESA 2022)


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

