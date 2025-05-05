from src.chat.consumer import RabbitMQConsumer
from dotenv import load_dotenv


if __name__ == '__main__':
  load_dotenv()

  consumer = RabbitMQConsumer()
  consumer.start()