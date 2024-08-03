import pika
import time
import random

def on_message_received(ch, method, properties, body):
  processing_time = random.randint(1,6)
  print(f"Nova mensagem recebida: {body}, irá levar {processing_time} segundos para processar")
  time.sleep(processing_time)
  ch.basic_ack(delivery_tag = method.delivery_tag)
  print("Mensagem processada")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue = 'letterbox')  

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue = 'letterbox', on_message_callback=on_message_received)

print("Consumindo")

channel.start_consuming()