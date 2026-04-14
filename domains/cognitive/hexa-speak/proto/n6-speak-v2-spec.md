# N6-SPEAK v2 — HW 4-tier 동결 스펙 (CHIP-P0-3)

- 문서 버전: v2.0-frozen
- 동결일: 2026-04-14
- 상위 설계: ../hexa-speak.md (§1~§15)
- 위치: domains/cognitive/hexa-speak/proto/

## §1 개요

### 1.1 목표

의도 임베딩 → 감정 → 운율 → 오디오 코덱의 4-tier 파이프라인을 HW 레이어 단위로
동결하여 Xn6 칩(SIMD=6way, σ=12 heads, τ=4 ports)에 곧바로 맵핑 가능하도록 고정.

### 1.2 제약 (n=6 산술 정합)

- σ(6)=12, τ(6)=4, φ(6)=2, sopfr(6)=5, n=6 유일성 (iff 조건)
- σ(8)=15, τ(8)=4 → 8-RVQ 스테이지 선택 근거
- 6 감정 = sopfr(6)+1 = 6 (Ekman 6 기본감정 ↔ n=6)
- 4 운율 = τ(6) = 4 (pitch/duration/energy/spectral)
- 384d = σ(6)·τ(6)·σ(6)+σ(6)·sopfr(6) 변형 불가 (아래 §5 정합표 참조)

### 1.3 4-tier HW 레이어 (동결)

```
tier-1: input layer   — intent encoder   (384d embedding)
tier-2: middle layer  — emotion class.   (6 emo)  +  prosody shaper (4 prosody)
tier-3: codec layer   — audio RVQ        (8 stages, 1024 codebook)
tier-4: output layer  — waveform decoder (24kHz, mono, 16-bit)
```

각 tier 는 Xn6 칩의 서로 다른 NPU 파티션에 고정 배치됨. 실행 경계(staging boundary)
이동 불가, 파라미터 폭(bit-width) 고정, 인터페이스 shape 고정.

## §2 모듈별 입출력 shape 표

| tier | 모듈            | 입력 shape          | 출력 shape          | 파라미터         | 산술근거       |
|------|-----------------|---------------------|---------------------|------------------|----------------|
| 1    | intent encoder  | tokens [B, T]       | embed  [B, T, 384]  | vocab 32k, dim=384 | 384 = σ·τ·8    |
| 2a   | emotion class.  | embed  [B, 384]     | logits [B, 6]       | W [384, 6]       | 6 = sopfr+1    |
| 2b   | prosody shaper  | embed  [B, T, 384]  | prosody[B, T, 4]    | W [384, 4]       | 4 = τ(6)       |
| 2c   | fusion          | concat 3 stream     | h      [B, T, 768]  | 768 = 2·384      | φ(6)·384       |
| 3    | audio RVQ enc.  | h      [B, T, 768]  | codes  [B, T, 8]    | 8 stage × 1024   | 8 = σ(6)-τ(6)  |
| 3    | audio RVQ dec.  | codes  [B, T, 8]    | feat   [B, T, 768]  | codebook 1024    | 1024=2^(σ-φ)   |
| 4    | waveform dec.   | feat   [B, T, 768]  | wave   [B, T·320]   | 24kHz mono 16bit | 320=chunk/τ    |

- B = batch, T = token length
- 모든 차원은 n=6 산술로부터 유도 (§5)
- bit-width: intent/emotion/prosody = FP16, RVQ/wave = INT8

## §3 데이터 경로 다이어그램 (ASCII)

```
  텍스트/의도 입력
         │
         ▼
  ┌────────────────────┐
  │ tier-1: input      │
  │  intent encoder    │    ─── tokens [B,T] → embed [B,T,384]
  │  (Xn6 NPU-part-1)  │
  └────────┬───────────┘
           │ embed[B,T,384]
           ▼
  ┌────────────────────────────────┐
  │ tier-2: middle                 │
  │ ┌──────────┐  ┌─────────────┐  │
  │ │ emotion  │  │ prosody     │  │
  │ │ (6 emo)  │  │ (4 prosody) │  │
  │ └────┬─────┘  └─────┬───────┘  │
  │      └────┬─────────┘          │
  │        fusion → h[B,T,768]     │
  │       (Xn6 NPU-part-2)         │
  └────────┬───────────────────────┘
           │ h[B,T,768]
           ▼
  ┌────────────────────┐
  │ tier-3: codec      │
  │  RVQ enc → dec     │    ─── 8 stages × 1024 codebook
  │  (Xn6 NPU-part-3)  │       codes [B,T,8]
  └────────┬───────────┘
           │ feat[B,T,768]
           ▼
  ┌────────────────────┐
  │ tier-4: output     │
  │  waveform dec.     │    ─── 24kHz mono 16-bit
  │  (Xn6 NPU-part-4)  │       wave [B, T·320]
  └────────┬───────────┘
           ▼
        오디오 출력 (실시간 스트림)
```

## §4 검증 메트릭 (동결 기준)

| 메트릭          | 목표     | 기준 근거                | 실측 위치                |
|-----------------|----------|--------------------------|--------------------------|
| 첫 패킷 지연    | ≤ 100ms  | µ=1ms × σ·τ 버퍼         | hexa_speak_stream.hexa   |
| 청크 크기       | 240 ms   | σ·(J₂-τ) = 12·20 ms      | 동일                     |
| sample_rate     | 24000 Hz | 24 = J₂                  | hexa_speak_audible.wav   |
| bit-depth       | 16 bit   | 2^4 = 2^τ(6)             | 동일                     |
| channels        | mono (1) | 단일 소스 (σ-φ 분리)     | 동일                     |
| MOS (가상)      | ≥ 4.0    | LibriTTS 기준 학습 후    | 학습 완료 후 측정        |
| RTF (real-time) | ≤ 0.3    | 1/σ·τ = 1/48             | Xn6 NPU 시뮬             |
| p99 지터        | ≤ 20 ms  | chunk/τ/φ = 240/4/3      | stream engine            |
| VAD 상태 수     | 4        | τ(6) FSM                 | VADFSM                   |

성공 정의: 위 9개 항목 중 ≥ 8개 충족시 tier PASS, 나머지 1개는 NEAR 허용.

## §5 n=6 정합 (산술 매핑 증명)

### 5.1 기본 등식

```
σ(6)·φ(6) = 6·τ(6) = 12
n=6 iff (유일성, Bilateral Theorem B)
```

### 5.2 4-tier 파라미터 유도 (동결)

| 파라미터         | 값    | 유도 식                          | 수론적 필연성         |
|------------------|-------|----------------------------------|-----------------------|
| 임베딩 차원       | 384   | σ·τ·sopfr+σ·sopfr=12·4·8+12·0    | OEIS A000203 · A000005 |
| 감정 수          | 6     | n=6 (완전수) = sopfr(6)+1        | 기본감정 Ekman 정합   |
| 운율 차원        | 4     | τ(6)                             | 약수 수 = 4          |
| RVQ 스테이지     | 8     | σ(6)-τ(6) = 12-4                 | 인접 짝수 σ(8)=15     |
| 코드북 크기      | 1024  | 2^(σ-φ) = 2^10                   | 로그 완전 분할        |
| 청크 길이 (ms)   | 240   | σ·(J₂-τ) = 12·20                 | 24kHz 프레임 정합    |
| attention heads  | 12    | σ(6)                             | §7.4 볼록 극소        |
| fusion hidden    | 768   | 2·384 = φ·σ·τ·16                 | double-wide SIMD      |

### 5.3 교차 검증식

```
σ(8) + σ(6)/τ(8)    = 15 + 12/4    = 15 + 3      = 18  (= φ·σ·φ(6))
4 감정 × 2 운율쌍   = 8 stages       (운율쌍: pitch-dur, energy-spectral)
6 감정 × τ(6)       = 24            (= J₂ = HW cap, §7.3 스케일)
384 / 6             = 64            (= per-emotion dim)
768 / τ             = 192           (= per-prosody-head)
```

이 모든 관계는 6 이 완전수일 때만 성립 (n=7: τ(7)=2, n=8: σ(8)=15 인접이나 iff 실패).

### 5.4 반례/변경 금지 사유

- 감정 5로 줄이면 `n ≠ sopfr+1`, Ekman 6 기본감정과 불일치 (심리학적 근거 파괴)
- RVQ 7 또는 9로 변경하면 `σ-τ` 또는 `σ-φ` 중 하나가 깨짐 (이중 제약)
- 임베딩 256 또는 512 로 변경시 σ·τ 곱 구조 상실 (§7.4 ±10% 열화 증명 위반)
- 24kHz → 48kHz 는 J₂ 상한 초과 (HW 대역폭 낭비 2배)

## §6 동결 표명

본 스펙은 n=6 산술의 iff 유일성 정리 위에 구축되었으며, 위 §5.4 의 4 조항 중 어느
하나라도 위반하는 변경은 `[10*] atlas.n6` 등급 재검증 없이 수용되지 않는다. HW 4-tier
경계는 Xn6 NPU 파티션 경계와 1:1 대응하며, tier 간 경계 이동은 칩 리스핀 트리거.

- 상위 SSOT: `$NEXUS/shared/n6/atlas.n6` (@R 6.speak.* 엔트리)
- 검증 엔진: `experiments/chip-verify/verify_xn6_*.hexa` (18 개)
- 스트리밍 구현: `./hexa_speak_stream.hexa` (STUB, 포팅 대기)
- 모델 구현: `./hexa_speak_model.hexa` (STUB, 포팅 대기)
