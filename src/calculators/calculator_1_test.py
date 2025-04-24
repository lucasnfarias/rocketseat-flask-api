from typing import Dict

from pytest import raises
from .calculator_1 import Calculator1

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

def test_calculate():
  mock_request = MockRequest(body={ "number": 1 })
  calculator_1 = Calculator1()

  response = calculator_1.calculate(mock_request)

  assert "data" in response
  assert "Calculator" in response["data"]
  assert "result" in response["data"]

  assert response["data"]["Calculator"] == 1
  assert response["data"]["result"] == 14.25

def test_calculate_with_body_error():
  mock_request = MockRequest(body={ "wrong": 1 })
  calculator_1 = Calculator1()

  with raises(Exception) as exc_info:
    calculator_1.calculate(mock_request)

  assert str(exc_info.value) == "Invalid fields."