# NIM

> 8 GB of RAM available to run the 7B models, 16 GB to run the 13B models, and 32 GB to run the 33B models.

**Local AI Workbenches**

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



## ollama
> Run LLM locally
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

```



