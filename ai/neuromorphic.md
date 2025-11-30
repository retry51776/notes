# Neuromorphic
>
> Human have 86 billion neurons with 100 trillion connections, to process related small experiences. LLM currently have 10 trillion connection to process all human writings.

> Brain uses Sparse Repr, it save energy, resilient to noise

> One major differences is NN can do backward propagation. But neuron synapse only fire single direction.

> Skill-Acquisition Efficiency (by Francois Chollet)
>> Also LLM can slowly adapt from same situation(same input) by repeat multiple cycles, but animals usually only experience situation once.

> Human don't receive error, we get feedback from interaction. But error can back propagation, but how to back propagation feedback? Maybe that's why positive discipline works, maybe success easier learned(back propagation) than failure. (I don't think it's success or failure matter, rather emotional level) <https://arxiv.org/abs/2406.08747>
>
## Neuron Plasticity
>
> There are many dimensions neuron plasticity;

**Fractals** are geometric shapes or patterns that show self-similarity across different scales.

- Neuron Synapse Length
- Neuron Oscillating Frequency
- NMDA receptor - biology mechanism explained `Hebbian rule: fire together wire together;`

- Neuron
  - spike - will flow both dendrites(input) & axon(output);
  - dendrites
    - apical dendrites(far away from nucleus)
      - NMDA receptor - trigger by internal spike
    - basal dendrites(near nucleus)
      - NMDA receptor - trigger by neighbor dendrites simultaneously spiked
  - nucleus
  - axon

## Speculation

- Biologist shown people practice skill will REDUCE amount brain regions uses, but LLM ALWAYS has SAME activation paths, NO MATTER how many times LLM already processed same input.
  - We need incentive/system LLM REDUCE its forward propagation path after repetition input.
    - Maybe SAE/ observation NN to Shorten forward propagation path?
    - Note: This system itself ALSO explain why human makes many mistakes

- Most likely things evolution optimize for long time will be harder to achieve in AI.
  - Parameter is similar to gene, DNA often has duplicate genes, allow intermediate modification without disrupt current process. More parameter in LLM allows more paths get to desire network.

## Books

- A thousand brains
  - 6 Layers
    - 1. wired network
    - 2 & 3: communication with other cluster
    - 4. Input(sensory or layer 2 & 3 output from other cluster)
    - 5. Action(Motor or attention movement)
    - 6. Place
