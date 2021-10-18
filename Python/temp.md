# PyBay 2021

Chater - share ownership

### First speaker
Andrew Knight - Pandy
Test data is as important as test itself

> Testing code vs Testing features

## Consider
- Size?
- Freshness?
- difficulty
- bureaucracy
- skill level
- cost?
## Terms
- test conrol input
- literal values
- output references

## collision

> multiple user uses same resource

- solution
    > restrict test access

    > deploy new container

    > make DB clone

    > serial instead parall
---
Ray Tune
> distribute computing framework


```
@ray.remote
def test():
    return -1

task = test()
assert ray.get(task) == -1

```

# IDOM
## Similar UI library for Jupeter Notebook
- IPyWidget
- boken
- panel
- streamlit

| Imperative | Declarative |
| -- | --- |
| state & UI transitions | only state |

myPy type checking
```
import idom

@idom.component
def Demo():
    count, set_count = idom.hooks.use_state(0)
    return idom.html.button({'onClick': lamba: x : set_count(count)}, 'test')
```
- Rust
> browser checker

# bit.io
build DB with python

# lightning talk

> uses slack webhook call flask app

python descriptor

python data orchestration
- scheduling
- alert
- history


```
__get__
__set__
```
m$$

---
My name is Terry, I'm Fullstack Web Dev at a medical company. You can think of us as turbo tax for nursing home. I works with their analysis product.  from react/redux to express server, flask micro server, design sql/no sql DB, design bussiness workflow, to GCP deployment. Obsively it's NOT a highly well structure like most small company. I love evnet driven architure, because it's fault tolerance, easier to scale, decoupleing, break up code base.

I'm focus on workflow, backend python engine, db design,µ

a bit understand sql plannern & execute engine,
but most bussinees logic is simple iteror scan

```
def maxProfit(self, prices: List[int]) -> int:
    cost, profit = float('inf'), 0
    for price in prices:
        if price < cost:
            cost = price
        if price - cost > profit:
            profit = price - cost
    return profit
```


# Google
Brandon Warner <brandonwarner@google.com>
Google Recruiting Operations

Allison Achenbaugh

Joyer

# health short

health coverage

ACA enroll <65

80 ppl n cal scaq, 

16 ppl
    ruby ralie, python,
    sevice, 
    postgres
    85% coverage
CRM