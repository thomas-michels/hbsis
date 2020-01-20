import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula34')
from model.endereco import Endereco
from dao.endereco_db import EnderecoDb

class EnderecoController():
    e = Endereco()
    e_db = EnderecoDb()

    def listar_todos(self):
        return self.e_db.listar_todos()

    def adicionar(self, logradouro, numero, complemento, bairro, cidade, cep):
        self.e_db.adicionar(logradouro, numero, complemento, bairro, cidade, cep)

    def deletar(self, id):
        self.e_db.deletar(id)