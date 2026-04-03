NEXUS-6 풀스캔을 실행합니다.

1. `python3 -c "import nexus6; r = nexus6.scan_all(__import__('numpy').random.randn(64,32)); print({k: {kk:round(vv,4) if isinstance(vv,float) else vv for kk,vv in v.items()} for k,v in r.items()})"` 실행
2. 결과에서 n6 EXACT 매칭 추출
3. 3+ 렌즈 합의 항목 보고
4. 발견 사항 있으면 즉시 기록

인자가 있으면 해당 데이터/도메인을 스캔합니다.
$ARGUMENTS
