import pika
def on_message_received(ch, method, properties, body):
    print(f'Recebeu uma nova mensagem: {body}')

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='secondexchange', exchange_type='fanout')

channel.queue_declare(queue='letterbox')

channel.queue_bind('letterbox', 'secondexchange')   #Faz um bind com o segundo exchange

channel.basic_consume(queue='letterbox', auto_ack=True,
    on_message_callback=on_message_received)

print("Consumindo")

channel.start_consuming()