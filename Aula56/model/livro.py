import sqlalchemy as db
from sqlalchemy.orm import relationship

from hbsis.Aula56.model.base import Base
from hbsis.Aula56.model.autor import Autor
from hbsis.Aula56.model.editora import Editora
from hbsis.Aula56.model.genero import Genero

class Livro(Base):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(length=100))
    sinopse = db.Column(db.String(length=100))
    data_primeira_publicacao = db.Column(db.DATE)
    autor_id = db.Column(db.Integer, db.ForeignKey('LIVRARIA_AUTOR.ID'))
    autor = relationship(Autor)
    editora_id = db.Column(db.Integer, db.ForeignKey('LIVRARIA_EDITORA.ID'))
    editora = relationship(Editora)
    genero_id = db.Column(db.Integer, db.ForeignKey('LIVRARIA_GENERO.ID'))
    genero = relationship(Genero)

    def as_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'data_primeira_publicacao': str(self.data_primeira_publicacao),
            'autor_id': self.autor_id,
            'autor': self.autor.as_dict(),
            'editora_id': self.editora_id,
            'editora': self.editora.as_dict(),
            'genero_id': self.genero_id,
            'genero': self.genero.as_dict()
        }