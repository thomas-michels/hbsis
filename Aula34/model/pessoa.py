import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula34')
from model.endereco import Endereco

class Pessoa:

    def __init__(self):
        self.id = 0
        self.nome = ''
        self.sobrenome = ''
        self.idade = 0
        self.endereco = Endereco()

    def __str__(self):
        return f'{self.id};{self.nome};{self.sobrenome};{self.idade};{self.endereco.id};{self.endereco.logradouro};{self.endereco.numero};{self.endereco.complemento};{self.endereco.bairro};{self.endereco.cidade};{self.endereco.cep}'