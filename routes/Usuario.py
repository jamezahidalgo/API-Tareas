from flask import Blueprint, jsonify, request

# Models
from models.UsuarioModel import UsuarioModel

# Entities
from models.entities.Usuario import Usuario

main = Blueprint("usuario_blueprint", __name__)

@main.route('/')
def getUsuarios():
  try:
      usuarios = UsuarioModel.getUsuarios()
      return jsonify(usuarios)
  except Exception as ex:
    return jsonify({"message": str(ex)}), 500

@main.route('/:id')
def getUsuario(id):
  try:
      usuario = UsuarioModel.getUsuario(id)
      return jsonify(usuario)
  except Exception as ex:
    return jsonify({"message": str(ex)}), 500


@main.route('/add', methods=['POST'])
def addUsuario():
  try:
      print(request.json)
      email = request.json['email']
      password = request.json['password']
      #encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
      #enc_pwd = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
          
      user = Usuario(email, password)
      
      affected_rows = UsuarioModel.add_user(user)      
      if affected_rows == 1:
        return jsonify(user.email)
      else:
        print("Error")
        return jsonify({"message": "Error en insert"}), 500
      
  except Exception as ex:
    return jsonify({"message": str(ex)}), 500
  
@main.route('/login', methods=['POST'])
def login():
  try:
    print(request.json)
    email = request.json['email']
    password = request.json['password']
    
    user = Usuario(email, password)
      
    if UsuarioModel.login(user):
      return jsonify({"message" : "Login success"})
    else:      
      return jsonify({"message": "Email y/o password incorrectos"}), 500
      
  except Exception as ex:
    return jsonify({"message": str(ex)}), 500    