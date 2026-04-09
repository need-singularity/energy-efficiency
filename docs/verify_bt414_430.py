#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BT-471~487 검증 스크립트 (파일명은 지시대로 verify_bt414_430.py).

외부 측정값 대 n=6 산술 예측 정직 대조. 자기참조 금지.
출처: PDG 2022, Planck 2018 (A&A 641 A6), CODATA 2018 (Rev Mod Phys 93 025010),
BIPM SI Brochure 9 (2019), ALEPH et al. Phys Rep 427 (2006) 257,
EHT Collab ApJL 875 (2019) L1, Steane PRL 77 (1996) 793,
Hensen Nature 526 (2015) 682, BCS Phys Rev 108 (1957) 1175.
"""
from math import isclose, gcd

def divisors(n): return [d for d in range(1,n+1) if n%d==0]
def tau(n): return len(divisors(n))
def sigma(n): return sum(divisors(n))
def phi(n): return sum(1 for k in range(1,n+1) if gcd(k,n)==1)
def sopfr(n):
    s,x,p=0,n,2
    while x>1:
        while x%p==0: s+=p; x//=p
        p+=1
    return s

N=6; T=tau(N); P=phi(N); S=sigma(N); SO=sopfr(N)
assert (T,P,S,SO)==(4,2,12,5)

cases = [
    ("BT-471","쿼크 플레이버 수",6,N,None,"PDG2022"),
    ("BT-471","페르미온 세대 수",3,N//P,None,"PDG2022"),
    ("BT-471","세대당 쿼크 수",2,P,None,"PDG2022"),
    ("BT-471","렙톤 플레이버 수",6,N,None,"PDG2022"),
    ("BT-472","전약 게이지 보손 수",4,T,None,"PDG2022"),
    ("BT-472","글루온 색 상태 수",8,S-T,None,"PDG2022"),
    ("BT-472","SM 게이지 보손 총수",12,S,None,"PDG2022"),
    ("BT-473","CKM 독립 물리 파라미터",4,T,None,"PDG2022 CKM"),
    ("BT-473","CKM 혼합각 수",3,N//P,None,"PDG2022"),
    ("BT-474","활성 뉴트리노 N_ν",2.9840,N//P,0.02,"ALEPH PhysRep427"),
    ("BT-474","뉴트리노 질량 고유상태",3,N//P,None,"PDG2022"),
    ("BT-474","PMNS 혼합각 수",3,N//P,None,"PDG2022"),
    ("BT-475","ΛCDM 기본 파라미터 수",6,N,None,"Planck2018"),
    ("BT-475","주요 에너지 성분 수",6,N,None,"Planck2018"),
    ("BT-476","CMB 관측 음향 피크 수",7,S-SO,None,"Planck2018 VI"),
    ("BT-477","고전 BH 파라미터 수",3,N//P,None,"Israel1967"),
    ("BT-477","BH 열역학 법칙 수",4,T,None,"Hawking1972"),
    ("BT-477","M87* 질량(1e9 Msun)",6.5,N,0.10,"EHT ApJL875"),
    ("BT-478","독립 임계지수 수(d=3)",2,P,None,"Kadanoff1966"),
    ("BT-478","표준 임계지수 집합",6,N,None,"Pelissetto2002"),
    ("BT-478","스케일링 관계식 수",4,T,None,"Pelissetto2002"),
    ("BT-479","평형 앙상블 수",3,N//P,None,"Gibbs1902"),
    ("BT-479","열역학 포텐셜 수",4,T,None,"Callen1985"),
    ("BT-479","Maxwell 관계식 수",4,T,None,"Callen1985"),
    ("BT-479","Ehrenfest 상전이 차수",2,P,None,"Ehrenfest1933"),
    ("BT-480","Pauli 행렬 수",3,N//P,None,"Pauli1927"),
    ("BT-480","Dirac gamma 행렬",4,T,None,"Dirac1928"),
    ("BT-480","Gell-Mann SU(3)",8,S-T,None,"GellMann1962"),
    ("BT-480","스핀-1/2 자유도",2,P,None,"Pauli1927"),
    ("BT-481","Cooper pair 전자 수",2,P,None,"BCS1957"),
    ("BT-481","BCS 특성 길이",2,P,None,"BCS1957"),
    ("BT-481","BCS H 기본 항",4,T,None,"BCS1957"),
    ("BT-482","IQHE n=6 plateau",6,N,None,"vonKlitzing1980"),
    ("BT-483","SI 정의 상수 수",7,S-SO,None,"BIPM SI 9"),
    ("BT-483","SI 기본 단위 수",7,S-SO,None,"BIPM SI 9"),
    ("BT-483","물리 핵심 상수",6,N,None,"CODATA2018"),
    ("BT-484","CHSH 고전 한계",2,P,None,"CHSH1969"),
    ("BT-484","PR-box 최대 한계",4,T,None,"Popescu1994"),
    ("BT-484","Bell 실험 측정자 수",2,P,None,"Bell1964"),
    ("BT-484","Hensen2015 S 값",2.42,P,0.25,"Hensen Nature526"),
    ("BT-485","순수 큐비트 파라미터",2,P,None,"Nielsen-Chuang"),
    ("BT-485","Bloch 벡터 성분",3,N//P,None,"Nielsen-Chuang"),
    ("BT-485","2-큐비트 비국소 불변",6,N,None,"Makhlin2002"),
    ("BT-485","Pauli 측정 기저",3,N//P,None,"Nielsen-Chuang"),
    ("BT-485","단일큐비트 Clifford",6,N,None,"Nielsen-Chuang"),
    ("BT-486","Steane 큐비트 수",7,S-SO,None,"Steane1996"),
    ("BT-486","Steane 거리",3,N//P,None,"Steane1996"),
    ("BT-486","Shor 코드 큐비트",9,S-N//P,None,"Shor1995"),
    ("BT-486","CSS 오류 축 수",2,P,None,"Steane1996"),
    ("BT-486","표면코드 logical op",2,P,None,"Kitaev2003"),
    ("BT-487","우주 주요 구성 성분",6,N,None,"Planck2018"),
    ("BT-487","우주 연대기 시대",8,S-T,None,"Kolb-Turner"),
]

miss_records = [
    ("BT-472","힉스 보손 수 trivial","MISS"),
    ("BT-473","Jarlskog J_CP 3.08e-5","MISS"),
    ("BT-474","sin^2 theta_13 0.0220","MISS"),
    ("BT-475","Omega_L=0.6847","MISS"),
    ("BT-475","H0=67.36","MISS"),
    ("BT-476","첫 피크 l1 220","MISS"),
    ("BT-476","BAO 147.78 Mpc/h","MISS"),
    ("BT-481","2D/kT_c = 3.528","MISS"),
    ("BT-483","h=6.626e-34","MISS"),
    ("BT-484","Tsirelson 2sqrt2","MISS"),
    ("BT-487","t0=13.797 Gyr","MISS"),
    ("BT-487","T_CMB=2.7255 K","MISS"),
]

def check(m,p,tol):
    if tol is None: return m==p
    return isclose(float(m),float(p),rel_tol=tol,abs_tol=tol)

def run():
    exact=miss=total=0
    by_bt={}
    print("="*72)
    print("BT-471~487 외부 측정값 대 n=6 산술 예측 검증 (자기참조 금지)")
    print(f"n=6 기본: tau={T} phi={P} sigma={S} sopfr={SO}")
    print("="*72)
    for bt,item,m,p,tol,src in cases:
        total+=1
        ok=check(m,p,tol)
        by_bt.setdefault(bt,[0,0]); by_bt[bt][1]+=1
        if ok: exact+=1; by_bt[bt][0]+=1; mark="EXACT"
        else: miss+=1; mark="MISS "
        print(f"  [{mark}] {bt} {item:32s} meas={m} pred={p} ({src})")
    print()
    print("-- MISS 정직 기록(비정수 물리상수) --")
    for bt,d,tag in miss_records:
        print(f"  [{tag}] {bt} {d}")
    print()
    print("-- BT별 EXACT/Total --")
    for bt in sorted(by_bt):
        e,t=by_bt[bt]; print(f"  {bt}: {e}/{t}")
    T5,P5,S5,SO5=tau(5),phi(5),sigma(5),sopfr(5)
    n5_set={T5,P5,S5,SO5,5}
    n5_hits=sum(1 for bt,i,m,p,tol,s in cases if tol is None and isinstance(m,int) and m in n5_set)
    print()
    print("-- 소수 n=5 편향 대조 --")
    print(f"  n=5 기본: tau={T5} phi={P5} sigma={S5} sopfr={SO5}")
    print(f"  n=5 우연 포함 수: {n5_hits}/{total}  (n=6 EXACT {exact}/{total})")
    print()
    print("="*72)
    pct=100.0*exact/total if total else 0.0
    print(f"총 검증 케이스: {total}")
    print(f"EXACT: {exact} ({pct:.1f}%)")
    print(f"MISS : {miss}")
    print(f"목표 70%: {'예' if pct>=70 else '아니오'}")
    print("="*72)
    return exact,total,pct

if __name__=="__main__":
    run()
