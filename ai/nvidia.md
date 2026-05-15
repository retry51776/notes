# Nvidia

> Do as much as needed, but as little as possible.

5 layers AI industry:

- Energy
- Chips (Hardware co-design)
- Infrastructure (data, data pipeline & kernels)
- Models
- Application

## Nvidia Product Lines

- **NVL72 Cluster**: 72 × B200 GPUs.
- **DGX SuperPOD**: n × NVL72 Nodes.

- **DGX / HGX** – AI‑focused servers (e.g., DGX A100, HGX H100).
  - H100 units cost at least $30k; DGX has 8×H100

- GB300 ~ $100k with 700GB HBM3
- **Quadro** – Professional workstations.
- Spark ~ $4k with 128GB DDR4
  - https://forums.developer.nvidia.com/c/accelerated-computing/dgx-spark-gb10/719

- **GeForce** – Consumer gaming GPUs.
- **Thor** - robotics 128GB.
- **Jetson** – Edge AI and robotics.
- **Tegra** – Embedded/mobile GPUs.

### BoM

- Compute Chassis Level ($250k H100)
  - Compute
  - Storage (30TB SSD) * 8
  - RAM (2TB)
  - CPU * 2
    - Intel Xeon (S > W > E > D)
    - AMD (bad for NCCL, tune NUMA NPS settings)
  - Backend Networking | InfiniBand (fastest)
    - ConnectX-7 NIC * 8 $($2k)
      - RoCEv2
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
    - Speed
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
  - Storage Management
    - Luster
    - GPFS
    - Weka
    - Vast Data
  - Workload Scheduler
    - SLURMs
    - K8s
      - AI Enterprise $4.5k per GPU per year
  - Virtualization

### Server Rack Components

- LPU - 500 SRAM @ 150TB/s
- GPU
- spectrum-x `fiber to`
- NV-Link switch `between nodes`

### GPU Components

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

- **Grid** – Collection of blocks; can be 1‑3 dimensions.
- **Block** – Up to 1024 threads; also 1‑3 dimensions.
- **Warp** – 32 threads executed in lockstep.
- Unified Virtual Addressing (UVA) - Share Memory across SINGLE NODE(Ex: a NVL72)

```py
# Developer perspective with Hopper
CPU
 ├─ Stream A → kernel launch
 │   ├─ kernel1 → Grid A
 │   ├─ kernel2 → Grid B
 │   └─ kernel3 → Grid C
 ├─ Stream B → kernel launch
 │   └─ kernel4 `kernel<<<gridDim, blockDim, sharedMem, stream>>>`
 └─ Stream C

# Kernel has flexible grid size & block size, index rule, define per thread computation
# gridDim unlimited, blockDim 0-1024, sharedMem 0-48 KB (per block),

#        ↓
# GPU scheduler
#        ↓
# Break kernels into block threads
Grid (kernel 1 to 1 grid)
 ├─ Block 0 (max 1024 Threads) → assigned to a single SM
 │   ├─ Warp 0 (a wrap = 32 Threads w SAME instruction, different states)
 │   ├─ …
 │   └─ Warp 63
 ├─ Block 1 (from 1 to 1024 Threads)
 ├─ …
 └─ Block 31

# Threads are independent, parallel, ordered diagnostic tasks.

# Grids may be 3 dimensional ($$GlobalID = (blockIdx.x \times blockDim.x) + threadIdx.x$$), purely software index.

'''
       ↓
Block-level scheduling:
- programmer defines blocks
- CUDA runtime/hardware schedules blocks onto SMs automatically

Tile-level scheduling:
- programmer/compiler defines tile decomposition inside a block
- execution of those tiles is handled within the block on the assigned SM
       ↓
'''

# Hardware perspective with Hopper
GPU (H100 / Hopper) has 132 SMs
 ├─ SM 0
 │   ├─ 4 Warp Scheduler(s) → similar Hyper-Threading, so 4 active warps (4 * 32 = 128 active threads per SM) continues working on millions threads.
 │   │   ├─ Warp 0 (32 threads SAME instruction)
 │   │   ├─ Warp 1 (only 4 active Warp per SM)
 │   │   ├─ ...
 │   │   └─ Warp 63
 │   ├─ Registers (per thread)
 │   ├─ Shared Memory (per block region)
 │   └─ 128 Tensor Cores / FP units
 │
 ├─ SM 1 with 256 KB L1 SRAM registers, shared by block
 │   └─ ...
 │
 └─ SM 131
```

- **SM** – Streaming Multiprocessor; contains CUDA cores, Tensor Cores, warp schedulers, SFUs, load/store units, L1 cache & shared memory.
- **L2 Cache** – Shared across SMs; large but slower than L1.
- **Global Memory** – HBM or GDDR attached to the GPU.
  - Zero-Copy Memory - GPU directly invoke host memory
  - GPUDirect
- error buffer is a "single-slot" & async, so never can guaranty all error messages are collected.
- Kernel indexing = mapping rule
- Launch config   = execution shape

Analogy: The Multi-Lane Toll Plaza.

- Entire traffic demand ~ Grid
  - shipping logistics ~ Kernel Indexing
    - number of roads ~ grimDim
    - number of car per road ~ blockDim
      - car convoy ~ wrap
  - road lanes ~ Block
    - road support capacity ~ sharedMem (per block)
  - individual car ~ Thread
    - complete stopped ~ thread data loaded, task ready to execute
    - cars convoy enter toll (32 cars) ~ active wrap
    - car weight ~ L1 SRAM register usage
- toll road ~ GPU
  - active wraps ~ 32 cars allow entry toll at once
  - toll station ~ SM
    - toll station controller ~ Warp Scheduler
  - toll gates > toll lanes ~ latency hiding

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

- **InfiniBand** – Uses Remote Direct Memory Access (RDMA) bypasses the CPU. Uses Reliable Datagram Protocol (RDP) to share Memory across BETWEEN CLUSTER. Backend Networking (InfiniBand or RoCEv2 Ethernet)
  - NCCL (NVIDIA Collective Communications Library) - specialize protocol for GPU, open source
  - **NVSHMEM** - GPU threads directly put/get/update data in remote GPU memory without CPU involvement.

- OpenUCX (Unified Communication X) is a high-performance communication framework; Replaced **Mellanox**
  - **Unified Virtual Addressing** (UVA) - Share Memory across SINGLE NODE(Ex: a NVL72)

- **Ethernet** – Standard networking. Frontend Network.

### Storage

GPUDirect Storage (GDS) support 27 GBps

## Server Software

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

### OS services

- BMC – Baseboard Management Controller (motherboard management).
- QSFP – High‑speed optical/electrical interface.
- nv-hostengine
- nvidia-smi
  - NVML

## CUDA Programming

> Note: Tensor Core CAN'T tokenization, softmax scaling, KV cache indexing, and sampling, which still operate on floating point in CUDA Core;

CUDA: New Features and Beyond by Stephen Jones. Every year talk about CUDA direction.

CUDA Platform Stack

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

pytorch -> NVCC compiler -> (Cubins or Fatbins) -> JIT -> PTX

### nvcc

Statically-linked `compiled with dependence`
Dynamically-linked `use CUDA runtime`

### kernel

CPU dispatch CUDA kernel, CUDA kernel can NOT invoke another CUDA kernel.

> Most kernel authoring are for improve training, room to improve inference are very small (inference are mostly memory bound).


- **cuDNN**, **DeepSpeed** for large‑scale training.
- Dependent Kernel Launch `sequential kernels`

### Asymmetric Parallelism

Symmetric Parallelism VS Asymmetric Parallelism

Tech stacks:

- CUDA Stream - opportunistic Asymmetric Parallelism Execution.
- Green Context - Dynamic partition with guaranty. Aka define consumer/worker & routing_key.
- Multi-Process Service (MPS) - Controlled GPU partition.
- Multi-Instance GPU (MIG) - fixed GPU partition

> CUDA has 2 main libraries categories: computation libraries & Communication libraries.

computation libraries is A MESS.


### FlashInfer

Specialized high-performance CUDA kernel library for LLM inference.

### C++ CUDA SIMT

https://docs.nvidia.com/cuda/

`CPU → submits work → Stream → GPU scheduler → SM`

classic CUDA code. Thread is lowest execute unit.

define the execution graph + hardware mapping explicitly.

### Triton

define the math + tiling, compiler defines execution. Manage by OpenAI. JIT compiler, so only generate kernel cache at runtime.

### CuTitle

since CUDA 13.0; **Tile IR** compile into GPU executable. Block is lowest execute unit. Array based programming.

There are both cuTile C++ & cuTile Python.

less controls then CUDA python SIMT.

```py
import nvshmem.core.device.tile
```

https://github.com/NVIDIA/TileGym

cuTile autotuner

@cuda.tile.kernel invoke @cuda.tile.function

### nvmath-python

```py
# NVTX annotation for Nsight Profiler

import nvtx
@nvtx.annotate(color="blue")
def xxx():
    with nvtx.annotate("this_loop", color="red"):
        pass

```

- stateless api ~ similar to numpy
- stateful api ~ `with nvmath.xxx(a, b)`

`numba-CUDA` is single thread python compiler, so developer can inspect CUDA code.

`nsight copolit`
import cuda.tile as ct

## CUDA Domain-Specific Language (DSL)

> kernel generator, performance between pytorch and CUDA C++.

```py
import cuda.tile as ct

@ct.func
def matmul(A: ct.Array,
           B: ct.Array,
           C: ct.Array,
           tshp: ct.Constant[ct.Shape]):

    sum = ct.zeros(tshp[0:1], A.dtype)

    pA = ct.partition(A, (tshp[0], tshp[2]))
    pB = ct.partition(B, (tshp[2], tshp[1]))

    for k in range(pA.shape[1]):
        sum = ct.mac(
            pA[ct.pid(0), k],
            pB[k, ct.pid(1)],
            sum
        )

    ct.store(C, ct.pid(0:2), sum)
```

### CUDA Driver

> `cuda-checkpoint` suspend & restore GPU active state. Often saved GPUs state into CPU DRAM.
>> Ex: switch LLM from 20s to 2s.

The command to enable GPUDirect RDMA is `sudo modprobe nvidia-peermem`
