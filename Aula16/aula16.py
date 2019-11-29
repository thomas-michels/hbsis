from musica import cadastrar, ler

if __name__ == "__main__":
    sair = False
    while sair is False:

        print("1 - Cadastrar musica")
        print("2 - Playlist")
        print("3 - Sair")
        opcao = int(input("Insira uma opcao: "))

        print('=' * 50)

        if opcao == 1:
            cadastrar()

        elif opcao == 2:
            playlist = ler()

            for musica in playlist:
                print(f'Musica: {musica["musica"]} - Artista: {musica["artista"]} - Album: {musica["album"]}')

        elif opcao == 3:
            sair = True

        print('=' * 50)