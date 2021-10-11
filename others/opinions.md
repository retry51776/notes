# There is no solution, only tradeoffs.

here are common trade offs
- CPU vs Memory
  > AKA space time trade offs
- Speed vs Accuracy
- Latency vs. Throughput
- consistency or availability
  > DB high avaibility problem
- features or scalebility
  > SQL vs no SQL
- complexity or flexibility

# Stuck?
> started from solution, extract key variables that calculated solution

> Question/Input properties?

> cache redone steps, common in tree, recursive

> Dynamic Programming or Recursive

> For most, longest, shortest question. Prefer solution that each computation step reduce possibility

**75 blind questions**
> Question types
- Array/Matrix
- Tree
  - Heap
    > Tree structure that will self reorder when add/poll node
  - Sufflix Trie
    > Tree structure that store string by letter, reduced space cost, useful for substring search
- Dynamic Programming


# Application Design
> Database is usually is the first bottleneck of application design
- Disk/Network IO
  > more fields or sister table

  > nested field or child table
- CPU
  > Store calculated field in DB, or aggs by DB
- DeadLock & Constrain
  > Enforce table constrain, or enforce in application level

  > Constrain will reduce DB performance, cause more deadlock
---
> Bussiness Logic & workflow
  - response time? request volumn?
  - where bussiness logic
    - compute @ engine, store in DB
    - compute @ DB proc
    - compute @ service endpoint
    - compute @ client side
  - Internal or External or both?
  - workflow interference & trigger DB bottneck

---
## Developer Metaphor
- Bussiness logic & data defines architecture.
- Useage determent house structure and foundation.

- Carpenter is determent by right tools and usage
- Common Developer problems:
  - didn't know the right tool/didn't familar with tool
    - reinvent the tool
    - wrong aproch the problem
  - bring too much tools
    - performance problem
    - over engineering
  - forgot to bring all the tools at once
    - tons DB query when they need it

## Security
- URL
  - expose static link on secure resource
  - open redirect
  - expose application structure
- ABAC
  > attribute based access control