# AI industry
>
> Only put tech stacks, companies, products here.

- General
- By Applications

## General

[oobabooga](https://oobabooga.github.io/benchmark.html)

[aider for code]https://aider.chat/docs/leaderboards/


- Machine Learning Frameworks
  - LLM model formats
    - .bin `binary file to store llm models`
    - .gguf `GGUF Format to store llama.cpp models`
    - .safetensors `support pytorch`
  - Pre Training `Build the whole model`
  - Post Training `Adjust part of model`
    - Low-Rank Adaptation (LoRA)
    - Fine-Tuning
    - Human Feedback Reinforcement Learning
    - Synthetic AI Data
  - Inference Compute `aka thinking models`

- Inference Engines
  - llama.cpp `most popular 24`
  - build in engine by Machine Learning Frameworks `slower`
  - JAX (Google)
  - ONNX (open-source)
  - TensorRT (NVIDIA)
  - vLLM

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
- Cosmos `Nvidia Physical Model`

### Vision

- Optical Character Recognition (OCR)
  - Gemini 2.0 Flash `Very Good, but not open source`
  - meta-llama/Llama-3.2-11B-Vision-Instruct `can do basic extra, but has error`
  - <https://llamaocr.com/> `fine tunned meta-llama, better, still error`

- Pixtral 12B `open source vision engine`
- DeepSeek

- Tools:
  - Gephi `Graph Visualization`


### PDF process
>
> This is very hard, is it text content focus? does it have OCR problem? or both?

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


## Retrival Augmented Generation(RAG)

strategy:
- Reranking
- Query Expansion
- Agentic `Given Tools; Ex: Web Crawler, Code Executor`
- LPG（Labeled Property Graph)
- RDF（Resource Description Framework）

Citation
>
> Just run classic similarly search compare output vs input.


## Debug

- Jaeger `distributed tracing tool`
- Langfuse `similar to sentry.io but for LLM`
- GraphRAG `knowledge graphs`



## Evaluation

- Sentiment
- Conversation Length
- Grounding
  - LLM -> Chat with user
  - Physical AI -> Physical World Response
  = Coder -> execute code

Prompts:
- How many words are in your response to this prompt?
- Guess cup game, multi round.
- Jake is walking to store that is 100 meter from him, every 1 second he walks 5 meter forward, then jump 1 meter back. How many seconds will take Jake walk to store.


## Beyond static LLM

- open socket interruption
- context caching
- thinking model
  - thinking interruptions


### Python

- litellm https://pypi.org/project/litellm/ `Common SDK`
- pydantic `I don't like it, structure output parser`