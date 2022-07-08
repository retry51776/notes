# Message Broker

> Improves decoupling, fault tolerance, scalability

> Queue : consumed once

> Pub Sub: consumed many time

> Decision Pipeline

> multi message same queue & engine VS different queue w its engine
### Protocal
- AMQP
  > Adcanced Message Queuing Protocol, move message between applications.
  
  > Pika is python implelemntation AMQP 0.9.1
- MQTT
- STOMP

---

# RabbitMQ
  > AMQP protocal

  > 3.9 support stream

  - Virtual Host
    - Exchange
      - Queue
      > fanout/direct/topic/header/namesless

      > topic/routing_key (M to M) Queue

```
def __process(ch, method, property, body):
    t = Thread(target=do_work)
    t.start()
    //method.message_count

conn.add_callback_threadsafe(ack_message)
ch.queue_declare('xxx', durable=True)
ch.queue_bind()
ch.basic_publish(
    exchange='xxx',
    routing_key='yyy',
    body=json.dumps({}),
    properties=pika.BasicProperties(delivery_mode=2) # very slow
)
consumer_tag = ch.basic_consume('yyy', __process, auto_ack=False)
ch.confirm_delivery()
ch.basic_qos(prefetch_count=1)
ch.basic_cancel(consumer_tag)
ch.basic_ack(delivery_tag=method.delivery_tag)
ch.basic_get()
ch.queue_unbind()
ch.start_consuming() # I forgets this
```

# Kafka
  - topic
    - partition
    > partition is append only log

    > by default topic randomly send to partiition, can set to hash

    > order is garanty is partition level, not topic level

    > offset is partition level

> .avsc is schema file

> custom binary protocol over TCP

> kafka-python

> confluent-kafka-python

> Faust is a stream processing library
```
class Order(faust.Record):
    sales_id: int
    sales_amt: double

@app.agent(app.topic('orders'), value_type=Order)
async def proc_order(orders: faust.Stream):
    async for order in orders:
        print(order.sales_id)
```


> zookeeper is complex, & able bring down server

https://www.rabbitmq.com/consumers.html#exclusivity

queue.method.message_count
## Java
```
xxxStream.groupByKey().aggregate(() -> 0.0,
    (key, order, total) -> total + order.getPrice(),
    Materialized.with(Serdes.String(), Serdes.Double()))
    .toStream()
    .to(xxxTopic, Produced.with(Serdes.String(), Serdes.Double()))
```

partition append-only 
order only guarantee in partition

Faust is Robinhood stream python library

topic/routing key & queue is m to m relationship

Site Reliable Engineer (SRE)

"incremental" aggregation functions include `count()`, `sum()`, `min()`, and `max()`