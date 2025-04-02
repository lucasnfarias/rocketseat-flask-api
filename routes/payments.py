from app import app, db, Payment
from flask import request, jsonify
from datetime import datetime, timedelta

@app.route('/payments/pix', methods=["POST"])
def create_pix_payment():
  data = request.get_json()

  if 'value' not in data:
    return jsonify({"message": "Invalid value"}), 400
  
  expiration_date = datetime.now() + timedelta(minutes=30)

  new_payment = Payment(value=data['value'], expiration_date=expiration_date)
  
  db.session.add(new_payment)
  db.session.commit()

  return jsonify({
    "message": "The PIX payment has been created.",
    "payment": new_payment.to_dict()
  })

@app.route('/payments/pix/confirmation', methods=["POST"])
def pix_payment_confirmation():
  return jsonify({"message": "The PIX payment has been confirmed."})

@app.route('/payments/pix/<int:payment_id>', methods=["GET"])
def get_pix_payment_page(payment_id):
  return f'{payment_id}'