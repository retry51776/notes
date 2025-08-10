# Python

> Battery included because Python comes with the standard library.

## Python Managers

| Manager   | Manages Python | Manages Packages | Start Command                              | Change        |
|-----------|----------------|------------------|--------------------------------------------|---------------|
| Anaconda  | ✅ Yes         | ✅ Yes           | `conda activate <environment_name>`        | Python Path   |
| Conda     | ✅ Yes         | ✅ Yes           | `conda activate <environment_name>`        | Python Path   |
| Pipenv    | ✅ Yes         | ✅ Yes           | `pipenv shell`                             | —             |
| Pyenv     | ✅ Yes         | ✅ Yes           | `pyenv activate <environment_name>`        | Python Path   |
| Virtualenv| ✅ Yes         | ❌ No            | `source <environment_name>/bin/activate`  | —             |
| Venv      | ✅ Yes         | ❌ No            | `source <environment_name>/bin/activate`  | Python Path   |
| Poetry    | ❌ No          | ✅ Yes           | `poetry shell`                             | —             |
| Pip       | ❌ No          | ✅ Yes           | N/A (pip doesn't manage environments)      | —             |
| uv        | ❌ No          | ✅ Yes           | N/A (package manager written in Rust)     | —             |

## Package Scope

> Packages have two types:
> - Need either `setup.py` **or** `pyproject.toml`.

> Executable package: has a `__main__.py` at the root as an entry point, runnable with `python -m <folder_name>`.

> Library package: usually contains an `__init__.py`.

- Package Manager
  - Package
    - Module `xx.py`
      - Global Scope
        - Built‑in
        - Custom `import xxx` & `def xxx()` & `class XX`
          - Enclosing Scope (`lambda x: y`)

## Change Logs

- **3.0**
  - `3 / 2 = 1.5`
  - `str` & `unicode`
- **3.5**
  - ``async def xxx():`` → ``ftr = xxx()`` → ``result = asyncio.run(ftr)`` → ``results = await asyncio.gather(*futures)``
- **3.6**
  - f‑strings: ``f'{ddd}_123'``
  - ``async``
- **3.8**
  - Walrus operator ``:=``
- **3.9**
  - Many new modules
- **3.10**
  - Pattern matching
  - Type union operator ``isinstance(1, int | str)``
- **3.11 (beta)**
  - Improved tracebacks, ``add_note()``, ``ExceptionGroup``
  - Self types
  - ~15 % performance increase
  - ``tomllib``
- **3.12**
  - Debug‑friendly f‑strings: ``f'His name is {name=}'``
  - Typing enhancements

## Frustrations

- ~~Destructure like ES6 ``const {a, b, ...others} = obj;``~~  
  > Python 3.10 supports similar functionality with the ``match`` statement.
- Missing “null‑ish” chaining (`?.`) – would be nice.
- Decorators as interceptors: they take a function and return a wrapped function.
- Default argument values should be immutable; using mutable defaults like ``[]`` or ``{}`` can cause unexpected shared state.
- Deleting items while iterating over a list leads to bugs.
- Logical operators often require verbose patterns (``or`` for any truthy value, but sometimes only ``None``). I dislike the need for explicit ``if‑else``.
- Python allows integers as dictionary keys, but JSON requires string keys; this mismatch can be surprising.
- Accessing an element that isn’t present raises an error: ``[1,2].index(0)`` → ``ValueError``. Use ``if 0 in [1,2]:`` first.
- Recursion limit is around 10 000.
- Transition from ``Pipfile`` to ``requirements.txt`` (``pipenv install``) can be confusing.
- ``round()`` has unintuitive behavior (bankers rounding).
- ``__init__`` cannot have multiple signatures.
- ``setattr()`` offers no IDE autocomplete.

## Working on a Library

```bash
# Install local package steps:
1. Copy source code into the Docker container's root folder
2. docker exec -it <container_name> sh
3. Delete <source_code_folder>/build
4. cd <source_code_folder>
5. python3 setup.py install
```

```bash
python3 -m build   # Build library
python3 setup.py sdist  # Publish package
```

- ``requirements.txt`` is for development environments; ``setup.py`` (or ``pyproject.toml``) defines the client‑side distribution.
- ``python -m site`` → list Python library locations.
- ``help('modules')`` prints module docstrings.

## Debugging

```bash
time -f python3 test.py
```

```python
from time import timeit  # @timeit
```

> “No such file or directory” errors often stem from a missing shebang (``#!/usr/bin/env python``).

## Type Checks

- **mypy**
- **pytype** (Google)
- **pyre** (Facebook)
- **pyright** (Microsoft)

```python
def test(a: str) -> str | None:
    ...
```

## Standard Library Helpers

```python
import sys
sys.maxsize               # Largest integer
float('inf')              # Infinity
str.endswith(...)
str.startswith(...)
str.upper()
str.lower()
str.title()
str.strip()               # lstrip / rstrip
[::-1]                    # Reverse a sequence
list.count(2)             # Count occurrences
dict.setdefault(key, default)
type('MyClass', (object,), {
    '__init__': lambda self: None,
    'some_method': lambda self: 'value',
})
a, b, c = 1, 2, 3
a, b, *_, d = range(10)
print(a, b, d)
a = b = c = 4
f'Rounded to {2222222.222:,.2f}'
f'Date: {date.today():%Y-%m-%d}'
```

## Attributes

```python
dir(class_object)               # List all attributes
getattr(Abc, 'xyz')            # Get attribute (works on classes)
hasattr(obj, 'name')
setattr(obj, 'name', value)
delattr(obj, 'name')
vars(obj)                      # Return __dict__
```

## Properties & Destructuring

```python
# Dictionary get with default
{}.get('xyz')

# Python destructuring using operator.itemgetter
from operator import itemgetter
a, b = itemgetter('a', 'b')(params)

# Function call with unpacking
>>> foo(*[1, 2, 3])
x=1
y=2
z=3

mydict = {'x': 1, 'y': 2, 'z': 3}
>>> foo(**mydict)
x=1
y=2
z=3
```

## Built‑in Functions

```python
all(iterable)
any(iterable)

sys.getsizeof(obj)          # Approximate memory usage

import timeit
timeit.timeit('code')
# For profiling:
# cProfile, pstats → more setup but give a full audit
```

## Dunder / Magic Methods & Decorators

```python
def cust_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@staticmethod
def static_method():
    ...

@classmethod
def class_method(cls):
    ...

@property
def prop(self):
    ...

# Magic methods
__new__(cls, name, bases, attrs)
__init__(self)
__enter__(self)   # Context manager entry
__exit__(self, exc_type, exc_val, exc_tb)
__del__(self)

# Descriptor protocol
__get__(self, instance, owner)
__set__(self, instance, value)
__hash__(self)
__dict__
__slots__          # Save memory by fixing attributes

# Metaclasses
class Meta(type):
    ...

class Test(metaclass=Meta):
    ...
```

## Loops & Iteration

```python
# Sort by a single key
sorted_items = sorted(
    [item for item in items if item['a'] > 0],
    key=lambda x: x['b'],
    reverse=True,
)

# Sort by multiple keys
import operator
sorted_items = sorted(items, key=operator.itemgetter('x', 'y'))

# Custom comparator
from functools import cmp_to_key
def custom_cmp(x, y):
    return 0
sorted_items = sorted(items, key=cmp_to_key(custom_cmp))

for idx, value in enumerate(array):
    ...

passed_tests = filter(lambda x: x['passed'], tests)

# Map / Reduce style
lengths = map(len, ['abc', 'de', 'fghi'])

# Zip examples
pairs = list(zip([1, 2, 3], ['a', 'b', 'c']))   # Inner join
from itertools import zip_longest
combined = list(zip_longest([1,2], [3]))       # Outer join

# Find first matching element
first_match = next(x for x in items if isinstance(x).__name__ == 'Abc')

# Create iterator
it = iter([1, 2, 3])

# Duplicate iterator (useful when you need independent traversals)
i1, i2, i3 = itertools.tee(it, 3)
```

## Custom Utilities

```python
# Decimal rounding with proper half‑up behavior
from decimal import Decimal, ROUND_HALF_UP, getcontext, Context
getcontext().prec = 28

def basic_round(x, d=0, as_decimal=False):
    if x is None:
        return None
    quant = Decimal('1').scaleb(-d)
    rounded = Decimal(str(x)).quantize(quant, rounding=ROUND_HALF_UP)
    return rounded if as_decimal else float(rounded)

# Safe nested get (similar to lodash's `get`)
from collections.abc import Mapping, Sequence
from typing import Any, Iterable, Union

def get_in(
    obj: Any,
    keys: Iterable[Union[int, str]] = (),
    default: Any = None,
) -> Any:
    """
    Safely navigate nested dicts/lists.
    Returns `default` if any key is missing or the path cannot be traversed.
    """
    try:
        for key in keys:
            if isinstance(obj, Mapping):
                obj = obj.get(key, default)
            elif isinstance(obj, Sequence) and not isinstance(obj, (str, bytes)) and isinstance(key, int):
                obj = obj[key] if 0 <= key < len(obj) else default
            else:
                return default
            if obj is None:
                return default
        return obj
    except (KeyError, IndexError, TypeError):
        return default
```

## Buzzwords Zoo

- **PEP** – Python Enhancement Proposal.
- `.whl` – binary wheel format (introduced 2012); `.egg` – older binary format (2004).
- `odbcinst.ini` – configuration file for ODBC drivers.
- Since Python 3, an object's type is its class: ``type(obj) is obj.__class__``.
- Exception chaining: ``raise ValueError("Bad grape") from exc``.
