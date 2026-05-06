# infra/ standalone repository pointers

Cross-reference index of `domains/infra/*` specs that have been extracted into standalone GitHub repositories.

## Active extractions

| Spec(s) | Standalone repo | Extracted | Notes |
|---|---|---|---|
| `climate`, `carbon-capture`, `environment-thermal`, `environmental-protection`, `desal`, `desalination`, `water-treatment`, `geology`, `earthquake-engineering`, `cartography-gis`, `earth-defense`, `hexa-defense` | 🌍 [need-singularity/hexa-earth](https://github.com/need-singularity/hexa-earth) | 2026-05-06 | 12-verb / 4 그룹 (climate + water + geo + defense). hexa-energy cross-link. MIT. |
| `robotics`, `robotics-transport`, `control-automation` | 🤖 [need-singularity/hexa-bot](https://github.com/need-singularity/hexa-bot) | 2026-05-06 | 4-verb robot substrate (+ `life/dog-robot-test` 합류). MIT. |
| `calendar-time-geography` | ⏰ [need-singularity/hexa-time](https://github.com/need-singularity/hexa-time) | 2026-05-06 | `domains/culture/_standalone_repos.md` 의 hexa-time 3-verb 묶음 안에 합류 (`calendar/` verb). |

## Convention

- Spec files in `domains/infra/<slug>/<slug>.md` 은 canonical (uchg-seal). 편집 금지.
- Standalone 레포 (`github.com/need-singularity/*`) 는 작동 구현 + 시드 복사.
- README in each standalone 은 doc/ 시드를 통해 canonical로 역참조; 본 인덱스는 정참조.

## Pending candidates

후속 standalone 후보:
- 🛡️ `hexa-safety` — `airbag` + `fire-science` + `safety` + `ultimate-safety` + `governance-safety-urban` + `civil-engineering`
- 🚗 `hexa-mobility` — `autonomous-driving` + `electric-vehicle` + `aviation` + `motorcycle`
- 💧 `hexa-water` — (이미 hexa-earth에 desal/desalination/water-treatment 합류; 별도 분리 시 후보)
- 💰 `hexa-econ` — `economics` + `currency-economics` + `economics-finance` + `ecommerce-fintech`
- 단독: `forensic-science`, `weather-control`, `architecture`, `construction-structural`, 등 ~40여 개
