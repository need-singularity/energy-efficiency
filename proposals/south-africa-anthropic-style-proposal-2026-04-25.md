---
title: South Africa Applied-Tech Proposal
date: 2026-04-25
status: draft
style: anthropic-proposal
scope: development-tech / impact-portfolio
---

## Executive Summary

South Africa is sitting at the intersection of several compounding crises that reinforce one another: an electricity system that no longer reliably delivers power, the world's third-largest tuberculosis burden, ongoing acid mine drainage from a century of gold mining, youth unemployment above 60 percent, accelerating dryland degradation in the Karoo and Limpopo, and rural data costs that price most learners out of the modern internet. We propose a concentrated six-item portfolio chosen at the intersection of high impact and near-term feasibility, where cost curves and policy windows have only recently crossed thresholds that make deployment plausible. The six bets are: rooftop PV plus second-life EV battery community microgrids, CRISPR-Cas13 point-of-care TB and HIV diagnostics, AMD sludge rare-earth recovery paired with mine-shaft pumped hydro storage, youth AI data labeling and RLHF hubs, biochar dryland soil restoration, and LoRa mesh offline learning terminals. Each item has independent value, but the interaction effects (microgrids power cold chains for diagnostics and edtech terminals; youth hubs supply skilled labor across the rest) make the portfolio more than the sum of its parts.

## Why South Africa, Why Now

The compound-crisis framing matters because the failures are not independent. When Eskom load-sheds, clinic refrigerators fail, which ruins TB and HIV sample integrity, which keeps transmission rates high, which keeps health system load high, which competes with industrial demand for scarce grid capacity. A microgrid is not just an energy intervention; it is a diagnostic intervention. Any single-vertical proposal will under-count its own value.

Several cost curves crossed affordability thresholds between 2023 and 2025. Utility-scale PV LCOE in the Northern Cape is now in the USD 30-40 per MWh band. Second-life EV battery packs from European and Asian fleet retirements are landing at roughly one-third of new-cell pricing. CRISPR-Cas13 reagent costs (SHERLOCK / DETECTR family) have dropped roughly an order of magnitude since 2021 as competition entered the diagnostic-grade enzyme market. LoRa end-node hardware is now under USD 10 per node at volume. None of these were true five years ago.

Policy windows are also opening. SAREM (the South African Renewable Energy Masterplan) has localization clauses that favor domestic assembly. NERSA's wheeling rules now permit private generators to move power across the grid to private offtakers. The SSEG (small-scale embedded generation) registration threshold has been raised, simplifying rooftop deployment. The Just Energy Transition Partnership, anchored at USD 8.5 billion of concessional finance from the EU, UK, US, Germany, and France, is actively seeking deployable projects rather than studies.

The demographic clock is the part that does not wait. The current 15-34 cohort is being permanently labor-market scarred; international evidence on long-term unemployment scarring suggests the window to intervene before lifetime earnings are durably suppressed is measured in single-digit years, not decades.

## The Portfolio (Six Bets)

### 1. Rooftop PV + 2nd-life EV battery community microgrids

- **Problem.** Eskom's effective availability factor has fallen below 60 percent. Communities, clinics, and small businesses cannot operate on a grid that fails several hours per day.
- **Approach.** Standardized 50-500 kW rooftop PV arrays on community anchor sites (clinics, schools, cooperatives) coupled with 100-500 kWh second-life lithium battery packs sourced from retired EV fleets. Deploy as community-owned cooperatives or anchor-tenant SPVs.
- **Why this works in SA.** Insolation in the Northern Cape, Free State, and inland Western Cape ranges 2,200-2,500 kWh per square meter per year, among the best in the world. The SSEG threshold revisions reduce registration friction below 100 kW. South Africa has a domestic mining and minerals industry that is itself transitioning fleets, creating a captive supply of second-life batteries within transport range.
- **Theory of change.** A clinic with a microgrid keeps its cold chain. A school with a microgrid keeps its server and its LoRa gateway running. A small workshop with a microgrid runs its CNC and pays back the loan. Each anchor site demonstrates an unsubsidized payback to a watching peer cluster, and replication is local and lender-led rather than donor-led.
- **Cost band.** Roughly USD 800-1,200 per kW installed for PV, USD 150-250 per kWh for second-life storage. Anchor-site systems land at USD 30,000-150,000 capex with 5-8 year payback at current diesel-replacement economics.
- **Hardest unknown.** Battery warranty and second-life cycle-life data are still thin. A pack that degrades twice as fast as projected halves the IRR.

### 2. CRISPR-Cas13 point-of-care TB/HIV diagnostics (SHERLOCK / DETECTR)

- **Problem.** South Africa carries the world's third-largest TB burden and a 13 percent HIV prevalence, but lab-based PCR diagnostics require cold chain, trained technicians, and turnaround that loses patients between test and result.
- **Approach.** Field-deployable Cas13-based isothermal nucleic-acid tests with lateral-flow or fluorescence readout. Target 30-60 minute time-to-result, no thermal cycler, room-temperature lyophilized reagents.
- **Why this works in SA.** Existing GeneXpert deployment has built clinic-level molecular diagnostic literacy, so the workforce skill base exists. SAHPRA has a recently formalized pathway for in-vitro diagnostic registration. Local research groups (UCT, Wits, SU) already work on Cas13 chemistry and would be credible academic partners for validation studies.
- **Theory of change.** A patient walks into a clinic and walks out the same hour with a diagnosis and a treatment script. Loss-to-follow-up between test and treatment, currently a major driver of MDR-TB emergence, drops. Treatment-initiation latency falls from days to hours.
- **Cost band.** Per-test reagent cost target USD 2-5 at scale. Reader hardware (if needed) USD 200-500 per unit. Validation study cost USD 1-3 million for SAHPRA registration.
- **Hardest unknown.** Whether lyophilized Cas13 reagents hold sensitivity and specificity in field humidity over a 6-12 month shelf life. Lab data is promising; sustained field data is not yet there.

### 3. AMD sludge rare-earth recovery + decommissioned-mine-shaft pumped hydro storage

- **Problem.** Acid mine drainage from Witwatersrand and Mpumalanga gold and coal mines is contaminating regional water tables. The cleanup cost is currently treated as a pure liability.
- **Approach.** Process AMD precipitate sludge for recoverable rare-earth elements (REEs) and base metals, converting a liability stream into a partial revenue stream. Pair with pumped hydro energy storage (PHES) using decommissioned mine shafts as the lower reservoir, exploiting the existing 1-3 km vertical drop.
- **Why this works in SA.** The geology is already there: thousands of meters of vertical shaft infrastructure, much of it currently being maintained only to prevent uncontrolled flooding. Mine-shaft PHES has been studied (Sibanye-Stillwater, others) and the engineering is conventional. REE recovery from AMD is at TRL 5-7 in academic literature and ready for pilot scaling.
- **Theory of change.** A mine that today costs the state money to keep dewatered becomes a grid-balancing asset and a critical-minerals asset. The cleanup is paid for by the byproduct rather than by perpetual public subsidy.
- **Cost band.** PHES capex USD 1,500-2,500 per kW; energy capacity USD 50-150 per kWh. REE recovery pilot USD 20-50 million capex for a regional facility. Capital intensive; this is the slow item in the portfolio.
- **Hardest unknown.** REE prices are volatile and the recovery economics flip from positive to negative with a 30-50 percent price move. Hedging structure is non-trivial.

### 4. Youth AI data labeling and RLHF hubs

- **Problem.** Youth unemployment above 60 percent in the 15-24 cohort and above 45 percent in the 15-34 cohort. The cohort has English proficiency, post-secondary education in many cases, and no on-ramp to formal employment.
- **Approach.** Establish 200-1,000 seat annotation and RLHF hubs in Cape Town, Johannesburg, Durban, and secondary cities. Focus on the higher-margin tail: domain-expert annotation (medical, legal, financial, multilingual African languages), red-teaming, and RLHF preference data, rather than commodity bounding-box work.
- **Why this works in SA.** English as a working language. Two-to-three hour timezone overlap with EU and UK clients, which is a hard constraint for synchronous review work. Eleven official languages including Zulu, Xhosa, Afrikaans, Sotho, and Tswana, which positions hubs to serve a multilingual annotation market that India and the Philippines cannot cover. Demand from frontier labs (Anthropic, OpenAI, Google DeepMind, Scale AI, Surge) for high-quality multilingual and domain-expert annotation is currently supply-constrained.
- **Theory of change.** A 22-year-old who would otherwise be permanently scarred takes a six-month training pathway into a hub seat at a wage 2-4x the prevailing informal-sector rate, banks savings, and either advances within the hub (team lead, QA, ML engineer) or exits into a related role with a verifiable employment record.
- **Cost band.** Per-seat capex USD 2,000-4,000 (workstation, building share, training). Operating cost per seat per month USD 600-1,200 fully loaded. Revenue per seat per month USD 1,200-3,500 depending on annotation tier.
- **Hardest unknown.** Whether the multilingual / domain-expert wage premium holds, or whether the annotation market commoditizes faster than the hub can climb the value ladder.

### 5. Biochar dryland soil restoration (Karoo, Limpopo)

- **Problem.** Roughly 10 million hectares of South African rangeland are degrading, with declining soil organic carbon, reduced water-holding capacity, and falling stocking rates. Dryland farmers have no working economic instrument to reverse the trend.
- **Approach.** Pyrolyze locally-available invasive biomass (Prosopis, black wattle, alien acacias) into biochar; apply to dryland soils at 5-20 tonnes per hectare; stack revenue from invasive-species clearance contracts, livestock productivity gains, and verified durable-carbon credits.
- **Why this works in SA.** Working for Water already pays for invasive clearance, providing a labor-cost subsidy for the biomass feedstock. The Karoo and Limpopo have the right hydrology (water-limited, biochar's water-retention benefit is highest in dryland conditions). Verra and Puro.earth biochar methodologies are mature enough to issue credits today.
- **Theory of change.** A farmer clears invasives (paid), pyrolyzes biomass (capex amortized over a co-op kiln), applies biochar (raises carrying capacity by 10-25 percent over 3-5 years), and sells the carbon credit (USD 80-150 per tonne CO2 equivalent in current durable-removal markets). Three revenue streams replace one declining one.
- **Cost band.** Co-op pyrolysis kiln USD 50,000-200,000. Biochar production cost USD 200-400 per tonne. Carbon credit revenue USD 200-450 per tonne biochar applied (using ~2.5 tCO2e per tonne biochar conversion).
- **Hardest unknown.** Voluntary carbon market durability. A second wave of integrity scandals could collapse credit prices and the unit economics with them.

### 6. LoRa mesh offline learning terminals

- **Problem.** Rural data costs in South Africa are among the highest in the world relative to median income. A learner who cannot afford 5 GB per month cannot use the open educational resources that exist.
- **Approach.** Solar-powered LoRa gateways at schools and community centers, paired with low-cost (sub-USD 80) e-paper or low-power Android terminals that sync curriculum, textbooks, and AI tutor responses over LoRa or store-and-forward when a backhaul link is available. Curriculum stack mirrors CAPS (the national curriculum) plus locally translated content.
- **Why this works in SA.** LoRa hardware costs collapsed past the affordability threshold in 2023. The microgrid item powers the gateways. The youth AI hubs can produce the localized content. Existing edtech actors (Siyavula, Snapplify) have curriculum infrastructure to plug into rather than rebuild.
- **Theory of change.** A learner in a village 80 km from a tower gets a terminal, syncs nightly, and accesses the same curriculum as a learner in a Cape Town suburb. Marginal cost per learner per year drops from USD 50-100 in mobile data to under USD 10 in amortized hardware and solar.
- **Cost band.** Gateway USD 300-800. Terminal USD 60-120. Per-learner-year all-in USD 8-15 at scale.
- **Hardest unknown.** Theft and device loss rates in deployment. A 30 percent annual attrition rate destroys the unit economics; a 5 percent rate sustains them.

## Why These Six (And Not Others)

The six were chosen at the intersection of four constraints: each addresses a top-tier compound-crisis bottleneck, each rides a cost curve or capability curve that has only recently made deployment plausible, none requires a regulatory regime that does not currently exist (only execution within existing regimes), and each creates near-term jobs while building durable infrastructure rather than one or the other. Things explicitly excluded include green hydrogen export, which is high-impact but capex-heavy, slow, and dependent on uncertain offtake; coastal desalination, which is important locally but project-scale rather than portfolio-scale; and grid-scale battery storage as a standalone bet, which is better expressed inside item 1 (community microgrids) and item 3 (mine-shaft PHES) than as a separate vertical. We also excluded a generic startup-incubator bet, which has the wrong shape for this kind of compound-crisis intervention.

## Sequencing

**0-12 months.** Launch the items that need only off-the-shelf hardware and existing regulation: rooftop PV plus second-life battery microgrids on 20-50 anchor sites, two to four youth AI hubs at 200-500 seats each, and LoRa edtech pilots at 100-300 schools. None of these require a new regulatory pathway. All can be financed under existing JETP and DBSA / IDC instruments.

**12-24 months.** Items that need regulatory pathway or supply-chain build: SAHPRA registration of the first Cas13 diagnostic with field-validation data from year-one clinic deployments; biochar carbon-credit MRV pipelines and verified issuance under Verra or Puro; expansion of microgrids and AI hubs based on year-one cohort outcomes data.

**24-36 months.** Capital-intensive items: AMD sludge REE recovery pilot at one Witwatersrand or Mpumalanga site; first mine-shaft PHES pilot at 50-200 MW. By this point the earlier items have generated cash flow, employment data, and political capital that lower the financing cost on the heavy capex.

## Risks and Failure Modes

- **Eskom microgrid regulatory rollback.** A future administration could re-tighten SSEG thresholds or wheeling rules under utility-protection lobbying. Early signal: any regulatory consultation that proposes raising registration cost or lowering the threshold size.
- **CRISPR POC regulatory slip.** SAHPRA approval timelines extending past funding window. Early signal: missing the 18-month milestone for first dossier acceptance, or a methodology objection that requires a second validation study.
- **Youth AI hub wage compression.** Race-to-the-bottom on annotation pricing as more low-cost-country hubs enter. Early signal: contract renewal rates with frontier-lab clients dropping below 70 percent or per-seat revenue declining year-over-year.
- **AMD/PHES commodity exposure.** REE recovery economics depend on a basket of volatile prices (neodymium, dysprosium, base metals). Early signal: a sustained 30 percent decline in the recovered-REE basket index over six months.
- **Biochar carbon-credit collapse.** A second wave of integrity scandals (parallel to the 2023 Verra REDD+ episode) erodes biochar credit prices. Early signal: durable-removal price index falling below USD 60 per tonne CO2e or major buyers exiting the market.
- **LoRa edtech execution failure.** Device theft above projection or curriculum localization that does not engage learners. Early signal: terminal attrition above 15 percent annually or daily-active-use below 30 percent of deployed devices.

## Open Questions

- Local manufacturing share versus import for each item (PV modules, battery packs, LoRa hardware, terminals, kilns) given SAREM localization preferences.
- ZAR financing blend across DBSA, IDC, JETP concessional, commercial bank, and equity for each item.
- SAHPRA, NERSA, and DMRE regulatory pathway specifics, including which items can use existing pathways and which require new guidance.
- Skills pipeline split: TVET colleges versus university partnerships versus on-the-job training versus the youth AI hubs themselves as a training feedstock for the other items.
- Operating model per item: which run as local SMEs, which as government partnerships, which as foreign NGO joint ventures, which as hybrid public-private structures.
- Carbon credit MRV partner selection for biochar (Verra, Puro.earth, Isometric, or a new local registry).
- Integration risk: do the six items interact positively (microgrid powers cold chain for diagnostics and gateway for terminals; AI hub trains operators for the rest) or compete for the same scarce skilled labor pool?

## What Would Make This Wrong

The portfolio is the wrong call under several specific futures. If Eskom executes a credible turnaround within 24 months, the microgrid item's economics deflate sharply, and item 1 becomes a hedge rather than a primary bet. If the AI annotation market consolidates rapidly into two or three hyperscale providers and prices collapse, item 4 either has to climb the value chain faster than expected or shrink. If a next-generation TB vaccine proves durably effective in trials and rolls out by 2030, the diagnostic gap that item 2 addresses narrows materially. If durable-removal carbon markets fail to recover from another integrity shock, item 5's third revenue leg disappears. And if commodity prices for REEs and base metals stay depressed through the construction window, item 3's revenue-from-liability story does not close. The honest version of the bet is that we believe the joint probability of all of these going against us simultaneously is low, but any one of them moving against us reshapes the portfolio.

## Closing

This is a portfolio bet, not a wish list. Each of the six items has independent value at deployment scale and is sized to be financeable under current instruments. The reason to do them as a portfolio rather than as six unrelated initiatives is that the interaction effects are real and undercounted: the microgrid keeps the diagnostic cold chain working and the LoRa gateway powered, the youth AI hubs supply skilled operators across the other five, and the biochar and AMD items both convert standing liabilities into productive assets. The expected value of the whole exceeds the sum of the parts only if it is run as a portfolio, with shared sequencing, shared financing structure, and shared learning loops between items.
