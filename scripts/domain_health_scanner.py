#!/usr/bin/env python3
"""
domain_health_scanner.py — ENG-P1-2

318 도메인 건강 스캔:
  - staleness 감지 (mtime 기반, 30일 이상 미수정)
  - 필수 파일 누락 체크 (CLAUDE.md, .md, verify.hexa)
  - 등급 decay 알림 (verify.hexa 내 FAIL/ERROR 키워드)
  - 성숙도 단계 자동 분류 (S1~S5)
  - 섹터별 요약 리포트

사용법:
  python3 scripts/domain_health_scanner.py                # 전체 스캔
  python3 scripts/domain_health_scanner.py --sector compute  # 섹터 지정
  python3 scripts/domain_health_scanner.py --stale-days 14   # staleness 기준 변경
  python3 scripts/domain_health_scanner.py --json            # JSON 출력
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

N6ARCH = Path(os.environ.get("N6ARCH", Path.home() / "Dev" / "n6-architecture"))
DOMAINS = N6ARCH / "domains"
PAPERS_DIR = N6ARCH / "papers"

REQUIRED_FILES = ["CLAUDE.md"]
DESIRED_FILES = ["verify.hexa"]
STANDARD_SECTIONS = ["WHY", "COMPARE", "REQUIRES", "STRUCT", "FLOW", "EVOLVE", "VERIFY"]


def scan_domain(domain_dir: Path, stale_days: int) -> dict:
    """단일 도메인 건강 스캔."""
    name = domain_dir.name
    sector = domain_dir.parent.name

    result = {
        "domain": name,
        "sector": sector,
        "path": str(domain_dir),
        "issues": [],
        "maturity_stage": 1,
        "files": {},
        "grade": None,
        "stale": False,
        "last_modified": None,
    }

    # 파일 존재 체크
    all_files = list(domain_dir.iterdir()) if domain_dir.is_dir() else []
    file_names = {f.name for f in all_files if f.is_file()}

    for req in REQUIRED_FILES:
        if req not in file_names:
            result["issues"].append(f"MISSING: {req}")
    result["files"]["claude_md"] = "CLAUDE.md" in file_names

    # 도메인 .md 파일
    md_file = domain_dir / f"{name}.md"
    has_md = md_file.exists()
    result["files"]["domain_md"] = has_md

    if not has_md:
        result["issues"].append(f"MISSING: {name}.md")
    else:
        result["maturity_stage"] = 2  # registered

    # verify.hexa 체크
    hexa_files = list(domain_dir.glob("*.hexa"))
    verify_files = [f for f in hexa_files if "verify" in f.name.lower()]
    result["files"]["verify_hexa"] = len(verify_files) > 0
    result["files"]["hexa_count"] = len(hexa_files)

    if verify_files:
        result["maturity_stage"] = max(result["maturity_stage"], 3)  # verified
        # FAIL/ERROR 체크
        for vf in verify_files:
            try:
                content = vf.read_text(encoding="utf-8", errors="replace")
                if "FAIL" in content or "ERROR" in content:
                    result["issues"].append(f"GRADE_DECAY: {vf.name} contains FAIL/ERROR")
            except OSError:
                result["issues"].append(f"READ_ERROR: {vf.name}")

    # .md 파일 섹션 체크
    if has_md:
        try:
            md_content = md_file.read_text(encoding="utf-8", errors="replace")
            found_sections = []
            for sec in STANDARD_SECTIONS:
                if re.search(rf"§\d+\s+{sec}|##\s+.*{sec}", md_content, re.IGNORECASE):
                    found_sections.append(sec)
            result["files"]["sections"] = len(found_sections)
            if len(found_sections) < 4:
                result["issues"].append(f"INCOMPLETE: only {len(found_sections)}/7 sections")

            # 등급 추출
            grade_match = re.search(r"\[(\d+\*?)\]", md_content)
            if grade_match:
                result["grade"] = f"[{grade_match.group(1)}]"

            # EXACT 키워드
            if "EXACT" in md_content:
                result["files"]["has_exact"] = True
            else:
                result["files"]["has_exact"] = False
        except OSError:
            result["issues"].append(f"READ_ERROR: {name}.md")

    # Staleness 체크 (mtime 기반)
    latest_mtime = 0
    for f in all_files:
        if f.is_file():
            try:
                mt = f.stat().st_mtime
                if mt > latest_mtime:
                    latest_mtime = mt
            except OSError:
                pass

    if latest_mtime > 0:
        age_days = (time.time() - latest_mtime) / 86400
        result["last_modified"] = datetime.fromtimestamp(latest_mtime, tz=timezone.utc).isoformat()
        result["age_days"] = round(age_days, 1)
        if age_days > stale_days:
            result["stale"] = True
            result["issues"].append(f"STALE: {age_days:.0f} days since last modification")

    # 제품 연결 (간이 체크)
    products_file = PAPERS_DIR / "_products.json"
    if products_file.exists():
        try:
            products = json.loads(products_file.read_text(encoding="utf-8"))
            if isinstance(products, list):
                linked = any(name in str(p) for p in products)
            else:
                linked = name in str(products)
            result["files"]["has_product"] = linked
            if linked:
                result["maturity_stage"] = max(result["maturity_stage"], 4)  # productized
        except (json.JSONDecodeError, OSError):
            result["files"]["has_product"] = False

    # 논문 연결 (간이 체크)
    paper_match = list(PAPERS_DIR.glob(f"*{name}*"))
    result["files"]["has_paper"] = len(paper_match) > 0
    if paper_match:
        result["maturity_stage"] = max(result["maturity_stage"], 5)  # published

    # 이슈 없으면 HEALTHY
    result["health"] = "HEALTHY" if not result["issues"] else "ISSUES"
    result["issue_count"] = len(result["issues"])

    return result


def scan_all(sector_filter: str | None, stale_days: int) -> list[dict]:
    """전체 도메인 스캔."""
    results = []
    for sector_dir in sorted(DOMAINS.iterdir()):
        if not sector_dir.is_dir() or sector_dir.name.startswith((".", "_")):
            continue
        if sector_filter and sector_dir.name != sector_filter:
            continue
        for domain_dir in sorted(sector_dir.iterdir()):
            if not domain_dir.is_dir() or domain_dir.name.startswith((".", "_")):
                continue
            results.append(scan_domain(domain_dir, stale_days))
    return results


def print_summary(results: list[dict]) -> None:
    """요약 리포트 출력."""
    total = len(results)
    healthy = sum(1 for r in results if r["health"] == "HEALTHY")
    stale = sum(1 for r in results if r["stale"])
    missing_verify = sum(1 for r in results if not r["files"].get("verify_hexa", False))
    missing_claude = sum(1 for r in results if not r["files"].get("claude_md", False))
    grade_decay = sum(1 for r in results if any("GRADE_DECAY" in i for i in r["issues"]))

    # 성숙도 분포
    stages = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for r in results:
        stages[r["maturity_stage"]] = stages.get(r["maturity_stage"], 0) + 1

    print(f"\n{'='*60}")
    print(f"  N6-ARCHITECTURE DOMAIN HEALTH SCAN")
    print(f"  {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"{'='*60}")
    print(f"\n  Total domains:      {total}")
    print(f"  Healthy:            {healthy} ({healthy*100//total}%)")
    print(f"  With issues:        {total - healthy} ({(total-healthy)*100//total}%)")
    print(f"  Stale:              {stale}")
    print(f"  Missing verify.hexa:{missing_verify}")
    print(f"  Missing CLAUDE.md:  {missing_claude}")
    print(f"  Grade decay:        {grade_decay}")

    print(f"\n  Maturity Distribution:")
    stage_names = {1: "Discovered", 2: "Registered", 3: "Verified", 4: "Productized", 5: "Published"}
    for s in range(1, 6):
        bar = "#" * (stages[s] // 3)
        print(f"    S{s} {stage_names[s]:<12}: {stages[s]:>4}  {bar}")

    # 섹터별 요약
    sectors = {}
    for r in results:
        sec = r["sector"]
        if sec not in sectors:
            sectors[sec] = {"total": 0, "healthy": 0, "stale": 0, "issues": 0}
        sectors[sec]["total"] += 1
        if r["health"] == "HEALTHY":
            sectors[sec]["healthy"] += 1
        if r["stale"]:
            sectors[sec]["stale"] += 1
        sectors[sec]["issues"] += r["issue_count"]

    print(f"\n  Sector Summary:")
    print(f"  {'Sector':<12} {'Total':>6} {'Healthy':>8} {'Stale':>6} {'Issues':>7}")
    print(f"  {'-'*41}")
    for sec in sorted(sectors, key=lambda s: sectors[s]["healthy"] / max(sectors[s]["total"], 1), reverse=True):
        s = sectors[sec]
        h_pct = s["healthy"] * 100 // max(s["total"], 1)
        print(f"  {sec:<12} {s['total']:>6} {s['healthy']:>5}({h_pct:>2}%) {s['stale']:>6} {s['issues']:>7}")

    # Top issues
    all_issues = []
    for r in results:
        for issue in r["issues"]:
            all_issues.append((r["domain"], r["sector"], issue))

    if all_issues:
        print(f"\n  Top Issues (first 15):")
        for domain, sector, issue in all_issues[:15]:
            print(f"    [{sector}/{domain}] {issue}")
        if len(all_issues) > 15:
            print(f"    ... +{len(all_issues) - 15} more")

    print()


def main():
    parser = argparse.ArgumentParser(description="N6 Domain Health Scanner")
    parser.add_argument("--sector", type=str, help="특정 섹터만 스캔")
    parser.add_argument("--stale-days", type=int, default=30, help="staleness 기준 일수 (기본: 30)")
    parser.add_argument("--json", action="store_true", help="JSON 출력")
    parser.add_argument("--output", type=str, help="리포트 저장 경로")
    args = parser.parse_args()

    results = scan_all(args.sector, args.stale_days)

    if args.json:
        output = {
            "generated": datetime.now(timezone.utc).isoformat(),
            "stale_threshold_days": args.stale_days,
            "total": len(results),
            "healthy": sum(1 for r in results if r["health"] == "HEALTHY"),
            "domains": results,
        }
        out_str = json.dumps(output, ensure_ascii=False, indent=2, default=str)
        if args.output:
            Path(args.output).write_text(out_str, encoding="utf-8")
            print(f"Written to {args.output}")
        else:
            print(out_str)
    else:
        print_summary(results)

        if args.output:
            report = {
                "generated": datetime.now(timezone.utc).isoformat(),
                "total": len(results),
                "domains": results,
            }
            Path(args.output).write_text(
                json.dumps(report, ensure_ascii=False, indent=2, default=str),
                encoding="utf-8",
            )
            print(f"Full report: {args.output}")


if __name__ == "__main__":
    main()
