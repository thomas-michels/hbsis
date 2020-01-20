import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula34')
from model.pessoa import Pessoa
from dao.pessoa_db import PessoaDb

class PessoaController:
    p = Pessoa()
    p_db = PessoaDb()

    def listar_todos(self):
        return self.p_db.listar_todos()

    def adicionar(self, nome, sobrenome, idade, id_endereco="NULL"):
        self.p_db.adicionar(nome, sobrenome, idade, id_endereco)

    def deletar(self, id_pessoa):
        self.p_db.deletar(id_pessoa)
