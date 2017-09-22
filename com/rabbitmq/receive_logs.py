#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare('logs', 'fanout')

# 报错：TypeError: exchange_declare() got an unexpected keyword argument 'type'
# channel.exchange_declare(exchange='logs', type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print('[*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print("[x] %r" % (body,))


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
