# Nvidia

- Offset Geometric Contact(OGC) replaced Individual Potential Contact (IPC) that can trigger object pass through bug.

- <https://github.com/NVIDIA/personaplex>

## Hardware Infrastructure

- **cuDNN**, **DeepSpeed** for large‑scale training.  
- **DGX Node**: 8 × A100 80 GB GPUs.
- **NVL72 Cluster**: 72 × B200 GPUs.
- **DGX SuperPOD**: n × NVL72 Nodes.
- **DGX Cloud**: rent DGX node level(not GPU level)

- GB300 ~ $100k with 700GB HBM3
- **Quadro** – Professional workstations.  
- **DGX / HGX** – AI‑focused servers (e.g., DGX A100, HGX H100).
  - H100 units cost at least $30k; DGX has 8×H100
- Spark ~ $4k with 128GB DDR4

- **GeForce** – Consumer gaming GPUs.
- **Jetson** – Edge AI and robotics.  
- **Tegra** – Embedded/mobile GPUs.

### Datacenter Components

- LPU - 500 SRAM @ 150TB/s
- GPU
- spectrum-x `fiber to`
- NV-Link switch `between nodes`

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

## Network

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

## CUDA Programming Concepts

- **Grid** – Collection of blocks; can be 1‑3 dimensions.  
- **Block** – Up to 1024 threads; also 1‑3 dimensions.  
- **Warp** – 32 threads executed in lockstep.  
- Unified Virtual Addressing (UVA) - Share Memory across SINGLE NODE(Ex: a NVL72)

### FlashInfer

Specialized high-performance CUDA kernel library for LLM inference

```py
# Developer perspective with Hopper
Grid (many Blocks)
 ├─ Block 0 (1024 Threads) → assigned to a single SM
 │   ├─ Warp 0 (32 Threads)
 │   └─ …
 ├─ Block 1 (many Threads)
 ├─ …
 └─ Block 31
```

- **SM** – Streaming Multiprocessor; contains CUDA cores, Tensor Cores, warp schedulers, SFUs, load/store units, L1 cache & shared memory.  
- **L2 Cache** – Shared across SMs; large but slower than L1.  
- **Global Memory** – HBM or GDDR attached to the GPU.

## NVIDIA Software Stack

- **AI Enterprise** → OS (Ubuntu + drivers) → Tools (Base Command Platform, Suit Command).  
- **NGC** – NVIDIA GPU Cloud for containers and pre‑built images.  
- **HGX** – High‑performance GPU servers (e.g., Dell PowerEdge R750xa, HPE ProLiant DL380 Gen10, Lenovo SR670, Supermicro SYS‑420GP).

Background services:

- nv-hostengine

## Nemotron-3

88 Blocks: (MEMEMEM*EMEMEMEM*EMEMEMEM*EMEMEMEMEM*EMEMEMEMEM*EMEMEMEMEM*EMEMEMEMEM*EMEMEMEM*EMEMEMEME)

3 block types:

- Mamba (Linear Attention or RNN)
- Attention
- MoE / MLP
