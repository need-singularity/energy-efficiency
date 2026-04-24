# HEXA-SPEAK Prototype

Pure-numpy implementation. PyTorch / TensorFlow not required.

## Files

- **`hexa_speak_model.py`** — model architecture (all 43 parameters applied)
  - `IntentConditioner` — fuses intent + emotion + prosody + voice_id
  - `DecoderLayer` — Multi-head attention + FFN (sigma=12 heads, tau=4 FFN expansion)
  - `AudioTokenPredictor` — 3-layer Transformer -> RVQ logits
  - `RVQDecoder` — 8-stage codebook lookup -> waveform synthesis
- **`hexa_speak_stream.py`** — real-time streaming pipeline
  - `VADFSM` — tau=4 state machine (SILENT/STARTING/SPEAKING/TRAILING)
  - `RingBuffer` — 240 ms = sigma*(J2-tau) buffer
  - `StreamingEngine` — chunk scheduler + crossfade + PLC
- **`hexa_speak_demo.wav`** — generated sample audio (24 kHz, mono, 16-bit)

## Run

```bash
# Architecture check (shape + forward pass)
python3 hexa_speak_model.py

# Streaming + WAV generation
python3 hexa_speak_stream.py
```

## Verification metrics (measured)

| Metric | Target | Measured | Status |
|--------|--------|----------|--------|
| First-packet latency | <=100 ms | 19.9 ms | OK (5x margin) |
| sample_rate | 24000 Hz | 24000 Hz | OK |
| bits | 16 | 16 | OK |
| channels | mono (1) | 1 | OK |
| hidden dim | 768 | 768 | OK |
| attention heads | 12 (sigma) | 12 | OK |
| RVQ stages | 8 (sigma-tau) | 8 | OK |
| codebook | 1024 (2^(sigma-phi)) | 1024 | OK |
| chunk = sigma frames | 240 ms | 240 ms | OK |
| VAD states | 4 (tau) | 4 | OK |

## Limitations (untrained)

- Weights are **randomly initialized** (not trained)
- Generated speech is at noise level
- Real linguistic quality requires **training the model on a large corpus**

## Next steps (Mk.I real implementation draft)

1. Port to PyTorch (GPU training)
2. Train on LibriTTS / Common Voice datasets
3. Swap in an EnCodec-compatible decoder (reuse pretrained weights)
4. Measure real-world latency (validate 100 ms boundary)
