from typing import List
import numpy

from src.interfaces.drivers.calculation_handler import CalculationHandlerInterface

class NumpyHandler(CalculationHandlerInterface):
  def __init__(self) -> None:
    self.__np = numpy

  def standard_deviation(self, numbers: List[float]) -> float:
      return self.__np.std(numbers)