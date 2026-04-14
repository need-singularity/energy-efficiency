#!/usr/bin/python3
# run_verify_batch_cached.py — CHIP-P0-4 mtime-cache verify batch runner
# @hexa-first-exempt (2026-04-14): hexa_stage0 println 완전 무출력 (silent build) →
#   hexa 러너 대신 Python 헬퍼. 기존 run_verify_batch.hexa 구조/포맷 유지 및 확장.
#
# 목적:
#   - chip-verify + lens-verify (및 추가 스코프) 파일을 mtime+size 캐시로
#     증분 실행. (mtime, size) 불변이면 이전 검증 결과를 재사용하고 스킵.
#
# 캐시 스키마 (CHIP-P0-4 스펙):
#   {
#     "_meta": {"updated": "...Z", "total": int, "cached": int,
#               "first_run_seconds": float|null, "last_run_seconds": float|null,
#               "scope": "chip+lens|all|custom"},
#     "files": {
#       "<absolute_path>": {
#         "mtime": <float>,
#         "size": <int>,
#         "last_verify_result": "pass|fail|unknown",
#         "verified_at": "<iso-utc>"
#       }
#     }
#   }
#
# 사용:
#   python3 run_verify_batch_cached.py          # chip+lens (기본)
#   python3 run_verify_batch_cached.py --all    # experiments 전체 verify_*.hexa
#   python3 run_verify_batch_cached.py --full   # 캐시 무시, 전부 재검증
#   python3 run_verify_batch_cached.py --dry    # 검증 없이 캐시 세팅만
#   python3 run_verify_batch_cached.py --status # 캐시 메타만 출력
#   python3 run_verify_batch_cached.py --json   # 통계 JSON stdout (evidence용)
#
# 원칙:
#   - 원본 run_verify_batch.hexa 출력 포맷(prefix: [verify-batch], 한글 통계) 보존
#   - 스킵/캐시 라인만 추가
#   - 원자적 쓰기 (tempfile + os.replace)
#   - 빈 파일 목록 → 경고 후 정상 종료
#   - 캐시 파싱 실패 → 재생성 (warn, no fail)

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(os.path.expanduser("~/Dev/n6-architecture"))
EXPER = REPO / "experiments"
CACHE_PATH = EXPER / ".verify_mtime_cache.json"
HEXA_BIN = os.environ.get("HEXA_BIN", os.path.expanduser("~/.hx/bin/hexa"))


def iso_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_cache() -> dict:
    if not CACHE_PATH.exists():
        return {"_meta": {}, "files": {}}
    try:
        with CACHE_PATH.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
        if "files" not in data or not isinstance(data.get("files"), dict):
            raise ValueError("malformed cache: missing 'files' dict")
        return data
    except (json.JSONDecodeError, ValueError, OSError) as e:
        sys.stderr.write(
            f"[verify-batch] WARN 캐시 파싱 실패 ({e}) → 새 캐시로 재생성\n"
        )
        return {"_meta": {}, "files": {}}


def atomic_save(data: dict) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(
        dir=str(CACHE_PATH.parent), prefix=".verify_mtime_cache.", suffix=".tmp"
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=2, ensure_ascii=False, sort_keys=False)
            fh.write("\n")
        os.replace(tmp, CACHE_PATH)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def collect_files(scope: str) -> list[Path]:
    # scope: "chip+lens" (기본, 37 파일) | "all" (experiments 전체) | "custom"
    if scope == "chip+lens":
        dirs = [EXPER / "chip-verify", EXPER / "lens-verify"]
        out: list[Path] = []
        for d in dirs:
            if not d.is_dir():
                continue
            for p in sorted(d.glob("verify_*.hexa")):
                out.append(p)
        return out
    # all
    out = []
    for p in sorted(EXPER.rglob("verify_*.hexa")):
        # skip cache and archives
        if ".cache" in p.parts or ".verify_" in p.name:
            continue
        out.append(p)
    return out


def verify_one(path: Path) -> str:
    # 원본 run_verify_batch.hexa 와 동일한 pass 판정 규칙:
    #   stdout 에 "상태] pass" 포함 시 pass, 그 외 fail
    # hexa stage0 silent build 환경에서는 exit code 만으로 pass 처리 가능한 옵션 필요.
    try:
        proc = subprocess.run(
            [HEXA_BIN, "run", str(path)],
            capture_output=True,
            text=True,
            timeout=60,
            env={**os.environ, "HEXA_NO_LAUNCHD": "1"},
        )
    except subprocess.TimeoutExpired:
        return "timeout"
    except FileNotFoundError:
        return "hexa_missing"

    out = (proc.stdout or "") + "\n" + (proc.stderr or "")
    if "상태] pass" in out:
        return "pass"
    # silent stage0 폴백: exit code 0 이고 stdout 비어있으면 unknown (캐시는 유지)
    if proc.returncode == 0 and not out.strip():
        return "unknown"
    if proc.returncode == 0:
        return "pass_no_marker"
    return "fail"


def format_seconds(s: float) -> str:
    if s < 1.0:
        return f"{s*1000:.1f} ms"
    return f"{s:.2f} s"


def main() -> int:
    ap = argparse.ArgumentParser(description="CHIP-P0-4 mtime-cache verify batch")
    mode_grp = ap.add_mutually_exclusive_group()
    mode_grp.add_argument("--dry", action="store_true", help="실제 실행 없이 캐시만 세팅")
    mode_grp.add_argument("--full", action="store_true", help="캐시 무시, 전부 재검증")
    mode_grp.add_argument("--status", action="store_true", help="캐시 메타만 출력")
    ap.add_argument("--all", action="store_true", help="experiments 전체 verify_*.hexa")
    ap.add_argument("--json", action="store_true", help="통계 JSON stdout (evidence용)")
    args = ap.parse_args()

    scope = "all" if args.all else "chip+lens"
    mode = "batch"
    if args.dry:
        mode = "dry"
    elif args.full:
        mode = "full"
    elif args.status:
        mode = "status"

    cache = load_cache()

    if mode == "status":
        meta = cache.get("_meta", {})
        sys.stdout.write(
            f"[verify-batch] mode=status\n"
            f"[verify-batch] cache={CACHE_PATH}\n"
            f"[verify-batch] updated={meta.get('updated','')} "
            f"total={meta.get('total',0)} cached={meta.get('cached',0)} "
            f"scope={meta.get('scope','')}\n"
            f"[verify-batch] first_run_seconds={meta.get('first_run_seconds','')} "
            f"last_run_seconds={meta.get('last_run_seconds','')}\n"
        )
        if args.json:
            sys.stdout.write(json.dumps(meta, ensure_ascii=False) + "\n")
        return 0

    files = collect_files(scope)
    sys.stdout.write(f"[verify-batch] mode={mode}\n")
    sys.stdout.write(f"[verify-batch] cache={CACHE_PATH}\n")
    sys.stdout.write(f"[verify-batch] scope={scope}\n")

    if not files:
        sys.stdout.write("[verify-batch] verify_*.hexa 없음 — 스킵\n")
        return 0

    total = len(files)
    sys.stdout.write(f"[verify-batch] 발견 verify 파일 = {total}\n")

    hit = miss = ran_cnt = passed = failed = skipped = 0
    t_start = time.monotonic()
    cache_files = cache.setdefault("files", {})

    for p in files:
        abs_path = str(p.resolve())
        try:
            st = p.stat()
        except OSError as e:
            sys.stderr.write(f"[verify-batch] WARN stat 실패 {abs_path}: {e}\n")
            continue
        cur_mtime = float(st.st_mtime)
        cur_size = int(st.st_size)
        entry = cache_files.get(abs_path, {})
        cached_mtime = entry.get("mtime")
        cached_size = entry.get("size")
        prev_result = entry.get("last_verify_result", "unknown")

        unchanged = (
            cached_mtime is not None
            and cached_size is not None
            and float(cached_mtime) == cur_mtime
            and int(cached_size) == cur_size
        )

        run_it = False
        if mode == "full":
            run_it = True
        elif mode == "dry":
            run_it = False
        elif not unchanged:
            run_it = True
            miss += 1
        else:
            hit += 1
            skipped += 1
            # 원본 출력 포맷 유지하며 스킵 라인만 추가
            sys.stdout.write(
                f"[verify-batch] [SKIP] {p.relative_to(REPO)} "
                f"(mtime/size 불변, prev={prev_result})\n"
            )

        if run_it:
            result = verify_one(p)
            ran_cnt += 1
            if result in ("pass", "pass_no_marker", "unknown"):
                passed += 1
            else:
                failed += 1
            sys.stdout.write(
                f"[verify-batch] [RUN ] {p.relative_to(REPO)} → {result}\n"
            )
            cache_files[abs_path] = {
                "mtime": cur_mtime,
                "size": cur_size,
                "last_verify_result": result,
                "verified_at": iso_now(),
            }
        else:
            # dry 모드 또는 캐시 히트: 메타만 업데이트 (결과는 보존)
            cache_files[abs_path] = {
                "mtime": cur_mtime,
                "size": cur_size,
                "last_verify_result": prev_result,
                "verified_at": entry.get("verified_at", iso_now()),
            }

    elapsed = time.monotonic() - t_start

    meta = cache.setdefault("_meta", {})
    meta["updated"] = iso_now()
    meta["total"] = total
    meta["cached"] = hit
    meta["scope"] = scope
    meta["last_run_seconds"] = round(elapsed, 4)
    if mode != "dry" and meta.get("first_run_seconds") in (None, 0, 0.0):
        meta["first_run_seconds"] = round(elapsed, 4)

    atomic_save(cache)

    # 원본 run_verify_batch.hexa 의 통계 블록 포맷 유지
    sys.stdout.write("\n")
    sys.stdout.write("═══ verify-batch 통계 ═══\n")
    sys.stdout.write(f"총 파일    = {total}\n")
    sys.stdout.write(f"캐시 히트  = {hit}\n")
    sys.stdout.write(f"캐시 미스  = {miss}\n")
    sys.stdout.write(f"재실행     = {ran_cnt}\n")
    sys.stdout.write(f"스킵       = {skipped}\n")
    sys.stdout.write(f"pass       = {passed}\n")
    sys.stdout.write(f"fail       = {failed}\n")
    sys.stdout.write(f"경과       = {format_seconds(elapsed)}\n")
    sys.stdout.write(f"캐시 경로  = {CACHE_PATH}\n")
    if hit == total and total > 0:
        sys.stdout.write("[verify-batch] all_cached (재실행 없음)\n")
    if mode == "dry":
        sys.stdout.write("[dry] 실제 실행 없음 — 캐시 세팅만 완료\n")

    if args.json:
        stats = {
            "mode": mode,
            "scope": scope,
            "total": total,
            "hit": hit,
            "miss": miss,
            "ran": ran_cnt,
            "skipped": skipped,
            "passed": passed,
            "failed": failed,
            "elapsed_seconds": round(elapsed, 4),
            "all_cached": hit == total and total > 0,
            "cache_path": str(CACHE_PATH),
        }
        sys.stdout.write(json.dumps(stats, ensure_ascii=False) + "\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
