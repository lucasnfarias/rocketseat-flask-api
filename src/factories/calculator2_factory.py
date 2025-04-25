from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_2 import Calculator2

def calculator2_factory():
  calculation_handler = NumpyHandler()
  calc = Calculator2(calculation_handler)
  return calc