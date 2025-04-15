from flask import request, jsonify, send_file, render_template
from app import app, db, Payment
from datetime import datetime, timedelta
from interfaces.payments.pix import Pix

@app.route('/payments/pix', methods=["POST"])
def create_pix_payment():
  data = request.get_json()

  if 'value' not in data:
    return jsonify({"message": "Invalid value"}), 400
  
  expiration_date = datetime.now() + timedelta(minutes=30)

  new_payment = Payment(value=data['value'], expiration_date=expiration_date)
  
  pix_obj = Pix()

  data_payment_pix = pix_obj.create_payment()

  new_payment.bank_payment_id = data_payment_pix["bank_payment_id"]
  new_payment.qr_code = data_payment_pix["qr_code_path"]

  db.session.add(new_payment)
  db.session.commit()

  return jsonify({
    "message": "The PIX payment has been created.",
    "payment": new_payment.to_dict()
  })

@app.route('/payments/pix/qr_code/<file_name>', methods=['GET'])
def get_image(file_name):
    return send_file(f"static/img/{file_name}.png", mimetype='image/png')

@app.route('/payments/pix/confirmation', methods=["POST"])
def pix_payment_confirmation():
  return jsonify({"message": "The PIX payment has been confirmed."})

@app.route('/payments/pix/<int:payment_id>', methods=["GET"])
def get_pix_payment_page(payment_id):
  payment = Payment.query.get(payment_id)

  return render_template(
    'payment.html',
    payment_id=payment.id,
    value=payment.value,
    host="http://localhost:5000",
    qr_code=payment.qr_code
  )
