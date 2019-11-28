def salvar(cerveja):
    arquivo = open('aula15.csv', 'a')
    arquivo.write(f'{cerveja["marca"]};{cerveja["teor"]};{cerveja["tipo"]}\n')
    arquivo.close()

def adicionar():
    marca = input("Marca: ")
    teor = float(input("Teor: "))
    tipo = input("Tipo: ")
    cerveja = {"marca": marca, "teor": teor, "tipo": tipo}
    return cerveja

def ler():
    cervejas = []

    arquivo = open('aula15.csv', 'r')
    for linha in arquivo:
        cerveja = {"marca": "", "teor": "", "tipo": ""}
        linha = linha.strip() #Remove os espaços em branco e o \n
        list_linha = linha.split(";") #Quebra a string a partir do caractere inserido
        cerveja["marca"] = list_linha[0]
        cerveja["teor"] = list_linha[1]
        cerveja["tipo"] = list_linha[2]
        cervejas.append(cerveja)
    
    arquivo.close()
    return cervejas

cerveja = adicionar()
salvar(cerveja)
cervejas = ler()

for cerveja in cervejas:
    print(f'Marca: {cerveja["marca"]} - Teor Alcoolico: {cerveja["teor"]} - Tipo: {cerveja["tipo"]}')