# AI
> I break down my AI notes into:

- Academic
- Industry
- Hardware
- IMO


## Human ability
- Input
  - ~~Hearing~~
  - Taste `limited by hardware`
  - Smell `limited by hardware`
  - Visual Perception
      - ~~Read~~
      - ~~Body Language Perception~~
      - Surrounding Awareness `Tesla already achieved`
  - Touch `Very hard for robot`
    - pressure
    - warmth
    - cold
    - pain
  - Kinesthesis `senses body movement and position`
  - Vestibular `monitor head's position and balance`
- State
  - Desire `do we want AI has its own desire?`
  - Understanding `AI already does; But we don't even know how brain makes conclusion, how we jude AIs' conclusions? Is it computation or storage?`
    - holding state across time `runtime compute`
    - AIs self conclusion
    - human conclusion
    - physical world conclusion `will soon better than human`
    - visual understanding `But not understand yet; One day a AI watch all Youtube Videos will smarter than any human`
- Output
  - ~~Listen & Speak~~
  - ~~Read/Write~~
  - Taste & Smell `limited by hardware`
  - Mobility `hard to achieve, Boston Dynamics`
      - Touch `hard`
      - Proprioception `body position`
      - ~~Body Language Expression~~
      - Stamina `biology is very effective`


# Tech
- Tiling `calculation by smaller block, uses scaler to rescale each row to combine whole`
- Recomputation `Don't store, recompute to save RAM`

- compute is NOT the bottleneck, rather is Memory size.

- Mixture of Expert(MOE) `combine smaller models`
- Multi Query Attention `reduce attention head to output to increase speed

- L1 regularization `L1 regularization penalizes the sum of the absolute values of the weights in the network. This encourages the network to use a smaller number of weights, and it can also help to prevent over fitting.`
- L2 regularization `L2 regularization penalizes the sum of the squares of the weights in the network. This also encourages the network to use a smaller number of weights, and it can also help to improve the generalization performance of the network.`

- Parameter Efficient Fine Tuning(PEFT)
- LoRa `Attach extra weight to original model feed forward layer, then train these extra weight; usually mb size`
- Prefix Tuning
- P tuning
- Prompt Tuning

- https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard