import sqlalchemy as db

from hbsis.Aula56.model.base import Base

class Genero(Base):
    __tablename__ = "LIVRARIA_GENERO"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100))
    descricao = db.Column(db.String(length=200))

    def as_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao
        }