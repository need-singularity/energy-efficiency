// ============================================================
// conv6_3x3.v — Ω₆ CONV6 3×3 spatial (conv.3x3 variant=00)
// ------------------------------------------------------------
// n6-architecture · chip-rtl-gen · Phase 3 Mk.I 샘플 출력
// rtl_generator.hexa → generate_conv6_module(12, 12, 3, 4, "00")
//
// 3×3 컨볼루션, n=6 사이클 pass, τ=4 채널 병렬
// ============================================================

module conv6_3x3 #(
    parameter IMG_H       = 12,     // σ=12
    parameter IMG_W       = 12,     // σ=12
    parameter KERNEL_SIZE = 3,      // 3×3
    parameter CHANNELS    = 4,      // τ=4
    parameter WIDTH_BITS  = 8,      // σ-τ=8
    parameter VARIANT     = 2'b00   // 00 = 3x3
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
// 생성 메타: op=conv6, variant=00, sigma=12, phi=2, tau=4, n=6, phase=Mk.I
// ============================================================
