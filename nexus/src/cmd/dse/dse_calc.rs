// dse-calc — HEXA DSE 도구 래퍼
// 원본: tools/dse-calc/main.hexa

pub fn run(args: &[String]) -> Result<(), String> {
    super::hx("dse-calc", args)
}
