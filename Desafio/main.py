import exe1

if __name__ == "__main__":
    sair = False

    while sair is False:
        opcao = int(input(exe1.exibir_cabecalho()))

        if opcao == 1:
            exe1.cadastrar_clientes()

        elif opcao == 2:
            exe1.exibir_clientes(False)

        elif opcao == 3:
            exe1.cadastrar_produtos()

        elif opcao == 4:
            exe1.exibir_produtos(False)

        elif opcao == 5:
            produtos = exe1.exibir_produtos(True)
            clientes = exe1.exibir_clientes(True)
            exe1.vender_produto(produtos, clientes)

        elif opcao == 6:
            produtos = exe1.exibir_produtos(True)
            clientes = exe1.exibir_clientes(True)
            exe1.relatorio_vendas(clientes, produtos)

        elif opcao == 7:
            sair = True
            print("Saindo...")

        else:
            print("Opcao Invalida")