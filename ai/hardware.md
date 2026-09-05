# Hardware

> Ultimately, the only limitation is chip real estate; space must be allocated to computation (flexible or efficient) or storage (latency or bandwidth or capacity).


## Runtime Workflow

### Compiler Pipeline

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

### Intermediate Representation

> IR represent the program in an intermediate form that is easier to analyze, transform, optimize, or retarget. Compiler engineer's territory.

> Just like SQL has many forms, IR has many versions.

> Each manufacturer has its own shading language.

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




### Hardware Scheduling
>CPU & GPU Execution Datapath
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

## Memory

> Memory hierarchy ~ traffic problem causes by variance vehicle: GPUs have limited high‑bandwidth memory (HBM or SRAM), while model parameters far exceed this capacity, forcing frequent off‑chip transfers.
>
> Impossible triangle: capacity, latency, bandwidth


> Each chip design with a FIXED Arithmetic Intensity, but different workload has different Arithmetic Intensity.

- Arithmetic Intensity | Compute Density ~ Compute / Data @ FP16
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
- **GPU memory** hides latency by interleaving many threads. Unlike CPUs, where context switches are expensive, GPU threads are lightweight and scheduled by hardware.


### RAM Types

- DRAM
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
      - Register 1 cycle access
      - Shared Memory
      - L2 Cache
- Data ~ water
- bandwidth ~ throughput
- NV speed of light ~ max Arithmetic Intensity

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

> Default compute precision is FP16.

> Apple don't publish GPU ISA/compiler backend; Unlike NVIDIA exposes PTX;

```md
Metal
├── Metal Performance Primitives / TensorOps
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

- **MLX** – General Framework for Apple silicon
  - mlx[cuda] compiled into CUDA api for CUDA runtime
  - https://github.com/ml-explore/mlx-lm/tree/main/mlx_lm/models defined supported models
- **Core ML** – Optimized inference engine; leverages the Apple Neural Engine (ANE).
  - Neural Engine is similar to Tensor Core, only does matrix ops
  - VERY few frameworks uses Neural Engine, almost pointless to have it


Instruments ~ Apple Metal Trace software

Apple GPU components:

- Shader Core ~ SM
  - ALU (int/fp/complex) ~ Cuda core
    - Special Function Unit (SFU): Accelerates certain mathematical operations like sin, cos, and log.
    - Matrix Multiply Accelerator (MMA) ~ old matrix core that uses ALU
  - M5's Neural Accelerator (NA) ~ newer tensor core
    - `execution_simdgroups` like
- SIMDgroup ~ Warp
- Threadgroup ~ Thread Block
- TB DMA ~ IB


> The ANE is not directly accessible from MLX or PyTorch.

Apple's strategy is use Unified Memory Architecture (UMA) avoid Nvidia's TMA.

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

## Benchmark

- Dylan's InferenceMax Total Cost Ownership
- MLCommons's MLPerf
  - https://mlcommons.org/benchmarks/inference-datacenter/