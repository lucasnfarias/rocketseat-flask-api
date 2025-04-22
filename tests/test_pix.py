import sys
sys.path.append("../")

import pytest
import os
from src.interfaces.payments.pix import Pix

STATIC_PATH = os.path.abspath("../static")


def test_pix_create_payment():
  pix_instance = Pix()

  # create a payment
  payment_info = pix_instance.create_payment(base_dir=STATIC_PATH)

  assert "bank_payment_id" in payment_info
  assert "qr_code_path" in payment_info

  qr_code_path = payment_info["qr_code_path"]
  file_path = f"../static/img/{qr_code_path}.png"
  assert os.path.isfile(file_path)

  # remove test file
  os.remove(file_path)