
lista = [3,5,6]
tupla = ('pao', lista, 3)
print(tupla[1][2])

nome = 'thomas' ' michels' ' rodriuges'
print(nome.count('a')) #conta quantos caracteres iguais
 print(nome.lower()) #minuscula
print(nome.split('s')) #separa uma string
print(nome.upper()) #maiculas
print(nome.strip()) #remove os espaços em branco e ou quebra de linha
print(nome.capitalize()) #primeira letra maiuscula
print((' oi ').join(nome)) #insere string no meio de outra string
print(lista[1:]) # o : separa onde começa a pegar a lista, neste caso começa no 1 e vai ate o fim
print(lista[:1]) # o : separa onde começa a pegar a lista, neste caso começa no 0 e vai te o 1

num1 = 30
num2 = 27

print(num1 // num2) #Divisao inteira
print(num1 % num2) #Resto da divisao
print(num1 ** num2) #Potenciação
print(num2**1/2) #Raiz quadrada
print(num2**1/3) #Raiz cubica

if "ola".count("l") > 0:
    print("tem l")

if "a" in "ola":
    print("tem a")

if 5 in lista:
    print("Existe o num 5 na lista")

if lista: #Verifica se a lista possui elementos
    print("Tem numeros")

