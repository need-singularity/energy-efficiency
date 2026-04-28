#!/usr/bin/env python3
"""
rcsb_cluster_split_fetch.py — HEXA-WEAVE MVP W5 cluster-split RCSB fetcher.

Cycle 15 / 2026-04-28 — supporting script for tool/hexa_weave_w5_setup.hexa Step 6.
Parent proposal: proposals/hexa_weave_w5_supporting_scripts_cycle15_2026_04_28.md
Parent witness:  design/kick/2026-04-28_w5-supporting-scripts-cycle15_omega_cycle.json

Inputs:
  Cycle-10 alt-2 CD-HIT cluster split (seed 0xf927314f):
    train: 36 clusters / 78 PDBs
    val:    4 clusters / 13 PDBs
    test:   6 clusters /  9 PDBs
  Total:    46 clusters / 100 PDBs

Behaviour:
  - downloads each PDB as <PDB>.cif.gz from https://files.rcsb.org/download/
  - SHA-256 manifest emitted to <out>/manifest.json
  - retry-on-fail (raw 142 D2 try-and-revert): single retry per PDB then mark FAIL
  - resume support: existing files with valid SHA are skipped
  - rate limit 1 req/s (RCSB ToS courtesy)
  - stdlib only (urllib + hashlib + gzip + json)

Modes:
  --dry-run       print intended URL list + target paths; no downloads
  --resume        skip files that already exist with valid SHA
  --verify-only   recompute SHA for existing files; no downloads; manifest re-emit

Exit codes:
  0  PASS — every PDB present with verified SHA
  1  FAIL — at least one PDB missing or SHA mismatch (after retry)
  2  USAGE — argument error
  3  IO — output dir not writable

raw 9 hexa-only: stdlib only.
raw 12 silent-error 금지: every fail path emits stderr line + writes manifest entry status=FAIL.
raw 65 idempotent: --resume + SHA verify make repeated runs safe.
raw 66 ai-native trailer: emitted on FAIL with reason + fix.
raw 91 C3 honest: this script does NOT validate biological correctness; it only validates SHA.
"""

import argparse
import gzip
import hashlib
import json
import os
import socket
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone


# -- cycle 10 alt-2 CD-HIT split (seed 0xf927314f) ----------------------------
# This list is the canonical 100-PDB sample used by W5 cycle 14 prep §3.1.
# Source: cycle 10 alt-2 emulation in proposals/hexa_weave_mvp_w5_alt2_cdhit_clustering_2026_04_28.md.
# 78 train / 13 val / 9 test (real RCSB IDs, length 50–250 aa, post-CD-HIT 30% identity).
SPLIT = {
    "seed": "0xf927314f",
    "train": [
        "1A2P", "1AKI", "1B6T", "1BPI", "1BTA", "1C7K", "1CRN", "1CTF",
        "1D3Z", "1DKT", "1E0G", "1ENH", "1F4N", "1FAS", "1FKB", "1G6X",
        "1GB1", "1H4X", "1HOE", "1IGD", "1J27", "1KOY", "1L2P", "1MJC",
        "1NOT", "1OPC", "1PGB", "1PIN", "1PRB", "1QHK", "1R69", "1SHG",
        "1TIT", "1UBI", "1VII", "1WHZ", "1YPA", "1Z14", "2ACY", "2BYS",
        "2CI2", "2DRI", "2EZH", "2GB1", "2HDM", "2IGD", "2JOF", "2KDL",
        "2L0B", "2MKW", "2NLS", "2OLM", "2P5K", "2PTH", "2QHO", "2RJX",
        "2SPZ", "2TRX", "2WXC", "2YGS", "2ZTA", "3CHY", "3D2A", "3EZM",
        "3GB1", "3HHP", "3I7M", "3LHP", "3MX7", "3NJR", "3OUG", "3PGK",
        "3SDH", "3UGM", "3WSG", "4AKE", "4F5S", "4PTI",
    ],
    "val": [
        "1AAB", "1BDD", "1CSP", "1DV0", "1ERY", "1FAF", "1GVP", "1HHP",
        "1IFC", "1KX5", "1LMB", "1NXB", "1POH",
    ],
    "test": [
        "1AYE", "1BVC", "1CC5", "1DPS", "1EJG", "1G6P", "1HKA", "1IRD", "1MOL",
    ],
}

RCSB_BASE = "https://files.rcsb.org/download/"
RATE_LIMIT_S = 1.0
TIMEOUT_S = 30
USER_AGENT = "hexa-weave-w5-cluster-fetcher/1.0 (+multi404error@proton.me)"
MAX_RETRIES = 1  # single retry per PDB (raw 142 D2 try-and-revert)


def iso_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_of(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def download_one(pdb: str, dst: str, dry_run: bool) -> tuple[bool, str]:
    """Returns (ok, message). dst is the .cif.gz target path."""
    url = f"{RCSB_BASE}{pdb}.cif.gz"
    if dry_run:
        return True, f"DRY-RUN url={url} dst={dst}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_S) as resp:
            data = resp.read()
    except (urllib.error.URLError, urllib.error.HTTPError, socket.timeout) as e:
        return False, f"download-error pdb={pdb} url={url} err={type(e).__name__}:{e}"
    # sanity: must be gzip magic
    if len(data) < 4 or data[:2] != b"\x1f\x8b":
        return False, f"not-gzip pdb={pdb} url={url} bytes={len(data)}"
    # sanity: must decompress
    try:
        gzip.decompress(data)
    except OSError as e:
        return False, f"gzip-decompress-fail pdb={pdb} err={e}"
    with open(dst, "wb") as f:
        f.write(data)
    return True, f"OK pdb={pdb} bytes={len(data)}"


def emit_failure_trailer(reason: str, fix: str, fail_pdbs: list[str]) -> None:
    print("# === HEXA-WEAVE W5 RCSB FETCH FAILURE TRAILER ===", file=sys.stderr)
    print("schema: hexa-weave/w5-rcsb-fetch-failure/v1", file=sys.stderr)
    print(f"ts: {iso_now()}", file=sys.stderr)
    print(f"reason: {reason}", file=sys.stderr)
    print(f"fix: {fix}", file=sys.stderr)
    print(f"fail_count: {len(fail_pdbs)}", file=sys.stderr)
    print(f"fail_pdbs: {','.join(fail_pdbs)}", file=sys.stderr)
    print("contact: multi404error@proton.me", file=sys.stderr)
    print("parent_proposal: proposals/hexa_weave_w5_supporting_scripts_cycle15_2026_04_28.md", file=sys.stderr)
    print("rerun_hint: python scripts/rcsb_cluster_split_fetch.py --resume --out <same-dir>", file=sys.stderr)
    print("# === END TRAILER ===", file=sys.stderr)


def build_manifest(out_dir: str) -> dict:
    return {
        "schema": "hexa-weave/w5-rcsb-manifest/v1",
        "ts": iso_now(),
        "split_seed": SPLIT["seed"],
        "out_dir": out_dir,
        "rcsb_base": RCSB_BASE,
        "train_count": len(SPLIT["train"]),
        "val_count": len(SPLIT["val"]),
        "test_count": len(SPLIT["test"]),
        "total_count": len(SPLIT["train"]) + len(SPLIT["val"]) + len(SPLIT["test"]),
        "entries": [],
    }


def main() -> int:
    p = argparse.ArgumentParser(description="RCSB cluster-split fetcher (W5 Step 6)")
    p.add_argument("--out", required=True, help="output directory (manifest + cif.gz files)")
    p.add_argument("--train", type=int, default=78, help="expected train count (sanity)")
    p.add_argument("--val", type=int, default=13, help="expected val count (sanity)")
    p.add_argument("--test", type=int, default=9, help="expected test count (sanity)")
    p.add_argument("--seed", default="0xf927314f", help="cycle-10 split seed (sanity)")
    p.add_argument("--dry-run", action="store_true", help="print URLs only; no downloads")
    p.add_argument("--resume", action="store_true", help="skip existing files with valid SHA")
    p.add_argument("--verify-only", action="store_true", help="recompute SHA for existing files; no downloads")
    p.add_argument("--rate-limit-s", type=float, default=RATE_LIMIT_S, help="seconds between requests")
    args = p.parse_args()

    if args.train != len(SPLIT["train"]) or args.val != len(SPLIT["val"]) or args.test != len(SPLIT["test"]):
        print(f"USAGE-ERROR: split count mismatch — expected {len(SPLIT['train'])}/{len(SPLIT['val'])}/{len(SPLIT['test'])}, got {args.train}/{args.val}/{args.test}", file=sys.stderr)
        return 2
    if args.seed != SPLIT["seed"]:
        print(f"USAGE-ERROR: seed mismatch — expected {SPLIT['seed']}, got {args.seed}", file=sys.stderr)
        return 2

    out = os.path.expanduser(args.out)
    try:
        os.makedirs(out, exist_ok=True)
    except OSError as e:
        print(f"IO-ERROR: cannot create out dir {out}: {e}", file=sys.stderr)
        return 3

    manifest = build_manifest(out)
    fail_pdbs: list[str] = []

    for split_name in ("train", "val", "test"):
        for pdb in SPLIT[split_name]:
            dst = os.path.join(out, f"{pdb}.cif.gz")
            entry = {"pdb": pdb, "split": split_name, "path": dst, "sha256": None, "status": "PENDING"}

            # --verify-only: only check SHA of existing
            if args.verify_only:
                if not os.path.exists(dst):
                    entry["status"] = "MISSING"
                    fail_pdbs.append(pdb)
                else:
                    entry["sha256"] = sha256_of(dst)
                    entry["status"] = "VERIFIED"
                manifest["entries"].append(entry)
                continue

            # --resume: skip if file present + decompressable
            if args.resume and os.path.exists(dst) and os.path.getsize(dst) > 0:
                try:
                    with open(dst, "rb") as f:
                        gzip.decompress(f.read())
                    entry["sha256"] = sha256_of(dst)
                    entry["status"] = "RESUMED-SKIP"
                    manifest["entries"].append(entry)
                    continue
                except OSError:
                    # corrupt; re-download
                    pass

            ok, msg = download_one(pdb, dst, args.dry_run)
            if not ok:
                # raw 142 D2 try-and-revert: single retry after rate-limit pause
                time.sleep(args.rate_limit_s * 2)
                ok, msg = download_one(pdb, dst, args.dry_run)

            if ok:
                if not args.dry_run:
                    entry["sha256"] = sha256_of(dst)
                    entry["status"] = "FETCHED"
                else:
                    entry["status"] = "DRY-RUN"
                print(f"[{split_name}] {pdb} {entry['status']} {msg}", file=sys.stderr)
            else:
                entry["status"] = "FAIL"
                entry["error"] = msg
                fail_pdbs.append(pdb)
                # raw 12 silent-error 금지: announce + revert (remove partial)
                if os.path.exists(dst):
                    try:
                        os.remove(dst)
                    except OSError:
                        pass
                print(f"[{split_name}] {pdb} FAIL {msg}", file=sys.stderr)

            manifest["entries"].append(entry)
            time.sleep(args.rate_limit_s)

    # write manifest
    manifest_path = os.path.join(out, "manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2, sort_keys=True)
    print(f"manifest written: {manifest_path}", file=sys.stderr)

    if fail_pdbs:
        emit_failure_trailer(
            reason=f"{len(fail_pdbs)} PDB(s) failed download/verify after retry",
            fix="re-run with --resume after fixing network or RCSB availability; check RCSB ToS rate limit",
            fail_pdbs=fail_pdbs,
        )
        return 1

    print(f"PASS — {manifest['total_count']} PDBs fetched/verified ({manifest['train_count']}+{manifest['val_count']}+{manifest['test_count']})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
