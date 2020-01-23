import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula37')
from Controller.squad_controller import SquadController
from flask import Flask, redirect, render_template, request
from Model.squad import Squad

app = Flask(__name__)
sc = SquadController()

@app.route('/')
def inicio():
    return render_template('home.html')

@app.route('/listar')
def listar():
    lista_squads = sc.listar_todos()
    return render_template('listar.html', lista_squads=lista_squads)

@app.route('/editar')
def editar():
    id = request.args['id']
    squad = sc.buscar(id)
    return render_template('/cadastrar', squad=squad)

@app.route('/excluir')
def excluir():
    id = int(request.args['id'])
    sc.deletar(id)
    return redirect('/listar')

@app.route('/cadastrar')
def cadastrar():
    squad = Squad()

    if 'id' in request.args:
        squad.id = request.args['id']

    return render_template('cadastrar.html', squad=squad)

@app.route('/salvar', methods=['GET', 'POST'])
def salvar():
    if request.method == 'POST':
        squad = Squad()
        squad.id = int(request.form['id'])
        squad.nome = request.form['nome']
        squad.descricao = request.form['descricao']
        squad.numeroPessoas = int(request.form['numeroPessoas'])
        squad.linguagemBackEnd = request.form['linguagemBackEnd']
        squad.frameworkFrontEnd = request.form['frameworkFrontEnd']

    if squad.id == 0:
        sc.adicionar(squad)
    else:
        sc.alterar(squad)

    return redirect('/listar')

app.run(debug=True)