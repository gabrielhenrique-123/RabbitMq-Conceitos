import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare('headersexchange', ExchangeType.headers)

message = 'Essa mensagem usa Headers Exchange'

channel.basic_publish(
    exchange='headersexchange', 
    routing_key='',   #Não é necessário Headers Exchange
    body=message, 
    properties=pika.BasicProperties(headers={'name': 'brian'}))

print(f'sent message: {message}')

connection.close()