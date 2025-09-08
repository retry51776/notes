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
  - Decouple Input & Output
  - Output interruption & Input interruption
  - Improve LLM from understand to apply tools `aka from understand to doing`
- ??: dynamic model

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
    - This solution may be another AI itself?

### Neural Network Terms

- Learning Workflow
  - Forward Propagation
  - Backward Propagation
    - Lost
    - ε (epsilon) `a tiny constant (typically 1e-5 or 1e-6); learning rate unit`
- Neuron `fundamental unit in a neural network that performs a simple mathematical operation on input data and passes the result to other neurons or output units`
  - Activation function
  - Weight
  - Bias `Doesn't uses in attention blocks`
- Auto Model Compression `pruning as reinforcement learning problem`

- Hill climbing `strong signal, LLM training`
- Sharded `Split LLM into chucks`
- Tiling `calculation by smaller block, uses scaler to rescale each row to combine whole`
- Recomputation `Don't store, recompute to save RAM`

- Mixture of Expert(MOE) `combine smaller models`
- Multi Query Attention `reduce attention head to output to increase speed

- L1 regularization `L1 regularization penalizes the sum of the absolute values of the weights in the network. This encourages the network to use a smaller number of weights, and it can also help to prevent over fitting.`
- L2 regularization `L2 regularization penalizes the sum of the squares of the weights in the network. This also encourages the network to use a smaller number of weights, and it can also help to improve the generalization performance of the network.`

- Parameter Efficient Fine Tuning(PEFT)
- LoRa `Attach extra weight to original model feed forward layer, then train these extra weight; usually mb size`

- Position Interpolation `extend context window without`

- gradient descent `Compute batch avg lose, nudge a little by batch avg lose direction. It works because unlike it stuck at local min, stuck requires all dimensions are at local minimum at the same time`

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

- x `input tokens`
- len(x) `input length`
- Q `Q = x * Wq, positional specific`
- K `K = x * Wk, position agnostic`
- V `V = x * Wv, position agnostic; each token possible meanings(need filter by contextual score)`
- $ QK^T $ `d_model * len(x), contextual score`

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

<hr>

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

Tools:

- TransformerLens

### Linear representation
>
> Currently(2024) common agreement is AI uses linear representation to store concepts. (`vector analogies` man - women = king - queen)

- feature/latent `single neuron only fires when a concept exists: Ex: DJT, NY`
  - feature visualization `also call Activation Maximization: Determent a feature neuron, then generate a input to maximize the feature neuron's output. Look that input represent. https://openai.com/index/microscope/`
  - high low frequency detector `many AIs uses this to find how sharp, smooth to find boundary`
- circuit `prune/SAE`

> Feature Frequencies matters a LOT for SAE(Sparse Auto Encoder), infrequence features SAE may not learn.

> Feature can inhabit another feature.

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
