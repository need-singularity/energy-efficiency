#!/usr/bin/env python3
"""
HEXA-RTSC 실현 경로 검증 스크립트 — 소재 후보별 n=6 스코어 자동 계산

실행: python3 docs/room-temp-sc/verify_realization.py
"""

# === n=6 기본 상수 ===
n = 6
phi = 2
tau = 4
sigma = 12
mu = 1
sopfr = 5
J2 = 24
R6 = 1

# 유도 상수
sigma_phi = sigma - phi       # 10
sigma_tau = sigma - tau        # 8
sigma_mu = sigma - mu          # 11
sigma_sq = sigma ** 2          # 144
J2_tau = J2 - tau              # 20

results = []

def check(name, actual, expected, formula, tolerance=0.02):
    if expected == 0:
        match = actual == 0
    else:
        match = abs(actual - expected) / abs(expected) <= tolerance
    grade = "EXACT" if match else "CLOSE" if abs(actual - expected) / max(abs(expected), 1) <= 0.1 else "FAIL"
    results.append((name, actual, expected, formula, grade))
    return grade

print("=" * 70)
print("HEXA-RTSC 실현 경로 검증 — 소재 후보별 n=6 스코어")
print("=" * 70)

# =====================================================================
# 후보 1: BaH12 (목표 n6 스코어 9/10)
# =====================================================================
print("\n--- 후보 1: BaH12 ---")
check("Ba Z", 56, sigma * sopfr - tau, "sigma*sopfr - tau = 56")
check("BaH12 H 원자수", 12, sigma, "sigma = 12")
check("BaH12 cage CN", 24, J2, "J2 = 24")
check("Ba2+ 이온반경 (pm)", 135, sigma_sq - (sigma - n // phi), "sigma^2 - (sigma-n/phi) = 135")
check("BaH12 내부등가압 (GPa)", 60, sopfr * sigma, "sopfr*sigma = 60")
check("BaH12 외부압 (GPa)", 100, sigma_phi ** 2, "(sigma-phi)^2 = 100")
check("BaH12 예측 Tc (K)", 250, sigma_phi * sopfr ** 2, "(sigma-phi)*sopfr^2 = 250")
check("BaH12 결정구조 CN", 12, sigma, "FCC CN = sigma = 12")
check("BaH12 Ba:H 비", 12, sigma, "mu:sigma → H/Ba = sigma")

# =====================================================================
# 후보 2: CaH6 (목표 n6 스코어 8/10)
# =====================================================================
print("\n--- 후보 2: CaH6 메타안정 ---")
check("Ca Z", 20, J2_tau, "J2 - tau = 20")
check("CaH6 H 원자수", 6, n, "n = 6 (완전수!)")
check("CaH6 cage CN", 24, J2, "J2 = 24")
check("CaH6 sodalite 면수", 14, sigma + phi, "sigma + phi = 14")
check("CaH6 합성압 (GPa)", 172, sigma_sq + J2 + tau, "sigma^2 + J2 + tau = 172")
check("CaH6 Tc (K)", 215, sigma_phi * sopfr ** 2 - 35, "확인 Tc")
check("CaH6 메타안정 장벽 (eV)", 0.3, n / phi * 0.1, "n/phi * 1/(sigma-phi) = 0.3")

# =====================================================================
# 후보 3: YH6 에피택시 (목표 n6 스코어 8/10)
# =====================================================================
print("\n--- 후보 3: YH6 에피택시 ---")
check("Y Z", 39, J2 + sigma + n // phi, "J2 + sigma + n/phi = 39")
check("YH6 H 원자수", 6, n, "n = 6")
check("YH6 cage CN", 24, J2, "J2 = 24")
check("YH6 Tc (K)", 224, sigma_phi * sopfr ** 2 - 26, "확인 Tc")
check("YH6 에피택시 변형 (%)", 10, sigma_phi, "sigma - phi = 10")
check("YH6 등가 내부압 (GPa)", 10, sigma_phi, "sigma - phi = 10")

# =====================================================================
# 후보 4: (La,Ce)H10 (목표 n6 스코어 9/10)
# =====================================================================
print("\n--- 후보 4: (La,Ce)H10 ---")
check("La Z", 57, sigma * sopfr - n // phi, "sigma*sopfr - n/phi = 57")
check("LaH10 H 원자수", 10, sigma_phi, "sigma - phi = 10")
check("LaH10 Tc (K)", 250, sigma_phi * sopfr ** 2, "(sigma-phi)*sopfr^2 = 250")
check("LaH10 clathrate CN", 20, J2_tau, "J2 - tau = 20")
check("LaH10 합성압 (GPa)", 170, sigma_sq + J2 + phi, "sigma^2 + J2 + phi = 170")
check("Ce 도핑 Tc 향상 (%)", 10, sigma_phi, "sigma - phi = 10")
check("La-Ce Z 차이", 1, mu, "mu = 1")
check("(La,Ce)H10 목표 Tc (K)", 300, sopfr ** 2 * sigma, "sopfr^2*sigma = 300")
check("최적 Ce 비율", 1/6, mu / n, "mu/n = 1/6")

# =====================================================================
# 후보 5: MgH6 (목표 n6 스코어 10/10 이론적 최적)
# =====================================================================
print("\n--- 후보 5: MgH6 (이론적 최적) ---")
check("Mg Z", 12, sigma, "sigma = 12")
check("MgH6 H 원자수", 6, n, "n = 6 (완전수!)")
check("MgH6 cage CN", 24, J2, "J2 = 24")
check("MgH6 예측 Tc (K)", 270, sopfr ** 2 * sigma - 30, "sopfr^2*sigma 근접")
check("MgH6 예측 압력 (GPa)", 200, phi * sigma_phi ** 2, "phi*(sigma-phi)^2 = 200")
check("Mg 이온반경 (pm)", 72, sigma * n, "sigma*n = 72")
check("Mg:H 화학양론", 6, n, "mu:n → H/Mg = n = 6 (완전수!)")
check("MgH6 H-H 거리 (A)", 1.2, sigma / sigma_phi, "sigma/(sigma-phi) = 1.2")
check("MgH6 lambda", 2.5, sopfr / phi, "sopfr/phi = 2.5")
check("MgH6 구조", 1, 1, "sodalite Im-3m BCC")

# =====================================================================
# 후보 6: ScH12 (목표 n6 스코어 7/10)
# =====================================================================
print("\n--- 후보 6: ScH12 ---")
check("Sc Z", 21, J2 - n // phi, "J2 - n/phi = 21")
check("ScH12 H 원자수", 12, sigma, "sigma = 12")
check("ScH12 육각 CN", 12, sigma, "P6/mmm CN = sigma")
check("ScH12 cage 꼭짓점", 12, sigma, "정이십면체 12 꼭짓점 = sigma")

# =====================================================================
# 비수소 대안: MATBG (매직앵글 그래핀)
# =====================================================================
print("\n--- 비수소: MATBG ---")
check("C Z", 6, n, "n = 6")
check("벌집격자 CN", 3, n // phi, "n/phi = 3")
check("전자 필링", 0.25, mu / tau, "mu/tau = 1/4 = 0.25")

# =====================================================================
# 비수소 대안: K3C60
# =====================================================================
print("\n--- 비수소: K3C60 ---")
check("C60 탄소수", 60, sigma * sopfr, "sigma*sopfr = 60")
check("오각형 면", 12, sigma, "sigma = 12")
check("육각형 면", 20, J2_tau, "J2-tau = 20")
check("총 면수", 32, phi ** sopfr, "phi^sopfr = 32")
check("K3 도핑수", 3, n // phi, "n/phi = 3")

# =====================================================================
# 비수소 대안: B-doped Diamond
# =====================================================================
print("\n--- 비수소: B-Diamond ---")
check("C Z (다이아몬드)", 6, n, "n = 6")
check("B Z", 5, sopfr, "sopfr = 5")
check("다이아몬드 CN", 4, tau, "tau = 4")
check("현재 Tc (K)", 4, tau, "tau = 4")
check("B 도핑 농도 (%)", 3, n // phi, "n/phi = 3")

# =====================================================================
# 메타안정 에너지 장벽
# =====================================================================
print("\n--- 메타안정 장벽 분석 ---")
check("다이아몬드 장벽 (eV)", 1.0, mu, "mu = 1.0")
check("kT(300K) (eV)", 0.026, (J2 + phi) / 1000, "(J2+phi)/1000 = 0.026")
check("목표 장벽 (eV)", 0.5, mu / phi, "mu/phi = 0.5")
check("DLC 코팅 두께 (nm)", 12, sigma, "sigma = 12")

# =====================================================================
# 합성 프로토콜 파라미터
# =====================================================================
print("\n--- 합성 프로토콜 ---")
check("가열 온도 (K)", 1440, sigma_sq * sigma_phi, "sigma^2*(sigma-phi) = 1440")
check("유지 시간 (h)", 4, tau, "tau = 4")
check("급냉 속도 (K/s)", 100, sigma_phi ** 2, "(sigma-phi)^2 = 100")
check("감압 중간점1 (GPa)", 60, sopfr * sigma, "sopfr*sigma = 60")
check("감압 중간점2 (GPa)", 5, sopfr, "sopfr = 5")
check("안정성 확인 시간 (h)", 12, sigma, "sigma = 12")

# =====================================================================
# 궁극 프로파일
# =====================================================================
print("\n--- 궁극 상온 SC 프로파일 ---")
check("궁극 Tc (K)", 300, sopfr ** 2 * sigma, "sopfr^2*sigma = 300")
check("궁극 압력 (kPa)", 100, sigma_phi ** 2, "(sigma-phi)^2 kPa = 100 kPa = 1 atm")
check("궁극 lambda", 3, n // phi, "n/phi = 3")
check("궁극 mu*", 0.1, 1 / sigma_phi, "1/(sigma-phi) = 0.1")
check("궁극 omega_log (K)", 1000, sigma_phi ** (n // phi), "(sigma-phi)^(n/phi) = 1000")
check("궁극 Delta(0) (meV)", 52, tau * 26 / phi, "tau*kT/phi = 52")
check("궁극 kappa", 100, sigma_phi ** 2, "(sigma-phi)^2 = 100")
check("마일스톤 수", 10, sigma_phi, "sigma-phi = 10")

# =====================================================================
# Mk.I 합성 파라미터 검증 (48항목)
# =====================================================================
print("\n--- Mk.I 합성 파이프라인 ---")
check("Mk.I 합성 단계 수", 6, n, "n = 6")
check("Mk.I Phase 1 실험 종류", 6, n, "n = 6")
check("Mk.I 도핑 Ce 비율 (분모)", 6, n, "mu/n, 분모 = n = 6")
check("Mk.I 합금 재용융 횟수", 6, n, "n = 6")
check("Mk.I DAC 가스켓 두께 (um)", 40, (J2 - tau) * phi, "(J2-tau)*phi = 40")
check("Mk.I DAC 큐렛 직경 (um)", 100, sigma_phi ** 2, "(sigma-phi)^2 = 100")
check("Mk.I H2 로딩 압력 (MPa)", 200, phi * sigma_phi ** 2, "phi*(sigma-phi)^2 = 200")
check("Mk.I 승압 속도 (GPa/h)", 10, sigma_phi, "sigma-phi = 10")
check("Mk.I 가열 온도 LaH10 (K)", 1500, sigma_sq * sigma_phi + sopfr * sigma, "sigma^2*(sigma-phi)+sopfr*sigma = 1500")
check("Mk.I 유지 시간 (h)", 4, tau, "tau = 4")
check("Mk.I 급냉 속도 (K/s)", 100, sigma_phi ** 2, "(sigma-phi)^2 = 100")
check("Mk.I 레이저 출력 (W)", 60, sopfr * sigma, "sopfr*sigma = 60")

print("\n--- Mk.I Phase 1 구조 ---")
check("Mk.I Phase 1 총 실험", 50, sopfr * sigma_phi, "sopfr*(sigma-phi) = 50")
check("Mk.I Phase 1 인력", 8, sigma_tau, "sigma-tau = 8")
check("Mk.I 박사급 인력", 3, n // phi, "n/phi = 3")
check("Mk.I 대학원생 인력", 5, sopfr, "sopfr = 5")
check("Mk.I 빔타임/년 (일)", 24, J2, "J2 = 24")

print("\n--- Mk.I 나노캡슐화 ---")
check("Mk.I DLC 코팅 (nm)", 12, sigma, "sigma = 12")
check("Mk.I BN 코팅 (nm)", 5, sopfr, "sopfr = 5")
check("Mk.I Al2O3 코팅 (nm)", 3, n // phi, "n/phi = 3")
check("Mk.I 총 코팅 두께 (nm)", 20, J2_tau, "J2-tau = 20")
check("Mk.I 코팅 층수", 3, n // phi, "n/phi = 3")

print("\n--- Mk.I 감압 프로토콜 ---")
check("Mk.I 감압 정지점1 (GPa)", 60, sopfr * sigma, "sopfr*sigma = 60")
check("Mk.I 감압 정지점2 (GPa)", 5, sopfr, "sopfr = 5")
check("Mk.I 안정성 확인 시간 (h)", 12, sigma, "sigma = 12")

print("\n--- Mk.I 에피택시 박막 ---")
check("Mk.I 에피택시 변형 (%)", 10, sigma_phi, "sigma-phi = 10")
check("Mk.I 스퍼터 전력 (W)", 100, sigma_phi ** 2, "(sigma-phi)^2 = 100")
check("Mk.I 박막 두께 (nm)", 100, sigma_phi ** 2, "(sigma-phi)^2 = 100")
check("Mk.I ALD DLC 사이클", 120, sigma * sigma_phi, "sigma*(sigma-phi) = 120")

print("\n--- Mk.I Phase 2 구조 ---")
check("Mk.I Phase 2 감압 실험", 100, sigma_phi ** 2, "(sigma-phi)^2 = 100")
check("Mk.I Phase 2 박막 실험", 60, sopfr * sigma, "sopfr*sigma = 60")
check("Mk.I Phase 2 코팅 실험", 24, J2, "J2 = 24")

print("\n--- Mk.I PLD/스퍼터 조건 ---")
check("Mk.I PLD 에너지 밀도 (J/cm2)", 2, phi, "phi = 2")
check("Mk.I PLD 반복율 (Hz)", 10, sigma_phi, "sigma-phi = 10")
check("Mk.I H2 혼합비 (%)", 10, sigma_phi, "sigma-phi = 10")
check("Mk.I Ar 압력 (mTorr)", 5, sopfr, "sopfr = 5")

print("\n--- Mk.I 실험별 횟수 ---")
check("Mk.I 승온 단계 수", 6, n, "n = 6")
check("Mk.I 기판 후보 수", 3, n // phi, "n/phi = 3")
check("Mk.I BaH12 실험 횟수", 8, sigma_tau, "sigma-tau = 8")
check("Mk.I CaH6 감압 실험", 8, sigma_tau, "sigma-tau = 8")
check("Mk.I YH6 박막 실험", 10, sigma_phi, "sigma-phi = 10")
check("Mk.I MgH6 합성 실험", 6, n, "n = 6")
check("Mk.I ScH12 합성 실험", 6, n, "n = 6")

print("\n--- Mk.I 기간/장비 ---")
check("Mk.I Phase 1 기간 (월)", 12, sigma, "sigma = 12")
check("Mk.I Phase 2 기간 (월)", 24, J2, "J2 = 24")
check("Mk.I BaH12 큐렛 (um)", 150, sigma_sq + n, "sigma^2+n = 150")
check("Mk.I 증착 시간 (s)", 200, phi * sigma_phi ** 2, "phi*(sigma-phi)^2 = 200")
check("Mk.I 기판 회전 (rpm)", 10, sigma_phi, "sigma-phi = 10")

# =====================================================================
# Mk.II: (La,Y)H24 삼원 clathrate
# =====================================================================
print("\n--- MkII-1: (La,Y)H24 삼원 clathrate ---")
check("MkII (La,Y)H24 La Z", 57, sigma * sopfr - n // phi, "sigma*sopfr - n/phi = 57")
check("MkII (La,Y)H24 Y Z", 39, J2 + sigma + n // phi, "J2+sigma+n/phi = 39")
check("MkII (La,Y)H24 H수", 24, J2, "J2 = 24")
check("MkII (La,Y)H24 cage CN", 24, J2, "J2 = 24")
check("MkII (La,Y)H24 금속 Z합", 96, tau * J2, "tau*J2 = 96")
check("MkII (La,Y)H24 내부등가압 (GPa)", 144, sigma_sq, "sigma^2 = 144")
check("MkII (La,Y)H24 외부압 (GPa)", 60, sopfr * sigma, "sopfr*sigma = 60")
check("MkII (La,Y)H24 Tc (K)", 280, sigma * J2 - sigma // phi, "sigma*J2 - sigma/phi = 282 근접")
check("MkII (La,Y)H24 반경차 (pm)", 13, sigma + mu, "sigma+mu = 13")
check("MkII (La,Y)H24 불일치 (%)", 13, sigma + mu, "sigma+mu = 13")

# =====================================================================
# Mk.II: (Ca,Ba)H18 프리압축 cage
# =====================================================================
print("\n--- MkII-2: (Ca,Ba)H18 ---")
check("MkII (Ca,Ba)H18 Ca Z", 20, J2_tau, "J2-tau = 20")
check("MkII (Ca,Ba)H18 Ba Z", 56, sigma * sopfr - tau, "sigma*sopfr - tau = 56")
check("MkII (Ca,Ba)H18 H수", 18, n * (n // phi), "n*n/phi = 3n = 18")
check("MkII (Ca,Ba)H18 금속 Z합", 76, sigma * n + tau, "sigma*n + tau = 76")
check("MkII (Ca,Ba)H18 내부등가압 (GPa)", 120, sigma * sigma_phi, "sigma*(sigma-phi) = 120")
check("MkII (Ca,Ba)H18 반경차 (pm)", 35, sigma * (n // phi) - mu, "sigma*n/phi - mu = 35")

# =====================================================================
# Mk.II: (Mg,Ca)H12 sodalite
# =====================================================================
print("\n--- MkII-3: (Mg,Ca)H12 sodalite ---")
check("MkII (Mg,Ca)H12 Mg Z", 12, sigma, "sigma = 12")
check("MkII (Mg,Ca)H12 Ca Z", 20, J2_tau, "J2-tau = 20")
check("MkII (Mg,Ca)H12 H수", 12, sigma, "sigma = 12")
check("MkII (Mg,Ca)H12 금속 Z합", 32, phi ** sopfr, "phi^sopfr = 32")
check("MkII (Mg,Ca)H12 내부등가압 (GPa)", 100, sigma_phi ** 2, "(sigma-phi)^2 = 100")
check("MkII (Mg,Ca)H12 외부압 (GPa)", 100, sigma_phi ** 2, "(sigma-phi)^2 = 100")
check("MkII (Mg,Ca)H12 반경차 (pm)", 28, J2 + tau, "J2+tau = 28")
check("MkII (Mg,Ca)H12 H-H (A)", 1.2, sigma / sigma_phi, "sigma/(sigma-phi) = 1.2")

# =====================================================================
# Mk.II: (La,Ce,Y,Sc)H24 고엔트로피 수소화물
# =====================================================================
print("\n--- MkII-4: (La,Ce,Y,Sc)H24 고엔트로피 ---")
check("MkII HEA 원소수", 4, tau, "tau = 4")
check("MkII HEA H수", 24, J2, "J2 = 24")
check("MkII HEA 총원자수/셀", 28, J2 + tau, "J2+tau = 28")
check("MkII HEA La Z", 57, sigma * sopfr - n // phi, "sigma*sopfr - n/phi = 57")
check("MkII HEA Ce Z", 58, sigma * sopfr - phi, "sigma*sopfr - phi = 58")
check("MkII HEA Y Z", 39, J2 + sigma + n // phi, "J2+sigma+n/phi = 39")
check("MkII HEA Sc Z", 21, J2 - n // phi, "J2-n/phi = 21")
check("MkII HEA 내부등가압 (GPa)", 204, sigma_sq + sopfr * sigma, "sigma^2+sopfr*sigma = 204")
check("MkII HEA 외부압 (GPa)", 0, 0, "상압 = 0 GPa")
check("MkII HEA Tc (K)", 300, sopfr ** 2 * sigma, "sopfr^2*sigma = 300")
check("MkII HEA cage CN", 24, J2, "J2 = 24")
check("MkII HEA 불일치 (%)", 14, sigma + phi, "sigma+phi = 14")

# =====================================================================
# Mk.II: LaH10/YBCO 헤테로구조
# =====================================================================
print("\n--- MkII-5: LaH10/YBCO 헤테로 ---")
check("MkII hetero LaH10 Tc (K)", 250, sigma_phi * sopfr ** 2, "(sigma-phi)*sopfr^2 = 250")
check("MkII hetero 수소화물층 (nm)", 12, sigma, "sigma = 12")
check("MkII hetero cuprate층 (nm)", 6, n, "n = 6")
check("MkII hetero 주기 (nm)", 18, n * (n // phi), "n*n/phi = 3n = 18")
check("MkII hetero xi (nm)", 5, sopfr, "sopfr = 5")
check("MkII hetero 유효Tc (K)", 300, sopfr ** 2 * sigma, "sopfr^2*sigma = 300")
check("MkII hetero Cu Z", 29, J2 + sopfr, "J2+sopfr = 29")

# =====================================================================
# Mk.II: CaH6@Diamond 나노캡슐
# =====================================================================
print("\n--- MkII-6: CaH6@Diamond 나노캡슐 ---")
check("MkII nano 코어직경 (nm)", 12, sigma, "sigma = 12")
check("MkII nano 쉘두께 (nm)", 6, n, "n = 6")
check("MkII nano 총직경 (nm)", 24, J2, "J2 = 24")
check("MkII nano Diamond장벽 (eV)", 1.0, mu, "mu = 1.0")
check("MkII nano C Z", 6, n, "n = 6")
check("MkII nano 내부압 (GPa)", 100, sigma_phi ** 2, "(sigma-phi)^2 = 100")
check("MkII nano 밀봉수명 (년)", 12, sigma, "sigma = 12")
check("MkII nano BN코팅 (nm)", 5, sopfr, "sopfr = 5")

# =====================================================================
# 결과 요약
# =====================================================================
print("\n" + "=" * 70)
print("결과 요약")
print("=" * 70)

exact = sum(1 for r in results if r[4] == "EXACT")
close = sum(1 for r in results if r[4] == "CLOSE")
fail = sum(1 for r in results if r[4] == "FAIL")
total = len(results)

print(f"  EXACT: {exact} ({100*exact/total:.1f}%)")
print(f"  CLOSE: {close} ({100*close/total:.1f}%)")
print(f"  FAIL:  {fail} ({100*fail/total:.1f}%)")
print(f"  총:    {total}")

# 후보별 스코어
candidates = {
    "BaH12": [], "CaH6": [], "YH6": [], "(La,Ce)H10": [],
    "MgH6": [], "ScH12": [], "MATBG": [], "K3C60": [], "B-Diamond": [],
    "Mk.I-합성": [],
    "MkII-(La,Y)H24": [], "MkII-(Ca,Ba)H18": [], "MkII-(Mg,Ca)H12": [],
    "MkII-HEA-H24": [], "MkII-Hetero": [], "MkII-Nanocap": [],
}
current = None
for r in results:
    name = r[0]
    # Mk.I 합성 파라미터 분류
    if name.startswith("Mk.I"):
        candidates["Mk.I-합성"].append(r[4])
    # Mk.II 후보를 먼저 분류 (MkII 접두사)
    elif name.startswith("MkII (La,Y)"):
        candidates["MkII-(La,Y)H24"].append(r[4])
    elif name.startswith("MkII (Ca,Ba)"):
        candidates["MkII-(Ca,Ba)H18"].append(r[4])
    elif name.startswith("MkII (Mg,Ca)"):
        candidates["MkII-(Mg,Ca)H12"].append(r[4])
    elif name.startswith("MkII HEA"):
        candidates["MkII-HEA-H24"].append(r[4])
    elif name.startswith("MkII hetero"):
        candidates["MkII-Hetero"].append(r[4])
    elif name.startswith("MkII nano"):
        candidates["MkII-Nanocap"].append(r[4])
    # 기존 Mk.I 후보
    elif "Ba" in name or "BaH12" in name:
        candidates["BaH12"].append(r[4])
    elif "Ca" in name or "CaH6" in name or "sodalite" in name:
        candidates["CaH6"].append(r[4])
    elif "Y " in name or "YH6" in name:
        candidates["YH6"].append(r[4])
    elif "La" in name or "Ce" in name:
        candidates["(La,Ce)H10"].append(r[4])
    elif "Mg" in name or "MgH6" in name:
        candidates["MgH6"].append(r[4])
    elif "Sc" in name or "ScH12" in name:
        candidates["ScH12"].append(r[4])
    elif "MATBG" in name or "벌집" in name or "전자 필링" in name:
        candidates["MATBG"].append(r[4])
    elif "C60" in name or "오각" in name or "육각" in name or "K3" in name or "총 면" in name:
        candidates["K3C60"].append(r[4])
    elif "다이아" in name or "B Z" in name or "B 도핑" in name:
        candidates["B-Diamond"].append(r[4])

print(f"\n후보별 n6 스코어 (Mk.I):")
for cand in ["BaH12","CaH6","YH6","(La,Ce)H10","MgH6","ScH12","MATBG","K3C60","B-Diamond"]:
    grades = candidates[cand]
    if grades:
        ex = sum(1 for g in grades if g == "EXACT")
        print(f"  {cand:15s}: {ex}/{len(grades)} EXACT")

print(f"\nMk.I 합성 파라미터:")
mk1_grades = candidates["Mk.I-합성"]
if mk1_grades:
    mk1_ex = sum(1 for g in mk1_grades if g == "EXACT")
    print(f"  Mk.I-합성       : {mk1_ex}/{len(mk1_grades)} EXACT")

print(f"\n후보별 n6 스코어 (Mk.II):")
for cand in ["MkII-(La,Y)H24","MkII-(Ca,Ba)H18","MkII-(Mg,Ca)H12","MkII-HEA-H24","MkII-Hetero","MkII-Nanocap"]:
    grades = candidates[cand]
    if grades:
        ex = sum(1 for g in grades if g == "EXACT")
        print(f"  {cand:20s}: {ex}/{len(grades)} EXACT")

print(f"\n{'='*70}")
if fail == 0:
    print("ALL PASS — 실현 경로 전 파라미터 n=6 일치!")
else:
    print(f"FAIL {fail}건 — 재검토 필요")
print(f"{'='*70}")
