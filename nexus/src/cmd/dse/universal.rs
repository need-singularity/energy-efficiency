// universal-dse — HEXA DSE 도구 래퍼
// 원본: tools/universal-dse/main.hexa

pub fn run(args: &[String]) -> Result<(), String> {
    super::hx("universal-dse", args)
}
