# Academic

- General
- Biology
- Mechanistic Interpretability
- Paper
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
    - Many transformer implementations (like LLaMA, for example) intentionally disable biases
- Auto Model Compression `pruning as reinforcement learning problem`

- Sharded `Split LLM into chucks`
- Tiling `calculation by smaller block, uses scaler to rescale each row to combine whole`
- Recomputation `Don't store, recompute to save RAM`

- compute is NOT the bottleneck, rather is Memory size.

- Mixture of Expert(MOE) `combine smaller models`
- Multi Query Attention `reduce attention head to output to increase speed

- L1 regularization `L1 regularization penalizes the sum of the absolute values of the weights in the network. This encourages the network to use a smaller number of weights, and it can also help to prevent over fitting.`
- L2 regularization `L2 regularization penalizes the sum of the squares of the weights in the network. This also encourages the network to use a smaller number of weights, and it can also help to improve the generalization performance of the network.`

- Parameter Efficient Fine Tuning(PEFT)
- LoRa `Attach extra weight to original model feed forward layer, then train these extra weight; usually mb size`

- Position Interpolation `extend context window without`

## Biology
>
> Human have 100 trillion connections, to process related small experiences. LLM currently have 10 trillion connection to process all human writings.

> Brain uses Sparse Repr, it save energy, resilient to noise

> One major differences is NN can do backward propagation. But neuron synapse only fire single direction.

<hr>

## Mechanistic Interpretability
>
> AI mechanistic interpretability is a field that will give a lot insight of how human brain works.

- Physics Informed Machine Learning
- Stable diffusion: add noise to image, let AI recover image;

> Netron: Interactive model graph exploration.
<https://www.neuron.app/>

### Linear representation
>
> Currently(2024) common agreement is AI uses linear representation to store concepts. (evident by man - women = king - queen)

- feature/latent `single neuron only fires when a concept exists: Ex: DJT, NY`
  - feature visualization `also call Activation Maximization: Determent a feature neuron, then generate a input to maximize the feature neuron's output. Look that input represent. https://openai.com/index/microscope/`
  - high low frequency detector `many AIs uses this to find how sharp, smooth to find boundary`
- circuit

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

<hr>

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
