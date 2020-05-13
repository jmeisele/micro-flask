import pika
from time import sleep
sleep(15)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq-server'))
channel = connection.channel()
channel.queue_declare(queue='orders')

exchange_name = 'product_order'
routing_key = 'product.order.build'
channel.queue_bind(exchange=exchange_name, queue='orders', routing_key=routing_key)

def callback(ch, method, properties, body):
    print(f"[x] Received order {body}")

channel.basic_consume(queue='orders', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for orders. To exit press CTRL+C')
channel.start_consuming()