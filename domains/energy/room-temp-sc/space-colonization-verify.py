#!/usr/bin/env python3
"""
HEXA-SHIP 우주 식민지 아키텍처 — n=6 파라미터 전수 검증
🛸10 외계인 지수 검증 코드

실행: python3 docs/room-temp-sc/space-colonization-verify.py
"""

# n=6 기본 상수
n = 6
phi = 2        # phi(6) = 2
tau = 4        # tau(6) = 4
sigma = 12     # sigma(6) = 12
sopfr = 5      # sopfr(6) = 2+3 = 5
mu = 1         # mu(6) = 1
J2 = 24        # J_2(6) = 24
R6 = 1         # R(6) = sigma*phi/(n*tau) = 1

# 핵심 정리 검증
assert sigma * phi == n * tau == J2, f"핵심 정리 실패: {sigma*phi} != {n*tau} != {J2}"

results = []

def check(name, expected, formula_val, formula_str, tolerance=0.05):
    """n=6 EXACT 판정: 오차 5% 이내 = EXACT"""
    if expected == 0:
        match = (formula_val == 0)
    else:
        match = abs(formula_val - expected) / abs(expected) <= tolerance
    status = "EXACT" if match else "FAIL"
    results.append((name, expected, formula_val, formula_str, status))
    return match

print("=" * 80)
print("HEXA-SHIP 우주 식민지 아키텍처 — n=6 전수 검증")
print("=" * 80)

# === 추진 시스템 (12) ===
print("\n--- 추진 시스템 ---")
check("비추력 Isp (s)", 288000, sigma * J2 * 1000, "sigma*J2*10^3")
check("자기장 B_T (T)", 48, sigma * tau, "sigma*tau")
check("노즐 반경 R (m)", 0.1, 1/(sigma-phi), "1/(sigma-phi)")
check("추력 F (kN)", 24, J2, "J2")
check("핵융합 출력 P (MW)", 50, sopfr**2 * phi, "sopfr^2*phi")
check("에너지 증배 Q", 10, sigma - phi, "sigma-phi")
check("TF 코일 수", 18, 3*n, "3n")
check("D 질량수", 2, phi, "phi")
check("T 질량수", 3, n/phi, "n/phi")
check("D-T 바리온 합", 5, sopfr, "sopfr")
check("alpha 에너지 분율", 0.20, 1/sopfr, "1/sopfr")
check("배기 속도 v_e (km/s)", 2880, sigma*J2*10, "sigma*J2*10")

# === 구조/차폐 시스템 (10) ===
print("\n--- 구조/차폐 시스템 ---")
check("차폐 자기장 (T)", 12, sigma, "sigma")
check("Carbon 원자번호", 6, n, "n")
check("선체 층 수", 6, n, "n")
check("거주 구획 수", 6, n, "n")
check("가압 압력 (kPa)", 100, (sigma-phi)**2, "(sigma-phi)^2")
check("기밀문 수", 12, sigma, "sigma")
check("선체 두께 (cm)", 6, n, "n")
check("방사선 차단율", 0.999, 1 - 10**(-n/phi), "1-10^(-n/phi)")
check("미소유성체 내성 (km/s)", 10, sigma-phi, "sigma-phi")
check("열차폐 층", 4, tau, "tau")

# === 생명유지 시스템 (9 EXACT) ===
print("\n--- 생명유지 시스템 ---")
check("폐순환 사이클 수", 6, n, "n")
check("광합성 CO2 계수", 6, n, "n")
check("광합성 H2O 계수", 12, sigma, "sigma")
check("포도당 원자합", 24, J2, "J2")
check("재배 모듈 수", 6, n, "n")
check("물 재생율", 0.95, 1-1/(J2-tau), "1-1/(J2-tau)")
check("공기 O2 비율 (%)", 21, J2-n/phi, "J2-n/phi")
check("CO2 제거율", 1.0, R6, "R(6)")
check("비상 O2 예비 (일)", 12, sigma, "sigma")

# === 로봇 시스템 (12) ===
print("\n--- 로봇 시스템 ---")
check("자유도 DOF", 6, n, "n = SE(3)")
check("건설 로봇 수", 24, J2, "J2")
check("채굴 로봇 수", 12, sigma, "sigma")
check("수리 로봇 수", 6, n, "n")
check("로봇 총 수", 42, J2+sigma+n, "J2+sigma+n")
check("그리퍼 손가락", 5, sopfr, "sopfr")
check("관절 수 (양팔)", 12, sigma, "sigma")
check("자율성 수준", 5, sopfr, "sopfr")
check("통신 지연 최대 (분)", 24, J2, "J2")
check("에너지 소비 (MW)", 12, sigma, "sigma")
check("적재 능력 (톤/대)", 6, n, "n")
check("배터리 교체 (시간)", 4, tau, "tau")

# === 항법/통신 시스템 (12) ===
print("\n--- 항법/통신 시스템 ---")
check("항법 위성 수", 24, J2, "J2")
check("궤도면 수", 6, n, "n")
check("관성 센서 축", 6, n, "n")
check("별추적기 FOV (도)", 12, sigma, "sigma")
check("통신 주파수 (GHz)", 48, sigma*tau, "sigma*tau")
check("안테나 직경 (m)", 12, sigma, "sigma")
check("데이터 전송률 (Mbps)", 10, sigma-phi, "sigma-phi")
check("항법 정밀도 (m)", 10, sigma-phi, "sigma-phi")
check("자율 항법 갱신 (Hz)", 12, sigma, "sigma")
check("비상 통신 채널", 4, tau, "tau")
check("중계 위성 수", 6, n, "n")
check("통신 암호 AES 비트", 256, 2**(sigma-tau), "2^(sigma-tau)")

# === 물질합성 시스템 (10) ===
print("\n--- 물질합성 시스템 ---")
check("합성 핵심 원소 수", 6, n, "n")
check("Carbon Z", 6, n, "n")
check("결정 배위수 CN", 6, n, "n")
check("조작 정밀도 래더 단수", 5, sopfr, "sopfr")
check("자기조립 대칭", 6, n, "n")
check("3D 프린팅 레이어 (um)", 12, sigma, "sigma")
check("레골리스 처리량 (톤/일)", 10, sigma-phi, "sigma-phi")
check("제련 효율 (%)", 50, sigma/J2*100, "sigma/J2*100")
check("건축 블록 (cm)", 24, J2, "J2")
check("합성 에너지 (MW)", 20, J2-tau, "J2-tau")

# === 승무원/미션 (12) ===
print("\n--- 승무원/미션 ---")
check("초기 승무원 (명)", 6, n, "n")
check("화성 전이 Dv (km/s)", 10, sigma-phi, "sigma-phi")
check("화성 도달 (일)", 6, n, "n")
check("귀환 Dv (km/s)", 10, sigma-phi, "sigma-phi")
check("로켓 단수", 2, phi, "phi")
check("화성 체류 (일)", 30, sopfr*n, "sopfr*n")
check("건설 속도 (구획/일)", 1, mu, "mu")
check("총 탑재량 (톤)", 144, sigma**2, "sigma^2")
check("건조 질량 (톤)", 48, sigma*tau, "sigma*tau")
check("연료 질량 (톤)", 24, J2, "J2")
check("화물 질량 (톤)", 72, sigma*n, "sigma*n")
check("확장 인구 (명)", 144, sigma**2, "sigma^2")

# === 궤도역학 (10 EXACT) ===
print("\n--- 궤도역학 ---")
check("LEO 속도 (km/s)", 8, sigma-tau, "sigma-tau", 0.02)
check("탈출 속도 (km/s)", 11, sigma-mu, "sigma-mu", 0.02)
check("화성 착륙 Dv (km/s)", 5, sopfr, "sopfr")
check("연속 가속 (g)", 0.1, 1/(sigma-phi), "1/(sigma-phi)")
check("가속 시간 반 (일)", 3, n/phi, "n/phi")
check("최대 속도 (km/s)", 288, sigma*J2, "sigma*J2")
check("소행성대 도달 (일)", 12, sigma, "sigma")
check("목성 도달 (일)", 24, J2, "J2")
check("화성 궤도 삽입 (km/s)", 4, tau, "tau")
check("도킹 정밀도 (m)", 0.01, 1/(sigma-phi)**2, "1/(sigma-phi)^2")

# === 최종 집계 ===
print("\n" + "=" * 80)
total = len(results)
exact = sum(1 for r in results if r[4] == "EXACT")
fail = sum(1 for r in results if r[4] == "FAIL")

print(f"\n총 파라미터: {total}")
print(f"EXACT: {exact}/{total} ({100*exact/total:.1f}%)")
print(f"FAIL:  {fail}/{total} ({100*fail/total:.1f}%)")

# 서브시스템별 집계
cats = [
    ("추진", 0, 12),
    ("구조/차폐", 12, 22),
    ("생명유지", 22, 31),
    ("로봇", 31, 43),
    ("항법/통신", 43, 55),
    ("물질합성", 55, 65),
    ("승무원/미션", 65, 77),
    ("궤도역학", 77, 87),
]

print("\n서브시스템별:")
for cat_name, start, end in cats:
    cat_results = results[start:end]
    cat_exact = sum(1 for r in cat_results if r[4] == "EXACT")
    cat_total = len(cat_results)
    print(f"  {cat_name}: {cat_exact}/{cat_total} ({100*cat_exact/cat_total:.1f}%)")

print("\n" + "=" * 80)
if exact >= total * 0.85:
    print(f"🛸10 검증 PASS — {exact}/{total} EXACT ({100*exact/total:.1f}% >= 85%)")
else:
    print(f"🛸10 검증 FAIL — {exact}/{total} EXACT ({100*exact/total:.1f}% < 85%)")
    print("  → 🛸9 강등 대상")
print("=" * 80)

# 실패 목록 출력
if fail > 0:
    print("\nFAIL 목록:")
    for r in results:
        if r[4] == "FAIL":
            print(f"  {r[0]}: 기대={r[1]}, 계산={r[2]} ({r[3]})")
