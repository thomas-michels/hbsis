
import MySQLdb
import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula42')
from Model.cerveja import Cerveja


class CervejaDAO:

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
                for beer in tuplas:
                    cerveja = Cerveja()
                    cerveja.id = beer[0]
                    cerveja.marca = beer[1]
                    cerveja.abv = beer[2]
                    cerveja.ibu = beer[3]
                    cerveja.ebc = beer[4]

                    dic = cerveja.__dict__

                    lista.append(dic)

                return lista

            else:
                cerveja = Pessoa()
                cerveja.id = tuplas[0]
                cerveja.marca = tuplas[1]
                cerveja.abv = tuplas[2]
                cerveja.ibu = tuplas[3]
                cerveja.ebc = tuplas[4]
                lista = cerveja
                return lista.__dict__

    def list_all(self):
        self.cursor.execute(f"SELECT * FROM Thomas_Cerveja;")
        result = self.cursor.fetchall()
        classes = self.conversor(result)
        return classes

    def get_id(self, id):
        self.cursor.execute(f'SELECT * FROM Thomas_Cerveja WHERE id={id}')
        result = self.cursor.fetchone()
        classe = self.conversor(result)
        return classe

    def insert(self, cerveja:Cerveja):
        self.cursor.execute(f'INSERT INTO Thomas_Cerveja (marca, abv, ibu, ebc) VALUES ("{cerveja.marca}", {cerveja.abv}, {cerveja.ibu}, {cerveja.ebc})')
        self.connetion.commit()
        cerveja.id = self.cursor.lastrowid
        return cerveja.__dict__

    def update(self, cerveja:Cerveja):
        self.cursor.execute(f"update Thomas_Cerveja SET marca = '{cerveja.marca}', abv = {cerveja.abv}, ibu = {cerveja.ibu}, ebc = {cerveja.ebc} where id = {cerveja.id};")
        self.connetion.commit()
        return cerveja.__dict__

    def remove(self, id):
        self.cursor.execute(f"DELETE FROM Thomas_Cerveja WHERE id = {id};")
        self.connetion.commit()
        return f"Removendo cerveja com id {id}"
