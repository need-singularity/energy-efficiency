// ============================================================
// reduce_template.v — Ω₅ REDUCE 원시연산 Verilog 템플릿
// ------------------------------------------------------------
// n6-architecture · chip-rtl-gen · Phase 3 Mk.I
// τ=4 reduce tree (sum/max/min/mean)
//
// 템플릿 플레이스홀더:
//   {{MODULE_NAME}}  : 생성 모듈 이름 (예: reduce_tau4)
//   {{TAU_DEPTH}}    : 입력 원소 수 (= τ=4)
//   {{WIDTH_BITS}}   : 원소 폭 (= σ-τ=8)
//   {{REDUCE_OP}}    : 0=sum 1=max 2=min 3=mean
//   {{VARIANT}}      : τ 선택 (00=sum 01=max 10=min 11=mean)
//
// 사이클: log₂(τ)=φ=2 (adder tree depth)
// ============================================================

module {{MODULE_NAME}} #(
    parameter TAU_DEPTH  = {{TAU_DEPTH}},
    parameter WIDTH_BITS = {{WIDTH_BITS}},
    parameter REDUCE_OP  = {{REDUCE_OP}},
    parameter VARIANT    = {{VARIANT}}
)(
    input                                  clk,
    input                                  rst_n,
    input                                  start,
    input  [TAU_DEPTH*WIDTH_BITS-1:0]      in_vec,
    output reg [WIDTH_BITS*2-1:0]          out_val,     // 2× 폭 (sum 오버플로우)
    output reg                             done
);

    // ------------------------------------------------------------
    // φ=2 스테이지 reduce tree
    //   스테이지 0: τ=4 원소 → 2 중간값
    //   스테이지 1: 2 중간값 → 1 결과
    // ------------------------------------------------------------
    reg [WIDTH_BITS*2-1:0] stage0_a, stage0_b;
    reg [1:0]              phase;

    reg [WIDTH_BITS-1:0] e0, e1, e2, e3;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            stage0_a <= {(WIDTH_BITS*2){1'b0}};
            stage0_b <= {(WIDTH_BITS*2){1'b0}};
            out_val  <= {(WIDTH_BITS*2){1'b0}};
            phase    <= 2'd0;
            done     <= 1'b0;
        end else begin
            case (phase)
                2'd0: begin
                    done <= 1'b0;
                    if (start) begin
                        e0 = in_vec[0*WIDTH_BITS +: WIDTH_BITS];
                        e1 = in_vec[1*WIDTH_BITS +: WIDTH_BITS];
                        e2 = in_vec[2*WIDTH_BITS +: WIDTH_BITS];
                        e3 = in_vec[3*WIDTH_BITS +: WIDTH_BITS];
                        // 스테이지 0 — 쌍별 축약
                        case (VARIANT)
                            2'b00, 2'b11: begin  // sum / mean
                                stage0_a <= e0 + e1;
                                stage0_b <= e2 + e3;
                            end
                            2'b01: begin         // max
                                stage0_a <= (e0 > e1) ? e0 : e1;
                                stage0_b <= (e2 > e3) ? e2 : e3;
                            end
                            2'b10: begin         // min
                                stage0_a <= (e0 < e1) ? e0 : e1;
                                stage0_b <= (e2 < e3) ? e2 : e3;
                            end
                            default: begin
                                stage0_a <= {(WIDTH_BITS*2){1'b0}};
                                stage0_b <= {(WIDTH_BITS*2){1'b0}};
                            end
                        endcase
                        phase <= 2'd1;
                    end
                end
                2'd1: begin
                    // 스테이지 1 — 최종 축약
                    case (VARIANT)
                        2'b00: out_val <= stage0_a + stage0_b;               // sum
                        2'b01: out_val <= (stage0_a > stage0_b) ? stage0_a : stage0_b; // max
                        2'b10: out_val <= (stage0_a < stage0_b) ? stage0_a : stage0_b; // min
                        2'b11: out_val <= (stage0_a + stage0_b) >> 2;        // mean = sum / τ=4
                        default: out_val <= {(WIDTH_BITS*2){1'b0}};
                    endcase
                    done  <= 1'b1;
                    phase <= 2'd0;
                end
                default: phase <= 2'd0;
            endcase
        end
    end

endmodule
// ============================================================
// 생성 메타: {{GEN_META}}
// ============================================================
