# Aula 21 - 16-12-2019
#Operadores in is ==

from gerenciadorLista import lista_simples_int_str
from gerenciadorLista import lista_simples_int
from gerenciadorLista import lista_simples_str
from gerenciadorLista import embaralhar


# A função embaralhar() irá criar listas aleátorias, copiar-las
# e embaralhar. Desta forma não se sabe se as listas são iguais ou
# se as listas são as mesmas. Como defult ela irá criar 3 listas
# diferentes com 30 itens, copiálas e embaralar randomicamente
# retornando uma lista com o dobro (6) de itens.

lista = embaralhar(2,10)

a = lista[0]
b = lista[1]
c = lista[2]
d = lista[3]

# print(a)
# print(b)
# print(c)
# print(d)

# Neste caso, ele irá criar 2 listas com 10 itens, e retornará
# uma lista com 4 listas podendo cada uma ser cópia ou uma só.




lista = embaralhar(2,10,2)

print(lista)

# 1) Analisnado a lista gerada (possui 2 listas), diga se as duas listas são elas
# mesmas (is) ou são somente iguais (==).
if lista[0] is lista[1]:
    print("São iguais com is")

elif lista[0] == lista[1]:
    print("São iguais com ==")


# 2) Qual é o maior valor destas duas listas 
maximo0 = max(lista[0])
maximo1 = max(lista[1])

if maximo0 > maximo1:
    print(maximo0)

else:
    print(maximo1)

# 3) Qual é o maior valor de cada lista
print(f"0: {maximo0}")
print(f"1: {maximo1}")

# 4) Há o número 10 dentro da lista[0]?
print(lista[0].count(10))

# 5) Há o número 20 dentro da lista[1]?
print(lista[1].count(20))

# 6) Quantos números da lista[0] tem dentro da lista[1]?
cont = 0
for i in lista[0]:
    if i in lista[1]:
        cont += 1

print(cont)

# 7) Mostre os números da lista[0] que estão dentro da lista[1]
for i in lista[0]:
    if i in lista[1]:
        print(i)


# 8) Mutliplique a soma da lista[0] com cada item da lista[1]
listaSoma = []
cont = 0
for i in lista[0]:
    soma = i + lista[1][cont]
    cont += 1
    listaSoma.append(soma)

mult = 1
for i in listaSoma:
    mult *= i

print(mult)

# 9) Faça uma divizão inteira do maior número da lista pelo menor numero da lista. Após verifique 
# se o resultado está dentro de uma das listas, se sim, diga qual!
div = max(lista[0]) // min(lista[0])
print(div)

if lista[0].count(div) >= 1:
    print("Na lista")

elif lista[1].count(div) >= 1:
    print("Na lista")

# 10) Ferifique se o maior número da lista[0] está dentro da lista[1] e se o menor número da
# lista[1] está na lista[0]
if maximo0 in lista[1]:
    print("dentro da lista 1")

if min(lista[1]) in lista[0]:
    print("dentro da lista 0")