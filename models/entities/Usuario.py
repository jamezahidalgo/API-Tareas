class Usuario():
  def __init__(self, email=None, password = None):
    self.email = email
    self.password = password

  def to_JSON(self):
    return {
            'email' : self.email,
            'password' : self.password
           }