from hbsis.Aula56.dao.base_dao import BaseDao
from hbsis.Aula56.model.livro import Livro

class LivroDao(BaseDao):
    def __init__(self):
        super().__init__(Livro)
