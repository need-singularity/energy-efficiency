#!/usr/bin/env python3
"""
Cross-Domain σ² Dual Recursion Propagation Test
================================================
HEXA-SPEAK에서 발견된 패턴:
  heads·ffn·layers = heads² = σ² = 144

이 이중 재귀가 다른 20개 도메인에도 존재하는가?

방법: 각 도메인 verify_alien10.py에서 상수 추출 → σ² 생성 경로 전수 검색.
"""

import re
import os
from pathlib import Path
from itertools import combinations

SIGMA_SQ = 144  # σ² = 12²
N6_TARGETS = {
    144: "σ² (sigma squared)",
    288: "σ·J₂ (double sigma)",
    72: "σ·n",
    576: "σ²·τ",
}

DOCS = Path(os.path.expanduser("~/Dev/n6-architecture/docs"))

def extract_constants(path):
    """verify_alien10.py에서 정수 상수 추출."""
    try:
        text = path.read_text()
    except:
        return []
    # check( ..., expected_value, actual_value, ... ) 패턴
    values = set()
    for m in re.finditer(r'\b(\d{1,5})\b', text):
        v = int(m.group(1))
        if 1 <= v <= 576:
            values.add(v)
    return sorted(values)

def find_sigma2_paths(values, target=144):
    """values에서 a·b=144, a·b·c=144, a² 경로 찾기."""
    paths = []
    vs = [v for v in values if v > 1 and v <= target]
    # Pairs a·b
    for a, b in combinations(vs, 2):
        if a * b == target:
            paths.append(("PAIR", a, b, f"{a}·{b}", f"{a}·{b}"))
    # Squares a²
    for a in vs:
        if a * a == target:
            paths.append(("SQUARE", a, a, f"{a}²", f"{a}²"))
    # Triples a·b·c (take small values to limit)
    small = [v for v in vs if v <= 24]
    for a, b, c in combinations(small, 3):
        if a * b * c == target:
            paths.append(("TRIPLE", a, b, c, f"{a}·{b}·{c}"))
    return paths

print("="*80)
print("Cross-Domain σ² (144) Dual Recursion Test")
print("="*80)
print(f"Target: {SIGMA_SQ} = σ² = 12²")
print()

domains = sorted(DOCS.glob("*/verify_alien10.py"))
results = {}

for script in domains:
    domain = script.parent.name
    consts = extract_constants(script)
    paths = find_sigma2_paths(consts)
    results[domain] = paths
    pair_n = sum(1 for p in paths if p[0] == "PAIR")
    sq_n = sum(1 for p in paths if p[0] == "SQUARE")
    tri_n = sum(1 for p in paths if p[0] == "TRIPLE")
    total = len(paths)
    marker = "⚡" if sq_n > 0 and tri_n > 0 else ("★" if total >= 3 else ("·" if total > 0 else " "))
    print(f"  {marker} {domain:28s} PAIR={pair_n:2d} SQ={sq_n} TRI={tri_n:2d} total={total}")

print()
print("="*80)
print("DUAL RECURSION (SQUARE + TRIPLE both present) 도메인")
print("="*80)
dual = [(d, p) for d, p in results.items()
        if any(x[0]=="SQUARE" for x in p) and any(x[0]=="TRIPLE" for x in p)]

for domain, paths in dual:
    print(f"\n[{domain}]")
    for p in paths[:6]:
        if p[0] == "SQUARE":
            print(f"  SQUARE:  {p[4]} = 144")
        elif p[0] == "TRIPLE":
            print(f"  TRIPLE:  {p[4]} = 144")

print()
print("="*80)
print(f"σ² 이중 재귀 전파율: {len(dual)}/{len(domains)} = {100*len(dual)//len(domains)}%")
print("="*80)

# 전파 결론
if len(dual) >= len(domains) // 2:
    print("\n✅ 전파 확정 — σ² 이중 재귀는 n=6 격자의 BOUNDARY INVARIANT")
    print("   설계 전반에 걸친 구조적 필연 (cross-domain universal)")
elif len(dual) >= 3:
    print(f"\n⚡ 부분 전파 ({len(dual)}개 도메인) — 자주 등장하나 보편 아님")
else:
    print(f"\n· 국소 현상 ({len(dual)}개 도메인) — HEXA-SPEAK 특유 가능성")

# Summary stats across all domains
print("\n[도메인별 총 σ² 경로 수]")
sorted_r = sorted(results.items(), key=lambda x: -len(x[1]))
for domain, paths in sorted_r[:10]:
    print(f"  {domain:28s}: {len(paths):3d} 경로")
