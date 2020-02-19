
from Aula60.Model.Base_local import BaseLocal

class Terminal(BaseLocal):

    pessoas = []

    def get_pessoas(self) -> list:
        return super().get_pessoas(self.pessoas)
