
import sqlalchemy as db
from hbsis.Aula55.Model.pessoa import Pessoa


class Cliente(Pessoa):

    __tablename__ = 'Thomas_Cliente'
    endereco = db.Column(db.String(length=200))
    numero_documento = db.Column(db.String(length=50))
    telefone = db.Column(db.String(length=20))
