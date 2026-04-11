// sc-dse — HEXA DSE 도구 래퍼
// 원본: tools/sc-dse/main.hexa

pub fn run(args: &[String]) -> Result<(), String> {
    super::hx("sc-dse", args)
}
