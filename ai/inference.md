# Inference
> Mostly focus on Inference Engine & Framework. Here assume you well aware academic.md & hardware.md.

## Analogy

> Logistics Manager(Inference Engineer) that orchestrate many Postman & Cargos through rail network.
> > Don't focus on geography interpretation, rather focus on traffic management aspect.
> 
> > Postman only carry cargos within his section. Postman won't travel the whole network.
>
> This network composite of Cities, and stopover between cities.
>
> Postman follow pickup route(prompt) to pickup & delivery cargos, until postman exhausted.
> > Pickup route(prompt) order MATTERS: Dallas → London → Paris → HongKong[10,945 miles] != Dallas → Paris → Hong Kong → London[16,910 miles]
>
> > When prefix pickup route is identical, cargos also identical.
>
> > All postman start from special token `<bos>`, and end at `<eos>`.
>
> Cargos are City's artifacts: impression, products, or history.
> > Ex: Texas ~ Big, Oil, Cowboys
> 
> New joinery's stopover needs past cargos.
> > Ex: Currently have "Cold" as past cargo, now postman more likely goes to London than Texas.


Artifacts:

- Weights ~ Postman
- Data ~ Cargos & Postman
- Different LLM ~ Different Worlds.
- Inference Job ~ Exploring World.

- Model File ~ All Postman & Hierarchy
  - Model Block ~ Stopover Group
    - Attention Head ~ Railcar Group, parallel cargo loading
      - Q ~ Postman's current looking for cargos
      - K ~ Cargo's Key or index
      - V ~ Cargo's Value
  - Model Depth ~ Number of Stopover

- All Tokens ~ Whole Route
  - Prompt Tokens(Input) ~ Pickup Route
    - Token ~ Train Station Code
      - `<EOS>` ~ THE final city when postman exhausted
  - KV cache ~ Past Cargos


- GPU command buffer ~ Train Manifest
  - Input & output matrix ~ Postman & Cargo
  - GPU kernels ~ Trip Sheet, which directions
  - Pipeline state ~ Train state

Operations:
- Inference Framework ~ Orchestrate Overall Traffic
  - Inference Engine ~ Orchestrate Station(s) Traffic
    - Load Model ~ Postman clock in to work
    - Tokenizer ~ Translation between City Name and Train Station Code
    - Prefill
    - Decode
  - KV cache orchestration ~ cargos management

> Prefill ~ sent MANY postman to ship & receive cargos to many cities at once
> > --chunk-size ~ how MANY postman sent to Station at once
> 
> > at each block(stopover), past token also sent its KV(cargo) to future tokens(trigger casual effect). 

> Decode ~ sent one postman & past cargoes to DISCOVERY MISSION to find new CITY, until postman exhausted.
> > can't parallel, because we don't know next city

Hardwares:
- Node ~ Train Station
  - CPU ~ Train Station Manager
    - Manage between HBM and storage ~ transfer cargo between station and warehouse
  - GPU ~ Train Terminal, 8 terminals per Station
    - FLOPS ~ Train Engine's HP
    - support kernels ~ Different Train Terminals supports different train size, train width....
    - SRAM ~ Train's cargo capacity
    - HBM ~ Terminal's cargo capacity
  - IO ~ Traffic
  - Storage
    - DDR ~ station's parking lot `near station, but rain can destroy cargos`
    - SSD ~ warehouse near station
- Multi Nodes ~ Train Network
  - PD disaggregated ~ Transfer Hub Design
  - IB switch ~ rail between stations or directly between terminals across stations

> Solving city traffic is HARD, because different vehicle has different capacity, speed, latency.

> The key is more async processes to utilize most IOs, avoid redundant traffic.
> > Compute IO overlapping ~ Train head detach railcar, let railcar uploading on side, and attach another loaded railcar and take off.
>
> > Smart system will always have shuttle bus run between airport & warehouse. Not wait til cargo arrived.
> 
> Why not increase train capacity? Longer cargos loading time.
> > Onboard time often longer than train head pull railcar time.
>
> > Just like container changes shipping, block/page/batch transfer has huge effect on IO.

> Quantization & Dequante ~ remove cargo packaging, compress into smaller form
> > Quantization & Dequante should only happen inside kernel. Analogy break, but important note: don't decompress cargos in Station, only decompress small % cargos inside Train on demand.

IO:
- Transfer Modes
  - Local: Within Terminal
  - Node: Within Station
  - P2P: Directly to Terminal
  - Remote: to warehouse
- Transfer Hardwares
  - Spectrum ~ Fiber Hardware
  - IB ~ Access directly to Terminal without security check
  - NVLink
  - Infinity Fabric
  - CXL
- Memory Allocator

> two_tokens_casual_paths = (num_token_in_between + num_blocks) / num_blocks * (routes_per_block ^ num_blocks)


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
- TGI
- **TensorRT**
  - SDK open source, but core close source. Covert pytorch modal to Nvidia kernel.
  - builtin `fused kernels` or `micro kernels`
  - 2–4× higher TPS to vllm

> TensorRT/TensorRT-LLM & MLX/MLX-LM is same idea: decouple kernel vs LLM mapping.

> Tokenizer / preprocessing / postprocessing — tokenization, chat templates, multimodal image preprocessing, sampling/logits processing, detokenization.

> XXX Pipeline includes multiple kernels.

Settings:
- prefill-chunk size effect memory pressure vs speed
- Speculation Settings
- TP settings
  - **network protocols**: RDMA|TCP


### Inference Frameworks:
> There are many other tasks, get bundle w inference engine as single framework.

Common capabilities:
└── engine integration
└── TP / PP / EP
└── multi-GPU/node coordination
└── request scheduling/routing
    └── refuse request when busy
└── model pull/load
└── API serving
└── Disaggregation
└── Software-Defined Networking (SDN)
└── Attention–FFN Disaggregation (AFD)
└── monitoring
└── Semantic Router
    └── Named Entity Recognition (GLiNER)
    └── Redaction (presidio) & Recover
    └── Guardrail

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

> K8s assume fungible compute is false in inference, yet k8s orchestration still useful.

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

> Note: Smaller LLM are more sensitive to compression!

Algorithm:
- Uniform Rounding (INT8, INT4)
  - W4A8 (4-bit Weights, 8-bit Activations)
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


## Kernels

> Dispatch single **CUDA Graph** is faster than individual kernels(Eager execution).

- DS4MetalTensor
  - MTLBuffer ~ memory pointer for GPU
  - offset
  - owner
  - live_snap & peak_snap

- MTLCommandQueue `command queue`
- MTLCommandBuffer `a batch GPU kernels`
- MTLBuffer `memory pointer for GPU kernel's inputs & results`
  - c: `graph->query_by_tier[graph->active_tier]` syntax similar struct
  - Lifetime: persists while MTLBuffer exists, outlast kernel.
  - Visibility: another kernel can read it later if you bind the same MTLBuffer.
  - Address space: it is device memory, global GPU memory, not per-thread local memory.
  - Synchronization: if one kernel writes it and another reads it, ordering matters. Separate encoders in the same command buffer are ordered; separate command buffers need dependency handling.
  - Performance: device memory is slower than thread-local registers or threadgroup memory

Optimizations:
- Persistent Kernels
- Memory Coalescing
- superkernel - reduce kernel swap by multi ops
- microbatch - split training batch into smaller batches
- flashcomm
- command-buffer schedules `how often CPU dispatch kernels`
- compiler cache - kernel re-use
- Placement Driver (PD) dispatcher
- SWAP_AB: Run smaller ops individually on inputs often faster then single ops on larger output.

- Thread Block Clusters - multiple SMs works on same SRAM
- Stationary Data/Array - in-place execution data
- Very Long Instruction Word (VLIW) - Compiler optimization
- Threadgroup walk order - increase cache hit rate(because x,y index increase slowly)
- Decode Context Parallelism (Flash-Decoding) - like prefill chunk, but split token's KV cache attention head when decode; `--decode-context-parallel-size 4`


### Compute Precision
> Because each `operation × dtype × backend matrix` requires unique kernel.

- CPU default FP32 AVX kernel
- MAC default FP16
- NVIDIA has many compute precision, NVFP4 is common inference precision


## Disaggregation

### Encoder-Prompt-Decode (EPD)

### Prefill Decode Disaggregation (PDD)
- Prefill REQUIRES ALL KV cache ready, also current compute batch.
- Decoder can start or load KV later
- Often 2x token throughput

### MoE Expert Disaggregation

### Attention–FFN Disaggregation (AFD)
> LSU for FFN; GPU for attention;

### Draft / Verify Disaggregation

## Parallelism Strategies

- Data Parallelism (DP): Replicate the whole model on each GPU; split data **batches**.
  - **Data Parallel Attention** (DPA): gives each request a “home GPU” for Attention/KV. Trading extra replicated attention-weight memory for independent attention execution and local KV caches.
- Pipeline Parallelism (PP): Split the model across **layers**; each GPU processes a different stage.
- Sequence Parallelism (SP): Partition long input **sequences** across GPUs. (useful for long context)
  - Ring Attention(Ring All Reduce): split Attention into chunks, share KV to neighbor.
- Tensor Parallelism (TP): Split **individual tensor(dim)** operations across devices (often less efficient).
  - Nvidia build optimize LLM image with tp1(single GPU), tp4(split attention head in 4 GPUs)
- Expert Parallelism (EP)
  - Elastic EP: hot expert & expert redundance


- all-reduce operation - very expensive operation; Ex: sync local gradient for global gradients.

## Advance Inference Optimization
> Common: quantization, speculation, caching, parallelism, and disaggregation

### Prompt Compression
> Avoid KV cache from the start.
> > Pro is universal, Con is no granular.

- LLMLingua
- Build-in architecture; Ex: LazyLLm 

### Speculative Decoding

Speeds up decode by predicting multiple tokens(8–16 token drafts) with **smaller** module, verify draft tokens in batch with prefill **expensive**.
  Validate by checking prefill draft token's logit within top-k(default top 1) logit.
  Also explain why most LLM objective is fully shift, otherwise this won't work.

Usually 5 tokens out of 8 draft tokens will be right; Only make sense on idol compute hardware, with batch size > 8;

Draft Token Accept Rule:
- greedy decoding
- **Fuzzy Speculative Decoding**: accept draft tokens that is NOT top token
- Probabilistic Acceptance: re_norm[drop_neg(target_logit - draft_logit)]

https://huggingface.co/collections/RedHatAI/speculator-models

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



## KV cache

> KV cache workflow: identify it, copy it, serialize it, restore it
>> request-level and token-level prefix cache hits

> Commonly dequantized KV cache requires custom attention kernels.

> Q & K channels with same block consistently have large outlier across many tokens;
> > Newer K keep original, older K quantized once enough K reach.
> V are more uniform.

> KV cache is even HARDER to compress than weight, at least weight static, KV cache is unique per trajectory.
KV approaches:

- KV cache compression
  - build-in compression; Ex: Deepseek MLA
  - Quantization & Precision Reduction; Ex: TurboQuant
  - KV cache dropping; Ex: KVzip, SnackKV, KVcompact `sequence-length compression`
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
- https://github.com/NVIDIA/kvpress

> KV cache has continues tendency in token axis(same channel & layer).
> > KV cache of same channel & layer across tokens is NOT sensitivity to token changes.
> 
> Shallow layer sensitivity.
> > Noise in shallow layer propagate noise father.

- **Preemption**: temporarily stopping one request so its GPU resources—especially KV-cache memory—can be used by another request.

### KV cache Context Shifting 
> Useful when agent compress context window, shift context to <bos>, default disable.

`llama.cpp --context-shift` 

llama.cpp manage KV cache in contiguous ranges, with context checkpoints;

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
Kimi's LMCache, large scale distributed network.

JSONL traces will define workload's size, but not same content.


## Llama.cpp
- Thread Allocation
- Mlock: memory residency avoid OS evict
- TP control

## vLLM
> Single Node w single or many GPU(s).
> > Everyone hates vLLM, yet they fork it!

- Prefix Aware Router
  - Message Queue
  - Replica selection
  - https://github.com/vllm-project/semantic-router
- [vLLM Scheduler](#scheduler) `batch / execution plan && coordinates the GPU worker(s)`
  - `scheduler_cls`
  - prefill/decode balancing
  - token budget
    - chunk size
    - kv cache
    - spec tokens
  - chunk size/splitting
  - request priority & preemption
  - Worker per GPU
- [ModelRunner](#inference-engine-workflow)
  - Attention backend
  - Sample/Decode/Draft
- [KVCacheManager](#kv-cache)
  - KV Connector
    - NIXL
      - NVLink
      - PCIe
      - InfiniBand / UCX
- DP Coordinator
  - RPC
- Flags:
  - `--gpu-memory-utilization`
  - `--tensor-parallel-size`
  - `--attention-backend` & `--moe-backend`
  - `--block-size` KV block size default 16; `--kv-cache-dtype`
  - `--tp --ep` DPA = DP & EP
  - structured output: (xgrammar)

Pin:
- vLLM 0.x.y
- PyTorch 2.x
- CUDA 12.x
- driver xxx

https://recipes.vllm.ai/
https://carbonforge.ai/en/models

> vllm compile `xx.so`, then `vllm serve xyzModel` will auto load compile so file.
> > `xx.so` is toolbox of kernels and native ops.

FlashInfer is kernel libraries, fork vLLM often for overwrite FlashInfer usage.

### Scheduler
> Scheduler step/batch is like train job: train capacity ~ batch token budget; 

- mixed prefill-decode batching

## Dynamo
> Multi Nodes, at least multiple DGX or NVL72.

- Dynamo Operator
  - optional: https://github.com/ai-dynamo/grove
- Discovery
- Frontend
  - Prefix Aware Router
  - PrefillRouter


## NV Helper Tools

- NVIDIA Triton Model Analyzer `Deployment Autotuning`
- [NVIDIA GenAI-Perf](https://github.com/ai-dynamo/aiperf) `End-to-end Benchmark tools`
- NVIDIA Model Optimizer `Model Optimization: quantization, distill, Neural Architecture Search`

## Monitor
- KV hit %
- TPS
- Batch Slot %
- Queue Wait Time
- Goodput % `exclude timeout tokens`

## Semantic Router
- Envoy — Gateway
  - proxy
- Router - Inspect request and decide model/path/policy
  - Signals
  - Decision Engine
    - decisions
      - priority
      - rules
      - plugins: `action`
      - modelRefs: `target LLM`
    - Plugin Chain
- dashboard
  - SIM container: `Simulator`
  - config.yaml