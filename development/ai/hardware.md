## Hardware
>
> Machine Learning Frameworks(PyTorch) > Acceleration Driver(cuDNN) > Hardware(GPU)

> Different hardware needs its custom version llama.cpp. Ex(Metal llama.cpp, ROCm llama.cpp, CUDA llama.cpp)

- near memory design:
- reconfigurable dataflow hardware vs parallelism on top of existing computation

> At the end of the day, only limitation is space; space either assign to computation(flexible or efficiency) or storage(latency or throughput);

## Training

- cuDNN
- Deep Learning GPU eXtreme(DGX) A100 server = 8 (A100 80GB GPU)
  - V(Volta)100 GPU
    - original GPT trained w 10,000 V100 GPUs
    - GV100, GA100, GH100,
      - Tensor Core that specialize in matrix multi
- HGX
  - H(Hopper)100 GPU
- APU

- DGX server have sister product (HGX server)High-Performance GPU (Graphics Processing Unit) eXtensible

## Inference

- <https://huggingface.co/TheBloke>

## Dataset

- BooksCorpus
- WebText
- Common Crawl


# AMD
> AMD uses Hipify to convert CUDA into AMD HIP.

# Nvidia
> A100 cost at least $10k
> DGX cost at least $350k, includes 8 A100 GPUs

- Training Tools
  - AI Enterprise (AIE) `charge by GPU`
  - AI Workbench
    - Single GPU
- Inference Tools
  - NVIDIA Inference Microservices (NIM)
    - Jupyter Notebook as Workbench
    - Standardize RESTful APIs

Nvidia Terms:

- Nvidia Base Command `enough for most devs`
- Nvidia Suit Command `edge vision deployment`

- VCenter `Aka Nvidia Cloud console, create VM`

Create VM steps:

1. Define hardware profile
2. Software `NVD guess driver & container toolkit`
3. App Config `aka volume, container, software, etc. Analogy: room blueprint`
4. Template Config `reusable blueprint; Analogy: house blueprint`
