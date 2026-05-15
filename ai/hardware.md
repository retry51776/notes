# Hardware

> Ultimately, the only limitation is chip real estate; space must be allocated to computation (flexible or efficient) or storage (latency or throughput).

Inference's hardware requirement is way lower than training. Nvidia is king of training.

AI workload similar to drink(compute) water(data) from cup(HBM) through straw(SRAM).

## Pitfall

- 30% GPU & NVLink failures
- 17% HBM memory
- 53% network & software

## Runtime Stack

> Machine‑learning frameworks (e.g., PyTorch) → Intermediate Representation(IR/compute graph) → Kernel (different subset CUDA/cuDNN/FlashInfer) → parallel thread execution (PTX assembly) → streaming assembly (SASS machine code) → hardware (GPU).

Different hardware needs its own version of `llama.cpp` (e.g., Metal, ROCm, CUDA).

Each manufacturer has its own shading language.

Open‑Source Ecosystem:

- **Exo Labs** – AI cluster management software.

## Memory

> The real bottleneck is the memory hierarchy: GPUs have limited high‑bandwidth memory (HBM or SRAM), while model parameters far exceed this capacity, forcing frequent off‑chip transfers.

- Arithmetic Intensity | Compute Density ~ Compute / Data @ FB16
  - Workload
    - Attention ~ 10–50 FLOPs/byte
    - GEMM / MLP ~ 100–1000+ FLOPs/byte
    - decode ~ 1–10 FLOPs/byte
  - Hardware
    - H100 FP16 ~ 300 FLOPs/byte
    - Groq ~ 3 - 8 FLOPs/byte

- RAM Flush speed ~ IO / capacity
  - NAND ~ seconds to minutes
  - DR5 ~ 0.2–0.5× / sec
  - HBM3 ~ 10–20× / sec
  - HBM4 ~ 30× / sec
  - SRAM ~ 300k / sec


- **GPU memory** hides latency by interleaving many threads. Unlike CPUs, where context switches are expensive, GPU threads are lightweight and scheduled by hardware.

### RAM Types

| Type | Description |
|------|-------------|
| SRAM (static) | Flip‑flop based; L1/L2/L3 caches |
| DRAM (dynamic) | Capacitor‑based; includes HBM (PCIe 5 ≈ 128 GB/s, SXM ≈ 600 GB/s), DDR1‑5, LPDDR, GDDR |

- DRAM
  - Low Power DDR (LPDDR)
  - Dual In-line Memory Module (DIMM) `common PCIe`
  - LPCAMM2 - laptop screw in RAM

  - STX support Context Memory Storage (CMX)
    - Small Outline Compact Advanced Memory Module (SOCAMM) * 64 @ 256GB ~ LPDDR with BlueField @ 120G/s for CPU `similar to cpu pins (694), but screw on`
      - start from GB300

Analogy:

- compute ~ drink water
  - CPU ~ drink through straw
    - DDR ~ water tank
  - GPU w HBM ~ drink through many straw
    - GDDR ~ water tank with more flow
    - HBM ~ water towers (stacked up water tanks)
    - SRAM ~ water cup
- Data ~ water
- bandwidth ~ throughput
- NV speed of light ~ max Arithmetic Intensity

### Near‑Memory Design

- Reconfigurable data‑flow hardware vs. parallelism on existing compute units.
- skew - variances of data transfer arrival time. HBM requires within 2 picoseconds variance arrival time.


Each chip design with a FIXED Arithmetic Intensity, but different workload has different Arithmetic Intensity.

Hardware Model codesign
- Gate Count
- Gate Size
- Energy Cost
- LLM Intelligent per jew

### Parallelism Strategies

| Strategy | Description |
|----------|-------------|
| Data Parallelism (DP) | Replicate the whole model on each GPU; split data **batches**. |
| Pipeline Parallelism (PP) | Split the model across **layers**; each GPU processes a different stage. |
| Sequence Parallelism (SP) | Partition long input **sequences** across GPUs. (very limited) |
| Tensor Parallelism (TP) | Split **individual tensor(dim)** operations across devices (often less efficient). |

- Nvidia build optimize LLM image with tp1(single GPU), tp4(split attention head in 4 GPUs)


## Performance Optimizations

| Optimization | Key Idea | Benefit |
|--------------|----------|---------|
| Tensor Cores | Use FP16/INT8 for matrix ops | 10–20× speedup |
| Memory Coalescing | Align memory accesses | Reduces latency |
| Kernel Fusion | Merge multiple kernels | Lowers launch overhead |
| FlashAttention | Blockwise attention computation | Saves memory, speeds inference |
| Lower Precision (FP16/INT8/FP8) | Reduce data size | Faster compute, less memory |
| Persistent Kernels | Keep threads alive | Cuts scheduling cost |
| CUDA Graphs | Pre‑record kernel launches | Avoids CPU bottlenecks |
| Multi‑token Decoding | Predict several tokens at once | Increases generation speed |

- superkernel - reduce kernel swap by multi ops
- microbatch - split training batch into smaller batches
- flashcomm
- compiler cache - kernel re-use
- MTP - Multi-Token Prediction
- Placement Driver (PD) dispatcher

- all-reduce operation - sync local gradient for global gradients.
- Activation Checkpoint - recompute activation every n layers when back props.

- Thread Block Clusters - multiple SMs works on same SRAM
- Stationary Data/Array - in-place execution data
- Very Long Instruction Word (VLIW) - Compiler optimization
- Threadgroup walk order - increase cache hit rate(because x,y index increase slowly)



## NEO Cloud Providers

https://substackcdn.com/image/fetch/$s_!vOm0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe347a756-d864-4e1b-983e-9bde22c34e53_1024x479.png


### Amazon & Anthropic

- **Trainium** – Custom AWS hardware compatible with CUDA.
- **Bedrock** – Managed LLM service (works with Anthropic).
  - Haiku（最小最快）
  - Sonnet（中间档）
  - Opus（最大最强）三档
  - Capybara/Mythos ?


### Google

- **TPU** – Tensor Processing Units, Google’s custom AI accelerator.
  - MXUs (Matrix Multiply Units) - aka tensor core
  - vector process unit (VPU) - aka normal math ops
  - scalar ALUs - normal CPU ops, aka control unit
  - Optical Circuit Switch (OCS) `aka programmable TPUs neighbor/network communication`
  - Cube ~ Node 4x4x4 = 64 TPUs
    - each Cude has 6 Faces, each Face connects another Cude's face through OCS
  - XLA compiler `aka CUDA for TPU`
  - Toroidal mesh - `Only network to neighbor TPU, GPU is all-to-all(up to 256 GPUs)`
  - 1.2 TB/s between TPUs @ v7 @ max 9,216 chips
  - Differences to Nvidia GPU
    - No warp schedulers
    - No thread switching hardware
- **Colab** – Free notebooks with GPU/TPU access.

### Apple

Metal Performance Primitives / TensorOps
└── Metal Performance Shaders
    └── MPSGraph
        ├── PyTorch-Metal
        ├── CoreML
        │   └── MetalFX
        └── (others)

- **MLX** – Efficient array framework for Apple silicon (supports 4‑ and 8‑bit).
  - MLX uses Apple GPUs, which is general purpose.
  - mlx[cuda] compiled into CUDA api for CUDA runtime
  - https://github.com/ml-explore/mlx-lm/tree/main/mlx_lm/models defined supported models
- **Core ML** – Optimized inference engine; leverages the Apple Neural Engine (ANE).
  - Neural Engine is similar to Tensor Core, only does matrix ops
  - VERY few frameworks uses Neural Engine, almost pointless to have it
- **vllm** <https://medium.com/@rohitkhatana/installing-vllm-on-macos-a-step-by-step-guide-bbbf673461af>

Instruments ~ Apple Metal Trace software

Apple GPU components:

- Shader Core ~ SM
- SIMDgroup ~ Warp
- Threadgroup ~ Thread Block
- M5's Neural accelerator ~ tensor core
  - GPU -> DRAM -> NPU -> DRAM -> GPU; slow, not on SRAM.
- ALU (int/fp/complex) ~ ALU

> The ANE is not directly accessible from MLX or PyTorch.

Known Bugs:

- LIBP2P's MDNS in mac os broken

### AMD

- Uses **HIP** to translate CUDA code to AMD GPUs.

### Intel

- intel/llm-scaler-vllm
- Dynamic auto cast LLM to int4 or fp8

### CoreWeave

- Cloud AI provider with GPU‑focused infrastructure.

### Haiwei

- Atlas cluster
  - UnifiedBus ~ NVLink Fabric
- Ascend(升腾) – Inference hardware from Huawei.
  - 910DT | 950DT
    - UE8M0 - (Unsigned Exponent, 8 bits, 0 mantissa) can only represent powers of two
    - hierarchy scale: 8 group 128 group
    - <https://github.com/omni-ai-npu/omni-infer>
- Software
  - Ascend C (Cuda alternative)
    - `EnQue` \ `DeQue` move data
  - TileLang-Ascend
  - CANN (CuDNN alternative) pre-optimized library


Support TorchTitan

### 寒武纪

- 思元（Siyuan）系列（如 590 / 690）
  - vLLM runtime compatibility

### Inference Acceleration Companies

- Groq - SRAM on weaver
- Etched - ASIC
- SambaNove
- PositronAI - Visual hardware
- Tenstorrent - RISK V

## Semiconductor

- IR Drop - `7% current drop from PSU to chip; Chip design must budget current supply.`
- Chip all 3D space all need to utilize, but at the expense of manufactory cost.
- Precision are getting smaller.


## Benchmark

- Dylan's InferenceMax Total Cost Ownership
- MLCommons's MLPerf
  - https://mlcommons.org/benchmarks/inference-datacenter/