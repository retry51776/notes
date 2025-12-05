# AI
>
> I break down my AI notes into:

```
/ai
├── /prompts
│   └── aider.md
│   └── claude.md
│   └── experience.md
├── academic.md (Focus on theory)
├── hardware.md
├── imo.md
└── industry.md
```

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

## Frustrations

- Mechanistic Interpretability(mech interp) moves very slows(close source, LLM specific) while AI capability keep accelerating.
- Tech stacks are NOT decouple, hardware & software are most likely interlock.
- Memory Hierarchy(both hardware & LLM)
  - Hardware: Disk < Infinity Switch < InfiniBand < HBM < L1 cache
  - LLM: fussy memory @ LLM weights < determinist memory @ context window < relevant memory @ residual stream
- Hardware failure needs complex multi level monitor system

## FAQ

- LLM is **NOT** a function ONLY generate single token, residual stream can decode as **full shifting tokens**. That's why we can pre-train LLM with huge amount data.
