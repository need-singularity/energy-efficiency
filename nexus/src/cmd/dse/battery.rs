// battery-dse — HEXA DSE 도구 래퍼
// 원본: tools/battery-dse/main.hexa

pub fn run(args: &[String]) -> Result<(), String> {
    super::hx("battery-dse", args)
}
