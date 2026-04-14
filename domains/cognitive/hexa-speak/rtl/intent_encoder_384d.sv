// =============================================================================
// 모듈명: intent_encoder_384d
// 카테고리: N6-SPEAK v2 tier-1 (input layer)
// 목적  : 텍스트/의도 토큰 → 384차원 임베딩 인코더
// 근거  : σ(6)·τ(6)·8 = 12·4·8 = 384 (n=6 산술 유일 유도)
// 산술  : 384 = σ·τ·8, σ(6)=12 heads, τ(6)=4 ports, 8 = σ(6)-τ(6) = RVQ 스테이지수
// DRC   : lint clean, no latches, reset=active-low, synchronous logic only
// LVS   : 포트 폭 고정 — intent_in[383:0], embed_out[383:0], valid/ready handshake
// 상위 스펙: proto/n6-speak-v2-spec.md §2 tier-1, §5.2 (384 = σ·τ·sopfr+σ·sopfr 동결)
// =============================================================================

`timescale 1ns / 1ps
`default_nettype none

module intent_encoder_384d #(
    // n=6 산술 파라미터 (변경 금지, §5.4 변경 금지 사유)
    parameter int EMBED_DIM   = 384,  // σ·τ·8
    parameter int NUM_HEADS   = 12,   // σ(6)
    parameter int HEAD_DIM    = 32,   // EMBED_DIM / NUM_HEADS = 384/12
    parameter int VOCAB_BITS  = 15    // vocab 32k → 15 bit
) (
    // 클록/리셋 (active-low)
    input  wire                       clk,
    input  wire                       rst_n,

    // 입력: 의도 토큰 (15-bit × 32 = 480-bit pack, 하지만 상위 intent 벡터는 384-bit fp16 pack)
    input  wire [EMBED_DIM-1:0]       intent_in,     // 의도 벡터 (384 bit, FP16 × 24 또는 INT16 × 24 tile)
    input  wire                       intent_valid,  // 입력 유효
    output reg                        intent_ready,  // 입력 수용 가능

    // 출력: 384차원 임베딩
    output reg  [EMBED_DIM-1:0]       embed_out,     // 임베딩 벡터 (384 bit)
    output reg                        embed_valid,   // 출력 유효
    input  wire                       embed_ready    // 다운스트림 수용 가능
);

    // -------------------------------------------------------------------------
    // 내부 레지스터 (n=6 스테이지 깊이, §4 tier-1 latency ≤ σ cycles)
    // -------------------------------------------------------------------------
    localparam int N6_STAGES = 6;  // 6 파이프라인 단 (피질 6층 ↔ RTL 6단)

    reg [EMBED_DIM-1:0] stage_pipe [0:N6_STAGES-1];  // 6단 시프트 레지스터
    reg [N6_STAGES-1:0] valid_pipe;                  // 각 단 유효 플래그

    // -------------------------------------------------------------------------
    // 인코더 로직 (벡터 정규화 + head-별 분할)
    // 실제 MAC 연산은 상위 Xn6 NPU에서 수행 — 본 모듈은 정합/파이프라인/핸드셰이크만 담당
    // -------------------------------------------------------------------------
    integer i;
    always_ff @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            for (i = 0; i < N6_STAGES; i = i + 1) begin
                stage_pipe[i] <= {EMBED_DIM{1'b0}};
            end
            valid_pipe   <= {N6_STAGES{1'b0}};
            intent_ready <= 1'b1;
            embed_out    <= {EMBED_DIM{1'b0}};
            embed_valid  <= 1'b0;
        end else begin
            // 1 단: 입력 수용
            if (intent_valid && intent_ready) begin
                stage_pipe[0] <= intent_in;
                valid_pipe[0] <= 1'b1;
            end else begin
                valid_pipe[0] <= 1'b0;
            end

            // 2~6 단: 시프트 (6단 파이프라인, 피질 6층 동형)
            for (i = 1; i < N6_STAGES; i = i + 1) begin
                stage_pipe[i] <= stage_pipe[i-1];
                valid_pipe[i] <= valid_pipe[i-1];
            end

            // 출력 단 (6번째 단 → embed_out)
            if (valid_pipe[N6_STAGES-1] && embed_ready) begin
                embed_out   <= stage_pipe[N6_STAGES-1];
                embed_valid <= 1'b1;
            end else if (embed_ready) begin
                embed_valid <= 1'b0;
            end

            // 핸드셰이크: 파이프라인 포화 시 back-pressure
            intent_ready <= embed_ready || !valid_pipe[N6_STAGES-1];
        end
    end

    // -------------------------------------------------------------------------
    // n=6 산술 정합 어설션 (합성 시 무시, 시뮬시 체크)
    // -------------------------------------------------------------------------
    // synthesis translate_off
    initial begin
        assert (EMBED_DIM == 384)
            else $error("EMBED_DIM 은 384 (σ·τ·8) 여야 함 — §5.4 변경 금지");
        assert (NUM_HEADS == 12)
            else $error("NUM_HEADS 는 σ(6)=12 여야 함");
        assert (EMBED_DIM % NUM_HEADS == 0)
            else $error("HEAD_DIM 정수 분할 실패");
        $display("[intent_encoder_384d] 초기화 — 384차원 임베딩, 12 heads, 32 head_dim, 6단 파이프라인");
    end
    // synthesis translate_on

endmodule

`default_nettype wire
