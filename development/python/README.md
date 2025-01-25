# Python

> battery included because python comes with std lib

## Python Managers

|  | Manages Python | Manages Packages | Start Command                      | Change |
|----------------|----------------|-----------------|------------------------------------|-----------------|
| Anaconda      | ✅ Yes          | ✅ Yes          | `conda activate <environment_name>` | Python Path |
| Conda         | ✅ Yes          | ✅ Yes          | `conda activate <environment_name>` | Python Path |
| Pipenv        | ✅ Yes          | ✅ Yes          | `pipenv shell`                      | |
| Pyenv         | ✅ Yes          | ✅ Yes          | `pyenv activate <environment_name>` | Python Path |
| Virtualenv    | ✅ Yes          | ❌ No           | `source <environment_name>/bin/activate` | |
| Venv          | ✅ Yes          | ❌ No           | `source <environment_name>/bin/activate` | Python Path |
| Poetry        | ❌ No           | ✅ Yes          | `poetry shell`                      | |
| Pip           | ❌ No           | ✅ Yes          | N/A (Pip doesn't manage environments) | |



## Python Scope

> Package has 2 types: 
> need either `setup.py` or `pyproject.toml`
> 
> > Executable package: has __main__.py in root as entrypoint, `python -m folder_name`
> 
> > Library package: (often with __init__.py in root)

- Package Manager
  - Package
    - Module `xx.py`
      - Global Scope
        - Built-in
        - Custom `imports xxx` & `def xxx()` & `class XX`
          - Enclosing Scope `lambda x: y`


## Change Logs

- 3.0
  - 3 / 2 = 1.5
  - str & unicode
- 3.5
  - `async def xxx():` `ftr = xxx()`  `result = asyncio.run(ftr)`  `results= await asyncio.gather(*futures)`
- 3.6
  - f'{ddd}_123'
  - async
- 3.8
  - := `walrus operator`
- 3.9
  - a lot new modules
- 3.10
  - pattern matching
  - Type Operator `isinstance(1, int | str)`
- 3.11 beta
  - expression error trackstack, add_note(), ExceptionGroup
  - self type
  - Performance increase 15%
  - tomlib

**Frustration**

- ~~destructure like es6 `const {a, b, ...others} = obj;`~~
    > new python 3.10 supports this <https://docs.python.org/release/3.10.0/whatsnew/3.10.html>
- get_in like methods or null chaining
- decorator acts as interceptor, takes func as args, return func
- function params's default value should be standard type
    > don't reference type `[]` or `{}`, any modify reference will presists default value in next function call
- don't delete in loop
- falsely values & or, need similar `or` for `None` only, I hate `if else`
- Python allow integer as key of object, but JSON file requires key as string. Can be surprised load object is different.
- `[1,2].index(0)` will throw an error, must check before get index`if 0 in [1,2]:`
- recursion limit: 10,000
- Pipfile going replace requirement.txt `pipenv install`
- Python round() sucks
- `__init__` doesn't support different params
- `setattr()` won't have IDE auto suggestion

**Working on library**

```py
Install local package steps:
    1. copy source code into docker container's root folder
    2. docker exec -it [container_name] sh
    3. delete [source_code_folder]/build
    4. cd [source_code_folder]
    5. python3 setup.py install
```

`python3 -m build`
> Build library

`python3 setup.py sdist`
> Publish package

> requirement.txt is for dev env, setup.py is for client env

`python -m site`
> List python library location

`help('modules')` print docstring
module docstring in `__init__.py` or `beginning of *.py`
function docstring in first line of function

# To debug Ram & time
>
> `time -f python3 test.py`

> `from time import timeit #@timeit`

> No such file or directory execute 'python' `#!/usr/bin/env python`

## type checks

- myPy
- pytype: google
- pyre: facebook
- pyright: microsoft

`def test(a: str) -> str | None:`

## Standard Type

```py
import sys
sys.maxint
float('Inf') # max value
endswith()
startswith()
upper()
lower()
.title()
.strip()#lstrip or rstrip
[::-1]#reverse
[1,2,2,3,3,3].count(2)
dictionary.setdefault(keyname, value)
type('xyz', (object), {
    '__init__': lambda: None,
    'some_method': 'return value',
})

a, b, c = 1, 2, 3
a, b, *_, d = list(range(10))
print(a, b,  d)
a = b = c = 4
f'Rounded to {2222222.222:,.2f}'
f'Format to {date.today():%Y-%m-%d}'
```

## Attriabutes

```py
dir(class_object) # show all attriabutes
getattr(Abc, 'xyz') # only work w class
hasattr()
setattr()
delattr()
vars(class) # retrun Object
```

## Property

```py
{}.get('xyz') # only works w obj

# python desturcture
from operator import itemgetter
a, b = itemgetter('a', 'b')(params)

# idiom, like destruct object in javascritp
>>> foo(*[1,2,3])
x=1
y=2
z=3

>>> mydict = {'x':1,'y':2,'z':3}
>>> foo(**mydict)
x=1
y=2
z=3
```

## Build in functions

```py
all()
any([0, 1, 0])

sys.getsizeof(obj) # debug variable Ram

timeit.timeit(xyz)
time -f python3 test.py # debug script Ram & time
#cProfile, pstats takes more setup, but better audit whole project
```

## dunder|magic methods, decorator

```py
def cust_decorator(func):
    def wrapper(*args, **kargs):
        func(*args, **kargs)
    return wrapper

@staticmethod # I don't like it, prefer stand along func
@classmethod(cls) # support inhertance, usually to load_xx & return instance
@porperty
@xyz.setter

class events
__new__(self, cls_name, bases, attrs) 
__init__(self):
__enter__ # Only for contextMgr
__exit__ # Only for contextMgr
__del__

# python descriptor
__get__
__set__
__hash__
__dict__
__slots__ # lock class attribute, to save RAM
__dict__ # access attribute as object
__repr__

# Only usecase with metaclass to intercept 3rd party modules
Python Metaclasses(type constructor)
class TestA(metaclass=TestB)
`class Test:` is same as `Test = type('Test', (), {
    'xx_method': lambda x: x
})`
__class__
# self implement class operators
from functools import totoal_ordering
@total_ordering
xyz.__class__ is self.__class__
__eq__
__ne__
__ge__
__lt__
__le__
```

## loop

```py
# Sort by 1 key
array = sorted(
    [item for item in items if item['a'] > 0],
    key=lambda x: x['b'], reverse=True
)
# Sort by multi keys
import operator
array = sorted(array, key = operator.itemgetter('x', 'y'))

# Sort by custom func
from functools import cmp_to_key
def custom_func(x, y):
    return 0
array = sorted(array, key=cmp_to_key(custom_func))

for idx, value in enumerate(arrays):

passed_tests = filter(lambda x: x['passed'], tests)

# convertion
map(len, ['abc', 'de', 'fghi'])

# combine
list(zip([1, 2, 3], ['a', 'b', 'c']))
zip # inner join
zip_longest() # outter join

# search
next(x for x in itms if type(x).__name__ == 'Abc')

# create iterator of object
# must create new iterator for every loop
i = iter([1, 2, 3])

# Kind bad idea, should pass array if you can
# any child looped will used parent itertor, but sibling pointer still works
i1, i2, i3 = itertools.tee(i, 3)
```

## custom utilities

```py
# round(2.50) == 2, wtf
# Python round have funny behavior
from decimal import Decimal, getcontext, Context
getcontext().prec = 2
getcontext().traps[decimal.DivisionByZero] = False
# Or decimal.setcontext(Context(prec=2, rounding=ROUND_HALF_UP))
print(Decimal(0.1) + Decimal(0.2))
def basic_round(x, d=0, as_decimal=False):
    if x is None:
        return None
    round_digit = Decimal(10) ** -d
    rounded = Decimal(str(x)).quantize(round_digit, rounding=ROUND_HALF_UP)
    return rounded if as_decimal else float(rounded)

def get_in(obj, keys=None, default=None):
    try:
        if obj is None or keys is None:
            return default
        first_key = keys[0]

        if isinstance(first_key, int) and isinstance(obj, list):
            if len(obj) <= first_key:
                return default
            elif len(keys) == 1:
                return obj[first_key]
            else:
                return get_in(obj[first_key], keys[1:], default)

        # Try convert key to str to find in object
        if first_key not in obj:
            first_key = str(first_key)
        has_first_key = first_key in obj

        if has_first_key:
            if len(keys) == 1:
                return obj[first_key] if obj[first_key] is not None else default
            else:
                return get_in(obj[first_key], keys[1:], default)
        else:
            return default
    except Exception:
        return default
```

# Buzzwords Zoo

Python Enhancement Proposals(PEP)

- .wheel is python binary file(2012), .egg is old binary format(2004)
- odbcinst.ini `registry and configuration file for ODBC drivers in an environment`
- Since Py3, object’s type = its class `type(obj) is obj.__class__`
- Exception chaining `raise ValueError("Bad grape") from exc`
