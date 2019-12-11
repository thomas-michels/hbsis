class Pessoa:
    '''
    Esta classe é uma demonstração para aula
    '''
    def __init__ (self,nome, idade, telefone, sexo):
        ''' 
        O __init__ é o motor que irá iniciar as variáveis da clase
        O self é o que irá conecta toda a classe
        '''
        # Atributos ##########
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.sexo = sexo
        # 
        self.divida = None
        self.cansada = 'não'
        self.viva = True
        self.fome = 'não'
        self.sede = 'não'

    #### Metodos

    def respira (self,respirar):
        if self.viva == True:
            if respirar == True:
                self.viva = True
            else:
                self.viva = False

    def corre (self,distancia):
        if self.viva:
            if distancia < 100:
                self.cansada = 'pouco'
                self.sede = 'pouco'
                self.fome = 'pouco'
            elif distancia >= 100 and distancia < 200:
                self.cansada = 'medio'
                self.sede = 'medio'
                self.fome = 'medio'
            elif distancia >= 200:
                self.cansada = 'muito'
                self.sede = 'muito'
                self.fome = 'muito'

    def dorme (self):
        if self.viva:
            self.cansada = 'não'
            self.bebe()
            self.come()


    def bebe (self):
        if self.viva:
                self.sede = 'não'
    
    def come (self):
        if self.viva:
            self.fome = 'não'
        

    def multiplica (self):
        pass # para outra hora!

a = Pessoa("ted", 156, 33, "m")
a.corre(150)
a.respira(True)
print(a.cansada)
a.corre(99)
print(a.cansada)