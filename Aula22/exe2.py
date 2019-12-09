# Aula 21 - 09-12-2019

# Crie uma classe cliente:

# 1) deve ter como atributos: codigo, cpf, nome, idade, sexo

# 2) como metodos: receber salario, comprar, pagar divida

# Quando recebe aumenta o dinheiro na carteira.

# quando compra aumenta os bens e diminui o dinheiro na carteira

# Se comprar e não tiver dinheiro o suficiente deve diminuir o dinheiro da carteira
# e aumentar a divida.

# Para pagar a divida tem que ter dinheiro o suficiente na carteira

# 3) atributos de estado: dinheiro na carteira, divida, bens

class Cliente():

    def __init__(self, codigo, cpf, nome, idade, sexo):
        self.codigo = codigo
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

        self.dinheiro = 0
        self.bens = 0
        self.divida = 0

    def receber_salario(self, salario):
        self.dinheiro += salario

    def comprar(self, valor_compra):
        if (self.dinheiro - valor_compra) < 0:
            divida = valor_compra - self.dinheiro
            self.bens += valor_compra
            self.dinheiro = 0
            self.divida += divida

        else:
            self.dinheiro -= valor_compra
            self.bens += valor_compra

    def pagar(self):
        if self.dinheiro >= self.divida:
            self.dinheiro -= self.divida
            self.divida = 0
            print("Divida paga")

        else:
            print("Não tem dinheiro para pagar a divida")

if __name__ == "__main__":
    pessoa = Cliente(1, 12345678, "Thomas", 19, "m")
    sair = False
    while not(sair):
        print(f'''
1 - Exibir Saldo
2 - Receber Salario
3 - Comprar
4 - Pagar divida
5 - Valor divida
6 - Sair''')
        opcao = int(input("Insira uma opcao: "))

        if opcao == 1:
            print(f'Saldo: R$ {pessoa.dinheiro}')

        elif opcao == 2:
            salario = float(input("Valor do salario: "))
            pessoa.receber_salario(salario)

        elif opcao == 3:
            valor = float(input("Valor da compra: "))
            pessoa.comprar(valor)

        elif opcao == 4:
            pessoa.pagar()

        elif opcao == 5:
            print(f'Divida: R$ {pessoa.divida}')

        elif opcao == 6:
            sair = True