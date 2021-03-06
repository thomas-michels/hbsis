from random import randint

# A HBSIS Airlines é uma empresa de aviação que opera rotas internacionais a partir de Blumenau.
# Cada voo é tripulado por seis elementos, sendo que estes se dividem em dois grupos: a tripulação
# técnica e a tripulação de cabine. A tripulação técnica é constituída pelo piloto e dois oficiais. 
# A tripulação de cabine é constituída pelo chefe de serviço de voo e duas comissárias.
# O transporte dos tripulantes entre o terminal e o avião é efetuado através de um Smart Fortwo, que
# é um veículo que leva apenas duas pessoas. Por política da empresa, apenas o piloto e o chefe de
# serviço de voo podem dirigir este veículo. É também política da empresa que nenhum dos oficiais
# pode ficar sozinho com o chefe de serviço de bordo, e nem nenhuma das comissárias pode ficar
# sozinha com o piloto.  No terminal de embarque estão os seis tripulantes e ainda um policial 
# junto com um presidiário. Estes oito elementos terão que embarcar segundo as regras descritas acima. 
# A empresa não coloca nenhum limite para o número de viagens entre o terminal e o avião.
# Por motivos de segurança o presidiário não pode ficar sozinho em momento algum com os
# tripulantes sem a presença do policial, nem no terminal e nem no avião. De forma a facilitar o
# processo, a empresa autorizou que o policial pudesse dirigir o veículo também.

# Requisitos:
# 1 - Sempre que o Fortwo se mover, apresentar no console quando ele chega no destino
# 2 - Sempre que acontecer um embarque, apresentar quais elementos estão embarcando
# 3 - Sempre que acontecer um embarque no terminal, apresentar quem está no terminal
# 4 - Sempre que acontecer um embarque no avião, apresentar quem está no avião
# 5 - Deve ser feito em Python

class Transporte():

    def __init__(self):
        self.__terminal = ['piloto', 'oficial 1', 'oficial 2', 'chefe de voo', 'comissaria 1', 'comissaria 2', 'policial', 'presidiario']
        self.__avião = []
        self.__fortwo_pos = "terminal"

    def selecionar(self, pessoa=None):
        if pessoa == None:
            sair = False
            while not(sair):
                try:
                    numero = randint(1, len(self.__terminal))
                    pessoa_pos = self.__terminal[numero]
                    #sair = True

                except IndexError as erro:
                    print('O erro é ',erro)

                else:
                    sair = True

        else:
            if self.__terminal.index(pessoa) + 1 > len(self.__terminal):
                numero = 1

            else:
                numero = self.__terminal.index(pessoa) + 1

        return numero
        
    def transportar(self, destino, pessoa1, pessoa2=None):
 
        if destino == "terminal":

            if pessoa1 == "piloto" and (pessoa2 == "comissaria 1" or pessoa2 == "comissaria 2"):
                nova_pessoa2 = pessoa2
                piloto = False
                while pessoa1 == "piloto" and (pessoa2 == "comissaria 1" or pessoa2 == "comissaria 2") and piloto is False:
                    nova_pessoa2 = self.selecionar(nova_pessoa2)
                    if nova_pessoa2 == "piloto":
                        False
                    else:
                        True

            else:
                nova_pessoa2 = pessoa2

            self.__fortwo_pos = "terminal"
            self.__terminal.insert(0, pessoa1)
            self.__avião.remove(pessoa1)

            if pessoa2 is not None:
                self.__terminal.insert(0, nova_pessoa2)
                self.__avião.remove(nova_pessoa2)

        elif destino == "aviao":

            if pessoa1 == "piloto" and (pessoa2 == "comissaria 1" or pessoa2 == "comissaria 2" or pessoa2 == None):
                 nova_pessoa2 = self.selecionar(pessoa2)

            else:
                nova_pessoa2 = pessoa2

            self.__fortwo_pos = "aviao"
            self.__avião.insert(0, pessoa1)
            self.__terminal.remove(pessoa1)

            if pessoa2 is not None:
                self.__avião.insert(0, nova_pessoa2)
                self.__terminal.remove(nova_pessoa2)

        return (pessoa1, pessoa2, destino)

    def loop(self):
        sair = False

        while not(sair):
            if len(self.__terminal) == 0:
                sair = True
                continue

            if self.__fortwo_pos == "aviao":
                 if self.__avião.index('piloto'):
                     pessoa1 = self.__avião[self.__avião.index("piloto")]
                     retorno = self.transportar("terminal", pessoa1)

                 elif self.__avião.index('chefe de voo'):
                     pessoa1 = self.__avião[self.__avião.index("chefe de voo")]
                     retorno = self.transportar("terminal", pessoa1)

                 elif self.__avião.index('policial' and self.__terminal.index("presidiario")):
                     pessoa1 = self.__avião[self.__avião.index("policial")]
                     retorno = self.transportar("terminal", pessoa1)

            else:
                pessoa1 = self.__terminal[0]
                selecionado = self.selecionar()
                print(selecionado)
                pessoa2 = self.__terminal[selecionado]
                retorno = self.transportar("aviao", pessoa1, pessoa2)

            print(f'Destino: {retorno[2]} - Pessoas: {retorno[0]}, {retorno[1]}')
            print(f'Fortwo posicao - {self.__fortwo_pos}')
            print(f'Terminal - {self.__terminal}')
            print(f'Aviao - {self.__avião}')
            print("")


fortwo = Transporte()
fortwo.loop()