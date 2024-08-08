import pika

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='firstexchange', exchange_type='direct')

channel.exchange_declare(exchange='secondexchange', exchange_type='fanout')

channel.exchange_bind('secondexchange', 'firstexchange')  #Bind de um excchange com outro

message = "Essa mensagem passa por multiplos exchange"

channel.basic_publish(exchange='firstexchange', routing_key='', body=message) #Mensagem foi publicada apenas 

print(f"Mensagem enviada: {message}")

connection.close()