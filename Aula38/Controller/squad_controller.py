import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula38')
from Model.squad import Squad
from Model.linguagem_back_end import LinguagemBackEnd
from Model.framework_front_end import FrameworkFrontEnd
from Model.sgbds import Sgbds
from DAO.squad_db import SquadDB
from Controller.backend_controller import BackendController
from Controller.frontend_controller import FrontendController
from Controller.sgbds_controller import SgbdsController

class SquadController():
    squad_db = SquadDB()
    backend_c = BackendController()
    frontend_c = FrontendController()
    sgbds_c = SgbdsController()

    def conversor(self, lista_tuplas):

        lista_squads = []
        try:
            if not lista_tuplas.nome:
                pass
            else:
                return lista_tuplas
            
        except AttributeError:
            if type(lista_tuplas[0]) == tuple:
                for equipe in lista_tuplas:
                    equip = Squad()
                    equip.id = equipe[0]
                    equip.nome = equipe[1]
                    equip.descricao = equipe[2]
                    equip.numeroPessoas = equipe[3]

                    equip.sgbds.id = equipe[7]
                    equip.sgbds.nome = equipe[8]
                    equip.linguagemBackEnd.id = equipe[9]
                    equip.linguagemBackEnd.nome = equipe[10]
                    equip.frameworkFrontEnd.id = equipe[11]
                    equip.frameworkFrontEnd.nome = equipe[12]

                    lista_squads.append(equip)
                return lista_squads

            else:
                equip = Squad()
                equip.id = lista_tuplas[0]
                equip.nome = lista_tuplas[1]
                equip.descricao = lista_tuplas[2]
                equip.numeroPessoas = lista_tuplas[3]

                equip.sgbds.id = lista_tuplas[7]
                equip.sgbds.nome = lista_tuplas[8]
                equip.linguagemBackEnd.id = lista_tuplas[9]
                equip.linguagemBackEnd.nome = lista_tuplas[10]
                equip.frameworkFrontEnd.id = lista_tuplas[11]
                equip.frameworkFrontEnd.nome = lista_tuplas[12]
                lista_squads = equip
                return lista_squads

    def adicionar(self, squad:Squad):

        backend = LinguagemBackEnd()
        backend.nome = squad.linguagemBackEnd.nome
        if squad.linguagemBackEnd.id == 0 or squad.linguagemBackEnd.id is None:
            squad.linguagemBackEnd.id = self.backend_c.adicionar(backend)

        else:
            backend_class = self.backend_c.buscar(squad.linguagemBackEnd.id)
            squad.linguagemBackEnd.nome = backend_class.nome

        frontend = FrameworkFrontEnd()
        frontend.nome = squad.frameworkFrontEnd.nome
        if squad.frameworkFrontEnd.id == 0 or squad.frameworkFrontEnd.id is None:
            squad.frameworkFrontEnd.id = self.frontend_c.adicionar(frontend)

        else:
            frontend_class = self.frontend_c.buscar(squad.frameworkFrontEnd.id)
            squad.frameworkFrontEnd.nome = frontend_class.nome

        sgbds = Sgbds()
        sgbds.nome = squad.sgbds.nome
        if squad.sgbds.id == 0 or squad.sgbds.id is None:
            squad.sgbds.id = self.sgbds_c.adicionar(sgbds)

        else:
            sgbds_class = self.sgbds_c.buscar(squad.sgbds.id)
            squad.sgbds.nome = sgbds_class.nome

        nome = squad.nome
        descricao = squad.descricao
        numeroPessoas = squad.numeroPessoas
        linguagemBackEnd = int(squad.linguagemBackEnd.id)
        frameworkFrontEnd = int(squad.frameworkFrontEnd.id)
        sgbd = int(squad.sgbds.id)

        self.squad_db.adicionar(nome, descricao, numeroPessoas, linguagemBackEnd, frameworkFrontEnd, sgbd)

    def deletar(self, id):
        self.squad_db.deletar(id)

    def buscar(self, id):
        squad_tuple = self.squad_db.buscar(id)
        squad = Squad()
        squad.id = squad_tuple[0]
        squad.nome = squad_tuple[1]
        squad.descricao = squad_tuple[2]
        squad.numeroPessoas = squad_tuple[3]
        squad.linguagemBackEnd.id = squad_tuple[4]
        squad.frameworkFrontEnd.id = squad_tuple[5]
        squad.sgbds.id = squad_tuple[6]

        id_frontend = squad.frameworkFrontEnd.id
        squad.frameworkFrontEnd = self.frontend_c.buscar(id_frontend)

        id_backend = squad.linguagemBackEnd.id
        squad.linguagemBackEnd = self.backend_c.buscar(id_backend)

        id_sgbd = squad.sgbds.id
        squad.sgbds = self.sgbds_c.buscar(id_sgbd)

        squad_class = self.conversor(squad)
        return squad_class

    def alterar(self, squad:Squad):

        backend = LinguagemBackEnd()
        backend.nome = squad.linguagemBackEnd.nome
        backend.id = squad.linguagemBackEnd.id

        if backend.nome == "":
            backend_class = self.backend_c.buscar(backend.id)
            backend.nome = backend_class.nome

        self.backend_c.alterar(backend)

        frontend = FrameworkFrontEnd()
        frontend.nome = squad.frameworkFrontEnd.nome
        frontend.id = squad.frameworkFrontEnd.id

        if frontend.nome == "":
            frontend_class = self.frontend_c.buscar(squad.frameworkFrontEnd.id)
            frontend.nome = frontend_class.nome

        self.frontend_c.alterar(frontend)

        sgbds = Sgbds()
        sgbds.nome = squad.sgbds.nome
        sgbds.id = squad.sgbds.id

        if sgbds.nome == "":
            sgbds_class = self.sgbds_c.buscar(squad.sgbds.id)
            sgbds.nome = sgbds_class.nome

        self.sgbds_c.alterar(sgbds)

        id = squad.id
        nome = squad.nome
        descricao = squad.descricao
        numeroPessoas = squad.numeroPessoas

        self.squad_db.alterar(id, nome, descricao, numeroPessoas, backend.id, frontend.id, sgbds.id)

    def listar_todos(self):

        lista_tuplas = self.squad_db.listar_todos()
        objetoSquad = self.conversor(lista_tuplas)

        return objetoSquad

if __name__ == '__main__':
    sc = SquadController()
    squad = Squad()
    squad.id = 8
    squad.nome = "TESTE alterar console"
    squad.descricao = "TESTE CONSOLE"
    squad.numeroPessoas = 5
    squad.linguagemBackEnd.id = 1
    squad.frameworkFrontEnd.id = 2
    squad.sgbds.id = 1
    #sc.alterar(squad)
    #sc.deletar(10)
    b = sc.buscar(5)
    print(b)
    a = sc.listar_todos()
    for i in a:
        print(i)