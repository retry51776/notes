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
    - radiology
  - Observability (privacy block some industry)
  - variance?
    - messy real-world physical manipulation
    - standard formats?
    - student in edu process (different success rates)
- output
  - digital? (text, image, audio, video, code, or structured decisions)
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

> Token(LLM output) is NOT what we want, it's just an intermediary. We don't want to read answer, rather we want to CHANGE/LEARN our BRAIN(residual stream) by reading answer.

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

## FAQ

- LLM is **NOT** a function ONLY generate single token, residual stream can decode as **full shifting tokens**. That's why we can pre-train LLM with huge amount data.
