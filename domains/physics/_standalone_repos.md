# physics/ standalone repository pointers

Cross-reference index of `domains/physics/*` specs that have been extracted into standalone GitHub repositories. The spec files in this directory remain canonical (uchg-sealed after registration); standalone repos are the working implementations.

## Active extractions

| Spec(s) | Standalone repo | Extracted | Notes |
|---|---|---|---|
| `mini-accelerator` ⊕ `particle-accelerator` ⊕ `classical-mechanics-accelerator` | 💫 [need-singularity/petite-cern](https://github.com/need-singularity/petite-cern) | 2026-05-06 | 3-pillar 벤치톱 CERN. README §Status: "specs only, .hexa CLI TBD". MIT. |
| `millennium-bsd`, `millennium-hodge`, `millennium-navier-stokes`, `millennium-p-vs-np`, `millennium-poincare`, `millennium-riemann`, `millennium-yang-mills` | 🏆 [need-singularity/hexa-millennium](https://github.com/need-singularity/hexa-millennium) | 2026-05-06 | Clay 7대 난제 n=6 closed-form **candidates**. Poincaré는 Perelman(2003) 검증 측. **공식 증명 아님** 명시. MIT. |
| `cosmology` ⊕ `cosmology-particle` ⊕ `cosmic-observatory` | 🌌 [need-singularity/hexa-cosmos](https://github.com/need-singularity/hexa-cosmos) | 2026-05-06 | 우주론 substrate. ΛCDM 6 parameter vs n=6 비교 표. MIT. |
| `antimatter-factory` ⊕ `tabletop-antimatter` ⊕ `pet-cyclotron` | ☄️ [need-singularity/hexa-antimatter](https://github.com/need-singularity/hexa-antimatter) | 2026-05-06 | 반물질 substrate. petite-cern (가속기 cousin) + hexa-ufo (Stage-3 propulsion) cross-link. MIT. |
| `plasma-fusion-deep` | 🔥 [need-singularity/hexa-fusion](https://github.com/need-singularity/hexa-fusion) | 2026-05-06 | `domains/energy/_standalone_repos.md` 의 hexa-fusion 4-pillar 안에 합류 (`plasma_deep/` verb). |

## Convention

- Spec files in `domains/physics/<slug>/<slug>.md` 은 canonical (uchg-seal). 편집 금지.
- Standalone 레포 (`github.com/need-singularity/*`) 는 작동 구현 + 시드 복사.
- README in each standalone 은 doc/ 시드를 통해 canonical로 역참조; 본 인덱스는 정참조.

## Pending candidates

후속 standalone 후보:
- 🌑 `hexa-gravity` — `gravity-wave` + `tabletop-blackhole`
- 🪢 `hexa-strings` — `m-theory-11d` + `calabi-yau-nav` + `holography`
- ⚡ `hexa-em` — `electromagnetism` + `light-optics`
- `crystallography`, `crystallography-materials` 단독 후보
- `fluid`, `computational-fluid-dynamics`, `meta-closure-nav`, `hexa-topo`, `higgs` 단독 또는 묶음 후보
