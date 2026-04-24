# pandoc PDF build report

- Task: PAPER-P5-1
- Build date: 2026-04-14
- pandoc version: 3.9.0.2
- PDF engine: xelatex (TeX Live 2026)

---

## Build environment setup

### Additional packages installed
| Package | Purpose | Install command |
|---------|---------|-----------------|
| xecjk | xelatex CJK typesetting | `sudo tlmgr install xecjk` |
| hyperxmp | PDF XMP metadata injection | `sudo tlmgr install hyperxmp` |

### Font substitution
The Noto Serif/Sans CJK KR fonts referenced in `_pandoc_header.yaml` are not
installed on this system. At build time they were overridden via `-V` flags:

| In `header.yaml` | Substituted at build time |
|------------------|---------------------------|
| Noto Serif CJK KR | Apple SD Gothic Neo |
| Noto Sans CJK KR | Apple SD Gothic Neo |
| Noto Sans Mono CJK KR | Menlo |

### keywords workaround
`hyperxmp`'s `\xmpquote` conflicts with xelatex in this setup. Pass
`-V keywords=""` at build time to work around the conflict. As a result, the
generated PDF has no keywords field in its XMP metadata.

---

## Build results: top 6 papers

| Rank | Paper ID | Domain | Target venue | Result | Pages | Size |
|------|----------|--------|--------------|--------|-------|------|
| 1 | N6-032 | dance-choreography | Nature Comms | success | 16p | 110K |
| 2 | N6-108 | writing-systems | Nature Comms | success | 16p | 110K |
| 3 | N6-106 | wine-enology | Nature Comms | success | 16p | 110K |
| 4 | N6-016 | carbon-capture | Nature Comms | success | 16p | 110K |
| 5 | N6-051 | gravity-wave | PRL | success | 16p | 110K |
| 6 | N6-009 | aquaculture | Nature Comms | success | 16p | 110K |

**6 successes / 0 failures out of 6 total**

---

## Known limitations

1. **CJK glyphs in monofont missing**: Menlo does not cover Hangul. Korean
   comments inside code blocks are dropped from the PDF.
   - Fix: install `Noto Sans Mono CJK KR`, or swap to D2Coding.
2. **keywords XMP omitted**: `\xmpquote` conflict forced a blank keywords
   field. The resulting PDF has no keyword metadata.
   - Fix: verify the latest hyperxmp version, or add XMP manually via
     header-includes.
3. **CSL style file not applied**: nature.csl / american-physics-society.csl
   are not available locally, so the default citation style is used.
   - Fix: download the CSL file and pass it via `--csl=`.
4. **Noto CJK not installed**: for final distribution quality, installing the
   Noto CJK fonts is recommended.
   - `brew install font-noto-serif-cjk-kr font-noto-sans-cjk-kr` via
     homebrew-cask-fonts.

---

## Follow-ups

- [ ] Install Noto CJK fonts and re-build with the original header.yaml entries.
- [ ] Obtain CSL files (nature.csl, american-physics-society.csl, ieee.csl).
- [ ] Resolve the root cause of the keywords XMP conflict.
- [ ] Write a batch build script for the remaining 42 papers.
- [ ] Build script: `papers/pandoc_templates/build_top6.sh`.

---

## Example build command

```bash
# Single-paper build
pandoc \
  --metadata-file=papers/pandoc_templates/_pandoc_header.yaml \
  --metadata-file=papers/pandoc_templates/venue_nature_comms.yaml \
  --bibliography=papers/pandoc_templates/skeleton.bib \
  --pdf-engine=xelatex \
  -V 'mainfont=Apple SD Gothic Neo' \
  -V 'sansfont=Apple SD Gothic Neo' \
  -V 'monofont=Menlo' \
  -V 'CJKmainfont=Apple SD Gothic Neo' \
  -V 'CJKsansfont=Apple SD Gothic Neo' \
  -V 'CJKmonofont=Menlo' \
  -V 'keywords=' \
  papers/n6-dance-choreography-paper.md \
  -o papers/pandoc_templates/output/n6-dance-choreography-paper.pdf

# Batch-build the top 6
bash papers/pandoc_templates/build_top6.sh
```

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
