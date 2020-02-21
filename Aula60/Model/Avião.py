
from Aula60.Model.Base_local import BaseLocal


class Aviao(BaseLocal):

    __pessoas = []

    def __init__(self):
        super().__init__(self.__pessoas)

    def get_pessoas(self):
        return super().get_pessoas()

    def __str__(self):
        return "Aviao"