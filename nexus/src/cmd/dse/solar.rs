// solar-dse — HEXA DSE 도구 래퍼
// 원본: tools/solar-dse/main.hexa

pub fn run(args: &[String]) -> Result<(), String> {
    super::hx("solar-dse", args)
}
