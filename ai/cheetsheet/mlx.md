# MLX

## OSS chat template
>
> Each LLM has its own chat template determent how it interpret input string & generate output

| Role | Has channel? | Why |
| - | - | - |
| system | ❌ | Only static context, no reasoning/phase separation |
| user | ❌ | Plain input, always one channel |
| assistant | ✅ | Has multiple output channels (analysis, final, etc.) |
| tool / python | ✅ (sometimes) | Treated as special assistant sub-channels |

```python
<|start|>  → begins a message
<|channel|>  → specifies what type of message (e.g. analysis, final)
<|message|>  → starts the content body
<|end|>  → closes the whole message
```

```py

import re
from typing import Optional, Dict, Any

def parse_gpt_oss_response(text: str):# -> Dict[str, Optional[Any]]:
    """
    Parses GPT-OSS / Harmony-style multi-channel output.

    Handles:
      - analysis, commentary, final channels
      - tool calls (functions.x)
      - optional <|constrain|> and <|call|> endings
      - 'to=' appearing before or after <|channel|>
      - removes 'functions.' prefix from tool names
    """
    pattern = (
        r"(?:<\|start\|>assistant)?"                   # optional assistant start
        r"(?:\s*to=(?P<to1>[\w\.\-]+))?"              # to= before <|channel|>
        r"\s*<\|channel\|>(?P<channel>\w+)"           # channel name
        r"(?:\s*to=(?P<to2>[\w\.\-]+))?"              # to= after <|channel|>
        r"(?:<\|constrain\|>(?P<constrain>\w+))?"     # optional constrain
        r"<\|message\|>(?P<content>.*?)"               # content body
        r"(?:<\|call\||<\|end\||(?=<\|start\|)|$)"    # end markers
    )

    result = {"reasoning": None, "message": None, "commentary": None, "tool_calls": []}

    for m in re.finditer(pattern, text, re.DOTALL):
        channel = m.group("channel")
        content = m.group("content").strip()
        to = m.group("to1") or m.group("to2")
        constrain = m.group("constrain")

        # remove known prefixes
        if to and "." in to:
            to = to.split(".", 1)[1]

        if channel == "analysis":
            result["reasoning"] = content
        elif channel == "final":
            result["message"] = content
        elif channel == "commentary":
            if to:
                result["tool_calls"].append({
                    "tool": to,
                    "constrain": constrain,
                    "args": content
                })
            else:
                result["commentary"] = content
        else:
            result[channel] = content

    return result
```

## Setup

```bash
conda create -n mlx python=3.11 -y
conda activate mlx

pip install --no-cache-dir mlx mlx-lm

# VS code / Command Palette (⇧⌘P) → Python: Select Interpreter  → choose ~./miniconda/envs/mlx

```

## MLX Basic

```py
# tokenizer
tokenizer.apply_chat_template() # json -> str|mx.array
tokenizer.encode() & batch_encode_plus() # str -> mx.array
decode(ids) # int -> str


# Core MLX model, by default NOT uses KV cache
outputs = model(input_ids, attention_mask=None, cache=None)
texts = model.generate(prompt, temp=1.0, draft_model=None, num_draft_tokens=0, verbose=True)

# Example kv_cache
logits, kv_cache = model(next_token, kv_cache=kv_cache)

from pprint import pprint

import mlx.core as mx
from mlx_lm import load, batch_generate
from mlx_lm.sample_utils import make_sampler
import numpy as np


# --- 1️⃣ Load model from local folder ---
model, tokenizer = load("~/.cache/lm-studio/models/mlx-community/gpt-oss-20b-MXFP4-Q8")
sampler = make_sampler(temp=0.4)

def process_prompts(prompts: list):# -> list:
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
    result = batch_generate(model, tokenizer, prompts_tokens, sampler=sampler, verbose=True, max_tokens=131072)

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

```

```py
# Manually Activation
def manual_activation(input_ids: list, layer_num: int = 0):
    mask = mx.ones_like(input_ids)

    # --- 3. Get embeddings ---
    hidden = model.model.embed_tokens(input_ids)

    # --- 4. Pass through first N layers manually ---
    for i in range(layer_num + 1):
        block = model.model.layers[i]
        hidden = block(hidden, mask)  # forward with mask
    
    # hidden shape: [batch, seq, hidden_dim]
    hidden_state = np.array(hidden[:, -1, :].astype(mx.float32))
    return hidden_state
```
