// fusion-dse — HEXA DSE 도구 래퍼
// 원본: tools/fusion-dse/main.hexa

pub fn run(args: &[String]) -> Result<(), String> {
    super::hx("fusion-dse", args)
}
