
import sqlalchemy as db
from sqlalchemy.orm import relationship
from hbsis.Aula55.Model.autor import Autor
from hbsis.Aula55.Model.editora import Editora
from hbsis.Aula55.Model.genero import Genero
from hbsis.Aula55.Model.base import Base

class Livro(Base):

    __tablename__ = "Thomas_Livro"
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(length=100))
    sinopse = db.Column(db.String(length=100))
    data_edicao = db.Column(db.DATE)
    id_autor = db.Column(db.Integer, db.ForeignKey('Thomas_Autor.id'))
    autor = relationship(Autor)
    id_editora = db.Column(db.Integer, db.ForeignKey('Thomas_Editora.id'))
    editora = relationship(Editora)
    id_genero = db.Column(db.Integer, db.ForeignKey('Thomas_Genero.id'))
    genero = relationship(Genero)
