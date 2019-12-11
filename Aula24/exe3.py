# Aula 22 - 10-12-2019
# # Como Tratar e Trabalhar Erros!!!

# Dica: O mais importante é conseguir fazer! Não importa como chegou ao resultado e sim o resultado!

# Dica2: na função .open() você pode escolher entre 'r' para ler, 'w' para sobrescrever e criar um 
# arquivo novo ou o 'a' que é abreveativo de append, onde ele inclui linha no final do arquivo.
# Você sabia que o 'r', 'w' e o 'a' são string que podem ser passadas via variável exemplo:

# atributo = 'r'
# nome_arquivo = 'cadastro'
# arquivo.open(f'exercicio/{nome_arquivo}.txt',atributo)



# 1) Crie uma classe cadastro.
# Esta classe deve abrir o arquivo cadastro2.txt e guardar os cadastro numa lista com dicionários.

# 2) crie o metodo salvar os dados dos clientes em um arquivo txt.
# 3) crie um metodo para cadastrar novos clientes. O código cliente é unico por pessoa, sendo assim não pode 
# se repetir.
# 3) Crie um metodo de consulta de cliente, mostrando os dados dele na tela.
# 4) Crie um metodo para atualizar o cadastro de um cliente qualquer pelo codigo cliente.
# Após atualizar, salvar todos no arquivo "cadastro_atualizado.txt" (use o 'w' para sobrescrever o arquivo.)
#
#  Observação: Use o try/filnaly para abrir e fechar os arquivos. Veja na aula 21- Ecessões como é!

class Cliente():
    codigo = 0

    def __init__(self, nome = None, idade = int, sexo = None, email = None, telefone = None):
        self.codigo += 1
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.email = email
        self.telefone = telefone

    def setInformacao(self, dadoBruto):

        dado = dadoBruto.strip().split(';')
        self.nome = dado[0]
        self.idade = int(dado[1])
        self.sexo = dado[2]
        self.email = dado[3]
        self.telefone = dado[4]

    def salvar(self, att):

        if att is False:
            arquivo = open("Aula24\\cadastro.txt", "a")
            arquivo.write(f'{self.codigo};{self.nome};{self.idade};{self.sexo};{self.email};{self.telefone}\n')
            arquivo.close()

        else:
            try:
                arquivo = open("Aula24\\cadastro.txt", "r")
                linhas = []
                cont = 0

                for linha_st in arquivo:
                    linha = linha_st.strip().split(";")
                    dados = {"codigo": linha[0], "nome": linha[1], "idade": linha[2], "sexo": linha[3], "email": linha[4], "telefone": linha[5]}
                    linhas.append(dados)

            except FileNotFoundError:
                print("Arquivo Não Encontrado")

            finally:
                arquivo.close()
            
            arquivoWrite = open("Aula24\\cadastro.txt", "w")

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
    cliente = Cliente()
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    dado = f'{nome};{idade};{sexo};{email};{telefone}'
    cliente.setInformacao(dado)
    cliente.salvar(False)
    