// fusion-verify — HEXA 분석 도구 래퍼
// 원본: tools/fusion-verify/main.hexa

pub fn run(args: &[String]) -> Result<(), String> {
    super::hx("fusion-verify", args)
}
