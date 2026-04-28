---
category: operational
date: 2026-04-28
parent_witness: design/kick/2026-04-28_b3-docker-hexa-runner-rebuild_omega_cycle.json
parent_proposal: proposals/hexa_weave_mvp_w4_lean4_mk_decision_2026_04_28.md
mission: F-MX-3-c kick infra closure (cycle 7 / fan-out 5/5)
---

# HEXA-WEAVE kick-infra B.3 — registry push bypass plan (docker save/load)

**Status**: PROPOSAL — not executed. Requires explicit user approval before any
host receives the rebuilt image.

**Predecessor**: B.3 cycle-2 witness (above) closed the local Mac
`hexa-runner:latest` with node 20 + npm 10 (image
`sha256:e911bceeb37a5ac157b8efeb30ca53049391db7f4e3a7ae5089edd2c1abd1db2`,
234 MB). Registry push to `docker.io/library/hexa-runner` failed with
`insufficient_scope` because that namespace is reserved by Docker Hub for
official images. As a result the rebuilt image is local-only on this Mac and
remote hosts (ubu1, ubu2, hetzner) continue to hit container-no-node rc=76 on
fallback to the docker hard-landing route.

This proposal enumerates four registry-push bypass options, recommends a
two-tier rollout, and lists the exact safety gates that must be cleared before
any of the options are run.

---

## §1 Options surveyed

| ID | Strategy | One-shot effort | Recurring cost | Auth needed | User approval |
|----|----------|-----------------|----------------|-------------|---------------|
| 1  | Self-hosted local docker registry (`registry:2` on a public host) | medium (~30min) | low | none external | YES — opens registry port |
| 2  | Per-host build (rsync Dockerfile + build-args, then `docker build` on each host) | medium-high | high (drift risk) | none | YES — needs ssh + 200MB+ build per host |
| 3  | GitHub Container Registry (`ghcr.io/<org>/hexa-runner`) | low | very low | needs `need-singularity` org permissions + PAT with `write:packages` | YES — public/private namespace decision + token issuance |
| 4  | Direct image transfer (`docker save | ssh host docker load`) | low (~3min/host) | medium (manual on each rebuild) | none beyond ssh | YES — produces ~234MB transfer per host |

### Recommendation
**Option 4 first** (one-shot transfer to ubu1/ubu2/hetzner so all four hosts
converge on the rebuilt image), **then Option 3** as the durable channel for
future rebuilds. Option 1 (self-hosted registry) is held in reserve in case
ghcr.io permissions cannot be issued. Option 2 is rejected as the primary path:
parallel builds on three hosts have repeatedly drifted (raw 71 falsifier
F-RUNTIME-DRIFT-1 lifted from W3 base-model integration witness).

---

## §2 Option 4 — `docker save | ssh load` execution plan

Manual run-book (NOT automated). Pre-condition checklist below MUST all pass
before any line is executed.

```sh
# ===== preflight (run on Mac) =====
# 0. confirm rebuilt image still exists
docker image inspect hexa-runner:latest \
  --format '{{.Id}} {{.Size}}' \
  | grep -q '^sha256:e911bceeb37a' || { echo "image drift; re-run B.3 build first"; exit 2; }

# 1. capture image digest + bytes for the witness
DIGEST=$(docker image inspect hexa-runner:latest --format '{{.Id}}')
SZ=$(docker image inspect hexa-runner:latest --format '{{.Size}}')
echo "transferring $DIGEST ($SZ bytes)"

# ===== transfer (per host) =====
for HOST in ubu1 ubu2 hetzner; do
  echo "=== $HOST ==="
  # 2a. precondition: ssh reachability
  ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=accept-new $HOST 'echo ok' \
    || { echo "$HOST unreachable; skip"; continue; }
  # 2b. precondition: remote docker daemon up
  ssh $HOST 'docker info >/dev/null 2>&1' \
    || { echo "$HOST docker daemon down; skip"; continue; }
  # 2c. transfer + load (single pipe — no temp file on either end)
  docker save hexa-runner:latest \
    | ssh $HOST 'docker load' \
    || { echo "$HOST load failed"; continue; }
  # 2d. verify on remote
  ssh $HOST "docker image inspect hexa-runner:latest --format '{{.Id}}'" \
    | grep -q "$DIGEST" \
    && echo "$HOST OK" \
    || echo "$HOST digest mismatch"
done
```

### Bandwidth estimate
- 234 MB compressed by docker save's tar layout to ~210 MB on the wire
- Mac → hetzner (Frankfurt): typical 100-200 ms RTT, sustained ~5-15 MB/s on
  residential uplink → ~14-42 s per transfer
- Mac → ubu1/ubu2 (LAN): expected <30 s per transfer
- Total wall-clock: ~2-3 min for all three hosts sequentially

### Failure modes (raw 71 falsifier preregistration)

| ID | Predicate | Mitigation |
|----|-----------|------------|
| F-B3-REG-1 | `docker save` on Mac produces a stream that fails to deserialise on the remote `docker load` (e.g. arch mismatch — Mac is arm64, hosts may be amd64) | architecture pre-check: `ssh $HOST uname -m` MUST match `arm64`/`aarch64` for Mac-built image; if amd64 → use buildx multi-arch rebuild before transfer |
| F-B3-REG-2 | ssh interrupted mid-stream → partial image state on remote (orphan layers, no manifest) | `ssh $HOST docker image prune -f` after a failed load to clear orphans; verification step (2d) catches it |
| F-B3-REG-3 | Remote disk fills (234MB × 3 hosts; existing ω-runner-7 78MB image still on disk) | pre-transfer: `ssh $HOST df -h /var/lib/docker` MUST show ≥1GB free; post-transfer optional `ssh $HOST docker image prune -f` |

---

## §3 Option 3 — ghcr.io durable channel plan

Pre-conditions for execution:
1. User confirms `need-singularity` org has packages enabled
2. User issues a fine-grained PAT with `write:packages` + `read:packages` on
   that org's namespace ONLY (not personal account)
3. User decides public vs private package visibility (private requires every
   pull host to also have a token in `~/.docker/config.json`)
4. Image rebuild adds the ghcr.io tag in addition to `:latest`:

```sh
docker tag hexa-runner:latest ghcr.io/need-singularity/hexa-runner:v1-node20
docker tag hexa-runner:latest ghcr.io/need-singularity/hexa-runner:latest
echo $GHCR_PAT | docker login ghcr.io -u <user> --password-stdin
docker push ghcr.io/need-singularity/hexa-runner:v1-node20
docker push ghcr.io/need-singularity/hexa-runner:latest
```

Once published, host pulls become:
```sh
echo $GHCR_PAT | ssh $HOST 'docker login ghcr.io -u <user> --password-stdin'
ssh $HOST 'docker pull ghcr.io/need-singularity/hexa-runner:latest'
```

Required follow-up patch (out of this proposal scope, in nexus repo):
`scripts/bin/hexa_remote` and `~/core/hive/tool/subagent_dispatch.hexa` should
be updated to fall back to `ghcr.io/need-singularity/hexa-runner:latest` when
the local `hexa-runner:latest` tag is missing.

---

## §4 Option 1 — self-hosted registry (reserve)

Only used if ghcr.io permissions cannot be issued.

```sh
# on hetzner (chosen because it is always-on and externally reachable)
docker run -d -p 5000:5000 --restart=always --name registry registry:2

# on Mac
docker tag hexa-runner:latest hetzner.example:5000/hexa-runner:latest
docker push hetzner.example:5000/hexa-runner:latest

# on ubu1/ubu2
docker pull hetzner.example:5000/hexa-runner:latest
```

Caveats:
- Port 5000 must be opened (firewall rule)
- TLS required for production: `registry:2` defaults to insecure HTTP; needs
  Let's Encrypt + cert mount OR a reverse proxy (nginx/caddy)
- All clients must list `hetzner.example:5000` under
  `/etc/docker/daemon.json#insecure-registries` if TLS is skipped (NOT
  recommended)

Estimated effort to harden: 2-3 cycles — deferred unless ghcr.io is blocked.

---

## §5 Option 2 — per-host build (rejected as primary)

Rejected because:
- Each host's `docker build` adds ~80 s + 200 MB+ pull of debian:12-slim base
- Three independent builds increases drift surface (cf raw 71 F-RUNTIME-DRIFT-1)
- Dockerfile rsync requires keeping `/Users/ghost/core/hexa-lang/docker/runner/`
  in sync across four trees — currently only the Mac copy is patched (ω-runner-8)

Use only if Options 3+4 are simultaneously unavailable.

---

## §6 Safety gates (raw 91 C3 honest)

NO option in this proposal is to be executed without ALL of:

1. User explicit "go" message with the chosen option ID (1/3/4; 2 requires
   double confirmation)
2. Option 4: arch pre-check passes for every targeted host
3. Option 3: PAT issued and stored in `~/.docker/config.json` (NOT in
   environment exports nor committed files)
4. Option 1: TLS plan attached to the proposal supplement
5. raw 13: NO external comms (email/slack/telegram) sent as part of execution;
   all output stays on stdout/stderr of the operator's TTY
6. raw 138 witness: every successful transfer MUST emit a JSONL row to a new
   `state/kick_infra/registry_push.jsonl` ledger (schema: `{ts, option, host,
   image_digest, bytes_sent, exit_code}`)

---

## §7 raw 71 falsifier roll-up (preregistered)

| ID | Predicate | Deadline | Auto check |
|----|-----------|----------|------------|
| F-B3-REG-1 | save→load arch-mismatch on any target host | 2026-05-05 | yes (uname -m vs `Mac arm64`) |
| F-B3-REG-2 | partial image state remains after interrupted ssh stream | 2026-05-05 | yes (image inspect digest mismatch) |
| F-B3-REG-3 | remote disk fills below 200MB free post-load | 2026-05-05 | yes (df parse) |
| F-B3-REG-4 | ghcr.io option chosen but `need-singularity` org refuses package publish | n/a until executed | no (manual confirm from publish error) |
| F-B3-REG-5 | self-hosted registry on hetzner reachable from any non-allowlisted IP within 24h of bring-up | 24h post-bring-up | partial (firewall log audit) |

---

## §8 Cross-link

- B.3 root witness:
  `design/kick/2026-04-28_b3-docker-hexa-runner-rebuild_omega_cycle.json`
- B.5 cascade prevention witness (defensive layer):
  `design/kick/2026-04-28_b5-cascade-block-prevention_omega_cycle.json`
- This-cycle closure witness (omega):
  `design/kick/2026-04-28_kick-infra-closure_omega_cycle.json`
- Mission frame: F-MX-3-c (cycle 7 / fan-out 5/5)
