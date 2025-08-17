# AI Industry

> Only list tech stacks, companies, and products here.

## Rules of Thumb

- Training requires ~4× the RAM needed for inference.  
- RAM size > RAM speed > GPU speed.  
- H100 costs $2–$4 per hour; it is a common unit and uses ~700 W.  
- Data‑center scale (2024): ~30 k A100 GPUs; 2025: ~100 k; 2026: 300–700 k.  
- Power‑to‑chip efficiency (`PUE`) improves from 1.8 (wasteful) to ~1.1 (effective).  
- Total Cost of Ownership: 10 % data center, 15 % power, 75 % GPU.  
- Large runs cost 2–4× more than research runs.  
- Output tokens are ~4× as expensive as input tokens (sequential generation).
- 128k ~ 100k words ~ agent handle 3-5 source files
- Measure LLM by training-data, energy per task(cost) vs human,

### Token‑per‑second Benchmarks

| Hardware | Model Size | Tokens/s |
|----------|------------|----------|
| RTX 4090 (8B LLaMA) | 60–80 |
| RTX 5090 (8B LLaMA) | 80–100 |
| Apple M3 Max | 50–70 |
| NVIDIA H100 (8B LLaMA) | ~2000 |

### Precision & Quantization

- **Quantization formats**  
  - AWQ – activation‑weight quantization.  
  - GGUF – CPU‑focused.  
  - GPTQ – GPU‑focused.

- **Precisions** – BF16, FP16, FP4 (default for Ollama).

- Model size matters as much as precision.

## Providers

- runpod.io  
- together.ai  
- Classic cloud providers  

## General Landscape

- **Machine‑learning frameworks**: PyTorch, TensorFlow, FlashAttention.  
- **Model formats**: `.bin`, `.gguf`, `.safetensors`.  
- **Pre‑training** – large‑scale training (e.g., DeepSpeed).  
- **Post‑training** – LoRA, fine‑tuning, RLHF, synthetic data.

### Inference Engines

| Category | Examples |
|----------|----------|
| Research | `transformers`, `llama.cpp` |
| Production | JAX, ONNX, TensorRT, vLLM, SGLang |

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

### Coding Assistants

- Cursor.sh, Codium, Aider, Continue.dev, Claude Dev.  

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

ai/imo.md
