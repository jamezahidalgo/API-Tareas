from databases.db import get_connection
from .entities.Tarea import Tarea

class TareaModel():
  @classmethod
  def getTareas(self):
    try:
        cx = get_connection()
        tareas = []
        with cx.cursor() as cursor:
          cursor.execute('SELECT numero_tarea, email_usuario, descripcion, finalizada FROM tarea ORDER BY email_usuario')
          resultset = cursor.fetchall()
          for row in resultset:
            tarea = Tarea(row[0], row[1], row[2], row[3])
            tareas.append(tarea.to_JSON())
          cx.close()
          return tareas
    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def getTareasByUsuario(self, user):
    try:
        cx = get_connection()
        tareas = []
        with cx.cursor() as cursor:
          cursor.execute('SELECT numero_tarea, descripcion, finalizada FROM tarea WHERE email_user = %s AND finalizada', (user,))
          resultset = cursor.fetchall()
          for row in resultset:
            tarea = Tarea(row[0], user, row[1], row[2])
            tareas.append(tarea.to_JSON())
        cx.close()
        return tareas
    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def add_tarea(self, tarea):
    try:
      cx = get_connection()
      with cx.cursor() as cursor:
          cursor.execute("INSERT INTO tarea(email_user, descripcion, finalizada) VALUES(%s, %s, %s )", (tarea.email_usuario, tarea.descripcion, False))
          affected_rows = cursor.rowcount
          cx.commit()
      cx.close()
      return affected_rows
    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def finish_task(self, tarea):
    try:
      cx = get_connection()
      with cx.cursor() as cursor:
          cursor.execute("UPDATE tarea SET finalizada = True WHERE email_user = %s AND numero_tarea = %s", (tarea.email_usuario, tarea.numero))
          affected_rows = cursor.rowcount
          cx.commit()
      cx.close()
      return affected_rows
    except Exception as ex:
      raise Exception(ex)    