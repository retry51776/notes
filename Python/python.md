# Python

**Frustration**
- destructure like es6 `const {a, b, ...others} = obj;`
- get_in like methods or null chaining


**Working on library**
```
Install local package steps:
    1. copy source code into docker container's root folder
    2. docker exec -it [container_name] sh
    3. delete [source_code_folder]/build
    4. cd [source_code_folder]
    5. python3 setup.py install
```
**Build library**

```python3 -m build```

***Publish package**

```python3 setup.py sdist```

```
python -m site // List python library location

No such file or directory execute 'python
#!/usr/bin/env python
```

# Codes
```
def __init__(self):
def __enter__(self):
def __exit__(self):

getattr(obj, 'xyz')
sys.getsizeof(obj)


array = sorted(
        [item for item in items if item['a'] > 0],
        key=lambda x: x['b'], reverse=True
    )
for idx, value in enumerate(arrays):

date(2018, 9, 30).replace(day=31)
# idiom, like destruct object in javascritp
>>> mylist = [1,2,3]
>>> foo(*mylist)
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

# Standard Library

```
for key, group in itertools.groupby(array_json, key_func)

// round(2.50) == 2, wtf
// Python round have funny behavior
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



import argparse
parser.add_argument('-d', '--debug', help='XXX', action='store_true')
args = parser.parse_args()
```
**Multi Process**
```
# Multi-Process
# Note: ProcessPoolExecutor print will not work, logs must return to main process
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
with ThreadPoolExecutor(max_workers=5) as executor:
	worker = executor.submit(funcion_x, arg1, arg2)
	for worker in as_completed([worker]):
		print(worker.result())
```

# Flask

```
# Flask Load Config
app = Flask(__name__)
app.config.from_pyfile('appcfg.py')
app.register_blueprint(company_app, url_prefix='/company')

# Flask Events
@app.before_request
@app.teardown_requesst

# Create Flask Endpoint
VIEW_APP = Blueprint('view', __name__)
@VIEW_APP.route('/ConfigureSSO', methods=['POST'])
def configure_sso():
    return json_response(response)

# Golbal Flask error handling
app.register_error_handler(Exception, handler)
```


# SQL Alchemy

- ORM classes
  - to CRUD table, but can't modify table. easier to handle in python
- Schema classes
  - harder to handle in python, can modify table

- `create_engine()` won't open connection until session query
- `sessionmaker()` will reuse connection pool

**Auto ORM**
```
from sqlalchemy.ext.automap import automap_base

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Product = Base.classes.tableName
count = db.session.query(Product).update({Product.ID: 123})
record = {'ID': 124, 'name': 'whatever', 'price': 0}
Product.insert().values(**record)
```

**Cursor Query**
```
cursor = session.connection().cursor()
cursor.execute(query) //session.execute() will work too

sales = [dict(zip(cursor.column_names, row)) for row in cursor.fetchall()]

# Reflection can modify schema
# https://docs.sqlalchemy.org/en/13/core/reflection.html
```

```
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

# Tech Terms

.wheel is python binary file