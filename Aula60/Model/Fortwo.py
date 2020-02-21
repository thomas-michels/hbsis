
class Fortwo:

    def __init__(self, motorista=None, passageiro=None):
        self.motorista_permitido = ['piloto', 'chefe de servico', 'policial']
        self.motorista = motorista
        self.passageiro = passageiro

    def set_motorista(self, motorista=None) -> bool:
        if self.__valida_regra_motorista__(motorista):
            self.motorista = motorista
            return True

        return False

    def __valida_regra_motorista__(self, motorista) -> bool:
        try:
            if motorista in self.motorista_permitido:
                return True

            else:
                raise ValueError

        except ValueError:
            return False

    def get_motorista(self) -> str:
        return self.motorista

    def __valida_regra_passageiro__(self, passageiro) -> bool:
        if self.motorista == 'policial':

            if passageiro == 'presidiario':

                return True

        elif self.motorista == 'piloto':
            if passageiro != 'comissario1' and passageiro != 'comissario2' and\
                    passageiro != 'presidiario':

                return True

        elif self.motorista == 'chefe de servico':
            if passageiro != 'oficial1' and passageiro != 'oficial2' and\
                    passageiro != 'presidiario':

                return True

        return False

    def set_passageiro(self, passageiro=None) -> bool:
        if self.__valida_regra_passageiro__(passageiro):

            self.passageiro = passageiro
            return True

        return False

    def get_passageiro(self) -> str:
        return self.passageiro

    def viagem(self, origem, destino):
        print(f'Saindo do {origem}')
        print(f'Iniciando viagem...')
        print(f'Motorista: {self.get_motorista()}')
        print(f'Passageiro: {self.get_passageiro()}')
        print(f'Chegando em {destino}')
        print(f'Saindo...')
        print(f'{self.get_motorista()} e {self.passageiro} descem')
        print("")
        print(f'{origem}: {origem.get_pessoas()}')
        print(f'{destino}: {destino.get_pessoas()}')
        print("")
