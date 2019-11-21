
# marca = input("Marca da cerveja: ")
# tipo = input("Tipo da cerveja: ")
# ibu = input("IBU da cerveja: ")
# abv = input("ABV da cerveja: ")
# ebc = input("EBC da cerveja: ")
# volume = input("Volume da cerveja: ")

# dic = {"marca": marca, "tipo": tipo, "ibu": ibu, "abv": abv, "ebc": ebc, "volume": volume}
# print("="*50)
# print(f' Marca: {dic["marca"]}\n Tipo: {dic["tipo"]}\n ibu: {dic["ibu"]}\n abv: {dic["abv"]}\n ebc: {dic["ebc"]}\n volume: {dic["volume"]}')



time = []

for i in range (0,11):
    dic_jogador = {"nome": "", "posicao": "", "numero": "", "pernaBoa": ""}
    dic_jogador['nome'] = input("Nome: ")
    dic_jogador['posicao'] = input("posicao: ")
    dic_jogador['numero'] = int(input("numero: "))
    dic_jogador['pernaBoa'] = input("Perna boa: ")
    time.append(dic_jogador)

for jogador in time:
    print(f'Nome: {jogador["nome"]} - Posicao: {jogador["posicao"]} - Numero: {jogador["numero"]} - Perna Boa: {jogador["pernaBoa"]}')
