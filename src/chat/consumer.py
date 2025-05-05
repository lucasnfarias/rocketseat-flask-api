import os
import pika

from src.chat.callback import rabbitmq_callback

class RabbitMQConsumer:
  def __init__(self):
    self.__host = os.getenv("RABBIT_MQ_HOST")
    self.__port = os.getenv("RABBIT_MQ_PORT")
    self.__username = os.getenv("RABBIT_MQ_USERNAME")
    self.__password = os.getenv("RABBIT_MQ_PASSWORD")
    self.__queue = os.getenv("RABBIT_MQ_QUEUE")
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
