import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


def callback_create(ch, method, properties, body):
    print(f"[x] [create] Received: {json.loads(body)}")

def callback_update(ch, method, properties, body):
    print(f"[x] [update] Received: {json.loads(body)}")


channel.basic_consume(queue='billing-customer-data-create', auto_ack=True, on_message_callback=callback_create)
channel.basic_consume(queue='billing-customer-data-update', auto_ack=True, on_message_callback=callback_update)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()