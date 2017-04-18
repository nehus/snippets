import pika
import json
import config as cfg
import sys

# Connect to RabbitMQ and create channel
connection = pika.BlockingConnection(pika.ConnectionParameters(host=cfg.RABBIT_HOST))
channel = connection.channel()

# Declare queue to send data
channel.queue_declare(queue=cfg.QUEUE_TOPIC)

data = {
        "id": 1,
        "name": "My Name",
        "description": "This is description about me"
    }
message = ' '.join(sys.argv[1:]) or "Hello World!"

# Send data
channel.basic_publish(exchange='',
                      routing_key=cfg.QUEUE_TOPIC,
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print(" [x] Sent %r" % message)
print(" [x] Sent data to RabbitMQ")
connection.close()



