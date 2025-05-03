import pika

def rabbitmq_callback(ch, method, properties, body):
  print(body)

class RabbitMQConsumer:
  def __init__(self):
    self.__host = "localhost"
    self.__port = 5672
    self.__username = "lfarias"
    self.__password = "lfarias"
    self.__queue = "my_queue"
    self.__channel = self.create_channel()

  def create_channel(self):
    connection_parameters = pika.ConnectionParameters(
      host=self.__host,
      port=self.__port,
      credentials=pika.PlainCredentials(
        username=self.__username,
        password=self.__password,
      )
    )

    channel = pika.BlockingConnection(connection_parameters).channel()
    channel.queue_declare(
      queue=self.__queue,
      durable=True
    )
    channel.basic_consume(
      queue=self.__queue,
      auto_ack=True,
      on_message_callback=rabbitmq_callback
    )

    return channel
  
  def start(self):
    print('System connected to RabbitMQ.')
    self.__channel.start_consuming()