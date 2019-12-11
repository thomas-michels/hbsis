# Aula 22 - 10-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)
# 5) Crie um metodo salvar que pegue os seguintes dados do cliente e salve em um arquivo. 
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# 6) crie um metodo que possa atualizar os dados do cliente (código cliente (inteiro), 
# nome, idade (inteiro), sexo, email, telefone). Este metodo deverá alterar tambem o dado bruto para
# que na hora de salvar o dado num arquivo, o mesmo não estaja desatualizado.

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

    def salvar(self, att):

        if att is False:
            arquivo = open("Aula24\\cadastro.txt", "a")
            arquivo.write(f'{self.codigo};{self.nome};{self.idade};{self.sexo};{self.email};{self.telefone}\n')
            arquivo.close()

        else:
            arquivo = open("Aula24\\cadastro.txt", "r")
            linhas = []
            cont = 0

            for linha_st in arquivo:
                linha = linha_st.strip().split(";")
                dados = {"codigo": linha[0], "nome": linha[1], "idade": linha[2], "sexo": linha[3], "email": linha[4], "telefone": linha[5]}
                linhas.append(dados)

            arquivo.close()
            
            arquivoWrite = open("Aula24\\cadastro.txt", "a")
            arquivoWrite.write("")

            for linha in linhas:
                conversor = f'{linha["codigo"]};{linha["nome"]};{linha["idade"]};{linha["sexo"]};{linha["email"]};{linha["telefone"]}\n'
                arquivoWrite.write(conversor)
                if (int(linha["codigo"]) == self.codigo):
                    conversor = f'{self.codigo};{self.nome};{self.idade};{self.sexo};{self.email};{self.telefone}\n'
                    arquivoWrite.write(conversor)
                
                cont += 1
            
            arquivoWrite.close()

    def atualizar(self, codigo, nome, idade, sexo, email, telefone):
        conversor = f'{codigo};{nome};{idade};{sexo};{email};{telefone}\n'
        self.setInformacao(conversor)
        self.salvar(True)

if __name__ == "__main__":

    def inputs():
        codigo = int(input("Codigo: "))
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        sexo = input("Sexo: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        return (codigo, nome, idade, sexo, email, telefone)

    dados = inputs()
    dadobruto = f'{dados[0]};{dados[1]};{dados[2]};{dados[3]};{dados[4]};{dados[5]}\n'
    pessoa = Pessoa()
    pessoa.setInformacao(dadobruto)
    pessoa.salvar(True)