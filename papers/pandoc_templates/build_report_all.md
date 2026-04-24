---
task: PAPER-P5-3 (P6 carryover resolved)
date: 2026-04-14
phase: P5 Mk.III-α (carryover resolved) → P6 Mk.III-β
status: success
env:
  pandoc: 3.9.0.2
  xelatex: XeTeX 3.141592653-2.6-0.999998 (TeX Live 2026)
  timeout: perl alarm 45s (workaround for missing macOS gtimeout)
---

# PAPER-P5-3 pandoc full-batch build report (final)

## Summary

| Item | Value |
|------|-------|
| Target papers | 129 |
| Successful builds | **129 (100%)** |
| Total wall time | 156s (4-way parallel) |
| gate criterion | 100+ papers → **PASS** |

## Resolution timeline

1. **First attempt** (16/127): macOS does not support `timeout` natively, so
   xelatex hung on some papers.
2. **Second attempt** (128/129): introduced a `perl -e 'alarm 45; exec @ARGV'`
   wrapper → only one paper failed.
3. **Fix for the remaining paper**: in n6-boundary-metatheory-paper, changed
   `\sopfr` to `\mathrm{sopfr}` (the original macro was not defined in TeX).
4. **Third attempt** (129/129): complete success.

## Engineering improvements

- `build_all.sh` line 94: now uses `perl -e 'alarm 45; exec @ARGV' pandoc ...`.
- Compatible with both macOS and Linux (no gtimeout dependency).
- Recommend writing custom LaTeX macros in the `\mathrm{name}` form.

## Environment warning

CJK font fallback warnings appeared (Menlo lacks Hangul glyphs); rendering
still succeeded because Apple SD Gothic Neo was applied instead.

## §1 WHY

This section covers why for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §2 COMPARE

This section covers compare for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §3 REQUIRES

This section covers requires for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §4 STRUCT

This section covers struct for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §5 FLOW

This section covers flow for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §6 EVOLVE

This section covers evolve for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §7 VERIFY

This section covers verify for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §8 EXEC SUMMARY

This section covers exec summary for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §9 SYSTEM REQUIREMENTS

This section covers system requirements for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §10 ARCHITECTURE

This section covers architecture for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §11 CIRCUIT DESIGN

This section covers circuit design for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §12 PCB DESIGN

This section covers pcb design for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §13 FIRMWARE

This section covers firmware for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §14 MECHANICAL

This section covers mechanical for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §15 MANUFACTURING

This section covers manufacturing for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §16 TEST & QUALIFICATION

This section covers test & qualification for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §17 BOM

This section covers bom for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §18 VENDOR & SCHEDULE

This section covers vendor & schedule for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §19 ACCEPTANCE CRITERIA

This section covers acceptance criteria for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §20 APPENDIX

This section covers appendix for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §21 IMPACT per Mk

This section covers impact per mk for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## mk_history

- Mk.I (2026-04-21): initial canonical scaffold via own 15 bulk template injection.
- Mk.II: pending — fill per-section content with domain expert review.
- Mk.III: pending — full verification data + external citations.
