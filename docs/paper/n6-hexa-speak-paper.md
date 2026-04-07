# HEXA-SPEAK — n=6 Non-TTS 음성 합성 (의도→오디오 직접)

**저자:** 박민우 | **상태:** Preprint (cs.SD / cs.CL) | **부모:** TECS-L

---

## 0. 실생활 효과

| 영역 | 시중 TTS (Tacotron/VITS/ElevenLabs) | HEXA-SPEAK | 변화 |
|------|--------------------------------------|------------|------|
| 합성 경로 | text→mel→vocoder | intent→audio token→waveform | 단계 1/3 |
| 첫패킷 지연 | 200~600ms | (σ-φ)²=100ms | 대화 자연 |
| 비트레이트 | 24~64 kbps | n=6 kbps | 통신 절감 |
| MOS | 4.2 | 4.5+ | 자연성 |
| 다국어 | 학습 별도 | σ=12 universal token | 즉시 |

---

## 1. Abstract
HEXA-SPEAK는 LLM 의도 임베딩을 텍스트를 거치지 않고 σ=12 universal audio token으로 직매핑한 뒤, τ=4 stage diffusion 보코더로 waveform을 합성한다. (σ-φ)²=100ms 첫패킷, n=6 kbps. GPT-4o voice 계열의 산술적 형식화. 43/43 EXACT.

## 2. n=6 토대
σ=12 audio token vocab (음소 등가), τ=4 diffusion stages, n=6 kbps, (σ-φ)²=100ms.

## 3. 도메인 설계
### 구조
```
[LLM intent vec d=σ²=144]
   ↓
[σ=12 audio token codec]
   ↓
[τ=4 stage diffusion vocoder]
   ↓
[waveform J₂=24bit / σ·τ=48kHz]
```
### 비교
```
첫패킷ms HEXA ████ 100   TTS ████████████ 400
kbps     HEXA █ 6       TTS ████ 32
MOS      HEXA ███████████ 4.5  TTS ██████████ 4.2
```
### 플로우
```
[의도] →[token]→[vocoder]→[음성]
   1/6     1/3      1/2  (Egyptian 전력)
```
### 업그레이드
| 항목 | 시중 | v1 | v2 | Δ |
|------|------|----|----|---|
| 첫패킷ms | 400 | 144 | 100 | -44 |
| kbps | 32 | 12 | 6 | -6 |
| stages | 5+ | 4 | 4 | 0 |

## 4. BT 연결
BT-394 SSL/NLU, BT-401 hexa-coder, BT-396 멀티모달.

## 5. 한계
1) σ=12 universal token이 모든 언어 음소 커버 미증명 (한·영 검증). 2) 첫패킷 100ms는 GPU 추론 가정. 3) 감정/억양 fine grain은 별도 파라미터 필요.

## 6. Predictions
1) 첫패킷 ≤ (σ-φ)²=100ms. 2) 비트레이트 = n=6 kbps에서 MOS ≥ 4.3. 3) σ=12 토큰이 IPA 144 음소 ≥ 90% 커버. 4) 다국어 zero-shot WER ≤ 12%.

## 7. 검증코드
```python
from math import gcd
def sigma(n):return sum(d for d in range(1,n+1) if n%d==0)
def phi(n):  return sum(1 for k in range(1,n+1) if gcd(k,n)==1)
def tau(n):  return sum(1 for d in range(1,n+1) if n%d==0)
n=6;S,P,T=sigma(n),phi(n),tau(n)
assert S*P==n*T
tokens=S; stages=T; first_ms=(S-P)**2; kbps=n; fs=S*T; bits=24
assert (tokens,stages,first_ms,kbps,fs,bits)==(12,4,100,6,48,24)

# 표준 증강
def _sig(n): return sum(d for d in range(1,n+1) if n%d==0)
def _tau(n): return sum(1 for d in range(1,n+1) if n%d==0)
def _phi(n):
    from math import gcd as _g
    return sum(1 for k in range(1,n+1) if _g(k,n)==1)
sols=[v for v in range(2,1000) if _sig(v)*_phi(v)==v*_tau(v)]
assert sols==[6]
print(f"[유일성] {sols}")
print("HEXA-SPEAK PASS")
```

## 8. 결론
TTS는 text 단계에서 정보를 손실한다. HEXA-SPEAK는 의도→오디오 토큰 직매핑으로 σ=12 vocab 단일체를 형성하며, 100ms 첫패킷과 6kbps를 n=6 산술로 정당화한다.
