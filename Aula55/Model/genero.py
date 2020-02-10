
import sqlalchemy as db
from hbsis.Aula55.Model.base import Base


class Genero(Base):

    __tablename__ = "Thomas_Genero"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100))
    descricao = db.Column(db.String(200))