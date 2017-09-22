#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print('[*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print("[x] Received %r" % (body,))
    # time.sleep(body.count('.'))
    print("[x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()


# python new_task.py First message.
# python new_task.py Second message..
# python new_task.py Third message...
# python new_task.py Fourth message....
# python new_task.py Fifth message.....