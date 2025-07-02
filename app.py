from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/iniciar')
def inicio_sesion():
    return render_template('login.html')

@app.route('/registro')
def registrarse():
    return render_template('register.html')

@app.route('/contact')
def contacto():
    return render_template('contact.html')



if __name__ == '__main__' :
    app.run(debug= True)



