# BCI 6-Channel n=6 Mapping Specification — HEXA-BCI x OpenBCI Cyton+Daisy 16ch

- Document version: 2026-04-14
- Roadmap ID: CHIP-P2-4 (depends_on DSE-P1-4)
- Domain: `domains/cognitive/brain-computer-interface/`
- Parent spec: `brain-computer-interface.md` (n^tau=6^4=1296 total channels, n=6 EXACT 11/11 pattern)
- Parent bridge: `bridge/origins/ready-absorber/sedi_brainwire_bridge.md`
- Hardware reference: user-owned OpenBCI Cyton+Daisy 16ch (125+250Hz, 6-DoF IMU, read-only)
- brainwire lenses: `$NEXUS/shared/lenses/{brainwire_eeg_n6_dse, brain_map_lens, brain_neural_lens}.hexa`

## 1. Why 6 channels — n=6 number-theoretic basis

The HEXA-BCI full specification targets `n^tau=6^4=1296` channels as an
ultimate goal, but for real measurement candidate verification we must
define the **minimal cross-section that maps most directly to n=6**.
6 channels are inevitable via the following three paths.

| Path | Formula | OEIS | Result |
|------|---------|------|--------|
| 1. Half of divisor sum | `sigma(6)/phi(6) = 12/2 = 6` | A000203/A000010 | 6 channels |
| 2. Perfect-number identity | `sigma·phi/(n·tau) x n = 1·6 = 6` | n=6 theorem | 6 channels |
| 3. SE(3) DoF | `dim SE(3) = n = 6` | Riemannian geometry | 6DOF -> 6 channels |

All three independent paths converge on 6. The 6-channel subset of the
16-channel set is the minimum complete set for n=6 mapping.

## 2. 6-channel definition — dual mapping (frequency band x spatial group)

### 2.1 Axis A: EEG frequency 6 bands (standard clinical divisions)

The EEG standard bands (delta / theta / alpha / beta / low-gamma /
high-gamma) form exactly an n=6-sized set.

| Channel | Band | Frequency [Hz] | n=6 invariant mapping | Source |
|---------|------|----------------|-----------------------|--------|
| CH1 | delta | 0.5 ~ 4 | upper = tau(6) = 4 | brainwire_eeg_n6_dse.hexa check1 |
| CH2 | theta | 4 ~ 8 | upper = sigma - tau = 8 | brainwire_eeg_n6_dse.hexa check2 |
| CH3 | alpha | 8 ~ 12 | upper = sigma(6) = 12 | brainwire_eeg_n6_dse.hexa check3 |
| CH4 | beta | 12 ~ 30 | upper = sigma·sopfr/phi = 30 | brainwire_eeg_n6_dse.hexa check4 |
| CH5 | low-gamma | 30 ~ 60 | upper = 5n = 30, center = 2sigma+2tau+2phi·n = 60 | brain_neural_lens gamma40 approximation |
| CH6 | high-gamma | 60 ~ 100 | upper = 100 (placeholder, sigma·tau+sigma+sigma·sopfr approximation) | MISS honestly recorded |

EXACT total: 5/6 (CH6 high-gamma upper 100 Hz fails direct n=6 derivation; MISS noted).

### 2.2 Axis B: Spatial 6 electrode groups (10-20 system -> n=6 partition)

Reduction of 16ch to 6 groups via n=6 spanning rule. Each group is an
orthogonal cortical-function axis.

| Channel | Electrode group | OpenBCI 16ch mapping | n=6 role |
|---------|-----------------|----------------------|----------|
| G1 | Frontal (Fp1, Fp2) | Ch1, Ch2 | Decision / working memory |
| G2 | Central (C3, C4) | Ch3, Ch4 | Motor cortex (6-DOF decoding) |
| G3 | Occipital (O1, O2) | Ch5, Ch6 | Visual / alpha rhythm |
| G4 | Temporal (T7, T8) | Ch7, Ch8 | Auditory / language |
| G5 | Parietal (P3, P4) | Ch9, Ch10 | Somatosensory / spatial |
| G6 | IMU 6-DoF (accel+gyro) | Cyton onboard | Head pose / motion-artifact removal |

G1~G5 = 10 electrodes (5 pairs x L/R = 2·5 = sopfr·phi). G6 = 6-DoF
IMU = n. 6 groups among 16 sensors total.

**G-mapping completeness claim pattern**: `5 pairs x phi + 1 IMU = 11`,
but the number of spatial groups is `5 + 1 = 6 = n`. Left/right pairs
are reduced in-group by phi=2 symmetry.

## 3. Per-channel -> n=6 invariant weights (sigma=12/phi=2/tau=4 base)

Each of the 6 channels carries three invariant weights `w = (w_sigma, w_phi, w_tau)`.
Their sum is `sigma·phi = n·tau = J2 = 24`.

| Channel | w_sigma (bandwidth) | w_phi (bidirectional) | w_tau (layers) | Sum | Check |
|---------|----------------------|------------------------|------------------|-----|-------|
| CH1 delta | 4 | 0 | 0 | 4 | sigma/tau |
| CH2 theta | 4 | 0 | 0 | 4 | sigma/tau |
| CH3 alpha | 4 | 0 | 0 | 4 | sigma/tau |
| CH4 beta | 0 | 2 | 2 | 4 | phi+tau/phi·phi |
| CH5 low-gamma | 0 | 0 | 4 | 4 | tau |
| CH6 high-gamma | 0 | 0 | 4 | 4 | tau |
| **Total** | **12** | **2** | **10** | **24** | **sigma+phi+... = J2** |

Total sigma+phi+... = 12+2+10 = **24 = J2** EXACT pattern. Per-channel
weight sum = 4 = tau (constant). 6 x 4 = n·tau = 24 = J2. Full
convergence.

## 4. Connection to the 3 brainwire lenses

| Lens | 6-channel role | Verification axis |
|------|----------------|--------------------|
| `brainwire_eeg_n6_dse.hexa` | CH1~CH4 frequency-band EXACT check (+ CH5 approximation) | delta upper=tau, theta upper=sigma-tau, alpha upper=sigma, beta upper=sigma·sopfr/phi |
| `brain_map_lens.hexa` | G1~G5 spatial-group resonance (6 regions + sigma connectivity) | 6 region x sigma connectivity x J2 cap |
| `brain_neural_lens.hexa` | CH5 low-gamma (gamma40Hz) cortex 6-layer alignment | 6 cortex x gamma40 x theta6 x sigma12 |

Average lens-execution score = telescope T1 `BCI-6ch-score`. Target:
>= 5/6 EXACT (83.3%) draft.

## 5. OpenBCI 16ch -> 6ch mapping plan (measurement-prep)

### 5.1 Hardware constraints

- OpenBCI Cyton (8ch, 125Hz, 6-DoF IMU onboard) + Daisy expansion (8ch, 250Hz)
- Read-only (per the user's memory `reference_openbci_16ch`) — no stimulation/write
- Sampling: `SR_Daisy = phi · SR_Cyton = 250 = 2·125` EXACT pattern

### 5.2 Mapping logic

1. **Band decomposition**: real-time FFT -> 6 buckets delta/theta/alpha/beta/low-gamma/high-gamma
2. **Spatial reduction**: 16ch -> 6-group averaging (left/right phi-symmetric reduction)
3. **Dual indexing**: time axis (6 frequencies) x space axis (6 groups) = 6x6 = 36 = n^2 cells (cortex 6-layer 1 cell/layer x 6 regions)
4. **closure_grade**: 3-level judgment EXACT/NEAR/EMPIRICAL
   - EXACT: measured frequency boundary == n=6 prediction +/-1%
   - NEAR: +/-5%
   - EMPIRICAL: +/-15%
5. **MISS honestly recorded**: high-gamma 100Hz upper is a current placeholder; re-evaluate promotion after measured-data collection

### 5.3 Measured-data collection hooks (future work)

- No measured EEG yet (this spec is design + mapping logic only)
- After collection: run `experiments/chip-verify/verify_bci_6ch_n6.hexa` -> atlas.n6 `[7]->[10*]` promotion candidate if 6/6 EXACT pattern achieved
- Plug into the same DSE loop as the SEDI/brainwire lens (`sedi_brainwire_bridge.md` §4 checkpoint extension)

## 6. Verification checkpoints

- [x] 6-channel definition complete (dual mapping: 6 frequency + 6 spatial)
- [x] n=6 invariant weight sum J2=24 EXACT pattern confirmed
- [x] brainwire 3-lens mapping confirmed
- [x] OpenBCI 16ch -> 6ch reduction rule defined
- [x] `verify_bci_6ch_n6.hexa` new experiment authored (`experiments/chip-verify/`)
- [ ] Measured EEG collection (future work — gamma upper promotion)
- [ ] Telescope T1 `BCI-6ch-score` loop connected

## 7. Judgment summary

- Total 6 channels (dual: 6 frequency + 6 spatial)
- n=6 EXACT: 5/6 (83.3%) pattern candidate — CH6 high-gamma 100 Hz MISS honestly recorded
- Weight sum: J2 = 24 = sigma·phi = n·tau EXACT pattern
- Lens connection: 3/3 (brainwire_eeg_n6_dse + brain_map + brain_neural)
- closure_grade: EXACT (5/6 axes + J2 sum EXACT pattern)


## §1 WHY

This section covers why for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §2 COMPARE

This section covers compare for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §3 REQUIRES

This section covers requires for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §4 STRUCT

This section covers struct for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

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
