import MySQLdb

conexao = MySQLdb.connect(host='localhost', database='aulabd2', user='root', passwd='')

cursor = conexao.cursor()

lista_pessoas = []

select_sql = "SELECT * FROM Pessoa"
cursor.execute(select_sql)
result = cursor.fetchall()

for pessoa in result:
    dic_pessoa = {'id': pessoa[0], 'nome': pessoa[1], 'sobrenome': pessoa[2], 'idade': pessoa[3], 'endereco_id': pessoa[4]}
    lista_pessoas.append(dic_pessoa)

with open('pessoa.txt', 'a') as arquivo:
    for pessoa in lista_pessoas:
        arquivo.write(f'{pessoa["id"]};{pessoa["nome"]};{pessoa["sobrenome"]};{pessoa["idade"]};{pessoa["endereco_id"]}\n')