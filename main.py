from flask import Flask

from routes import Usuario, Tarea

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask!'


# Blueprint
#app.register_blueprint(Empleado.main, url_prefix='/api/empleados')
app.register_blueprint(Usuario.main, url_prefix='/api/usuarios')
app.register_blueprint(Tarea.main, url_prefix='/api/tareas')
app.run(host='0.0.0.0', port=81)
