
import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula43')
from Model.cerveja_model import CervejaModel
from DAO.base_dao import BaseDAO


class CervejaDAO(BaseDAO):

    def __init__(self):
        super().__init__()

    def list_all(self):
        return super().list_all(CervejaModel)

    def get_id(self, id):
        return super().get_id(CervejaModel, id)

    def insert(self, cerveja:CervejaModel):
        objeto = super().insert(cerveja)
        return objeto.as_dict()

    def update(self, cerveja:CervejaModel):
        query = self.party.query(CervejaModel).filter(CervejaModel.id == cerveja.id)
        query.update({CervejaModel.marca: cerveja.marca,
                      CervejaModel.abv: cerveja.abv,
                      CervejaModel.ibu: cerveja.ibu,
                      CervejaModel.ebc: cerveja.ebc}, synchronize_session = False)
        self.party.commit()
        return cerveja.as_dict()

    def remove(self, id):
        return super().remove(CervejaModel, id)
