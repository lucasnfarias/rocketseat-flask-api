import pika
import json
import os

class RabbitMQPublisher:
  def __init__(self):
    self.__host = os.getenv("RABBIT_MQ_HOST")
    self.__port = os.getenv("RABBIT_MQ_PORT")
    self.__username = os.getenv("RABBIT_MQ_USERNAME")
    self.__password = os.getenv("RABBIT_MQ_PASSWORD")
    self.__exchange = os.getenv("RABBIT_MQ_EXCHANGE")
    self.__routing_key = os.getenv("RABBIT_MQ_ROUTING_KEY")
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
    return channel

  def send_message(self, body: dict):
    self.__channel.basic_publish(
      exchange=self.__exchange,
      routing_key=self.__routing_key,
      body=json.dumps(body),
      properties=pika.BasicProperties(
          delivery_mode=2
      )
    )
