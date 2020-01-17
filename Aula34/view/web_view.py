from flask import Flask, render_template, redirect, request
import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula34')
from Controller.pessoa_controller import PessoaController
from Controller.endereco_controller import EnderecoController

app = Flask(__name__)
pc = PessoaController()
ec = EnderecoController()

@app.route('/')
def inicio():
    return render_template('index1.html')

@app.route('/listar')
def listar():
    pessoas = pc.listar_todos()
    return render_template('index.html', lista=pessoas)

@app.route('/endereco')
def listar_end():
    enderecos = ec.listar_todos()
    return render_template('index2.html', lista=enderecos)

@app.route('/cadastro', methods=['GET', 'POST'])
def adicionar_pessoa():
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        idade = int(request.form['idade'])
        id_endereco = int(request.form['id_endereco'])
        pc.adicionar(nome, sobrenome, idade, id_endereco)
        return redirect('/')

    return render_template('cadastro.html')

@app.route('/cadastro-endereco', methods=['GET', 'POST'])
def adicionar_endereco():
    if request.method == 'POST':
        logradouro = request.form['logradouro']
        numero = int(request.form['numero'])
        complemento = request.form['complemento']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        cep = request.form['cep']
        ec.adicionar(logradouro, numero, complemento, bairro, cidade, cep)
        return redirect('/')

    return render_template('cadastro_end.html')

@app.route('/deletar-pessoa', methods=['GET', 'POST'])
def deletar_pessoa():
    if request.method == 'POST':
        id = request.form['id']
        pc.deletar(id)
        return redirect('/')

    return render_template('deletar.html', caminho="/deletar-pessoa")

@app.route('/deletar-endereco', methods=['GET', 'POST'])
def deletar_endereco():
    if request.method == 'POST':
        id = request.form['id']
        ec.deletar(id)
        return redirect('/')

    return render_template('deletar.html', caminho="/deletar-endereco")

app.run(debug=True)