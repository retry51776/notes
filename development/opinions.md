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

> For most, longest, shortest, max, min question. Prefer solution that each computation step reduce possibility

  - Ex: max question: only keep track of local max result, throw away past calculation

## Architecture
- Monolithic/layered
- Service Base/microservice
- distrubate/event driven

> IMO these just 3 basic architectures mixed together
- MicroKernel/Plug-in
  > Core system & plugins
- Service-Oriented
- Space-based

**Key Properties**
- (API or Service)? (Internal or External)? UI? 
  > API: External service without UI

  > Service: Internal service without UI

  > UI: repo has client side, can be internal or external

Backend
- Engine
  > any async service, crons, Pub/Sub
  - Manager
    > Creates msgs, keep track job status 
  - Worker
    > Consumer of msgs

- Calculator Class
  > Just bussiness logic

  > NO network connections
- Service Class 
  > handle network connections, data retrieve

  > application level cache
  
  > init Calculator Class instance
- Scripts
  > One off job, Ex: test  

**75 blind questions types**

- Array/Matrix
  - Quick Seach|Sort
  - Window Slicing
- Recursive
  - Divide and Conquer
    > Merge sort is easy to parrel

  - Dynamic Programming
    - Tree
      > Only single path from root to any node

      > Depth-first search
        - Preorder is priorty is left, node, right
        - Inorder is started from leftest leave, then root, at last right subtree
        - Postorder is started from leftest leave, then silbing, at last parent

      > Breadth-first search(level order) prioty is lower level scan first
      - Heap
        > Tree structure that will self reorder when add/poll node
      - Sufflix Trie
        > Tree structure that store string by letter, reduced space cost, useful for substring search

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

> FE distrubated in Content Deliver Network(CDN) is at good as it gets, maybe dynamics import too

> Horizontal scaling service & engine, most of works in here

> Golbal DB is very hard, beyond me


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

## Language
> The reason c++ is fast because good coder will reduce work `Ex: python get val from dict always generate hash, but in c++ if you already gen hash, just reused hash`
> But in the same time, developer have to manager more details
> Think of driving, the more direct control over car engine faster you can drive. But I love automatic transmission!

## ASCII vs UTF8 vs UTF16
> encoder is like html
>
> common encoder formats:
>> ASCII is old 7 bit character mapping
>> UTF8 is most common 8 bit mapping
>> UTF16 is larger room 16 bit mapping

> font is like css

### Docker VS VM
> docker just using linux kernel namespace partitions

> VM have overhead from virtal hardware, virtal OS


# Quiz
- The Minion Game