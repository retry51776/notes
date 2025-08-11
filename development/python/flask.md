# SQLAlchemy

> ORM classes simplify CRUD operations on tables, but they cannot modify the schema.

> Schema (DDL) classes are harder to work with in Python; they generate `CREATE` and `DROP` statements.

`SQLALCHEMY_DATABASE_URL` is used by `SQLAlchemy(app)` by default.

## SQLAlchemy Modules

- **orm**
  - `Load(xxx_orm).load_only('c1', 'c2')`
  - `sessionmaker(bind=xxx_engine)()`
  - `joinedload` – force a query to load related objects together
  - `relationship("orm_class_name", back_populates="parent_orm.xxx_relationship_name")`
  - `backref`
  - **exc**
    - `NoResultFound`
    - `DBAPIError`
    - `TimeoutError`

- **ext**
  - `automap`
    - `automap_base`
  - `declarative`
    - `declarative_base()` – define a non‑default schema with `metadata.schema`
  - `hybrid`
    - `hybrid_property` – calculate fields on the fly

- **sql**
  - `select`, `and_`, `or_`, `not_`, `tuple_`
  - Functions: `count()`, `sum()`, etc.
  - Expressions: `desc`, `asc`, `literal`

- **schema**
  - `Sequence`

- Core utilities
  - `create_engine`
  - `MetaData`
  - `Table('xxx_table', MetaData(), autoload=True, autoload_with=xxx_engine)`
  - `Column`, `Integer`, `String`, `Boolean`, `Date`, `ForeignKey`, `VARBINARY`, `Enum`

### Table Relationships

> `backref` is a legacy parameter and often causes confusion.

> It defines the relationship only on one side of the ORM; the opposite side must be defined manually (e.g., with `back_populates`).

#### How ORM Processes Relationships
1. The ORM processes the **Director** model.  
2. A relationship called `movies` is created.  
3. If `uselist=True`, `Director.movies = [Movie, Movie]`; otherwise `Director.movies = Movie`.  
4. `Movie` has a foreign key (`ForeignKey('director.id')`) → decides between sub‑query or left join.  
5. If `backref` is present, `Movie.<backref_value>` points back to `Director`.

```python
class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # ORM_Name creates Movie.director automatically
    movies = relationship("Movie", backref="director", uselist=False, lazy='select')
```

`back_populates` must explicitly define the relationship on both sides.

Lazy loading options: `select`, `immediate`, `joined`, `subquery`, `selectin`.

## Engine & Session Management

- `engine = create_engine(URI, pool_pre_ping=True, pool_size=10,
                         connect_args={"sslrootcert": "", "sslcert": "", "sslkey": ""})`
  - Does not create a connection until the first query.
  - Defines a connection pool.

- `SessionLocal = sessionmaker(bind=engine)`
  - Creates a session factory (connection pool).

- `session = SessionLocal()`
  - Obtains a connection from the pool; **not thread‑safe**.
  - `session.close()` may not commit or close the underlying connection.

### Auto‑Schema Operations

```python
from sqlalchemy.ext.automap import automap_base

# 1. Automap the whole database
Base = automap_base()
Base.prepare(db.engine, reflect=True)
Product = Base.classes.Product

# 2. Automap a single table
meta = MetaData()
Product = Table('Product', meta, autoload=True, autoload_with=mysql_engine)

# 3. Define schema manually
metadata_obj = MetaData()
Product = Table("Product", metadata_obj,
               Column('amount', Integer))
```

#### Reading & Editing

```python
p = db.session.query(Product).update({Product.ID: 123})
record = {'ID': 124, 'name': 'whatever', 'price': 0}
Product.insert().values(**record)
```

### ORM Operations

```python
sale = Sale(amount=123)
session.add(sale)
session.commit()

sale.amount = 321
session.commit()

# Create or update
sale = Sale() if create else session.query(Sale).first()
setattr(sale, 'amount', 123)
if create:
    session.add(sale)
session.commit()

# Add multiple records
session.add_all([sale, addr, invt])

# ORM query with joinedload
query = query.options(joinedload('abc').joinedload('efg'))
```

```python
import enum
from sqlalchemy import Enum

class ColorEnum(enum.Enum):
    red = 1
    green = 2

    def to_json(self):
        return self.name

color = Column('color', Enum(ColorEnum))
```

### Raw Cursor Queries

```python
cursor = session.connection().cursor()
cursor.execute(query)          # session.execute() also works
sales = [dict(zip(cursor.column_names, row)) for row in cursor.fetchall()]
```

*Reflection can modify the schema.*  
[SQLAlchemy Reflection Documentation](https://docs.sqlalchemy.org/en/13/core/reflection.html)

# Flask

> Recommended number of workers: `2 * CPU + 1`.

## HTTP Methods
- **GET**
- **POST** – insert (common mistake)
- **PUT** – idempotent, usually for updates
- **DELETE**
- **PATCH** – similar to PUT but with side effects

## Common Flask Modules

- `Flask`
- `Blueprint`
  - `@before_app_request`
  - `@before_app_first_request`
  - `@before_request`
  - `@after_request`
  - `@after_app_request`
- `request` (has attribute `method: str`)
- Signals: `request_started`, `request_finished`
- `app`
  - CLI commands via `@app.cli.command("xx_cmd")`
- `g` – global namespace for request‑scoped variables
- `current_app`

### Session Management
- `session` object (requires `app.secret_key`)
- `sessions` – utilities for managing Flask sessions

### Responses
- `Response`
- `stream_with_context` – e.g., `return Response(stream_with_context(generator))`
- `make_response`, `jsonify`, `send_file`, `send_from_directory`, `render_template`, `url_for`

```python
res = make_response(json.dumps(xxx))
res.headers['Content-Type'] = 'application/json'
res.status_code = 200
```

#### Flask Configuration Example

```python
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app)
app.config.from_pyfile('appcfg.py')
app.register_blueprint(company_app, url_prefix='/company')
```

#### Flask Events

```python
@app.before_first_request
def before_first():
    pass

@app.before_request
def before():
    pass

@app.teardown_request
def teardown(exception):
    pass
```

### Blueprint Example

```python
VIEW_APP = Blueprint('view', __name__)

@VIEW_APP.route('/ConfigureSSO', methods=['POST'])
@cache.cached(timeout=60)
def configure_sso():
    return json_response(response)
```

#### Global Error Handling

```python
app.register_error_handler(Exception, handler)
```

## Webargs

> Parse and validate HTTP request data.

- **flaskparser**
  - `use_args` – inject parameters as positional args  
  - `use_kwargs` – inject parameters as keyword args  
  - `parser`
- **fields**
  - `Nested`, `DelimitedList`, `Int()`, `Decimal`, `String(validate=Regexp())`,
    `Bool()`, `List()`, `Raw()`
- **validate**
  - `Length()`, `Range()`, `Regexp`, `OneOf`, `NoneOf`

## Marshmallow

> Serialization / deserialization library for complex data types.

```python
@xxx.route('')
@use_kwargs(sss(), location=('json'),)
def xxx():
    pass

class sss(Schema):
    some_prop = fields.Str()

    @validates_schema
    def validate(self, data, **kwargs):
        # complex validation logic here
        raise Exception('validation error')
```

## Flask Templates

```html
<p>Name is {{ name }}</p>

<img src="{{ url_for('static', filename='xxx.jpg') }}" />
```

### Template Inheritance

```jinja
{% extends "base.html" %}
{% block content %}
<h1>Title</h1>
{% endblock %}
```

## Flask Middleware

```python
from werkzeug.wrappers import Request, Response

class XxxMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        req = Request(environ)
        print(req.get_data())
        # Example condition
        if True:
            return self.app(environ, start_response)
        res = Response('Deny', mimetype='text/plain', status=401)
        return res(environ, start_response)

# Attach middleware to Flask app
app.wsgi_app = XxxMiddleware(app.wsgi_app)
```
