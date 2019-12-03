# Aula 18 - 03-11-2019

# Festa da HBSIS

# 1 - Faça uma função que leia do arquivo cadastro.txt e retorne uma lista com dicionários.
# cada linha possui os dados na seguinte posição: codigo, nome, sexo, idade

def ler():
    linhas = []
    pessoas = []
    arquivo = open('cadastro.txt', 'r')
    linhas_arq = arquivo.readlines()
    for linha in linhas_arq:
        linha = linha.strip().split(';')
        linhas.append(linha)

    for pessoa in linhas:
        pessoa = {"codigo": pessoa[0], "nome": pessoa[1], "sexo": pessoa[2], "idade": pessoa[3]}
        pessoas.append(pessoa)

    arquivo.close()
    return pessoas
        
pessoas = ler()

# 2 - Como a entrada da festa é mais barata para mulheres (R$ 15,00) do que para os homens (R$ 35,00) 
# deve-se separar os dois em duas listas separadas e salvar em arquivos separados. Como é uma festa de arromba,
# menores de idade não podem entrar.

def separar_pessoas(pessoas):
    arquivo_homem = open("homens.txt", 'a')
    arquivo_mulher = open("mulheres.txt", 'a')

    for pessoa in pessoas:
        if int(pessoa["idade"]) >= 18:
            if pessoa["sexo"] == 'm':
                arquivo_homem.write(f'{pessoa["codigo"]};{pessoa["nome"]};{pessoa["sexo"]};{pessoa["idade"]}\n')

            else:
                arquivo_mulher.write(f'{pessoa["codigo"]};{pessoa["nome"]};{pessoa["sexo"]};{pessoa["idade"]}\n')

    arquivo_homem.close()
    arquivo_mulher.close()

separar_pessoas(pessoas)

# 3 - Faça uma terceira função que ao digitar o código do participante ele imprima o nome do participante, 
# o valor do ingresso, e em caso de menores de idade apareça o texto "Entrada Proibida!"

def buscarParticipante(pessoas):
    cod = int(input("Codigo do Participante: "))    

    for pessoa in pessoas:
        if int(pessoa["codigo"]) == cod:
            print(f'Nome: {pessoa["nome"]}')
            if int(pessoa["idade"]) <= 18:
                print("Entrada Proibida")

            else:
                if pessoa["sexo"] == 'm':
                    print(f'Valor Ingresso R$ 35')

                else:
                    print(f'Valor Ingresso R$ 15')

buscarParticipante(pessoas)