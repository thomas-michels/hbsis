import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula38')
from Model.sgbds import Sgbds
from Model.linguagem_back_end import LinguagemBackEnd
from Model.framework_front_end import FrameworkFrontEnd

class Squad():

    def __init__(self):
        self.id = 0
        self.nome = ''
        self.descricao = ''
        self.numeroPessoas = 0
        self.linguagemBackEnd = LinguagemBackEnd()
        self.frameworkFrontEnd =FrameworkFrontEnd()
        self.sgbds = Sgbds()

    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.numeroPessoas};{self.linguagemBackEnd};{self.frameworkFrontEnd};{self.sgbds}'