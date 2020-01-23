import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula37')
from Model.squad import Squad
from DAO.squad_db import SquadDB

class SquadController():
    squad_db = SquadDB()

    def conversor(self, lista_tuplas):

        lista_squads = []

        if type(lista_tuplas[0]) == tuple:
            for equipe in lista_tuplas:
                equip = Squad()
                equip.id = equipe[0]
                equip.nome = equipe[1]
                equip.descricao = equipe[2]
                equip.numeroPessoas = equipe[3]
                equip.linguaguemBackEnd = equipe[4]
                equip.frameworkFrontEnd = equipe[5]
                lista_squads.append(equip)

        else:
            equip = Squad()
            equip.id = lista_tuplas[0]
            equip.nome = lista_tuplas[1]
            equip.descricao = lista_tuplas[2]
            equip.numeroPessoas = lista_tuplas[3]
            equip.linguaguemBackEnd = lista_tuplas[4]
            equip.frameworkFrontEnd = lista_tuplas[5]
            lista_squads = equip

        return lista_squads

    def adicionar(self, squad:Squad):
        nome = squad.nome
        descricao = squad.descricao
        numeroPessoas = squad.numeroPessoas
        linguagemBackEnd = squad.linguagemBackEnd
        frameworkFrontEnd = squad.frameworkFrontEnd
        self.squad_db.adicionar(nome, descricao, numeroPessoas, linguagemBackEnd, frameworkFrontEnd)

    def deletar(self, id):
        self.squad_db.deletar(id)

    def buscar(self, id):
        squad = self.squad_db.buscar(id)
        squad_class = self.conversor(squad)
        return squad_class

    def alterar(self, squad:Squad):
        id = squad.id
        nome = squad.nome
        descricao = squad.descricao
        numeroPessoas = squad.numeroPessoas
        linguagemBackEnd = squad.linguagemBackEnd
        frameworkFrontEnd = squad.frameworkFrontEnd
        self.squad_db.alterar(id, nome, descricao, numeroPessoas, linguagemBackEnd, frameworkFrontEnd)

    def listar_todos(self):

        lista_tuplas = self.squad_db.listar_todos()
        objetoSquad = self.conversor(lista_tuplas)

        return objetoSquad