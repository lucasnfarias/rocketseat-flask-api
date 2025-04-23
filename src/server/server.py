from flask import Flask
from flask_login import LoginManager
from src.repository.database import db
from src.models.user import User
from flask_socketio import SocketIO

app = Flask(__name__,
            template_folder='../../templates',
            static_url_path='',
            static_folder='../../static',)

# sqlite config
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@localhost:3306/flask_crud'

db.init_app(app)
socketio = SocketIO(app)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'auth_routes.login'

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

# Routes
from src.routes.auth import auth_route_bp
app.register_blueprint(auth_route_bp)

from src.routes.calculators import calc_route_bp
app.register_blueprint(calc_route_bp)

from src.routes.payments import payments_route_bp
app.register_blueprint(payments_route_bp)

# Websockets
from src.websockets.events import *
