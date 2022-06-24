# Python

**Frustration**
- ~~destructure like es6 `const {a, b, ...others} = obj;`~~
    > new python 3.10 supports this https://docs.python.org/release/3.10.0/whatsnew/3.10.html
- get_in like methods or null chaining
- decorator just kind hard to read, maybe should implement in context manager instead
- function params's default value should be standard type
    > don't reference type `[]` or `{}`, any modify reference will presists default value in next function call
- don't delete in loop
- falsely values & or, need similar `or` for `None` only, I hate `if else`
- Python allow integer as key of object, but JSON file requires key as string. Can be suprised load object is different.
- `[1,2].index(0)` will throw an error, must check before get index`if 0 in [1,2]:`


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

`def test(a: str) -> str | None:`

# Python Codes
## Starndard Type
```
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

a, b, c = 1, 2, 3
a, b, *_, d = list(range(10))
print(a, b,  d)
a = b = c = 4
f'Rounded to {2222222.222:,.2f}'
f'Format to {date.today():%Y-%m-%d}'
```
## CRUD Property
```
{}.get('xyz') # only works w obj

getattr(Abc, 'xyz') # only work w class
hasattr()
setattr()
delattr()
vars(class) # retrun Object

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

# dates
```
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

# less than month unit
date(2018, 9, 30).replace(day=31) + timedelta(days=1)
# more than month unit
date.today() + relativedelta(months=1)
date.max
date.min
```
## Build in functions
```
all()
any([0, 1, 0])

sys.getsizeof(obj) # debug variable Ram

timeit.timeit(xyz)
time -f python3 test.py # debug script Ram & time
#cProfile, pstats takes more setup, but better audit whole project

# Set linux envirement variables
export URL=test //set env

# logging show stacktrace
stack_info=True
for line in traceback.format_stack():
    print(line.strip())
```

## dunder|magic methods, decorator
```
@staticmethod
@porperty
@xyz.setter

class events
__init__(self):
__enter__
__exit__
__del__

# python descriptor
__get__
__set__
__hash__
__dict__
__slots__ # similar to property, can't add more __slots__ in run time, but less RAM
__repr__

# self implement class operators
from functools import totoal_ordering
@total_ordering
xyz.__class__ is self.__class__
__eq__
__ne__
__ge__
__lt__
__le__

# auto implement
from dataclasses import dataclass, field
@dataclass(order=True)
class Xyz:
    id: int
    text: str = field(default="xxx")
    def __lt__(self, element):
        return self.id > element.id;
```

## loop
```
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

# Standard Library
## functools
```
@functools.cache # only 3.10
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
# requires array already sorted by key
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
from collections import defaultdict
obj = defaultdict(int) # default int, no more  key error!! super

from collections import Counter

c = Counter(list)
c.keys() # set of list values
c.values() # repeat count
c.most_common(5) // top 5 counts, :-2:-1 to get least count
c.total() == len(list)
c.subtract(an_other_counter) # will modify c

from collections import deque
# stack methods
t = deque()
t.append(0)
t.append(1)
t.pop()

t.popleft()
```
> Counter is super, but counter WON'T change with array. Uses heap instead

## queue
```
from queue import PriorityQueue
q = PriorityQueue()

q.put((5, 'Write'))
q.put((1, 'Code'))
q.put((3, 'Study'))
q.qsize()

while not q.empty():
    next_item = q.get()
    print(next_item) # smalest first
```

## heapq
```
import heapq
heapq.heapify(list_unorder)
heapq.heappush(
heapq.heappop( # smallest

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
class DB():
    def __exit__(self, exc_type, exc_val, exc_traceback):
        self.disconnect_db()

    def init_db(self):
        self.db_engine = create_engine(self.config.XXX_URI, pool_pre_ping=True, pool_size=self.pool_size)
        self.session_mk = sessionmaker(bind=self.db_engine)

    def disconnect_db(self):
        if hasattr(self, 'session_mk') and self.session_mk:
            self.session_mk.close_all()
        if hasattr(self, 'db_engine') and self.db_engine:
            self.db_engine.dispose()

    @contextmanager
    def get_session(self):
        session = None
        for i in range(1, 4):
            try:
                session = self.session_mk()
                break
            except Exception:
                self.logger.exception(f'Reconnecting to XXX. {i}th attempted')
                self.init_db()
        yield session
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
    print('before sleep')
    await asyncio.slee(2)
    print('after sleep')
    return 0

asyncio.run(what()) # runs in MAIN branch
task = asyncio.create_task(what()) # runs off branch
await task # similar thread.join()

```
> httpx grather is faster multiple network requests
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