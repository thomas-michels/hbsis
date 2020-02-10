
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

BaseAlchemy = declarative_base()


class CervejaModel(BaseAlchemy):

    __tablename__ = 'Thomas_Cerveja'
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(length=50))
    abv = db.Column(db.String(length=50))
    ibu = db.Column(db.String(length=50))
    ebc = db.Column(db.String(length=50))

    def __str__(self) -> str:
        return f'{self.id};{self.marca};{self.abv};{self.ibu};{self.ebc}'

    def as_dict(self) -> dict:
        dic = {'id': self.id,
               'marca': self.marca,
               'abv': self.abv,
               'ibu': self.ibu,
               'ebc': self.ebc}
        return dic