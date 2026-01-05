# Code

## Python

Packages:

- networkx `Graph package`
- lancedb `database engine for all sort datatypes`

## Command fix shits

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

export PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0

# Default HuggingFace downloads folder
~/.cache/huggingface

huggingface-cli scan-cache
```

```
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


curl http://localhost:11434/api/chat -d '{
  "model": "llama2:7b",
  "messages": [
    {
      "role": "user",
      "content": "why is the sky blue?"
    }
  ],
  "stream": false,
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_current_weather",
        "description": "Get the current weather for a location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The location to get the weather for, e.g. San Francisco, CA"
            },
            "format": {
              "type": "string",
              "description": "The format to return the weather in, e.g. 'celsius' or 'fahrenheit'",
              "enum": ["celsius", "fahrenheit"]
            }
          },
          "required": ["location", "format"]
        }
      }
    }
  ]
}'

curl http://localhost:11434/api/generate -d '{
  "model": "deepseek-r1:14b",
  "prompt": "What color is the sky at different times of the day? Respond using JSON",
  "format": "json",
  "stream": false
}'

pip install open-webui
open-webui serve

/Users/xxx/miniconda3/lib/python3.11/site-packages/open_webui

```

## Pytorch

> Ask LLM `structured list of common PyTorch methods`

Tensor components:

- array: array
- requires_grad: bool
- grad: array
- recipe
  - func: np.multiple
  - args: ([1, 2])
  - kwargs: { keep_dim: true, dim=-1 }
  - parents: {0:x, 1:x}

```py
import torch
import gc

gc.collect()
torch.cuda.empty_cache()


# basic indexing: index dimension < matrix dimension; return component of matrix;
matrix[1] = [x, y]
# advance indexing: index dimension greater or unrelated matrix dimension; return expansion of index(tokens); So pytorch assumes all values within index are able to lookup.
W_E: [d_vocab: Int, d_model: Float]
tokens: Int[Tensor, "batch position"]

W_E[tokens] -> Float[Tensor, "batch position d_model"]

t.stack(x, dim=0) # combine tensors along a new dimension.
t.cat(x, dim=0) # append existing dimension

## Pytorch Math Ops
torch.add
torch.sub
torch.mul
torch.div
torch.pow
torch.sqrt
torch.exp
torch.log
torch.log1p
torch.abs
torch.sign
torch.clamp
torch.maximum
torch.minimum
torch.floor
torch.ceil
torch.round
torch.trunc

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
```

## Weight & Bias

```py
import wandb
wandb.init(project=self.args.wandb_project, name=self.args.wandb_name, config=self.args)
wandb.watch(self.model.out_layers[-1], log="all", log_freq=50)
```

## PDF

```
# Max 12G RAM
# pip install marker-pdf
# apt-get install -y libgl1-mesa-glx
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered
```

## CUDA

<https://learn.nvidia.com/courses/course?course_id=course-v1:DLI+T-AC-01+V1&unit=block-v1:DLI+T-AC-01+V1+type@vertical+block@e5689ab035a445868125e1b27a258f99>

These __global__ functions are known as kernels, and code that runs on the GPU is often called device code, while code that runs on the CPU is host code.

> CUDA is essentially divide and conquer strategy. User defined divide & conquer logic, CUDA assign SM & WRAP to execute.
>>
>> 1. CUDA wrapper(CPU part) determent divide logic: boundary, tiling size, input & output pointers ...etc
>> 2. `__golbal__` kernel(GPU part) does conquer: find sub target(with `block` & `thread`), runs desire logic, avoid out of bound.

- Hierarchy of computations
- corresponding memory space
- synchronization primitives
  - `cudaDeviceSynchronize()`
  - `__syncthreads();`
  - `__syncwarp()`

Nsight System - Advance GUI debugger

Pytorch will calculate SM size, and choice best tiling size CUDA kernel.

```c++
// CUDA Kernel function to add the elements of two arrays on the GPU
__global__
void add(int n, float *x, float *y)
{
  int i = blockIdx.x * blockDim.x + threadIdx.x;
  if (i >= n)
    return

  for (int i = 0; i < n; i++)
      y[i] = x[i] + y[i];
}

  // Allocate Unified Memory -- accessible from CPU or GPU
  float *x, *y;
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

//<<<gridDim, blockDim>>>; const
// blockIdx.x; blockIdx.y; blockIdx.z
// threadIdx.x; threadIdx.y; threadIdx.z;
// Both gridDim & blockDim supports from 1 to 3 dimensions (x, y, z)
dim3 gridDim(x, y);
dim3 blockDim(x, y, z);
add<<<gridDim, blockDim>>>(N, x, y);

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

```

### Open AI Triton
>
> Manage Memory coalescing, Schedule SMs on top of CUDA. Just better version pytorch compile.

> Let dev just work on block level, not the lower CUDA thread level.

```py
x = tl.load([start_ptr, s+1, ....s+BLOCK_SIZE])
tl.store(y_ptrs, y_row)

```

## transformers

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

''' 
model.layers.3.post_attention_layernorm: Qwen2RMSNorm((5120,), eps=1e-05)
---
model.layers.4: Qwen2DecoderLayer(
  (self_attn): Qwen2Attention(
    (q_proj): Linear(in_features=5120, out_features=5120, bias=True)
    (k_proj): Linear(in_features=5120, out_features=1024, bias=True)
    (v_proj): Linear(in_features=5120, out_features=1024, bias=True)
    (o_proj): Linear(in_features=5120, out_features=5120, bias=False)
  )
  (mlp): Qwen2MLP(
    (gate_proj): Linear(in_features=5120, out_features=27648, bias=False)
    (up_proj): Linear(in_features=5120, out_features=27648, bias=False)
    (down_proj): Linear(in_features=27648, out_features=5120, bias=False)
    (act_fn): SiLU()
  )
  (input_layernorm): Qwen2RMSNorm((5120,), eps=1e-05)
  (post_attention_layernorm): Qwen2RMSNorm((5120,), eps=1e-05)
)
---
model.layers.4.self_attn: Qwen2Attention(
  (q_proj): Linear(in_features=5120, out_features=5120, bias=True)
  (k_proj): Linear(in_features=5120, out_features=1024, bias=True)
  (v_proj): Linear(in_features=5120, out_features=1024, bias=True)
  (o_proj): Linear(in_features=5120, out_features=5120, bias=False)
)
---
model.layers.4.self_attn.q_proj: Linear(in_features=5120, out_features=5120, bias=True)
---
model.layers.4.self_attn.k_proj: Linear(in_features=5120, out_features=1024, bias=True)
---
model.layers.4.self_attn.v_proj: Linear(in_features=5120, out_features=1024, bias=True)
---
model.layers.4.self_attn.o_proj: Linear(in_features=5120, out_features=5120, bias=False)
---
model.layers.4.mlp: Qwen2MLP(
  (gate_proj): Linear(in_features=5120, out_features=27648, bias=False)
  (up_proj): Linear(in_features=5120, out_features=27648, bias=False)
  (down_proj): Linear(in_features=27648, out_features=5120, bias=False)
  (act_fn): SiLU()
)
---
model.layers.4.mlp.gate_proj: Linear(in_features=5120, out_features=27648, bias=False)
---
model.layers.4.mlp.up_proj: Linear(in_features=5120, out_features=27648, bias=False)
---
model.layers.4.mlp.down_proj: Linear(in_features=27648, out_features=5120, bias=False)
---
model.layers.4.mlp.act_fn: SiLU()
---
model.layers.4.input_layernorm: Qwen2RMSNorm((5120,), eps=1e-05)
---
model.layers.4.post_attention_layernorm: Qwen2RMSNorm((5120,), eps=1e-05)
---
model.layers.5: Qwen2DecoderLayer(
  (self_attn): Qwen2Attention(
    (q_proj): Linear(in_features=5120, out_features=5120, bias=True)
    (k_proj): Linear(in_features=5120, out_features=1024, bias=True)
    (v_proj): Linear(in_features=5120, out_features=1024, bias=True)
    (o_proj): Linear(in_features=5120, out_features=5120, bias=False)
  )
  (mlp): Qwen2MLP(
    (gate_proj): Linear(in_features=5120, out_features=27648, bias=False)
    (up_proj): Linear(in_features=5120, out_features=27648, bias=False)
    (down_proj): Linear(in_features=27648, out_features=5120, bias=False)
    (act_fn): SiLU()
  )
  (input_layernorm): Qwen2RMSNorm((5120,), eps=1e-05)
  (post_attention_layernorm): Qwen2RMSNorm((5120,), eps=1e-05)
)
--- '''

# Parameter Analysis

import torch
import torch.nn as nn
from torch.nn import functional as F

class Qwen2RMSNorm(nn.Module):
    def __init__(self, dim, eps=1e-5):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(dim))

    def _norm(self, x):
        return x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)

    def forward(self, x):
        output = self._norm(x.float()).type_as(x)
        return output * self.weight

class Qwen2Attention(nn.Module):
    def __init__(self, hidden_size, num_heads, num_kv_heads):
        super().__init__()
        self.hidden_size = hidden_size
        self.num_heads = num_heads
        self.head_dim = hidden_size // num_heads
        self.num_kv_heads = num_kv_heads

        self.q_proj = nn.Linear(hidden_size, hidden_size, bias=True)
        self.k_proj = nn.Linear(hidden_size, num_kv_heads * self.head_dim, bias=True)
        self.v_proj = nn.Linear(hidden_size, num_kv_heads * self.head_dim, bias=True)
        self.o_proj = nn.Linear(hidden_size, hidden_size, bias=False)

    def forward(self, x, kv_cache):
        # Attention Block can either process prefill(prompt tokens) or decode(single new token)
        # (Full implementation requires key-value caching and rotary positional embeddings)
        return out  # (batch, posn_Q, d_model)

class Qwen2MLP(nn.Module):
    def __init__(self, hidden_size, intermediate_size):
        super().__init__()
        self.gate_proj = nn.Linear(hidden_size, intermediate_size, bias=False)
        self.up_proj = nn.Linear(hidden_size, intermediate_size, bias=False)
        self.down_proj = nn.Linear(intermediate_size, hidden_size, bias=False)
        self.act_fn = nn.SiLU()

    def forward(self, x):
        gate = self.act_fn(self.gate_proj(x))
        up = self.up_proj(x)
        return self.down_proj(gate * up)

class Qwen2DecoderLayer(nn.Module):
    def __init__(self, hidden_size, num_heads, num_kv_heads, intermediate_size):
        super().__init__()
        self.self_attn = Qwen2Attention(hidden_size, num_heads, num_kv_heads)
        self.mlp = Qwen2MLP(hidden_size, intermediate_size)
        self.input_layernorm = Qwen2RMSNorm(hidden_size)
        self.post_attention_layernorm = Qwen2RMSNorm(hidden_size)

    def forward(self, x):
        # Simplified forward pass (actual implementation needs residuals)
        x = self.input_layernorm(x)
        x = self.self_attn(x)
        x = self.post_attention_layernorm(x)
        x = self.mlp(x)
        return x

class Qwen2Model(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.layers = nn.ModuleList([
            Qwen2DecoderLayer(
                hidden_size=config.hidden_size,
                num_heads=config.num_attention_heads,
                num_kv_heads=config.num_key_value_heads,
                intermediate_size=config.intermediate_size
            )
            for _ in range(config.num_hidden_layers)
        ])
        self.norm = Qwen2RMSNorm(config.hidden_size)

    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return self.norm(x)

# Configuration class to match your architecture
class Qwen2Config:
    def __init__(self):
        self.hidden_size = 5120
        self.num_attention_heads = 40  # 5120 / 128
        self.num_key_value_heads = 8    # 1024 / 128
        self.intermediate_size = 27648
        self.num_hidden_layers = 64
        self.vocab_size = 100000  # Adjust based on your tokenizer

# Usage
config = Qwen2Config()
model = Qwen2Model(config)
```

## MCP

__Use Cases__

- Expose Figma design to claude cli
- Expose DB cli to manage DB

<https://context7.com/>

```bash
uv run mcp install weather.py

```

[Remote MCP servers](https://glama.ai/mcp/servers)

## TensorRT

> 2~4 × improvement pytorch

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

## Visual Tools

<https://plotly.com/python/>
