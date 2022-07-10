# I hate leetcode

### For Pointer, sliding windows Questions:

- init result,
- always create extra operation pointer `avoid pointer interfior with  each other`
- divide task into setup up phase, process phase, reset phase,
- mark variables types: reset each cycle, cycles/golbal state


```
for x in zip(*['abc', 'def', 'ghi'])
    //x = ['a', 'd', 'g']
```

### For Divide & Conquer Questions:
> Often a prefer solution in Production because predictable runtime & able parallized process

Always at least 2 parts:
1. dividsion // create pointers, recursive function
2. merge // where logic happens

