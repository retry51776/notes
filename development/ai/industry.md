# AI industry
>
> Only put tech stacks, companies, products here.

- Machine Learning Frameworks
  - LLM model formats
    - .bin `binary file to store llm models`
    - .gguf `GGUF Format to store llama.cpp models`
    - .safetensors `support pytorch`
  - Pre Training
  - Post Training
    - Low-Rank Adaptation (LoRA)
    - Fine-Tuning

- Inference Engines
  - llama.cpp `most popular 24`
  - build in engine by Machine Learning Frameworks `slower`
  - JAX (Google)
  - ONNX (open-source)
  - TensorRT (NVIDIA)
  - vLLM

<hr\>

**By Applications**

## Optical Character Recognition (OCR)

- Gemini 2.0 Flash `Very Good, but not open source`
- meta-llama/Llama-3.2-11B-Vision-Instruct `can do basic extra, but has error`
- <https://llamaocr.com/> `on top meta-llama, better, still error`

## PDF process
>
> This is very hard, is it text content focus? does it have OCR problem? or both?

## Text process

- Understanding
  - llama3.1 `very good`
  - gemini 2 flash `very good`

## Codings
>
> VS code has many plugins to support llm; Ex: continue.dev

```
    { "name": "code", "params": {} },
    { "name": "docs", "params": {} },
    { "name": "diff", "params": {} },
    { "name": "terminal", "params": {} },
    { "name": "problems", "params": {} },
    { "name": "folder", "params": {} },
    { "name": "codebase", "params": {} }
```

- Variables
  - context
  - Speed vs Ability

- fill-in-the-middle (FIM) `aka autocomplete model, usually smaller`
  - codellama `I prefer for now, but slow`
  - qwen2.5-coder `okayish, not super impressive`
  - starcoder `very bad`
- Chat model `normal llm`
- Voice to Text(VS Code Speech ⌥⌘V or "Hey Code")

## Workflow

frameworks:

- FlowiseAI
- <https://n8n.io/>

features:

- structure output parser
- system message
- Prompt-Embedded Tools  VS Explicit tools Parameter
  - (Ex: llama3-groq-tool-use, because llama3.1 doesn't support it)

> system instruction & output parser & llm need to work together, test & qa before workflow successful.

```
docker pull flowiseai/flowise
docker run -d --name flowise -p 3000:3000 flowiseai/flowise


```

## Cool AIs

- CodeFormer `Image/movie recover & enhance AI`
- ChatGPT `Everyone knows`
- Quillbot `Rephrase text`
- <https://beta.elevenlabs.io/voice-lab>
- <https://you.com/>
- midjourney
- Heygen.com `video generation ai`
- <https://app.suno.ai/> `music ai`

<hr>

**By Company**

## OPENAI
>
> OpenAI can be think of "University for AI"; How OpenAI measure/test AI, what course they teach/train AI, how OpenAI get feedback from AI?
>
> It's NOT graduated student from University makes University valuable. It's graduated student proven University's education process.
>
> Diff: OPENAI can design student. I don't know if AI design matter a lot or little.

> My guess OpenAI train AI with more output layers; More output layers force AI to have deeper understanding.

<hr>

# CICD

- Modeling
- Deployment
- Versioning
- Orchestration
- Compute
- Data

## Modeling

- 1. What are we modeling?
  - Study human? or Study physic? Ex: color is only human biology, in reality just wave freq.
- 2. Curate Data
  - The biggest bottleneck; Both human & robot data collection limited by reality.
- 3. Design AI Architecture
  - Dark magic? Ask AI expert
  - Symmetry within model (Ex: time, left vs right, position,)
  - Kind like structure engineer
- 4. Craft Loss Function
  - Relates to #1, from which perspective?
  - Physic law can embed within lost function to ensure Model learn physic law.
- 5. Optimization
  - This solution may be another AI itself?

- Identify object
- Assign object properties

## Deployment Stacks

- NIM
- Local AI Workbenches
  - Model Loader(llama.cpp) `loading models & executing inference computations`
    - GPU Acceleration (CUDA, Metal)
  - UI interface
  - API/CLI Access
  - Model Management
- Other data services

## Tools

- Chain: predetermine workflow
- Agent: undetermined workflow
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

'''ls
docker login nvcr.io
export NGC_APU_KEY=xxx
export LOCAL_NIM_CACHE=/tmp/.cache/nim
'''

```ls
brew install ollama

ollama serve
ollama pull llama2:7b
ollama run llama2:7b

http://localhost:11434


curl http://localhost:11434/api/chat -d '{
  "model": "llama2:7b",
  "messages": [
    {
      "role": "user",
      "content": "why is the sky blue?"
    }
  ],
  "stream": false
}'

pip install open-webui
open-webui serve

/Users/xxx/miniconda3/lib/python3.11/site-packages/open_webui

```

## Citation
>
> Just run classic similarly search compare output vs input.
