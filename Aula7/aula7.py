alunos = []

for i in range(0,2):
    nome = input("Nome do aluno:")
    aluno = []
    aluno.append(nome)
    for j in range(0,4):
        aluno.append(float(input("Insira a nota: ")))

    alunos.append(aluno)

for aluno in alunos:
    media = (aluno[1] + aluno[2] + aluno[3] + aluno[4]) / 4
    status = "Reprovado"

    if media >= 7:
        status = "Aprovado"

    print(f'A media de {aluno[0]} foi {status} é {media}')