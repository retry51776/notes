# MLX

## Setup

```bash
conda create -n mlx python=3.11 -y
conda activate mlx

pip install --no-cache-dir mlx mlx-lm

# VS code / Command Palette (⇧⌘P) → Python: Select Interpreter  → choose ~./miniconda/envs/mlx

```

```py

# Core MLX model, by default NOT uses KV cache
outputs = model(input_ids, attention_mask=None, cache=None)
outputs = model.generate(prompt, temp=1.0)

# Example kv_cache
logits, kv_cache = model(next_token, kv_cache=kv_cache)

from pprint import pprint
import time

import mlx.core as mx
from mlx_lm import load, batch_generate
import numpy as np

import re
from typing import Optional, Dict

def parse_gpt_oss_response(text: str) -> Dict[str, Optional[str]]:
    """
    Parses GPT-OSS / MLX model outputs to extract reasoning and final message.
    Works even if <|start|>assistant is omitted.
    """
    pattern = (
        r"(?:<\|start\|>assistant)?"
        r"(?: to=[\w\.]+)?"
        r"<\|channel\|>(?P<channel>\w+)"
        r"<\|message\|>(?P<content>.*?)"
        r"(?=<\|start\||<\|end\||<\|return\||$)"
    )

    matches = list(re.finditer(pattern, text, re.DOTALL))
    result = {"reasoning": None, "message": None}

    for m in matches:
        channel = m.group("channel")
        content = m.group("content").strip()
        if channel == "analysis":
            result["reasoning"] = content
        elif channel == "final":
            result["message"] = content
        elif channel and content:
            # For any other channel, store content under its name
            result[channel] = content

    return result

# --- 1️⃣ Load model from local folder ---
# folderx should contain model.mxfp4 and tokenizer files (e.g., tokenizer.model or tokenizer.json)
model, tokenizer = load("~/.cache/lm-studio/models/mlx-community/gpt-oss-20b-MXFP4-Q8")

def process_prompts(prompts: list) -> list:
    # Apply the chat template and encode to tokens
    prompts_tokens = [
        tokenizer.apply_chat_template(
            [{"role": "user", "content": p}],
            add_generation_prompt=True,
            reasoning_effort="minimal",
            model_identity="You are a helpful assistant.",
        )
        for p in prompts
    ]
    result = batch_generate(model, tokenizer, prompts_tokens, verbose=True, max_tokens=131072)

    clean_outputs = [parse_gpt_oss_response(t) for t in result.texts]

    # The returned result contains texts completions in the same order as prompts
    pprint(clean_outputs)
    pprint(result.stats)

# Size: 1
# peak_memory ~ 12MB for KV-cache growth, logits, temp 
BatchStats(prompt_tokens=65,
           prompt_tps=445.94783582531005,
           prompt_time=0.14575695805251598,
           generation_tokens=1027,
           generation_tps=120.4994149696857,
           generation_time=8.522862955462188,
           peak_memory=12.182971726)
# Size: 29
BatchStats(prompt_tokens=2023,
           prompt_tps=1332.5709122350333,
           prompt_time=1.5181180839426816,
           generation_tokens=17518,
           generation_tps=287.3757254868944,
           generation_time=60.95852379431017,
           peak_memory=12.778164722)
# SizeL 101
BatchStats(prompt_tokens=7017,
           prompt_tps=1100.5434404319476,
           prompt_time=6.375940959900618,
           generation_tokens=70896,
           generation_tps=328.5884810732216,
           generation_time=215.7592371115461,
           peak_memory=13.945100936)

# chat template
# Each LLM has its own chat template determent how it interpret input string & generate output
# template / channel

"""OSS
<|start|>  → begins a message
<|channel|>  → specifies what type of message (e.g. analysis, final)
<|message|>  → starts the content body
<|end|>  → closes the whole message
"""
```

| Role | Has channel? | Why |
| - | - | - |
| system | ❌ | Only static context, no reasoning/phase separation |
| user | ❌ | Plain input, always one channel |
| assistant | ✅ | Has multiple output channels (analysis, final, etc.) |
| tool / python | ✅ (sometimes) | Treated as special assistant sub-channels |
