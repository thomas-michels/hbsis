import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula37')
from Controller.squad_controller import SquadController
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
sc = SquadController()

@app.route('/')
def inicio():
    return render_template('home.html')

@app.route('/listar')
def listar():
    return ''

app.run(debug=True)