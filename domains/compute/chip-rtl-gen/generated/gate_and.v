// ============================================================
// gate_and.v — Ω₄ GATE bit AND 마스크 (gt.and variant=01)
// ------------------------------------------------------------
// n6-architecture · chip-rtl-gen · Phase 3 Mk.I 샘플 출력
// rtl_generator.hexa → generate_gate_module(12, "01")
//
// μ=1 사이클 AND/OR/XOR 마스크, Boltzmann 1/e 임계 옵션
// ============================================================

module gate_mu1_and #(
    parameter VEC_LEN    = 12,      // σ=12
    parameter WIDTH_BITS = 8,       // σ-τ=8
    parameter GATE_MODE  = 1,       // 1 = AND
    parameter VARIANT    = 2'b01    // 01 = gt.and
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
// 생성 메타: op=gate, variant=01, sigma=12, phi=2, tau=4, n=6, phase=Mk.I
// ============================================================
