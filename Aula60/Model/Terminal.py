
from Aula60.Model.Base_local import BaseLocal


class Terminal(BaseLocal):

    __pessoas = ['piloto', 'oficial1', 'oficial2', 'chefe de servico',
                 'comissario1', 'comissario2', 'policial', 'presidiario']

    def __init__(self):
        super().__init__(self.__pessoas)

    def get_pessoas(self) -> list:
        return super().get_pessoas(self.__pessoas)

    def __str__(self):
        return 'Terminal'