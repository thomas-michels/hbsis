
import sqlalchemy as db
from hbsis.Aula55.Model.base import Base


class Editora(Base):

    __tablename__ = "Thomas_Editora"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100))
