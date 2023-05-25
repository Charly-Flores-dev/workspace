from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'hola mundo'

@app.route('/lala/<usuario>')
def lala(usuario):
    return'lala' + usuario

@app.route('/lele')
def lele():
    return'lele'
