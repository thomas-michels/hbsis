
from Aula60.Model.Pessoa import Pessoa

class BaseLocal:

    def get_pessoas(self, pessoas) -> list:
        return pessoas

    def adicionar_pessoa(self, pessoa:Pessoa):
        self.pessoas.append(pessoa)

    def remover_pessoa(self, pessoa:Pessoa):
        self.pessoas.remove(pessoa)
