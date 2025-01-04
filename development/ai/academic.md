# Academic

- General
- Biology
- Analogy
- Training

## General

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
    - This solution may be another AI itself?

### Neural Network Terms

- Learning Workflow
  - Forward Propagation
  - Backward Propagation
    - Lost
- Neuron `fundamental unit in a neural network that performs a simple mathematical operation on input data and passes the result to other neurons or output units`
  - Activation function
  - Weight
  - Bias `a value that is added to the output of a neuron before it is passed to the next layer.`
- Auto Model Compression `pruning as reinforcement learning problem`

- Tiling `calculation by smaller block, uses scaler to rescale each row to combine whole`
- Recomputation `Don't store, recompute to save RAM`

- compute is NOT the bottleneck, rather is Memory size.

- Mixture of Expert(MOE) `combine smaller models`
- Multi Query Attention `reduce attention head to output to increase speed

- L1 regularization `L1 regularization penalizes the sum of the absolute values of the weights in the network. This encourages the network to use a smaller number of weights, and it can also help to prevent over fitting.`
- L2 regularization `L2 regularization penalizes the sum of the squares of the weights in the network. This also encourages the network to use a smaller number of weights, and it can also help to improve the generalization performance of the network.`

- Parameter Efficient Fine Tuning(PEFT)
- LoRa `Attach extra weight to original model feed forward layer, then train these extra weight; usually mb size`

## Biology
>
> Human have 100 trillion connections, to process related small experiences. LLM currently have 10 trillion connection to process all human writings.

> Brain uses Sparse Repr, it save energy, resilient to noise

> One major differences is NN can do backward propagation. But neuron synapse only fire single direction.

## Analogy

- Weights = binary of programs.
- Activation = memory/state of programs.
- Neuron = assembly instructions.
- Architecture = VM/compiler/Runtime of program.

> Think of AI as a kid, we are designing games to see which game `architecture` help AI `kid` grow;

> LLM is similar to foreigner that can see & draw picture with 1409 points;

<hr>

# Mechanistic interpretability
>
> AI mechanistic interpretability is a field that will give a lot insight of how human brain works.

- Physics Informed Machine Learning
- Stable diffusion: add noise to image, let AI recover image;

> Netron: Interactive model graph exploration.
<https://www.neuron.app/>

## linear representation
>
> Currently(2024) common agreement is AI uses linear representation to store concepts. (evident by man - women = king - queen)

- feature/latent `single neuron only fires when a concept exists: Ex: DJT, NY`
  - feature visualization `also call Activation Maximization: Determent a feature neuron, then generate a input to maximize the feature neuron's output. Look that input represent. https://openai.com/index/microscope/`
  - high low frequency detector `many AIs uses this to find how sharp, smooth to find boundary`
- circuit

> Feature Frequencies matters a LOT for SAE(Sparse Auto Encoder), infrequence features SAE may not learn.

> Feature can inhabit another feature.

## Superposition
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

<hr>

# Paper

> Break into 4 types

- Classic `Great Improvement`
- New Research `Not proven`
- Tech Improve `Small improvement`

### Classic

- "Scaling Laws for Neural Language Models" by OpenAI

- "Toy Models of Superposition” by Anthropic (2022)

- "Explaining and Harnessing Adversarial Examples" by Ian Goodfellow, et al. (2014)

- "Human-level performance in multi-task reinforcement learning" by Volodymyr Mnih, et al. (2015)

- "Attention Is All You Need" by Vaswani, et al. (2017):
  > Position encoding is similar how external ear changes noise a little for brain detecte position.
  > GPT4 has 220 billions parameters; 16 way mixture model; 8 set of weights;

  > Filter query step:
  The idea is embedding layer encoded w position info. Then train attention matrix(n^2) to capture relationship weights; Then attention matrix times embedding layer to get filtered input.

- "The Lottery Ticket Hypothesis" `reuses pruned large network's connection & weights; iterator pruning; some network only need 3% weights same performance.`

  > Deconstructing Lottery Tickets: magitude_increase is best, large final is easy & pretty good.

- The Dark Matter of Neural Networks `By Chris Olah; explore NN features.`

### Tech Improve

- "GPT-3: Language Models are Few-Shot Learners" by Alec Radford, et al. (2021)

- Tree of Through

- Anthropic’s “Scaling Monosemanticity”

### New Research

- Just forward passes

- Dynamic Routing Between Capsules `Capsule Networks`

- TransformerFAM: Feedback attention is working memory

- Attention with Linear Biases (ALiBi) `ALiBi addresses this problem by adding a linear bias to the attention scores between each query and key. The bias is inversely proportional to the distance between the query and key, so that closer tokens have a higher attention weight than more distant tokens. This helps to ensure that the model focuses on the most relevant tokens, even when the sequence is very long.`

- Flash Attention achieves its speed and memory efficiency by using a number of techniques, including:

  > Tiling: The attention computation is divided into smaller tiles, which are computed in parallel.
  Sparse matrix multiplication: The attention scores are computed using sparse matrix multiplication, which is more efficient than dense matrix multiplication.
  IO-awareness: The attention computation is carefully designed to minimize the number of memory reads and writes.

- Retrieval Enhanced Transformers (RETRO) are a type of language model that combines the strengths of both retrieval-based and generative models. RETRO models first retrieve a set of relevant documents from a large corpus, and then use a generative model to generate text that is consistent with the retrieved documents.

- SynFlow prune network connection by assign score to each connection. score = dervitity_lose / dervitity_weight * weight; Because we want to prune connection auto balance between layers(I am not 100% agrees here.)

- Quantized is normalized weight & activation input & output. But outlier weight is problem. maybe need split out outlier process.

# Open AI Ideas

> The age of pre-training is over.

Open AI Imagines AGI in 5 phrases:

- Chatbot
- Reasoning and Planning
- Agent able analysis & take actions
- Innovation able to Innovate
- Organization

Reinforcement Learning for "Open AI Strawberry" components

- 1. Policy Initialization
- 2. Reward Design
- 3. Search
- 4. Learning

- Goal qualification
  - Outcome Reward Maximization (ORM) `reward by final outcome`
  - Process Reward Maximization (PRM) `reward per step, good for Math, coding`
- Task Decomposition
- Alternative proposal
- Solution generation `llm bad at`
  - Best of n sample | Beam Search | Monte Carlo Tree Search | Sequential Revision
  - self evaluation `llm good at`
  - Solution Level Search, Step Level Search, Token Level Search
- self correction

Training more likely Beam Search, inference more likely Sequential Revision

- Scaling of Search and Learning: A Roadmap to Reproduce o1 from Reinforcement Learning Perspective

> <https://docs.neuronpedia.org/> inspect llm neuron meaning.

# SAE
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
