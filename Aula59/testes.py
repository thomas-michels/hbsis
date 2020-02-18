
# Assert verifica se a condição é True


def check(idade):
    if idade >= 18:
        return True
    else:
        return False


assert check(19) == True
assert check(18) == True
assert check(17) != True


class Calculadora:

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.resultado = 0

    def set_n1(self, valor):
        self.n1 = valor

    def get_n1(self):
        return self.n1

    def get_n2(self):
        return self.n2

    def set_n2(self, valor):
        self.n2 = valor

    def get_resultado(self):
        return self.resultado

    def soma(self):
        self.resultado = self.n1 + self.n2
        return self.resultado

    def subtrair(self):
        self.resultado = self.n1 - self.n2
        return self.resultado

    def multiplicar(self):
        self.resultado = self.n1 * self.n2
        return self.resultado

    def dividir(self):
        self.resultado = self.n1 / self.n2
        return self.resultado


calc = Calculadora(5, 5)
assert isinstance(calc, Calculadora) # Testa se calc é um objeto de Calculadora

assert calc.soma() == 10

assert calc.subtrair() == 0

assert calc.multiplicar() == 25

assert calc.dividir() == 1

assert calc.get_resultado() == 1

assert calc.get_n1() == 5

assert calc.set_n1(10) is None
assert calc.get_n1() == 10

assert calc.get_n2() == 5

assert calc.set_n2(55) is None
assert calc.get_n2() == 55
