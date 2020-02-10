
import sqlalchemy as db
from hbsis.Aula55.Model.base import Base


class Pessoa(Base):

    __tablename__ = "Thomas_Pessoa"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100))
    sobrenome = db.Column(db.String(length=100))
    data_nascimento = db.Column(db.DATE)
    naturalidade = db.Column(db.String(length=100))
