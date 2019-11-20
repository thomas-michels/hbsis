nome = input("Nome: ")
cpf = input("CPF: ")
reg = int(input("Nº registro: "))
cargo = input("Cargo: ")
salario = float(input("Salario: "))

def calc_inss(salario):

    if 0 < salario <= 1751.8:
        inss = salario * 0.08

    elif 1751.8 < salario <= 2919.72:
        inss = salario * 0.095

    elif 2919.72 < salario <= 5839.45:
        inss = salario * 0.11

    else:
        inss = 642.34

    return inss

def calc_irrf(inss, salario):
    irrf = 0

    if 1903.98 < salario <= 2826.65:
        irrf = ((salario - inss) * 0.075) - 142.8

    elif 2826.65 < salario <= 3751.05:
        irrf = ((salario - inss) * 0.095) - 354.8

    elif 3751.05 < salario <= 4664.68:
        irrf = ((salario - inss) * 0.11) - 636.13

    elif salario > 4664.68:
        irrf = ((salario - inss) * 0.275 ) - 869.36

    return irrf

inss = calc_inss(salario)
irrf = calc_irrf(inss, salario)
res = salario - inss - irrf
print(res)