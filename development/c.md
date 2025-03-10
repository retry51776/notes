# C

## File Types

- **`.c`**: Source code files
- **`.h`**: Header files (interface definitions)

## Shared Modules

### Platforms

| OS      | File Extension | Default Path           |
|---------|----------------|------------------------|
| Linux   | `.so`          | `/usr/local/lib`       |
| Windows | `.dll`         | (OS-dependent)         |

> Temporarily add current directory to library path (Linux)

export LD_LIBRARY_PATH="${pwd}"

# Debugging Tools

- `.text`: Executable code  
- `.data`: Initialized global variables  
- `.bss`: Uninitialized static storage  
- `.rodata`: Constants/readonly data  
- `.reloc`: Relocation entries (dynamic linking)  

## Core Concepts

| Term       | Description                                                                 |
|------------|-----------------------------------------------------------------------------|
| **GOT**    | Global Offset Table: Stores addresses for shared library symbols             |
| **PIC**    | Position Independent Code (-fPIC flag): Enables shared libraries to load anywhere in memory |
| **ELF**    | Executable and Linkable Format (Linux/Unix)                                |
| **PE**     | Portable Executable format (Windows)                                       |

## Build Tools

- **Makefiles**: Define build rules for compiling/linking modules  
  *(Example: `target: dependencies` pattern)*
