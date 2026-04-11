// robot-dse — HEXA DSE 도구 래퍼
// 원본: tools/robot-dse/main.hexa

pub fn run(args: &[String]) -> Result<(), String> {
    super::hx("robot-dse", args)
}
