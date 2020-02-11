import sqlalchemy as db
from sqlalchemy.orm import relationship

from hbsis.Aula56.model.pessoa import Pessoa

class Cliente:
    __tablename__ = "LIVRARIA_CLIENTE"
    id = db.Column(db.Integer, primary_key=True)
    endereco = db.Column(db.String(length=200))
    numero_documento = db.Column(db.String(length=50))
    telefone = db.Column(db.String(length=20))
    pessoa_id = db.Column(db.Integer, db.ForeignKey('LIVRARIA_PESSOA.ID'))
    pessoa = relationship(Pessoa)

    def as_dict(self):
        return {
            'id': self.id,
            'endereco': self.endereco,
            'numero_documento': self.numero_documento,
            'telefone': self.telefone,
            'pessoa_id': self.pessoa_id,
            'pessoa': self.pessoa.as_dict()
        }