## Hardware
> Machine Learning Frameworks(PyTorch) > Acceleration Driver(cuDNN) > Hardware(GPU)

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
- https://huggingface.co/TheBloke


## Dataset
- BooksCorpus
- WebText
- Common Crawl