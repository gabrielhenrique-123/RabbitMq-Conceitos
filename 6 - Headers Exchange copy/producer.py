import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare('headersexchange', exchange_type=ExchangeType.headers)

message = "Essa mensagem usa Headers Exchange"

# Enviando a mensagem com os cabeçalhos corretos para correspondência
channel.basic_publish(
    exchange='headersexchange', 
    routing_key='',  # Não é necessário com headers exchange
    body=message, 
    properties=pika.BasicProperties(headers={'name': 'brian'}))

print(f'Enviou uma mensagem: {message}') 

connection.close()
