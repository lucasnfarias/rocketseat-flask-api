from typing import Dict, List
from flask import request as FlaskRequest

from src.interfaces.drivers.calculation_handler import CalculationHandlerInterface
from src.drivers.numpy_handler import NumpyHandler

class Calculator2:
  def __init__(self, calculation_handler: CalculationHandlerInterface) -> None:
    self.__calculation_handler = calculation_handler

  def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
    body = request.json
    input_data = self.__validate_body(body)

    calculated_number = self.__process_data(input_data)
    formatted_response = self.__format_response(calculated_number)

    return formatted_response

  def __validate_body(self, body: Dict) -> List[float]:
    if "numbers" not in body:
      raise Exception("Invalid fields.")

    input_data = body["numbers"]
    return input_data
  
  def __process_data(self, input_data: List[float]) -> float:
    first_process_result = [(num * 11) ** 0.95 for num in input_data]
    result = self.__calculation_handler.standard_deviation(first_process_result)

    return 1 / result

  def __format_response(self, calculated_number: float) -> Dict:
    return {
      "data": {
        "Calculator": 2,
        "result": round(calculated_number, 2)
      }
    }