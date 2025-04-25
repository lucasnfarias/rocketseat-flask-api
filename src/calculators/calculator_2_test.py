from pytest import raises

from src.interfaces.drivers.calculation_handler import CalculationHandlerInterface
from src.drivers.numpy_handler import NumpyHandler
from .calculator_2 import Calculator2
from typing import Dict, List

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

class MockCalculationHandler:
  def standard_deviation(self, numbers: List[float]) -> float:
    return 3

def test_calculate():
  mock_request = MockRequest({
    "numbers": [2.12, 4.62, 1.32]
  })

  calculator_2 = Calculator2(MockCalculationHandler())
  response = calculator_2.calculate(mock_request)

  assert isinstance(response, dict)
  assert response == { 'data': { 'Calculator': 2, 'result': 0.33 } }

def test_calculate_integration():
  mock_request = MockRequest({
    "numbers": [2.12, 4.62, 1.32]
  })

  calculator_2 = Calculator2(NumpyHandler())
  response = calculator_2.calculate(mock_request)

  assert isinstance(response, dict)
  assert response == { 'data': { 'Calculator': 2, 'result': 0.08 } }

def test_calculate_with_body_error_integration():
  mock_request = MockRequest(body={ "wrong": 1 })
  calculator_1 = Calculator2(NumpyHandler())

  with raises(Exception) as exc_info:
    calculator_1.calculate(mock_request)

  assert str(exc_info.value) == "Invalid fields."