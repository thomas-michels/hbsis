
class Pessoa():

    def __init__(self):
        self.id = 0
        self.nome = ""
        self.id_endereco = 0

    def __str__(self):
        return f"{self.id};{self.nome};{self.id_endereco}"