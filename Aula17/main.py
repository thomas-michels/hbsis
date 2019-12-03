import exe1

if __name__ == "__main__":
    sair = False

    while sair is False:
        opcao = int(input(exe1.exibir_cabecalho()))

        if opcao == 1:
            exe1.cadastrar_cliente()
            pass

        elif opcao == 2:
            pass

        elif opcao == 3:
            pass

        elif opcao == 4:
            pass

        elif opcao == 5:
            pass

        elif opcao == 6:
            pass

        elif opcao == 7:
            sair = True
            print("Saindo...")

        else:
            print("Opcao Invalida")