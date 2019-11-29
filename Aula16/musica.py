def chamarInfo():

    informacoes = {"musica": "", "artista": "", "album": ""}
    return informacoes

def cadastrar():

    informacoes = chamarInfo()
    musica = input("Nome da musica: ")
    artista = input("Artista: ")
    album = input("Album: ")

    informacoes["musica"] = musica
    informacoes["artista"] = artista
    informacoes["album"] = album

    salvar(informacoes)

def salvar(informacoes):
    arquivo = open('Aula16/aula16.csv', 'a')
    arquivo.write(f'{informacoes["musica"]};{informacoes["artista"]};{informacoes["album"]}\n')
    arquivo.close()

def ler():
    playlist = []

    arquivo = open('Aula16/aula16.csv', 'r')
    for linha in arquivo:

        informacoes = chamarInfo()

        linha = linha.strip().split(';')
        informacoes["musica"] = linha[0]
        informacoes["artista"] = linha[1]
        informacoes["album"] = linha[2]
        playlist.append(informacoes)

    arquivo.close()
    return playlist