from flask_mysqldb import MySQLdb
from contextlib import closing

__dados = {'host': "mysql.topskills.study",
'database': 'topskills01',
'user': 'topskills01',
'passwd': 'ts2019',
'port': 3306}

def cadastrar(nome, idade):
    with closing(MySQLdb.connect(**__dados)) as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO topskills01.ThomasMichels (idade, nome) VALUES ('{idade}', '{nome}')")
        conn.commit()

def consultarAll():
    with closing(MySQLdb.connect(**__dados)) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ThomasMichels")
        print(cursor.fetchall())

for i in range(1):
    nome = input("Insira o nome: ")
    idade = int(input("Insira a idade: "))
    cadastrar(nome, idade)

consultarAll()