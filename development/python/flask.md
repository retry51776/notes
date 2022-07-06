# SQLAlchemy

> ORM classes
>> easier to CRUD table
>
>> but can't modify schema


> Schema classes
>> harder to handle in python;
>
>> CREATE and DROP statements (known as DDL), constructing SQL queries

> `SQLALCHEMY_DATABASE_URL` will used by SQLAlchemy(app) by default
## Sqlalchemy Modules
- orm
  - Load `Load(xxx_orm).load_only('c1', 'c2')`
  - sessionmaker `(bind=xxx_engine)()`
  - joinedload `Force Query everything together`
  - relationship `("orm_class_name", back_populates="parent_orm.xxx_relationship_name")`
  - backref
  - exc
    - NoResultFound
    - DBAPIError
    - TimeoutError
- ext
  - automap
    - automap_base
  - declaretive
    - declararive_base() `Define not default schema with metadata.schema`
  - hybrid
    - hybrid_property `seems like calculate field`
- sql
  - select
  - and_
  - or_
  - not_
  - tuple_
  - functions `advance aggeration`
    - count()
    - sum()
  - expression
    - desc
    - asc
    - literal
- schema
  - Sequence

- create_engine
- MetaData
- Table `('xxx_table', MetaData(), autoload=True, autoload_with=xxx_engine)`
- Column
- Integer
- String
- Boolean
- Date
- ForeignKey
- VARBINARY
- Enum


### Table Relationship

> backref is legacy parameter

> It's one of most conflusion area.

### How ORM process relationship
> 1. ORM process Director model
> 2. there is a relationship call movies
> 3. uselist ? Director.movies = [Movie, Movie] : Director.movies = cls
> 4. Movie cls have ForeignKey('director.id') ? do_sub_query : left_join
> 5. has backref ? Movie.[backref_value] = Director
```
# backref only create relationship in one ORM, never both
class Director(db.Model): 
  id = db.Column(db.Integer, primary_key=True)
  #                     ORM_Name    create Movie.director
  movies = relationship("Movie", backref="director", uselist=False, lazy='select')

# back_populates must explicitly define relationship both ORM

lazy [select, immediate, joined, subquery, selectin]
```


<hr/>

- `engine = create_engine(URI, pool_pre_ping=True, pool_size=10)` 
  - won't create connection until query
  - defined connection pool
- `conn_pool = sessionmaker(bind=engine)`
  - create connection pool
  - defined session default behavior
- `session = conn_pool()`
  - will make a connection or reuse from pool
  - not thread safe
  - `session.close()` may not commit, may not close connection

**Auto Schema Ops**

```
from sqlalchemy.ext.automap import automap_base

# 1. Auto Map Whole DB
Base = automap_base()
Base.prepare(db.engine, reflect=True)
Product = Base.classes.Product

# 2. Auto Map single table
meta = MetaData()
Product = Table('Product', meta, autoload=True,  autoload_with=mysql_engine)

# 3. Self define Schema
metadata_obj = MetaData()
Product = Table("Product", metadata_obj, Column('amount', Integer))

# read/edit
p = db.session.query(Product).update({Product.ID: 123})
record = {'ID': 124, 'name': 'whatever', 'price': 0}
Product.insert().values(**record)

```

**ORM ops**
```
sale = Sale(amount=123)
session.add(sale)
session.commit()

sale.amount = 321
session.commit()

# support create & edit
sale = Sale() if create else session.query(Sale).first()
setattr(sale, 'amount', 123)
if create:
    session.add(sale)
session.commit()

# add multi records
session.add_all([sale, addr, invt])

# orm property, not relationship name
query = query.options(joinedload('abc').joinedload('efg'))

import enum
from sqlalchemy import Enum

class xxx(enum.Enum):
  red = 1
  green = 2

  def to_json(self):
    return self.name

color = Column('color', Enum(xxx))
```

**Cursor Query**
```
cursor = session.connection().cursor()
cursor.execute(query) //session.execute() will work too

sales = [dict(zip(cursor.column_names, row)) for row in cursor.fetchall()]

# Reflection can modify schema
# https://docs.sqlalchemy.org/en/13/core/reflection.html
```

# Flask

## Methods
- Get
- Post `insert, common mistake`
- Put `idempotent; usually for edit`
- Delete
- Patch `similar to put, but with side effect`

## Common Used Modules
- Flask
- Blueprint
  - @before_app_request
  - @before_app_first_request
  - @before_request
  - @after_request
  - @after_app_request
- request
  - method `str`
- request_started
- request_finished
- app
  - cli
    - command("xx_cmd") `flask xxx_app xx_cmd`
- g `gobal; able to access all wsgi variables`
- current_app
- appcontext_tearing_down `appcontext_tearing_down.connect(xxx, app)`

- session `session object, required app.secret_key`
- sessions `looks like flask manage session utilities`
- Response
- stream_with_context `return Response(stream_with_context(generator))`


- make_response
- jsonify
- send_file
- send_from_directory
- render_template `render_template("xxx.html", name="xxx")`
- url_for


```
res = make_response(json.dumps(xxx))
res.headers['Content-Type'] = 'application/json'
res.status_code = 200

# Flask Load Config
from flask_cache import Cache
app = Flask(__name__)
cache = Cache(app)
app.config.from_pyfile('appcfg.py')
app.register_blueprint(company_app, url_prefix='/company')

# Flask Events
before_first_request
@app.before_request
@app.teardown_requesst

# Create Flask Endpoint
VIEW_APP = Blueprint('view', __name__)
@VIEW_APP.route('/ConfigureSSO', methods=['POST'])
@cache.cached(timeout=60)
def configure_sso():
    return json_response(response)

# Golbal Flask error handling
app.register_error_handler(Exception, handler)
```
## webargs

> parse & validate HTTP request object

- flaskparser
  - use_args `inject params as args`
  - use_kwargs `inject params as kwargs`
  - parser
- fields
  - Nested
  - DelimitedList `never used`
  - Int()
  - Decimal
  - String(validate=Regexp())
  - Bool()
  - List()
  - Raw()
- validate `don't have schema, Regexp`
  - Length()
  - Range()
  - Regexp
  - OneOf
  - NoneOf


## marshmallow
> ORM for complex data types

- fields
  - Nested()
  - Date()
  - Str()
- validate
  - Regexp
  - OneOf
  - Range
  - Schema
- validates_schema

```
@xxx.route('')
@use_kwargs(sss(), location=('json'),)
def xxx()

class sss(Schema):
  some_prop = fiel.Str()

  @validates_schema
  def valid(self, data):
    # complex logic check here
    raise Exception('sss')
```

## Flask Template
```
<p>name is {{ name }}</p>

<img src="{{ url_for('static', filename="xxx.jpg")}}"/>

# Template Inheritance
{% block content %} # Similar to PHP, supports python loop
{% endblock %}

{% extends "xxx.html" %}
{% block content %}
<h1>xxxx</h1>
{% endblock %}
```

# Flask Middleware
```
from werkzeug.wrappers import Request, Response
class xxxMiddleWare():
  def __init__(self, app)
    pass
  def __call__(self, environ, start_response):
    req = Request(environ)
    print(req.body)
    if True:
      return self.app(environ, start_response)
    res = Response('Deny', minetype='text/plain', status=401)
    return res(environ, start_response)

# attach middleware to flask
app.wsgi_app = xxxMiddleWare(app.wsgi_app)
```