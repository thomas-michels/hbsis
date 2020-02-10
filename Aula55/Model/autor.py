
import sqlalchemy as db
from hbsis.Aula55.Model.pessoa import Pessoa


class Autor(Pessoa):

    __tablename__ = 'Thomas_Autor'
    pseudonimo = db.Column(db.String(length=100))
    descricao = db.Column(db.String(length=100))
