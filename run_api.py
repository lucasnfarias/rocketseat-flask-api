from src.server.server import socketio, app
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
  socketio.run(app, host="0.0.0.0", port=5000, debug=True)
