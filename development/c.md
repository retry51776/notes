# C
> `xxx.c` is source code, `xxx.h` is interface def
> compiled shared module in windows is `xxx.dll`; in linux is `xxx.so`

> linux default share module path `/usr/local/lib`, env is `export LD_LIBRARY_PATH="${pwd}"`

> `makefile` define modules linkage
### sections
- header
- .text
- .data
- ...
- .reloc


## CMDs
```bash
# Compile shared module from math.c into libmath.so
gcc -shared -fPIC math.c -o libmath.so

# Compile
gcc main.o math.o -o main

# Compile executable & reference shared module
gcc main.c -lmath -L. -o main

# Check executable meta info
readelf -h main.o

# check executable sections
readelf -S

# Check compiled ddl dependence
readelf -d xxx_script | grep NEEDED
```

## Buzzwords
- Global Offset Table (GOT) `Memory table store shared module`
- Position Independent Code (PIC) `-fPIC flags shared module uses GOT`
- Executable and Linkable Format (ELF) `Linux`
- Portable Executable (PE) `Windows`