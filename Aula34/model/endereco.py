class Endereco():
    id = 0
    logradouro = ""
    numero = 0
    complemento = ""
    bairro = ""
    cidade = ""
    cep = ""

    def exportar_txt(self, lista_pessoas):
        # ----- Cria um arquivo e atribui a uma variável 'arquivo'
        with open('33-Aula33/Aula33-4/pessoas4.txt', 'a') as arquivo:
            # ---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
            for p in lista_pessoas:
                arquivo.write(f"{str(p)}\n")

    def __str__(self):
        return f'{self.id};{self.logradouro};{self.numero};{self.complemento};{self.bairro};{self.cidade};{self.cep}'