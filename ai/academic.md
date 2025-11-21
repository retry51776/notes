# Academic

- General
- Architecture
- Biology
- Mechanistic Interpretability
- Paper
- Training

## General

### History

Stage:

- pre 2018: Encoder + Decoder Components `There are different components of model, different task needs different components`
- 2020-2022: LLM that needs fine tune `LLM is not reliable, fine tune required`
- 2023: Post Training w Reinforcement Learning: General Model handle different tasks
- 2025: Async Model `Model can continuously take input, change action base off new input(observation) while its outputting; Not like current LLM is turn base.`
  - Parallel Output `paralyzed LLM output, maybe generate outline first, then generate each subsection by batch`
  - Hierarchical Reasoning Model (Recurring frequency vs Output frequency)
  - Decouple Input & Output
  - Output interruption & Input interruption
  - Improve LLM from understand to apply tools `aka from understand to doing`
- ??: dynamic model & benchmark

### Modeling Steps

1. What are we modeling?
    - Study human? or Study physic? Ex: color is only human biology, in reality just wave freq.
2. Curate Data
    - The biggest bottleneck; Both human & robot data collection limited by reality.
3. Design AI Architecture
    - Dark magic? Ask AI expert
    - Symmetry within model (Ex: time, left vs right, position,)
    - Kind like structure engineer
4. Craft Loss Function
    - Relates to #1, from which perspective?
    - Physic law can embed within lost function to ensure Model learn physic law.
5. Optimization
    - Adaptive Moment Estimation (ADAM)
      - magnitude $v_t = \beta_2 \cdot v_{t-1} + (1 - \beta_2) \cdot g_t^2$
      - momentum $m_t = \beta_1 \cdot m_{t-1} + (1 - \beta_1) \cdot g_t$
    - This solution may be another AI itself?

### Neural Network Terms

- Basic General
  - Forward Propagation
  - Backward Propagation
    - Lost
    - ε (epsilon) `a tiny constant (typically 1e-5 or 1e-6); learning rate unit`

  - Tiling `calculation matrix multiplication by smaller block, each SM loads target block row & col to calculate small final result block`
  - Neuron `fundamental unit in a neural network that performs a simple mathematical operation on input data and passes the result to other neurons or output units; weights usually gaussian distribution`
  - Activation function
    - Relu - range 0 to x;
    - SiLU - GPT-OSS; likely range from -1 to 50
    - GELU - (Gaussian Error Linear Unit)
  - Weight - Usually range from -1 to 1
  - Bias - Usually small; Doesn't uses in attention blocks;
  - Output - center around 0 because normalization layer;  Activations Density under 0.5%
  - ROPE - # 2D rotation on each pair (even_i, odd_i); `x_rot_even =  x_even *cos - x_odd* sin; x_rot_odd  =  x_even *sin + x_odd* cos;`
  - Hill climbing `strong signal, LLM training`
  - Hidden States `Residual Stream's output; [seq, d_model]`
    - Logit values `the token level raw scores before softmax`

- Advance General
  - low-loss paths `small changes do not significantly increase the loss`
  - Auto Model Compression `pruning as reinforcement learning problem`
  - Tensor Parallelism `similar to tiling, but need sum to get final result(tilting need append to get final result)`
- architecture design
  - Tokenizer `prompt(str) → input_ids(list(int)) → embedding(list(list(double))) → logit(list(double)) → prob(list(double)) → token(int) → output(str)`
    - chat-template
      - different role/channel
      - special tokens
    - embedding space at layer 0 is often scrambled and highly non-semantic
  - Mixture of Expert(MOE)
  - Multi Query Attention `reduce attention head to output to increase speed`
- Training
  - Activation checkpoint `Don't store Activation, recompute to save RAM`
  - pre-training objectives
    - full shifting
    - windowed loss
    - Last-token only loss
    - Multi-token prediction

- post-train
  - ~100mb/100k instruction dataset
  - Parameter Efficient Fine Tuning(PEFT)
    - google/IFEval
  - LoRa `Attach extra weight to original model feed forward layer, then train these extra weight; usually mb size`
  - On Policy Distillation `kl(student_prob - teach_prob)`

- L1 regularization `L1 regularization penalizes the sum of the absolute values of the weights in the network. This encourages the network to use a smaller number of weights, and it can also help to prevent over fitting.`
- L2 regularization `L2 regularization penalizes the sum of the squares of the weights in the network. This also encourages the network to use a smaller number of weights, and it can also help to improve the generalization performance of the network.`
  - Weight decay `adds a penalty term to the loss function that discourages large parameter values`

- Position Interpolation `extend context window without retrain`

- Perplexity in LLMs is a metric for how well the model predicts a sequence of tokens
- bias-variance tradeoff - overfitting training data. As LLM size increase, bais error is easy to reduce(aka training error), while variance(range of understanding) error domain, then variance error decrease.
  - The problem is human brain are similar, so default variance are small. But LLM are very different, larger variance relative to another human.
- gradient descent `Compute batch avg lose, nudge a little by batch avg lose direction. It works because unlike it stuck at local min, stuck requires all dimensions are at local minimum at the same time`
  - big batch size can support large learning rate, small batch size should able fine tune. RL ~ batch size = 1; Think as case specific knowledge can't be mixed.
- epoch, batch, slot
- Collective Operations
  - Broadcast
  - Scatter - each rank gets subset of data
  - Gather - collect all ranks into single rank
  - Reduce
  - All-gather - every rank broadcast & gather;
  - Reduce-scatter - every rank get op(sub_set)
  - All-reduce = reduce-scatter + all-gather

## Tokenizer

> Token is atomic unit in LLM. Frequent words should encode into single token. Token map can both algorithm assign or learn by nn.

> Multiple segmentations are possible. Ex: "abc" -> "ab" + "c" or "a" + "bc"

> Tokenizer applies greedy longest-match-first rule

## Architecture

- Autoregressive Decoding `We need go beyond greedy decode.`
  - Solution 1: Search different decoding paths for high confident answer
  - Solution 2: Vote

  > Prompt engineering = reshape LLM output distribution

### Limitation of Back Propagation
>
> There’s a mathematical result showing that a neural network with just two layers can approximate any function. The challenge, however, is that we don’t know how to efficiently optimize the weights to reach those solutions.
>> Ex: 2 layers nn often stuck on some error rate, no matter how much we increase width of nn.
>
> Problem with training nn that too deep, is too much noise drawn out signal in back propagation.
>> Residual Connection `It works by smoothing lost gradient, shorten signal distinct.`

📦 KV Cache Structure

For a model with:

- L  layers (transformer blocks)
- H  heads per layer
- S  sequence length (number of tokens)
- d_head  = head dimension

 Total size ∝ L × H × S × d_head × 2  # (×2 because K and V)

residual stream/latent space `The intermediate output between NN layers`

### Transformer

<https://poloclub.github.io/transformer-explainer/>

- x `input tokens`
- len(x) `input length`
- Q `Q = x * Wq, positional specific`
- K `K = x * Wk, position agnostic`
- V `V = x * Wv, position agnostic; each token possible meanings(need filter by contextual score)`
- H `Number of attention heads`
- d_head `often 128, len(x) * d_head`
- d_model = `d_head * H` is residual stream size.
- $ QK^T $ `d_model * len(x), contextual score`

deepseek:

- Multi-Head Latent Attention (MLA)
  - Find common denominator matrix C for in KV matrix, so when store KV cache, store KV/C to save storage.
- Cross-Layer Attention (CLA)
- Due Pipeline - Decouple backprops into 2 components; Only run 2nd part when GPU is free
  - Calculate backprops for early layer
  - Calculate weight update

```py
model.model.layers ModuleList(
  (0-63): 64 x Qwen2DecoderLayer(
    (self_attn): Qwen2Attention(
      (q_proj): Linear(in_features=5120, out_features=5120, bias=True)
      (k_proj): Linear(in_features=5120, out_features=1024, bias=True)
      (v_proj): Linear(in_features=5120, out_features=1024, bias=True)
      (o_proj): Linear(in_features=5120, out_features=5120, bias=False)
    )
    (mlp): Qwen2MLP(
      (gate_proj): Linear(in_features=5120, out_features=27648, bias=False)
      (up_proj): Linear(in_features=5120, out_features=27648, bias=False)
      (down_proj): Linear(in_features=27648, out_features=5120, bias=False)
      (act_fn): SiLU()
    )
    (input_layernorm): Qwen2RMSNorm((5120,), eps=1e-05)
    (post_attention_layernorm): Qwen2RMSNorm((5120,), eps=1e-05)
  )
)
```

### Diffusion

> Diffusion train data by noise sample both variances(gaussian noise) & mean(drift direction toward 0/normal distribution).
>> **Drift** is known deterministic force, **variance** is random force.

Forward SDE is mathematical model diffusion process, but surprisingly there is mathematical model REVERSE SDE.

> Reverse SDE break into 2 components: **variance** assume cancel by **variance**; **Drift** is -1/2 *beta(t)* x for DDPM;

> Score Function - For any given point in the data space, it tells you the direction in which the probability density of the distribution increases the fastest.
>> Once Score-Diffusion compute diffusion score, it ues reverse SDE formula to denoise input. Then iteratively repeat until diffusion score reach threshold.

> Diffusion Model generate all tokens, then mask tokens with low logit, regenerate again.

DDMP paper by Johnathan Ho @ 2020
(Evidence Lower Bound)ELBO

- scored diffusion - `llm learn score noised sample`

<hr>

### Pretrain

> Pretrain is all about imitation.

### Supervise Finetune Training(SFT)

> SFT can't scale, generate the whole distribution is too expensive. Also too hard to judge/score SFT solution.

### Reinforcement Learning

> Think of it as outer loop of learning.

> The limitation of supervise learning is teacher HAS answer, and student will NEVER out smart teacher, teacher requires build large teaching exercise.

> The limitation of RL is reward sparsity, which it's why important to have small achievable goal.

Good LLM RL practices:

- LLM self aware its known & unknown
- LLM self aware its context window
- Learn HF preference
- LLM self aware compute & RAM usage

- Solve/Predict/Explain/Counter/Coherence/Confidence

**PPO components**:

> reinforcement learning human feedback with Proximal Policy Optimization(PPO), just promote subset response probability over undesired responses.

> Collect set of complete responses, each token calculate its advantage estimate(from reward_model) & baseline_value(from ref_model)

- police_model/SFT model - AI that takes input & generate output action.
- ref_model - Frozen SFT model, uses to calculate lose by compare new action vs old action
- reward_model - LLM with LORA(attach head) trained with ranking loss.
  - Learn from human how to rate LLM output
- value_function - How much value does solution sub step worth
- policy gradient
  - Kullback‑Leibler divergence (KL) - measure difference between 2 distributions `normalize by log(observation^(1/n))`;
    - KL = Cross Entropy - Entropy
  - advantage estimate = total_discount_reward - baseline_value
    - total discounted reward $G_t$ is from time step t; `aka future reward needs discount rate`
      - discount factory - how much future reward needs to discount
    - baseline value = ref_model

**GRPO**

> Group Relative Policy Optimization(GRPO) from deepseek
>> Replace ref_model to calculate baseline with generic baseline(per question, excludes answer);
>> Replace per step reward with final reward.

**Direct Preference Optimization**

## Sparse Reward

 • Reward shaping → add intermediate signals that guide progress.
 • Curriculum learning → start with easy tasks, gradually scale difficulty.
 • Exploration strategies (entropy bonuses, intrinsic motivation, count-based bonuses, etc.).
 • Self-play (used in AlphaGo, AlphaZero, OpenAI Five).
 • Hierarchical RL → break down long horizon tasks into sub-policies.

## Mechanistic Interpretability
>
> AI mechanistic interpretability is a field that will give a lot insight of how human brain works.

> higher-level concepts or computations reside in the middle of graphs
>> detokenization → abstract features → retokenization

<https://transformer-circuits.pub/2025/attribution-graphs/biology.html>

- Physics Informed Machine Learning
- Stable diffusion: add noise to image, let AI recover image;
  - KV Cache Incompatibility: old tokens can also attend to new token, which means the representations of all tokens must be recomputed.

> Netron: Interactive model graph exploration.
<https://www.neuron.app/>

Techs:

- Patchscopes `Swap activations from a clean run into a corrupted run to test causality.`
- vocabulary projection
- Feature Attribution Methods (Gradient-based)
- Probs - Individual neuron activation indicate x feature

Tools:

- TransformerLens

Rule of Thumb

- Facts are expects to resides in early layers of FFN

### Linear representation
>
> Currently(2024) common agreement is AI uses linear representation to store concepts. (`vector analogies` man - women = king - queen)

- feature/latent `single neuron only fires when a concept exists: Ex: DJT, NY`
  - feature visualization `also call Activation Maximization: Determent a feature neuron, then generate a input to maximize the feature neuron's output. Look that input represent. https://openai.com/index/microscope/`
  - high low frequency detector `many AIs uses this to find how sharp, smooth to find boundary`
- circuit `prune/SAE`

> Feature Frequencies matters a LOT for SAE(Sparse Auto Encoder), infrequence features SAE may not learn.

> Feature can inhabit another feature.

**Reasoning Tuned**
> Fine tuning with verifiable task

- Reinforcement Learning with Verifiable Reward(RLVR)

### Superposition
>
> One neuron → Multiple features; Math explanation: in higher dimensions, vectors are likely about about 90 degree(ALMOST perpendicular to another vector); Therefore as dimensions increase, the numbers of ideas can store increase exponentially.
> > Just think in 2D, relax perpendicular constrain will leave 2 small triangles space near Y axis. These 2 small triangles space in 3D will become 2 "walls", many vectors can lives in these 2 "walls". As dimensions increase, more space available for ALMOST perpendicular vectors.

> <https://www.alignmentforum.org/posts/iGuwZTHWb6DFY3sKB/fact-finding-attempting-to-reverse-engineer-factual-recall>

- Circuitry `neuron connections`
  - AIs shows some common Circuitry across different models seems be useful. `IMO, Circuitry = habit; Promote Engineer = Cue; fine-tunning = repeat to strengthen;`
  - Steering LLM `Forcefully fire llm features/neurons`
  - Superposition `One neuron → Multiple features; also explain why llm get confused when similar ideas present at once.`
- Feature Visualization
  - Attention Mechanism Analysis – Understanding how attention layers in transformers allocate focus.
    - Activation Engineering – Analyzing and modifying neuron activations in neural networks.
    - Token-level Interpretability – Studying how individual tokens influence model outputs.
    - Representation Learning Analysis – Exploring the embeddings and internal representations learned by AI models.
    - Gradient-based Interpretability – Using gradients to understand decision-making processes.
- Model Debugging
  - causals intervention is great tool to exam AI features
- AI Alignment
- AI Safety

### SAE
>
> The goal is reduce input dimensional space to reduce noise.
> The lose function of Sparse Modeling has extra Regularization to encourage sparsity in the network

x = D * α

- x `input signal`
- Dictionary (D) `n(input size) by k matrix; Think as collection of basic feature sets;`
- n `flatten input(x) size; also dictionary's width`
- k `dictionary's columns, usually bigger n`
- α `multi hot encoding vector;`
- l0 `norm is counting the non-zero in α`
- atom `a column from dictionary; think as a basic feature set;`

> input = collection of atoms from Dictionary

> The goal is find a dictionary where each data will repr by a few atoms from dictionary.

Relaxation (Basic Pursuit)
Go Greedy (Matching Pursuit)

Predefined dictionary: steerable, wavelet, curvelet, contourlets, bandlets.

Sparse Identification of NoneLinear Dynamics(SINDy) converts time-series data to sparse model

sparse optimization algorithm

- Least Absolute Shrinkage and Selection Operator(Lasso)
- Orthogonal Matching Pursuit (OMP)
- Basis Pursuit (BP)
- Matching Pursuit (MP)
- Elastic Net
- Hard Thresholding

> Sparse Auto Encoders(SAE) can find a lot (maybe most) of features, but for sure some LLM understand features are not found in SAE.

**Activation density**
> Most transformer neuron fires under 0.5%; early layers fires more than later layers. But human cortex Activation density ~ 1-5%.

## Paper

### Notable Papers & Ideas

- Attention is all you need
- **“GPT‑3: Language Models are Few‑Shot Learners”** – Radford et al., 2021  
- **Tree of Thought**  
- **Anthropic’s “Scaling Monosemanticity”**  
- **Position Interpolation for Extending Context Window in Transformers** – OpenAI, 2023  

### New Research Directions

- **Leave No Context Behind** – Google’s approach to extending context windows.  
- **Dynamic Routing Between Capsules** – Capsule Networks.  
- **TransformerFAM** – Feedback attention as working memory.  
- **Attention with Linear Biases (ALiBi)** – Adds a distance‑based linear bias to attention scores, giving higher weight to closer tokens.  
- efficiency is part of the intelligent feature, keep increase token to solve solution is similar to brute force search. Both DATA & COMPUTE Efficiency.
- Maybe the problem LLM is aggregate learning. Human individual have memory system that can retrace in time. Maybe aggregate learning in training phrase prevent it have memory system. We need a training system that have strong memory module, and have llm reflect on those memories. `IMO current LLM still have very low memory absorption rate, it uses aggregate learning to compensate low memory absorption`
