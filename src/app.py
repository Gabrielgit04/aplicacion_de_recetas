import ast
from flask_cors import CORS
from user import Admin, User
from flask import Flask, request, jsonify, Response, render_template, session

app = Flask("app")
app.secret_key = "aaasssddd"
CORS(app)
"""
***************************
*  TEMPLATES RENDER:
***************************
"""
global informacion
global lista_recetas
@app.route("/", methods = ['GET'])
def index():
    iniciador = Admin()
    iniciador.db_init()
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
    return render_template("principal.html", datos_usuario=session["usuario"], dicc_recetas=obtener_recetas())

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
    operator = User()
    user = request.form["username"]
    passw = request.form["password"]
    informacion = operator.verific_user(user, passw)
    lista_recetas = obtener_recetas()
    if informacion:
        session["usuario"] = informacion
        return render_template("principal.html", datos_usuario=informacion, dicc_recetas=lista_recetas)
    else:
        return render_template('login.html', error="Credenciales incorrectas")
"""
***************************
*  APIS PARA LAS RECETAS:
***************************
"""

@app.route("/api/crear_receta_nueva", methods = ['POST'])
def crear_receta():
    # si alguien lee esto: perdi 30 minutos arreglando este error y porque la solucion fue incoherente y no entendible
    # le puse asi, no se que causaba el error pero haciendolo asi funciono. Si funciona no le muevas
    incoherencias = dict(request.form)
    data = {
        "title" : request.form["nombre"],
        "descripcion": request.form["descripcion"],
        "ingredients": request.form["ingredientes"],
        "steps": request.form["instrucciones"],
        "category": incoherencias['categoria'],
        "id_user": incoherencias["name_user"]
    }
    operator = User()
    result = operator.agg(data)
    if result:
        return render_template("principal.html", datos_usuario=session["usuario"], dicc_recetas=obtener_recetas())
    else:
        print("no se creo")

@app.route("/api/obtener_receta", methods = ['POST'])
def obtener_receta_por_titulo():
    global result
    elemento_a_buscar = request.form["search"]
    operator = User()
    indices = ["title", "id_user"]
    for indice in indices:
        result = operator.get_recipe(indice, elemento_a_buscar)
        print("INDICE:", indice)
        print("RESULTADO: ", result)
        if result is None and indice == "id_user":
            operator.db.close()
            return render_template("search.html")
        if result:
            break
    claves = ("id", "titulo", "descripcion", "ingredientes", "pasos", "categoria", "id_usuario")
    result_json = [dict(zip(claves, elementos)) for elementos in result]
    operator.db.close()
    return render_template("search.html", numero_recetas=len(result_json), dicc_recetas=result_json)

@app.route("/api/mostrar_receta", methods = ['POST'])
def mostrar():
    data = request.form["datos"]
    return render_template("plantilla_receta.html", data= ast.literal_eval(data))

@app.route('/api/mostrar_todas_recetas', methods = ['GET'])
def obtener_recetas():
    operator = User()
    elementos = operator.get_all()
    claves = ("id", "titulo", "descripcion", "ingredientes", "pasos", "categoria", "id_usuario")
    result_json = [dict(zip(claves, elementos)) for elementos in elementos]
    operator.db.close()
    return result_json
"""
***************************
*  FUNCIONES:
***************************
"""



if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(e)
    app.run(host='0.0.0.0',port=5000)


