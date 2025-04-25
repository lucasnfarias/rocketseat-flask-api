from pytest import raises

from src.drivers.numpy_handler import NumpyHandler
from .calculator_2 import Calculator2
from typing import Dict

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

def test_calculate():
  mock_request = MockRequest({
    "numbers": [2.12, 4.62, 1.32]
  })

  calculator_2 = Calculator2(NumpyHandler())
  response = calculator_2.calculate(mock_request)

  assert isinstance(response, dict)
  assert response == { 'data': { 'Calculator': 2, 'result': 0.08 } }


def test_calculate_with_body_error():
  mock_request = MockRequest(body={ "wrong": 1 })
  calculator_1 = Calculator2(NumpyHandler())

  with raises(Exception) as exc_info:
    calculator_1.calculate(mock_request)

  assert str(exc_info.value) == "Invalid fields."