# Code

## Python

Packages:

- networkx `Graph package`
- lancedb `database engine for all sort datatypes`

## Command fix shits

```
pip3 install torch -U

# Metal Performance Shaders (MPS)
import torch
print(torch.backends.mps.is_available())  # Should return True
print(torch.backends.mps.is_built()) 

export PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0

# Default HuggingFace downloads folder
~/.cache/huggingface

huggingface-cli scan-cache
```

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

## Ollama

> Pretty much Docker for LLM containerization; layer cache, build from layers. Support OLLAMA_KV_CACHE_TYPE by default across all Models.

<https://github.com/ollama/ollama#extensions--plugins>

- Modelfile `aka Dockerfile`
- CLI `docker pull vs ollama pull; ls, ps, rm ...etc`

```shell
brew install ollama

ollama serve
ollama pull llama2:7b
ollama run llama2:7b

OLLAMA_KEEP_ALIVE=1              # 0 is unload, negative is stay in RAM, 
OLLAMA_KV_CACHE_TYPE=q8_0        # storing past attention states, reducing redundant computations (default: f16)
OLLAMA_NUM_PARALLEL=1            # The maximum number of parallel requests each model will process at the same time
OLLAMA_FLASH_ATTENTION           # Reduce RAM
OLLAMA_MAX_QUEUE

http://localhost:11434
 
http://host.docker.internal:11434


curl http://localhost:11434/api/chat -d '{
  "model": "llama2:7b",
  "messages": [
    {
      "role": "user",
      "content": "why is the sky blue?"
    }
  ],
  "stream": false,
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_current_weather",
        "description": "Get the current weather for a location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The location to get the weather for, e.g. San Francisco, CA"
            },
            "format": {
              "type": "string",
              "description": "The format to return the weather in, e.g. 'celsius' or 'fahrenheit'",
              "enum": ["celsius", "fahrenheit"]
            }
          },
          "required": ["location", "format"]
        }
      }
    }
  ]
}'

curl http://localhost:11434/api/generate -d '{
  "model": "deepseek-r1:14b",
  "prompt": "What color is the sky at different times of the day? Respond using JSON",
  "format": "json",
  "stream": false
}'

pip install open-webui
open-webui serve

/Users/xxx/miniconda3/lib/python3.11/site-packages/open_webui

```
