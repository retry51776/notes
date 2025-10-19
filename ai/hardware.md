# Hardware

> Ultimately, the only limitation is chip real estate; space must be allocated to computation (flexible or efficient) or storage (latency or throughput).

## Software Stack

> Machine‑learning frameworks (e.g., PyTorch) → acceleration drivers (cuDNN) → parallel thread execution (PTX assembly) → streaming assembly (SASS machine code) → hardware (GPU).

Different hardware needs its own version of `llama.cpp` (e.g., Metal, ROCm, CUDA).

Each manufacturer has its own shading language.

### Near‑Memory Design

- Reconfigurable data‑flow hardware vs. parallelism on existing compute units.

## Memory Hierarchy

> The real bottleneck is the memory hierarchy: GPUs have limited high‑bandwidth memory (HBM or SRAM), while model parameters far exceed this capacity, forcing frequent off‑chip transfers.

- **GPU memory** hides latency by interleaving many threads. Unlike CPUs, where context switches are expensive, GPU threads are lightweight and scheduled by hardware.

### RAM Types

| Type | Description |
|------|-------------|
| DRAM (dynamic) | Capacitor‑based; includes HBM (PCIe 5 ≈ 128 GB/s, SXM ≈ 600 GB/s), DDR1‑5, LPDDR, GDDR |
| SRAM (static) | Flip‑flop based; L1/L2/L3 caches |

### Network

- CX [8, 9] Network Interface Control (NIC) uses InfiniBand; Node to Node
  - InfiniBand and RoCE NICs uses **RDMA**(looks like folder `/dev/infiniband` in Linux)
  - RoCEv2 UDP ports (typically 4791, 4790).

- NVLink [5, 6, 8]; NVLink; GPU to GPU
  - Part of /dev/nvidia; No linux exposure

Analogy: A Shipping Port with Cranes

Think of your RDMA NIC (HCA = Host Channel Adapter) as a giant shipping port.
Applications (NCCL, UCX, MPI, etc.) want to move “containers” (data) quickly from one port to another.

But applications can’t directly drive the cranes, forklifts, and trucks at the port.
Instead, the Linux kernel provides gates (device nodes in /dev/infiniband).
Each gate has a special purpose — like customs, traffic control, or the big cranes.

- **InfiniBand** – Uses Remote Direct Memory Access (RDMA) bypasses the CPU. Uses Reliable Datagram Protocol (RDP) to share Memory across BETWEEN CLUSTER.
  - NCCL (NVIDIA Collective Communications Library) - specialize protocol for GPU, open source
  - **NVSHMEM** - GPU threads directly put/get/update data in remote GPU memory without CPU involvement.

- OpenUCX (Unified Communication X) is a high-performance communication framework; Replaced **Mellanox**
  - **Unified Virtual Addressing** (UVA) - Share Memory across SINGLE NODE(Ex: a NVL72)

- **Ethernet** – Standard networking.

## Training Infrastructure

- **cuDNN**, **DeepSpeed** for large‑scale training.  
- **DGX Node**: 8 × A100 80 GB GPUs.
- **NVL72 Cluster**: 72 × B200 GPUs.
- **DGX SuperPOD**: n × NVL72 Nodes.
- **DGX Cloud**: rent DGX node level(not GPU level)

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

## Open‑Source Ecosystem

- **Exo Labs** – AI cluster management software.

## Inference Hardware

> Most inference hardware uses in‑memory compute rather than relying on external HBM.

- **Groq** – Converts PyTorch models to ONNX, then compiles for Groq ASICs.  
- **Etched**, **D‑Matrix** – Emerging inference accelerators.

## Cloud Providers

### Amazon

- **Trainium** – Custom AWS hardware compatible with CUDA.  
- **Bedrock** – Managed LLM service (works with Anthropic).

### Google

- **TPU** – Tensor Processing Units, Google’s custom AI accelerator.  
  - MXUs (Matrix Multiply Units) - aka tensor core
  - vector process unit (VPU) - aka normal math ops
  - scalar ALUs - normal CPU ops, aka control unit
  - XLA compiler
  - Toroidal mesh - `Only network to neighbor TPU, GPU is all-to-all(up to 256 GPUs)`
- **Colab** – Free notebooks with GPU/TPU access.

### Apple

- **MLX** – Efficient array framework for Apple silicon (supports 4‑ and 8‑bit).
  - MLX uses Apple GPUs, which is general purpose.
- **Core ML** – Optimized inference engine; leverages the Apple Neural Engine (ANE).
  - Neural Engine is similar to Tensor Core, only does matrix ops
  - VERY few frameworks uses Neural Engine, almost pointless to have it
- **vllm** <https://medium.com/@rohitkhatana/installing-vllm-on-macos-a-step-by-step-guide-bbbf673461af>

> The ANE is not directly accessible from MLX or PyTorch.

### AMD

- Uses **HIP** to translate CUDA code to AMD GPUs.

### CoreWeave

- Cloud AI provider with GPU‑focused infrastructure.

### Haiwei

- Ascend 910 – Inference hardware from Huawei.
  - UE8M0 - (Unsigned Exponent, 8 bits, 0 mantissa) can only represent powers of two
  - <https://github.com/omni-ai-npu/omni-infer>

## NVIDIA Ecosystem

> the entire product line includes:

- **GeForce** – Consumer gaming GPUs.  
- **Quadro** – Professional workstations.  
- **DGX / HGX** – AI‑focused servers (e.g., DGX A100, HGX H100).
  - H100 units cost at least $30k; DGX has 8×H100
- **Jetson** – Edge AI and robotics.  
- **Tegra** – Embedded/mobile GPUs.

### GPU Architecture Components

| Component | Role |
|-----------|------|
| CUDA Core | General‑purpose compute unit |
| Tensor Core | Matrix multiplication (FP16/INT8) |
| RT Core | Ray tracing |
| Raster Unit | Vector → pixel conversion |
| Texture Unit | Apply textures to geometry |
| Memory | GDDR5/6/6X, HBM2/2E |
| NVLink | High‑speed GPU‑to‑GPU interconnect |
| NVENC / NVDEC | Video encode/decode |

> Note: Tensor Core CAN'T tokenization, softmax scaling, KV cache indexing, and sampling, which still operate on floating point in CUDA Core;

### Training Tools

- **AI Enterprise** – On Prem DGX Cloud.
- **DGX Cloud** – NVIDIA’s AI suite. `Alternative to AWS, GPC, Azure` `https://build.nvidia.com/explore/discover`
  - **NVIDIA NIM** – Inference micro‑services.  `similar to ollama; But NIM has different docker image for audio/image/video/biology service too`
    - **Triton Inference Server**
      - vllm (default engine)
      - **TensorRT**
      - sglang
  - **NVIDIA NeMo** – Model training framework.

## Management Controllers

- BMC – Baseboard Management Controller (motherboard management).  
- QSFP – High‑speed optical/electrical interface.

## CUDA Programming Concepts

- **Grid** – Collection of blocks; can be 1‑3 dimensions.  
- **Block** – Up to 1024 threads; also 1‑3 dimensions.  
- **Warp** – 32 threads executed in lockstep.  
- Unified Virtual Addressing (UVA) - Share Memory across SINGLE NODE(Ex: a NVL72)

```
# Developer perspective
Grid (many Blocks)
 ├─ Block 0 (1024 Threads) → assigned to a single SM
 │   ├─ Warp 0 (32 Threads)
 │   └─ …
 ├─ Block 1 (many Threads)
 └─ Block N
```

- **SM** – Streaming Multiprocessor; contains CUDA cores, Tensor Cores, warp schedulers, SFUs, load/store units, L1 cache & shared memory.  
- **L2 Cache** – Shared across SMs; large but slower than L1.  
- **Global Memory** – HBM or GDDR attached to the GPU.

## NVIDIA Software Stack

- **AI Enterprise** → OS (Ubuntu + drivers) → Tools (Base Command, Base Command Manager, Suit Command).  
- **NGC** – NVIDIA GPU Cloud for containers and pre‑built images.  
- **HGX** – High‑performance GPU servers (e.g., Dell PowerEdge R750xa, HPE ProLiant DL380 Gen10, Lenovo SR670, Supermicro SYS‑420GP).````

ai/code.md
