---
title: Critical Mineral Conflict Arbitration — kick-spec
category: cross-axis-domain
umbrella: post-fossil-resource-geopolitics
created: 2026-05-06
updated: 2026-05-06
status: draft kick-spec (pre-registration; awaiting cycle entry)
target_axis: infra
target_domain_name: critical-mineral-conflict-arbitration
target_alien_grade: 10 PHYSICAL-LIMIT
parent_thread: Ukraine-Russia war deep research (2026-05-06 conversation)
sister_domain: energy/amd-ree-mineshaft-phes (D2EHPA REE chemistry shared)
style: own#15 21-section preview + own#32 design-by-physics + own#33 Block A-G
---

# HEXA-CMCA — Critical Mineral Conflict Arbitration (kick-spec)

> **One-line summary**: a contested-territory critical-mineral arbitration architecture where (i) royalty splits between sovereign / occupying-power / external-investor are derived from **Nash 1953 bargaining + Hotelling 1931 exhaustible-resource pricing + Coase 1960 externality bargaining** rather than political bid; (ii) recovery yields are bound by **D2EHPA solvent-extraction physics (Sastri-Shibata 2003) + 5-stage Kremser 1930 countercurrent**; (iii) enforcement uses the same **CTBTO IMS seismic + Sentinel-1 SAR InSAR** verification stack as ceasefire monitoring. Trigger case: Ukraine-US 2025-04-30 Mineral Resources Agreement + Russian-occupied Donbas Li/Ti/Mn/REE deposits ($12T SecDev estimate). Reusable to Greenland / DRC / Mongolia / Chile.

> Honest scope per raw 91 C3: kick-spec at this revision is **theoretical-architectural** (Nash-bargaining solver + Hotelling price-path simulator + D2EHPA mass-balance). Empirical realization gated on F-CMCA-MVP-1..5 (2026-08-30 / 2026-11-30 / 2027-02-28). own#2 master identity preserved as separable Block A; design constants are physical-limit values, not n=6 force-fit (own#32).

---

## §0 WHY THIS IS A DOMAIN, NOT AN ESSAY

The Ukraine-Russia war research (2026-05-06 thread) surfaced that **the resource layer is the only layer with measurable, falsifiable, reproducible physical anchors**:

- security/identity layers → political-science framework, no physical-limit ceiling, no falsifier
- **resource layer** → USGS reserves data + LME spot + Hotelling price path + Nash bargaining + D2EHPA chemistry are **all empirically anchored and reproducible**

The framework also **generalizes**: the same arbitration physics applies to Greenland REE (2025 US bid), DRC cobalt (Chinese SOE control), Mongolia copper (Rio Tinto / Russia transit), Chile lithium salar (state vs private). One domain, N reusable cases.

→ qualifies for n6-arch: physical-anchored + falsifiable + reusable + cross-axis fan-in.

---

## §1 PHYSICAL / MATHEMATICAL ANCHORS (each engineering target → published model)

| Effect | Anchor | Citation |
|--------|--------|----------|
| Bilateral royalty split (sovereign vs investor) | Nash 1953 bargaining solution | Econometrica 21:128 |
| Trilateral split (sovereign + occupier + investor) | Shapley 1953 cooperative game value | Annals Math Stud 28:307 |
| Optimal extraction price path | Hotelling 1931 exhaustible resource | J Polit Econ 39:137 |
| Externality assignment (occupied territory) | Coase 1960 social-cost theorem | J Law Econ 3:1 |
| REE coprecipitation yield (≥ 70%) | Byrne 1988 / Bau 1999 Fe-Al hydroxide pH 5-6 envelope | Geochim Cosmochim Acta |
| D2EHPA β_Y/Eu separation factor (2.5) | Sastri-Shibata 2003 D2EHPA hydrometallurgy | Pergamon |
| 5-stage countercurrent for 99% recovery | Kremser 1930 absorption / Treybal 1980 | Industrial Eng Chem |
| Lithium spodumene recovery (75-85%) | USGS Mineral Commodity Summaries 2025 | USGS |
| Reserve-price floor / volatility | LME spot 2024-2025 + IEA Critical Minerals Outlook 2024 | LME / IEA |
| Sovereign-default option pricing | Merton 1974 risky-debt model | J Finance 29:449 |
| Political-risk hedge | Black-Scholes 1973 + MIGA precedent | J Polit Econ 81:637 |
| Receivership precedent (frozen assets) | G7 REPO loan 2024 ($300B Russia frozen / $50B loan) | US Treasury 2024 |
| Verification — territory boundary | Sentinel-1 SAR C-band 12-day revisit / 5 m IW + Goldstein-Werner 1998 InSAR ±1 cm | ESA Copernicus |
| Verification — shipment audit | CTBTO IMS infrasound 0.02-4 Hz + Bayesian source attribution (Stuart-Ord 1991) | CTBTO |
| Reserve estimate uncertainty | JORC 2012 / CRIRSCO mineral resource classification | JORC code |

---

## §2 SIX PRECURSOR DOMAINS (own#33 Block A inheritance)

| # | Precursor | alien_min | Inheritance reason |
|---|-----------|-----------|--------------------|
| 1 | `infra/mining` | 7 | JORC reserve classification + extraction kinetics + Witwatersrand-class deposit geology (sister-overlap with amd-ree-mineshaft-phes) |
| 2 | `infra/jurisprudence` | 7 | International Investment Treaty arbitration (ICSID precedent) + sovereign immunity carve-outs + bilateral investment treaties |
| 3 | `infra/currency-economics` | 7 | Hotelling exhaustible-resource pricing + commodity-currency interaction + reserve-currency seigniorage on royalty flows |
| 4 | `materials/recycling` | 7 | D2EHPA solvent-extraction selectivity + Kremser countercurrent + REE sludge processing (direct sister to amd-ree-mineshaft-phes) |
| 5 | `infra/economics-finance` | 7 | Merton 1974 sovereign default option + Black-Scholes political-risk hedge + Reinhart-Rogoff 2009 base-rate priors |
| 6 | `infra/insurance` | 7 | MIGA political-risk insurance + reinsurance pool math + Lloyd's war-risk syndicate pricing |

All 6 precursors verified present on disk (2026-05-06 check).

---

## §3 FALSIFIER GATES (F-CMCA-MVP-1..5, 90-day to 12-month windows)

| ID | Date | Falsification trigger | Anchor |
|----|------|----------------------|--------|
| F-CMCA-MVP-1 | 2026-08-30 | Nash-bargaining solver on US-UA 2025-04-30 deal terms (50% royalty / joint reconstruction fund) deviates ≥ 15% from observed split → model invalid | Nash 1953 |
| F-CMCA-MVP-2 | 2026-08-30 | D2EHPA β_Y/Eu < 1.5 in bench-scale Donbas-analog AMD synthetic feed → recovery yield assumption falsified | Sastri-Shibata 2003 |
| F-CMCA-MVP-3 | 2026-11-30 | Hotelling price-path simulator vs LME 2024-2025 Li / Ti / Mn / REE spot RMSE > 25% → exhaustible-resource model insufficient | Hotelling 1931 + LME |
| F-CMCA-MVP-4 | 2026-11-30 | Sentinel-1 InSAR detection of mining-activity change at 4 contested-zone sites (Donbas / Greenland / Lobito / Salar) misses ≥ 1 active site → verification stack inadequate | Goldstein-Werner 1998 |
| F-CMCA-MVP-5 | 2027-02-28 | Receivership legal-precedent search returns < 3 enforceable cases of frozen-asset → mineral-rights conversion (G7 REPO 2024 + 2 others) → enforcement pathway unproven | US Treasury / ICSID |

**Hardest unknown**: enforceability of arbitration award against an occupying nuclear-armed power (Russia / China). Mitigation = MIGA + frozen-asset receivership + multilateral consortium dilution of single-state exposure (gated by F-CMCA-MVP-5).

---

## §4 SISTER-DOMAIN STRUCTURE

```
   energy/amd-ree-mineshaft-phes  (SA bet #3, registered 2026-05-01)
            │
            │ shared D2EHPA chemistry
            │ shared 5-stage Kremser
            │ shared REE coprecipitation pH 5-6
            │
            ▼
   infra/critical-mineral-conflict-arbitration  (PROPOSED, 2026-05-06)
            │
            │ generalizes the recovery physics from
            │ "domestic AMD waste valorization" (SA)
            │ to "contested-territory arbitration" (UA / Greenland / DRC)
            ▼
   reusable framework for N future cases
```

Verb-distinction (own#33 sister-pairing rule):
- amd-ree-mineshaft-phes **EXTRACTS** REE from domestic AMD liability (no sovereignty conflict)
- critical-mineral-conflict-arbitration **ALLOCATES** rights to extracted minerals across contested sovereignty (legal/financial layer atop the same chemistry)

---

## §5 GROUND-TRUTH DATASET (already exists, no new collection needed)

| Source | Content | Use |
|--------|---------|-----|
| Ukraine-US Mineral Resources Agreement (2025-04-30) | 55 minerals listed + 50/50 royalty + joint Reconstruction Investment Fund | Nash-bargaining solver calibration (F-MVP-1) |
| US Treasury REPO Act (2024) | $300B Russia frozen / $50B loan structure | Receivership precedent (F-MVP-5) |
| SecDev 2024 Ukraine occupied-territory mineral inventory | $12T mineral wealth / 63% coal / 27% Fe / 50% Mn / 100% Sr under Russian control | Reserve-base inputs |
| USGS Mineral Commodity Summaries 2025 | Global Li / REE / Ti / Mn / Co reserves + production | Hotelling price-path inputs |
| LME 2024-2025 spot history | Daily Li / Ni / Co / Cu / Sn settlement | Volatility + price-floor |
| ESA Copernicus Sentinel-1 archive (2017-present) | Free SAR coverage of all contested zones | F-MVP-4 InSAR baseline |

→ no field deployment required for kick-spec; all data either public or commercially available.

---

## §6 NON-N6 SCOPE BOUNDARIES (own#32 honesty)

This domain is **NOT** about:
- explaining war causation (political science, no physical-limit anchor)
- predicting war outcomes (counterfactual, not falsifiable)
- moral arbitration of occupation legitimacy (out of scope)
- comparing peace-plan provisions (1-shot analysis, not architecture)

This domain **IS** about:
- mineral-rights royalty-split mathematics under contested sovereignty
- recovery-chemistry physical-limit ceilings on what can be extracted
- verification-stack physics for compliance with arbitration awards
- reusable framework spanning Ukraine + Greenland + DRC + Mongolia + Chile

---

## §7 NEXT STEPS (cycle entry checklist)

- [ ] User approval to proceed to full domain SSOT (21-section template, ~1000-1200 lines)
- [ ] Verify 6 precursor domains' alien_grade ≥ 7 (mining + jurisprudence may need uplift)
- [ ] Draft `domains/infra/critical-mineral-conflict-arbitration/critical-mineral-conflict-arbitration.md` per own#15
- [ ] Add §7.1 Python verify Block A-G (Nash solver + Hotelling simulator + D2EHPA mass balance + InSAR baseline check + Merton default-option calc)
- [ ] Update `domains/_index.json` (_total 399 → 400, infra count 59 → 60, _changelog entry "2.4.0")
- [ ] Update `domains/infra/_index.json`
- [ ] own#31 v3.19 lint + own_doc_lint --rule 6 + 15 PASS
- [ ] §7.1 Python verify Block A-G all PASS
- [ ] commit + chflags uchg lock

---

## §8 LINKED REGISTRIES (traceability, prospective)

- **Parent thread**: 2026-05-06 conversation (Ukraine-Russia war deep research)
- **Sister domain**: [`domains/energy/amd-ree-mineshaft-phes/`](../domains/energy/amd-ree-mineshaft-phes/amd-ree-mineshaft-phes.md) — registered 2026-05-01, shares D2EHPA + Kremser + Byrne-Bau coprecipitation
- **Precursor SSOTs**:
  - [`domains/infra/mining/`](../domains/infra/mining/mining.md)
  - [`domains/infra/jurisprudence/`](../domains/infra/jurisprudence/jurisprudence.md)
  - [`domains/infra/currency-economics/`](../domains/infra/currency-economics/currency-economics.md)
  - [`domains/materials/recycling/`](../domains/materials/recycling/recycling.md)
  - [`domains/infra/economics-finance/`](../domains/infra/economics-finance/economics-finance.md)
  - [`domains/infra/insurance/`](../domains/infra/insurance/insurance.md)
- **Registry SSOT (target update)**: [`domains/_index.json`](../domains/_index.json) v2.3.0 → v2.4.0
- **Governance**: own#15 (21-section template) + own#32 (design-by-physics, NOT n=6 force-fit) + own#33 (Block A-G inheritance) + own#31 v3.19 (verify-tautology-ban)
- **External references**: USGS MCS 2025, LME spot history, IEA Critical Minerals Outlook 2024, ESA Copernicus Sentinel-1, CTBTO IMS, ICSID Convention, MIGA, JORC 2012, CRIRSCO, Ukraine-US MRA 2025-04-30, US Treasury REPO Act 2024

---

## §9 FALSIFICATION OF THE KICK-SPEC ITSELF

This kick-spec is **wrong** if any of the following hold:

1. ≥ 1 of the 6 precursor domains scores alien_grade < 7 (would require uplift before fan-in)
2. The Nash bargaining model is structurally inapplicable to trilateral (sovereign + occupier + investor) settings (Shapley value fallback documented but unverified)
3. D2EHPA chemistry from amd-ree-mineshaft-phes does not generalize to Donbas-analog ore (vs AMD sludge) — different feed matrix may invalidate β_Y/Eu transfer
4. Sentinel-1 12-day revisit + 5 m IW resolution is insufficient to detect mining-activity changes at the relevant scale (would require commercial SAR or higher-revisit constellation)
5. No legal precedent exists for converting frozen sovereign assets to mineral-rights receivership (G7 REPO 2024 may be sui generis and non-replicable)

Each of (1)-(5) maps directly to F-CMCA-MVP-1..5 above.

---

**End of kick-spec.**
