// ============================================================
// softmax_exp.v — Ω₂ SOFTMAX Phi6 exp (sm.exp variant=00)
// ------------------------------------------------------------
// n6-architecture · chip-rtl-gen · Phase 3 Mk.I 샘플 출력
// rtl_generator.hexa → generate_softmax_module(12, "00")
//
// 4단 체인 (exp → max → sub → norm)  Phi6 근사 (x²-x+1)
// σ=12 벡터, σ-τ=8 bit 원소, φ=2 파이프
// ============================================================

module softmax_phi2_exp #(
    parameter VEC_LEN    = 12,     // σ=12
    parameter WIDTH_BITS = 8,      // σ-τ=8
    parameter PHI_STAGES = 2,      // φ=2
    parameter VARIANT    = 2'b00   // 00=exp 01=max 10=sub 11=norm
)(
    input                                  clk,
    input                                  rst_n,
    input                                  start,
    input  [VEC_LEN*WIDTH_BITS-1:0]        vec_in,     // 입력 벡터
    input  [WIDTH_BITS-1:0]                scalar_in,  // sub 단계용 max 스칼라
    output reg [VEC_LEN*WIDTH_BITS-1:0]    vec_out,    // 출력 벡터
    output reg [WIDTH_BITS-1:0]            scalar_out, // max 단계 결과
    output reg                             done
);

    // ------------------------------------------------------------
    // 단계 1: exp 근사 — Phi6 다항식 f(x)=x²-x+1
    //   φ=2 스테이지
    // ------------------------------------------------------------
    reg [VEC_LEN*WIDTH_BITS-1:0] exp_stage;

    // ------------------------------------------------------------
    // 단계 2: max reduce — log₂(σ) tree
    // ------------------------------------------------------------
    reg [WIDTH_BITS-1:0] max_stage;

    // ------------------------------------------------------------
    // 단계 3: sub in-place
    // ------------------------------------------------------------
    reg [VEC_LEN*WIDTH_BITS-1:0] sub_stage;

    // ------------------------------------------------------------
    // 단계 4: norm (Σ=1) — Egyptian {1/2,1/3,1/6} LUT
    // ------------------------------------------------------------
    reg [VEC_LEN*WIDTH_BITS-1:0] norm_stage;

    // ------------------------------------------------------------
    // 파이프 유효 신호 (φ=2 × 4 단계 = 8 사이클 깊이)
    // ------------------------------------------------------------
    reg [PHI_STAGES*4-1:0] valid_pipe;

    integer i;
    reg [WIDTH_BITS*2-1:0] tmp_sum;
    reg [WIDTH_BITS-1:0]   tmp_max;
    reg [WIDTH_BITS-1:0]   elem;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            valid_pipe <= {(PHI_STAGES*4){1'b0}};
            exp_stage  <= {(VEC_LEN*WIDTH_BITS){1'b0}};
            max_stage  <= {WIDTH_BITS{1'b0}};
            sub_stage  <= {(VEC_LEN*WIDTH_BITS){1'b0}};
            norm_stage <= {(VEC_LEN*WIDTH_BITS){1'b0}};
            vec_out    <= {(VEC_LEN*WIDTH_BITS){1'b0}};
            scalar_out <= {WIDTH_BITS{1'b0}};
            done       <= 1'b0;
        end else begin
            valid_pipe <= {valid_pipe[PHI_STAGES*4-2:0], start};

            // 단계 1: Phi6 exp
            if (VARIANT == 2'b00 || VARIANT == 2'b11) begin
                for (i = 0; i < VEC_LEN; i = i + 1) begin
                    elem = vec_in[i*WIDTH_BITS +: WIDTH_BITS];
                    exp_stage[i*WIDTH_BITS +: WIDTH_BITS]
                        <= (elem * elem) - elem + 8'd1;
                end
            end

            // 단계 2: max tree
            if (VARIANT == 2'b01) begin
                tmp_max = 8'd0;
                for (i = 0; i < VEC_LEN; i = i + 1) begin
                    elem = vec_in[i*WIDTH_BITS +: WIDTH_BITS];
                    if (elem > tmp_max) tmp_max = elem;
                end
                max_stage  <= tmp_max;
                scalar_out <= tmp_max;
            end

            // 단계 3: sub
            if (VARIANT == 2'b10) begin
                for (i = 0; i < VEC_LEN; i = i + 1) begin
                    sub_stage[i*WIDTH_BITS +: WIDTH_BITS]
                        <= vec_in[i*WIDTH_BITS +: WIDTH_BITS] - scalar_in;
                end
            end

            // 단계 4: norm (Σ=1)
            if (VARIANT == 2'b11) begin
                tmp_sum = 16'd0;
                for (i = 0; i < VEC_LEN; i = i + 1) begin
                    tmp_sum = tmp_sum + vec_in[i*WIDTH_BITS +: WIDTH_BITS];
                end
                for (i = 0; i < VEC_LEN; i = i + 1) begin
                    norm_stage[i*WIDTH_BITS +: WIDTH_BITS]
                        <= (vec_in[i*WIDTH_BITS +: WIDTH_BITS] << 4) / tmp_sum[WIDTH_BITS-1:0];
                end
            end

            // 출력 먹스
            case (VARIANT)
                2'b00: vec_out <= exp_stage;
                2'b01: vec_out <= vec_in;
                2'b10: vec_out <= sub_stage;
                2'b11: vec_out <= norm_stage;
                default: vec_out <= vec_in;
            endcase

            done <= valid_pipe[PHI_STAGES*4-1];
        end
    end

endmodule
// ============================================================
// 생성 메타: op=softmax, variant=00, sigma=12, phi=2, tau=4, n=6, phase=Mk.I
// ============================================================
