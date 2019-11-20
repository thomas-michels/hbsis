from operacoes import *

num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))

print(f'Soma: {somar(num1, num2)}')
print(f'Subtração: {subtrair(num1, num2)}')
print(f'Multiplicação: {multiplicar(num1, num2)}')
print(f'Divisao: {dividir(num1, num2)}')
print(f'Divisao Inteira: {dividir_int(num1, num2)}')
print(f'Resto da divisao: {resto_div(num1, num2)}')
print(f'Raiz: {raiz(num1, num2)}')