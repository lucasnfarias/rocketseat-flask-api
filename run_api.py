import os
from src.server.server import socketio, app
from dotenv import load_dotenv

if __name__ == '__main__':
  load_dotenv()
  host=os.getenv("SERVER_HOST")
  port=os.getenv("SERVER_PORT")

  socketio.run(app, host=host, port=port, debug=True)
