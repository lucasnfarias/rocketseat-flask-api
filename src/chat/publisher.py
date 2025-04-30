import pika
import json

class RabbitMQPublisher:
  def __init__(self):
    self.__host = "localhost"
    self.__port = 5672
    self.__username = "lfarias"
    self.__password = "lfarias"
    self.__exchange = "my_exchange"
    self.__routing_key = ""
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
    print(channel)
    return channel