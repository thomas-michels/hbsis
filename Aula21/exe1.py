# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Crie um arquivo que leia 2 números inteiros e imprima a soma, 
# multiplicação, divisão e subtração com uma f-string.

# 2 - Crie um while que pergunte se deseja continuar. Se digitar 's' o
# programa termina.

#################### até aqui tudo bem! ##########################

# 3 - faça um tratamento de exceção para que ao digitar o valor que 
# não seja inteiro, ele avise o usuário para ele digitar denovo.
# 4 - Faça outro tratamento de exceção para evitar que divida um numero
# por zero.

def inserir_numero():
    arquivo = open("numeros.csv", "w")
    try:
        num1 = int(input("numero 1: "))
        num2 = int(input("numero 2: "))

    except ValueError:
        print("Numero errado")
        inserir_numero()

    else:
        arquivo.write(f'{num1}\n{num2}')
        arquivo.close()

def ler():
    dados = []
    arquivo = open("numeros.csv", "r")

    for linha_st in arquivo:
        linha = linha_st.strip().split(';')
        dados.append(linha)

    arquivo.close()
    return dados

def imprimir(numeros):
    print(f'Num1: {numeros[0][0]} Num2: {numeros[1][0]}')
    print(f'Soma: {int(numeros[0][0]) + int(numeros[1][0])}')
    print(f'Subtração: {int(numeros[0][0]) - int(numeros[1][0])}')
    print(f'Multiplicação: {int(numeros[0][0]) * int(numeros[1][0])}')
    print(f'Divisão: {int(numeros[0][0]) / int(numeros[1][0])}')

def perguntar():
    sair = False
    inserir_numero()
    while not(sair):
        try:
            numeros = ler()
            imprimir(numeros)
            sair_r = input("Deseja sair? S ou N - ")
            if sair_r == "S":
                sair = True

        except ZeroDivisionError:
            print("Divisão por zero não é possivel")
            inserir_numero()

perguntar()