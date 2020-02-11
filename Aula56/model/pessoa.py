import sqlalchemy as db
from hbsis.Aula56.model.base import Base

class Pessoa(Base):
    __tablename__ = 'LIVRARIA_PESSOA'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100))
    sobrenome = db.Column(db.String(length=100))
    data_nascimento = db.Column(db.DATE)
    naturalidade = db.Column(db.String(length=100))

    def as_dict(self):
        dicionario = {
            'id': self.id,
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'data_nascimento': str(self.data_nascimento),
            'naturalidade': self.naturalidade
        }
        return dicionario
