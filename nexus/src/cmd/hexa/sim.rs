// hexa-sim — 분석/시뮬 벤치마크 자료 디렉터리
// 원본: tools/hexa-sim/
// 디렉터리 경로만 출력하는 얇은 진입점. 벤치는 .hexa 스크립트로 실행.

pub fn run(args: &[String]) -> Result<(), String> {
    let dir = super::tools_dir("hexa-sim");
    if args.is_empty() {
        println!("[hexa-sim] 자산 디렉터리: {}", dir);
        println!("  analysis/  benchmarks/  configs/");
        return Ok(());
    }
    Err(format!(
        "[hexa-sim] 서브커맨드 미구현: {:?} — 디렉터리={}",
        args, dir
    ))
}
