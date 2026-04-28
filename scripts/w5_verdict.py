#!/usr/bin/env python3
"""
w5_verdict.py — HEXA-WEAVE MVP W5 deterministic verdict for 6L1U dry-run inference.

Cycle 15 / 2026-04-28 — supporting script for tool/hexa_weave_w5_setup.hexa Step 8.
Parent proposal: proposals/hexa_weave_w5_supporting_scripts_cycle15_2026_04_28.md
Parent witness:  design/kick/2026-04-28_w5-supporting-scripts-cycle15_omega_cycle.json

Deterministic verdict (raw 53 / raw 91 C3): no LLM judge.

Pass criteria (all required):
  - RMSD < 5.0 Angstrom        (Bio.PDB.Superimposer CA-only)
  - TM-score > 0.4             (TMalign external binary)
  - VRAM peak < 11000 MB       (nvidia-smi -lms 500 csv awk max)
  - inference rc == 0
  - wall < 1800s
  - residue count match (input FASTA len == output PDB CA count)

Exit codes:
  0 PASS
  1 RMSD-FAIL
  2 TM-FAIL
  3 VRAM-FAIL
  4 INFERENCE-FAIL (rc != 0)
  5 WALL-FAIL
  6 RESIDUE-FAIL
  7 USAGE-ERROR

Outputs:
  state/audit/w5_verdict_events.jsonl  (raw 77 schema-versioned ledger; --audit-jsonl)
  <out>.json                            (per-run verdict JSON; --out)

raw 9 hexa-only: stdlib-first; Bio.PDB optional (gracefully degrades to a
                 simple CA-extraction parser when biopython missing).
raw 12 silent-error 금지: every fail path emits stderr line + raw-66 trailer on FAIL.
raw 53 deterministic-verifier: 0 LLM judge.
raw 65 idempotent: SHA-stable inputs -> identical verdict.
raw 66 ai-native trailer: emitted on any FAIL with reason + fix.
raw 77 audit-ledger: schema-versioned JSONL row appended.
raw 91 C3 honest: this script does NOT invoke OpenFold; it only verdicts post-run artifacts.
"""

import argparse
import glob
import json
import os
import platform
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone


SCHEMA = "hexa-weave/w5-verdict/v1"
TM_BIN_DEFAULT = "TMalign"

EXIT_PASS = 0
EXIT_RMSD = 1
EXIT_TM = 2
EXIT_VRAM = 3
EXIT_INFERENCE = 4
EXIT_WALL = 5
EXIT_RESIDUE = 6
EXIT_USAGE = 7


def iso_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def env_capture() -> dict:
    return {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "machine": platform.machine(),
        "ts": iso_now(),
    }


def parse_ca_atoms(pdb_path: str) -> list[tuple[float, float, float]]:
    """stdlib fallback CA-only parser; chain A only. Returns [(x,y,z)]."""
    coords = []
    with open(pdb_path) as f:
        for line in f:
            if not line.startswith("ATOM"):
                continue
            if line[12:16].strip() != "CA":
                continue
            if line[21] != "A":
                continue
            try:
                x = float(line[30:38])
                y = float(line[38:46])
                z = float(line[46:54])
            except ValueError:
                continue
            coords.append((x, y, z))
    return coords


def rmsd_via_biopython(ref_pdb: str, pred_pdb: str) -> tuple[float, str] | None:
    try:
        from Bio.PDB import PDBParser, Superimposer  # type: ignore
    except ImportError:
        return None
    parser = PDBParser(QUIET=True)
    ref = parser.get_structure("ref", ref_pdb)
    pred = parser.get_structure("pred", pred_pdb)
    ref_atoms = [a for a in ref[0]["A"] if a.id == "CA"]
    pred_atoms = [a for a in pred[0]["A"] if a.id == "CA"]
    n = min(len(ref_atoms), len(pred_atoms))
    if n == 0:
        return None
    sup = Superimposer()
    sup.set_atoms(ref_atoms[:n], pred_atoms[:n])
    return float(sup.rms), f"biopython n={n}"


def rmsd_stdlib(ref_pdb: str, pred_pdb: str) -> tuple[float, str] | None:
    """Stdlib fallback: rigid superposition via Kabsch (numpy only); if no numpy,
    return naive RMSD over min-length CA pairs (no rotation)."""
    ref = parse_ca_atoms(ref_pdb)
    pred = parse_ca_atoms(pred_pdb)
    n = min(len(ref), len(pred))
    if n == 0:
        return None
    try:
        import numpy as np  # type: ignore
        a = np.array(ref[:n])
        b = np.array(pred[:n])
        a -= a.mean(axis=0)
        b -= b.mean(axis=0)
        h = a.T @ b
        u, _, vt = np.linalg.svd(h)
        d = np.sign(np.linalg.det(vt.T @ u.T))
        s = np.eye(3)
        s[2, 2] = d
        r = vt.T @ s @ u.T
        b_rot = b @ r.T
        rmsd = float(np.sqrt(((a - b_rot) ** 2).sum() / n))
        return rmsd, f"stdlib-kabsch n={n}"
    except ImportError:
        # last-resort naive (no rotation): correlated upper bound
        d2 = sum((rx - px) ** 2 + (ry - py) ** 2 + (rz - pz) ** 2
                 for (rx, ry, rz), (px, py, pz) in zip(ref[:n], pred[:n]))
        return (d2 / n) ** 0.5, f"stdlib-naive n={n}"


def measure_rmsd(ref_pdb: str, pred_pdb: str) -> tuple[float | None, str]:
    r = rmsd_via_biopython(ref_pdb, pred_pdb)
    if r is not None:
        return r
    r = rmsd_stdlib(ref_pdb, pred_pdb)
    if r is not None:
        return r
    return None, "rmsd-uncomputable"


def measure_tm(ref_pdb: str, pred_pdb: str, tm_bin: str) -> tuple[float | None, str]:
    if shutil.which(tm_bin) is None:
        return None, f"tm-binary-missing path={tm_bin}"
    try:
        out = subprocess.check_output(
            [tm_bin, pred_pdb, ref_pdb],
            timeout=300,
            stderr=subprocess.STDOUT,
            text=True,
        )
    except (subprocess.SubprocessError, FileNotFoundError) as e:
        return None, f"tm-invoke-fail err={type(e).__name__}:{e}"
    # TMalign emits "TM-score=  0.4567 (if normalized by length of Chain_2..." twice
    best = None
    for line in out.splitlines():
        if "TM-score=" in line:
            try:
                v = float(line.split("TM-score=")[1].strip().split()[0])
            except (IndexError, ValueError):
                continue
            if best is None or v > best:
                best = v
    if best is None:
        return None, "tm-parse-fail"
    return best, "tmalign ok"


def measure_vram_peak_mb(csv_glob: str) -> tuple[float | None, str]:
    """Parse nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits -lms 500 logs.
    First column is memory.used in MiB."""
    files = sorted(glob.glob(os.path.expanduser(csv_glob)))
    if not files:
        return None, f"vram-csv-not-found glob={csv_glob}"
    peak = 0.0
    rows = 0
    for fp in files:
        with open(fp) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                tok = line.split(",")[0].strip()
                try:
                    v = float(tok)
                except ValueError:
                    continue
                rows += 1
                if v > peak:
                    peak = v
    if rows == 0:
        return None, f"vram-csv-empty files={len(files)}"
    return peak, f"nvidia-smi rows={rows} files={len(files)}"


def count_residues_fasta(fasta_path: str) -> int:
    n = 0
    with open(fasta_path) as f:
        for line in f:
            if line.startswith(">"):
                continue
            n += sum(1 for c in line.strip() if c.isalpha())
    return n


def emit_trailer(reason: str, fix: str, verdict: dict) -> None:
    print("# === HEXA-WEAVE W5 VERDICT FAILURE TRAILER ===", file=sys.stderr)
    print("schema: hexa-weave/w5-verdict-failure/v1", file=sys.stderr)
    print(f"ts: {iso_now()}", file=sys.stderr)
    print(f"reason: {reason}", file=sys.stderr)
    print(f"fix: {fix}", file=sys.stderr)
    print(f"verdict_summary: rmsd={verdict.get('rmsd_angstrom')} tm={verdict.get('tm_score')} vram_mb={verdict.get('vram_peak_mb')} rc={verdict.get('inference_rc')} wall_s={verdict.get('wall_seconds')} residues={verdict.get('residue_match')}", file=sys.stderr)
    print("contact: multi404error@proton.me", file=sys.stderr)
    print("parent_proposal: proposals/hexa_weave_w5_supporting_scripts_cycle15_2026_04_28.md", file=sys.stderr)
    print("rerun_hint: re-execute Step 8 with reduced batch or --bf16 + check nvidia-smi", file=sys.stderr)
    print("# === END TRAILER ===", file=sys.stderr)


def append_audit(audit_path: str, row: dict) -> None:
    os.makedirs(os.path.dirname(audit_path), exist_ok=True)
    with open(audit_path, "a") as f:
        f.write(json.dumps(row, sort_keys=True) + "\n")


def main() -> int:
    p = argparse.ArgumentParser(description="W5 deterministic verdict (Step 8)")
    p.add_argument("--pred", required=True, help="predicted PDB path")
    p.add_argument("--ref", required=True, help="reference PDB path (RCSB experimental)")
    p.add_argument("--fasta", help="input FASTA path (residue count check)")
    p.add_argument("--vram-csv", required=True, help="nvidia-smi CSV (glob accepted)")
    p.add_argument("--rmsd-max", type=float, default=5.0, help="RMSD threshold Å")
    p.add_argument("--tm-min", type=float, default=0.4, help="TM-score threshold")
    p.add_argument("--vram-max-mb", type=float, default=11000.0, help="VRAM peak threshold MiB")
    p.add_argument("--inference-rc", type=int, default=0, help="observed inference exit code")
    p.add_argument("--wall-seconds", type=float, default=0.0, help="observed wall seconds")
    p.add_argument("--wall-max-seconds", type=float, default=1800.0, help="wall threshold")
    p.add_argument("--tm-bin", default=TM_BIN_DEFAULT, help="TMalign binary path")
    p.add_argument("--out", required=True, help="output verdict JSON path")
    p.add_argument("--audit-jsonl", default="state/audit/w5_verdict_events.jsonl", help="audit ledger path")
    p.add_argument("--seed", default="0xf927314f", help="reproducibility seed log")
    args = p.parse_args()

    for pth in (args.pred, args.ref):
        if not os.path.exists(pth):
            print(f"USAGE-ERROR: missing file {pth}", file=sys.stderr)
            return EXIT_USAGE

    t0 = time.perf_counter()

    rmsd_val, rmsd_note = measure_rmsd(args.ref, args.pred)
    tm_val, tm_note = measure_tm(args.ref, args.pred, args.tm_bin)
    vram_val, vram_note = measure_vram_peak_mb(args.vram_csv)

    ref_ca = len(parse_ca_atoms(args.ref))
    pred_ca = len(parse_ca_atoms(args.pred))
    fasta_len = count_residues_fasta(args.fasta) if args.fasta and os.path.exists(args.fasta) else None
    residue_match = (
        fasta_len is None  # if no FASTA provided, do not gate on residue count
        or fasta_len == pred_ca
    )

    verdict = {
        "schema": SCHEMA,
        "ts": iso_now(),
        "seed": args.seed,
        "env": env_capture(),
        "inputs": {"pred": args.pred, "ref": args.ref, "fasta": args.fasta, "vram_csv": args.vram_csv},
        "rmsd_angstrom": rmsd_val,
        "rmsd_note": rmsd_note,
        "rmsd_threshold": args.rmsd_max,
        "tm_score": tm_val,
        "tm_note": tm_note,
        "tm_threshold": args.tm_min,
        "vram_peak_mb": vram_val,
        "vram_note": vram_note,
        "vram_threshold_mb": args.vram_max_mb,
        "inference_rc": args.inference_rc,
        "wall_seconds": args.wall_seconds,
        "wall_max_seconds": args.wall_max_seconds,
        "ref_ca_count": ref_ca,
        "pred_ca_count": pred_ca,
        "fasta_residue_count": fasta_len,
        "residue_match": residue_match,
        "verdict_wall_s": time.perf_counter() - t0,
        "verdict": "PENDING",
        "exit_code": -1,
    }

    # gate ordering matches exit-code spec (1..6)
    code = EXIT_PASS
    fail_reason = None
    fail_fix = None

    if rmsd_val is None or rmsd_val >= args.rmsd_max:
        code = EXIT_RMSD
        fail_reason = f"RMSD {rmsd_val} >= threshold {args.rmsd_max} (or uncomputable)"
        fail_fix = "verify chain A alignment + check OpenFold output for truncation"
    elif tm_val is None or tm_val <= args.tm_min:
        code = EXIT_TM
        fail_reason = f"TM {tm_val} <= threshold {args.tm_min} (or TMalign missing)"
        fail_fix = "install TMalign binary in PATH; verify pred PDB shape vs ref"
    elif vram_val is None or vram_val >= args.vram_max_mb:
        code = EXIT_VRAM
        fail_reason = f"VRAM peak {vram_val} >= threshold {args.vram_max_mb} (or csv missing)"
        fail_fix = "engage --bf16 + chunk_size=4 + reduce eval_resolution; consult ladder L1->L4"
    elif args.inference_rc != 0:
        code = EXIT_INFERENCE
        fail_reason = f"inference rc {args.inference_rc} != 0"
        fail_fix = "inspect ~/core/hexa-weave/outputs/dryrun.log tail; check CUDA visible + weights present"
    elif args.wall_seconds >= args.wall_max_seconds:
        code = EXIT_WALL
        fail_reason = f"wall {args.wall_seconds}s >= threshold {args.wall_max_seconds}s"
        fail_fix = "warm CUDA cache; verify no thermal throttle; consider sm_120 deepspeed compile"
    elif not residue_match:
        code = EXIT_RESIDUE
        fail_reason = f"FASTA len {fasta_len} != predicted CA {pred_ca}"
        fail_fix = "ensure FASTA chain A only; check OpenFold residue truncation log"

    verdict["verdict"] = "PASS" if code == EXIT_PASS else "FAIL"
    verdict["exit_code"] = code
    if fail_reason:
        verdict["fail_reason"] = fail_reason
        verdict["fail_fix"] = fail_fix

    out_path = os.path.expanduser(args.out)
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(verdict, f, indent=2, sort_keys=True)

    # audit append
    audit_row = {
        "schema": SCHEMA,
        "ts": verdict["ts"],
        "verdict": verdict["verdict"],
        "exit_code": code,
        "rmsd_angstrom": rmsd_val,
        "tm_score": tm_val,
        "vram_peak_mb": vram_val,
        "inference_rc": args.inference_rc,
        "wall_seconds": args.wall_seconds,
        "residue_match": residue_match,
        "out": out_path,
        "seed": args.seed,
    }
    append_audit(args.audit_jsonl, audit_row)

    if code == EXIT_PASS:
        print(f"PASS — rmsd={rmsd_val:.3f} tm={tm_val:.3f} vram={vram_val:.0f}MB rc={args.inference_rc} wall={args.wall_seconds:.1f}s", file=sys.stderr)
    else:
        emit_trailer(reason=fail_reason or "unknown", fix=fail_fix or "inspect verdict JSON", verdict=verdict)

    return code


if __name__ == "__main__":
    sys.exit(main())
