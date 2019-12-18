from exe6 import Sorteio
from menu import Menu
import os

if __name__ == "__main__":
    sair = False
    menu = Menu()
    stringMenu = menu.getMenu()

    while not(sair):
        try:
            sorteio = Sorteio()
            os.system("cls")
            opcao = int(input(stringMenu))
            if opcao == 3:
                sair = True
                print("Saindo...")

            elif opcao == 1:
                print(sorteio.sortear())
                continuar = input("Deseja continuar? (S/N) ").upper()
                if continuar == 'S':
                    continue

                else:
                    sair = True

            elif opcao == 2:
                dados = sorteio.getDados()
                os.system("cls")
                print("========== ALUNOS ==========")
                for dado in dados:
                    print(dado)

                print("============================")
                continuar = input("Deseja continuar? (S/N) ").upper()
                if continuar == 'S':
                    continue

                else:
                    sair = True

        except ValueError:
            sair = True
        