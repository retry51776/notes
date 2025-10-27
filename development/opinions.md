# Opinions
>
> Here are collections of my random opinions.

## Software Analogy
>
> Old‑school Windows software deployment is like “sending you a big coffee machine to your house. The manufacturer can't clean it because they don't have access. The user can't clean the machine or adjust the coffee concentration because the user can't open it (closed source).”

> Open‑source development is like “we publish the coffee‑machine parts (motor, pump, electric switches) design to the public; users can make their own parts and wire them together. Now the user knows how to take it apart and clean it. But the user now needs to figure out which parts to use and how to wire them together.”

> Modern hook libraries are like “we send you a smart coffee machine (with a touch screen) that supports limited adjustments (callback parameters). The hope is that the user can find a coffee machine that does everything they need.”
>> `const { /* here is where the user picks up coffee */ } = useXXX(/* telling the machine how to brew */)`
>> `useXXX()` is the machine.
>> `onXXX` passed into `useXXX()` is like a custom request—similar to telling the coffee machine before it brews, “do X, Y, Z.” If the machine doesn't support a custom request, then you either try to see if you can add water after you get coffee, or pick another machine.

> Function is stateless, vs Class is stateful.

> Event‑based:

> Computation is moving data, just with an inseparable move.

## Philosophy

> Talk is cheap; show me your code.

> Make it work, make it right, make it fast.

> There is no solution, only trade‑offs

Here are common trade‑offs:

- CPU vs Memory  
  > AKA space–time trade‑off
- Speed vs Accuracy
- Latency vs Throughput
- Consistency or availability  
  > Database high‑availability problems
- Features or scalability  
  > SQL vs NoSQL
- Complexity or flexibility

## Prediction

1. In the future (within 10 years), developers will write/describe MVP code and give it to an AI compiler for optimization. The AI compiler may ask the developer for assumptions or clarifications, then compile production‑ready code much faster.
2. Everything will be event‑based; **except** databases.
3. Databases will support all types—time series, NoSQL, SQL, graph, etc.—perhaps as cloud services with accelerated hardware.

## Architecture

- Monolithic / layered
- Service‑based / microservice
- Distributed / event‑driven  

> IMO these are the three basic architectures, often mixed together.

- Microkernel / plug‑in  
  > Core system & plugins
- Service‑oriented
- Space‑based

**Key Properties**

- (API or Service)? (Internal or External)? UI?  
  > API: external service without UI  
  > Service: internal service without UI  
  > UI: repository has client side, can be internal or external

## Backend Pattern

- `/Engine`  
  > Any async service, cron jobs, Pub/Sub
  - `Manager` – creates messages, tracks job status
  - `Worker` – consumes messages
- `/Calculator`  
  > Business logic only  
  > **No** network connections
- `/Service`  
  > Handles network connections and data retrieval  
  > Application‑level cache  
  > Instantiates a `Calculator` class
- `/Script`  
  > One‑off jobs, e.g., tests

## Application Design
>
> The database is usually the first bottleneck in application design.

- Disk / Network I/O  
  > More fields or larger tables; nested fields or child tables
- CPU  
  > Store calculated fields in the DB, or aggregate in the DB
- Deadlock & constraints  
  > Enforce constraints in the DB or at the application level. Constraints can reduce DB performance and cause more deadlocks.

---

> Business logic & workflow

- Response time? Request volume?
- Where does business logic run?  
  - Compute in engine, store in DB  
  - Compute in DB stored procedure  
  - Compute in service endpoint  
  - Compute on client side
- Exposed to internal or external users—or both?
- Cache everywhere
- Workflow interference & DB bottlenecks

> Front‑end distribution via CDN is as good as it gets; dynamic imports may also be used.

> Horizontal scaling of services and engines handles most workloads.

> Global databases are very hard—beyond my current scope.

> Example: act as documentation & test.

> Understand common actions, their rough cost (time, space).

---

## Difficult Things to Document

- Reality mapping
- Technical decisions
- Requirement changes

---

## Developer Metaphor

- Business logic & data define architecture.
- Usage determines house structure and foundation.

- The carpenter is determined by the right tools and usage.

Common developer problems:

- Not knowing the right tool / unfamiliar with a tool  
  - Reinvent the tool  
  - Take the wrong approach
- Bringing too many tools  
  - Performance problems  
  - Over‑engineering
- Forgetting to bring all needed tools at once  
  - Resulting in excessive DB queries when they are needed

---

> Compare a developer to a car: a sports car (senior dev) accelerates 0–60 faster than a Corolla (junior dev); the difference lies in top speed. Developers often don’t notice their mistakes until they look in the rear‑view mirror.

## Security

- URL  
  - Expose static links on secure resources  
  - Open redirects  
  - Reveal application structure
- ABAC  
  > Attribute‑Based Access Control

## Encoding
>
> An encoder is like HTML.

Common encoding formats:

- ASCII – old 7‑bit character mapping; invented in the US
- Unicode – universal character encoding standard; each region has its prefix  
  - UTF‑8 – most common 8‑bit mapping  
  - UTF‑16 – larger 16‑bit space
- MessagePack – backward‑compatible with UTF
- Avro – Apache custom schema; each communication sends schemas
- Protobuf – Google’s custom schema; sends the schema once

> A font is like CSS.

### Docker vs VM
>
> Docker uses Linux kernel namespaces for partitioning.  
> VMs have overhead from virtual hardware and a virtual OS.

## Python
>
> It’s slow, but 90 % of business use cases accept horizontal scaling to mitigate the problem.  
> Adding TypeScript‑like features to Python would be cool.  
> I love `snake_case` variable naming; every language should use it.

## JS
>
> Very large ecosystem—now that’s a problem.  
> Too many frameworks; even JS engines and runtimes exceed what I want to learn.  
> At the end of the day, it’s a single‑threaded process, similar performance issues as Python.  
> I wish all browsers supported TypeScript and Sass by default. I can dream.  
> I don’t like UpperCamelCase or lowerCamelCase.

## C++
>
> C++ is fast because good programmers reduce work (e.g., Python gets a hash for every dict lookup, but in C++ you can reuse a pre‑computed hash).  
> At the same time, developers must manage more details. Think of driving: the more direct control over the car engine, the faster you can drive. But I love automatic transmission!

## .NET
>
> One major thing I don’t like about .NET is that it isn’t very clear what calls what, where code/DI comes from. I have to read micro‑docs, but there are just too many versions with no clear differences.

## Perl
>
> Who can read this crap?

## YAML
>
> YAML’s indentation is already messy and unreadable; now Helm workflow adds another layer of mess? Why? It’s ugly! Easy to make mistakes. I want my good old JSON format back.  
> I get it—parsers are easier when you can trust indentation. I hope someone builds a better parser and a different format.

---

## gRPC | WebTransport
>
> gRPC (Google) remote procedure call makes client requests look like functions, replacing REST/webhooks.  

> WebSocket cons: each new message type needs a new socket; the server can’t create a new connection.

## Tailwind
>
> 2019 CSS framework—I like it; it makes sense.

## Browser IDE
>
> Very cool; just live on 2021‑10‑21  
> <https://vscode.dev/>
