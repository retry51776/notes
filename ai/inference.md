# Inference



## Analogy

> Logistics Manager(Inference Engineer) that orchestrate many Postman & Cargos through rail network.
> > Don't focus on geography interpretation, rather focus on traffic management aspect.
> 
> > Like silk road, postman only carry cargos within its section. Postman won't travel the whole network.
>
> This network composite of Cities, and stopover between cities.
>
> Postman follow pickup route(prompt) to delivery & receive cargos, until postman exhausted.
> > Pickup route(prompt) order MATTERS: Dallas → London → Paris → HongKong[10,945 miles] != Dallas → Paris → Hong Kong → London[16,910 miles]
>
> > When prefix pickup route is identical, cargos also identical.
>
> > All postman start from special token `<bos>`, and end at `<eos>`.
>
> Cargos are City's artifacts: impression, products, or history.
> > Ex: Texas ~ Big, Oil, Cowboys
> 
> New joinery's stopover needs past cargos.
> > Ex: Currently have "Cold" as past cargo, now postman more likely goes to London than Texas.


Artifacts:
- Model File ~ All Postman & Hierarchy
  - Model Block ~ Stopover Group
    - Attention Head ~ Railcar Group, parallel cargo loading
      - Q ~ Postman's current looking for cargos
      - K ~ Cargo's Key or index
      - V ~ Cargo's Value
  - Model Depth ~ Number of Stopover

- All Tokens ~ Whole Route
  - Prompt Tokens(Input) ~ Pickup Route
    - Token ~ Train Station Code
      - `<EOS>` ~ THE final city when postman exhausted
  - KV cache ~ Past Cargos

- Weights ~ Postman
- Data ~ Cargos & Postman

- GPU command buffer ~ Train Manifest
  - Input & output matrix ~ Postman & Cargo
  - GPU kernels ~ Trip Sheet, which directions
  - Pipeline state ~ Train state

Operations:
- Inference Framework ~ Orchestrate Overall Traffic
  - Inference Engine ~ Orchestrate Station(s) Traffic
    - Load Model ~ Postman clock in to work
    - Tokenizer ~ Translation between City Name and Train Station Code
    - Prefill
    - Decode
  - KV cache orchestration ~ cargos management

> Prefill ~ sent MANY postman to ship & receive cargos to many cities at once
> > --chunk-size ~ how MANY postman sent to Station at once
> 
> > at each block(stopover), past token also sent its KV(cargo) to future tokens(trigger casual effect). 

> Decode ~ sent one postman & past cargoes to DISCOVERY MISSION to find new CITY, until postman exhausted.
> > can't parallel, because we don't know next city

Hardwares:
- Node ~ Train Station
  - CPU ~ Train Station Manager
    - Manage between HBM and storage ~ transfer cargo between station and warehouse
  - GPU ~ Train Terminal, 8 terminals per Station
    - FLOPS ~ Train Engine's HP
    - support kernels ~ Different Train Terminals supports different train size, train width....
    - SRAM ~ Train's cargo capacity
    - HBM ~ Terminal's cargo capacity
  - IO ~ Traffic
  - Storage
    - DDR ~ station's parking lot `near station, but rain can destroy cargos`
    - SSD ~ warehouse near station
- Multi Nodes ~ Train Network
  - PD disaggregated ~ Transfer Hub Design
  - IB switch ~ rail between stations or directly between terminals across stations

> Solving city traffic is HARD, because different vehicle has different capacity, speed, latency.

> The key is more async processes to utilize most IOs, avoid redundant traffic.
> > Compute IO overlapping ~ Train head detach railcar, let railcar uploading on side, and attach another loaded railcar and take off.
>
> > Smart system will always have shuttle bus run between airport & warehouse. Not wait til cargo arrived.
> 
> Why not increase train capacity? Longer cargos loading time.
> > Onboard time often longer than train head pull railcar time.
>
> > Just like container changes shipping, block/page/batch transfer has huge effect on IO.

> Quantization & Dequante ~ remove cargo packaging, compress into smaller form
> > Quantization & Dequante should only happen inside kernel. Analogy break, but important note: don't decompress cargos in Station, only decompress small % cargos inside Train on demand.

IO:
- Transfer Modes
  - Local: Within Terminal
  - Node: Within Station
  - P2P: Directly to Terminal
  - Remote: to warehouse
- Transfer Hardwares
  - Spectrum ~ Fiber Hardware
  - IB ~ Access directly to Terminal without security check
  - NVLink
  - Infinity Fabric
  - CXL
- Memory Allocator

> two_tokens_casual_paths = (num_token_in_between + num_blocks) / num_blocks * (routes_per_block ^ num_blocks)

## Kernels

- DS4MetalTensor
  - MTLBuffer ~ memory pointer for GPU
  - offset
  - owner
  - live_snap & peak_snap

- MTLCommandQueue `command queue`
- MTLCommandBuffer `a batch GPU kernels`
- MTLBuffer `memory pointer for GPU kernel's inputs & results`
  - c: `graph->query_by_tier[graph->active_tier]` syntax similar struct
  - Lifetime: persists while MTLBuffer exists, outlast kernel.
  - Visibility: another kernel can read it later if you bind the same MTLBuffer.
  - Address space: it is device memory, global GPU memory, not per-thread local memory.
  - Synchronization: if one kernel writes it and another reads it, ordering matters. Separate encoders in the same command buffer are ordered; separate command buffers need dependency handling.
  - Performance: device memory is slower than thread-local registers or threadgroup memory


## Performance Optimizations

- Persistent Kernels
- Memory Coalescing
- command-buffer schedules `how often CPU dispatch kernels`
- superkernel - reduce kernel swap by multi ops
- microbatch - split training batch into smaller batches
- flashcomm
- compiler cache - kernel re-use
- MTP - Multi-Token Prediction
- Placement Driver (PD) dispatcher

- all-reduce operation - sync local gradient for global gradients.
- Activation Checkpoint - recompute activation every n layers when back props.

- Thread Block Clusters - multiple SMs works on same SRAM
- Stationary Data/Array - in-place execution data
- Very Long Instruction Word (VLIW) - Compiler optimization
- Threadgroup walk order - increase cache hit rate(because x,y index increase slowly)
- Attention–FFN Disaggregation (AFD) - LSU for FFN; GPU for attention;

### Parallelism Strategies

| Strategy | Description |
|----------|-------------|
| Data Parallelism (DP) | Replicate the whole model on each GPU; split data **batches**. |
| Pipeline Parallelism (PP) | Split the model across **layers**; each GPU processes a different stage. |
| Sequence Parallelism (SP) | Partition long input **sequences** across GPUs. (very limited) |
| Tensor Parallelism (TP) | Split **individual tensor(dim)** operations across devices (often less efficient). |

- Nvidia build optimize LLM image with tp1(single GPU), tp4(split attention head in 4 GPUs)