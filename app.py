from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

# consumiendo apis de las vistas

# home view
@app.route('/')
def index():
    return render_template('index.html')

# inicio sesion
@app.route('/iniciar')
def inicio_sesion():
    return render_template('login.html')

# registro view
@app.route('/registro')
def registrarse():
    return render_template('register.html')

# contacto view
@app.route('/contact')
def contacto():
    return render_template('contact.html')
# principal view
@app.route('/principal')
def principal():
    return render_template('principal.html')

# plantilla receta view
@app.route('/template-recipe')
def recipe():
    return render_template('plantilla_receta.html')

# search view
@app.route('/search')
def search():
    return render_template('search.html')




# recetas por default folder
# |
    # arepa view

@app.route('/arepa')
def arepa():
    return render_template('templates-default/arepa.html')

    # bandeja paisa view
@app.route('/bandeja')
def bandeja():
    return render_template('templates-default/bandeja.html')

    # empanadas argentinas view
@app.route('/empanadas')
def empanada():
    return render_template('templates-default/empanadas.html')

    # tequenos view
@app.route('/tequenos')
def tequeno():
    return render_template('templates-default/tequenos.html')
    # hasta aca las views de la carpeta template-recipe
    


# hasta aca se consumen las apis de las vistas

# cosumiendo apis de las validaciones
    # |
    # public/js folder
        # |
            # validations with js

@app.route('/js-validation')
def principal_dialog():
    return render_template('public/js/principalViewFunction.js')

@app.route('/js-validation-inputs')
def validate_inputs():
    return render_template('public/js/validation.js')





if __name__ == '__main__' :
    app.run(debug= True)



