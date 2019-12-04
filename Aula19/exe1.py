class FestaHbsis():
    def __init__(self):

        self.pessoas = []
        self.ler()
    
    def ler(self):
        
        arquivo = open('cadastro.txt', 'r')
        for linha in arquivo:
            linha = linha.strip().split(';')
            pessoa = {"codigo": linha[0], "nome": linha[1], "sexo": linha[2], "idade": linha[3]}
            self.pessoas.append(pessoa)

        arquivo.close()

    def separar_pessoas(self):

        arquivo_homem = open("homens.txt", 'a')
        arquivo_mulher = open("mulheres.txt", 'a')

        for pessoa in self.pessoas:
            if int(pessoa["idade"]) >= 18:
                if pessoa["sexo"] == 'm':
                    arquivo_homem.write(f'{pessoa["codigo"]};{pessoa["nome"]};{pessoa["sexo"]};{pessoa["idade"]}\n')

                else:
                    arquivo_mulher.write(f'{pessoa["codigo"]};{pessoa["nome"]};{pessoa["sexo"]};{pessoa["idade"]}\n')

        arquivo_homem.close()
        arquivo_mulher.close()

    def buscarParticipante(self):

        cod = int(input("Codigo do Participante: "))    

        for pessoa in self.pessoas:
            if int(pessoa["codigo"]) == cod:
                print(f'Nome: {pessoa["nome"]}')
                if int(pessoa["idade"]) <= 18:
                    print("Entrada Proibida")

                else:
                    if pessoa["sexo"] == 'm':
                        print(f'Valor Ingresso R$ 35')

                    else:
                        print(f'Valor Ingresso R$ 15')

festa = FestaHbsis()
festa.buscarParticipante()