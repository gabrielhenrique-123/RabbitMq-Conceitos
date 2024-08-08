import pika

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue = 'letterbox')  

message = "Ola consumidor"

channel.basic_publish(exchange = '', routing_key='letterbox', body=message)

print(f"Enviou a mensagem: {message}")

connection.close