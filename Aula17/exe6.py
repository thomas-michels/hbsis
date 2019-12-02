def cadastrar_cliente(cod_cliente, nome, cpf, data_nascimento, estado, cep, bairro, rua, numero_casa, complemento):
    cliente = {"cod_cliente": cod_cliente, "nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "estado": estado, "cep": cep, "bairro": bairro, "rua": rua, "numero_casa": numero_casa, "complemento": complemento}
    salvar(cliente)

def salvar(cliente):
    arquivo = open("clientes.csv", "a")
    resultado = ""
    for chave in cliente:
        resultado += chave + ";"
    arquivo.write(resultado)

    arquivo.close()


if __name__ == "__main__":
    perguntas = ["Codigo Cliente: ", "Nome: ", "CPF: ", "Data de Nascimento: ", "Estado: ", "CEP: ", "Bairro: ", "Rua: ", "Numero da casa: ", "Complemento: "]
    respostas = []

    for pergunta in perguntas:
        resposta = input(pergunta)
        respostas.append(resposta)

    cadastrar_cliente(respostas[0], respostas[1], respostas[2], respostas[3], respostas[4], respostas[5], respostas[6], respostas[7], respostas[8], respostas[9])
