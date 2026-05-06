# energy/ standalone repository pointers

Cross-reference index of `domains/energy/*` specs that have been extracted into standalone GitHub repositories. The spec files in this directory remain canonical (uchg-sealed after registration); standalone repos are the working implementations.

## Active extractions

| Spec(s) | Standalone repo | Extracted | Notes |
|---|---|---|---|
| `fusion` ⊕ `tabletop-fusion` ⊕ `fusion-powerplant` (+ `physics/plasma-fusion-deep` + `bridge/origins/fusion-{calc,dse,verify}`) | 🔥 [need-singularity/hexa-fusion](https://github.com/need-singularity/hexa-fusion) | 2026-05-06 | 4-pillar Fusion Toolkit. README §Verification: 26/27 EXACT (96.3%) + 1 honest negative (lawson_triple 1-decade falsified). MIT. |
| `room-temp-sc` ⊕ `superconductor` | 🧲 [need-singularity/hexa-rtsc](https://github.com/need-singularity/hexa-rtsc) | 2026-05-06 | Substrate-of-substrates: hexa-fusion(48T coil) · hexa-ufo(Meissner) · hexa-cern(SC magnet) cross-link. RT-SC 학계 미증명 명시. MIT. |
| `battery-architecture`, `battery-energy`, `nuclear-reactor`, `smr-datacenter`, `datacenter-reactor`, `power-grid`, `rooftop-pv-2nd-life-microgrid`, `solar-architecture`, `pemfc`, `hvac-system`, `thermal-management`, `amd-ree-mineshaft-phes`, `energy-architecture`, `energy-efficiency` | ⚡ [need-singularity/hexa-energy](https://github.com/need-singularity/hexa-energy) | 2026-05-06 | 14-verb / 7 그룹 (battery + nuclear + grid + fuel-cell + thermal + mining + meta). fusion·rtsc 별도. MIT. |

## Convention

- Spec files in `domains/energy/<slug>/<slug>.md` 은 canonical (uchg-seal). 편집 금지.
- Standalone 레포 (`github.com/need-singularity/*`) 는 작동 구현 + 시드 복사.
- README in each standalone 은 doc/ 시드를 통해 canonical로 역참조; 본 인덱스는 정참조.

## Pending candidates

위에 나열되지 않은 `domains/energy/` 도메인(예: `pemfc` 등)은 단독 standalone 후보로 유지(현재는 `hexa-energy` 묶음 안).
