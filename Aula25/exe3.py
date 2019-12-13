from criadorCod import Codigo

# Aula 21 - 12-12-2019


# Produto

# Crie uma classe produto.

# Esta classe deve ter como atributo: codigo produto(int), nome, marca, preço de custo(float),
# preço de venda(float) e quantidade em estoque(int).

# Cada produto deve ter um código unico e sequencial.
# Só pode vender produtos que tenha no estoque.

# Metodos: Atualizar dados do produto, adicionar e 
# remover produtos do estoque, __str__ e __eq__ (para pesquisar mais facilmente o
# código do produto)


class Produto(object):

    __getCodigo = Codigo()

    def __init__(self,nome, marca, preco_custo, preco_venda, estoque, codigo=None):
        self.__nome = nome
        self.__marca = marca
        self.__preco_custo = preco_custo
        self.__preco_venda = preco_venda
        self.__estoque = int(estoque)
        self.__codigo = codigo

        self.setCodigo()

    def setCodigo(self):
        self.__codigo = self.__getCodigo.getCodigo()

    def atualizar (self, dados):
        '''
        Este metodo serve para atualizar o cadastro do produto. 
        Os dados que podem ser atualizados são: 
        nome, marca, preço de custo(float),preço de venda(float)
        '''
        conversor = dados.strip().split(";")
        self.__nome = conversor[0]
        self.__marca = conversor[1]
        self.__preco_custo = conversor[2]
        self.__preco_venda = conversor[3]
        self.__estoque = conversor[4]
        self.__codigo = conversor[5]

    def atualizar_estoque(self, quantidade):
        '''
        Esta função é usada para atualizar a quantidade de produto no estoque.
        
        '''
        if (self.__estoque - quantidade) < 0:
            qtdPermitida = self.__estoque

        else:
            qtdPermitida = quantidade

        self.__estoque -= qtdPermitida

        #print(self.__estoque)
        #print(qtdPermitida)

        return qtdPermitida

    def getEstoque(self):
        return self.__estoque

    def getNome(self):
        return self.__nome

    def __eq__(self,valor):
        '''
        Este metodo deve comparar se o valor do código é igual ao valor.
        Se positivo ele retorna True caso contrário retorna False
        '''
        if self.__codigo == valor:
            return True

        else:
            return False

    def __toString__(self):
        '''
        Este metodo deve retornar uma string com todos os dados.
        Use f-string para interpolar o texto com as variáveis
        '''
        #print(self.__preco_venda)
        conversor = f'{self.__codigo};{self.__nome};{self.__preco_custo};{self.__preco_venda};{self.__estoque}'
        return conversor
   


if __name__ == "__main__":
    p = Produto('agua','ab',15.6,20,10)
    print(p)
    p.atualizar_estoque(11)
    print(p)
