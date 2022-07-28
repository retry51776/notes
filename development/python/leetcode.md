# I hate leetcode
# Quiz
- The Minion Game
- DateTime label

**75 blind questions types**

- Array/Matrix
  - Quick Search|Sort
  - Window Slicing
- Recursive
  - Divide and Conquer
    > Merge sort is easy to parallel

  - Dynamic Programming
    - Tree
      > Only single path from root to any node

      > Depth-first search
        - Preorder is priority is left, node, right
        - Inorder is started from leftest leave, then root, at last right subtree
        - Postorder is started from leftest leave, then sibling, at last parent

      > Breadth-first search(level order) priory is lower level scan first
      - Heap
        > Tree structure that will self reorder when add/poll node
      - Sufflix Trie
        > Tree structure that store string by letter, reduced space cost, useful for substring search

# Stuck?
> started from solution, extract key variables that calculated solution

> Question/Input properties?

> cache redone steps, common in tree, recursive

> Dynamic Programming or Recursive

> For most, longest, shortest, max, min question. Prefer solution that each computation step reduce possibility

  - Ex: max question: only keep track of local max result, throw away past calculation


### For Pointer, sliding windows Questions:

- init result,
- always create extra operation pointer `avoid pointer interfior with  each other`
- divide task into setup up phase, process phase, reset phase,
- mark variables types: reset each cycle, cycles/global state


```py
for x in zip(*['abc', 'def', 'ghi'])
    //x = ['a', 'd', 'g']
```

### For Divide & Conquer Questions:
> Often a prefer solution in Production because predictable runtime & able parallel process

Always at least 2 parts:
1. division `create pointers, recursive function`
2. merge `where logic happens`

