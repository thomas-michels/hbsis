
class Fortwo:
    posicao_atual = "Terminal"

    def __init__(self, motorista=None, passageiro=None):
        self.motorista_permitido = ['piloto', 'chefe de servico', 'policial']
        self.motorista = motorista
        self.passageiro = passageiro
        self.destino = ""

    def set_motorista(self, motorista=None):
        try:
            if motorista in self.motorista_permitido:
                self.motorista = motorista

            else:
                raise ValueError

        except ValueError:
            print("Motorista não autorizado")

    def get_motorista(self):
        return self.motorista

    def set_passageiro(self, passageiro=None):
        if self.motorista == 'policial':
            if passageiro == 'presidiario':
                self.passageiro = passageiro

        elif self.motorista == 'piloto':
            if passageiro != 'comissario1' and passageiro != 'comissario2' and passageiro != 'presidiario':
                self.passageiro = passageiro

    def set_posicao(self, posicao):
        self.posicao_atual = posicao
