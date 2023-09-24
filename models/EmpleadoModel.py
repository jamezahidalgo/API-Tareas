from databases.db import get_connection
from .entities.Empleado import Empleado

class EmpleadoModel():
  @classmethod
  def getEmpleados(self):
    try:
        cx = get_connection()
        empleados = []
        with cx.cursor() as cursor:
          cursor.execute('SELECT id, nombre, email FROM empleado ORDER BY nombre')
          resultset = cursor.fetchall()
          for row in resultset:
            empleado = Empleado(row[0], row[1], row[1])
            empleados.append(empleado.to_JSON())
          cx.close()
          return empleados
    except Exception as ex:
      raise Exception(ex)
"""

  def getEmpleado(self, id):
      try:
          cx = get_connection()
          cursor = cx.cursor()
          cursor.execute("SELECT nombre, email FROM empleado WHERE id")
          cx.close()
          return empleado
      except Exception as ex:
        raise Exception(ex)  
"""        