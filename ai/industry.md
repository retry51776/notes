# AI industry
>
> Only put tech stacks, companies, products here.

- Rule of thumb
- General
- By Applications

## Rule of thumb

- Training needs 4X RAM as inference
- RAM size > RAM speed > GPU speed
- H100 from $2/hr to $4/hr; H100 is common unit; Use 700 watts
- Data Warehouse size: 30 thousands A100 @ 2024 is Top tier, 100k @ 2025, 300k-700k @2026;
- Power to Chip `PUE` from 1.1(effective) to 1.8(wasteful);
- Total Cost Ownership `TCO` 10% Data Center, 15% Power, 75% GPU
- YOLO RUN(huge run) 2-4X of research runs;
- Output Token(generate sequential) is 4X cost of Input Token(batch process)
- Token per second (>10tps be useable)
  - 4090 on 8b llama 60-80tps;
  - 5090 on 8b llama 80-100tps; on 32b uses 24GB RAM @ 30-50tps
  - m3 max 50-70tps; MLX will 60-80tps;
  - m4 on llama 90b 7tps
  - H100 on 8b llama 2000tps
- Precision
  - Quantization
    - Formats
      - AWQ `Focus on activation weights`
      - GGUF `Focus on CPU`
      - GPTQ `Focus on GPU`
    - Precisions
      - BF16 (Brain Floating Point)
      - FP16 (Floating Point)
      - FP4 (Ollama default)
  - LLM parameter count
- Open-Source vs. Optimized Model

## Provider

- <www.runpod.io>
- together.ai
- classic cloud providers

## General

<https://semianalysis.com/>

<https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard>

<https://aider.chat/docs/leaderboards/>

<https://huggingface.co/spaces/hf-accelerate/model-memory-usage>
> Add 3GB extra memory on top estimator result. `3rd party models need RAM too`

- Machine Learning Frameworks
  - LLM model formats
    - .bin `binary file to store llm models`
    - .gguf `GGUF Format to store llama.cpp models`
    - .safetensors `support pytorch`
  - Pre Training `Build the whole model`
    - deep speed `reduce RAM for training`
  - Post Training `Adjust part of model`
    - Low-Rank Adaptation (LoRA)
    - Fine-Tuning
    - Human Feedback Reinforcement Learning
    - Synthetic AI Data
  - Inference Compute `aka thinking models`
    - Prefill phase `Process input tokens`
    - autoregressive decoding phase `Generate output one token at a time`

- Inference Engines
  - Research
    - pip packages
      - transformers `by hugging face, needs CUDA & Python`
        - PyTorch
        - Tensorflow
        - flash-attn
    - llama.cpp `most popular, no Python or CUDA dependency`
  - Production
    - JAX (Google)
    - ONNX (open-source)
    - TensorRT (NVIDIA)
    - vLLM
    - SGLang `faster continues batching`

- Speculative Decoding `speed up inference tps`

> usage statistics by Claude.ai Clio Project: <https://www.anthropic.com/research/clio>
> > Conversation -> Privatized Summary & Tags -> Cluster Groups -> Hierarchical Tree

- develop Web & mobile applications 10.4%
- Content Creation & Communication 9.2%
- Academic Research 7.2%
- Education & Career 7.1%
- Advanced AI/ML Applications 6.0%
- Business Strategy 5.6%
- Language Translation 4.5%
- DevOps 3.9%
- Digital Marketing 3.7%
- Data Visualization 3.5%

- Understanding
  - llama3.1 `very good`
  - gemini 2 flash `very good`
- LLM train by Reinforcement Learning
  - DeepSeek-R1
- Context
  - System Instructions
  - Working Context `Function Executor`
  - FIFO Queue `Queue Manager`
  - Output Tokens

Variables:

- roles `“system,” “user,” and “assistant”`

LLM Response Evaluation

- Factuality
- Sentiment
- Semantic Similarity
- String Matching
- JSON Schema Validation
- Grammar and Syntax
- Relevance and Context Adherence
- Security and Safety Checks
- Hallucination Detection

<hr/>

## By Applications

### Robot

- Physical Intelligence `openai & tesla ceo`
  - Pi Zero `Opensource physical engine`
- Boston Dynamics `google robot`
- Unitree `chinese robot`
  - G1 `$24k basic, EDU $60k`
    - Hardware
      - LiDAR
        - KISS-ICP
      - CPUs
        - 192.168.123.161 `low level control; runs c++ in 2ms loop;`
        - 192.168.123.164 `high level Jetson control; python give high level demand`
    - FSM
      - command
      - fsm_id
        - 0 `zero torque`
        - 1 `damp`
        - 2 `squat`
        - 3 `sit`
        - 4 `stand-up`
        - 200 `start: in command operation`
        - 702 `lie to stand`
        - 706 `squat-to-stand-up`
      - mode
        - 0 `static`
        - 1 `dynamic/gait`
        - 2 `feet un-loaded / airborn`
      - state <https://github.com/unitreerobotics/unitree_rl_gym/blob/757b05158058a2a8005810c2bb2e1e8667cf3f17/legged_gym/envs/g1/g1_env.py#L8>
        - damp `quiet gravity compensation`
        - stand_up `extend legs & arms; FSM Mode from 1 to 4`
        - balance_stand `continues self balances`
        - continuous_gait `free up previous demand & set to balance_stand`
          - `mode = 1` can move
        - start `FSM 200;`
          - custom commands
          - balance_stand
        - stop
        - continuous_gait
- Cosmos `Nvidia Physical Model`

### Vision

- multi-models-LLM
  - Gemini 2.0 Flash `Very Good, but not open source`
  - meta-llama/Llama-3.2-11B-Vision-Instruct `can do basic extra, but has error`
  - <https://llamaocr.com/> `fine tunned meta-llama, better, still error`
  - Pixtral 12B `open source vision engine`
  - DeepSeek VL

- Optical Character Recognition (OCR) `I don't think OCR is right approach, Directly multi models LLM should replace OCR`
  - Google tesseract-ocr
  - EasyOcr
- Document process
  - Amazon Textaction
  - Google Document AI
  - pymupdf4llm
  - marker
  - Pali Gemma 2 mix

- Tools:
  - Gephi `Graph Visualization`
  - mermaidchart `Flowchart Visualization`

### Audio

- Whisper `text to speech by open ai`

> No open source audio to audio model yet. Even o4 is audio -> text -> audio.

### Codings

Products:

- Cursor.sh `close source IDE`
- codium `close source IDE`
- Aider `shell IDE with llm support`
- Continue.dev `vs code plugin`
- Cline (prev. Claude Dev) `vs code plugin, llm edit the whole repo; similar to Cursor composer`

  - Continue.dev autocomplete templates: <https://github.com/continuedev/continue/blob/aa02e0bd630fa5700d8cb48f17b5e624b940f095/core/autocomplete/templating/AutocompleteTemplate.ts>
  - <https://github.com/continuedev/continue/blob/aa02e0bd630fa5700d8cb48f17b5e624b940f095/core/context/providers/DiffContextProvider.ts#L8>

- Variables
  - context
  - Speed vs Ability
  - template `FIM template`

- fill-in-the-middle (FIM) `aka autocomplete model, usually smaller`
  - codellama `I prefer for now, but slow`
  - qwen2.5-coder `okayish, not super impressive`
  - deepseek-coder:1.3b-base `fast, but not smart`
  - starcoder `very bad`
- instruct model `normal llm`
- Composer `shift + cmd + i; only cursor.sh, multi file edit`
- Voice to Text
  - VS Code Speech `⌥⌘V or "Hey Code"`
  - Mac Dictation `press F5`
- Manage Context Provider (MCP)

## Workflow Platform

frameworks:

- low code `always has problem with 3rd party libraries`
  - FlowiseAI
  - <https://n8n.io/>
- python chains
  - smolagents
  - langchain

features:

- structure output parser
  - `system instruction & output parser & llm need to work together, test & qa before workflow successful.`
- system message
- Prompt-Embedded Tools  VS Explicit tools Parameter
  - (Ex: llama3-groq-tool-use, because llama3.1 doesn't support it)
  - Also llama3.1:8b sucks on `tool_calls`, but 70b works fine
- presence_penalty & frequency_penalty `I prefer turn this on`

## Agent

- AutoGen `Microsoft`
- ADK `Google`
- Coding Agent
  - CLI Agent
    - claude cli
    - codex
      - agent logic <https://github.com/openai/codex/blob/7ac633b69ca92ed8a3860fdc7fed0b74342dde31/codex-cli/src/utils/agent/agent-loop.ts#L381>
      - prompt <https://github.com/openai/codex/blob/3eba86a55353f6b6f0efee19704b8d11e683b4ad/codex-cli/src/utils/agent/agent-loop.ts#L1140>
      - ~/.codex/config.yaml
      - ~/.codex/instructions.md
      - patch format `to edit files through bash`
  - GUI Agent
    - continue.dev
    - cursor
    - windsurf

## Protocol

- MCP `Model Context Protocol, aka inject System Prompt instruction & tool_desc & resp format; Cons: uses too much tokens, needs smart LLM.`
  - MCP Client `LLM Invoker`
    - LLM API
      - `add role:system instruction; <tool_name><parameter1_name>xx</parameter1_name></parameter1_value>`
    - config.json
      - type `stdio(bash) or sse(http)`
      - cmd or URL `how to start/reach MCP Server`
    - MCP Inspector `npx @modelcontextprotocol/inspector node build/index.js`
      - MCP Inspector UI 6274
      - MCP Proxy 6277
  - FastMCP Server `connection management, protocol compliance, and message routing`
    - Tool `aka endpoint`
      - args
      - desc≈
    - default local MCP proxy <http://127.0.0.1:6277/health>

- A2A `Agent 2 Agent` <https://google.github.io/A2A/#/documentation> `async, similar to assign task to worker, can get task status or callback`
  - `input-required` aka interrupt status, agent needs input
  - `tasks/sendSubscribe` uses http streaming for ongoing task

## Cool AIs

- CodeFormer `Image/movie recover & enhance AI`
- <https://beta.elevenlabs.io/voice-lab>
- <https://you.com/>
- midjourney
- Heygen.com `video generation ai`
- <https://app.suno.ai/> `music ai`

<hr >

## CICD

1. Modeling
    - Pytorch
    - Tensorflow
2. Deployment
    - NIM
3. Versioning
4. Orchestration
    - K8s
5. Compute
    - NVIDIA
      - DGX
      - RTX
    - AMD
    - Apple
6. Data
    - <https://site.financialmodelingprep.com/playground>
7. Post Deployment Services
    - Langfuse
    - Lunary

## Deployment Stacks

- Nvidia Interface Microservice (NIM)
- Local AI Workbenches
  - Model Loader(llama.cpp) `loading models & executing inference computations`
    - GPU Acceleration (CUDA, Metal)
  - UI interface
  - API/CLI Access
  - Model Management
- AI fine tunning & QA services

## Tools

- Chain: predetermine workflow
- Agent: undetermined workflow
  - Orchestra Agent `most open source llm not yet specially train for`
    - Analysis Problem
    - Decompose Task
    - Alternative Proposal
    - Evaluation & Correction
  - Sub Agent
    - Transform Agent `transform input into usable format`
      - OCR
      - PDF
      - Image
      - Audio
    - Tool Agent `decide which tool, generate input into tools`
      - Tools `utilities for llm`
    - Database Agent `crud again database`

- LanceDB `similar to SQLite, support embedded query, store files & binary data, also graph`
  - graph `nodes in a table, relationship store in another table`
- Source Grounded AI - `AI that reference some documents to answer chats`
  - Citation = `AI able to refer back where it get source`
  - Separation - `AI able to understand structure of source`
  - Filter - `AI able to find most important part source, and focus attention around that section.`

> <https://r.jina.ai/> convert any html to jina to reduce token usage

## Datastore
>
> high-dimensional vector search; Similar to pandas specialized libraries for data process;

- pinecone
- milvus
- qdrant
- redis
- weaviate
- zilliz

## Plugin

PluginFlask server

- /upsert `convert info into openapi format; Then convert text to openapi text-embedding-ada-002; Last store in Datastore format(pinecone) in our DB`
- /query `convert query_str into openapi embedding; Then use Datastore find top related records; Then return to ChatGPT`

We translate 4096 words/tokens to a LLM picture(1049 points), then let LLM draw a response picture(1049 points), then translate back.

## Filter
>
> Filter functions are designed to add, format, edit the user input. They act as middleware for pre-processing and post-processing messages.
>> Pre-LLM: Modify or validate user inputs before sending them to the LLM.
>
>> Post-LLM: Alter, enhance, or validate the LLM's responses before showing them to the user.
Filters can implement use cases like translation, logging, or toxicity filtering.

## ollama
>
> Run LLM locally, seems like just a docker wrapper.

An Ollama model package includes:

 1. Model Weights: The actual neural network weights (in a proprietary format).
 2. Tokenizer Configuration: Required for text encoding/decoding.
 3. Model Configuration: Metadata, quantization details, parameters, etc.
 4. Runtime Instructions: Optimizations for model execution.

## Retrival Augmented Generation(RAG)

strategy:

- Context Optimization
  - Reranking
  - Query Expansion
  - Fake Answer Search
  - Agentic `Given Tools; Ex: Web Crawler, Code Executor`
  - LPG（Labeled Property Graph)
  - RDF（Resource Description Framework）
- LLM Intelligent/Behavior Optimization

Citation
>
> Just run classic similarly search compare output vs input.

Problems:

- Information Sparsity `occurs when incomplete extraction result; aka context loss`

## Debug

- Jaeger `distributed tracing tool`
- Langfuse `similar to sentry.io but for LLM`
- GraphRAG `knowledge graphs`

## Evaluation

> By Methods

- Multiple-Choice (MCQ)
  - MMLU
- Free-Form Answer
  - GSM8K
  - TruthfulQA
- Softmax Probability Differences
- Code Generation
  - HumanEval
- Long-Context
  - Needle in a Haystack

> By Application

- Sentiment
- Conversation Length
- Grounding
  - LLM -> Chat with user
  - Physical AI -> Physical World Response
  = Coder -> execute code

> Products

- Arize-ai/ phoenix
- lm-evaluation-harness
Prompts:

- How many words are in your response to this prompt?
- Guess cup game, multi round.
- Jake is walking to store that is 100 meter from him, every 1 second he walks 5 meter forward, then jump 1 meter back. How many seconds will take Jake walk to store.

## Beyond static LLM

- open socket interruption
- context caching

### Python

- litellm <https://pypi.org/project/litellm/> `Common SDK`
