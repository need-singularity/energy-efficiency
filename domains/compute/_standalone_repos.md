# compute/ standalone repository pointers

Cross-reference index of `domains/compute/*` specs that have been extracted into standalone GitHub repositories.

## Active extractions

| Spec(s) | Standalone repo | Extracted | Notes |
|---|---|---|---|
| `chip-architecture`, `chip-isa-n6`, `chip-hexa1`, `chip-design`, `chip-dse-pipeline`, `chip-rtl-gen`, `chip-eda`, `chip-verify-test`, `chip-process`, `chip-materials`, `chip-wafer`, `chip-yield`, `chip-thermal-power`, `chip-packaging`, `advanced-packaging`, `chip-3d`, `chip-hbm`, `chip-interconnect`, `chip-sc`, `chip-npu-n6`, `chip-pim`, `chip-photonic`, `hexa-accel`, `hexa-asic`, `hexa-pim`, `hexa-3d`, `hexa-wafer`, `consciousness-chip`, `consciousness-soc` | 🔲 [need-singularity/hexa-chip](https://github.com/need-singularity/hexa-chip) | 2026-05-06 | 28-verb / 7 그룹 (architecture · design · process · packaging · accelerator · consciousness). hexa-rtsc · hexa-codex · anima cross-link. MIT. |

## Convention

- Spec files in `domains/compute/<slug>/<slug>.md` 은 canonical (uchg-seal). 편집 금지.
- Standalone 레포 (`github.com/need-singularity/*`) 는 작동 구현 + 시드 복사.

## Pending candidates

후속 standalone 후보:
- 단독: `5g-6g-network`, `blockchain`, `browser`, `compiler-os`, `cryptography`, `digital-twin`, `display`, `display-8stack`, `dram`, `exynos`, `ai-efficiency`, `ai-native-architecture` 등 ~40여 개
- 묶음: `hexa-display` (display + display-8stack + LED 등), `hexa-network` (5g-6g + browser + blockchain 등), `hexa-crypto` (cryptography + 등)
