# Code

## Python

Packages:

- networkx `Graph package`
- lancedb `database engine for all sort datatypes`


# Nvidia
'''ls
docker login nvcr.io
export NGC_APU_KEY=xxx
export LOCAL_NIM_CACHE=/tmp/.cache/nim
'''

# Ollama
```ls
brew install ollama

ollama serve
ollama pull llama2:7b
ollama run llama2:7b

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
  "model": "llama3.2",
  "prompt": "What color is the sky at different times of the day? Respond using JSON",
  "format": "json",
  "stream": false
}'

pip install open-webui
open-webui serve

/Users/xxx/miniconda3/lib/python3.11/site-packages/open_webui

```

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
```
