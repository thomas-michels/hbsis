

class Pessoa:

    def __init__(self, id, funcao):
        self.id = id
        self.funcao = funcao

    def __str__(self):
        return f"{self.id};{self.funcao}"