# Computer Analogy
> Think of Process Data is like making a cake from scratch; 
> > CPU master cooks that can make any cake, but expensive salary; 
> 
> > GPU are cooks can do a lot cakes, cheaper salary;
> 
> > FPGA is smart machine makes couple types of cakes;
> 
> > ASIC is machine that only makes one type cake, but very fast; 
> 
> RAM is kitchen table; 
> 
> Disk is supermarket; 
> 
> The idea is avoid cook waiting of supermarket deliver, avoid walking around, and kitchen arrangement to optimize cook workflow.

# Chip Architecture
> These day everything is going to be System on Chip (SOC) design; 4 main chip architectures [CPU, GPU, FPGA, ASIC]
## CPU
  - CISC
    - x86
    > Access memory prior instruction, & different instruction size, makes out of order execution hard, 

    > Variable length instructions

    > Can perform arithmetic & access memory in a instruction

    > fewer resisters

    > larger & complexer instructions

    > multi cycle instruction
  - RISC
    - MIPS
    - Arm
    - RISC5
      > Fixed Instruction Length allows preload & preprocessed easy, out of order execution 

      > simple instruction & same instruction size makes decoder easy to scale

      > memory & arithmetic instructions are separate

      > more registers

      > less instruction

      > single cycle instruction
## GPU
> simple small, but many cores

> Hardware -> Driver -> Developer Framework -> Application

> Render Driver
>> - OpenGL Shading Language (GLSL) `C-style language; open platform; easier`
>> - DirectX `C++; start as direct3D; only in windows;`
>> - Metal `C++; apple's directX; only in mac system`
>>> Geometric Primitive: smallest build unit [point, line, triangle, Cube, Cone, Cylinder ...]

>> Game Engine `Render framework enable user works w physical engine, shapes, light, texture; higher level unit than driver`
>>> - Unity `can compile into OpenGL or DirectX`
>>> - unreal `unreal engine 5 support crazy real 3D render. such as unlimited polygons, glass effect(reflection & see through)`

>> Computer-aided design (CAD) 
>> OpenCV `Library for Computer Vision, take vision as input, not output! Support C++; Python; Java; Written C++;`
>>> Facial Recognition
>>> Object Detection
>>> Activity Recognition

>> Compute Unified Device Architecture (CUDA) `2006 Nvidia C extension only works on Nvidia GPU`

## Field programmable Gate Array (FPGA)
> FPGA original design to debug & test in FAB; Each time before compute, it needs to load compiled design, then execute; It's great for process stream data;
- Hardware description language
  - RTL (Register Transfer Language)
  - VHDL
  - Verilog
  - System Verilog
## Application Specific Integrated Circuit (ASIC)
> Kind like hardcode programming, but in hardware; Because everything is hardcoded, there is only 1 or few application;

## Buzzwords
- EDA `is hardware design software`
- Standard Cell Library `Group of transistor gates, Ex: And, Or, Add operation`
- Track Height `Standard Cell Library KPI`
- Design for Manufacturability -> Design Technology Co-Optimization
- multi-patterning `multi mask on single layer`
- half-pitch `length of gate`
- Resolution Enhancement Techniques `Similar to special font to improve readability of bad print`
- Power, Performance, Area, Cost `chip KPI`
- Transceiver `is network modern for fiber`
- Translation Lookaside Buffer (TLB) `is a memory cache that stores recent translations of virtual memory to physical addresses for faster retrieval`

# Fabrication (FAB)
## Frontend
  - design
  - produce
## Backend
  - cut
  - Sip(封装)
  - chiplet
  - interposer
  - 3D Nand
    - 2014 24 layers
    - 2016 48 layers
    - 2020 1XX layers

# Others
Battery
- Anode : negative terminal
  - graphite, lithium
- Cathode : positive terminal
  - cobalt, nickel and manganese