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

queue.method.message_count

# Kafka

partition append-only 
order only guarantee in partition

Faust is Robinhood stream python library

topic/routing key & queue is m to m relationship

Site Reliable Engineer (SRE)