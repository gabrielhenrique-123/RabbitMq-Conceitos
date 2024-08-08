import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange = 'routing', exchange_type=ExchangeType.direct)

message = "Essa mensagem precisa ser roteada"

channel.basic_publish(exchange = 'routing', routing_key='both', body=message)   #Routing key aqui define qual consumidor vai receber

print(f"Enviou uma mensagem: {message}")

connection.close