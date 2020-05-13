import pika
from time import sleep
sleep(15)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq-server'))
channel = connection.channel()
channel.queue_declare(queue='orders')

def callback(ch, method, properties, body):
    print(" [x] Received order %r" % body)

channel.basic_consume(queue='orders', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for orders. To exit press CTRL+C')
channel.start_consuming()