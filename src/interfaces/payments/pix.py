import uuid
import qrcode
import os

STATIC_PATH = os.path.abspath("static")

class Pix:

    def __init__(self) -> None:
        pass

    def create_payment(self, base_dir=STATIC_PATH):
        bank_payment_id = str(uuid.uuid4())

        hash_payment = f'hash_payment_{bank_payment_id}'

        img = qrcode.make(hash_payment)

        img.save(f"{base_dir}/img/qr_code_payment_{bank_payment_id}.png")

        return {
          "bank_payment_id":  bank_payment_id,
          "qr_code_path": f"qr_code_payment_{bank_payment_id}",
        }