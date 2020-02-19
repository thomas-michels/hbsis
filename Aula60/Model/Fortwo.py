
class Fortwo:
    posicao_atual = "Terminal"

    def __init__(self, motorista=None, passageiro=None):
        self.motorista_permitido = ['piloto', 'chefe de servico', 'policial']
        self.motorista = motorista
        self.passageiro = passageiro
        self.destino = ""

    def set_motorista(self, motorista=None):
        if self.__valida_regra_motorista__(motorista):
            self.motorista = motorista

    def __valida_regra_motorista__(self, motorista) -> bool:
        try:
            if motorista in self.motorista_permitido:
                return True

            else:
                raise ValueError

        except ValueError:
            return False

    def get_motorista(self):
        return self.motorista

    def __valida_regra_passageiro__(self, passageiro) -> bool:
        if self.motorista == 'policial':
            if passageiro == 'presidiario':
                return True

        elif self.motorista == 'piloto':
            if passageiro != 'comissario1' and passageiro != 'comissario2' and passageiro != 'presidiario':
                return True

        elif self.motorista == 'chefe de servico':
            if passageiro != 'oficial1' and passageiro != 'oficial2' and passageiro != 'presidiario':
                return True

        return False

    def set_passageiro(self, passageiro=None):
        if self.__valida_regra_passageiro__(passageiro):
            self.passageiro = passageiro

    def set_posicao(self, posicao):
        self.posicao_atual = posicao
