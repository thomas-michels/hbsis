import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula38')
from DAO.backend_db import BackendDB
from Model.linguagem_back_end import LinguagemBackEnd

class BackendController():
    backend_db = BackendDB()

    def conversor(self, lista_tuplas):

        lista_backends = []

        if type(lista_tuplas[0]) == tuple:
            for linguagem in lista_tuplas:
                lingua = LinguagemBackEnd()

                lingua.id = linguagem[0]
                lingua.nome = linguagem[1]

                lista_backends.append(lingua)

        else:
            lingua = LinguagemBackEnd()

            lingua.id = lista_tuplas[0]
            lingua.nome = lista_tuplas[1]
            lista_backends = lingua

        return lista_backends

    def adicionar(self, backend:LinguagemBackEnd):
        nome = backend.nome
        self.backend_db.adicionar(nome)

    def deletar(self, id):
        self.backend_db.deletar(id)

    def buscar(self, id):
        backend = self.backend_db.buscar(id)
        backend_class = self.conversor(backend)
        return backend_class

    def alterar(self, backend:LinguagemBackEnd):
        id = backend.id
        nome = backend.nome

        self.backend_db.alterar(id, nome)

    def listar_todos(self):

        lista_tuplas = self.backend_db.listar_todos()
        objetosBackend = self.conversor(lista_tuplas)

        return objetosBackend

if __name__ == '__main__':
    bc = BackendController()
    a = bc.listar_todos()
    for i in a:
        print(i)