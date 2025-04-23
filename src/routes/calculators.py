from flask import Blueprint, jsonify, request

from src.calculators.calculator_1 import Calculator1

calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculators/1", methods=["GET"])
def calculator_1():
  calc = Calculator1()
  response = calc.calculate(request)

  return jsonify(response)