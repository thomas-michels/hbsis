# Aula 28 - 17-12-2019
# Lista com for e metodos

# Dica: Para este formulário será necessário usar um metodo para string novo.
# Vocês já conhecem o .strip() que remove os caracteres especiais \n do final 
# da string. o .splint('') que quebra a string em uma lista conforme o caracteres
# que tem dentro das aspas.
# O metodo novo para este exercico é o .replace('{velho}','{novo}') - O velho
# é um caracter que queira substituir e o novo é o caracter que deseja incluir.
# Exemplo pelo shell do pyton: 
# >>> 'agua verde mar'.replace('a','A') 
# 'AguA verde mAr'
# >>> 'agua verde mar'.replace('a','')
# 'gu verde mr'

# Como vemos, no primeiro exemplo o caracter "a" foi substituido pelo "A"
# e no segundo exemplo o "a" foi removido da string.

# https://forms.gle/PLuAZXpmpBvE1vkX7

# Fazer usando funções

# 1 - abrir o arquivo pesquisa.csv e fazer o tratamento padrão dos dados
# (criar lista com dicionarios)

def abrir():
    arquivo = open("Aula27\\Pesquisa de Gostos.csv", "r")
    linhas = []
    dados = []
    for linha_st in arquivo:
        linha = linha_st.strip().split(',')
        linhas.append(linha)

    arquivo.close()

    for i in linhas[2::]:
         
        dic = {
        "{}".format(linhas[0][0]): i[0],
        "{}".format(linhas[0][1]): i[1],
        "{}".format(linhas[0][2]): i[2],
        "{}".format(linhas[0][3]): i[3],
        "{}".format(linhas[0][4]): i[4],
        "{}".format(linhas[0][5]): i[5],
        "{}".format(linhas[0][6]): i[6],
        "{}".format(linhas[0][7]): i[7],
        "{}".format(linhas[0][8]): i[8],
        "{}".format(linhas[0][9]): i[9],
        "{}".format(linhas[0][10]): i[10],
        "{}".format(linhas[0][11]): i[11],
        "{}".format(linhas[0][12]): i[12],
        "{}".format(linhas[0][13]): i[13],
        "{}".format(linhas[0][14]): i[14]}
        dados.append(dic)
    
    return dados

dados = abrir()

# 2 - Separar aqueles que gostam de cerveja e salvar no cerveja.txt

def separar(nome_arq,dados, key, resposta_padrao):
    respostas = []
    for dado in dados:
        if dado[key].upper() == resposta_padrao:
            respostas.append(dado)

    arquivo = open("Aula27\\{}.txt".format(nome_arq), "a")
    for resposta in respostas:
        conversor = f'{resposta["Carimbo de data/hora"]},{resposta["Sexo"]},{resposta["Qual a sua escolariedade?"]},{resposta["Voce possui algum veiculo?"]},{resposta["Qual destes?"]},{resposta["Qual a sua idade?"]},{resposta["Qual e o correto?"]},{resposta["Gosta de Cerveja?"]},{resposta["Qual a marca de cerveja voce mais gosta?"]},{resposta["Quantas cervejas voce comprou no MercadoTec? (Digite somente numeros)"]},{resposta["Gosta de Refrigerante?"]},{resposta["Qual a marca de refrigerante voce mais gosta?"]},{resposta["Quantos refrigerantes voce comprou no MercadoTec? (Digite somente numeros)"]},{resposta["Qual o valor em Reais gasto no MercadoTec em Refrigerante? (Digite somente numeros)"]}\n'
        arquivo.write(conversor)

    arquivo.close()

separar("cerveja", dados, "Gosta de Cerveja?", "SIM")
# 3 - Separar aqueles que gostam de refigerantes e salvar no refrigerante.txt

separar("refrigerante", dados, "Gosta de Refrigerante?", "SIM")

# 4 - Separar em arquivos .txt os homens das mulheres

separar("homens", dados, "Sexo", "M")
separar("mulheres", dados, "Sexo", "F")