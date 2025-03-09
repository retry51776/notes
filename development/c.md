# C Language Essentials

## File Types

- **`.c`**: Source code files  
- **`.h`**: Header files (interface definitions)  

## Shared Modules

### Platforms

| OS      | File Extension | Default Path           |
|---------|----------------|------------------------|
| Linux   | `.so`          | `/usr/local/lib`       |
| Windows | `.dll`         | (OS-dependent)         |

### Environment Setup

```bash
# Temporarily add current directory to library path (Linux)
export LD_LIBRARY_PATH="${pwd}"
```

## Compilation

### Key Commands

```bash
# Create shared library from math.c (Linux)
gcc -shared -fPIC math.c -o libmath.so

# Link static libraries
gcc main.o math.o -o main

# Link shared library dynamically
gcc main.c -L. -lmath -o main  # Searches current dir for libmath.so

# Debugging Tools
readelf -h main.o    # Display ELF header info  
readelf -S main      # List sections of executable  
readelf -d xxx_script | grep NEEDED  # Show dependencies
```

## Memory Layout (ELF Format)

### Key Sections

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
