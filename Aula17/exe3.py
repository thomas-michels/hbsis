from random import randint

sorteio = randint(1, 1000)

opcao = 0

while sorteio != opcao:
    opcao = int(input('Insira o numero: '))        

    if opcao > sorteio:
        print("O numero é menor")
        continue

    elif opcao < sorteio:
        print("O numero é maior")
        continue

    print("Acertou")