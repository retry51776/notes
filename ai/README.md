# AI

## Inference Stack
1. [General ML Framework](./academic.md)
   PyTorch / MLX / TensorFlow / JAX
   └── tensor ops, compiler, kernels, autograd, hardware backend

2. [Model Artifact](./industry.md#model-arthifact)
   **safetensors** / GGUF / ONNX / mlpackage
   ├── weights
   ├── architecture/config
   ├── metadata
   └── tokenizer

3. [Inference Engine](./inference.md#inference-engine)
   llama.cpp / vLLM engine / TensorRT-LLM / ONNX Runtime
   └── model execution / kernel conversation
   └── KV cache
   └── batching
   └── decode
   └── quantization
   └── memory management

4. [Compute & Communication Runtime](./hardware.md#runtime)
   CUDA / ROCm / Metal
   NCCL / RCCL

5. [Compute Hardware](./hardware.md)
   CPU / GPU / Networking / Storage


## Folder Structure
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


## Frustrations

- Mechanistic Interpretability(mech interp) moves very slows(close source, LLM specific) while AI capability keep accelerating.
- Tech stacks are NOT decouple, hardware & software are most likely interlock.
- Memory Hierarchy(both hardware & LLM)
  - Hardware: Disk < Infinity Switch < InfiniBand < HBM < L1 cache
  - LLM: fussy memory @ LLM weights < determinist memory @ context window < relevant memory @ residual stream
- Hardware failure needs complex multi level monitor system
- Some LLM(Ex: qwen) refuse answer when there is only single system message
- verify that their InfiniBand network is properly isolated
- It's SO hard to estimate RAM requirement when running training.
  - LLM answer length variance.
  - No ideas 3rd party libraries doing, what RAM they need.
- Measure LLM is very hard, and expensive.
- Inference engine's random behavior, but not through error out.


## Tradeoff

- capacity utilization vs sensitivity/robustness
- capacity vs compute
- throughput vs compute
- Plasticity vs Generalization
  - Generalization rely on noise cancel out each other.
- Stability-Plasticity Dilemma
  - BP has strong constrain on network stability. dynamical isometry!