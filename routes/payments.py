from app import app, db, User
from flask import request, jsonify
from flask_login import login_user, current_user, logout_user, login_required
import bcrypt

@app.route('/payments/pix', methods=["POST"])
def create_pix_payment():
  return jsonify({"message": "The PIX payment has been created."})

@app.route('/payments/pix/confirmation', methods=["POST"])
def pix_payment_confirmation():
  return jsonify({"message": "The PIX payment has been confirmed."})

@app.route('/payments/pix/<int:payment_id>', methods=["GET"])
def get_pix_payment_page(payment_id):
  return f'{payment_id}'