from flask import Blueprint, jsonify, request

# Models
from models.TareaModel import TareaModel

# Entities
from models.entities.Tarea import Tarea

main = Blueprint("tarea_blueprint", __name__)

@main.route('/user', methods=['POST'])
def getTareas():
  try:
    #return jsonify({})
    user = request.json['email']
    print(user)
    tareas = TareaModel.getTareasByUsuario(user)
    return jsonify(tareas)
  except Exception as ex:
    return jsonify({"message": str(ex)}), 500

@main.route('/add', methods=['POST'])
def addTarea():
  try:
    email_user = request.json['email']
    descripcion = request.json['descripcion']    
    tarea = Tarea(usuario = email_user, descripcion = descripcion)
    if TareaModel.add_tarea(tarea) == 1:
      return jsonify(tarea.to_JSON())
    else:
      return jsonify({"message": "Error al agregar la tarea"}), 500  
  except Exception as ex:
    return jsonify({"message": str(ex)}), 500

@main.route('/terminar', methods=['PATCH'])
def marcarTarea():
  try:
    user = request.json['email']
    numero = request.json['numero']
    tarea = Tarea(numero = numero, usuario = user)
    if TareaModel.finish_task(tarea) == 1:
      return jsonify(tarea.to_JSON())
    else:
      return jsonify({"message": "Error al agregar la tarea"}), 500  
  except Exception as ex:
    return jsonify({"message": str(ex)}), 500