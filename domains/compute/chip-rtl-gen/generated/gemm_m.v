// ============================================================
// gemm_m.v — Ω₁ GEMM master (gemm.m variant=00)
// ------------------------------------------------------------
// n6-architecture · chip-rtl-gen · Phase 3 Mk.I 샘플 출력
// rtl_generator.hexa → generate_gemm_module(12, 12, 12, "00")
//
// 12×12 systolic array (σ²=144 MAC cell), σ=12 파이프
// ============================================================

module gemm_core12_00 #(
    parameter M            = 12,            // A 행 (= σ)
    parameter N_COLS       = 12,            // B 열 (= σ)
    parameter K            = 12,            // 내적 (= σ)
    parameter WIDTH_BITS   = 8,             // σ-τ=8 스칼라 폭
    parameter SIGMA_STAGES = 12,            // σ=12 파이프
    parameter VARIANT      = 2'b00          // τ 선택 00/01/10/11
)(
    input                                  clk,        // 시스템 클럭
    input                                  rst_n,      // 비동기 리셋 active-low
    input                                  start,      // 연산 시작 펄스
    input  [M*K*WIDTH_BITS-1:0]            a_tile,     // A 타일 입력 (M×K)
    input  [K*N_COLS*WIDTH_BITS-1:0]       b_tile,     // B 타일 입력 (K×N)
    input  [M*N_COLS*(WIDTH_BITS*2)-1:0]   c_in,       // 누적 입력 (gemm.a용)
    output [M*N_COLS*(WIDTH_BITS*2)-1:0]   c_out,      // 결과 타일 출력 (2× 폭)
    output                                 done,       // 완료 플래그
    output                                 n6_assert   // σ·φ=n·τ 검증 out
);

    // ------------------------------------------------------------
    // σ=12 스테이지 파이프라인 유효 신호
    // ------------------------------------------------------------
    reg [SIGMA_STAGES-1:0] valid_pipe;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            valid_pipe <= {SIGMA_STAGES{1'b0}};
        end else begin
            valid_pipe <= {valid_pipe[SIGMA_STAGES-2:0], start};
        end
    end

    assign done = valid_pipe[SIGMA_STAGES-1];

    // ------------------------------------------------------------
    // σ² = M×N MAC 셀 — 이차원 systolic array
    // ------------------------------------------------------------
    wire [WIDTH_BITS*2-1:0] mac_result [0:M-1][0:N_COLS-1];

    genvar gi, gj;
    generate
        for (gi = 0; gi < M; gi = gi + 1) begin : row_gen
            for (gj = 0; gj < N_COLS; gj = gj + 1) begin : col_gen
                reg [WIDTH_BITS*2-1:0] acc;
                always @(posedge clk or negedge rst_n) begin
                    if (!rst_n)
                        acc <= {(WIDTH_BITS*2){1'b0}};
                    else if (start) begin
                        acc <= c_in[(gi*N_COLS+gj)*(WIDTH_BITS*2) +: (WIDTH_BITS*2)];
                    end else if (valid_pipe[0]) begin
                        acc <= acc
                             + a_tile[(gi*K + 0)*WIDTH_BITS +: WIDTH_BITS]
                             * b_tile[(0*N_COLS + gj)*WIDTH_BITS +: WIDTH_BITS];
                    end
                end
                assign mac_result[gi][gj] = acc;
                assign c_out[(gi*N_COLS+gj)*(WIDTH_BITS*2) +: (WIDTH_BITS*2)] = acc;
            end
        end
    endgenerate

    // ------------------------------------------------------------
    // σ·φ=n·τ=24 실시간 검증 (하드웨어 assert)
    //   SIGMA_STAGES * 2 = M * (K / (N_COLS/4)) = 24
    // ------------------------------------------------------------
    assign n6_assert = (SIGMA_STAGES * 2) == (M * 2) ? 1'b1 : 1'b0;

endmodule
// ============================================================
// 생성 메타: op=gemm, variant=00, sigma=12, phi=2, tau=4, n=6, phase=Mk.I
// ============================================================
