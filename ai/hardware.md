# Hardware

> Ultimately, the only limitation is chip real estate; space must be allocated to computation (flexible or efficient) or storage (latency or throughput).


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


### Near‑Memory Design

- Reconfigurable data‑flow hardware vs. parallelism on existing compute units.
- skew - variances of data transfer arrival time. HBM requires within 2 picoseconds variance arrival time.



> RAM size like water tank, fundamental we need match workload's compute density to hardware's compute density. RAM size just buffer enable short time of mismatch.

Increase network bandwidth, then compute density should be lower, and scale out cluster.

Each chip design with a FIXED Arithmetic Intensity, but different workload has different Arithmetic Intensity.

### Parallelism Strategies

| Strategy | Description |
|----------|-------------|
| Data Parallelism (DP) | Replicate the whole model on each GPU; split data **batches**. |
| Pipeline Parallelism (PP) | Split the model across **layers**; each GPU processes a different stage. |
| Sequence Parallelism (SP) | Partition long input **sequences** across GPUs. (very limited) |
| Tensor Parallelism (TP) | Split **individual tensor(dim)** operations across devices (often less efficient). |

- Nvidia build optimize LLM image with tp1(single GPU), tp4(split attention head in 4 GPUs)

## Networking Details

- Ethernet cable color codes: OrgWhite, Org, GreenWhite, Blue, BlueWhite, Green, BrownWhite, Brown; only pins 1,2,3,6 are used for 100 Mb/s.  
- QSFP – Quad Small Form‑factor Pluggable.  
- Fiber optics for high‑speed links.

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


## Inference Hardware

> Most inference hardware uses in‑memory compute rather than relying on external HBM.

- **Groq** – Converts PyTorch models to ONNX, then compiles for Groq ASICs.  
- **Etched**, **D‑Matrix** – Emerging inference accelerators.

## NEO Cloud Providers

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

### AMD

- Uses **HIP** to translate CUDA code to AMD GPUs.

### Intel

- intel/llm-scaler-vllm
- Dynamic auto cast LLM to int4 or fp8

### CoreWeave

- Cloud AI provider with GPU‑focused infrastructure.

### Haiwei

- Ascend 910 – Inference hardware from Huawei.
  - UE8M0 - (Unsigned Exponent, 8 bits, 0 mantissa) can only represent powers of two
  - <https://github.com/omni-ai-npu/omni-infer>

## Semiconductor

- IR Drop - `7% current drop from PSU to chip; Chip design must budget current supply.`
- Chip all 3D space all need to utilize, but at the expense of manufactory cost.
- Precision are getting smaller.
