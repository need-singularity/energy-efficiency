// bt-extension-verifier — HEXA 분석 도구 래퍼
// 원본: tools/bt-extension-verifier/main.hexa

pub fn run(args: &[String]) -> Result<(), String> {
    super::hx("bt-extension-verifier", args)
}
