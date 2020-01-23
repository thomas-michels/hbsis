import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula38')
from DAO.sgbds_db import SgbdsDB
from Model.sgbds import Sgbds

class SgbdsController():
    sgbds_db = SgbdsDB()

    def conversor(self, lista_tuplas):

        lista_sgbds = []

        if type(lista_tuplas[0]) == tuple:
            for sgbd_tuple in lista_tuplas:
                sgbd = Sgbds()

                sgbd.id = sgbd_tuple[0]
                sgbd.nome = sgbd_tuple[1]

                lista_sgbds.append(sgbd)

        else:
            sgbd = Sgbds()

            sgbd.id = lista_tuplas[0]
            sgbd.nome = lista_tuplas[1]
            lista_sgbds = sgbd

        return lista_sgbds

    def adicionar(self, sgbd:Sgbds):
        nome = sgbd.nome
        self.sgbds_db.adicionar(nome)

    def deletar(self, id):
        self.sgbds_db.deletar(id)

    def buscar(self, id):
        sgbd = self.sgbds_db.buscar(id)
        sgbd_class = self.conversor(sgbd)
        return sgbd_class

    def alterar(self, sgbd:Sgbds):
        id = sgbd.id
        nome = sgbd.nome

        self.frontend_db.alterar(id, nome)

    def listar_todos(self):

        lista_tuplas = self.sgbds_db.listar_todos()
        objetosSgbds = self.conversor(lista_tuplas)

        return objetosSgbds

if __name__ == '__main__':
    sc = SgbdsController()
    a = sc.listar_todos()
    for i in a:
        print(i)