
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

# orm property, not relationship name
query = query.options(joinedload('abc').joinedload('efg'))
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

## Crawler
### splash
> render dynamic page for scrapy
```
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy_splash import SplashRequest


# Start the scraping process
process = CrawlerProcess({
  'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(TestScraper)
process.start()

class TestScraper(scrapy.Spider):
  name = 'test'
  custom_settings = {
      'SPLASH_URL': SPLASH_URL,
      'DOWNLOADER_MIDDLEWARES': {
          'scrapy_splash.SplashCookiesMiddleware': 723,
          'scrapy_splash.SplashMiddleware': 725,
          'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
      },
      'SPIDER_MIDDLEWARES': {
          'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
      },
      'DUPEFILTER_CLASS': 'scrapy_splash.SplashAwareDupeFilter',
      'HTTPCACHE_STORAGE': 'scrapy_splash.SplashAwareFSCacheStorage',
      'LOG_ENABLED': False, // Splash Logger attched to golbal logger, not good
  }

  def start_requests(self):
      yield SplashRequest(
          url=url,
          callback=self.parse,
          args={'wait': 3}
      )

  def parse(self, response):
      for url in response.xpath('//ul[@class="abc"]/li/a[@class="xyz"]/@href').getall():
          // whatever
```
---
## Message Broker

> Improves decoupling, fault tolerance, scalability

> Queue : consumed once

> Pub Sub: consumed many time
### Protocal
- AMQP
  > Adcanced Message Queuing Protocol, move message between applications.
  
  > Pika is python implelemntation AMQP 0.9.1
- MQTT
- STOMP

---

**RabbitMQ**
  > AMQP protocal

  > 3.9 support stream

  - Virtual Host
    - Exchange
      - Queue
      > fanout/direct/topic/header/namesless

      > topic/routing_key (M to M) Queue


**Kafka**
  - topic
    - partition
    > partition is append only log

    > by default topic randomly send to partiition, can set to hash

    > order is garanty is partition level, not topic level

    > offset is partition level
> binary protocol over TCP

> kafka-python

> confluent-kafka-python

> Faust is a stream processing library

> zookeeper is complex, & able bring down server

https://www.rabbitmq.com/consumers.html#exclusivity