# AI Industry

## Model Artifact

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
- `.ckpt` pytorch checkpoint
- `.onnx` ONNX Model file also contain compute graph
- `.mlpackage` CoreML convert diffusion models for CoreML engine runs on MAC

### Block Storage Formats
> numbers ALWAYS store in blocks, within a block there is scaler & basis adjust all elements at once. superblock even have group as element.
> > default iteration order is row-major, block-by-block.
>
> > row's width **must** be divisible by the block size
>
> > filename indicates the lowest precision present in the file, not the average.
>
> > Q4_K_M or UD-Q4_K_XL as default, KV cache q8_0.

File Extension Meanings:
- Trailing _0/_1: legacy, type-0 (scale) / type-1 (scale+min)
- _K: super-blocks of 256 with quantized sub-scales.
- _NL: non-linear lookup table
- S ≈ pure base type
- M ≈ base + promoted sensitive tensors
- L ≈ base + promoted further
- IQ: codebook/lattice quants.
- _XXS/_XS/_S/_M: size grades within the bit class.
- TQ / Q1_0: ternary/binary packing for models trained at that precision;
- UD-: Unsloth Dynamic recipe.

Source code all ggml formats: https://github.com/ggml-org/llama.cpp/blob/master/ggml/src/ggml-common.h

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


Ex: IQ2_XXS ~ (66 * 8) / 256 = 2.0625 bits-per-weight (bpw) 

# Mixed-precision 
Q4_K (loaded storage format to RAM)
    ↓
dequantize (engine decides which dequantize kernel; or manually `--compute-type fp16`)
    ↓
FP16 values (inference engine dequantized FP16 at GPU's SRAM)
    ↓
multiply
    ↓
FP32 accumulation (later kernel quantize accumulation to desire precision, popular Q8_K)
```


## Inference Engine
> Inference Engine translate Model File to Engine's model structure, then map to Hardware's supported Compute Precision.
>
> Inference engine, based on its available kernels, backend, hardware, and sometimes user configuration, decides what floating-point format to dequantize into

### Inference Engine workflow
- 1. Load model file
  - `gguf` meta defined tensor layout
  - Analogy: get production line machine
- 2. Bind model tensors to engine’s model structure
  - 2.1 Read model architecture metadata
  - 2.2 Construct the engine’s model structure
  - 2.3 Engine model structure infer matrix ops from tensor name
  - 2.4 Optionally transpose, split, fuse, repack, or index matrix.
  - Notes:
    - Ex: Attention class has (Wq Wk Wv Wo; KVCache; xxx_kernel;) need memory mapping points to loaded RAM address
    - Analogy: unpack production line machine inside factory floor
- 3. Initialize backend engine (CPU, Metal, CUDA)
  - 3.1 setup weight cache, kernel buffers, workspace
  - 3.2 maps weights to accelerator
  - 3.3 manage thread pool, batch scheduler
  - Notes:
    - CUDA has hardware support dequantize + multiply + accumulate
    - Apple uses Metal Shading Language to dequantize block
    - Analogy: setup production line
- 4. Create runtime session
  - 4.1 allocate KV cache + decode scratch
  - 4.2 batch prefill
    - calculate prefill chunk starting point
    - check prompt hit KV cache
    - enqueue block kernel
      - overwrite Q scratch
      - overwrite K/V temporary representation
      - write persistent K/V cache
      - overwrite attention scratch
      - overwrite FFN scratch
      - swap hidden buffers
    - release tensor pointers
    - Notes:
      - no TP: `1 GPU barrier wait + 1 host readback`
      - with TP: `per layer barrier waits + 1 output-head wait + 1 host readback`
  - 4.3 batch decode loop
    - repeat blocks
      - enqueue kernel
      - save kv cache into store
    - enqueue output_head kernel
    - decode token & speculated ops
    - eos check & batch swap
  - Notes:
    - compute graph ~ model operations & tensor dependencies
    - Adv: distributed coordinator / TP registration
    - Analogy: feed raw material into production line
- 5. Cleanup engine & session

Weight Loading Strategy:
- Memory-mapped (file-backed)
- Tensor-backed
- Streaming
- Distributed/Sharded
- Precompiled to Engine Binary

Inference Engines:
- CoreML `Apple inference engine`
- llama.cpp
- vllm
- SGLang `uses @ xAI / chinese labs`
- **TensorRT**
  - SDK open source, but core close source. Covert pytorch modal to Nvidia kernel.
  - builtin `fused kernels` or `micro kernels`
  - 2–4× higher TPS to vllm

> Tokenizer / preprocessing / postprocessing — tokenization, chat templates, multimodal image preprocessing, sampling/logits processing, detokenization.

Settings:
- prefill-chunk size effect memory pressure vs speed
- Speculation Settings
- TP settings
  - **network protocols**: RDMA|TCP
- NUMA Aware = Non-Uniform Memory Access Aware; `aware CPU's RAM w different speeds`

### Inference Frameworks:
> There are many other tasks, get bundle w inference engine as single framework.

Common capabilities:
└── engine integration
└── TP / PP / EP
└── multi-GPU/node coordination
└── request scheduling/routing
└── model pull/load
└── API serving
└── Disaggregation
└── Software-Defined Networking (SDN)
└── Attention–FFN Disaggregation (AFD)
└── monitoring

- **Dynamo** - 2+ nodes will 2X throughput tps
  - cli run
  - Planner
  - KV Cache-aware routing
  - **NVIDIA Inference Microservices** (NIM) - ~3GB `nvcr.io/nim/nvidia/llm-nim:latest`
    - Triton Inference Engine (Docker Image)
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
- Kserver: K8s, CNCF
- AIBrix

> Distributed execution Examples: NCCL, RCCL, MPI, Ray, DeepSpeed inference, plus TP/PP implementations inside vLLM/TensorRT-LLM.


### Compute Precision
> Compute Precision are precisions have native hardware support. Hardware also can support NONE native **Block Storage Precision** at extra compute cost.

`Storage format -> Compute precision -> Accumulator precision -> Output precision`

Mac native compute precision includes: (FP16, BF16, INT8, INT4); yet llama.cpp engine w dequant support `IQ2_XXS`;

NVIDIA native support: FP8, FP6, FP4, MXFP8, and NVFP4.

**Native support vs Storage-only support**
> Note: ComfyUI fp8 on mac problem: ComfyUI backend is PyTorch; mac DON'T have native fp8 support.
> > It's simple add dequantize script, it's hard to support Mixed-precision of fp8:
>
> > llama.cpp supports a much narrower execution pattern; PyTorch must support a huge operation × dtype × backend matrix;

Mainstream@26 is same storage encoding for all components within block. Just less code/logic kernels. More flexible storage encoding can reduce storage, RAM, and IO, at the cost inference engine complexity.


### Weight Compression Algorithm
> Compression has lowest error when numbers normal/beta distribution, highest error when numbers are bipolar.

> IMO At most can have something 50% better than IQ2_XXS. Almost impossible below 1bit per weight.

Algorithm:
- Uniform Rounding (INT8, INT4)
- Block Floating Point
  - MXFP8
  - NVFP4 `B200 hardware support, similar to Q4_K storage, but faster`
- Block Quantization (Q4_0, Q4_1, Q4_K)
  - type-0 (Q4_0) `32 elements, assume symmetry: y=sx`
  - type-1 (Q4_1) `add bias: y=sx+b`
  - K-quants `256 block & 16 group elements, 2 scale levels + 1 offset level`
- Importance-aware Quantization (IQ2_XXS, IQ3_XXS, IQ3_S, IQ4_NL) `with more compute cost`
  - **codebook*: weight magnitude pattern
  - sign_pattern: weight sign_pattern
  - error scaling per block
  - IQ2_XXS dequantize: `weight[i] = global_scale × local_scale × codebook[grid_index][i] × sign_pattern[sign_index][i]`
- AWQ `focus important channel`
- GPTQ `focus minimizes result error`
- TurboQuant

**Activation-aware Weight Quantization** (AWQ)
> **Imatrix** is used to make the quantized expert weights preserve the directions that matter most for the actual MoE inputs, so the quantized model usually stays closer to the original model’s expert behavior on the kinds of prompts you calibrated on. Need create custom script for quantized the expert. or fallback `sum(row[c] * row[c])`.

**Unsloth Dynamic 2.0 Quantization**
> Need python code to output gguf formats are directly compatible with mainstream inference engines.

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


## Client

- Chat
- Agent
- UI
- **Async worker** - `async worker that send batch inference to inference engine queue, latency insensitive`


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


## High-Performance Computing

HPC common problems:
- Lot of small file (LOSF) may cause random unmount volumnes; patch with `autofs`

HPC components:
- Control Plane: Assign GPU works, spawn & kill process. Control Plane. Swap hot spare. Heal monitor.
- CheckPointer: Async save LLM state into DDR(~5min), then SSD(~30min), then HDD(~3hr).
- Data Factory:
  - Generate
  - Annotate
  - Validate
- Eval Factory: https://github.com/NVIDIA-NeMo/Evaluator
  - Checkpoint
  - Benchmark
  - Throughput
  - Cycle Time
- Inference Factory
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


## KV cache

> KV cache workflow: identify it, copy it, serialize it, restore it
>> request-level and token-level prefix cache hits

> Commonly dequantized KV cache requires custom attention kernels.

> Q & K channels with same block consistently have large outlier across many tokens;
> > Newer K keep original, older K quantized once enough K reach.
> V are more uniform.
KV approaches:

- KV cache compression
  - build-in compression; Ex: Deepseek MLA, DSA
  - math compression; Ex: TurboQuant
  - KV cache dropping; Ex: KVzip, SnackKV
- **non-prefix caching** Ex: CacheBlend
  - selective recompute % KV cache layer by layer
- **prefix caching** Ex: RadixAttention

KV cache researches:
- KV compression
- KV Blending
  - Simulate cross attention on subset KV & layers for causality, assume changes continues on token axis.
- Partial reuse
- Semantic reuse
- Cross-model reuse
- Trainable KV
- KV retrieval
- Attention steering

> KV cache has continues tendency in token axis(same channel & layer).
> > KV cache of same channel & layer across tokens is NOT sensitivity to token changes.
> 
> Shallow layer sensitivity.
> > Noise in shallow layer propagate noise father.

### KV cache Context Shifting 
> Useful when agent compress context window, shift context to <bos>, default disable.

`llama.cpp --context-shift`

### LMCache
> LMCache needs compute to warn up cache chunks, allow reusing of KV caches of multiple text chunks in one LLM input.
https://github.com/LMCache/LMCache 

- has its own demon
- block ids over ZMQ
- block
  - block_size ~ group of 256 tokens
  - parent_hash
  - hash
- KV cache pool in global DRAM, multiple inference engines can access
- multi-tier storage
  - local GPU
  - local CPU
  - Remote CPU
  - local SSD
  - Remote storage

### Mooncake
Kimi's LMCache

## Advance Inference Optimization
> Common: quantization, speculation, caching, parallelism, and disaggregation

### Prompt Compression
> Avoid KV cache from the start.

- LLMLingua
- Build-in architecture; Ex: LazyLLm 

### Speculative Decoding

Speeds up decode by predicting multiple tokens(8–16 token drafts) with **smaller** module, verify draft tokens in batch with prefill **expensive**.
  Validate by checking prefill draft token's logit within top-k(default top 1) logit.
  Also explain why most LLM objective is fully shift, otherwise this won't work.

Usually 5 tokens out of 8 draft tokens will be right; Only make sense on idol compute hardware, with batch size > 8;

Fuzzy Speculative Decoding: accept draft tokens that is NOT top token


#### SpecForge
train draft module.

`draft_cost + verify_cost + replay_cost < saved_target_decode_cost`

- Speculative Compute Cost
  - draft_cost - often cheapest part
  - verify_cost - prefill on draft tokens, often expensive
  - replay_cost - update KV cache, often part of verify process
- Speculative RAM Cost
  - `mtp.gguf`
- Efficiency Variable
  - token acceptance rate
  - high batch size reduce spare compute power
  - temperature


```c
// MTP sudo code:
e = enorm(embedding_or_previous_mtp_state);
h = hnorm(main_model_hidden_state);

e = e_proj(e);
h = h_proj(h);

x = e + h;                  // or concat(e, h), depending on tensor shapes
x = norm(x);

x = transformer_block(x, block);
logits = hc_head(x);
```

#### EAGLE
> similar to MTP, but also take mid activation & early activation as input. To get more context for most accuracy.

#### DFlash
Diffusion solve the next (16)N-token chunk jointly.

#### DSpark

- draft token includes prev draft token
- stop when draft token logit fuzzy
- DSPARK_SCHEDULER `extra skip logic`
  - many no_draft cycles
  - low average accepted drafts
  - no accepted long drafts
  - low confidence early on
  - poor measured break-even if optional timing gates are enabled
  - tail of generation has too few tokens left

```c
hidden_states = main_model_selected_layers(...);
draft_state = initialize_with_noise_or_token_context(...);

for (uint32_t i = 0; i < w->n_stages; i++) {
    draft_state = dspark_stage_forward(
        &w->stage[i],
        draft_state,
        hidden_states,
        w->block_size,
        w->markov_rank
    );
}

draft_tokens = decode_stage_output(draft_state);

// M4 dspark: verify_cost 1259 ms; replay 944 ms; draft_cost was 816 ms.
```

### Token-adaptive compute

Adaptive Computation Time (ACT) / Universal Transformer style halting. Each token decides when it has had “enough” layers.
>> Design ACT needs balance between check cost vs compute saving. Avoid early checking, check every X layers?

>> Production Env always uses batch! So efficient batch design.

- Design 1: Accumulated compute value until reach threshold
- Design 2: Keep slide window of token's projects across layers, either KL or NN decides.
- Design 3: Advance Routing (similar to MOE) support loop.

token premium effects: differences in compression rates across languages.

## Batching

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

Presentation: piktochart

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

## Agent

90% prefill and under 10% generated.

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


### Protocols

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

Common Problems:
- Read Only operations in some system still leave traces, that allow agent communicate. Ex: SEO leaves search queries history. Folder & file names can uses for communication.