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
  - vllm H200 ~ 400tpsg | 50 output tpus @ $3/hr GLM 5.2 fp8 → $2/M tokens cost
  - Model FLOPs Utilization (MFU) > 30% good, > 40% excellent
  - Power‑to‑chip efficiency (PUE) improves from 1.8 (wasteful) to ~1.1 (effective).
  - Total Cost of Ownership: 10 % data center, 15 % power, 75 % Compute Hardwares.
  - Bottlenecks
    - Compute bound
    - Memory bound
    - Latency bound
    - Sync bound
    - Scaling bound
- Training
  - Context Growth Stages: 8k, 16k, 24k, 40k, 64k, 96k, 128k...
  - 90% Flops to pretrain; 3–7% to fine tune; 1-3% to RL;
  - Lab compute allocation: 40% inference, 50% research; 10% final training run.
  - RL is similar to lottery-yield manufacturing
  - Get high-entropy data(LLM hard to predict seq, measure by sum(log_prob))
  - Most Research are find pattern/correlation of hyper parameters in smaller LLM, project its correlation to larger LLM.
  - **Chinchilla optimal**
  - d_ff ~ 4 * d_model; FFN most often 2 layers;
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
  - Thinking ~ 85% decode tokens
- Business
  - AI industry often compares to Cloud Service Provider
  - Demand is key unknown variable, profit is adjustable by balancing training vs inference.
  - Investor allowable runway determents take off speed(intelligent) of LLM.
  - Automatic value ~ (success_task_% - failed_task_%) * task_value_$ - llm_cost_$

### Chinchilla
- Scaling Law: predictable power-law relationship between hyperparameter!
  - Allow devs forecast, and outlier detection.
  - Compute is flexible resource that can target different sections: beam search, dataset, weight...
- 1B parameters LLM needs 20B token in pre-train, takes 3 days in H100(1979e12) with 40% MFU. $$\text{Training FLOPs} \; C \;\approx\; 6 \cdot N \cdot D$$
  - 120B GPT-OSS uses range 3 trillion tokens.
- 4 ~ 16 epochs
- d_model / d_layer ~ 10 - 100

## High-Performance Computing

HPC common problems:
- Lot of small file (LOSF) may cause random unmount volumnes; patch with `autofs`

HPC components:
- VM hypervisor: Partition Resources for VM, but AI often bare metal; Ex: KVM/QEMU; Firecracker;
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

- Langfuse: Telemetry Log Across Applications
- https://github.com/The-PR-Agent/pr-agent

### Protocols

- MCP (Model Context Protocol) – inject system prompts, tool descriptions, and response formats.
- A2A (Agent‑to‑Agent) – asynchronous task assignment with status callbacks.
- ACL (Agent Client Protocol) - created by Zed, between editor to LLM.


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


## Other Companies

- https://www.primeintellect.ai/
  - Prime Agent
- Baseten `Inference SASS company`
  - Zero Data Retention. Data goes into Automated PI removal pipeline, then train, then throw away data.
  - Dedicated Inference
  - Truss `simple deployments version`
  - Iterative SFT: Self-generated rollouts repaired via feedback loops.