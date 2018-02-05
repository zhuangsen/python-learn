 #!/usr/bin/python
# -*- coding: UTF-8 -*-
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()
# 接下来我们创建名字为hello的queue：
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print("[x] Sent 'Hello World!'")

connection.close()
