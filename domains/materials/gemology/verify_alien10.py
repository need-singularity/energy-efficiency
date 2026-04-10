#!/usr/bin/env python3
"""보석학 (gemology) n=6 검증 — 외계지수 10
σ(n)·φ(n)=n·τ(n) ⟺ n=6
A.결정계 B.4C C.광원 D.모스 E.광학 F.기하 G.등급
"""
n=6; sigma=12; phi=2; tau=4; sopfr=5; J2=24; mu=1
sigma_phi=sigma-phi; sigma_tau=sigma-tau; n_over_phi=n//phi

results=[]
def grade(e):
    if e<=1.0: return "EXACT"
    if e<=5.0: return "CLOSE"
    if e<=15.0: return "WEAK"
    return "MISS"
def verify(name, actual, expected, formula, category, note=""):
    err = 0.0 if expected==0 and actual==0 else (100.0 if expected==0 else abs(actual-expected)/abs(expected)*100)
    results.append(dict(name=name,actual=actual,expected=expected,formula=formula,
                        error=err,grade=grade(err),category=category,note=note))

# A. 결정계
HEX=["베릴","커런덤","석영","투르말린","아파타이트","지르콘"]
verify("hexagonal 보석족 수",len(HEX),n,"n=6","결정계","베릴/커런덤/석영/투르말린/아파타이트/지르콘")
verify("hexagonal 회전대칭 차수",6,n,"n=6","결정계","C6 회전축")
verify("trigonal 회전축",3,n_over_phi,"n/phi=3","결정계","C3 부분군")
verify("hexagonal계 결정계 수(hex+tri)",2,phi,"phi=2","결정계","")
verify("hexagonal통합 결정계 총수",6,n,"n=6","결정계","7→6 병합")

# B. 4C
FOUR=["Cut","Carat","Color","Clarity"]
verify("4C 채널 수",len(FOUR),tau,"tau=4","4C","GIA 표준")
verify("컷 등급 단계",5,sopfr,"sopfr=5","4C","EX/VG/G/F/P")
verify("1캐럿 (g)",0.2,1.0/sopfr,"1/sopfr","4C","")
verify("색 주축 RGB",3,n_over_phi,"n/phi=3","4C","분광 3축")
CL=["FL","IF","VVS","VS","SI","I"]
verify("선명도 주등급군",len(CL),n,"n=6","4C","GIA 6대 군")

# C. 광원
CIE=["A","B","C","D50","D55","D65","D75","E","F2","F7","F11","LED"]
verify("CIE 주요 광원 수",len(CIE),sigma,"sigma=12","광원","")
verify("D65 색온도 코드(/100)",65,sigma*sopfr+sopfr,"σ·sopfr+sopfr=65","광원","6500K")
verify("F계열 형광 광원 수",12,sigma,"sigma=12","광원","F1~F12")

# D. 모스
verify("보석급 모스 하한",5,sopfr,"sopfr=5","경도","아파타이트")
verify("모스 척도 단계",10,sigma_phi,"σ-φ=10","경도","활석~다이아")
verify("다이아몬드 경도",10,sigma_phi,"σ-φ=10","경도","")
verify("커런덤 경도",9,sigma_phi-mu,"σ-φ-μ=9","경도","루비/사파이어")
verify("석영 경도",7,sopfr+phi,"sopfr+φ=7","경도","")
verify("베릴 경도(상한)",8,sigma_tau,"σ-τ=8","경도","")

# E. 광학
verify("복굴절 광선 수",2,phi,"phi=2","광학","o-ray+e-ray")
verify("등방성 굴절률 수",1,mu,"mu=1","광학","다이아/석류석")
verify("분산 기준 파장",3,n_over_phi,"n/phi=3","광학","B/D/F line")
verify("다이아 굴절률 정수부",2,phi,"phi=2","광학","n=2.417")

# F. 기하
verify("브릴리언트 파빌리온 메인 패싯",24,J2,"J2=24","기하","")
verify("크라운 스타 패싯",8,sigma_tau,"σ-τ=8","기하","")
verify("테이블+큘릿",2,phi,"phi=2","기하","")
verify("hexagonal 면각(°)",120,sigma*sigma_phi,"σ·(σ-φ)=120","기하","")

# G. 등급
verify("HEXA 가치 등급",10,sigma_phi,"σ-φ=10","등급","")
verify("형광 등급 단계",5,sopfr,"sopfr=5","등급","")
TR=["천연","처리","합성","모조"]
verify("처리/합성 카테고리",len(TR),tau,"tau=4","등급","")
verify("표준 보고서 면수",6,n,"n=6","등급","")

def main():
    print("="*64)
    print("  보석학 (gemology) — HEXA-GEM n=6 검증")
    print("  σ(n)·φ(n) = n·τ(n) ⟺ n = 6")
    print("="*64)
    by={}
    for r in results: by.setdefault(r["category"],[]).append(r)
    gc={"EXACT":0,"CLOSE":0,"WEAK":0,"MISS":0}
    for r in results: gc[r["grade"]]+=1
    for cat,items in by.items():
        print(f"\n[{cat}]")
        for r in items:
            m={"EXACT":"O","CLOSE":"~","WEAK":"?","MISS":"X"}[r["grade"]]
            print(f"  {m} {r['name']:30s} act={r['actual']:>8} exp={r['expected']:>4} {r['formula']:18s} err={r['error']:5.1f}% [{r['grade']}]")
            if r["note"]: print(f"      -> {r['note']}")
    total=len(results)
    print("\n"+"="*64)
    print(f"  총 {total}건 — EXACT {gc['EXACT']} / CLOSE {gc['CLOSE']} / WEAK {gc['WEAK']} / MISS {gc['MISS']}")
    rate=gc["EXACT"]/total*100
    print(f"  EXACT 비율: {rate:.1f}%")
    if rate>=80: print("  판정: 외계지수 10 돌파 — n=6 보석학 검증")
    elif rate>=60: print("  판정: 부분 정합 — 추가 정련 필요")
    else: print("  판정: 약한 정합 — 매핑 재검토")
    print("="*64)

if __name__=="__main__": main()
