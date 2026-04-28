---
category: operational
date: 2026-04-28
parent_witness: design/kick/2026-04-28_kick-infra-metric-cycle10_omega_cycle.json
companion: proposals/hexa_weave_kick_infra_b3_registry_2026_04_28.md (cycle 7 — Option 4 docker save/load + Option 3 ghcr.io)
mission: F-MX-3-c kick infra closure (cycle 10 / fan-out 5/5) — B.3 ghcr.io durable-channel detail plan
status: PROPOSAL — not executed. Requires explicit user approval AND a `write:packages` PAT before any push.
---

# HEXA-WEAVE B.3 — `ghcr.io/need-singularity/hexa-runner` push plan (durable channel)

## §0 Why ghcr.io is the durable channel

The cycle-7 B.3 registry-bypass proposal selected **Option 4 (docker save/ssh
load)** as the immediate one-shot transfer for ubu1/ubu2/hetzner convergence,
and **Option 3 (ghcr.io)** as the durable channel for future rebuilds. This
plan details Option 3.

Why ghcr.io over Docker Hub:
- Docker Hub `docker.io/library/<name>` is reserved for official images
  (cycle-7 push failed with `insufficient_scope`); user-namespace push would
  need a paid org plan.
- ghcr.io ties access to existing GitHub `need-singularity` org credentials —
  no new account, no new billing surface.
- ghcr.io supports private images at no charge; visibility is per-image.
- Native `docker buildx` multi-arch support for arm64 (Mac) → amd64 (ubu1/
  ubu2/hetzner) crossover; F-B3-REG-1 falsifier mitigation.

## §1 Five-step plan

> Each step lists exact command + expected exit + safety gate. NONE of these
> commands are run by this plan. Execution requires user invocation.

### Step 1 — issue PAT with `write:packages` scope

User action (browser, GitHub UI):
1. Navigate to <https://github.com/settings/tokens?type=beta> (fine-grained)
   or <https://github.com/settings/tokens> (classic).
2. **Token type**: classic PAT preferred (fine-grained PATs do not yet
   support all GHCR write paths reliably; verify per current GitHub docs).
3. **Expiration**: 90 days max (raw 65 minimal-blast-radius).
4. **Scopes**: `write:packages`, `read:packages`, `delete:packages`
   (the last only if cycle-12+ image GC is anticipated).
5. **Org access**: must include the `need-singularity` org if the image is
   to be pushed under that org namespace.
6. Copy the generated token. **Do NOT paste it into chat.** User stores it
   locally (e.g. `pass insert ghcr/hexa-runner-pat` or
   `~/.config/hexa/ghcr.token` mode 0600).

**Safety gate G1**: PAT NEVER appears in any committed file, in any tool
stdout, or in any cycle witness JSON. If a PAT leaks accidentally, user
MUST revoke it via the same UI before continuing.

### Step 2 — local docker login to ghcr.io

User action (Mac shell, NEVER inside this agent):
```sh
# Read PAT from a file (or pass-style cmd) — never interpolated in shell history.
read -rs GHCR_PAT < ~/.config/hexa/ghcr.token   # or: GHCR_PAT=$(pass show ghcr/hexa-runner-pat)
echo "$GHCR_PAT" | docker login ghcr.io -u <github-username> --password-stdin
unset GHCR_PAT
```

Expected: `Login Succeeded`. Credentials are now stored in
`~/.docker/config.json` (raw 65 disclosure: this file is mode 0600 by
default, but contains a base64-encoded PAT; NEVER commit it).

**Safety gate G2**: `docker login` MUST be run interactively by the user;
this agent does NOT run it (raw 91 C3 honest — TTY-bound credential entry).

### Step 3 — tag local image for ghcr.io

User action (Mac shell):
```sh
DIGEST=$(docker image inspect hexa-runner:latest --format '{{.Id}}')
echo "tagging $DIGEST"
docker tag hexa-runner:latest ghcr.io/need-singularity/hexa-runner:latest
docker tag hexa-runner:latest ghcr.io/need-singularity/hexa-runner:2026-04-28
docker tag hexa-runner:latest ghcr.io/need-singularity/hexa-runner:cycle-10
docker images ghcr.io/need-singularity/hexa-runner   # verify 3 tags
```

Expected: 3 tag lines, all with the same image ID. (The `latest` floating
tag + a date tag + a cycle tag give us atomic rollback granularity.)

**Safety gate G3**: tagging MUST happen on the cycle-7 verified image
(sha256:e911bceeb37a…). If the image ID has drifted, re-run B.3 build
before tagging.

### Step 4 — push to ghcr.io (and optionally multi-arch buildx)

User action (Mac shell — single-arch arm64 first):
```sh
docker push ghcr.io/need-singularity/hexa-runner:cycle-10
docker push ghcr.io/need-singularity/hexa-runner:2026-04-28
docker push ghcr.io/need-singularity/hexa-runner:latest
```

Expected each: `<digest>: digest: sha256:… size: <n>` and exit 0.

For multi-arch (arm64 + amd64) durable channel, prefer `buildx`:
```sh
docker buildx create --name hexa-builder --use 2>/dev/null || docker buildx use hexa-builder
docker buildx build \
  --platform linux/arm64,linux/amd64 \
  --tag ghcr.io/need-singularity/hexa-runner:cycle-10 \
  --tag ghcr.io/need-singularity/hexa-runner:latest \
  --push \
  -f ./hexa-runner/Dockerfile ./hexa-runner
```

This eliminates F-B3-REG-1 (arch mismatch) entirely on the durable channel.

**Safety gate G4**: visibility check after first push:
```sh
gh api -H 'Accept: application/vnd.github+json' \
  /orgs/need-singularity/packages/container/hexa-runner \
  | jq '{name, visibility, url}'
```
If visibility is `public` and that is unintended, set it private via UI:
<https://github.com/orgs/need-singularity/packages/container/hexa-runner/settings>.

### Step 5 — remote pull on ubu1 / ubu2 / hetzner

For each remote host, user action (or scripted via this agent only with
explicit approval):
```sh
# 5a. login on the remote (PAT is the same; user pastes it via ssh tty,
#     or scp's a token file with mode 0600 then deletes it)
ssh ubu1 'echo "$GHCR_PAT" | docker login ghcr.io -u <github-username> --password-stdin'

# 5b. pull
ssh ubu1 'docker pull ghcr.io/need-singularity/hexa-runner:cycle-10'

# 5c. retag locally so existing fallback chain code finds it
ssh ubu1 'docker tag ghcr.io/need-singularity/hexa-runner:cycle-10 hexa-runner:latest'

# 5d. verify
ssh ubu1 "docker image inspect hexa-runner:latest --format '{{.Id}}'"
```

Repeat for `ubu2` and `hetzner`. The `cycle-10` immutable tag avoids
the `latest` race condition during partial rollouts.

**Safety gate G5**: post-pull, verify the rebuilt image actually fixes
container-no-node (rc=76). Run the smallest reproducible kick on the
remote to confirm node 20 + npm 10 are present:
```sh
ssh ubu1 'docker run --rm hexa-runner:latest sh -c "node --version && npm --version"'
```
Expected: `v20.x.x` and `10.x.x`. If either prints `command not found`,
ROLLBACK by `docker tag <previous-image-id> hexa-runner:latest` on that
host before any kick traffic resumes.

## §2 Failure modes (raw 71 preregistration — 5 items)

| ID | Predicate | Mitigation |
|----|-----------|------------|
| F-B3-GHCR-1 | PAT leaks into a committed file (cycle witness, marker, or `.docker/config.json` accidentally tracked). | pre-commit hook: deny `ghp_*`, `gho_*`, `ghu_*`, `ghs_*`, `ghr_*` patterns; revoke PAT on detection. |
| F-B3-GHCR-2 | `docker buildx` multi-arch produces an amd64 layer mismatched with the arm64 manifest list (rare GHCR manifest-v2 bug). | post-push, `docker buildx imagetools inspect ghcr.io/need-singularity/hexa-runner:cycle-10` MUST list both linux/arm64 + linux/amd64 entries; if not, re-push. |
| F-B3-GHCR-3 | Remote `docker pull` succeeds but the cached image on the remote is from a previous tag race (latest mutated mid-pull on another host). | always pull the immutable `cycle-10` tag, not `latest`; retag locally on each host. |
| F-B3-GHCR-4 | `need-singularity` org PAT-issuance permission is not yet granted to the user (org membership state). | preflight: `gh api /user/orgs` must list `need-singularity`; if not, fall back to user-namespace `ghcr.io/<user>/hexa-runner`. |
| F-B3-GHCR-5 | GHCR rate-limit on anonymous pull during a remote without `docker login` (the package is public but rate-limited). | always `docker login` on remotes too; or set image visibility to public ONLY if no proprietary code is baked into the image. |

## §3 Approval matrix

| Action | Requires user approval? | Why |
|--------|--------------------------|-----|
| Step 1 (issue PAT) | YES — user-only | PAT issuance is a TTY/browser action; agent CANNOT do it (raw 91 C3). |
| Step 2 (`docker login`) | YES — user-only | TTY credential entry; agent MUST NOT see PAT (raw 65). |
| Step 3 (tag) | YES — read-only on credentials, but mutates local docker state | could be agent-run with explicit go-ahead |
| Step 4 (push) | YES — explicit approval per push | first push is blast-radius decision (visibility); agent MUST confirm before pushing |
| Step 5 (remote pull/retag) | YES — per-host approval | each ssh action is a remote-state mutation under raw 13 transport disclosure |

The combined plan REQUIRES explicit user approval at minimum for Steps 1, 2,
and 4. Steps 3 and 5 may be agent-executed only after a one-line approval
("approve B.3 ghcr Step <N>") from the user.

## §4 Rollback plan

1. `docker pull` the previous image id on each remote (snapshot before
   Step 5 runs): `ssh hostX 'docker image inspect hexa-runner:latest --format "{{.Id}}"' > /tmp/prev_img_<host>`.
2. On rollback: `ssh hostX "docker tag $(cat /tmp/prev_img_<host>) hexa-runner:latest"`.
3. Optionally delete the bad ghcr.io tag (requires `delete:packages` scope
   on the PAT, or UI deletion).

## §5 Cycle-10 closure summary

This plan does NOT close the B.3 remote-host transport gate. It documents
the user-actionable durable channel. Combined with the cycle-7 Option-4
plan, the user has TWO independent paths to remote-host convergence:
- Option 4 (one-shot, ~3 min, no PAT) for immediate cycle-10 closure
- Option 3 (durable, this plan) for cycle-11+ rebuilds

raw 91 C3 honest: until the user runs at least one of these plans, gate
(c)-remote remains OPEN regardless of how many cycles accumulate.

— end —
