# Computer Analogy
>
> Think of process data like making a cake from scratch:
>
> - **CPU**: Master chef that can make any cake, but commands a high salary.  
> - **GPU**: Multiple chefs that can bake many cakes in parallel, cheaper per chef.  
> - **FPGA**: Specialized machine that makes a few types of cakes very efficiently.  
> - **ASIC**: Dedicated machine that only makes one type of cake, but does it extremely fast.

- **RAM** is the kitchen table.  
- **Disk** is the supermarket.

The goal is to avoid waiting for supermarket deliveries, minimize walking around, and arrange the kitchen to optimize workflow.

## Chip Architecture
>
> Nowadays everything is moving toward System‑on‑Chip (SoC) designs. The four main architectures are CPU, GPU, FPGA, and ASIC.

### CPU

**CISC**

- **x86**
  - Accesses memory before execution; variable‑length instructions make out‑of‑order execution harder.
  - Fewer registers, larger & more complex instructions, multi‑cycle operations.

**RISC**

- **MIPS**, **ARM**, **RISC‑V**
  - Fixed instruction length enables easy preloading and out‑of‑order execution.
  - Simpler instructions, more registers, single‑cycle operations.

### GPU
>
> Simple, small cores but many of them.

Graphics pipeline:

1. Vertex & Index Buffer → Vertex Shader → Rasterizer → Pixel Shader → Alpha Blend

**Render Driver Stack**

- **OpenGL Shading Language (GLSL)** – C‑style, cross‑platform.  
- **DirectX** – C++, Windows only.  
- **Metal (MSL)** – C++, Apple’s counterpart.

**Geometric Primitives:** point, line, triangle, cube, cone, cylinder…

**Game Engines**

- Unity → compiles to OpenGL or DirectX  
- Unreal Engine 5 → supports high‑poly scenes, realistic lighting, etc.  
- GameMaker – beginner‑friendly 2D engine

#### Terms

- **Level of Detail (LOD)** – lower detail uses billboards.  
- **Dynamic Level of Detail (DLD)** – adjusts polygon count based on distance.  
- **Foliage**, **Nanite Foliage**  

### FPGA
>
> Originally designed for debugging and testing in FABs. Before computation, a compiled design is loaded onto the device.

Hardware Description Languages:

- RTL, VHDL, Verilog, SystemVerilog

### ASIC
>
> Hard‑coded circuitry for a single (or few) applications; extremely fast but inflexible.

## Buzzwords

- **EDA** – hardware design software.  
- **Standard Cell Library** – pre‑designed logic gates (AND, OR, ADD).  
- **Track Height**, **Design for Manufacturability**, **Multi‑patterning**, **Half‑pitch**, **Resolution Enhancement Techniques**.  
- **Power / Performance / Area / Cost (PPAC)** metrics.  
- **Transceiver** – high‑speed fiber networking.  

# Fabrication (FAB)

> The industry is highly siloed. One day AI might understand the whole stack. Most power is spent moving data, not computing.

## Frontend

- Design
  - IP blocks(Ex: GPU, CPU)
    - Sub blocks(Ex: arithmetic logic unit, control unit)
      - CMOS standard cell library(density or performance tradeoff)
        - Logic gates
        - Sequential elements
        - Special Function cells
        - Power management cells
        - Physical only cell
        - IO & interface cells
        - multi-drive variants
- Produce  

## Backend

- Cut  
- SIP (封装)  
  - CoWoS (Chip-on-Wafer-on-Substrate)
    - CoWoS-S (S=Silicon)
    - CoWoS-SR (R=Reticle Stitching)
    - CoWoS-L (Local) `similar to plastic/PCB`
    - CoWoS-R (Redistribution)
    - CoWoS-A (Active interposer)
  - CPO (Co-Packaged Optics)
    - Light transfer data directly to chip
- Chiplet  
- Interposer  
- 3D NAND  
  - 2014: 24 layers  
  - 2016: 48 layers  
  - 2020: ~100+ layers

# Other Topics

**Battery**

- **Anode** – graphite, lithium (negative)  
- **Cathode** – cobalt, nickel, manganese (positive)
