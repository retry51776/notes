# Message Broker

> It's fast because zero‑copy uses the Linux system call `sendfile()` to directly transfer the OS cache into the NIC buffer; sequential I/O is append‑only.

> Improves decoupling, fault tolerance, and scalability.

- **Queue**: consumed once  
- **Pub/Sub**: can be consumed many times  

## Decision Pipeline

- Multiple messages in the same queue & engine vs. different queues with their own engines.

> From my experience, it takes about 3 minutes to publish 5,000 small messages.

### Protocols

- **AMQP**
  > Advanced Message Queuing Protocol; moves messages between applications.  
  > Pika is a Python implementation of AMQP 0.9.1.
- **MQTT**
- **STOMP**

---

## RabbitMQ
> Uses the AMQP protocol.  

> Version 3.9 adds stream support.

### Concepts
- **Virtual Host**
- **Exchange**
  - Types: `fanout`, `direct`, `topic`, `header`, nameless.
- **Queue**
  - Bindings such as `topic/routing_key` (many‑to‑many).

```python
def __process(ch, method, property, body):
    t = Thread(target=do_work)
    t.start()
    # method.message_count

conn.add_callback_threadsafe(ack_message)

ch.queue_declare(
    'xxx',
    durable=True,
    arguments={
        'x-delivery-limit': 3,
        'x-dead-letter-exchange': 'nnn',
        'x-dead-letter-routing-key': 'xxx',
    },
)
ch.queue_bind()
ch.basic_publish(
    exchange='xxx',
    routing_key='yyy',
    body=json.dumps({}),
    properties=pika.BasicProperties(delivery_mode=2)  # very slow
)
consumer_tag = ch.basic_consume('yyy', __process, auto_ack=False)
ch.confirm_delivery()
ch.basic_qos(prefetch_count=1)
ch.basic_cancel(consumer_tag)
ch.basic_ack(delivery_tag=method.delivery_tag)
ch.basic_get()
ch.queue_unbind()
ch.start_consuming()  # I forgot this
```

## Kafka
- **Topic**
  - **Partition** – an append‑only log.
    > By default, messages are distributed randomly across partitions; you can use a hash key to control placement.  
    > Ordering is guaranteed only at the partition level, not across the whole topic.  
    > Offsets are also per‑partition.

- `.avsc` files define schemas.  
- Uses a custom binary protocol over TCP.  

### Python Clients
- `kafka-python`
- `confluent-kafka-python`

### Stream Processing
- Faust is a stream‑processing library.

```python
class Order(faust.Record):
    sales_id: int
    sales_amt: float

@app.agent(app.topic('orders'), value_type=Order)
async def proc_order(orders: faust.Stream):
    async for order in orders:
        print(order.sales_id)
```

> Zookeeper is complex and can bring down the server if misconfigured.

[RabbitMQ consumer exclusivity documentation](https://www.rabbitmq.com/consumers.html#exclusivity)

### Java Example
```java
xxxStream.groupByKey()
    .aggregate(
        () -> 0.0,
        (key, order, total) -> total + order.getPrice(),
        Materialized.with(Serdes.String(), Serdes.Double())
    )
    .toStream()
    .to(xxxTopic, Produced.with(Serdes.String(), Serdes.Double()));
```

*Partition append‑only; ordering guaranteed only within a partition.*

Faust is a Robinhood‑style stream library for Python.

**Topic/routing key ↔ queue** is a many‑to‑many relationship.

---

## Site Reliability Engineering (SRE)

> Incremental aggregation functions include `count()`, `sum()`, `min()`, and `max()`.

