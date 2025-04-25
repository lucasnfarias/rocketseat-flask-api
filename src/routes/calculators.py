from flask import Blueprint, jsonify, request

from src.errors.error_handler import error_handler
from src.factories.calculator1_factory import calculator1_factory
from src.factories.calculator2_factory import calculator2_factory
from src.factories.calculator3_factory import calculator3_factory

calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculators/1", methods=["GET"])
def calculator_1():
  try:
    calc = calculator1_factory()
    response = calc.calculate(request)

    return jsonify(response)
  except Exception as exception:
    error_response = error_handler(exception)
    return jsonify(error_response["body"]), error_response["status_code"]

@calc_route_bp.route("/calculators/2", methods=["GET"])
def calculator_2():
  try:
    calc = calculator2_factory()
    response = calc.calculate(request)

    return jsonify(response)
  except Exception as exception:
    error_response = error_handler(exception)
    return jsonify(error_response["body"]), error_response["status_code"]

@calc_route_bp.route("/calculators/3", methods=["GET"])
def calculator_3():
  try:
    calc = calculator3_factory()
    response = calc.calculate(request)

    return jsonify(response)
  except Exception as exception:
    error_response = error_handler(exception)
    return jsonify(error_response["body"]), error_response["status_code"]