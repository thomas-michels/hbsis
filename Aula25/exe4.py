import exe3

# Aula 21 - 12-12-2019
# Cadastro do produto.

# Crie uma classe para o cadastro do produto, ler e gravar em arquivo .txt,
# atualizar produtos, e pesquisa pelo código de produto. (use como base a classe 
# cadastrar cliente)

# Para guardar os produtos importe a classe do exercicio 3 e atribua numa lista.


class CadastroProduto():

    __produtos = []

    def ler_arquivo(self):
        '''
        Este metodo serve para ler um arquivo .txt que deve possuir os 
        dados dos produtos cadastrados.
        Vai receber como parametro o nome do arquivo (nome_arquivo) a ser 
        lido.
        Os dados lidos devem ser atribuidos a classe produto.
        '''
        try:
            arquivo = open("Aula25\\produtos.txt", "r")

            for linha_st in arquivo:
                linha = linha_st.strip().split(";")
                produto = exe3.Produto(linha[1], linha[2], linha[3], linha[4], linha[0])
                self.__produtos.append(produto)

        except FileNotFoundError:
            print("Arquivo Não Encontrado")

        finally:
            arquivo.close()

    def cadastro_produto(self):
        '''
        Este metodo é utilizado para cadastrar um produto.
        Os dados devem ser aplicados em uma classe produto.
        O codigo produto não pode se repetir e deve estar na sequencia númerica
        Neste caso se faz necessário adicionar linha no arquivo de texto com o metodo
        gravar adicionando os novos produtos (use o atributo 'a')
        '''
        nome = input("Insira o nome: ")
        marca = input("marca: ")
        preco_custo = input("preco custo: ")
        preco_venda = input("preco venda: ")
        estoque = input("estoque: ")
        produto = exe3.Produto(nome, marca, preco_custo, preco_venda, estoque)
        self.gravar(att, produto)

    def pesquisa_codigo(self,codigo, att = False):
        '''
        Neste metodo é feito a pesquisa do produto, mostrando os 
        dados do mesmo.
        No caso perguntará se vai querer alterar os dados.
        Se sim, altere e encaminhe para o metodo gravar.
        Lembrando que no caso de alteração, será necessário fazer a gravação de
        todos os dados usando o atributo 'w'.
        '''
        self.ler_arquivo()
        cont = 0
        for produto in self.__produtos:
            dados = produto.__toString__().strip().split(';')
            if int(dados[0]) is codigo:

                if att:
                    nome = input("Insira o nome: ")
                    marca = input("marca: ")
                    preco_custo = input("preco custo: ")
                    preco_venda = input("preco venda: ")
                    estoque = input("estoque: ")
                    conversor = f'{nome};{marca};{preco_custo};{preco_venda};{estoque};{codigo}\n'
                    produto.atualizar(conversor)
                    self.gravar(True)

                return produto

            cont += 1

        return False

    def gravar(self, att, produto = None):
        '''
        Este é responsável por gravar os dados.
        use o atributo 'w' para sobrescrever o arquivo e o
        atributo 'a' para adicionar linha.
        o parametro nome_arquivo é o nome do arquivo em que se deseja gravar.
        '''
        if att is False and produto is not None:
            arquivo = open("Aula25\\produtos.txt", "a")
            dados = produto.__toString__()
            arquivo.write(f'{dados}\n')
            arquivo.close()

        else:
            arquivoWrite = open("Aula25\\produtos.txt", "w")
            for produto_c in self.__produtos:
                produto = produto_c.__toString__()
                conversor = f'{produto}\n'
                arquivoWrite.write(conversor)
            
            arquivoWrite.close()

if __name__ == "__main__":
    cadastro = CadastroProduto()
    cadastro.cadastro_produto()
    cadastro.cadastro_produto()
    print(cadastro.pesquisa_codigo(int(input("Codigo: "))))