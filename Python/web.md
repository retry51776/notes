
# SQL Alchemy

- ORM classes
  - easier to CRUD table
  - but can't modify schema
- Schema classes
  - harder to handle in python
  - CREATE and DROP statements (known as DDL), constructing SQL queries

- `engine = create_engine(URI, pool_pre_ping=True, pool_size=10)` 
  - won't create connection pool
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

query = query.options(joinedload('building'))
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

```
# Flask Load Config
app = Flask(__name__)
app.config.from_pyfile('appcfg.py')
app.register_blueprint(company_app, url_prefix='/company')

# Flask Events
before_first_request
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

