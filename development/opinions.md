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

## Backend Pattern
- /Engine
  > any async service, crons, Pub/Sub
  - Manager
    > Creates msgs, keep track job status 
  - Worker
    > Consumer of msgs

- /Calculator
  > Just bussiness logic

  > NO network connections
- /Service 
  > handle network connections, data retrieve

  > application level cache
  
  > init Calculator Class instance
- /Script
  > One off job, Ex: test  


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

<hr />

> Compare Developer to car, sport car(senior dev) 0-60 is faster than corolla(jr dev), where it make differences is on max speed(dev don't awared their mistakes until review mirror). 
## Security
- URL
  - expose static link on secure resource
  - open redirect
  - expose application structure
- ABAC
  > attribute based access control

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

# Application Language
# SQL
> It's NOT a standard when it suppose to be a standard.
> 
> If function is such bad for performance, why make it so powerful. It's like puting posion in nice soda can.
# Python
> It's slow, but 90% bussiness use cases accpets horizontal scaling to mitigate problem.
> 
> Typescipt like feature on Python will be cool.
> 
> I love snake_case variable naming. Every language should use it.

# JS
> Very big ecosystem, now it's problem.
> 
> Too many framework, even JS engines & JS runtime have more than I want to learn.
> 
> At the end of day, it's single thread process. Similar max performance issue like Python.
> 
> I want all browser support typescript, sass by default. I can dream.
> 
> I don't like UpperCamelCase or LowerCamelCase

# C++
> The reason c++ is fast because good coder will reduce work `Ex: python get val from dict always generate hash, but in c++ if you already gen hash, just reused hash`
> But in the same time, developer have to manager more details
> Think of driving, the more direct control over car engine faster you can drive. But I love automatic transmission!

## .Net
> One major thing I don't like about .net: isn't very clear what calls what, where code/DI from. I have to read micro docs, but there just too many versions w no clear differences.

## YAML
> YAML itself indentation already messy and unreadable, now Helm workflow control on TOP of this mess? Why? It's ugly! Easy to make mistakes. I want my good old json format back :(
> I get it, it's easy make parser if we can trust indent. I hope someone build better parser & different format.