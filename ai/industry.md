# AI Industry
> General Framework -> Model Formats -> Inference Engine -> Compute Hardware -> Forward Deploy Engineer

- **General frameworks**: PyTorch, TensorFlow, MLX.
  - **Pre‑training** – custom kernels, cuTile
  - **Post‑training** – LoRA, fine‑tuning, RLHF, synthetic data.

## Model Formats

Formats:
- `.safetensors` - [header JSON metadata][binary tensor blobs], source checkpoint, can convert to any runtime.
  - `model.safetensors.index.json` index for multiple `model-000x.safetensors`.
  - tensor-per-layer
  - support by mlx or llama runtimes
  - other formats: `awq`, `exl2`
    - salient weight
- `.gguf` – deployment artifact for llama.cpp-class runtimes.
  - weights split into blocks (e.g. 32/64 elements)
    - hierarchy scaling - 256 group on top 32 group
  - layout is hard-coded for GGML kernels
- `models/blobs/sha256-xxxx` Ollama Modelfile
  - similar to dockerfile bundle gguf with
    - model registry
    - versioning
    - prompt templates
    - system prompts
    - tool configs

## Inference Engine

Inference Engine workflow:
- 1. Load model file
  - `gguf` meta defined tensor layout
  - Analogy: import raw material for factory
- 2. Bind model tensors to engine’s model structure
  - Ex: Attention class has (Wq Wk Wv Wo; KVCache; xxx_kernel;) need memory mapping points to loaded RAM address
  - Analogy: prep raw material for production line
    - optimization: fuse matrix, matrix changes, build index.
- 3. Initialize backend engine (CPU, Metal, CUDA)
  - 3.1 setup weight cache, kernel buffers, workspace
  - 3.2 maps weights to accelerator
  - 3.3 manage thread pool, batch scheduler
  - Notes:
    - CUDA has hardware support dequantize + multiply + accumulate
    - Apple uses Metal Shading Language to dequantize block
- 4. Create runtime session
  - 4.1 allocate KV cache + decode scratch
  - 4.2 generate compute graph
  - 4.3 manage graph execution & tensor pipeline
  - Notes:
    - compute graph ~ model operations & tensor dependencies
    - Adv: distributed coordinator / TP registration
- 5. Cleanup engine & session


| Category | Examples |
|----------|----------|
| Research | `transformers`, `llama.cpp` |
| Inference Engine | JAX, ONNX, **TensorRT**, **vLLM**, SGLang, NVIDIA Megatron-LM / Megatron-Core |
| Inference Orchestrate Framework | llm-d, Ray, Dynamo |

- **TensorRT**
  - SDK open source, but core close source. Covert pytorch modal to Nvidia kernel.
  - builtin `fused kernels` or `micro kernels`
  - 2–4× higher TPS to vllm
- [JAX](https://developer.apple.com/metal/jax/)
  - `pip install "jax==0.4.34" "jaxlib==0.4.34" "jax-metal==0.1.1"`
  - AXLearn `Google's alternative Hugging Face transformers`
- **llm-d**: a Kubernetes-native high-performance distributed LLM inference framework; (ONLY CUDA/ROCm)
  - Gateway
  - Inference Scheduler (similar to nginx, at request level)
    - `xxx-instruct-epp-xxxx`
    - attempt to uses last Decode Engine to avoid move KV cache
    - prioritize kv cache match over workload
  - KV Cache Indexer
  - Inference-engine(vllm)
    - NIXL (NVIDIA communication library designed for fast KV-cache)
    - Prefill Engine (generate KV cache)
      - `threshold 100 token`
      - uses top spec GPUs
      - column-parallel(every seq's token at once) ops; (That's why prefill so efficient)
    - Decode Engine
      - can done in smaller GPUs with enough RAM
      - row-parallel(seq independent) ops; (That's why decode token ~4x expensive)
  - ModelService Controller (Pod Controller)
  - Prometheus (Monitor)

- **NVIDIA Inference Microservices** (NIM) - ~3GB `nvcr.io/nim/nvidia/llm-nim:latest`
  - Triton Inference Engine
- **Dynamo** - 2+ nodes will 2X throughput tps
  - cli run
  - Planner

### Compute Precision
> Compute Precision are precisions have native hardware support. Hardware also can support NONE native **Block Storage Precision** at extra compute cost.

`Storage format -> Compute precision -> Accumulator precision -> Output precision`

Mac native compute precision includes: (FP16, BF16, INT8, INT4); yet llama.cpp engine w dequant support `IQ2_XXS`;

NVIDIA native support: FP8, FP6, FP4, MXFP8, and NVFP4.

### Weight Compression Algorithm
> Compression has lowest error when numbers normal/beta distribution, highest error when numbers are bipolar.

> IMO At most can have something 50% better than IQ2_XXS. Almost impossible below 1bit per weight.

Algorithm:
- Uniform Rounding (INT8, INT4)
- Block Floating Point
  - MXFP8
  - NVFP4 `B200 hardware support, similar to Q4_K storage, but faster`
- Block Quantization (Q4_0, Q4_K)
- Importance-aware Quantization (IQ2_XXS, IQ3_XXS, IQ3_S, IQ4_NL)
  - **codebook*: weight magnitude pattern
  - sign_pattern: weight sign_pattern
  - IQ2_XXS dequantize: `weight[i] = global_scale × local_scale × codebook[grid_index][i] × sign_pattern[sign_index][i]`
- AWQ `focus important channel`
- GPTQ `focus minimizes result error`
- TurboQuant

**Activation-aware Weight Quantization** (AWQ)
> **Imatrix** is used to make the quantized expert weights preserve the directions that matter most for the actual MoE inputs, so the quantized model usually stays closer to the original model’s expert behavior on the kinds of prompts you calibrated on. Need create custom script for quantized the expert. or fallback `sum(row[c] * row[c])`.

**Runtime Quantization**
> Beside weight, there are KV cache, activation, attention score... many temporary tensors that also takes up storage can be quantize.

> Different components of Transformer has different precision needs.
>> Q, K, V, FFN, early layers are less sensitive to precision; embedding, normalization, KV cache are sensitive to precision.

**PolarQuant**
> quant - Add random rotation. Convert cartisian to polar coordinates. For normalize input & preserves dot product.

Q' · K' (quantized)
   ↓
(+ QJL correction)
   ↓
attention scores

- rotate `convert Cartesian into Spherical, same precision`
- quantize `only apply to KV, not Q; compress into 8 buckets`

3-bit PolarQuant format (2-bit quantization + 1-bit sign) with a block size of 32.
So $2^3$ = 8 buckets.

**TurboQuant**

Deterministic Compress KV cache Algorithm, apply to any LLM, enhances vector search.

> Convert KV cache into TurboQuant space, convert new Query's token into TurboQuant when inference, compute in TurboQuant space, then dequantize output into fp16. Same rotation per Layer.

Cartesian coordinates: Standard; smooth, linear gradient;
Spherical coordinates: Circle; nonlinear, coupled gradient;


### Block Storage Formats
> numbers ALWAYS store in blocks, within a block there is scaler & basis adjust all elements at once. superblock even have group as element.

```
quantization_code: (num_elements, bytes, quantization_formats)
-----------------------------------------
0: (1, 4, "F32"),
1: (1, 2, "F16"),
8: (32, 34, "Q8_0"),
10: (256, 84, "Q2_K"),
12: (256, 144, "Q4_K"),
16: (256, 66, "IQ2_XXS"),
26: (1, 4, "I32"),


Ex: IQ2_XXS ~ (66 * 8) / 256 = 2.0625

# Mixed-precision 
Q4_K
    ↓
dequantize
    ↓
FP16 values
    ↓
multiply
    ↓
FP32 accumulation
```


**Native support vs Storage-only support**
> Note: Comfyui fp8 on mac problem: ComfyUI backend is PyTorch; mac DON'T have native fp8 support.
> > It's simple add dequantize script, it's hard to support Mixed-precision of fp8:
>
> > llama.cpp supports a much narrower execution pattern; PyTorch must support a huge operation × dtype × backend matrix;


## Compute Hardware
> Reference to hardware.md

## Rules of Thumb

- Important
  - Compute
  - Data Quantity & Distribution
  - Train Time
  - Optimizer Direction
  - Stability Designs
- Hardware
  - RAM size > RAM speed > GPU speed.
  - Data‑center scale: 2024: ~30k A100 GPUs; 2025: ~100k; 2026: 300–700k.
  - H100 costs $2–$4 per hour; uses ~700 W @ 2000 TFLOPS @ FB16.
  - Model FLOPs Utilization (MFU) > 30% good, > 40% excellent
  - Power‑to‑chip efficiency (PUE) improves from 1.8 (wasteful) to ~1.1 (effective).
  - Total Cost of Ownership: 10 % data center, 15 % power, 75 % Compute Hardwares.
- Training
  - 90% Flops to pretrain; 3–7% to fine tune; 1-3% to RL;
  - RL is similar to lottery-yield manufacturing
  - Get high-entropy data(LLM hard to predict seq, measure by sum(log_prob))
  - Most Research are find pattern/correlation of hyper parameters in smaller LLM, project its correlation to larger LLM.
  - **Chinchilla optimal** - 1B parameters LLM needs 20B token in pre-train, takes 3 days in H100(1979e12) with 40% MFU. $$\text{Training FLOPs} \; C \;\approx\; 6 \cdot N \cdot D$$
  - 120B GPT-OSS uses range 3 trillion tokens.
  - d_ff ~ 4 * d_model; FFN most often 2 layers;
  - d_model / d_layer ~ 10 - 100
  - Large runs cost 2–4× more than research runs. 120B OSS uses ~ 1 trillion token research run.
    - Training requires ~4× the RAM needed for inference(weight, gradient, Adam m, v). `Because more RAM used for optimizer`
      - Zero Redundancy Optimizer(ZeRO)
      - `Batch size` $\propto$ `Learning rate`; early training gradient has low noise, small batch size sufficient; later fine tuning needs large batch to average out noise within gradient.
  - Pre-Norm ensure gradient doesn't vanish. $$x_{l+1} = x_l + F(\text{LN}(x_l))$$ where x_l does NOT effected by normalization.
  - Or move all norm layers outside residual stream, only addition to RS.
  - RMSNorm replaced LayerNorm
- Inference
  - Output tokens(decode/RAM/slow/expensive) are ~4× as expensive as input tokens (prefill/compute/fast/cheap).
  - 128k ~ 100k words ~ agent handle 3-5 source files
  - 4k tokens @ 8bit @ 120B OSS ≈ ~1 GB KV cache
  - Measure LLM by training-data, energy per task(cost) vs human
  - Inference Flop ~ 2 X tokens X parameters
- Business
  - AI industry often compares to Cloud Service Provider
  - Demand is key unknown variable, profit is adjustable by balancing training vs inference.
  - Investor allowable runway determents take off speed(intelligent) of LLM.
  - Automatic value ~ (success_task_% - failed_task_%) * task_value_$ - llm_cost_$


### Control Plane

> Assign GPU works, spawn & kill process. Control Plane. Swap hot spare. Heal monitor.

### CheckPointer

> Async save LLM state into DDR(~5min), then SSD(~30min), then HDD(~3hr).

### Data Factory

- Generate
- Annotate
- Validate

### Eval Factory

https://github.com/NVIDIA-NeMo/Evaluator

AgentBench

- Checkpoint
- Benchmark
- Throughput
- Cycle Time

### Inference Factory

- Optimize
- Build Container Image
- Validate
  - security scan
  - accuracy
  - performance
- Key controls
  - Batch size
  - tps per user
  - Prefill worker vs decode worker

## Cache Strategies

| Phase                     | Cache Type          | Description |
|---------------------------|---------------------|-------------|
| **Embedding**               | Embedding Cache     | Used only for similarity search; very limited. Does **not** save LLM token cost. |
| **Prefill**               | Tokenizer Cache     | First step; small savings; order does not matter. |
|                           | Prompt Cache        | Requires an exact prefix match; works only during the prefill phase. |
| **Autoregressive Decoding** | KV Cache            | Used for token generation. The query (latest token) changes each step, while the key and value (past tokens) remain static.<br>• Implicit cache – handled automatically by the LLM provider.<br>• Explicit cache – must be programmed. |
|                           | FlashAttention Cache| Combines KV cache with softmax optimization. |

There are 3 KV approaches:

- build-in compression; Ex: Deepseek MLA
- math compression; Ex: TurboQuant
- Increase cache hit rate;
  - Split into large context subagent; Common doc has its own system prompt;
  - Decouple Prefill vs Decode; Ex: Nvidia Dyno


## Speculative Decoding

Speeds up decode by predicting multiple tokens(8–16 token drafts) with **smaller** LLM, validate predicted token in batch(prefill/fast) with **larger** LLM(bottleneck).
  Validate by checking prefill draft token's logit within top-k logit.
  Also explain why most LLM objective is fully shift, otherwise this won't work.

Usually 5 tokens out of 8 draft tokens will be right.

### DSpark

- draft token includes prev draft token
- stop when draft token logit fuzzy

## Token-adaptive compute

Adaptive Computation Time (ACT) / Universal Transformer style halting. Each token decides when it has had “enough” layers.
>> Design ACT needs balance between check cost vs compute saving. Avoid early checking, check every X layers?

>> Production Env always uses batch! So efficient batch design.

- Design 1: Accumulated compute value until reach threshold
- Design 2: Keep slide window of token's projects across layers, either KL or NN decides.
- Design 3: Advance Routing (similar to MOE) support loop.

token premium effects: differences in compression rates across languages.

## Batching

### Pad Batching
>The last real token in ALL sequences within same batch **must share same RoPE index** to batch properly.
>> Because during prefill, attention is computed “column-wise”;
>
>> SHORTER prompt’s ROPE absolute positions DO change depending on the longest prompt in the batch.

pad token

- will mask out by attention mask
- never get through attention
- never received ROPE
- Left padding / PREFILL:
  - Ex: `<pad>    <pad>    Hello`
  - purpose: algin ALL sequences within same batch to SAME RoPE index;
  - attention is computed column-wise across the batch, so prefill sacrifices absolute position alignment for batched speed.
- Right padding / GENERATION:
  - Ex: `Hello    <pad>    <pad>`
  - attention is computed sequence-wise, independently per row;
  - The position of new tokens is computed from the cache length, not from the tensor shape.

Vllm will swap out completed slot with another request. Max out batch usage avoid padding.
Dual Batch ~ 2 micro batch

### Selective Batching

Flat & concatenate multiple MLP input sequence, so batch process all inputs with different sequence at the same time.

### Ragged Batching
>
> Also called "Packed batch"
>
> up to Jan 26, still main stream production method.
>
> Change a batch KV cache store in memory(requires pad & waste memory) to single long seq's KV cache; Uses attention mask acts as sequence segregation.

Pros:

- remove pad(memory waste)
- remove max batch seq setting
- efficient RAM allocation
- fuse RoPE into the Q·K matmul kernel
- Attention Q & Output still calculate in parallel
- FFN still calculate in parallel
- Generate new token per seq within batch

Cons:

- breaks column alignment for fast prefill RoPE;
- Memory access patterns become more irregular.
  - Tokens of the same sequence are not contiguous after decoding continues;
  - Hard to preload memory
  - memory gap/whole
- increased complexity
  - hard to debug
  - hard to distribute
  - can't FlashAttention

## Applications Overview

### Presentation

piktochart

### Deep Research Agents
>
> AI researcher DRAs. OpenAI expects this mature before 2027.

> LLM needs to improve its reasoning resilient, verified its sources.

### Robotics

- Physical intelligence (OpenAI, Tesla)
  - Pi Zero – open‑source physical engine.
- Boston Dynamics – owned by Google.
- Unitree – Chinese robot company.

#### Unitree G1 Specs (excerpt)

| Component | Detail |
|-----------|--------|
| CPUs | 192.168.123.161 (low‑level C++ loop, ~2 ms) |
|   | 192.168.123.164 (high‑level Jetson, Python control) |
| FSM States | 0: zero torque, 1: damp, 2: squat, 3: sit, 4: stand‑up, 200: start, … |

### Agent

- UX Agent
  - https://stitch.withgoogle.com/
- Coding Agent
- Workflow Agent
  - Budget
  - Security
    - Log
    - Access Manager
    - Skill market place
  - Custom Hardwares `integrate with agent skills to manage it`
    - Door Locks
    - Print
    - Projector & TV
    - Clock in/out machine
    - Headphone
- Govern System
 1. Identity / trust boundary
 2. Tool permission policy
 3. Filesystem governance
 4. Command governance
 5. Network / connector governance
 6. Audit / rollback / approval

- Google Workflow Framework
  - Agent Development Kit `Google's langchain`
  - ADK Web UI

#### Prompt Engineering for Code Generation

```json
{
  "type": "function",
  "function": {
    "name": "get_current_weather",
    "description": "Get the current weather for a location",
    "parameters": {
      "type": "object",
      "properties": {
        "location": { "type": "string", "description": "Location, e.g., San Francisco, CA" },
        "format":   { "type": "string", "description": "celsius or fahrenheit", "enum": ["celsius","fahrenheit"] }
      },
      "required": ["location","format"]
    }
  }
}
```


## Protocols

- MCP (Model Context Protocol) – inject system prompts, tool descriptions, and response formats.
- A2A (Agent‑to‑Agent) – asynchronous task assignment with status callbacks.


## Retrieval‑Augmented Generation (RAG)

- Context size vs. RAG: summarization needs large context; translation can use RAG.
- Strategies: reranking, query expansion, fake answer search, agentic tools, property graphs, RDF.

### Vector Databases

> Vector DB ONLY will NOT store chunk's Causality, only chunk's Observable State.

>> Embedding projection chunks into clusters. More that it exclude unrelate info, more than find relevant info. 

- LanceDB, Pinecone, Milvus, Qdrant, Redis, Weaviate, Zilliz.

### Context-1

User query
  ↓
Context-1 (LLM agent)
  ↓
Generate subqueries
  ↓
Hybrid retrieval (BM25 + dense, top-50)
  ↓
Rerank (cross-encoder)
  ↓
Prune / summarize / filter
  ↓
Decide: enough info?
   ├─ No → issue new query (loop)
   └─ Yes → return final docs


## Debugging & Evaluation

- Tracing: Jaeger, Langfuse.
- GraphRAG – knowledge‑graph based retrieval.


## Beyond Static LLMs

- Open‑socket interruption, context caching.
- Google Titan

### Python Ecosystem

- `litellm` – common SDK for multiple providers.
- `jaxtyping` - similar to typescript, define matrix size meaning during variable definition.
- `einsum` - syntax define matrix ops; Ex: `batch seq1 hidden, batch seq2 hidden -> batch seq1 seq2`

## Memory Architecture

- Google’s TITANS and MIRAS / MORAS
  - Contextual Memory Module
    - Inject context into main LLM RS from another AI Contextual Memory Module
  - Customize parameters per user
    - Help Main LLM process/adapt injected context

- Meta's Code World Model (CWM) https://arxiv.org/pdf/2510.02387
  - Training data is a text format of function's execution stacktraces.
  - The problem with source code don't show LLM variables transition/transformation. This stacktrace will help LLM see/understand detail working of code.
    - “episodify” execution stacktraces
      - Begin with <|frame_sep|> followed by the event token which can be <|call_sep|>, <|line_sep|>, <|return_sep|> or <|exception_sep|>.
      - After <|call_sep|> or <|line_sep|> put the local variable states as dictionary in JSON format followed by the <|action_sep|> token and the current source code line.
      - After <|return_sep|>, <|exception_sep|> directly put the <|action_sep|> token and the current source code line followed by an <|arg_sep|> token and the return or exception arguments.
    - attach relevant source code
    - attach semantic context
      - desc
      - unit tests: given input, expected output
    - execution commands
    - execution results
    - review result

  - Mutate-fix task `introduce bug on work code, let LLM fix broken code`
  - Issue-fix task `open Github PR on github issue`
  - Deduplication `concatenation all actions, have another LLM train to learn these trajectories, only train with not predictable trajectories.`
  - Construct Input/Output task
  - Future task
    - Jump from section to another


## Safety

- DeepMind: Frontier Safety Framework (FSF)
  - Critical Capability Levels (CCLs)
  - Early warning tests
- Anthropic: Responsible Scaling Policy (RSP)
  - AI Safety Levels (ASL)
  - Project Glasswing2
- OpenAI: Preparedness Framework

- Mesa-optimizers

- H-Neurons drive the AI to be overly compliant and eager to please the user.

removes LLM censorship: https://github.com/p-e-w/heretic
