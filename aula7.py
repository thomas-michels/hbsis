# lista = []

# for i in range(0,10):
#     nome = input("Insira o nome: ")
#     lista.append(nome)

# print(lista)

# tabuada = int(input("Insira o numero: "))

# for i in range(0,11):
#     print(f'{tabuada} X {i} = {tabuada * i}')

alunos = []


for i in range(0,2):
    nome = input("Nome do aluno:")
    aluno = nome
    aluno = []
    aluno.append(nome)
    for j in range(0,4):
        aluno.append(float(input("Insira a nota: ")))

    alunos.append(aluno)

for aluno in alunos:
    media = (aluno[1] + aluno[2] + aluno[3] + aluno[4]) / 4

    if media >= 7:
        status = "Aprovado"

    else:
        status = "Reprovado"

    print(f'A media do {aluno[0]} foi {status} é {media}')
