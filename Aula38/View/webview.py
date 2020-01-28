import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula38')
from Controller.squad_controller import SquadController
from Controller.sgbds_controller import SgbdsController
from Controller.backend_controller import BackendController
from Controller.frontend_controller import FrontendController
from flask import Flask, render_template, redirect, request
from Model.squad import Squad
from Model.sgbds import Sgbds
from Model.linguagem_back_end import LinguagemBackEnd
from Model.framework_front_end import FrameworkFrontEnd

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
    lista_bc = bc.listar_todos()
    lista_fc = fc.listar_todos()
    lista_sgbd = sg.listar_todos()

    if 'id' in request.args:
        id = request.args['id']
        squad = sc.buscar(id)


    return render_template('cadastrar.html', squad=squad, lista_bc=lista_bc, lista_fc=lista_fc, lista_sgbd=lista_sgbd)

@app.route('/cadastrar_bc')
def cadastrar_bc():
    classe = LinguagemBackEnd()
    caminho = '/salvar_bc'

    if 'id' in request.args:
        id = request.args['id']
        classe = bc.buscar(id)

    return render_template('cadastro2.html', classe=classe, caminho=caminho)

@app.route('/cadastrar_sgbds')
def cadastrar_sgbds():
    classe = Sgbds()
    caminho = '/salvar_sgbds'

    if 'id' in request.args:
        id = request.args['id']
        classe = sg.buscar(id)

    return render_template('cadastro2.html', classe=classe, caminho=caminho)

@app.route('/cadastrar_fc')
def cadastrar_fc():
    classe = FrameworkFrontEnd()
    caminho = '/salvar_fc'

    if 'id' in request.args:
        id = request.args['id']
        classe = fc.buscar(id)

    return render_template('cadastro2.html', classe=classe, caminho=caminho)

@app.route('/listar')
def listar():
    lista_squads = sc.listar_todos()
    return render_template('listar.html', lista_squads=lista_squads)

@app.route('/editar')
def editar():
    id = request.args['id']
    squad = sc.buscar(id)
    return render_template('/cadastrar', squad=squad)

@app.route('/editar_sg')
def editar_sg():
    id = request.args['id']
    caminho = '/salvar_sgbds'
    classe = sg.buscar(id)
    return render_template('cadastro2.html', classe=classe, caminho=caminho)

@app.route('/editar_bc')
def editar_bc():
    id = request.args['id']
    caminho = '/salvar_bc'
    classe = bc.buscar(id)
    return render_template('cadastro2.html', classe=classe, caminho=caminho)

@app.route('/editar_fc')
def editar_fc():
    id = request.args['id']
    caminho = '/salvar_fc'
    classe = fc.buscar(id)
    return render_template('cadastro2.html', classe=classe, caminho=caminho)

@app.route('/excluir')
def excluir():
    id = int(request.args['id'])
    sc.deletar(id)
    return redirect('/listar')

@app.route('/excluir_sg')
def excluir_sg():
    id = int(request.args['id'])
    sg.deletar(id)
    return redirect('/listar_sgbds')

@app.route('/excluir_fc')
def excluir_fc():
    id = int(request.args['id'])
    fc.deletar(id)
    return redirect('/listar_fc')

@app.route('/excluir_bc')
def excluir_bc():
    id = int(request.args['id'])
    bc.deletar(id)
    return redirect('/listar_bc')

@app.route('/salvar_bc', methods=['GET', 'POST'])
def salvar_bc():
    if request.method == 'POST':
        back = LinguagemBackEnd()
        back.nome = request.form['nome']

        try:
            back.id = int(request.form['id'])

        except ValueError:
            back.id = None

        if back.id == 0 or back.id is None:
            bc.adicionar(back)
        else:
            bc.alterar(back)

    return redirect('/listar_bc')

@app.route('/salvar_fc', methods=['GET', 'POST'])
def salvar_fc():
    if request.method == 'POST':
        back = FrameworkFrontEnd()
        back.nome = request.form['nome']

        try:
            back.id = int(request.form['id'])

        except ValueError:
            back.id = None

        if back.id == 0 or back.id is None:
            fc.adicionar(back)
        else:
            fc.alterar(back)

    return redirect('/listar_fc')

@app.route('/salvar_sgbds', methods=['GET', 'POST'])
def salvar_sgbds():
    if request.method == 'POST':
        sgbd = Sgbds()
        sgbd.nome = request.form['nome']

        try:
            sgbd.id = int(request.form['id'])

        except ValueError:
            sgbd.id = None

        if sgbd.id == 0 or sgbd.id is None:
            sg.adicionar(sgbd)
        else:
            sg.alterar(sgbd)

    return redirect('/listar_sgbds')

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
def listar_sgbds():
    lista = sg.listar_todos()
    caminho = "/cadastrar_sgbds"
    link1 = "/editar_sg"
    link2 = "/excluir_sg"
    nome_botao = "Cadastrar SGBD"
    return render_template('lista_ind.html', lista=lista, caminho=caminho, nome_botao=nome_botao, link1=link1, link2=link2)

@app.route('/listar_bc')
def listar_bc():
    lista = bc.listar_todos()
    caminho = "/cadastrar_bc"
    nome_botao = "Cadastrar BackEnd"
    link1 = "/editar_bc"
    link2 = "/excluir_bc"
    return render_template('lista_ind.html', lista=lista, caminho=caminho, nome_botao=nome_botao, link1=link1, link2=link2)

@app.route('/listar_fc')
def listar_fc():
    lista = fc.listar_todos()
    caminho = "/cadastrar_fc"
    nome_botao = "Cadastrar Framework"
    link1 = "/editar_fc"
    link2 = "/excluir_fc"
    return render_template('lista_ind.html', lista=lista, caminho=caminho, nome_botao=nome_botao, link1=link1, link2=link2)

app.run(debug=True)