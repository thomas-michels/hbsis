valor = float(input("Valor do investimento: "))

def calcularSelic(valor):
    selic = 104.1
    qtd = valor // selic
    if qtd == 0:
        return "Não é possivel aplicar com esse valor"

    sobra = valor - selic * qtd
    resultado = ((selic * qtd) * (1 + 0.0502) ** 4.333)
    return (resultado, sobra)
        
investimento = calcularSelic(valor)
total = "{0:.2f}".format(investimento[0])
sobra = float("{0:.2f}".format(investimento[1]))

print(f'O valor aplicado foi de R$ {valor - sobra} e rendeu R$ {total}')

#rendimento selic + 0,02 a.a
#selic 10410 - aplicação minima 104,10
# vencimento 01/03/2025