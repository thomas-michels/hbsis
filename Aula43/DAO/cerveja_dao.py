
import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula43')
from Model.cerveja_model import CervejaModel
from DAO.base_dao import BaseDAO


class CervejaDAO(BaseDAO):

    def __init__(self):
        super().__init__()

    def list_all(self) -> dict:
        return super().list_all(CervejaModel)

    def get_id(self, id) -> dict:
        return super().get_id(CervejaModel, id)

    def insert(self, cerveja:CervejaModel) -> dict:
        return super().insert(cerveja).as_dict()

    def update(self, cerveja:CervejaModel) -> dict:
        return super().update(cerveja).as_dict()

    def remove(self, id) -> str:
        return super().remove(CervejaModel, id)
