# Standard Library Utilities

## dates
```py
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse

parse('2019-01-01').date().strftime('%Y-%m-%d')
# less than month unit
date(2018, 9, 30).replace(day=31) + timedelta(days=1)
# more than month unit
date.today() + relativedelta(months=1)
date.max
date.min
```


# os, socket module
```py
from pprint import pprint
print(object)
print(object, depth=2) # only print 2nd nested level

# Set linux envirement variables
export URL=test //set env
import os
os.environ // all envirement variables
os.getcwd() // current dir

import socket
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)


# logging show stacktrace
stack_info=True
for line in traceback.format_stack():
    print(line.strip())
```


## Custom Data Types
```py
from dataclasses import dataclass, field
@dataclass(order=True)
class Xyz:
    id: int
    text: str = field(default="xxx")
    def __lt__(self, element):
        return self.id > element.id;

from enum import Enum
class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2


match color:
    case Color.RED:
        print("")
    case _:
        print ('no match')

# Store variables into binary
import struct
x = struct.pack('111', 11, 22)

(a, b, c) = struct.unpack(x)
```

## functools
```py
functools.partial(xxx_func, 1, 2, 3) # prefill xxx_func w params
@functools.wraps(func) # assign __name__, __doc__ attributes in the wrapping function before returning it (think of update 'this = super' in js)
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
```py
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
```py
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
```py
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
```py
import heapq
heapq.heapify(list_unorder)
heapq.heappush(
heapq.heappop( # smallest

heapq.nlargest(n:int, iterable, key:None) # key similar to sort(list, key)
heapq.nsmallest()

```
## CSV
```py
import csv

with open("numbers.csv") as f:
    r = csv.reader(f)
    for row in r:
        print row
```

## Multi Process

- Multi Thread cost time for context switch
- Multi Process cost more CPU
- Cooperative Multi Task (similar single event loop)
    - Coroutine `A variant of functions that enables concurrentcy via Cooperative Multi Task`

```py
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

import multiprocessing
pool = multiprocessing.Pool(multiprocessing.cpu_count())
def xxx_func(whatever):
    return whatever

result = pool.map(xxx_func, frame.iterrows())
pool.close()
pool.join()


def xx(counter):
    counter.value += 1
counter = multiprocessing.Value('i', 0)
tsk = multiprocessing.Process(target=xx, args(counter))
import subprocess
subprocess.run()
```
## contextlib
```py
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
```py
import argparse
parser.add_argument('-d', '--debug', help='XXX', action='store_true')
args = parser.parse_args()

import sys
print(sys.argv[1])
```
## asyncio
```py
async def what():
    print('before sleep')
    await asyncio.slee(2)
    print('after sleep')
    return 0

asyncio.run(what()) # runs in MAIN branch
task = asyncio.create_task(what()) # runs off branch
await task # similar thread.join()

```

## others standard lib
```py
from pathlib import Path
from urllib.request import urlopen
import pickle // store in binary
import json // store in json
```
> httpx grather is faster multiple network requests