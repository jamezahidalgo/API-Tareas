import psycopg2
from psycopg2 import DatabaseError
import os

def get_connection():
  try:

    # Obtiene el string de conexión desde la variable de entorno
    cx_string = os.environ["CONNECTION_URL"]
    # Se conecta al servidor usando en string de conexión
    cx = psycopg2.connect(dsn = cx_string)
    return cx
  except DatabaseError as ex:
    raise ex
  #return os.environ("CONNECTION_URL")
