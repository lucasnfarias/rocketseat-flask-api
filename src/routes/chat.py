from flask import Blueprint, request, jsonify
from src.chat.publisher import RabbitMQPublisher

chat_route_bp = Blueprint("chat_routes", __name__)

@chat_route_bp.route('/chat/telegram/send-message', methods=["POST"])
def send_telegram_message():
  data = request.get_json()

  if 'message' not in data:
    return jsonify({"message": "Invalid message"}), 400
  
  publisher = RabbitMQPublisher()
  publisher.send_message({ "msg": data["message"] })

  return jsonify({
    "message": "Message sent.",
  })