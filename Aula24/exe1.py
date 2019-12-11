# Aula 22 - 10-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)

class Pessoa():

    def __init__(self, codigo = int, nome = None, idade = int, sexo = None, email = None, telefone = None):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.email = email
        self.telefone = telefone

    def setInformacao(self, dadoBruto):
        dado = dadoBruto.strip().split(';')
        self.codigo = int(dado[0])
        self.nome = dado[1]
        self.idade = int(dado[2])
        self.sexo = dado[3]
        self.email = dado[4]
        self.telefone = dado[5]

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

pessoa = Pessoa()
pessoa.setInformacao(dadobruto)
print(pessoa.codigo)
print(pessoa.nome)
print(pessoa.idade)
print(pessoa.sexo)
print(pessoa.email)
print(pessoa.telefone)