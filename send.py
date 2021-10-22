import pika
import json
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

data = {'id': 1, 'name': 'test'}

for i in range(1,10):
    print(f"sending {i}...")    
    data['id'] = i
    channel.basic_publish(exchange='customer-created',
                        routing_key='billing-customer-data-create',
                        body=json.dumps(data)) 

    channel.basic_publish(exchange='customer-updated',
                        routing_key='billing-customer-data-update',
                        body=json.dumps(data)) 
    time.sleep(5)                        

print(f"[x] Sent data: {data}")
connection.close()