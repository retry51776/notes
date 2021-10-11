# Python

**Frustration**
- ~~destructure like es6 `const {a, b, ...others} = obj;`~~
    > new python 3.10 supports this https://docs.python.org/release/3.10.0/whatsnew/3.10.html
- get_in like methods or null chaining
- decorator just kind hard to read, maybe should implement in context manager instead
- function params's default value should be standard type
    > don't do `[]` or `{}`, buggs, reference, not by value
- don't delete in loop


**Working on library**
```
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

`python -m site`
> List python library location

## Problems
> No such file or directory execute 'python

`#!/usr/bin/env python`

## type checks
- myPy - 
- pytype: google
- pyre: facebook
- pyright: microsoft
  

# Python Codes
## Build in functions
```
float('Inf') # max value
def test(a: str) -> str | None:

@staticmethod
@porperty
@cache

class events
def __init__(self):
def __enter__(self):
def __exit__(self):
__del__

# python descriptor
__get__
__set__

{}.get('xyz') # only works w obj
hasattr()
getattr(obj, 'xyz') # also work in class
setattr()
delattr()

all()
any([0, 1, 0])

vars(class) # retrun Object
sys.getsizeof(obj) # debug variable Ram
time -f python3 test.py # debug script Ram & time

date(2018, 9, 30).replace(day=31)

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

# python desturcture
a, b = itemgetter('a', 'b')(params)

# Set linux envirement variables
export URL=test //set env
```

## loop
```
array = sorted(
    [item for item in items if item['a'] > 0],
    key=lambda x: x['b'], reverse=True
)
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

# Standard Library
## functools
```
@functools.cache
@lru_cache(maxsize=32)

functools.reduce(lambda a, b: a+b, lis, 100)

def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging
```

## Itertools
```
for key, group in itertools.groupby(array_json, key_func)

# really only uses in quiz
combinations_with_replacement
combinations

random.shuffle
itertools.chain # join list

# islice('ABCDEFG', 2) --> A B
# islice('ABCDEFG', 2, 4) --> C D
# islice('ABCDEFG', 2, None) --> C D E F G
# islice('ABCDEFG', 0, None, 2) --> A C E G
```
## collections
```
collections.defaultdict
from collections import Counter

c = Counter(list)
c.keys() # set of list values
c.values() # repeat count
c.most_common(5) // top 5 counts, :-2:-1 to get least count
c.total() == len(list)
c.subtract(an_other_counter) # will modify c

```
> Counter is super, but counter WON'T change with array. Uses heap instead


## heapq
```
import heapq
heapq.heapify(list_unorder)
heapq.heappush(
heapq.heappop(

heapq.nlargest(n:int, iterable, key:None) # key similar to sort(list, key)
heapq.nsmallest()

```
## CSV
```
import csv

with open("numbers.csv") as f:
    r = csv.reader(f)
    for row in r:
        print row
```
## Multi Process
```
# Multi-Process
# Note: ProcessPoolExecutor print will not work, logs must return to main process
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
with ThreadPoolExecutor(max_workers=5) as executor:
	worker = executor.submit(funcion_x, arg1, arg2)
	for worker in as_completed([worker]):
		print(worker.result())

import threading
x = threading.Thread(target=thread_function, args=(1,))
x.start()
# similar JS await
x.join()
```
## contextlib
```
from contextlib import contextmanager

@contextmanager
def get_session(self):
    session = None
    for i in range(1, 4):
        try:
            session = sessionmaker(bind=self.XXX_engine)()
            yield session
            break
        except Exception:
            self.logger.exception(f'Reconnecting to XXX. {i}th attempted')

            # Re-create engine
            self.xxx_engine = create_engine(self.config.XXX_URI, pool_pre_ping=True, pool_size=self.pool_size)
    if session:
        session.close()
```
## argparse
```
import argparse
parser.add_argument('-d', '--debug', help='XXX', action='store_true')
args = parser.parse_args()
```
## asyncio
```
async def what():
    return 0
asyncio.run(what)
```
## custom utilities
```
# round(2.50) == 2, wtf
# Python round have funny behavior
def basic_round(x, d=0, as_decimal=False):
    if x is None:
        return None
    round_digit = Decimal(10) ** -d
    rounded = Decimal(str(x)).quantize(round_digit, rounding=ROUND_HALF_UP)
    return rounded if as_decimal else float(rounded)
```
```
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

# Tech Terms

- .wheel is python binary file
- odbcinst.ini
    > registry and configuration file for ODBC drivers in an environment