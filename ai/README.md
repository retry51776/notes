# AI

## Inference Stack
```md
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
```

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


## Tradeoff

- capacity utilization vs sensitivity/robustness
- capacity vs compute
- throughput vs compute
- Plasticity vs Generalization
  - Generalization rely on noise cancel out each other.
- Stability-Plasticity Dilemma
  - BP has strong constrain on network stability. dynamical isometry!