# Hardware

> At the end of the day, only limitation is chip space(Real estate); space either assign to computation(flexible or efficiency) or storage(latency or throughput);

## Software
>
> Machine Learning Frameworks(PyTorch) > Acceleration Driver(cuDNN) > Parallel Thread Execution(PTX: assembly code) > Streaming ASSembly (SASS: machine code) > Hardware(GPU)

> Different hardware needs its custom version llama.cpp. Ex(Metal llama.cpp, ROCm llama.cpp, CUDA llama.cpp)

> Each manufactory has its own Shading Language(SL).

- near memory design:
- reconfigurable dataflow hardware vs parallelism on top of existing computation

## RAM
>
> The real bottleneck is the memory hierarchy: the GPU has limited high-bandwidth memory (HBM or SRAM), and the model's parameters far exceed this capacity. This forces frequent data transfers between off-chip and on-chip memory.

> > GPU hide its memory latency by WRAP handle multiple threads. Unlike CPU switch threads are slow & expensive, GPU thread are Lightweight Context, schedule by hardcore not OS.

> RAM size & speed & throughput is key bottleneck of AI training & inference.

> GRAM are high throughput, unlike CPU focus on low latency.

- RAM
  - Dynamic RAM (DRAM) `capacitors`
    - HBM
      - PCIe 5 `128 GB/s`
      - SXM `600 GB/s`
    - DDR1-5
    - LPDDR
    - GDDR
  - Static RAM (SRAM) `flip-flops (latches)`
    - L1, L2, L3 cache
- Flash

## Network

- InfiniBand
  - Remote Direct Memory Access (RDMA) `by pass CPU, network card can directly store data into RAM
  - Reliable Datagram Protocol (RDP)`
- Ethernet

## Training

- cuDNN
- Deep Learning GPU eXtreme(DGX) A100 server = 8 (A100 80GB GPU)
  - V(Volta)100 GPU
    - original GPT trained w 10,000 V100 GPUs
    - GV100, GA100, GH100,
      - Tensor Core that specialize in matrix multi
- HGX
  - H(Hopper)100 GPU
- APU

- DGX server have sister product (HGX server)High-Performance GPU (Graphics Processing Unit) eXtensible

- Data Parallelism (DP) `Clone the whole Model`
- Pipeline Parallelism (PP) `Split the model across layers; Deep Model`
- Sequence Parallelism (SP) `Long Input token`
- Tensor Parallelism (TP) `very bad idea`
- State Batch `Sync Back Props loss`
- Master Weight

## Networking

- Ethernet Cable `Color (OrgWhite, Org, GreenWhite, Blue, BlueWhite, Green, BrownWhite, Brown), Only need (1,2,3,6) to work, but limited to 100mb`
- QSFP (Quad Small Form-factor Pluggable)
- Fiber Optic Cables

## Improvement

| Optimization            | Key Idea                          | Benefit                                |
|-------------------------|-----------------------------------|----------------------------------------|
| Use Tensor Cores        | FP16/INT8 for matrix ops          | 10-20x speedup in matrix multiplication |
| Memory Coalescing       | Align memory for efficient access | Avoids global memory latency           |
| Kernel Fusion           | Merge multiple operations         | Reduces launch overhead                |
| FlashAttention          | Compute attention in blocks       | Saves memory and speeds up inference   |
| Lower Precision (FP16/INT8/FP8) | Reduce data size           | Faster compute, lower memory use       |
| Persistent Kernels      | Keep threads active              | Reduces scheduling overhead            |
| CUDA Graphs             | Precompute kernel calls           | Avoids CPU bottlenecks                 |
| Multi-token Decoding    | Predict multiple tokens           | Speeds up text generation              |

## OpenSource

- Exo Labs `AI clusters software`

## Inference Hardware
>
> Usually they all use In Memory Compute instead HBM

- Groq `inference workloads only. PyTorch model to ONNX, then ONNX compiled into Groq hardware.`
- Etched ``
- D-Matrix ``

## Amazon

- Trainium `Amazon design hardware supports CUDA`
- Bedrock `LLM SSAS provider`

> anthropic works with Amazon.

## Google

- TPU `Google design hardware`
- Colab `Google Jupiter notebook with FREE GPU`

## Apple

> MLX is an array framework designed for efficient and flexible machine learning research on Apple silicon. But only support 4 & 8 bits

> CoreML is Apple’s optimized AI inference engine for running ML models on Apple devices. It supports ANE (Apple Neural Engine) for maximum efficiency.

CUDA vs. Mac Interpolation Support

Apple Neural Engine(ANE) is not accessible to MLX or PyTorch directly.

## AMD

> AMD uses Hipify to convert CUDA into AMD HIP.

## CoreWeave

> Bunch top finical ground funded Cloud AI warehouse.

## Haiwei

> Ascend910 Inference Hardware

## Open AI

> Triton is OpenAI alternative to CUDA.

## Nvidia

> H100 cost at least $30k; standard unit;
> NVIDIA makes 1-2 million H100 per year.
> DGX cost at least $350k, includes 8 A100 GPUs; Commonly call a node.

- Product Lines:
  - GeForce Series (Gaming and Consumer GPUs)
  - Quadro Series (Professional Workstations)
  - DGX & HGX (AI)
  - Jetson Series (Edge AI and Robotics)
  - Tegra Series (Embedded and Mobile GPUs)

- GPU hardware units `Each unit has its generation architecture`
  - CUDA Core `General propose unit`
    - from 1.x -> CUDA 11.x
    - DLSS 3 (Deep Learning Super Sampling 3)
    - DLSS 4 `switch CNN to Transformer`
  - Tensor Core `Matrix Only`
    - Volta (first generation)
    - Turing (improved with INT8 and INT4 support)
    - Ampere (added sparsity support)
    - Ada Lovelace (further efficiency improvements)
  - RT cores: `For ray tracing, enhancing realistic lighting and shadows in graphics.`
  - Raster units: `For converting vector graphics to raster images.`
  - Texture units: `For texture mapping, which applies images to 3D models.`
  - Memory
    - GDDR5
    - GDDR6
    - GDDR6X
    - HBM2
  - NVLink: `For high-speed interconnects between GPUs.`
  - Display Engine
  - NVENC (Encoder) & NVDEC (Decoder)

- Training Tools
  - AI Enterprise (AIE) `charge by GPU`
    - Triton Inference Server
      - TensorRT `LLM runtime`
    - NVIDIA NeMo `Training`
  - AI Workbench
    - Single GPU
- Inference Tools
  - NVIDIA Inference Microservices (NIM)
    - Jupyter Notebook as Workbench
    - Standardize RESTful APIs

Nvidia Hardware Terms:
DGX -> DGX Base Pods -> DGX Super Pods -> DGX Cloud
NVLink `within a server` vs InfiniBand `across servers`

Baseboard Management Controller (BMC) `aka mother board`
Quad Small Form-factor Pluggable (QSFP) `aka fast ethernet`

Terms

- CUDA compiler (nvcc)
- Streaming Multiprocessors (SMs)
- NVIDIA Collective Communications Library (NCCL)
- cuda-gdb `debug`
- mixed precision execution(runs 8 bit operations on 16 bit to maximize hardware usage)

- Grid `each scope has its own memory; Grid won't free unless cudaFree(); reduce synchronization size.`
  - Block `Set of threads; memory reset after finished.  max 1024 threads.`
    - Thread `1 to 1 cuda core;`

> Both Grid & Block supports up to 3 dimensions (x, y, z)

> Each thread is map to single CUDA core

> Only one kernel is execute, by default won't have multiple kernel run at once.

```ps

# Developer Perspective
Grid (Many Blocks)
 ├── Block 0 (1024 Threads) `assign to single SM`
 |    ├── Warp 0 (32 Threads)
 |    │    ├── Thread 0 `assign to CUDA core`
 |    │    ├── ...
 |    │    ├── Thread 31
 |    ├── Warp 1 (32 Threads)
 |    │    ├── Thread 32
 |    │    ├── ...
 |    │    └── Thread 63
 |    ├── Warp 31
 |    │    ├── Thread 991
 |    │    ├── ...
 |    │    └── Thread 1023
 ├── Block 1 (Many Threads)
 │    ├── Thread 0
 │    ├── Thread 1
 │    ├── ...
 │    └── Thread 1023
 └── Block 255 (Many Threads)

# Hardware Perspective
GPU (H100)
 ├── SM 0 (SIMT) `Single Instruction, Multiple Threads`
 │    ├── CUDA Cores
 │    ├── Tensor Cores
 │    ├── Warp Schedulers (4)
 |    |   ├── Warp 0 (32 Threads) `rotate threads on SM to increase occupancy rate`
 |    |   ├── ...
 |    |   └── Warp N
 │    ├── SFUs (Trigonometric & special functions)
 |    ├── Load/Store Units (Memory operations)
 |    ├── L1 Cache & Shared Memory (228 KB)
 |    ├── RT Cores (if present) (For ray tracing)
 |    └── Texture Units (For graphical applications)
 ├── SM 1
 ├── ...
 ├── SM 131
 |
 ├── L2 Cache (50 MB, Shared across SMs, on chip memory)
 └── Global Memory (aka HBM RAM, 80GB)

```

Nvidia Software Terms:

- AI Enterprise
  - DGX OS `Ubuntu + custom tools & drivers`
    - Tools:
      - Nvidia Base Command `enough for most devs`
      - Nvidia Base Command Manager `UI for base command`
      - Nvidia Suit Command `edge vision deployment`
    - Tech:
      - Remote Direct Memory Access (RDMA)
  - Nvidia GPU Cloud (NGC) `Only for Nvidia Hardwares`
    - VCenter `Aka Nvidia Cloud console, create VM`
      - WorkLoads `spin up container`
      - DataSources
  - Hyperscale GPU Accelerator (HGX) `Certified Servers for NVIDIA AI Enterprise`
    - Dell PowerEdge Servers (e.g., R750xa, R760)
    - HPE ProLiant Servers (e.g., DL380 Gen10, DL385 Gen11)
    - Lenovo ThinkSystem Servers (e.g., SR670, SR650)
    - Supermicro GPU Servers (e.g., SYS-420GP-TNAR, SYS-210GP-DNR)

```

nvdia-smi

```

Create VM steps:

1. Define hardware profile
2. Software `NVD guess driver & container toolkit`
3. App Config `aka volume, container, software, etc. Analogy: room blueprint`
4. Template Config `reusable blueprint; Analogy: house blueprint`

Registers(8TB/s) < Shared (1.5TB/s `L1 cache`) < Const Memory(`immutable constance`) < Local(200GB/s) < Host (5GB/s)
