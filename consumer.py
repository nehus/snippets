import pika
import json
import config as cfg
import time

# Connect to RabbitMQ and create channel
connection = pika.BlockingConnection(pika.ConnectionParameters(host=cfg.RABBIT_HOST))
channel = connection.channel()
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()

# Declare and listen queue
channel.queue_declare(queue=cfg.QUEUE_TOPIC)#here we are creating the veiw

print(' [*] Waiting for messages. To exit press CTRL+C')

# Function process and print data
# def callback(ch, method, properties, body):
#     print("Method: {}".format(method))
#     print("Properties: {}".format(properties))

#     data = json.loads(body)
#     print("ID: {}".format(data['id']))
#     print("Name: {}".format(data['name']))
#     print('Description: {}'.format(data['description']))
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")

# Listen and receive data from queue
channel.basic_consume(callback, queue=cfg.QUEUE_TOPIC,no_ack=True)
channel.start_consuming()

