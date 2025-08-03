# Code

## Python

Packages:

- networkx `Graph package`
- lancedb `database engine for all sort datatypes`

## Command fix shits

```
pip3 install torch -U

# Metal Performance Shaders (MPS)
import torch
print(torch.backends.mps.is_available())  # Should return True
print(torch.backends.mps.is_built()) 

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

```py
import torch
import gc

gc.collect()
torch.cuda.empty_cache()
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

- Hierarchy of computations
- corresponding memory space
- synchronization primitives
  - `cudaDeviceSynchronize()`
  - `__syncthreads();`
  - `__syncwarp()`

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

    def forward(self, x):
        # Implement attention logic here
        # (Full implementation requires key-value caching and rotary positional embeddings)
        return x  # Simplified return

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

<https://context7.com/>

```bash
uv run mcp install weather.py

```
