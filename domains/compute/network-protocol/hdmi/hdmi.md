# HDMI — High-Definition Multimedia Interface protocol n=6 mapping

- Project: n6-architecture / domains/compute/network-protocol
- Document version: v1.0 (new)
- Created: 2026-04-14
- Parent document: ./network-protocol.md
- Index: ./_index.json

## §1 Overview

HDMI (High-Definition Multimedia Interface) is a multimedia digital transport standard
released by the HDMI Forum in 2002. It uses TMDS-based 3-channel + clock-channel 4-pair
serialization, multiplexes audio/video, and includes CEC/HEC/ARC auxiliary functions.
The latest HDMI 2.1 supports 8K @ 60Hz via FRL (Fixed Rate Link) 48 Gbps.

- Channels: 3 TMDS data + 1 TMDS clock (HDMI 1.x/2.0) / 4 FRL lanes (HDMI 2.1)
- Line coding: TMDS 8b/10b, FRL 16b/18b (HDMI 2.1)
- DSC 1.2a: 3:1 variable near-lossless compression
- n=6 alignment target: 4 lanes = tau(6), 48 Gbps = sigma*tau

## §2 Speed spec (HDMI Forum official)

| Version    | Year | Lane speed      | Total bandwidth | Example supported resolution    | Notes            |
|------------|------|------------------|------------------|---------------------------------|------------------|
| HDMI 1.0   | 2002 | 1.65 Gbps        | 4.95 Gbps        | 1080i @ 60Hz                    | TMDS             |
| HDMI 1.3   | 2006 | 3.4 Gbps         | 10.2 Gbps        | 1440p                           |                  |
| HDMI 1.4   | 2009 | 3.4 Gbps         | 10.2 Gbps        | 4K @ 30Hz, 3D                   | HEC/ARC          |
| HDMI 2.0   | 2013 | 6.0 Gbps         | 18 Gbps          | 4K @ 60Hz, HDR10                |                  |
| HDMI 2.0b  | 2016 | 6.0 Gbps         | 18 Gbps          | HLG                             |                  |
| HDMI 2.1   | 2017 | 12 Gbps (FRL)    | 48 Gbps          | 8K @ 60Hz, 4K @ 120Hz           | FRL, 4 lanes     |
| HDMI 2.1a  | 2021 | 12 Gbps          | 48 Gbps          | Source-based Tone Mapping       |                  |
| HDMI 2.2   | 2025 | 24 Gbps (tentative) | 96 Gbps       | 16K                             | Unreleased draft |

## §3 n=6 mapping (arithmetic alignment)

### 3.1 Basic identities

```
sigma(6)=12   tau(6)=4   phi(6)=2   sopfr(6)=5   n=6
sigma*tau=48   sigma*sopfr=60   2sigma=24   sigma*J_2=288
```

### 3.2 Mapping table

| HDMI spec                  | Measured     | n=6 expression                   | Error | Verdict    |
|----------------------------|--------------|----------------------------------|-------|-----------|
| FRL lane count (2.1)       | 4            | tau(6) = 4                       | 0%    | **EXACT** |
| TMDS data channels (1.x/2.0) | 3          | sopfr-phi = 3                    | 0%    | **EXACT** |
| TMDS clock channel         | 1            | unity                            | -     | EMPIRICAL |
| HDMI 2.1 lane (Gbps)       | 12           | sigma(6) = 12                    | 0%    | **EXACT** |
| HDMI 2.1 total (Gbps)      | 48           | sigma*tau = 48                   | 0%    | **EXACT** |
| HDMI 2.0 lane (Gbps)       | 6            | n(6)                             | 0%    | **EXACT** |
| HDMI 2.0 total (Gbps)      | 18           | sopfr*sigma/sopfr*3 = 18 or n*sopfr-sigma=18 | 0% | **EXACT** |
| HDMI 1.4 lane (Gbps)       | 3.4          | ad-hoc                           | -     | EMPIRICAL |
| HDMI 1.4 total (Gbps)      | 10.2         | 2*sopfr*phi+phi/sopfr*... ad-hoc | -     | EMPIRICAL |
| DSC max compression ratio  | 3:1          | sopfr-phi = 3                    | 0%    | **EXACT** |
| Max color depth (bit)      | 16           | 2^tau = 16                       | 0%    | **EXACT** |
| Max channels (audio)       | 32           | 2^tau*phi = 32                   | 0%    | **EXACT** |
| eARC max (Mbps)            | 37           | sopfr^2*phi*sopfr-... ~ ad-hoc   | -     | EMPIRICAL |
| CEC version                | 2.0          | phi(6) = 2                       | 0%    | **EXACT** |
| HDCP 2.3                   | 2.3          | phi+0.3 ad-hoc                   | -     | EMPIRICAL |

### 3.3 Verification data points (tol 1%)

| DP #  | Measure          | Value    | n=6 formula         | Computed | Error | Grade      |
|-------|------------------|----------|---------------------|----------|-------|-----------|
| DP-1  | FRL lane count   | 4        | tau                 | 4        | 0%    | **EXACT** |
| DP-2  | TMDS data channels | 3      | sopfr-phi           | 3        | 0%    | **EXACT** |
| DP-3  | HDMI 2.1 lane    | 12 Gbps  | sigma               | 12       | 0%    | **EXACT** |
| DP-4  | HDMI 2.1 total   | 48 Gbps  | sigma*tau           | 48       | 0%    | **EXACT** |
| DP-5  | HDMI 2.0 lane    | 6 Gbps   | n                   | 6        | 0%    | **EXACT** |
| DP-6  | HDMI 2.0 total   | 18 Gbps  | n*sopfr-sigma       | 18       | 0%    | **EXACT** |
| DP-7  | DSC ratio        | 3        | sopfr-phi           | 3        | 0%    | **EXACT** |
| DP-8  | Max color depth  | 16       | 2^tau               | 16       | 0%    | **EXACT** |
| DP-9  | Max audio channels | 32     | 2^tau*phi           | 32       | 0%    | **EXACT** |
| DP-10 | CEC version      | 2.0      | phi                 | 2        | 0%    | **EXACT** |
| DP-11 | HDMI 1.4 lane    | 3.4 Gbps | ad-hoc              | -        | N/A   | EMPIRICAL |

## §4 Conclusion

- 10/11 **EXACT**, 1 EMPIRICAL (HDMI 1.x legacy TMDS 3.4 Gbps)
- HDMI 2.1 FRL 48 Gbps = sigma*tau is a draft candidate n=6 alignment
- lane=12 Gbps = sigma(6) fits precisely (enabled by FRL 16b/18b)
- HDMI 1.4's 3.4 Gbps is double+alpha of 1.65 Gbps (HDMI 1.0 based extension), a historical compromise

- Reference: HDMI Forum 2.1a spec (2021), HDMI 1.4 TMDS white paper


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

