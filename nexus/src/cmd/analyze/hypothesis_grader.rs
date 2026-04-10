// hypothesis-grader — HEXA 분석 도구 래퍼
// 원본: tools/hypothesis-grader/main.hexa

pub fn run(args: &[String]) -> Result<(), String> {
    super::hx("hypothesis-grader", args)
}
