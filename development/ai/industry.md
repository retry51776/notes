# AI industry
> Only put tech stacks, companies, products here.

<hr>

**By Applications**

## Optical Character Recognition (OCR)
- Gemini 2.0 Flash `Very Good, but not open source`
- meta-llama/Llama-3.2-11B-Vision-Instruct `can do basic extra, but has error`
- https://llamaocr.com/ `on top meta-llama, better, still error`

## PDF process
> This is very hard, is it text content focus? does it have OCR problem? or both?


## Text process
- Understanding
  - llama3.1 `very good`
  - gemini 2 flash `very good`

## Cool AIs
- CodeFormer `Image/movie recover & enhance AI`
- ChatGPT `Everyone knows`
- Quillbot `Rephrase text`
- https://beta.elevenlabs.io/voice-lab
- https://you.com/
- midjourney
- Heygen.com `video generation ai`
- https://app.suno.ai/ `music ai`

<hr>

**By Company**

## OPENAI
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


## Tools
- Chain: predetermine workflow
- Agent: undetermined workflow
- Source Grounded AI - `AI that reference some documents to answer chats`
    - Citation = `AI able to refer back where it get source`
    - Separation - `AI able to understand structure of source`
    - Filter - `AI able to find most important part source, and focus attention around that section.`

## Datastore
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
## Citation
> Just run classic similarly search compare output vs input.