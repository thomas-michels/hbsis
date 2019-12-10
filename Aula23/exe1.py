dias_de_cada_mes = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

qual_mes = int(input('Digite o número do mês (1..12): '))

print('O mês', qual_mes, 'tem', dias_de_cada_mes[qual_mes], 'dias')

print('Dias que faltam para acabar o ano, a partir do mês informado: ')

mes = 0
for i in range(qual_mes, 13):
    mes += dias_de_cada_mes[i]

print(mes)