from hbsis.Aula56.dao.base_dao import BaseDao
from hbsis.Aula56.model.cliente import Cliente

class ClienteDao(BaseDao):
    def __init__(self):
        super().__init__(Cliente)