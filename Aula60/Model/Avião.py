
from Aula60.Model.Base_local import BaseLocal

class Aviao(BaseLocal):

    pessoas = []

    def get_pessoas(self):
        return super().get_pessoas(self.pessoas)