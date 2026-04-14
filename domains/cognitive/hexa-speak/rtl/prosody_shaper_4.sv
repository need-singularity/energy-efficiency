// =============================================================================
// 모듈명: prosody_shaper_4
// 카테고리: N6-SPEAK v2 tier-2b (middle layer, prosody branch)
// 목적  : 384차원 임베딩 → 4 운율 파라미터 (pitch/speed/volume/tone)
// 근거  : 4 = τ(6) = 약수 개수 (운율쌍: pitch-duration / energy-spectral)
// 산술  : W [384, 4] 가중치, 각 prosody 16-bit FP16 출력, 총 4×16=64-bit
// DRC   : lint clean, no latches, reset=active-low
// LVS   : 입력 384-bit, 출력 prosody_out[3:0][15:0] (4×16 = 64-bit)
// 상위 스펙: proto/n6-speak-v2-spec.md §2 tier-2b, §5.2 (4 = τ(6) 동결)
// =============================================================================

`timescale 1ns / 1ps
`default_nettype none

module prosody_shaper_4 #(
    parameter int EMBED_DIM   = 384,  // σ·τ·8
    parameter int NUM_PROSODY = 4,    // τ(6)=4 (pitch/speed/volume/tone)
    parameter int PROSODY_W   = 16    // FP16 bit 폭
) (
    // 클록/리셋 (active-low)
    input  wire                                       clk,
    input  wire                                       rst_n,

    // 입력: 384차원 임베딩 (tier-1에서)
    input  wire [EMBED_DIM-1:0]                       embed_in,
    input  wire                                       embed_valid,
    output reg                                        embed_ready,

    // 출력: 4 운율 파라미터 (unpacked array)
    // [0] = pitch    (음높이)
    // [1] = speed    (속도/duration)
    // [2] = volume   (크기/energy)
    // [3] = tone     (음색/spectral)
    output reg  [PROSODY_W-1:0]                       prosody_out [0:NUM_PROSODY-1],
    output reg                                        prosody_valid,
    input  wire                                       prosody_ready
);

    // -------------------------------------------------------------------------
    // 384d → 4d 축약 (per-prosody 96-dim 슬라이스, 384/4=96)
    // 실제 W[384,4] 행렬곱은 Xn6 NPU 에서 수행. 본 RTL은 파이프라인 staging 담당.
    // -------------------------------------------------------------------------
    localparam int SLICE_DIM = EMBED_DIM / NUM_PROSODY;  // 96

    wire [PROSODY_W-1:0] prosody_acc [0:NUM_PROSODY-1];

    // 각 prosody 차원에 대해 96-dim 슬라이스의 상위 16-bit 대표값 사용
    genvar gi;
    generate
        for (gi = 0; gi < NUM_PROSODY; gi = gi + 1) begin : g_acc
            assign prosody_acc[gi] = embed_in[gi*SLICE_DIM +: PROSODY_W];
        end
    endgenerate

    // -------------------------------------------------------------------------
    // τ=4 병렬 스테이지 (각 운율 차원이 τ 병렬 처리)
    // latency = 1 cycle (tier-2b 는 경량)
    // -------------------------------------------------------------------------
    integer k;
    always_ff @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            for (k = 0; k < NUM_PROSODY; k = k + 1) begin
                prosody_out[k] <= {PROSODY_W{1'b0}};
            end
            prosody_valid <= 1'b0;
            embed_ready   <= 1'b1;
        end else begin
            if (embed_valid && embed_ready && prosody_ready) begin
                // τ=4 병렬 업데이트
                for (k = 0; k < NUM_PROSODY; k = k + 1) begin
                    prosody_out[k] <= prosody_acc[k];
                end
                prosody_valid <= 1'b1;
            end else if (prosody_ready) begin
                prosody_valid <= 1'b0;
            end

            embed_ready <= prosody_ready;
        end
    end

    // -------------------------------------------------------------------------
    // n=6 산술 정합 어설션
    // -------------------------------------------------------------------------
    // synthesis translate_off
    initial begin
        assert (NUM_PROSODY == 4)
            else $error("NUM_PROSODY 는 τ(6)=4 여야 함 — §5.4 변경 금지");
        assert (EMBED_DIM == 384)
            else $error("EMBED_DIM 은 384 여야 함");
        assert (EMBED_DIM % NUM_PROSODY == 0)
            else $error("임베딩 τ=4 분할 실패 (384/4=96 정수 여야 함)");
        $display("[prosody_shaper_4] 초기화 — 4 운율 (pitch/speed/volume/tone), per-prosody 96-dim slice");
    end
    // synthesis translate_on

endmodule

`default_nettype wire
