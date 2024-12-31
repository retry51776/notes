# Tech stack

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
<hr>

## Inference Stacks
> Machine Learning Frameworks(PyTorch) > Acceleration Driver(cuDNN) > Hardware(GPU)



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
    - llama.cpp
    - PyTorch
    - TensorFlow
    - JAX (Google)
    - ONNX (open-source)
    - TensorRT (NVIDIA)
    - vLLM



## Deployment Stacks

- NIM
- Local AI Workbenches
    - Model Loader(llama.cpp) `loading models & executing inference computations`
        - GPU Acceleration (CUDA, Metal)
    - UI interface
    - API/CLI Access
    - Model Management
- Other data services

### LLM Runtime
- Metal llama.cpp
- ROCm llama.cpp
- CUDA llama.cpp

### Visualize Model
> Netron: Interactive model graph exploration.
https://www.neuron.app/


## Local AI Workbenches
> 8 GB of RAM available to run the 7B models, 16 GB to run the 13B models, and 32 GB to run the 33B models.

- open-webui (pip package) + ollama
- LM Studio (all in one)

| Feature             | Ollama          | LM Studio      | text-generation-webui | llama.cpp       | GPT4All          | vLLM |
|----------------------|-----------------|----------------|----------------------|-----------------|-----------------|------|
| **Ease of Use**     | Very High       | High           | Medium               | Low             | High             | Low |
| **Interface**        | CLI             | GUI            | Web GUI              | CLI/Library     | GUI               | API   |
| **Model Management** | Basic          | Good          | Excellent            | N/A            | Good           | N/A |
| **Customization**    | Basic           | Medium         | Very High            | High            | Medium          | High |
| **Performance**      | Moderate        | Moderate       | Good                | Very High       | Moderate        | Very High |
| **Community Support** | Growing       | Strong       | Very Strong          | Very Strong     | Medium           | Growing |
| **Target User**      |  Beginners      | Beginners/Intermediate | Advanced           | Developers      | Beginners         | API Users |
| **Trend**          | Growing           | Growing      | Established         | Very Strong         | Growing        | Growing |



### Filter
> Filter functions are designed to add, format, edit the user input. They act as middleware for pre-processing and post-processing messages.
>> Pre-LLM: Modify or validate user inputs before sending them to the LLM.
> 
>> Post-LLM: Alter, enhance, or validate the LLM's responses before showing them to the user.
Filters can implement use cases like translation, logging, or toxicity filtering.

### Tools
> 3rd party tools for LLM

### Action
> User optional actions; Ex: Graph, download & exec code, send email

> > Run Code is done by Pyodide.

### Pipeline

## ollama
> Run LLM locally, seems like just a docker wrapper.

https://docs.openwebui.com/

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

/Users/terry/miniconda3/lib/python3.11/site-packages/open_webui

class Tools:
    def __init__(self):
        self.citation = True

    async def get_youtube_transcript(
        self, url: str, __event_emitter__: Callable[[dict], Any] = None
    ) -> str:
    await __event_emitter__(description, "success", True)


    await __event_emitter__(
        {
            "type": "status",
            "data": {
                "status": status,
                "description": description,
                "done": done,
            },
        }
    )
```

> https://r.jina.ai/ convert any html to jina to reduce token usage



# AMD
> AMD uses Hipify to convert CUDA into AMD HIP.

