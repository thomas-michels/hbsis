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
    #
    # def criar(self, id, nome, sobrenome, idade, endereco_logradouro, endereco_numero, endereco_complemento, endereco_bairro, endereco_cidade, endereco_cep, enderco_id=None):
    #     self.id = id
    #     self.nome = nome
    #     self.idade = idade
    #     self.sobrenome = sobrenome
    #     self.endereco.logradouro = endereco_logradouro
    #     self.endereco.numero = endereco_numero


    def exportar_txt(self, lista_pessoas):
        # ----- Cria um arquivo e atribui a uma variável 'arquivo'
        with open('33-Aula33/Aula33-4/pessoas4.txt', 'a') as arquivo:
            # ---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
            for p in lista_pessoas:
                arquivo.write(f"{str(p)}\n")

    def __str__(self):
        return f'{self.id};{self.nome};{self.sobrenome};{self.idade};{self.endereco.id};{self.endereco.logradouro};{self.endereco.numero};{self.endereco.complemento};{self.endereco.bairro};{self.endereco.cidade};{self.endereco.cep}'