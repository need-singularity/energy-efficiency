// ============================================================
// topk_pick.v — Ω₃ TOPK top-φ=2 선택 (tk.pick variant=01)
// ------------------------------------------------------------
// n6-architecture · chip-rtl-gen · Phase 3 Mk.I 샘플 출력
// rtl_generator.hexa → generate_topk_module(12, 2, "01")
//
// τ=4 선별기, k=φ=2 default, MoE 활성 전문가 선택
// ============================================================

module topk_phi2_pick #(
    parameter VEC_LEN    = 12,     // σ=12 후보
    parameter K          = 2,      // φ=2 선별
    parameter WIDTH_BITS = 8,      // σ-τ=8
    parameter IDX_BITS   = 4,      // log₂(σ) = 4
    parameter VARIANT    = 2'b01   // 01 = pick
)(
    input                               clk,
    input                               rst_n,
    input                               start,
    input  [VEC_LEN*WIDTH_BITS-1:0]     scores_in,      // 점수 벡터
    output reg [K*IDX_BITS-1:0]         top_idx,        // 선별 인덱스
    output reg [K*WIDTH_BITS-1:0]       top_val,        // 선별 값
    output reg                          done
);

    // ------------------------------------------------------------
    // 선별 레지스터 (k=φ=2 슬롯)
    // ------------------------------------------------------------
    reg [IDX_BITS-1:0]   top1_idx,  top2_idx;
    reg [WIDTH_BITS-1:0] top1_val,  top2_val;

    // ------------------------------------------------------------
    // 파이프 상태
    // ------------------------------------------------------------
    reg [1:0] phase;

    integer i;
    reg [WIDTH_BITS-1:0] cur_val;
    reg [IDX_BITS-1:0]   cur_idx;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            phase    <= 2'd0;
            top1_idx <= {IDX_BITS{1'b0}};
            top2_idx <= {IDX_BITS{1'b0}};
            top1_val <= {WIDTH_BITS{1'b0}};
            top2_val <= {WIDTH_BITS{1'b0}};
            top_idx  <= {(K*IDX_BITS){1'b0}};
            top_val  <= {(K*WIDTH_BITS){1'b0}};
            done     <= 1'b0;
        end else begin
            case (phase)
                2'd0: begin
                    done <= 1'b0;
                    if (start) phase <= 2'd1;
                end
                2'd1: begin
                    // 스테이지 1 — top-1 탐색
                    top1_val = 8'd0;
                    top1_idx = 4'd0;
                    for (i = 0; i < VEC_LEN; i = i + 1) begin
                        cur_val = scores_in[i*WIDTH_BITS +: WIDTH_BITS];
                        cur_idx = i[IDX_BITS-1:0];
                        if (cur_val > top1_val) begin
                            top1_val = cur_val;
                            top1_idx = cur_idx;
                        end
                    end
                    phase <= 2'd2;
                end
                2'd2: begin
                    // 스테이지 2 — top-2 탐색 (top-1 제외)
                    top2_val = 8'd0;
                    top2_idx = 4'd0;
                    for (i = 0; i < VEC_LEN; i = i + 1) begin
                        cur_val = scores_in[i*WIDTH_BITS +: WIDTH_BITS];
                        cur_idx = i[IDX_BITS-1:0];
                        if (cur_idx != top1_idx && cur_val > top2_val) begin
                            top2_val = cur_val;
                            top2_idx = cur_idx;
                        end
                    end
                    top_idx[0*IDX_BITS +: IDX_BITS]     <= top1_idx;
                    top_idx[1*IDX_BITS +: IDX_BITS]     <= top2_idx;
                    top_val[0*WIDTH_BITS +: WIDTH_BITS] <= top1_val;
                    top_val[1*WIDTH_BITS +: WIDTH_BITS] <= top2_val;
                    done  <= 1'b1;
                    phase <= 2'd0;
                end
                default: phase <= 2'd0;
            endcase
        end
    end

endmodule
// ============================================================
// 생성 메타: op=topk, variant=01, sigma=12, phi=2, tau=4, n=6, phase=Mk.I
// ============================================================
