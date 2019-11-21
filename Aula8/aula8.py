
nome = "thomas"
notas = [10,20,50,70]
media = sum(notas) / len(notas)

status = "Reprovado"
if media >= 7:
    status = "Aprovado"

dic = {"nome":nome, "notas":notas, "media":media, "status":status}

print(f'Nome: {dic["nome"]} - Media: {dic["media"]} - Status: {dic["status"]}')