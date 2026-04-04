#!/usr/bin/env python3
"""
ready-absorber: ~/Dev/ready/ 망가진/오염 버전에서 유실 정보 추출 → 본체 프로젝트로 라우팅

사용법:
  python3 absorber.py                    # 전체 스캔 (미완료 프로젝트부터)
  python3 absorber.py --project anima    # 특정 프로젝트만
  python3 absorber.py --dry-run          # 실제 전달 없이 발견만
  python3 absorber.py --status           # 현재 진행 상태
  python3 absorber.py --reset            # 상태 초기화
"""

import os, sys, json, hashlib, difflib, subprocess, re, time
from pathlib import Path
from datetime import datetime
from typing import Optional

READY_DIR = Path.home() / "Dev" / "ready"
MAIN_DIR = Path.home() / "Dev"
TOOL_DIR = Path(__file__).parent
STATE_FILE = TOOL_DIR / "state.json"
ROUTES_FILE = TOOL_DIR / "routes.json"
FINDINGS_DIR = TOOL_DIR / "findings"

# 무시할 패턴
IGNORE_PATTERNS = {
    ".git", "__pycache__", "node_modules", ".venv", "venv",
    "target", ".DS_Store", ".mypy_cache", ".pytest_cache",
    "*.pyc", "*.pyo", "*.so", "*.dylib", ".env",
    ".infinite_growth.pid", ".growth", "*.log"
}

BINARY_EXTS = {
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".woff", ".woff2",
    ".ttf", ".eot", ".mp3", ".mp4", ".wav", ".zip", ".tar",
    ".gz", ".bz2", ".pdf", ".bin", ".exe", ".o", ".a"
}

# 고가치 파일 패턴 (우선 스캔)
HIGH_VALUE_PATTERNS = [
    "*.md", "*.py", "*.rs", "*.toml", "*.json",
    "*.ts", "*.tsx", "*.js", "docs/**", "src/**",
    "techniques/**", "experiments/**", "engines/**",
    "hypotheses*", "verification*", "breakthrough*",
    "calc/**", "tools/**"
]


def load_json(path: Path) -> dict:
    with open(path) as f:
        return json.load(f)


def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def is_ignored(path: Path) -> bool:
    parts = path.parts
    for p in parts:
        if p in IGNORE_PATTERNS:
            return True
    if path.suffix in BINARY_EXTS:
        return True
    return False


def file_hash(path: Path) -> Optional[str]:
    try:
        h = hashlib.md5()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()
    except (OSError, PermissionError):
        return None


def safe_read(path: Path, max_lines=500) -> Optional[str]:
    try:
        with open(path, "r", errors="replace") as f:
            lines = []
            for i, line in enumerate(f):
                if i >= max_lines:
                    break
                lines.append(line)
            return "".join(lines)
    except (OSError, PermissionError):
        return None


def diff_files(ready_path: Path, main_path: Path) -> dict:
    """두 파일 간 차이 분석"""
    ready_content = safe_read(ready_path)
    main_content = safe_read(main_path)

    if ready_content is None:
        return {"type": "unreadable", "path": str(ready_path)}

    if main_content is None:
        # 본체에 없는 파일 = ready에만 존재
        return {
            "type": "only_in_ready",
            "path": str(ready_path.relative_to(READY_DIR)),
            "size": ready_path.stat().st_size,
            "lines": ready_content.count("\n"),
            "preview": ready_content[:500]
        }

    if ready_content == main_content:
        return {"type": "identical"}

    # 차이 계산
    ready_lines = ready_content.splitlines(keepends=True)
    main_lines = main_content.splitlines(keepends=True)

    diff = list(difflib.unified_diff(main_lines, ready_lines,
                                      fromfile="main", tofile="ready", n=1))

    added = [l[1:].strip() for l in diff if l.startswith("+") and not l.startswith("+++")]
    removed = [l[1:].strip() for l in diff if l.startswith("-") and not l.startswith("---")]

    return {
        "type": "different",
        "path": str(ready_path.relative_to(READY_DIR)),
        "added_lines": len(added),
        "removed_lines": len(removed),
        "added_preview": added[:20],
        "removed_preview": removed[:20],
        "diff_size": len(diff)
    }


def classify_finding(finding: dict, project: str, routes: dict) -> dict:
    """발견을 분류하고 목적지 결정"""
    path = finding.get("path", "")
    content = finding.get("preview", "") + " ".join(finding.get("added_preview", []))

    # 기본 목적지 = 같은 이름의 프로젝트
    dest = project.lower()

    # 키워드 기반 라우팅 오버라이드
    best_score = 0
    for route_name, route_info in routes.get("routes", {}).items():
        score = 0
        for kw in route_info.get("keywords", []):
            if kw.lower() in content.lower() or kw.lower() in path.lower():
                score += 1
        for pat in route_info.get("file_patterns", []):
            pat_clean = pat.replace("**", "").replace("*", "").strip("/")
            if pat_clean and pat_clean in path:
                score += 2
        if score > best_score:
            best_score = score
            dest = route_name.lower()

    finding["destination"] = dest
    finding["confidence"] = min(best_score / 5.0, 1.0)
    return finding


def scan_project(project_name: str, routes: dict, dry_run=False) -> list:
    """단일 프로젝트 스캔: ready vs main 비교"""
    ready_root = READY_DIR / project_name
    # 대소문자 다를 수 있으므로 매핑
    main_candidates = [
        MAIN_DIR / project_name,
        MAIN_DIR / project_name.lower(),
        MAIN_DIR / project_name.upper(),
        MAIN_DIR / project_name.replace("-", "_"),
    ]
    main_root = None
    for c in main_candidates:
        if c.exists():
            main_root = c
            break

    if not ready_root.exists():
        print(f"  [SKIP] {project_name}: ready 경로 없음")
        return []

    findings = []
    scanned = 0
    skipped = 0

    print(f"\n{'='*60}")
    print(f"  SCANNING: {project_name}")
    print(f"  ready: {ready_root}")
    print(f"  main:  {main_root or '(없음 - 전체가 유실 데이터)'}")
    print(f"{'='*60}")

    for ready_path in sorted(ready_root.rglob("*")):
        if not ready_path.is_file():
            continue
        if is_ignored(ready_path):
            skipped += 1
            continue

        rel = ready_path.relative_to(ready_root)
        scanned += 1

        if main_root:
            main_path = main_root / rel
            result = diff_files(ready_path, main_path)
        else:
            # 본체 자체가 없는 경우 = 전부 유실
            content = safe_read(ready_path)
            result = {
                "type": "only_in_ready",
                "path": str(rel),
                "size": ready_path.stat().st_size if ready_path.exists() else 0,
                "lines": content.count("\n") if content else 0,
                "preview": (content[:500] if content else "")
            }

        if result["type"] in ("only_in_ready", "different"):
            result["project"] = project_name
            result["ready_path"] = str(ready_path)
            finding = classify_finding(result, project_name, routes)
            findings.append(finding)

        if scanned % 1000 == 0:
            print(f"  ... {scanned} files scanned, {len(findings)} findings")

    print(f"  DONE: {scanned} scanned, {skipped} skipped, {len(findings)} findings")
    return findings


def save_findings(project_name: str, findings: list):
    """발견 사항을 파일로 저장"""
    if not findings:
        return

    out_path = FINDINGS_DIR / f"{project_name.lower()}.json"
    save_json(out_path, {
        "project": project_name,
        "timestamp": datetime.now().isoformat(),
        "count": len(findings),
        "by_type": {
            "only_in_ready": len([f for f in findings if f["type"] == "only_in_ready"]),
            "different": len([f for f in findings if f["type"] == "different"]),
        },
        "by_destination": {},
        "findings": findings
    })

    # 목적지별 집계
    data = load_json(out_path)
    dest_counts = {}
    for f in findings:
        d = f.get("destination", "unknown")
        dest_counts[d] = dest_counts.get(d, 0) + 1
    data["by_destination"] = dest_counts
    save_json(out_path, data)

    print(f"  Saved: {out_path} ({len(findings)} findings)")

    # 목적지별 요약
    for dest, count in sorted(dest_counts.items(), key=lambda x: -x[1]):
        print(f"    → {dest}: {count} items")


def print_summary(all_findings: dict):
    """전체 요약 출력"""
    print(f"\n{'='*60}")
    print(f"  ABSORBER SUMMARY")
    print(f"{'='*60}")

    total = 0
    dest_totals = {}
    for proj, findings in all_findings.items():
        count = len(findings)
        total += count
        print(f"  {proj}: {count} findings")
        for f in findings:
            d = f.get("destination", "unknown")
            dest_totals[d] = dest_totals.get(d, 0) + 1

    print(f"\n  TOTAL: {total} findings across {len(all_findings)} projects")
    print(f"\n  ROUTING DESTINATIONS:")
    for dest, count in sorted(dest_totals.items(), key=lambda x: -x[1]):
        print(f"    {dest}: {count}")


def update_state(state: dict, project: str, status: str, findings_count: int = 0):
    """상태 업데이트"""
    state["current_project"] = project if status == "scanning" else None
    state["status"] = status
    state["last_run"] = datetime.now().isoformat()
    if status == "done":
        if project not in state["completed"]:
            state["completed"].append(project)
        state["findings_count"] = state.get("findings_count", 0) + findings_count
    save_json(STATE_FILE, state)


def show_status():
    """현재 상태 출력"""
    state = load_json(STATE_FILE)
    print(f"\n  Status: {state['status']}")
    print(f"  Last run: {state.get('last_run', 'never')}")
    print(f"  Completed: {len(state['completed'])}/{len(state['scan_order'])}")
    print(f"  Total findings: {state.get('findings_count', 0)}")
    print(f"  Routed: {state.get('routed_count', 0)}")

    remaining = [p for p in state["scan_order"] if p not in state["completed"]]
    if remaining:
        print(f"\n  Remaining ({len(remaining)}):")
        for p in remaining:
            print(f"    - {p}")
    else:
        print(f"\n  ALL COMPLETE!")

    # findings 디렉토리 확인
    if FINDINGS_DIR.exists():
        finding_files = list(FINDINGS_DIR.glob("*.json"))
        if finding_files:
            print(f"\n  Finding files ({len(finding_files)}):")
            for ff in sorted(finding_files):
                data = load_json(ff)
                print(f"    {ff.name}: {data.get('count', 0)} findings")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="ready-absorber: 오염본에서 정보 추출")
    parser.add_argument("--project", "-p", help="특정 프로젝트만 스캔")
    parser.add_argument("--dry-run", "-n", action="store_true", help="전달 없이 발견만")
    parser.add_argument("--status", "-s", action="store_true", help="진행 상태 확인")
    parser.add_argument("--reset", action="store_true", help="상태 초기화")
    parser.add_argument("--high-value", action="store_true", help="고가치 파일만 스캔")
    args = parser.parse_args()

    if args.status:
        show_status()
        return

    if args.reset:
        state = load_json(STATE_FILE)
        state["completed"] = []
        state["findings_count"] = 0
        state["routed_count"] = 0
        state["errors"] = []
        state["status"] = "idle"
        state["current_project"] = None
        save_json(STATE_FILE, state)
        print("  State reset.")
        return

    state = load_json(STATE_FILE)
    routes = load_json(ROUTES_FILE)
    FINDINGS_DIR.mkdir(exist_ok=True)

    # 스캔 대상 결정
    if args.project:
        targets = [args.project]
    else:
        targets = [p for p in state["scan_order"] if p not in state["completed"]]

    if not targets:
        print("  All projects already scanned. Use --reset to restart.")
        return

    print(f"\n  Ready Absorber — {len(targets)} projects to scan")
    print(f"  Mode: {'dry-run' if args.dry_run else 'full'}")
    print(f"  Source: {READY_DIR}")

    all_findings = {}
    state["status"] = "running"
    save_json(STATE_FILE, state)

    for project in targets:
        try:
            update_state(state, project, "scanning")
            findings = scan_project(project, routes, dry_run=args.dry_run)
            save_findings(project, findings)
            all_findings[project] = findings
            update_state(state, project, "done", len(findings))
        except Exception as e:
            print(f"  [ERROR] {project}: {e}")
            state["errors"].append({"project": project, "error": str(e), "time": datetime.now().isoformat()})
            save_json(STATE_FILE, state)
            continue

    state["status"] = "complete"
    save_json(STATE_FILE, state)

    print_summary(all_findings)


if __name__ == "__main__":
    main()
