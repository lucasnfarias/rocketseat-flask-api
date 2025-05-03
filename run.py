from src.chat.consumer import RabbitMQConsumer
from src.server.server import socketio, app


if __name__ == '__main__':
  consumer = RabbitMQConsumer()
  consumer.start()

  socketio.run(app, host="0.0.0.0", port=5000, debug=True)
