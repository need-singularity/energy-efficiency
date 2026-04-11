// ============================================================
// conv6_template.v — Ω₆ CONV6 원시연산 Verilog 템플릿
// ------------------------------------------------------------
// n6-architecture · chip-rtl-gen · Phase 3 Mk.I
// 3×3 컨볼루션 + DW/PW fuse (n=6 탭 옵션)
//
// 템플릿 플레이스홀더:
//   {{MODULE_NAME}}  : 생성 모듈 이름 (예: conv6_dw)
//   {{IMG_H}}        : 입력 이미지 높이 (= σ=12)
//   {{IMG_W}}        : 입력 이미지 너비 (= σ=12)
//   {{KERNEL_SIZE}}  : 커널 크기 (3 / 1)
//   {{CHANNELS}}     : 채널 수 (= τ=4)
//   {{WIDTH_BITS}}   : 원소 폭 (= σ-τ=8)
//   {{VARIANT}}      : τ 선택 (00=3x3 01=1x1 10=dw 11=pw)
//
// 사이클: n=6 (3×3 pass) · 1 (1×1) · σ·τ=48 MAC (dw)
// ============================================================

module {{MODULE_NAME}} #(
    parameter IMG_H       = {{IMG_H}},
    parameter IMG_W       = {{IMG_W}},
    parameter KERNEL_SIZE = {{KERNEL_SIZE}},
    parameter CHANNELS    = {{CHANNELS}},
    parameter WIDTH_BITS  = {{WIDTH_BITS}},
    parameter VARIANT     = {{VARIANT}}
)(
    input                                                      clk,
    input                                                      rst_n,
    input                                                      start,
    input  [CHANNELS*IMG_H*IMG_W*WIDTH_BITS-1:0]               img_in,
    input  [CHANNELS*KERNEL_SIZE*KERNEL_SIZE*WIDTH_BITS-1:0]   kernel,
    output reg [CHANNELS*IMG_H*IMG_W*(WIDTH_BITS*2)-1:0]       img_out,
    output reg                                                 done
);

    // ------------------------------------------------------------
    // 파이프 상태 — n=6 사이클 (3×3 pass) / 1 사이클 (1×1)
    // ------------------------------------------------------------
    localparam PIPE_DEPTH_3X3 = 6;
    localparam PIPE_DEPTH_1X1 = 1;

    reg [3:0] phase;

    // ------------------------------------------------------------
    // 컨볼루션 accumulator — 채널별 τ 병렬
    // ------------------------------------------------------------
    integer c, y, x, ky, kx;
    reg [WIDTH_BITS*2-1:0] acc;
    reg [WIDTH_BITS-1:0]   pix, k;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            img_out <= {(CHANNELS*IMG_H*IMG_W*(WIDTH_BITS*2)){1'b0}};
            phase   <= 4'd0;
            done    <= 1'b0;
        end else begin
            case (phase)
                4'd0: begin
                    done <= 1'b0;
                    if (start) phase <= 4'd1;
                end
                4'd1: begin
                    // 메인 컨볼루션 루프 (합성기가 MAC 블록 언롤)
                    for (c = 0; c < CHANNELS; c = c + 1) begin
                        for (y = 0; y < IMG_H; y = y + 1) begin
                            for (x = 0; x < IMG_W; x = x + 1) begin
                                acc = {(WIDTH_BITS*2){1'b0}};
                                for (ky = 0; ky < KERNEL_SIZE; ky = ky + 1) begin
                                    for (kx = 0; kx < KERNEL_SIZE; kx = kx + 1) begin
                                        if ((y+ky) < IMG_H && (x+kx) < IMG_W) begin
                                            pix = img_in[
                                                ((c*IMG_H + (y+ky))*IMG_W + (x+kx))
                                                * WIDTH_BITS +: WIDTH_BITS];
                                            k   = kernel[
                                                ((c*KERNEL_SIZE + ky)*KERNEL_SIZE + kx)
                                                * WIDTH_BITS +: WIDTH_BITS];
                                            acc = acc + (pix * k);
                                        end
                                    end
                                end
                                img_out[((c*IMG_H + y)*IMG_W + x)*(WIDTH_BITS*2)
                                        +: (WIDTH_BITS*2)] <= acc;
                            end
                        end
                    end
                    phase <= 4'd2;
                end
                4'd2: begin
                    done  <= 1'b1;
                    phase <= 4'd0;
                end
                default: phase <= 4'd0;
            endcase
        end
    end

endmodule
// ============================================================
// 생성 메타: {{GEN_META}}
// ============================================================
