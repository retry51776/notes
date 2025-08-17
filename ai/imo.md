# AI Insights & Research Overview

## IMO

- AI is "crystallize intelligent". Similar to kinetic energy being converted into potential energy.
- AI is similar to Chemistry/Physical in 1800. There's some set logic/mechanism(usable metal); We play around data(Iron Ore) with some computation process(refine ore). Maybe the remaining data AKA model(Iron/steel) is what we desire. So value of the data is NOT determent by amount, but the data contains logic/mechanism we desires.

  > Mining & Extraction = Data Collection & Scraping
  >
  > Computation = Heat
  >
  > Data Center = Blast Furnace
  >
  > Data = Iron Ore
  >
  > Model = Iron
  >
  > Fine-Tuning (Specialized Model Training) = Alloying (Adding Carbon to Make Steel)
  >
  > Inference & Deployment = Rolling & Shaping Steel
  >
  > AI Evaluation (Benchmarks, Alignment, RLHF) = Quality Testing & Hardening
  >
  > AI Applications = Bridges, Cars, Tools
  >
  > Smart AI answer's is info density = Purity Iron weight more Same As Human

## Recent Concepts

- **Combine token_d's key & value of Attention into a single embedding**  
  - Reduce dimensionality: 2d → 0.7d (c < 1)  
  - Concatenate (do **not** add) RoPE‑enhanced embeddings for the attention head.

- **8/32 MOE auxiliary‑loss‑free strategy** – load balancing without additional loss.

- **Multi‑Token Prediction (MTP)** – use `next_token_prediction` (expected token) + `next_token` (actual token) to predict a new token.

- **Interactive Environment** - Percept -> Plan -> Action -> Reflection
  - find & store intermediate relationships
  - validate intermediate relationships

- Skill != AGI `or AGI is unique set of skills that text data doesn't cover`

## Knowledge Distillation

- Hard labels (human annotations) often miss nuances.  
- Soft labels (LLM statistical probabilities) capture richer relationships.  
- Label smoothing lets a model learn from soft labels instead of hard ones.  

**64 experts** are employed in the current setup.

## Biology of Large Language Models

[On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html)  
LLMs work by providing each “world” with context, which includes relevant information and logic.

---

## Technical Improvements

### Cache Strategies

| Phase                     | Cache Type          | Description |
|---------------------------|---------------------|-------------|
| **Agentic**               | Embedding Cache     | Used only for similarity search; very limited. Does **not** save LLM token cost. |
| **Prefill**               | Tokenizer Cache     | First step; small savings; order does not matter. |
|                           | Prompt Cache        | Requires an exact prefix match; works only during the prefill phase. |
| **Autoregressive Decoding** | KV Cache            | Used for token generation. The query (latest token) changes each step, while the key and value (past tokens) remain static.<br>• Implicit cache – handled automatically by the LLM provider.<br>• Explicit cache – must be programmed. |
|                           | FlashAttention Cache| Combines KV cache with softmax optimization. |

### Notable Papers & Ideas

- **“GPT‑3: Language Models are Few‑Shot Learners”** – Radford et al., 2021  
- **Tree of Thought**  
- **Anthropic’s “Scaling Monosemanticity”**  
- **Position Interpolation for Extending Context Window in Transformers** – OpenAI, 2023  

> Instead of using positions `[1, 2, 3, …, L]` (where *L* is the pre‑trained sequence length), we use repeated blocks such as `[1, 1, 1, 1, 2, 2, 2, 2, …, L, L, L, L]`.

- **OmniHuman Lab** – <https://omnihuman-lab.github.io/>

---

## New Research Directions

- **Leave No Context Behind** – Google’s approach to extending context windows.  
- **Dynamic Routing Between Capsules** – Capsule Networks.  
- **TransformerFAM** – Feedback attention as working memory.  
- **Attention with Linear Biases (ALiBi)** – Adds a distance‑based linear bias to attention scores, giving higher weight to closer tokens.  
- efficiency is part of the intelligent feature, keep increase token to solve solution is similar to brute force search. Both DATA & COMPUTE Efficiency.
- Maybe the problem LLM is aggregate learning. Human individual have memory system that can retrace in time. Maybe aggregate learning in training phrase prevent it have memory system. We need a training system that have strong memory module, and have llm reflect on those memories. `IMO current LLM still have very low memory absorption rate, it uses aggregate learning to compensate low memory absorption`

### Flash Attention Techniques

1. **Tiling** – Divides attention computation into smaller parallel tiles.  
2. **Sparse Matrix Multiplication** – More efficient than dense multiplication.  
3. **I/O Awareness** – Minimizes memory reads/writes.

- **Retrieval‑Enhanced Transformers (RETRO)** – Combine retrieval of relevant documents with generative modeling.  

- **SynFlow Pruning** – Scores connections by `score = (∂Loss/∂Weight) * Weight`, aiming for balanced layer pruning.  

- **Quantization Challenges** – Normalizes weights and activations, but outlier weights require special handling.

- **Generative Agents** – Simulate human‑like behavior with memory, planning, reaction, and reflection in interactive environments.

---

## OpenAI Perspective

> *The age of pre‑training is over.*

### Five Pillars for AGI (according to OpenAI)

1. Conversational LLMs  
2. Reasoning & Planning  
3. Actionable Agents (analysis + execution)  
4. Innovation  
5. Organization  

#### Reinforcement Learning Components (“Open AI Strawberry”)

1. **Policy Initialization**  
2. **Reward Design** – Outcome Reward Maximization (ORM) vs. Process Reward Maximization (PRM).  
3. **Search** – Beam Search, Monte Carlo Tree Search, Sequential Revision, etc.  
4. **Learning**  - Skill(remember) & Adaptability(learn)

### Task Decomposition & Solution Generation

- **Self‑Evaluation** – LLMs excel at evaluating their own outputs.  
- **Solution‑Level Search**, **Step‑Level Search**, **Token‑Level Search** – Different granularities of search during inference.

Training often uses beam search, while inference favors sequential revision.

---

## Additional Resources

- **Scaling of Search and Learning: A Roadmap to Reproduce o1 from a Reinforcement Learning Perspective**  
- **Neuronpedia** – Inspect neuron meanings: <https://docs.neuronpedia.org/>

---
