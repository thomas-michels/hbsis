
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Basemodel = declarative_base()


class Cerveja(Basemodel):

    __tablename__ = 'Thomas_Cerveja'
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(length=50))
    abv = db.Column(db.String(length=50))
    ibu = db.Column(db.String(length=50))
    ebc = db.Column(db.String(length=50))

    def __str__(self):
        return f'{self.id};{self.marca};{self.abv};{self.ibu};{self.ebc}'


# database+conector://user:passwd@url:porta/database

conexao = db.create_engine('mysql+mysqlconnector://topskills01:ts2019@mysql.topskills.dev:3306/topskills01')
create_party = db.orm.sessionmaker()
create_party.configure(bind=conexao)
party = create_party()

cervejas = party.query(Cerveja).all()
for i in cervejas:
    print(i)