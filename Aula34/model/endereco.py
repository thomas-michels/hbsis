class Endereco():
    id = 0
    logradouro = ""
    numero = 0
    complemento = ""
    bairro = ""
    cidade = ""
    cep = ""

    def __str__(self):
        return f'{self.id};{self.logradouro};{self.numero};{self.complemento};{self.bairro};{self.cidade};{self.cep}'