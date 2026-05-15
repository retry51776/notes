# Neuromorphic
>
> Human have 86 billion neurons with 100 trillion connections, to process related small experiences. LLM currently have 10 trillion connection to process all human writings.

> One major differences is NN can do backward propagation. But neuron synapse only fire single direction.
>> My guess is brain has vague global signal, also relies on local/regional signal(coincidence).

> Skill-Acquisition Efficiency (by Francois Chollet)
>> Also LLM can slowly adapt from same situation(same input) by repeat multiple cycles, but animals usually only experience situation once.

> Human don't receive error, we get feedback from interaction. But error can NOT back propagation(neuron only fires 1 direction), but how to back propagation feedback? Maybe that's why positive discipline works, maybe success easier learned(back propagation) than failure. (I don't think it's success or failure matter, rather emotional level) <https://arxiv.org/abs/2406.08747>
>

## Interaction Principal

- abstract away upstream complexity
  - LLM uses chain rule (keep scope local)
    - Chain rule is powerful, enable bidirectional. But constrain NN flow be directional, unlike brain.
  - Brain some unknown biology
- Adapted Learning
  - LLM adjust weights
  - Brain has Neuron Plasticity
- Routing vs Compute
  - LLM uses attention, MOE as routing
  - Brain cluster has different neurons density at different layers, assume denser layers are compute, sparse layers are routing.

## Architecture

Emerge Behaviors:

- no forget mechanism
- memorized differences, memorization just emerge properties
- cluster ideas
- momentum of thinking
- hierarchy of feature extraction

Different:

- LLM NN can both forward & backward, but brain neurons can't.
  - I assume abstract upstream & adjust on cluster level, but forward and backward must be on different paths.
- LLM same compute path per token, human repeat will get easier.
- LLM's residual stream in central system. Brain has distributed residual streams.

## Neuron Plasticity
>
> There are many dimensions neuron plasticity;

**Fractals** are geometric shapes or patterns that show self-similarity across different scales.

- Neuron Synapse Length
- Neuron Oscillating Frequency
- receptor - (size changes/ learning rate) proportional to its size;
  - NMDA receptor - biology mechanism explained `Hebbian rule: fire together wire together;`

- Neuron
  - spike - will flow both dendrites(input) & axon(output);
    - Fire Rate Hz ~ Log‑Normal Distribution (effects compound multiplicatively)
      - Low Freq:
      - Med Freq: 5–30 Hz
      - High Freq: Sustained 100–200 Hz
  - dendrites
    - apical dendrites(far away from nucleus)
      - NMDA receptor - trigger by internal spike
    - basal dendrites(near nucleus)
      - NMDA receptor - trigger by neighbor dendrites simultaneously spiked
  - nucleus
  - axon

## Speculation

- citizen-initiated ballot analogy
  - Query ~ Ask ~ Sensor data; current voting ballot.
    - new_query = new_Query(Value(old_query)); After town citizen voted, collected all voted & generate new ballot for next town.
  - Key ~ Acknowledge ~ city consoles. (Duty: 1. Accept ballot; 2. Find town citizen that knows ballot;)
    - K cache ~ elected consoles's decisions;
      - K cache is same neuron, but different connections(actual value need stored).
      - K is good feedback point.
    - Score ~ citizen's attention about ballot.
  - Value ~ Answer ~ town citizens. (Duty: 1. Vote on ballot; 2. Generate new ballot;)
    - V cache ~ citizen vote history; Output control signal;
  - Residual Stream ~ propagate across dense layers
    - Brain must be distributed residual streams.

- Transformer predict 1 token is like clawing, MTP is like walking. Most likely jump skip prediction Nth tokens ~ human expectation, when exception > threshold & use expected RS & skip normal flow ~ lazy thinking.
  - Lazy thinking ~ GPU fast path (like build-in distill nn)
  - Normal Transformer flow ~ GPU slow path
  - deep thinking ~ fork to deep nn flow

- Both MOE & Group Query Attention (GQA) size prove that we needs to avoid connects every ideas together.
  - Local & Smaller cluster are easier to adapt, less cross interference.

- Compute density ~ neuron density.
  - neuron density has upper limited. Sometime people can't change, Maybe their neuron cluster overcrowded, new neurons don't have room to growth.
  - Similar to superposition interference.

- Amortize ~ LLM learn Monte Carlo search/beam search within its internal process.

- We can simplify human inference to the point upload to cloud. But simplification will distort actual human development trajectory.

- Communication Through Coherence (CTC) `Neurons that fire in the same oscillation phase communicate more effectively.`
- Reward Shaping ~ partial credit;
  - Dopamine ~ partial credit for reproduction. Reproduction is final reward, but too sparse. So Dopamine is partial credit for actions leads to reproduction.

- hypothesis: Neuron naturally has incentive balance activity across networks.
  - Over active neurons will die out.
  - Consistence input will active SAME path which neuron don't want. (aka bored)
  - homeostatic plasticity: Each neuron has its own prefer fire freq.
    - Rare token must shares with other things increase its fire freq.

- Biologist shown people practice skill will REDUCE amount brain regions uses, but LLM ALWAYS has SAME activation paths, NO MATTER how many times LLM already processed same input.
  - We need incentive/system LLM REDUCE its forward propagation path after repetition input.
    - Maybe SAE/ observation NN to Shorten forward propagation path?
    - Note: This system itself ALSO explain why human makes many mistakes

- Sleep time has strong correlation with rapid/burst response time. Ex: cat, snake, crocodile, bats, sloth.
  - no obvious correlation with intelligent
- Most likely things evolution optimize for long time will be harder to achieve in AI.
  - Parameter is similar to gene, DNA often has duplicate genes, allow intermediate modification without disrupt current process. More parameter in LLM allows more paths get to desire network.

- Knowing is dig a hole in ground; Doing is expand that hole, so near by will fall into hole.

- Deep Equilibrium Models ~ cortex clusters reach consensus equilibrium(neuronal avalanches)
  - neuronal avalanches ~ only trigger when cluster agrees(cluster reach equilibrium)
    - wake-up grumpiness ~ not reach equilibrium caused frustration
    - repeat task get easier ~ easy stay in equilibrium

## Entrorhinal cortex
>
> The entorhinal cortex is the major interface between the neocortex and the hippocampal formation.

> Near by hippocampus that provides general coordinate system. Acts similar to RoPE in transformer.

## Hippocampus

- hippocampus replay/preplan ~ RL fine tuning
- Psychological dimensions @ Hippocampus: Power & Affiliation
- Path Integration / Coordination : project relation into algorithm operable space

## Terms

- Temporal-Difference (TD) Learning `Learn by comparing what you expected now vs. what you expect next.`

## Problems

- Brain Neurons inherent have different behavior with different input seq, but AI Neurons if inputs are same = output same;
- Takes CNN 5~8 layers to simulate single cortical neuron.

## Org

- <https://braininitiative.nih.gov/>

## Books

- [dynamical system in neuroscience]

- A thousand brains
  - 6 Layers
    - 1. wired network
    - 2 & 3. communication with other cluster
    - 1. Input(sensory or layer 2 & 3 output from other cluster)
    - 1. Action(Motor or attention movement)
    - 1. Place

  - Transformer Similar to cortex cluster
    - 1. Expert Router
    - 2 & 3. Q.K increase connections surfaces
    - 1. Tokenizer
    - 1. Output
    - 1. Embedding/RoPE

### dynamical system in neuroscience

<https://www.izhikevich.org/publications/dsn.pdf>

Hodgkin-Huxley model:

- limit cycle - `area that neuron will repeatedly spike`
  - Voltage nullcline - keep V constance
  - n-nullcline - potassium channel gating variable (n) is in equilibrium with the membrane voltage.
- stable equilibrium  - `area that neuron will be stable & won't spike`

- Formula
  - Membrane Voltage Equation = I_Na + I_K - I_leak
  - 3 Gating Variable Equations
    - sodium activation (m)
      - very fast, most important, trigger spike
      - pull Na⁺ ions, more positive
      - Input has 2 dimensions: % channels & voltage
    - sodium inactivation (h)
      - Na⁺ entry stops, trigger soon after Na⁺ entry
      - not critical
    - potassium activation (n)
      - remove K⁺, more negative
      - Na⁺/K⁺ ATPase pump continuously restores the balance

- Integrator Neurons - cumulative inputs, spike/output is fixed; input timing does NOT matter;
  - Saddle Node `no periodic output`
  - Saddle-Node on Invariant Circle `periodic output with single input`
- Resonator Neurons - depends on input timing, input can either strength or weak output
  - Subcritical Hopf ~ SiLU; spike/output is variable;
  - Supercritical Hopf ~ SiLU with positive bias; spike/output is variable AND always on;

- state variables:
  • Membrane voltage V
  • Gating variables (m,h,n)
  • Synaptic currents
  • Population firing rates


## Psychology Interpretation

Way to interact stubborn people, it's not through BP, rather introduce diverse input (ask questions).