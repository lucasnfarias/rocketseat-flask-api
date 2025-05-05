from src.chat.consumer import RabbitMQConsumer
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
  consumer = RabbitMQConsumer()
  consumer.start()