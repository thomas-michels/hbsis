
class Cerveja():

    def __init__(self):
        self.id = 0
        self.marca = ""
        self.abv = 0
        self.ibu = 0
        self.ebc = 0


    def __str__(self):
        return f"{self.id};{self.marca};{self.abv};{self.ibu};{self.ebc}"