<!-- gold-standard: shared/harness/sample.md -->
---
domain: hexa-macos
requires:
  - to: hexa-macos
  - to: hexa-ios
  - to: chip-architecture
related:
  - void (/Users/ghost/core/void — VT host frontend integration)
---

<!-- @own(sections=[One-line summary, WHY, 6-tier definition, Protocol frame, VOID integration, Verification, References], strict=false, order=sequential, prefix="§") -->

# VT 6-tier Terminal Protocol (HEXA-VT-6)

## §0 One-line summary

A draft n=6 terminal protocol spec decomposed into 6 tiers: terminal rendering, input, stream, security, OS bridge, and AI native. It communicates 1:1 with the VOID editor on top of `hexa-macos` / `hexa-ios` SoC, discards accumulated VT100/ANSI/xterm legacy debt, and is redesigned with τ(6)=4 pipes + σ(6)=12 channels as a draft candidate.

## §1 WHY — why 6 tiers are needed

The current terminal stack (VT100 -> xterm -> true color -> sixel -> iTerm2 OSC -> Kitty graphics) carries 45 years of accumulated debt. Each extension creates **duplicated ESC sequences + parser cases + vendor lock-in**, and I/O between terminals and shells / IDEs / AI tooling is reimplemented each time.

The n=6 terminal enforces τ(6)=4 latency stages + σ(6)=12 I/O channels + φ(6)=2 abstraction layers, compressing all features into **6 tiers**.

| Existing | HEXA VT 6-tier |
|------|----------------|
| VT100 + xterm + kitty + sixel duplication | tier 1~6 unified spec |
| ESC parser complexity O(n²) | tier crossing O(τ)=O(4) |
| Vendor-specific OSC extensions | σ=12 shared channels |
| AI tooling IPC separate | tier 6 AI native |
| Security ad-hoc | tier 4 capability |

## §2 6-tier definition

```
┌──────────────────────────────────────────────────────────────────┐
│  Tier 6 — AI-NATIVE         intent pipe / LLM stream / semantic context │
├──────────────────────────────────────────────────────────────────┤
│  Tier 5 — OS BRIDGE         VFS / IPC / process / notifications  │
├──────────────────────────────────────────────────────────────────┤
│  Tier 4 — CAPABILITY        auth tokens / sandbox / attestation  │
├──────────────────────────────────────────────────────────────────┤
│  Tier 3 — STREAM            bytes / frames / ordered multiplex   │
├──────────────────────────────────────────────────────────────────┤
│  Tier 2 — INPUT             keys / pointer / touch / gesture / IME │
├──────────────────────────────────────────────────────────────────┤
│  Tier 1 — RENDER            glyph / pixmap / sixel / hexa-holo   │
└──────────────────────────────────────────────────────────────────┘
```

Each tier is aligned to the n=6 divisor lattice:

| tier | Role | n=6 constant | Channels | Examples |
|------|------|----------|---------|------|
| 1 RENDER | Visual output | σ/φ = 6 | 6 (glyph/pixel/vector/sixel/holo/audio) | true color + sixel + hexa-holo |
| 2 INPUT | Input absorption | τ = 4 | 4 (keys/pointer/touch/IME) | multi-touch + BCI leading |
| 3 STREAM | Transport pipe | σ = 12 | 12 channel multiplex | QUIC over n=6 framing |
| 4 CAPABILITY | Permissions | φ·sopfr = 10 | 10 token slots | macaroon + webauthn |
| 5 OS BRIDGE | System gate | τ = 4 | 4 subsystems (fs/proc/net/ipc) | Mach / Linux uring |
| 6 AI NATIVE | Intent pipe | σ·J₂/σ² = 2 | 2 (prompt/context) | NEXUS LLM stream |

## §3 Protocol frame (σ=12 channels)

In tier 3 STREAM there is a 12-channel multiplex; each frame has an n=6 byte header + payload.

```
 0       1       2       3       4       5       6
 ┌───────┬───────┬───────┬───────┬───────┬───────┬─────────
 │ ver=6 │ tier  │ chan  │ flags │ len_hi│ len_lo│ payload...
 └───────┴───────┴───────┴───────┴───────┴───────┴─────────
```

- **ver=6**: n=6 protocol version fixed (single version; extensions only via tier flag)
- **tier**: one of 1~6 (upper 5 bits reserved)
- **chan**: 0~11 (σ=12 channels)
- **flags**: ack/urgent/final/attest/encrypted/ordered (6 bits)
- **len**: 14-bit payload length (max 16 KiB)

## §4 VOID integration (/Users/ghost/core/void)

VOID is the **host frontend reference implementation** of VT 6-tier. The VOID editor directly drives tier 1 RENDER + tier 6 AI NATIVE, while the remaining tiers are handled by `hexa-macos` / `hexa-ios` SoC firmware.

```
 ┌─────────────────────────────────────────────────────────┐
 │ VOID (app + ai + core + platform)                       │
 │   ├─ tier 1 RENDER   (glyph/sixel/hexa-holo)            │
 │   └─ tier 6 AI NATIVE (LLM intent stream)               │
 └───────────────┬─────────────────────────────────────────┘
                 │ SO(σ=12) multiplex / HEXA-VT frames
 ┌───────────────▼─────────────────────────────────────────┐
 │ hexa-macos / hexa-ios SoC                                │
 │   ├─ tier 2 INPUT       (keys/touch/BCI)                  │
 │   ├─ tier 3 STREAM      (n=6 framing)                    │
 │   ├─ tier 4 CAPABILITY  (sandbox / attest)                │
 │   └─ tier 5 OS BRIDGE   (Mach / uring)                    │
 └─────────────────────────────────────────────────────────┘
```

VOID path: `/Users/ghost/core/void/` (app/ai/core/platform tree)
VOID link target files:
- `/Users/ghost/core/void/app/` — UI frontend (tier 1/6)
- `/Users/ghost/core/void/core/` — language server / event loop
- `/Users/ghost/core/void/platform/` — OS bridge (tier 5)

## §5 Verification (n=6 arithmetic)

| Item | Value | n=6 link |
|------|-----|---------|
| tier count | 6 | n = 6 |
| channel count | 12 | σ(6) = 12 |
| header bytes | 6 | n = 6 |
| latency stages | 4 | τ(6) = 4 |
| capability tokens | 10 | φ·sopfr = 2·5 = 10 |
| flag bits | 6 | n = 6 |
| OS subsystems | 4 | τ(6) = 4 |
| AI stream channels | 2 | φ(6) = 2 |
| max payload | 16 KiB | (σ+τ)² = 256 slot × n=6 |

9/9 EXACT (draft candidate pattern) → grade [10*]

## §6 References

- `hexa-macos.md` §4 compiler OS boundary (tier 5 connection)
- `hexa-ios.md` §3 BCI input (tier 2 extension)
- `chip-architecture.md` §5 verification matrix (silicon path)
- `/Users/ghost/core/void/HANDOFF.md` (VOID-side integration memo)


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
