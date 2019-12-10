def exibir_cabecalho():
    menu = """
######################################################################

#                 I Festival de Cerveja em Ituroró                   #

######################################################################

1 - Cadastrar Cliente
2 - Ver Clientes Cadastrados
3 - Cadastrar Produto
4 - Ver Produtos Cadastrados
5 - Vendas
6 - Relatório de Vendas
7 - Sair

Insira a opcao desejada: """
    return menu

def cadastrar_clientes():
    cod_cliente = int(input("Insira o codigo do cliente: "))
    cpf = input("CPF: : ")
    nome = input("Nome: ")
    data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
    estado = input("Estado: ")
    cidade = input("Cidade: ")
    cep = input("CEP: ")
    bairro = input("Bairro: ")
    rua = input("Rua: ")
    num_casa = int(input("Numero da casa: "))
    complemento = input("Complemento: ")

    cliente = {"cod_cliente": cod_cliente, "cpf": cpf, "nome": nome,
    "data_nascimento": data_nascimento, "estado": estado, "cidade": cidade,
    "cep": cep, "bairro": bairro, "rua": rua, "num_casa": num_casa, "complemento": complemento}

    toString = f'{cliente["cod_cliente"]};{cliente["cpf"]};{cliente["nome"]};{cliente["data_nascimento"]};{cliente["estado"]};{cliente["cidade"]};{cliente["cep"]};{cliente["bairro"]};{cliente["rua"]};{cliente["num_casa"]};{cliente["complemento"]}\n'

    salvar("festivalIturoro.csv", toString, "a")

def salvar(nome_arquivo, toString, tipo_de_abertura):
    arquivo = open(nome_arquivo, tipo_de_abertura)
    arquivo.write(toString)
    arquivo.close()

def exibir_produtos(retornar):
    produtos = []
    arquivo = open("produtos.csv", "r")

    for linha_st in arquivo:
        linha = linha_st.strip().split(";")
        produto = {"codigo_da_bebida": linha[0], "nome_da_bebida": linha[1], "tipo_da_bebida": linha[2],
        "volume_da_bebida": linha[3], "preco_unitario": linha[4]}
        produtos.append(produto)

    if retornar:
        return produtos

    else:
        for produto in produtos:
            imprimir = f'''
Codigo da bebida: {produto["codigo_da_bebida"]}; Nome: {produto["nome_da_bebida"]}; Tipo: {produto["tipo_da_bebida"]};
Volume: {produto["volume_da_bebida"]}; Preço: {produto["preco_unitario"]}\n'''
            print(imprimir)

def cadastrar_produtos():
    codigo_da_bebida = int(input("Codigo da Bebida: "))
    nome_da_bebida = input("Nome da bebida: ")
    tipo_da_bebida = input("Tipo: ")
    volume_da_bebida = int(input("Volume: "))
    preco_unitario = float(input("Preço: "))

    produto = {"codigo_da_bebida": codigo_da_bebida, "nome_da_bebida": nome_da_bebida, "tipo_da_bebida": tipo_da_bebida, "volume_da_bebida": volume_da_bebida, "preco_unitario": preco_unitario}

    toString = f'{produto["codigo_da_bebida"]};{produto["nome_da_bebida"]};{produto["tipo_da_bebida"]};{produto["volume_da_bebida"]};{produto["preco_unitario"]}\n'

    salvar("produtos.csv", toString, "a")

def exibir_clientes(retorno):
    pessoas = []
    arquivo = open("festivalIturoro.csv", "r")

    for linha_st in arquivo:
        linha = linha_st.strip().split(";")
        pessoa = {"cod_cliente": linha[0], "cpf": linha[1], "nome": linha[2],
        "data_nascimento": linha[3], "estado": linha[4], "cidade": linha[5],
        "cep": linha[6], "bairro": linha[7], "rua": linha[8], "num_casa": linha[9], "complemento": linha[10]}
        pessoas.append(pessoa)

    if retorno:
        return pessoas

    else:
        for pessoa in pessoas:
            print(f'''
Codigo Cliente: {pessoa["cod_cliente"]}; CPF: {pessoa["cpf"]}; Nome: {pessoa["nome"]};
Data de Nascimento: {pessoa["data_nascimento"]}; Estado: {pessoa["estado"]}; Cidade: {pessoa["cidade"]};
CEP: {pessoa["cep"]}; Bairro: {pessoa["bairro"]}; Rua: {pessoa["rua"]};
Numero casa: {pessoa["num_casa"]}; Complemento: {pessoa["complemento"]}\n''')

def vender_produto(produtos, clientes):
    codigo_da_venda = int(input("Codigo da Venda: "))
    data_da_venda = input("Data da venda (dd/mm/aaaa): ")
    codigo_do_cliente = int(input("Codigo do Cliente: "))
    codigo_da_cerveja = int(input("Codigo da Cerveja: "))
    quantidade_de_cerveja_comprada = int(input("Quantidade: "))

    cliente = 0
    produto = 0

    for cliente_ in clientes:
        if int(cliente_["cod_cliente"]) == codigo_do_cliente:
            nome_do_cliente = cliente_["nome"]
            endereco = f'{cliente_["estado"]} - {cliente_["cidade"]} - {cliente_["rua"]} - {cliente_["num_casa"]}'
            cliente = cliente_
            salvar_c = True
            break

    if cliente == 0:
        print("Cliente não encontrado")
        salvar_c = False

    for produto_ in produtos:
        cod_produto = int(produto_['codigo_da_bebida'])
        
        if cod_produto == codigo_da_cerveja:
            nome_da_cerveja = produto_["nome_da_bebida"]
            preco = produto_["preco_unitario"]
            produto = produto_
            salvar_p = True
            break

    if produto == 0:
        print("Produto não encontrado")
        salvar_p = False

    if salvar_p is True and salvar_c is True:
        print("Venda Realizada")
        venda = {"codigo_da_venda": codigo_da_venda, "data_da_venda": data_da_venda,
        "codigo_do_cliente": codigo_do_cliente, "nome_do_cliente": nome_do_cliente,
        "endereco": endereco,
        "codigo_da_cerveja": codigo_da_cerveja, "nome_da_cerveja": nome_da_cerveja,
        "preco": preco, "quantidade_de_cerveja_comprada": quantidade_de_cerveja_comprada}

        toString = f'{venda["codigo_da_venda"]};{venda["data_da_venda"]};{venda["codigo_do_cliente"]};{venda["nome_do_cliente"]};{venda["endereco"]};{venda["codigo_da_cerveja"]};{venda["nome_da_cerveja"]};{venda["preco"]};{venda["quantidade_de_cerveja_comprada"]}\n'

        salvar("vendas.csv", toString, "a")

    else:
        print("Venda não Realizada")

def relatorio_vendas(clientes, produtos):
    vendas = []
    arq = open("vendas.csv", "r")

    for linha_st in arq:
        linha = linha_st.strip().split(';')
        argumentos = {"codigo_da_venda": linha[0], "codigo_do_cliente": linha[2],
        "nome_do_cliente": linha[3], "endereco": linha[4], "codigo_da_cerveja": linha[5],
        "nome_da_cerveja": linha[6], "preco": linha[7], "quantidade_de_cerveja_comprada": linha[8]}
        vendas.append(argumentos)
    
    for venda in vendas:
        total = float(venda["preco"]) * int(venda["quantidade_de_cerveja_comprada"])
        retorno = f'''
Codigo da Venda: {venda["codigo_da_venda"]}
Codigo do Cliente: {venda["codigo_do_cliente"]} - Nome do Cliente: {venda["nome_do_cliente"]}
Endereco: {venda["endereco"]}
Codigo da cerveja: {venda["codigo_da_cerveja"]} - Nome da cerveja: {venda["nome_da_cerveja"]}
Preço: {venda["preco"]} - Total do Pedido: {total}\n'''
        print(retorno)