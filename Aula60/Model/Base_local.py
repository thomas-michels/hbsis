
class BaseLocal:

    def __init__(self, pessoas: list):
        self.__pessoas = pessoas

    def get_pessoas(self) -> list:
        return self.__pessoas

    def entrada(self, pessoa):
        if self.valida_entrada(pessoa):
            self.__pessoas.append(pessoa)
            return True

        else:
            return False

    def saida(self, pessoa):
        if self.validar_saida(pessoa):
            if pessoa != '':
                self.__pessoas.remove(pessoa)

            return True

        else:
            return False

    def validar_saida(self, pessoa):

        if pessoa in self.__pessoas:

            if pessoa == 'policial' and 'presidiario' in self.__pessoas and len(self.__pessoas) > 3:
                return False

            if len(self.__pessoas) <= 4:
                if pessoa == 'chefe de servico' and 'piloto' in self.__pessoas and 'comissario1' \
                        in self.__pessoas and 'comissario2' in self.__pessoas:
                    return False

                if pessoa == 'piloto' and 'chefe de servico' in self.__pessoas and 'oficial1' \
                        in self.__pessoas and 'oficial2' in self.__pessoas:
                    return False

            if len(self.__pessoas) <= 3:
                if pessoa == 'chefe de servico' and 'piloto' in self.__pessoas and \
                        ('comissario1' in self.__pessoas or 'comissario2' in self.__pessoas):
                    return False

                if pessoa == 'piloto' and 'chefe de servico' in self.__pessoas and \
                        ('oficial1' in self.__pessoas or 'oficial2' in self.__pessoas):
                    return False

        elif pessoa != '':
            return False

        return True

    def valida_entrada(self, pessoa):

        if len(self.__pessoas) <= 2:

            if len(self.__pessoas) == 1:

                if 'presidiario' in self.__pessoas and pessoa != 'policial':
                    return False

                if ('comissario1' in self.__pessoas or 'comissario2' in self.__pessoas) and pessoa == 'piloto':
                    return False

                if ('oficial1' in self.__pessoas or 'oficial1' in self.__pessoas) and pessoa == 'chefe de servico':
                    return False

            if pessoa == 'piloto' and ('comissario1' in self.__pessoas and 'comissario2' in self.__pessoas):
                return False

            if pessoa == 'chefe de servico' and ('oficial1' in self.__pessoas and 'oficial2' in self.__pessoas):
                return False

        return True
