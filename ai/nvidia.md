# Nvidia

> Do as much as needed, but as little as possible. Jensen Huang;

5 layers AI industry:

- Energy
- Chips (Hardware co-design)
- Infrastructure (Datacenter: power, cooling, data)
- Models
- Application

research teams:
- demand side
  - Circuits
  - Architecture
  - Programming Systems
  - VLSI
  - Storage
  - Networking
  - Security
- supply side
  - AI
  - Autonomous Vehicles
  - Quantum Computing
  - Robotics
  - Graphics

## Datacenter Infrastructure

- Compute Chassis Level ($250k H100)
  - Compute
  - Storage (30TB SSD) * 8
  - RAM (2TB)
  - CPU * 2
    - Intel Xeon (S > W > E > D)
    - AMD (bad for NCCL, tune NUMA NPS settings)
  - Backend Networking | InfiniBand (fastest)
    - ConnectX-7 NIC * 8 $($2k)
    - Bluefield-3 DPU * 2 ($3k)
      - more expensive than connectX
      - has build-in CPU
      - network virtualization
      - 400GB/s
  - Frontend Networking (ethernet++)
    - Falcon/GRD from GCP
    - Spectrum-X SN4600 switch * 2 @ 200GB/s
  - Out of Band Networking
    - SN2201 switch * 4
- Rack Level (9 nodes)
  - Rack Elevation
    - NVLink (between 8 GPUs)
    - NVLink fabric (between 256 GPUs ~ 50TB HBM, internal electric external optical)
      - fabricmanager
  - Datacenter Floor plan
  - Cables
    - distinct
      - Optical 100m+
      - DAC 3m, reliable
      - No cable 50m
    - Speed
      - Mini Cool Edge I/O (MCIO) ~ 10G/s per lane
      - QSFP28 @ 100G/s
      - QSFP56 @ 200G/s
      - QSFP-DD @ 400G/s
    - Active / Passive
    - Breakout
- Cluster Level 1024 H100 ($5mil)
  - Networking Topology
    - IB LinkX 400G Fiber
    - IB Transceiver
    - IB NIC * 1024 ($3k)
      - Single-port * 1024
        - 2 Virtual interfaces
      - Twin-port * 1536 (to switch)
    - IB Switch
      - SN8700 * 48 with 40 ports
        - NDR @ 400G/s > HDR @ 200G/s > EDR @ 100G/s
      - QM9700 with 64 ports
      - X800 with 128 ports
    - IP switch (frontend network)
  - Cluster BOM
  - Installation Plan
  - Acceptance Test
  - Power
  - Cooling
- Software Level
  - Network Management
    - Unified Fabric Manager (UFM)
  - Storage Management (~10TB/s @ training)
    - Luster
    - GPFS
    - Weka
    - Vast Data
  - Workload Scheduler
    - SLURMs
    - K8s
      - AI Enterprise $4.5k per GPU per year
  - Virtualization

### Server Tray

- CPU * 2
- GDDR
- GPU * 8
  - SM
    - CUDA Core: General‑purpose compute unit
    - Tensor Core: Matrix multiplication
    - SFUs: Special Function Units
    - **Tensor Memory Accelerator**(TMA): async io between global memory and shared memory;
    - **Shared Memory**
    - **Wrap Scheduler** ~ Wrap's manager manage threads instruction & state. `latency hiding happens here`
    - Dispatch Unit ~ Router for Wrap's active thread's instruction
    - load/store units
    - L1 cache
  - **L2 Cache** – Shared across SMs; large but slower than L1.
- **Global Memory** – HBM
  - Zero-Copy Memory - GPU directly invoke host memory
  - GPUDirect
- Networking:
  - spectrum-x `fiber to`
  - NV-Link switch `between nodes`


> SM's architecture determent hardware support kernels: SM100(spark) != SM120(H200); blackwell/rubin just marketing names.


### Nvidia Product Lines

- **Rubin NVL 144 CPX** `CPX means cluster comes w LPU`
- **NVL72 Cluster**: 72 × B200 GPUs.
- **DGX SuperPOD**: n × NVL72 Nodes.

- **DGX / HGX** – AI‑focused servers (e.g., DGX A100, HGX H100).
  - H100 units cost at least $30k; DGX has 8×H100
  - GH200 CPU has 900 GB/s bi-directional bandwidth between the CPU and GPU memory, much higher than others.

- GB300 ~ $100k with 700GB HBM3
- **Quadro** – Professional workstations.
- Spark ~ $4k with 128GB DDR4
  - https://forums.developer.nvidia.com/c/accelerated-computing/dgx-spark-gb10/719
  - [sparkrun](https://github.com/spark-arena/sparkrun)

- **GeForce** – Consumer gaming GPUs.
- **Thor** - robotics 128GB.
- **Jetson** – Edge AI and robotics.
- **Tegra** – Embedded/mobile GPUs.

Video GPU components:
- RTX Core: Ray tracing `Tree Traverse through bounding volume hierarchy`
- Raster Unit: Vector → pixel conversion
- Texture Unit: Apply textures to geometry
- NVENC / NVDEC: Video encode/decode


### Network Components

- CX [8, 9] Network Interface Control (NIC) uses InfiniBand; Node to Node
  - InfiniBand and RoCE NICs uses **RDMA**(looks like folder `/dev/infiniband` in Linux)
    - LinkX NDR ACC cables
  - RDMA over Converged Ethernet (RoCEv2) UDP ports (typically 4791, 4790).

- NVLink [5, 6, 8]; NVLink; GPU to GPU
  - Part of /dev/nvidia; No linux exposure

Analogy: A Shipping Port with Cranes

Think of your RDMA NIC (HCA = Host Channel Adapter) as a giant shipping port.
Applications (NCCL, UCX, MPI, etc.) want to move “containers” (data) quickly from one port to another.

But applications can’t directly drive the cranes, forklifts, and trucks at the port.
Instead, the Linux kernel provides gates (device nodes in /dev/infiniband).
Each gate has a special purpose — like customs, traffic control, or the big cranes.

- **InfiniBand** – Uses Remote Direct Memory Access (RDMA) bypasses the CPU. Uses Reliable Datagram Protocol (RDP) to share Memory across BETWEEN CLUSTER. Backend Networking

- OpenUCX (Unified Communication X) is a high-performance communication framework; Replaced **Mellanox**
  - **Unified Virtual Addressing** (UVA) - Share Memory across SINGLE NODE(Ex: a NVL72)

- **Ethernet** – Standard networking. Frontend Network.
- QSFP – High‑speed optical/electrical interface.

Important Network Settings:
- GID = Global Identifier, a 128-bit address used by InfiniBand/RDMA verbs.

### Storage

GPUDirect Storage (GDS) support 27 GBps


## NVIDIA Software Stack

- **AI Enterprise** – OS (Ubuntu + drivers)
  - MagnumIO
  - SLURM `srun –gres=gpu=8 -w NODE_NAME –pty bash`
  - Base Command Manager (BCM) $4.5k/yr per gpu
- **DGX Cloud** – NVIDIA’s AI suite. `Alternative to AWS, GPC, Azure` `https://build.nvidia.com/explore/discover`
  - **NGC** – NVIDIA GPU Cloud for containers and pre‑built images.
  - **NVIDIA NIM** – Inference micro‑services.  `similar to ollama; But NIM has different docker image for audio/image/video/biology service too`
    - **Triton Inference Server**
      - vllm (default engine)
      - **TensorRT**
      - sglang
  - **NVIDIA NeMo** – Model training framework.

> Usually deploy as container. Has SDK container w full tool sets, and Server container.

- Nsight Compute - Kernel optimization


### OS services

- BMC – Baseboard Management Controller (motherboard management).
- nv-hostengine
- nvidia-smi
  - NVML

## CUDA Programming

> Note: Tensor Core CAN'T tokenization, softmax scaling, KV cache indexing, and sampling, which still operate on floating point in CUDA Core;

> >  SM120 consumer fake blackwell, often SM100 kernel won't support.
CUDA: New Features and Beyond by Stephen Jones. Every year talk about CUDA direction.


Program Scope:
- CUDA Application
  - CUDA Stream
    - Kernel Launch: **Grid-Stride Loop**
      - **gridDim**   ≈ number of worker groups
      - **blockDim**  ≈ workers per group
      - **kernel**    ≈ work each worker executes
- GPU: runtime allocate workers to wraps
  - SM
    - **Warp** – 32 threads executed in lockstep.


| Layer                          | Examples                                                                 |
|--------------------------------|--------------------------------------------------------------------------|
| Frameworks & DSLs              | TensorRT · Omniverse · JAX · PyTorch                                      |
| SDKs                           | RAPIDS · CUDA-Q · BioNeMo · Ariel                                         |
| Domain-Specific Libraries      | cuQuantum · CUDA-CV · cuDNN · nvComp                                      |
| Accelerated Libraries          | Thrust · cuBLAS · cuFFT · NPP                                             |
| Communication Libraries        | NCCL · NVSHMEM · MPI · UCX                                                |
| Device Libraries               | CUB · CUTLASS · cuBLASDx · libc++                                         |
| Kernel Authoring               | CUDA C++ · PTX · OpenCL · CUDA Fortran                                    |
| Compiler Stack                 | nvcc · nvrtc · nvptx · ptxas                                              |
| Host Runtimes & Tools          | CUDA Runtime · Drivers · Nsight Tools · Installers                        |


- cuBLAS (Basic Linear Algebra Subprograms)
  - GEMM (General Matrix-Matrix Multiplication)
- cuDNN (CUDA Deep Neural Network)
- CUTLASS is a template library that provides building blocks for writing
high-performance kernels

### Parallel Thread Execution Instructions
> PTX Instructions are GPU Primitives.
> GPU architectural differences in details. By OpenAI ofc.
> > **tcgen05** & **TMEN/UMMA** ~ SM100 instructions.
>
> CUDA_ARCH 9.0 = SM90
>
> NVVM is Nvidia's extension of LLVM.

| GPU Primitives | Job | Ampere SM80 | Hopper SM90 | Blackwell SM100 |
|---|---|---|---|---|
| **Compute** | Matrix math | `mma.sync` | `wgmma` | `tcgen05.mma` |
| **Data movement** | Move tensors/tiles | `cp.async` | **TMA** / `cp.async.bulk` | TMA + `tcgen05.cp` |
| **Matrix load/store** | Move fragments between memory levels | `ldmatrix` | `ldmatrix` | `tcgen05.ld/st` |
| **Synchronization** | Coordinate async work | barriers | `mbarrier` | `mbarrier` + newer mechanisms |
| **Execution grouping** | Define cooperating threads | warp/CTA | **warp-group / cluster** | CTA pairs / clusters |
| **Memory hierarchy** | Where working data lives | Reg + SMEM | Reg + SMEM + DSM | Reg + SMEM + **TMEM** |
| **Communication** | GPU↔GPU / CTA↔CTA | NVLink, atomics | DSM/NVLink | enhanced NVLink mechanisms |
| **Scalar/vector** | Normal arithmetic | `add`, `mul`, `fma`, etc. | same | same |

- CTA: Cooperative Thread Array, CUDA Thread Block hardware
- WGMMA: Warp Group Matrix Multiply Accumulate, let wrap runs matrix multiply in background, while wrap moves on other data movements.


### Nvidia C Compiler

> Nvidia C Compiler(nvcc) compile kernel into PTX.

Statically-linked `compiled with dependence`
Dynamically-linked `use CUDA runtime`

```bash
# Compile kernel for NCU
nvcc [filename.cu] -o benchmark

# Then let NCU print kernel profile result
ncu --set full ./benchmark

# check registers spillover
nvcc -Xptxas=-v kernel.cu -o kernel

# -O: optimized level
nvcc -O3 kernel.cu

# Often cmake define whole project @ CMakeLists.txt, wrapper around nvcc
cmake -B build
cmake --build build
```

### Kernel

CPU dispatch CUDA kernel, kernel rarely invoke another kernel(Dynamic Parallelism).


- **cuDNN**, **DeepSpeed** for large‑scale training.
- Dependent Kernel Launch `sequential kernels`
- DeepGEMM kernel H100

### Kernel Selection/Tuning
```md
Algorithm
   ↓
Candidate kernel family
   ↓
Shape + dtype + layout + hardware + workload constraints
   ↓
Candidate kernel configurations
   ↓
Benchmark / heuristic / autotune
   ↓
Selected kernel
```

> autotuning shows up every stacks!

> kernel microbenchmarks and actual inference-engine performance.

Benchmark:
- Arithmetic intensity
- memory traffic
- compute utilization
- Scheduling: occupancy/stalls

Tools:
- Torch profiler
- Nsight Systems
- Nsight Compute
- CUTLASS / Triton profiler
- Nvidia Compute Profiler (NCU)

Optimazation:
- block decomposition
- thread/lane assigment
- Matrix Multiply and Accumulate/WGMMA lowering
- reg allocation
- instruction scheduling


### FlashInfer

Specialized high-performance CUDA kernel library for LLM inference.

Vllm, sglang now offloads their most kernel development to FlashInfer.

> Major reason inference companies fork vLLM/SGLang is to take tighter control over exactly FlashInfer usage.

### CUDA Driver

> `cuda-checkpoint` suspend & restore GPU active state. Often saved GPUs state into CPU DRAM.
>> Ex: switch LLM from 20s to 2s.

The command to enable GPUDirect RDMA is `sudo modprobe nvidia-peermem`

## Debug

```md
NVIDIA GPU Errors
│
├── Application
│   └── CUDA / NCCL / PyTorch
│
├── Driver / Firmware
│   ├── NVIDIA Kernel Driver
│   │
│   └── **GSP** (GPU System Processor) `xid: 120`
│       ├── GSP firmware crash
│       ├── GSP timeout / hang
│       ├── RPC failure
│       ├── firmware boot failure
│       └── driver ↔ GSP communication failure
│
├── GPU Hardware / RAS
│   ├── SM
│   ├── HBM
│   ├── L2
│   └── internal fabric
│
├── Interconnect
│   ├── PCIe
│   ├── NVLink
│   └── NVSwitch
│
└── Power / Thermal
```


### NCU
NVTX markers

### Pytorch Profiler


- runtime profiling: export as [json chrome traces](chrome://tracing/)
  - CPU tracks
    - forward pass & backward pass(autograd engine) usually on different threads.
  - CUDA Stream tracks
- GPU memory profiling
- communication profiling
`1GB = 1e6`


tips:
- verify `Synch` blocks are necessary
- [dispatch chain UI](https://ui.perfetto.dev/)