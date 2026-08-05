# AI
>

> I break down my AI notes into:

```text
/ai
├── /cheetsheet
│   └── aider.md
│   └── claude.md
│   └── experience.md
├── /skills
│   └── README.md
│   └── /pitfalls
│       └── SKILL.md
├── /static
│   └── *.png / *.jpg / *.gif (AI diagrams, charts, and animations)
├── academic.md (basic terms)
├── architecture.md (Adv)
├── hardware.md
├── mathematic.md
├── neuromorphic.md (relates to human neurons)
├── imo.md (unorganized notes)
└── industry.md
```

Most likely automate by AI industries traits:

- input
  - digital?
    - data source?
      - by capture
        - physical data
        - human feedback
      - by generate
        - simulation
        - verification
  - observability?
  - variance?
    - messy real-world physical manipulation
    - standard formats?
    - different success rates (Ex: student goes through same class but different grades)
- output
  - digital? (text, image, audio, video, code, or structured decisions)
  - observability?
  - variance?
    - human target audience will have big variance (differ mood, preference)
    - human has more native control on voice than AI
    - code low variance because IDE execute result same
    - time-horizon variance
      - hiring decision, policy design, medical treatment plan
    - uncertainty
      - poker, strategy result, therapy resp
  - Incentive alignment
    - Education/politics/art
- huge volumes of historical data (code, movie)
- workflows that repeat at scale

## Analogy

- AI today mirrors 19th‑century chemistry. Metallurgist(AI scientist) through heat(computation) turn iron ore(raw data) into a refined steel (LLM model). The value of the iron ore(data) isn’t measured by sheer quantity, rather resides in the Iron Content (world knowledge & logic).

  - Mining & Extraction → Data collection & scraping
  - Computation → Heat
  - Data center → Blast furnace
  - Data → Iron ore
  - Model → Steel
  - Fine‑tuning / specialized model training → Alloying (adding carbon to make steel)
  - Inference & deployment → Rolling & shaping steel
  - AI evaluation (benchmarks, alignment, RLHF) → Quality testing & hardening
  - AI applications → Bridges, cars, tools
  - Smart AI output token’s information density → Iron density

<hr/>

> LLM is predictive, but what we need prescriptive.
> > Token(LLM output) is NOT what we want, it's just an intermediary. We don't want to read answer, rather we want to CHANGE/LEARN our BRAIN(residual stream) by reading answer.

- Token(str: atom)
- Embedding(vector @ beginning of LLM: atom's lowest energy/identity state)
- LLM weights & residual stream(spacetime)
- World knowledge & ration(law of physics, dictate interaction atom & spacetime)

- LLM similar to spacetime with many probable_black_holes, prompt  trajectory will eventually suck into one of black hole.
  - The most obvious black_hole is the least interesting.
    - because human nature like surprise.
    - because most people already knew, therefore has very few value.
    - Pick token by logit wave, so all trajectory tokens follows natural dist(contain high logit tokens & low logit token).

## Frustrations

- Mechanistic Interpretability(mech interp) moves very slows(close source, LLM specific) while AI capability keep accelerating.
- Tech stacks are NOT decouple, hardware & software are most likely interlock.
- Memory Hierarchy(both hardware & LLM)
  - Hardware: Disk < Infinity Switch < InfiniBand < HBM < L1 cache
  - LLM: fussy memory @ LLM weights < determinist memory @ context window < relevant memory @ residual stream
- Hardware failure needs complex multi level monitor system
- Some LLM(Ex: qwen) refuse answer when there is only single system message
- Lot of small file (LOSF) may cause random unmount volumnes; patch with `autofs`
- verify that their InfiniBand network is properly isolated
- It's SO hard to estimate RAM requirement when running training.
  - LLM answer length variance.
  - No ideas 3rd party libraries doing, what RAM they need.
- Measure LLM is very hard, and expensive.

## Interesting POV

- LLM is predictive, what we need is prescriptive.
- LLM, Brain are networks; with 2 perspective: `inference goal` & `network control theory`.
- The training data property that LLM relied on: random noise will average out evenly, logical behavior will NOT average out because logical behavior property is consistency.
- There are no irreducible logic.
- Memorization is goal / emergent behavior, not fundamental operative. Ex: DB also achieve memorization, but its fundamental operative is balance tree.
  - Sure transistor acts like a switch, so most fundamental operative is ALWAYS if statement.
- LLM is **NOT** a function ONLY generate single token, residual stream can decode as **full shifting tokens**. That's why we can pre-train LLM with huge amount data.
- LLM weights functions
  - inference weights
    - deterministic (Ex: embedding, LM head, RoPE)
    - compute (Ex: Attention V, MLP)
      - Matrix Ops ~ divide & conquer & regroup(robustness & superposition)
    - routing (Ex: DSA, MOE, maybe even attention score)
      - benefit: decouple gradients, partition representational space, reduce interference
    - stability control (Ex: normal layer)
  - training weights
    - loss function
    - optimizer state
      - direction
      - momentum
    - activation/activation checkpoints
    - custom settings (Ex: LR, decay)

## Tradeoff

- capacity utilization vs sensitivity/robustness
- capacity vs compute
- throughput vs compute
- Plasticity vs Generalization
  - Generalization rely on noise cancel out each other.
- Stability-Plasticity Dilemma
  - BP has strong constrain on network stability. dynamical isometry!


## DL Theory

weight matrix ~ transformation;
- spectral norm ~ single scalar number represent max stretch

activation function ~ cut after transformation; irreversible change;

Known layer weight constrains:

- Weight Distributions Gaussian; (NOT normal distributions)
  - Heavy-Tailed Weight Spectra; (Many weights end up contributing very little)
- mean ~ 0
  - Weight Updates Have Mean Near Zero
- variance ~ 1/n
  - Stable Activation Variance Across Depth
- magnitudes ~ $|W_{ij}| \propto \frac{1}{\sqrt{d}}$
  - largest individual weight can never exceed the spectral norm
  - Row/Column Norms Tend Toward Similar Scale

- singular values ~ 1 $\sigma_i(W) \approx 1$
- Effective Rank Is Usually Much Lower Than Matrix Size
- Symmetry Must Be Broken
- Scale Symmetries Exist; if W1 -> 2W1; then shrink W2 -> 0.5W2; can undo;

Training:
- In training both signal % & noise % reach constance ratio;  gradient = signal + noise;
- Different Attention Heads Specialize
- Features Become More Orthogonal `aka remember differences`