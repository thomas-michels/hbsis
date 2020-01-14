from flask_mysqldb import MySQLdb

class Endereco():

    def __init__(self):
        self.conexao = MySQLdb.connect(host = "localhost", database = 'aulabd', user = 'root', passwd = '')
        self.cursor = self.conexao.cursor()

    def comitar(self):
        self.conexao.commit()

    def cadastrar(self, rua, numero, complemento):
        self.cursor.execute(f"INSERT INTO Endereco (rua, numero, complemento) VALUES ('{rua}', {numero}, '{complemento}')")
        self.comitar()

    def buscar(self, id_endereco):
        self.cursor.execute(f"SELECT * FROM Endereco WHERE id = {id_endereco}")
        pessoa = self.cursor.fetchone()
        print(pessoa)

    def alterar(self, id_endereco, rua, numero, complemento):
        self.cursor.execute(f"UPDATE Endereco SET rua = '{rua}', numero = {numero}, complemento = '{complemento}' WHERE Endereco.id = {id_endereco}")
        self.comitar()

    def consultarAll(self):
        self.cursor.execute("SELECT * FROM Endereco")
        pessoas = self.cursor.fetchall()
        for pessoa in pessoas:
            print(pessoa)

    def apagar(self, id_endereco):
        cursor.execute(f"DELETE FROM Pessoa WHERE id = {id_endereco}")
        self.comitar()

if __name__ == "__main__":
    endereco = Endereco()
    #endereco.cadastrar("Gustavo Zimmermann", 100, "casa")
    endereco.consultarAll()