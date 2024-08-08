import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body):
    print(f"Second Consumer: recebeu uma mensagem: {body}")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

queue = channel.queue_declare(queue = '', exclusive=True)  #Escolhe aleatoriamente uma fila
#exclusive faz com que quando terminar, a fila é excluída

channel.queue_bind(exchange='pubsub', queue=queue.method.queue)    #Bind com exchange necessario para receber as mensagens

channel.basic_consume(queue = queue.method.queue, auto_ack=True, on_message_callback=on_message_received)

print("Consumindo")

channel.start_consuming()