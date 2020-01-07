from random import randint

class Sorteio():
    __tamanho = 0
    __dados = []

    def __init__(self):
        self.__dados = self.lerArquivo("alunos")
        self.getTamanhoArquivo()

    def getTamanhoArquivo(self):
        self.__tamanho = len(self.__dados)
        if self.__tamanho == 0:
            self.atualizarArquivo()

    def getDados(self):
        return self.__dados

    def atualizarArquivo(self):
        self.__dados = self.lerArquivo("alunos_backup")
        self.salvar("alunos")

    def salvar(self, nome_arquivo):
        arquivo = open("hbsis\\Aula27\\{}.txt".format(nome_arquivo), "w")
        for dado in self.__dados:
            arquivo.write(f'{dado}\n')

        arquivo.close()

        self.getTamanhoArquivo()

    def lerArquivo(self, arquivo):
        arquivo1 = open(f"hbsis\\Aula27\\{arquivo}.txt", "r")
        linhas = []
        for linha_st in arquivo1:
            linha = linha_st.strip()
            linhas.append(linha)

        arquivo1.close() 

        return linhas

    def sortear(self):
        tamanho = self.__tamanho - 1
        if tamanho < 0:
            tamanho = 0

        print(tamanho)
        sorteado = self.__dados[randint(0, tamanho)]
        self.__dados.remove(sorteado)
        self.salvar("alunos")
        self.getTamanhoArquivo()

        return sorteado