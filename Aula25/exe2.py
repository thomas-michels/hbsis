import exe1

# Aula 21 - 12-12-2019
# 
# Cadastro de cliente.

# Crie uma classe para cadastrar cliente. 
# Para guardar os clientes cadastrado, utilize a classe feita no
# exercicio1.py importando ela.

# Como atributo, utilize uma lista vazia para guardar os clientes.

class CadastroCliente():

    __clientes = []

    def ler_arquivo(self):
        '''
        Este metodo serve para ler um arquivo .txt que deve possuir os 
        dados de clientes cadastrados.
        Vai receber como parametro o nome do arquivo (nome_arquivo) a ser 
        lido.
        Os dados lidos devem ser atribuidos a classe pessoa.
        '''

        try:
            arquivo = open("Aula25\\cadastro.txt", "r")

            for linha_st in arquivo:
                linha = linha_st.strip().split(";")
                cliente = exe1.Cliente(linha[1], linha[2], linha[3], linha[4], linha[5], linha[0])
                self.__clientes.append(cliente)

        except FileNotFoundError:
            print("Arquivo Não Encontrado")

        finally:
            arquivo.close()

    def cadastro_cliente(self):
        '''
        Este metodo é utilizado para cadastrar um cliente.
        Os dados devem ser aplicados em uma classe pessoa.
        O codigo cliente não pode se repetir e deve estar na sequencia númerica
        (novos clientes recebem os ultimos numeros)
        Neste caso se faz necessário adicionar linha no arquivo de texto com o metodo
        gravar adicionando os novos clientes (use o atributo 'a')
        '''
        nome = input("Insira o nome: ")
        idade = int(input("Idade: "))
        telefone = input("Telefone: ")
        email = input("Email: ")
        endereco = input("Endereco: ")
        cliente = exe1.Cliente(nome, idade, telefone, email, endereco)
        self.gravar(False, cliente)

    def pesquisa_codigo(self,codigo, att = False):
        '''
        Neste metodo é feito a pesquisa do cliente, mostrando os 
        dados do mesmo.
        No caso perguntará se vai querer alterar os dados do cliente.
        Se sim, altere e encaminhe para o metodo gravar.
        Lembrando que no caso de alteração, será necessário fazer a gravação de
        todos os dados usando o atributo 'w'.
        '''
        self.ler_arquivo()
        cont = 0
        for cliente in self.__clientes:
            dados = cliente.__toString__().strip().split(';')
            if int(dados[0]) == codigo:

                try:
                    if att:
                        nome = input("Nome: ")
                        idade = int(input("Idade: "))
                        telefone = input("Telefone: ")
                        email = input("Email: ")
                        endereco = input("Endereco: ")
                        conversor = f'{nome};{idade};{telefone};{email};{endereco};{codigo}\n'
                        cliente.atualizar(conversor)
                        self.gravar(True)

                finally:
                    return cliente

            cont += 1

        return False
                
    def gravar(self, att, cliente = None):

        '''
        Este é responsável por gravar os dados dos clientes.
        use o atributo 'w' para sobrescrever o arquivo e o
        atributo 'a' para adicionar linha.
        o parametro nome_arquivo é o nome do arquivo em que se deseja gravar.
        '''
        if att is False and cliente is not None:
            arquivo = open("Aula25\\cadastro.txt", "a")
            dados = cliente.__toString__()
            arquivo.write(f'{dados}\n')
            arquivo.close()

        else:
            arquivoWrite = open("Aula25\\cadastro.txt", "w")
            for cliente_c in self.__clientes:
                cliente = cliente_c.__toString__()
                conversor = f'{cliente}\n'
                arquivoWrite.write(conversor)
            
            arquivoWrite.close()

if __name__ == "__main__":
    cadastro = CadastroCliente()
    #cadastro.cadastro_cliente()
    codigo = int(input("Codigo: "))
    print(cadastro.pesquisa_codigo(codigo))
