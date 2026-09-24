# Hardware

> Ultimately, the only limitation is chip real estate; space must be allocated to computation (flexible or efficient) or storage (latency or bandwidth or capacity).

> **GPU vs CPU** hides latency by interleaving many wraps. Unlike CPUs, where context switches are expensive, GPU threads are lightweight and scheduled by hardware.
> > GPU trade CPU's scheduler area for more SM cores.

## Runtime Workflow

### Compiler Pipeline

> [Online Compiler Godbolt](https://godbolt.org/)

```md
Model / Python program
        │
        ▼
1. Graph capture / tracing
   └─ Turn eager tensor operations into a graph
      e.g. matmul → add → RMSNorm → attention
        │
        ▼
2. High-level graph IR
   └─ Framework-independent-ish tensor operations
      shapes, dtypes, dependencies, constants
        │
        ▼
3. Graph optimization
   ├─ constant folding
   ├─ dead-op elimination
   ├─ layout propagation
   ├─ operator fusion
   └─ algebraic simplification
        │
        ▼
4. Lowering
   └─ High-level ops → lower-level primitive operations

      matmul
        ↓
      tiled loads
      multiply-accumulate
      reduction
      stores
        │
        ▼
5. Kernel formation / scheduling
   ├─ Decide which operations become one kernel
   ├─ choose tiles
   ├─ threads / warps / workgroups
   ├─ shared/local memory
   ├─ vectorization
   └─ memory access pattern
        │
        ▼
6. Kernel IR
   └─ Explicit parallel program

      program_id
      load
      dot
      barrier
      store
        │
        ▼
7. Target code generation
   ├─ NVIDIA → PTX / LLVM → SASS
   ├─ AMD → LLVM/AMDGPU → GCN/RDNA ISA
   ├─ Apple → Metal compiler → Apple GPU ISA
   └─ CPU → LLVM → x86/ARM ISA
        │
        ▼
8. Runtime launch
   ├─ allocate buffers
   ├─ bind arguments
   ├─ select grid/block dimensions
   └─ launch compiled kernel
        │
        ▼
GPU / CPU hardware
```

### Kernel

> kernel ~ C++ void function executed by MANY GPU threads(Grid-Stride Loop);

- **Grid-Stride Loop**: gridDim * blockDim loop
  - build-in variables: `gridDim, blockDim, blockIdx, threadIdx, warpSize`
  - gridDim   ≈ number of worker groups
  - blockDim  ≈ workers per group
  - kernel    ≈ work each worker executes
- kernel consideration:
  - dtype
    - quantization
  - M, N, K dimensions
  - [layout(coordinate) → index](code.md#cute)
    - coordinate: WHICH logical element(row & col of matrix)?
    - index: linear offset into the underlying storage
    - shape & stride: matrix shape & indexing pattern! `coordinate may not be continues`
  - contiguous/strided
  - workspace memory

```md

Kernel Contract:
├── Operation       GEMM? attention? RMSNorm? MoE dispatch?
├── Input shapes    M × K, K × N
├── Layout          row-major / column-major / tiled
├── Dtype           FP16 / BF16 / FP8 / INT8
├── Output          dtype + layout
├── Semantics       scaling, bias, activation, masking, etc.
├── Hardware        Hopper? Blackwell? AMD?
└── Runtime/API     CUDA stream, workspace, synchronization


Grid-Stride Loop

══════════════════════════════════════════════════════════════

                    GRID
              gridDim.x = 3
         ≈ 3 worker groups (blocks)

     ┌──────────┬──────────┬──────────┐
     │ BLOCK 0  │ BLOCK 1  │ BLOCK 2  │
     │blockIdx=0│blockIdx=1│blockIdx=2│
     │          │          │          │
     │ T0 T1 T2 │ T0 T1 T2 │ T0 T1 T2 │
     │          │          │          │
     └──────────┴──────────┴──────────┘
          ↑
     blockDim.x = 3
     ≈ 3 workers / group

Global thread IDs

──────────────────────────────────────────────────────────────

 Block 0        Block 1        Block 2

┌─────────┐    ┌─────────┐    ┌─────────┐
│ T0 → 0  │    │ T0 → 3  │    │ T0 → 6  │
│ T1 → 1  │    │ T1 → 4  │    │ T1 → 7  │
│ T2 → 2  │    │ T2 → 5  │    │ T2 → 8  │
└─────────┘    └─────────┘    └─────────┘

i = blockIdx.x * blockDim.x + threadIdx.x

Grid stride

──────────────────────────────────────────────────────────────

stride = gridDim.x * blockDim.x
       = 3 * 3
       = 9

                    WORK SPACE

  0  1  2  3  4  5  6  7  8 | 9 10 11 12 13 14 15 16 17 | ...
  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑   ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑
 T0 T1 T2 T3 T4 T5 T6 T7 T8  T0 T1 T2 T3 T4 T5 T6 T7 T8
  │                          stride = 9
  └──────────────────────────────→

Each worker executes the kernel repeatedly:
Thread 0 :  0 ──→  9 ──→ 18 ──→ 27 ...
Thread 1 :  1 ──→ 10 ──→ 19 ──→ 28 ...
Thread 2 :  2 ──→ 11 ──→ 20 ──→ 29 ...
...
Thread 8 :  8 ──→ 17 ──→ 26 ──→ 35 ...

CUDA built-ins
──────────────────────────────────────────────────────────────
gridDim    ≈ number of worker groups
blockDim   ≈ workers per group
blockIdx   = which worker group am I?
threadIdx  = which worker am I within the group?
warpSize   = workers executed together as a warp (32)
kernel     ≈ work each worker executes
```

#### Layout
> Kernel logic is heavily influenced by the tensor layout.
>
> SubTile has SAME stride as parent, but with different pointer.
```md
Tensor
├── Engine
│   └── Where/how data is accessed
│       ├── pointer
│       ├── registers
│       ├── shared memory
│       └── global memory
│
└── Layout
    ├── Shape
    │   └── (M, N, ...)
    │
    └── Stride
        └── mapping coordinates → linear offset

Shape  = (3, 4)
Stride = (4, 1)

         Shape
      4 columns
    ┌─────────────┐
  3 │ 0  1  2  3  │
rows│ 4  5  6  7  │
    │ 8  9 10 11  │
    └─────────────┘

Move ↓ one row:    index += 4
Move → one column: index += 1
                    ↑
                  Stride
```

> Nest shape is possible, think of it as sql composite index;
> > Ex: shape A (1, 2, 3) vs shape B ((1, 2), 3)
> > A has 3 indexes to access A; while B only has 2 indexes, first index is composite index!

#### Compute Precision
> kernel contain quantize & dequantize logic, determent compute & accumulate precision.
> > Hardware support, then use instruction; Otherwise cuda code bitwise manipulation does pack & unpack.
>
> Industrial standard is shared quantized & dequantized in shared method.

- CPU default FP32 AVX kernel
- MAC default FP16
- NVIDIA has many compute precision, NVFP4 is common inference precision
- prologue vs epilogue


### Intermediate Representation

> IR represent the program in an intermediate form that is easier to analyze, transform, optimize, or retarget. Compiler engineer's territory.

> Just like SQL has many forms, IR has many versions.

LLVM Frontend: `understands Language`
- Clang
- Flang

LLVM Optimizer: `understands Program`
  │
  ├── Inlining
  ├── Constant folding
  ├── Dead-code elimination
  ├── Loop optimizations
  ├── Loop Vectorizer
  ├── SLP Vectorizer
  └── many others

LLVM Backend: `understands HARDWARE`
- Apple: AArch64 ISA
- Nvidia: NVPTX backend
- AMD: AMDGPU backend




### Hardware Execution Model
> CPU & GPU Execution Datapath
> Kernel function + arguments / buffers + thread/grid dimensions + pipeline state = dispatch descriptor

CPU/Metal driver side:
- records each kernel dispatch
- binds pipeline state, buffers, offsets, constants
- validates resource usage
- builds command streams
- commits command buffers to the GPU queue

GPU command processor / scheduler:
- reads the command stream
- launches each dispatch in command-buffer order
- assigns threadgroups to GPU cores
- manages barriers/order between dispatches
- tracks resource hazards enough to preserve command ordering
- handles occupancy: how many threadgroups can fit based on registers, threadgroup memory, threads, etc.

Per-kernel execution:
- allocates threadgroup memory/SRAM if the kernel declares it
- schedules SIMDgroups/threads
- runs memory loads/stores and ALU work
- retires threadgroups

> SM assignment is hardware/runtime decides!
> Thread Blocks / CTAs is indivisible scheduling units.

```py
# Hopper Workflow

# Optional: NUMA Aware = Non-Uniform Memory Access Aware; `aware CPU's RAM w different speeds`; `nvidia-smi topo -m`


# 1. Developer
# Program ask CPU to launch CUDA application with gridDim, blockDim.
# must ensure grid-stride loop(gridDim * blockDim) covers all works, but possible extra threads!
CPU
 ├─ Stream A → kernel launch
 │   ├─ kernel1 → Grid A
 │   ├─ kernel2 → Grid B
 │   └─ kernel3 → Grid C
 ├─ Stream B → kernel launch
 │   └─ kernel4 `kernel<<<gridDim, blockDim, sharedMem, stream>>>`
 └─ Stream C

#        ↓
# 2. CUDA runtime
# schedules thread-blocks onto SMs automatically
Grid
└── Thread Block Cluster # multiple SMs possible
    └── Thread Block / Cooperative Thread Array (CTA) # exactly ONE SM, max 1024 threads / lane
        ├── block_id:   `blockIdx.x`
        ├── block_size: `blockDim.x`
        ├── Shared Memory
        │
        └── Warp / simdgroup # SIMT execution unit, 32 threads
            ├── warp_id in CTA: `threadIdx.x / warpSize`
            │
            └── Thread # within ONE warp
                ├── lane_id: `threadIdx.x % warpSize`
                └── Registers

#        ↓
# Hardware perspective with Hopper
#
# 3. Wrap Scheduler
# spawn 32 threads with grid-stride loop coordinates & kernel
# execution same instruction with 32 threads at once
#        ↓
GPU # H100 has 132 SMs
 ├─ SM 0 # Each SM max 32 resident blocks
 │   ├─ 4 Warp Scheduler(s) # similar Hyper-Threading, so 4 active warps (4 * 32 = 128 active threads per SM) continues working on millions threads.
 │   │   ├─ Warp 0
 │   │   │   ├─ instruction # 32 threads SAME instruction.
 │   │   │   ├─ active mask # hardware implement warp divergence by mask out threads
 │   │   │   ├─ Scheduling State
 │   │   │   ├─ Thread 0
 │   │   │   ├─ ...
 │   │   │   └─ Thread 31
 │   │   ├─ Warp 1 (only 4 active Warp per SM)
 │   │   ├─ ...
 │   │   └─ Warp 63 # Wrap is NOT child, but managed by Warp Scheduler.
 │   ├─ ScoreBoard # hardware bookkeeping ALL wrap's next instruction ready
 │   ├─ Registers (per thread)
 │   ├─ Shared Memory (per block region) # Developer can control
 │   ├─ L1 cache # cache-policy through PTX
 │   └─ 128 Tensor Cores / FP units
 │
 ├─ SM 1 # with 256 KB L1 SRAM registers, shared by block
 │   └─ ...
 │
 ├─ SM 131
 │
 ├─ L2 Cache # cache-policy through PTX
 ├─ Global Memory # HBM, Developer can control
 ├─ IO Interface
 │   ├─ PCIe
 │   └─ NVLink
 └─ Copy Engine # DMA/data transfer for Global Memory

```

SM Analogy:
- SM ~ tiny computer
  - Cuda Core ~ CPU does general compute;
  - Tensor Core ~ GPU hold most FLOPs;
  - **Tensor Memory Accelerator**(TMA) ~ swap tensor tile in background;
  - **Wrap Scheduler** ~ Wrap's manager manage threads instruction & state. `latency hiding happens here`
  - Dispatch Unit ~ Router for Wrap's active thread's instruction
- instructions
  - WGMMA ~ offload heavy workload from cuda core to tensor core.
  - mbarrier ~ async completion/event flag


- error buffer is a "single-slot" & async, so never can guaranty all error messages are collected.
- Kernel indexing = mapping rule
- Launch config   = execution shape
- Unified Virtual Addressing (UVA) - Share Memory across SINGLE NODE(Ex: a NVL72)

#### Asymmetric Parallelism

> SM core's Symmetric Parallelism VS Asymmetric Parallelism, disaggregation strategy on SM scheduler.
>
> Async CUDA pipeline ≈ multiple streams + events/dependencies

Tech stacks:

- CUDA Stream - opportunistic Asymmetric Parallelism Execution.
- Green Context - Dynamic partition with guaranty. Aka define consumer/worker & routing_key.
- Multi-Process Service (MPS) - Controlled GPU partition.
- Multi-Instance GPU (MIG) - fixed GPU partition

> CUDA has 2 main libraries categories: computation libraries & Communication libraries.

computation libraries is A MESS.

```md
Async coordination
├── Kernel level
│   └── Streams + Events
│
└── Inside-kernel level
    └── Async memory operations + Barriers
```

## IO

> Memory hierarchy ~ traffic problem causes by variance vehicle: GPUs have limited high‑bandwidth memory (HBM or SRAM), while model parameters far exceed this capacity, forcing frequent off‑chip transfers.
>
> Impossible triangle: capacity, latency, bandwidth

- Global memory: maximize coalescing io
- Shared memory: avoid bank conflicts
- Register: avoid spillover

> Roofline Model: Each chip has a peak CGMA, but different workload has different CGMA.

- Arithmetic Intensity | Compute Density ~ Compute / Data @ FP16 `compute to global memory access (CGMA) ratio`
  - Workload
    - Attention ~ 10–50 FLOPs/byte
    - GEMM / MLP ~ 100–1000+ FLOPs/byte
    - decode ~ 1–10 FLOPs/byte
  - Hardware
    - H100 FP16 ~ 300 FLOPs/byte
    - Groq ~ 3 - 8 FLOPs/byte

- RAM Flush speed ~ IO / capacity≈
  - NAND ~ seconds to minutes
  - DR5 ~ 0.2–0.5× / sec
  - HBM3 ~ 10–20× / sec
  - HBM4 ~ 30× / sec
  - SRAM ~ 300k / sec

- Byte Ratio: compute FLOPs / io throughput


### RAM Types

- Registers     # 1 cycle
- L1 Cache      # 3 ~ 5 cycle
- Shared memory # 20 ~ 30 cycle
- L2 Cache      # 150 ~ 250 cycle

- HBM           # 400+ cycle
- DRAM          # 500+ cycle
  - Low Power DDR (LPDDR)
  - Dual In-line Memory Module (DIMM) `common PCIe`
  - LPCAMM2 - laptop screw in RAM

  - STX support Context Memory Storage (CMX)
    - Small Outline Compact Advanced Memory Module (SOCAMM) * 64 @ 256GB ~ LPDDR with BlueField @ 120G/s for CPU `similar to cpu pins (694), but screw on`
      - start from GB300

Analogy:
>  AI workload similar to drink(compute) water(data) from cup(HBM) through straw(SRAM).
- compute ~ drink water
  - CPU ~ drink through straw
    - DDR ~ water tank
    - CXL Memory ~ PCIe memories
  - GPU w HBM ~ drink through many straw
    - GDDR ~ water tank with more flow
    - HBM ~ water towers (stacked up water tanks)
    - SRAM ~ water cup
      - Register | Local Memory
      - Shared Memory
      - L2 Cache
- Data ~ water
- bandwidth ~ throughput
- NV speed of light ~ max Arithmetic Intensity

physic:
- electric charge
- trapped charged
- phrase change material
- magnetic state
- resistance state
- polarization

Connections:
- CXL/SXM: CPU↔device/memory standard
- NVLink
- AMD Infinity Fabric
- Consumer Grades
  - SlimSAS | MCIO ports
  - PCIe: General IOs
  - PCIe switch

Hardware designs:
- Reconfigurable data‑flow hardware vs. parallelism on existing compute units.
- skew - variances of data transfer arrival time. HBM requires within 2 picoseconds variance arrival time.
- Multiplexer - hardware circuit that load target cache into ALU. Aka hidden data movement cost.
  - Data movement is similar to ADD operation.
  - Dot Product keep large matrix inside register, load smaller vector into register. Load register similar to train, shallow register moves its data into deeper register.
- Hardware Model codesign
  - Gate Count
  - Gate Size
  - Energy Cost
  - LLM Intelligent per jew

> SXM removed: 8 pins power supply, PCIe connection, cooling & display ports; Replaced w 2 sections SXM connections: NVLink & General(power, io, display signal); cooling (70mm x 32mm)




## Other Hardwares
- Each GPU uses 16x PCIe Lanes, which caped by CPU & motherboard.
- Host RAM bandwidth
- NIC bandwidth + topology
- PSU needs separate circuit.

## Vendors

### Big 4
- Dell
- CISCO
- Lenovo
- HPE: custom solution
  - AMD prefer

### Mid providers
$200k+
- Supermicro: common for mid size company
- Celestica: hyperscaler

### Custom Hardwares
$50k ~ $100k
- https://www.octoserver.com/
- https://tinycorp.myshopify.com/

### Datacenter rental
- $150/month per KWh rent
- Preboot eXecution Environment(PXE): bare metal boot loader;
- GPU default Full Height Double Width. Often consumer GPU are slight more width;
  - Backplane: OXM or SXM GPU interconnect board;

## NEO Cloud Providers

![Neocloud Providers](https://substackcdn.com/image/fetch/$s_!vOm0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe347a756-d864-4e1b-983e-9bde22c34e53_1024x479.png)

4 types business models:
- Sell Hardware
- Cloud Rental
- White Glove Offering (include maintain service)
- API

### Amazon & Anthropic

- **Trainium** – Custom AWS hardware w runtime.
- **Bedrock** – Managed LLM service (works with Anthropic).
  - Haiku（最小最快）
  - Sonnet（中间档）
  - Opus（最大最强）三档
  - Capybara/Mythos ?


### Google

> TPU network is way harder to hot swap!

- **TPU** – Tensor Processing Units, Google’s custom AI accelerator. `wrap is small SIMD, TPU is large SIMD`
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

> Default compute precision is FP16.

> Metal Shading Language (MSL) xxx.metal kernels is lowest lower for dev.
> > Apple don't publish GPU ISA/compiler backend; Unlike NVIDIA exposes PTX;


> The ANE is not directly accessible from MLX or PyTorch.

> MLX support mxxfp8_tensor.

Apple's strategy is use Unified Memory Architecture (UMA) avoid Nvidia's TMA.

```md
Metal
├── Metal Performance Primitives | TensorOps (~ CUDA libraries)
│   └── Metal Performance Shaders
│       └── MPSGraph
│           ├── PyTorch-Metal
│           ├── Core ML
│           │   └── MetalFX
│           └── (others)
│
├── MTLComputeCommandEncoder
│   └── dispatch compute work to GPU ALU / Neural Accelerator
│
├── MTLRenderCommandEncoder
│   └── graphics/render pipeline
│
└── MTLBlitCommandEncoder
    └── move/manage GPU resources
        ├── buffer ↔ buffer copy
        ├── buffer ↔ texture copy
        ├── texture ↔ texture copy
        ├── fill buffers
        ├── mipmap generation
        └── synchronization / resource management
```

Frameworks:
- **MLX** – General Framework for Apple silicon
  - mlx[cuda] compiled into CUDA api for CUDA runtime
  - https://github.com/ml-explore/mlx-lm/tree/main/mlx_lm/models defined supported models
- **Core ML** – Optimized inference engine; leverages the Apple Neural Engine (ANE).
  - Neural Engine is similar to Tensor Core, only does matrix ops
  - VERY few frameworks uses Neural Engine, almost pointless to have it

- Instruments ~ Apple Metal Trace software

Apple GPU components:
> Each manufacturer has its own shading language.

- Shader Core ~ SM
  - ALU (int/fp/complex) ~ Cuda core
    - Special Function Unit (SFU): Accelerates certain mathematical operations like sin, cos, and log.
    - Matrix Multiply Accelerator (MMA) ~ old matrix core that uses ALU
  - M5's Neural Accelerator (NA) ~ newer tensor core
    - `execution_simdgroups` like
- SIMDgroup ~ Warp
- Threadgroup ~ Thread Block
  - Threadgroup Memory ~ Shared Memory
    - Cooperative Tensor ~ MMA fragment / WMMA
- TB DMA ~ IB


Metal API objects:
- MTLTensor
  - data plane
  - scale plane
- MTLCommandQueue `command queue`
- MTLCommandBuffer `a batch GPU kernels`
- MTLBuffer `memory pointer for GPU kernel's inputs & results`
  - c: `graph->query_by_tier[graph->active_tier]` syntax similar struct
  - Lifetime: persists while MTLBuffer exists, outlast kernel.
  - Visibility: another kernel can read it later if you bind the same MTLBuffer.
  - Address space: it is device memory, global GPU memory, not per-thread local memory.
  - Synchronization: if one kernel writes it and another reads it, ordering matters. Separate encoders in the same command buffer are ordered; separate command buffers need dependency handling.
  - Performance: device memory is slower than thread-local registers or threadgroup memory

Known Bugs:

- LIBP2P's MDNS in mac os broken

### AMD

- AMD Helios Rackscale Solution
  - MI300 ~ $20k w 192 GB, OAM connector
- Uses **HIP** to translate CUDA code to AMD GPUs.

- AITer `AMD inference kernels, like FlashInfer`

### Cerebras

whole wafer chip ~ 40GB SRAM

### Intel

Software:
- OpenVINO (Open Visual Inference and Neural Network Optimization) `in tel inference engine`
- intel/llm-scaler-vllm `custom vLLM inference engine`

Hardware:
- Intel Gaudi 3 `w 128 GB of HBM2e`
- GPU Max Series (Ponte Vecchio)


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

Chip Placement:
- center: logic core
- top: network
- bottom: IO
- surround: HBM or DRAM

Pitfall:
- 30% GPU & NVLink failures
- 17% HBM memory
- 53% network & software

signal speed ~ 2 millimeter per 1 nanosecond

decode care more about latency than throughput, and increase RAM capacity.

## Benchmark

- Dylan's InferenceMax Total Cost Ownership
- MLCommons's MLPerf
  - https://mlcommons.org/benchmarks/inference-datacenter/