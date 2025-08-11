# I Hate LeetCode

## Quiz Topics
- The Minion Game  
- DateTime label  

**75 blind question types**

### Categories

#### Array / Matrix
- Quick Search | Sort
- Sliding Window

#### Recursive
- Divide and Conquer  
  > Merge sort is easy to parallelize.

#### Dynamic Programming
- **Tree**
  - Only a single path exists from the root to any node.
  - Depth‑first search (DFS)
    - Preorder: left → node → right  
    - Inorder: leftmost leaf → root → right subtree  
    - Postorder: leftmost leaf → siblings → parent
  - Breadth‑first search (BFS, level order): scans lower levels first.

- **Heap**
  > A tree structure that reorders itself when nodes are added or removed.

- **Suffix Trie**
  > Stores strings character by character; reduces space and is useful for substring searches.

## Getting Unstuck
> Start from the solution and extract the key variables used to compute it.

- Identify question/input properties.  
- Cache repeated steps (common in tree/recursive problems).  
- Decide between DP or plain recursion.  

### Typical Patterns

#### Pointer / Sliding‑Window Questions
1. Initialise result.  
2. Create extra pointers that do **not** interfere with each other.  
3. Divide the task into:
   - Setup phase  
   - Process phase  
   - Reset phase  
4. Mark variable scopes: per‑cycle vs. global.

```python
for x in zip(*['abc', 'def', 'ghi']):
    # x == ('a', 'd', 'g')
    pass
```

#### Divide & Conquer Questions
> Often preferred in production because runtime is predictable and the approach can be parallelised.

Always consists of at least two parts:
1. **Division** – create pointers, define a recursive function.  
2. **Merge** – combine results where the main logic resides.

