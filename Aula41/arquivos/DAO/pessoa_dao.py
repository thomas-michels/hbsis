
import MySQLdb
import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula41/arquivos')
from Model.pessoa import Pessoa


class PessoaDAO:

    def __init__(self):
        self.connetion = MySQLdb.connect(host='mysql.topskills.dev', database='topskills01', user='topskills01', passwd='ts2019')
        self.cursor = self.connetion.cursor()

    def conversor(self, tuplas):
        lista = []
        try:
            if not tuplas.nome:
                pass
            else:
                return lista

        except AttributeError:
            if type(tuplas[0]) == tuple:
                for person in tuplas:
                    pessoa = Pessoa()
                    pessoa.id = person[0]
                    pessoa.nome = person[1]
                    pessoa.id_endereco = person[2]
                    dic = pessoa.__dict__

                    lista.append(dic)

                return lista

            else:
                pessoa = Pessoa()
                pessoa.id = tuplas[0]
                pessoa.nome = tuplas[1]
                pessoa.id_endereco = tuplas[2]
                lista = pessoa
                return lista.__dict__

    def list_all(self):
        self.cursor.execute(f"SELECT * FROM Thomas_Pessoa;")
        result = self.cursor.fetchall()
        classes = self.conversor(result)
        return classes

    def get_id(self, id):
        self.cursor.execute(f'SELECT * FROM Thomas_Pessoa WHERE id={id}')
        result = self.cursor.fetchone()
        classe = self.conversor(result)
        return classe

    def insert(self, pessoa:Pessoa):
        self.cursor.execute(f'INSERT INTO Thomas_Pessoa (nome, id_endereco) VALUES ("{pessoa.nome}", {pessoa.id_endereco})')
        self.connetion.commit()
        pessoa.id = self.cursor.lastrowid
        return pessoa.__dict__

    def update(self, pessoa:Pessoa):
        self.cursor.execute(f"update Thomas_Pessoa SET nome = '{pessoa.nome}', id_endereco= {pessoa.id_endereco} where id = {pessoa.id};")
        self.connetion.commit()
        return pessoa.__dict__

    def remove(self, id):
        self.cursor.execute(f"DELETE FROM Thomas_Pessoa WHERE id = {id};")
        self.connetion.commit()
        return f"Removendo pessoa com id {id}"
