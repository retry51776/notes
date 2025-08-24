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

- **Unified Virtual Addressing** (UVA) - Share Memory across SINGLE NODE(Ex: a NVL72)

- **InfiniBand** – Uses Remote Direct Memory Access (RDMA) bypasses the CPU. Uses Reliable Datagram Protocol (RDP) to share Memory across BETWEEN CLUSTER.  
- **Ethernet** – Standard networking.

## Training Infrastructure

- **cuDNN**, **DeepSpeed** for large‑scale training.  
- **DGX Node**: 8 × A100 80 GB GPUs.
- **NVL72 Cluster**: 72 × B200 GPUs.
- **DGX SuperPOD**: n × NVL72 Nodes.

### Parallelism Strategies

| Strategy | Description |
|----------|-------------|
| Data Parallelism (DP) | Replicate the whole model on each GPU; split data batches. |
| Pipeline Parallelism (PP) | Split the model across layers; each GPU processes a different stage. |
| Sequence Parallelism (SP) | Partition long input sequences across GPUs. |
| Tensor Parallelism (TP) | Split individual tensor operations across devices (often less efficient). |

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
- **Colab** – Free notebooks with GPU/TPU access.

### Apple

- **MLX** – Efficient array framework for Apple silicon (supports 4‑ and 8‑bit).  
- **Core ML** – Optimized inference engine; leverages the Apple Neural Engine (ANE).

> The ANE is not directly accessible from MLX or PyTorch.

### AMD

- Uses **HIP** to translate CUDA code to AMD GPUs.

### CoreWeave

- Cloud AI provider with GPU‑focused infrastructure.

### Haiwei

- Ascend 910 – Inference hardware from Huawei.

## NVIDIA Ecosystem

> H100 units cost at least $30k; the entire product line includes:

- **GeForce** – Consumer gaming GPUs.  
- **Quadro** – Professional workstations.  
- **DGX / HGX** – AI‑focused servers (e.g., DGX A100, HGX H100).  
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

### Training Tools

- **AI Enterprise** – NVIDIA’s AI suite.  
  - **Triton Inference Server** (includes TensorRT).  
  - **NVIDIA NeMo** – Model training framework.

### Inference Tools

- **NVIDIA NIM** – Inference micro‑services.  
- **Jupyter notebooks** for experimentation.  

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
