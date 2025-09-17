# AI Industry

> Only list tech stacks, companies, and products here.

## Rules of Thumb

- Training requires ~4× the RAM needed for inference(weight, gradient, Adam m, v).
- RAM size > RAM speed > GPU speed.  
- H100 costs $2–$4 per hour; uses ~700 W.  
- Data‑center scale: 2024: ~30k A100 GPUs; 2025: ~100k; 2026: 300–700k.  
- Power‑to‑chip efficiency (`PUE`) improves from 1.8 (wasteful) to ~1.1 (effective).  
- Total Cost of Ownership: 10 % data center, 15 % power, 75 % GPU.  
- Large runs cost 2–4× more than research runs.  
- Output tokens(decode/RAM/slow) are ~4× as expensive as input tokens (prefill/compute/fast).
- 128k ~ 100k words ~ agent handle 3-5 source files
- 4k tokens @ 8bit ≈ ~10 GB KV cache
- Measure LLM by training-data, energy per task(cost) vs human,
- Model FLOPs Utilization (MFU) > 30% good, > 40% excellent

### Token‑per‑second Benchmarks

| Hardware  | Tokens/s |
|----------|----------|
| RTX 4090 (8B LLaMA) | 60–80 |
| RTX 5090 (8B LLaMA) | 80–100 |
| Apple M3 Max | 50–70 |
| NVIDIA H100 (8B LLaMA) | ~2000 |

### Cache Strategies

| Phase                     | Cache Type          | Description |
|---------------------------|---------------------|-------------|
| **Agentic**               | Embedding Cache     | Used only for similarity search; very limited. Does **not** save LLM token cost. |
| **Prefill**               | Tokenizer Cache     | First step; small savings; order does not matter. |
|                           | Prompt Cache        | Requires an exact prefix match; works only during the prefill phase. |
| **Autoregressive Decoding** | KV Cache            | Used for token generation. The query (latest token) changes each step, while the key and value (past tokens) remain static.<br>• Implicit cache – handled automatically by the LLM provider.<br>• Explicit cache – must be programmed. |
|                           | FlashAttention Cache| Combines KV cache with softmax optimization. |

### Precision & Quantization

- **Quantization formats**  
  - AWQ – activation‑weight quantization.  
  - GGUF – CPU‑focused.  
  - GPTQ – GPU‑focused.

- **Precisions**
  - BF16 - 8-bit exponent + 7-bit mantissa (+1 sign)
  - FP16
  - FP4 (Ollama default)
  - NF4 - Hardcoded 16 numbers -1 to 1
  - MXFP4
  - NVFP4

> Different components of Transformer has different precision needs.
>> Q, K, V, FFN, early layers are less sensitive to precision; embedding, normalization, KV cache are sensitive to precision.

> Model size matters as much as precision.

## General Landscape

- **Machine‑learning frameworks**: PyTorch, TensorFlow, FlashAttention.  
- **Model formats**: `.bin`, `.gguf`, `.safetensors`.  
- **Pre‑training** – large‑scale training (e.g., DeepSpeed).  
- **Post‑training** – LoRA, fine‑tuning, RLHF, synthetic data.

### Inference Framework

> Exclude training framework, only inference.

**Things to consider**

- intelligence
- responsiveness
- energy efficiency
- cost
- throughput

| Category | Examples |
|----------|----------|
| Research | `transformers`, `llama.cpp` |
| Inference Engine | JAX, ONNX, **TensorRT**, **vLLM**, SGLang |
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
    - Prefill Engine
      - `threshold 100 token`
      - uses top spec GPUs
    - Decode Engine
      - can done in smaller GPUs with enough RAM
  - ModelService Controller (Pod Controller)
  - Prometheus (Monitor)

- **NVIDIA Inference Microservices** (NIM) - ~3GB `nvcr.io/nim/nvidia/llm-nim:latest`
  - Triton Inference Engine
- **Dynamo** - 2+ nodes will 2X throughput tps

## Speculative Decoding

Speeds up inference by predicting multiple tokens ahead.

## Applications Overview

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

### Vision

- Multi‑model LLMs: Gemini 2.0 Flash, LLaMA‑3.2‑11B‑Vision‑Instruct, Pixtral 12B, DeepSeek VL.  
- OCR tools: Tesseract, EasyOCR.  
- Document processing: Amazon Textract, Google Document AI, pymupdf4llm, marker.

### Audio

- Whisper (OpenAI) – speech‑to‑text.  
- No open‑source audio‑to‑audio models yet; most pipelines use speech‑to‑text → LLM → text‑to‑speech.

### Coding Agent

- Cursor.sh
- Codium
- Aider
- Continue.dev
- Supermaven
- Claude Dev
- Windsurf

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

## Workflow Platforms

- Low‑code: FlowiseAI, n8n.  
- Python chains: smolagents, LangChain.

### Agent Features

- instruction hierarchy (LLM able prioritize instruction base off roles)
- Structured output parsers (system prompt + output parser).  
- Tool usage vs. explicit tool calls (e.g., Llama 3.1 lacks native tool calls; 70B works fine).  
- Penalties: presence & frequency can improve reasoning.

## Agents

- AutoGen (Microsoft)  
- ADK (Google)  

### Agent Types

- CLI agents (Claude CLI, Codex).  
- GUI agents (Continue.dev, Cursor).

## Protocols

- MCP (Model Context Protocol) – inject system prompts, tool descriptions, and response formats.  
- A2A (Agent‑to‑Agent) – asynchronous task assignment with status callbacks.

## Tools & Utilities

- Chain: predefined workflow.  
- Agent: dynamic workflow.  

### Vector Databases

- LanceDB, Pinecone, Milvus, Qdrant, Redis, Weaviate, Zilliz.

### Plugins

- PluginFlask server exposing `/upsert` and `/query` endpoints for tool integration.

## Retrieval‑Augmented Generation (RAG)

- Context size vs. RAG: summarization needs large context; translation can use RAG.  
- Strategies: reranking, query expansion, fake answer search, agentic tools, property graphs, RDF.

## Debugging & Evaluation

- Tracing: Jaeger, Langfuse.  
- GraphRAG – knowledge‑graph based retrieval.  

### Evaluation Methods

| Type | Examples |
|------|----------|
| Multiple‑choice | MMLU |
| Free‑form answer | GSM8K, TruthfulQA |
| Code generation | HumanEval |
| Long‑context | Needle in a Haystack |

## Beyond Static LLMs

- Open‑socket interruption, context caching.

### Python Ecosystem

- `litellm` – common SDK for multiple providers.````
