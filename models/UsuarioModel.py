from databases.db import get_connection
from .entities.Usuario import Usuario

import bcrypt

class UsuarioModel():
  @classmethod
  def getUsuarios(self):
    try:
        cx = get_connection()
        usuarios = []
        with cx.cursor() as cursor:
          cursor.execute('SELECT email, password FROM usuario ORDER BY email')
          resultset = cursor.fetchall()
          for row in resultset:
            usuario = Usuario(row[0], row[1])
            usuarios.append(usuario.to_JSON())
          cx.close()
          return usuarios
    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def getUsuario(self, email):
    try:
        cx = get_connection()
    
        with cx.cursor() as cursor:
          cursor.execute('SELECT email, password FROM usuario WHERE email = %s', (email,))
          row = cursor.fetchone()
          usuario = None
          if row != None:
            usuario = Usuario(row[0], row[1])
            usuario = usuario.to_JSON()
          cx.close()
          return usuario
    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def add_user(self, user):
    try:
      cx = get_connection()
      with cx.cursor() as cursor:
        enc_pwd = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt(10))
        print(enc_pwd)
        print(enc_pwd.decode())
        #print(enc_pwd.encode("utf-8"))
        cursor.execute("INSERT INTO usuario VALUES(%s, %s)", (user.email, enc_pwd.decode(),))
        affected_rows = cursor.rowcount
        cx.commit()
      cx.close()
      return affected_rows
    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def login(self, user):
    try:
      cx = get_connection()
      
      with cx.cursor() as cursor:
        cursor.execute("SELECT password FROM usuario WHERE email = %s", (user.email,)) 
        if cursor.rowcount == 1:
          row = cursor.fetchone()
          # Hashing the password
          #hash = row[0].encode() # bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt(10))
          #print(row[0].encode('utf-8'))
          #print(hash)
          print(bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt(10)))
          print(row[0].encode("utf-8"))
          print(bcrypt.checkpw(row[0].decode(), bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt(10))))
        
          #pwd = password.encode('utf8'), user['password'].encode('utf8')
          #pwd = bcrypt.checkpw(row[0].encode('utf-8'), hash)   
          # bcrypt.checkpw(password,getpwd)
          pwd =  True
        else:
          pwd = False
      cx.close()
      return pwd
    except Exception as ex:
      raise Exception(ex)    
