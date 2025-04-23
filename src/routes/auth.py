from src.server.server import app, db
from src.models.user import User
from flask import request, jsonify, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
import bcrypt

auth_route_bp = Blueprint("auth_routes", __name__)

@auth_route_bp.route('/login', methods=["POST"])
def login():
  data = request.json
  username = data.get("username")
  password = data.get("password")

  if username and password:
    user = User.query.filter_by(username=username).first()

    if user and bcrypt.checkpw(str.encode(password), str.encode(user.password)):
      login_user(user)
      return jsonify({"message": "Successfully authenticated."})

  return jsonify({"message": "Invalid credentials."}), 401

@auth_route_bp.route('/logout', methods=["GET"])
@login_required
def logout():
  logout_user()

  return jsonify({"message": "Successful logout."})

@auth_route_bp.route('/users', methods=["POST"])
def create_user():
  data = request.json
  username = data.get("username")
  password = data.get("password")

  if username and password:
    hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
    user = User(username=username, password=hashed_password, role='user')

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User successfully created."})

  return jsonify({"message": "Invalid fields."}), 400

@auth_route_bp.route('/users/<int:user_id>', methods=["GET"])
@login_required
def read_user(user_id):
  user = User.query.get(user_id)

  if user:
      return {"username": user.username}

  return jsonify({"message": "User not found."}), 404

@auth_route_bp.route('/users/<int:user_id>', methods=["PUT"])
@login_required
def update_user(user_id):
  data = request.json

  if user_id != current_user.id and current_user.role == "user":
    return jsonify({"message": f"You are not allowed to update another user: {user_id}"}), 403

  if not data.get("password"):
    return jsonify({"message": "Password field not found."}), 400

  user = User.query.get(user_id)

  if user:
      user.password = data.get("password")
      db.session.commit()

      return jsonify({"message": f"User {user_id} updated successfully."})

  return jsonify({"message": "User not found."}), 404

@auth_route_bp.route('/users/<int:user_id>', methods=["DELETE"])
@login_required
def delete_user(user_id):
  if current_user.role != "admin":
    return jsonify({"message": "You are not allowed to delete users"}), 403

  if user_id == current_user.id:
    return jsonify({"message": f"Cannot delete yourself: {user_id}"}), 400

  user = User.query.get(user_id)

  if user:
      db.session.delete(user)
      db.session.commit()

      return jsonify({"message": f"User {user_id} deleted successfully."})

  return jsonify({"message": "User not found."}), 404