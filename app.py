from flask import Flask, request, jsonify
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from models.user import User
from models.payment import Payment
from repository.database import db
from flask_socketio import SocketIO
app = Flask(__name__)
# sqlite config
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@localhost:3306/flask_crud'

db.init_app(app)
socketio = SocketIO(app)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

# Routes
from routes.auth import *
from routes.payments import *

# Websockets
from websockets.events import *

if __name__ == '__main__':
      socketio.run(app, debug=True)
