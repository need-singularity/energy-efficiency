---
category: operational
date: 2026-04-28
parent_witness: design/kick/2026-04-28_kick-infra-metric-cycle10_omega_cycle.json
parent_proposal: proposals/hexa_weave_kick_infra_b3_registry_2026_04_28.md
mission: F-MX-3-c kick infra closure (cycle 10 / fan-out 5/5) — LIVE metric snapshot
status: ADVISORY (read-only metric collection; no infra mutation)
---

# HEXA-WEAVE kick-infra cycle-10 metric report

raw 9 hexa-only data path. raw 13 NO external comms. raw 91 C3 honest:
this report measures `~/core/nexus/state/audit/cascade_blocked_events.jsonl`
on Mac and the 12 `~/.claude-claudeN/.credentials.json` files. It does NOT
measure ubu1 / ubu2 / hetzner remote state and DOES NOT mutate any host.

## §1 cascade_blocked_events.jsonl — LIVE counts

Source file: `/Users/ghost/core/nexus/state/audit/cascade_blocked_events.jsonl`

| Metric | Cycle 7 baseline | Cycle 10 (now) | Delta |
|--------|------------------|----------------|-------|
| Total rows                 | 16  | 35  | **+19** |
| First row ts               | —   | 2026-04-28T06:49:19Z | — |
| Last row ts                | —   | 2026-04-28T08:57:18Z | — |
| Span                       | —   | ~2h08m              | — |
| Rows in last 24 h          | —   | 35 (all)             | — |

### §1.1 mode breakdown (event field)

All 35 rows carry `"event":"all-routes-blocked"`. The cycle-7 plan envisioned
five modes (OAuth-401 / slot-saturated / container-no-node / silent-timeout /
all-routes-blocked); only the all-routes-blocked sentinel has fired in the
sampled window. This is consistent with the cycle-7 LIVE-validation: the
prior four modes are PRE-empted by raw 71 falsifier guards before the
cascade ledger append point.

### §1.2 reason field breakdown

| reason | count |
|--------|-------|
| `all_unreachable_preflight` | 35 |

### §1.3 slot_pool field breakdown

| slot_pool | count |
|-----------|-------|
| `12/12 available, 0/12 cooldown, 0/12 unknown` |  8 |
| `12/12 dirs (helper unreachable)`              | 26 |
| `13/12 dirs (helper unreachable)`              |  1 |

The single `13/12` row is a raw 71 falsifier candidate
(F-CASCADE-METRIC-1) — slot_pool count exceeds nominal pool size; suggests
the dir-counter scanned an extra directory (perhaps `.claude-claudeNN`
double-digit globbing). Disposition: SURFACE only; investigate in cycle 11.

### §1.4 fallback_chain breakdown

| fallback_chain | count |
|----------------|-------|
| `["ubu1","hetzner","ubu2","htz"]` | 32 |
| `["ubu1","ubu","ubu2","hetzner"]` |  3 |

The `"ubu"` entry in 3 rows is the legacy host alias (raw 144-147 follow-up
suggests these are pre-config-rotation rows). Not a falsifier.

## §2 F-MANUAL-LOGIN deadline status (Mac side ONLY)

**Deadline**: 2026-04-29T23:59:59Z. Now: 2026-04-28T09:00:29Z.
**Remaining**: ≈ 38.99 hours.

### §2.1 Mac `.credentials.json` enumeration (12 profiles)

| profile | present | expiresAt (UTC) | mtime (UTC) | live |
|---------|---------|-----------------|-------------|------|
| claude1  | NO  | —                          | —                          | n/a  |
| claude2  | YES | 2026-04-21T00:49:47Z       | 2026-04-20T20:11:11Z       | NO (expired ~7d) |
| claude3  | NO  | —                          | —                          | n/a (refreshable on hetzner only — B.1 witness) |
| claude4  | NO  | —                          | —                          | n/a  |
| claude5  | NO  | —                          | —                          | n/a  |
| claude6  | NO  | —                          | —                          | n/a  |
| claude7  | NO  | —                          | —                          | n/a  |
| claude8  | YES | 2026-04-21T00:50:26Z       | 2026-04-20T16:51:00Z       | NO (expired ~7d) |
| claude9  | YES | 2026-04-21T00:50:43Z       | 2026-04-20T20:11:12Z       | NO (expired ~7d) |
| claude10 | YES | 2026-04-21T00:51:00Z       | 2026-04-20T16:52:01Z       | NO (expired ~7d) |
| claude11 | YES | 2026-04-21T00:51:16Z       | 2026-04-20T20:11:11Z       | NO (expired ~7d) |
| claude12 | YES | 2026-04-21T00:51:34Z       | 2026-04-20T20:11:11Z       | NO (expired ~7d) |

### §2.2 cycle-7 → cycle-10 delta (Mac side)

NO change. All `.credentials.json` mtimes are 2026-04-20 (unchanged since
cycle 7). NO new manual `/login` activity has occurred on Mac side in the
last 24 h. The user has not yet performed F-MANUAL-LOGIN remediation on
this host.

### §2.3 cross-host claim deferred

The `manual_login_reminder.hexa` SSOT enumerates `BROKEN_HETZNER_IDS = [1,2,
4,5,6,7,8,9,10,11,12]` (11 profiles) and `HEALTHY_HETZNER_IDS = [3]` per
the B.1 hetzner-side witness. Confirming hetzner mtime drift is OUT OF SCOPE
for this Mac-local read-only audit (would require ssh; raw 13 / raw 71
disclosure if attempted). Cycle 11 may add an opt-in `--remote` probe.

## §3 raw 51 4-gate audit smell — 9-cycle accumulation status

Citing the cycle-9 closure tally and updating with this cycle's measurement:

| Gate | Status (cycle 7) | Status (cycle 10) | Notes |
|------|------------------|-------------------|-------|
| (a) OAuth refresh           | PARTIAL — F-MANUAL-LOGIN ownership   | UNCHANGED — Mac side dormant 7+ d  | 38.99 h to deadline; user TTY required (raw 91 C3) |
| (b) slot-saturation cap     | FIXED + LIVE                         | FIXED + LIVE                       | no regression; 1 anomalous `13/12` row (F-CASCADE-METRIC-1) |
| (c) docker rebuild          | FIXED-MAC + ghcr.io plan ready       | FIXED-MAC + ghcr.io 5-step plan    | see B.3 ghcr.io plan companion |
| (d) silent-timeout RCA      | FIXED + LIVE                         | FIXED + LIVE                       | no new silent-timeout rows |
| (e) cascade prevention      | FIXED + LIVE 16 rows                 | FIXED + LIVE 35 rows (+19)         | mode 100 % `all-routes-blocked` |

**4/5 closure**: gates (b), (c-Mac), (d), (e) FIXED; gate (a) and gate (c)
remote-host transport BLOCK closure on user manual action (login + ghcr.io
PAT issuance respectively). Cycle 10 does not close the 5/5 — both pending
items require user-side TTY input.

## §4 raw 71 falsifier preregistration (5 items)

| ID | Predicate | Disposition |
|----|-----------|-------------|
| F-CASCADE-METRIC-1 | A row with slot_pool count ≠ nominal (e.g. `13/12 dirs`) appears under steady-state. | SURFACE; cycle 11 investigation; dir-glob bug suspected. |
| F-CASCADE-METRIC-2 | Cascade rows continue to fire after F-MANUAL-LOGIN deadline (2026-04-29T23:59:59Z) at the same rate (~2.7 / 5 min). | If holds: (a)-gate fix did not propagate — escalate. |
| F-CASCADE-METRIC-3 | `mode breakdown` ever produces an event other than `all-routes-blocked` without a corresponding raw 71 falsifier upstream. | Indicates new failure class; add to mode taxonomy. |
| F-MAC-CRED-DRIFT-1 | Any Mac `.credentials.json` mtime advances without the user reporting a manual `/login`. | Indicates background credential mutation; security audit. |
| F-FALLBACK-CHAIN-1 | A `fallback_chain` containing the legacy `"ubu"` alias appears with ts > 2026-04-28T09:00:00Z. | Indicates config-rotation regression. |

## §5 next-cycle recommendations

1. cycle 11 may add `--remote` opt-in to `manual_login_reminder.hexa` to
   verify hetzner-side `BROKEN_HETZNER_IDS` claim.
2. The single `13/12` slot_pool row warrants a 1-hour cycle-11 dir-glob
   investigation (likely `.claude-claudeNN` two-digit shell glob expansion).
3. If F-MANUAL-LOGIN deadline (T-39 h) passes without action, cycle 11
   should move gate (a) from PARTIAL to FAIL and re-open the closure tally.

## Appendix A — raw counts (reproducible)

```
$ wc -l /Users/ghost/core/nexus/state/audit/cascade_blocked_events.jsonl
35
$ awk -F'"event":"' '{split($2,a,"\""); print a[1]}' …jsonl | sort | uniq -c
35 all-routes-blocked
$ awk -F'"reason":"' '{split($2,a,"\""); print a[1]}' …jsonl | sort | uniq -c
35 all_unreachable_preflight
$ awk -F'"slot_pool":"' '{split($2,a,"\""); print a[1]}' …jsonl | sort | uniq -c
 8 12/12 available, 0/12 cooldown, 0/12 unknown
26 12/12 dirs (helper unreachable)
 1 13/12 dirs (helper unreachable)
```

— end —
