class Menu():

    def __init__(self):
        self.__menu = """
===================================
1 - Sortear Aluno
2 - Lista de Alunos
3 - Sair
===================================
Insira uma opcao: """

    def getMenu(self):
        retorno = self.__menu
        return retorno