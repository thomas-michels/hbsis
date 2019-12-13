from datetime import date
import exe2, exe4
# Aula 21 - 12-12-2019
# Venda de produtos

# Crie uma classe que pegue os dados de um produto, dados de um cliente, faça a venda.
# Lembre-se que é necessário ter produto no estoque e o cliente ter crédito para a 
# compra.
# Caso a compra seja realizada, então salve em um arquivo os seguintes dados:
# codigo cliente, codigo produto, data de venda, quantidade vendida e preço.

# Na consulta da venda, deve aparecer o seguinte:
# Nome do cliente, endereço do cliente, nome do produto, dada da venda, quantidade de produto, valor unitário
# e valor total do produto.

# Importe as classes necessárias dos exercicios anteriores.

class Venda():

    def vender(self, cliente, produto, quantidade_produto):
        cliente.limite_credito()
        devedor = cliente.getClienteDev()

        cliente_b = cliente.__toString__()
        produto_b = produto.__toString__()

        cliente_f = cliente_b.strip().split(';')
        produto_f = produto_b.strip().split(';')

        cod_cliente = cliente_f[0]
        cod_produto = produto_f[0]

        preco_venda = produto_f[3]

        estoque = produto.getEstoque()

        atualizar_estoque = produto.atualizar_estoque(quantidade_produto)
        total = atualizar_estoque * preco_venda

        if devedor is not True and int(estoque) > 0:
            arquivo = open("vendas.txt", "a")
            data = date.today()
            dados = f'{cod_cliente};{cod_produto};{data};{quantidade_produto};{preco_venda};{total}'
            arquivo.write(dados)
            arquivo.close()

    def consultarVendas(self):
        try:
            arquivo = open("vendas.txt", "r")
            for linha_st in arquivo:
                linha = linha_st.strip().split(";")
                cod_cliente = linha[0]
                cod_produto = linha[1]
                data = linha[2]
                preco_venda = linha[3]
                total = linha[4]

                cliente = exe2.CadastroCliente().pesquisa_codigo(int(cod_cliente))
                produto = exe4.CadastroProduto().pesquisa_codigo(int(cod_produto))

                nome_cliente = cliente.getNome()
                endereco = cliente.getEndereco()
                nome_produto = produto.getNome()

                print('=' * 50)
                print(f'Nome Cliente: {nome_cliente}')
                print(f'Endereco: {endereco}')
                print(f'Nome Produto: {nome_produto}')
                print(f'Data: {data}')
                print(f'Preço de Venda: {preco_venda}')
                print(f'Total: {total}')

        except FileNotFoundError:
            print("Arquivo Não Encontrado")

        finally:
            arquivo.close()

if __name__ == "__main__":
    venda = Venda()
    cliente = exe2.CadastroCliente().pesquisa_codigo(1)
    print(cliente)
    produto = exe4.CadastroProduto().pesquisa_codigo(1)
    print(produto.__toString__())
    #concertar o metodo de leitura do produto
    venda.vender(cliente, produto, 301)
    venda.consultarVendas()