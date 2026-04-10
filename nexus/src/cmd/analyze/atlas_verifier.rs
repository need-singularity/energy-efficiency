// atlas-verifier — HEXA 분석 도구 래퍼
// 원본: tools/atlas-verifier/main.hexa

pub fn run(args: &[String]) -> Result<(), String> {
    super::hx("atlas-verifier", args)
}
