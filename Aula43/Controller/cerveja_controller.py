
import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula43')
from DAO.cerveja_dao import CervejaDAO
from flask_restful import request
from Model.cerveja_model import CervejaModel
from Controller.base_controller import BaseController


class CervejaController(BaseController):

    def __init__(self):
        cd = CervejaDAO()
        super().__init__(cd)

    def get_parametros(self):
        cerveja = CervejaModel()
        cerveja.marca = request.json['marca']
        cerveja.abv = request.json['abv']
        cerveja.ibu = request.json['ibu']
        cerveja.ebc = request.json['ebc']
        return cerveja

    def post(self):
        classe = self.get_parametros()
        return self.db.insert(classe)

    def put(self, id):
        classe = self.get_parametros()
        classe.id = id
        result = self.db.update(classe)
        return result
