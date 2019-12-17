# Aula 28 - 17-12-2019
# Listas

# DICA!!!!
# Procurem primeiro o padrão que estas listas vão apresentar! Depois de encontrado, faça o uso da linguagem
# para facilitar na hora de codar!


lista1 = [['frutas','verduras','legumes','preço'],
         ['mamão','abacaxi','laranja','uva','pera','maçã','vergamota'],
         ['alface crespa', 'alface lisa','rucula','almerão','repolho','salsinha','cebolinha'],
         ['feijão', 'erviha', 'lentilha','vagem','feijão branco','gão de bico','soja'],
         [ [10.00, 2.56, 5.25, 9.5, 10.05, 15, 5.75], [2.99, 2.95, 3.5, 3.25, 5.89, 2.9, 2.5],
           [9.0, 5.0, 7.5, 1.75, 10.9, 5.99, 3.55] 
         ]
        ]


# 1) Faça um dicionário com a lista1 onde cada elemento esteja junto com o seu respectivo
# preço. (Dica: Use a indexação e fatiamento para ajudar)

def agruparElementos(lista):
    lista1 = []
    frutas = lista[1]
    frutas_p= lista[4][0]

    verduras = lista[2]
    verduras_p = lista[4][1]

    legumes = lista[3]
    legumes_p = lista[4][2]

    frutas1 = []
    for i in range(len(frutas)):
        dic = {"nome": frutas[i],
        "preco": frutas_p[i]}
        frutas1.append(dic)

    lista1.append(frutas1)

    verduras1 = []
    for i in range(len(verduras)):
        dic = {"nome": verduras[i],
        "preco": verduras_p[i]}
        verduras1.append(dic)

    lista1.append(verduras1)

    legumes1 = []
    for i in range(len(legumes)):
        dic = {"nome": legumes[i],
        "preco": legumes_p[i]}
        legumes1.append(dic)

    lista1.append(legumes1)
    return lista1

dados = agruparElementos(lista1)

# 2) Com o dicionário, imprima os seguintes valores:
# 2.1) Preço do feijão

# 2.2) Preço da cebolinha

# 2.3) Preço da Alface lisa

# 2.4) Preço do Abacaxi

# 2.5) Preço do feijão branco.

for j in dados:
    for i in j:
        print(f'Nome: {i["nome"]} - Preco: R$ {i["preco"]}')

# 3) Com a lista1 qual seria a média dos valores das frutas, verduras e legumes?
soma = 0
qtd = 0
for i in dados[0]:
    soma += float(i["preco"])
    qtd += 1

media = soma / qtd

print(f'A media de precos é {round(media, 2)}')

# 4) Com a lista 1, Qual é o maior e menor valor das frutas, verduras e legumes?
maior = 0
menor = 10000

for j in dados:
    for i in j:
        preco = float(i["preco"])
        if preco > maior:
            maior = preco

        elif preco < menor:
            menor = preco

print(f"Maior preco: {maior}")
print(f"Menor preco: {menor}")

# 5) Adicione no cabeçalho da lista1 (entre o legumes e preço) a "roupa". Aṕos adicione de forma que fique 
# com a lista coerente 7 roupas e os seus preços.

lista1[0].insert(-1,"roupa")

roupas = ["camisa", "terno", "calca", "tenis", "regata", "bone", "chinelo"]
precos = ["20", "100", "50", "25", "33", "55", "10"]

lista1.insert(4, roupas)
lista1[5].insert(len(lista1[5]), precos)

print(lista1)

# 6) Salve esta lista em um arquivo .txt de moque que cada linha tenha o item e seu preço. 

def salvar(lista):
    arquivo = open("Aula27\\itens.txt", "a")

    cont = 0
    for i in range(1, 5):
        cont2 = 0
        for dado in lista[i]:
            preco = lista[5][cont][cont2]
            if cont2 < len(lista[5][0]):
                cont2 += 1
            
            arquivo.write(f'{dado};{preco}\n')

        if cont < 7:
            cont += 1

    arquivo.close()

salvar(lista1)
# 7) Com a lista2, crie uma lista com dicionário onde cada dicionário é um cadastro de uma pessoa.

lista2 = ['nome',   ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
                'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
                ]

def receberPessoas(lista):
    lista1 = []
    nomes = lista[1]
    telefones = lista[3]
    email = lista[5]
    idade = lista[7]

    for i in range(len(nomes)):
        dic = {"nome": nomes[i],
        "telefone": telefones[i],
        "email": email[i],
        "idade": idade[i]}
        lista1.append(dic)

    return lista1

print(receberPessoas(lista2))

# 8) Organize a lista2, retirando o cabeçalho e junte os dados de modo que cada cliente ocupe uma lista. Após, salve os dados
# em um arquivo .txt 

# 9) Criando uma fila. Uma fila é uma estrutura de dados onde o primeiro item que entra é o ultimo que sai. Resumindo, o item novo
# entra no indice 0 da lista e sai pelo ultimo indice. 
# Ex:
# >>> []
# >>> [1]
# >>> [2,1]
# >>> [3,2,1]
# >>> [3,2]
# >>> [3] 

# Crie um programa que adiciona novos clientes em uma fila e conforme vai atendendo, remova-os da fila do caixa da loja.

# 10) Criando uma pilha. Uma pilha é uma estrutura de dados onde o primeiro que entra é o ultimo a sair. Resumindo,
# Os elementos são adicionados e removidos no mesmo lado da lista.
# Ex:
# >>> []
# >>> [1]
# >>> [1,2]
# >>> [1,2,3]
# >>> [1,2]
# >>> [1] 

# Crie um programa em que adicione os novos números na pilha. Após some eles removendo da pilha.

numeros = []
qtd = int(input("Numeros: "))
cont = 1
for i in range(qtd):
    numeros.insert(0, cont)
    cont += 1
    print(numeros)

cont = qtd
for i in range(qtd):
    numeros.remove(cont)
    cont -= 1
    print(numeros)