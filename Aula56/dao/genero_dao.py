from Aula56.dao.base_dao import BaseDao
from Aula56.model.genero import Genero

class GeneroDao(BaseDao):
    def __init__(self):
        super().__init__(Genero)
