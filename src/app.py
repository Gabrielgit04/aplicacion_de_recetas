import ast

from flask import Flask, request, jsonify, Response, render_template
from flask_cors import CORS
from user import Admin, User

app = Flask("app")
CORS(app)
"""
***************************
*  TEMPLATES RENDER:
***************************
"""

@app.route("/", methods = ['GET'])
def index():
    return render_template("index.html")

@app.route("/login", methods = ['GET'])
def inicio_sesion():
    return render_template("login.html")

@app.route("/register", methods = ['GET'])
def registrarse():
    return render_template("register.html")

@app.route("/contacto", methods = ['GET'])
def contacto():
    return render_template("contact.html")

@app.route("/principal", methods = ['GET'])
def principal():
    return render_template("principal.html")

@app.route("/resultado_busqueda", methods = ['GET'])
def tequeno():
    return render_template("tequenos.html")

@app.route("/resultado_busqueda", methods = ['GET'])
def arepa():
    return render_template("arepa.html")

@app.route("/resultado_busqueda", methods = ['GET'])
def bandeja():
    return render_template("bandeja.html")

@app.route("/resultado_busqueda", methods = ['GET'])
def empanada():
    return render_template("empanadas.html")

@app.route("/receta_detallado", methods = ['GET'])
def recipe():
    return render_template("plantilla_receta.html")

@app.route("/plantilla-iframe", methods = ['GET'])
def iframe():
    return render_template("plantilla_iframe.html")

@app.route("/profile", methods = ['GET'])
def perfil():
    return render_template("perfil_usuario.html")

# validate js
@app.route('/js-validation')
def principal_dialog():
    return render_template('public/js/principalViewFunction.js')

@app.route('/js-validation-inputs')
def validate_inputs():
    return render_template('public/js/validation.js')



"""
***************************
*  APIS PARA LOS USUARIOS:
***************************
"""

@app.route("/api/crear_usuario_nuevo", methods = ['POST'])
def crear_usuario():
    data = {
        "user" : request.form["username"],
        "email": request.form["adreess"],
        "passw": request.form["password"],
    }
    operator = Admin()
    result = operator.agg(dict(data))
    if result == 111:
        return render_template("login.html")
    elif result == 456:
        return render_template("register.html", error="Nombre de Usuario ya existente")
    elif result == 457:
        return render_template("register.html", error="Correo ya registrado en la plataforma")
    else:
        print("error")
        return Response(status=401)

@app.route('/api/verificar_usuario', methods = ['POST'])
def verificar_usuario():
    operator = Admin()
    user = request.form["username"]
    passw = request.form["password"]
    if operator.verific_user(user, passw):
        return render_template("principal.html")
    else:
        return render_template('login.html', error="Credenciales incorrectas")
"""
***************************
*  APIS PARA LAS RECETAS:
***************************
"""

@app.route("/api/obtener_receta", methods = ['POST'])
def obtener_receta_por_titulo():
    titulo = request.form["search"]
    operator = User()
    result = operator.get_recipe(titulo)
    if result is None:
        operator.db.close()
        return jsonify(None)
    claves = ("id", "titulo", "descripcion", "ingredientes", "pasos", "categoria", "id_usuario")
    result_json = [dict(zip(claves, elementos)) for elementos in result]
    operator.db.close()
    return render_template("search.html", numero_recetas = len(result_json),
                           dicc_recetas = result_json)

@app.route("/api/mostrar_receta", methods = ['POST'])
def mostrar():
    data = request.form["datos"]
    return render_template("plantilla_receta.html", data= ast.literal_eval(data))

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(e)
    app.run(host='0.0.0.0',port=5000)


