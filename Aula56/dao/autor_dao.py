from hbsis.Aula56.dao.base_dao import BaseDao
from hbsis.Aula56.model.autor import Autor

class AutorDao(BaseDao):
    def __init__(self):
        super().__init__(Autor)