# Aula 21 - 16-12-2019
#Funções para listas

from gerenciadorLista import lista_simples_int


lista1 = lista_simples_int()
lista2 = lista_simples_int()
lista3 = lista_simples_int()


# 1) Com as listas aleatórias (lista1,lista2,lista3) e usando as funções para listas,
# f-string, responda as seguintes questões:


# 1.1) Qual é o tamanho da lista1?
print(f'{len(lista1)}')

# 1.2) Qual é o maior valor da lista2?
print(f'{max(lista1)}')

# 1.3) Qual seria a soma do maior valor com o menor valor da lista2?
print(f'{max(lista2) + min(lista2)}')

# 1.4) Qual é a média aritmética da lista1?
print(f'{sum(lista1) / len(lista1)}')

# 1.5) Qual o valor da soma de todas as listas e a soma total delas?
# quero que mostre a soma individual (por lista) e a soma total de todas elas (soma das somas das listas)
print(f'Soma de todos: {sum(lista1) + sum(lista2) + sum(lista3)}')
print(f'Lista1: {sum(lista1)}')
print(f'Lista2: {sum(lista2)}')
print(f'Lista3: {sum(lista3)}')

# 1.6) Usando o f-string, imprima todos os valores da lista1 um de baixo do outro.
for i in lista1:
    print(f'{i}')

# 1.7) Com a indexação e f-string, mostre o valor das posições 5, 9, 10 e 25 de cada lista.
# trate para evitar o erro: IndexError
listas = [lista1, lista2, lista3]
cont = 1
try:
    for i in listas:
        print(f'Lista{cont} - 5: {i[5]} - 9: {i[9]} - 10: {i[10]} - 25: {i[25]}')
except IndexError:
    print(f'Deu nao')

# 1.8) Mostre qual das listas tem mais itens (lembre-se, as listas são randômicas, não há como prever o 
# tamanho delas).
list1 = len(lista1)
list2 = len(lista2)
list3 = len(lista3)

print(f'{list1} {list2}')

if list1 > (list2 and list3):
    print(f'lista 1')

elif list2 > (list1 and list3):
    print(f'lista 2')

elif list3 > (list2 and list1):
    print(f'lista 3')

else:
    print("Listas com o mesmo tamanho")

# 1.9) Some os maiores números de todas as listas e subtraia pelo menor número dos menores valores das listas.
# Para obter o menor valor, pegue o menor valor das listas e veja qual deles é o menor e use ele.


# 1.10) Pegue o maior valor de todas as listas e some com o menor valor de todas as listas
maximo = max(lista1) + max(lista2) + max(lista3)
minimo = min(lista1) + min(lista2) + min(lista3)

print(f'{maximo - minimo}')