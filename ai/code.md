# Code

## Python

Packages:

- [plotly](https://plotly.com/python/)
- networkx `Graph package`
- lancedb `database engine for all sort datatypes`

- `litellm` – common SDK for multiple providers.
- `jaxtyping` - similar to typescript, define matrix size meaning during variable definition.
- `einsum` - syntax define matrix ops; Ex: `batch seq1 hidden, batch seq2 hidden -> batch seq1 seq2`


### MCP

__Use Cases__

- Expose Figma design to claude cli
- Expose DB cli to manage DB

<https://context7.com/>

```bash
uv run mcp install weather.py

```

[Remote MCP servers](https://glama.ai/mcp/servers)

Figma MCP:

file_key - whole design document
node_id - specific frame / component

Apple Design: <https://developer.apple.com/design/resources/>
Figma Community Design: <https://www.figma.com/community/libraries?resource_type=files>
Developer or Produce Owner should pick design from here as UX ground for agent.

### Command fix shits

```py
pip3 install torch -U

# Metal Performance Shaders (MPS)
import torch
print(torch.backends.mps.is_available())  # Should return True
print(torch.backends.mps.is_built())

# pytorch matrix defined into specific GPUs
import torch.distributed as dist
device_tensor = torch.empty(1, device="cuda:1")
# NCCL disturbed operation
dist.all_reduce(input=device_tensor, output=output, op=dist.ReduceOp.SUM)
# Group weights into bucket, once bucket excess nbytes threshold,

# For python RAY worker, NCCL to broadcast between ray workers.
import ray.util.collective as collective
collective.broadcast(self.bucket, src_rank=0, group_name=self.group_name)

export PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0

# ZeroMQ broadcasts the Python metadata describing what is inside that bucket
self.socket.send_pyobj(self.metadata) # socket is ZeroMQ
self.metadata = self.socket.recv_pyobj()


# Default HuggingFace downloads folder
~/.cache/huggingface

```bash
huggingface-cli scan-cache
```

```text
# Example ollama Model File Definition

MODEL_FILE ./mymodel.gguf

# Explicitly define runtime parameters
PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER context_length 2048

# Define system prompt (optional)
SYSTEM "You are a custom fine-tuned AI model, ready to assist."

# Set tokenizer path explicitly if needed
TOKENIZER ./tokenizer.model
```

<https://docs.openwebui.com/>

'''ls
docker login nvcr.io
export NGC_APU_KEY=xxx
export LOCAL_NIM_CACHE=/tmp/.cache/nim
'''

## Huggingface

> default path `~.cache/huggingface/hub/`

```py
# Ex: error when out of RAM
#[WARNING] Generating with a model that requires 134570 MB which is close to the maximum recommended size of 98304 MB. This can be slow. See the documentation for possible work-arounds: https://github.com/ml-explore/mlx-examples/tree/main/llms#large-models

brew install git-lfs

# pip install datasets
from datasets import Dataset

data = Dataset.from_dict({
    "question": ["What is 2+2?", "Capital of France?"],
    "answer": ["4", "Paris"]
})

data.push_to_hub("your-username/your-benchmark")

lm-eval \
    --model ggml \
    --model_args pretrained=local,base_url=http://localhost:1234 \
    --tasks piqa \
    --batch_size 8

lm-eval \
    --model hf \
    --model_args pretrained=your-model-name \
    --tasks boolq \
    --batch_size 8
```


### Transformers

> Python package by huggingface

- nn.Module `aka NN block, residual connections must exists within NN block, most common unit.`
  - nn.Linear `aka Matrix, self.q_proj(input)`

```bash
│ [commit-hash]/
│   ├── model.safetensors         # Weights
│   ├── modeling_[model_name].py  # Custom Architecture
│   ├── config.json               # Architecture
│   └── tokenizer.json            # Tokenizer

https://huggingface.co/deepseek-ai/DeepSeek-V3-0324/blob/main/modeling_deepseek.py
```

```py
# Basic

'''
x.shape = (batch_size, hidden_size=3)
gate_proj = nn.Linear(self.hidden_size, self.intermediate_size, bias=False)
gate_proj.weight.shape = (intermediate_size, hidden_size)

gate_proj(x)
= x @ gate_proj.weight.T
= (batch_size, hidden_size) @ (hidden_size, intermediate_size)
= (batch_size, intermediate_size)
'''

# Structural Inspection
print(model)
# print(model.embed_positions)

# layer detail view
for name, module in model.named_modules():
    print(f"{name}: {module}\n---")
# parameter detail view
for name, param in model.named_parameters():
    print(f"{name} | Shape: {param.shape} | Dtype: {param.dtype}")

# model source code
import transformers
print(transformers.models.qwen2.modeling_qwen2.__file__)


```

## Ollama

> Pretty much Docker for LLM containerization; layer cache, build from layers. Support OLLAMA_KV_CACHE_TYPE by default across all Models.

<https://github.com/ollama/ollama#extensions--plugins>

- Modelfile `aka Dockerfile`
- CLI `docker pull vs ollama pull; ls, ps, rm ...etc`

```shell
brew install ollama

ollama serve
ollama pull llama2:7b
ollama run llama2:7b

OLLAMA_KEEP_ALIVE=1              # 0 is unload, negative is stay in RAM,
OLLAMA_KV_CACHE_TYPE=q8_0        # storing past attention states, reducing redundant computations (default: f16)
OLLAMA_NUM_PARALLEL=1            # The maximum number of parallel requests each model will process at the same time
OLLAMA_FLASH_ATTENTION           # Reduce RAM
OLLAMA_MAX_QUEUE

http://localhost:11434

http://host.docker.internal:11434

```

## Dynamo

```bash
uv pip install 'ai-dynamo[all]'

# This just let user test prompt with LLM locally, without router, api-service
dynamo run in=http out=auto deepseek-ai/DeepSeek-R1-Distill-Llama-8B

dynamo serve graphs.agg:Frontend -f config/agg.yaml --VllmWorker.ServiceArgs.workers 4

'''agg.yaml
Frontend:
  model: deepseek-ai/DeepSeek-R1-Distill-Llama-8B
  endpoint: dynamo.Processor.chat/completions
  port:8000

Processor:
  model: deepseek-ai/DeepSeek-R1-Distill-Llama-8B
  block-size: 64

VllmWorker:
  model: deepseek-ai/DeepSeek-R1-Distill-Llama-8B
  tensor-parallel-size: 1

PrefillWorker:

'''

# Build a docker image
dynamo build
```


## Domain Specific Language

> DSL covers AI, SQL, Regex, GraphQL .... We are focus on GPU | Accelerator Programming here.

> In AI Domain, DSL has range Higher abstraction(Helion) to hardware control(PTX).

Terms:
- Tail effect
- Memory coalesce: not only initial step memory read continues, every read within kernel execution loop should read continues address.
- Occupancy
- Warp Divergence: it's okay kernel has if statement, as long as wrap's 32 threads enter SAME if result.

### Pytorch

> [General Framework](academic.md#general-frameworks) similar to numpy, with build-in support backprops, optimizer.
>
> Compiler pipeline: xxx.py > Dynamo(FX graph) > AOTAutograd(ATen) > Inductor (GPU kernels)
> > registration-based dispatch pattern

> Beginner should start with Pytorch code, then ask LLM to convert to CUDA.

https://discuss.pytorch.org/

Tensor components:
- array: array
- requires_grad: bool
- grad: array
- recipe
  - func: np.multiple
  - args: ([1, 2])
  - kwargs: { keep_dim: true, dim=-1 }
  - parents: {0:x, 1:x}

backprop_cal(grad_out: Arr, out: Arr, x: Arr)

Tools:
- torch autograd profiler
- pytorch profiler


```py
import torch
import gc

gc.collect()
torch.cuda.empty_cache()

@triton.jit(interpreter=True)

# basic indexing: index dimension < matrix dimension; return component of matrix;
matrix[1] = [x, y]
# advance indexing: index dimension greater or unrelated matrix dimension; return expansion of index(tokens); So pytorch assumes all values within index are able to lookup.
W_E: [d_vocab: Int, d_model: Float]
tokens: Int[Tensor, "batch position"]

W_E[tokens] -> Float[Tensor, "batch position d_model"]

t.stack(x, dim=0) # combine tensors along a new dimension.
t.cat(x, dim=0) # append existing dimension

# profiler
with torch.autograd.profiler.profile():

# Pytorch will auto stretch when dimension = 1;
# Many PyTorch functions take an optional keyword argument `out` for in-place execution.

# squeeze: remove target dimension, only works when target dimension.size = 1;
dim = 2
matrix.squeeze(dim)
# unsqueeze: insert new dimension
matrix.unsqueeze(3)


var_unbiased = ((x - x.mean())**2).sum() / (N - 1)
var_biased = ((x - x.mean())**2).sum() / N

# PyTorch Initializer
## Uniform family
nn.init.normal_ # curve
.uniform_ # bar & default
.trunc_normal_
.kaiming_uniform_ # GELU Default
# attention ignores gain because Multiplicative Nature of Attention

## Constant family
.zeros_
.ones_
.constant_

## xavier
## Special design distribution avoid gradient problem: [fan_out, fan_in, H, W]; fan_in = fan_in * H * W;

.xavier_uniform_ # Default/most common
.xavier_normal_

# Einstein summation with einops-style named dimensions, only contracts, reorders, or broadcasts existing dimensions.
# torch.einsum() notation FIRST, einops.einsum() matrix FIRST
y = torch.einsum("b h i d, b h d j -> b h i j", q, k)
# default Einstein will be multiplication
arr4 = einops.repeat(arr[0], "c h w -> c (h 2) w")

import einops
q = (
    einops.einsum(
        normalized_resid_pre,
        self.W_Q,
        "batch posn d_model, nheads d_model d_head -> batch posn nheads d_head",
    )
    + self.b_Q
)

# General einops rules:
#   `dim=-1` means last dimension; `dim=0` means first dimension;
#   Inside ( ), left = outer loop, right = inner loop.
#   Repeated axis name (i i) ⇒ take diagonal

# einsum()
#   Omitted axis ⇒ SUM;
#   Shared axis across inputs ⇒ MULTIPLY + SUM;

# rearrange() never changes data
# Repeat it across batch and sequence dimensions
y = einops.rearrange(x, 'b t (h d) -> b h t d', h=8)

y = einops.repeat(x, '... d -> ... batch seq d', batch=2, seq=3)

# valid reduce_ops: "mean", "sum", "max", "min", "prod"
y = einops.reduce(temps, "(h 7) -> h", reduce_ops)

# For new col/row matrix ops, must done BEFORE einsum
W_U_ext = torch.cat([self.W_U, extra_W], dim=1)


# Freeze Layers
for freeze_layer in layers:
  freeze_layer.requires_grad_(False)

assert layer0.weight.grad is None

# Pytorch multiprocessing
import torch.multiprocessing as mp
mp.spawn(
    xxx_function,
    args=(x_arg, y_arg, target_device),
    nprocs=3,
    join=True,
)

# Uses NCCL underneath, communicate between mp
import torch.distributed as dist

# Avoid race condition
atomicAdd()

# registration/dispatch pattern

.register_implementation()
.register_operator()
```



### Triton
> Develop By OpenAI, one of CUDA DSL.
> Manage Memory coalescing, Schedule SMs on top of CUDA. Just better version pytorch compile.

> Let dev just work on block level, not the lower CUDA thread level.

> Backend uses LLVM.

[Example DeepGEMM kernel](https://github.com/deepseek-ai/DeepGEMM/blob/main/deep_gemm/legacy/a_fused_k_grouped_gemm.py)

```py
x = tl.load([start_ptr, s+1, ....s+BLOCK_SIZE])
tl.store(y_ptrs, y_row)

```

Gluon: Triton give ways for dev to implement wrap specialization.

### CUDA

[Nvidia Training Course](https://www.nvidia.com/en-us/training/)

[Programming Massively Parallel Processors](https://www.cse.iitd.ac.in/~rijurekha/col730_2022/cudabook.pdf)

These __global__ functions are known as kernels, and code that runs on the GPU is often called device code, while code that runs on the CPU is host code.

> CUDA is essentially divide and conquer strategy. User defined divide & conquer logic, CUDA assign SM & WRAP to execute.
>>
>> 1. CUDA wrapper(CPU part) determent divide logic: boundary, tiling size, input & output pointers ...etc
>> 2. `__golbal__` kernel(GPU part) does conquer: find sub target(with `block` & `thread`), runs desire logic, avoid out of bound.

CUDA variable lifetime:
- Thread `int x;`
- Block `__shared__ float x[];`
- CUDA Stream
- CUDA Application `__constant__` && `__device__`

Tools:
- Nsight System - Advance GUI debugger
- nvprof

```md
CUDA APIs
├── CUDA Driver API                    # <cuda.h>
│   ├── cuInit()
│   ├── cuDeviceGet()
│   ├── cuCtxCreate()
│   ├── cuMemAlloc()
│   ├── cuLaunchKernel()
│   │
│   └── Checkpoint API
│       ├── cuCheckpointProcessLock()
│       ├── cuCheckpointProcessCheckpoint()
│       ├── cuCheckpointProcessRestore()
│       └── cuCheckpointProcessUnlock()
│
├── CUDA Runtime API                   # <cuda_runtime.h>
│   ├── cudaMalloc()
│   ├── cudaMemcpy()
│   ├── cudaLaunchKernel()
│   └── ...
│
└── CUDA C++ libraries | namespaces     # <cuda/experimental>
    └── namespace cuda::
        ├── device::
        ├── experimental::
        ├── std::
        └── mr::

GPU Kernel responsibility
│
├── 1. Work / Thread Indexing
│
├── 2. Boundary Handling
│   ├── if (i < N)
│   ├── predication / masking
│   ├── partial tiles
│   └── padding
│
├── 3. Address Calculation
│   ├── base + offset
│   ├── strides
│   ├── tensor coordinates → linear address
│   └── pointer arithmetic
│
├── 4. Global Memory I/O
│   ├── load
│   ├── store
│   ├── vectorized load/store
│   └── coalesced access
│
├── 5. Tiling
│   ├── assign output tile to CTA
│   ├── split tile among warps
│   ├── split warp tile among lanes
│   └── loop over K / sequence / reduction dimension
│
├── 6. Data Staging / Movement
│   ├── Global → Shared Memory
│   ├── Shared Memory → Registers
│   ├── async copy
│   ├── TMA
│   └── double/multi buffering
│
├── 7. Synchronization
│   ├── `__syncthreads()`
│   ├── `__synchwrap()`
│   ├── barriers
│   ├── mbarrier
│   └── producer/consumer synchronization
│
├── 8. Computation
│   ├── scalar/vector ALU
│   ├── FMA
│   ├── MMA / WGMMA
│   ├── exp / sqrt / reciprocal
│   └── comparisons
│
├── 9. Reduction
│   ├── sum
│   ├── max
│   ├── warp shuffle
│   ├── shared-memory reduction
│   └── cross-warp reduction
│
├── 10. Control Flow
│   ├── loops
│   ├── branches
│   ├── predicates
│   └── early return
│
├── 11. Type / Representation Handling
│   ├── FP16/BF16 → FP32 accumulation
│   ├── FP8 scaling
│   ├── INT4 unpacking
│   ├── dequantization
│   └── casting
│
├── 12. Inter-thread Communication
│   ├── warp shuffle
│   ├── shared memory
│   ├── atomics
│   └── distributed shared memory
│
└── 13. Output / Epilogue
    ├── scaling
    ├── bias
    ├── activation
    ├── quantization
    └── final store
```


```c++
// CUDA Kernel function to add the elements of two arrays on the GPU
__global__ void add(int n, float *x, float *y)
{
    //
    // uses Predefined variables calculate Thread Indexing
  int i = blockIdx.x * blockDim.x + threadIdx.x;
  if (i >= n)
    return

  for (int i = 0; i < n; i++)
      y[i] = x[i] + y[i];

    // Kernel memory ops
    // malloc()
    // free()
}

// loadInline() invoke kernel
from torch.utils.cpp_extension import load_inline
module = load_inline(
    name="my_cuda_extension",
    cpp_sources=cpp_src,
    cuda_sources=cuda_src,
    functions=["add_cuda"],
)

@numba.cuda.jit
def kernel_x():
    //pass

// Allocate Unified Memory -- Only CPU invokes, not inside kernel.
float *x, *y;
cudaMemcpy()
cudaMallocManaged(&x, N*sizeof(float));
cudaMallocManaged(&y, N*sizeof(float));

// Wait for GPU to finish before accessing on host; AKA thread.join()
cudaDeviceSynchronize();
...

// Free memory
cudaFree(x);
cudaFree(y);


// Profile CUDA script
nvprof ./add_cuda

// compile custom CUDA
module = load_inline(
  cuda_sources=[xxx],
  cpp_sources=[yyy],
  functions=['gelu'],
  extra_cflags=['-02'],
  verbose=True,
  name="inline_gelu",
  build_directory="var/cuda_gelu"
)

// blockIdx.x; blockIdx.y; blockIdx.z
// threadIdx.x; threadIdx.y; threadIdx.z;
// Global thread coordinate requeires x, y, z when blockDim is 3 dimensions
dim3 gridDim(x, y);
dim3 blockDim(x, y, z);
add<<<gridDim, blockDim>>>(N, x, y); // gridDim.x * blockDim.x > N

// overlapping kernel execution using streams
cudaStream_t stream1, stream2;
cudaStreamCreate(&stream1);
cudaStreamCreate(&stream2);

my_kernel<<<gridDim, blockDim, 0, stream1>>>();
my_other_kernel<<<gridDim, blockDim, 0, stream2>>>();

__global__ void warpAlignedKernel(int *x) {
    int tid = threadIdx.x;
    int warp_id = tid / 32;  // Ensure full warp executes together

    if (warp_id % 2 == 0) {  // Full warps take the same path
        x[tid] += 1;
    }
}

// Warp Matrix Multiply-Accumulate(wmma)
wmma::mma_sync(Output, M, N, Bias); // V100 by 1 wrap
wgmma.mma_async(); // H100 by 4 wraps async, but accumulator at register
tcgen05.mma(); // B100 accumulator at TMEM, reduce register pressure; & CTA-pair.

// CUTLASS mma ops (description of HOW to perform MMA)
cute::gemm(mma, A_tile, B_tile, C_tile);


```


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

#### Advance CUDA
```c++
// Declare template parameter allow CUDA compiler optimized x versions
template<int TILE_M, int TILE_N, int TILE_K>
__global__ void matmul_kernel(
    const float* A,
    const float* B,
    float* C,
    int M, int N, int K)
{

    __shared__ float As[TILE_M][TILE_K];
}
// Now compiler will compile 1 predefine kernel
matmul_kernel<64, 32, 16><<<grid64, dim3(32,8)>>>(A, B, C, M, N, K);



// EXPLICITLY issue TMA ptx instruction:

#include <cuda.h>
#include <cuda/barrier>
#include <cuda/ptx>


cuda::device::experimental::
    cp_async_bulk_tensor_2d_global_to_shared(
        &tile[0][0],
        &tensor_map,
        /* x = */ 0,
        /* y = */ 0,
        bar
    );
```


- CCCL: Cuda Core manage WHAT parallel operation do those workers perform?
  - libcu++: CUDA C++ standard facilities for general cuda
  - CUB: GPU parallel primitives
  - **Thrust**: high-level parallel algorithms, mostly HOST Library.



### CuTitle

since CUDA 13.0; **Tile IR** compile into GPU executable. Block is lowest execute unit. Array based programming.

There are both cuTile C++ & cuTile Python.

less controls then CUDA python SIMT.

> NVSHMEM PE selection partitions work across GPUs/nodes. Too advance for me.


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

### Metal


```h
// @autoreleasepool ~ @with mark variables for cleanup, except 
id result;

@autoreleasepool {
    id temp = make_object();
    result = temp;   // under ARC, result holds a strong reference
}

// result is still alive here
use(result);



//TP service thread ~ request queue, mutex/condition variable, and the service loop

```

### Specialized kernel libraries
> Many prebuild libraies for developer won't have to know PTX instructions, yet still need performance.
>
> Triton, Pytorch, Cuda are general kernels covers all ops, but here are other kernel libraries cover common complex ops.

- [GGML (High: hardware compatibility)](https://huggingface.co/blog/introduction-to-ggml)

- Host Call:
  - GGML (Highest: w multi hardware support)
  - FlashInfer (Highest)
  - cuDNN (High: Block module)
  - cuBLAS (High: matrix multiplication)
  - FlashAttention
  - custom Attention Kernels
    - FlashKDA
- Device Call:
  - CUTLASS (Mid: custom kernel)
  - DeepGEMM (Mid: matrix ops)
  - CuTe (Low: tiling + layouts)
  - WMMMA (Low: explicit MMA)
  - PTX (Low: memory control)

#### Cutlass
> nvcc compile giant template-heavy CUTLASS build, super slow. While CuTe 4 DSL Python will JIT or AOT compilation!

Hardwares:
- Pascle P40 SM61 Not support
- P100 w NVLink 1
- Tesla V100 SM70 with NCCL kernel
- A100 SM80 w `cp.async`
- H100 w TMA & WGMMA & NVLink 4 Multicast PTX instructions `multimem`
- Blackwell w TMEN

Versions:
- CUTLASS 2.* ~ bundle thread layout & data layout
- CUTLASS 3.* ~ built from CuTe
- CUTLASS 4.* ~ python `nvidia-cutlass-dsl` faster compile than c++

Layers:
- device layer
- kernel layer
- collective layer
- cute layer
- atom layer

Dirs:
- /include - Library Core
- /python/CuTeDSL/cutlass - Python Lib
  - /cute - Cute DSL Core ~ `import cutlass.cute`
  - /cutlass_dsl - DSL compiler/JIT machinery

Terms:
- SMEM descriptor: `start address & leading offset & stride offset & swizzle mode`
- SharedStorage: ShareMemory Variables struct
- warp specialization: Not every warp participates in load + compute
  - single TMA producer warp
  - Ping-pong warp specialization: 2 Consumer wrap groups interleaving Epilogue(uses ALU) & Mainloop(uses tensor core)
  - Functional specialization: two consumer warpgroups invoke different calculation units
  - AR Mode: LDMCxSTMC" (Load Multicast & Store Multicast) ~ Fused All-Reduce
    - ldmcxstmc_default_inflight_depth: chunks/fragments of the C tile can be pipelined

Cutlass Kernel Workflow:
- 1. host side
  - 1.1 Define problem
    - problem shape M,N,K
    - A/B/C dtype & layout/stride
  - 1.2 Construct kernel components
    - CTA tile shape
    - TiledMMA
    - TiledCopy
      - `tCsA ~ thread Copy share_memory A;`
      - `tCrA ~ thread Copy register A`
    - Optional Adv components
      - **Pipeline**: acquire → TMA → commit → wait → MMA → release;
        - StageCount: concurrent pipelines
      - Async TMA
      - **Warp specialization**
  - 1.3 lanuch kernel
    - gridDim: number of worker groups
    - blockDim: workers per group
    - Cluster shape: how worker groups are grouped into teams
    - Dynamic SMEM size
- 2. device side
  - 2.1 Identify CTA's work `cute.local_tile()` 
  - 2.2 Create tensor views
  - 2.3 Partition tensors `.partition_A()`
  - 2.4 Allocate storage `.make_fragment_A()` or `cute.make_rmem_tensor`
  - 2.5 MAINLOOP over K tiles: invoke kernel components
    - `load_A & load_B` or `cute.copy()`
    - MMA
    - Optional Adv components:
      - Pipeline: Async pub/sub like cycle.
      - Warp specialization
      - Async
  - 2.6 Epilogue: K reduction post-process
    - accumulator transformations
    - scaling / bias / activation / conversion
    - output layout handling
  - 2.7 Storage: to global memory


```c++
// Cutlass C++
auto row = Int<10>{}; // static Constant // (_10, 1): (5, 2) underscore prefix mean Constant
```

3 Staging:
- Pre-Stage: Python DSL -> Python AST -> Intermediate Python(Structure Capture)
- Meta Stage: Python Interpeter -> MLIR (Tracing)
- Object Stage: MLIR -> MLIR Compiler

```python
# CuTe DSL
# `@cute.jit` is entry point for host method; kernel(A).launch(...)
# `@kernel` is entry point for device method
# thr_ ~ thread

@cute.jit
def gemm()

# Often Kernel Class entrypoint happens in __call__
@cute.jit
def __call__()

# Conditional eval ON runtime, not compile time
cutlass.const_expr() 

cute.printf("x: {}", x)
cute.print_tensor()
compiled_func = cute.compile(kernel, args)

llvm.inline_asm()
```

#### CuTe
> CuTe can apple [layout](hardware.md#layout) both data & compute resources(thread's assignment). Idea is tensor shape still same, but stride does thread's assignment.
>
> Early FORTRAN function name limited by 6 characters, that is orgin of cryptic function name!
>
> Replace Old Kernel Loop Philosophy! idx = inner_product(coordnate, stride)
> > Same tensor, with different layout ~ matrix transform
>
> CuTe will compile to TileIR, bypass PTX directly compiled to SASS.

Basic Terms:
- layout: Coordinate → offset
  - **Iteration Order**: Order those coordinates are visited. Most people visualize this.
    - row_major
    - col_major
    - swizzle
  - shape: matrix's row & col
  - stide: row_increment, col_increment
- storage: any write iterator also support pointer retrieval.
  - Coordinate can be any 1D, 2D, hD
- tensor: storage_pointer + layout. `make_tensor(storage_iterator, layout)`
  - predicate tensor: mask tensor
  - MMA: M, N, K -> M, N; Tensor Core only take 2D matrixs as input.
    - M ~ row mode; often dynamic.
    - N ~ col mode; large N needs specialization.
    - K ~ reduction mode; often static, large K needs specialization.
    - P ~ batch mode that need flatten into M;


Manipulate layout(Layout Algebra operations):
- grouping layout modes: flatten matrix, tensor contractions
- right|left inverse layout:
- compliment layout: many properties
  - Left & Right identity
  - Associativity
  - Left Distributivity
- product layouts: swape element of target_layout with another layout
- divide layouts: split target_layout according another layout
- common layouts: continues offsets between 2 layouts

Tensor Operations:
- copy
  - gather: merge modes
  - scatter: split modes
  - broadcast: increase matrix dimension
  - transpose: run copy from A layout to B layout(A's transpose)
- gemm
  - transpose output matrix
  - General Tensor-Tensor contraction(GeTT): CuTe allow inner deminsion out of order.
  - convolution
- **composition**: partition = composition + slice
  - partition_A, _B, _C: kernel's thread coordinate calculation

- [Example Cute](https://github.com/NVIDIA/cutlass/blob/main/examples/cute/tutorial)
  - Index mapping: balance between scope (the ability to represent any computable index mapping) and closure (ensuring that operations on these mappings return objects within the same representation)
    - Memory Layout
    - Tiling
    - Access Distribution
    - Broadcast/Expand Dimension
    - All Aboves Combinations

- CuTe Layout Representation and Algebra: partition & combine
  - colexicographic isomorphism
  - Fast Fourier Transform (FFT)

- Compiler(heuristic)
- Metaprogram(transparent, runtime)
  - Geometry: ex: Tile, Layout, Cluster, Wrap
  - Mechanism: PipeLine, Scheduler, Epilogue
  - **Hardware**: WGMMA, TMA, SM, dType

```md
CUTLASS 3.x | nvidia-cutlass-dsl

Device layer: host-facing launch/argument API
└── `cutlass::gemm::device::GemmUniversalAdapter`
      │
      │
      ▼
Kernel layer
└── `cutlass::gemm::kernel::GemmUniversal`
      │
      ├── **Tile Scheduler**: grid-strid loop, ASSIGN work to CTA
      │   ├── Conventional: 1 C tile per 1 CTA; good for Large M,N, bad if small C
      │   ├── Stream-K(Persistent scheduling): fixed # workers, rotate work chunks; Irregular batch M/N.
      │   └── Split-K: each CTA works 1 slice of K, good for M/N are small and K is large.
      ├── **Mainloop**: inner loop of kernel
      │   ├── StageCount(PipelineDepth): concurrent tiles(pipelines)
      │   └── Atom: invoke PTX instruction
      │     ├── TMA producer: load StageCount # tiles from global into share memory
      │     └── MMA consumer
      └── **Epilogue**: Mainloop's post-processing
          └── `cutlass::epilogue::collective::CollectiveEpilogue`
```
```c++
// c3x ~ CUTLASS 3.x

// CUTLASS device-side scheduler


// Producer: publish message when TMA loaded data
while (work_tile_info.is_valid_tile) {
    collective_mainloop.load();          // TMA copy tensor tile from HBM to shared memory
    scheduler.advance_to_next_work();    // advance 1 work item
    work_tile_info = scheduler.get_current_work();
}

// Consumer: SM wraps start compute
while (work_tile_info.is_valid_tile) {
    collective_mainloop.compute();       // WGMMA / mainloop compute
    scheduler.advance_to_next_work(NumConsumers);
    work_tile_info = scheduler.get_current_work();
}

// CollectiveBuilder ~ compiler determent best layout, mainloop, TMA...

// Async barrier
shared_storage.pipelines.xxx_barrier
    //.init()
    //.arrive()
    //.wait()

```

### PTX

> Example PTX instruction, give more controls over communication/memory movement.
>
> These new PTX instruction(ex: mma.sync) often wrapped into CuTe / CUTLASS libraries for CUDA devs.
>
> L1, L2 cache PTX instruction can set police, but still no direct control.

- Flush-to-Zero(FTZ)
- 
```md
ld.global.nc.L1::no_allocate.L2::256B

ld.global
│
├── .nc                 use non-coherent/read-only path
│
├── .L1::no_allocate    don't allocate this into L1
│
└── .L2::256B           request 256-byte L2 prefetch/cache behavior


## TMA ops
tma_load(tile, tensor_map, k_offset, m_offset, barrier);
cp.async.bulk.tensor.2d.global.shared::cta.bulk_group
    [tensor_map, {x, y}],
    [smem_ptr];

## compiler to discover a TMA transfer automatically
cp.async.bulk.tensor.2d.shared::cluster.global.mbarrier::complete_tx::bytes
    [smem_addr],
    [tensor_map, {x, y}],
    [mbarrier];

## operands: Instruction arguments

## xxx.approx arithmetic 2× faster; Inline PTX script

__device__ __forceinline__ float sqrt_fast(float x) {
#if defined(__CUDA_ARCH__)
    float result;
    asm("sqrt.approx.f32 %0, %1;" : "=f"(result) : "f"(x));
    return result;
#else
    return sqrtf(x);
#endif
}
```

## Tensor Framework

> Developer directly works in IR, avoid tech stacks between General Framework and LLVM!

> So these DSL/Framework tends to focus ML primitives, not from hardware or developer. 

### Tinygrad
> Note: tinygrad is specialized alternative LLVM stacks. More pytorch competivitor than inference alternative.
- UOp (micro-operation) IR

Tensor API
      ↓
UOp graph
      ↓
scheduler / optimizer
      ↓
kernel codegen
      ↓
hardware

### candle

## TensorRT

> 2~4 × improvement pytorch
>
> Engine Directory is folder of compiled engine artifacts.
>
> **exllamav3** engine is faster for single user, but only support exl3, and fewer LLMs.

https://github.com/triton-inference-server/model_navigator 

extensions:
- .engine
- .plan

```bash
trtllm-build
trtllm-serve

# A100
nvidia-smi

export NGC_API_KEY=
echo $NGC_API_KEY

echo $NGC_API_KEY | docker login nvcr.io --username '$oauthtoken' --password-stdin

#docker pull nvcr.io/nim/nvidia/llm-nim:latest
docker pull nvcr.io/nim/nvidia/llama3.1-nemotron-nano-4b-v1.1:latest

# NVIDIA model catalog IDs
export NIM_MODEL_NAME=meta-llama/Llama-3.1-8B-Instruct
# LOCAL_NIM_CACHE is where NIM store LLM, inference engine & tokenizer
export LOCAL_NIM_CACHE=~/.cache/nim
mkdir -p "$LOCAL_NIM_CACHE"
chmod 777 $LOCAL_NIM_CACHE

# NIM only run single LLM, run multi LLM requires multiple pods
# Case 1: Generic NIM image: nvcr.io/nim/nvidia/llm-nim:latest with NIM_MODEL_PROFILE controls LLM(Ex:tensorrt_llm-A100-fp16-tp1-throughput)
docker run -it --rm --name=nim-server \
  --runtime=nvidia \
  --gpus='all' \
  -e NGC_API_KEY=$NGC_API_KEY \
  -p 8000:8000 \
  -v "$LOCAL_NIM_CACHE:/opt/nim/.cache/" \
  nvcr.io/nim/nvidia/llm-nim:latest
  list-model-profiles

# list-model-profiles will is NIM utility list opinions that Nvidia has
/v1/health/ready
/docs
/openapi.json


# Case 2: Custom build TensorRT
trtllm-build --checkpoint_dir /path/to/oss-120b \
             --gpus 0,1,2 \
             --tp_size 3 \
             --gemm_plugin float8 \
             --kv_cache_dtype fp16 \
             --max_seq_len 8192

# Search LLM from https://build.nvidia.com/, pick LLM deploy instruction
docker run -it --rm \
    --gpus all \
    --shm-size=16GB \
    -e NGC_API_KEY \
    -e NIM_MODEL_ID=openai/gpt-oss-120b\
    -e NIM_TENSOR_PARALLEL_SIZE=3\
    -e NIM_MAX_MODEL_LEN=8192\
    -e NIM_MAX_NUM_SEQS=6\
    -e NIM_GPU_MEMORY_UTILIZATION=0.85\
    -v "$LOCAL_NIM_CACHE:/opt/nim/.cache" \
    -u $(id -u) \
    -p 8000:8000 \
    nvcr.io/nim/nvidia/llama3.1-nemotron-nano-4b-v1.1:latest

# NeMo is training
# ngc registry model download-version nvidia/nemo/llama_3_8B:1.0


```

```py
import torch_tensorrt

tensor_script = torch.git.trace(model, inout_data, strict=False)
trt_model = torch_tensorrt.compile(tensor_script, inputs=[input_data], ir='ts')
```

## llama.cpp
```md
Your scalar C/C++ code
        ↓
Compiler
        ↓
SLP vectorizer
        ↓
Groups compatible scalar operations
        ↓
SIMD instructions
        ↓
ARM NEON / x86 AVX / etc.
```

```c
llama_memory_t mem = llama_get_memory(ctx);

llama_memory_seq_cp(
    mem,
    MAIN,
    SAFETY,
    0,
    fork_pos
);
```

## Mojo
> Python like syntax, but also support memory layout definetion, ownership, Compile-time params.
>
> This is more developer focus framework.
