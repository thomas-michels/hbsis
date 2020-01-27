import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula38')
from Controller.squad_controller import SquadController
from Controller.sgbds_controller import SgbdsController
from Controller.backend_controller import BackendController
from Controller.frontend_controller import FrontendController
from flask import Flask, render_template, redirect, request
from Model.squad import Squad

app = Flask(__name__)
sc = SquadController()
sg = SgbdsController()
bc = BackendController()
fc = FrontendController()

@app.route('/')
def inicio():
    return render_template('home.html')

@app.route('/cadastrar')
def cadastrar():
    squad = Squad()

    if 'id' in request.args:
        squad.id = request.args['id']

    return render_template('cadastrar.html', squad=squad)

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

@app.route('/salvar', methods=['GET', 'POST'])
def salvar():
    if request.method == 'POST':
        squad = Squad()
        squad.id = int(request.form['id'])
        squad.nome = request.form['nome']
        squad.descricao = request.form['descricao']
        squad.numeroPessoas = int(request.form['numeroPessoas'])

        try:
            squad.linguagemBackEnd.id = int(request.form['id_linguagemBackEnd'])
        except ValueError:
            squad.linguagemBackEnd.id = None
        
        squad.linguagemBackEnd.nome = request.form['nome_linguagemBackEnd']
        
        try:
            squad.frameworkFrontEnd.id = int(request.form['id_frameworkFrontEnd'])
        except ValueError:
            squad.frameworkFrontEnd.id = None

        squad.frameworkFrontEnd.nome = request.form['nome_frameworkFrontEnd']
        
        try:
            squad.sgbds.id = int(request.form['id_sgbds'])
        except ValueError:
            squad.sgbds.id = None

        squad.sgbds.nome = request.form['nome_sgbds']

    if squad.id == 0 or squad.id is None:
        sc.adicionar(squad)
    else:
        sc.alterar(squad)

    return redirect('/listar')

@app.route('/listar_sgbds')
def listar_lgbds():
    lista = sg.listar_todos()
    return render_template('lista_ind.html', lista=lista)

@app.route('/listar_bc')
def listar_bc():
    lista = bc.listar_todos()
    return render_template('lista_ind.html', lista=lista)

@app.route('/listar_fc')
def listar_fc():
    lista = fc.listar_todos()
    return render_template('lista_ind.html', lista=lista)
app.run(debug=True)