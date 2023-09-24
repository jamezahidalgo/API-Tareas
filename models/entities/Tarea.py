class Tarea():
  def __init__(self, numero = None, usuario = None, descripcion = None, finalizada = False):
    self.numero = numero
    self.email_usuario = usuario
    self.descripcion = descripcion
    self.finalizada = finalizada

  def to_JSON(self):
    return {
            'email_usuario' : self.email_usuario,
            'descripcion' : self.descripcion,
            'estado' : ("Terminada" if self.finalizada else "Pendiente")
           }