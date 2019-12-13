from criadorCod import Codigo

# Aula 21 - 12-12-2019


# Cliente.....

# Crie uma classe cliente.
# Use os seguintes atributos: codigo cliente(int), nome, idade(int), telefone, email, endereço
# Use o seguinte atributo de estado: crédito em R$, saldo R$, 
#                                    cliente_devedor(True/False)
# O atributo cliente_devedor deve ser True toda vez que o saldo negativo for menor 
# ou igual ao crédito. 
# Para o atributo cliente_devedor voltar a ser False o cliente deve pagar sua divida
# ficando com o saldo igual a 0 ou positivo.



# Como metodo use:

class Cliente(object):

    __getCodigo = Codigo()

    def __init__(self, nome, idade, telefone, email, endereco, codigo=None):
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = int(idade)
        self.__telefone = telefone
        self.__email = email
        self.__endereco = endereco

        self.__credito = 0
        self.__saldo = 0
        self.__cliente_devedor = False

        self.setCodigo()

    def setCodigo(self):
        if self.__codigo is None:
            self.__codigo = self.__getCodigo.getCodigo()

    def atualizar (self, dados):
        '''
        Este metodo serve para atualizar o cadastro do cliente. 
        Os dados que podem ser atualizados são: 
        nome, idade(int), telefone, email, endereço
        '''
        conversor = dados.strip().split(";")
        self.__nome = conversor[0]
        self.__idade = conversor[1]
        self.__telefone = conversor[2]
        self.__email = conversor[3]
        self.__endereco = conversor[4]
        self.__codigo = conversor[5]

    def getClienteDev(self):
        return self.__cliente_devedor

    def getSaldo(self):
        return self.__saldo

    def getNome(self):
        return self.__nome

    def getEndereco(self):
        return self.__endereco

    def limite_credito(self,valor = None):
        '''
        O crédito é o valor máximo que o cliente pode ter de saldo negativo.
        Este metodo altera o valor tanto para aumentar o crédito quanto para 
        diminuir ou eliminar o crédito.
        Este valor deve ser passado como número negativo (ex: -50.00) para o atributo
        credito
        Se diminuir o crédito (exemplo de -50 para -10) e o 
        cliente ficar com o saldo menor que o cédito (exemplo saldo = -20 e cédito -10)
        o cliente_devedor fica True
        Se o cliente_devedor estiver True, o crédito pode ser diminuido porem não aumentado.
        
        '''
        if valor is None:
            valor = self.__credito

        if valor > 0:
            valor *= -1

        if self.__cliente_devedor is True and self.__credito > valor:
            self.__credito = valor

        elif self.__cliente_devedor is False:
            self.__credito = valor

        if self.__credito <= self.__saldo:
            self.__cliente_devedor = False

        else:
            self.__cliente_devedor = True
      
    def dinheiro(self,valor):
        '''
        Este metodo serve para adicionar/remover valor em R$ para o atributo saldo para 
        o cliente.
        Esta função revebe o valor como parametro. Se o valor for positivo, o saldo
        aumenta, se o valor for negativo o saldo diminui. 
        
        O cliente não pode ter seu saldo menor que o crédito. Então se o valor exceder
        deve retornar False e a operação fica cancelada.
        (Exemplo: limite do cartão de crédito)
        Caso o valor não exceda o crédito a operação será realizada, o valor do saldo
        irá diminuir e deve retornar True
        Se o cliente_devedor estiver True o dinheiro só poderá receber valores positivos.
        Se o cliente_devedor estiver True e o cliente depositar dinheiro suficiente para
        o saldo ficar maior ou igual a 0 o cliente_devedor deve ser alterado para False.
        '''
        if self.__cliente_devedor is True and valor < 0:
            return False

        elif self.__cliente_devedor is True and (self.__saldo + valor) >= 0:
            self.__saldo += valor
            print(self.limite_credito())
            return True

        elif self.__cliente_devedor is True and valor >= 0:
            self.__saldo += valor
            return True
        
        elif self.__cliente_devedor is False:
            self.__saldo += valor
            return True

    def __toString__(self):
        '''
        Este metodo deve retornar uma string com todos os dados do cliente.
        Use f-string para interpolar o texto com as variáveis
        '''
        conversor = f'{self.__codigo};{self.__nome};{self.__idade};{self.__telefone};{self.__email};{self.__endereco}'
        return conversor


if __name__ == "__main__":

    '''
    Use este if para fazer os testes com a classe.
    Este if pergunta se este arquivo está sendo executado diretamente.
    Caso positivo o código será executado.
    '''
    cliente = Cliente("Ted", 18, 3333, "ted@ted", "rua das ruas, nº 20")
    cliente.dinheiro(100)
    print(cliente.__toString__())
    cliente2 = Cliente("Jao", 17, 7777, "jao@jao", "rua")
    print(cliente2.__toString__())
    print(cliente.dinheiro(-101))
    print(cliente.limite_credito())
    print(cliente.dinheiro(-10))
