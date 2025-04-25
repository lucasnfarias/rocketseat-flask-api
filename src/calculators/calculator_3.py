from flask import request as FlaskRequest
from typing import Dict, List

from src.interfaces.drivers.calculation_handler import CalculationHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_bad_request import HttpBadRequestError

class Calculator3:

  def __init__(self, calculation_handler: CalculationHandlerInterface) -> None:
    self.__calculation_handler = calculation_handler

  def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
    body = request.json
    input_data = self.__validate_body(body)

    variance = self.__calculate_variance(input_data)
    multiplication = self.__calculate_multiplication(input_data)
    self.__verify_results(variance, multiplication)
    formatted_response = self.__format_response(variance)

    return formatted_response

  def __validate_body(self, body: Dict) -> List[float]:
    if "numbers" not in body:
      raise HttpUnprocessableEntityError("Invalid fields.")

    input_data = body["numbers"]
    return input_data

  def __calculate_variance(self, numbers: List[float]) -> float:
    variance = self.__calculation_handler.variance(numbers)
    return variance

  def __calculate_multiplication(self, numbers: List[float]) -> float:
    multiplication = 1

    for num in numbers:
      multiplication *= num

    return multiplication

  def __verify_results(self, variance: float, multiplication: float) -> None:
    if variance < multiplication:
      raise HttpBadRequestError('Process failed: variance is lower than multiplication.')

  def __format_response(self, variance: float) -> Dict:
    return {
      "data": {
        "Calculator": 3,
        "value": variance,
        "Success": True,
      }
    }