valor = float(input("Insira o valor do investimento: "))
taxa = (float(input("Insira a taxa mensal: ")))

def calcularInvestimento(valor, taxa):
    convert = taxa / 100
    montante = valor * (1 + convert) ** 12
    return montante

def calcularPorcent(valor, montante):
    porcent = ((montante * 100) / valor) - 100
    return porcent

montante = float("{0:.2f}".format(calcularInvestimento(valor, taxa)))
porcent = float("{0:.2f}".format(calcularPorcent(valor, montante)))

print("=" * 75)
print(f'''R$ {valor} terá um valor final de R$ {montante} no periodo de 12 meses
a uma taxa de {taxa}% o que equivale a {porcent}% do valor inicial''')