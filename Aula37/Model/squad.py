class Squad():

    def __init__(self):
        self.id = 0
        self.nome = ''
        self.descricao = ''
        self.numeroPessoas = 0
        self.linguagemBackEnd = ''
        self.frameworkFrontEnd = ''

    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.numeroPessoas};{self.linguagemBackEnd};{self.frameworkFrontEnd}'