from flask import Blueprint, jsonify, request

from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_2 import Calculator2
from src.calculators.calculator_1 import Calculator1

calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculators/1", methods=["GET"])
def calculator_1():
  calc = Calculator1()
  response = calc.calculate(request)

  return jsonify(response)

@calc_route_bp.route("/calculators/2", methods=["GET"])
def calculator_2():
  calc = Calculator2(NumpyHandler())
  response = calc.calculate(request)

  return jsonify(response)