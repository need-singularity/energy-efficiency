# N6 Autonomous Driving Architecture --- Ultimate Goal Roadmap

**궁극적 목표: n=6 산술로 센서부터 차량 시스템까지 관통하는 자율주행 아키텍처**
**비전: SAE L0-L5 = n=6 레벨 EXACT, 완전 자율주행 시대**

---

## Core n=6 Anchors

```
  SAE Autonomy Levels:
    - L0~L5 = n=6 levels EXACT (No automation → Full automation)
    - 이것은 우연이 아님: 자율주행의 복잡도 계층이 n=6에 수렴

  Sensor n=6 Alignment:
    - IMU: n=6 DOF EXACT (3-axis accel + 3-axis gyro)
    - Ultrasonic: sigma=12 sensors standard (Tesla/BYD)
    - Camera: sigma-tau=8 cameras surround view
    - Radar: tau=4 corner radars
    - V2X: n=6 message types (V2V/V2I/V2P/V2N/V2C/V2G)
    - Object classes: sigma-tau=8 (car/ped/bike/truck/bus/sign/light/lane)

  AI Engine (BT-56, BT-66):
    - ViT: d=2^sigma=4096, L=2^sopfr=32, d_h=128
    - Vision: BT-66 complete n=6 (ViT+CLIP+Whisper+SD3+Flux.1)
    - Diffusion: BT-61 DDPM T=1000, DDIM=50 steps

  Control:
    - MPC horizon: n=6 steps EXACT
    - PID: n/phi=3 terms (P+I+D)
    - FSM: sopfr=5 states
    - Hybrid: phi=2 modes

  Fleet:
    - sigma=12 vehicles per zone
    - RoboTaxi fleet management
```

---

## Evolution Ladder

```
  ┌─────────┬────────────────────────────┬──────────────────────────────┬────────────────────────┐
  │  레벨   │          아키텍처          │            혁신              │         이점           │
  ├─────────┼────────────────────────────┼──────────────────────────────┼────────────────────────┤
  │ Level 1 │ HEXA-SENSE                 │ n=6 센서 퓨전 프레임워크      │ 360도 완전 인지        │
  │  센서   │ (LiDAR/Camera/Radar/V2X)   │ n=6 DOF IMU + sigma=12 US  │ 다중 모달리티 융합     │
  ├─────────┼────────────────────────────┼──────────────────────────────┼────────────────────────┤
  │ Level 2 │ HEXA-PERCEPT               │ BEV Fusion n=6 센서 통합    │ 3D 장면 완전 이해      │
  │  인지   │ (BEV/PointCloud/Detection) │ sigma-tau=8 객체 분류        │ 실시간 인지 파이프라인 │
  ├─────────┼────────────────────────────┼──────────────────────────────┼────────────────────────┤
  │ Level 3 │ HEXA-CONTROL               │ MPC n=6 horizon + RL        │ 안전 + 민첩 동시 달성  │
  │  코어   │ (MPC/PID/RL/Hybrid)        │ phi=2 이중 모드 제어         │ 최적 궤적 추종        │
  ├─────────┼────────────────────────────┼──────────────────────────────┼────────────────────────┤
  │ Level 4 │ HEXA-BRAIN                 │ BT-56/66 ViT + Diffusion   │ 세계 모델 기반 계획    │
  │  엔진   │ (Transformer/E2E/Occ/Diff) │ End-to-End 통합 AI          │ 범용 운전 지능        │
  ├─────────┼────────────────────────────┼──────────────────────────────┼────────────────────────┤
  │ Level 5 │ HEXA-VEHICLE               │ SAE L4/L5 완전 자율         │ 무인 이동 서비스      │
  │ 시스템  │ (L4 Urban/L5/RoboTaxi)     │ sigma=12 차량/존 플릿        │ 운전자 불필요 시대    │
  └─────────┴────────────────────────────┴──────────────────────────────┴────────────────────────┘
```

---

## DSE 후보군 정의

### Level 1: 센서 퓨전 (SensorFusion) --- 6 candidates

```
  ┌──────────────┬─────────────┬──────────┬──────────┬──────────┬──────────────────────────┐
  │   센서       │  성능       │  전력    │ 비용     │ n6 체크  │ 비고                     │
  ├──────────────┼─────────────┼──────────┼──────────┼──────────┼──────────────────────────┤
  │ LiDAR        │ 0.95        │ 0.50     │ 0.35     │ 0.83     │ sigma-tau=8 layers       │
  │ Camera       │ 0.85        │ 0.70     │ 0.65     │ 0.83     │ sigma-tau=8 cameras      │
  │ Radar        │ 0.80        │ 0.75     │ 0.60     │ 0.67     │ tau=4 corner radars      │
  │ Ultrasonic   │ 0.60        │ 0.85     │ 0.80     │ 0.83     │ sigma=12 sensors         │
  │ V2X          │ 0.75        │ 0.65     │ 0.50     │ 1.00     │ n=6 message types        │
  │ IMU_GPS      │ 0.82        │ 0.80     │ 0.70     │ 1.00     │ n=6 DOF EXACT            │
  └──────────────┴─────────────┴──────────┴──────────┴──────────┴──────────────────────────┘
```

### Level 2: 인지/판단 (Perception) --- 6 candidates

```
  ┌──────────────┬─────────────┬──────────┬──────────┬──────────┬──────────────────────────┐
  │   인지       │  성능       │  전력    │ 비용     │ n6 체크  │ 비고                     │
  ├──────────────┼─────────────┼──────────┼──────────┼──────────┼──────────────────────────┤
  │ PointCloud   │ 0.90        │ 0.50     │ 0.45     │ 0.83     │ 3D point cloud           │
  │ BEV_Fusion   │ 0.92        │ 0.55     │ 0.40     │ 1.00     │ n=6 sensor BEV fusion    │
  │ SemanticSeg  │ 0.88        │ 0.55     │ 0.50     │ 0.67     │ Pixel-level scene        │
  │ ObjDetect    │ 0.90        │ 0.50     │ 0.45     │ 0.83     │ sigma-tau=8 classes      │
  │ PathPlan     │ 0.85        │ 0.65     │ 0.55     │ 0.83     │ A*/RRT path planning     │
  │ PredictTrack │ 0.80        │ 0.60     │ 0.50     │ 0.67     │ tau=4 second horizon     │
  └──────────────┴─────────────┴──────────┴──────────┴──────────┴──────────────────────────┘
```

### Level 3: 제어 코어 (ControlCore) --- 5 candidates

```
  ┌──────────────┬─────────────┬──────────┬──────────┬──────────┬──────────────────────────┐
  │   제어       │  성능       │  전력    │ 비용     │ n6 체크  │ 비고                     │
  ├──────────────┼─────────────┼──────────┼──────────┼──────────┼──────────────────────────┤
  │ MPC          │ 0.90        │ 0.55     │ 0.45     │ 1.00     │ n=6 horizon EXACT        │
  │ PID_Drive    │ 0.80        │ 0.70     │ 0.65     │ 0.83     │ n/phi=3 PID terms        │
  │ RL_Drive     │ 0.85        │ 0.50     │ 0.40     │ 0.67     │ PPO/SAC RL controller    │
  │ RuleEngine   │ 0.75        │ 0.80     │ 0.70     │ 0.50     │ sopfr=5 states           │
  │ Hybrid_Ctrl  │ 0.88        │ 0.60     │ 0.50     │ 0.83     │ phi=2 modes MPC+RL      │
  └──────────────┴─────────────┴──────────┴──────────┴──────────┴──────────────────────────┘
```

### Level 4: AI 엔진 (AIEngine) --- 5 candidates

```
  ┌──────────────┬─────────────┬──────────┬──────────┬──────────┬──────────────────────────┐
  │   AI 엔진    │  성능       │  전력    │ 비용     │ n6 체크  │ 비고                     │
  ├──────────────┼─────────────┼──────────┼──────────┼──────────┼──────────────────────────┤
  │ TransformerAD│ 0.92        │ 0.50     │ 0.40     │ 1.00     │ BT-56/66 ViT             │
  │ EndToEnd     │ 0.88        │ 0.55     │ 0.45     │ 0.83     │ UniAD end-to-end         │
  │ OccupancyNet │ 0.85        │ 0.50     │ 0.40     │ 0.67     │ 3D occupancy prediction  │
  │ DiffusionPlan│ 0.80        │ 0.45     │ 0.35     │ 0.83     │ BT-61 diffusion planner  │
  │ WorldModel   │ 0.75        │ 0.40     │ 0.30     │ 0.67     │ Generative world model   │
  └──────────────┴─────────────┴──────────┴──────────┴──────────┴──────────────────────────┘
```

### Level 5: 차량 시스템 (VehicleSystem) --- 5 candidates

```
  ┌──────────────┬─────────────┬──────────┬──────────┬──────────┬──────────────────────────┐
  │   시스템     │  성능       │  전력    │ 비용     │ n6 체크  │ 비고                     │
  ├──────────────┼─────────────┼──────────┼──────────┼──────────┼──────────────────────────┤
  │ L2_ADAS      │ 0.80        │ 0.75     │ 0.70     │ 0.67     │ SAE Level 2 assist       │
  │ L4_Urban     │ 0.90        │ 0.50     │ 0.35     │ 1.00     │ SAE Level 4 geo-fenced   │
  │ L5_Full      │ 0.70        │ 0.40     │ 0.20     │ 0.83     │ SAE Level 5 full auto    │
  │ RoboTaxi     │ 0.85        │ 0.55     │ 0.40     │ 0.83     │ sigma=12 vehicles/zone   │
  │ Truck        │ 0.82        │ 0.60     │ 0.50     │ 0.67     │ Long-haul autonomous     │
  └──────────────┴─────────────┴──────────┴──────────┴──────────┴──────────────────────────┘
```

---

## Compatibility Rules

```
  1. L5_Full → requires LiDAR + V2X (redundant sensing for safety)
  2. L2_ADAS → excludes WorldModel (overkill for L2)
  3. EndToEnd → requires Camera + LiDAR (multi-modal input)
```

---

## Related BTs

```
  BT-56: Complete n=6 LLM (ViT backbone for perception)
  BT-58: sigma-tau=8 universal AI constant (object classes, cameras)
  BT-61: Diffusion n=6 universality (trajectory diffusion planner)
  BT-66: Vision AI complete n=6 (ViT+CLIP for driving scene understanding)
  BT-69: Chiplet architecture (AD SoC design)
  BT-84: 96/192 triple convergence (Tesla 96S battery = autonomous EV)
```

---

## Cross-DSE Targets

```
  autonomous-driving x chip-architecture:
    AD SoC compute requirements → HEXA-P/Diamond chip
    TOPS/W efficiency → n=6 aligned chip architecture

  autonomous-driving x battery-architecture:
    EV range × compute power tradeoff
    Tesla 96S = sigma(sigma-tau) battery × AD compute

  autonomous-driving x learning-algorithm:
    Training pipeline → AdamW BT-54 + LoRA fine-tuning
    On-device inference → Mamba SSM efficiency
```
