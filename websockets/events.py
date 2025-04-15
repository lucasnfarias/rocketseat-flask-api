from app import socketio

@socketio.on('connect')
def handle_connect():
  print("Client connected.")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected.")