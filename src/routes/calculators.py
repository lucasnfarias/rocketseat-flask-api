from flask import Blueprint, jsonify, request

from src.factories.calculator1_factory import calculator1_factory
from src.factories.calculator2_factory import calculator2_factory
from src.calculators.calculator_1 import Calculator1

calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculators/1", methods=["GET"])
def calculator_1():
  calc = calculator1_factory()
  response = calc.calculate(request)

  return jsonify(response)

@calc_route_bp.route("/calculators/2", methods=["GET"])
def calculator_2():
  calc = calculator2_factory()
  response = calc.calculate(request)

  return jsonify(response)