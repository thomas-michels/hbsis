
import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula43')
from Model.cerveja_model import CervejaModel
from DAO.base_dao import BaseDAO


class CervejaDAO(BaseDAO):

    def __init__(self):
        super().__init__()

    def list_all(self):
        cervejas = self.party.query(CervejaModel).all()
        retorno = self.conversor(cervejas)
        return retorno

    def get_id(self, id):
        query = self.party.query(CervejaModel).filter(CervejaModel.id.like(f'%{id}'))
        classe = query.first()
        return classe.as_dict()

    def insert(self, cerveja:CervejaModel):
        self.party.add(cerveja)
        self.party.commit()
        return cerveja.as_dict()

    def update(self, cerveja:CervejaModel):
        query = self.party.query(CervejaModel).filter(CervejaModel.id.like(f'%{cerveja.id}')).one()
        query.update({CervejaModel.marca: cerveja.marca,
                      CervejaModel.abv: cerveja.abv,
                      CervejaModel.ibu: cerveja.ibu,
                      CervejaModel.ebc: cerveja.ebc})
        self.party.commit()

        return query.as_dict()

    def remove(self, id):
        self.cursor.execute(f"DELETE FROM Thomas_Cerveja WHERE id = {id};")
        self.connetion.commit()
        return f"Removendo cerveja com id {id}"
