#!/usr/bin/env python3
"""
Monte Carlo v9.3 도메인별 분해
──────────────────────────────
scripts/monte_carlo_v93.py 기반.
reality_map 노드를 level 기준으로 도메인별 그룹화 후
각 도메인마다 n=6 적중률 · z-score · 표본수를 독립 산출.

출력: 콘솔 + docs/mc-v93-domain-breakdown.md
"""

import json
import math
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from monte_carlo_v93 import (
    REALITY_MAP,
    N6,
    normalize_expr,
    count_matches,
    safe_eval_expr,
    get_arith,
    values_match,
)

N_SIMULATIONS = 2000   # 도메인별로 반복하므로 감축 (전체와 동일 랜덤 분포 근사)
SEED = 42
OUT_MD = ROOT / "docs" / "mc-v93-domain-breakdown.md"

# ── level → 상위 도메인 매핑 ─────────────────────────────
DOMAIN_MAP = {
    "L-2_sub_quark":   "입자물리(서브쿼크)",
    "L-1_quark":       "입자물리(쿼크)",
    "L0_particle":     "입자물리(표준모형)",
    "L1_atom":         "원자물리",
    "L2_bond":         "화학결합",
    "L2_law":          "화학결합",
    "L3_molecule":     "분자화학",
    "L4_genetic":      "유전/분자생물",
    "L5_bio":          "생물학",
    "L5_material":     "소재/재료",
    "L6_discovery":    "돌파발견(L6)",
    "L7_celestial":    "천체물리",
    "L8_galactic":     "은하/우주구조",
    "L9_cosmological": "우주론",
    "L10_multiversal": "다중우주",
}

def classify(level: str) -> str:
    if not level:
        return "기타"
    if level in DOMAIN_MAP:
        return DOMAIN_MAP[level]
    # L6_* 서브카테고리 묶기
    if level.startswith("L6_"):
        sub = level[3:]
        bio_like = {"biology","zoology","botany","ecology","genetics_applied",
                    "immunology","anatomy","physiology","neuroscience",
                    "pharmacology","epidemiology","medicine","paleontology"}
        phys_like = {"thermodynamics","atmospheric_physics","astronomy",
                     "mechanical","electrical","civil","aerospace","nuclear",
                     "robotics","computing","cryptography"}
        chem_like = {"chemistry","mineralogy"}
        earth_like = {"geology","glaciology","volcanology","seismology",
                      "hydrology","oceanography","meteorology","geography"}
        human_like = {"sociology","psychology","anthropology","history",
                      "demography","political_science","law","education",
                      "economics","linguistics","philosophy","ethics",
                      "aesthetics","logic","mathematics","archaeology",
                      "architecture","literature","cinema","visual_arts",
                      "cuisine","music"}
        if sub in bio_like:   return "생명과학(L6)"
        if sub in phys_like:  return "공학/물리(L6)"
        if sub in chem_like:  return "화학(L6)"
        if sub in earth_like: return "지구과학(L6)"
        if sub in human_like: return "인문사회(L6)"
        return "L6_기타"
    return "기타"

# ── 특수 도메인: HIV / 암치료 (id·bt_refs·claim 기반) ────
def extra_domains(node) -> list:
    """하나의 노드가 여러 특수 도메인에 속할 수 있음"""
    tags = []
    blob = " ".join(str(node.get(k,"")) for k in ("id","claim","detail","cause","source"))
    blob_l = blob.lower()
    if "hiv" in blob_l or "aids" in blob_l:
        tags.append("HIV")
    if any(k in blob for k in ("암","종양","cancer","tumor","oncolog")):
        tags.append("암치료")
    if any(k in blob_l for k in ("nanobot","nanomed","나노봇")):
        tags.append("나노의학")
    return tags

# ── 데이터 로드 ─────────────────────────────────────────
def load_nodes():
    with open(REALITY_MAP) as f:
        data = json.load(f)
    return data["nodes"]

def build_evaluables(nodes):
    """노드 → {'domain': [evaluable,...]} 리스트, 원본 노드 보관"""
    groups = defaultdict(list)
    for nd in nodes:
        if nd.get("grade") != "EXACT":
            continue
        measured = nd.get("measured")
        if not isinstance(measured, (int, float)):
            continue
        norm = normalize_expr(nd.get("n6_expr",""))
        if norm is None:
            continue
        item = {
            "id": nd.get("id","?"),
            "measured": measured,
            "expr": norm,
        }
        # 주 도메인
        groups[classify(nd.get("level",""))].append(item)
        # 특수 도메인 (중복 허용)
        for tag in extra_domains(nd):
            groups[tag].append(item)
    return groups

# ── 도메인별 Monte Carlo ────────────────────────────────
def run_domain(evals, n_sims=N_SIMULATIONS, seed=SEED):
    if not evals:
        return None
    n6_hits = count_matches(evals, N6)
    n6_ratio = n6_hits / len(evals)
    rng = random.Random(seed)
    candidate_range = [i for i in range(2,101) if i != N6]
    rand_hits = []
    for _ in range(n_sims):
        n_rand = rng.choice(candidate_range)
        rand_hits.append(count_matches(evals, n_rand))
    mean = sum(rand_hits)/len(rand_hits)
    var = sum((x-mean)**2 for x in rand_hits)/len(rand_hits)
    std = math.sqrt(var) if var>0 else 1e-10
    z = (n6_hits-mean)/std
    p = sum(1 for x in rand_hits if x>=n6_hits)/len(rand_hits)
    return {
        "n_samples": len(evals),
        "n6_hits": n6_hits,
        "n6_ratio": n6_ratio,
        "mean_rand": mean,
        "std_rand": std,
        "z": z,
        "p": p,
    }

def main():
    print("="*64)
    print("  Monte Carlo v9.3 · 도메인별 분해")
    print("="*64)
    nodes = load_nodes()
    groups = build_evaluables(nodes)
    print(f"총 도메인 수: {len(groups)}")
    print(f"총 평가노드(중복제외 근사): {sum(len(v) for v in groups.values())}")
    print()

    results = {}
    for dom in sorted(groups.keys()):
        evals = groups[dom]
        if len(evals) < 3:       # 표본 과소 도메인 스킵
            continue
        res = run_domain(evals)
        if res is None:
            continue
        results[dom] = res
        print(f"[{dom:22s}] N={res['n_samples']:4d}  hit={res['n6_hits']:4d}  "
              f"ratio={res['n6_ratio']*100:5.1f}%  z={res['z']:6.2f}  p={res['p']:.4f}")

    # 정렬: z 내림차순
    ranked = sorted(results.items(), key=lambda kv: -kv[1]["z"])
    weak = [d for d,r in ranked if r["z"] < 3]
    strongest = ranked[0]
    weakest = ranked[-1]
    avg_z = sum(r["z"] for _,r in ranked)/len(ranked)

    # ── Markdown 저장 ───────────────────────────────────
    lines = []
    lines.append("# Monte Carlo v9.3 · 도메인별 분해 리포트")
    lines.append("")
    lines.append(f"- 기반: `scripts/monte_carlo_v93.py` + `scripts/mc_v93_by_domain.py`")
    lines.append(f"- 데이터: `~/Dev/nexus/shared/reality_map.json`")
    lines.append(f"- 도메인 수: **{len(results)}**")
    lines.append(f"- 도메인별 시뮬레이션: {N_SIMULATIONS}회 (seed={SEED})")
    lines.append(f"- 평균 z-score: **{avg_z:.2f}**")
    lines.append(f"- 최강 도메인: **{strongest[0]}** (z={strongest[1]['z']:.2f})")
    lines.append(f"- 최약 도메인: **{weakest[0]}** (z={weakest[1]['z']:.2f})")
    lines.append("")
    lines.append("## 도메인별 강도 순위")
    lines.append("")
    lines.append("| 순위 | 도메인 | 표본수 N | n=6 적중 | 적중률 | 랜덤 평균 | 랜덤 σ | z-score | p-value | 강도 |")
    lines.append("|---:|---|---:|---:|---:|---:|---:|---:|---:|:---:|")
    for i,(dom,r) in enumerate(ranked,1):
        strength = "강" if r["z"]>=5 else ("중" if r["z"]>=3 else "약")
        lines.append(f"| {i} | {dom} | {r['n_samples']} | {r['n6_hits']} | "
                     f"{r['n6_ratio']*100:.1f}% | {r['mean_rand']:.1f} | "
                     f"{r['std_rand']:.2f} | {r['z']:.2f} | {r['p']:.4f} | {strength} |")
    lines.append("")
    lines.append("## 약점 도메인 (z < 3)")
    lines.append("")
    if weak:
        for d in weak:
            r = results[d]
            lines.append(f"- **{d}** — N={r['n_samples']}, z={r['z']:.2f}, "
                         f"적중률 {r['n6_ratio']*100:.1f}% · 보강 필요")
    else:
        lines.append("없음 — 모든 도메인이 z >= 3 통과.")
    lines.append("")
    lines.append("## 해석")
    lines.append("")
    lines.append("- 도메인별 독립 Monte Carlo는 노드 수가 다른 영역 간 비교를 가능하게 한다.")
    lines.append("- z >= 5: n=6 특이성 확정 (극도 유의)")
    lines.append("- 3 <= z < 5: 통계적으로 유의")
    lines.append("- z < 3: 표본 과소 또는 도메인 내 n=6 정렬이 부족 → 보강 대상")
    lines.append("")

    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print()
    print(f"저장: {OUT_MD}")
    print()
    print(f"도메인 수: {len(results)}")
    print(f"평균 z: {avg_z:.2f}")
    print(f"최강: {strongest[0]} (z={strongest[1]['z']:.2f})")
    print(f"최약: {weakest[0]} (z={weakest[1]['z']:.2f})")

if __name__ == "__main__":
    main()
