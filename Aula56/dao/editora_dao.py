from hbsis.Aula56.dao.base_dao import BaseDao
from hbsis.Aula56.model.editora import Editora

class EditoraDao(BaseDao):
    def __init__(self):
        super().__init__(Editora)
