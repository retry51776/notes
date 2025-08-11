# Standard Library Utilities

## dates

```python
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

## bisect

```python
import bisect

# Get the index where a value should be inserted to keep the list sorted
idx = bisect.bisect(array, value)

# Insert into a sorted array while keeping order
bisect.insort(array, value)
```

## os and socket modules

```python
from pprint import pprint
import os
import socket
import traceback

# Print an object (pretty‑printed)
pprint(obj)

# Print an object with limited depth
pprint(obj, depth=2)  # only prints two nested levels

# Set a Linux environment variable
os.environ['URL'] = 'test'  # set env var

# List all environment variables
print(os.environ)

# Current working directory
print(os.getcwd())

# Walk the filesystem
for root, dirs, files in os.walk('/'):
    print(root, dirs, files)

# Check if a path exists
os.path.exists('/etc')

# Remove a file
os.remove('/etc/test.txt')

# Remove an empty directory
os.rmdir('/folder')

# Get hostname and IP address
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f'Hostname: {hostname}, IP: {ip_address}')

# Show stack trace (useful for debugging)
for line in traceback.format_stack():
    print(line.strip())
```

## Custom Data Types

```python
from dataclasses import dataclass, field
from enum import Enum

@dataclass(order=True)
class Xyz:
    id: int
    text: str = field(default="xxx")

    def __lt__(self, other):
        return self.id > other.id  # reversed order for demonstration


class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2

# Pattern matching (Python 3.10+)
color = Color.RED
match color:
    case Color.RED:
        print("Red")
    case _:
        print("No match")

# Store variables into binary format
import struct

packed = struct.pack('ii', 11, 22)          # pack two integers
a, b = struct.unpack('ii', packed)         # unpack them again
print(a, b)
```

## functools

```python
import functools
from functools import lru_cache

# Partially apply arguments to a function
partial_func = functools.partial(some_func, 1, 2, 3)

# Preserve metadata when wrapping a function
@functools.wraps(func)
def wrapper(*args, **kwargs):
    return func(*args, **kwargs)

# Cache results (Python 3.10+)
@functools.cache
def expensive_computation(x):
    ...

# LRU cache with a maximum size
@lru_cache(maxsize=32)
def another_expensive_func(y):
    ...

# Reduce a sequence
result = functools.reduce(lambda a, b: a + b, [1, 2, 3], 0)

# Simple logging decorator
def logged(func):
    @functools.wraps(func)
    def with_logging(*args, **kwargs):
        print(f"{func.__name__} was called")
        return func(*args, **kwargs)
    return with_logging
```

## itertools

```python
import itertools

# Group consecutive items by a key function (requires sorted input)
for key, group in itertools.groupby(sorted_array, key=key_func):
    print(key, list(group))

# Combinations with replacement
list(itertools.combinations_with_replacement([1, 2, 3], 2))

# Simple combinations
list(itertools.combinations([1, 2, 3], 2))

# Shuffle a list (in‑place)
import random
random.shuffle(my_list)

# Chain multiple iterables together
combined = itertools.chain(list1, list2)

# Cartesian product
for x, y in itertools.product([1, 2], ['a', 'b']):
    print(x, y)

# Slice an iterator (islice)
list(itertools.islice('ABCDEFG', 2))            # A B
list(itertools.islice('ABCDEFG', 2, 4))         # C D
list(itertools.islice('ABCDEFG', 2, None))      # C D E F G
list(itertools.islice('ABCDEFG', 0, None, 2))   # A C E G
```

## collections

```python
from collections import defaultdict, Counter, deque

# Default dictionary with int default (avoids KeyError)
counts = defaultdict(int)
counts['apple'] += 1

# Counter for frequency counting
c = Counter(['a', 'b', 'a', 'c'])
print(c.most_common(5))   # top 5 most common elements
print(c.total())          # total number of items counted
c.subtract(Counter({'a': 2}))  # subtract counts

# Deque as a stack or queue
stack = deque()
stack.append(0)      # push
stack.append(1)
stack.pop()          # pop

queue = deque()
queue.append('first')
queue.popleft()      # dequeue
```

> `Counter` is very efficient, but note that it does **not** automatically update when the underlying list changes.

## queue

```python
from queue import PriorityQueue

q = PriorityQueue()
q.put((5, 'Write'))
q.put((1, 'Code'))
q.put((3, 'Study'))

while not q.empty():
    priority, task = q.get()
    print(f'Priority {priority}: {task}')
```

## heapq

```python
import heapq

heap = [5, 1, 3]
heapq.heapify(heap)          # Transform list into a heap in‑place
heapq.heappush(heap, 2)      # Push new item
smallest = heapq.heappop(heap)  # Pop smallest item

# Largest n elements
largest_three = heapq.nlargest(3, iterable)

# Smallest n elements
smallest_three = heapq.nsmallest(3, iterable)
```

## importlib

```python
import importlib

module_name = "some_package.module_a"
module = importlib.import_module(module_name)
```

## csv

```python
import csv

with open('numbers.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

## Multiprocessing and Threading

### General notes

- **Multithreading** incurs context‑switch overhead.
- **Multiprocessing** uses more CPU but avoids the GIL.
- **Cooperative multitasking** (async/await) is similar to a single‑threaded event loop.

```python
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed

def some_function(arg1, arg2):
    ...

# Using threads
with ThreadPoolExecutor(max_workers=5) as executor:
    future = executor.submit(some_function, 'a', 'b')
    for result in as_completed([future]):
        print(result.result())

# Using processes
with ProcessPoolExecutor() as executor:
    futures = [executor.submit(some_function, i) for i in range(10)]
    for f in as_completed(futures):
        print(f.result())
```

### Threading example

```python
import threading

def thread_function(name):
    print(f"Thread {name} starting")
    # do work here
    print(f"Thread {name} finished")

t = threading.Thread(target=thread_function, args=('A',))
t.start()
t.join()  # Wait for the thread to finish
```

### Multiprocessing example

```python
import multiprocessing

def worker(x):
    return x * x

with multiprocessing.Pool() as pool:
    results = pool.map(worker, range(10))
    print(results)

# Shared value example
counter = multiprocessing.Value('i', 0)

def increment(counter):
    with counter.get_lock():
        counter.value += 1

p = multiprocessing.Process(target=increment, args=(counter,))
p.start()
p.join()
print(counter.value)
```

### Running external commands

```python
import subprocess

subprocess.run(['ls', '-l'])
```

## contextlib

```python
from contextlib import contextmanager

@contextmanager
def managed_resource():
    # Setup code
    resource = acquire_resource()
    try:
        yield resource
    finally:
        # Teardown code
        release_resource(resource)

# Usage
with managed_resource() as res:
    # work with res
    pass
```

## argparse

```python
import argparse

parser = argparse.ArgumentParser(description='Example script')
parser.add_argument('-d', '--debug', help='Enable debug mode', action='store_true')
args = parser.parse_args()

if args.debug:
    print('Debug mode is on')
```

## asyncio

```python
import asyncio

async def what():
    print('before sleep')
    await asyncio.sleep(2)
    print('after sleep')
    return 0

# Run the coroutine in the main thread
asyncio.run(what())

# Create a task that runs concurrently
task = asyncio.create_task(what())
await task  # In an async context, wait for completion
```

## Other standard‑library utilities

```python
from pathlib import Path
from urllib.request import urlopen
import pickle   # Store binary data
import json     # Store JSON data
```

> `httpx` is often faster than the built‑in `urllib` for multiple network requests.

