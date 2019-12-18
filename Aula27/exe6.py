from random import randint

# Aula 28 - 17-12-2019
# Revisão de listas, arquivo

# 1) Faça um programa de sorteio de alunos.
# Especificações:
# - Deve sortear um aluno por vez.
# - O programa deve garantir que todos os alunos sejam sorteados antes de reiniciar
# o sorteio.
# - O programa deve garantir que mesmo que ele seja fechado, o sorteio dos alunos só
# seja reiniciado quando todos os alunos forem sorteados.
# - Faça um menu para o program e de destaque para o aluno sorteado.

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
        arquivo = open("Aula27\\{}.txt".format(nome_arquivo), "w")
        for dado in self.__dados:
            arquivo.write(f'{dado}\n')

        arquivo.close()

        self.getTamanhoArquivo()

    def lerArquivo(self, arquivo):
        arquivo1 = open(f"Aula27\\{arquivo}.txt", "r")
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

# Dica: 
# Ovo de pascua
# O "import os" pode habiliar alguns comandos como o os.system() que pode passar comando 
# do DOS, shell script do python para o terminal.
# 
# Como vocês ainda não sabem o que é o import e como ele funciona, então o pode-se trocar por:
# 
# from os import system
# system('dir')
#
# Agora imagine se usar o system('cls') para windows ou system('clear') para linux
# o cls/clear apaga o que foi impresso anteriormente na tela do terminal.
# 
# 
# :-)
# Poste no grupo do whatsapp #ACHEI! se vc ler esta mensagem! 
# (ninguem achou este ovo de pascua!)
