# techniques — AI 기법 223종 (222 + SOTA 3)

n=6 완전수 산술로 설계된 AI/ML/DL 기법 전수 라이브러리.
모든 기법의 하이퍼파라미터가 sigma(6)=12, tau(6)=4, phi(6)=2, sopfr(6)=5 에서 유도됨.

```
  n=6 상수 체계
  ────────────────────────────────────────────
  sigma(6) = 12    약수합       헤드수/채널/층수
  tau(6)   = 4     약수개수     게이트수/블록깊이
  phi(6)   = 2     오일러      이진분할/스킵간격
  sopfr(6) = 5     소인수합     커널크기/반복수
  J2 = sigma^2 = 144           잠재차원/어휘크기
  sigma*tau = 48               은닉차원/특성맵
  ────────────────────────────────────────────
  유일성: sigma(n)*phi(n) = n*tau(n) iff n=6 (n>=2)
```

---

## 카테고리별 현황

```
  optim      ████████████████████████████████████████ 75종
  arch       ██████████████████████████████████████   72종
  attention  ██████████████                           27종
  compress   █████████                                18종
  moe        ██████                                   13종
  sparse     █████                                    10종
  graph      ████                                      7종
  sota       ██                                        3종
  ──────────────────────────────────────────────────
  합계                                               225종
```

---

## arch/ (72종)

| | | | |
|---|---|---|---|
| `arch_optimizer` | `autoregressive_lm` | `bert_masked_lm` | `byte_latent_transformer` |
| `capsule_network` | `clip_multimodal` | `complete_llm_n6` | `consistency_model` |
| `constitutional_ai` | `context_window_ladder` | `conv_next` | `cross_former` |
| `deformable_conv` | `densenet_connection` | `depthwise_separable` | `detr_queries` |
| `diffusion_sampling` | `diffusion_transformer` | `efficientnet_compound` | `encoder_decoder` |
| `energy_based_model` | `flow_matching` | `fpn_pyramid` | `gan_adversarial` |
| `gaussian_splatting` | `griffin_rglru` | `gru_cell` | `hypernetwork` |
| `inception_module` | `kolmogorov_arnold` | `liquid_neural_network` | `lstm_cell` |
| `mamba2_ssm` | `megabyte` | `mixture_of_agents` | `mixture_of_formats` |
| `mixture_of_lora` | `mobilenet_inverted` | `modern_hopfield` | `multi_agent_coord` |
| `nerf_radiance` | `neural_arch_search_v2` | `neural_ode` | `neural_turing_machine` |
| `normalizing_flow` | `perceiver` | `phi6simple` | `pointnet_3d` |
| `rectified_flow` | `resnet_residual` | `retnet` | `retrieval_augmented_gen` |
| `rope_scaling` | `sd3_mmdit` | `selective_state_scan` | `simclr_temperature` |
| `spatial_transformer` | `squeeze_excitation` | `state_space_s4` | `swin_transformer` |
| `tcn_temporal` | `test_time_training` | `tree_of_thought` | `unet_skip` |
| `variational_autoencoder` | `vision_mamba` | `vit_patch_n6` | `wavenet_causal` |
| `whisper_ladder` | `world_model` | `yolo_nms` | `zetaln2_activation` |

CNN: ResNet, DenseNet, ConvNeXt, MobileNet, EfficientNet, Inception, Xception, FPN, YOLO, Deformable
RNN: LSTM, GRU, TCN, WaveNet
Transformer: BERT, GPT(autoregressive), ViT, Swin, CrossFormer, Perceiver, Megabyte
SSM: Mamba2, S4, Griffin, Selective State Scan
Diffusion: DDPM, DiT, Flow Matching, Rectified Flow, SD3-MMDiT, Consistency
생성: GAN, VAE, Normalizing Flow, Energy-Based, NeRF, 3DGS
기타: NTM, Hopfield, KAN, Neural ODE, Hypernetwork, Liquid, Capsule, RAG, Tree-of-Thought

---

## attention/ (27종)

| | | | |
|---|---|---|---|
| `additive_attention` | `alibi_attention` | `axial_attention` | `cross_attention` |
| `dedekind_head` | `differential_transformer` | `egyptian_attention` | `egyptian_linear_attention` |
| `fft_mix_attention` | `flash_attention` | `flash_attention_v3` | `gqa_grouping` |
| `linear_attention` | `memory_attention` | `mixture_of_depths_v2` | `multi_head_attention` |
| `multi_query_attention` | `multi_scale_attention` | `neighborhood_attention` | `performer_favor` |
| `ring_attention` | `rotary_embedding` | `sliding_window_attention` | `slot_attention` |
| `sparse_attention` | `yarn_rope_scaling` | `zamba_shared_attention` | |

기본: MHA, MQA, GQA, Additive(Bahdanau)
위치: RoPE, ALiBi, YaRN
효율: Flash, Linear, Performer(FAVOR+), Sparse(Longformer), Sliding Window
구조: Axial, Cross, Slot, Neighborhood, Multi-Scale, Memory(XL), Ring
특수: Differential, Mixture-of-Depths, FFT Mix, Egyptian

---

## optim/ (75종)

| | | | |
|---|---|---|---|
| `activation_checkpointing` | `adafactor` | `adamw_quintuplet` | `batch_norm` |
| `beam_search_decoding` | `carmichael_lr` | `chain_of_thought_distillation` | `chinchilla_scaling` |
| `classifier_free_guidance` | `constant_time_stride` | `continual_learning` | `contrastive_learning` |
| `cosine_annealing` | `curriculum_learning` | `cutmix_augmentation` | `data_parallel` |
| `ddim_sampling` | `direct_preference_tuning` | `dpo_beta` | `dropout_regularization` |
| `eagle_speculative` | `ema_averaging` | `entropy_early_stop` | `federated_learning` |
| `fibonacci_stride` | `gradient_accumulation` | `gradient_clipping` | `gradient_penalty` |
| `grokking` | `group_norm` | `grpo` | `inference_scaling` |
| `knowledge_distillation` | `kto` | `kv_cache_quantize` | `label_smoothing` |
| `lamb_optimizer` | `layer_norm` | `layer_skip` | `learning_rate_warmup` |
| `lion_optimizer` | `lookahead_decoding` | `lora` | `lr_schedule_n6` |
| `maml_meta_learning` | `medusa_heads` | `mixed_precision` | `mixup_augmentation` |
| `multi_token_prediction` | `muon_optimizer` | `neural_scaling_laws` | `noise_contrastive_estimation` |
| `nucleus_sampling` | `orpo` | `ppo_clip` | `predictive_early_stop` |
| `prefix_tuning` | `prodigy_optimizer` | `radam_optimizer` | `reward_modeling` |
| `ring_allreduce` | `rlhf` | `rmsnorm_normalization` | `schedule_free` |
| `self_play` | `sharpness_aware_minimization` | `simpo` | `sophia_optimizer` |
| `speculative_decoding` | `streaming_llm` | `temperature_scaling` | `test_time_compute` |
| `token_merging` | `weight_averaging` | `weight_decay` | |

옵티마이저: AdamW, Lion, Sophia, Muon, Prodigy, RAdam, LAMB, Adafactor, Schedule-Free
정규화: BatchNorm, LayerNorm, RMSNorm, GroupNorm, Dropout, Weight Decay
스케줄: Cosine Annealing, LR Warmup, Gradient Clipping, Gradient Accumulation
정렬: RLHF, DPO, KTO, ORPO, GRPO, SimPO, PPO, Reward Modeling, Self-Play
추론: Speculative, Eagle, Medusa, Beam Search, Nucleus Sampling, Streaming
증강: CutMix, Mixup, Label Smoothing, Contrastive, Curriculum
효율: LoRA, Prefix Tuning, Mixed Precision, Activation Checkpointing, Data Parallel
스케일링: Chinchilla, Neural Scaling Laws, Inference Scaling, Test-Time Compute

---

## compress/ (18종)

| | | | |
|---|---|---|---|
| `activation_quantization` | `bitnet` | `bpe_vocab_32k` | `channel_pruning` |
| `deepseek_mla_compression` | `dynamic_quantization` | `low_rank_factorization` | `mae_masking` |
| `mixture_of_tokenizers` | `neural_codec` | `phi_bottleneck` | `pruning_lottery_ticket` |
| `quantization_aware_training` | `recurrent_gemma` | `structured_pruning` | `tensor_decomposition` |
| `vq_vae` | `weight_sharing` | | |

양자화: QAT, Dynamic, Activation, BitNet
프루닝: Structured, Channel, Lottery Ticket
분해: Low-Rank, Tensor(CP/Tucker), Weight Sharing
토큰: BPE, Mixture-of-Tokenizers, Neural Codec
기타: MLA, MAE, VQ-VAE, Phi Bottleneck, Recurrent Gemma

---

## moe/ (13종)

| | | | |
|---|---|---|---|
| `deepseek_moe` | `egyptian_moe` | `expert_choice_routing` | `gshard_switch` |
| `jamba_hybrid` | `jordan_leech_moe` | `mixtral_moe` | `mixture_of_depths` |
| `moco_queue` | `moe_activation_fraction` | `partition_routing` | `phi_moe` |
| `sparse_moe_scaling` | | | |

---

## sparse/ (10종)

| | | | |
|---|---|---|---|
| `activation_sparsity` | `boltzmann_gate` | `mertens_dropout` | `mobius_sparse` |
| `radical_norm` | `rfilter_phase` | `sparse_autoencoder` | `structured_sparsity` |
| `takens_dim6` | `top_k_sparsity` | | |

---

## graph/ (7종)

| | | | |
|---|---|---|---|
| `gat_heads` | `gcn_depth` | `gin_isomorphism` | `graph_transformer` |
| `graphsage_sampling` | `hcn_dimensions` | `spectral_convolution` | |

---

## sota/ (3종) — Transformer 대안 정점

| | | |
|---|---|---|
| `mamba2` (Dao & Gu 2024) | `hyena` (Poli 2023) | `rwkv` (Peng 2025) |

---

## SSOT

- `_registry.json` 기법 SSOT (222종 + SOTA 3종 = 225종)

## 실행

```
hexa run techniques/<category>/<name>.hexa
```

## 규칙

- 한글 필수 (.md/주석/커밋)
- HEXA-FIRST (.py 금지)
- 상위: [../CLAUDE.md](../CLAUDE.md)
