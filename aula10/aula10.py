from flask import Flask, render_template, request
from operacoes import *

title = "Calculadora"

app = Flask(__name__)

@app.route('/')

def home():
    return render_template("home.html", titulo=title)

@app.route('/calcular')

def calcular():
    num1 = float(request.args["num1"])
    num2 = float(request.args["num2"])
    soma = somar(num1, num2)
    sub = subtrair(num1, num2)
    mult = multiplicar(num1, num2)
    div = dividir(num1, num2)
    div_int = dividir_int(num1, num2)
    raiz1 = raiz(num1, num2)
    resto = resto_div(num1, num2)

    return render_template("calcular.html", num1 = num1, num2 = num2, soma = soma, sub = sub, mult = mult, div = div, div_int = div_int, raiz = raiz1, resto = resto)

app.run(debug=True)