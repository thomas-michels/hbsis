bandas = []
albuns = []
musicas = []

def exibir_menu():
    menu = """
1 - Cadastrar Banda
2 - Cadastrar Album
3 - Cadastrar Musica
4 - Sair

Digite a opcao: """
    return menu

def cadastrar_banda(nome):
    banda = {"nome": nome}
    return banda

def cadastrar_album(nome, banda):
    album = {"nome": nome, "banda": banda}
    return album

def cadastrar_musica(nome, banda, album):
    musica = {"nome": nome, "banda": banda, "album": album}
    return musica

def exibir_cadastros():
    print("=" * 50 + "\n")
    print("Bandas\n")
    for banda in bandas:
        print(f'Nome da banda: {banda["nome"]}')

    print("=" * 50 + "\n")
    print("Albuns\n")
    for album in albuns:
        print(f'Nome do album: {album["nome"]} - Banda: {album["banda"]}')

    print("=" * 50 + "\n")
    print("Musicas\n")
    for musica in musicas:
        print(f'Nome da musica: {musica["nome"]} - Nome do album: {musica["album"]} - Banda: {musica["banda"]}')

    print("=" * 50)

    sair = True

    return sair

if __name__ == "__main__":
    sair = False

    while sair is False:
        opcao = int(input(exibir_menu()))

        if opcao == 1:
            nome = input("Insira o nome da banda: ")
            bandas.append(cadastrar_banda(nome))

        elif opcao == 2:
            album = input("Insira o nome do album: ")
            banda = input("Insira o nome da banda: ")
            albuns.append(cadastrar_album(album, banda))

        elif opcao == 3:
            musica = input("Insira o nome da musica: ")
            banda = input("Insira o nome da banda: ")
            album = input("Insira o nome do album: ")
            musicas.append(cadastrar_musica(musica, banda, album))

        elif opcao == 4:
            sair = exibir_cadastros()

        else:
            print("Insira uma opcao valida")
