import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula38')
from DAO.frontend_db import FrontendDB
from Model.framework_front_end import FrameworkFrontEnd

class FrontendController():
    frontend_db = FrontendDB()

    def conversor(self, lista_tuplas):

        lista_frontends = []

        if type(lista_tuplas[0]) == tuple:
            for framework in lista_tuplas:
                frame = FrameworkFrontEnd()

                frame.id = framework[0]
                frame.nome = framework[1]

                lista_frontends.append(frame)

        else:
            frame = FrameworkFrontEnd()

            frame.id = lista_tuplas[0]
            frame.nome = lista_tuplas[1]
            lista_frontends = frame

        return lista_frontends

    def adicionar(self, frontend:FrameworkFrontEnd):
        nome = frontend.nome
        id = self.frontend_db.adicionar(nome)
        return id

    def deletar(self, id):
        self.frontend_db.deletar(id)

    def buscar(self, id):
        frontend = self.frontend_db.buscar(id)
        frontend_class = self.conversor(frontend)
        return frontend_class

    def alterar(self, frontend:FrameworkFrontEnd):
        id = frontend.id
        nome = frontend.nome

        self.frontend_db.alterar(id, nome)

    def listar_todos(self):

        lista_tuplas = self.frontend_db.listar_todos()
        objetosFrontend = self.conversor(lista_tuplas)

        return objetosFrontend

if __name__ == '__main__':
    fc = FrontendController()
    a = fc.listar_todos()
    for i in a:
        print(i)