
import sqlalchemy as db
from sqlalchemy.orm import relationship
from hbsis.Aula56.model.pessoa import Pessoa
from hbsis.Aula56.model.base import Base


class Autor(Base):
    __tablename__ = "LIVRARIA_AUTOR"
    id = db.Column(db.Integer, primary_key=True)
    pseudonimo = db.Column(db.String(length=100))
    descricao = db.Column(db.String(length=200))
    pessoa_id = db.Column(db.Integer, db.ForeignKey('LIVRARIA_PESSOA.id'))
    pessoa = relationship(Pessoa)

    def as_dict(self):
        return {
            'id': self.id,
            'pseudonimo': self.pseudonimo,
            'descricao': self.descricao,
            'pessoa_id': self.pessoa_id,
            'pessoa': self.pessoa.as_dict()
        }
