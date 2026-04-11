// ============================================================
// gate_template.v — Ω₄ GATE 원시연산 Verilog 템플릿
// ------------------------------------------------------------
// n6-architecture · chip-rtl-gen · Phase 3 Mk.I
// μ=1 사이클 AND/OR/XOR 마스크 (Boltzmann 1/e 임계 옵션)
//
// 템플릿 플레이스홀더:
//   {{MODULE_NAME}}  : 생성 모듈 이름 (예: boltz_gate)
//   {{VEC_LEN}}      : 벡터 길이 (= σ=12)
//   {{WIDTH_BITS}}   : 원소 폭 (= σ-τ=8)
//   {{GATE_MODE}}    : 0=mul 1=and 2=or 3=xor
//   {{VARIANT}}      : τ 선택 (00=mul 01=and 10=or 11=xor)
//
// 사이클: μ=1 (단일 사이클)
// Boltzmann 임계: 1/e ≈ 94 (8비트) / 256
// ============================================================

module {{MODULE_NAME}} #(
    parameter VEC_LEN    = {{VEC_LEN}},
    parameter WIDTH_BITS = {{WIDTH_BITS}},
    parameter GATE_MODE  = {{GATE_MODE}},
    parameter VARIANT    = {{VARIANT}}
)(
    input                              clk,
    input                              rst_n,
    input                              start,
    input  [VEC_LEN*WIDTH_BITS-1:0]    a_in,      // 입력 벡터 A
    input  [VEC_LEN*WIDTH_BITS-1:0]    mask_in,   // 마스크 벡터
    input  [WIDTH_BITS-1:0]            threshold, // Boltzmann 1/e 임계
    output reg [VEC_LEN*WIDTH_BITS-1:0] y_out,    // 게이트 출력
    output reg [VEC_LEN-1:0]            keep_bits,// zero-skip 마스크
    output reg                          done
);

    // Boltzmann 1/e (8 비트) = 256/e ≈ 94
    localparam [WIDTH_BITS-1:0] BOLTZ_INV_E = 8'd94;

    integer i;
    reg [WIDTH_BITS-1:0] ae, me;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            y_out     <= {(VEC_LEN*WIDTH_BITS){1'b0}};
            keep_bits <= {VEC_LEN{1'b0}};
            done      <= 1'b0;
        end else if (start) begin
            // μ=1 사이클 — 조합 게이팅
            for (i = 0; i < VEC_LEN; i = i + 1) begin
                ae = a_in[i*WIDTH_BITS +: WIDTH_BITS];
                me = mask_in[i*WIDTH_BITS +: WIDTH_BITS];
                case (VARIANT)
                    2'b00: y_out[i*WIDTH_BITS +: WIDTH_BITS] <= ae * me;   // gt.mul
                    2'b01: y_out[i*WIDTH_BITS +: WIDTH_BITS] <= ae & me;   // gt.and
                    2'b10: y_out[i*WIDTH_BITS +: WIDTH_BITS] <= ae | me;   // gt.or
                    2'b11: y_out[i*WIDTH_BITS +: WIDTH_BITS] <= ae ^ me;   // gt.xor
                    default: y_out[i*WIDTH_BITS +: WIDTH_BITS] <= ae;
                endcase
                // Boltzmann zero-skip 비트 — 1/e 임계 미만 zero 처리
                keep_bits[i] <= (ae >= threshold) ? 1'b1 : 1'b0;
            end
            done <= 1'b1;
        end else begin
            done <= 1'b0;
        end
    end

endmodule
// ============================================================
// 생성 메타: {{GEN_META}}
// ============================================================
