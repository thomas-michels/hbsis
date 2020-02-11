from hbsis.Aula56.dao.base_dao import BaseDao
from hbsis.Aula56.model.pessoa import Pessoa

class PessoaDao(BaseDao):
    def __init__(self):
        super().__init__(Pessoa)
