import pika
from pika.exchange_type import ExchangeType

#Pub Sub
#Não é necessário de declarar filas, os próprios consumidores resolvem isso
#Responsavel apenas por publicar
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

message = "O Pub Sub funciona"

channel.basic_publish(exchange = 'pubsub', routing_key='', body=message)

print(f"Mensagem enviada: {message}")

connection.close