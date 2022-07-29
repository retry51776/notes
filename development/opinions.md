s# Software Analogy
> Old school windows software deployment is like `send you big coffee machine to you house. Manufactory can't clean it because they don't have access. User can't clean machine, or adjust coffee concentration because user can't open it(Closed source)`

> Then open source dev is like `we publish coffee machine parts(motor, pump, electric switches) design to public, user can make their own parts & wired them together. Now user knows how to take it apart & clean it. But now user needs to figure out what parts & how to wired parts together`

> Modern Hook libraries is like `we send you smart coffee machine(w touch screen) supports limited adjustment (callback parameters); Hope user able to find coffee machine that does everything you need.`
>> `const { /* here is where user pick up coffee */ } = useXXX(/* telling machine how to cook */)`
>> `useXXX()` is the machine
>> `onXXX` that passed into useXXX() is like custom request `similar to tell coffee machine before it cook, do x, y z; If machine doesn't support custom request, then you have to either try to see if you can modify add water after you got coffee, or pick another machine`

> Event base:
> 
 
# There is no solution, only tradeoffs.
here are common trade offs
- CPU vs Memory
  > AKA space time trade offs
- Speed vs Accuracy
- Latency vs. Throughput
- consistency or availability
  > DB high availability problem
- features or scalability
  > SQL vs no SQL
- complexity or flexibility


## Architecture
- Monolithic/layered
- Service Base/microservice
- distribute/event driven

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
  > Just business logic

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
> Business Logic & workflow
  - response time? request volumes?
  - where business logic
    - compute @ engine, store in DB
    - compute @ DB proc
    - compute @ service endpoint
    - compute @ client side
  - exposed to Internal or External or both?
  - cache everywhere
  - workflow interference & trigger DB bottleneck

> FE distributed in Content Deliver Network(CDN) is at good as it gets, maybe dynamics import too

> Horizontal scaling service & engine, most of works in here

> Global DB is very hard, beyond me

> Example Act as documentation & test
---
## Developer Metaphor
- Business logic & data defines architecture.
- Usage determent house structure and foundation.

- Carpenter is determent by right tools and usage
- Common Developer problems:
  - didn't know the right tool/didn't familiar with tool
    - reinvent the tool
    - wrong approach the problem
  - bring too much tools
    - performance problem
    - over engineering
  - forgot to bring all the tools at once
    - tons DB query when they need it

<hr />

> Compare Developer to car, sport car(senior dev) 0-60 is faster than corolla(jr dev), where it make differences is on max speed(dev don't aware their mistakes until review mirror). 
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

> VM have overhead from virtual hardware, virtual OS

# Application Language
# SQL
> It's NOT a standard when it suppose to be a standard.
> 
> If function is such bad for performance, why make it so powerful. It's like putting poisons in nice soda can.
# Python
> It's slow, but 90% bushiness use cases accepts horizontal scaling to mitigate problem.
> 
> Typescript like feature on Python will be cool.
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


<hr />

# other

## gRPC | webtransport
> grpc(Google) remote procedure call
make client request looks like function, replaces rest, webhook

> web socket cons: each new message type needs new socket; server can't create new connection;

## Tailwind 
> 2019 css framework, I like it, make sense

## Browser IDE
> very cool, just live on 10-21-2021
https://vscode.dev/
