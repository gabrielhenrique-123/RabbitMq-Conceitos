import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body):
    print(f'Recebeu uma nova mensagem: {body}')

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare('headersexchange', exchange_type=ExchangeType.headers)

channel.queue_declare('letterbox')

bind_args = {
  'x-match': 'any',
  'name': 'brian',
  'age' : '47'
}

channel.queue_bind('letterbox', 'headersexchange', arguments=bind_args)

channel.basic_consume(queue='letterbox', auto_ack=True,
    on_message_callback=on_message_received)

print('Consumindo')

channel.start_consuming()