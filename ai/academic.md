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
    - Shampoo
    - K-FAC
    - Muon - Take the gradient of a matrix, normalize it, orthogonalize it, then apply a clean step.
    - Adaptive Moment Estimation (ADAM)
      - magnitude $v_t = \beta_2 \cdot v_{t-1} + (1 - \beta_2) \cdot g_t^2$
      - momentum $m_t = \beta_1 \cdot m_{t-1} + (1 - \beta_1) \cdot g_t$
        - Ideas is oscillation will cancel out momentum, while continue acceleration will accumulate momentum;
    - RMSprops
      - derivative ~ change direction; `dW = W - a(dW/sqrt(dW))` not adapt/learn when inconsistent direction/lose
    - This solution may be another AI itself?
      - `[lr, momentum, weight_decay]`
      - `params` groups parameters into many groups with different `lr`.

### Neural Network Terms

- Mathematic Basic
  - numpy basic <https://github.com/RoyiAvital/Julia100Exercises>
  - activation functions
    - Relu - range 0 to x;
    - SiLU - GPT-OSS; likely range from -1 to 50
    - GELU - (Gaussian Error Linear Unit)
    - cosin ~ measure alignment
    - sin ~ measure orthogonal difference
    - tanh ~ single softmax conversion with offset; output: zero-centered, −1 or +1
    - sigmoid ~ single softmax conversion; output: 0 or 1;
    - softmax ~ Mutual exclusive
  - distribution
    - variance stable: $fan_{in} \cdot \sigma^2 \approx 1
\quad\Rightarrow\quad
\sigma^2 \approx \frac{1}{fan_{in}}$
    - activation function's tendency to decrease the signal variance; (Ex: Relu drop all negative variance)
    - gain: how much matrix/weight need to compensate lost variance.
    - Explains why warn up period, as training continue, individual layer will lost variance stable, but cross layers(the whole network) stable.
- Basic General
  - Forward Propagation
  - Backward Propagation
    - Lost
    - ε (epsilon) `a tiny constant (typically 1e-5 or 1e-6); learning rate unit`
    - $J(\theta)$ `the loss function / objective function being minimized`
  - Tiling `calculation matrix multiplication by smaller block, each SM loads target block row & col to calculate small final result block`
  - Neuron `fundamental unit in a neural network that performs a simple mathematical operation on input data and passes the result to other neurons or output units; weights usually gaussian distribution`
  - Activation function
  - Weight - Usually range from -1 to 1
  - Bias - Usually small; Doesn't uses in attention blocks;
  - Output - center around 0 because normalization layer;  Activations Density under 0.5%
  - Hill climbing `strong signal, LLM training`
  - Residual Stream `contaminated every head's output; size(RS) = n_head * size(head); The widest part of LLM`
    - Attention Hidden States `Each attention head state; size(hidden_state) = len(Q)`
      - Logit values `the token level raw scores before softmax`
      - Temperature `logit denominator; High temperature value shrink all logit value(shrink differences), small temperature enlarge logit differences.`

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
- Weight decay `shrink weight by 0.9999 every iteration toward 0`
  - The easiest way to increase logit differences is to increase vector norms. To avoid this, we counter with weight decay.

- Position Interpolation `extend context window without retrain`
- Groking `Training lost doesn't improve & Testing lost is huge. Continues training will sudden have testing lost improve, and stabilize testing lost.`

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

> Token is atomic unit of LLM input & output. Frequent words should encode into single token. Token map can both algorithm assign or learn by nn.

> Multiple segmentations are possible. Ex: "abc" -> "ab" + "c" or "a" + "bc"

> Tokenizer applies greedy longest-match-first rule

Modern Tokenizer usually

- ALL integer values from 0 to 999(improve LLM reasoning capability)
- All ASCII English characters
- Last resort: fall back to byte tokens(raw bytes 0–255); Worst-case 4 tokens per char

Tokenizer components:

- `normalizer` applies Unicode transformations before pre-tokenization.
- `pre_tokenizer` breaks raw text into initial chunks before BPE/Unigram encoding happens
- `model` (the core) defines:
  - vocabulary
  - token <-> id mapping
  - merge rules
  - Unigram probabilities`
- `decoder`
- `post_processor` Adds tokens after encoding
- `trainer`

No standard tokenizer reasons:

- Tokenizers must fit the training distribution
- Vocabulary size dramatically affects compute
  - 1B–7B → 50k vocab
  - 30B–70B → 200k vocab
  - 400B+ → 300k+ vocab (DeepSeek-V3, GPT-4 class models)
- Models use different internal control tokens
  - reserved space for future tokens (~10k slots)

Important notes:

- How to encode numbers will effect LLM reasoning
  - GPT-120 encodes from 0 to 999
- Whitespace handle important for coding
- all Unicode characters and sequences are encoded
- Keep trace of avg_token_bytes ratio

### Back Propagation
>
> There’s a mathematical result showing that a neural network with just two layers can approximate any function. The challenge, however, is that we don’t know how to efficiently optimize the weights to reach those solutions.

> The chain rule says: Total effect = (effect on intermediate) × (effect of intermediate on final)

> Chain rule backprops prerequisite: nn is DAG(no Cyclic graph).

#### Implicit Differentiation
>
> Deep Equilibrium Models(DEQ) are Cyclic graph without unroll, just find equilibrium destination token.

> Standard backprops with chain rule is inefficient(unroll costs RAM & compute) to solve Cyclic graph(has loop).

Mathematic prerequisites:

- Explicit equation `y = f(x)` vs Implicit equation `g(x, y) = 5` describe relationship
  - Equilibrium Theorem @ Dynamical Systems `some condition will guarantee Equilibrium Set exists`
  - Equilibrium/Fix Point/Rest State `derivative(f(x)) ~ 0`
    - Stable
    - Unstable
      - unstable equilibria naturally repel the very dynamics the solver
    - Saddle
  - DEQs usually don’t collapse(trajectory goes wrong Equilibrium)
    - Initialization
    - training pressure
    - still need linear projection decode head, final Equilibrium acts as final RS.
- Implicit Differentiation(ID)
  - equilibrium: nn output converges; `assume converges ~ solvable Implicit Differentiation`
  - loss: `how much adjust Weight & Bias to make nn be solvable Implicit Differentiation`
- ID Root finding methods `z where g(z) ~ 0`
  - Newton
  - Broyden
  - Fixed-point iteration
  - Trust-region methods
- Spectral Normalization

Analogy: We has mathematical tool(Implicit Differentiation ~ solvable equations), so we adjust NN from not Implicit Differentiation to become Implicit Differentiation.

FAQ:

- Limitations
  - f must be differentiable almost everywhere
  - must be stable enough (typically spectral radius < 1)
- Inference stop logic:
  - `Tolerance Threshold > (z_new - z_old) / z_new` or `Steps > Max Limit`
- Why Implicit Differentiation?
  - because Implicit Differentiation establish relationship between variables, and solvable equations.
  - Implicit differentiation is used because we do not want unroll the cyclic graph.
  - Assume repeat nonlinear activation function over deep of NN.
  - Constant Memory Usage, no intermediate activation storage.
- Why not standard backprops? because we want Cyclic graph for reduce LLM variables(weights & bias).
- Why Cyclic graph? We ASSUME cycle will reduce LLM variables. ~ 10x smaller parameters, but ~2x slower inference

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

> Dynamic Activation Pruning and Optimization (DAPO): L1 that prune inactive / low-importance neurons or channels during training

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
- introspective awareness: LLM should self aware injected thoughts(by path activation).

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

## Stability knob

- Gradient Control
  - Warmup
  - Weight Decay
  - Gradient clipping
- Weight Initialization Knobs
  - Xavier
    - Layer Gain
  - Shrink Residual Connect effect
- Normalization/Layer
  - Softmax behavior
  - Precision
- Architecture Control
  - Trade Deep with width
  - Activation Function
- Training size
  - batch size
  - seq length
  - Regularization
- Statistic Monitor
  - residual stream variance
  - attention entropy
  - ?

## Mechanistic Interpretability
>
> AI mechanistic interpretability is a field that will give a lot insight of how human brain works.

> higher-level concepts or computations reside in the middle of graphs
>> detokenization → abstract features → retokenization

**Get Start**

1. Understand EVERY components of Transformer: <https://poloclub.github.io/transformer-explainer/>  

2. Logit Lens: <https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens>
3. Anthropic’s
Interpretability Research: <https://transformer-circuits.pub/>

    3.1 <https://transformer-circuits.pub/2025/attribution-graphs/biology.html>

- Physics Informed Machine Learning
- Stable diffusion: add noise to image, let AI recover image;
  - KV Cache Incompatibility: old tokens can also attend to new token, which means the representations of all tokens must be recomputed.

- **Circuits** `sub network that perform X calculation`
- **Feature Manifold** `lives in a particular subspace of the residual stream (RS), orientation and shape are stable;`
  - rarely need more than 1–3 dimensions
  - can live inside many RS channels at once

### Feature Manifold

 • positional manifolds
 • semantic/subspace manifolds
 • category clusters

1. Collect RS activation contains Manifold
2. Uses PCA/UMAP reduce/compress activation, hope variance drops very fast after the first few components

> Netron: Interactive model graph exploration.
<https://www.neuron.app/>

Techs:

- causal interventions
  - ablation (Ex: Attention head ablation)
  - replace
    - Patchscopes `Swap activations from a clean run into a corrupted run to test causality.`
    - Replace with randomness noise `check target feature impacted or not`
  - Feature Attribution Methods `interpret from Magnitude of gradients`
- interpretability methods
  - vocabulary projection
  - Probs - Individual neuron activation indicate x feature
  - find/confirm/project correlations in different scales
    - confirm/find: Create Tasks with known Answers & difficulty, measure LLM KPI differences; aka increase contrast find conclusion

Tools:

- TransformerLens
- nnsight
- PCA, UMAP, SVD, Ridge probing

Intuitions:

- Facts are expects to resides in early layers of FFN
- FFN can think as 'nonlinear feature generator' to each token independently at RS, not between tokens. That's why we need attention, mix tokens first, then capture 'nonlinear feature generator'.
  - FFN shared across tokens because the meaning of a feature is universal, not token-specific.

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
