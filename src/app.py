from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from user import Admin, User

app = Flask("app")
CORS(app)
"""
***************************
*  APIS PARA LOS USUARIOS:
***************************
"""
@app.route("/api/crear_usuario_nuevo", methods = ['POST'])
def crear_usuario():
    data = request.get_json()
    operator = Admin()
    result = operator.agg(dict(data))
    if result == 111:
        return Response(status=201)
    elif result == 456:
        return Response(status=456)
    elif result == 457:
        return Response(status=457)
    else:
        return Response(status=401)

"""
***************************
*  APIS PARA LAS RECETAS:
***************************
"""
@app.route("/api/obtener_receta", methods = ['POST'])
def obtener_receta_por_titulo():
    data = request.get_json()
    operator = User()
    result = operator.get_recipe(data['title'])
    if result is None:
        operator.db.close()
        return jsonify(None)
    claves = ("id", "titulo", "descripcion", "ingredientes", "pasos", "categoria", "id_usuario")
    result_json = dict(zip(claves, result))
    operator.db.close()
    return jsonify(result_json)

if __name__ == '__main__':
    app.run(debug=True)

