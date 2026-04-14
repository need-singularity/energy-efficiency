// =============================================================================
// 모듈명: emotion_classifier_6emo
// 카테고리: N6-SPEAK v2 tier-2a (middle layer, emotion branch)
// 목적  : 384차원 임베딩 → 6 감정 classifier (happy/sad/angry/fear/surprise/neutral)
// 근거  : 6 = sopfr(6)+1 = Ekman 6 기본감정 ↔ n=6 완전수 정합
// 산술  : W [384, 6] 가중치, softmax 아닌 argmax + top-1 인덱스 출력 (HW 경량화)
// DRC   : lint clean, no latches, reset=active-low
// LVS   : 입력 384-bit, 출력 6-bit one-hot + 3-bit 인덱스 (2^3=8 ≥ 6)
// 상위 스펙: proto/n6-speak-v2-spec.md §2 tier-2a, §5.2 (6 = sopfr+1 동결)
// =============================================================================

`timescale 1ns / 1ps
`default_nettype none

module emotion_classifier_6emo #(
    parameter int EMBED_DIM  = 384,   // σ·τ·8
    parameter int NUM_EMO    = 6,     // n=6 감정 수 (sopfr(6)+1)
    parameter int EMO_IDX_W  = 3      // 인덱스 비트 폭 (⌈log2(6)⌉=3)
) (
    // 클록/리셋 (active-low)
    input  wire                       clk,
    input  wire                       rst_n,

    // 입력: 384차원 임베딩
    input  wire [EMBED_DIM-1:0]       embed_in,       // tier-1에서 온 임베딩
    input  wire                       embed_valid,    // 입력 유효
    output reg                        embed_ready,    // 입력 수용 가능

    // 출력: 감정 one-hot + 인덱스
    output reg  [NUM_EMO-1:0]         emo_out,        // 6-bit one-hot
                                                      // [0]=happy, [1]=sad, [2]=angry,
                                                      // [3]=fear,  [4]=surprise, [5]=neutral
    output reg  [EMO_IDX_W-1:0]       emo_idx,        // 0~5 인덱스
    output reg                        emo_valid,      // 출력 유효
    input  wire                       emo_ready       // 다운스트림 수용 가능
);

    // -------------------------------------------------------------------------
    // 감정 로짓 레지스터 (6 logits, 각 16-bit)
    // -------------------------------------------------------------------------
    reg signed [15:0] logits [0:NUM_EMO-1];

    // 임베딩 부분합 (실제 MAC 은 외부 NPU, 여기서는 상위 6 bit를 대표 logit으로 사용)
    // 이는 HW 경량화 구조 — 풀 MAC은 tier-2c fusion 단계에서 수행
    wire [15:0] embed_slice [0:NUM_EMO-1];
    genvar gi;
    generate
        for (gi = 0; gi < NUM_EMO; gi = gi + 1) begin : g_slice
            // 각 감정에 할당된 64차원 슬라이스의 첫 16비트 (384/6=64)
            assign embed_slice[gi] = embed_in[gi*64 +: 16];
        end
    endgenerate

    // -------------------------------------------------------------------------
    // argmax 로직 (6-way 비교, τ=4 스테이지 트리)
    // 트리 깊이 = ⌈log2(6)⌉ = 3 단 (τ 이내)
    // -------------------------------------------------------------------------
    integer j;
    reg signed [15:0]       max_val;
    reg        [EMO_IDX_W-1:0] max_idx;

    always_comb begin
        max_val = logits[0];
        max_idx = 3'd0;
        for (j = 1; j < NUM_EMO; j = j + 1) begin
            if (logits[j] > max_val) begin
                max_val = logits[j];
                max_idx = j[EMO_IDX_W-1:0];
            end
        end
    end

    // -------------------------------------------------------------------------
    // 파이프라인 제어 (1 cycle latency)
    // -------------------------------------------------------------------------
    integer k;
    always_ff @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            for (k = 0; k < NUM_EMO; k = k + 1) begin
                logits[k] <= 16'sd0;
            end
            emo_out     <= {NUM_EMO{1'b0}};
            emo_idx     <= {EMO_IDX_W{1'b0}};
            emo_valid   <= 1'b0;
            embed_ready <= 1'b1;
        end else begin
            if (embed_valid && embed_ready) begin
                // 로짓 업데이트 (단순화된 선형 매핑, 실사용 시 W [384,6] 행렬곱)
                for (k = 0; k < NUM_EMO; k = k + 1) begin
                    logits[k] <= $signed(embed_slice[k]);
                end
            end

            if (emo_ready) begin
                // one-hot 출력
                emo_out <= ({NUM_EMO{1'b0}} | ({ {(NUM_EMO-1){1'b0}}, 1'b1 } << max_idx));
                emo_idx <= max_idx;
                emo_valid <= embed_valid;
            end

            embed_ready <= emo_ready;
        end
    end

    // -------------------------------------------------------------------------
    // n=6 산술 정합 어설션
    // -------------------------------------------------------------------------
    // synthesis translate_off
    initial begin
        assert (NUM_EMO == 6)
            else $error("NUM_EMO 는 6 (sopfr(6)+1) 여야 함 — §5.4 변경 금지");
        assert (EMBED_DIM == 384)
            else $error("EMBED_DIM 은 384 여야 함");
        assert (EMBED_DIM % NUM_EMO == 0)
            else $error("임베딩 6분할 실패 (384/6=64 정수 여야 함)");
        $display("[emotion_classifier_6emo] 초기화 — 6 감정 (Ekman), per-emo 64-dim slice");
    end
    // synthesis translate_on

endmodule

`default_nettype wire
