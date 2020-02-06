
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from hbsis.Aula43.Model.cerveja_model import CervejaModel

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


cerveja = CervejaModel()
cerveja.id = 3
cerveja.marca = "brahma"
cerveja.abv = 22
cerveja.ibu = 33
cerveja.ebc = 44

cervejas = party.query(CervejaModel).all()
query = party.query(Cerveja).filter(Cerveja.id.like('%4')).order_by(Cerveja.id)
a = query.first()
print(a)

#for i in cervejas:
#    print(i)