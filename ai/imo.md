# AI Insights


## Analogy

- Terms:
  - LLM ~ vehicle's propulsion system
    - modality ~ fuel type
    - context window size ~ fuel tank size
      - generation token ~ engine cycle
      - inference cost ~ gasoline
    - weight/param ~ engine block
    - architecture ~ engine design
      - transformer ~ four-stroke cycle(most common engine design)
        - attention heads/experts ~ cylinders
        - hidden state(KV cache) ~ vehicle momentum / inertia
    - roles (system / developer / user / assistant / tool) ~ control priority


  - agentic system / harness ~ vehicle operation
    - prompt / inference ~ driving
      - inference system ~ road trip
        - workflow instruction (role: system | developer ) ~ driver handling control
          - monitor component ~ dashboard
        - task context (role: user) ~ driving route
          - prompt ambiguity ~ ambiguity route
          - lazy delegation ~ incomplete route
      - evaluation system ~ test drive
    - memory system ~ driving history
      - working memory ~ driving state (Ex: speedometer, direction)
        - KV cache ~ current momentum / speed / engine state
        - context rot ~ driver fatigue
      - persistent memory ~ stored vehicle records
        - session.md / episodic memory ~ trip history (can restore driving state)
        - skills / semantic memory / general knowledge ~ driving manual / driving habits
    - agent tools ~ vehicle attachments

  - task ~ mission
    - task context ~ draft driving route
    - workflow instruction ~ reprocess draft driving route
      - break route into sections
      - equipped traction tires getting out bad situation

    - agentic thinking ~ driver thinking
      - planning: choosing tool & order
      - maintain coherence: general direction tracking
      - reflection: deciding when to stop thinking and take an action
      - responsiveness: react to data from dashboard

    - agentic action ~ driving / exploration
      - consistency: action consistent with planning
      - handiness: use tool


propulsion system:
> Most user has no control beside choose which propulsion system.

> Top close source LLM(large engine), even bad harness/prompt(bad driver) can overcome task(arrive destination)
> Open source LLM(smaller engine), requires lighter hardwares(gasoline), but requires good harness(good driver)

vehicle dynamics:
> Unlike car analogy, here user has A LOT control on their car's vehicle dynamics(chassis & drive style)

> Main focus should be Destination & Route. Because car/LLM seems improve rapidly.

> Different chassis (harness) alter how the landscape (task) is navigated.

> In future, LLM support multiple instructions coordination?

Destination:
> We need well describe trajectory(destination); Since engine improves, we only need harness good enough to works.

> Break task into chunks ~ Break mountain route into sections; car avoid lost control momentum, and have fallback/resume point.
>> huge Momentum: hard to stop/control;
>> little/no momentum: no progress;

>> Long route ~ truck driver drives over 10hrs. Longer driver drives, their attention sensitivity decrease. ~ later position KV cache has more Context Rot.

> We need dashboard/Evaluation System; We can only improve what we can measure.


## IMO

Parameters → "what you know"
Loops → "how long you think"


- Merge PR ~ RL changes into LLM
  - My heuristic ≠ LLM heuristic
    - Typical Companies CAN'T RL LLM, just like customer need report their issues to SASS company. Typical companies' job is collect issues, relevant background, avoid known issues, info LLM provider, updates to latest LLM.
  - Define heuristic differences into SKILL/Prompt/Data
  - RL update ~ Implement update to patch bugs

- Bottlenecks:
  - Info communication/absorption rate.
  - Specialize skills/tech, that LLM need harness or fine tune
  - Convert goal into text
  - Other data modally Ex: Video, X-ray
  - LLM's experienced output tech stacks
    - visual
      - svg
      - png
      - slidev
      - html
      - BPMN (Business Process Model & Notation)
      - PlantUML
    - code
      - js
      - python
      - sql
      - bash
    - data
      - JSON
      - YAML
      - CSV
    - writing
      - markdown
      - /SKILL.md
- Person's Life ~ LLM's Context window.
  - It's no about extend life, it's about what you do(generate token) solve problem.
  - Pretrain ~ Child Development(Perception)
  - RL ~ Adult

- Don't rush to scale yourself with AI, focus on control first. Just like baby, walk before run.

- Search problem → Selection problem; Our job is select good opinion from LLM answers.
  - Constraints shrink the opinion space
  - Clear objective
  - Clear priority

- I disagree invest so much on decode accelerator hardwares. IMO problem source is transformer design tradeoff, transformer reduce compute density by kv cache(which demand RAM). Maybe diffusion like architecture is more future, which utilize all compute.

- Data > Infra > Algorithm > Talent

- The problem with Back Pros is earlier adjustment takes a LOT longer to adjust.
  - Is there ways to find Mid, or Early blocks' target, and adjust? Because we should KNEW which it's active expert.

- Speed up COT
  - Uses none english, pure vectors.
  - Use DAG COT, increase possible async sections.

- LLM has different sensitivity, just like human more sensitivity on hands, less sensitivity on back. LLM has high sensitivity on start & end tokens, less on middle & later position.
  - Another prove of my hypothesis, less activity region less neurons -> less sensitivity.
  - Also explain why ppl want kinky sex, activate rare regions is natural desire of neuron.

- We SHOULD allow LLM be stubborn(refuse RL until right COT hits).
  - Forcing RL or COT will adjust WRONG circuit.
  - The SOLUTION COT should NOT memorize. Rather find highest useful COT that LLM understand.
    - Similar to coach design specific training for each athlete.
      - Standard TEST or practice are needed. But we need build custom common mistakes & judgment/correction COT;
      - The problem is EACH LLM has different mistakes.
      - Optimize for the smallest intervention.
      - separate assumptions from observations.
      - specific failure mode
      - \text{Good supervision} = \text{task response} -> \text{target reasoning trace} + \text{specific failure mode}

- As Code World Model (CWM) turn into mainstream, DEFINE state variable/KPI is the next frontier.

- Pretraining ~ memorization, priors formation, form lego; RL ~ reflection, combine legos form trajectory latent space;

- LLM training ~ contrast learning; Decode ~ Pattern Completion;

- The problem is backprops adjustment ONLY align for CURRENT trajectories, but most likely mis align / conflict with other trajectories. Sure we rely on momentum. I suspect better alternative.

- Before train AI(or our self development), we needs to consider its available action space vs information space.

- Data formats
  - Alpaca Format
  - Markdown
    - LaTeX
  - Code

- LLM weights functions
  - inference weights
    - deterministic (Ex: embedding, LM head, RoPE)
    - compute (Ex: Attention V, MLP)
    - routing (Ex: DSA, MOE, maybe even attention score)
      - benefit: decouple gradients, partition representational space, reduce interference
    - stability control (Ex: norm)
  - training weights
    - loss function
    - optimizer state
      - direction
      - momentum
    - activation/activation checkpoints
    - custom settings (Ex: LR, decay)

- Avoid interference is THE REASON why MOE works.
  - KPI, measure NN's capacity by shrink NN's precision cost accuracy.
  - MoE improves the signal-to-noise ratio of gradient flow.
  - Gradients are partially isolated.
  - The fact smaller experts works shows RS ONLY needs x weighs, none active experts are dead weights.
  - Sure smaller LLM by reuses weight are POSSIBLE, at expense of flexibility of LLM.
- Transformer ~ Turing Machine
 Infinite tape ~ RS
 Head ~ Attention Head
 Head position  ~ Attention weights (soft, distributed)

- Use case dictate LLM architecture design.
- AI agent workflow should design as dynamic sophisticated process. At the end, there is fundamental trade off between compute vs throughput.
  - All design have some optimal scale, ~ 1 to 10x. Beyond that workflow should redesign.
- Prompt ~ flexible code with compute cost; LLM ~ compiler;

Operations:

1. Read ~ QK circuit
2. Compute ~ OV circuit + MLP
3. Write ~ Residual add
4. Move ~ next block

- Planner ~ Task Coherence
- Good question ~ increase trajectory probo confident

- How/Why NN growth? Tokens not attended → no gradient reinforcement
  - Attention momentum ~ state-space attention

- incentive for symmetry. maybe SVD.
- Balance between stability vs changes.
- LLM need to study project evolution training data[trajectory data](projects grow). Not typical Snapshot data.
- LLM imitating human slow thinking, but not trained with human instinct.
  - cause 1: attention scale o(n^2), although attention only 20% calculation
  - cause 2: FFN calculation is intense
- The problem with pre-training is dense reward on every token. Only subset of token signal is True.
- Simple ideas are easy to transfer(both people & LLM); complex ideas are not. Hard part is always make idea/context simple.
- Data/Experience > Architecture > Implementation(Biology or Chip Design)

- Data
  - Data is the most important, because none open source its data.
  - robot.txt
  - DCLM classier - Model that assign data embedding for data filter.
  - Synthetic Data
    - rephrase to improve quality
    - generate tasks; Ex: summary, info extra
- Training
  - Very few use case for fine tune. Has very large static knowledge, that does NOT conflicts with LLM known knowledge, and very diverse.
  - Multi Head decode RS with Multi Goals:
    - default: Fully Shift
    - New RS Head Ideas:
      - attach its thoughts
      - extract keywords
      - edits
      - Early error less loss
- Evaluation
  - ARC benchmark isolate reasoning from knowledge & linguistic.
  - Quizzing(has answer) vs Asking(don't know answer)
  - LogitLens - decode intermediate RS back to token for interpret. <https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens>

- LLM is about finding easy to scale axis.
- KV cache ~ all possible meaning/effect of a token.
- layer depth is sequential and width is parallel.
  - need found layers with sharp lost gradient: aka gradient scatter everywhere
    - opt 1: dynamic increase parallel processing, reroute connections. `aka condense nn from sparse to dense`
    - opt 2: find a way to have distinct storage in RS.
    - opt 3: in optimizer, we remove neurons with gradient * fire_freq > threshold. (remove neuron spoke often, with wrong output.)
- FFN always project into larger dimension, then compress; I think it's because project to larger dimension avoid collision

- Human's ONLY advantage over AI is signal absorption rate is far HIGHER than AI.
- Currently the problem in LLM is lifetime of context is short.
  - We have session compression to lengthen lifetime of session, but still no good way to manipulate session like human does in conversation(partially reset, topic reset).
    - We need to pre-train LLM ability to re-adjust session in each conversation, rather currently manually reset.
- Interestingly or scarily that LLM sometime already aware the input prompt is evaluation prompt.
- Progressive model growth
- compute is NOT the bottleneck, rather is Memory size.
- We have mathematical proof that 2 layer of NN can imitate any functions, but the problem is we don't know the way to optimize to that 2 layer NN.

- token interaction range  <<  total context
  - total context:
    - compressed
    - summarized
    - selectively retrieved(by emotion)
    - distributed
  - token interaction
    - sliding window
    - small
    - recurrent

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

## Biology of Large Language Models

[On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html)  
LLMs work by providing each “world” with context, which includes relevant information and logic.

---

## Technical Improvements

- **OmniHuman Lab** – <https://omnihuman-lab.github.io/>

---

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

> log(compute) ~ log(intelligent)

- Self Taught Reasoner (STaR)

  > Open AI reinforcement learning by study LLM verified & diverse solutions.
  >
  > Consistent answer that SUPPORT by REASONING. (Max Marginal Inference)
  >
  > Sample multiple times(use TOP n paths) vs generate multiple responses(n TIME MAX probability path)
  >> The GOAL is find RIGHT answer & AVOID greedy decode.
  >
  >> Option 1: Beam search

Guiding principles:

- directly optimize what we want
- Reliable verifier is the most crucial in RL finetuning, not the RL algorithm. by Rich Sutton
  - After exhausted problems have Reliable verifier, LLM can study problem with solution has rough estimate.

#### Reinforcement Learning Components (“Open AI Strawberry”)

> Reinforcement Learning(sparse reward) compares to pre-training(dense reward).
>> This also support principles in Positive Discipline by Jane.

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

## Game Benchmark

- FIDE rule on chess with 50 moves
  - FEN (board state)
  - Portal Game Notation (PGN) history

## Blogs


### 17

- Attention is all you need

### 18

### 19

### 20

### 21

- **“GPT‑3: Language Models are Few‑Shot Learners”** – Radford et al., 2021  

### 22

- Chinchilla scaling laws, titled "Training Compute-Optimal Large Language Models"

### 23

### 24

- **Anthropic’s “Scaling Monosemanticity”**  

### 25

### 2026

- <https://research.google/blog/sequential-attention-making-ai-models-leaner-and-faster-without-sacrificing-accuracy/> shrink up & down, find which feature matters. Aka contrast between training data vs benchmark data. When a feature is "locked," its selection weight $w_i$ is permanently set to 1.0.

- https://arxiv.org/pdf/2603.15031 Attention on previous block's residual stream replace residual connections.
  - layer: both NLP & Attention counts as an layer; Recommend N=8;
  - Q `profile of block`
  - V `input/hidden_states of each blocks`
  - K `norm(V), v=input`
