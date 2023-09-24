from flask import Blueprint, jsonify

from models.EmpleadoModel import EmpleadoModel

main = Blueprint("empleado_blueprint", __name__)


@main.route('/')
def getEmpleados():
  try:
      empleados = EmpleadoModel.getEmpleados()
      return jsonify(empleados)
  except Exception as ex:
    return jsonify({"message": str(ex)}), 500 
  #return jsonify({"msg": "Probando"})
