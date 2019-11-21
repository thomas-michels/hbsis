def calcular_iss(valor):
    return (valor * 0.05)

valor = float(input("Insira o valor do serviço: "))
imp = calcular_iss(valor)

print(f'O valor do ISS a ser pago é R$ {imp} - O valor total é R$ {valor + imp}')