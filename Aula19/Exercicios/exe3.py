# Aula 19 - 04-12-2019
# Lista com for e metodos

# Como comer um gigante.... é com um pedaço de cada vez.
# Na hora de fazer este exercicio, atentar para 

# Com o arquivo de cadastro.txt onde possui os seguintes dados: codigo cliente, nome, idade, sexo, e-mail e telefone
# 1 - Crie um metodo que gere e retorne uma lista com bibliotecas com os dados dos clientes
def ler():
    pessoas = []
    arquivo = open("cadastro.txt", "r")

    for linha_st in arquivo:
        linha = linha_st.strip().split(";")
        pessoa = {"cod_cliente": linha[0], "nome": linha[1], "idade": linha[2], "sexo": linha[3], "email": linha[4], "telefone": linha[5]}
        pessoas.append(pessoa)

    arquivo.close()
    return pessoas

pessoas = ler()

# 2 - Com a lista do exercicio 1, separe os adultos dos menores de idade e salve em um arquivo .txt cada.

def separar_adultos(pessoas):
    arquivo = open("maiores18.txt", "a")
    lista_pessoas = []

    for pessoa in pessoas:
        if int(pessoa["idade"]) >= 18:
            dic = {"cod_cliente": pessoa["cod_cliente"], "nome": pessoa["nome"], "idade": pessoa["idade"], "sexo": pessoa["sexo"], "email": pessoa["email"],"telefone": pessoa["telefone"]}
            lista_pessoas.append(dic)
            arquivo.write(f'{pessoa["cod_cliente"]};{pessoa["nome"]};{pessoa["idade"]};{pessoa["sexo"]};{pessoa["email"]};{pessoa["telefone"]}\n')
    arquivo.close()
    return lista_pessoas

separar_adultos(pessoas)

# Esta função tambem retornar uma lista com a biblioteca dos maiores de idades.
# 3 - Crie uma função que conte quantas mulheres e quantos homens tem na lista. Salve cada um em um arquivo diferente.

def separar_homens_mulheres(pessoas):
    arquivo_homens = open("homensexe3.txt", "a")
    arquivo_mulheres = open("mulheresexe3.txt", "a")
    contHomens = 0
    contMulheres = 0

    for pessoa in pessoas:
        if str(pessoa["sexo"]) == "m":
            contHomens += 1
            arquivo_homens.write(f'{pessoa["cod_cliente"]};{pessoa["nome"]};{pessoa["idade"]};{pessoa["sexo"]};{pessoa["email"]};{pessoa["telefone"]}\n')

        elif str(pessoa["sexo"]) == "f":
            arquivo_homens.write(f'{pessoa["cod_cliente"]};{pessoa["nome"]};{pessoa["idade"]};{pessoa["sexo"]};{pessoa["email"]};{pessoa["telefone"]}\n')
            contMulheres += 1
        
    arquivo_homens.close()
    arquivo_mulheres.close()
    print(f'Homens: {contHomens} - Mulheres: {contMulheres}')

separar_homens_mulheres(pessoas)

# 4 - Faça uma função de consulta de cadastro. A função deve receber o valor do código do cliente e deve imprimir na 
# tela os dados do cliente com f-string usando a lista do exercicio 1
#  4.1 - A pesquisa deve aparecer uma frase para as seguintes condições:
#           Mulheres até 16 anos: "Ola {nome}! Você quer aproveitar nosso Tikito sabor Gloss? É uma delicia!""
#           Mulheres acima de 16 a 18 anos: "Olá {nome}! Quer experimentar nosso refigerante sabor alegria! O seu 
#                                            cruch vai adorar!"
#           Mulheres acima de 18:  "Olá {nome}! Já experimentou nossa bebida a base de tequila? Baixo tero alcoolico
#                                                com o dobro de sabor!!!"
#           Homens até 16 anos: "Ola {nome}! Você quer aproveitar nosso Tikito sabor Meleka? É uma delicia!""
#           Homens acima de 16 a 18 anos: "Olá {nome}! Quer experimentar nosso refigerante sabor Corriga de carros!  
#                                          A sua amada vai adorar!"
#           Homens acima de 18:  "Olá {nome}! Já experimentou nossa cerveja? alto teor alcoolico
#                                                com o dobro do amargor!!!"
#      Lembre-se: É importante que apareça a frase. Pois a mesma será encaminhada por e-mail pela equipe de marketing

def consultar(cod, pessoas):
     for pessoa in pessoas:
        if int(pessoa["cod_cliente"]) == cod:
            if str(pessoa["sexo"]) == "f":
                if int(pessoa["idade"]) <= 16:
                    print(f'Ola {pessoa["nome"]}! Você quer aproveitar nosso Tikito sabor Gloss? É uma delicia!')
                    continue

                elif int(pessoa["idade"]) <= 18:
                    print(f'Olá {pessoa["nome"]}! Quer experimentar nosso refigerante sabor alegria! O seu cruch vai adorar!')
                    continue

            elif str(pessoa["sexo"]) == "m":
                if int(pessoa["idade"]) <= 16:
                    print(f'Ola {pessoa["nome"]}! Você quer aproveitar nosso Tikito sabor Meleka? É uma delicia!')
                    continue

                elif int(pessoa["idade"]) <= 18:
                    print(f'Olá {pessoa["nome"]}! Quer experimentar nosso refigerante sabor Corriga de carros! A sua amada vai adorar!')
                    continue

                elif int(pessoa["idade"]) >= 18:
                    print(f'Olá {pessoa["nome"]}! Já experimentou nossa cerveja? alto teor alcoolico com o dobro do amargor!!!')

cod = int(input("Codigo: "))
consultar(cod, pessoas)