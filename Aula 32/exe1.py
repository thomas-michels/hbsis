from flask_mysqldb import MySQLdb

class Pessoa():

    def __init__(self):
        self.conexao = MySQLdb.connect(host = "localhost", database = 'aulabd', user = 'root', passwd = '')
        self.cursor = self.conexao.cursor()

    def comitar(self):
        self.conexao.commit()

    def cadastrar(self, nome, idade, endereco="NULL"):
        self.cursor.execute(f"INSERT INTO Pessoa (nome, idade, endereco) VALUES ('{nome}', {idade}, {endereco})")
        self.comitar()

    def buscar(self, id_pessoa):
        self.cursor.execute(f"SELECT * FROM Pessoa WHERE id = {id_pessoa}")
        pessoa = self.cursor.fetchone()
        print(pessoa)

    def alterar(self, id_pessoa, nome, idade, endereco="NULL"):
        self.cursor.execute(f"UPDATE Pessoa SET nome = '{nome}', idade = '{idade}', endereco = '{endereco}' WHERE Pessoa.id = {id_pessoa}")
        self.comitar()

    def consultarAll(self):
        self.cursor.execute("SELECT * FROM Pessoa")
        pessoas = self.cursor.fetchall()
        for pessoa in pessoas:
            print(pessoa)

    def apagar(self, id_pessoa):
        cursor.execute(f"DELETE FROM Pessoa WHERE id = {id_pessoa}")
        self.comitar()


if __name__ == "__main__":
    pessoa = Pessoa()
    #pessoa.cadastrar("Ana ao contrario", 19)
    #pessoa.buscar(1)
    pessoa.alterar(2, "Ana", 19, 1)