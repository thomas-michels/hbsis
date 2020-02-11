import sqlalchemy as db

from hbsis.Aula56.model.base import Base

class Editora(Base):
    __tablename__ = 'LIVRARIA_EDITORA'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100))

    def as_dict(self):
        return {
            'id': self.id,
            'nome': self.nome
        }