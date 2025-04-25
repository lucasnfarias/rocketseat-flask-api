from pytest import raises

from src.interfaces.drivers.calculation_handler import CalculationHandlerInterface
from src.drivers.numpy_handler import NumpyHandler
from .calculator_3 import Calculator3
from typing import Dict, List

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

class MockCalculationErrorHandler:
  def variance(self, numbers: List[float]) -> float:
    return 3

class MockCalculationHandler:
  def variance(self, numbers: List[float]) -> float:
    return 1000000

def test_calculate():
  mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
  calculator_3 = Calculator3(MockCalculationHandler())

  response = calculator_3.calculate(mock_request)

  assert response == {'data': {
      'Calculator': 3,
      'value': 1000000,
      'Success': True,
      }
  }

def test_calculate_with_variance_error():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    calculator_3 = Calculator3(MockCalculationErrorHandler())

    with raises(Exception) as exc_info:
        calculator_3.calculate(mock_request)

    assert str(exc_info.value) == 'Process failed: variance is lower than multiplication.'

def test_calculate_integration():
  mock_request = MockRequest({
    "numbers": [1, 1, 1, 1, 100]
  })

  calculator_3 = Calculator3(NumpyHandler())
  response = calculator_3.calculate(mock_request)

  assert isinstance(response, dict)
  assert response == { 'data': { 'Calculator': 3, 'value': 1568.16, 'Success': True } }

def test_calculate_with_body_error_integration():
  mock_request = MockRequest(body={ "wrong": 1 })
  calculator_1 = Calculator3(NumpyHandler())

  with raises(Exception) as exc_info:
    calculator_1.calculate(mock_request)

  assert str(exc_info.value) == "Invalid fields."