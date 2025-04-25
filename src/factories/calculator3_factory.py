from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_3 import Calculator3

def calculator3_factory():
  calculation_handler = NumpyHandler()
  calc = Calculator3(calculation_handler)
  return calc